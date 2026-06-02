#!/usr/bin/env python3
"""Extract the single HIGH_LEVEL_CONVOS source (high level convos.docx) to normalized text.

docx -> plain text via pandoc (already on PATH). No OCR. No new dependency.
Reads from raw/ (never modifies it). Refuses to overwrite an existing extracted file.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
SRC = os.path.join(REPO, "raw/07_CONTENT/high_level_convos.docx")
OUTDIR = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/high_level_convos_extracted")
OUT = os.path.join(OUTDIR, "high_level_convos.txt")


def main():
    if not os.path.isfile(SRC):
        sys.exit(f"FAIL: source not found: {SRC}")
    os.makedirs(OUTDIR, exist_ok=True)
    if os.path.isfile(OUT):
        sys.exit(f"REFUSE: extracted file already exists: {OUT}")
    r = subprocess.run(["pandoc", SRC, "-t", "plain", "-o", OUT], capture_output=True, text=True)
    if r.returncode != 0 or not os.path.isfile(OUT):
        sys.stderr.write(r.stdout + "\n" + r.stderr + "\n")
        sys.exit("FAIL: pandoc did not produce output")
    words = chars = lines = 0
    with open(OUT, encoding="utf-8") as fh:
        for line in fh:
            lines += 1
            chars += len(line)
            words += len(line.split())
    print("source in : 1 (high_level_convos.docx)")
    print("extracted : 1 ->", OUT)
    print(f"words={words} chars={chars} lines={lines}")
    print("method=pandoc · no OCR · no new dependency")


if __name__ == "__main__":
    main()
