#!/usr/bin/env python3
"""
BATCH_003 extraction · Tier 2 canon books
Source: ~/AI-Brain-Refinery/raw/03_TIER_2_CANON_BOOKS/
Dest:   ~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/batch_003_extracted/

Modeled on extract_batch_002.py. 10 source files: 8 epub via pandoc, 2 pdf via pdftotext.
"""

import subprocess
import sys
from pathlib import Path

SRC = Path.home() / "AI-Brain-Refinery" / "raw" / "03_TIER_2_CANON_BOOKS"
DEST = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "batch_003_extracted"
DEST.mkdir(parents=True, exist_ok=True)

PANDOC = "/opt/homebrew/bin/pandoc"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"

JOBS = [
    {
        "src": "Blair Enns - The Win Without Pitching Manifesto (2010, RockBench Publishing Corp) - libgen.li.epub",
        "out": "wwp_manifesto_enns.md",
        "tool": "pandoc",
    },
    {
        "src": "Blair Enns - Pricing Creativity_ A Guide to Profit Beyond the Billable Hour (2018, RockBench Publishing Corp.) - libgen.li.epub",
        "out": "pricing_creativity_enns.md",
        "tool": "pandoc",
    },
    {
        "src": "Will Guidara - Unreasonable Hospitality_ The Remarkable Power of Giving People More Than They Expect (2022, Optimism Press) - libgen.li.pdf",
        "out": "unreasonable_hospitality_guidara.txt",
        "tool": "pdftotext",
    },
    {
        "src": "Alain De Botton - Status Anxiety (2005, Vintage) - libgen.li.epub",
        "out": "status_anxiety_de_botton.md",
        "tool": "pandoc",
    },
    {
        "src": "Simler, Kevin _ Hanson, Robin - The Elephant in the Brain_ Hidden Motives in Everyday Life (2017, Oxford University Press) - libgen.li.epub",
        "out": "elephant_in_the_brain_simler_hanson.md",
        "tool": "pandoc",
    },
    {
        "src": "[Company of One] Jarvis, Paul - Company of one why staying small is the next big thing for business (2018_2019, Penguin Books Ltd_Penguin Business) - libgen.li.epub",
        "out": "company_of_one_jarvis.md",
        "tool": "pandoc",
    },
    {
        "src": "Holiday, Ryan - Perennial seller_ the art of making and marketing work that lasts (2017, Penguin Publishing Group_Portfolio_Penguin) - libgen.li.epub",
        "out": "perennial_seller_holiday.md",
        "tool": "pandoc",
    },
    {
        "src": "Naval Ravikant, Eric Jorgenson, Jack Butcher, Tim Ferriss - The Almanack of Naval Ravikant_ A Guide to Wealth and Happiness (2020) - libgen.li.pdf",
        "out": "almanack_naval_ravikant.txt",
        "tool": "pdftotext",
    },
    {
        "src": "Elberse, Anita - Blockbusters_ Hit-making, Risk-taking, and the Big Business of Entertainment (2013, Henry Holt and Co.) - libgen.li.epub",
        "out": "blockbusters_elberse.md",
        "tool": "pandoc",
    },
    {
        "src": "Sax, David - The Revenge of Analog_ Real Things and Why They Matter (2016, PublicAffairs) - libgen.li.epub",
        "out": "revenge_of_analog_sax.md",
        "tool": "pandoc",
    },
]


def run_pandoc(src_path: Path, dst_path: Path):
    cmd = [PANDOC, "-f", "epub", "-t", "markdown", "--wrap=none", "-o", str(dst_path), str(src_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stderr


def run_pdftotext(src_path: Path, dst_path: Path):
    cmd = [PDFTOTEXT, "-layout", str(src_path), str(dst_path)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stderr


def main():
    results = []
    for job in JOBS:
        src_path = SRC / job["src"]
        dst_path = DEST / job["out"]

        if not src_path.exists():
            results.append((job["out"], "MISSING-SOURCE", 0, "source file not found"))
            print(f"  MISSING  {job['out']}")
            continue

        if job["tool"] == "pandoc":
            rc, err = run_pandoc(src_path, dst_path)
        elif job["tool"] == "pdftotext":
            rc, err = run_pdftotext(src_path, dst_path)
        else:
            results.append((job["out"], "UNKNOWN-TOOL", 0, f"tool={job['tool']}"))
            continue

        if rc != 0:
            results.append((job["out"], "FAILED", 0, err.strip()[:200]))
            print(f"  FAILED   {job['out']}  rc={rc}  {err.strip()[:200]}")
        else:
            sz = dst_path.stat().st_size if dst_path.exists() else 0
            results.append((job["out"], "OK", sz, job["tool"]))
            print(f"  OK       {sz:>9,} B  ({job['tool']})  {job['out']}")

    print()
    ok = sum(1 for r in results if r[1] == "OK")
    fail = sum(1 for r in results if r[1] != "OK")
    total_bytes = sum(r[2] for r in results)
    print(f"Done: {ok} ok, {fail} failed, {total_bytes/1024/1024:.2f} MB extracted")
    return results


if __name__ == "__main__":
    main()
