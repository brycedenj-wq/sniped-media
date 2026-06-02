# DECISION_JUDGMENT mini-batch · plan only · 2026-05-25

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document inventories the `decision_judgment` folder, probes extractability, runs an authoritative already-chunked overlap check, recommends a split architecture, names the first lane, and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `e0c31ba save session after POSITIONING_DISRUPTION consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,676 · 10 numbered batches + 35 mini-batches · 62 official domains (75 combined keys).
- **Recovery program complete; classical block complete; historical-biography complete; OPERATING_FOUNDER complete; NETWORK_DISTRIBUTION complete; the sales_positioning folder resolved (POSITIONING_DISRUPTION).** DECISION_JUDGMENT is the next lane named in the remaining backlog.
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified · 13 files in `raw/03_TIER_2_CANON_BOOKS/decision_judgment/`)

The folder holds **two distinct registers**: a decision/judgment/psychology core and a storytelling/narrative-craft sub-cluster.

### A. Decision / judgment / psychology (9 files · the DECISION_JUDGMENT register proper)

| Source | Author | Format | Size | Words (probe) | Status |
|---|---|---|---|--:|---|
| Thinking, Fast and Slow | Daniel Kahneman | mobi | 1.1M | 190,774 | CLEAN |
| Noise: A Flaw in Human Judgment | Kahneman, Sibony, Sunstein | pdf | 3.6M | 133,394 | CLEAN |
| The Righteous Mind | Jonathan Haidt | azw3 | 2.0M | 137,787 | CLEAN |
| The Coddling of the American Mind | Lukianoff & Haidt | pdf | 5.4M | 119,516 | CLEAN |
| The True Believer | Eric Hoffer | epub | 2.0M | 48,694 | CLEAN |
| The Crowd | Gustave Le Bon | pdf | 3.6M | 56,670 | CLEAN |
| Games People Play | Eric Berne | epub | 154K | 50,273 | CLEAN |
| Man's Search for Meaning | Viktor E. Frankl | pdf | 983K | 47,250 | CLEAN |
| The Denial of Death | Ernest Becker | djvu | 3.4M | **0 (unsupported)** | **BROKEN** |

### B. Storytelling / narrative craft (4 files · a DISTINCT register · NOT decision/judgment)

| Source | Author | Format | Size | Words (probe) | Status |
|---|---|---|---|--:|---|
| The Anatomy of Story | John Truby | pdf | 6.8M | 126,225 | CLEAN |
| The Hero with a Thousand Faces | Joseph Campbell | epub | 5.1M | 142,098 | CLEAN |
| Save the Cat! | Blake Snyder | pdf | 9.6M | 59,787 | CLEAN |
| Story | Robert McKee | pdf | 53M | **0 (scanned/image-only)** | **BROKEN** |

Read-only `pdftotext` / `ebook-convert`-to-/tmp probes (temp deleted; all mtimes unchanged). **8 clean judgment/psychology books (~784,358 words) + 3 clean storytelling books (~328,110 words) + 2 broken (Denial of Death djvu, Story/McKee scanned).**

## 2. Source-quality / stub / scan check

- **8 clean, text-bearing judgment/psychology sources** + **3 clean storytelling sources** (word counts above). epubs/mobi/azw3 via `ebook-convert`; pdfs via `pdftotext`. No OCR.
- **BROKEN (2):**
  - **The Denial of Death (Becker):** `.djvu` (unsupported · no `djvutxt` · 0 extractable text). Flagged in ORIGINAL_SOURCE_COMPLETION_AUDIT §8 · re-acquire a clean epub. DEFER.
  - **Story (Robert McKee):** 53 MB pdf · `pdftotext` extracted **0 words** (scanned / image-only). Newly confirmed broken · re-acquire a clean epub. DEFER (storytelling lane anyway).
- At ship, sample each extracted .txt to confirm real book text before chunking.

## 3. Already-chunked overlap check (verified · authoritative by source_title / author / source_file across all 35 batch jsonls)

**All 13 folder titles are NET-NEW as book sources** (0 chunks as a source):

- Thinking, Fast and Slow / Noise / The Righteous Mind / The Coddling of the American Mind / The True Believer / The Crowd / Games People Play / Man's Search for Meaning / The Denial of Death · **net-new.**
- Save the Cat! / The Anatomy of Story / The Hero with a Thousand Faces / Story (McKee) · **net-new.**

**Notes / near-misses checked:**
- **"Noise" produced ONE false-positive substring hit** in `BATCH_006_CHUNKS.jsonl` (a chunk titled `signal-noise-forecasting-bayesian`, author "Claude AI Skills 50-Pack") · that is the word "noise" in a forecasting-skills framework prompt, **NOT the book Noise** by Kahneman/Sunstein/Sibony. The book is net-new.
- **Thinking, Fast and Slow** was listed in ORIGINAL_SOURCE_COMPLETION_AUDIT §5 as a heuristic *apparent-gap* example ("staged elsewhere"); the authoritative source-field check supersedes that: it has **0 chunks as a source** and is genuinely net-new.
- **Predictably Irrational (Ariely)** is NOT in this folder (it lives in `persuasion_psych` and is already chunked in PERSUASION_RECOVERY, where it grew `decision-making` 1 to 5). No overlap.
- **Frankl's Man's Search for Meaning** is net-new here; distinct from the LITERARY_CANON lanes (no overlap).

Cross-lane distinctness: distinct from PERSUASION_RECOVERY (Predictably Irrational), BATCH_009 / BATCH_009_EXPANSION (persuasion/positioning commercial canon), POSITIONING_DISRUPTION (positioning/customer-truth/disruption), OPERATING_FOUNDER (build/scale/operate), and CLASSICAL_STRATEGY (strategy treatises). The Crowd / The True Believer (crowd & mass-movement psychology) are adjacent to POLITICAL_THEORY_DISCOURSES's institutional-power material but are net-new psychology sources, not political theory.

## 4. Classification table

| Source | Classification |
|---|---|
| Thinking, Fast and Slow (Kahneman) | **net-new** · individual judgment / biases (cognition core) |
| Noise (Kahneman/Sibony/Sunstein) | **net-new** · noise vs bias in judgment (cognition core) |
| The Righteous Mind (Haidt) | **net-new** · moral/social psychology |
| The Coddling of the American Mind (Haidt/Lukianoff) | **net-new** · cognitive distortions / antifragility |
| The True Believer (Hoffer) | **net-new** · mass movements |
| The Crowd (Le Bon) | **net-new** · crowd psychology |
| Man's Search for Meaning (Frankl) | **net-new** · meaning / response to adversity |
| Games People Play (Berne) | **net-new** · transactional analysis / social games |
| The Denial of Death (Becker) | **broken / needs-reacquire** (djvu) |
| The Anatomy of Story (Truby) | **net-new but OUT-OF-REGISTER** (storytelling lane) |
| The Hero with a Thousand Faces (Campbell) | **net-new but OUT-OF-REGISTER** (storytelling lane) |
| Save the Cat! (Snyder) | **net-new but OUT-OF-REGISTER** (storytelling lane) |
| Story (McKee) | **broken / needs-reacquire** (scanned) + out-of-register (storytelling lane) |

## 5. Architecture recommendation: SPLIT into register-appropriate sub-lanes (mirror the OPERATING_FOUNDER pattern)

The decision/judgment register alone is **8 clean books / ~784K words** spanning three sub-registers (individual cognition / social-moral-crowd psychology / meaning-interaction). That is too large and too heterogeneous for one mini-batch (it would balloon to 25-30 chunks or go shallow per book · the corpus norm is ~10-18 chunks per 2-4 book lane). The storytelling sub-cluster is a **different register entirely** and should be its own future lane, not folded in. Recommended split:

1. **DECISION_JUDGMENT_COGNITION (recommended FIRST lane) · the individual-judgment / biases / noise register** · Thinking, Fast and Slow (Kahneman) + Noise (Kahneman/Sibony/Sunstein). ~324,168 words · the decision-judgment core most directly relevant to BJ's operator decision-making (System 1/2, heuristics and biases, the difference between bias and noise, when to trust intuition, decision hygiene).
2. **DECISION_JUDGMENT_CROWDS (deferred) · the social / moral / crowd-psychology register** · The Righteous Mind (Haidt) + The Coddling of the American Mind (Haidt/Lukianoff) + The True Believer (Hoffer) + The Crowd (Le Bon). ~362,667 words · moral foundations, the elephant and the rider, cognitive distortions, mass movements, crowd behavior.
3. **DECISION_JUDGMENT_MEANING (deferred) · the meaning / interaction register** · Man's Search for Meaning (Frankl) + Games People Play (Berne). ~97,523 words · meaning as a response to adversity, transactional analysis / social games. (Smallest and softest-fit; could alternatively fold into CROWDS as "the human element," operator's call at ship time.)

**Separately (NOT part of DECISION_JUDGMENT):**
- **STORYTELLING_NARRATIVE (a distinct future lane)** · The Anatomy of Story (Truby) + The Hero with a Thousand Faces (Campbell) + Save the Cat! (Snyder) clean; Story (McKee) broken/re-acquire. The operator flagged this storytelling sub-cluster as potentially its own lane · it is narrative-craft, not decision/judgment. Plan separately (and audit against any existing story material first, e.g. Building a StoryBrand in BATCH_009).
- **DEFER / broken:** The Denial of Death (Becker · djvu) and Story (McKee · scanned) · re-acquire clean epubs.

**No deferral of the whole lane is warranted** (the COGNITION first lane is clean and ready); a split is the right call, not a single mega-batch.

## 6. Recommended first lane: DECISION_JUDGMENT_COGNITION (include / defer / exclude)

- **INCLUDE (2 · CORE · curated · the individual-judgment / biases / noise register):**
  - Thinking, Fast and Slow (Daniel Kahneman) · mobi · ~190,774 words.
  - Noise: A Flaw in Human Judgment (Kahneman, Sibony, Sunstein) · pdf · ~133,394 words.
  - Combined ~324,168 words · curated, not exhaustive.
- **DEFER (subsequent DECISION_JUDGMENT sub-lanes):**
  - **DECISION_JUDGMENT_CROWDS:** The Righteous Mind + The Coddling of the American Mind + The True Believer + The Crowd.
  - **DECISION_JUDGMENT_MEANING:** Man's Search for Meaning + Games People Play.
- **EXCLUDE (0 chunks):**
  - **The storytelling sub-cluster** (Anatomy of Story, Hero with a Thousand Faces, Save the Cat!, Story) · a different register · future STORYTELLING_NARRATIVE lane.
  - **The Denial of Death (Becker · djvu) + Story (McKee · scanned)** · broken · re-acquire.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical source and every other-cluster source (PERSUASION_RECOVERY / BATCH_009 / POSITIONING_DISRUPTION / OPERATING_FOUNDER / the classical block / Tier-2). CURRENT_IDENTITY sources.

## 7. Recommended chunk target / range (first lane)

- **Target:** ~11-13 chunks · **Range:** 9-15 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the judgment-hygiene toolkit + the optionality guardrail).
- **Provisional per-source split:** Thinking, Fast and Slow ~6-7 · Noise ~4-5 · + 1 synthesis. Curated/representative from ~324K words, NOT chapter-by-chapter (TFS is dense and large; cover the load-bearing ideas: the two systems, anchoring, availability, representativeness, loss aversion / prospect theory, overconfidence / planning fallacy, WYSIATI; Noise: system noise vs bias, the noise audit, decision hygiene, mediating assessments).

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `decision-making` (5), `mental-models` (5), `strategy` (205), `systems-thinking` (52), `operator-doctrine` (109), `operator-process` (95), `ethics` (49), `founder-psychology` (37).

| Domain | Planned use in the first lane |
|---|---|
| `decision-making` (anchor) | The core judgment material: System 1/2, heuristics and biases, the bias-vs-noise distinction, when to trust intuition, prospect theory / loss aversion as decision inputs. (Grows from a thin 5 · was seeded by PERSUASION_RECOVERY's Predictably Irrational.) |
| `mental-models` | The reusable thinking tools (anchoring, availability, representativeness, base rates, regression to the mean, the planning fallacy, WYSIATI) held as portable models. (Grows from a thin 5.) |
| `operator-process` | Decision hygiene as a process: the noise audit, mediating assessments protocol, structured aggregation, checklists · the executional discipline of better judgment. |
| `operator-doctrine` | The disciplined doctrine of judging under uncertainty + the closing synthesis. |
| `systems-thinking` (if warranted) | Noise as a system property of an organization's judgments · used where squarely systemic. |
| `strategy` (if warranted) | Where a bias/noise lesson bears directly on a strategic bet · used sparingly. |
| `ethics` / `founder-psychology` (if warranted) | Only if a squarely-present moral or founder-emotional dimension appears · likely 0-1. |

**Recommended anchor:** `decision-making` (the lane's namesake and Kahneman's core), with `mental-models` and `operator-process` the strong secondaries.

### Domain issues to flag (important)

- **`psychology`, `behavioral-psychology`, `behavioral-economics`, `cognition`, `bias`, `risk`, `uncertainty`, `decision-science` do NOT exist and will NOT be created** · cognition/bias material -> `decision-making` / `mental-models`; risk/uncertainty material -> `decision-making` / `strategy`; behavioral-economics -> `decision-making` (as PERSUASION_RECOVERY already did); decision-science -> `decision-making` / `operator-process`.
- **`storytelling` and `narrative` do NOT exist and will NOT be created** (the storytelling sub-cluster is a deferred separate lane anyway).
- **`decision-making` (5) and `mental-models` (5) are thin existing domains** · this lane will reuse and grow them, NOT create anything new.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 9. Connections (cross-references this lane opens)

- **PERSUASION_RECOVERY (Predictably Irrational / Ariely):** the applied behavioral-economics primary source · DECISION_JUDGMENT_COGNITION is the foundational individual-judgment layer beneath it (same `decision-making` domain · Kahneman is the theory beneath Ariely's experiments).
- **OPERATING_FOUNDER (Lean Startup validated learning, The Goal's constraint thinking):** better judgment under uncertainty is the cognitive discipline beneath the build/operate methods.
- **POSITIONING_DISRUPTION (The Mom Test):** the Mom Test guards against bias in customer conversations · Kahneman explains why the bias exists (WYSIATI, confirmation, overconfidence).
- **CLASSICAL_STRATEGY (Clausewitz's friction/uncertainty, Marcus Aurelius's judgment):** the classical treatment of judgment under uncertainty reads against the modern cognitive-science treatment.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane; CURRENT_IDENTITY remains plan-only / NOT extracted.

## 10. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the books as a **decision-support / pattern-library lens read against CURRENT_OPERATOR_REALITY_BRIEF** · the closing synthesis chunk makes the optionality discipline explicit. It is **NOT a directive that BJ become a quant, a rationalist, a behavioral economist, an investor, or a decision-theory guru** · the biases/noise/judgment-hygiene material is read as transferable thinking discipline applied to BJ's actual build-mode stage. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 11. Decision/judgment material = decision-support / pattern-library only (not a directive)

Thinking, Fast and Slow and Noise are held strictly as a **decision-support / pattern-library layer**: transferable patterns of how human judgment goes wrong (biases, noise, overconfidence) and how to improve it (decision hygiene, base rates, mediating assessments). It is **NOT a directive that BJ become a quant, a rationalist, a behavioral economist, an investor, or a decision-theory guru**, and not a mandate to turn every decision into a formal model. The methods are read as transferable thinking discipline for a solo field-engineer in build-mode, loading the backend before final brand/offer/company-architecture decisions.

## 12. Deliverables for the future ship (NOT created now)

For the recommended first lane. **Naming note:** the operator's deliverable list (Sec. 17) uses umbrella `DECISION_JUDGMENT_*` names. If the operator accepts the split, the FIRST lane ships under `DECISION_JUDGMENT_COGNITION` (`DECISION_JUDGMENT_COGNITION_CHUNKS.jsonl`, `decision_judgment_cognition_extracted/`, etc.); if the operator prefers a single curated lane, the first lane keeps the umbrella `DECISION_JUDGMENT` name and chunks only the 2 Kahneman-family books, deferring the rest. **Recommendation: the split with the `DECISION_JUDGMENT_COGNITION` batch_id.**

| Deliverable | Path (umbrella form) |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/DECISION_JUDGMENT_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/decision_judgment_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/DECISION_JUDGMENT_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/DECISION_JUDGMENT_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/DECISION_JUDGMENT_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/DECISION_JUDGMENT_COMPLETE.md` |
| Extraction script | `scripts/extract_decision_judgment.py` |
| Chunk writer | `scripts/write_decision_judgment_chunks.py` |

(If the split is accepted, substitute the `DECISION_JUDGMENT_COGNITION` / `decision_judgment_cognition_*` names.) Schema: the canonical 12-field JSONL · `chunk_id` pattern `DECISION_JUDGMENT_COGNITION_NNN` (or `DECISION_JUDGMENT_NNN`). Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · 2 sources · no new domain · `decision-making` anchor · psychology/behavioral-psychology/behavioral-economics/cognition/bias/risk/uncertainty/decision-science/storytelling/narrative NOT created · storytelling sub-cluster + Denial of Death + Story/McKee 0 · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 13. Projected post-consolidation state (for reference · NOT applied now)

If the first lane (DECISION_JUDGMENT_COGNITION) ships at the mid-target (~12) and consolidates: 1,676 + ~12 = ~1,688 chunks · 10 numbered batches + 36 mini-batches · 62 domains (NO new domain · bumps to `decision-making` [anchor] / `mental-models` / `operator-process` / `operator-doctrine`, plus `systems-thinking` / `strategy` where warranted). Exact counts finalized at ship/consolidation time. Subsequent DECISION_JUDGMENT sub-lanes: CROWDS (Haidt ×2 + Hoffer + Le Bon) and MEANING (Frankl + Berne); then STORYTELLING_NARRATIVE (Truby + Campbell + Snyder; McKee broken), Tier-2 (incl the Greene trio), BRAND_CANON.

## 14. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,676.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 15. Next step (operator decision · do not start without authorization)

Authorize the **DECISION_JUDGMENT_COGNITION** first lane (2 curated sources · Thinking, Fast and Slow + Noise · target ~11-13 · existing domains only · `decision-making` anchor · no new domain · psychology/behavioral-psychology/behavioral-economics/cognition/bias/risk/uncertainty/decision-science/storytelling/narrative NOT created · the storytelling sub-cluster + broken Denial of Death / Story deferred · Bible excluded · curated, not exhaustive · decision-support not a directive), then commit the ship outputs, then consolidate. The CROWDS and MEANING sub-lanes (and the separate STORYTELLING_NARRATIVE lane) follow as their own plan/ship/consolidate cycles.
