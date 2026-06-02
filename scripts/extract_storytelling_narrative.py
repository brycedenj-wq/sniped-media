#!/usr/bin/env python3
"""Extract the 4 STORYTELLING_NARRATIVE sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
Option 2 locked: Truby + Campbell + Snyder + Block. McKee (broken/scanned) excluded.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/storytelling_narrative_extracted")

# (relative raw path, normalized output name, method)
SOURCES = [
    ("03_TIER_2_CANON_BOOKS/decision_judgment/ John Truby - The Anatomy of Story_ 22 Steps to Becoming a Master Storyteller (2008, Faber & Faber) - libgen.li.pdf",
     "anatomy_of_story_truby.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/decision_judgment/ Joseph Campbell - The Hero with a Thousand Faces (2020, Joseph Campbell Foundation) - libgen.li.epub",
     "hero_with_a_thousand_faces_campbell.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/decision_judgment/ Blake Snyder - Save The Cat! The Last Book on Screenwriting You'll Ever Need (2005, Michael Wiese Productions) - libgen.li.pdf",
     "save_the_cat_snyder.txt", "pdf"),
    (" Bruce Block - The Visual Story, _ Creating the Visual Structure of Film, TV and Digital Media (2007, Focal Press) - libgen.li.pdf",
     "visual_story_block.txt", "pdf"),
]


def extract_pdf(src, dst):
    subprocess.run(["pdftotext", src, dst], check=True)


def extract_epub(src, dst):
    subprocess.run(["ebook-convert", src, dst],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    os.makedirs(OUT, exist_ok=True)
    results = []
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
            extract_pdf(src, dst)
        else:
            extract_epub(src, dst)
        words = len(open(dst, encoding="utf-8", errors="replace").read().split())
        results.append((name, words))
        print(f"  extracted {name}: {words} words")
    print(f"\nSOURCES IN: {len(SOURCES)} · EXTRACTED OUT: {len(results)} · FAILURES: 0")


if __name__ == "__main__":
    main()
