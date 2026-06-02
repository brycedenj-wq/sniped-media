#!/usr/bin/env python3
"""Extract the 5 BRAND_CANON sources into the lane's extracted dir.

Read-only on raw/. No OCR. No new dependencies (pdftotext + ebook-convert on PATH).
The 5 net-new brand-strategy books (decision-neutral lane). SNIPED-authored brand
docs HELD; fashion_luxury a separate future lane; StoryBrand/Alchemy/Status and
Culture already canonical (excluded).
"""
import os
import subprocess
import sys

REPO = os.path.expanduser("~/AI-Brain-Refinery")
RAW = os.path.join(REPO, "raw")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/brand_canon_extracted")

SOURCES = [
    ("The Brand Gap, Revised Edition{Marty Neumeier}(2005, Pearson Education (US)){113262716} libgen.li.pdf",
     "the_brand_gap_neumeier.txt", "pdf"),
    ("Alina Wheeler, Rob Meyerson - Designing Brand Identity_ A Comprehensive Guide to the World of Brands and Branding (2024, Wiley) - libgen.li.pdf",
     "designing_brand_identity_wheeler.txt", "pdf"),
    ("Airey, David - Identity designed_ the definitive guide to visual branding (2019, Rockport Publishers) - libgen.li.epub",
     "identity_designed_airey.txt", "epub"),
    ("Rob Meyerson - Brand Naming_ The Complete Guide to Creating a Name for Your Company, Product, or Service (2021, Business Expert Press) - libgen.li.epub",
     "brand_naming_meyerson.txt", "epub"),
    ("[BK business book] Watkins, Alexandra - Hello, my name is awesome_ how to create brand names that stick (2014, Berrett-Koehler Publishers) - libgen.li.epub",
     "hello_my_name_is_awesome_watkins.txt", "epub"),
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
