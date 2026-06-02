# PERSONAL_OPERATING_CODE mini-batch plan · 88 Laws of the Masculine Mindset · 2026-05-19

Plan only. No extraction, no chunking, no master-file updates. Authorization required before any execution.

**Theme:** John Winters · *The 88 Laws Of The Masculine Mindset · How To Elevate Your Life To The Next Level* (Calibre-generated PDF · 2025) as prescriptive primary-source backing for the SNIPED operator-doctrine cluster. Where INTELLECTUAL_ARTIST_FRAME (MJ Moonwalk · 7 chunks) gives **descriptive** cultural-canon weight to the disciplined-time + cross-domain-study + performer-operator-lineage frame, this mini-batch gives **prescriptive** cultural-canon weight to the same cluster from a different rhetorical register.

**Pairs structurally with INTELLECTUAL_ARTIST_FRAME** · the two mini-batches sit together in Family 9 (operator-doctrine cultural-canon extensions) as the back-to-back operator-doctrine compounding pass per the operator-queued position 2 designation in `NEW_INTAKE_ACK_2026-05-19_88_LAWS.md` §7.

**Scope: tightly filtered.** Per operator brief: extract only the operator-doctrine substrate. Skip the gender-war framing + nutrition + dating + fitness tactics + body-image + culture-war commentary. The chunker (when authorized) must explicitly skip chapters that cannot be framed as a reinforcement of the SNIPED operator-doctrine cluster.

---

## 1 · Source confirmation

**Source path:**
```
raw/02_TIER_1_CANON_BOOKS/operating_founder/_OceanofPDF.com_The_88_Laws_Of_The_Masculine_Mindset_-_John_Winters.pdf
```

**File details:**
- Size: 1,164,280 bytes (~1.16 MB)
- Format: PDF v1.4 · 163 pages · letter (612 × 792 pts)
- Producer: Calibre 7.4.0 (likely epub-to-PDF conversion · clean text layer expected)
- CreationDate: 2025-01-01
- Encrypted: NO
- Title metadata: "The 88 Laws Of The Masculine Mindset: How To Elevate Your Life To The Next Level"
- Author metadata: "Winters, John"
- Staged: 2026-05-19 (commit `44f4776`)
- Neighbors in `operating_founder/`: MJ Moonwalk (just chunked in INTELLECTUAL_ARTIST_FRAME), Goldratt The Goal, Hammer/Champy Reengineering the Corporation, Hoffman/Yeh Blitzscaling, Wasserman Founder's Dilemmas, Slootman Amp It Up, Horowitz The Hard Thing, Ries The Lean Startup, Warrillow Built to Sell, Gerber E-Myth Revisited, Weinberg/Mares Traction.

**Source exists.** Confirmed via `ls -la` at plan-write time.

---

## 2 · Extraction method

**Method:** `pdftotext -layout` (already on PATH at `/opt/homebrew/bin/pdftotext`).

```bash
pdftotext -layout \
  "raw/02_TIER_1_CANON_BOOKS/operating_founder/_OceanofPDF.com_The_88_Laws_Of_The_Masculine_Mindset_-_John_Winters.pdf" \
  "01_KNOWLEDGE_BASE/batches/personal_operating_code_extracted/88_laws_winters.txt"
```

**Rationale:**
- PDF format · `pdftotext` is the canonical extractor.
- `-layout` preserves visual structure (chapter headers + 88 numbered laws), which makes selective chunking easier.
- Same pipeline used in BATCH_005 for `sontag_on_photography.txt` and other text-dense PDFs.
- Output: plain text `.txt` for chunking.
- Normalize filename to `88_laws_winters.txt` at extraction (drop OceanofPDF prefix).

**No OCR needed.** Text layer is healthy.

---

## 3 · Text-layer check

**Pre-flight result:** PDF has a clean, extractable text layer.

- `pdftotext -layout -f 1 -l 10` produced **1,464 words** in the first 10 pages.
- Extrapolated whole-book estimate: ~24,000 words across 163 pages (low end · 88 Laws format implies short pithy chapters with whitespace).
- Sample of pages 1-2 shows clean title + author rendering · no OCR artifacts, no garbled characters.

**500-word sanity check at extraction time:** expected to pass comfortably. If extraction yields < 500 words against expectation (~24K), halt and surface to operator (would indicate a Calibre PDF that needs different extractor flags).

**No OCR. No `ocrmypdf`. No fallback to image extraction.**

---

## 4 · Estimated chunk yield

**Target: 8 chunks · range 7-10.**

Per-chunk breakdown (anticipated · final count determined at extraction-time content density · provisional concept list mirrors `NEW_INTAKE_ACK_2026-05-19_88_LAWS.md` §6):

| # | Provisional concept | Domain | Notes |
|--:|---|---|---|
| 1 | Ownership · radical self-responsibility as operating axiom | operator-doctrine | The first-principles chunk · the move from blaming external conditions to owning internal response |
| 2 | Discipline · daily-rep cadence + non-negotiable conditions | operator-doctrine | Pairs with INTELLECTUAL_ARTIST_FRAME_001 (rehearsal-as-default) · prescriptive complement to MJ's descriptive account |
| 3 | Mission obsession · single-thread focus + the elimination discipline | operator-doctrine | The thing-that-matters lens · pairs with B7 Monday cockpit one-thing-that-must-happen filter |
| 4 | Code · self-imposed rule-system as identity | operator-doctrine | Rules as scaffolding for identity · pairs with B7 CANONICAL_TRUTHS override-on-conflict pattern |
| 5 | Time control · time-as-currency + opportunity-cost thinking | operator-process | Time as the finite asset · pairs with B7 Monday cockpit + Saturday-build cadence |
| 6 | Consistency · streak discipline + the compound-arc thesis | operator-doctrine | The long-game thesis · pairs with B3 Holiday perennial-seller + feedback_repetition_over_novelty + INTELLECTUAL_ARTIST_FRAME_006 depth-over-churn |
| 7 | Execution · ship-over-plan + bias-to-action | operator-doctrine | Pairs with B4 Lock 10 (architecture refinement banned · execution is the only frontier) + B7 LEAN_EXECUTION_AUDIT |
| 8 | Composure · state management under pressure + emotional regulation | operator-process | The unflappable register · pairs with B3 Guidara hospitality + INTELLECTUAL_ARTIST_FRAME_004 no-off-night discipline |

**Optional 9th-10th chunks** if content density supports:
- Resourcefulness · problem-solving frame · the "find a way" discipline (operator-doctrine)
- Self-audit · operator-feedback loop · the weekly-review + lean-audit habit (operator-process · pairs with B7 weekly_review template + LEAN_EXECUTION_AUDIT)
- Mindset-as-software · install discipline as default state (operator-doctrine · the meta-chunk · the frame that holds the other chunks together)

**Stay in 7-10 range.** Realistic landing: 8 chunks at hand-authored depth. Padding to 10 risks low-signal additions.

---

## 5 · Approved domains + tags

**Approved domains (2 existing · `taste`/`aesthetics` optional · no new domains needed):**

| Domain | Status | Expected chunks |
|---|---|---:|
| `operator-doctrine` | EXISTING (B5/B6/B7/IAF) | ~6 |
| `operator-process` | EXISTING (B6/B7) | ~2 |
| `aesthetics` | EXISTING · optional cross-tag | 0 (only if composure surfaces as image-making material) |

**Recommended primary-domain split:** 6 operator-doctrine + 2 operator-process = 8 chunks. No NEW domains required.

**Why no NEW domain (e.g., `personal-operating-code`, `discipline-code`, `mindset-as-software`):** Existing `operator-doctrine` and `operator-process` buckets absorb the content cleanly. Adding a NEW domain for a single mini-batch would dilute the routing taxonomy. Future similar acquisitions (Jocko Willink *Discipline Equals Freedom*, Marcus Aurelius *Meditations*, Goggins *Can't Hurt Me*, Pressfield *War of Art*) can join the same domain bucket.

**Approved tag set (per AGENTS.md schema · array field):**

Core tags (apply to most chunks):
- `88-laws`
- `winters`
- `personal-operating-code`
- `operator-doctrine`
- `mindset-as-software`

Per-chunk specific tags:
- chunk 1: `ownership`, `radical-responsibility`, `internal-locus-of-control`, `operator-axiom`
- chunk 2: `discipline`, `daily-rep-cadence`, `non-negotiable-conditions`, `rehearsal-as-default`
- chunk 3: `mission-obsession`, `single-thread-focus`, `elimination-discipline`, `one-thing-that-matters`
- chunk 4: `code`, `self-imposed-rules`, `rules-as-identity`, `canonical-truths-pattern`
- chunk 5: `time-control`, `time-as-currency`, `opportunity-cost`, `time-as-finite-asset`
- chunk 6: `consistency`, `streak-discipline`, `compound-arc`, `long-game-thesis`
- chunk 7: `execution`, `ship-over-plan`, `bias-to-action`, `lock-10-companion`
- chunk 8: `composure`, `state-management`, `emotional-regulation`, `no-off-night`

**Tag-taxonomy alignment:** All tags follow the existing kebab-case + cross-batch-reuse convention. `88-laws` and `winters` are new source-attribution tags. `personal-operating-code` is the new mini-batch slug.

---

## 6 · How this mini-batch connects to existing corpus

### Connection to INTELLECTUAL_ARTIST_FRAME (MJ Moonwalk · 7 chunks · just consolidated)

The two mini-batches are **structurally complementary** · same operator-doctrine cluster, different rhetorical registers:

| INTELLECTUAL_ARTIST_FRAME (descriptive) | PERSONAL_OPERATING_CODE (prescriptive) |
|---|---|
| 001 disciplined-time (rehearsal-as-default) | 2 discipline (daily-rep cadence as non-negotiable condition) |
| 002 cross-domain study (deciphering performers' mechanics) | (no direct PERSONAL chunk · MJ's empirical study has no prescriptive parallel in 88 Laws) |
| 003 performer-operator lineage (Astaire-Brown-Gordy chain) | (no direct PERSONAL chunk · Winters is rule-based not lineage-based) |
| 004 obsessive craft (concentration-burn + no-off-night) | 8 composure (state management under pressure · emotional regulation) |
| 005 stagecraft + image-making (pre-planning apparatus) | (no direct PERSONAL chunk · 88 Laws does not deeply cover stagecraft) |
| 006 depth-over-churn (change-as-growth · long-game arc) | 6 consistency (streak discipline · compound-arc thesis) |
| 007 movement composition (gesture as composable language) | (no direct PERSONAL chunk · 88 Laws does not cover gesture craft) |

**Net effect:** 5 of 8 PERSONAL chunks pair with IAF chunks at the doctrine level. 3 of 8 PERSONAL chunks (ownership · mission obsession · code · time control · execution) extend the cluster into prescriptive territory that MJ did not cover directly. Together, the two mini-batches give the operator-doctrine cluster ~14 cultural-canon-backed chunks across descriptive and prescriptive registers.

### Connection to BATCH_007 (locked doctrine + SOPs · 128 chunks)

PERSONAL_OPERATING_CODE chunks ground SNIPED-internal doctrine in prescriptive cultural-canon backing:

- **CANONICAL_TRUTHS.md (B7 · 3 chunks)** ↔ chunk 4 (code · self-imposed rule-system as identity). The 12 SNIPED canonical truths follow the same structural pattern Winters prescribes · self-imposed rules that override on conflict. The pattern is the canonical-truths frame at primary-source weight.
- **THE_OPERATOR_CODED_DEFINITION.md (B7 · 2 chunks · un-delegate-ables ledger)** ↔ chunk 1 (ownership · radical self-responsibility). The un-delegate-ables ledger is the operationalized form of the radical-responsibility axiom.
- **LEAN_EXECUTION_AUDIT.md (B7 · 4 chunks · 100Q recalibration overrides + 2026 win conditions + force-decide rule)** ↔ chunks 7 (execution · ship-over-plan) + 9-optional (self-audit · operator-feedback loop). The lean audit is the operationalized form of the bias-to-action + self-audit discipline.
- **MONDAY_COCKPIT.md (B7 · 2 chunks · one-thing-that-must-happen filter)** ↔ chunk 3 (mission obsession · single-thread focus). Same structural pattern.
- **SATURDAY_BUILD_BRIEF.md (B7 · 3 chunks · 3-tier priority stack)** ↔ chunk 5 (time control · time-as-currency). Saturday-as-protected-build-time is the time-control discipline operationalized.
- **recurring_checklists.md (B7 · 2 chunks · daily/weekly cadence + Sunday rest)** ↔ chunk 2 (discipline · daily-rep cadence).
- **SYSTEM_FINAL_STATUS.md (B7 · 4 chunks · 65+ named-refusals + BASEPLATE firewall + Year-10 destination)** ↔ chunk 6 (consistency · long-game arc). The Year-10 destination is the multi-decade execution of the compound-arc thesis.

### Connection to BATCH_006 (operator-engine skill layer · 114 chunks)

- **sniped-canonical-truths skill** ↔ chunks 1+4 (ownership + code) · the skill invokes the canonical-truth frame; PERSONAL chunks 1+4 give it primary-source prescriptive backing.
- **sniped-monday-cockpit skill** ↔ chunks 3+5 (mission + time control).
- **sniped-lean-audit skill** ↔ chunks 7 + optional self-audit.
- **sniped-execution-prioritization skill** ↔ chunk 3 (mission obsession · single-thread focus).

### Connection to BATCH_004 (locked aesthetic discipline · 6 Aesthetic_Statement_v1 chunks)

Indirect connection only. PERSONAL_OPERATING_CODE is operator-doctrine territory, not aesthetic-doctrine. If chunk 8 (composure) reads as image-making material (the un-shaken-on-stage register), it could cross-tag `aesthetics` · operator decision at chunk-write time.

### Connection to intel + feedback auto-memory

- `intel_perennial_logic.md` (Holiday · perennial-seller · long-game patience) ↔ chunk 6 (consistency · compound-arc · long-game thesis) at high signal density.
- `intel_leverage_logic.md` (Naval · 3 forms of leverage) ↔ chunk 5 (time control · time-as-currency) tangentially.
- `feedback_repetition_over_novelty.md` (LOCKED 2026-05-12) ↔ chunks 2 + 6 (discipline + consistency) directly.
- `feedback_max_default.md` (LOCKED 2026-05-12 · every task ships max creative/strategic depth by default) ↔ chunk 7 (execution · ship-over-plan).
- `project_sniped_meta_thesis.md` (BJ's 2026-05-07 articulated thesis) ↔ chunks 6 + optional self-audit.

---

## 7 · Deliverables

| File | Path | Purpose |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/PERSONAL_OPERATING_CODE_CHUNKS.jsonl` | Canonical chunked output · ~8 lines (range 7-10) |
| Extracted source | `01_KNOWLEDGE_BASE/batches/personal_operating_code_extracted/88_laws_winters.txt` | Normalized pdftotext output |
| Extraction script | `scripts/extract_personal_operating_code.py` | Single-source pdftotext wrapper · 500-word sanity check · log |
| Chunk writer | `scripts/write_personal_operating_code_chunks.py` | Hand-authored chunk emit with canonical 12-field schema + em-dash sweep |
| Summary | `01_KNOWLEDGE_BASE/summaries/PERSONAL_OPERATING_CODE_SUMMARY.md` | Narrative summary + cross-reference map (INTELLECTUAL_ARTIST_FRAME pairing table + B4/B6/B7 references) |
| Source index | `01_KNOWLEDGE_BASE/indexes/PERSONAL_OPERATING_CODE_SOURCE_INDEX.md` | Per-chunk concept + range + cross-reference table |
| Extraction log | `00_COMMAND_CENTER/batch_logs/PERSONAL_OPERATING_CODE_EXTRACTION_LOG.md` | Single-job log · word count + status |
| Completion marker | `00_COMMAND_CENTER/batch_logs/PERSONAL_OPERATING_CODE_COMPLETE.md` | Headline numbers + validation summary + next-recommended-action |

**Both scripts are NEW.** Pattern templates:
- `scripts/extract_intellectual_artist_frame.py` (single-source wrapper) → adapt for `pdftotext -layout` instead of `ebook-convert`
- `scripts/write_intellectual_artist_frame_chunks.py` (hand-authored 8-chunk emit · operator-doctrine cluster · em-dash sweep) → adapt concept list per §4

**Chunk_id pattern:** `PERSONAL_OPERATING_CODE_001` through `_008` (or up to `_010` if content density supports).

---

## 8 · Validation requirements

Per `.claude/skills/jsonl-validation/SKILL.md`, the 6-check gate:

| Check | Method |
|---|---|
| JSONL parse | `jq -c . PERSONAL_OPERATING_CODE_CHUNKS.jsonl > /dev/null` · 0 errors |
| Required fields per line | `chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags` |
| chunk_id uniqueness | Python set check · 0 duplicates |
| batch_id consistency | Single value `PERSONAL_OPERATING_CODE` across all lines |
| source_file resolution | All `source_file` values resolve under `personal_operating_code_extracted/` |
| Counts | Final tally · expected ~8 chunks · 1 unique source |

**Em-dash sweep** (lifetime rule per global CLAUDE.md): scan output JSONL for `chr(0x2014)`; sweep to middle dot before validation if found.

---

## 9 · Schema decisions

**`batch_id` value:** `PERSONAL_OPERATING_CODE` (mini-batch slug · matches the IAF `INTELLECTUAL_ARTIST_FRAME` naming pattern · preserves `BATCH_008` for the originally-planned AI/tech canon).

**`chunk_id` pattern:** `PERSONAL_OPERATING_CODE_NNN` (zero-padded 3-digit · `_001` through `_008`).

**`author` value:** `John Winters` (the only credited author · no co-author).

**`source_title` value:** `The 88 Laws Of The Masculine Mindset · John Winters` (no em-dash · per lifetime rule).

**`source_file` value:** `88_laws_winters.txt` (the normalized extracted filename · drops OceanofPDF prefix · drops " - " separators).

**Schema family:** BATCH_003-007 + INTELLECTUAL_ARTIST_FRAME canonical 12-field structure.

**`batch_kind`:** `mini-batch` (matches IAF entry in MASTER_CHUNK_MAP.json).

**Family at master-consolidation:** Family 9 (operator-doctrine cultural-canon extensions · the cluster opened by INTELLECTUAL_ARTIST_FRAME).

---

## 10 · INCLUDE / EXCLUDE scope discipline (per operator brief)

**INCLUDE** (chunkable content · estimated 7-10 chunks):

| Theme | SNIPED cross-reference |
|---|---|
| Ownership (radical self-responsibility · internal locus of control) | B7 THE_OPERATOR_CODED_DEFINITION + un-delegate-ables ledger |
| Discipline (daily-rep cadence · non-negotiable conditions) | B7 recurring_checklists + Monday cockpit + Saturday-build + INTELLECTUAL_ARTIST_FRAME_001 |
| Mission obsession (single-thread focus · elimination discipline) | B4 100Q win conditions + 12 canonical truths + project_sniped_meta_thesis |
| Code (rule-system as identity · self-imposed standards) | B7 CANONICAL_TRUTHS + OPERATING_LOCKS + 12 truths override-on-conflict |
| Time control (time-as-currency · opportunity-cost thinking) | B7 Monday cockpit one-thing + Saturday build cycle + feedback_execution_mode |
| Consistency (streak discipline · anti-streak-vs-streak doctrine) | B3 Holiday perennial-seller + feedback_repetition_over_novelty + INTELLECTUAL_ARTIST_FRAME_006 |
| Execution (ship-over-plan · bias-to-action) | B4 Lock 10 (architecture refinement banned · execution is the only frontier) |
| Composure (state management · emotional regulation under pressure) | B7 hospitality layer + B3 Guidara service-vs-hospitality + INTELLECTUAL_ARTIST_FRAME_004 |
| Resourcefulness (problem-solving frame · "find a way" discipline) · OPTIONAL | feedback_max_default + B7 operator-engineering principles |
| Self-audit (operator-feedback loop · weekly review + lean audit habit) · OPTIONAL | B7 LEAN_EXECUTION_AUDIT + monthly_constraint_audit + weekly_review templates |
| Mindset-as-software (install discipline as default state · meta-frame) · OPTIONAL | The connecting tissue chunk · pairs with INTELLECTUAL_ARTIST_FRAME meta-thesis |

**EXCLUDE / SKIP** (per operator brief · explicit skip list):

| Theme | Why excluded |
|---|---|
| Gender-war framing (manosphere rhetoric · men-vs-women cultural critique) | Off-theme · SNIPED operator-doctrine is gender-neutral · the locked Lineage Doctrine specifies cultural-lineage (Black church / HBCU / Southern athletic / engineering / LA Black founder), NOT gender |
| Dating / relationship strategy | Off-theme · personal life vs operating-system distinction |
| Nutrition specifics (macros · supplement stacks · meal plans) | Off-theme · adjacent to SNIPED but not load-bearing for operator-engine work |
| Fitness tactics (gym routines · specific exercise prescriptions) | Off-theme · same reason as nutrition |
| Body-image / aesthetic-performance prescriptions | Off-theme · SNIPED aesthetic discipline is for client work, not personal performance theater |
| Anti-feminist or culture-war commentary | Off-theme · risks contaminating chunks with content that would need to be filtered at retrieval time |
| Specific tactics for romantic-pursuit or social-dominance | Off-theme |
| Religious / spiritual prescriptions (beyond generic "purpose" framing) | Off-theme unless they align directly with operator-doctrine (mission obsession · code) |

**Chunk-time discipline (operator instruction):** if a Winters chapter or law cannot be framed as a reinforcement of the SNIPED operator-doctrine cluster, SKIP it. The chunker (when authorized) must hand-author each chunk with explicit SNIPED-relevance framing.

---

## 11 · Extraction sequence (post-authorization · DO NOT EXECUTE NOW)

1. Operator authorizes mini-batch execution.
2. Run `scripts/extract_personal_operating_code.py` to convert PDF → `88_laws_winters.txt` in `personal_operating_code_extracted/`. Log word count + status in `PERSONAL_OPERATING_CODE_EXTRACTION_LOG.md`. Halt if word count < 500.
3. Run `scripts/write_personal_operating_code_chunks.py` to emit `PERSONAL_OPERATING_CODE_CHUNKS.jsonl` with 7-10 hand-authored chunks per §4 + §5 + §10 (INCLUDE/EXCLUDE discipline).
4. Run the 6-check validation gate against the JSONL.
5. Write `PERSONAL_OPERATING_CODE_SUMMARY.md` + `PERSONAL_OPERATING_CODE_SOURCE_INDEX.md`.
6. Write `PERSONAL_OPERATING_CODE_COMPLETE.md` completion marker.
7. STOP. Do not update master files. Operator authorizes `master-consolidation PERSONAL_OPERATING_CODE` in a separate session. New corpus total after consolidation: 867 + 8 (or wherever count lands) = ~875.

---

## 12 · What this mini-batch enables (post-consolidation)

1. **Prescriptive primary-source backing for the SNIPED operator-doctrine cluster.** Where IAF (MJ Moonwalk) gives descriptive cultural-canon weight, 88 Laws gives prescriptive rule-system weight. Both reinforce the same cluster from different rhetorical angles.
2. **Family 9 (operator-doctrine cultural-canon extensions) expands from 1 mini-batch → 2.** Validates the cluster's structural integrity. Future similar acquisitions (Willink, Aurelius, Goggins, Pressfield) can join.
3. **Code-as-identity frame** (chunk 4) becomes chunk-addressable. The pattern Winters prescribes (self-imposed rules override identity-drift) is the structural backing for SNIPED's CANONICAL_TRUTHS override-on-conflict rule.
4. **Single-thread mission obsession** (chunk 3) gains a primary-source articulation. Anchor for future operator-questions sessions when scope-creep temptations surface.
5. **Time-as-currency frame** (chunk 5) gives the Saturday-build + Monday-cockpit + Sunday-rest cadence a primary-source rationale.
6. **Composure under pressure** (chunk 8) extends the hospitality-layer doctrine (B3 Guidara) and the no-off-night discipline (IAF 004) into state-management territory.
7. **3-hop retrieval pattern extends.** Operator question → B6 skill chunk → B7 doctrine chunk → PERSONAL_OPERATING_CODE prescriptive primary-source backing. Same pattern as IAF, but from the prescriptive register.

---

## 13 · What this plan does NOT do

- No extraction. `personal_operating_code_extracted/` is not created.
- No chunking. `PERSONAL_OPERATING_CODE_CHUNKS.jsonl` is not written.
- No master file updates. `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched.
- No commits.
- No new dependencies. `pdftotext`, `pdfinfo`, `jq` already on PATH.
- No source moves. The staged PDF in `raw/02_TIER_1_CANON_BOOKS/operating_founder/` is read-only this session.
- No OCR.
- No BATCH_008 start. BATCH_008 AI/tech canon stays reserved.

Authorization required before any of the above. Stop here.

---

## 14 · Operator decisions surfaced (3 items · all non-blocking)

1. **Optional 9th-10th chunks (resourcefulness · self-audit · mindset-as-software meta-chunk).** Plan provisions for 8 chunks · operator can authorize adding 1-2 optional chunks if content density supports. Default: ship 8 high-signal chunks rather than pad to 10.
2. **`aesthetics` cross-tag on chunk 8 (composure).** Composure as image-making material (the un-shaken-on-stage register) could cross-tag `aesthetics`. Default: keep chunk 8 as `operator-process` primary; surface as a tag if the content explicitly covers presentation-layer composure.
3. **`taste` cross-tag on chunk 6 (consistency).** The long-game compound-arc thesis pairs with B5 taste domain (the practiced eye). Default: do not cross-tag · `operator-doctrine` is the cleaner primary.

End of plan.
