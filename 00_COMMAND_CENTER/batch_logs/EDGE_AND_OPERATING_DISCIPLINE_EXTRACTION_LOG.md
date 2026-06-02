# EDGE_AND_OPERATING_DISCIPLINE extraction log · 2026-05-23

## Method

- 3 pdf worksheets via `pdftotext -layout`.
- Keyword-substring matching on filenames in `scripts/extract_edge_and_operating_discipline.py`.
- NO OCR. NO new dependencies. raw/ not modified. Refuses to overwrite an existing extracted file.

## Sources extracted (3 of 3 · 0 failures)

| Output file | Source (raw/13_OPERATING_DISCIPLINE/) | Type | Words |
|---|---|---|---:|
| `icp_definition_worksheet.txt` | ICP Definition Worksheet.pdf | pdf | 2,614 |
| `setting_goals.txt` | Setting Goals.pdf | pdf | 1,264 |
| `weekly_reflections.txt` | Weekly Reflections.pdf | pdf | 1,399 |

Total: 5,277 words (INTERNAL chunk-authoring reference only).

## Notes

- All three extracted cleanly · word counts match the plan's pre-flight peek · NOT scanned (real text layer) · no OCR needed.
- All three are generic operating-discipline frameworks from "The AI Edge" course family (© The AI Edge / Agera Management LTD). They are blank/method worksheets, not SNIPED-filled, so no stale SNIPED/BASEPLATE assumptions were carried in.
- Extracted files live under `01_KNOWLEDGE_BASE/batches/edge_and_operating_discipline_extracted/`.
