# MEDIA_BUSINESS extraction log · 2026-05-23

## Method

- 2 epub via Python stdlib `zipfile` + spine-ordered (OPF) HTML-strip · 1 mobi (Tinderbox) via `ebook-convert` (calibre · already on PATH · not a new dependency).
- Keyword-substring matching on filenames in `scripts/extract_media_business.py`.
- NO OCR. NO new dependencies. raw/ not modified. Refuses to overwrite an existing extracted file.

## Sources extracted (3 of 3 CORE · 0 failures)

| Output file | Subject | Type | Words |
|---|---|---|---:|
| `those_guys_espn.txt` | ESPN · the network's oral history | epub | 308,249 |
| `live_from_new_york_snl.txt` | SNL · uncensored oral history | epub | 234,078 |
| `tinderbox_hbo.txt` | HBO · the channel's rise (ebook-convert from mobi) | mobi | 426,623 |

Total: 968,950 words (INTERNAL chunk-authoring reference only).

## Notes

- All three extracted cleanly · ESPN/SNL real epub text; Tinderbox converted from mobi via ebook-convert (calibre).
- All three are in-copyright trade-book oral histories; extracted full text is internal reference only.
- Files live under `01_KNOWLEDGE_BASE/batches/media_business_extracted/`.
- Excluded per plan (0 extraction): Hit Men (scanned · recovery), The Mailroom (`.djvu` · recovery), BIOGRAPHY_FOUNDER_MEDIA core, BATCH_010 culture sources, CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources, recovery/acquisition items, any other memoirs_biographies files.
