#!/usr/bin/env python3
"""
Extract the 3 EDGE_AND_OPERATING_DISCIPLINE worksheets from raw/13_OPERATING_DISCIPLINE/
into 01_KNOWLEDGE_BASE/batches/edge_and_operating_discipline_extracted/.

3 pdf via pdftotext -layout. Keyword-substring matching on filenames. No OCR. No new deps.
Does NOT modify raw/. Refuses to overwrite an existing extracted file.
"""

import subprocess
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
SRC = ROOT / "raw" / "13_OPERATING_DISCIPLINE"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "edge_and_operating_discipline_extracted"
OUT.mkdir(parents=True, exist_ok=True)

# (output_name, keyword to match the raw filename)
TARGETS = [
    ("icp_definition_worksheet.txt", "ICP Definition Worksheet"),
    ("setting_goals.txt", "Setting Goals"),
    ("weekly_reflections.txt", "Weekly Reflections"),
]


def find_raw(keyword):
    matches = [p for p in SRC.iterdir() if p.is_file() and keyword in p.name]
    if len(matches) != 1:
        raise SystemExit(f"ABORT · expected 1 match for '{keyword}', got {len(matches)}: {[m.name for m in matches]}")
    return matches[0]


def extract_pdf(path):
    out = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise SystemExit(f"ABORT · pdftotext failed for {path.name}: {out.stderr[:200]}")
    return out.stdout


def main():
    summary = []
    for out_name, keyword in TARGETS:
        dest = OUT / out_name
        if dest.exists():
            raise SystemExit(f"ABORT · refuse to overwrite existing {dest}")
        src = find_raw(keyword)
        text = extract_pdf(src)
        wc = len(text.split())
        dest.write_text(text, encoding="utf-8")
        summary.append((out_name, src.name, wc))
        print(f"  extracted {wc:>6} words -> {out_name}  (from {src.name})")
    print(f"\nDONE · {len(summary)} worksheets extracted into {OUT}")
    print(f"total words: {sum(s[2] for s in summary)}")


if __name__ == "__main__":
    main()
