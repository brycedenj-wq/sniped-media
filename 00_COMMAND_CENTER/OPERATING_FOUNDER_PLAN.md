# OPERATING_FOUNDER mini-batch · plan only · 2026-05-25

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document triages the operating_founder backlog, recommends a split architecture, names the first lane to execute, and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `97b9433 save session after POLITICAL_THEORY_DISCOURSES consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,609 · 10 numbered batches + 30 mini-batches · 62 official domains (75 combined keys).
- **Recovery program cleared; historical-biography cleared; the classical block CLOSED** (CLASSICAL_STRATEGY + CLASSICAL_HISTORY + MODERN_COMMAND_NAPOLEON + POLITICAL_THEORY_DISCOURSES). OPERATING_FOUNDER is the next lane named in the sequenced CLASSICAL_STRATEGY_OPERATING_CANON plan and the ORIGINAL_SOURCE_COMPLETION_AUDIT.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified · all in `raw/02_TIER_1_CANON_BOOKS/operating_founder/`)

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| The Founder's Dilemmas | Noam Wasserman | epub | 145,096 | CLEAN |
| The Goal | Eliyahu Goldratt | pdf | 143,658 | CLEAN (see note) |
| Blitzscaling | Reid Hoffman, Chris Yeh | epub | 86,781 | CLEAN |
| The Lean Startup | Eric Ries | pdf | 84,808 | CLEAN |
| Reengineering the Corporation | Hammer & Champy | pdf | 79,110 | CLEAN |
| The Hard Thing About Hard Things | Ben Horowitz | epub | 78,703 | CLEAN |
| The E-Myth Revisited | Michael Gerber | mobi | 66,284 | CLEAN |
| Amp It Up | Frank Slootman | pdf | 49,598 | CLEAN |
| Built to Sell | John Warrillow | pdf | 38,682 | CLEAN (see note) |
| **Traction** | Weinberg & Mares | epub | **0 (empty)** | **BROKEN** |

Read-only `pdftotext` / `ebook-convert`-to-/tmp probes (temp deleted; all 2026-05-1x mtimes unchanged). **9 clean sources · ~772,720 combined words.**

## 2. Source-quality / stub / scan check

- **9 clean, text-bearing sources** (word counts above). The mobi (E-Myth) extracts via `ebook-convert`; the pdfs via `pdftotext`; the epubs via `ebook-convert`. No OCR needed.
- **Note (The Goal):** `file` reports "5 pages" but `pdftotext` extracted 143,658 words of real text · the page-count is a PDF-metadata quirk, not a stub. **Built to Sell** similarly: `file` says "21 pages" but 38,682 words extracted (it is a short business parable). **At ship, sample each extracted .txt to confirm it is the actual book** (not repeated/garbage content) before chunking.
- **BROKEN:** **Traction (Weinberg & Mares)** is a 0-byte empty epub · contributes 0 · re-acquire a clean copy (its get-customers / `distribution`-channel material would otherwise be a strong fit). Flag for the recovery backlog.
- **OUT-OF-SCOPE files sitting in the folder (NOT operating-founder · EXCLUDE from this lane):**
  - `_OceanofPDF.com_The_88_Laws_Of_The_Masculine_Mindset_ - John Winters.pdf` (a self-help / "masculine mindset" book · not operating-founder · misfiled · skip / route elsewhere only on explicit operator instruction).
  - `Michael Jackson - Moonwalk.epub` (a music memoir · not operating-founder · misfiled · belongs to a biography/media register if anywhere · skip here).

## 3. Already-chunked overlap check (verified)

- **All 9 named titles + Traction are fully net-new** · 0 chunks as a source in any batch jsonl (verified by `source_title` + `author` search: lean startup / hard thing / horowitz / blitzscaling / hoffman / founder's dilemma / wasserman / the goal / goldratt / amp it up / slootman / reengineering / hammer / built to sell / warrillow / e-myth / gerber / traction / weinberg all return net-new).
- **Distinct from FOUNDER_SECOND_TIER** (the scale-arc pattern library · Titan/Rockefeller etc.), **BIOGRAPHY_FOUNDER_MEDIA**, **ONWARD_TURNAROUND** (Schultz/Onward), **HIGH_LEVEL_CONVOS** (transcripts), and **MEDIA_BUSINESS_RECOVERY** (Hit Men / The Mailroom) · those are founder/media biographies and turnaround/media arcs, NOT these operating-founder how-to texts. No title overlap.
- **Distinct from the classical block** (strategy treatises / ancient histories / Napoleon / Discourses) · different register entirely.

## 4. Architecture recommendation: SPLIT into a sequence of register-appropriate sub-lanes

9 clean sources spanning ~772K words across **four distinct registers** is too large and too heterogeneous for one mini-batch (it would either go shallow per book or balloon to 30+ chunks and mix registers · the corpus norm is ~16-18 chunks per 2-4 book lane). Recommended split into **three sequenced sub-lanes** (the operator's "founder-cost" register folds naturally into the startup/founder-reality lane):

1. **OPERATING_FOUNDER_STARTUP (recommended FIRST lane) · the start / survive / founder-reality register** · The Lean Startup (Ries · validated learning, build-measure-learn, MVP, pivot) + The Hard Thing About Hard Things (Horowitz · the CEO's hard decisions, the struggle, leading in crisis) + The Founder's Dilemmas (Wasserman · co-founder/equity/role pitfalls, rich-vs-king). ~308,607 words · the register most directly relevant to BJ's current build-mode / loading-the-backend stage.
2. **OPERATING_FOUNDER_SCALING (deferred) · the hypergrowth / intensity register** · Blitzscaling (Hoffman/Yeh) + Amp It Up (Slootman). ~136,379 words.
3. **OPERATING_FOUNDER_OPERATIONS (deferred) · the systems / process / owner-independence register** · The Goal (Goldratt · theory of constraints) + Reengineering the Corporation (Hammer/Champy) + The E-Myth Revisited (Gerber · systematize the small business) + Built to Sell (Warrillow · the owner-independent, sellable business). ~327,734 words.

**Naming note:** the operator's deliverable list (Sec. 16) uses umbrella `OPERATING_FOUNDER_*` names. If the operator accepts the split, the FIRST lane ships under `OPERATING_FOUNDER_STARTUP` (`OPERATING_FOUNDER_STARTUP_CHUNKS.jsonl`, `operating_founder_startup_extracted/`, etc.); if the operator prefers a single curated lane, the first lane keeps the umbrella `OPERATING_FOUNDER` name and chunks only the 3 startup-register books, deferring the rest. **Recommendation: the split with the `OPERATING_FOUNDER_STARTUP` batch_id.**

## 5. Recommended first lane: OPERATING_FOUNDER_STARTUP (include / defer / exclude)

- **INCLUDE (3 · CORE · curated · the start/survive/founder-reality register):**
  - The Lean Startup (Eric Ries) · pdf · ~84,808 words.
  - The Hard Thing About Hard Things (Ben Horowitz) · epub · ~78,703 words.
  - The Founder's Dilemmas (Noam Wasserman) · epub · ~145,096 words.
  - Combined ~308,607 words · curated, not exhaustive.
- **DEFER (subsequent OPERATING_FOUNDER sub-lanes):**
  - **OPERATING_FOUNDER_SCALING:** Blitzscaling + Amp It Up.
  - **OPERATING_FOUNDER_OPERATIONS:** The Goal + Reengineering + E-Myth + Built to Sell.
- **EXCLUDE (0 chunks):**
  - **Traction** (0-byte broken epub · re-acquire · flag for recovery backlog).
  - **The 88 Laws of the Masculine Mindset** + **Moonwalk** (misfiled, out-of-scope for operating-founder · skip).
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical source and every other-cluster source (FOUNDER_SECOND_TIER / BIOGRAPHY_FOUNDER_MEDIA / ONWARD_TURNAROUND / HIGH_LEVEL_CONVOS / the classical block / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2). CURRENT_IDENTITY sources.

## 6. Recommended chunk target / range (first lane)

- **Target:** ~14-16 chunks · **Range:** 12-18 (halt-and-report if outside).
- **Synthesis:** 1-2 closing synthesis chunks (the founder/operating pattern + the optionality guardrail).
- **Provisional per-source split:** Lean Startup ~4-5 · Hard Thing ~4-5 · Founder's Dilemmas ~4-5 · + 1-2 synthesis. Curated/representative from ~308K words, NOT chapter-by-chapter.

## 7. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `operator-doctrine` (97), `operator-process` (85), `founder-psychology` (32), `strategy` (194), `commercial-architecture` (53), `leadership` (51), `systems-thinking` (48), `distribution` (9), `ethics` (48).

| Domain | Planned use in the first lane |
|---|---|
| `operator-doctrine` (anchor) | The disciplined doctrine for building under uncertainty · validated learning as a discipline, pivot-or-persevere judgment, leading through "the struggle," the rich-vs-king choice held as doctrine. |
| `founder-psychology` | The founder's emotional reality (Horowitz's "struggle"); co-founder / relationship / role pitfalls and the rich-vs-king motivation (Wasserman). |
| `operator-process` | The build-measure-learn loop, the minimum viable product, innovation accounting / actionable (not vanity) metrics (Ries) · the operational machinery. |
| `strategy` | Pivot vs persevere as a strategic inflection; the engine of growth; the founder's strategic bets (Ries / Horowitz). |
| `leadership` | The CEO's job in crisis, hiring/firing, telling the hard truth, "take care of people, products, and profits, in that order" (Horowitz). |
| `commercial-architecture` | The business-model / growth-engine architecture beneath the product (Ries / Wasserman). |
| `systems-thinking` (if warranted) | The startup as an experiment system with feedback loops · used where squarely systemic. |
| `ethics` (if warranted) | Honesty in hard times, the CEO who tells the truth, founder integrity under pressure · used where the moral dimension is squarely present. |
| `distribution` (if warranted) | Go-to-market channel / customer-acquisition patterns · thin (count 9) · used only if clearly warranted (the strongest distribution source, Traction, is broken and deferred). |

### Domain issues to flag (important)

- **`product-development` does NOT exist** (ABSENT · verified). It will NOT be created · MVP / product-iteration material routes to `operator-process` + `strategy`.
- **`operations` and `scaling` ALREADY EXIST** in the corpus (pre-existing domains), but they are on the operator's forbidden list for this lane. **They will NOT be created (they already exist) and will NOT be used or grown by this lane** · operations material routes to `operator-process`; scaling material routes to `operator-process` / `strategy` / `founder-psychology` (relevant mainly to the deferred SCALING sub-lane, still routed to existing non-forbidden domains).
- **`startup`, `entrepreneurship`, `founder`, `business` do NOT exist and will NOT be created** · startup/entrepreneurship -> operator-doctrine / operator-process / strategy; founder -> founder-psychology / leadership; business -> commercial-architecture / operator-process.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 8. Connections (cross-references this lane opens)

- **FOUNDER_SECOND_TIER + BIOGRAPHY_FOUNDER_MEDIA + ONWARD_TURNAROUND:** the founder-arc / scale / turnaround pattern libraries · OPERATING_FOUNDER_STARTUP is the early-build, how-to-operate companion to those biographical-arc lanes (same `founder-psychology` family · method vs narrative).
- **HIGH_LEVEL_CONVOS:** the practical operator-conversation lessons (capital, deal structure, operator judgment) · this lane supplies the canonical book-grade method beneath those transcripts.
- **EDGE_AND_OPERATING_DISCIPLINE + the operator-process / operator-doctrine lanes:** the execution-discipline family this deepens (ICP-as-method, weekly reflection) gains the build-measure-learn / hard-decision layer.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails + ORIGINAL_SOURCE_COMPLETION_AUDIT:** the optionality discipline governs this lane; the audit named the operating_founder cluster as remaining high-value backlog. CURRENT_IDENTITY remains plan-only / NOT extracted.

## 9. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the books as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk(s) making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 10. Operating-founder material = decision-support / pattern-library only (not a directive)

The Lean Startup, The Hard Thing About Hard Things, and The Founder's Dilemmas are held strictly as a **decision-support / pattern-library layer**: transferable patterns of building under uncertainty, validated learning, founder decision-making, co-founder/equity judgment, and leading through hard times. It is **NOT a directive that BJ become a startup founder, a VC-style operator, a software CEO, or an agency owner**, and not a mandate to raise venture capital, hyperscale, or build a software company. The methods are read as a transferable operating toolkit decoupled from the specific startup/VC context that produced them, applied to BJ's actual stage (a solo field-engineer in build-mode, loading the backend before final brand/offer/company-architecture decisions). Photography remains one option among several.

## 11. Deliverables for the future ship (NOT created now)

For the recommended first lane (batch_id `OPERATING_FOUNDER_STARTUP`):

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/OPERATING_FOUNDER_STARTUP_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/operating_founder_startup_extracted/` (3 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/OPERATING_FOUNDER_STARTUP_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/OPERATING_FOUNDER_STARTUP_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/OPERATING_FOUNDER_STARTUP_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/OPERATING_FOUNDER_STARTUP_COMPLETE.md` |
| Extraction script | `scripts/extract_operating_founder_startup.py` |
| Chunk writer | `scripts/write_operating_founder_startup_chunks.py` |

(If the operator instead collapses to a single curated lane, the umbrella `OPERATING_FOUNDER_*` paths from the task spec apply, chunking only the 3 startup-register books and deferring the rest.) Schema: the canonical 12-field JSONL · `batch_id` = `OPERATING_FOUNDER_STARTUP` (or `OPERATING_FOUNDER`) · `chunk_id` pattern `OPERATING_FOUNDER_STARTUP_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · 3 sources · no new domain · startup/entrepreneurship/founder/business/operations/scaling NOT created-or-used · product-development NOT created · Traction 0 · misfiled out-of-scope files 0 · deferred SCALING/OPERATIONS sources 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 12. Projected post-consolidation state (for reference · NOT applied now)

If the first lane ships at the mid-target (~15) and consolidates: 1,609 + ~15 = ~1,624 chunks · 10 numbered batches + 31 mini-batches · 62 domains (NO new domain · bumps to operator-doctrine [anchor] / founder-psychology / operator-process / strategy / leadership / commercial-architecture, plus systems-thinking / ethics / distribution where warranted). Exact counts finalized at ship/consolidation time. Subsequent OPERATING_FOUNDER sub-lanes: OPERATING_FOUNDER_SCALING (Blitzscaling + Amp It Up) and OPERATING_FOUNDER_OPERATIONS (The Goal + Reengineering + E-Myth + Built to Sell). Then NETWORK_DISTRIBUTION, SALES_POSITIONING (post overlap-audit), DECISION_JUDGMENT, Tier-2 (incl the Greene trio), BRAND_CANON.

## 13. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,609.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 14. Next step (operator decision · do not start without authorization)

Authorize the **OPERATING_FOUNDER_STARTUP** first lane (3 curated sources · The Lean Startup + The Hard Thing About Hard Things + The Founder's Dilemmas · target ~14-16 · existing domains only · `operator-doctrine` anchor · no new domain · startup/entrepreneurship/founder/business/operations/scaling NOT created-or-used · product-development NOT created · Traction broken/deferred · misfiled files excluded · Bible excluded · curated, not exhaustive · decision-support not a directive), then commit the ship outputs, then consolidate. The SCALING and OPERATIONS sub-lanes follow as separate plan/ship/consolidate cycles.
