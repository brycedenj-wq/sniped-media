# MODERN_COMMAND_NAPOLEON extraction log · 2026-05-24

## Source

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `napoleon_a_life_roberts.txt` | Napoleon: A Life | Andrew Roberts | epub | `raw/02_TIER_1_CANON_BOOKS/strategy_history/Emperor of the French Napoleon I_ Frankreich Kaiser Napoléon I._ - Napoleon _ a life (2014, Penguin Group_Viking) - libgen.li.epub` | 385,251 |

## Method

- **Tool:** `ebook-convert` (epub to txt). Already on PATH.
- **No OCR. No new dependencies.** The source file was read-only (not modified · 2026-05-18 mtime unchanged).
- **Output:** `01_KNOWLEDGE_BASE/batches/modern_command_napoleon_extracted/napoleon_a_life_roberts.txt` (385,251 words).
- **Script:** `scripts/extract_modern_command_napoleon.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded / deferred (0 chunks · 0 extraction)

- **Discourses on Livy (Machiavelli):** DEFERRED to a political-theory lane (CLASSICAL_STRATEGY-adjacent) · NOT extracted.
- **Grant + Washington: A Life (Chernow):** already chunked in HISTORICAL_BIOGRAPHY · NOT extracted.
- **Herodotus / Thucydides / Arrian / Engels:** already chunked in CLASSICAL_HISTORY · NOT extracted.
- **The Prince / On War / Meditations / Landmark Caesar:** already chunked in CLASSICAL_STRATEGY · NOT extracted.
- **Art of War / 48 Laws of Power / 33 Strategies of War:** already chunked in BATCH_002 · NOT extracted.
- **The Book of Five Rings (Musashi):** `.djvu` (unsupported) · NOT extracted.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked. Held separately as a SPIRITUAL_FOUNDATION anchor.
- **Every operating_founder / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2 source, and CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** NOT extracted.

## Scope-guard note (large single biography)

The single source is ~385,251 words (a long ~800+ page biography). Per the operator's scope guard, the lane is **representative modern-command / leadership / power / operator-pattern extraction, NOT a chapter-by-chapter biography summary** · 14 curated chunks (incl. 1 synthesis), not a retelling of the life.

## Result

- Sources in: 1 · extracted out: 1 · failures: 0.
- Ready for chunking (completed in the same ship · see `MODERN_COMMAND_NAPOLEON_COMPLETE.md`).
