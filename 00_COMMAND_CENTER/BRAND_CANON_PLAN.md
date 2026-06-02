# BRAND_CANON mini-batch · plan only · 2026-05-25

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document locates the brand-canon candidates, probes extractability, runs an authoritative already-chunked overlap check, recommends a batch architecture, names the first lane, and stops. Nothing is extracted or chunked here.

## Operator decision (LOCKED 2026-05-25): the 5-book decision-neutral lane SELECTED

The operator selected **the 5 external brand-strategy books, chunked decision-neutrally**, as the BRAND_CANON lane.

- **INCLUDE (5 · SELECTED):** The Brand Gap (Marty Neumeier) · Designing Brand Identity (Alina Wheeler & Rob Meyerson) · Identity Designed (David Airey) · Brand Naming (Rob Meyerson) · Hello, My Name Is Awesome (Alexandra Watkins).
- **HOLD / DEFER:** the SNIPED-authored brand docs (BRAND_STRATEGY_2026-05-13 set + Brand_Builders_Playbook.docx + branding x clothes gold.docx + Build a Brand Like Apple.docx) · held until the fresh SNIPED brief · the fashion_luxury folder (The Luxury Strategy + fashion histories/memoirs) · a separate future FASHION_LUXURY lane.
- **EXCLUDE:** Building a StoryBrand (BATCH_009) · Alchemy (BATCH_009) · Status and Culture (CULTURE_AND_STATUS) · the 13 already-canonical sales_positioning titles · the KJV Bible · CURRENT_IDENTITY sources.

The books are read **decision-neutrally** as how brands work (market perception, symbolic capital, category design, proof architecture, taste-as-strategy), NOT as SNIPED identity decisions. This selection locks §5/§6 and §15. Extraction/chunking still requires a separate authorized ship step.

## 0. Verified starting state

- **Head commit:** `0a98e7f save session after TIER_2_GREENE_STRATEGY consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,742 · 10 numbered batches + 40 mini-batches · 62 official domains (75 combined keys).
- **STORYTELLING_NARRATIVE + TIER_2_GREENE_STRATEGY complete.** BRAND_CANON is a named remaining lane (identity-side · the audits flagged it "keep decision-neutral under optionality guardrails").
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified)

A full `raw/` sweep for brand / luxury / fashion / identity / naming / category-design candidates found the following.

### A. The net-new brand-strategy / identity / naming books (the lane core · `raw/` top-level)

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| Designing Brand Identity | Alina Wheeler & Rob Meyerson | pdf | 97,195 | CLEAN · NET-NEW |
| Identity Designed | David Airey | epub | 55,889 | CLEAN · NET-NEW |
| Brand Naming | Rob Meyerson | epub | 43,009 | CLEAN · NET-NEW |
| Hello, My Name Is Awesome | Alexandra Watkins | epub | 23,925 | CLEAN · NET-NEW |
| The Brand Gap | Marty Neumeier | pdf | 22,630 | CLEAN · NET-NEW |

Combined: ~242,648 words. Read-only `pdftotext` / `ebook-convert`-to-/tmp probes (temp deleted; mtimes unchanged). Real book text confirmed by sampling.

### B. Already-canonical brand-adjacent (verified · EXCLUDE)

| Source | Author | Where | Status |
|---|---|---|---|
| Building a StoryBrand | Donald Miller | BATCH_009 | already-canonical (applied brand-message) |
| Alchemy | Rory Sutherland | BATCH_009 | already-canonical (brand-psychology) |
| Status and Culture | W. David Marx | CULTURE_AND_STATUS | already-canonical (status/taste/symbolic value) |
| (the 13 sales_positioning titles: Made to Stick, Obviously Awesome, Purple Cow, This Is Marketing, Differentiate or Die, Play Bigger, Eating the Big Fish, etc.) | various | BATCH_009 / BATCH_009_EXPANSION / POSITIONING_DISRUPTION | already-canonical |

### C. Net-new but DISTINCT register · the fashion_luxury folder (SEPARATE future lane · NOT this lane)

`raw/03_TIER_2_CANON_BOOKS/fashion_luxury/` (8 files): The Luxury Strategy (Kapferer/Bastien · net-new), The End of Fashion (Agins), The Beautiful Fall (Drake), The Chiffon Trenches (Talley), Dior by Dior, The Little Dictionary of Fashion (Dior), Deluxe (Thomas), Abloh Figures of Speech. This is a **luxury-brand-strategy + fashion-culture/history register**, distinct from the general brand-strategy/identity canon. Recommend a separate **FASHION_LUXURY** lane (see §5), not folding it into BRAND_CANON.

### D. SNIPED-authored brand material · HELD / decision-neutral · NOT chunked (identity-side)

- **`raw/00_BRIEF/BRAND_STRATEGY_2026-05-13/` (10 md):** BRIEF, AUDIT, NAMING_CRITERIA, NAMING_CANDIDATES, NAME_RECOMMENDATION, BRAND_ARCHITECTURE, POSITIONING_STATEMENT, BRAND_VOICE, VISUAL_IDENTITY_BRIEF, MIGRATION_PLAN.
- **`raw/Brand_Builders_Playbook.docx`, `raw/branding x clothes gold.docx`, `raw/Build a Brand Like Apple.docx`** (raw-root docx).

These are **SNIPED's actual brand/naming/identity decisions**, tied to the held CURRENT_IDENTITY_AND_BRAND_OPTIONALITY lane. They are **held, decision-neutral, and NOT chunked** (they predate and are governed-in-spirit by CURRENT_OPERATOR_REALITY_BRIEF; processing them would risk finalizing SNIPED identity). NOT part of BRAND_CANON.

## 2. Source-quality / stub / scan check

- **5 clean, text-bearing brand-strategy books** (word counts above). pdfs via `pdftotext`, epubs via `ebook-convert`. No OCR. Real book text confirmed by content sampling.
- **No broken candidates** among the 5. (The Luxury Strategy in fashion_luxury is clean but deferred to the separate lane.)
- At ship, sample each extracted .txt to confirm real book text before chunking.

## 3. Already-chunked overlap check (authoritative · by source_title / author across all 40 batch jsonls)

**The 5 brand-strategy books are NET-NEW as sources** (0 chunks each · verified): The Brand Gap, Designing Brand Identity, Identity Designed, Hello My Name Is Awesome, Brand Naming.

**Checked against the operator's named lanes:**
- **BATCH_009:** holds Building a StoryBrand (Miller · applied brand-message) and Alchemy (Sutherland · brand-psychology) and the bulk of the applied positioning/persuasion canon · already-canonical · EXCLUDED. BRAND_CANON is the **upstream brand-strategy/identity/naming layer** beneath the applied message craft.
- **BATCH_009_EXPANSION:** Play Bigger (category design), Eating the Big Fish (challenger brands), Competing Against Luck, Never Split the Difference, Tribes · already-canonical · EXCLUDED.
- **POSITIONING_DISRUPTION:** Crossing the Chasm, The Innovator's Dilemma, The Mom Test · already-canonical · EXCLUDED.
- **NETWORK_DISTRIBUTION:** Kelly / Anderson / McCormick · no brand-strategy overlap.
- **STORYTELLING_NARRATIVE:** the StoryBrand craft is the narrative layer; BRAND_CANON is the brand-identity/perception layer · cross-referenced, no overlap.
- **MEDIA_BUSINESS_RECOVERY / PERSUASION_RECOVERY:** Hit Men / The Mailroom / Predictably Irrational · no brand-strategy overlap.
- **CULTURE_AND_STATUS:** Status and Culture (Marx) + The Status Game (Storr) · already hold the taste/status/symbolic-value theory · BRAND_CANON cross-references it (taste-as-strategy routes there), does NOT re-chunk it.
- No existing brand / aesthetics / positioning / commercial-architecture / media-business lane contains the 5 brand-strategy books.

## 4. Classification table

| Source | Classification |
|---|---|
| The Brand Gap (Neumeier) | **net-new** · the brand-strategy spine (the gap between strategy and creativity; brand = a gut feeling) |
| Designing Brand Identity (Wheeler) | **net-new** · the comprehensive brand-identity-system guide |
| Identity Designed (Airey) | **net-new** · visual branding / identity design craft |
| Brand Naming (Meyerson) | **net-new** · naming as a craft/process |
| Hello, My Name Is Awesome (Watkins) | **net-new** · naming craft (names that stick) |
| Building a StoryBrand (Miller) | **already-canonical** (BATCH_009) · exclude |
| Alchemy (Sutherland) | **already-canonical** (BATCH_009) · exclude |
| Status and Culture (Marx) | **already-canonical** (CULTURE_AND_STATUS) · exclude |
| The Luxury Strategy + fashion_luxury folder | **net-new but DISTINCT register** · separate FASHION_LUXURY lane |
| SNIPED brand docs (BRAND_STRATEGY_2026-05-13 + 3 docx) | **held / decision-neutral / not chunked** (identity-side) |

## 5. Architecture recommendation: ONE curated mini-batch of the 5 brand-strategy books (do NOT split · do NOT defer the books)

The 5 net-new books form **one coherent register: brand as market perception and the systems that shape it** (the brand gap, identity systems, visual branding, naming craft). At ~242,648 words across 5 books this is squarely in-band for the corpus's curated lanes. **A split (brand-strategy vs naming) would over-fragment** (naming is a sub-discipline of the same brand-identity register). **The fashion_luxury folder is a genuinely distinct register and should be its own future FASHION_LUXURY lane**, not folded in.

**On deferral (the real question for this lane):** brand/naming is the most identity-adjacent register, and the audits flagged "keep decision-neutral / arguably hold until the fresh SNIPED brief." The resolution: the brand-strategy **BOOKS** are external, general knowledge (how brands work as market perception, symbolic capital, category design, proof architecture, taste-as-strategy) and can be chunked **decision-neutrally** without finalizing any SNIPED identity. What must wait for the fresh SNIPED brief is the **SNIPED-authored brand material** (the BRAND_STRATEGY_2026-05-13 set + the 3 brand docx), which stays HELD. So: **proceed with the 5 books decision-neutrally; hold the SNIPED docs.** Whole-lane deferral is NOT required for the books.

**Recommendation: a single curated BRAND_CANON mini-batch of the 5 net-new brand-strategy books, chunked decision-neutrally.** (Operator may alternatively choose to defer the entire lane until the fresh SNIPED brief; not recommended for the books, recommended for the SNIPED docs.)

## 6. Recommended first (and only) lane: BRAND_CANON (include / defer / exclude)

- **INCLUDE (CORE · curated · the brand-as-market-perception register):**
  - The Brand Gap (Marty Neumeier) · pdf · ~22,630 words.
  - Designing Brand Identity (Alina Wheeler & Rob Meyerson) · pdf · ~97,195 words.
  - Identity Designed (David Airey) · epub · ~55,889 words.
  - Brand Naming (Rob Meyerson) · epub · ~43,009 words.
  - Hello, My Name Is Awesome (Alexandra Watkins) · epub · ~23,925 words.
- **DEFER / HELD:**
  - The SNIPED-authored brand material (BRAND_STRATEGY_2026-05-13 set + Brand_Builders_Playbook.docx + branding x clothes gold.docx + Build a Brand Like Apple.docx) · held / decision-neutral until the fresh SNIPED brief.
  - The fashion_luxury folder (The Luxury Strategy + fashion histories/memoirs) · a separate future FASHION_LUXURY lane.
- **EXCLUDE (0 chunks):**
  - Building a StoryBrand, Alchemy (already BATCH_009), Status and Culture (already CULTURE_AND_STATUS), the 13 already-canonical sales_positioning titles · cross-referenced, NOT re-chunked.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical positioning / persuasion / commercial source. CURRENT_IDENTITY sources.

## 7. Recommended chunk target / range

- **Target:** ~14-16 chunks · **Range:** 12-18 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the brand-as-perception toolkit + the optionality guardrail).
- **Provisional per-source split:** Designing Brand Identity ~4 (the comprehensive system guide) · The Brand Gap ~3 (the short, dense brand-strategy spine) · Identity Designed ~3 (visual branding craft) · Brand Naming ~2 · Hello My Name Is Awesome ~2 · + 1 synthesis. Curated/representative (NOT page-by-page): The Brand Gap (brand as a gut feeling, the gap between strategy and creative, the five disciplines: differentiate, collaborate, innovate, validate, cultivate); Designing Brand Identity (the brand-identity process, brandmarks/systems, brand as a strategic asset, governance/consistency); Identity Designed (the identity-design process, working from strategy to visual system, the role of research and the designer-client relationship); Brand Naming + Hello My Name Is Awesome (naming as a craft and process: brief, generation, screening, the SMILE/SCRATCH tests, memorability and meaning) · held as naming-craft, NOT a directive to pick a SNIPED name.

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `brand` (39), `brand-psychology` (29), `aesthetics` (78), `positioning` (20), `commercial-architecture` (60), `media-business` (12), `culture` (66), `status` (16), `strategy` (207), `operator-doctrine` (120), `ethics` (53).

| Domain | Planned use |
|---|---|
| `brand` (anchor) | Brand as market perception (a gut feeling), the brand gap, brand as a strategic asset, the brand-identity system. |
| `brand-psychology` | How meaning and perception form in the customer's mind; memorability and the psychology of names. |
| `aesthetics` | Visual identity / design craft (Airey, Wheeler's brandmark/system material). |
| `positioning` | The brand's position and differentiation in the market. |
| `commercial-architecture` | Brand as a business asset and governance system (consistency, brand management). |
| `culture` | Brand as cultural meaning and shared signal. |
| `status` (if warranted) | Brand as a status/symbolic signal · used where squarely status-relevant (taste-as-strategy routes here). |
| `strategy` | Brand strategy, category design, the strategy-vs-creative gap. |
| `operator-doctrine` | The transferable brand discipline + the closing synthesis. |
| `ethics` / `media-business` (if warranted) | Only if squarely present · likely 0-1 each. |

**Recommended anchor:** `brand` (the lane's namesake and core), with `aesthetics` / `brand-psychology` / `positioning` / `strategy` / `commercial-architecture` the secondaries, and `culture` / `status` for the symbolic/taste material.

### Domain issues to flag (important)

- **`branding`, `luxury`, `fashion`, `identity`, `creator`, `influencer`, `personal-brand`, `lifestyle`, `hype`, `clout` do NOT exist and will NOT be created.** Verified absent in `combined_domain_counts`.
- **`taste` ALREADY EXISTS (count 12, from the status/culture lanes) but is on the operator's do-not-use list for this lane.** BRAND_CANON will **NOT use `taste` as a domain**; taste-as-strategy material routes to `aesthetics` / `culture` / `status` / `brand`. (This is the one forbidden-list token that already exists; not creating it, and not using it here.)
- **`brand` (39), `brand-psychology` (29), `positioning` (20), `status` (16) are mid-size existing domains** · this lane will reuse and grow them, NOT create anything new.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 9. Connections (cross-references this lane opens)

- **BATCH_009 (Building a StoryBrand / Alchemy / Made to Stick / Obviously Awesome / Purple Cow / This Is Marketing):** the applied brand-message and brand-psychology layer · BRAND_CANON is the upstream brand-strategy/identity/naming layer beneath it.
- **BATCH_009_EXPANSION (Play Bigger / Eating the Big Fish) + POSITIONING_DISRUPTION (Crossing the Chasm):** category design and positioning · the strategic-market layer the brand expresses.
- **CULTURE_AND_STATUS (Status and Culture / The Status Game) + BATCH_010 (lineage / status games):** the taste / status / symbolic-value theory brand identity reads against (taste-as-strategy routes here).
- **STORYTELLING_NARRATIVE (Building a StoryBrand craft / the narrative layer):** brand message as story · the narrative companion to brand identity.
- **TIER_2_GREENE_STRATEGY + CULTURE_AND_STATUS:** brand as a status/perception signal · the symbolic-capital reading.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane especially tightly (brand is the most identity-adjacent register); CURRENT_IDENTITY and the SNIPED brand docs remain held / NOT extracted.

## 10. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the books as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF** · the closing synthesis chunk makes the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY and the SNIPED-authored brand-strategy material remain held / NOT extracted.** The naming books are held as naming-craft, NOT a directive to finalize a SNIPED name.

## 11. Brand material = market perception / symbolic capital / category design / proof architecture / taste-as-strategy (NOT a directive)

The 5 books are held strictly as a **decision-support / pattern-library layer**: how brands work as **market perception, symbolic capital, category design, proof architecture, and taste-as-strategy**. It is **NOT a directive that BJ become a fashion brand, a luxury influencer, a personal-brand guru, a lifestyle creator, an agency bro, a clout account, or an aesthetics-only operator**, and not a mandate to launch or finalize a brand. The methods are read as transferable brand-perception literacy for a solo field-engineer in build-mode, loading the backend before final brand/offer/company-architecture decisions.

## 12. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BRAND_CANON_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/brand_canon_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/BRAND_CANON_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/BRAND_CANON_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BRAND_CANON_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BRAND_CANON_COMPLETE.md` |
| Extraction script | `scripts/extract_brand_canon.py` |
| Chunk writer | `scripts/write_brand_canon_chunks.py` |

Schema: the canonical 12-field JSONL · `chunk_id` pattern `BRAND_CANON_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · 5 sources · no new domain · `brand` anchor · branding/luxury/fashion/taste/identity/creator/influencer/personal-brand/lifestyle/hype/clout NOT created · `taste` not used · Building a StoryBrand / Alchemy / Status and Culture 0 [already canonical] · fashion_luxury 0 [separate lane] · SNIPED brand docs 0 [held] · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive + brand-as-perception guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 13. Projected post-consolidation state (for reference · NOT applied now)

If the lane ships at the mid-target and consolidates: 1,742 + ~14-16 = **~1,756-1,758 chunks** · 10 numbered batches + **41 mini-batches** · **62 domains (NO new domain** · bumps to `brand` [anchor] / `brand-psychology` / `aesthetics` / `positioning` / `strategy` / `commercial-architecture` / `culture`, plus `status` / `operator-doctrine` where warranted). Exact counts finalized at ship/consolidation time. Subsequent lanes: a separate FASHION_LUXURY lane (The Luxury Strategy + fashion histories), the remaining Tier-2 clusters (leadership_mgmt, consulting_service, systems_thinking, expertise_creativity), the optional operator-docs cleanup, the fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship, the SPIRITUAL_FOUNDATION decision, and the broken-backlog re-acquisitions.

## 14. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,742.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted · all mtimes unchanged).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 15. Next step (operator decision · do not start without authorization)

Authorize the **BRAND_CANON** lane (5 net-new brand-strategy books · The Brand Gap + Designing Brand Identity + Identity Designed + Brand Naming + Hello My Name Is Awesome · target ~14-16 · existing domains only · `brand` anchor · no new domain · branding/luxury/fashion/taste/identity/creator/influencer/personal-brand/lifestyle/hype/clout NOT created · `taste` not used [routes to aesthetics/culture/status] · Building a StoryBrand / Alchemy / Status and Culture excluded as already canonical · the fashion_luxury folder deferred to a separate FASHION_LUXURY lane · the SNIPED-authored brand docs held / decision-neutral · Bible excluded · curated, not exhaustive · brand-as-market-perception / symbolic-capital / category-design / proof-architecture / taste-as-strategy, NOT a directive and NOT a finalized SNIPED brand). Then commit the ship outputs, then consolidate, then session-save.
