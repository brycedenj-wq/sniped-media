#!/usr/bin/env python3
"""Extract the OPERATING_FOUNDER_SCALING sources (2 curated hypergrowth/intensity books).

Blitzscaling (Reid Hoffman, Chris Yeh) epub + Amp It Up (Frank Slootman) pdf.
ebook-convert + pdftotext (both on PATH). No OCR. No new dependencies. Does NOT modify
the raw/ originals (read-only input). Excludes the OPERATING_FOUNDER_STARTUP sources
(Lean Startup, Hard Thing, Founder's Dilemmas · already chunked), the deferred
OPERATING_FOUNDER_OPERATIONS sources (The Goal, Reengineering, E-Myth, Built to Sell),
the broken Traction (0-byte), the misfiled out-of-scope files (88 Laws of the Masculine
Mindset, Moonwalk), and the Bible.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SH = REPO / "raw" / "02_TIER_1_CANON_BOOKS" / "operating_founder"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "operating_founder_scaling_extracted"

# (source filename in operating_founder/, normalized output stem, tool)
SOURCES = [
    ("[Blitzscaling] Reid Hoffman, Chris Yeh, Bill Gates - Blitzscaling_ The Lightning-Fast "
     "Path to Building Massively Valuable Companies (2018, Currency) - libgen.li.epub",
     "blitzscaling_hoffman_yeh", "ebook-convert"),
    ("Amp It Up{Frank Slootman}(2022, Wiley){112881352} libgen.li.pdf",
     "amp_it_up_slootman", "pdftotext"),
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
