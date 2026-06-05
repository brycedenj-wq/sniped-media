#!/usr/bin/env python3
"""
os_adobe_composite.py , targeted production fixes (logged, never silent, never in-place).

Deterministic fixes that close the LOT 00 gate misses and general cleanup:
  colorlaw : enforce the world color-law (only auction-red stays saturated; everything else neutral)
  glyph    : restore legibility of a small mark by overlaying crisp serif text (e.g. "LOT 00")
  cleanup  : artifact removal via median filter on a region
  crop     : crop to a box

  os_adobe_composite.py colorlaw --src IMG --out IMG [--keep-deg 5] [--width 30] [--outside 0.12] [--boost 1.15] [--log LOG]
  os_adobe_composite.py glyph    --src IMG --out IMG --x PX --y PX --text "LOT 00" [--size 22] [--color 140,20,15] [--log LOG]
  os_adobe_composite.py cleanup  --src IMG --out IMG --box x0,y0,x1,y1 [--strength 3] [--log LOG]
  os_adobe_composite.py crop     --src IMG --out IMG --box x0,y0,x1,y1 [--log LOG]

For a seamless generative re-stamp / content-aware removal a local op cannot do, the script logs an
Adobe-MCP escalation (os_adobe_asset.adobe_escalation_stub) instead of faking it.
"""
import os, sys, argparse, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

def _mod(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def colorlaw(src, out, keep_deg, width, outside, boost, log_path=None):
    A = _mod("os_adobe_asset"); G = _mod("os_adobe_grade"); A.guard_not_inplace(src, out)
    from PIL import Image
    im = Image.open(src).convert("RGB")
    arr = np.asarray(im).astype(np.float32) / 255.0
    h, s, v = G._rgb_to_hsv(arr)
    keep = G._band_weight(h, keep_deg, width)          # 1 near red, ~0 elsewhere
    s_new = s * (keep * boost + (1.0 - keep) * outside)
    s_new = np.clip(s_new, 0, 1)
    rgb = G._hsv_to_rgb(h, s_new, v)
    Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8)).save(out)
    if log_path:
        A.log_edit(log_path, "colorlaw", src, out,
                   f"keep_deg={keep_deg} width={width} outside={outside} boost={boost}",
                   "color-law: only auction-red retains saturation")
    return out

def _load_serif(size):
    from PIL import ImageFont
    for p in ("/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
              "/System/Library/Fonts/Supplemental/Georgia.ttf",
              "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
              "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
              "/Library/Fonts/Times New Roman.ttf"):
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except Exception: pass
    from PIL import ImageFont
    return ImageFont.load_default()

def glyph(src, out, x, y, text, size, color, log_path=None):
    A = _mod("os_adobe_asset"); A.guard_not_inplace(src, out)
    from PIL import Image, ImageDraw
    im = Image.open(src).convert("RGB"); d = ImageDraw.Draw(im)
    font = _load_serif(size)
    # slight cream backing so stamp reads on a kraft tag without looking pasted-flat
    try:
        bb = d.textbbox((x, y), text, font=font)
        d.rectangle([bb[0]-3, bb[1]-2, bb[2]+3, bb[3]+2], fill=(214, 205, 188))
    except Exception:
        pass
    d.text((x, y), text, fill=tuple(color), font=font)
    im.save(out)
    if log_path:
        A.log_edit(log_path, "glyph", src, out, f"x={x} y={y} text='{text}' size={size}",
                   "legibility fix: serif stamp overlay (deterministic). Adobe generative re-stamp = AMBER escalation")
    return out

def cleanup(src, out, box, strength, log_path=None):
    A = _mod("os_adobe_asset"); A.guard_not_inplace(src, out)
    from PIL import Image, ImageFilter
    im = Image.open(src).convert("RGB")
    x0, y0, x1, y1 = box
    region = im.crop((x0, y0, x1, y1)).filter(ImageFilter.MedianFilter(size=strength if strength % 2 else strength+1))
    im.paste(region, (x0, y0))
    im.save(out)
    if log_path:
        A.log_edit(log_path, "cleanup", src, out, f"box={box} strength={strength}", "artifact removal (median)")
    return out

def crop(src, out, box, log_path=None):
    A = _mod("os_adobe_asset"); A.guard_not_inplace(src, out)
    from PIL import Image
    Image.open(src).convert("RGB").crop(tuple(box)).save(out)
    if log_path:
        A.log_edit(log_path, "crop", src, out, f"box={box}", "crop")
    return out

def _box(s): return [int(v) for v in s.split(",")]
def _color(s): return [int(v) for v in s.split(",")]

def main():
    ap = argparse.ArgumentParser(prog="os_adobe_composite.py")
    sub = ap.add_subparsers(dest="cmd")
    c = sub.add_parser("colorlaw"); c.add_argument("--src", required=True); c.add_argument("--out", required=True)
    c.add_argument("--keep-deg", type=float, default=5); c.add_argument("--width", type=float, default=30)
    c.add_argument("--outside", type=float, default=0.12); c.add_argument("--boost", type=float, default=1.15)
    c.add_argument("--log", default="")
    g = sub.add_parser("glyph"); g.add_argument("--src", required=True); g.add_argument("--out", required=True)
    g.add_argument("--x", type=int, required=True); g.add_argument("--y", type=int, required=True)
    g.add_argument("--text", required=True); g.add_argument("--size", type=int, default=22)
    g.add_argument("--color", default="140,20,15"); g.add_argument("--log", default="")
    cl = sub.add_parser("cleanup"); cl.add_argument("--src", required=True); cl.add_argument("--out", required=True)
    cl.add_argument("--box", required=True); cl.add_argument("--strength", type=int, default=3); cl.add_argument("--log", default="")
    cr = sub.add_parser("crop"); cr.add_argument("--src", required=True); cr.add_argument("--out", required=True)
    cr.add_argument("--box", required=True); cr.add_argument("--log", default="")
    a = ap.parse_args()
    if a.cmd == "colorlaw":
        colorlaw(a.src, a.out, a.keep_deg, a.width, a.outside, a.boost, a.log or None); print(f"colorlaw -> {a.out}"); return 0
    if a.cmd == "glyph":
        glyph(a.src, a.out, a.x, a.y, a.text, a.size, _color(a.color), a.log or None); print(f"glyph -> {a.out}"); return 0
    if a.cmd == "cleanup":
        cleanup(a.src, a.out, _box(a.box), a.strength, a.log or None); print(f"cleanup -> {a.out}"); return 0
    if a.cmd == "crop":
        crop(a.src, a.out, _box(a.box), a.log or None); print(f"crop -> {a.out}"); return 0
    ap.print_help(); return 0

if __name__ == "__main__":
    sys.exit(main())
