#!/usr/bin/env python3
"""Extract the 3 recovered ADVERTISING_RECOVERY sources to normalized text.

pdftotext (pdf) + ebook-convert (azw3/epub) · poppler + calibre already on PATH.
No OCR. No new dependency. Reads from raw/ only (never modifies it). Uses the
_RECOVERED files only (NOT the old scanned Confessions pdf, NOT Caples, NOT Hey Whipple).
Refuses to overwrite an existing extracted file.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw/02_TIER_1_CANON_BOOKS/advertising")
OUTDIR = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/advertising_recovery_extracted")

SOURCES = [
    ("Confessions-of-an-Advertising-Man-by-Ogilvy-David-Parker-Alan-z-lib.org__RECOVERED.pdf",
     "confessions_of_an_advertising_man_ogilvy.txt", "pdf"),
    ("The Adweek Copywriting Handbook_ The Ultimate Guide to Writing Powerful Advertising and Marketing...{Sugarman, Joseph}(2024){112008782} libgen.li_RECOVERED.azw3",
     "the_adweek_copywriting_handbook_sugarman.txt", "ebook"),
    ("Gary C Halbert - The Boron Letters (2013) - libgen.li_RECOVERED.epub",
     "the_boron_letters_halbert.txt", "ebook"),
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
    for fname, out, method in SOURCES:
        src = os.path.join(RAW, fname)
        dst = os.path.join(OUTDIR, out)
        if not os.path.isfile(src):
            sys.exit(f"FAIL: source missing: {src}")
        if os.path.isfile(dst):
            sys.exit(f"REFUSE: extracted file exists: {dst}")
        if method == "pdf":
            r = subprocess.run(["pdftotext", src, dst], capture_output=True, text=True)
        else:
            r = subprocess.run(["ebook-convert", src, dst], capture_output=True, text=True)
        if r.returncode != 0 or not os.path.isfile(dst):
            sys.stderr.write(r.stdout + "\n" + r.stderr + "\n")
            sys.exit(f"FAIL: extraction failed for {fname}")
        print(f"  {out:48} {words(dst):>7} words")
        done += 1
    print(f"extracted {done} of {len(SOURCES)} · pdftotext + ebook-convert · no OCR · no new deps")


if __name__ == "__main__":
    main()
