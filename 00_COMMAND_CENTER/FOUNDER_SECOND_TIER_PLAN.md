# FOUNDER_SECOND_TIER mini-batch · PLAN

**Date planned:** 2026-05-23
**Status:** PLAN ONLY · not extracted, not chunked, master files untouched, not committed.
**Batch kind:** mini-batch (descriptive slug · the 17th mini-batch).

> **OPERATOR DECISIONS APPLIED (2026-05-23 · locked):**
> 1. **CORE = 7 sources** (one arc per founder/operator · section 4): Sam Walton/Walmart, Elon Musk, Super Pumped/Uber, The Airbnb Story, Titan/Rockefeller, The Fish That Ate the Whale/Banana King, Pour Your Heart Into It/Starbucks origin.
> 2. **Onward DEFERRED** (Schultz turnaround/repair companion · not this lane).
> 3. **Target ~18-24 chunks** (range 15-28) · 1-2 synthesis chunks.
> 4. **NO new domain** · existing domains only (section 6): founder-psychology (anchor), operator-doctrine, operator-process, strategy, commercial-architecture, brand, capital, systems-thinking, culture (if warranted), ethics (if warranted).
> 5. **Grant + Washington DEFERRED** to a future historical-biography lane.
> 6. **Exclude:** BIOGRAPHY_FOUNDER_MEDIA core, MEDIA_BUSINESS sources, broken/recovery memoirs, CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources.
> 7. **CURRENT_OPERATOR_REALITY_BRIEF guardrails preserved** · founder arcs are pattern-library only · NO directive for BJ to copy any founder or manufacture a myth · no final SNIPED / SNIPED Media / BASEPLATE direction.

---

## 0. Verified starting state

- **Head commit:** `cb8f096 save session after MEDIA_BUSINESS consolidation`
- **Working tree:** clean.
- **Total chunks:** 1,371 · 10 numbered batches + 16 mini-batches · 62 official domains (75 combined_domain_counts keys).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked (`ca5c4db`). **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **No lane started:** no `FOUNDER_SECOND_TIER_CHUNKS.jsonl`, no extracted dir, no COMPLETE marker, no prior plan.

---

## 1. Goal + theme

Founder second-tier expansion after BIOGRAPHY_FOUNDER_MEDIA: company-building arcs, scale psychology, category creation, platform expansion, operational obsession, leadership contradictions, capital control, myth-building, founder risk, distribution, and how ambitious operators turn small openings into durable institutions. The source set is the founder second-tier deferred from BIOGRAPHY_FOUNDER_MEDIA, in `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/`.

---

## 2. Candidate inventory (`raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/`)

| File | Founder · Company | Type | Words | Status |
|---|---|---|--:|---|
| Sam Walton: Made In America | Sam Walton · Walmart | pdf | 96,353 | net-new |
| Elon Musk (Isaacson) | Musk · Tesla/SpaceX | epub (86MB) | 204,776 | net-new |
| Super Pumped | Mike Isaac · Uber | epub | 125,963 | net-new |
| The Airbnb Story | Leigh Gallagher · Airbnb | epub | 87,528 | net-new |
| Titan | Chernow · Rockefeller / Standard Oil | mobi | (ebook-convert) | net-new |
| The Fish That Ate the Whale | Rich Cohen · Sam Zemurray / United Fruit (Banana King) | mobi | (ebook-convert) | net-new |
| Pour Your Heart Into It | Howard Schultz · Starbucks (the build) | mobi | (ebook-convert) | net-new |
| Onward | Howard Schultz · Starbucks (the return/turnaround) | mobi | (ebook-convert) | net-new |

Note: the operator listed 7 founders; Schultz has 2 books (Pour Your Heart Into It = the founding arc · Onward = the 2008 turnaround). All 8 are net-new (the "Onward" overlap hit was a body-text mention of the word, not a source).

---

## 3. Pre-flight peek · source quality

- **Net-new:** all 8 verified net-new (0 chunked source-refs). None overlap BIOGRAPHY_FOUNDER_MEDIA core (Vreeland/Instagram/Branson/Kroc/Netflix/Sony) or MEDIA_BUSINESS (ESPN/SNL/HBO).
- **Clean text:** Sam Walton (96K pdf), Elon Musk (205K epub · 86MB but real text), Super Pumped (126K epub), Airbnb (88K epub).
- **mobi (need `ebook-convert` · calibre on PATH · no OCR):** Titan, The Fish That Ate the Whale, Pour Your Heart Into It, Onward.
- **No stubs, no scanned PDFs, no image-heavy, no broken formats** among these 8.
- **Recovery/acquisition items:** untouched (none here · the broken memoirs files Hit Men/Grace/Total Recall/The Mailroom are NOT in this set and remain recovery).

### SCALE note
8 founder books (~900K+ words; Titan/Rockefeller and Elon Musk are long). A mini-batch (~18-24 chunks) covers one founder per ~2-3 chunks. **Recommendation:** CORE = 7 distinct founders/companies (one Schultz book), defer the 2nd Schultz (Onward) as an optional companion · keeps the mini-batch one-arc-per-founder and tight. If the operator wants the full 8, it stays a mini-batch at the upper bound (~24-26 chunks).

---

## 4. Recommended inclusion / defer / exclude

### INCLUDE · CORE · 7 sources (LOCKED · one arc per founder/company)
1. **Sam Walton: Made In America** · Walmart · relentless cost discipline, expansion, operational obsession.
2. **Elon Musk** (Isaacson) · Tesla/SpaceX · scale ambition, risk tolerance, leadership contradictions, first-principles.
3. **Super Pumped** · Uber · blitzscale, category creation, the dark side of growth-at-all-costs (ethics).
4. **The Airbnb Story** · Airbnb · platform expansion, trust at scale, turning a small opening into a category.
5. **Titan** · Rockefeller / Standard Oil · capital control, consolidation, the original scale playbook (and its ethics).
6. **The Fish That Ate the Whale** · Sam Zemurray / United Fruit · the immigrant-operator myth, hustle to empire (and its dark geopolitics · ethics).
7. **Pour Your Heart Into It** · Schultz / Starbucks · brand-through-experience, scaling culture, the build arc.

### DEFER
- **Onward** (Schultz · the 2008 turnaround) · optional companion to Pour Your Heart Into It · defer to keep one-arc-per-founder, or add as an 8th if the operator wants the turnaround arc too.

### EXCLUDE
- BIOGRAPHY_FOUNDER_MEDIA core (already chunked) · MEDIA_BUSINESS sources (already chunked) · the broken/recovery memoirs (Hit Men, Grace, Total Recall, The Mailroom · not in this set) · the Chernow histories Grant + Washington (historical-biography lane, not founder second-tier) · CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources.

---

## 5. Estimated chunk yield

7 deep founder bios, ~3 chunks each + 1-2 synthesis:

| Source | Chunks |
|---|--:|
| Sam Walton | 3 |
| Elon Musk | 3 |
| Super Pumped (Uber) | 3 |
| The Airbnb Story | 2-3 |
| Titan (Rockefeller) | 3 |
| The Fish That Ate the Whale | 2-3 |
| Pour Your Heart Into It (Starbucks) | 2-3 |
| cross-source synthesis | 1-2 |

**Target: ~18-24 chunks. Acceptable range: 15-28.** (If Onward is added, ~21-26.) ID pattern `FOUNDER_SECOND_TIER_NNN`. 1-2 synthesis chunks.

---

## 6. Domain set (NO new domain · all verified to exist)

Anchored on `founder-psychology` (23). All proposed domains exist:

| Domain | Current | Use here |
|---|--:|---|
| `founder-psychology` | 23 | founder temperament, ambition, risk, contradictions, inevitability |
| `operator-doctrine` | 65 | operational obsession, standards, discipline at scale |
| `operator-process` | 67 | scaling systems, expansion mechanics |
| `strategy` | 166 | category creation, consolidation, platform expansion |
| `commercial-architecture` | 41 | business-model structure, moats, distribution |
| `brand` | 33 | brand-through-experience, myth-building, the founder-as-brand |
| `capital` | 9 | capital control, ownership, consolidation economics (Rockefeller, Walton) |
| `systems-thinking` | 38 | scale dynamics, network/flywheel effects |
| `culture` | 44 | LIGHT · scaling culture (Starbucks), the operator-as-myth |
| `ethics` | 26 | LIGHT · the dark side of scale (Uber, Standard Oil, United Fruit) where warranted |

**NO new domain.** Estimated distribution (indicative): founder-psychology ~6-7 · strategy ~4 · operator-doctrine ~3 · commercial-architecture ~3 · capital ~2 · brand ~2 · systems-thinking ~1-2 · ethics ~1-2 · operator-process ~1 · culture ~1. Finalized at chunk time.

### 7. NEW domain check (explicit)

No new domain is needed · all 10 candidate domains exist (founder-psychology is the anchor, as in BIOGRAPHY_FOUNDER_MEDIA). `ethics` is the only borderline-tempting addition for the dark-side-of-scale chunks (Uber/Standard Oil/United Fruit), but the existing `ethics` domain (26) covers it · NO new domain proposed. If a concept fits none of the 10, halt and surface rather than mint one.

---

## 8. How this mini-batch connects to the corpus

- **BIOGRAPHY_FOUNDER_MEDIA:** the first founder/taste/media arc layer · FOUNDER_SECOND_TIER extends it with scale/company-building arcs (Walmart, Tesla, Uber, Airbnb, Standard Oil, United Fruit, Starbucks) · same `founder-psychology` anchor.
- **MEDIA_BUSINESS:** the institutional/attention layer · this is the company-building/operator layer · complementary patterns of turning openings into institutions.
- **MONEY_OWNERSHIP:** the capital/ownership economics · here enacted (Rockefeller's consolidation, Walton's cost discipline, the ownership arcs) · `capital` domain shared.
- **EDGE_AND_OPERATING_DISCIPLINE:** the discipline/standards frameworks · here shown as operational obsession at scale (Walton, Schultz).
- **BATCH_009 / BATCH_009_EXPANSION:** positioning/category/challenger theory · here enacted (Airbnb category creation, Uber blitzscale, Starbucks brand-through-experience).
- **CURRENT_OPERATOR_REALITY_BRIEF:** the read-first current-state anchor (solo operator, ideation/build mode) · these arcs are held as pattern-library against current reality, not imposed.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** founder arcs are pattern-library / decision-support, NOT a directive for BJ to copy any founder or manufacture a myth · optionality preserved.
- **Future SNIPED direction (without deciding it):** supplies scale/company-building patterns the operator can draw from · reversible inputs.

---

## 9. This lane does NOT finalize brand direction (and arcs are pattern-library only)

Confirmed. FOUNDER_SECOND_TIER chunks founder/company-building biographies as pattern-library / decision-support. It does **not** decide SNIPED, SNIPED Media, or BASEPLATE direction, does **not** prescribe a founder for BJ to copy, and does **not** direct BJ to manufacture a founder myth or build a company at scale. Per the active guardrails and CURRENT_OPERATOR_REALITY_BRIEF, `sniped_relevance` frames each arc as a lens (what this operator did, why it worked, and its costs), with SNIPED's direction undecided and photography one option among several. The dark-side chunks (Uber/Standard Oil/United Fruit) are included precisely to keep the patterns honest, not aspirational.

---

## 10. Deliverables (produced only at the authorized ship step · NOT now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/FOUNDER_SECOND_TIER_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/founder_second_tier_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/FOUNDER_SECOND_TIER_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/FOUNDER_SECOND_TIER_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/FOUNDER_SECOND_TIER_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/FOUNDER_SECOND_TIER_COMPLETE.md` |
| Extract script | `scripts/extract_founder_second_tier.py` (epub via stdlib zipfile · pdf via pdftotext · mobi via ebook-convert) |
| Chunk writer | `scripts/write_founder_second_tier_chunks.py` |

Schema: the canonical 12-field JSONL. `batch_id` = `FOUNDER_SECOND_TIER`. source_file values resolve under `founder_second_tier_extracted/`. Copyright-safe quote discipline: in-copyright trade books · short illustrative lines only (target longest <= 14 words) · most chunks paraphrase. No OCR · ebook-convert (calibre) is on PATH for the 4 mobi (no new dependency).

---

## Constraints honored by this plan

- Did NOT extract, chunk, update master files, or commit.
- Did NOT modify any `raw/` source file · recovery/acquisition items reported only, untouched.
- No em-dashes.
- No new domain proposed (all 10 candidate domains exist · founder-psychology is the anchor).
- Does not finalize SNIPED / SNIPED Media / BASEPLATE direction · founder arcs are pattern-library only.
- Respects CURRENT_OPERATOR_REALITY_BRIEF (anchor, not chunked).
- Stops at the plan.

## Open questions · ALL RESOLVED (2026-05-23)

1. **CORE:** RESOLVED · the 7 distinct founders (one Schultz book · Pour Your Heart Into It). Onward deferred.
2. **Target band:** RESOLVED · ~18-24 chunks (range 15-28) · 1-2 synthesis chunks.
3. **Domain set:** RESOLVED · the 10 existing domains in section 6 · NO new domain (`ethics` light for the dark-side-of-scale chunks).
4. **Chernow histories:** RESOLVED · Grant + Washington deferred to a future historical-biography lane.

Plan is ready to ship on authorization (extract -> chunk -> validate -> consolidate). No new domain; founder-psychology is the anchor.
