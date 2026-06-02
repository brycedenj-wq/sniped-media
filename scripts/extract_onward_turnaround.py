#!/usr/bin/env python3
"""Extract the single ONWARD_TURNAROUND source (Onward, Howard Schultz) to normalized text.

mobi -> plain text via ebook-convert (calibre, already on PATH). No OCR. No new dependency.
Reads from raw/ (never modifies it). Refuses to overwrite an existing extracted file.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(
    REPO,
    "raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/"
    " Howard Schultz, Joanne Gordon - Onward_ How Starbucks Fought for Its Life"
    " without Losing Its Soul (2011, Rodale Books) - libgen.li.mobi",
)
OUTDIR = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/onward_turnaround_extracted")
OUT = os.path.join(OUTDIR, "onward_schultz.txt")


def main():
    if not os.path.isfile(RAW):
        sys.exit(f"FAIL: source not found: {RAW}")
    os.makedirs(OUTDIR, exist_ok=True)
    if os.path.isfile(OUT):
        sys.exit(f"REFUSE: extracted file already exists: {OUT} (delete it to re-extract)")

    # ebook-convert handles mobi -> txt cleanly; same path used for Titan / Fish / Pour Your Heart.
    cmd = ["ebook-convert", RAW, OUT]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0 or not os.path.isfile(OUT):
        sys.stderr.write(res.stdout + "\n" + res.stderr + "\n")
        sys.exit("FAIL: ebook-convert did not produce output")

    words = chars = lines = 0
    with open(OUT, encoding="utf-8") as fh:
        for line in fh:
            lines += 1
            chars += len(line)
            words += len(line.split())
    print("source in : 1 (Onward, Howard Schultz)")
    print("extracted : 1 ->", OUT)
    print(f"words={words} chars={chars} lines={lines}")
    print("method=ebook-convert (calibre) · no OCR · no new dependency")


if __name__ == "__main__":
    main()
