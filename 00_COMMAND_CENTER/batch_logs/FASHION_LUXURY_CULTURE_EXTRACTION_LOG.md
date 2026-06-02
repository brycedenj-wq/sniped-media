# FASHION_LUXURY_CULTURE extraction log · 2026-05-26

## Tooling

- `pdftotext` (pdf) and `ebook-convert` / calibre (epub, mobi). Both on PATH. No OCR. No new dependencies installed.
- Script: `scripts/extract_fashion_luxury_culture.py` (read-only on `raw/`; refuses to overwrite existing extracted files).
- Output dir: `01_KNOWLEDGE_BASE/batches/fashion_luxury_culture_extracted/`.

## Sources extracted (4 of 4 · 0 failures)

| Source | raw/ path (under `03_TIER_2_CANON_BOOKS/fashion_luxury/`) | Method | Extracted file | Words |
|---|---|---|---|--:|
| The Beautiful Fall (Drake) | ` Alicia Drake - The Beautiful Fall_ ... (2009, Little, Brown) - libgen.li.mobi` | ebook-convert (mobi) | `the_beautiful_fall_drake.txt` | 169,922 |
| The Chiffon Trenches (Talley) | ` André Leon Talley - The Chiffon Trenches_ A Memoir (2020, Random House) - libgen.li.epub` | ebook-convert (epub) | `the_chiffon_trenches_talley.txt` | 87,847 |
| Dior by Dior (Dior) | ` Christian Dior - Dior by Dior- The Autobiography of Christian Dior - libgen.li.pdf` | pdftotext (pdf) | `dior_by_dior_dior.txt` | 73,252 |
| The Little Dictionary of Fashion (Dior) | ` Christian Dior - The little dictionary of fashion (2007, V & A) - libgen.li.epub` | ebook-convert (epub) | `the_little_dictionary_of_fashion_dior.txt` | 18,733 |

`SOURCES IN: 4 · EXTRACTED OUT: 4 · FAILURES: 0`. Total ~349,754 words. All filenames carry a leading space in raw/; preserved exactly in the script's SOURCES paths.

## Sampling / quality confirmation

- Each extracted .txt sampled to confirm real book text (not scan artifacts): Drake's narrative prose, Talley's first-person memoir, Dior's autobiography chapters, and Dior's A-to-Z dictionary entries all confirmed clean and text-bearing.
- The Little Dictionary's odd container type ("data") extracted cleanly via ebook-convert (18,733 words · consistent with the plan probe).
- Word counts match the FASHION_LUXURY_PLAN read-only probes within rounding (probe: 169,937 / 87,830 / 73,252 / 18,733).

## Integrity

- raw/ source files NOT modified (mtimes unchanged · 2026-05-17).
- No OCR. No new dependencies. No `pip`/`brew`/`apt` installs.
- The 3 FASHION_LUXURY_STRATEGY books (already canonical), the Abloh "Figures of Speech" article (third-party / tiny · Abloh already BATCH_005), and the already-canonical Status and Culture / The Status Game / Grace / BRAND_CANON sources were NOT extracted.
- The KJV Bible was NOT touched, staged, or extracted (not present in raw/).
- CURRENT_IDENTITY_AND_BRAND_OPTIONALITY and the SNIPED-authored brand docs were NOT extracted (held).

## Next step

Chunking is a separate step. See `scripts/write_fashion_luxury_culture_chunks.py` → `FASHION_LUXURY_CULTURE_CHUNKS.jsonl` (13 chunks · validated). Master-consolidation awaits separate operator authorization.
