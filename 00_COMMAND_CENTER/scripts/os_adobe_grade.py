#!/usr/bin/env python3
"""
os_adobe_grade.py , apply the locked SNIPED look as a repeatable grade pass (not manual Lightroom).

Deterministic RGB encoding of SNIPED_LOCKED_LOOK_v3_LUXURY (Adobe Neutral base). Same input +
same spec always yields the same output (grain is seeded). Never mutates the source; logs the
before/after sha1 + a param hash to EDIT_LOG.csv.

  os_adobe_grade.py apply --src IMG --out IMG [--spec grade.json] [--log LOG]
  os_adobe_grade.py show  [--spec grade.json]

The global look only. The LOT 00 red-only color-law is a composite op (os_adobe_composite.py).
"""
import os, sys, json, argparse, importlib.util, hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
DEFAULT_SPEC = os.path.join(CC, "postproduction", "specs", "SNIPED_LUXURY_GRADE.json")

def _asset():
    spec = importlib.util.spec_from_file_location("os_adobe_asset", os.path.join(HERE, "os_adobe_asset.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

# hue band centers in degrees (Lightroom HSL channels)
BANDS = {"red": 0, "orange": 30, "yellow": 60, "green": 120, "aqua": 180, "blue": 240, "purple": 270, "magenta": 300}

def _band_weight(hue_deg, center, width=40.0):
    """gaussian weight of a pixel hue toward a band center, on a circular hue axis."""
    d = np.abs(((hue_deg - center + 180) % 360) - 180)
    return np.exp(-(d * d) / (2 * width * width))

def _rgb_to_hsv(arr):
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    mx = arr.max(-1); mn = arr.min(-1); df = mx - mn + 1e-8
    h = np.zeros_like(mx)
    mask = df > 1e-6
    rc = (mx - r) / df; gc = (mx - g) / df; bc = (mx - b) / df
    h = np.where(mx == r, bc - gc, h)
    h = np.where(mx == g, 2.0 + rc - bc, h)
    h = np.where(mx == b, 4.0 + gc - rc, h)
    h = (h / 6.0) % 1.0
    s = np.where(mx > 1e-6, df / (mx + 1e-8), 0.0)
    v = mx
    return h * 360.0, s, v

def _hsv_to_rgb(h, s, v):
    h = (h % 360.0) / 60.0
    i = np.floor(h).astype(int); f = h - i
    p = v * (1 - s); q = v * (1 - s * f); t = v * (1 - s * (1 - f))
    i = i % 6
    r = np.select([i==0,i==1,i==2,i==3,i==4,i==5],[v,q,p,p,t,v])
    g = np.select([i==0,i==1,i==2,i==3,i==4,i==5],[t,v,v,q,p,p])
    b = np.select([i==0,i==1,i==2,i==3,i==4,i==5],[p,p,t,v,v,q])
    return np.stack([r, g, b], -1)

def grade_array(rgb01, spec):
    """rgb01: HxWx3 float in [0,1]. returns graded float [0,1]."""
    h, s, v = _rgb_to_hsv(rgb01)

    # 1) per-hue saturation + luminance (HSL panel)
    for band, center in BANDS.items():
        wsat = spec["hsl_saturation"].get(band, 0) / 100.0
        wlum = spec["hsl_luminance"].get(band, 0) / 100.0
        if wsat or wlum:
            wmask = _band_weight(h, center)
            s = s * (1.0 + wsat * wmask)
            v = v * (1.0 + wlum * 0.5 * wmask)

    # 2) global saturation / vibrance
    s = s * (1.0 + spec["global"]["saturation"] / 100.0)
    s = np.clip(s, 0, 1)
    rgb = _hsv_to_rgb(h, s, v)

    # 3) tone: lift creamy blacks + gentle highlight rolloff
    lift = spec["tone"]["lift_blacks"]
    roll = spec["tone"]["highlight_rolloff"]
    shadow_w = (1.0 - rgb) ** 2
    rgb = rgb + lift * shadow_w                      # raise the black floor only in shadows
    hi_w = rgb ** 2
    rgb = rgb - roll * hi_w * (rgb)                  # soften extreme highlights
    rgb = np.clip(rgb, 0, 1)

    # 4) split toning (cool shadows / warm highlights) + midtone color grade
    lum = (0.299*rgb[...,0] + 0.587*rgb[...,1] + 0.114*rgb[...,2])
    def tint(hue_deg, sat, weight):
        if sat <= 0: return np.zeros_like(rgb)
        col = _hsv_to_rgb(np.full_like(lum, hue_deg), np.full_like(lum, sat/100.0), np.ones_like(lum))
        return (col - 0.5) * (weight[..., None])
    sh_w = (1.0 - lum); hi_w2 = lum; mid_w = 1.0 - np.abs(lum - 0.5) * 2.0
    rgb = rgb + tint(spec["split_tone"]["shadow_hue"], spec["split_tone"]["shadow_sat"], sh_w) * 0.30
    rgb = rgb + tint(spec["split_tone"]["highlight_hue"], spec["split_tone"]["highlight_sat"], hi_w2) * 0.30
    rgb = rgb + tint(spec["color_grade"]["midtone_hue"], spec["color_grade"]["midtone_sat"], mid_w) * 0.30
    rgb = np.clip(rgb, 0, 1)

    return rgb

def apply_grade(src, out, spec_path, log_path=None):
    A = _asset(); A.guard_not_inplace(src, out)
    spec = json.load(open(spec_path))
    from PIL import Image, ImageFilter
    im = Image.open(src).convert("RGB")
    arr = np.asarray(im).astype(np.float32) / 255.0
    g = grade_array(arr, spec)

    # 5) clarity/texture (subtle midtone local-contrast reduction, both negative)
    soft_amt = (abs(spec["global"]["clarity"]) + abs(spec["global"]["texture"])) / 200.0  # ~0.04
    g8 = (np.clip(g, 0, 1) * 255).astype(np.uint8)
    gi = Image.fromarray(g8)
    blur = gi.filter(ImageFilter.GaussianBlur(radius=2))
    gi = Image.blend(gi, blur, soft_amt)

    # 6) grain (seeded -> repeatable) on luma
    grain = spec["grain"]["amount"]
    if grain:
        rng = np.random.default_rng(spec["grain"]["seed"])
        ga = np.asarray(gi).astype(np.float32)
        noise = rng.normal(0, grain / 100.0 * 18.0, ga.shape[:2])[..., None]
        ga = np.clip(ga + noise, 0, 255).astype(np.uint8)
        gi = Image.fromarray(ga)

    # 7) capture sharpening (Unsharp)
    amt = spec["global"]["sharpen_amount"]
    if amt:
        gi = gi.filter(ImageFilter.UnsharpMask(radius=spec["global"].get("sharpen_radius", 1.0),
                                               percent=int(amt * 3), threshold=2))
    gi.save(out)
    phash = hashlib.sha1(json.dumps(spec, sort_keys=True).encode()).hexdigest()[:8]
    if log_path:
        A.log_edit(log_path, "grade", src, out, f"spec={spec['name']} phash={phash}",
                   "locked LUXURY look applied (deterministic)")
    return out

def main():
    ap = argparse.ArgumentParser(prog="os_adobe_grade.py")
    sub = ap.add_subparsers(dest="cmd")
    a = sub.add_parser("apply"); a.add_argument("--src", required=True); a.add_argument("--out", required=True)
    a.add_argument("--spec", default=DEFAULT_SPEC); a.add_argument("--log", default="")
    sh = sub.add_parser("show"); sh.add_argument("--spec", default=DEFAULT_SPEC)
    args = ap.parse_args()
    if args.cmd == "apply":
        if not os.path.exists(args.src): print(f"missing src: {args.src}"); return 1
        apply_grade(args.src, args.out, args.spec, args.log or None)
        print(f"graded -> {args.out}"); return 0
    if args.cmd == "show":
        print(json.dumps(json.load(open(args.spec)), indent=2)); return 0
    ap.print_help(); return 0

if __name__ == "__main__":
    sys.exit(main())
