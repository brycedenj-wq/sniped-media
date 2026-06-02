# TIER_2_GREENE_STRATEGY extraction log · 2026-05-25

## Method

- **Tooling:** `pdftotext` (1 PDF) + `ebook-convert` (1 EPUB + 1 MOBI). Both on PATH. **No OCR. No new dependencies.**
- **Read-only on raw/:** sources converted into `01_KNOWLEDGE_BASE/batches/tier_2_greene_strategy_extracted/`. Original files untouched (mtimes unchanged · 2026-05-17 / 2026-05-18).
- **Script:** `scripts/extract_tier_2_greene_strategy.py` (refuses to overwrite; fails on missing source).
- **Source set:** the net-new Greene trio. The 48 Laws of Power / The 33 Strategies of War / The Art of War already canonical (BATCH_002 · excluded). The Book of Five Rings (djvu) broken (deferred). The Art of Seduction not present.

## Sources extracted (3 of 3 · 0 failures)

| source_file | source_title | author | format | words |
|---|---|---|---|--:|
| `laws_of_human_nature_greene.txt` | The Laws of Human Nature | Robert Greene | pdf | 270,897 |
| `mastery_greene.txt` | Mastery | Robert Greene | epub | 153,468 |
| `the_50th_law_50cent_greene.txt` | The 50th Law | 50 Cent and Robert Greene | mobi | 71,830 |

Combined: ~496,195 words. Content sampled per file to confirm real book text.

## Excluded / deferred

- **The 48 Laws of Power, The 33 Strategies of War, The Art of War:** already canonical (BATCH_002) · NOT re-extracted.
- **The Book of Five Rings (Musashi):** djvu · broken · DEFER · re-acquire clean text · NO OCR · not Greene.
- **The Art of Seduction (Greene):** not present in the universe · nothing to extract.
- **Adjacent Tier-2 clusters** (leadership_mgmt, consulting_service, systems_thinking, expertise_creativity, fashion_luxury): separate future lanes · NOT extracted.
- **The KJV Bible:** held SPIRITUAL_FOUNDATION anchor · NOT touched/staged/extracted.

## Notes

- No `raw/` mutation, no OCR, no installs, no master-file writes during extraction.
- The 50th Law (50 Cent & Greene) is a co-authored applied companion to Greene's power canon; held with the same defensive-awareness framing.
