# LITERARY_RECOVERY extraction log · 2026-05-24

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `beloved_morrison.txt` | Beloved | Toni Morrison | azw3 (recovered) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_black/Toni Morrison - Beloved (Vintage International) - libgen.li_RECOVERED.azw3` | 97,915 |
| `jonathan_livingston_seagull_bach.txt` | Jonathan Livingston Seagull | Richard Bach | epub (recovered) | `raw/02_TIER_1_CANON_BOOKS/literary_canon_general/ Bach, Richard - Jonathan Livingston Seagull (2010, Avon Books) - libgen.li_RECOVERED.epub` | 8,977 |

## Method

- **Tool:** `ebook-convert` (calibre · already on PATH). azw3/epub to plain .txt.
- **No OCR. No new dependencies.** No pip install. Both source files were read-only (not modified).
- **Output:** `01_KNOWLEDGE_BASE/batches/literary_recovery_extracted/` (2 .txt · 106,892 words total).
- **Script:** `scripts/extract_literary_recovery.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded (0 chunks · 0 extraction)

- **Old Beloved 4-page PDF stub** (`[Beloved Trilogy 1 ...] Beloved{Toni Morrison}(1987) ... libgen.li.pdf`): a 4-page excerpt, NOT the full novel. NOT extracted. Left in place untouched.
- **Old Jonathan Livingston Seagull djvu** (`Richard Bach - Jonathan Livingston Seagull. (1973, Avon Books, N. Y.) - libgen.li.djvu`): unsupported format (no djvutxt on PATH). NOT extracted. Left in place untouched.
- **Already-chunked literary-canon titles** (incl. Morrison's The Bluest Eye in LITERARY_CANON_BLACK): NOT extracted (net-new titles only).
- **The KJV Bible:** NOT touched, staged, extracted, or chunked.
- **Every other literary_canon_black / literary_canon_general source:** NOT extracted (single curated 2-source lane).

## Note (Seagull word count)

The Seagull `_RECOVERED.epub` extracts to 8,977 words. This is correct: Jonathan Livingston Seagull is a novella-length fable, not a truncation. The full text (all three Parts) is present.

## Result

- Sources in: 2 · extracted out: 2 · failures: 0.
- Ready for chunking (completed in the same ship · see `LITERARY_RECOVERY_COMPLETE.md`).
