#!/usr/bin/env python3
"""Extract the PERSUASION_RECOVERY source (recovered Predictably Irrational epub only).

Single source. ebook-convert (calibre) only. No OCR. No new dependencies.
Does NOT modify the raw/ original (read-only input). Writes one normalized .txt.
Old Predictably Irrational .djvu is excluded. Bible is not touched.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw" / "03_TIER_2_CANON_BOOKS" / "persuasion_psych"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "persuasion_recovery_extracted"

# (source filename in raw/, normalized output stem)
SOURCES = [
    (
        "Dan Ariely - Predictably Irrational, Revised and Expanded Edition_ "
        "The Hidden Forces That Shape Our Decisions (2009, HarperCollins) - "
        "libgen.li_RECOVERED.epub",
        "predictably_irrational_ariely",
    ),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    failures = 0
    for src_name, stem in SOURCES:
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
        # ebook-convert epub -> txt (read-only on the source)
        r = subprocess.run(
            ["ebook-convert", str(src), str(dst)],
            capture_output=True, text=True,
        )
        if r.returncode != 0 or not dst.exists():
            print(f"FAIL extract: {src_name}\n{r.stderr[-500:]}")
            failures += 1
            continue
        words = len(dst.read_text(errors="ignore").split())
        total += words
        print(f"OK {src_name}\n   -> {dst.name} ({words:,} words)")
    print(f"\nsources in: {len(SOURCES)} · extracted out: {len(SOURCES) - failures} · "
          f"failures: {failures} · total words: {total:,}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
