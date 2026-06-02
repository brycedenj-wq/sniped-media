#!/usr/bin/env python3
"""Extract the CLASSICAL_HISTORY sources (4 curated ancient Greek/Macedonian histories).

The Landmark Herodotus (epub) + The Landmark Thucydides (epub) + Arrian / The Campaigns
of Alexander (azw3) + Engels / Alexander the Great and the Logistics of the Macedonian
Army (pdf). pdftotext + ebook-convert (both on PATH). No OCR. No new dependencies.
Does NOT modify the raw/ originals (read-only input). Excludes Napoleon: A Life and
Discourses on Livy (deferred to register-appropriate lanes), Art of War / 48 Laws /
33 Strategies (already BATCH_002), Book of Five Rings (djvu), The Prince / On War /
Meditations / Landmark Caesar (already CLASSICAL_STRATEGY), and the Bible.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SH = REPO / "raw" / "02_TIER_1_CANON_BOOKS" / "strategy_history"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "classical_history_extracted"

# (source filename in strategy_history/, normalized output stem, tool)
SOURCES = [
    ("Herodotus, Robert B. Strassler[ed] - The Landmark Herodotus_ Histories "
     "(2007, 2009, Anchor Books) - libgen.li.epub",
     "herodotus_histories", "ebook-convert"),
    ("Thucydides, Robert B. Strassler, Richard Crawley, Victor Davis H - The Landmark "
     "Thucydides_ A Comprehensive Guide to the Peloponnesian War (1998, Free Press) - "
     "libgen.li.epub",
     "thucydides_peloponnesian_war", "ebook-convert"),
    ("[Classics] Arrian - The Campaigns of Alexander (2003, Penguin Books Ltd) - libgen.li.azw3",
     "arrian_campaigns_of_alexander", "ebook-convert"),
    ("Donald W. Engels - Alexander the Great and the Logistics of the Macedonian Army "
     "(2020, University of California Press) [10.1525_9780520352162] - libgen.li.pdf",
     "engels_macedonian_logistics", "pdftotext"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    failures = 0
    for src_name, stem, tool in SOURCES:
        src = SH / src_name
        dst = OUT / f"{stem}.txt"
        if not src.exists():
            print(f"FAIL missing source: {src}")
            failures += 1
            continue
        if dst.exists():
            print(f"REFUSE overwrite (exists): {dst}")
            failures += 1
            continue
        cmd = ["pdftotext", str(src), str(dst)] if tool == "pdftotext" else ["ebook-convert", str(src), str(dst)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0 or not dst.exists():
            print(f"FAIL extract: {src_name}\n{r.stderr[-500:]}")
            failures += 1
            continue
        words = len(dst.read_text(errors="ignore").split())
        total += words
        print(f"OK [{tool}] {src_name}\n   -> {dst.name} ({words:,} words)")
    print(f"\nsources in: {len(SOURCES)} · extracted out: {len(SOURCES) - failures} · "
          f"failures: {failures} · total words: {total:,}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
