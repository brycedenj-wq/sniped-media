# STORYTELLING_NARRATIVE extraction log · 2026-05-25

## Method

- **Tooling:** `pdftotext` (3 PDFs) + `ebook-convert` (1 EPUB). Both on PATH. **No OCR. No new dependencies.**
- **Read-only on raw/:** sources converted into `01_KNOWLEDGE_BASE/batches/storytelling_narrative_extracted/`. Original files untouched (mtimes unchanged · 2026-05-16 / 2026-04-26).
- **Script:** `scripts/extract_storytelling_narrative.py` (refuses to overwrite; fails on missing source).
- **Source set:** Option 2 (operator-locked) · 4 clean sources. Story/McKee excluded (broken/scanned · 0 words · no OCR).

## Sources extracted (4 of 4 · 0 failures)

| source_file | source_title | author | format | words |
|---|---|---|---|--:|
| `anatomy_of_story_truby.txt` | The Anatomy of Story | John Truby | pdf | 126,225 |
| `hero_with_a_thousand_faces_campbell.txt` | The Hero with a Thousand Faces | Joseph Campbell | epub | 142,097 |
| `save_the_cat_snyder.txt` | Save the Cat! | Blake Snyder | pdf | 59,787 |
| `visual_story_block.txt` | The Visual Story | Bruce Block | pdf | 61,118 |

Combined: ~389,227 words. Content sampled per file to confirm real book text (not scanned/garbage).

## Excluded / deferred

- **Story (Robert McKee):** 56MB pdf · `pdftotext` = 0 words (scanned/image-only) · **DEFER · re-acquire clean text · NO OCR.**
- **Building a StoryBrand (Miller):** already canonical (BATCH_009) · NOT re-extracted.
- **life story.docx:** personal note · out-of-scope · NOT extracted.
- **The KJV Bible:** held SPIRITUAL_FOUNDATION anchor · NOT touched/staged/extracted.

## Notes

- The "19 pages" / "6 pages" metadata on some PDFs is a container quirk; word counts confirm full text extracted.
- Block's `The Visual Story` sits at `raw/` top-level (leading space in filename); path quoted in the extract script.
- No `raw/` mutation, no OCR, no installs, no master-file writes during extraction.
