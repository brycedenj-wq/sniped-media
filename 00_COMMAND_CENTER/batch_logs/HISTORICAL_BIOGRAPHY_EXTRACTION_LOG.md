# HISTORICAL_BIOGRAPHY extraction log · 2026-05-24

## Sources

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `grant_chernow.txt` | Grant | Ron Chernow | epub | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Ron Chernow - Grant (2017, Penguin Publishing Group) - libgen.li.epub` | 477,787 |
| `washington_a_life_chernow.txt` | Washington: A Life | Ron Chernow | pdf (clean text layer) | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/Ron Chernow - Washington_ A Life - libgen.li.pdf` | 434,269 |

## Method

- **Tools:** `ebook-convert` (calibre) for the Grant epub; `pdftotext` for the Washington pdf (945-page clean text layer, NOT scanned). Both already on PATH.
- **No OCR. No new dependencies.** Both source files were read-only (not modified).
- **Output:** `01_KNOWLEDGE_BASE/batches/historical_biography_extracted/` (2 .txt · 912,056 words total).
- **Script:** `scripts/extract_historical_biography.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded (0 chunks · 0 extraction)

- **Titan: The Life of John D. Rockefeller (Chernow)** · present in the same memoirs_biographies folder · already chunked in FOUNDER_SECOND_TIER · NOT extracted here (author overlap, distinct title/register).
- **The KJV Bible:** NOT touched, staged, extracted, or chunked.
- **Every other memoirs_biographies / already-canonical source:** NOT extracted (single curated 2-source lane).

## Scope-guard note (very large sources)

Combined ~912,056 words (the two largest single sources approached so far). Per the operator's scope guard, the lane is **representative leadership/power/operator-pattern extraction, NOT exhaustive biography summary** · 16 curated chunks (Grant 8, Washington 8), not chapter-by-chapter coverage. The Washington pdftotext output carries a leading `rrrr...` cover-image artifact line; it is harmless and was not chunked.

## Result

- Sources in: 2 · extracted out: 2 · failures: 0.
- Ready for chunking (completed in the same ship · see `HISTORICAL_BIOGRAPHY_COMPLETE.md`).
