# CONSULTING_SERVICE extraction log · 2026-05-26

## Tooling

- `pdftotext` (pdf) and `ebook-convert` / calibre (epub). Both on PATH. No OCR. No new dependencies installed.
- Script: `scripts/extract_consulting_service.py` (read-only on `raw/`; refuses to overwrite existing extracted files).
- Output dir: `01_KNOWLEDGE_BASE/batches/consulting_service_extracted/`.

## Sources extracted (7 of 7 · 0 failures)

| Source | Author | Method | Extracted file | Words |
|---|---|---|---|--:|
| Value-Based Fees | Alan Weiss | pdftotext (pdf) | `value_based_fees_weiss.txt` | 81,605 |
| Million Dollar Consulting | Alan Weiss | pdftotext (pdf) | `million_dollar_consulting_weiss.txt` | 143,350 |
| The McKinsey Way | Ethan M. Rasiel | pdftotext (pdf) | `the_mckinsey_way_rasiel.txt` | 42,414 |
| Managing the Professional Service Firm | David H. Maister | pdftotext (pdf) | `managing_the_professional_service_firm_maister.txt` | 126,173 |
| Getting Naked | Patrick Lencioni | pdftotext (pdf) | `getting_naked_lencioni.txt` | 47,421 |
| The Advantage | Patrick Lencioni | pdftotext (pdf) | `the_advantage_lencioni.txt` | 58,648 |
| Flawless Consulting | Peter Block | ebook-convert (epub) | `flawless_consulting_block.txt` | 107,028 |

`SOURCES IN: 7 · EXTRACTED OUT: 7 · FAILURES: 0`. Total ~606,639 words. Word counts match the ADJACENT_TIER_2_CLUSTERS_PLAN read-only probe exactly.

## Notes

- `pdftotext` emitted benign `Syntax Warning: Invalid Font Weight` and a few `Dictionary key must be a name object` parser warnings on the older PDFs; these are harmless font/dictionary structure notes on stderr, NOT OCR and NOT extraction failures. All seven files extracted full, clean book text (sampled to confirm real prose).
- The Lencioni *Getting Naked* and *The Advantage* are the two clean full PDFs in `consulting_service/`; the separate *Death by Meeting* `.txt` in `leadership_mgmt/` is a ~1,131-word third-party summary stub and was NOT extracted (out of scope for this lane and a stub regardless).

## Integrity

- raw/ source files NOT modified (mtimes unchanged · 2026-05-18).
- No OCR. No new dependencies. No `pip`/`brew`/`apt` installs.
- The leadership_mgmt / systems_thinking / expertise_creativity folders were NOT extracted (their own deferred lanes).
- The Death by Meeting summary stub, the Dieter Rams image-only monograph, the Csikszentmihalyi `.djvu`, and the McLuhan duplicate twin were NOT extracted.
- The KJV Bible was NOT touched, staged, or extracted (not present in raw/).
- CURRENT_IDENTITY_AND_BRAND_OPTIONALITY and the SNIPED-authored brand docs were NOT extracted.

## Next step

Chunking is a separate step. See `scripts/write_consulting_service_chunks.py` -> `CONSULTING_SERVICE_CHUNKS.jsonl` (15 chunks · validated). Master-consolidation awaits separate operator authorization.
