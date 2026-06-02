# SALES_POSITIONING overlap audit · read-only · 2026-05-25

**Status:** READ-ONLY AUDIT. No extraction into knowledge-base folders, no chunking, no master-file changes, no raw mutation, no Bible touch. This document inventories the `sales_positioning` folder, probes extractability, runs an authoritative already-chunked overlap check against all 34 batch jsonls, classifies each candidate, and recommends an architecture. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `58e0264 save session after NETWORK_DISTRIBUTION consolidation`
- **Working tree:** clean (only this audit file is added after writing it).
- **Total chunks:** 1,665 · 10 numbered batches + 34 mini-batches · 62 official domains (75 combined keys).
- **Recovery program complete; classical block complete; the OPERATING_FOUNDER sequence COMPLETE; NETWORK_DISTRIBUTION complete and canonical.** SALES_POSITIONING is the next lane named in the remaining backlog, gated on this overlap audit (it sits "above" the already-chunked BATCH_009 / BATCH_009_EXPANSION commercial canon, so the audit was required before any plan/ship).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified · 16 files in `raw/02_TIER_1_CANON_BOOKS/sales_positioning/`)

| # | Source | Author | Format | Size | Words (probe) | Extract |
|--:|---|---|---|---|--:|---|
| 1 | Eating the Big Fish | Adam Morgan | pdf | 2.8M | 124,173 | CLEAN |
| 2 | Made to Stick | Chip & Dan Heath | pdf | 922K | 89,852 | CLEAN |
| 3 | Competing Against Luck | Clayton Christensen et al. | epub | 273K | 80,143 | CLEAN |
| 4 | Crossing the Chasm (3rd ed.) | Geoffrey A. Moore | mobi | 632K | 71,724 | CLEAN |
| 5 | Differentiate or Die | Jack Trout, Steve Rivkin | pdf | 1.1M | 63,919 | CLEAN |
| 6 | Play Bigger | Ramadan / Peterson / Lochhead / Maney | epub | 421K | 80,192 | CLEAN |
| 7 | $100M Leads | Alex Hormozi | epub | 16M | 67,559 | CLEAN |
| 8 | $100M Offers | Alex Hormozi | epub | 2.0M | 44,914 | CLEAN |
| 9 | Building a StoryBrand | Donald Miller | mobi | 2.3M | 50,907 | CLEAN |
| 10 | Obviously Awesome | April Dunford | epub | 2.0M | 32,547 | CLEAN |
| 11 | The Mom Test | Rob Fitzpatrick | azw3 | 263K | 30,791 | CLEAN |
| 12 | Never Split the Difference | Chris Voss, Tahl Raz | epub | 456K | 81,884 | CLEAN |
| 13 | Purple Cow | Seth Godin | pdf | 1.8M | 33,712 | CLEAN |
| 14 | This Is Marketing | Seth Godin | pdf | 3.7M | 57,107 | CLEAN |
| 15 | Tribes | Seth Godin | epub | 149K | 31,444 | CLEAN |
| 16 | The Innovator's Dilemma | Clayton M. Christensen | pdf | 3.0M | 80,876 | CLEAN |

Read-only `pdftotext` / `ebook-convert`-to-/tmp probes (temp deleted; all mtimes unchanged). **All 16 extract clean · no broken, stub, or scanned files in the folder · no OCR needed.**

## 2. Authoritative already-chunked overlap check (by `source_title` + `author` + `source_file`, not incidental text mentions · across all 34 batch jsonls)

**13 of 16 are ALREADY CANONICAL** (chunked in BATCH_009 or BATCH_009_EXPANSION):

| Source | Already in | source_title / author (as chunked) |
|---|---|---|
| Eating the Big Fish | BATCH_009_EXPANSION | 'Eating the Big Fish' / Adam Morgan |
| Competing Against Luck | BATCH_009_EXPANSION | 'Competing Against Luck' / Christensen et al. |
| Play Bigger | BATCH_009_EXPANSION | 'Play Bigger' / Ramadan et al. |
| Never Split the Difference | BATCH_009_EXPANSION | 'Never Split the Difference' / Voss & Raz |
| Tribes | BATCH_009_EXPANSION | 'Tribes: We Need You to Lead Us' / Godin |
| Made to Stick | BATCH_009 | 'Made to Stick (2007)' / Heath & Heath |
| Differentiate or Die | BATCH_009 | 'Differentiate or Die (2008)' / Trout & Rivkin |
| $100M Leads | BATCH_009 | '$100M Leads (2023)' / Hormozi |
| $100M Offers | BATCH_009 | '$100M Offers (2021)' / Hormozi |
| Building a StoryBrand | BATCH_009 | 'Building a StoryBrand (2017)' / Miller |
| Obviously Awesome | BATCH_009 | 'Obviously Awesome (2019)' / Dunford |
| Purple Cow | BATCH_009 | 'Purple Cow (2003)' / Godin |
| This Is Marketing | BATCH_009 | 'This Is Marketing (2018)' / Godin |

**3 of 16 are NET-NEW** (0 source hits across all batches · confirmed by distinctive-token search):

| Source | Author | Format | Words | Register |
|---|---|---|--:|---|
| Crossing the Chasm (3rd ed.) | Geoffrey A. Moore | mobi | 71,724 | positioning / go-to-market (the chasm, the bowling alley, the whole product, mainstream-market adoption) |
| The Mom Test | Rob Fitzpatrick | azw3 | 30,791 | customer-discovery method (how to talk to customers, avoid false positives / compliments) |
| The Innovator's Dilemma | Clayton M. Christensen | pdf | 80,876 | disruption strategy (why great firms fail, sustaining vs disruptive innovation) |

Combined net-new: **~183,391 words across 3 books.**

**Note on Christensen:** he appears as an author in the corpus only via **Competing Against Luck** (BATCH_009_EXPANSION · jobs-to-be-done). **The Innovator's Dilemma is a different, net-new title** by the same author. The two are complementary (JTBD demand-side vs disruption supply-side), not duplicative.

**Note on a prior heuristic flag:** ORIGINAL_SOURCE_COMPLETION_AUDIT §5 listed The Mom Test among "titles already chunked under a normalized name / staged elsewhere" as a heuristic *apparent-gap* example. The authoritative source-field check here supersedes that: The Mom Test has **0 chunks as a source** and is genuinely **NET-NEW** (it was staged, never chunked).

## 3. Specific overlap checks the operator requested

- **BATCH_009:** 8 of the 16 are here (Made to Stick, Differentiate or Die, $100M Leads, $100M Offers, Building a StoryBrand, Obviously Awesome, Purple Cow, This Is Marketing) · the copy / offer / positioning / remarkability commercial-voice canon. **None of the 3 net-new sources overlap.**
- **BATCH_009_EXPANSION:** 5 of the 16 are here (Eating the Big Fish, Competing Against Luck, Play Bigger, Never Split the Difference, Tribes) · negotiation, challenger, category design, JTBD, tribe-building. **None of the 3 net-new sources overlap.**
- **ADVERTISING_RECOVERY** (Ogilvy / Sugarman / Halbert · copy craft): no folder title here; no overlap with the 3 net-new.
- **PERSUASION_RECOVERY** (Predictably Irrational / Ariely): no folder title here; no overlap with the 3 net-new.
- **NETWORK_DISTRIBUTION** (Kelly / Anderson / McCormick): no folder title here; no overlap with the 3 net-new (Crossing the Chasm's go-to-market is distinct from the distribution-economics register · it is positioning/adoption-lifecycle).
- **OPERATING_FOUNDER (STARTUP/SCALING/OPERATIONS):** The Mom Test (customer discovery) is adjacent to OPERATING_FOUNDER_STARTUP's The Lean Startup (validated learning) and The Innovator's Dilemma is adjacent to the build/scale registers, but **neither is a chunked source there** · both net-new · chunks must complement, not duplicate, the Lean Startup validated-learning and the scaling material.
- **HIGH_LEVEL_CONVOS** (Earn Your Leisure transcripts): no folder title here; no overlap.
- **Existing copywriting / positioning / offer-design / sales-flow / brand-psychology sources:** all live in BATCH_009 / BATCH_009_EXPANSION (the 13 canonical above). The 3 net-new are **positioning/strategy/customer-method**, not copy/offer/sales-flow.

## 4. Classification table

| Source | Classification |
|---|---|
| Eating the Big Fish, Competing Against Luck, Play Bigger, Never Split the Difference, Tribes | **already-canonical** (BATCH_009_EXPANSION) |
| Made to Stick, Differentiate or Die, $100M Leads, $100M Offers, Building a StoryBrand, Obviously Awesome, Purple Cow, This Is Marketing | **already-canonical** (BATCH_009) |
| Crossing the Chasm (Moore) | **net-new** · positioning / go-to-market |
| The Mom Test (Fitzpatrick) | **net-new** · customer-discovery method |
| The Innovator's Dilemma (Christensen) | **net-new** · disruption strategy |
| (none) | broken / needs-reacquire: NONE in this folder |
| (none) | out-of-scope: NONE in this folder (all 16 are commercial/strategy books) |

**Headline:** the `sales_positioning` folder is ~81% already-canonical (13/16). The genuine remaining work is a **3-book net-new remainder**, and its register is **positioning + customer-truth + disruption strategy**, NOT the sales-copy / offer / sales-flow material (which is already fully chunked in BATCH_009 / BATCH_009_EXPANSION).

## 5. Architecture recommendation: ONE small curated mini-batch of the 3 net-new (no split · do NOT defer)

The net-new remainder is only 3 books, so a split (copywriting / sales-process / positioning / negotiation) is **not warranted** · those sub-registers are already covered by BATCH_009 (copy/offer), BATCH_009_EXPANSION (negotiation/challenger/category), and ADVERTISING_RECOVERY (copy craft). No deferral is warranted either · all 3 are clean and net-new, nothing is broken.

**Honest naming caveat:** the operator's working name is `SALES_POSITIONING`, but the net-new content is **positioning (Crossing the Chasm) + customer-discovery method (The Mom Test) + disruption strategy (The Innovator's Dilemma)**. Only Crossing the Chasm is squarely "positioning"; The Mom Test is method and The Innovator's Dilemma is strategy. The lane is best understood as a **"positioning, customer-truth, and disruption" remainder**, not a sales/copy lane. Two options:
- **Option A (recommended):** ship under the operator's `SALES_POSITIONING` batch_id (it is the folder's name and the operator's named lane), chunking only the 3 net-new books, with the theme framed as positioning + customer-truth + disruption.
- **Option B:** rename to something like `POSITIONING_DISRUPTION` to reflect the actual register. Cosmetic; the content is identical. Recommend Option A for continuity with the operator's plan vocabulary unless the operator prefers the rename.

## 6. Recommended first (and only) lane: SALES_POSITIONING (include / defer / exclude)

- **INCLUDE (3 · CORE · curated · the positioning / customer-truth / disruption remainder):**
  - Crossing the Chasm (Geoffrey A. Moore) · mobi · ~71,724 words.
  - The Mom Test (Rob Fitzpatrick) · azw3 · ~30,791 words.
  - The Innovator's Dilemma (Clayton M. Christensen) · pdf · ~80,876 words.
  - Combined ~183,391 words · curated, not exhaustive.
- **DEFER:** none (no broken sources in this folder).
- **EXCLUDE (0 chunks):**
  - The 13 already-canonical BATCH_009 / BATCH_009_EXPANSION titles (listed in §2) · do NOT re-chunk.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every other already-canonical source and every other-cluster source (ADVERTISING_RECOVERY / PERSUASION_RECOVERY / NETWORK_DISTRIBUTION / OPERATING_FOUNDER / HIGH_LEVEL_CONVOS / the classical block / decision_judgment / brand-canon / Tier-2). CURRENT_IDENTITY sources.

## 7. Recommended chunk target / range (small lane)

- **Target:** ~9-11 chunks · **Range:** 8-13 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the positioning / customer-truth / disruption toolkit + the optionality guardrail).
- **Provisional per-source split:** Crossing the Chasm ~3-4 · The Innovator's Dilemma ~3-4 · The Mom Test ~2-3 · + 1 synthesis. Curated/representative from ~183K words, NOT chapter-by-chapter (The Mom Test is short and method-dense; contributes 2-3).

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `positioning` (17), `strategy` (203), `commercial-architecture` (59), `operator-process` (93), `systems-thinking` (51), `distribution` (14), `sales-flow` (17), `offer-design` (19), `copywriting` (24), `brand-psychology` (29), `operator-doctrine` (108), `ethics` (49).

| Domain | Planned use in this lane |
|---|---|
| `positioning` (anchor candidate) | Crossing the Chasm's go-to-market positioning (the chasm, the bowling-alley beachhead, the whole product, target-the-niche-then-cross), the act of choosing who you are for. |
| `strategy` | The Innovator's Dilemma's disruption logic (sustaining vs disruptive, why incumbents rationally lose), Crossing the Chasm's market-entry strategy. |
| `commercial-architecture` | The whole-product / market-structure architecture; the disruptive-business-model structure beneath the strategy. |
| `operator-process` | The Mom Test's customer-conversation method (ask about their life not your idea, avoid compliments/fluff, commitment + advancement) · the executional discipline. |
| `systems-thinking` | The Innovator's Dilemma's value-network / resource-allocation systems explanation of why good management fails · used where squarely systemic. |
| `distribution` (if warranted) | Crossing the Chasm's channel / go-to-market reach into the mainstream · used only where clearly distribution. |
| `operator-doctrine` (synthesis) | The closing synthesis chunk and the optionality-guarded reading. |
| `ethics` (if warranted) | only if a squarely-present moral dimension appears (unlikely · likely 0). |

**Recommended anchor:** `positioning` (the lane's namesake and Crossing the Chasm's core), with `strategy` the strong secondary.

### Domain issues to flag (important)

- **The existing `sales-flow` (17), `offer-design` (19), `copywriting` (24), `brand-psychology` (29) domains will likely see little or no use in this lane** · the net-new content is positioning/strategy/method, and the sales-copy/offer/brand-psychology material those domains hold is already canonical (BATCH_009 / BATCH_009_EXPANSION). They are available if a chunk squarely warrants one, but should NOT be force-fit.
- **`sales`, `marketing`, `persuasion`, `negotiation`, `closing`, `lead-generation`, `funnel`, `business` do NOT exist and will NOT be created** · sales material -> `sales-flow`; marketing -> `positioning` / `distribution` / `commercial-architecture`; persuasion -> `brand-psychology` / `copywriting`; negotiation -> `sales-flow` / `strategy` (and Never Split the Difference is already canonical anyway); closing/lead-generation/funnel -> `sales-flow` / `commercial-architecture`; business -> `commercial-architecture` / `operator-doctrine`.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 9. Connections (cross-references a future lane would open)

- **BATCH_009 + BATCH_009_EXPANSION:** the already-canonical commercial canon (copy, offer, remarkability, challenger, category, JTBD, negotiation, tribes) · this 3-book remainder is the positioning/adoption + customer-truth + disruption layer above/beside it (same `positioning` / `strategy` family · Competing Against Luck's JTBD pairs with The Innovator's Dilemma's disruption by the same author).
- **OPERATING_FOUNDER_STARTUP (The Lean Startup):** The Mom Test is the customer-conversation discipline beneath validated learning · complementary method, not duplicate.
- **NETWORK_DISTRIBUTION (The Long Tail / Kelly):** Crossing the Chasm's go-to-market reads against the distribution-economics register (positioning + reach).
- **CURRENT_OPERATOR_REALITY_BRIEF + CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** every chunk would reference the brief and hold the lane as decision-support only.

## 10. Identity-optionality confirmation

A future SALES_POSITIONING lane would NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- Material held as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF** · **NOT a directive that BJ become a salesperson, a copywriter, an agency owner, a funnel builder, or a marketing guru.** Positioning/disruption/customer-truth read as transferable judgment for how an eventual offer is framed, validated, and defended, applied to BJ's build-mode stage. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 11. Bible status

**The KJV Bible was NOT touched, staged, extracted, or chunked in this audit.** It remains OUTSIDE `raw/`, untracked in git, and held as a reverent SPIRITUAL_FOUNDATION anchor in the source universe. No `*bible*` file in the `sales_positioning` folder; 0 Bible matches as a source in any batch.

## 12. Deliverables a future ship would create (NOT created now)

For the recommended lane (batch_id `SALES_POSITIONING`): `01_KNOWLEDGE_BASE/batches/SALES_POSITIONING_CHUNKS.jsonl` + `batches/sales_positioning_extracted/` (3 .txt) + `summaries/SALES_POSITIONING_SUMMARY.md` + `indexes/SALES_POSITIONING_SOURCE_INDEX.md` + `00_COMMAND_CENTER/batch_logs/SALES_POSITIONING_EXTRACTION_LOG.md` + `_COMPLETE.md` + `scripts/extract_sales_positioning.py` + `scripts/write_sales_positioning_chunks.py`. Schema: the canonical 12-field JSONL · `chunk_id` pattern `SALES_POSITIONING_NNN`.

## 13. Scope guards honored by this audit

- Did NOT extract into knowledge-base folders, chunk, consolidate, or modify master files · total_chunks stays 1,665.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started; wrote only this audit file. Em-dash clean. Not committed (operator will review first).

## 14. Recommendation summary (operator decision · do not start without authorization)

Authorize a **SALES_POSITIONING** lane chunking **only the 3 net-new sources** (Crossing the Chasm + The Mom Test + The Innovator's Dilemma · ~183K words · target ~9-11 chunks · existing domains only · `positioning` anchor · no new domain · sales/marketing/persuasion/negotiation/closing/lead-generation/funnel/business NOT created · the 13 already-canonical BATCH_009 / BATCH_009_EXPANSION titles excluded · Bible excluded · curated, not exhaustive · decision-support not a directive). Then a normal plan -> ship -> consolidate -> session-save cycle. The lane is small and content-honest (positioning + customer-truth + disruption), not a sales/copy lane.
