# BATCH_003 · Tier 2 Canon Books · Extraction Plan

**Date drafted:** 2026-05-16
**Status:** PLAN ONLY · no extraction or chunking performed yet
**Batch theme:** Tier 2 canon books and adjacent doctrine sources that strengthen SNIPED's operating system beyond BATCH_001 (current OS state) and BATCH_002 (Tier 1 canon).

**Source folder (just established):** `~/AI-Brain-Refinery/raw/03_TIER_2_CANON_BOOKS/`

---

## Why this batch · the gap it closes

After BATCH_001 (106 chunks, SNIPED OS) and BATCH_002 (152 chunks, Tier 1 canon), the corpus has the **current operating state** and the **multi-century strategic substrate**. But several canonical sources currently exist only as auto-memory intel summaries (`intel_pricing_logic.md`, `intel_hospitality_layer.md`, `intel_status_psychology.md`, `intel_perennial_logic.md`, `intel_wwp_proclamations.md`, `intel_blockbuster_strategy.md`, `intel_analog_premium.md`, `intel_company_of_one.md`, `intel_leverage_logic.md`). The intel summaries are 1-2 page distillations; the full books carry 10-50× more usable principle density.

BATCH_003 will pull these books into the chunked corpus at BATCH_002 depth, converting auto-memory summaries into retrievable, citable, `sniped_relevance`-tagged chunks.

---

## Source coverage matrix

### Selected (10 files · all moved into `raw/03_TIER_2_CANON_BOOKS/`)

| # | Title | Author | Format | Size | Extraction tool | Difficulty |
|--:|-------|--------|--------|-----:|------------------|------------|
| 1 | The Win Without Pitching Manifesto | Blair Enns | epub | 89 KB | pandoc | EASY · short book, dense principles, one-pass |
| 2 | Pricing Creativity | Blair Enns | epub | 6.5 MB | pandoc | EASY · larger but well-structured |
| 3 | Unreasonable Hospitality | Will Guidara | pdf | 2.5 MB | pdftotext -layout | EASY · text-bearing PDF confirmed via 3-page sample |
| 4 | Status Anxiety | Alain de Botton | epub | 11.2 MB | pandoc | EASY · large but standard epub |
| 5 | The Elephant in the Brain | Simler + Hanson | epub | 736 KB | pandoc | EASY |
| 6 | Company of One | Paul Jarvis | epub | 1.1 MB | pandoc | EASY |
| 7 | Perennial Seller | Ryan Holiday | epub | 2.2 MB | pandoc | EASY |
| 8 | The Almanack of Naval Ravikant | Naval (ed. Jorgenson) | pdf | 1.9 MB | pdftotext -layout | EASY · text-bearing PDF confirmed; may have layout artifacts (multi-column / quote formatting) |
| 9 | Blockbusters | Anita Elberse | epub | 639 KB | pandoc | EASY |
| 10 | The Revenge of Analog | David Sax | epub | 851 KB | pandoc | EASY |

**Format breakdown:** 8 EPUBs, 2 PDFs. Both PDFs verified text-bearing via 3-page pdftotext sample (Naval and Guidara both extract clean prose; no OCR required).

**Total source size:** 26.4 MB. Estimated extracted text: ~10-12 MB after EPUB unwrapping and PDF text extraction (similar to BATCH_002 yield ratio).

**Md5 check:** All 10 files have unique md5s. Zero overlap with BATCH_002 sources. Safe to process without dedupe risk.

### Excluded (1 file · expected but not present)

| Title | Author | Reason | Disposition |
|-------|--------|--------|-------------|
| The Hype Handbook | Michael Schein | Not present in `raw/` after grep across the entire raw tree | DEFER to BATCH_004 or top-up later. Per user decision (2026-05-16), proceed with the 10 available books rather than block on Schein. |

### NOT in this batch (intentionally · already covered)

| Source | Status | Where covered |
|--------|--------|---------------|
| Hit Makers · Derek Thompson | Deduped in BATCH_002 | Already represented via STRATEGIC_PRINCIPLES synthesis in BATCH_001 |
| Trust Equation · David Maister | Synthesized | In BATCH_001 chunks via STRATEGIC_PRINCIPLES section 1 |
| Bruce Block · The Visual Story | Not tier-2 canon | Defer to future visual-craft batch (would pair with photographer Studies depth-fill) |
| Watkins · Hello My Name Is Awesome | Naming-specific | Defer to future brand-system batch (low current priority) |
| Reedsy · How to Market a Book | Lower-tier | Defer; covered partially by Holiday's Perennial Seller |
| Ross/Tyler · Predictable Revenue | Sales-process specific | Defer; BATCH_001 already has WWP outreach doctrine |
| Airey · Identity Designed | Visual brand reference | Defer to future visual-craft batch |
| Ries/Kotler · Positioning | Synthesized | Largely covered by Greene 48 Laws + Thiel (BATCH_002) |
| Wheeler · Designing Brand Identity (209 MB PDF) | Reference book | Defer; high cost to extract, low marginal density vs synthesis already in BATCH_001 |

---

## Expected domains and concepts per file

For each file, the predicted primary domains (per chunk schema's `domain` field) and the 3-5 highest-signal concepts expected.

### 1. Blair Enns · The Win Without Pitching Manifesto
- **Domains:** positioning, pricing, sales-flow, refusal-discipline
- **Expected concepts:** the 12 proclamations (specialize, lead, value over process, etc.), say-no-to-bad-fit, expertise-positioning, refusal as sales technique, the proposal-as-confirmation principle
- **SNIPED relevance:** validates Reset $1,500 floor, refusal-positioning lane, premium-confidence pricing language, narrow-niche specialization

### 2. Blair Enns · Pricing Creativity
- **Domains:** pricing, offer-design, sales-flow, value-capture
- **Expected concepts:** 3-option pricing architecture, premium-as-insurance, value-based vs hourly billing, the lighthouse identity, anchoring with the premium tier, pricing conversation choreography
- **SNIPED relevance:** directly informs Op Kit and Brand System tier pricing, the 3-tier anchor model in BATCH_001 chunk on pricing

### 3. Will Guidara · Unreasonable Hospitality
- **Domains:** hospitality, client-experience, brand, culture
- **Expected concepts:** hospitality vs service distinction, the "more than expected" delta, the hot-dog story, unreasonable as deliberate strategy, the dining-room theater, recognition-driven personalization
- **SNIPED relevance:** the entire premium-service touchpoint design (welcome packet, post-delivery moment, white-glove delivery, Direction Stack consultation experience). The single most operationally-actionable book in BATCH_003 for client-facing decisions.

### 4. Alain de Botton · Status Anxiety
- **Domains:** status, philosophy, founder-psychology, brand
- **Expected concepts:** the historical origin of status anxiety, 5 causes (lovelessness, snobbery, expectation, meritocracy, dependence), 5 solutions (philosophy, art, politics, religion, bohemia), the spectator's gaze
- **SNIPED relevance:** the *why* behind why founders pay premium for portraits — they are buying status-anxiety relief. Informs Cultural Doc tone, pricing-page copy, founder-buyer experience design.

### 5. Simler + Hanson · The Elephant in the Brain
- **Domains:** status, signaling, founder-psychology, hidden-motives
- **Expected concepts:** stated vs revealed motives, costly signaling, conspicuous consumption analog, why we don't tell ourselves the truth, the hidden-motive map for politics/charity/medicine/education/art
- **SNIPED relevance:** premium photography buyers' stated motive ("I need professional photos") vs revealed motive (status signaling to investors / team / peer founders). Designing for the real motive without naming it directly.

### 6. Paul Jarvis · Company of One
- **Domains:** leverage, scaling-discipline, founder-psychology, strategy
- **Expected concepts:** staying small as deliberate strategy, resilience over scale, growth as a tax not a reward, defining "enough," resisting the scale narrative, the right-sized business
- **SNIPED relevance:** validates the Year-10 destination state (4-7 person team, NOT a 50-person agency). Defense against the perpetual "you should scale" pressure from advisors and culture.

### 7. Ryan Holiday · Perennial Seller
- **Domains:** creator-economics, patience, brand, long-game
- **Expected concepts:** make work that lasts decades, Iron Maiden patience, the difference between launch and life, marketing as ongoing not one-shot, building an audience pre-launch, the platform compounding
- **SNIPED relevance:** Direction Stack book launch strategy, Cultural Doc cadence as platform-building, the 10-year arc validation, the bet on permanent vs trending work

### 8. Naval Ravikant · The Almanack
- **Domains:** leverage, wealth, philosophy, founder-psychology
- **Expected concepts:** 3 forms of leverage (labor / capital / code+media), specific knowledge, accountability, equity, escape competition through authenticity, judgment over hours, happiness as a skill
- **SNIPED relevance:** the leverage framework directly maps to SNIPED's hire-vs-DIY decisions, the code+media leverage of the Direction Stack book + Cultural Doc, the "escape competition through authenticity" frame for the anti-AI positioning

### 9. Anita Elberse · Blockbusters
- **Domains:** strategy, distribution, entertainment-economics, capital-allocation
- **Expected concepts:** bet big or don't bet, superstar economics, distribution dominates, the long-tail myth, why studios concentrate budget on tentpoles, the named-talent multiplier
- **SNIPED relevance:** Direction Stack book launch as blockbuster bet, named-client (Founder Tier) strategy, the case for concentrating energy on power-law bets rather than spreading across many small projects

### 10. David Sax · The Revenge of Analog
- **Domains:** analog-premium, taste, anti-tech-counter-movement, brand
- **Expected concepts:** why vinyl/film/paper/print/board games came back, analog as deliberate premium, the digital fatigue counter-current, the social and tactile premium, why physical artifacts retain value
- **SNIPED relevance:** the historical and structural precedent for SNIPED's anti-AI position. Validates the "scarcity will compound as everyone else races to AI" thesis. Direct material for the Cultural Doc "On Refusing to Use AI" essay.

---

## Domain coverage projection (vs current corpus)

Current corpus domain top-10 (BATCH_001 + BATCH_002 combined):

| Domain | Current | BATCH_003 expected adds | Projected new total |
|--------|--------:|------------------------:|--------------------:|
| strategy | 57 | +15 (Elberse, Naval, Enns ×2 partial) | ~72 |
| leadership | 36 | +5 (Jarvis, Guidara partial) | ~41 |
| pricing | 2 | **+15** (Enns ×2 dominant) | ~17 |
| status / signaling | ~0 | **+15** (de Botton + Simler/Hanson) | ~15 (NEW depth) |
| hospitality / client-experience | ~0 | **+10** (Guidara) | ~10 (NEW depth) |
| leverage | ~0 | **+8** (Naval, Jarvis) | ~8 (NEW depth) |
| brand | 13 | +5 (Holiday, Sax) | ~18 |
| founder-psychology | 5 | +6 (Jarvis, de Botton, Naval) | ~11 |
| analog-premium / craft | ~0 | **+8** (Sax) | ~8 (NEW depth) |
| creator-economics / patience | ~0 | **+8** (Holiday, Naval) | ~8 (NEW depth) |
| capital-allocation | 4 | +3 (Elberse) | ~7 |
| philosophy / taste | 3 | +6 (de Botton, Naval) | ~9 |

**Net effect:** BATCH_003 will fill 5 currently-thin domains (status/signaling, hospitality, leverage, analog-premium, creator-economics) AND deepen pricing from 2 to ~17 chunks. The corpus moves from strategy-heavy / operations-heavy toward a more balanced profile that covers the full premium-service business stack.

---

## Estimated chunk yield

Based on BATCH_002 density (152 chunks from 19 books = ~8 chunks/book avg, range 3-16):

| Book | Expected chunk range | Mid-estimate |
|------|---------------------:|-------------:|
| Enns · WWP Manifesto | 10-14 | 12 |
| Enns · Pricing Creativity | 10-14 | 12 |
| Guidara · Unreasonable Hospitality | 10-14 | 12 |
| de Botton · Status Anxiety | 8-12 | 10 |
| Simler+Hanson · Elephant in the Brain | 8-12 | 10 |
| Jarvis · Company of One | 8-10 | 9 |
| Holiday · Perennial Seller | 8-10 | 9 |
| Naval · Almanack | 10-14 | 12 |
| Elberse · Blockbusters | 6-10 | 8 |
| Sax · Revenge of Analog | 6-10 | 8 |

**Estimated total:** 84-120 chunks. Mid-estimate: **102 chunks**. Conservative floor: 90, ceiling: 140.

Combined corpus after BATCH_003: 258 + ~102 = **~360 chunks** (range 348-398).

---

## Risks and missing items

### Confirmed risks
1. **Schein missing.** The Hype Handbook is on the recommended source list but not present in `raw/`. User has decided to proceed with the 10-book set. Adding Schein later requires either a top-up batch or BATCH_004 inclusion. Risk impact: LOW · the hype/attention-economics domain is partially covered by Holiday and Elberse.

2. **PDF layout artifacts.** Naval's Almanack PDF has highly-styled typography (block quotes, multi-column sidebars, large-type pull-quotes). pdftotext -layout may capture stray formatting that needs cleanup similar to Sun Tzu's page-header removal in BATCH_002. Risk impact: LOW-MEDIUM · post-extraction cleanup is well-rehearsed from BATCH_002.

3. **de Botton's Status Anxiety is large (11.2 MB epub).** Likely the longest source in this batch by word count. Chunking discipline must be tight to avoid bloating chunk yield with low-signal narrative passages. Risk impact: LOW · pandoc handles size fine; chunking is a curation discipline regardless of source size.

4. **Naval Almanack is a curated quote collection.** Different structural pattern from narrative books. Many short principles vs few long arguments. Chunking should probably be more granular here (one principle per chunk) and may push toward the high end of the estimate (12-14 chunks). Risk impact: LOW.

### Non-risks (verified clear)
- Both PDFs are text-bearing (no OCR required, verified)
- Zero md5 overlap with BATCH_002 sources (verified)
- All 10 files have unique md5s (verified)
- Folder structure mirrors BATCH_002 convention (raw/03_TIER_2_CANON_BOOKS/)
- Required tools already installed from BATCH_002 (pandoc, pdftotext, ebook-convert, textutil)

### Pending user confirmation (no blocker for extraction)
- None for this batch. Direction Stack PDF canonical confirmation remains pending but does not affect BATCH_003.

---

## Recommended next command for BATCH_003 extraction

When ready to proceed, execute:

```bash
python3 ~/AI-Brain-Refinery/scripts/extract_batch_003.py
```

(Script does not yet exist; will be created at extraction step, modeled on `scripts/extract_batch_002.py`.)

The extraction step will:
1. Iterate the 10 files in `raw/03_TIER_2_CANON_BOOKS/`
2. Pick the right tool per file (`pandoc` for `.epub`, `pdftotext -layout` for `.pdf`)
3. Output cleaned text to `01_KNOWLEDGE_BASE/batches/batch_003_extracted/<slug>.md` or `.txt`
4. Apply page-header cleanup if needed (likely for Naval PDF; possibly Guidara PDF)
5. Write extraction log to `00_COMMAND_CENTER/batch_logs/BATCH_003_EXTRACTION_LOG.md`

After extraction completes, the chunking pipeline (modeled on `scripts/write_batch_002_chunks.py`) will produce `01_KNOWLEDGE_BASE/batches/BATCH_003_CHUNKS.jsonl` plus the three required companion files (summary, source index, completion log).

---

## Summary

- **Files found in raw/:** 10 of 11 tier-2 candidates
- **Files selected for BATCH_003:** 10 (all moved to `raw/03_TIER_2_CANON_BOOKS/`)
- **Files excluded (not present):** 1 (Schein · Hype Handbook · defer to later)
- **Total source size:** 26.4 MB
- **Estimated chunk yield:** 84-120 chunks (mid-estimate 102)
- **Estimated extraction time:** <5 minutes (all tools installed, all files text-bearing)
- **Estimated chunking time:** longest phase (book-by-book pass like BATCH_002)
- **Major risks:** none blocking; minor cleanup expected on Naval PDF layout
- **Blocker:** none

Ready to proceed with extraction on user signal.
