# BATCH_009_EXPANSION source index · 2026-05-23

5 source files · 22 chunks · batch_id `BATCH_009_EXPANSION`. NO NEW domain. The 2 synthesis chunks (021-022) cite a representative book file per the prior-batch convention. All sources from `raw/02_TIER_1_CANON_BOOKS/sales_positioning/`.

## Sources

| # | Extracted file | Author · Title | Source content chunks | Original source |
|--:|---|---|---|---|
| 1 | `never_split_the_difference_voss.txt` | Chris Voss & Tahl Raz · Never Split the Difference (2016) | 001-004 (4) | `Raz, Tahl_Voss, Chris - Never Split the Difference_ ... (2016, HarperBusiness) - libgen.li.epub` |
| 2 | `eating_the_big_fish_morgan.txt` | Adam Morgan · Eating the Big Fish (2009) | 005-008 (4) | ` Adam Morgan - Eating the Big Fish_ How Challenger Brands Can Compete Against Brand Leaders (2009) - libgen.li.pdf` |
| 3 | `play_bigger_ramadan_lochhead.txt` | Ramadan/Peterson/Lochhead/Maney · Play Bigger (2016) | 009-013 (5) + 022 synthesis | `Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney - Play Bigger_ ... (2016, HarperBusiness) - libgen.li.epub` |
| 4 | `tribes_godin.txt` | Seth Godin · Tribes (2008) | 014-016 (3) | `Seth Godin - Tribes_ We Need You to Lead Us (2008, Penguin) - libgen.li.epub` |
| 5 | `competing_against_luck_christensen.txt` | Christensen/Dillon/Hall/Duncan · Competing Against Luck (2016) | 017-020 (4) + 021 synthesis | ` Christensen, Clayton M. & Dillon, Karen & Hall, Taddy & Duncan, - Competing Against Luck_ ... (2016) - libgen.li.epub` |

Extracted via stdlib zipfile + HTML-strip (epub) and pdftotext -layout (pdf) · no OCR · no new dependencies · 404,437 words total (INTERNAL chunk-authoring reference only).

## Net-new confirmation

All five verified net-new: 0 source-refs across all `*_CHUNKS.jsonl` for every title/author. The lone "Seth Godin" hits are This Is Marketing + Purple Cow (BATCH_009) and The Dip (BATCH_003); Tribes itself is 0 everywhere.

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source |
|---|---|---|---|
| 001 | Tactical empathy: name and understand the other side's emotions | sales-flow | voss |
| 002 | Mirroring, labeling, and the accusation audit | sales-flow | voss |
| 003 | 'No' is protection; 'That's right' is the breakthrough | brand-psychology | voss |
| 004 | Calibrated questions, Ackerman bargaining, and Black Swans | sales-flow | voss |
| 005 | The Challenger mindset: ideas-led, not budget-led | positioning | morgan |
| 006 | Lighthouse Identity: project who you are and draw people to you | brand | morgan |
| 007 | Sacrifice and Overcommitment: concentrate force | strategy | morgan |
| 008 | Intelligent Naivety and Thought Leadership of the consumer | brand-psychology | morgan |
| 009 | Category design and the category king's economics | commercial-architecture | play-bigger |
| 010 | Point of View: frame a problem the world doesn't yet name | positioning | play-bigger |
| 011 | The Magic Triangle: co-design product, company, and category | systems-thinking | play-bigger |
| 012 | The Lightning Strike: a concentrated blitz that conditions the market | content-strategy | play-bigger |
| 013 | Conditioning the market and becoming the category king | strategy | play-bigger |
| 014 | A tribe needs a shared interest and a way to communicate | brand-psychology | godin |
| 015 | Leadership is not management; heretics challenge the status quo | operator-process | godin |
| 016 | Lead the smallest viable tribe and give them tools to connect | content-strategy | godin |
| 017 | Jobs to Be Done: customers hire products to make progress | strategy | christensen |
| 018 | Every job has functional, social, and emotional dimensions | brand-psychology | christensen |
| 019 | Demand-side thinking: circumstance over customer attributes | client-application | christensen |
| 020 | Integrate experiences and the organisation around the job | offer-design | christensen |
| 021 | SYNTHESIS: the commercial-strategy stack as a sequence of lenses | strategy | christensen (synthesis) |
| 022 | SYNTHESIS: option-generators, not a mandate; preserve optionality | systems-thinking | play-bigger (synthesis) |

## Domain distribution (NO NEW domain · 11 approved domains only)

brand-psychology 4 · strategy 4 · sales-flow 3 · positioning 2 · systems-thinking 2 · content-strategy 2 · brand 1 · commercial-architecture 1 · operator-process 1 · client-application 1 · offer-design 1 = 22.

## Identity optionality guardrail

All 22 chunks carry the guardrail in `sniped_relevance`: this lane does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction. Category design (Play Bigger) and challenger positioning (Morgan) are recorded as decision-support lenses / option-generators, with the explicit note that direction is undecided and photography remains one option among several.

## Cross-batch reinforcement summary

| Chunk(s) | Link |
|---|---|
| 001-004 negotiation | BATCH_009 sales-flow + intel_trust_equation (low self-orientation) + B2B_POSITIONING discovery |
| 005-008 challenger | BATCH_009 positioning (Trout/Dunford) + intel_company_of_one (constraint as strategy) |
| 009-013 category design | BATCH_009 offers (Hormozi) + commercial-architecture + future SNIPED category decision (held) |
| 014-016 tribe | CULTURE_AND_STATUS (belonging/status) + feedback_scene_density_thinking (depth over breadth) |
| 017-020 JTBD | OPPORTUNITY_MANAGEMENT_TEMPLATES (qualification) + offer-design + BATCH_009 StoryBrand |
| 021-022 synthesis | CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails (decision-support, optionality preserved) |

## Copyright-safe quote discipline

All five are in-copyright trade books. `direct_quotes` are SHORT illustrative lines only (longest 14 words). 5 of 22 chunks carry a quote; 17 paraphrase. Extracted full text is internal reference.

## Excluded material (NOT chunked)

| Material | Reason |
|---|---|
| BATCH_009 core sources | Already canonical · 0 chunks |
| BATCH_010 / CULTURE_AND_STATUS sources | Out of scope · 0 chunks |
| recovery/acquisition items | Out of scope · 0 chunks |
| CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources | Out of scope · 0 chunks |
| any other sales_positioning files | Out of scope · only the 5 expansion books |
