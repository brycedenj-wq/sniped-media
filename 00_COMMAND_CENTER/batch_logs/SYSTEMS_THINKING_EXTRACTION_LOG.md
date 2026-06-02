# SYSTEMS_THINKING extraction log · 2026-05-26

## Tooling

- `pdftotext` (pdf), `ebook-convert` / calibre (epub). Both on PATH. No OCR. No new dependencies installed.
- Script: `scripts/extract_systems_thinking.py` (read-only on `raw/`; refuses to overwrite existing extracted files).
- Output dir: `01_KNOWLEDGE_BASE/batches/systems_thinking_extracted/`.

## Sources extracted (4 of 4 · 0 failures)

| Source | Author | Method | Extracted file | Words |
|---|---|---|---|--:|
| The Checklist Manifesto | Atul Gawande | ebook-convert (epub) | `the_checklist_manifesto_gawande.txt` | 56,799 |
| Understanding Media (1994 Lapham/MIT copy) | Marshall McLuhan | pdftotext (pdf) | `understanding_media_mcluhan.txt` | 121,372 |
| Thinking in Systems: A Primer | Donella Meadows | pdftotext (pdf) | `thinking_in_systems_meadows.txt` | 71,197 |
| The Fifth Discipline | Peter M. Senge | pdftotext (pdf) | `the_fifth_discipline_senge.txt` | 142,790 |

`SOURCES IN: 4 · EXTRACTED OUT: 4 · FAILURES: 0`. Total ~392,158 words. Word counts match the ADJACENT_TIER_2_CLUSTERS_PLAN read-only probe.

## Duplicate handling (McLuhan)

The `systems_thinking/` folder holds two copies of *Understanding Media*: the 15 MB 1995 McLuhan PDF (OCR-inflated · 212,931-word extraction with artifacts) and the cleaner 1 MB 1994 Lapham/MIT PDF (121,372 words). **The 1994 1 MB copy was used; the 15 MB 1995 duplicate twin was NOT extracted** (per the plan). The 15 MB file remains untouched in raw/ (mtime unchanged, still ~16 MB).

## Notes

- `pdftotext` emitted benign font/dictionary parser warnings on the older PDFs (suppressed); these are harmless stderr notes, NOT OCR and NOT extraction failures. All four files extracted full, clean book text (sampled to confirm real prose).

## Integrity

- raw/ source files NOT modified (mtimes unchanged · 2026-05-16 to 2026-05-17).
- No OCR. No new dependencies. No `pip`/`brew`/`apt` installs.
- The consulting_service / leadership_mgmt / expertise_creativity folders were NOT extracted (CONSULTING_SERVICE + LEADERSHIP_MGMT already canonical; expertise_creativity deferred).
- The 15 MB McLuhan duplicate twin, the Death by Meeting summary stub, the Dieter Rams image-only monograph, and the Csikszentmihalyi `.djvu` were NOT extracted.
- The KJV Bible was NOT touched, staged, or extracted (not present in raw/).
- CURRENT_IDENTITY_AND_BRAND_OPTIONALITY and the SNIPED-authored brand docs were NOT extracted.

## Next step

Chunking is a separate step. See `scripts/write_systems_thinking_chunks.py` -> `SYSTEMS_THINKING_CHUNKS.jsonl` (12 chunks · validated). Master-consolidation awaits separate operator authorization.
