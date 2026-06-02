#!/usr/bin/env python3
"""Extract the 8 DEEP_FINANCE_EXPANSION CORE sources to normalized text.

pdftotext (pdf) + ebook-convert (epub/azw3) · calibre + poppler already on PATH.
No OCR. No new dependency. Reads from raw/ only (never modifies it).
Refuses to overwrite an existing extracted file. Uses the RECOVERED Margin of Safety
epub (NOT the old scanned pdf).
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw/03_TIER_2_CANON_BOOKS/investing_finance")
OUTDIR = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/deep_finance_expansion_extracted")

# (raw filename, normalized output, method)
SOURCES = [
    ("[Security Analysis Prior Editions] Benjamin Graham, David Dodd, Warren Buffett - Security Analysis_ Sixth Edition, Foreword by Warren Buffett (2008, McGraw-Hill) [10.1036_0071592539] - libgen.li.pdf",
     "security_analysis_graham_dodd.txt", "pdf"),
    ("Schroeder, Alice - The Snowball_ Warren Buffett and the Business of Life (2008, Bantam) - libgen.li.pdf",
     "the_snowball_schroeder.txt", "pdf"),
    (" Benjamin Graham - The Intelligent Investor_ The Definitive Book on Value Investing. A Book of Practical Counsel (2003, Collins Business) - libgen.li.pdf",
     "the_intelligent_investor_graham.txt", "pdf"),
    ("Howard Marks - Mastering the Market Cycle_ Getting the Odds on Your Side (2018, Houghton Mifflin Harcourt) - libgen.li.epub",
     "mastering_the_market_cycle_marks.txt", "ebook"),
    ("James Dale Davidson_ William Rees-Mogg - The sovereign individual _ how to survive and thrive during the collapse of the welfare state (1997, Simon & Schuster) - libgen.li.pdf",
     "the_sovereign_individual_davidson.txt", "pdf"),
    ("Christopher Leonard - The Lords of Easy Money_ How the Federal Reserve Broke the American Economy (2022) - libgen.li.epub",
     "the_lords_of_easy_money_leonard.txt", "ebook"),
    ("Jason Kelly - The New Tycoons_ Inside the Trillion Dollar Private Equity Industry That Owns Everything (2012, Bloomberg Press) - libgen.li.azw3",
     "the_new_tycoons_kelly.txt", "ebook"),
    ("Seth A. Klarman - Margin of Safety_ Risk-Averse Value Investing Strategies for the Thoughtful Investor (1991, HarperCollins) - libgen.li_RECOVERED.epub",
     "margin_of_safety_klarman.txt", "ebook"),
]


def words(path):
    n = 0
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            n += len(line.split())
    return n


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    done = 0
    for fname, out, method in SOURCES:
        src = os.path.join(RAW, fname)
        dst = os.path.join(OUTDIR, out)
        if not os.path.isfile(src):
            sys.exit(f"FAIL: source missing: {src}")
        if os.path.isfile(dst):
            sys.exit(f"REFUSE: extracted file exists: {dst}")
        if method == "pdf":
            r = subprocess.run(["pdftotext", src, dst], capture_output=True, text=True)
        else:
            r = subprocess.run(["ebook-convert", src, dst], capture_output=True, text=True)
        if r.returncode != 0 or not os.path.isfile(dst):
            sys.stderr.write(r.stdout + "\n" + r.stderr + "\n")
            sys.exit(f"FAIL: extraction failed for {fname}")
        print(f"  {out:42} {words(dst):>8} words")
        done += 1
    print(f"extracted {done} of {len(SOURCES)} · method pdftotext + ebook-convert · no OCR · no new deps")


if __name__ == "__main__":
    main()
