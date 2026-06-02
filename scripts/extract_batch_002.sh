#!/bin/bash
# Extract BATCH_002_TIER_1_CANON_BOOKS.
# Idempotent: skips files that already have a non-empty extraction.

set -u
SRC="$HOME/AI-Brain-Refinery/raw/02_TIER_1_CANON_BOOKS"
DST="$HOME/AI-Brain-Refinery/batches/batch_002_extracted"
mkdir -p "$DST"

# Resolve tools (calibre may be in /Applications)
PANDOC="$(command -v pandoc)"
PDFTOTEXT="$(command -v pdftotext)"
EBOOK_CONVERT="$(command -v ebook-convert || true)"
[ -z "$EBOOK_CONVERT" ] && EBOOK_CONVERT="/Applications/calibre.app/Contents/MacOS/ebook-convert"
TEXTUTIL="$(command -v textutil)"

echo "TOOLS:"
echo "  pandoc       = $PANDOC"
echo "  pdftotext    = $PDFTOTEXT"
echo "  ebook-convert= $EBOOK_CONVERT"
echo "  textutil     = $TEXTUTIL"
echo

# Slugs map filename → short clean output name
declare -A SLUG
SLUG[" Andrew Chen - The Cold Start Problem_ How to Start and Scale Network Effects (2021, Harper Business) - libgen.li.epub"]="cold_start_problem_chen"
SLUG[" Brad Stone - The Everything Store_ Jeff Bezos and the Age of Amazon (2013, Little, Brown and Company) - libgen.li.epub"]="everything_store_bezos_stone"
SLUG[" Charles T. Munger, Peter D. Kaufman, Ed Wexler, Warren E. Buffet - Poor Charlie's Almanack_ The Wit and Wisdom of Charles T. Munger (2005, Walsworth Publishing Company) - libgen.li.pdf"]="poor_charlies_almanack_munger"
SLUG[" Colin Bryar_ Bill Carr - Working Backwards (2021, St. Martin's Publishing Group) - libgen.li.epub"]="working_backwards_bryar_carr"
SLUG[" Ed Catmull, Amy Wallace - Creativity, Inc._ Overcoming the Unseen Forces That Stand in the Way of True Inspiration (2014, Random House) - libgen.li.epub"]="creativity_inc_catmull"
SLUG[" Jack Weatherford - Genghis Khan and the Making of the Modern World (2005, Broadway) - libgen.li.epub"]="genghis_khan_weatherford"
SLUG[" James B. Stewart - DisneyWar _ the battle for the magic kingdom (2006, Pocket) - libgen.li.epub"]="disneywar_stewart"
SLUG[" John Seabrook - The Song Machine_ Inside the Hit Factory (2015, W. W. Norton & Company) - libgen.li.epub"]="song_machine_seabrook"
SLUG[" Peter Thiel, Blake Masters - Zero to One_ Notes on Startups, or How to Build the Future (2014, Crown Business) - libgen.li.epub"]="zero_to_one_thiel"
SLUG[" Phil knight - Shoe dog (0) - libgen.li.mobi"]="shoe_dog_knight"
SLUG[" Robert Iger_ Joel Lovell - The Ride of a Lifetime_ Lessons Learned from 15 Years as CEO of the Walt Disney Company (2019, Random House) - libgen.li.epub"]="ride_of_a_lifetime_iger"
SLUG[" Stoute, Steve - The Tanning of America_ How Hip-Hop Created a Culture That Rewrote the Rules of the New Economy (2011, Penguin Group USA, Inc.) - libgen.li.epub"]="tanning_of_america_stoute"
SLUG[" Walter Isaacson - Steve Jobs Walter Isaacson (2011) - libgen.li.epub"]="steve_jobs_isaacson"
SLUG[" William N. Thorndike - The Outsiders_ Eight Unconventional CEOs and Their Radically Rational Blueprint for Success (2012, Harvard Business Review Press) - libgen.li.epub"]="outsiders_thorndike"
SLUG["[Alexander the Great 1 ] Freeman, Philip - Alexander the Great (2016) - libgen.li.epub"]="alexander_the_great_freeman"
SLUG["[Baker & Taylor Books (Firm)._ Axis 360] Robert Greene_ Joost Elffers - The 48 Laws of Power (2000, Penguin Group) - libgen.li.epub"]="48_laws_of_power_greene"
SLUG["[Joost Elffers Books ] Greene, Robert - The 33 Strategies of War (2008_2007, Penguin (Non-Classics)) - libgen.li.epub"]="33_strategies_of_war_greene"
SLUG["ArtOfWar.pdf"]="art_of_war_sun_tzu"
SLUG["mostly Powerhouse-.docx"]="stoute_powerhouse_talk"

cd "$SRC" || exit 1
TOTAL=0
SKIPPED=0
FAILED=0
SUCCESS=0

for f in *; do
  [ -f "$f" ] || continue
  TOTAL=$((TOTAL + 1))

  # Skip the Hit Makers duplicate explicitly
  if [[ "$f" == *"Hit Makers"* ]]; then
    echo "SKIP-DUP: $f"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  slug="${SLUG[$f]:-}"
  if [ -z "$slug" ]; then
    echo "NO-SLUG: $f" >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  ext="${f##*.}"
  ext_lower=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
  out_md="$DST/${slug}.md"
  out_txt="$DST/${slug}.txt"

  # Idempotency
  if [ -s "$out_md" ] || [ -s "$out_txt" ]; then
    echo "ALREADY: $slug"
    SKIPPED=$((SKIPPED + 1))
    continue
  fi

  case "$ext_lower" in
    epub)
      echo "PANDOC: $slug"
      if "$PANDOC" -f epub -t markdown --wrap=none -o "$out_md" "$f" 2>/dev/null; then
        SUCCESS=$((SUCCESS + 1))
      else
        echo "  fallback to ebook-convert"
        if "$EBOOK_CONVERT" "$f" "$out_txt" >/dev/null 2>&1; then
          SUCCESS=$((SUCCESS + 1))
        else
          echo "  FAILED" >&2
          FAILED=$((FAILED + 1))
        fi
      fi
      ;;
    mobi)
      echo "EBOOK-CONVERT: $slug"
      if "$EBOOK_CONVERT" "$f" "$out_txt" >/dev/null 2>&1; then
        SUCCESS=$((SUCCESS + 1))
      else
        echo "  FAILED" >&2
        FAILED=$((FAILED + 1))
      fi
      ;;
    pdf)
      # Special-case the giant Munger PDF: test 5 pages first, separate file
      if [[ "$slug" == "poor_charlies_almanack_munger" ]]; then
        echo "PDFTOTEXT (test sample, 5 pages): $slug"
        "$PDFTOTEXT" -layout -f 1 -l 5 "$f" "$DST/${slug}_SAMPLE5.txt" 2>/dev/null
        if [ -s "$DST/${slug}_SAMPLE5.txt" ]; then
          echo "  sample extracted · $(wc -c < "$DST/${slug}_SAMPLE5.txt") bytes"
          SUCCESS=$((SUCCESS + 1))
        else
          echo "  empty extraction · file is likely image-scanned (OCR required)" >&2
          FAILED=$((FAILED + 1))
        fi
      else
        echo "PDFTOTEXT: $slug"
        if "$PDFTOTEXT" -layout "$f" "$out_txt" 2>/dev/null && [ -s "$out_txt" ]; then
          SUCCESS=$((SUCCESS + 1))
        else
          echo "  FAILED" >&2
          FAILED=$((FAILED + 1))
        fi
      fi
      ;;
    docx)
      echo "TEXTUTIL: $slug"
      if "$TEXTUTIL" -convert txt -output "$out_txt" "$f" 2>/dev/null; then
        SUCCESS=$((SUCCESS + 1))
      else
        echo "  FAILED" >&2
        FAILED=$((FAILED + 1))
      fi
      ;;
    *)
      echo "UNKNOWN-EXT: $f ($ext_lower)" >&2
      FAILED=$((FAILED + 1))
      ;;
  esac
done

echo
echo "DONE. total=$TOTAL success=$SUCCESS skipped=$SKIPPED failed=$FAILED"
echo
echo "EXTRACTED:"
ls -lh "$DST/" | tail -n +2
