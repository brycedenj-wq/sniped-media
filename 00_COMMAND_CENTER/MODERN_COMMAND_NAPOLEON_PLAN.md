# MODERN_COMMAND_NAPOLEON mini-batch · plan only · 2026-05-24

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document plans the first of the two deferred classical-canon splits (the modern-command lane), recommends scope, and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `acffa22 save session after CLASSICAL_HISTORY consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,583 · 10 numbered batches + 28 mini-batches · 62 official domains (75 combined keys).
- **CLASSICAL_STRATEGY** (`c3936a2`) and **CLASSICAL_HISTORY** (`12df2fd`) both complete and canonical; recovery + historical-biography lanes cleared. The sequenced CLASSICAL_STRATEGY_OPERATING_CANON plan (`c27da6f`) and the CLASSICAL_HISTORY plan (`d726e08`) both named **Napoleon: A Life -> a modern-command lane (HISTORICAL_BIOGRAPHY-adjacent)** as a deferred split.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate file located in raw/ (verified)

| Source | Author | Format | Size | Words | Register | Path |
|---|---|---|---|--:|---|---|
| Napoleon: A Life | Andrew Roberts | epub | 43 MB | 385,255 | modern (2014) command biography | `raw/02_TIER_1_CANON_BOOKS/strategy_history/Emperor of the French Napoleon I_ Frankreich Kaiser Napoléon I._ - Napoleon _ a life (2014, Penguin Group_Viking) - libgen.li.epub` |

## 2. Source-quality / stub / scan check

- **Extracts cleanly.** A read-only `ebook-convert`-to-/tmp probe returned **385,255 words** (matching the CLASSICAL_HISTORY_PLAN estimate exactly) of real prose (Viking/Penguin front matter, "Copyright (c) 2014 by Andrew Roberts", running biographical text). Temp deleted; the raw file's 2026-05-18 mtime is unchanged.
- **No stub / scan / broken issue.** The 43 MB size is the full single-volume biography (a long, dense ~800+ page book), not image weight. No OCR needed.
- **Scale flag:** at ~385K words this is a large single source · chunking MUST be curated/representative, never exhaustive (the HISTORICAL_BIOGRAPHY + CLASSICAL_HISTORY precedent).

## 3. Already-chunked overlap check (verified)

- **Napoleon: A Life (Roberts) is fully net-new** · 0 chunks as a source. No batch jsonl has Napoleon as a `source_title` / `source_file`, and "Andrew Roberts" is not an `author` anywhere.
- **The "napoleon" string appears only as a passing in-body reference** in BATCH_002 (Greene's strategy canon), LITERARY_CANON_DYSTOPIAN, and HISTORICAL_BIOGRAPHY (illustrative mentions), never as a chunked source.
- **Distinct from HISTORICAL_BIOGRAPHY:** that lane chunked Chernow's Grant + Washington: A Life only (verified · 2 titles). Napoleon: A Life is a different modern biography in the same register.
- **Distinct from CLASSICAL_STRATEGY** (The Prince / On War / Meditations / Landmark Caesar) **and CLASSICAL_HISTORY** (Herodotus / Thucydides / Arrian / Engels) · different title, different register (modern command biography, not a strategy treatise or an ancient primary history).

## 4. Architecture recommendation: single-source mini-batch

- **MODERN_COMMAND_NAPOLEON = Napoleon: A Life alone.** It is the only deferred *modern-command* source in the corpus. The other deferred split, **Discourses on Livy (Machiavelli), belongs to a separate political-theory lane** (CLASSICAL_STRATEGY-adjacent · a strategy treatise, not a command biography), so it is NOT bundled here. The Greene trio (Laws of Human Nature / Mastery / 50th Law) is a separate Tier-2-style cluster, not modern-command. No other staged source fits this register.
- **Result:** a single-source mini-batch, register-matched to HISTORICAL_BIOGRAPHY (a modern biography of a military-political leader), kept curated.

## 5. Recommended include / defer / exclude

- **INCLUDE (1 · CORE · curated):**
  - Napoleon: A Life (Andrew Roberts) · epub · ~385,255 words · curated, not exhaustive.
- **DEFER:**
  - **Discourses on Livy (Machiavelli)** -> the separate political-theory lane (CLASSICAL_STRATEGY-adjacent · the next planned split).
- **EXCLUDE (0 chunks):**
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical source (HISTORICAL_BIOGRAPHY's Grant + Washington; CLASSICAL_STRATEGY's Prince/On War/Meditations/Caesar; CLASSICAL_HISTORY's Herodotus/Thucydides/Arrian/Engels; BATCH_002's Art of War / 48 Laws / 33 Strategies) and every other-cluster source (operating_founder / network_distribution / sales_positioning / decision_judgment / brand-canon / Tier-2). CURRENT_IDENTITY sources.

## 6. Recommended chunk target / range

- **Target:** ~12-14 chunks · **Range:** 10-16 (halt-and-report if outside).
- **Synthesis:** 1-2 closing synthesis chunks (the modern-command operating pattern + the optionality / overreach-is-cautionary guardrail).
- **Curated/representative,** not chapter-by-chapter; a single 385K-word biography mined for transferable command / power / administration / over-reach patterns, not a retelling of the life. (For calibration: HISTORICAL_BIOGRAPHY gave Grant 8 + Washington 8 as a pair from ~912K words; a sole-focus 385K-word biography warrants slightly more depth than a half-share, hence ~12-14.)

## 7. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `leadership` (46), `power` (21), `strategy` (191), `operator-process` (81), `operator-doctrine` (94), `ethics` (46), `founder-psychology` (31), `systems-thinking` (46), `culture` (56).

| Domain | Planned use in this lane |
|---|---|
| `leadership` (anchor) | Napoleon as commander and administrator · leading from the front, energy and tempo, the bond with the Grande Armee, decision-making under pressure, the meritocratic command culture. |
| `power` | The accumulation, consolidation, and ultimate over-reach of power · the arc from First Consul to Emperor to exile · the corruption of unchecked ambition (read cautionary). |
| `strategy` | The operational art · speed, concentration of force, the central position, the decisive battle · and the strategic over-extension (the Continental System, the 1812 Russia campaign as a culminating-point catastrophe). |
| `operator-process` | The administrative machine · the Code Napoleon, the prefect system, meritocracy / careers-open-to-talent, the relentless working method, logistics and institution-building (the durable civil legacy beneath the wars). |
| `founder-psychology` (if warranted) | The self-made outsider arc (the Corsican arriviste who reinvented himself), the relentless drive, the cult of self and image · held as a pattern library, NOT a directive. |
| `ethics` (if warranted) | The human cost · the wars and the dead, the authoritarian turn, censorship, the betrayal of the Revolution's ideals, the reinstatement of slavery in the colonies · kept honest, cautionary, not glorified. |
| `operator-doctrine` | The synthesis · the durable lessons of energy + system + the limits of will, and the optionality guardrail. |
| `systems-thinking` (if warranted) | Over-extension as a system · the Continental System and the Russia campaign as a self-defeating feedback loop (echoing Engels' carrying-capacity limit and Clausewitz's culminating point) · used where squarely systemic. |
| `culture` (if warranted) | Image-making and the Napoleonic legend / propaganda (the self-authored narrative, echoing Caesar's Commentaries) · used sparingly. |

### Domain issue to flag (important)

- **`military`, `politics`, `empire`, `conquest`, `biography`, `history`, `commander` do NOT exist** (ABSENT · verified), alongside the prior lanes' `statecraft` / `war` / `civilization` / `antiquity`. **None will be created.** Routing: military-command -> `leadership` / `strategy`; politics -> `power` / `strategy`; empire / conquest -> `power` (cautionary); biography -> `leadership` / `founder-psychology`; history -> `culture` / `strategy`; commander -> `leadership`; administration -> `operator-process`.
- **NO new domain will be created by default.** All planned domains pre-exist. `mental-models` (count 5) is available if the culminating-point / over-reach model is squarely a model, but it is NOT planned by default (the over-reach material routes to `strategy` + `systems-thinking`); it would only be used sparingly if clearly warranted at ship time.

## 8. Connections (cross-references this lane opens)

- **HISTORICAL_BIOGRAPHY (the direct register-sibling):** the leadership/power-restraint through-line · Napoleon read AGAINST Grant's and Washington's restraint and disciplined relinquishing of power · Napoleon is the cautionary counter-case (he did NOT relinquish; the over-reach destroyed him). Same `leadership` + `power` register.
- **CLASSICAL_STRATEGY:** Clausewitz literally theorized Napoleonic war · the friction, the center of gravity, and especially the culminating point are Napoleon's campaigns made into theory · Machiavelli's power realism reads against Napoleon's rise. The strategy treatises and this lived case illuminate each other.
- **CLASSICAL_HISTORY:** Alexander's hubris and over-reach (Arrian) and the Sicilian-expedition over-extension (Thucydides) are the ancient mirror of Napoleon's Russia 1812 · the same culminating-point / over-reach pattern across eras. Same `strategy` anchor for the over-reach lessons.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane (see Sec. 9-10). CURRENT_IDENTITY remains plan-only / NOT extracted.

## 9. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the biography as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF**, with the closing synthesis chunk(s) making the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 10. Napoleon = decision-support / pattern-library only (not a directive)

Napoleon: A Life is held strictly as a **decision-support / pattern-library layer**: transferable patterns of command, energy, administration, system-building, the strategic art, and the dynamics of power and over-reach. It is **NOT a directive that BJ copy Napoleon, seek conquest or status, or build an empire**, and not an endorsement of authoritarianism or war. The **over-reach, ego, and collapse material (the imperial turn, the Continental System, the 1812 Russia catastrophe, the exile) is read as cautionary analysis, NOT aspiration** · it is the counter-case to HISTORICAL_BIOGRAPHY's power-restraint lesson. The `ethics` chunk keeps the human cost honest (the wars, the dead, the authoritarian turn, the reinstatement of slavery), not glorified. The admirable patterns (the working method, meritocracy, the civil-code institution-building) are separable from the conquest that they served. Photography remains one option among several.

## 11. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/MODERN_COMMAND_NAPOLEON_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/modern_command_napoleon_extracted/` (1 normalized .txt) |
| Summary | `01_KNOWLEDGE_BASE/summaries/MODERN_COMMAND_NAPOLEON_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/MODERN_COMMAND_NAPOLEON_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/MODERN_COMMAND_NAPOLEON_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/MODERN_COMMAND_NAPOLEON_COMPLETE.md` |
| Extraction script | `scripts/extract_modern_command_napoleon.py` |
| Chunk writer | `scripts/write_modern_command_napoleon_chunks.py` |

Schema: the canonical 12-field JSONL (chunk_id, batch_id, source_title, source_file, author, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags) · `batch_id` = `MODERN_COMMAND_NAPOLEON` · `chunk_id` pattern `MODERN_COMMAND_NAPOLEON_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · single source · no new domain · military/politics/empire/conquest/biography/history/commander NOT created · Discourses deferred 0 · Bible 0 · already-canonical sources 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + overreach-cautionary guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 12. Projected post-consolidation state (for reference · NOT applied now)

If shipped at the mid-target (~13) and consolidated: 1,583 + ~13 = ~1,596 chunks · 10 numbered batches + 29 mini-batches · 62 domains (NO new domain · bumps to leadership / power / strategy / operator-process / operator-doctrine / ethics, plus founder-psychology / systems-thinking / culture where warranted). Exact counts finalized at ship/consolidation time. Subsequent lanes: the deferred Discourses on Livy (political-theory) pass, then OPERATING_FOUNDER, NETWORK_DISTRIBUTION, SALES_POSITIONING (post overlap-audit), DECISION_JUDGMENT, Tier-2, BRAND_CANON.

## 13. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,583.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 14. Next step (operator decision · do not start without authorization)

Authorize the MODERN_COMMAND_NAPOLEON ship (1 curated source · Napoleon: A Life / Roberts · target ~12-14 · existing domains only · `leadership` anchor · no new domain · military/politics/empire/conquest/biography/history/commander NOT created · Discourses deferred · Bible excluded · curated, not exhaustive · over-reach material cautionary), then commit the ship outputs, then consolidate. The Discourses on Livy (political-theory) lane follows as the second deferred split.
