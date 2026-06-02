# ADVERTISING_RECOVERY extraction log · recovered advertising/copywriting canon · 2026-05-24

## Sources (3 of 3 recovered · 0 failures)

| # | Title | Author | Recovered format | Extraction | Words | Output |
|---|---|---|---|---|--:|---|
| 1 | Confessions of an Advertising Man | David Ogilvy | pdf (z-lib `_RECOVERED`) | pdftotext | 42,924 | `confessions_of_an_advertising_man_ogilvy.txt` |
| 2 | The Adweek Copywriting Handbook | Joseph Sugarman | azw3 (`_RECOVERED`) | ebook-convert | 107,745 | `the_adweek_copywriting_handbook_sugarman.txt` |
| 3 | The Boron Letters | Gary Halbert | epub (`_RECOVERED`) | ebook-convert | 43,043 | `the_boron_letters_halbert.txt` |

Total ~193,712 words. Method: pdftotext (poppler) + ebook-convert (calibre), both pre-existing on PATH. **No OCR. No new dependencies.**

## Process

1. `scripts/extract_advertising_recovery.py` read the 3 `_RECOVERED` files from `raw/02_TIER_1_CANON_BOOKS/advertising/` (read-only · originals unmodified) and wrote normalized `.txt` to `advertising_recovery_extracted/`. Refuses to overwrite.
2. **Used the `_RECOVERED` files only.** The old scanned Confessions PDF (`David Ogilvy_ Alan Parker - ... libgen.li.pdf`, 0 extractable words) contributed 0. Caples (Tested Advertising Methods · still scanned) and Hey, Whipple, Squeeze This (a different Adweek-series book) were NOT extracted.
3. No other advertising-folder file, no recovery item outside these 3, no CURRENT_IDENTITY source, and no already-canonical batch source was touched. The Bible was NOT touched/staged/extracted.

## Coverage map (used to ground curated, attributed chunks)

- **Ogilvy (Confessions):** agency management + leadership, get/keep clients, build great campaigns, headlines as the decisive element, brand image, research/testing discipline, honesty ("never write an ad you would not want your family to read").
- **Sugarman (Adweek Copywriting Handbook):** the first-sentence job, the slippery slide, seeds of curiosity, copy as emotion (sell emotion / justify logic), psychological triggers.
- **Halbert (Boron Letters):** the starving crowd (market-first), personal conversational copy, the offer + AIDA, the list and the response sequence.

## Deviations

None. 3 recovered sources as planned. No OCR, no new dependency, no master-file change, no raw modification. Bible excluded.
