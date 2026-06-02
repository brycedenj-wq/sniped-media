# LEADERSHIP_MGMT extraction log · 2026-05-26

## Tooling

- `pdftotext` (pdf), `ebook-convert` / calibre (epub, mobi, azw3). Both on PATH. No OCR. No new dependencies installed.
- Script: `scripts/extract_leadership_mgmt.py` (read-only on `raw/`; refuses to overwrite existing extracted files).
- Output dir: `01_KNOWLEDGE_BASE/batches/leadership_mgmt_extracted/`.

## Sources extracted (9 of 9 · 0 failures)

| Source | Author | Method | Extracted file | Words |
|---|---|---|---|--:|
| The Culture Code | Daniel Coyle | ebook-convert (epub) | `the_culture_code_coyle.txt` | 63,281 |
| Leadership in Turbulent Times | Doris Kearns Goodwin | ebook-convert (epub) | `leadership_in_turbulent_times_goodwin.txt` | 195,517 |
| Team of Rivals | Doris Kearns Goodwin | ebook-convert (azw3) | `team_of_rivals_goodwin.txt` | 90,717 |
| Extreme Ownership | Jocko Willink & Leif Babin | ebook-convert (mobi) | `extreme_ownership_willink_babin.txt` | 84,758 |
| The Dichotomy of Leadership | Jocko Willink & Leif Babin | ebook-convert (epub) | `the_dichotomy_of_leadership_willink_babin.txt` | 96,028 |
| Measure What Matters | John Doerr | ebook-convert (epub) | `measure_what_matters_doerr.txt` | 71,642 |
| Radical Candor | Kim Scott | ebook-convert (epub) | `radical_candor_scott.txt` | 93,384 |
| Turn the Ship Around! | L. David Marquet | ebook-convert (epub) | `turn_the_ship_around_marquet.txt` | 65,697 |
| High Output Management | Andrew S. Grove | pdftotext (pdf) | `high_output_management_grove.txt` | 68,084 |

`SOURCES IN: 9 · EXTRACTED OUT: 9 · FAILURES: 0`. Total ~829,108 words. Word counts match the ADJACENT_TIER_2_CLUSTERS_PLAN read-only probe.

## Notes

- `pdftotext` emitted benign font/dictionary parser warnings on the older Grove PDF (suppressed); these are harmless stderr notes, NOT OCR and NOT extraction failures. All nine files extracted full, clean book text (sampled to confirm real prose).
- The Team of Rivals azw3 carries Portuguese-edition front matter on its title page (a Brazilian Record edition of the English text); the body is the full English book. The title-page phrase renders as "Team of rivals."
- The separate Death by Meeting `.txt` in this folder is a ~1,131-word third-party summary stub and was NOT extracted (excluded per the plan).

## Integrity

- raw/ source files NOT modified (mtimes unchanged · 2026-05-16 to 2026-05-18).
- No OCR. No new dependencies. No `pip`/`brew`/`apt` installs.
- The consulting_service / systems_thinking / expertise_creativity folders were NOT extracted (their own lanes · CONSULTING_SERVICE already canonical).
- The Death by Meeting summary stub, the Dieter Rams image-only monograph, the Csikszentmihalyi `.djvu`, and the McLuhan duplicate twin were NOT extracted.
- The KJV Bible was NOT touched, staged, or extracted (not present in raw/).
- CURRENT_IDENTITY_AND_BRAND_OPTIONALITY and the SNIPED-authored brand docs were NOT extracted.

## Next step

Chunking is a separate step. See `scripts/write_leadership_mgmt_chunks.py` -> `LEADERSHIP_MGMT_CHUNKS.jsonl` (16 chunks · validated). Master-consolidation awaits separate operator authorization.
