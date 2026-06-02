#!/usr/bin/env python3
"""
CLAUDE_OPERATOR_DOCS extraction · loose AI/Claude operator docs (per CLAUDE_OPERATOR_DOCS_PLAN.md §4.1).

INCLUDE (5 · all docx · pandoc -f docx -t plain):
  - Claude_Operating_Manual.docx        (raw/)
  - The_Claude_Stack (1).docx           (raw/)
  - claude cowork genius.docx           (raw/)
  - ai after ramon.docx                 (raw/)  · dedupe: skip the byte-identical "copy"
  - using ai x gumroad x digital products.docx (raw/) · light coverage
DEFER (0 chunks · NOT extracted): astro claude websites 3x faster.docx · MORE CLAUDE 5.docx
EXCLUDE (0 chunks · NOT extracted): ai after ramon copy.docx (dup) · document.pdf (Seth Godin
  "This is Marketing" → BATCH_009) · index.html (AI Ops Dashboard artifact · 0 text · B006 overlap)
No OCR. No new dependencies. In-copyright/operator-authored · extracted text is INTERNAL reference only.
"""

import re
import subprocess
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
DEST = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "claude_operator_docs_extracted"
LOG_PATH = ROOT / "00_COMMAND_CENTER" / "batch_logs" / "CLAUDE_OPERATOR_DOCS_EXTRACTION_LOG.md"
PANDOC = "/opt/homebrew/bin/pandoc"

NL_RE = re.compile(r"\n{3,}")

# (relative path, outname, floor)
INCLUDE = [
    ("raw/Claude_Operating_Manual.docx", "claude_operating_manual.txt", 1500),
    ("raw/The_Claude_Stack (1).docx", "the_claude_stack.txt", 3000),
    ("raw/claude cowork genius.docx", "claude_cowork_genius.txt", 3000),
    ("raw/ai after ramon.docx", "ai_after_ramon.txt", 3000),
    ("raw/using ai x gumroad x digital products.docx", "using_ai_x_gumroad_digital_products.txt", 3000),
]
DEFERRED = [
    "astro claude websites 3x faster.docx (web-page scrape · 853k words boilerplate noise · DEFER)",
    "MORE CLAUDE 5.docx (Anthropic Help Center / release-notes scrape · stale · archived · DEFER)",
]
EXCLUDED = [
    "ai after ramon copy.docx (byte-identical duplicate of ai after ramon.docx · md5 4e9fd4f2... · EXCLUDE)",
    "document.pdf (Seth Godin · This is Marketing 2018 · marketing book · REROUTE to BATCH_009 · EXCLUDE)",
    "index.html (AI Ops Dashboard build artifact · 0 extractable text · overlaps BATCH_006 PRD · EXCLUDE)",
]


def wc(out: Path) -> int:
    return len(out.read_text(encoding="utf-8", errors="ignore").split())


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    log = ["# CLAUDE_OPERATOR_DOCS extraction log · 2026-05-22\n",
           "Loose AI/Claude operator docs · 5 included sources (per CLAUDE_OPERATOR_DOCS_PLAN.md §4.1).\n",
           "Method: pandoc -f docx -t plain · no OCR · no new dependencies.\n",
           "Operator-authored / in-copyright · extracted text is INTERNAL chunk-authoring reference only.\n"]
    results = {}
    failed = False

    log.append("## Included sources (5)\n")
    for relpath, outname, floor in INCLUDE:
        src = ROOT / relpath
        out = DEST / outname
        if not src.exists():
            log.append(f"FAIL · not found: {relpath}"); failed = True; continue
        r = subprocess.run([PANDOC, "-f", "docx", "-t", "plain", str(src), "-o", str(out)],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0 or not out.exists():
            log.append(f"FAIL · pandoc · {relpath} rc {r.returncode}: {r.stderr.strip()[:120]}"); failed = True; continue
        out.write_text(NL_RE.sub("\n\n", out.read_text(encoding="utf-8", errors="ignore")).strip() + "\n", encoding="utf-8")
        results[outname] = wc(out)
        flag = "" if results[outname] >= floor else f"  WARNING below floor {floor}"
        log.append(f"OK · docx · {relpath} -> {outname} · {results[outname]:,} words{flag}")
        if results[outname] < floor:
            failed = True

    log.append("\n## Deferred (NOT extracted · 0 chunks)\n")
    for d in DEFERRED:
        log.append(f"- {d}")
    log.append("\n## Excluded / rerouted (NOT extracted · 0 chunks)\n")
    for e in EXCLUDED:
        log.append(f"- {e}")

    log.append("\n## Summary")
    log.append(f"- Included sources extracted OK: {len(results)} of 5")
    for k, v in results.items():
        log.append(f"  - {k}: {v:,} words")
    log.append(f"- Total words: {sum(results.values()):,}")

    if failed:
        log.append("\nFAIL · a source failed or missed its floor. Halt. Do not chunk.")
        LOG_PATH.write_text("\n".join(log), encoding="utf-8")
        print("FAIL · extraction · see log"); return 1

    log.append("\nDone.")
    LOG_PATH.write_text("\n".join(log), encoding="utf-8")
    print(f"Extraction complete · {len(results)} of 5 sources · {sum(results.values()):,} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
