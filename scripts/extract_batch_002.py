#!/usr/bin/env python3
"""Extract BATCH_002_TIER_1_CANON_BOOKS. Idempotent."""
import os
import subprocess
import sys
from pathlib import Path

SRC = Path.home() / "AI-Brain-Refinery" / "raw" / "02_TIER_1_CANON_BOOKS"
DST = Path.home() / "AI-Brain-Refinery" / "batches" / "batch_002_extracted"
DST.mkdir(parents=True, exist_ok=True)

PANDOC = "/opt/homebrew/bin/pandoc"
PDFTOTEXT = "/opt/homebrew/bin/pdftotext"
EBOOK_CONVERT = "/opt/homebrew/bin/ebook-convert"
TEXTUTIL = "/usr/bin/textutil"

# Filename → output slug
SLUG = {
    " Andrew Chen - The Cold Start Problem_ How to Start and Scale Network Effects (2021, Harper Business) - libgen.li.epub": "cold_start_problem_chen",
    " Brad Stone - The Everything Store_ Jeff Bezos and the Age of Amazon (2013, Little, Brown and Company) - libgen.li.epub": "everything_store_bezos_stone",
    " Charles T. Munger, Peter D. Kaufman, Ed Wexler, Warren E. Buffet - Poor Charlie's Almanack_ The Wit and Wisdom of Charles T. Munger (2005, Walsworth Publishing Company) - libgen.li.pdf": "poor_charlies_almanack_munger",
    " Colin Bryar_ Bill Carr - Working Backwards (2021, St. Martin's Publishing Group) - libgen.li.epub": "working_backwards_bryar_carr",
    " Ed Catmull, Amy Wallace - Creativity, Inc._ Overcoming the Unseen Forces That Stand in the Way of True Inspiration (2014, Random House) - libgen.li.epub": "creativity_inc_catmull",
    " Jack Weatherford - Genghis Khan and the Making of the Modern World (2005, Broadway) - libgen.li.epub": "genghis_khan_weatherford",
    " James B. Stewart - DisneyWar _ the battle for the magic kingdom (2006, Pocket) - libgen.li.epub": "disneywar_stewart",
    " John Seabrook - The Song Machine_ Inside the Hit Factory (2015, W. W. Norton & Company) - libgen.li.epub": "song_machine_seabrook",
    " Peter Thiel, Blake Masters - Zero to One_ Notes on Startups, or How to Build the Future (2014, Crown Business) - libgen.li.epub": "zero_to_one_thiel",
    " Phil knight - Shoe dog (0) - libgen.li.mobi": "shoe_dog_knight",
    " Robert Iger_ Joel Lovell - The Ride of a Lifetime_ Lessons Learned from 15 Years as CEO of the Walt Disney Company (2019, Random House) - libgen.li.epub": "ride_of_a_lifetime_iger",
    " Stoute, Steve - The Tanning of America_ How Hip-Hop Created a Culture That Rewrote the Rules of the New Economy (2011, Penguin Group USA, Inc.) - libgen.li.epub": "tanning_of_america_stoute",
    " Walter Isaacson - Steve Jobs Walter Isaacson (2011) - libgen.li.epub": "steve_jobs_isaacson",
    " William N. Thorndike - The Outsiders_ Eight Unconventional CEOs and Their Radically Rational Blueprint for Success (2012, Harvard Business Review Press) - libgen.li.epub": "outsiders_thorndike",
    "[Alexander the Great 1 ] Freeman, Philip - Alexander the Great (2016) - libgen.li.epub": "alexander_the_great_freeman",
    "[Baker & Taylor Books (Firm)._ Axis 360] Robert Greene_ Joost Elffers - The 48 Laws of Power (2000, Penguin Group) - libgen.li.epub": "48_laws_of_power_greene",
    "[Joost Elffers Books ] Greene, Robert - The 33 Strategies of War (2008_2007, Penguin (Non-Classics)) - libgen.li.epub": "33_strategies_of_war_greene",
    "ArtOfWar.pdf": "art_of_war_sun_tzu",
    "mostly Powerhouse-.docx": "stoute_powerhouse_talk",
}

SKIP_PATTERNS = ["Hit Makers"]  # already covered in BATCH_001

success = skipped = failed = 0
results = []

for f in sorted(SRC.iterdir()):
    if not f.is_file():
        continue
    name = f.name

    if any(p in name for p in SKIP_PATTERNS):
        print(f"SKIP-DUP: {name}")
        skipped += 1
        results.append((name, "skip-dup", None))
        continue

    slug = SLUG.get(name)
    if not slug:
        print(f"NO-SLUG: {name}", file=sys.stderr)
        failed += 1
        results.append((name, "no-slug", None))
        continue

    ext = f.suffix.lower()
    out_md = DST / f"{slug}.md"
    out_txt = DST / f"{slug}.txt"

    if (out_md.exists() and out_md.stat().st_size > 0) or \
       (out_txt.exists() and out_txt.stat().st_size > 0):
        print(f"ALREADY: {slug}")
        skipped += 1
        results.append((name, "already", slug))
        continue

    try:
        if ext == ".epub":
            print(f"PANDOC: {slug}")
            r = subprocess.run(
                [PANDOC, "-f", "epub", "-t", "markdown", "--wrap=none",
                 "-o", str(out_md), str(f)],
                capture_output=True, text=True, timeout=120,
            )
            if r.returncode == 0 and out_md.exists() and out_md.stat().st_size > 0:
                success += 1
                results.append((name, "ok-pandoc", slug))
            else:
                print(f"  pandoc failed (rc={r.returncode}), fallback to ebook-convert")
                r2 = subprocess.run(
                    [EBOOK_CONVERT, str(f), str(out_txt)],
                    capture_output=True, text=True, timeout=180,
                )
                if r2.returncode == 0 and out_txt.exists() and out_txt.stat().st_size > 0:
                    success += 1
                    results.append((name, "ok-ebook-convert", slug))
                else:
                    print(f"  FAILED: {r2.stderr[:200]}", file=sys.stderr)
                    failed += 1
                    results.append((name, "failed", slug))
        elif ext == ".mobi":
            print(f"EBOOK-CONVERT: {slug}")
            r = subprocess.run(
                [EBOOK_CONVERT, str(f), str(out_txt)],
                capture_output=True, text=True, timeout=180,
            )
            if r.returncode == 0 and out_txt.exists() and out_txt.stat().st_size > 0:
                success += 1
                results.append((name, "ok-ebook-convert", slug))
            else:
                print(f"  FAILED: {r.stderr[:200]}", file=sys.stderr)
                failed += 1
                results.append((name, "failed", slug))
        elif ext == ".pdf":
            if slug == "poor_charlies_almanack_munger":
                sample = DST / f"{slug}_SAMPLE5.txt"
                print(f"PDFTOTEXT (test sample, 5 pages): {slug}")
                r = subprocess.run(
                    [PDFTOTEXT, "-layout", "-f", "1", "-l", "5",
                     str(f), str(sample)],
                    capture_output=True, text=True, timeout=120,
                )
                if r.returncode == 0 and sample.exists() and sample.stat().st_size > 0:
                    sz = sample.stat().st_size
                    print(f"  sample extracted, {sz} bytes")
                    success += 1
                    results.append((name, f"ok-sample-{sz}b", slug))
                else:
                    print("  empty extraction · file is likely image-scanned (OCR required)",
                          file=sys.stderr)
                    failed += 1
                    results.append((name, "scanned-needs-ocr", slug))
            else:
                print(f"PDFTOTEXT: {slug}")
                r = subprocess.run(
                    [PDFTOTEXT, "-layout", str(f), str(out_txt)],
                    capture_output=True, text=True, timeout=120,
                )
                if r.returncode == 0 and out_txt.exists() and out_txt.stat().st_size > 0:
                    success += 1
                    results.append((name, "ok-pdftotext", slug))
                else:
                    failed += 1
                    results.append((name, "failed", slug))
        elif ext == ".docx":
            print(f"TEXTUTIL: {slug}")
            r = subprocess.run(
                [TEXTUTIL, "-convert", "txt", "-output", str(out_txt), str(f)],
                capture_output=True, text=True, timeout=60,
            )
            if r.returncode == 0 and out_txt.exists() and out_txt.stat().st_size > 0:
                success += 1
                results.append((name, "ok-textutil", slug))
            else:
                failed += 1
                results.append((name, "failed", slug))
        else:
            print(f"UNKNOWN-EXT: {name} ({ext})", file=sys.stderr)
            failed += 1
            results.append((name, "unknown-ext", slug))
    except subprocess.TimeoutExpired:
        print(f"  TIMEOUT extracting {slug}", file=sys.stderr)
        failed += 1
        results.append((name, "timeout", slug))

print()
print(f"DONE. success={success} skipped={skipped} failed={failed}")
print()
print("Files in batch_002_extracted/:")
for p in sorted(DST.iterdir()):
    print(f"  {p.stat().st_size:>10,}  {p.name}")
