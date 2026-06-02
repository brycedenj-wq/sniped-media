# FOUNDER_SECOND_TIER extraction log · 2026-05-23

## Method

- 2 epub via Python stdlib `zipfile` + spine-ordered (OPF) HTML-strip · 1 pdf via `pdftotext -layout` · 3 mobi via `ebook-convert` (calibre · already on PATH · not a new dependency). (Airbnb + Elon Musk + Super Pumped epub; Sam Walton pdf; Titan + Banana King + Pour Your Heart mobi.)
- Keyword-substring matching on filenames in `scripts/extract_founder_second_tier.py`.
- NO OCR. NO new dependencies. raw/ not modified. Refuses to overwrite an existing extracted file.

## Sources extracted (7 of 7 CORE · 0 failures)

| Output file | Founder · Company | Type | Words |
|---|---|---|---:|
| `sam_walton_made_in_america.txt` | Sam Walton · Walmart | pdf | 96,353 |
| `elon_musk_isaacson.txt` | Musk · Tesla/SpaceX | epub | 204,776 |
| `super_pumped_uber_isaac.txt` | Kalanick · Uber | epub | 125,963 |
| `the_airbnb_story_gallagher.txt` | Chesky · Airbnb | epub | 87,560 |
| `titan_rockefeller_chernow.txt` | Rockefeller · Standard Oil | mobi | 332,866 |
| `the_fish_that_ate_the_whale_cohen.txt` | Zemurray · United Fruit (Banana King) | mobi | 94,096 |
| `pour_your_heart_into_it_schultz.txt` | Schultz · Starbucks (origin) | mobi | 107,337 |

Total: 1,048,951 words (INTERNAL chunk-authoring reference only).

## Notes

- All seven extracted cleanly · the 3 mobi converted via ebook-convert (calibre).
- All in-copyright trade books; extracted full text is internal reference only.
- Files live under `01_KNOWLEDGE_BASE/batches/founder_second_tier_extracted/`.
- Excluded per plan (0 extraction): Onward (Schultz turnaround · deferred), Grant + Washington (Chernow histories · deferred to a historical-biography lane), BIOGRAPHY_FOUNDER_MEDIA core, MEDIA_BUSINESS sources, broken/recovery memoirs (Hit Men, Grace, Total Recall, The Mailroom), CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources, recovery/acquisition items, any other memoirs_biographies files.
