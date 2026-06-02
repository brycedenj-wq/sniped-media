#!/usr/bin/env python3
"""Extract the POLITICAL_THEORY_DISCOURSES source (1 curated political-theory treatise).

Discourses on Livy (Niccolo Machiavelli, Ninian Hill Thomson tr., Dover) pdf. pdftotext
(on PATH). No OCR. No new dependencies. Does NOT modify the raw/ original (read-only
input). Excludes The Prince / On War / Meditations / Landmark Caesar (already
CLASSICAL_STRATEGY), Herodotus / Thucydides / Arrian / Engels (already CLASSICAL_HISTORY),
Napoleon: A Life (already MODERN_COMMAND_NAPOLEON), Art of War / 48 Laws / 33 Strategies
(already BATCH_002), Book of Five Rings (djvu), and the Bible.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SH = REPO / "raw" / "02_TIER_1_CANON_BOOKS" / "strategy_history"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "political_theory_discourses_extracted"

# (source filename in strategy_history/, normalized output stem, tool)
SOURCES = [
    ("[Dover books on history, political and social science] Niccolo Machiavelli, "
     "Ninian Hill Thomson - Discourses on Livy (2007, Dover Publications) - libgen.li.pdf",
     "discourses_on_livy_machiavelli", "pdftotext"),
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
