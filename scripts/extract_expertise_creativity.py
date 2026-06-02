#!/usr/bin/env python3
"""Extract the 4 EXPERTISE_CREATIVITY sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The deliberate-practice / mastery / creative-craft / visual-perception register · the
FOURTH and FINAL of the four ADJACENT_TIER_2_CLUSTERS sub-lanes (operator-locked ·
CONSULTING_SERVICE + LEADERSHIP_MGMT + SYSTEMS_THINKING complete). The Dieter Rams
image-only monograph (0 extractable text) and the Csikszentmihalyi djvu (unsupported)
are excluded; the other three cluster folders are deferred/canonical.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/expertise_creativity_extracted")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/expertise_creativity/ John Berger - Ways of Seeing (2008, Penguin Books Ltd) - libgen.li.epub",
     "ways_of_seeing_berger.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/expertise_creativity/ Rick Rubin - The Creative Act_ A Way of Being (2023, Penguin Publishing Group) - libgen.li.epub",
     "the_creative_act_rubin.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/expertise_creativity/Anders Ericsson, Robert Pool - Peak_ Secrets from the New Science of Expertise (2016, Eamon Dolan_Houghton Mifflin Harcourt) - libgen.li.epub",
     "peak_ericsson_pool.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/expertise_creativity/Geoff Colvin - Talent Is Overrated_ What Really Separates World-Class Performers from Everybody Else (2008, Portfolio Hardcover) - libgen.li.pdf",
     "talent_is_overrated_colvin.txt", "pdf"),
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
