# PERSUASION_RECOVERY extraction log · 2026-05-24

## Source

| source_file | source_title | author | format | path in raw/ | words |
|---|---|---|---|---|--:|
| `predictably_irrational_ariely.txt` | Predictably Irrational: The Hidden Forces That Shape Our Decisions (Revised and Expanded Edition) | Dan Ariely | epub (recovered) | `raw/03_TIER_2_CANON_BOOKS/persuasion_psych/Dan Ariely - Predictably Irrational, Revised and Expanded Edition_ The Hidden Forces That Shape Our Decisions (2009, HarperCollins) - libgen.li_RECOVERED.epub` | 107,956 |

## Method

- **Tool:** `ebook-convert` (calibre · already on PATH). EPUB to plain .txt.
- **No OCR. No new dependencies.** No pip install. The source `.epub` was read-only (not modified).
- **Output:** `01_KNOWLEDGE_BASE/batches/persuasion_recovery_extracted/predictably_irrational_ariely.txt` (647,297 bytes · 107,956 words).
- **Script:** `scripts/extract_persuasion_recovery.py` (refuses to overwrite an existing extracted file; refuses on missing source).

## Excluded (0 chunks · 0 extraction)

- **Old Predictably Irrational `.djvu`** (`...Predictably Irrational_ ... (2010, Harper Perennial) - libgen.li.djvu`): unsupported format (no djvutxt on PATH), superseded by the recovered epub. NOT extracted. Left in place untouched.
- **The KJV Bible:** NOT touched, staged, extracted, or chunked.
- **Every other `persuasion_psych/` and already-canonical source:** NOT extracted (single-source lane).

## Word-count reconciliation

- Plan / intake / staging recorded 107,959 words (ebook-convert default whitespace handling at probe time).
- This extraction produced 107,956 words (a 3-word delta from minor whitespace/line-join differences between the probe and the committed conversion). Same source, same edition; the difference is non-material tokenization noise.

## Result

- Sources in: 1 · extracted out: 1 · failures: 0.
- Ready for chunking (completed in the same ship · see `PERSUASION_RECOVERY_COMPLETE.md`).
