#!/usr/bin/env python3
"""
os_mark.py , signature mark-injection / retouch stage (logged, never silent).

When a raw generation drops a signature detail (e.g. AXIS's mole) but the HARD
identity structure holds, restore the signature deterministically , WITHOUT
overwriting the original and WITHOUT hiding the edit. Every injection:
  - writes a NEW asset (never mutates the source),
  - records source, output, coordinates, reason in MARK_INJECTION_LOG.csv.
An unlogged or in-place edit is treated as a violation by the tests.

Commands:
  inject --src IMG --out IMG --x PX --y PX [--radius R] [--color #rrggbb] --reason "..." --log LOGCSV
  log    --log LOGCSV                         show the injection log
"""
import os, sys, csv, time, argparse


def cmd_inject(a):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        print("  Pillow not installed: pip install Pillow"); return 1
    if not os.path.isfile(a.src):
        print(f"  source not found: {a.src}"); return 1
    if os.path.abspath(a.src) == os.path.abspath(a.out):
        print("  REFUSED: output must differ from source (no in-place edit; original is preserved)"); return 1
    if not a.reason:
        print("  REFUSED: --reason is mandatory (no silent edits)"); return 1
    im = Image.open(a.src).convert("RGB")
    w, h = im.size
    if not (0 <= a.x < w and 0 <= a.y < h):
        print(f"  REFUSED: ({a.x},{a.y}) outside image {w}x{h}"); return 1
    # parse color
    c = a.color.lstrip("#")
    rgb = tuple(int(c[i:i+2], 16) for i in (0, 2, 4)) if len(c) == 6 else (60, 40, 35)
    draw = ImageDraw.Draw(im)
    r = max(1, a.radius)
    draw.ellipse([a.x - r, a.y - r, a.x + r, a.y + r], fill=rgb)
    im.save(a.out)
    # mandatory log
    new = not os.path.exists(a.log)
    os.makedirs(os.path.dirname(a.log) or ".", exist_ok=True)
    with open(a.log, "a", newline="") as f:
        wr = csv.writer(f)
        if new:
            wr.writerow(["ts", "source", "output", "x", "y", "radius", "color", "reason"])
        wr.writerow([time.strftime("%Y-%m-%d %H:%M"), a.src, a.out, a.x, a.y, r, "#" + c, a.reason])
    print(f"  injected signature mark at ({a.x},{a.y}) r{r} -> {a.out}")
    print(f"  LOGGED to {a.log} (source preserved, edit recorded)")
    return 0


def cmd_log(a):
    if not os.path.isfile(a.log):
        print("  no injection log yet"); return 0
    with open(a.log) as f:
        for row in f:
            print("  " + row.rstrip())
    return 0


def main():
    p = argparse.ArgumentParser(prog="os_mark.py")
    sub = p.add_subparsers(dest="cmd")
    inj = sub.add_parser("inject")
    inj.add_argument("--src", required=True); inj.add_argument("--out", required=True)
    inj.add_argument("--x", type=int, required=True); inj.add_argument("--y", type=int, required=True)
    inj.add_argument("--radius", type=int, default=3); inj.add_argument("--color", default="#3c2823")
    inj.add_argument("--reason", required=True); inj.add_argument("--log", required=True)
    lg = sub.add_parser("log"); lg.add_argument("--log", required=True)
    a = p.parse_args()
    if a.cmd == "inject":
        return cmd_inject(a)
    if a.cmd == "log":
        return cmd_log(a)
    p.print_help(); return 1


if __name__ == "__main__":
    sys.exit(main())
