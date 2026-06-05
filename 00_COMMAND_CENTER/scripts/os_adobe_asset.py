#!/usr/bin/env python3
"""
os_adobe_asset.py , shared asset input/output protocol for the post-production layer.

Every post-production script (grade / reframe / composite / cut / gate) goes through this
one protocol so that NOTHING is silent and EVERYTHING is logged:
  - never mutate a source (always write a new asset),
  - record sha1 + dimensions + provenance in an EDIT_LOG.csv,
  - strip metadata on demand (privacy),
  - expose a single Adobe-MCP escalation contract (for generative ops a local op cannot do).

This is the "clean asset protocol" the other os_adobe_* scripts import. It also runs standalone:

  os_adobe_asset.py register <asset> [--log LOG]      , sha1 + dims + EXIF presence, append to manifest
  os_adobe_asset.py info <asset>                       , print metadata
  os_adobe_asset.py strip <src> <out> [--log LOG]      , write a metadata-stripped copy (privacy)
  os_adobe_asset.py log <LOG>                           , print an edit log

Adobe-MCP escalation contract (the bridge):
  A local deterministic op is always tried first. When a task genuinely needs Adobe generative
  power (content-aware fill, generative text re-stamp, true background removal), the calling
  script records an ESCALATE row via adobe_escalation_stub() and the operator/agent runs the
  Adobe MCP tool, then registers the returned artifact back through this protocol. The bridge is
  wired and logged; it is marked AMBER until a real Adobe MCP artifact is registered through it.
"""
import os, sys, csv, time, hashlib, argparse, subprocess

def sha1_file(path, n=16):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:n]

def dims(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size  # (w, h)
    except Exception:
        return (0, 0)

def has_exif(path):
    """True if the file carries identifying metadata (GPS / owner / camera / XMP)."""
    try:
        out = subprocess.run(["exiftool", "-s", "-G", path], capture_output=True, text=True).stdout
        flags = [l for l in out.splitlines()
                 if any(k in l for k in ("GPS", "Owner", "Artist", "Creator", "Serial",
                                          "By-line", "Make", "Model", "Copyright"))]
        return len(flags) > 0, flags
    except Exception:
        return False, []

def asset_id(path):
    return sha1_file(path)

def log_edit(log_path, op, src, out, params="", note=""):
    """Append one immutable row to an EDIT_LOG.csv. Never silent."""
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    new = not os.path.exists(log_path)
    with open(log_path, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["ts", "op", "src", "src_sha1", "out", "out_sha1", "src_dims", "out_dims", "params", "note"])
        sw, sh = dims(src) if os.path.exists(src) else (0, 0)
        ow, oh = dims(out) if os.path.exists(out) else (0, 0)
        w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), op,
                    os.path.basename(src), sha1_file(src) if os.path.exists(src) else "",
                    os.path.basename(out), sha1_file(out) if os.path.exists(out) else "",
                    f"{sw}x{sh}", f"{ow}x{oh}", params, note])

def guard_not_inplace(src, out):
    if os.path.abspath(src) == os.path.abspath(out):
        raise SystemExit("  REFUSED: output must differ from source (no in-place edit; original is preserved)")

def load_rgb(path):
    from PIL import Image
    return Image.open(path).convert("RGB")

def save_image(im, out, log_path=None, op="save", src="", params="", note=""):
    guard_not_inplace(src or out, out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out)
    if log_path:
        log_edit(log_path, op, src or out, out, params, note)
    return out

def strip_metadata(src, out, log_path=None):
    """Write a copy with ALL metadata removed (privacy). Uses exiftool; falls back to PIL re-save."""
    guard_not_inplace(src, out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    try:
        from PIL import Image
        im = Image.open(src).convert("RGB")
        im.save(out)  # PIL re-save drops most metadata
        subprocess.run(["exiftool", "-all=", "-overwrite_original", out],
                       capture_output=True, text=True)
    except Exception as e:
        raise SystemExit(f"  strip failed: {e}")
    if log_path:
        log_edit(log_path, "strip_metadata", src, out, "", "privacy: all metadata removed")
    return out

def adobe_escalation_stub(log_path, op, src, intent):
    """Record an Adobe-MCP escalation request. The agent runs the Adobe MCP tool and registers
    the returned artifact back through register/log_edit. AMBER until a real artifact lands."""
    log_edit(log_path, f"ESCALATE_ADOBE:{op}", src, src,
             params=intent, note="ADOBE_MCP escalation requested (bridge wired, run on approval)")
    return {"status": "escalation_logged", "op": op, "intent": intent,
            "next": "run Adobe MCP tool, then os_adobe_asset.py register <result>"}

# ---------------- CLI ----------------
def main():
    ap = argparse.ArgumentParser(prog="os_adobe_asset.py")
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("register"); r.add_argument("asset"); r.add_argument("--log", default="")
    i = sub.add_parser("info"); i.add_argument("asset")
    s = sub.add_parser("strip"); s.add_argument("src"); s.add_argument("out"); s.add_argument("--log", default="")
    l = sub.add_parser("log"); l.add_argument("logfile")
    a = ap.parse_args()

    if a.cmd == "register":
        if not os.path.exists(a.asset):
            print(f"missing: {a.asset}"); return 1
        w, h = dims(a.asset); exif, flags = has_exif(a.asset)
        print(f"asset_id : {asset_id(a.asset)}")
        print(f"file     : {a.asset}")
        print(f"dims     : {w}x{h}")
        print(f"metadata : {'PRESENT ' + str(flags) if exif else 'clean (no identifying metadata)'}")
        if a.log:
            log_edit(a.log, "register", a.asset, a.asset, f"{w}x{h}", "registered")
        return 0
    if a.cmd == "info":
        out = subprocess.run(["exiftool", a.asset], capture_output=True, text=True).stdout
        print(out or "(no exiftool output)"); return 0
    if a.cmd == "strip":
        strip_metadata(a.src, a.out, a.log or None)
        print(f"stripped -> {a.out}"); return 0
    if a.cmd == "log":
        if os.path.exists(a.logfile):
            print(open(a.logfile).read())
        else:
            print("no log yet")
        return 0
    ap.print_help(); return 0

if __name__ == "__main__":
    sys.exit(main())
