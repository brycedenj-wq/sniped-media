#!/usr/bin/env python3
"""Extract the 3 FASHION_LUXURY_STRATEGY sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The luxury-strategy / commercial register (split lane · operator-locked). The
FASHION_LUXURY_CULTURE 4 books deferred; the Abloh article + already-canonical
sources excluded.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/fashion_luxury_strategy_extracted")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/fashion_luxury/ Jean-Noel Kapferer, Vincent Bastien - The Luxury Strategy_ Break the Rules of Marketing to Build Luxury Brands (2009, Kogan Page) - libgen.li.pdf",
     "the_luxury_strategy_kapferer.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/fashion_luxury/ Dana Thomas - Deluxe_ How Luxury Lost Its Luster (2008, Penguin Books) - libgen.li.epub",
     "deluxe_thomas.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/fashion_luxury/ Agins, Teri - The end of fashion_ how marketing changed the clothing business forever (1999_2000, HarperCollins_Quill) - libgen.li.epub",
     "the_end_of_fashion_agins.txt", "epub"),
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
