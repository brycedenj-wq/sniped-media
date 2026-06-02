#!/usr/bin/env python3
"""Extract the LITERARY_RECOVERY sources (2 recovered literary e-books only).

Beloved (Morrison) azw3 + Jonathan Livingston Seagull (Bach) epub, the `_RECOVERED`
files only. ebook-convert (calibre) only. No OCR. No new dependencies.
Does NOT modify the raw/ originals (read-only input). Old 4-page PDF stub + old djvu
excluded. Bible not touched.
"""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
T1 = REPO / "raw" / "02_TIER_1_CANON_BOOKS"
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "literary_recovery_extracted"

# (relative path under 02_TIER_1_CANON_BOOKS, normalized output stem)
SOURCES = [
    (
        "literary_canon_black/Toni Morrison - Beloved (Vintage International) - "
        "libgen.li_RECOVERED.azw3",
        "beloved_morrison",
    ),
    (
        "literary_canon_general/ Bach, Richard - Jonathan Livingston Seagull "
        "(2010, Avon Books) - libgen.li_RECOVERED.epub",
        "jonathan_livingston_seagull_bach",
    ),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    failures = 0
    for rel, stem in SOURCES:
        src = T1 / rel
        dst = OUT / f"{stem}.txt"
        if not src.exists():
            print(f"FAIL missing source: {src}")
            failures += 1
            continue
        if dst.exists():
            print(f"REFUSE overwrite (exists): {dst}")
            failures += 1
            continue
        r = subprocess.run(
            ["ebook-convert", str(src), str(dst)],
            capture_output=True, text=True,
        )
        if r.returncode != 0 or not dst.exists():
            print(f"FAIL extract: {rel}\n{r.stderr[-500:]}")
            failures += 1
            continue
        words = len(dst.read_text(errors="ignore").split())
        total += words
        print(f"OK {rel}\n   -> {dst.name} ({words:,} words)")
    print(f"\nsources in: {len(SOURCES)} · extracted out: {len(SOURCES) - failures} · "
          f"failures: {failures} · total words: {total:,}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
