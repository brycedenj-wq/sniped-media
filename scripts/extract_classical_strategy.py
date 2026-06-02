#!/usr/bin/env python3
"""Extract the CLASSICAL_STRATEGY sources (4 curated classical-strategy texts only).

The Prince (Machiavelli) pdf + On War (Clausewitz) pdf + Meditations (Marcus Aurelius)
epub + Landmark Caesar (web essays) pdf. pdftotext + ebook-convert (both on PATH).
No OCR. No new dependencies. Does NOT modify the raw/ originals (read-only input).
Excludes Art of War / 48 Laws / 33 Strategies (already in BATCH_002), Book of Five
Rings (djvu), Discourses, Napoleon, Herodotus, Thucydides, Arrian, Engels, and the
Bible.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SH = REPO / "raw" / "02_TIER_1_CANON_BOOKS" / "strategy_history"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "classical_strategy_extracted"

# (source filename in strategy_history/, normalized output stem, tool)
SOURCES = [
    ("Niccolo Machiavelli - The prince (2008, Hackett Pub. Co) - libgen.li.pdf",
     "the_prince_machiavelli", "pdftotext"),
    ("[Oxford World's Classics] Carl von Clausewitz, Beatrice Heuser - On War "
     "(2007, Oxford University Press, USA) - libgen.li.pdf",
     "on_war_clausewitz", "pdftotext"),
    ("Marcus Aurelius - Meditations - libgen.li.epub",
     "meditations_marcus_aurelius", "ebook-convert"),
    ("LandmarkCaesarWebEssays_5Jan2018.pdf",
     "landmark_caesar", "pdftotext"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    failures = 0
    for src_name, stem, tool in SOURCES:
        src = SH / src_name
        dst = OUT / f"{stem}.txt"
        if not src.exists():
            print(f"FAIL missing source: {src}")
            failures += 1
            continue
        if dst.exists():
            print(f"REFUSE overwrite (exists): {dst}")
            failures += 1
            continue
        cmd = ["pdftotext", str(src), str(dst)] if tool == "pdftotext" else ["ebook-convert", str(src), str(dst)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0 or not dst.exists():
            print(f"FAIL extract: {src_name}\n{r.stderr[-500:]}")
            failures += 1
            continue
        words = len(dst.read_text(errors="ignore").split())
        total += words
        print(f"OK [{tool}] {src_name}\n   -> {dst.name} ({words:,} words)")
    print(f"\nsources in: {len(SOURCES)} · extracted out: {len(SOURCES) - failures} · "
          f"failures: {failures} · total words: {total:,}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
