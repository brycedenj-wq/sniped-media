#!/usr/bin/env python3
"""
PROMPT_TEMPLATES_DEEP extraction · 6 unique AI-Edge prompt-template PDFs

Source lane: raw/10_REFERENCE/_intake_2026-05-19/prompt_templates/
Output: 01_KNOWLEDGE_BASE/batches/prompt_templates_deep_extracted/<normalized>.txt (one per unique PDF)
Log: 00_COMMAND_CENTER/batch_logs/PROMPT_TEMPLATES_DEEP_EXTRACTION_LOG.md

Method: pdftotext -layout (Poppler · already on PATH · strong text layer confirmed at plan time).
NO OCR. NO new dependencies.

Dedupe: extract ONLY the 6 unique PDFs. The 2 md5-confirmed duplicate `-2` copies are SKIPPED
(Combining Techniques-2 == -3, Self Criticism (Advanced)-2 == -3).
Promo lines (skool.com / "Join My AI & Automation Community") are stripped as noise.
Sanity floor: each extracted file must yield >= 100 words; otherwise mark OCR-deferred (do NOT OCR).
"""

import re
import subprocess
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "10_REFERENCE" / "_intake_2026-05-19" / "prompt_templates"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "prompt_templates_deep_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "PROMPT_TEMPLATES_DEEP_EXTRACTION_LOG.md"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"
MIN_WORDS = 100

# canonical PDF -> normalized output name (6 UNIQUE only)
FILES = {
    "Prompt Template - In Context-2.pdf": "prompt_template_in_context.txt",
    "Prompt Template - Thought Generation-2.pdf": "prompt_template_thought_generation.txt",
    "Prompt Template - Problem Decomposition.pdf": "prompt_template_problem_decomposition.txt",
    "Prompt Template - Self Criticism (Basic)-3.pdf": "prompt_template_self_criticism_basic.txt",
    "Prompt Template - Self Criticism (Advanced)-3.pdf": "prompt_template_self_criticism_advanced.txt",
    "Prompt Template - Combining Techniques-3.pdf": "prompt_template_combining_techniques.txt",
}
# md5-confirmed duplicates · NOT extracted (recorded for the log)
SKIPPED_DUPES = [
    "Prompt Template - Combining Techniques-2.pdf (md5-identical to -3)",
    "Prompt Template - Self Criticism (Advanced)-2.pdf (md5-identical to -3)",
]

PROMO_RE = re.compile(r"(join my ai|skool\.com|unlock exclusive|👉|⚡)", re.I)


def strip_promo(text: str) -> str:
    out = []
    for line in text.splitlines():
        if PROMO_RE.search(line):
            continue
        out.append(line)
    # collapse 3+ blank lines to 1
    cleaned = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return cleaned.strip() + "\n"


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# PROMPT_TEMPLATES_DEEP extraction log · 2026-05-19\n",
           "Method: pdftotext -layout · no OCR · no new dependencies. 6 unique PDFs extracted; 2 md5-duplicate copies skipped; promo lines stripped.\n"]
    total_words = 0
    ocr_deferred = []
    failed = False

    for fname, outname in FILES.items():
        src = LANE / fname
        out = DEST / outname
        if not src.exists():
            log.append(f"FAIL · source not found: {fname}")
            failed = True
            continue
        if out.exists():
            log.append(f"SKIP · {outname} exists · refusing overwrite")
            total_words += len(out.read_text(encoding="utf-8").split())
            continue
        try:
            r = subprocess.run([PDFTOTEXT, "-layout", str(src), "-"],
                               capture_output=True, text=True, timeout=120)
        except Exception as e:
            log.append(f"FAIL · {fname} exception: {e}")
            failed = True
            continue
        if r.returncode != 0:
            log.append(f"FAIL · {fname} pdftotext rc {r.returncode}: {r.stderr.strip()[:200]}")
            failed = True
            continue
        text = strip_promo(r.stdout)
        words = len(text.split())
        if words < MIN_WORDS:
            ocr_deferred.append(f"{fname} ({words} words)")
            log.append(f"OCR-DEFERRED · {fname} -> only {words} words after strip · NOT writing · NOT OCRing")
            continue
        out.write_text(text, encoding="utf-8")
        total_words += words
        log.append(f"OK · {fname} -> {outname} · {words} words")

    log.append("\n## Skipped duplicates (md5-confirmed · 0 chunks)")
    for d in SKIPPED_DUPES:
        log.append(f"- {d}")

    log.append("\n## Summary")
    log.append(f"- Unique sources in: {len(FILES)}")
    log.append(f"- Extracted OK: {sum(1 for o in FILES.values() if (DEST/o).exists())}")
    log.append(f"- Duplicates skipped: {len(SKIPPED_DUPES)}")
    log.append(f"- OCR-deferred: {len(ocr_deferred)}" + (f" ({', '.join(ocr_deferred)})" if ocr_deferred else ""))
    log.append(f"- Total words: {total_words:,}")

    if failed:
        log.append("\nFAIL · an extraction job failed. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction")
        return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {sum(1 for o in FILES.values() if (DEST/o).exists())}/6 unique · {total_words:,} words · OCR-deferred {len(ocr_deferred)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
