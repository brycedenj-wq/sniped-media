# MONEY_OWNERSHIP extraction log · 2026-05-23

## Method

- 3 pdf via `pdftotext -layout` · 2 epub via Python stdlib `zipfile` + spine-ordered HTML-strip · 1 docx via `pandoc -f docx -t plain`.
- Keyword-substring matching on filenames in `scripts/extract_money_ownership.py` (handles leading-space filenames in `investing_finance/`).
- NO OCR. NO new dependencies. raw/ not modified. Refuses to overwrite an existing extracted file.

## Sources extracted (6 of 6 CORE · 0 failures)

| Output file | Source | Type | Words |
|---|---|---|---:|
| `psychology_of_money_housel.txt` | Morgan Housel · The Psychology of Money | pdf | 52,730 |
| `essays_of_warren_buffett.txt` | Buffett/Cunningham · The Essays of Warren Buffett | epub | 119,340 |
| `the_most_important_thing_marks.txt` | Howard Marks · The Most Important Thing | pdf | 65,219 |
| `king_of_capital_blackstone.txt` | Carey/Morris · King of Capital (Blackstone) | epub | 127,983 |
| `the_power_law_mallaby.txt` | Sebastian Mallaby · The Power Law | epub | 198,120 |
| `money_wealth_getting_ahead.txt` | SNIPED (synthesis) · Money, Wealth & Getting Ahead | docx | 1,687 |

Total: 565,079 words (INTERNAL chunk-authoring reference only).

## Notes

- All six extracted cleanly · word counts match the plan's pre-flight peek · no scanned/stub files among the CORE.
- The 5 books are in-copyright trade books; the docx is SNIPED-authored. Extracted full text is internal reference only.
- Files live under `01_KNOWLEDGE_BASE/batches/money_ownership_extracted/`.
- Excluded per plan (0 extraction): Poor Charlie's Almanack (chunked BATCH_002), Naval Almanack (chunked BATCH_003), Margin of Safety (scanned · recovery), the 7 deferred long/deep texts, memoirs_biographies, recovery/acquisition items, CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources, any other investing_finance files.
