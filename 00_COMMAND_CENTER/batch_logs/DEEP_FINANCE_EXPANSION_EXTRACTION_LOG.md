# DEEP_FINANCE_EXPANSION extraction log · deep capital / finance expansion · 2026-05-24

## Sources (8 of 8 CORE · 0 failures)

| # | Title | Author | Raw format | Extraction | Words | Output |
|---|---|---|---|---|--:|---|
| 1 | Security Analysis: Sixth Edition | Graham, Dodd (Buffett foreword) | pdf | pdftotext | 391,812 | `security_analysis_graham_dodd.txt` |
| 2 | The Snowball | Alice Schroeder | pdf | pdftotext | 411,951 | `the_snowball_schroeder.txt` |
| 3 | The Intelligent Investor | Benjamin Graham | pdf | pdftotext | 45,067 | `the_intelligent_investor_graham.txt` |
| 4 | Mastering the Market Cycle | Howard Marks | epub | ebook-convert | 83,675 | `mastering_the_market_cycle_marks.txt` |
| 5 | The Sovereign Individual | Davidson, Rees-Mogg | pdf | pdftotext | 160,083 | `the_sovereign_individual_davidson.txt` |
| 6 | The Lords of Easy Money | Christopher Leonard | epub | ebook-convert | 123,192 | `the_lords_of_easy_money_leonard.txt` |
| 7 | The New Tycoons | Jason Kelly | azw3 | ebook-convert | 80,071 | `the_new_tycoons_kelly.txt` |
| 8 | Margin of Safety (RECOVERED epub) | Seth A. Klarman | epub | ebook-convert | 72,828 | `margin_of_safety_klarman.txt` |

Total extracted: ~1,368,679 words. Method: pdftotext (poppler) + ebook-convert (calibre), both pre-existing on PATH. **No OCR. No new dependencies.**

## Process

1. `scripts/extract_deep_finance_expansion.py` read the 8 CORE files from `raw/03_TIER_2_CANON_BOOKS/investing_finance/` (read-only · originals unmodified) and wrote normalized `.txt` to `deep_finance_expansion_extracted/`. The script refuses to overwrite existing extracted files.
2. **Margin of Safety used the RECOVERED epub** (`... - libgen.li_RECOVERED.epub`, 72,828 words), NOT the old scanned PDF (`... - libgen.li.pdf`, which remains in raw/ untouched and contributed 0).
3. No other `investing_finance/` file was extracted. The already-chunked MONEY_OWNERSHIP sources in that folder (Psychology of Money, Essays of Warren Buffett, The Most Important Thing, King of Capital, The Power Law) and the BATCH_002 Poor Charlie's Almanack were excluded.

## Notes

- **The Intelligent Investor** extracted as 45,067 words / ~142 pp · the staged copy is partial/abridged (full edition ~640 pp). Per plan, it was chunked modestly (3 chunks) for its core principles only.
- All 8 extracted cleanly with usable text layers; no scans, stubs, or conversion failures.

## Deviations

None. 8 CORE sources as planned. No OCR, no new dependency, no master-file change, no raw modification.
