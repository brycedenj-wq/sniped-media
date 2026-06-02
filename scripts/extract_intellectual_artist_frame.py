#!/usr/bin/env python3
"""
INTELLECTUAL_ARTIST_FRAME extraction · MJ Moonwalk (1988 · 2009 Crown Archetype reissue)

Single source: raw/02_TIER_1_CANON_BOOKS/operating_founder/ Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub
Output:        01_KNOWLEDGE_BASE/batches/intellectual_artist_frame_extracted/mj_moonwalk.txt
Log:           00_COMMAND_CENTER/batch_logs/INTELLECTUAL_ARTIST_FRAME_EXTRACTION_LOG.md

Method: ebook-convert (Calibre) with --enable-heuristics
Sanity check: 500-word minimum · halt if extraction yields less.
"""

import subprocess
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
SRC = ROOT / "raw" / "02_TIER_1_CANON_BOOKS" / "operating_founder" / " Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "intellectual_artist_frame_extracted"
OUT = DEST / "mj_moonwalk.txt"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "INTELLECTUAL_ARTIST_FRAME_EXTRACTION_LOG.md"

DEST.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"
MIN_WORDS = 500


def main():
    log = ["# INTELLECTUAL_ARTIST_FRAME extraction log · 2026-05-19\n"]

    if not SRC.exists():
        log.append(f"FAIL · source not found: {SRC}")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print(f"FAIL · source missing")
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
            [EBOOK_CONVERT, str(SRC), str(OUT), "--enable-heuristics"],
            capture_output=True, text=True, timeout=180,
        )
        if result.returncode != 0:
            log.append(f"FAIL · ebook-convert returncode {result.returncode}")
            log.append(f"stderr: {result.stderr.strip()[:500]}")
            LOG_PATH.write_text("\n".join(log), encoding="utf-8")
            print(f"FAIL · ebook-convert returncode {result.returncode}")
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
