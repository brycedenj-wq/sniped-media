#!/usr/bin/env python3
"""Extract the 9 LEADERSHIP_MGMT sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The leading-people / team-culture / management-system register · the SECOND of the
four ADJACENT_TIER_2_CLUSTERS sub-lanes (operator-locked · CONSULTING_SERVICE first,
now LEADERSHIP_MGMT). The Death by Meeting .txt summary stub, the consulting_service
/ systems_thinking / expertise_creativity folders, and the broken/duplicate sources
excluded.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/leadership_mgmt_extracted")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/ Daniel Coyle - The Culture Code_ The Secrets of Highly Successful Groups (2018, Bantam) - libgen.li.epub",
     "the_culture_code_coyle.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/Goodwin, Doris Kearns - Leadership_ In Turbulent Times (2018, Simon & Schuster) - libgen.li.epub",
     "leadership_in_turbulent_times_goodwin.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/Goodwin, Doris Kearns - Team of rivals_ the political genius of Abraham Lincoln (2013, Editora Record) - libgen.li.azw3",
     "team_of_rivals_goodwin.txt", "azw3"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/Jocko Willink, Leif Babin - Extreme Ownership_ How U.S. Navy SEALs Lead and Win (2015, St. Martin's Press) - libgen.li.mobi",
     "extreme_ownership_willink_babin.txt", "mobi"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/Jocko Willink_ Leif Babin - The Dichotomy of Leadership_ Balancing the Challenges of Extreme Ownership to Lead and Win (2018, St. Martin’s Press) - libgen.li.epub",
     "the_dichotomy_of_leadership_willink_babin.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/John Doerr - Measure What Matters_ How Google, Bono, and the Gates Foundation Rock the World with OKRs (2018, Portfolio) - libgen.li.epub",
     "measure_what_matters_doerr.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/Kim Scott - Radical Candor_ Be a Kick-Ass Boss Without Losing Your Humanity (2017, St. Martin’s Press) - libgen.li.epub",
     "radical_candor_scott.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/L. David Marquet - Turn the Ship Around! - A True Story of Turning Followers into Leaders (2013, Portfolio) - libgen.li.epub",
     "turn_the_ship_around_marquet.txt", "epub"),
    ("03_TIER_2_CANON_BOOKS/leadership_mgmt/[Andrew_S._Grove]_High_Output_Management(z-lib.org).pdf",
     "high_output_management_grove.txt", "pdf"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    out = []
    for rel, name, method in SOURCES:
        src = os.path.join(RAW, rel)
        dst = os.path.join(OUT, name)
        if not os.path.isfile(src):
            print(f"MISSING SOURCE: {src}")
            sys.exit(1)
        if os.path.exists(dst):
            print(f"REFUSING to overwrite existing: {dst}")
            sys.exit(1)
        if method == "pdf":
            subprocess.run(["pdftotext", src, dst], check=True)
        else:
            subprocess.run(["ebook-convert", src, dst],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        words = len(open(dst, encoding="utf-8", errors="replace").read().split())
        out.append((name, words))
        print(f"  extracted {name}: {words} words")
    print(f"\nSOURCES IN: {len(SOURCES)} · EXTRACTED OUT: {len(out)} · FAILURES: 0")


if __name__ == "__main__":
    main()
