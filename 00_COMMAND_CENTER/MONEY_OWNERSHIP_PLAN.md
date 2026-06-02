# MONEY_OWNERSHIP mini-batch · PLAN

**Date planned:** 2026-05-23
**Status:** PLAN ONLY · not extracted, not chunked, master files untouched, not committed.
**Batch kind:** mini-batch (descriptive slug · the 14th mini-batch) · curated CORE scale (operator-decided · see section A).

> **OPERATOR DECISIONS APPLIED (2026-05-23 · locked):**
> 1. **NEW domain `capital` APPROVED.** `investing` NOT created (held as unnecessary for now). On ship + consolidation this lane will register `capital` as the 61st official domain (60 to 61).
> 2. **Curated mini-batch scale** (not a full numbered batch).
> 3. **6 CORE sources locked** (section 4).
> 4. **Deferred** the 7 long/deep finance texts; **excluded** Poor Charlie's Almanack + Naval (already chunked); **Margin of Safety = recovery** (scanned); **memoirs_biographies deferred** to a separate biography/founder-media lane.
> 5. **Identity optionality preserved** · ownership/capital thinking is a decision-support lens, not a pivot · no final SNIPED / SNIPED Media / BASEPLATE direction.

---

## 0. Verified starting state

- **Head commit:** `cf912e9 save CURRENT_SOURCE_AUDIT checkpoint`
- **Working tree:** clean before this plan.
- **Total chunks:** 1,311 · 10 numbered batches + 13 mini-batches · 60 official domains (73 combined_domain_counts keys).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **No lane started:** no `MONEY_OWNERSHIP_CHUNKS.jsonl`, no extracted dir, no COMPLETE marker, no prior plan.

---

## 1. Goal + theme

Ownership, wealth, capital allocation, investing judgment, private equity, founder economics, compounding, risk, leverage, incentives, cash flow, enterprise value, long-term capital thinking, and how the operator avoids staying only a talented service provider.

The clean, net-new, on-theme source set is the `raw/03_TIER_2_CANON_BOOKS/investing_finance/` folder, plus the SNIPED-authored `Money_Wealth_Getting_Ahead.docx`.

---

## TWO FLAGS · RESOLVED BY OPERATOR (2026-05-23)

### A. SCALE FLAG · RESOLVED: curated mini-batch
The net-new usable investing_finance books total **~1.5M+ words across 12 dense books** (Snowball 412K, Security Analysis 396K, Power Law 198K, Sovereign Individual 160K, King of Capital 128K, Lords of Easy Money 126K, Essays of Buffett 119K, Mastering the Market Cycle 84K, Most Important Thing 65K, Psychology of Money 53K, Intelligent Investor 45K, New Tycoons azw3) · numbered-batch scale. **DECISION: ship the curated CORE of 6 ownership/capital titles as a mini-batch now** (section 4). The deep/long texts are deferred (section 4 DEFER).

### B. DOMAIN FLAG · RESOLVED: approve `capital`, hold `investing`
Checked against `combined_domain_counts`: `capital`, `ownership`, `investing`, `wealth`, `economics` are all MISSING; only `finance` (2) exists. **DECISION (operator-approved): introduce ONE new domain `capital`** (capital allocation / ownership economics / PE / VC / enterprise value / compounding). **`investing` is NOT created** (held as unnecessary for now). All other concepts route to existing domains. On ship + consolidation, official domains go **60 to 61** (`capital` is the 61st). This is the first new domain since LITERARY_CANON_DYSTOPIAN's `systems-thinking`.

The reference table and original options below are retained for the audit trail.

### (reference · original domain check · per requirement #7)
Checked against `combined_domain_counts`:

| Proposed domain | Status |
|---|---|
| `capital` | **MISSING** (not an official domain) |
| `ownership` | **MISSING** |
| `investing` | **MISSING** |
| `wealth` | **MISSING** |
| `economics` | **MISSING** |
| `finance` | EXISTS (only 2 chunks) |
| `strategy` | EXISTS (156) |
| `commercial-architecture` | EXISTS (38) |
| `operator-doctrine` | EXISTS (61) |
| `systems-thinking` | EXISTS (34) |
| `ethics` | EXISTS (26) |
| `lineage` | EXISTS (20) |
| `small-company-strategy` | EXISTS (9) |

This lane is fundamentally about capital / ownership / investing, and those domains do **not** exist. The corpus has held a strict no-new-domain discipline for 13 consecutive mini-batches. This is a real decision, NOT something to resolve silently. **Options:**
- **Option B1 (recommended · operator approval required):** introduce a small, deliberate set of NEW domains: `capital` (capital allocation / ownership economics / PE / VC), and optionally `investing` (investing judgment / risk / market cycles). This is the honest home for the material and keeps `strategy`/`commercial-architecture` from being distorted.
- **Option B2 (no new domain):** route everything to existing domains: `finance` (deepen from 2), `strategy`, `commercial-architecture`, `operator-doctrine`, `systems-thinking`, `ethics`. Cost: `finance` jumps from 2 to ~10+ and the capital/ownership distinction is lost inside `strategy`.
- **Option B3:** defer the lane until the operator rules on domains.

No domains will be created without explicit operator approval. The plan does not pre-decide this.

---

## 2. Candidate inventory

### Group A · `raw/03_TIER_2_CANON_BOOKS/investing_finance/` (14 files)

| File | Author · Title | Type | Words | Status |
|---|---|---|--:|---|
| Intelligent Investor | Benjamin Graham | pdf | 45,414 | net-new |
| Poor Charlie's Almanack | Munger/Kaufman | pdf (184MB) | 186,925 | **ALREADY CHUNKED (BATCH_002)** |
| Security Analysis (6th) | Graham/Dodd/Buffett | pdf | 396,564 | net-new (huge) |
| The Lords of Easy Money | Christopher Leonard | epub | 126,267 | net-new |
| King of Capital (Blackstone) | Carey/Morris | epub | 127,983 | net-new |
| Mastering the Market Cycle | Howard Marks | epub | 84,127 | net-new |
| The Most Important Thing | Howard Marks | pdf | 65,219 | net-new |
| The Sovereign Individual | Davidson/Rees-Mogg | pdf | 160,178 | net-new |
| The New Tycoons (PE) | Jason Kelly | azw3 | (ebook-convert) | net-new |
| The Psychology of Money | Morgan Housel | pdf | 52,730 | net-new |
| The Snowball (Buffett bio) | Alice Schroeder | pdf | 412,025 | net-new (huge) |
| The Power Law (VC) | Sebastian Mallaby | epub | 198,256 | net-new |
| Margin of Safety | Seth Klarman | pdf | **0 (SCANNED)** | **BROKEN · OCR-blocked** |
| The Essays of Warren Buffett | Buffett/Cunningham | epub | 119,352 | net-new |

### Group B · loose money/ownership sources

| File | Notes |
|---|---|
| `Money_Wealth_Getting_Ahead.docx` (raw root) | SNIPED-authored synthesis · "Constraint Elimination, Financial Architecture & Leverage Systems" · net-new · on-theme · deferred here from EDGE |
| `The Almanack of Naval Ravikant` (Tier-2 root) | **ALREADY CHUNKED (BATCH_003)** · wealth/leverage · exclude |

### Group C · memoirs_biographies (the audit flagged it · but mostly OFF-THEME for money)
The `memoirs_biographies/` folder (~17 staged) is general founder/media biography (Branson, Schultz, Vreeland, Coddington, Arnold/Total Recall, etc.). The on-theme money bios are already captured in investing_finance (Snowball, King of Capital). **Recommendation: DEFER memoirs_biographies to a separate biography/founder-media lane**, not this one. (Exception: none needed here.)

---

## 3. Pre-flight peek · source quality

- **Scanned / broken:** Margin of Safety (Klarman) extracts 0 words via pdftotext · image-only scan · OCR-blocked · **BROKEN_OR_NEEDS_REACQUISITION** (re-acquire a text edition). Not chunkable now.
- **Already chunked (exclude):** Poor Charlie's Almanack (BATCH_002 · the investing_finance PDF is the same book) · The Almanack of Naval Ravikant (BATCH_003).
- **Overlap-hit verification:** "the most important thing", "snowball", "power law" matched only as body-text phrases in other chunks, NOT as source_title/source_file · the Howard Marks / Schroeder / Mallaby books are genuinely net-new.
- **Format note:** The New Tycoons is `.azw3` · needs `ebook-convert` (calibre, on PATH) · no OCR.
- **All other 11 net-new books** extract cleanly (epub via stdlib zipfile, pdf via pdftotext). No stubs.
- **Recovery/acquisition items:** untouched · none involved (Margin of Safety becomes a new recovery flag).

---

## 4. Recommended inclusion / defer / exclude

### INCLUDE · curated CORE (LOCKED · 6 sources)
The highest-signal ownership / capital-thinking titles most relevant to the operator's "avoid staying only a talented service provider" question:
1. **The Psychology of Money** (Housel) · behavior, wealth, compounding, enough.
2. **The Essays of Warren Buffett** (Buffett/Cunningham) · owner-economics, capital allocation, intrinsic value.
3. **The Most Important Thing** (Howard Marks) · risk, second-level thinking, market cycles.
4. **King of Capital** (Blackstone) · private equity / ownership economics / enterprise value.
5. **The Power Law** (Mallaby) · venture capital, power-law returns, the economics of ownership stakes.
6. **Money_Wealth_Getting_Ahead.docx** · the SNIPED-authored leverage/wealth synthesis.

### DEFER (to a future MONEY_OWNERSHIP_EXPANSION or numbered batch)
The deep / very long value-investing + macro texts: Security Analysis (396K), The Snowball (412K bio), Intelligent Investor, Mastering the Market Cycle, The Sovereign Individual, The Lords of Easy Money, The New Tycoons. High-value but heavy · better as a second pass once domains are settled.

### EXCLUDE
- Poor Charlie's Almanack (chunked BATCH_002) · The Almanack of Naval Ravikant (chunked BATCH_003).
- Margin of Safety (scanned · recovery item).
- memoirs_biographies folder (off-theme · defer to a biography lane).

---

## 5. Estimated chunk yield

Scope-dependent:
- **Curated CORE (6 sources):** ~18-24 chunks (4-5 per book + 1-2 synthesis). Target ~18-24, range 15-28. (This exceeds a small mini-batch; the 6 books are substantial.)
- **Full numbered batch (12 books + docx):** ~50-70 chunks (a BATCH_011-scale effort).

ID pattern `MONEY_OWNERSHIP_NNN`. 1-2 cross-source synthesis chunks.

---

## 6. Domain set (LOCKED)

**ONE new domain: `capital`** (operator-approved · capital allocation / ownership economics / PE / VC / enterprise value / compounding / leverage-as-capital). All other concepts route to EXISTING domains: `strategy`, `commercial-architecture`, `operator-doctrine`, `systems-thinking`, `finance` (deepen from 2), `ethics` (incentives/risk where warranted). **`investing` is NOT created** (held). `lineage` only if a genuinely lineage-relevant ownership chunk appears (unlikely).

Estimated distribution (curated CORE, indicative): `capital` ~6-8 · `strategy` ~3-4 · `systems-thinking` ~3 · `operator-doctrine` ~2-3 · `finance` ~2 · `commercial-architecture` ~2 · `ethics` ~1. Finalized at chunk time.

---

## 7. NEW domain decision (LOCKED)

`capital`, `ownership`, `investing`, `wealth`, `economics` were all MISSING. **Operator approved exactly ONE new domain: `capital`.** `investing` is NOT created (held as unnecessary for now). No other new domain. On ship + consolidation the official domain count goes 60 to 61 (`capital` is the 61st). This is the only sanctioned new-domain introduction for this lane · any further candidate new domain at chunk time must halt and re-surface to the operator.

---

## 8. How this mini-batch connects to the corpus

- **BATCH_009 / BATCH_009_EXPANSION (commercial strategy):** B009 is how to sell and price; MONEY_OWNERSHIP is what to do with the proceeds · capital allocation, ownership stakes, compounding · the layer above revenue.
- **EDGE_AND_OPERATING_DISCIPLINE:** energy/goal discipline directs the work; MONEY_OWNERSHIP supplies the economic end the discipline compounds toward (owner outcomes, not just service income).
- **BATCH_008 (AI/tech canon):** AI leverage (labor + code) pairs with capital leverage · the Naval leverage logic (already chunked) gets its capital-side complement.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the "avoid staying only a talented service provider" theme is decision-support about the operator's economic future · it must stay an OPTION-set (ownership thinking as a lens), NOT a decision that SNIPED becomes an investment vehicle or that the operator pivots away from the craft.
- **Future SNIPED direction (without deciding it):** supplies the capital/ownership frameworks the operator can apply to whatever direction emerges · reversible inputs, not a verdict.

---

## 9. This lane does NOT finalize brand direction

Confirmed. MONEY_OWNERSHIP chunks general capital / ownership / investing theory. It does **not** decide SNIPED, SNIPED Media, or BASEPLATE direction, does not commit the operator to an investing path, and does not pivot away from the photography craft. Per the active guardrails, `sniped_relevance` frames everything as decision-support / optionality-preserving (ownership and capital thinking as lenses), with direction undecided and photography one option among several.

---

## 10. Deliverables (produced only at the authorized ship step · NOT now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/MONEY_OWNERSHIP_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/money_ownership_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/MONEY_OWNERSHIP_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/MONEY_OWNERSHIP_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/MONEY_OWNERSHIP_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/MONEY_OWNERSHIP_COMPLETE.md` |
| Extract script | `scripts/extract_money_ownership.py` (epub via stdlib zipfile · pdf via pdftotext · azw3 via ebook-convert · docx via pandoc) |
| Chunk writer | `scripts/write_money_ownership_chunks.py` |

Schema: the canonical 12-field JSONL. `batch_id` = `MONEY_OWNERSHIP`. source_file values resolve under `money_ownership_extracted/`. Copyright-safe quote discipline: in-copyright trade books · short illustrative lines only (target longest <= 14 words) · most chunks paraphrase. No OCR · no new dependencies (ebook-convert/pandoc/pdftotext already on PATH).

---

## Constraints honored by this plan

- Did NOT extract, chunk, update master files, or commit.
- Did NOT modify any `raw/` source file · recovery/acquisition items untouched.
- No em-dashes.
- **No new domain created** · the domain issue is flagged for operator decision (requirement #7-8).
- Does not finalize SNIPED / SNIPED Media / BASEPLATE direction (optionality preserved).
- Stops at the plan.

## Open questions · ALL RESOLVED (2026-05-23)

1. **DOMAIN decision:** RESOLVED · approve ONE new domain `capital`; `investing` NOT created.
2. **SCALE decision:** RESOLVED · curated CORE mini-batch (6 sources · ~18-24 chunks).
3. **memoirs_biographies:** RESOLVED · deferred to a separate biography/founder-media lane.
4. **CORE confirm:** RESOLVED · the 6 titles in section 4 are locked (Psychology of Money, Essays of Warren Buffett, The Most Important Thing, King of Capital, The Power Law, Money_Wealth_Getting_Ahead.docx).

Plan is ready to ship on authorization (extract -> chunk -> validate -> consolidate). The ship will register `capital` as the 61st official domain.
