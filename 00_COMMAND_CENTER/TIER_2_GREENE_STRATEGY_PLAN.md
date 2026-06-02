# TIER_2_GREENE_STRATEGY mini-batch · plan only · 2026-05-25

**Status:** PLAN ONLY. No extraction, no chunking, no master-file changes, no raw mutation, no Bible touch. This document locates the remaining Robert Greene / strategy-human-behavior candidates, probes extractability, runs an authoritative already-chunked overlap check, recommends a batch architecture, names the first lane, and stops. Nothing is extracted or chunked here.

## 0. Verified starting state

- **Head commit:** `4fa8ab4 save session after STORYTELLING_NARRATIVE consolidation`
- **Working tree:** clean (only this plan file is added after writing it).
- **Total chunks:** 1,726 · 10 numbered batches + 39 mini-batches · 62 official domains (75 combined keys).
- **DECISION_JUDGMENT sequence COMPLETE; STORYTELLING_NARRATIVE COMPLETE.** The Greene / strategy-human-behavior cluster is the named Tier-2 lane (the Greene trio flagged repeatedly across recent session saves).
- **CURRENT_OPERATOR_REALITY_BRIEF:** anchor-only / NOT chunked. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY:** plan-only / NOT extracted. Identity optionality guardrails ACTIVE.
- **Bible:** held / excluded / not chunked.

## 1. Candidate files located in raw/ (verified)

A full `raw/` sweep for Greene / power / strategy / seduction / mastery / human-nature found the following.

### A. The net-new Greene trio (the lane core · `raw/02_TIER_1_CANON_BOOKS/strategy_history/`)

| Source | Author | Format | Words (probe) | Status |
|---|---|---|--:|---|
| The Laws of Human Nature | Robert Greene | pdf | 270,897 | CLEAN · NET-NEW |
| Mastery | Robert Greene | epub | 153,468 | CLEAN · NET-NEW |
| The 50th Law | 50 Cent & Robert Greene | mobi | 71,830 | CLEAN · NET-NEW |

Combined: ~496,195 words. Read-only `pdftotext` / `ebook-convert`-to-/tmp probes (temp deleted; mtimes unchanged). Real book text confirmed by content sampling.

### B. Already-canonical Greene / strategy (BATCH_002 · verified · EXCLUDE)

| Source | Author | Where | Status |
|---|---|---|---|
| The 48 Laws of Power | Robert Greene | BATCH_002 | already-canonical |
| The 33 Strategies of War | Robert Greene | BATCH_002 | already-canonical |
| The Art of War | Sun Tzu | BATCH_002 | already-canonical |

### C. Broken (Greene-adjacent · DEFER)

| Source | Author | Format | Status |
|---|---|---|---|
| The Book of Five Rings | Miyamoto Musashi | djvu | BROKEN (no djvutxt · 0 text · re-acquire · NOT Greene) |

### D. Absent from the universe (noted · not a candidate)

- **The Art of Seduction (Greene)** is NOT present in `raw/` or the source universe (no `*seduction*` file). Not a candidate; nothing to chunk.

## 2. Source-quality / stub / scan check

- **3 clean, text-bearing Greene sources** (Laws of Human Nature pdf 270,897w · Mastery epub 153,468w · The 50th Law mobi 71,830w). pdfs via `pdftotext`, epub/mobi via `ebook-convert`. No OCR.
- **BROKEN (1 · not part of this lane):** The Book of Five Rings (djvu · 0 text) · re-acquire · this is a Musashi strategy classic, not Greene.
- At ship, sample each extracted .txt to confirm real book text before chunking.

## 3. Already-chunked overlap check (authoritative · by source_title / author across all 39 batch jsonls)

**The 3 Greene trio books are NET-NEW as sources** (0 chunks each · verified):
- The Laws of Human Nature · Mastery · The 50th Law · **net-new.**

**Checked against the operator's named lanes:**
- **BATCH_002:** holds The 48 Laws of Power + The 33 Strategies of War (Greene) + The Art of War (Sun Tzu) · already-canonical · EXCLUDED. The trio is a distinct, net-new Greene set (human-nature / mastery / fearlessness, not the laws-of-power / strategies-of-war pair).
- **CLASSICAL_STRATEGY** (The Prince / On War / Meditations / Caesar), **CLASSICAL_HISTORY** (Herodotus / Thucydides / Arrian / Engels), **MODERN_COMMAND_NAPOLEON** (Napoleon), **POLITICAL_THEORY_DISCOURSES** (Discourses on Livy): the classical/strategy treatises · all already-canonical · the entire `strategy_history/` folder is canonical EXCEPT the 3 Greene trio (net-new) and Five Rings (broken).
- **HISTORICAL_BIOGRAPHY** (Grant / Washington), **DECISION_JUDGMENT** (Kahneman / Haidt / Frankl / Berne), **PERSUASION_RECOVERY** (Predictably Irrational): adjacent registers · no overlap with the Greene trio (cross-references opened in §9, not re-chunks).
- No existing power / strategy / operator-doctrine / founder-psychology lane contains these three titles.

## 4. Classification table

| Source | Classification |
|---|---|
| The Laws of Human Nature (Greene) | **net-new** · human-behavior pattern recognition / reading people |
| Mastery (Greene) | **net-new** · the path to mastery / apprenticeship / development |
| The 50th Law (50 Cent & Greene) | **net-new** · fearlessness / self-reliance / environment-mastery |
| The 48 Laws of Power (Greene) | **already-canonical** (BATCH_002) · exclude |
| The 33 Strategies of War (Greene) | **already-canonical** (BATCH_002) · exclude |
| The Art of War (Sun Tzu) | **already-canonical** (BATCH_002) · exclude |
| The Book of Five Rings (Musashi) | **broken / needs-reacquire** (djvu) · not Greene · defer |
| The Art of Seduction (Greene) | **not present** in the universe · not a candidate |

### Adjacent Tier-2 clusters (DISTINCT registers · SEPARATE future lanes · NOT this lane)

A sweep confirms these are coherent clusters of their own, not Greene / power-strategy material, and should be planned separately:
- **leadership_mgmt (9):** Culture Code, High Output Management, Death by Meeting, Goodwin Leadership/Team of Rivals, Jocko Extreme Ownership/Dichotomy, Measure What Matters, Radical Candor, Turn the Ship Around (Marquet already in a prior lane).
- **consulting_service (7):** Alan Weiss x2, The McKinsey Way, Maister Managing the Professional Service Firm, Lencioni Getting Naked/The Advantage, Flawless Consulting.
- **systems_thinking (5):** Thinking in Systems, The Fifth Discipline, Checklist Manifesto, Understanding Media (McLuhan x2).
- **expertise_creativity (6):** Peak, Talent Is Overrated, The Creative Act (Rubin), Ways of Seeing (Berger), Dieter Rams, Creativity (Csikszentmihalyi · djvu-broken).
- **fashion_luxury (8):** The End of Fashion, The Beautiful Fall, The Chiffon Trenches, Dior by Dior, Little Dictionary of Fashion, Deluxe, The Luxury Strategy, Abloh Figures of Speech.

These are **out of scope for TIER_2_GREENE_STRATEGY** and noted as separate future lanes.

## 5. Architecture recommendation: ONE curated mini-batch (do NOT split · do NOT defer)

The three net-new Greene books form **one coherent register: Greene's applied operator-psychology under power dynamics** (read others, develop yourself, act without fear). Laws of Human Nature is about reading people; Mastery is about developing the self toward expertise; The 50th Law is about fearless self-reliance. Together they are a single "Greene operator-psychology toolkit," held strictly as **pattern recognition / defensive awareness / operator judgment**, not an endorsement of predatory tactics. At ~496K words across 3 books this is squarely in-band for the corpus's curated 3-4-book lanes (CLASSICAL_STRATEGY 18 from ~597K; HISTORICAL_BIOGRAPHY 16 from ~912K). **A split (human-nature/power vs mastery/development) would over-fragment 3 books into two thin lanes**; the unifying operator-psychology thread is stronger held together. **Whole-lane deferral is NOT warranted** (all 3 are clean and ready; the only broken neighbor, Five Rings, is not Greene and not in this lane).

**Recommendation: a single curated TIER_2_GREENE_STRATEGY mini-batch of the 3 net-new Greene books.**

## 6. Recommended first (and only) lane: TIER_2_GREENE_STRATEGY (include / defer / exclude)

- **INCLUDE (CORE · curated · the Greene operator-psychology register):**
  - The Laws of Human Nature (Robert Greene) · pdf · ~270,897 words.
  - Mastery (Robert Greene) · epub · ~153,468 words.
  - The 50th Law (50 Cent & Robert Greene) · mobi · ~71,830 words.
- **DEFER (broken · not Greene · re-acquire clean text · NO OCR):**
  - The Book of Five Rings (Musashi) · djvu · for a future classical-strategy addendum.
- **EXCLUDE (0 chunks):**
  - The 48 Laws of Power, The 33 Strategies of War, The Art of War (already BATCH_002 · cross-referenced, NOT re-chunked).
  - The adjacent Tier-2 clusters (leadership_mgmt, consulting_service, systems_thinking, expertise_creativity, fashion_luxury) · separate future lanes.
  - The KJV Bible (held SPIRITUAL_FOUNDATION anchor).
  - Every already-canonical classical/strategy/decision/biography source. CURRENT_IDENTITY sources.

## 7. Recommended chunk target / range

- **Target:** ~15-17 chunks · **Range:** 13-19 (halt-and-report if outside).
- **Synthesis:** 1 closing synthesis chunk (the Greene operator-psychology toolkit + the optionality + defensive-awareness guardrail).
- **Provisional per-source split:** The Laws of Human Nature ~7 (the longest/densest · 270K words · the 18 laws condensed to load-bearing patterns) · Mastery ~5 · The 50th Law ~3 · + 1 synthesis. Curated/representative (NOT law-by-law or chapter-by-chapter): Laws of Human Nature (irrationality and emotional self-awareness, reading people past the mask, the role of the unconscious / projection, narcissism vs empathy, the shortsighted vs the strategic, group/court dynamics and conformity, envy and grandiosity, mortality awareness as motive force); Mastery (the apprenticeship phase, finding the mentor, social intelligence, the creative-active phase, the high end / intuitive mastery, the dimensional mind); The 50th Law (intense realism / see things as they are, self-reliance and ownership, fearlessness as the master trait, opportunism and the moment, mastering one's environment, self-belief without illusion).

## 8. Recommended domains (EXISTING domains only · NO new domain)

Verified to exist (current counts): `power` (27), `strategy` (206), `operator-doctrine` (118), `founder-psychology` (37), `leadership` (55), `culture` (64), `ethics` (52), `mental-models` (8), `decision-making` (16).

| Domain | Planned use |
|---|---|
| `power` (anchor) | Greene's core subject: power dynamics, fearlessness as leverage, court/group dynamics, reading people for position · held DEFENSIVELY (recognize to navigate and protect, not to exploit). |
| `founder-psychology` | Mastery's apprenticeship/development arc and The 50th Law's self-reliance, ownership, and fearless action · the operator-development thread. |
| `decision-making` | Reading human irrationality and one's own emotional reactions to make better judgments (pairs directly with the DECISION_JUDGMENT lanes). |
| `mental-models` | The laws of human nature held as portable models for reading behavior (grows from a thin 8). |
| `strategy` | Strategic patience, opportunism, mastering the environment, the long game · used where squarely strategic. |
| `culture` | Social intelligence, role-playing, conformity, group/court dynamics · the social-reading material. |
| `operator-doctrine` | The transferable operator discipline + the closing synthesis. |
| `ethics` (if warranted) | The defensive-not-predatory framing and the moral boundary where a Greene tactic should be recognized but not used · likely 1-2. |
| `leadership` (if warranted) | Social intelligence applied to leading/mobilizing others · used sparingly. |

**Recommended anchor:** `power` (Greene's lifelong subject and the corpus's existing power domain, already home to the BATCH_002 Greene pair), with `founder-psychology` the strong co-lead and `decision-making` / `mental-models` / `culture` the secondaries. The defensive-awareness guardrail (not endorsement) is what makes the `power` register safe, applied in every chunk.

### Domain issues to flag (important)

- **`seduction`, `manipulation`, `psychology`, `human-nature`, `war`, `politics`, `strategy-book`, `self-help`, `masculinity`, `dominance` do NOT exist and will NOT be created.** Verified absent in `combined_domain_counts`. Routing: human-behavior pattern recognition -> `decision-making` / `mental-models` / `culture`; power dynamics -> `power` (held defensively); mastery/self-development -> `founder-psychology` / `operator-doctrine`; fearlessness/self-reliance -> `power` / `founder-psychology`; the moral boundary -> `ethics`.
- **`power` (27) and `mental-models` (8) are thin-ish existing domains** · this lane will reuse and grow them, NOT create anything new.
- **NO new domain will be created by default.** All planned domains pre-exist.

## 9. Connections (cross-references this lane opens)

- **BATCH_002 (The 48 Laws of Power / The 33 Strategies of War / Greene + The Art of War):** the canonical Greene/strategy pair · this lane extends Greene into human-nature, mastery, and fearlessness (the development and people-reading companions to the laws/strategies).
- **CLASSICAL_STRATEGY (The Prince / On War) + POLITICAL_THEORY_DISCOURSES (Discourses on Livy):** the classical power/strategy treatises Greene draws on and historicizes.
- **DECISION_JUDGMENT (Kahneman / Haidt / Frankl / Berne):** Laws of Human Nature's irrationality and emotional self-awareness read directly against System 1/2, intuition-first, and Berne's ego-states/games; The 50th Law's see-things-as-they-are reads against decision hygiene.
- **HISTORICAL_BIOGRAPHY (Grant / Washington) + FOUNDER_SECOND_TIER + BIOGRAPHY_FOUNDER_MEDIA:** Mastery's development arc and The 50th Law's self-reliance read against the founder/leadership arcs (the restraint counterweight to raw power).
- **CULTURE_AND_STATUS (Storr / Marx):** Greene's court/group dynamics and social intelligence read against the status-game theory.
- **CURRENT_OPERATOR_REALITY_BRIEF:** every chunk references the brief in `sniped_relevance` and holds the lane as decision-support / defensive-awareness only (the brief is the read-first anchor · NOT a chunked source).
- **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails:** the optionality discipline governs this lane; CURRENT_IDENTITY remains plan-only / NOT extracted.

## 10. Identity-optionality confirmation

This lane does NOT finalize brand direction:
- **No final SNIPED direction.** SNIPED is the live operator identity / handle / container.
- **No final SNIPED Media direction.** SNIPED Media is the current photography company.
- **No final BASEPLATE direction.** BASEPLATE is historical/optional, not current truth.
- All chunks frame the books as a **decision-support / pattern-library / defensive-awareness lens read against CURRENT_OPERATOR_REALITY_BRIEF** · the closing synthesis chunk makes the optionality discipline explicit. Photography remains one option among several. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY remains plan-only / NOT extracted.**

## 11. Greene material = pattern recognition / defensive awareness / operator judgment (NOT a directive, NOT an endorsement)

The Greene trio is held strictly as a **decision-support / pattern-library / defensive-awareness layer**: how to read human behavior and power dynamics, how to develop toward mastery, and how to act with less fear. It is **NOT a directive that BJ become a manipulator, a guru, a pickup-artist, a dark-psychology brand, a political operator, a masculine-influence account, or a power-cosplay persona**, and not a mandate to deploy predatory tactics. **Greene-style power material is read as pattern recognition and defensive awareness (recognize the move so you are not the mark) and as operator judgment (develop real skill, see reality clearly, act without paralysis), NOT as an endorsement of predatory tactics.** The methods are translated into transferable people-reading, self-development, and fearless-but-ethical operating for a solo field-engineer in build-mode, loading the backend before final brand/offer/company-architecture decisions.

## 12. Deliverables for the future ship (NOT created now)

| Deliverable | Path |
|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/TIER_2_GREENE_STRATEGY_CHUNKS.jsonl` |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/tier_2_greene_strategy_extracted/` |
| Summary | `01_KNOWLEDGE_BASE/summaries/TIER_2_GREENE_STRATEGY_SUMMARY.md` |
| Source index | `01_KNOWLEDGE_BASE/indexes/TIER_2_GREENE_STRATEGY_SOURCE_INDEX.md` |
| Extraction log | `00_COMMAND_CENTER/batch_logs/TIER_2_GREENE_STRATEGY_EXTRACTION_LOG.md` |
| Completion marker | `00_COMMAND_CENTER/batch_logs/TIER_2_GREENE_STRATEGY_COMPLETE.md` |
| Extraction script | `scripts/extract_tier_2_greene_strategy.py` |
| Chunk writer | `scripts/write_tier_2_greene_strategy_chunks.py` |

Schema: the canonical 12-field JSONL · `chunk_id` pattern `TIER_2_GREENE_STRATEGY_NNN`. Validation: 6/6 jsonl-validation checks + the lane's additional checks (net-new · 3 sources · no new domain · `power` anchor · seduction/manipulation/psychology/human-nature/war/politics/strategy-book/self-help/masculinity/dominance NOT created · 48 Laws/33 Strategies/Art of War 0 [already BATCH_002] · Five Rings 0 [broken] · Bible 0 · CURRENT_OPERATOR_REALITY_BRIEF respected · optionality + not-a-directive + defensive-awareness-not-endorsement guardrail in every chunk · quote discipline · em-dash sweep · curated-not-exhaustive).

## 13. Projected post-consolidation state (for reference · NOT applied now)

If the lane ships at the mid-target and consolidates: 1,726 + ~15-17 = **~1,741-1,743 chunks** · 10 numbered batches + **40 mini-batches** · **62 domains (NO new domain** · bumps to `power` [anchor] / `founder-psychology` / `decision-making` / `mental-models` / `strategy` / `culture` / `operator-doctrine`, plus `ethics` / `leadership` where warranted). Exact counts finalized at ship/consolidation time. Subsequent lanes: the remaining Tier-2 clusters (leadership_mgmt, consulting_service, systems_thinking, expertise_creativity, fashion_luxury), BRAND_CANON, the optional operator-docs cleanup, the fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship, the SPIRITUAL_FOUNDATION decision, and the broken-backlog re-acquisitions (Five Rings, Denial of Death, Creativity, Caples, Story/McKee).

## 14. Scope guards honored by this planning pass

- Did NOT extract, chunk, consolidate, or modify master files · total_chunks stays 1,726.
- Did NOT modify any `raw/` or source file (read-only `find` / `file` / `pdftotext`+`ebook-convert`-to-/tmp · temp deleted · all mtimes unchanged).
- Did NOT create any `*_CHUNKS.jsonl` or `*_extracted/` dir.
- Did NOT OCR and did NOT install anything.
- Did NOT touch the Bible.
- NO new domain created.
- No lane started beyond writing this plan.
- Wrote only this plan file. Em-dash clean. Not committed (operator will review first).

## 15. Next step (operator decision · do not start without authorization)

Authorize the **TIER_2_GREENE_STRATEGY** lane (3 net-new Greene sources · The Laws of Human Nature + Mastery + The 50th Law · target ~15-17 · existing domains only · `power` anchor · no new domain · seduction/manipulation/psychology/human-nature/war/politics/strategy-book/self-help/masculinity/dominance NOT created · 48 Laws/33 Strategies/Art of War excluded as already BATCH_002 · Five Rings deferred broken · the adjacent Tier-2 clusters are separate future lanes · Bible excluded · curated, not exhaustive · pattern recognition / defensive awareness / operator judgment, NOT a directive and NOT an endorsement of predatory tactics). Then commit the ship outputs, then consolidate, then session-save.
