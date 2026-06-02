# FASHION_LUXURY_STRATEGY extraction log · 2026-05-25

## Method

- **Tooling:** `pdftotext` (1 PDF) + `ebook-convert` (2 EPUBs). Both on PATH. **No OCR. No new dependencies.**
- **Read-only on raw/:** sources converted into `01_KNOWLEDGE_BASE/batches/fashion_luxury_strategy_extracted/`. Original files untouched (mtimes unchanged · 2026-05-17).
- **Script:** `scripts/extract_fashion_luxury_strategy.py` (refuses to overwrite; fails on missing source).
- **Source set:** the 3 luxury-strategy / commercial-register sources (the FIRST of the two split FASHION_LUXURY sub-lanes · operator-locked). The FASHION_LUXURY_CULTURE 4 books deferred; the Abloh article + already-canonical sources excluded.

## Sources extracted (3 of 3 · 0 failures)

| source_file | source_title | author | format | words |
|---|---|---|---|--:|
| `the_luxury_strategy_kapferer.txt` | The Luxury Strategy | Jean-Noel Kapferer and Vincent Bastien | pdf | 125,784 |
| `deluxe_thomas.txt` | Deluxe | Dana Thomas | epub | 117,693 |
| `the_end_of_fashion_agins.txt` | The End of Fashion | Teri Agins | epub | 100,393 |

Combined: ~343,870 words. Content sampled per file to confirm real book text.

## Excluded / deferred

- **FASHION_LUXURY_CULTURE (deferred sub-lane · its own future cycle):** The Beautiful Fall (Drake), The Chiffon Trenches (Talley), Dior by Dior, The Little Dictionary of Fashion (Dior) · NOT extracted.
- **Abloh "Figures of Speech" (Peters · third-party journal article · tiny · Abloh already BATCH_005):** NOT extracted.
- **Status and Culture / The Status Game** (already CULTURE_AND_STATUS), **Grace** (already FOUNDER_FASHION_RECOVERY), the **BRAND_CANON** sources (already canonical): NOT re-extracted.
- **SNIPED-authored brand docs:** held until the fresh SNIPED brief · NOT extracted.
- **The KJV Bible:** held SPIRITUAL_FOUNDATION anchor · NOT touched/staged/extracted.

## Notes

- No `raw/` mutation, no OCR, no installs, no master-file writes during extraction.
- The lane is the luxury-strategy / commercial register · read decision-neutrally (symbolic value / status architecture / scarcity / commercial perception), NOT a fashion-history/memoir/lifestyle summary and NOT a SNIPED brand directive.
