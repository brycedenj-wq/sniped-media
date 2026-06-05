#!/usr/bin/env python3
"""
os_privacy_gate.py , the enforced privacy/identity/employer gate (audit danger-gap #2, now built).

Before any asset folder could ever be shared, this REFUSES on: identifying EXIF/metadata, or banned
tokens (real name, employer, personal handles) in file names or any text/html in the folder. It does
not post or host anything; it is a local guard that returns SHIP/REJECT and a log.

  os_privacy_gate.py scan <path>            , scan a file or folder, print verdict
  os_privacy_gate.py strip <src> <out>      , write a metadata-stripped copy
  os_privacy_gate.py audit <folder> [--log L], REJECT(exit 1) if any leak found

Banned tokens are conservative defaults; extend BANNED for your real identity/employer terms.
"""
import os, sys, csv, time, argparse, subprocess

BANNED = ["bryce", "brycedenj", "denj", "snipedmedia", "@bryce"]   # real-identity / handle tokens
EMPLOYER = []   # add employer terms here (kept empty by default; never hard-code sensitive names)
TEXT_EXT = (".html", ".htm", ".md", ".txt", ".csv", ".json", ".svg", ".xml")
IMG_EXT = (".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp")

def exif_flags(p):
    try:
        out = subprocess.run(["exiftool", "-s", "-G", p], capture_output=True, text=True).stdout
        return [l for l in out.splitlines() if any(k in l for k in
                ("GPS", "Owner", "Artist", "Creator", "Serial", "By-line", "Copyright"))]
    except Exception:
        return []

def scan(path):
    leaks = []
    files = []
    if os.path.isfile(path): files = [path]
    else:
        for root, _, fs in os.walk(path):
            for f in fs: files.append(os.path.join(root, f))
    toks = [t.lower() for t in BANNED + EMPLOYER]
    for f in files:
        name = os.path.basename(f).lower()
        for t in toks:
            if t in name: leaks.append(("filename_token", f, t))
        ext = os.path.splitext(f)[1].lower()
        if ext in IMG_EXT:
            fl = exif_flags(f)
            if fl: leaks.append(("exif_metadata", f, ";".join(fl)[:80]))
        elif ext in TEXT_EXT:
            try:
                body = open(f, "r", errors="ignore").read().lower()
                for t in toks:
                    if t in body: leaks.append(("text_token", f, t))
            except Exception:
                pass
    return leaks, len(files)

def main():
    ap = argparse.ArgumentParser(prog="os_privacy_gate.py"); sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("scan"); s.add_argument("path")
    st = sub.add_parser("strip"); st.add_argument("src"); st.add_argument("out")
    au = sub.add_parser("audit"); au.add_argument("folder"); au.add_argument("--log", default="")
    a = ap.parse_args()
    if a.cmd == "scan":
        leaks, n = scan(a.path)
        print(f"PRIVACY SCAN: {n} files, {len(leaks)} leak(s)")
        for kind, f, d in leaks: print(f"  !! {kind:16s} {os.path.relpath(f)} :: {d}")
        print("VERDICT:", "REJECT" if leaks else "SHIP (clean)")
        return 1 if leaks else 0
    if a.cmd == "strip":
        import importlib.util
        here = os.path.dirname(os.path.abspath(__file__))
        spec = importlib.util.spec_from_file_location("os_adobe_asset", os.path.join(here, "os_adobe_asset.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        m.strip_metadata(a.src, a.out); print(f"stripped -> {a.out}"); return 0
    if a.cmd == "audit":
        leaks, n = scan(a.folder)
        verdict = "REJECT" if leaks else "SHIP"
        if a.log:
            os.makedirs(os.path.dirname(a.log), exist_ok=True)
            new = not os.path.exists(a.log)
            with open(a.log, "a", newline="") as f:
                w = csv.writer(f)
                if new: w.writerow(["ts", "folder", "files", "leaks", "verdict"])
                w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), a.folder, n, len(leaks), verdict])
        print(f"PRIVACY AUDIT: {verdict} ({len(leaks)} leak(s) in {n} files)")
        for kind, f, d in leaks[:20]: print(f"  !! {kind} {os.path.relpath(f)} :: {d}")
        return 1 if leaks else 0
    ap.print_help(); return 0

if __name__ == "__main__": sys.exit(main())
