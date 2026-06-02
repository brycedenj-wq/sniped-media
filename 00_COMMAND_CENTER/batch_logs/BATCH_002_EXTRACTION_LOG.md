# BATCH_002_TIER_1_CANON_BOOKS · Extraction Log

**Date:** 2026-05-16
**Source:** `raw/02_TIER_1_CANON_BOOKS/` (20 files, 1 of which was an in-flight replacement of a corrupted scanned PDF with a clean EPUB)
**Destination:** `01_KNOWLEDGE_BASE/batches/batch_002_extracted/`

## Tooling installed for this batch

| Tool | Version path | Purpose |
|------|----|---------|
| pandoc | `/opt/homebrew/bin/pandoc` (3.9.0.2) | epub → markdown |
| pdftotext | `/opt/homebrew/bin/pdftotext` (poppler 26.04.0) | pdf → text |
| ebook-convert | `/opt/homebrew/bin/ebook-convert` (Calibre 9.8.0) | mobi → text + epub fallback |
| textutil | `/usr/bin/textutil` (macOS native) | docx → text |

Installed via single command: `brew install pandoc poppler calibre`.

## Outcome

- **Files successfully extracted:** 19
- **Files failed:** 0
- **Files skipped as duplicates:** 1 (Hit Makers epub · byte-identical to existing copy at `raw/` root, md5 `29a7347d955bdb80...`, already covered in BATCH_001 via `STRATEGIC_PRINCIPLES.md`)
- **Files deferred:** 0
- **OCR required:** 0
- **Total extracted text:** 15.12 MB across 17 markdown + 2 text files

## Per-file results

| # | Source filename (in `raw/02_TIER_1_CANON_BOOKS/`) | Output | Size | Method | Notes |
|--:|----------------------------------------------------|--------|-----:|--------|-------|
| 1 | `Andrew Chen - The Cold Start Problem...epub` | `cold_start_problem_chen.md` | 678 KB | pandoc | clean |
| 2 | `Brad Stone - The Everything Store...epub` | `everything_store_bezos_stone.md` | 737 KB | pandoc | clean |
| 3a | `Charles T. Munger - Poor Charlie's Almanack...PDF` (184 MB) | _replaced_ | — | — | **Original 184 MB scanned PDF replaced mid-batch with clean EPUB version (item 3b). 5-page pdftotext sample (`poor_charlies_almanack_munger_SAMPLE5.txt`) returned garbled text confirming image-PDF without usable text layer. Sample file removed after EPUB extraction succeeded.** |
| 3b | `Charles T. Munger - Poor Charlie's Almanack...epub` | `poor_charlies_almanack_munger.md` | 900 KB | pandoc | clean · contains the Eleven Talks (incl. Psychology of Human Misjudgment), Mungerisms, Portrait by Broggie |
| 4 | `Colin Bryar, Bill Carr - Working Backwards...epub` | `working_backwards_bryar_carr.md` | 614 KB | pandoc | clean |
| 5 | `Derek Thompson - Hit Makers...epub` | — | — | **SKIP-DUP** | byte-identical to `raw/Derek Thompson - Hit Makers...epub` (md5 `29a7347d955bdb80...`). Already synthesized in BATCH_001. |
| 6 | `Ed Catmull, Amy Wallace - Creativity, Inc...epub` | `creativity_inc_catmull.md` | 648 KB | pandoc | clean |
| 7 | `Jack Weatherford - Genghis Khan...epub` | `genghis_khan_weatherford.md` | 813 KB | pandoc | clean |
| 8 | `James B. Stewart - DisneyWar...epub` | `disneywar_stewart.md` | 1.4 MB | pandoc | clean |
| 9 | `John Seabrook - The Song Machine...epub` | `song_machine_seabrook.md` | 624 KB | pandoc | clean |
| 10 | `Peter Thiel, Blake Masters - Zero to One...epub` | `zero_to_one_thiel.md` | 374 KB | pandoc | clean |
| 11 | `Phil knight - Shoe dog...mobi` | `shoe_dog_knight.txt` | 679 KB | ebook-convert (Calibre) | clean · Scribner publisher front-matter preserved as source evidence |
| 12 | `Robert Iger - The Ride of a Lifetime...epub` | `ride_of_a_lifetime_iger.md` | 501 KB | pandoc | clean |
| 13 | `Stoute, Steve - The Tanning of America...epub` | `tanning_of_america_stoute.md` | 659 KB | pandoc | clean |
| 14 | `Walter Isaacson - Steve Jobs...epub` | `steve_jobs_isaacson.md` | 1.4 MB | pandoc | clean |
| 15 | `William N. Thorndike - The Outsiders...epub` | `outsiders_thorndike.md` | 610 KB | pandoc | clean |
| 16 | `[Alexander the Great 1] Freeman - Alexander the Great...epub` | `alexander_the_great_freeman.md` | 1.0 MB | pandoc | clean |
| 17 | `[Baker & Taylor] Robert Greene - The 48 Laws of Power...epub` | `48_laws_of_power_greene.md` | 1.3 MB | pandoc | clean |
| 18 | `[Joost Elffers Books] Greene - The 33 Strategies of War...epub` | `33_strategies_of_war_greene.md` | 1.6 MB | pandoc | clean |
| 19 | `ArtOfWar.pdf` | `art_of_war_sun_tzu.txt` | 347 KB → **345 KB after cleanup** | pdftotext + page-header cleanup | 113 page-header lines removed (e.g. `CHAPTER 1. INTRODUCTION   6` repeating across pages, `CONTENTS  2`, `BIBLIOGRAPHY  27`). See cleanup section below. |
| 20 | `mostly Powerhouse-.docx` | `stoute_powerhouse_talk.txt` | 420 KB | textutil | clean · Steve Stoute talk transcript at Silicon Valley event on cultural capital as creator of financial capital. YouTube-style timestamps (`0:01`, `0:09`, etc) preserved as source content (transcript artifact, not page header). |

## Cleanup applied

Only ONE file required cleanup. All others extracted clean.

### `art_of_war_sun_tzu.txt` — page-header removal

Source format was a Project Gutenberg LaTeX-rendered PDF that included recurring chapter-name running headers on every page. `pdftotext -layout` captures these as separate lines mid-document.

**Pattern removed (113 lines total):**
```
^[\s]*([A-Z][A-Z .,0-9]{4,40}?)[\s]{4,}([0-9]{1,4})[\s]*$
```
Match list:
- `CHAPTER 1. INTRODUCTION   N` × 20
- `CHAPTER 12. THE NINE SITUATIONS   N` × 21
- `CHAPTER 10. THE ARMY ON THE MARCH   N` × 10
- `CHAPTER 8. MANEUVERING   N` × 8
- `CHAPTER 14. THE USE OF SPIES   N` × 8
- `CHAPTER 11. TERRAIN   N` × 6
- `CHAPTER 7. WEAK POINTS AND STRONG   N` × 6
- `CHAPTER 4. ATTACK BY STRATAGEM   N` × 5
- `CHAPTER 6. ENERGY   N` × 5
- `CHAPTER 9. VARIATION IN TACTICS   N` × 5
- `CHAPTER 13. THE ATTACK BY FIRE   N` × 5
- `CHAPTER 2. LAYING PLANS` × 3, `CHAPTER 3. WAGING WAR` × 3, `CHAPTER 5. TACTICAL DISPOSITIONS` × 3, `CONTENTS` × 3
- `BIBLIOGRAPHY` × 2

After removal: 3+ consecutive blank lines collapsed to 2 to avoid large gaps where page headers were stripped.

No real chapter heading lines were lost (each true heading appears once and is followed by content; the matched lines are all page-top running headers with trailing page numbers).

## Decisions and notes

1. **Munger PDF mid-batch swap** — original 184 MB scanned PDF was replaced by user with a 1.4 MB clean EPUB version during this batch. The corrupted sample file (`poor_charlies_almanack_munger_SAMPLE5.txt`) was removed after the EPUB version extracted cleanly. The EPUB version is now the canonical Munger source. The original PDF is no longer in the source folder.
2. **Hit Makers duplicate** — confirmed via md5 against existing `raw/Derek Thompson - Hit Makers...epub`. Skipped without extraction. Canonical = the root-level copy; the BATCH_002 copy is structurally redundant. Recommend the user delete the BATCH_002 copy from `raw/02_TIER_1_CANON_BOOKS/` to prevent re-processing.
3. **Stoute transcript timestamps** — `0:01`, `0:09`, `Run DMC My Adidas` etc. in `stoute_powerhouse_talk.txt` are part of the YouTube-auto-generated transcript structure, not page-header artifacts. Preserved as content. `[ __ ]` markers are YouTube's auto-censored word filter, also preserved.
4. **Shoe Dog Scribner front-matter** — first ~15 lines are publisher boilerplate ("Thank you for downloading this Scribner eBook"). Preserved as source-traceable evidence; downstream chunking will skip it naturally.
5. **Pandoc anchor artifacts** — EPUB→markdown output includes `[]{#fragment-id}` navigation anchors and `{.calibre1}` style markers. These are noise but preserve source-traceability (each anchor maps back to a specific EPUB internal location). Preserved as-is. Downstream chunkers should strip via regex if a clean prose output is needed.

## Files in `01_KNOWLEDGE_BASE/batches/batch_002_extracted/` (final)

```
   1,639,589  33_strategies_of_war_greene.md
   1,379,366  48_laws_of_power_greene.md
   1,070,635  alexander_the_great_freeman.md
     344,993  art_of_war_sun_tzu.txt           (cleaned · 113 headers removed)
     694,191  cold_start_problem_chen.md
     663,974  creativity_inc_catmull.md
   1,455,576  disneywar_stewart.md
     754,297  everything_store_bezos_stone.md
     832,617  genghis_khan_weatherford.md
     624,844  outsiders_thorndike.md
     921,622  poor_charlies_almanack_munger.md  (from EPUB replacement, not the scanned PDF)
     513,459  ride_of_a_lifetime_iger.md
     695,690  shoe_dog_knight.txt
     639,093  song_machine_seabrook.md
   1,508,532  steve_jobs_isaacson.md
     430,500  stoute_powerhouse_talk.txt
     674,862  tanning_of_america_stoute.md
     628,854  working_backwards_bryar_carr.md
     383,087  zero_to_one_thiel.md
```

**Total: 19 files · 15.12 MB extracted text · 0 failures · 1 skipped duplicate · 0 deferred · 0 OCR needed.**

## Next step

The extraction phase is complete. Ready for downstream chunking. The 15 MB of canon text is well outside single-pass chunking budget; recommend splitting BATCH_002 chunking into per-cluster sub-batches by theme, e.g.:

- **Operator memoirs** · Isaacson, Iger, Knight, Stoute (Tanning), Catmull, Bryar/Carr
- **Strategy canon** · Sun Tzu, Greene (×2), Weatherford, Freeman/Alexander, Thorndike
- **Network + distribution mechanics** · Chen (Cold Start), Seabrook (Song Machine), Thiel (Zero to One)
- **Org / culture** · Stone (Everything Store), Stewart (DisneyWar), Stoute (Powerhouse talk)
- **Wisdom layer** · Munger Almanack (especially Psychology of Human Misjudgment)

Each sub-batch processed independently → its own chunks file → merged at the end into a single `BATCH_002_CHUNKS.jsonl`.
