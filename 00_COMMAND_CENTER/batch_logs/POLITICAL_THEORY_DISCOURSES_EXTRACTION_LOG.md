# POLITICAL_THEORY_DISCOURSES extraction log · 2026-05-24

## Source

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `discourses_on_livy_machiavelli.txt` | Discourses on Livy | Niccolo Machiavelli (Ninian Hill Thomson, tr.) | pdf (490 pp) | `raw/02_TIER_1_CANON_BOOKS/strategy_history/[Dover books on history, political and social science] Niccolo Machiavelli, Ninian Hill Thomson - Discourses on Livy (2007, Dover Publications) - libgen.li.pdf` | 143,936 |

## Method

- **Tool:** `pdftotext` (pdf to txt). Already on PATH.
- **No OCR. No new dependencies.** The source file was read-only (not modified · 2026-05-18 mtime unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/political_theory_discourses_extracted/discourses_on_livy_machiavelli.txt` (143,936 words · clean text layer · intact chapter structure).
- **Script:** `scripts/extract_political_theory_discourses.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **The Prince (Machiavelli):** already chunked in CLASSICAL_STRATEGY · NOT extracted (the Discourses is the complementary republican-strategy treatise by the same author).
- **On War / Meditations / Landmark Caesar:** already chunked in CLASSICAL_STRATEGY · NOT extracted.
- **Herodotus / Thucydides / Arrian / Engels:** already chunked in CLASSICAL_HISTORY · NOT extracted.
- **Napoleon: A Life (Roberts):** already chunked in MODERN_COMMAND_NAPOLEON · NOT extracted.
- **Art of War / 48 Laws of Power / 33 Strategies of War:** already chunked in BATCH_002 · NOT extracted.
- **The Book of Five Rings (Musashi):** `.djvu` (unsupported) · NOT extracted.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. Held separately as a SPIRITUAL_FOUNDATION anchor.
- **Every operating_founder / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2 source (incl. the Greene trio), and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (dense ~140-chapter treatise)

The single source is ~143,936 words across three books and ~140 short chapters. Per the operator's scope guard, the lane is **representative institutional-power / organization-design / operator-pattern extraction, NOT a chapter-by-chapter political-theory summary** · 12 curated chunks (incl. 1 synthesis), not a chapter walk.

## Result

- Sources in: 1 · extracted out: 1 · failures: 0.
- Ready for chunking (completed in the same ship · see `POLITICAL_THEORY_DISCOURSES_COMPLETE.md`).
