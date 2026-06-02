# DEEP_FINANCE_EXPANSION mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation. Stop after writing this plan.

**Revision (2026-05-24, post-RECOVERY_INTAKE_CHECK · committed `9814893`):** Margin of Safety (Klarman) has been recovered as a usable epub (~72,828 words) and is added as the 8th CORE source. The earlier exclusion (it was a scanned/image-only PDF) is superseded. Source count 7 → 8; target band raised to ~25-31 (hard range 22-36). The recovered file currently lives in the source universe (`~/Downloads/    SNIPED_OS/`), not yet in `raw/`; it awaits a future authorized routing/staging pass. All other decisions unchanged (capital anchors · NO new domain · `economics` NOT created · identity optionality guardrails active).

## 0. Verified starting state

- **Head commit:** `710338a plan RECOVERY_REACQUISITION pass`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,403 · **numbered batches:** 10 · **mini-batches:** 18 · **official domains:** 62 (keys 75).
- **MONEY_OWNERSHIP:** complete and canonical · `capital` is the registered 61st domain (count 10) · `finance` exists (count 4).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.

## 1. Theme

Deep capital and finance expansion after MONEY_OWNERSHIP: value investing, market cycles, risk, balance-sheet logic, long-term compounding, monetary systems, private capital, sovereign/technology macro forces, power-law capital, and the mental models needed to understand ownership beyond service income. The depth layer beneath the MONEY_OWNERSHIP foundation, held strictly as a decision-support lens read against CURRENT_OPERATOR_REALITY_BRIEF.

## 2. Candidates located + inventory (8 sources · 7 staged in `raw/03_TIER_2_CANON_BOOKS/investing_finance/` · Margin of Safety recovered in the source universe, pending staging)

| # | Title (author) | Format | Size | Pages/words | Extraction method | Location |
|---|---|---|---|---|---|---|
| 1 | Security Analysis · 6th ed (Graham, Dodd; Buffett foreword) | pdf | 4.8 MB | 1,095 pp · 391,812 words | pdftotext | raw/ |
| 2 | The Snowball: Warren Buffett and the Business of Life (Schroeder) | pdf | 7.4 MB | 641 pp · 411,951 words | pdftotext | raw/ |
| 3 | The Intelligent Investor (Graham) | pdf | 0.6 MB | 142 pp · 45,067 words | pdftotext | raw/ |
| 4 | Mastering the Market Cycle (Howard Marks) | epub | 3.9 MB | ~83,675 words | ebook-convert | raw/ |
| 5 | The Sovereign Individual (Davidson, Rees-Mogg) | pdf | 1.3 MB | 331 pp · 160,083 words | pdftotext | raw/ |
| 6 | The Lords of Easy Money (Christopher Leonard) | epub | 4.9 MB | ~123,192 words | ebook-convert | raw/ |
| 7 | The New Tycoons: Inside the Trillion Dollar Private Equity Industry (Jason Kelly) | azw3 | 0.4 MB | ~80,071 words | ebook-convert | raw/ |
| 8 | Margin of Safety: Risk-Averse Value Investing (Klarman) | epub | 0.6 MB | ~72,828 words | ebook-convert | source universe (recovered · pending staging) |

All extractors are on PATH (pdftotext, ebook-convert/calibre). No OCR, no new dependencies. Combined raw volume ~1.37M words across 8 deep books. Margin of Safety (source 8) was recovered after RECOVERY_INTAKE_CHECK as a usable epub and will be staged into `raw/03_TIER_2_CANON_BOOKS/investing_finance/` (replacing the old scanned PDF) in a future authorized routing/staging pass.

## 3. Pre-flight peek (read-only · PDFs via pdftotext-to-/tmp, ebooks via ebook-convert-to-/tmp · temp deleted · raw untouched)

- **Security Analysis:** 1,095 pp · 391,812 words · clean text layer. (`file` reported "0 pages" from an unreadable header, but pdfinfo/pdftotext extract the full text fine.) Foundational, massive.
- **The Snowball:** 641 pp · 411,951 words · clean text layer. Full-length Buffett biography.
- **The Intelligent Investor:** 142 pp · 45,067 words · clean text layer **but appears ABRIDGED / partial** (the full Collins Business edition with Zweig commentary is ~640 pp). Usable for the core value-investing principles (Mr. Market, margin-of-safety concept, defensive vs enterprising investor), but flag the abridgement · verify completeness at extraction; do NOT over-chunk it.
- **Mastering the Market Cycle:** ~83,675 words · converts cleanly · NOT a stub.
- **The Sovereign Individual:** 331 pp · 160,083 words · clean text layer.
- **The Lords of Easy Money:** ~123,192 words · converts cleanly · NOT a stub.
- **The New Tycoons:** azw3 (Mobipocket-family) · ~80,071 words · converts cleanly · NOT a stub.
- **Margin of Safety (recovered):** epub · ~72,828 words · converts cleanly · NOT a stub. Per RECOVERY_INTAKE_CHECK (`9814893`), the old staged copy was a scanned/image-only PDF (68 pp · 0 extractable words); BJ re-acquired a clean epub now sitting in the source universe. It is usable and on-theme (risk-averse value investing, margin-of-safety discipline · complements Graham's Security Analysis / Intelligent Investor).
- **No scans, no 0-byte stubs, no duplicates, no unsupported formats, no off-theme sources.** All 8 are usable.

## 4. Already-chunked overlap check

- **All 8 are net-new** (0 hits as source_title/source_file across every `*_CHUNKS.jsonl` · Margin of Safety also confirmed 0 already-canonical chunks in RECOVERY_INTAKE_CHECK).
- **Author-overlap note (not a duplicate):** Howard Marks is already in the corpus via *The Most Important Thing* (MONEY_OWNERSHIP · 4 chunks · risk, second-level thinking). **Mastering the Market Cycle is a DISTINCT Marks book** (the cycle-positioning deep dive). Chunks must complement, not restate, MONEY_OWNERSHIP's Marks chunks (cycle mechanics + where-we-are positioning, not generic risk).
- **Thematic-adjacency notes (distinct books, no overlap):** King of Capital (Blackstone history · MONEY_OWNERSHIP) and The Power Law (venture · MONEY_OWNERSHIP) are private-capital-adjacent to The New Tycoons (a PE-industry overview), but all three are distinct books; The New Tycoons is the industry-wide ownership lens. Essays of Warren Buffett (MONEY_OWNERSHIP) is distinct from both Security Analysis (Graham/Dodd valuation method) and The Snowball (Schroeder biography).

## 5. Recommendation: INCLUDE all 8

INCLUDE all 8 candidates. All are clean, net-new, on-theme, supported formats. The Intelligent Investor is included with the abridgement caveat (extract its core principles, keep its chunk count modest).

**Margin of Safety (Klarman) is now INCLUDED as the 8th CORE source.** It was previously excluded as a scanned/image-only PDF (68 pp · 0 extractable words) per RECOVERY_REACQUISITION_PLAN.md. After RECOVERY_INTAKE_CHECK (`9814893`), BJ re-acquired a clean **epub** (~72,828 words) that converts and extracts fine. That earlier exclusion is therefore **superseded**. The recovered epub currently lives in the source universe (`~/Downloads/    SNIPED_OS/`) and will be staged into `raw/03_TIER_2_CANON_BOOKS/investing_finance/` (replacing the old scanned PDF) in a future authorized routing/staging pass · it is NOT moved here. No other exclusions.

## 6. Mini-batch vs numbered batch vs split

**Recommendation: ONE curated mini-batch** (the 19th mini-batch · `DEEP_FINANCE_EXPANSION`), NOT a numbered BATCH_011, and NOT split into two by default.

Rationale:
- **Not a numbered batch.** Numbered batches are the corpus's major foundational pillars (70-160 chunks). Turning 8 finance books into a numbered batch (~80+ chunks) would over-index the corpus on finance and cut against the operator's stance that capital/finance is a **decision-support lens, not a directive to become a finance brand**. MONEY_OWNERSHIP (21 chunks) is the precedent: the capital lane is a curated mini-batch, and this is its depth extension.
- **Not split by default.** The 8 cluster into two clean sub-themes: **value-investing / compounding** (Security Analysis, The Intelligent Investor, The Snowball, Mastering the Market Cycle, Margin of Safety) and **macro / monetary / private-capital** (The Sovereign Individual, The Lords of Easy Money, The New Tycoons). A single curated mini-batch covers both with balanced, principle-level depth and avoids fragmentation. If the operator prefers tighter passes, the natural split is those two halves (5 + 3 books) as `DEEP_FINANCE_VALUE` + `DEEP_FINANCE_MACRO` · flagged as an option, not the default.

## 7. Estimated chunk yield + target range

- **Target:** ~25-31 chunks.
- **Hard range:** 22-36 (halt and surface if outside).
- **Indicative per-source allocation** (principle-level, content-faithful at chunk time):
  - Security Analysis 4 · The Snowball 3 · The Intelligent Investor 2-3 (abridged · keep modest) · Mastering the Market Cycle 3 · Margin of Safety 2-3 (margin-of-safety discipline, risk-aversion, value-vs-price · complements Graham, keep modest to avoid overlap) · The Sovereign Individual 3 · The Lords of Easy Money 3 · The New Tycoons 3 · cross-source synthesis 2.
- Depth is principle-extraction, not summary; the giant books (Security Analysis, The Snowball) are sampled for their durable models, not exhaustively chunked. Margin of Safety and The Intelligent Investor both orbit Graham's margin-of-safety idea, so their chunks must stay distinct (Klarman = risk-aversion + value-investing-as-discipline; Graham = Mr. Market + defensive vs enterprising investor).

## 8. Domain set (EXISTING domains only · NO new domain · `capital` anchors)

| Domain | Indicative chunks | What it carries |
|---|---:|---|
| capital (anchor) | ~8 | owner economics, compounding, private-capital/PE ownership, capital allocation, power-law capital |
| finance | ~5 | valuation method, balance-sheet logic, value investing, margin-of-safety concept, intrinsic value |
| systems-thinking | ~4 | market cycles, monetary systems, the Fed/easy-money machine, sovereign/technology macro forces |
| strategy | ~3 | long-term positioning, cycle-aware decision-making, contrarian/second-level thinking |
| commercial-architecture | ~2 | private-equity ownership structures, the trillion-dollar PE model, who-owns-what |
| operator-doctrine | ~1 | patience, temperament, risk discipline as operating practice |
| ethics | ~1 (if warranted) | consequences of easy money / PE "owning everything" / wealth concentration |

All seven domains pre-exist (capital 10, finance 4, systems-thinking 41, strategy 169, commercial-architecture 44, operator-doctrine 69, ethics 30). `ethics` is conditional (included only if the macro/monetary content genuinely warrants).

## 9. Domain decision: `economics` is NOT created

- **`economics` does NOT exist in the corpus** (verified · not in combined_domain_counts). Per the operator instruction ("economics only if it already exists"), it is **NOT created**. The macro/monetary content (The Lords of Easy Money, The Sovereign Individual) that would naturally route to "economics" is instead routed to **`systems-thinking`** (monetary systems, cycles, macro forces as systems) and **`capital`/`strategy`** (monetary forces as they bear on ownership and positioning). **NO new domain is introduced.** `capital` anchors the lane.

## 10. Connections to existing lanes + the brief

- **MONEY_OWNERSHIP:** the direct parent. That lane installed the foundation (Housel wealth psychology, Essays of Warren Buffett, Marks *The Most Important Thing*, King of Capital, The Power Law, the SNIPED Money/Wealth synthesis). DEEP_FINANCE_EXPANSION is the depth layer beneath it: the primary valuation method (Graham/Dodd), the compounding/temperament biography (Buffett/Schroeder), cycle mechanics (Marks), and the macro/monetary/private-capital forces. Same `capital` anchor.
- **FOUNDER_SECOND_TIER:** Rockefeller's consolidation + capital control and the founder ownership arcs are here given their financial-theory substrate (valuation, capital allocation, compounding).
- **MEDIA_BUSINESS:** recurring revenue + ownership-of-attention as a capital asset · the PE/ownership lens (The New Tycoons) reads against the media-empire ownership patterns.
- **EDGE_AND_OPERATING_DISCIPLINE:** risk judgment, patience, and strategic patience as operating discipline · the temperament side of value investing and cycle positioning.
- **CURRENT_OPERATOR_REALITY_BRIEF:** referenced in every chunk. The mental models are decision-support for how BJ understands ownership beyond service income (a solo field-engineer/operator loading the backend), NOT a directive. The "avoid permanent service-provider status" thread from MONEY_OWNERSHIP continues here as a lens.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** fully honored (see 11-12).

## 11. Identity optionality confirmation

This lane does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction. SNIPED remains the live operator identity/container; SNIPED Media the existing photography company; BASEPLATE a possible historical rebrand asset, not the decided future. Every chunk frames the finance content as a decision-support / pattern-library LENS read against CURRENT_OPERATOR_REALITY_BRIEF. Photography remains one option among several.

## 12. Capital/finance thinking is a decision-support lens only

The capital/finance models are **NOT a directive that BJ become an investor or a finance/investing brand.** They are mental models for understanding ownership, compounding, risk, cycles, and capital beyond service income, held as lenses against current reality (early ideation/build, not a finance venture). A closing synthesis chunk will make this optionality discipline explicit (mirroring MONEY_OWNERSHIP and the FOUNDER_SECOND_TIER / ONWARD_TURNAROUND precedents).

## 13. Deliverables (created only when extraction/chunking is later authorized · NOT now)

- `01_KNOWLEDGE_BASE/batches/DEEP_FINANCE_EXPANSION_CHUNKS.jsonl` (12-field canonical schema · batch_id `DEEP_FINANCE_EXPANSION`)
- `01_KNOWLEDGE_BASE/batches/deep_finance_expansion_extracted/` (8 normalized .txt)
- `01_KNOWLEDGE_BASE/summaries/DEEP_FINANCE_EXPANSION_SUMMARY.md`
- `01_KNOWLEDGE_BASE/indexes/DEEP_FINANCE_EXPANSION_SOURCE_INDEX.md`
- `00_COMMAND_CENTER/batch_logs/DEEP_FINANCE_EXPANSION_EXTRACTION_LOG.md`
- `00_COMMAND_CENTER/batch_logs/DEEP_FINANCE_EXPANSION_COMPLETE.md`
- `scripts/extract_deep_finance_expansion.py`
- `scripts/write_deep_finance_expansion_chunks.py`

(This plan file `00_COMMAND_CENTER/DEEP_FINANCE_EXPANSION_PLAN.md` is the only artifact written now.)

## 14-18. Scope guards for this planning pass

- **14. Do not extract.** Honored (the section-3 peeks went to /tmp and were deleted · the deliverable `deep_finance_expansion_extracted/` was NOT created).
- **15. Do not chunk.** Honored.
- **16. Do not update master files.** Honored (MASTER_INDEX / MASTER_CHUNK_MAP / ACTIVE_KNOWLEDGE_STATE untouched).
- **17. Do not touch recovery/acquisition items except to report status.** Honored. Status (read-only): **Margin of Safety** has been recovered as a clean epub (per RECOVERY_INTAKE_CHECK `9814893`) and is now the 8th CORE source · the recovered file is NOT moved or staged here (it stays in the source universe until an authorized routing/staging pass). No source file was touched.
- **18. Stop after writing the plan.** Honored. No commit (operator will review first).

## Execution sequence (when later authorized · the locked 7-step SOP, steps 5-7)

0. **Authorized routing/staging pass first:** move Margin of Safety (epub) from the source universe into `raw/03_TIER_2_CANON_BOOKS/investing_finance/` (replacing the old scanned PDF) so all 8 sources are staged before extraction. (Not done here.)
1. `scripts/extract_deep_finance_expansion.py` · pdftotext (Security Analysis, The Snowball, The Intelligent Investor, The Sovereign Individual) + ebook-convert (Mastering the Market Cycle, The Lords of Easy Money, The New Tycoons, Margin of Safety) into `deep_finance_expansion_extracted/` (refuse to overwrite). No OCR, no new dependency.
2. `scripts/write_deep_finance_expansion_chunks.py` · author 22-36 chunks (target ~25-31) · 12-field schema · batch_id `DEEP_FINANCE_EXPANSION` · short illustrative quotes only (copyright-safe · in-copyright trade books) · em-dash clean · CURRENT_OPERATOR_REALITY_BRIEF referenced in every chunk · optionality guardrail in the closing chunk · `economics` NOT used.
3. Validate: 6 jsonl-validation checks + per-lane checks (8 sources resolve, NO new domain, no already-chunked overlap, Marks chunks complement MONEY_OWNERSHIP, Margin-of-Safety chunks distinct from The Intelligent Investor, brief not chunked, em-dash 0, quote discipline).
4. Ship commit, then a separate authorized master-consolidation (bumps capital/finance/etc · NO new domain), then session save. Each step gated and scoped.

## Open questions for the operator

1. **Single mini-batch vs split:** default is ONE curated mini-batch (~25-31). Confirm, or request the 5+3 split (`DEEP_FINANCE_VALUE` + `DEEP_FINANCE_MACRO`).
2. **The Intelligent Investor abridgement:** the staged PDF appears partial (142 pp / 45k words). Include with a modest chunk count (default), or defer it to a recovery re-acquire of the full edition?
3. **Chunk depth:** confirm ~25-31 (range 22-36), or signal a tighter cap if you want only the sharpest models from these 8 deep books.
4. **Staging timing:** the recovered Margin of Safety epub needs an authorized routing/staging pass into `raw/` before extraction can include it · confirm whether to fold that staging into the eventual ship-step authorization or run it as a separate move.
