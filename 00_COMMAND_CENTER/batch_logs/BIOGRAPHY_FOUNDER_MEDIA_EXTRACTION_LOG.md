# BIOGRAPHY_FOUNDER_MEDIA extraction log · 2026-05-23

## Method

- 5 epub via Python stdlib `zipfile` + spine-ordered (OPF) HTML-strip · 1 pdf (Made in Japan) via `pdftotext -layout`.
- Keyword-substring matching on filenames in `scripts/extract_biography_founder_media.py`.
- NO OCR. NO new dependencies (no mobi in CORE, so ebook-convert not needed). raw/ not modified. Refuses to overwrite an existing extracted file.

## Sources extracted (6 of 6 CORE · 0 failures)

| Output file | Author · Subject | Type | Words |
|---|---|---|---:|
| `dv_vreeland.txt` | Diana Vreeland · D.V. (Vogue/Bazaar editor · taste-making) | epub | 65,693 |
| `no_filter_instagram_frier.txt` | Sarah Frier · No Filter (Instagram) | epub | 115,806 |
| `losing_my_virginity_branson.txt` | Richard Branson · Virgin | epub | 181,881 |
| `grinding_it_out_kroc.txt` | Ray Kroc · McDonald's | epub | 70,620 |
| `that_will_never_work_randolph.txt` | Marc Randolph · Netflix | epub | 102,037 |
| `made_in_japan_morita.txt` | Akio Morita · Sony | pdf | 135,753 |

Total: 671,790 words (INTERNAL chunk-authoring reference only).

## Notes

- All six extracted cleanly · word counts match the plan's pre-flight peek · no scanned/stub files among the CORE (Made in Japan is a 34MB pdf with a real text layer, not a scan).
- All in-copyright trade books; extracted full text is internal reference only.
- Files live under `01_KNOWLEDGE_BASE/batches/biography_founder_media_extracted/`.
- Excluded per plan (0 extraction): founder second tier (Super Pumped, Airbnb, Sam Walton, Elon Musk, Schultz x2, Titan, Banana King), media-business cluster (ESPN, SNL, Tinderbox), Chernow histories (Grant, Washington), broken/recovery (Hit Men scanned, Grace 0-byte stub, Total Recall 0-byte stub, The Mailroom djvu), recovery/acquisition items, CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources, any other memoirs_biographies files.
