#!/usr/bin/env python3
"""
B2B_POSITIONING_CLAUDE_OPERATOR extraction · Claude for Small Business research (SNIPED OS)

Sources:
  Canonical: raw/08_AI_TECH/claude_for_small_business/claude_for_small_business_organized.docx
  Legacy:    raw/08_AI_TECH/claude_for_small_business/_legacy/claude for small business.docx

Outputs:
  Canonical chunk source: 01_KNOWLEDGE_BASE/batches/b2b_positioning_claude_operator_extracted/claude_for_small_business_organized.txt
  Legacy quote-recovery:  01_KNOWLEDGE_BASE/batches/b2b_positioning_claude_operator_extracted/claude_for_small_business_legacy_quote_recovery.txt

Log: 00_COMMAND_CENTER/batch_logs/B2B_POSITIONING_CLAUDE_OPERATOR_EXTRACTION_LOG.md

Method: pandoc -f docx -t plain (already on PATH · clean text confirmed at plan time).
Per plan: the legacy is extracted only so its verbatim quotes resolve on disk for 2 chunks.
The legacy is NOT a standalone chunk source.
No OCR.
"""

import subprocess
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
LANE = ROOT / "raw" / "08_AI_TECH" / "claude_for_small_business"
SRC_ORG = LANE / "claude_for_small_business_organized.docx"
SRC_LEG = LANE / "_legacy" / "claude for small business.docx"

DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "b2b_positioning_claude_operator_extracted"
OUT_ORG = DEST / "claude_for_small_business_organized.txt"
OUT_LEG = DEST / "claude_for_small_business_legacy_quote_recovery.txt"

LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "B2B_POSITIONING_CLAUDE_OPERATOR_EXTRACTION_LOG.md"

PANDOC = "/opt/homebrew/bin/pandoc"
MIN_WORDS_ORG = 500   # canonical chunk source sanity floor
MIN_WORDS_LEG = 500   # legacy reference sanity floor


def extract(src: Path, out: Path, log: list) -> int:
    if not src.exists():
        log.append(f"FAIL · source not found: `{src}`")
        return -1
    log.append(f"Source: `{src.name}` ({src.stat().st_size:,} bytes) -> `{out.name}`")
    if out.exists():
        log.append(f"SKIP · `{out.name}` already exists. Refusing to overwrite without operator confirmation.")
        text = out.read_text(encoding="utf-8", errors="ignore")
        return len(text.split())
    try:
        result = subprocess.run(
            [PANDOC, "-f", "docx", "-t", "plain", str(src), "-o", str(out)],
            capture_output=True, text=True, timeout=180,
        )
    except Exception as e:
        log.append(f"FAIL · exception: {e}")
        return -1
    if result.returncode != 0:
        log.append(f"FAIL · pandoc returncode {result.returncode}: {result.stderr.strip()[:400]}")
        return -1
    words = len(out.read_text(encoding="utf-8", errors="ignore").split())
    log.append(f"OK · extracted {words:,} words")
    return words


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    log = ["# B2B_POSITIONING_CLAUDE_OPERATOR extraction log · 2026-05-19\n"]
    log.append("## Canonical (chunk source)\n")
    w_org = extract(SRC_ORG, OUT_ORG, log)

    log.append("\n## Legacy (quote-recovery reference only · NOT a standalone chunk source)\n")
    w_leg = extract(SRC_LEG, OUT_LEG, log)

    failed = (w_org < 0) or (w_leg < 0)
    sanity = (w_org < MIN_WORDS_ORG) or (w_leg < MIN_WORDS_LEG)

    log.append("\n## Summary")
    log.append(f"- Sources in: 2 (1 canonical chunk source + 1 legacy quote-recovery reference)")
    log.append(f"- Extracted OK: {2 - (1 if w_org < 0 else 0) - (1 if w_leg < 0 else 0)}")
    log.append(f"- Canonical words: {w_org:,}" if w_org >= 0 else "- Canonical words: FAIL")
    log.append(f"- Legacy words: {w_leg:,}" if w_leg >= 0 else "- Legacy words: FAIL")
    log.append(f"- Canonical output: `{OUT_ORG.relative_to(ROOT)}`")
    log.append(f"- Legacy output: `{OUT_LEG.relative_to(ROOT)}`")

    if failed:
        log.append("\nFAIL · an extraction job failed. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction job failed")
        return 1
    if sanity:
        log.append("\nFAIL · sanity floor not met. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · sanity check")
        return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · canonical {w_org:,} words · legacy {w_leg:,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
