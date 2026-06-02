#!/usr/bin/env python3
"""Extract the 2 DECISION_JUDGMENT_COGNITION sources into decision_judgment_cognition_extracted/.
ebook-convert for mobi, pdftotext for pdf. No OCR. Refuses to overwrite. Read-only on raw/."""
import os, subprocess, sys

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/decision_judgment_cognition_extracted")
RAW = os.path.join(ROOT, "raw")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Daniel Kahneman - Thinking, Fast and Slow (2011, Farrar, Straus and Giroux) - libgen.li.mobi",
     "thinking_fast_and_slow_kahneman.txt", "ebook"),
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Sunstein, Cass R._ Sibony, Olivier_ Kahneman, Daniel - Noise_ A Flaw in Human Judgment (2021, Little, Brown and Company) - libgen.li.pdf",
     "noise_kahneman_sibony_sunstein.txt", "pdf"),
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
    print(f"OK  {name:40} {words:>8} words")
    ok += 1

print(f"\nSources in: {len(SOURCES)} · extracted out: {ok} · failures: {len(SOURCES)-ok}")
