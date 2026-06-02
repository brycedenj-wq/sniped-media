#!/usr/bin/env python3
"""Extract the 4 DECISION_JUDGMENT_CROWDS sources into decision_judgment_crowds_extracted/.
ebook-convert for azw3/epub, pdftotext for pdf. No OCR. Refuses to overwrite. Read-only on raw/."""
import os, subprocess, sys

ROOT = "/Users/sniper/AI-Brain-Refinery"
OUT = os.path.join(ROOT, "01_KNOWLEDGE_BASE/batches/decision_judgment_crowds_extracted")
RAW = os.path.join(ROOT, "raw")

SOURCES = [
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Jonathan Haidt - The Righteous Mind_ Why Good People Are Divided by Politics and Religion (2012, Pantheon) - libgen.li.azw3",
     "righteous_mind_haidt.txt", "ebook"),
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Greg Lukianoff, Jonathan Haidt - The Coddling of the American Mind_ How Good Intentions and Bad Ideas Are Setting up a Generation for Failure (2018, Penguin Press) - libgen.li.pdf",
     "coddling_lukianoff_haidt.txt", "pdf"),
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Eric Hoffer - The true believer_ Thoughts on the nature of mass movements (1980, Time-Life Books) - libgen.li.epub",
     "true_believer_hoffer.txt", "ebook"),
    ("03_TIER_2_CANON_BOOKS/decision_judgment/Gustave Le Bon - The crowd_ a study of the popular mind (2001, Dover Publications) - libgen.li.pdf",
     "the_crowd_lebon.txt", "pdf"),
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
    print(f"OK  {name:32} {words:>8} words")
    ok += 1

print(f"\nSources in: {len(SOURCES)} · extracted out: {ok} · failures: {len(SOURCES)-ok}")
