#!/usr/bin/env python3
"""Extract the 4 SYSTEMS_THINKING sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The systems-literacy / process / media-ecology register · the THIRD of the four
ADJACENT_TIER_2_CLUSTERS sub-lanes (operator-locked · CONSULTING_SERVICE +
LEADERSHIP_MGMT complete). Uses the preferred 1994 McLuhan/Lapham 1 MB copy; the
15 MB 1995 McLuhan duplicate twin, the consulting_service / leadership_mgmt /
expertise_creativity folders, and the broken/stub sources are excluded.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/systems_thinking_extracted")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/systems_thinking/ Atul Gawande - The Checklist Manifesto_ How to Get Things Right (2009, Metropolitan Books) - libgen.li.epub",
     "the_checklist_manifesto_gawande.txt", "epub"),
    # PREFERRED copy: the 1994 Lapham/MIT 1 MB edition (clean text). The 15 MB 1995 twin is EXCLUDED.
    ("03_TIER_2_CANON_BOOKS/systems_thinking/ Marshall McLuhan, Lewis H. Lapham - Understanding Media_ The Extensions of Man (1994, The MIT Press) - libgen.li.pdf",
     "understanding_media_mcluhan.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/systems_thinking/ Meadows, Donella H. Wright, Diana - Thinking in Systems_ A Primer - libgen.li.pdf",
     "thinking_in_systems_meadows.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/systems_thinking/ Peter M. Senge - The Fifth Discipline_ The Art & Practice of The Learning Organization (1994, Doubleday Business) - libgen.li.pdf",
     "the_fifth_discipline_senge.txt", "pdf"),
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
