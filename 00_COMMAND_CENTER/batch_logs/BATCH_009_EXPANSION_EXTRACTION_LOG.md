# BATCH_009_EXPANSION extraction log · 2026-05-23

## Method

- 4 epub via Python stdlib `zipfile` + spine-ordered (OPF) HTML-strip.
- 1 pdf (Eating the Big Fish) via `pdftotext -layout`.
- Leading-space filenames (Eating the Big Fish, Competing Against Luck) handled by keyword-substring matching in `scripts/extract_batch_009_expansion.py`, not exact names.
- NO OCR. NO new dependencies. raw/ not modified. Refuses to overwrite an existing extracted file.

## Sources extracted (5 of 5 · 0 failures)

| Output file | Source (raw/02_TIER_1_CANON_BOOKS/sales_positioning/) | Type | Words |
|---|---|---|---:|
| `never_split_the_difference_voss.txt` | Voss & Raz · Never Split the Difference (2016) | epub | 82,437 |
| `eating_the_big_fish_morgan.txt` | Adam Morgan · Eating the Big Fish (2009) | pdf | 125,574 |
| `play_bigger_ramadan_lochhead.txt` | Ramadan/Peterson/Lochhead/Maney · Play Bigger (2016) | epub | 81,161 |
| `tribes_godin.txt` | Seth Godin · Tribes (2008) | epub | 31,472 |
| `competing_against_luck_christensen.txt` | Christensen/Dillon/Hall/Duncan · Competing Against Luck (2016) | epub | 83,793 |

Total: 404,437 words (INTERNAL chunk-authoring reference only).

## Notes

- All five extracted cleanly · word counts match the plan's pre-flight peek (small epub deltas from spine-ordering vs raw HTML-strip are expected).
- Eating the Big Fish PDF has a real text layer (125,574 words) · not scanned · no OCR needed.
- Extracted files live under `01_KNOWLEDGE_BASE/batches/batch_009_expansion_extracted/`.
