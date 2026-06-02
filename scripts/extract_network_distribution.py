#!/usr/bin/env python3
"""Extract the 5 NETWORK_DISTRIBUTION sources into network_distribution_extracted/.
pdftotext for pdfs, ebook-convert for epubs. No OCR. Refuses to overwrite. Read-only on raw/."""
import os, subprocess, sys

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/network_distribution_extracted")
RAW = os.path.join(ROOT, "raw")

# (raw relative path, normalized output name, method)
SOURCES = [
    ("02_TIER_1_CANON_BOOKS/network_distribution/Kevin Kelly - The Inevitable_ Understanding the 12 Technological Forces That Will Shape Our Future (2016, Viking) - libgen.li.epub",
     "the_inevitable_kelly.txt", "epub"),
    ("02_TIER_1_CANON_BOOKS/network_distribution/Kevin Kelly - New Rules for the New Economy_ 10 Radical Strategies for a Connected World (1999) - libgen.li.pdf",
     "new_rules_kelly.txt", "pdf"),
    ("02_TIER_1_CANON_BOOKS/network_distribution/Chris Anderson - Long Tail, The, Revised and Updated Edition_ Why the Future of Business is Selling Less of More (2008, Hyperion) - libgen.li.epub",
     "long_tail_anderson.txt", "epub"),
    ("02_TIER_1_CANON_BOOKS/network_distribution/Chris Anderson - Free_ The Future of a Radical Price (Abridged) (2009, Random House Business Books) - libgen.li.pdf",
     "free_anderson.txt", "pdf"),
    ("02_TIER_1_CANON_BOOKS/network_distribution/XcMwr2sETldxuEwaZeEw_The+Great+Online+Game+-+Not+Boring+by+Packy+McCormick.pdf",
     "great_online_game_mccormick.txt", "pdf"),
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
    print(f"OK  {name:34} {words:>8} words")
    ok += 1

print(f"\nSources in: {len(SOURCES)} · extracted out: {ok} · failures: {len(SOURCES)-ok}")
