# ONWARD_TURNAROUND mini-batch · plan only · 2026-05-23

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes. Stop after writing this plan.

## 0. Verified starting state

- **Head commit:** `dd2d244 save session after FOUNDER_SECOND_TIER consolidation`
- **Working tree:** clean (verified before this plan · only this plan file is added after writing it).
- **Total chunks:** 1,391 (header = sum of `.batches[].chunk_count` = sum of jsonl line counts).
- **Canonical sets:** 10 numbered batches + 17 mini-batches · 62 official domains (combined_domain_counts keys 75).
- **FOUNDER_SECOND_TIER:** complete and canonical (consolidated `ca50373`).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted (`1211da5`).
- **Identity optionality guardrails:** ACTIVE.

## 1. Theme

Turnaround discipline after scale: founder return, repairing drift, simplification, operational renewal, cultural repair, brand trust, customer experience, standards, focus, emotional resilience, and how an operator diagnoses what broke after growth. The companion arc to FOUNDER_SECOND_TIER's build-up story (Pour Your Heart Into It): not how Starbucks scaled, but how Schultz returned as CEO in 2008 and repaired the damage that scale and drift had caused.

## 2. Source located + inventory

| Field | Value |
|---|---|
| Title | Onward: How Starbucks Fought for Its Life without Losing Its Soul |
| Authors | Howard Schultz, Joanne Gordon |
| Publisher / year | Rodale Books, 2011 |
| Path | `raw/03_TIER_2_CANON_BOOKS/memoirs_biographies/ Howard Schultz, Joanne Gordon - Onward_ How Starbucks Fought for Its Life without Losing Its Soul (2011, Rodale Books) - libgen.li.mobi` |
| File type | Mobipocket e-book (mobi · version 6 · codepage 65001 UTF-8) |
| File size | 2,278,971 bytes (~2.28 MB · 1,051,816 bytes uncompressed) |
| Likely extraction method | `ebook-convert` (calibre · already on PATH at `/opt/homebrew/bin/ebook-convert`) · mobi to plain text · no OCR · no new dependency |

**Filename note:** the filename has a LEADING SPACE before `Howard`. The extraction script must quote the exact path (including the leading space) · same handling pattern used for the spaced source-universe folder.

## 3. Pre-flight peek (read-only · converted to /tmp, measured, deleted · NOT into the deliverable dir)

- **Conversion:** ebook-convert succeeded cleanly.
- **Yield:** 117,893 words · 716,617 chars · 11,115 lines. Substantial, full-length book. NOT a stub, NOT a scan, NOT a bad download.
- **Format:** supported (mobi · ebook-convert handles it · same path as Titan / Fish That Ate the Whale / Pour Your Heart Into It in FOUNDER_SECOND_TIER).
- **Theme markers present + strong:** "transformation agenda" (35), "VIA" (100 · the instant-coffee product launch central to the turnaround), "reinvent" (25), "onward" (20), "turnaround" (5), "reignite" (5), store-closure language (multiple). Squarely on-theme · the 2008 turnaround narrative.
- **No conversion needs beyond ebook-convert.** No off-theme issue.

## 4. Already-chunked overlap check

- **Onward as a source:** 0 hits across all `*_CHUNKS.jsonl`. NOT chunked anywhere. Net-new.
- **Pour Your Heart Into It (the build-up book):** confirmed chunked in FOUNDER_SECOND_TIER · 2 chunks · `source_file = pour_your_heart_into_it_schultz.txt`. That is the company-building arc (1987-1997). **Onward is the DISTINCT turnaround companion** (2008-2011, Schultz's return). Different book, different period, different lesson set (build vs repair). No content overlap risk; the two are complementary, not duplicative.
- No other Schultz/Starbucks turnaround source exists in the corpus.

## 5. Recommendation: INCLUDE

INCLUDE Onward as a single-source dedicated mini-batch. Rationale:
- Clean, full-length, on-theme, net-new, supported format, no new dependency.
- Fills the one gap FOUNDER_SECOND_TIER deliberately deferred (the turnaround/repair arc) · explicitly flagged as a next option in the FOUNDER_SECOND_TIER session save.
- The turnaround/repair lens is distinct from every other lane (build-up, scale, media-empire, capital) and maps directly onto the operator's current diagnostic posture (see §9).

No defer/exclude within this lane (single source). All recovery/acquisition items remain untouched (status reported in §11, not actioned).

## 6. Estimated chunk yield + target range

- **Target:** ~8-12 chunks.
- **Hard range:** 6-14 (halt and surface if outside).
- **Rationale:** single rich ~118K-word book on one tightly-scoped theme (the turnaround). FOUNDER_SECOND_TIER gave the Starbucks BUILD arc 2 chunks as one of 7 sources; a dedicated turnaround mini-batch warrants more depth but should stay disciplined to the distinct lessons rather than re-narrate the whole company. ~10 distinct turnaround principles is the natural yield.
- **Synthesis/closing chunk:** 0-1 allowed (a single "turnaround pattern + optionality guardrail" closing chunk), citing the one source file. No cross-source synthesis (single source).
- Final count is content-faithful; the range governs.

## 7. Domain set (EXISTING domains only · NO new domain)

Indicative distribution within a ~10-chunk target (content-faithful at chunk time):

| Domain | Indicative chunks | What it carries |
|---|---:|---|
| founder-psychology | 2 | Schultz's return; founder identity tied to the company; emotional resilience under crisis; the weight of coming back |
| operator-process | 2 | operational renewal; simplification; store closures + the supply-chain/roasting fixes; La Boulange / espresso-machine standards reset |
| operator-doctrine | 2 | diagnosing what broke after growth; focus over expansion; restoring standards; the discipline of saying no to the growth reflex |
| strategy | 1 | the transformation agenda; refocus on the core; closing 600+ US stores + halting reckless expansion |
| brand | 1 | brand-trust repair; the customer-experience reset; restoring "the romance" / the third place |
| commercial-architecture | 1 | VIA instant coffee as a new revenue line; unit economics repair; the digital/loyalty groundwork |
| systems-thinking | 1 | the operator's diagnosis of how scale caused the drift (root cause, not symptom); the whole-system view of decline |
| culture | (0-1, if warranted) | cultural repair; re-engaging partners (employees); the New Orleans leadership conference; values re-grounding |
| ethics | (0-1, if warranted) | handling layoffs / store closures humanely; the "without losing its soul" tension between cost discipline and people |

`culture` and `ethics` are conditional (included only if the chunked content genuinely warrants, per the operator's "if warranted" instruction). All nine are existing domains (verified present: founder-psychology 26, operator-doctrine 67, operator-process 69, strategy 168, brand 35, commercial-architecture 43, systems-thinking 40, ethics 29, culture 45).

## 8. NO new domains

This lane introduces NO new domain. All chunks route to the existing domains in §7. Official domain count stays 62; combined_domain_counts keys stay 75. (No `turnaround`, `crisis`, `leadership`, or any other new key.)

## 9. Connections to existing lanes + the brief

- **FOUNDER_SECOND_TIER:** the direct parent. That lane chunked the Starbucks BUILD arc (Pour Your Heart Into It · 2 chunks) plus six other founders' scale arcs. ONWARD_TURNAROUND is the REPAIR arc · same founder, same `founder-psychology` anchor family, opposite phase (decline + recovery rather than build + scale). Closes the deferred turnaround gap.
- **BIOGRAPHY_FOUNDER_MEDIA:** the founder/taste/media arc layer · ONWARD adds the "what an operator does when the thing they built drifts" dimension to the founder-psychology picture.
- **MEDIA_BUSINESS:** the institutional/attention layer · ONWARD is the operator-repair counterpoint (institutions decay; the turnaround is how an operator re-grounds one). Cross-reads with the "renewable institution" theme (SNL franchise renewal).
- **MONEY_OWNERSHIP:** the capital/ownership economics · ONWARD shows capital discipline in reverse (cost cuts, store closures, balance-sheet repair, VIA as a new line) · `commercial-architecture`/`capital`-adjacent without claiming `capital`.
- **EDGE_AND_OPERATING_DISCIPLINE:** the discipline/standards frameworks · ONWARD is those standards re-applied as repair after they slipped at scale (the espresso-machine/quality reset is a standards story).
- **CURRENT_OPERATOR_REALITY_BRIEF:** referenced in every chunk as the read-first guardrail. The turnaround diagnostic ("what broke after growth, and how do you re-ground?") maps onto BJ's current posture: a solo field-engineer/operator loading the backend and diagnosing real-world pain before committing to a final brand/offer. The "diagnose root cause, simplify, restore standards" pattern is decision-support for how BJ evaluates options, NOT a directive.
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** fully honored (see §10-11).

## 10. Identity optionality confirmation

This lane does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction. SNIPED remains the live operator identity/container; SNIPED Media remains the existing photography company; BASEPLATE remains a possible historical rebrand asset, not the decided future. Every chunk frames Schultz's turnaround as a decision-support / pattern-library LENS read against CURRENT_OPERATOR_REALITY_BRIEF. Photography remains one option among several.

## 11. Turnaround patterns are decision-support lenses only

The turnaround patterns are NOT a directive that BJ needs to "return" to old SNIPED Media or revive an old brand. Schultz's return-to-repair-a-mature-company arc is the OPPOSITE of BJ's current situation (BJ is in early ideation/build, not recovering a scaled company). The value is the diagnostic discipline (find the root cause of drift, simplify, restore standards, protect the soul while cutting cost), held as a lens, not as a script. No chunk will imply BJ should revive SNIPED Media or any prior brand. A closing chunk will make this optionality discipline explicit (mirroring FOUNDER_SECOND_TIER chunk 020 and MEDIA_BUSINESS chunk 017).

## 12. Deliverables (created only when extraction/chunking is later authorized · NOT now)

- `01_KNOWLEDGE_BASE/batches/ONWARD_TURNAROUND_CHUNKS.jsonl` (12-field canonical schema · batch_id `ONWARD_TURNAROUND`)
- `01_KNOWLEDGE_BASE/batches/onward_turnaround_extracted/` (1 normalized .txt · `onward_schultz.txt`)
- `01_KNOWLEDGE_BASE/summaries/ONWARD_TURNAROUND_SUMMARY.md`
- `01_KNOWLEDGE_BASE/indexes/ONWARD_TURNAROUND_SOURCE_INDEX.md`
- `00_COMMAND_CENTER/batch_logs/ONWARD_TURNAROUND_EXTRACTION_LOG.md`
- `00_COMMAND_CENTER/batch_logs/ONWARD_TURNAROUND_COMPLETE.md`
- `scripts/extract_onward_turnaround.py`
- `scripts/write_onward_turnaround_chunks.py`

(This plan file `00_COMMAND_CENTER/ONWARD_TURNAROUND_PLAN.md` is the only artifact written now.)

## 13-17. Scope guards for this planning pass

- **13. Do not extract.** Honored (the §3 peek went to /tmp and was deleted · the deliverable `onward_turnaround_extracted/` was NOT created).
- **14. Do not chunk.** Honored.
- **15. Do not update master files.** Honored (MASTER_INDEX / MASTER_CHUNK_MAP / ACTIVE_KNOWLEDGE_STATE untouched).
- **16. Do not touch recovery/acquisition items except to report status.** Honored. Status (read-only): the broken/recovery items remain flagged and untouched · Hit Men (`.pdf` scan · in this same folder), The Mailroom (`.djvu` · same folder), Grace (0-byte stub · same folder), Total Recall (0-byte stub · same folder), Margin of Safety text edition, Security Analysis, The Snowball, The Intelligent Investor, Mastering the Market Cycle, The Sovereign Individual, Lords of Easy Money, The New Tycoons, Beloved, Maus I, Jonathan Livingston Seagull, Maus II, Russian-author mobi, Confessions text edition, Sugarman, Caples, Halbert, Predictably Irrational. Grant + Washington (Chernow histories · same folder) remain deferred to the historical-biography lane. None touched.
- **17. Stop after writing the plan.** Honored. No commit (operator will review first).

## Execution sequence (when later authorized · the locked 7-step SOP, steps 5-7)

1. `scripts/extract_onward_turnaround.py` · ebook-convert the mobi to `onward_turnaround_extracted/onward_schultz.txt` (quote the leading-space path · refuse to overwrite). No OCR, no new dependency.
2. `scripts/write_onward_turnaround_chunks.py` · author 6-14 chunks (target ~8-12) · 12-field schema · batch_id `ONWARD_TURNAROUND` · short illustrative quotes only (copyright-safe · in-copyright trade book) · em-dash clean · CURRENT_OPERATOR_REALITY_BRIEF referenced in every chunk · optionality guardrail in the closing chunk.
3. Validate: 6 jsonl-validation checks + per-lane additional checks (single source resolves under `onward_turnaround_extracted/`, NO new domain, no Onward overlap with FOUNDER_SECOND_TIER, brief not chunked, em-dash 0, quote discipline).
4. Ship commit (chunks + extracted + summary + index + logs + scripts), then a separate authorized master-consolidation, then session save. Each step gated and scoped.

## Open question for the operator

- **Chunk depth:** confirm the ~8-12 target (range 6-14) for a single-source dedicated mini-batch, or signal a tighter cap (e.g., ~6-8) if you want only the sharpest turnaround principles. Default is ~8-12 unless you say otherwise.
