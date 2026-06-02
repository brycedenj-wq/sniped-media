#!/usr/bin/env python3
"""Extract the FOUNDER_FASHION_RECOVERY sources (2 recovered memoir epubs only).

Grace: A Memoir (Coddington) + Total Recall (Schwarzenegger), the `_RECOVERED.epub`
files only. ebook-convert (calibre) only. No OCR. No new dependencies.
Does NOT modify the raw/ originals (read-only input). Old 0-byte stubs excluded.
Bible not touched.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "raw" / "03_TIER_2_CANON_BOOKS" / "memoirs_biographies"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "founder_fashion_recovery_extracted"

SOURCES = [
    (
        "Grace Coddington - Grace_ A Memoir (2012, Random House) - "
        "libgen.li_RECOVERED.epub",
        "grace_a_memoir_coddington",
    ),
    (
        "Schwarzenegger, Arnold - Total Recall- My Unbelievably True Life Story "
        "(2012, Simon & Schuster) - libgen.li_RECOVERED.epub",
        "total_recall_schwarzenegger",
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
