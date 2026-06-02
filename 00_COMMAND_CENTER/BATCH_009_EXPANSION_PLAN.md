# BATCH_009_EXPANSION mini-batch · PLAN

**Date planned:** 2026-05-23
**Status:** PLAN ONLY · not extracted, not chunked, master files untouched, not committed.
**Batch kind:** mini-batch (descriptive slug `BATCH_009_EXPANSION` · would be the 12th mini-batch · numbered slots stay reserved for canon batches).
**Relationship:** the operator-deferred EXPANSION set from BATCH_009 core (the 5 commercial-strategy books held out of the 18-book core).

---

## 0. Verified starting state

- **Head commit:** `1211da5 plan CURRENT_IDENTITY_AND_BRAND_OPTIONALITY mini-batch`
- **Working tree:** clean (`git status --short` empty before this plan).
- **Total chunks:** 1,278 · 10 numbered batches + 11 mini-batches · 60 official domains (73 combined_domain_counts keys).
- **BATCH_009 core:** complete and canonical (76 chunks · 18 books).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan committed only (`1211da5`), not extracted.
- **No expansion lane started:** no `BATCH_009_EXPANSION_CHUNKS.jsonl`, no `batch_009_expansion_extracted/`, no `BATCH_009_EXPANSION_COMPLETE.md`, no prior plan.

---

## 1. Goal + theme

Commercial-strategy expansion after the BATCH_009 commercial-voice core: **negotiation, category design, challenger positioning, tribe building, customer progress (jobs-to-be-done), demand creation, strategic offers, and market framing.** Where BATCH_009 core is the copy/persuasion/offer craft, this lane is the **strategic-commercial layer above the copy**: how to create and dominate a market, how to compete from behind, how to read what customers are really hiring a product to do, and how to negotiate the deal.

This is decision-support theory. It does NOT finalize any SNIPED direction (see §9).

---

## 2. Candidate sources (all five located in `raw/02_TIER_1_CANON_BOOKS/sales_positioning/`)

| # | File (exact · note leading spaces on 2) | Author · Title | Type | Extraction |
|--:|---|---|---|---|
| 1 | `Raz, Tahl_Voss, Chris - Never Split the Difference_ Negotiating As If Your Life Depended On It (2016, HarperBusiness) - libgen.li.epub` | Chris Voss & Tahl Raz · Never Split the Difference (2016) | epub | stdlib zipfile + HTML-strip |
| 2 | `· Adam Morgan - Eating the Big Fish_ How Challenger Brands Can Compete Against Brand Leaders (2009) - libgen.li.pdf` (leading space) | Adam Morgan · Eating the Big Fish (2009) | pdf | pdftotext -layout |
| 3 | `Al Ramadan, Dave Peterson, Christopher Lochhead, Kevin Maney - Play Bigger_ ... (2016, HarperBusiness) - libgen.li.epub` | Ramadan/Peterson/Lochhead/Maney · Play Bigger (2016) | epub | stdlib zipfile + HTML-strip |
| 4 | `Seth Godin - Tribes_ We Need You to Lead Us (2008, Penguin) - libgen.li.epub` | Seth Godin · Tribes (2008) | epub | stdlib zipfile + HTML-strip |
| 5 | `· Christensen, Clayton M. & Dillon, Karen & Hall, Taddy & Duncan, - Competing Against Luck_ ... (2016) - libgen.li.epub` (leading space) | Christensen/Dillon/Hall/Duncan · Competing Against Luck (2016) | epub | stdlib zipfile + HTML-strip |

Theme mapping: Voss = negotiation · Morgan = challenger positioning · Play Bigger = category design / demand creation · Tribes = tribe building / movement leadership · Christensen = customer progress (jobs-to-be-done) / demand-side thinking.

---

## 3. Pre-flight peek · source quality

| Source | Size | Extracted words | Verdict |
|---|--:|--:|---|
| Never Split the Difference | 466 KB | 82,449 | Clean epub · full text · no stub |
| Eating the Big Fish | 2.97 MB | 125,574 (pdftotext) | **Text PDF, NOT scanned** · clean text layer · no OCR needed |
| Play Bigger | 431 KB | 81,173 | Clean epub · full text |
| Tribes | 153 KB | 31,561 | Clean epub · short manifesto-length book (expected) · no stub |
| Competing Against Luck | 280 KB | 83,793 | Clean epub · full text |

- **No stubs, no bad downloads, no unsupported formats, no scanned PDFs.** All extract with the proven toolchain (stdlib zipfile epub + pdftotext) · no OCR · no new dependencies.
- **Net-new (already-chunked overlap check):** grep across every `*_CHUNKS.jsonl` returned 0 for all five titles/authors. The lone "Seth Godin" hit (2 files) is **This Is Marketing / Purple Cow (BATCH_009)** + **The Dip (BATCH_003)** · **Tribes itself = 0 everywhere** (confirmed net-new). All five are genuinely net-new.
- **Recovery/acquisition items:** untouched · none involved.
- **Leading-space filenames** on Eating the Big Fish + Competing Against Luck · handled by keyword-substring matching in the extract script (the established pattern), not exact names.

---

## 4. Recommended inclusion / defer / exclude

### INCLUDE · CORE · all 5 sources

All five are net-new, on-theme, full-text, and were explicitly the operator-deferred BATCH_009 EXPANSION set. No reason to defer any. This is the cleanest possible mini-batch: one tight commercial-strategy theme, five canon books, zero overlap.

### DEFER / EXCLUDE

- None from this set. (The other BATCH_009 follow-ups · Confessions text edition, Sugarman/Caples/Halbert re-acquisitions, Predictably Irrational `.djvu` · are separate recovery items and remain untouched, NOT part of this lane.)

---

## 5. Estimated chunk yield

BATCH_009 core ran ~4.2 chunks/book. Applying that with book length:

| Source | Chunks |
|---|--:|
| Never Split the Difference (negotiation) | 4-5 |
| Eating the Big Fish (challenger) | 4-5 |
| Play Bigger (category design) | 4-5 |
| Tribes (leadership / movement · shorter book) | 3 |
| Competing Against Luck (jobs-to-be-done) | 4-5 |
| cross-source synthesis | 1-2 |

**Target: ~18-24 chunks. Acceptable range: 15-28.** ID pattern `BATCH_009_EXPANSION_001..NNN`. Synthesis chunks (last 1-2) cite a representative book file per the prior-batch convention.

---

## 6. Domain set (NO new domain · all 11 verified to exist)

| Domain | Current | Use here |
|---|--:|---|
| `strategy` | 150 | category design, challenger strategy, JTBD demand-side |
| `positioning` | 14 | challenger positioning, category POV, differentiation |
| `sales-flow` | 12 | negotiation tactics, calibrated questions, the deal |
| `commercial-architecture` | 37 | category-as-market-structure, the category king |
| `offer-design` | 15 | JTBD → offer shaping, strategic offers |
| `brand` | 27 | challenger brand, lighthouse identity |
| `brand-psychology` | 22 | tactical empathy, tribe belonging, social/emotional jobs |
| `content-strategy` | 49 | point-of-view, movement/tribe communication |
| `operator-process` | 59 | negotiation process, category-design process |
| `client-application` | 15 | negotiation in Reset/client conversations |
| `systems-thinking` | 31 | category creation + demand creation as systems |

**Estimated distribution (≈ target):** strategy 5-6 · positioning 4-5 · sales-flow 3-4 · commercial-architecture 2-3 · brand-psychology 2-3 · offer-design 2 · brand 2 · content-strategy 1-2 · operator-process 1-2 · client-application 1-2 · systems-thinking 1.

### 7. NEW domain flag

**None required.** Every domain pre-exists (the same discipline that kept BATCH_009 core at no-new-domain). If a concept genuinely fits none of the 11 during chunking, halt and surface rather than mint a domain.

---

## 8. How this mini-batch connects to the corpus

- **BATCH_009 advertising/copywriting canon (core):** core is the copy/persuasion/offer *craft* (Hopkins, Cialdini, Hormozi, Trout, Dunford). EXPANSION is the *strategic-commercial layer above the copy* · how to create a category, compete as a challenger, read the customer's job, and negotiate. Dunford's positioning + Hormozi's offers connect directly up into Play Bigger's category design and Christensen's JTBD.
- **B2B_POSITIONING_CLAUDE_OPERATOR:** Voss negotiation + Christensen JTBD + Morgan challenger framing sharpen the B2B discovery/positioning conversation and the one-liner.
- **OPPORTUNITY_MANAGEMENT_TEMPLATES:** JTBD (Christensen) and category/demand creation (Play Bigger) feed the hopper qualification and business-case logic; negotiation (Voss) feeds the close.
- **CLAUDE_OPERATOR_DOCS + BATCH_008:** the AI/Claude operation layer is HOW the operator executes at leverage; this lane is part of the WHAT (the commercial-strategy standard) that execution serves.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** this lane is **decision-support input** to the upcoming direction decision · category design, challenger positioning, and JTBD are *option-generators*, NOT a mandate to pick a category/niche now. Chunks present these as reusable lenses, not as a SNIPED category verdict.
- **Future SNIPED offer/category decisions:** when the operator runs the direction decision, this lane supplies the frameworks (JTBD to find the real demand, Play Bigger to evaluate category creation, Morgan to assess a challenger play, Voss to structure the deal) · as inputs, kept reversible.

---

## 9. This lane does NOT finalize brand direction

Confirmed. BATCH_009_EXPANSION introduces general commercial-strategy theory only. It does **not** decide SNIPED, SNIPED Media, or BASEPLATE direction, does not pick a category/niche, does not set an offer ladder, and does not lock photography as the frame. Per the CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails, every chunk's `sniped_relevance` frames the theory as **optionality-preserving decision-support** (an option-input lens), never as a finalized SNIPED commercial decision. Where a book argues for committing to a single category (Play Bigger) or a single challenger identity (Morgan), the chunk records it as a *framework to evaluate*, with the explicit note that SNIPED's direction is undecided.

---

## 10. Deliverables (produced only at the authorized ship step · NOT now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/BATCH_009_EXPANSION_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/batch_009_expansion_extracted/` (5 normalized `.txt`) |
| Summary | `01_KNOWLEDGE_BASE/summaries/BATCH_009_EXPANSION_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/BATCH_009_EXPANSION_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/BATCH_009_EXPANSION_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/BATCH_009_EXPANSION_COMPLETE.md` |
| Extract script | `scripts/extract_batch_009_expansion.py` (4 epub via stdlib zipfile · 1 pdf via pdftotext · keyword-match the leading-space filenames) |
| Chunk writer | `scripts/write_batch_009_expansion_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags). `batch_id` = `BATCH_009_EXPANSION`. source_file values resolve under `batch_009_expansion_extracted/`. Copyright-safe quote discipline: all five are in-copyright trade books · `direct_quotes` short illustrative lines only (target longest ≤ 14 words) · most chunks paraphrase · extracted full text is INTERNAL chunk-authoring reference only.

---

## Constraints honored by this plan

- Did NOT extract, chunk, update master files, or commit.
- Did NOT modify any `raw/` source file · recovery/acquisition items untouched.
- No em-dashes.
- No new domain proposed.
- Does not finalize SNIPED / SNIPED Media / BASEPLATE direction (optionality preserved).
- Stops at the plan. Ship/extract/chunk/validate/consolidate await explicit operator authorization.

## Open questions for the operator (resolve before ship)

1. **Scope confirm:** CORE = all 5 books (no defer)? (Recommended.)
2. **Target band:** ~18-24 chunks (range 15-28) · acceptable?
3. **Synthesis chunks:** 1-2 cross-source synthesis chunks at the end (per BATCH_009 convention) · OK?
