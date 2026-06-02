# FASHION_LUXURY_CULTURE source index · 2026-05-26

batch_id `FASHION_LUXURY_CULTURE` · 13 chunks · 4 sources · `aesthetics` anchor · NO new domain. The fashion-history / memoir / taste / craft register (the SECOND split FASHION_LUXURY sub-lane). Read decision-neutrally. `taste` reused (warranted · not created).

## Sources and chunk attribution

| # | source_title | author | source_file | format | words | chunks | chunk_ids |
|---|---|---|---|---|--:|--:|---|
| 1 | The Beautiful Fall | Alicia Drake | `the_beautiful_fall_drake.txt` | mobi | 169,922 | 4 | 001-004 |
| 2 | The Chiffon Trenches | Andre Leon Talley | `the_chiffon_trenches_talley.txt` | epub | 87,847 | 3 | 005-007 |
| 3 | Dior by Dior | Christian Dior | `dior_by_dior_dior.txt` | pdf | 73,252 | 4 | 008-010, 013 (synthesis) |
| 4 | The Little Dictionary of Fashion | Christian Dior | `the_little_dictionary_of_fashion_dior.txt` | epub | 18,733 | 2 | 011-012 |

Totals: 4 sources · ~349,754 words extracted · 13 chunks · 1 synthesis (013). Curated, not exhaustive.

## Chunk map (chunk_id · domain · concept)

| chunk_id | source | domain | concept |
|---|---|---|---|
| FASHION_LUXURY_CULTURE_001 | The Beautiful Fall | aesthetics | Aesthetic authority: the implicit standard that disciplines a scene |
| FASHION_LUXURY_CULTURE_002 | The Beautiful Fall | status | The designer-as-star: from dressmaker to symbolic figure |
| FASHION_LUXURY_CULTURE_003 | The Beautiful Fall | founder-psychology | Rivalry and two temperaments: discipline versus torment |
| FASHION_LUXURY_CULTURE_004 | The Beautiful Fall | culture | The scene as a creative resource: density, milieu, and fascination |
| FASHION_LUXURY_CULTURE_005 | The Chiffon Trenches | taste | Taste formation: built from outside through obsessive study |
| FASHION_LUXURY_CULTURE_006 | The Chiffon Trenches | status | Editorial status and access: apprenticing into a closed world |
| FASHION_LUXURY_CULTURE_007 | The Chiffon Trenches | ethics | Loyalty, dignity, and the human cost beneath the glamour |
| FASHION_LUXURY_CULTURE_008 | Dior by Dior | aesthetics | Craft justifies the effect: workmanship beneath the beauty |
| FASHION_LUXURY_CULTURE_009 | Dior by Dior | operator-doctrine | Reconciling personality and discipline; the editing that destroys |
| FASHION_LUXURY_CULTURE_010 | Dior by Dior | strategy | Reading the moment: conviction over the dictates of commerce |
| FASHION_LUXURY_CULTURE_011 | The Little Dictionary of Fashion | taste | Elegance is not money: simplicity, care, and good taste |
| FASHION_LUXURY_CULTURE_012 | The Little Dictionary of Fashion | aesthetics | Quality over quantity and individuality over slavish fashion |
| FASHION_LUXURY_CULTURE_013 | Dior by Dior | operator-doctrine | Synthesis: the fashion/luxury culture and taste-systems toolkit |

## Domain distribution (NO new domain · `aesthetics` anchor · `taste` reused)

| Domain | Chunks |
|---|---:|
| aesthetics (anchor) | 3 |
| status | 2 |
| taste | 2 |
| operator-doctrine | 2 |
| founder-psychology | 1 |
| culture | 1 |
| ethics | 1 |
| strategy | 1 |

8 distinct domains · all pre-existing · `luxury`/`fashion`/`style`/`designer`/`apparel`/`streetwear`/`hype`/`clout`/`lifestyle`/`influencer` NOT used · `brand` and `media-business` available but not used.

## Source provenance (raw/)

All 4 sources live under `raw/03_TIER_2_CANON_BOOKS/fashion_luxury/` (filenames carry a leading space; quoted in the extraction script). Extracted read-only to `01_KNOWLEDGE_BASE/batches/fashion_luxury_culture_extracted/` via `pdftotext` (pdf) and `ebook-convert` (epub/mobi). No OCR. No new dependencies. raw/ mtimes unchanged (2026-05-17).

## Cross-references

- **FASHION_LUXURY_STRATEGY (sibling · canonical):** The Luxury Strategy / Deluxe / The End of Fashion · the luxury-strategy / commercial register this lane complements.
- **CULTURE_AND_STATUS (Status and Culture / Marx + The Status Game / Storr):** the status/taste theory this lane's lived culture applies.
- **FOUNDER_FASHION_RECOVERY (Grace / Coddington) + BIOGRAPHY_FOUNDER_MEDIA (Vreeland):** the fashion-memoir / taste-maker register this lane extends (Talley apprenticed under Vreeland).
- **BRAND_CANON:** the general brand-strategy / identity layer.
- **BATCH_005 (Abloh public lecture · photography/aesthetics canon):** the contemporary fashion/aesthetics bridge (Abloh already represented there; the Abloh article excluded here).
- **CURRENT_OPERATOR_REALITY_BRIEF + CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** the optionality guardrails and current-state anchor governing this lane (the SNIPED-authored brand docs remain held).
