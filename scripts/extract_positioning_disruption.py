#!/usr/bin/env python3
"""Extract the 3 net-new POSITIONING_DISRUPTION sources into positioning_disruption_extracted/.
ebook-convert for mobi/azw3, pdftotext for pdf. No OCR. Refuses to overwrite. Read-only on raw/."""
import os, subprocess, sys

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/positioning_disruption_extracted")
RAW = os.path.join(ROOT, "raw")

SOURCES = [
    ("02_TIER_1_CANON_BOOKS/sales_positioning/ Geoffrey A. Moore - Crossing the Chasm, 3rd Edition_ Marketing and Selling Disruptive Products to Mainstream Customers (2014, HarperBusiness) - libgen.li.mobi",
     "crossing_the_chasm_moore.txt", "ebook"),
    ("02_TIER_1_CANON_BOOKS/sales_positioning/Fitzpatrick, Rob - The Mom Test_ How to talk to customers & learn if your business is a good idea when everyone is lying to you (2016) - libgen.li.azw3",
     "mom_test_fitzpatrick.txt", "ebook"),
    ("02_TIER_1_CANON_BOOKS/sales_positioning/The Innovator&_039_s Dilemma_ When New Technologies Cause Great Firms to Fail (Management of Innovatio...{Clayton M. Christensen}(2013, Harvard Business Review Press){113262812} libgen.li.pdf",
     "innovators_dilemma_christensen.txt", "pdf"),
]

os.makedirs(OUT, exist_ok=True)
ok = 0
for rel, name, method in SOURCES:
    src = os.path.join(RAW, rel)
    dst = os.path.join(OUT, name)
    if not os.path.isfile(src):
        print(f"MISSING SOURCE: {src}", file=sys.stderr); sys.exit(1)
    if os.path.exists(dst):
        print(f"REFUSE OVERWRITE: {dst}", file=sys.stderr); sys.exit(1)
    if method == "pdf":
        subprocess.run(["pdftotext", src, dst], check=True)
    else:
        subprocess.run(["ebook-convert", src, dst], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    words = len(open(dst, encoding="utf-8", errors="replace").read().split())
    print(f"OK  {name:36} {words:>8} words")
    ok += 1

print(f"\nSources in: {len(SOURCES)} · extracted out: {ok} · failures: {len(SOURCES)-ok}")
