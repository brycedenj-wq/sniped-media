#!/usr/bin/env python3
"""Extract the MODERN_COMMAND_NAPOLEON source (1 curated modern-command biography).

Napoleon: A Life (Andrew Roberts) epub. ebook-convert (on PATH). No OCR. No new
dependencies. Does NOT modify the raw/ original (read-only input). Excludes Discourses
on Livy (deferred to a political-theory lane), Grant / Washington (already
HISTORICAL_BIOGRAPHY), Herodotus / Thucydides / Arrian / Engels (already
CLASSICAL_HISTORY), The Prince / On War / Meditations / Landmark Caesar (already
CLASSICAL_STRATEGY), Art of War / 48 Laws / 33 Strategies (already BATCH_002),
Book of Five Rings (djvu), and the Bible.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SH = REPO / "raw" / "02_TIER_1_CANON_BOOKS" / "strategy_history"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "modern_command_napoleon_extracted"

# (source filename in strategy_history/, normalized output stem, tool)
SOURCES = [
    ("Emperor of the French Napoleon I_ Frankreich Kaiser Napoléon I._ - Napoleon _ a life "
     "(2014, Penguin Group_Viking) - libgen.li.epub",
     "napoleon_a_life_roberts", "ebook-convert"),
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
