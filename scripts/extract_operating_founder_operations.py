#!/usr/bin/env python3
"""Extract the OPERATING_FOUNDER_OPERATIONS sources (4 curated systems/process books).

The Goal (Goldratt) pdf + Reengineering the Corporation (Hammer/Champy) pdf + The E-Myth
Revisited (Gerber) mobi + Built to Sell (Warrillow) pdf. pdftotext + ebook-convert (both
on PATH). No OCR. No new dependencies. Does NOT modify the raw/ originals (read-only
input). Excludes the OPERATING_FOUNDER_STARTUP sources (Lean Startup, Hard Thing,
Founder's Dilemmas) and OPERATING_FOUNDER_SCALING sources (Blitzscaling, Amp It Up) which
are already chunked, the broken Traction (0-byte), the misfiled out-of-scope files (88
Laws of the Masculine Mindset, Moonwalk), and the Bible.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SH = REPO / "raw" / "02_TIER_1_CANON_BOOKS" / "operating_founder"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "operating_founder_operations_extracted"

# (source filename in operating_founder/, normalized output stem, tool)
SOURCES = [
    (" Eliyahu, Goldratt - The goal_ a process of ongoing improvement "
     "(2004, North River Press) - libgen.li.pdf",
     "the_goal_goldratt", "pdftotext"),
    (" Michael Hammer_ James Champy - Reengineering the corporation _ a manifesto for "
     "business revolution (2001, HarperBusiness) - libgen.li.pdf",
     "reengineering_hammer_champy", "pdftotext"),
    ("Michael E. Gerber - The E-Myth Revisited_ Why Most Small Businesses Don't Work and "
     "What to Do About It (1995, HarperCollins) - libgen.li.mobi",
     "emyth_revisited_gerber", "ebook-convert"),
    ("John Warrillow - Built to Sell_ Turn Your Business Into One You Can Sell "
     "(2010) - libgen.li.pdf",
     "built_to_sell_warrillow", "pdftotext"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    failures = 0
    for src_name, stem, tool in SOURCES:
        src = SH / src_name
        dst = OUT / f"{stem}.txt"
        if not src.exists():
            print(f"FAIL missing source: {src}")
            failures += 1
            continue
        if dst.exists():
            print(f"REFUSE overwrite (exists): {dst}")
            failures += 1
            continue
        cmd = ["pdftotext", str(src), str(dst)] if tool == "pdftotext" else ["ebook-convert", str(src), str(dst)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0 or not dst.exists():
            print(f"FAIL extract: {src_name}\n{r.stderr[-500:]}")
            failures += 1
            continue
        words = len(dst.read_text(errors="ignore").split())
        total += words
        print(f"OK [{tool}] {src_name}\n   -> {dst.name} ({words:,} words)")
    print(f"\nsources in: {len(SOURCES)} · extracted out: {len(SOURCES) - failures} · "
          f"failures: {failures} · total words: {total:,}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
