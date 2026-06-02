#!/usr/bin/env python3
"""Extract the 2 recovered MEDIA_BUSINESS_RECOVERY sources to normalized text.

ebook-convert (azw3/epub) · calibre already on PATH. No OCR. No new dependency.
Reads from raw/ only (never modifies it). Uses the `_RECOVERED` files only (NOT the old
scanned Hit Men pdf, NOT the old Mailroom djvu). Refuses to overwrite an existing extracted file.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw/03_TIER_2_CANON_BOOKS/memoirs_biographies")
OUTDIR = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/media_business_recovery_extracted")

SOURCES = [
    ("[Vintage] Dannen, Fredric - Hit Men_ Power Brokers and Fast Money Inside the Music Business (2011, Knopf Doubleday Publishing Group_Vintage eBooks) - libgen.li_RECOVERED.azw3",
     "hit_men_dannen.txt"),
    ("Rensin, David - The Mailroom_ Hollywood History from the Bottom Up (2007, Random House Publishing Group) - libgen.li_RECOVERED.epub",
     "the_mailroom_rensin.txt"),
]


def words(path):
    n = 0
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            n += len(line.split())
    return n


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    done = 0
    for fname, out in SOURCES:
        src = os.path.join(RAW, fname)
        dst = os.path.join(OUTDIR, out)
        if not os.path.isfile(src):
            sys.exit(f"FAIL: source missing: {src}")
        if os.path.isfile(dst):
            sys.exit(f"REFUSE: extracted file exists: {dst}")
        r = subprocess.run(["ebook-convert", src, dst], capture_output=True, text=True)
        if r.returncode != 0 or not os.path.isfile(dst):
            sys.stderr.write(r.stdout + "\n" + r.stderr + "\n")
            sys.exit(f"FAIL: extraction failed for {fname}")
        print(f"  {out:28} {words(dst):>7} words")
        done += 1
    print(f"extracted {done} of {len(SOURCES)} · ebook-convert · no OCR · no new deps")


if __name__ == "__main__":
    main()
