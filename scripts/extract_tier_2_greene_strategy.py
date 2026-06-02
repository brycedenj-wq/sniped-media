#!/usr/bin/env python3
"""Extract the 3 TIER_2_GREENE_STRATEGY sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The net-new Greene trio: Laws of Human Nature + Mastery + The 50th Law.
48 Laws / 33 Strategies / Art of War already canonical (BATCH_002 · excluded).
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/tier_2_greene_strategy_extracted")

SOURCES = [
    ("02_TIER_1_CANON_BOOKS/strategy_history/[Laws of Human Nature] Robert Greene - The Laws of Human Nature (2019, VIKING) - libgen.li.pdf",
     "laws_of_human_nature_greene.txt", "pdf"),
    ("02_TIER_1_CANON_BOOKS/strategy_history/Greene, Robert - Mastery (2013_2012, Penguin Group_ Penguin Books_Viking Adult) - libgen.li.epub",
     "mastery_greene.txt", "epub"),
    ("02_TIER_1_CANON_BOOKS/strategy_history/50 Cent, Robert Greene - The 50th Law (2009, Harper) - libgen.li.mobi",
     "the_50th_law_50cent_greene.txt", "ebook"),
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
