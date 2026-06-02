# FOUNDER_SECOND_TIER source index · 2026-05-23

7 source files · 20 chunks · batch_id `FOUNDER_SECOND_TIER`. NO new domain (anchored on existing `founder-psychology`). The 2 synthesis chunks (019-020) cite a representative source file (Walton, Musk).

## Sources

| # | Extracted file | Founder · Company | Source-content chunks | Original source |
|--:|---|---|---|---|
| 1 | `sam_walton_made_in_america.txt` | Sam Walton · Walmart | 001-003 (3) + 019 synthesis | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/` (pdf) |
| 2 | `elon_musk_isaacson.txt` | Musk · Tesla/SpaceX | 004-006 (3) + 020 synthesis | `.../memoirs_biographies/` (epub) |
| 3 | `super_pumped_uber_isaac.txt` | Kalanick · Uber | 007-009 (3) | `.../memoirs_biographies/` (epub) |
| 4 | `the_airbnb_story_gallagher.txt` | Chesky · Airbnb | 010-011 (2) | `.../memoirs_biographies/` (epub) |
| 5 | `titan_rockefeller_chernow.txt` | Rockefeller · Standard Oil | 012-014 (3) | `.../memoirs_biographies/` (mobi) |
| 6 | `the_fish_that_ate_the_whale_cohen.txt` | Zemurray · United Fruit | 015-016 (2) | `.../memoirs_biographies/` (mobi) |
| 7 | `pour_your_heart_into_it_schultz.txt` | Schultz · Starbucks | 017-018 (2) | `.../memoirs_biographies/` (mobi) |

Extracted via stdlib zipfile (epub) + pdftotext (pdf) + ebook-convert (mobi) · no OCR · no new dependencies · 1,048,951 words total (INTERNAL chunk-authoring reference only).

## Net-new + exclusion confirmation

- All 7 verified net-new (the "Onward" overlap hit was a body-text mention, not a source · Onward itself was deferred).
- Excluded per plan: Onward (Schultz turnaround), Grant + Washington (Chernow histories · historical-biography lane), BIOGRAPHY_FOUNDER_MEDIA core, MEDIA_BUSINESS sources, broken/recovery memoirs (Hit Men, Grace, Total Recall, The Mailroom), CURRENT_IDENTITY sources, recovery items, any other memoirs_biographies files. All contributed 0 chunks.

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source |
|---|---|---|---|
| 001 | Customer obsession and relentless cost discipline | operator-doctrine | walton |
| 002 | Distribution and logistics as the real moat | commercial-architecture | walton |
| 003 | Learn relentlessly and align the associates | operator-process | walton |
| 004 | Mission-driven extreme risk tolerance | founder-psychology | musk |
| 005 | First principles and the machine that builds the machine | systems-thinking | musk |
| 006 | Hardcore intensity and leadership contradictions | founder-psychology | musk |
| 007 | Blitzscale: growth as the only metric | strategy | uber |
| 008 | Operating ahead of the rules | commercial-architecture | uber |
| 009 | The toxic-culture collapse: the dark side of win-at-all-costs | ethics | uber |
| 010 | Manufacturing trust between strangers | systems-thinking | airbnb |
| 011 | Design thinking, the 11-star experience, and belonging | brand | airbnb |
| 012 | Consolidation and capital control: the Standard Oil trust | capital | rockefeller |
| 013 | Efficiency obsession and leverage over suppliers | operator-doctrine | rockefeller |
| 014 | Ruthlessness, monopoly, and the philanthropy that followed | ethics | rockefeller |
| 015 | On-the-ground operator knowledge beats the head office | operator-process | zemurray |
| 016 | United Fruit and the dark geopolitics of power | ethics | zemurray |
| 017 | Brand through experience: the romance and the third place | brand | schultz |
| 018 | Scaling culture: partners, values, and the growth tension | culture | schultz |
| 019 | SYNTHESIS: the scale-operator pattern | founder-psychology | walton (synthesis) |
| 020 | SYNTHESIS: pattern-library only, read against current reality | strategy | musk (synthesis) |

## Domain distribution (NO new domain · anchored on `founder-psychology`)

founder-psychology 3 · ethics 3 · operator-doctrine 2 · commercial-architecture 2 · operator-process 2 · systems-thinking 2 · strategy 2 · brand 2 · capital 1 · culture 1 = 20.

- **NO new domain.** All 10 domains pre-exist. `ethics` (3) carries the dark-side-of-scale chunks (Uber toxic culture, Standard Oil monopoly, United Fruit geopolitics), keeping the patterns honest.
- founder-psychology is the anchor (3 · joint-largest with ethics); the company-building content distributes across operator-doctrine / strategy / commercial-architecture / capital, which is expected for a scale-operator lane.

## Identity optionality guardrail

All 20 chunks carry the guardrail in `sniped_relevance`, read against CURRENT_OPERATOR_REALITY_BRIEF: founder arcs are PATTERN-LIBRARY / decision-support lenses, NOT a directive for BJ to copy any founder or manufacture a myth. This lane does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option among several. Chunk 020 makes the optionality discipline explicit. (Brief referenced in all 20 · no-copy-founder framing in all 20.)

## Cross-batch reinforcement summary

| Chunk(s) | Link |
|---|---|
| 001-003 Walton | EDGE_AND_OPERATING_DISCIPLINE (cost/standards discipline) + operator-process |
| 004-006 Musk | founder-psychology + systems-thinking (the production system) |
| 007-009 Uber | BATCH_009_EXPANSION (blitzscale/category) + ethics (the dark side) |
| 010-011 Airbnb | systems-thinking (trust-engineering) + brand (design/experience · ties to SNIPED craft) |
| 012-014 Rockefeller | MONEY_OWNERSHIP (capital control / consolidation) + ethics |
| 015-016 Zemurray | the on-the-ground operator edge (relevant to BJ's field-operator profile) + ethics |
| 017-018 Schultz | brand-through-experience (SNIPED craft) + culture (scaling values) |
| 019-020 synthesis | CURRENT_OPERATOR_REALITY_BRIEF + CURRENT_IDENTITY_AND_BRAND_OPTIONALITY (pattern-library only) |

## Copyright-safe quote discipline

7 in-copyright trade books · `direct_quotes` are SHORT illustrative lines only (longest 6 words). 4 of 20 chunks carry a quote ("the machine that builds the machine" · "Always Be Hustlin" · "belong anywhere" · "Third Place"); 16 paraphrase. Extracted full text is internal reference.
