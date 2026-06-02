#!/usr/bin/env python3
"""Extract the OPERATING_FOUNDER_STARTUP sources (3 curated start/survive/founder-reality books).

The Lean Startup (Ries) pdf + The Hard Thing About Hard Things (Horowitz) epub + The
Founder's Dilemmas (Wasserman) epub. pdftotext + ebook-convert (both on PATH). No OCR.
No new dependencies. Does NOT modify the raw/ originals (read-only input). Excludes the
deferred OPERATING_FOUNDER sub-lane sources (Blitzscaling, Amp It Up, The Goal,
Reengineering, E-Myth, Built to Sell), the broken Traction (0-byte), the misfiled
out-of-scope files (88 Laws of the Masculine Mindset, Moonwalk), and the Bible.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SH = REPO / "raw" / "02_TIER_1_CANON_BOOKS" / "operating_founder"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "operating_founder_startup_extracted"

# (source filename in operating_founder/, normalized output stem, tool)
SOURCES = [
    ("Eric Ries - The Lean Startup How Todays Entrepreneurs Use Continuous Innovation To "
     "Create Radically Successful Businesses (2017_2011, Crown Business) - libgen.li.pdf",
     "lean_startup_ries", "pdftotext"),
    ("Ben Horowitz - The Hard Thing About Hard Things_ Building a Business When There Are "
     "No Easy Answers (2014, HarperBusiness) - libgen.li.epub",
     "hard_thing_horowitz", "ebook-convert"),
    ("[Kauffman Foundation Series on Innovation and Entrepreneurship] Noam Wasserman - The "
     "Founder's Dilemmas_ Anticipating and Avoiding the Pitfalls That Can Sink a Startup "
     "(2012, Princeton University Press) - libgen.li.epub",
     "founders_dilemmas_wasserman", "ebook-convert"),
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
