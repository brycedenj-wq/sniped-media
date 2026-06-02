#!/usr/bin/env python3
"""Extract the HISTORICAL_BIOGRAPHY sources (2 Chernow biographies only).

Grant (Chernow) epub + Washington: A Life (Chernow) pdf. ebook-convert (epub) +
pdftotext (pdf). No OCR. No new dependencies. Does NOT modify the raw/ originals
(read-only input). Titan (Rockefeller) is excluded (already chunked in
FOUNDER_SECOND_TIER). Bible not touched.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw" / "03_TIER_2_CANON_BOOKS" / "memoirs_biographies"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "historical_biography_extracted"

# (source filename in raw/, normalized output stem, tool)
SOURCES = [
    ("Ron Chernow - Grant (2017, Penguin Publishing Group) - libgen.li.epub",
     "grant_chernow", "ebook-convert"),
    ("Ron Chernow - Washington_ A Life - libgen.li.pdf",
     "washington_a_life_chernow", "pdftotext"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    failures = 0
    for src_name, stem, tool in SOURCES:
        src = RAW / src_name
        dst = OUT / f"{stem}.txt"
        if not src.exists():
            print(f"FAIL missing source: {src}")
            failures += 1
            continue
        if dst.exists():
            print(f"REFUSE overwrite (exists): {dst}")
            failures += 1
            continue
        if tool == "pdftotext":
            cmd = ["pdftotext", str(src), str(dst)]
        else:
            cmd = ["ebook-convert", str(src), str(dst)]
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
