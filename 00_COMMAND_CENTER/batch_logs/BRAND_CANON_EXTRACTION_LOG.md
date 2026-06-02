# BRAND_CANON extraction log · 2026-05-25

## Method

- **Tooling:** `pdftotext` (2 PDFs) + `ebook-convert` (3 EPUBs). Both on PATH. **No OCR. No new dependencies.**
- **Read-only on raw/:** sources converted into `01_KNOWLEDGE_BASE/batches/brand_canon_extracted/`. Original files untouched (mtimes unchanged · 2026-05-13).
- **Script:** `scripts/extract_brand_canon.py` (refuses to overwrite; fails on missing source).
- **Source set:** the 5 net-new brand-strategy books (decision-neutral lane · operator-locked). SNIPED-authored brand docs HELD; fashion_luxury a separate future lane; StoryBrand/Alchemy/Status and Culture already canonical (excluded).
- A benign `Syntax Warning: Invalid Font Weight` appeared from `pdftotext` on Designing Brand Identity; word count confirms full text extracted.

## Sources extracted (5 of 5 · 0 failures)

| source_file | source_title | author | format | words |
|---|---|---|---|--:|
| `the_brand_gap_neumeier.txt` | The Brand Gap | Marty Neumeier | pdf | 22,630 |
| `designing_brand_identity_wheeler.txt` | Designing Brand Identity | Alina Wheeler and Rob Meyerson | pdf | 97,191 |
| `identity_designed_airey.txt` | Identity Designed | David Airey | epub | 55,889 |
| `brand_naming_meyerson.txt` | Brand Naming | Rob Meyerson | epub | 43,009 |
| `hello_my_name_is_awesome_watkins.txt` | Hello, My Name Is Awesome | Alexandra Watkins | epub | 23,925 |

Combined: ~242,644 words. Content sampled per file to confirm real book text.

## Excluded / held / deferred

- **SNIPED-authored brand docs** (BRAND_STRATEGY_2026-05-13 set + Brand_Builders_Playbook.docx + branding x clothes gold.docx + Build a Brand Like Apple.docx): HELD until the fresh SNIPED brief · NOT extracted.
- **fashion_luxury folder** (The Luxury Strategy + fashion histories/memoirs): separate future FASHION_LUXURY lane · NOT extracted.
- **Building a StoryBrand, Alchemy** (already BATCH_009), **Status and Culture** (already CULTURE_AND_STATUS), the 13 already-canonical sales_positioning titles: NOT re-extracted.
- **The KJV Bible:** held SPIRITUAL_FOUNDATION anchor · NOT touched/staged/extracted.

## Notes

- No `raw/` mutation, no OCR, no installs, no master-file writes during extraction.
- The naming books (Meyerson, Watkins) are held as naming-craft only · NOT a directive to finalize a SNIPED, SNIPED Media, or BASEPLATE name.
