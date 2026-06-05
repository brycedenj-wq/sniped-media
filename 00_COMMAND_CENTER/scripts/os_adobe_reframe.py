#!/usr/bin/env python3
"""
os_adobe_reframe.py , one hero image in, platform export set out.

Subject-aware crop to each spec in SNIPED_EXPORT_SPECS.json (4:5, 1:1, 9:16, banner, thumbnail,
web, print). Crops around a focal point so the subject is never sliced; resizes to the target.
Respects don't_enlarge: a spec that needs upscaling past the source long edge is FLAGGED, not
silently enlarged (it is still written, but recorded as enlarged=true so the gate can catch it).

  os_adobe_reframe.py run --src IMG --outdir DIR [--specs specs.json] [--focus 0.5,0.55] [--log LOG]
  os_adobe_reframe.py specs [--specs specs.json]

--focus is the normalized (x,y) of the subject to keep centered (0,0 top-left .. 1,1 bottom-right).
"""
import os, sys, json, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.dirname(HERE)
DEFAULT_SPECS = os.path.join(CC, "postproduction", "specs", "SNIPED_EXPORT_SPECS.json")

def _asset():
    spec = importlib.util.spec_from_file_location("os_adobe_asset", os.path.join(HERE, "os_adobe_asset.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def _crop_to_aspect(im, tw, th, fx, fy):
    """crop the largest tw:th window from im, centered on focal (fx,fy normalized)."""
    W, H = im.size
    target = tw / th
    if W / H > target:           # source too wide -> limit width
        cw = int(round(H * target)); ch = H
    else:                        # source too tall -> limit height
        cw = W; ch = int(round(W / target))
    cx, cy = fx * W, fy * H
    x0 = int(round(cx - cw / 2)); y0 = int(round(cy - ch / 2))
    x0 = max(0, min(x0, W - cw)); y0 = max(0, min(y0, H - ch))
    return im.crop((x0, y0, x0 + cw, y0 + ch))

def run(src, outdir, specs_path, focus, log_path=None):
    from PIL import Image
    A = _asset()
    cfg = json.load(open(specs_path))
    dont_enlarge = cfg.get("dont_enlarge", True)
    os.makedirs(outdir, exist_ok=True)
    im = Image.open(src).convert("RGB")
    srcW, srcH = im.size; src_long = max(srcW, srcH)
    fx, fy = focus
    results = []
    for s in cfg["specs"]:
        tw, th = s["w"], s["h"]
        cropped = _crop_to_aspect(im, tw, th, fx, fy)
        enlarged = max(tw, th) > src_long
        method = Image.LANCZOS
        outim = cropped.resize((tw, th), method)
        out = os.path.join(outdir, f"lot00_{s['key']}_{tw}x{th}.png")
        outim.save(out)
        if log_path:
            A.log_edit(log_path, "reframe", src, out, f"{s['key']} {tw}x{th} focus={fx},{fy}",
                       ("ENLARGED past source (flagged)" if enlarged else "ok"))
        results.append((s["key"], f"{tw}x{th}", "ENLARGED" if enlarged else "ok", out))
    return results

def main():
    ap = argparse.ArgumentParser(prog="os_adobe_reframe.py")
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run"); r.add_argument("--src", required=True); r.add_argument("--outdir", required=True)
    r.add_argument("--specs", default=DEFAULT_SPECS); r.add_argument("--focus", default="0.5,0.55"); r.add_argument("--log", default="")
    sp = sub.add_parser("specs"); sp.add_argument("--specs", default=DEFAULT_SPECS)
    a = ap.parse_args()
    if a.cmd == "run":
        if not os.path.exists(a.src): print(f"missing src: {a.src}"); return 1
        fx, fy = [float(v) for v in a.focus.split(",")]
        res = run(a.src, a.outdir, a.specs, (fx, fy), a.log or None)
        for k, dim, flag, out in res:
            print(f"  {k:16s} {dim:10s} {flag:9s} -> {os.path.basename(out)}")
        print(f"{len(res)} exports -> {a.outdir}"); return 0
    if a.cmd == "specs":
        print(json.dumps(json.load(open(a.specs)), indent=2)); return 0
    ap.print_help(); return 0

if __name__ == "__main__":
    sys.exit(main())
