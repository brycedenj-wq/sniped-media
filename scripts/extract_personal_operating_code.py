#!/usr/bin/env python3
"""
PERSONAL_OPERATING_CODE extraction · The 88 Laws Of The Masculine Mindset (John Winters · 2025)

Single source: raw/02_TIER_1_CANON_BOOKS/operating_founder/_OceanofPDF.com_The_88_Laws_Of_The_Masculine_Mindset_-_John_Winters.pdf
Output:        01_KNOWLEDGE_BASE/batches/personal_operating_code_extracted/88_laws_winters.txt
Log:           00_COMMAND_CENTER/batch_logs/PERSONAL_OPERATING_CODE_EXTRACTION_LOG.md

Method: pdftotext -layout (Poppler · already on PATH · clean text layer confirmed at plan time)
Sanity check: 500-word minimum · halt if extraction yields less.
No OCR.
"""

import subprocess
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
SRC = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "operating_founder" / "_OceanofPDF.com_The_88_Laws_Of_The_Masculine_Mindset_-_John_Winters.pdf"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "personal_operating_code_extracted"
OUT = DEST / "88_laws_winters.txt"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "PERSONAL_OPERATING_CODE_EXTRACTION_LOG.md"

DEST.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

PDFTOTEXT = "/opt/homebrew/bin/pdftotext"
MIN_WORDS = 500


def main():
    log = ["# PERSONAL_OPERATING_CODE extraction log · 2026-05-19\n"]

    if not SRC.exists():
        log.append(f"FAIL · source not found: {SRC}")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · source missing")
        return 1

    log.append(f"Source: `{SRC.name}`")
    log.append(f"Size: {SRC.stat().st_size:,} bytes")
    log.append(f"Output: `{OUT.name}`\n")

    if OUT.exists():
        log.append("SKIP · output already exists. Refusing to overwrite without explicit operator confirmation.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print(f"SKIP · {OUT.name} already exists")
        return 0

    try:
        result = subprocess.run(
            [PDFTOTEXT, "-layout", str(SRC), str(OUT)],
            capture_output=True, text=True, timeout=180,
        )
        if result.returncode != 0:
            log.append(f"FAIL · pdftotext returncode {result.returncode}")
            log.append(f"stderr: {result.stderr.strip()[:500]}")
            LOG_PATH.write_text("\n".join(log), encoding="utf-8")
            print(f"FAIL · pdftotext returncode {result.returncode}")
            return 1
    except Exception as e:
        log.append(f"FAIL · exception: {e}")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print(f"FAIL · {e}")
        return 1

    text = OUT.read_text(encoding="utf-8", errors="ignore")
    words = len(text.split())
    log.append(f"OK · extracted {words:,} words")

    if words < MIN_WORDS:
        log.append(f"\n## SANITY CHECK FAILED · {words} < {MIN_WORDS} minimum")
        log.append("Halt and surface to operator. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print(f"FAIL · sanity check · only {words} words extracted")
        return 1

    log.append(f"\n## Summary")
    log.append(f"- Total jobs: 1")
    log.append(f"- Extracted OK: 1")
    log.append(f"- Failed: 0")
    log.append(f"- Word count: {words:,}")
    log.append(f"- Output path: `{OUT.relative_to(ROOT)}`")
    log.append(f"\nDone.")

    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {words:,} words")
    print(f"Output: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
