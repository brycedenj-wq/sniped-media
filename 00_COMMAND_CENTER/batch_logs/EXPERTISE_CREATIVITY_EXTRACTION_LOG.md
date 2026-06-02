# EXPERTISE_CREATIVITY extraction log · 2026-05-26

## Tooling

- `pdftotext` (pdf), `ebook-convert` / calibre (epub). Both on PATH. No OCR. No new dependencies installed.
- Script: `scripts/extract_expertise_creativity.py` (read-only on `raw/`; refuses to overwrite existing extracted files).
- Output dir: `01_KNOWLEDGE_BASE/batches/expertise_creativity_extracted/`.

## Sources extracted (4 of 4 · 0 failures)

| Source | Author | Method | Extracted file | Words |
|---|---|---|---|--:|
| Ways of Seeing | John Berger | ebook-convert (epub) | `ways_of_seeing_berger.txt` | 22,532 |
| The Creative Act | Rick Rubin | ebook-convert (epub) | `the_creative_act_rubin.txt` | 47,357 |
| Peak | Anders Ericsson & Robert Pool | ebook-convert (epub) | `peak_ericsson_pool.txt` | 110,138 |
| Talent Is Overrated | Geoff Colvin | pdftotext (pdf) | `talent_is_overrated_colvin.txt` | 74,216 |

`SOURCES IN: 4 · EXTRACTED OUT: 4 · FAILURES: 0`. Total ~254,243 words. Word counts match the ADJACENT_TIER_2_CLUSTERS_PLAN read-only probe. Ways of Seeing is a short, heavily-illustrated essay (22,532 words is the real text).

## Excluded broken / image-only sources (NOT extracted)

- **Dieter Rams: As Little Design as Possible (Lovell):** 73 MB image-heavy design monograph · 0 extractable text · excluded (untouched in raw/, mtime unchanged).
- **Creativity (Csikszentmihalyi):** `.djvu` (unsupported format, no djvutxt) · 0 text · excluded (untouched in raw/) · re-acquire a clean epub for any future pass.

## Notes

- `pdftotext` emitted benign font/dictionary parser warnings on the Colvin PDF (suppressed); these are harmless stderr notes, NOT OCR and NOT extraction failures. All four files extracted full, clean book text (sampled to confirm real prose).

## Integrity

- raw/ source files NOT modified (mtimes unchanged · 2026-05-15 to 2026-05-18 · the Dieter Rams + Csikszentmihalyi files untouched).
- No OCR. No new dependencies. No `pip`/`brew`/`apt` installs.
- The consulting_service / leadership_mgmt / systems_thinking folders were NOT extracted (CONSULTING_SERVICE + LEADERSHIP_MGMT + SYSTEMS_THINKING already canonical).
- The Death by Meeting summary stub and the 15 MB McLuhan duplicate twin were NOT extracted.
- The KJV Bible was NOT touched, staged, or extracted (not present in raw/).
- CURRENT_IDENTITY_AND_BRAND_OPTIONALITY and the SNIPED-authored brand docs were NOT extracted.

## Next step

Chunking is a separate step. See `scripts/write_expertise_creativity_chunks.py` -> `EXPERTISE_CREATIVITY_CHUNKS.jsonl` (11 chunks · validated). Master-consolidation awaits separate operator authorization.
