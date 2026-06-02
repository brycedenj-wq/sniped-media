# POLITICAL_THEORY_DISCOURSES mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans the second (and final) of the two deferred classical-canon splits (the political-theory lane), recommends scope, and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `c03689b save session after MODERN_COMMAND_NAPOLEON consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,597 · 10 numbered batches + 29 mini-batches · 62 official domains (75 combined keys).
- **CLASSICAL_STRATEGY** (`c3936a2`), **CLASSICAL_HISTORY** (`12df2fd`), and **MODERN_COMMAND_NAPOLEON** (`bf4c029`) all complete and canonical; recovery + historical-biography lanes cleared. The sequenced CLASSICAL_STRATEGY_OPERATING_CANON plan (`c27da6f`) and the CLASSICAL_HISTORY plan (`d726e08`) both named **Discourses on Livy -> a political-theory pass (CLASSICAL_STRATEGY-adjacent)** as the second deferred split.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate file located in raw/ (verified)

| Source | Author | Format | Size | Words | Register | Path |
|---|---|---|---|--:|---|---|
| Discourses on Livy | Niccolo Machiavelli (Ninian Hill Thomson, tr.) | pdf (490 pp) | 1 MB | 143,937 | Renaissance (1531) republican-strategy / political theory | `raw/02_TIER_1_CANON_BOOKS/strategy_history/[Dover books on history, political and social science] Niccolo Machiavelli, Ninian Hill Thomson - Discourses on Livy (2007, Dover Publications) - libgen.li.pdf` |

## 2. Source-quality / stub / scan check

- **Extracts cleanly.** A read-only `pdftotext`-to-/tmp probe returned **143,937 words** (matching the CLASSICAL_HISTORY_PLAN estimate exactly) of real prose with intact chapter structure (e.g., Book I Chapter VII "That to preserve Liberty in a State there must exist the Right to accuse", the Coriolanus example from Livius). Temp deleted; the raw file's 2026-05-18 mtime is unchanged.
- **No stub / scan / broken issue.** The 490-page Dover edition has a clean text layer. No OCR needed.
- **Scale flag:** ~144K words is moderate (about the length of The Prince), but dense and systematic · chunking MUST be curated/representative, never chapter-by-chapter (the Discourses has ~140 short chapters across three books).

## 3. Already-chunked overlap check (verified)

- **Discourses on Livy (Machiavelli) is fully net-new** · 0 chunks as a source. No batch jsonl has Discourses or "Livy" as a `source_title` / `source_file`, and there are no body mentions of it.
- **Distinct from The Prince (CLASSICAL_STRATEGY):** Machiavelli appears as an `author` in exactly one place, CLASSICAL_STRATEGY's "The Prince" (4 chunks). The Discourses is his longer, complementary **republican-strategy** treatise (Livy commentary), a different work, different register (republican institutions vs the single prince).
- **Distinct from CLASSICAL_HISTORY** (Herodotus / Thucydides / Arrian / Engels) **and MODERN_COMMAND_NAPOLEON** (Napoleon: A Life): the Discourses comments ON Roman history (Livy) but is a theory treatise, not an ancient primary history or a modern biography.
- **Art of War / 48 Laws / 33 Strategies** (already BATCH_002) are not this source.

## 4. Architecture recommendation: single-source mini-batch

- **POLITICAL_THEORY_DISCOURSES = Discourses on Livy alone.** It is the only classical political-theory source remaining; the other un-chunked strategy_history items (the Greene trio: The Laws of Human Nature / Mastery / The 50th Law) are a separate modern strategy/psychology cluster (a Tier-2-style lane), NOT classical political theory, so they are NOT bundled here. The Book of Five Rings (djvu) is broken and out of scope.
- **Result:** a single-source mini-batch, register-matched to CLASSICAL_STRATEGY (the princely companion The Prince is already there), kept curated. This split closes the classical block of the sequenced canon.

## 5. Recommended include / defer / exclude

- **INCLUDE (1 · CORE · curated):**
  - Discourses on Livy (Niccolo Machiavelli) · pdf · ~143,937 words · curated, not exhaustive.
- **DEFER:**
  - none specific to this split (the classical block closes here · subsequent lanes are OPERATING_FOUNDER / NETWORK_DISTRIBUTION / SALES_POSITIONING / DECISION_JUDGMENT / Tier-2 [incl the Greene trio] / BRAND_CANON).
- **EXCLUDE (0 chunks):**
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical source (CLASSICAL_STRATEGY's The Prince / On War / Meditations / Caesar; CLASSICAL_HISTORY's Herodotus / Thucydides / Arrian / Engels; MODERN_COMMAND_NAPOLEON's Napoleon: A Life; BATCH_002's Art of War / 48 Laws / 33 Strategies) and every other-cluster source (operating_founder / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2). CURRENT_IDENTITY sources. The Book of Five Rings (djvu).

## 6. Recommended chunk target / range

- **Target:** ~10-12 chunks · **Range:** 8-14 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the republican / institutional operating pattern + the optionality guardrail).
- **Curated/representative,** not chapter-by-chapter; a single ~144K-word, ~140-chapter treatise mined for transferable institution-design / power-balance / renewal / adaptation patterns, not a chapter walk. (For calibration: The Prince at ~140K words gave 4 chunks as part of CLASSICAL_STRATEGY; as a sole-focus standalone the longer, denser Discourses warrants more depth, hence ~10-12.)

## 7. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `power` (22), `strategy` (192), `leadership` (50), `operator-doctrine` (95), `operator-process` (84), `ethics` (47), `culture` (57), `systems-thinking` (47), `mental-models` (5).

| Domain | Planned use in this lane |
|---|---|
| `power` (anchor) | The balance of power · the few vs the many and the mixed constitution; checks and balances; the right to accuse as a power-release valve; how power corrupts institutions over time. (Translated to org-design / power-balance patterns.) |
| `operator-doctrine` | Return to first principles · periodic renewal back to founding values ("ridurre ai principii"); the founder-vs-maintainer distinction (one person to establish, durable institutions to sustain). |
| `strategy` | Adapt to the times (fortune favors the impetuous; the one who cannot change with circumstance falls); why conspiracies usually fail (the asymmetry of risk); the indirect approach and deception in conflict. |
| `operator-process` | Institutional release valves · the right to accuse vs calumny; designing healthy outlets for internal conflict so "evil humours" do not overwhelm the organization. |
| `leadership` | The founder who must sometimes act decisively/alone to establish order; leading institutional renewal; the limits of relying on any one person. |
| `ethics` | Ends-and-means realism / dirty hands · read honestly as analysis of how power behaves, explicitly NOT an endorsement of manipulation or cruelty. |
| `culture` (if warranted) | Civic religion and shared belief as organizational glue (Machiavelli's instrumental view of religion as social cohesion) · used honestly, sparingly. |
| `systems-thinking` (if warranted) | Institutions decay without renewal; the cyclical corruption and regeneration of regimes (anacyclosis) as a systems model · used where squarely systemic. |
| `mental-models` (if warranted) | The regime-cycle / corruption-renewal model · used sparingly (the thin domain, count 5) and only if clearly a transferable model; by default the cycle routes to `systems-thinking`. |

### Domain issue to flag (important)

- **`politics`, `political-theory`, `republic`, `statecraft`, `governance`, `history`, `empire` do NOT exist** (ABSENT · verified). **None will be created.** Routing: political-theory / republic / governance / statecraft -> `power` / `operator-doctrine` / `strategy`; institutional design -> `operator-process` / `power`; history (Livy/Rome) -> `culture` / `strategy`; empire -> `power` (cautionary). This mirrors the CLASSICAL_STRATEGY routing (where the same `statecraft`/`politics`/`history` were deliberately not registered).
- **NO new domain will be created by default.** All planned domains pre-exist. `power` (the anchor) is a thinner domain (count 22) that this lane legitimately deepens.

## 8. Connections (cross-references this lane opens)

- **CLASSICAL_STRATEGY (the direct parent):** The Prince is the princely companion to this republican treatise · same author, complementary works (the prince who founds vs the institutions that endure) · Machiavelli's power realism runs through both. Closes the Machiavelli pair.
- **CLASSICAL_HISTORY:** the Discourses is literally a commentary on Livy's history of Rome · the Roman-republic examples (Coriolanus, the tribunes, the corruption of the late republic) are the same world Thucydides/Arrian illuminate · the corruption / over-reach themes mirror the Sicilian expedition and Alexander's hubris.
- **MODERN_COMMAND_NAPOLEON:** the institution-building lesson · Napoleon's Code Napoleon as durable institutions echoes the Discourses' core teaching that institutions outlast founders; the renewal / relinquishment themes read against Napoleon's failure to relinquish.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane (see Sec. 9-10). CURRENT_IDENTITY remains plan-only / NOT extracted.

## 9. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the treatise as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 10. Discourses = decision-support / pattern-library only (not a directive)

The Discourses on Livy is held strictly as a **decision-support / pattern-library layer**: transferable patterns of institution design, power-balance, organizational renewal, adaptation to circumstance, and how organizations corrupt and regenerate. It is **NOT a directive that BJ pursue political power, build a republic, manipulate people, or copy Machiavelli**, and not an endorsement of cruelty or manipulation. Per the operator's framing, the **republican / institutional material is translated into organization design, culture, incentives, and power-balance patterns only where relevant** (the few vs the many becomes stakeholder balance; the right to accuse becomes a healthy-conflict release valve; return to first principles becomes periodic values-renewal; civic religion becomes shared-belief cohesion). The realpolitik / ends-and-means material (chunked under `ethics`) is read as honest analysis of how power behaves, NOT as a mandate for manipulation. Photography remains one option among several.

## 11. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/POLITICAL_THEORY_DISCOURSES_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/political_theory_discourses_extracted/` (1 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/POLITICAL_THEORY_DISCOURSES_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/POLITICAL_THEORY_DISCOURSES_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/POLITICAL_THEORY_DISCOURSES_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/POLITICAL_THEORY_DISCOURSES_COMPLETE.md` |
| Extraction script | `scripts/extract_political_theory_discourses.py` |
| Chunk writer | `scripts/write_political_theory_discourses_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags) · `batch_id` = `POLITICAL_THEORY_DISCOURSES` · `chunk_id` pattern `POLITICAL_THEORY_DISCOURSES_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · single source · no new domain · politics/political-theory/republic/statecraft/governance/history/empire NOT created · The Prince [CLASSICAL_STRATEGY] 0 · CLASSICAL_HISTORY + MODERN_COMMAND_NAPOLEON sources 0 · BATCH_002 strategy/power sources 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 12. Projected post-consolidation state (for reference · NOT applied now)

If shipped at the mid-target (~11) and consolidated: 1,597 + ~11 = ~1,608 chunks · 10 numbered batches + 30 mini-batches · 62 domains (NO new domain · bumps to power [anchor] / operator-doctrine / strategy / operator-process / leadership / ethics, plus culture / systems-thinking / mental-models where warranted). Exact counts finalized at ship/consolidation time. **This split CLOSES the classical block of the sequenced CLASSICAL_STRATEGY_OPERATING_CANON** (CLASSICAL_STRATEGY + CLASSICAL_HISTORY + MODERN_COMMAND_NAPOLEON + POLITICAL_THEORY_DISCOURSES). Subsequent lanes: OPERATING_FOUNDER, NETWORK_DISTRIBUTION, SALES_POSITIONING (post overlap-audit), DECISION_JUDGMENT, Tier-2 (incl the Greene trio), BRAND_CANON.

## 13. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,597.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 14. Next step (operator decision · do not start without authorization)

Authorize the POLITICAL_THEORY_DISCOURSES ship (1 curated source · Discourses on Livy / Machiavelli · target ~10-12 · existing domains only · `power` anchor · no new domain · politics/political-theory/republic/statecraft/governance/history/empire NOT created · Bible excluded · curated, not exhaustive · republican/institutional material translated to org-design/power-balance patterns · realpolitik analytical not endorsing), then commit the ship outputs, then consolidate. This closes the classical block; the next lane is OPERATING_FOUNDER (or another queued option).
