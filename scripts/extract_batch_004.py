#!/usr/bin/env python3
"""
BATCH_004 extraction · SNIPED OS depth-fill
8 sources: 5 docx (extract) + 3 md (copy).
Output: 01_KNOWLEDGE_BASE/batches/batch_004_extracted/
"""

import shutil
import subprocess
from pathlib import Path

RAW = Path.home() / "AI-Brain-Refinery" / "raw"
DEST = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "batch_004_extracted"
DEST.mkdir(parents=True, exist_ok=True)

PANDOC = "/opt/homebrew/bin/pandoc"
TEXTUTIL = "/usr/bin/textutil"

JOBS = [
    {"src": "chat Sniped MAster thread.docx", "out": "chat_sniped_master_thread.md", "tool": "pandoc-docx"},
    {"src": "Gemini Sniped MAster thread.docx", "out": "gemini_sniped_master_thread.md", "tool": "pandoc-docx"},
    {"src": "Aesthetic_Statement_v1.docx", "out": "aesthetic_statement_v1.md", "tool": "pandoc-docx"},
    {"src": "00_BRIEF/100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md", "out": "100q_audit_optimizations.md", "tool": "copy"},
    {"src": "10_REFERENCE/STRATEGIC_PRINCIPLES.md", "out": "strategic_principles.md", "tool": "copy"},
    {"src": "00_BRIEF/SNIPED_OS_V1_SYNTHESIS_2026-05-12.md", "out": "sniped_os_v1_synthesis.md", "tool": "copy"},
    {"src": "The_Offer_Stack.docx", "out": "offer_stack_full.md", "tool": "pandoc-docx"},
    {"src": "The_Platform_Stack.docx", "out": "platform_stack_full.md", "tool": "pandoc-docx"},
]


def run_pandoc_docx(src, dst):
    cmd = [PANDOC, "-f", "docx", "-t", "markdown", "--wrap=none", "-o", str(dst), str(src)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, r.stderr


def main():
    results = []
    for job in JOBS:
        src = RAW / job["src"]
        dst = DEST / job["out"]
        if not src.exists():
            print(f"  MISSING  {job['src']}")
            results.append((job["out"], "MISSING", 0))
            continue

        if job["tool"] == "pandoc-docx":
            rc, err = run_pandoc_docx(src, dst)
            if rc != 0:
                print(f"  FAILED   {job['out']}: {err[:150]}")
                results.append((job["out"], "FAILED", 0))
                continue
        elif job["tool"] == "copy":
            shutil.copy2(src, dst)
        else:
            print(f"  UNKNOWN tool: {job['tool']}")
            continue

        sz = dst.stat().st_size
        print(f"  OK       {sz:>9,} B  ({job['tool']:11s})  {job['out']}")
        results.append((job["out"], "OK", sz))

    print()
    ok = sum(1 for r in results if r[1] == "OK")
    total = sum(r[2] for r in results)
    print(f"Done: {ok}/{len(JOBS)} ok · {total/1024:.1f} KB extracted")


if __name__ == "__main__":
    main()
