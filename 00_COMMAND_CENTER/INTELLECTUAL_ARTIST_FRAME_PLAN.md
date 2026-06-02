# INTELLECTUAL_ARTIST_FRAME mini-batch plan · 2026-05-19

Plan only. No extraction, no chunking, no master-file updates. Authorization required before any execution.

**Theme:** MJ Moonwalk (1988 original · 2009 Crown Archetype reissue) as primary-source backing for the preserved operator-doctrine frame:

- Disciplined uninterrupted time as a non-negotiable operating condition
- Deep study over content-churn
- Intellectual artist · craft as study, not performance-for-its-own-sake
- Obsessive craft development across multiple lifetimes-of-practice
- Performer / operator lineage (Astaire, Brown, Gordy mentorship chain)
- Depth over half-baked attention-span energy
- Cross-domain study: music, dance, film, composition, movement, mythology, image-making

**Smallest validation pass** for the 2026-05-19 intake staging copy (35 files committed in `215ffce`). Validates the new mini-batch naming convention (non-BATCH_NNN), the new `02_TIER_1_CANON_BOOKS/operating_founder/` chapter neighbor pattern, and the epub extraction pipeline against a small source before the larger downstream mini-batches run.

---

## 1 · Source confirmation

**Source path:**
```
raw/02_TIER_1_CANON_BOOKS/operating_founder/ Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub
```

**File details:**
- Size: 411,489 bytes (~411 KB)
- Format: `.epub`
- Note: filename has a leading space (libgen.li download artifact). Preserve verbatim in source_file references; normalize to `mj_moonwalk.txt` at extraction time.
- Staged: 2026-05-19 (commit `215ffce`)
- Neighbors in `operating_founder/`: Goldratt The Goal, Hammer/Champy Reengineering the Corporation, Hoffman/Yeh Blitzscaling, Wasserman Founder's Dilemmas, Slootman Amp It Up, Horowitz The Hard Thing, Ries The Lean Startup, Weinberg/Mares Traction, Warrillow Built to Sell, Gerber E-Myth Revisited, etc. Moonwalk sits intentionally outside the founder-canon · operator-as-craft-artist lineage rather than operator-as-startup-builder.

**Source exists.** Confirmed via `ls -la` at plan-write time.

---

## 2 · Extraction method

**Method:** `ebook-convert` (Calibre · already on PATH at `/opt/homebrew/bin/ebook-convert`).

```bash
ebook-convert \
  "raw/02_TIER_1_CANON_BOOKS/operating_founder/ Michael Jackson - Moonwalk (2009, Crown Archetype) - libgen.li.epub" \
  "01_KNOWLEDGE_BASE/batches/intellectual_artist_frame_extracted/mj_moonwalk.txt" \
  --enable-heuristics
```

**Rationale:**
- Same epub → txt pipeline used successfully in BATCH_005 (Barthes `Camera Lucida`, Day `Robert Frank's The Americans`, Stevens `Avedon: Something Personal`, Freeman `The Photographer's Vision`, Maisel `Light, Gesture, and Color`).
- `--enable-heuristics` improves paragraph/section detection for memoir-formatted epubs.
- Output: plain text `.txt` for chunking.

**Sanity check at extraction time:**
- Expected word count: 50,000-80,000 words (Moonwalk is a ~280-page memoir).
- If extraction yields < 500 words, mark OCR-deferred (matches the BATCH_005 sanity-check rule) and surface to operator.
- No expected OCR risk · MJ Moonwalk has clean text-layer in the 2009 epub edition.

**Tooling confirmed on PATH:** `ebook-convert`, `pandoc`, `jq` all present.

---

## 3 · Estimated chunk yield

**Target: 7 chunks · range 5-10.**

Per-chunk breakdown (anticipated · final count determined at extraction time based on actual content density):

| # | Provisional concept | Domain | Notes |
|--:|---|---|---|
| 1 | Disciplined-time frame · MJ's daily-practice non-negotiable | operator-doctrine | The load-bearing chunk · MJ's account of his own rehearsal-volume + uninterrupted-time discipline |
| 2 | Cross-domain study · music + dance + film + composition + image-making | operator-doctrine | The intellectual-artist breadth · MJ's deliberate study across mediums |
| 3 | Performer / operator lineage · Astaire + James Brown + Gordy mentorship | operator-doctrine | The lineage chain · who MJ studied from and how |
| 4 | Obsessive craft development · reverse-engineered dance moves + repetition patterns | operator-doctrine | The craft-discipline frame · specific examples of move-construction |
| 5 | Stagecraft + image-making · persona construction + visual signature | aesthetics | Pairs with B4 aesthetic-doctrine + B5 Avedon-apparatus chunks |
| 6 | Depth-over-churn · the long-game career arc | operator-doctrine | The anti-content-churn frame · MJ's articulated decade-arc thinking |
| 7 | Movement composition · gesture as primary-source counterpoint | aesthetics | Maisel's "gesture" from B5 reframed in dance-composition register |

**Optional 8th-10th chunks** if content density supports:
- Mythology + persona register (MJ's awareness of stagecraft persona as deliberate construction)
- Cross-cultural study (specific non-American references that shaped his work)
- Refusal discipline (what MJ refused to do · pairs with the SNIPED 65+ named-refusals catalog)

**Stay in 5-10 range.** This is a single 411-KB epub · the 7-chunk center estimate reflects realistic content-density extraction without over-fitting.

---

## 4 · Approved domains + tags

**Approved domains (3 existing · no new domains needed):**

| Domain | Status | Expected chunks |
|---|---|---:|
| `operator-doctrine` | EXISTING (B5/B6/B7) | ~5 |
| `aesthetics` | EXISTING (B5/B6/B7) | ~2 |
| `taste` | EXISTING (B5) · optional cross-tag | 0-1 |

**Recommended primary-domain split:** 5 operator-doctrine + 2 aesthetics = 7 chunks. No NEW domains required · the chunks fit cleanly inside existing buckets.

**Why no NEW domain (e.g., `craft-discipline`):** The operator-doctrine domain already absorbs discipline frames (sniped-canonical-truths + lean-execution-audit + Saturday-build cadence). Adding a 4th NEW operator-engine domain would dilute the routing taxonomy. Future similar acquisitions (Quincy Jones autobiography, Miles Davis autobiography, etc.) can join the same domain bucket.

**Approved tag set (per AGENTS.md schema · array field):**

Core tags (apply to most chunks):
- `mj-moonwalk`
- `intellectual-artist-frame`
- `operator-doctrine`
- `cross-domain-study`
- `disciplined-time`

Per-chunk specific tags:
- chunk 1: `disciplined-time`, `daily-practice`, `uninterrupted-time`, `operator-cadence`
- chunk 2: `cross-domain-study`, `music-dance-film`, `breadth-of-study`, `intellectual-artist`
- chunk 3: `performer-operator-lineage`, `fred-astaire`, `james-brown`, `berry-gordy`, `mentorship-chain`
- chunk 4: `obsessive-craft`, `reverse-engineered-moves`, `rehearsal-volume`, `repetition-pattern`
- chunk 5: `stagecraft`, `persona-construction`, `image-making`, `apparatus-layer`
- chunk 6: `depth-over-churn`, `decade-arc`, `long-game-career`, `anti-content-churn`
- chunk 7: `movement-composition`, `gesture`, `dance-composition`

**Tag-taxonomy alignment:** All proposed tags follow the existing kebab-case + cross-batch-reuse convention (see B6 `extended-methodology`, B7 `7-signature-test`, B5 `studio-as-apparatus` pattern).

---

## 5 · How this mini-batch connects to existing corpus

### Connection to BATCH_004 (locked aesthetic discipline · 6 Aesthetic_Statement_v1 chunks)

MJ Moonwalk validates the locked SNIPED aesthetic discipline from a primary-source-stagecraft angle:

- **Aesthetic Statement v1 · 5 signatures + 5 descriptors filter** ↔ MJ's deliberate persona-construction discipline · the chunk on stagecraft (5) gives a cross-cultural backing for the locked aesthetic framework.
- **Aesthetic Statement what-is-NOT catalog** ↔ MJ's named-refusals (what he refused to perform / record / endorse) · the optional 8th chunk surfaces a parallel refusal-discipline cluster.
- **B4 SYNTHESIS Moat 2 longitudinal commitment** ↔ MJ's decade-arc career thinking · chunk 6 (depth-over-churn).

### Connection to BATCH_005 (photography canon · 161 chunks · 9-photographer Art Series)

MJ Moonwalk is the gesture / movement / composition primary-source counterpoint to the photography canon:

- **Maisel's three things (light, gesture, color)** ↔ MJ's chunk 7 (movement composition · gesture as primary-source backing). Maisel said the photographer captures gesture; MJ studied gesture as the performer who creates it. Two halves of the same coin.
- **Stevens-Avedon studio-as-apparatus** ↔ MJ's chunk 5 (stagecraft + persona construction). Avedon's apparatus is the photographic studio; MJ's apparatus is the stage + rehearsal room. Both are operator-grade systems.
- **Barthes's four-poses + the "becoming-body" moment** ↔ MJ's chunk 4 (reverse-engineered moves) · the dance move is the becoming-body moment at performer-side, not subject-side.
- **9-photographer Art Series doctrine** ↔ the mini-batch could be the seed for a future `9-PERFORMER_LINEAGE` Art Series (MJ + Quincy + Astaire + Brown + Gordy + Diana Ross + Stevie Wonder + Bowie + Prince) · operator decision · post-mini-batch validation.

### Connection to BATCH_007 (locked doctrine + SOPs · 128 chunks)

MJ Moonwalk grounds the SNIPED operator-doctrine cluster with primary-source backing:

- **THE SPINE Section 5 (10 Direction Stack protocols)** ↔ MJ's chunk 4 (obsessive craft development · reverse-engineered moves). MJ's process of breaking down a move into its constituent micro-steps mirrors the Direction Stack diagnostic's calibration discipline.
- **SATURDAY_BUILD_BRIEF + recurring_checklists · Sunday rest discipline** ↔ MJ's chunk 1 (disciplined-time). MJ's account of uninterrupted-time-as-non-negotiable backs the SNIPED Saturday-build + Sunday-rest cadence with cultural-canon weight.
- **CANONICAL_TRUTHS Truth 5 (operator-coded definition)** ↔ MJ's chunk 3 (performer / operator lineage). The Astaire-Brown-Gordy mentorship chain is operator-coded craft transmission · same structural pattern as the SNIPED methodology-as-IP doctrine.
- **content_philosophy · single-intentional-element rule + 99-percent-baseline-plus-1-percent-departure** ↔ MJ's chunk 7 (movement composition). The single deliberate move in a sequence + the choreographed-baseline pattern mirrors the SNIPED frame discipline.
- **B7 content-philosophy operator-engineering principles (locked-frame methodology + system over inspiration + pricing-is-the-price)** ↔ MJ's chunk 2 (cross-domain study) + chunk 6 (depth-over-churn). The operator-engineering frame is system-over-inspiration · MJ's account of crossover study + repetition is the cultural-canon validation.

### Connection to BATCH_006 (operator-engine skill layer · 114 chunks)

- **sniped-canonical-truths skill** ↔ chunks 1, 3, 6 (discipline + lineage + depth-over-churn) ground 3 of the 12 canonical truths in primary-source cultural-canon backing.
- **sniped-direction-stack skill** ↔ chunk 4 (reverse-engineered moves) is the cross-cultural cousin of the 5-question diagnostic.
- **sniped-lean-audit skill** ↔ chunk 1 (disciplined uninterrupted time) is the time-budget discipline at performer-canon scale.

### Connection to intel auto-memory

- `intel_perennial_logic.md` (Holiday) · MJ's chunk 6 (depth-over-churn · decade-arc) directly validates Holiday's "build for the long-tail" thesis with cultural-canon weight.
- `intel_hit_mechanics.md` (Berger) · MJ's chunk 4 (reverse-engineered moves) is the cross-domain analog to Berger's MAYA principle (familiar + surprising · dance moves built from familiar-vocabulary + 1-deliberate-surprise).
- `intel_blockbuster_strategy.md` (Elberse) · MJ's chunk 6 (decade-arc) is the operator-side companion to Elberse's distribution-dominates thesis.
- The preserved operator note `project_sniped_meta_thesis.md` (BJ's 2026-05-07 articulated thesis · photography is the 2026 moat, systems-as-creative-leverage is the method, product emerges in 2028+) is directly reinforced by MJ's depth-over-churn frame.

### Connection to feedback auto-memory

- `feedback_repetition_over_novelty.md` (LOCKED 2026-05-12 · architecture is built; next 90 days are reps; new strategic frameworks BANNED) ↔ MJ's chunks 1 and 4 (disciplined-time + obsessive-craft · rehearsal volume) are the cultural-canon validation of the operator's repetition-over-novelty discipline.
- `feedback_scene_density_thinking.md` (LOCKED 2026-05-12 · audience-growth OUT, scene-density IN) ↔ MJ's chunk 3 (performer-operator lineage · the Astaire-Brown-Gordy chain is scene-density inheritance at the highest cultural level).

---

## 6 · Deliverables

| File | Path | Purpose |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/INTELLECTUAL_ARTIST_FRAME_CHUNKS.jsonl` | Canonical chunked output · ~7 lines (range 5-10) |
| Extracted source tree | `01_KNOWLEDGE_BASE/batches/intellectual_artist_frame_extracted/` | 1 normalized `mj_moonwalk.txt` |
| Extraction script | `scripts/extract_intellectual_artist_frame.py` | Single-source ebook-convert wrapper · 500-word sanity check · log |
| Chunk writer | `scripts/write_intellectual_artist_frame_chunks.py` | Hand-authored chunk emit with the canonical 12-field schema |
| Summary | `01_KNOWLEDGE_BASE/summaries/INTELLECTUAL_ARTIST_FRAME_SUMMARY.md` | Narrative summary + cross-reference map |
| Source index | `01_KNOWLEDGE_BASE/indexes/INTELLECTUAL_ARTIST_FRAME_SOURCE_INDEX.md` | Per-chunk concept + range + cross-reference table |
| Extraction log | `00_COMMAND_CENTER/batch_logs/INTELLECTUAL_ARTIST_FRAME_EXTRACTION_LOG.md` | Single-job log · word count + status |
| Completion marker | `00_COMMAND_CENTER/batch_logs/INTELLECTUAL_ARTIST_FRAME_COMPLETE.md` | Headline numbers + validation summary + next-recommended-action |

**Both scripts are NEW.** Pattern templates: `scripts/extract_batch_005.py` (handles epub extraction) + `scripts/write_batch_007_chunks.py` (hand-authored 12-field chunk schema). Chunk_id pattern: `INTELLECTUAL_ARTIST_FRAME_001` through `_007` (or up to `_010` if content density supports).

---

## 7 · Validation requirements

Per `.claude/skills/jsonl-validation/SKILL.md`, the 6-check gate before chunks become canonical:

| Check | Method |
|---|---|
| JSONL parse | `jq -c . INTELLECTUAL_ARTIST_FRAME_CHUNKS.jsonl > /dev/null` · 0 errors |
| Required fields per line | `chunk_id`, `batch_id`, `source_title`, `source_file`, `author`, `domain`, `concept`, `summary`, `usable_principle`, `sniped_relevance`, `direct_quotes`, `tags` |
| chunk_id uniqueness | Python set check across ~7 chunks · 0 duplicates |
| batch_id consistency | Single value `INTELLECTUAL_ARTIST_FRAME` across all lines |
| source_file resolution | All `source_file` values resolve under `intellectual_artist_frame_extracted/` |
| Counts | Final tally · expected ~7 chunks · 1 unique source |

**Em-dash sweep** (lifetime rule per global CLAUDE.md): scan output JSONL for `chr(0x2014)`; if found, sweep to middle dot before validation.

---

## 8 · Schema decisions

**`batch_id` value:** `INTELLECTUAL_ARTIST_FRAME` (string · matches `BATCH_005` / `BATCH_006` / `BATCH_007` short-form pattern but uses a mini-batch slug instead of a numbered slot · preserves `BATCH_008` for the originally-planned AI/tech canon).

**`chunk_id` pattern:** `INTELLECTUAL_ARTIST_FRAME_NNN` (zero-padded 3-digit · e.g., `INTELLECTUAL_ARTIST_FRAME_001`).

**`author` value:** `Michael Jackson (with Robert Hilburn)` · the canonical co-author credit for Moonwalk. The Hilburn credit is documented in the 1988 first edition and preserved in the 2009 Crown Archetype reissue.

**`source_title` value:** `Moonwalk · Michael Jackson` (no em-dash · per lifetime rule).

**`source_file` value:** `mj_moonwalk.txt` (the normalized extracted filename).

**Schema family:** BATCH_003/004/005/006/007 canonical 12-field structure. Adds 1 new mini-batch to the master_index Family 9 (operator-doctrine-extension) or fits as a satellite of Family 7 (operator-engine skill layer) · operator decision at master-consolidation time.

---

## 9 · Extraction sequence (post-authorization · DO NOT EXECUTE NOW)

1. Operator authorizes mini-batch execution.
2. Run `scripts/extract_intellectual_artist_frame.py` to convert epub → `mj_moonwalk.txt` in `intellectual_artist_frame_extracted/`. Log word count + status in `INTELLECTUAL_ARTIST_FRAME_EXTRACTION_LOG.md`. Halt if word count < 500.
3. Run `scripts/write_intellectual_artist_frame_chunks.py` to emit `INTELLECTUAL_ARTIST_FRAME_CHUNKS.jsonl` with 7-10 hand-authored chunks per §3 + §4.
4. Run the 6-check validation gate against the JSONL.
5. Write `INTELLECTUAL_ARTIST_FRAME_SUMMARY.md` + `INTELLECTUAL_ARTIST_FRAME_SOURCE_INDEX.md`.
6. Write `INTELLECTUAL_ARTIST_FRAME_COMPLETE.md` completion marker.
7. STOP. Do not update master files. Operator authorizes `master-consolidation` in a separate session. New corpus total after consolidation: 860 + 7 (or wherever count lands) = ~867.

---

## 10 · What this mini-batch enables (post-consolidation)

1. **Primary-source backing for the disciplined-time / depth-over-churn frame** that previously existed only in operator notes (preserved in `feedback_repetition_over_novelty.md` + `feedback_scene_density_thinking.md`).
2. **Cross-cultural validation of the operator-coded identity claim** (THE_OPERATOR_CODED_DEFINITION.md). MJ Moonwalk gives the highest-tier cultural-canon weight to the operator-as-craft-artist-not-product-builder distinction.
3. **The performer-operator lineage** (Astaire → Brown → Gordy → MJ) becomes a chunk-addressable structural pattern that mirrors the 9-photographer Art Series (B5) and the SNIPED methodology-transmission discipline.
4. **The "intellectual artist" frame** gains a load-bearing chunk that future content-strategy work (LinkedIn POV bank, IG captions, Direction Stack book chapters) can pull from with primary-source attribution.
5. **The 2-hop retrieval pattern (B6 skill → B7 doctrine → mini-batch source-of-truth)** extends to a 3-hop pattern when the source is a non-SNIPED canonical work · B6 skill → B7 doctrine → mini-batch cultural-canon backing.
6. **Validates the new mini-batch naming convention.** Future similar single-source mini-batches (Quincy Jones autobiography, Miles Davis autobiography, etc.) can follow the same `BATCH_<THEME_NAME>` pattern without consuming numbered batch slots.

---

## 11 · What this plan does NOT do

- No extraction. `intellectual_artist_frame_extracted/` is not created.
- No chunking. `INTELLECTUAL_ARTIST_FRAME_CHUNKS.jsonl` is not written.
- No master file updates. `MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched.
- No commits.
- No new dependencies. `ebook-convert`, `pandoc`, `jq` already on PATH.
- No source moves. `raw/02_TIER_1_CANON_BOOKS/operating_founder/` is read-only this session.
- No BATCH_008 start. BATCH_008 AI/tech canon remains reserved.

Authorization required before any of the above. Stop here.

---

## 12 · Operator decisions surfaced (none blocking · plan can proceed as written)

1. **`craft-discipline` proposed as NEW domain · REJECTED in this plan.** Recommendation is to reuse `operator-doctrine` for the 5 discipline-frame chunks rather than add a 4th NEW operator-engine domain. Operator can override at extraction-time if a NEW domain is preferred for downstream cluster expansion (future MJ-adjacent acquisitions).
2. **Family 9 vs Family 7 satellite at master-consolidation time.** Two options for how this mini-batch lands in `MASTER_INDEX.md`:
   - Option A · NEW Family 9 (`operator-doctrine extensions from cultural canon · MJ Moonwalk + future acquisitions`). Cleanest for future mini-batches.
   - Option B · satellite of Family 7 (operator-engine skill layer) · folds the cultural-canon backing into the existing operator-doctrine cluster.
   - Default recommendation: NEW Family 9. Decision deferred to master-consolidation.
3. **9-PERFORMER_LINEAGE future Art Series** (operator decision · NOT in scope for this mini-batch). MJ + Quincy + Astaire + Brown + Gordy + Diana Ross + Stevie Wonder + Bowie + Prince is a candidate parallel-canon to the 9-photographer Art Series. Hold for future operator decision after this mini-batch validates the pattern.
4. **Author attribution decision: `Michael Jackson (with Robert Hilburn)` vs `Michael Jackson`** · operator preference at chunk-write time. Default: include Hilburn co-author credit (matches the canonical attribution in the source).
