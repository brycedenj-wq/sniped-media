#!/usr/bin/env python3
"""Extract the 4 FASHION_LUXURY_CULTURE sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The fashion-history / memoir / taste / craft register (split lane · the SECOND of
the two FASHION_LUXURY sub-lanes · FASHION_LUXURY_STRATEGY already canonical). The
3 luxury-strategy books + the Abloh article + already-canonical sources excluded.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/fashion_luxury_culture_extracted")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/fashion_luxury/ Alicia Drake - The Beautiful Fall_ Fashion, Genius, and Glorious Excess in 1970s Paris (2009, Little, Brown and Company) - libgen.li.mobi",
     "the_beautiful_fall_drake.txt", "mobi"),
    ("03_TIER_2_CANON_BOOKS/fashion_luxury/ André Leon Talley - The Chiffon Trenches_ A Memoir (2020, Random House Publishing Group) - libgen.li.epub",
     "the_chiffon_trenches_talley.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/fashion_luxury/ Christian Dior - Dior by Dior- The Autobiography of Christian Dior - libgen.li.pdf",
     "dior_by_dior_dior.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/fashion_luxury/ Christian Dior - The little dictionary of fashion (2007, V & A Publications) - libgen.li.epub",
     "the_little_dictionary_of_fashion_dior.txt", "epub"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    out = []
    for rel, name, method in SOURCES:
        src = os.path.join(RAW, rel)
        dst = os.path.join(OUT, name)
        if not os.path.isfile(src):
            print(f"MISSING SOURCE: {src}")
            sys.exit(1)
        if os.path.exists(dst):
            print(f"REFUSING to overwrite existing: {dst}")
            sys.exit(1)
        if method == "pdf":
            subprocess.run(["pdftotext", src, dst], check=True)
        else:
            subprocess.run(["ebook-convert", src, dst],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        words = len(open(dst, encoding="utf-8", errors="replace").read().split())
        out.append((name, words))
        print(f"  extracted {name}: {words} words")
    print(f"\nSOURCES IN: {len(SOURCES)} · EXTRACTED OUT: {len(out)} · FAILURES: 0")


if __name__ == "__main__":
    main()
