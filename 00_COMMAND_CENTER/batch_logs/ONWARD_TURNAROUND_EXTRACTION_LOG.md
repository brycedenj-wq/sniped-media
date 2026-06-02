# ONWARD_TURNAROUND extraction log · 2026-05-23

## Source (1 of 1 · single-source dedicated mini-batch)

| Field | Value |
|---|---|
| Title | Onward: How Starbucks Fought for Its Life without Losing Its Soul |
| Authors | Howard Schultz, Joanne Gordon |
| Publisher / year | Rodale Books, 2011 |
| Raw path | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/ Howard Schultz, Joanne Gordon - Onward_ How Starbucks Fought for Its Life without Losing Its Soul (2011, Rodale Books) - libgen.li.mobi` (note leading space) |
| Format | Mobipocket (mobi · v6 · codepage 65001 UTF-8) |
| Size | 2,278,971 bytes |
| Method | `ebook-convert` (calibre · pre-existing at `/opt/homebrew/bin/ebook-convert`) |
| Output | `01_KNOWLEDGE_BASE/batches/onward_turnaround_extracted/onward_schultz.txt` |
| Yield | 117,893 words · 711,198 chars · 11,115 lines |
| OCR | none |
| New dependencies | none |

## Process

1. `scripts/extract_onward_turnaround.py` converted the mobi to plain text via ebook-convert. Reads from `raw/` only; the original file was not modified (mtime stays 2026-05-17 11:52). The script refuses to overwrite an existing extracted file.
2. The script reported the word/char/line counts above. Full-length book, clean conversion, not a stub or scan.
3. No other source was extracted. Pour Your Heart Into It and all FOUNDER_SECOND_TIER / BIOGRAPHY_FOUNDER_MEDIA / MEDIA_BUSINESS / broken-recovery / Grant / Washington / recovery-acquisition sources were left untouched.

## Chapter structure observed (used to ground chunk authoring)

Five parts: Love (ch 1-7), Confidence (ch 8-16), Pain (ch 17-21), Hope (ch 22-26), Courage (ch 27-33). Key turnaround episodes located and read: the commoditization memo (ch on the leaked memo), the February 2008 closing of 7,100 stores to retrain espresso (ch 1), the founder return as CEO (Introduction), the Transformation Agenda (Pain/Hope chapters), closing ~600 underperforming stores and layoffs, Plan B cost discipline + Lean ($400M permanent cuts), the New Orleans leadership conference, VIA Ready Brew and the rewards program, and the conscience/values thread.

## Deviations

None. Single source as planned. No OCR, no new dependency, no master-file change, no raw modification.
