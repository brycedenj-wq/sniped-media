# DECISION_JUDGMENT_CROWDS complete · the curated crowds / social-belief toolkit · 2026-05-25

## Status

**Extraction:** complete (4 of 4 sources · 0 failures · ~362,658 words · ebook-convert + pdftotext · no OCR · no new dependencies).
**Chunking:** complete (14 chunks · mid of the ~13-15 target · within the 11-17 range · 1 synthesis chunk · CURATED, not exhaustive).
**Validation:** 6/6 PASS per `.claude/skills/jsonl-validation/SKILL.md` + the additional checks PASS.
**Master files:** NOT updated (per operator instruction · awaits `master-consolidation`). NO new domain to register.
**Identity optionality:** preserved · crowds/social-belief material is a pattern-library / decision-support layer only · NOT a directive that BJ become a political commentator, culture-war operator, manipulator, propagandist, activist, social theorist, academic, or ideology brand · held descriptively, NOT a manipulation playbook or a culture-war stance · no final SNIPED / SNIPED Media / BASEPLATE direction.
**Bible:** NOT touched, staged, chunked, or included.

## Artifacts produced

| File | Path | Status |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/DECISION_JUDGMENT_CROWDS_CHUNKS.jsonl` | written · 14 chunks · validated |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/decision_judgment_crowds_extracted/` | 4 normalized .txt |
| Extraction script | `scripts/extract_decision_judgment_crowds.py` | written |
| Chunk writer | `scripts/write_decision_judgment_crowds_chunks.py` | written |
| Extraction log | `00_COMMAND_CENTER/batch_logs/DECISION_JUDGMENT_CROWDS_EXTRACTION_LOG.md` | written |
| Summary | `01_KNOWLEDGE_BASE/summaries/DECISION_JUDGMENT_CROWDS_SUMMARY.md` | written |
| Source index | `01_KNOWLEDGE_BASE/indexes/DECISION_JUDGMENT_CROWDS_SOURCE_INDEX.md` | written |
| Completion marker | `00_COMMAND_CENTER/batch_logs/DECISION_JUDGMENT_CROWDS_COMPLETE.md` | this file |

## Headline numbers

- CORE sources extracted: 4 of 4 (The Righteous Mind / Haidt · The Coddling of the American Mind / Lukianoff+Haidt · The True Believer / Hoffer · The Crowd / Le Bon)
- Chunks: 14 (target ~13-15 · range 11-17 · landed 14 · CURATED from ~362,658 words)
- Distinct source_file references: 4
- Domains touched: 6 · NO new domain (`decision-making` anchor)
- Synthesis chunks: 1 (014)
- Unique batch_id: `DECISION_JUDGMENT_CROWDS`
- Extraction: ebook-convert + pdftotext · 0 new dependencies · no OCR

## Validation summary

| Check | Result |
|---|---|
| JSONL parse | PASS |
| Required fields present per line | PASS · 0 missing (all 12 fields) |
| chunk_id uniqueness | PASS · 0 duplicates across 14 chunks |
| batch_id consistency | PASS · single value `DECISION_JUDGMENT_CROWDS` |
| source_file resolution | PASS · 4 files resolve under `decision_judgment_crowds_extracted/` |
| Counts | 14 chunks · 4 unique sources |

Em-dash sweep: PASS · 0 em-dashes in SNIPED-authored output.

## Additional checks (per operator requirement)

1. **Exactly the 4 DECISION_JUDGMENT_CROWDS sources chunked.** CONFIRMED (Righteous Mind / Coddling / True Believer / The Crowd · 4 source_files · per-source 5/4/3/2).
2. **Thinking, Fast and Slow contributed 0 chunks.** CONFIRMED (already DECISION_JUDGMENT_COGNITION).
3. **Noise contributed 0 chunks.** CONFIRMED (already DECISION_JUDGMENT_COGNITION).
4. **Man's Search for Meaning contributed 0 chunks.** CONFIRMED (deferred · MEANING).
5. **Games People Play contributed 0 chunks.** CONFIRMED (deferred · MEANING).
6. **The Denial of Death contributed 0 chunks.** CONFIRMED (broken djvu).
7. **Anatomy of Story contributed 0 chunks.** CONFIRMED (storytelling lane).
8. **Hero with a Thousand Faces contributed 0 chunks.** CONFIRMED (storytelling lane).
9. **Save the Cat! contributed 0 chunks.** CONFIRMED (storytelling lane).
10. **Story / McKee contributed 0 chunks.** CONFIRMED (broken scanned · storytelling lane).
11. **Predictably Irrational / PERSUASION_RECOVERY source contributed 0 chunks.** CONFIRMED (already canonical).
12. **Bible contributed 0 chunks and was untouched.** CONFIRMED.
13. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources contributed 0 chunks.** CONFIRMED.
14. **No already-canonical persuasion/positioning/operator/classical source contributed chunks.** CONFIRMED.
15. **No storytelling/narrative source contributed chunks.** CONFIRMED.
16. **No NEW domains.** CONFIRMED · all 6 domains pre-exist (cross-checked against MASTER_CHUNK_MAP.json).
17. **psychology / behavioral-psychology / behavioral-economics / cognition / bias / risk / uncertainty / decision-science / politics / ideology / culture-war / social-psychology / crowd-psychology / mass-movements / storytelling / narrative NOT used as domains.** CONFIRMED · all 6 used domains within the approved set (decision-making, culture, ethics, systems-thinking, operator-doctrine, power).
18. **CURRENT_OPERATOR_REALITY_BRIEF respected.** CONFIRMED · referenced in all 14 chunks · brief NOT chunked (not a source_file).
19. **Identity optionality guardrail preserved.** CONFIRMED · all 14 chunks · pattern-library / decision-support only · NOT a directive that BJ become a political commentator / culture-war operator / manipulator / propagandist / activist / social theorist / academic / ideology brand · no final SNIPED / SNIPED Media / BASEPLATE direction.
20. **Scope guard (curated, not exhaustive; descriptive, not posture/manipulation).** CONFIRMED · 14 chunks from ~362,658 words · representative crowds/social-belief patterns · held descriptively · the not-a-manipulation-playbook clause is present in all 14 chunks · Le Bon's prestige/contagion framed as defensive awareness.
21. **Master files unchanged at 1,688.** CONFIRMED · no DECISION_JUDGMENT_CROWDS entry · domain keys still 75 · official 62.
22. **raw/ source files not modified.** CONFIRMED · the 4 sources retain their mtimes.
23. **No OCR / no new dependencies.** CONFIRMED · ebook-convert + pdftotext (both on PATH).
24. **SNIPED-authored outputs em-dash clean.** CONFIRMED · 0 em-dashes.
25. **Quote discipline.** CONFIRMED · longest direct_quote = 4 words.

## Per-source chunk distribution

| Source | Source-content chunks | + synthesis | source_file total |
|---|---:|---:|---:|
| The Righteous Mind (Haidt) | 4 | 1 (014) | 5 |
| The Coddling of the American Mind (Lukianoff/Haidt) | 4 | 0 | 4 |
| The True Believer (Hoffer) | 3 | 0 | 3 |
| The Crowd (Le Bon) | 2 | 0 | 2 |

## Domain distribution (NO new domain · `decision-making` anchor)

| Domain | Chunks |
|---|---:|
| decision-making | 4 |
| culture | 3 |
| operator-doctrine | 3 |
| power | 2 |
| ethics | 1 |
| systems-thinking | 1 |

## Deviations from DECISION_JUDGMENT_PLAN.md

1. **Batch_id `DECISION_JUDGMENT_CROWDS`** (the plan's named deferred sub-lane).
2. **Final count 14** (target ~13-15). On target (mid).
3. **1 synthesis chunk** (014 operator-doctrine).
4. **Per-source Righteous Mind 5 / Coddling 4 / True Believer 3 / The Crowd 2** · within the rough targets.
5. **`decision-making` anchor (4)**, culture (3) + operator-doctrine (3) secondaries; power (2) for unification/prestige (descriptive); ethics (1); systems-thinking (1). `strategy`/`status`/`mental-models`/`operator-process` available but not used.
6. **No structural deviations.** No master files updated. No new dependencies. No OCR. The COGNITION/MEANING/storytelling sources, broken sources, Predictably Irrational, and the Bible excluded. Curated (not exhaustive); sensitive material held descriptively, not as posture or manipulation doctrine.

## What is canonical now (post-validation)

The 14 chunks are validated and ready for master-consolidation. Until `master-consolidation` runs:
- `MASTER_INDEX.md` still shows 10 batches + 36 mini-batches (1,688 chunks · 62 domains).
- `MASTER_CHUNK_MAP.json` still shows 1,688 total · no DECISION_JUDGMENT_CROWDS entry.

After authorized master-consolidation, the corpus will reflect 10 numbered batches + 37 mini-batches (1,702 chunks · 62 unique domains · NO new domain · bumps: decision-making +4 to 13, culture +3 to 61, operator-doctrine +3 to 113, power +2 to 27, ethics +1 to 50, systems-thinking +1 to 54).

## Next recommended action

**Option A · commit DECISION_JUDGMENT_CROWDS artifacts, then authorize `master-consolidation DECISION_JUDGMENT_CROWDS`** (no new domain · new total 1,702).
**Option B · pause for review** of the 14 chunks (especially the moral-foundations chunk 002, the Hoffer unification chunk 010, and the Le Bon prestige chunk 013 given the sensitivity), then authorize commit + consolidation.

After this lane: the DECISION_JUDGMENT sequence continues with MEANING (Frankl + Berne); then the separate STORYTELLING_NARRATIVE lane (Truby + Campbell + Snyder; McKee broken), Tier-2 (incl the Greene trio), and BRAND_CANON.

Stopping here per the operator's execution spec: "Stop after validation and reporting."
