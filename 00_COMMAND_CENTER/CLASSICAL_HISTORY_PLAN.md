# CLASSICAL_HISTORY mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans the second lane of the sequenced CLASSICAL_STRATEGY_OPERATING_CANON and recommends scope. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `fd5136b save session after CLASSICAL_STRATEGY consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,565 · 10 numbered batches + 27 mini-batches · 62 official domains (75 combined keys).
- **CLASSICAL_STRATEGY** (the first canon lane) complete and canonical (`c3936a2`); the sequenced CLASSICAL_STRATEGY_OPERATING_CANON plan (`c27da6f`) named CLASSICAL_HISTORY as the next lane.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified · all in `raw/02_TIER_1_CANON_BOOKS/strategy_history/`)

| Source | Author | Format | Size | Words | Register |
|---|---|---|---|--:|---|
| The Landmark Herodotus: Histories | Herodotus (Strassler ed.) | epub | 23 MB | 437,842 | ancient Greek history |
| The Landmark Thucydides: Peloponnesian War | Thucydides (Strassler ed.) | epub | 6.9 MB | 352,171 | ancient Greek history |
| The Campaigns of Alexander | Arrian | azw3 | 0.85 MB | 132,066 | ancient Macedonian history |
| Alexander the Great and the Logistics of the Macedonian Army | Donald W. Engels | pdf (208 pp · text layer present) | 44 MB | 75,419 | ancient military-logistics history |
| Napoleon: A Life | Andrew Roberts | epub | 43 MB | 385,255 | modern (2014) command biography |
| Discourses on Livy | Niccolo Machiavelli | pdf (490 pp) | 1 MB | 143,937 | Renaissance political theory |

Combined ~1,526,690 words across 6 huge sources spanning **three distinct registers**.

## 2. Source-quality / stub / scan check

- **All 6 extract cleanly** (word counts above confirmed via pdftotext / ebook-convert to /tmp). **Engels is NOT image-only** despite its 44 MB size: it has a real text layer (75,419 words extracted); the size is embedded maps/figures.
- **No broken / scanned / stub candidates** in this set. (The Book of Five Rings djvu was a CLASSICAL_STRATEGY exclusion, not part of this lane.)
- **Scale flag:** the two Landmark Greek histories alone are ~790K words; chunking MUST be curated/representative, never exhaustive (the CLASSICAL_STRATEGY + HISTORICAL_BIOGRAPHY precedent).

## 3. Already-chunked overlap check (verified)

- **Herodotus, Thucydides, Arrian (Campaigns of Alexander), Engels (Alexander logistics), Napoleon: A Life (Roberts), Discourses on Livy:** all **net-new** (0 chunks as source). The single "Macedonian" grep hit is a passing mention in BATCH_002, not Arrian/Engels as a source.
- **Distinct from CLASSICAL_STRATEGY:** that lane chunked The Prince / On War / Meditations / Landmark Caesar; these six are different titles. **Distinct from HISTORICAL_BIOGRAPHY:** that lane chunked Chernow's Grant + Washington; Napoleon: A Life (Roberts) is a different modern biography (same register · see 5).
- **Art of War / 48 Laws / 33 Strategies** (already BATCH_002) are not in this set.

## 4. Architecture recommendation: SPLIT into three register-appropriate lanes

The six candidates are **not one coherent mini-batch** · they span three registers and ~1.5M words. Recommended split:

1. **CLASSICAL_HISTORY (this first lane) = the ancient Greek + Macedonian histories** · Herodotus + Thucydides + Arrian + Engels. One coherent cluster (the ancient Greek world: Persian Wars, Peloponnesian War, Alexander's campaigns + their logistics). ~997K words · curated.
2. **Napoleon: A Life (Roberts) -> DEFER to a modern-command lane (HISTORICAL_BIOGRAPHY-adjacent).** It is a modern (2014) biography of a military-political leader, register-wise much closer to Chernow's Grant/Washington than to ancient primary histories. Best handled with the historical-biography register, not folded into the ancient-history lane.
3. **Discourses on Livy (Machiavelli) -> DEFER to a political-theory pass (CLASSICAL_STRATEGY-adjacent).** It is Machiavelli's republican-strategy treatise, the companion to The Prince (already in CLASSICAL_STRATEGY); it belongs with the strategy treatises, not the histories.

This first lane stays a coherent "ancient histories" mini-batch; Napoleon and Discourses get register-appropriate homes later.

## 5. Recommended include / defer / exclude (first CLASSICAL_HISTORY lane)

- **INCLUDE (4 · CORE · curated · the ancient Greek/Macedonian histories):**
  - The Landmark Herodotus (Histories) · epub · ~437,842 words.
  - The Landmark Thucydides (Peloponnesian War) · epub · ~352,171 words.
  - The Campaigns of Alexander (Arrian) · azw3 · ~132,066 words.
  - Alexander the Great and the Logistics of the Macedonian Army (Engels) · pdf · ~75,419 words.
  - Combined ~997,498 words · curated, not exhaustive.
- **DEFER:**
  - **Napoleon: A Life (Roberts)** -> a modern-command lane (HISTORICAL_BIOGRAPHY-adjacent).
  - **Discourses on Livy (Machiavelli)** -> a political-theory pass (CLASSICAL_STRATEGY-adjacent).
- **EXCLUDE (0 chunks):**
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical source and every other-cluster source (operating_founder / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2).

## 6. Recommended chunk target / range (first lane)

- **Target:** ~16-20 chunks · **Range:** 12-22 (halt-and-report if outside).
- **Synthesis:** 1-2 closing synthesis chunks (the ancient-history pattern + the optionality guardrail).
- **Provisional per-source split:** Herodotus ~4-5 · Thucydides ~5-6 (the richest strategy/power source) · Arrian ~3-4 · Engels ~2-3 · + 1-2 synthesis. Curated/representative (a pattern library, not a chapter-by-chapter retelling of the histories).

## 7. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist: `strategy` (187), `power` (19), `leadership` (44), `operator-doctrine` (92), `operator-process` (78), `culture` (55), `ethics` (45), `systems-thinking` (45), `mental-models` (3).

| Domain | Planned use in the first lane |
|---|---|
| `strategy` (anchor) | Thucydides' strategic analysis (Pericles' war strategy, the Sicilian expedition as catastrophic over-reach); Herodotus on Greek vs Persian strategy; Alexander's campaign design. |
| `power` | Thucydides' realism (the Melian dialogue · "the strong do what they can"); the rise, hubris, and overreach of Athenian power; Alexander's accumulation of power. |
| `leadership` | Pericles, Themistocles, Alexander as commanders; Arrian on Alexander's generalship and the bond with his troops. |
| `operator-process` | Engels' logistics (how the Macedonian army was actually supplied and sustained · the unglamorous machinery behind the campaigns). |
| `culture` | Herodotus as the first cultural anthropologist (custom, nomos, the Greek/Persian civilizational contrast); the cultural context of the histories. |
| `ethics` | The moral dimension (the Melian dialogue's power-vs-justice; Thucydides on how war corrupts societies, the Corcyrean revolution; hubris and nemesis). |
| `operator-doctrine` | The synthesis · the durable lessons of overreach, preparation, and the limits of power. |
| `systems-thinking` (if warranted) | Thucydides on war as a system that degrades the societies waging it; logistics as a system (Engels) · used where squarely systemic. |
| `mental-models` (if warranted) | Over-reach / the culminating point (echoing Clausewitz); the rising-vs-ruling-power dynamic (the "Thucydides Trap") as a model · used sparingly (the thin domain, count 3). |

### Domain issue to flag (important)

- **`history`, `empire`, `war`, `politics`, `statecraft`, `military`, `civilization` do NOT exist** (ABSENT). **None will be created.** Routing: history -> `culture` / `strategy`; empire -> `power` / `strategy`; war -> `strategy` / `leadership`; logistics/military-ops -> `operator-process`; cultural-anthropology -> `culture`; statecraft/politics -> `strategy` / `power`.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 8. Connections (cross-references this lane opens)

- **CLASSICAL_STRATEGY:** the direct parent · the strategy treatises (Clausewitz's friction/center-of-gravity/culminating-point, Machiavelli's power realism) that these histories illustrate in lived events (the Sicilian expedition as a culminating-point catastrophe; the Melian dialogue as raw power realism). Same `strategy` anchor.
- **HISTORICAL_BIOGRAPHY:** the leadership/power-restraint through-line · Alexander's command and the over-reach lessons read against Grant/Washington's restraint; Napoleon: A Life is deferred to this register.
- **ORIGINAL_SOURCE_COMPLETION_AUDIT:** the classical canon it named · this is the next sequenced lane after CLASSICAL_STRATEGY.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane (see §9-10).

## 9. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the histories as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk(s) making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 10. Classical history = decision-support / pattern-library only (not a directive)

Herodotus, Thucydides, Arrian, and Engels are held strictly as a **decision-support / pattern-library layer**: transferable patterns of strategy, power, overreach, leadership, logistics, and how societies and campaigns succeed or collapse. They are **NOT a directive that BJ build an empire, seek political power, or copy ancient rulers**, and not an endorsement of conquest. The power/overreach material (the Melian dialogue, the Sicilian expedition, Alexander's hubris) is read as cautionary analysis, not aspiration. The `ethics` chunks keep the moral dimension honest (war's corrupting effect, power-vs-justice), not glorified. Photography remains one option among several.

## 11. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/CLASSICAL_HISTORY_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/classical_history_extracted/` (4 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/CLASSICAL_HISTORY_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/CLASSICAL_HISTORY_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/CLASSICAL_HISTORY_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/CLASSICAL_HISTORY_COMPLETE.md` |
| Extraction script | `scripts/extract_classical_history.py` |
| Chunk writer | `scripts/write_classical_history_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags) · `batch_id` = `CLASSICAL_HISTORY` · per-source attribution. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · no new domain · Napoleon/Discourses deferred 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 12. Projected post-consolidation state (for reference · NOT applied now)

If shipped at the mid-target (~18) and consolidated: 1,565 + ~18 = ~1,583 chunks · 10 numbered batches + 28 mini-batches · 62 domains (NO new domain · bumps to strategy / power / leadership / operator-process / culture / ethics / operator-doctrine, plus systems-thinking / mental-models where warranted). Exact counts finalized at ship/consolidation time. Subsequent lanes: the deferred Napoleon (modern-command) and Discourses (political-theory) passes, then OPERATING_FOUNDER, NETWORK_DISTRIBUTION, SALES_POSITIONING (post overlap-audit), DECISION_JUDGMENT, Tier-2, BRAND_CANON.

## 13. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,565.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 14. Next step (operator decision · do not start without authorization)

Authorize the CLASSICAL_HISTORY first lane (4 ancient histories · Herodotus + Thucydides + Arrian + Engels · target ~16-20 · existing domains only · `strategy` anchor · no new domain · history/empire/war/politics/statecraft/military/civilization NOT created · Napoleon + Discourses deferred · Bible excluded · curated, not exhaustive), then commit the ship outputs, then consolidate. Napoleon (modern-command) and Discourses (political-theory) follow as separate register-appropriate lanes.
