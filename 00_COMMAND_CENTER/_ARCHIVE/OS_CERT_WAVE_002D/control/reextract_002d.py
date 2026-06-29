#!/usr/bin/env python3
"""
reextract_002d.py - deterministic re-extraction of Wave 002-D book text.

WHY: the resume workers (wave002d-R3..R13.js) read per-part .txt files from
/tmp/wave002d/. That dir is volatile and was wiped on a reboot. This script
rebuilds those exact files from the original source books so the existing
workflow scripts run unchanged. No model, no spend, fully deterministic.

Source of truth: /tmp/002d_map.json (slug -> src path, ext, parts, unit file paths),
produced by the join step. If that file is gone (another reboot), regenerate it
with the join harvested from the R-scripts + BOOK_CANON_CERTIFICATION_LEDGER.csv.

Usage:
  python3 reextract_002d.py R3 R4        # extract only those batches
  python3 reextract_002d.py all          # extract every R3-R13 book
  python3 reextract_002d.py R3 --force    # re-extract even if files exist
"""
import json, os, sys, subprocess, tempfile, shutil

MAP = "/tmp/002d_map.json"

def extract_fulltext(src, ext):
    ext = ext.lower().lstrip(".")
    out = tempfile.NamedTemporaryFile(suffix=".txt", delete=False).name
    if ext == "pdf":
        subprocess.run(["pdftotext", "-enc", "UTF-8", src, out],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:  # epub, mobi, azw3, djvu -> calibre
        subprocess.run(["ebook-convert", src, out],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    txt = open(out, errors="ignore").read()
    os.unlink(out)
    return txt

def split_words(txt, n):
    words = txt.split()
    if n <= 1:
        return [txt]
    per = (len(words) + n - 1) // n
    # split on the raw text by word index, but keep original whitespace by re-slicing tokens
    parts = []
    for i in range(n):
        chunk = words[i*per:(i+1)*per]
        parts.append(" ".join(chunk))
    # drop trailing empties if rounding produced fewer real chunks
    parts = [p for p in parts if p.strip()] or [""]
    # if we produced fewer than n (short book), pad by re-splitting evenly
    while len(parts) < n:
        parts.append("")
    return parts[:n]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    batches = None if (not args or args == ["all"]) else set(args)
    mp = json.load(open(MAP))
    todo = [b for b in mp if (batches is None or b["batch"] in batches)]
    print(f"re-extract: {len(todo)} books  batches={'ALL' if batches is None else sorted(batches)}")
    ok, fail = 0, 0
    for b in todo:
        units = b["units"]
        files = [u["file"] for u in units]
        if not force and all(os.path.exists(f) and os.path.getsize(f) > 100 for f in files):
            print(f"  SKIP (exists) {b['batch']} {b['slug']}")
            ok += 1; continue
        for f in files:
            os.makedirs(os.path.dirname(f), exist_ok=True)
        try:
            txt = extract_fulltext(b["src"], b["ext"])
            wc = len(txt.split())
            parts = split_words(txt, b["parts"])
            for f, p in zip(files, parts):
                open(f, "w").write(p)
            pw = [len(open(f).read().split()) for f in files]
            print(f"  OK   {b['batch']} {b['slug'][:34]:34s} total_words={wc:>7} parts={b['parts']} per_part={pw}")
            ok += 1
        except Exception as e:
            print(f"  FAIL {b['batch']} {b['slug']} :: {type(e).__name__}: {e}")
            fail += 1
    print(f"done: ok={ok} fail={fail}")
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
