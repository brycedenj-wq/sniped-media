#!/usr/bin/env python3
"""Extract the 7 CONSULTING_SERVICE sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The professional-services / consulting / client-craft register · the FIRST of the
four ADJACENT_TIER_2_CLUSTERS sub-lanes (operator-locked · CONSULTING_SERVICE first).
The leadership_mgmt / systems_thinking / expertise_creativity folders deferred to
their own lanes; the Death by Meeting stub, Dieter Rams, Csikszentmihalyi djvu, and
the McLuhan duplicate excluded.
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/consulting_service_extracted")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/consulting_service/Alan Weiss - Value-Based Fees_ How to Charge - and Get - What You're Worth (Ultimate Consultant (Pfeiffer)) (2008, Pfeiffer) - libgen.li.pdf",
     "value_based_fees_weiss.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/consulting_service/Alan Weiss, Alan Weiss - Million Dollar Consulting_ The Professional's Guide to Growing a Practice (2002, McGraw-Hill) - libgen.li.pdf",
     "million_dollar_consulting_weiss.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/consulting_service/Ethan M. Rasiel - The McKinsey Way_ Using the Techniques of the World's Top Strategic Consultants to Help You and Your Business (1999, McGraw-Hill) [10.1036_0071368833] - libgen.li.pdf",
     "the_mckinsey_way_rasiel.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/consulting_service/Maister, David H. - Managing the professional service firm (1997, Free Press Paperbacks) - libgen.li.pdf",
     "managing_the_professional_service_firm_maister.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/consulting_service/Patrick Lencioni - Getting Naked_ A Business Fable About Shedding The Three Fears That Sabotage Client Loyalty (J-B Lencioni Series) (2010) - libgen.li.pdf",
     "getting_naked_lencioni.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/consulting_service/Patrick Lencioni - The advantage _ why organizational health trumps everything else in business (2012, Jossey-Bass) - libgen.li.pdf",
     "the_advantage_lencioni.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/consulting_service/Peter Block - Flawless consulting_ a guide to getting your expertise used (2000, Jossey-Bass_Pfeiffer) - libgen.li.epub",
     "flawless_consulting_block.txt", "epub"),
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
