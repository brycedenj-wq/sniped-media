# POSITIONING_DISRUPTION extraction log · 2026-05-25

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `crossing_the_chasm_moore.txt` | Crossing the Chasm (3rd ed.) | Geoffrey A. Moore | mobi | `raw/02_TIER_1_CANON_BOOKS/sales_positioning/ Geoffrey A. Moore - Crossing the Chasm, 3rd Edition_ ... (2014, HarperBusiness) - libgen.li.mobi` | 71,720 |
| `mom_test_fitzpatrick.txt` | The Mom Test | Rob Fitzpatrick | azw3 | `raw/02_TIER_1_CANON_BOOKS/sales_positioning/Fitzpatrick, Rob - The Mom Test_ ... (2016) - libgen.li.azw3` | 30,791 |
| `innovators_dilemma_christensen.txt` | The Innovator's Dilemma | Clayton M. Christensen | pdf | `raw/02_TIER_1_CANON_BOOKS/sales_positioning/The Innovator&_039_s Dilemma_ ... {Clayton M. Christensen}(2013, Harvard Business Review Press)... libgen.li.pdf` | 80,876 |

## Method

- **Tools:** `ebook-convert` (Crossing the Chasm mobi, The Mom Test azw3) + `pdftotext` (The Innovator's Dilemma pdf). Both already on PATH.
- **No OCR. No new dependencies.** All three source files were read-only (not modified · mtimes unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/positioning_disruption_extracted/` (3 .txt · 183,387 words total).
- **Source selection:** the 3 net-new sources confirmed by SALES_POSITIONING_OVERLAP_AUDIT (the other 13 sales_positioning books are already canonical in BATCH_009 / BATCH_009_EXPANSION). Content sanity confirmed before chunking (chasm/whole-product/pragmatist anchors in Moore; compliments/commitment/fluff in Fitzpatrick; disruptive-technology/value-network/trajectory in Christensen).
- **Script:** `scripts/extract_positioning_disruption.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **The 13 already-canonical sales_positioning titles:** Made to Stick, Differentiate or Die, $100M Leads, $100M Offers, Building a StoryBrand, Obviously Awesome, Purple Cow, This Is Marketing (BATCH_009); Eating the Big Fish, Competing Against Luck, Play Bigger, Never Split the Difference, Tribes (BATCH_009_EXPANSION) · NOT extracted, NOT re-chunked.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked · held SPIRITUAL_FOUNDATION anchor.
- **Every ADVERTISING_RECOVERY / PERSUASION_RECOVERY / NETWORK_DISTRIBUTION / OPERATING_FOUNDER source, every other-cluster source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (3 sources · ~183,387 words)

Per the operator's scope guard, the lane is **representative positioning / customer-truth / disruption pattern extraction, NOT a sales/copy/offer/negotiation summary** (that material is already canonical) · 11 curated chunks (incl. 1 synthesis · per-source Crossing the Chasm 5 [4 + synthesis] / The Innovator's Dilemma 4 / The Mom Test 2), not a chapter walk.

## Result

- Sources in: 3 · extracted out: 3 · failures: 0.
- Ready for chunking (completed in the same ship · see `POSITIONING_DISRUPTION_COMPLETE.md`).
