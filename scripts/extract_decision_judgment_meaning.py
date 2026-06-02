#!/usr/bin/env python3
"""Extract the 2 DECISION_JUDGMENT_MEANING sources into decision_judgment_meaning_extracted/.
pdftotext for pdf, ebook-convert for epub. No OCR. Refuses to overwrite. Read-only on raw/."""
import os, subprocess, sys

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/decision_judgment_meaning_extracted")
RAW = os.path.join(ROOT, "raw")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Viktor E. Frankl - Man's search for meaning (2000, Beacon Press) - libgen.li.pdf",
     "mans_search_for_meaning_frankl.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Eric Berne - Games People Play_ The Basic Handbook of Transactional Analysis. (1996, Ballantine Books) - libgen.li.epub",
     "games_people_play_berne.txt", "ebook"),
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
