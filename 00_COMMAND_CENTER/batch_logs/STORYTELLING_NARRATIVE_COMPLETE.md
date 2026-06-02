# STORYTELLING_NARRATIVE complete · the curated story-craft / visual-narrative toolkit · 2026-05-25

## Status

**Extraction:** complete (4 of 4 sources · 0 failures · ~389,227 words · pdftotext + ebook-convert · no OCR · no new dependencies).
**Chunking:** complete (15 chunks · low end of the ~15-17 target · within the 13-19 range · 1 synthesis chunk · CURATED, not exhaustive).
**Validation:** 6/6 PASS per `.claude/skills/jsonl-validation/SKILL.md` + the additional checks PASS.
**Master files:** NOT updated (per operator instruction · awaits `master-consolidation`). NO new domain to register.
**Identity optionality:** preserved · story-craft / visual-narrative material is a pattern-library / decision-support layer only · NOT a directive that BJ become a screenwriter, myth-brand guru, novelist, film critic, narrative consultant, or self-help storyteller · Campbell held as cultural/narrative pattern (not faith), Block translated for the visual operator · no final SNIPED / SNIPED Media / BASEPLATE direction.
**Bible:** NOT touched, staged, chunked, or included.

## Artifacts produced

| File | Path | Status |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/STORYTELLING_NARRATIVE_CHUNKS.jsonl` | written · 15 chunks · validated |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/storytelling_narrative_extracted/` | 4 normalized .txt |
| Extraction script | `scripts/extract_storytelling_narrative.py` | written |
| Chunk writer | `scripts/write_storytelling_narrative_chunks.py` | written |
| Extraction log | `00_COMMAND_CENTER/batch_logs/STORYTELLING_NARRATIVE_EXTRACTION_LOG.md` | written |
| Summary | `01_KNOWLEDGE_BASE/summaries/STORYTELLING_NARRATIVE_SUMMARY.md` | written |
| Source index | `01_KNOWLEDGE_BASE/indexes/STORYTELLING_NARRATIVE_SOURCE_INDEX.md` | written |
| Completion marker | `00_COMMAND_CENTER/batch_logs/STORYTELLING_NARRATIVE_COMPLETE.md` | this file |

## Headline numbers

- CORE sources extracted: 4 of 4 (Anatomy of Story / Truby · Hero with a Thousand Faces / Campbell · Save the Cat! / Snyder · The Visual Story / Block)
- Chunks: 15 (target ~15-17 · range 13-19 · landed 15 · CURATED from ~389,227 words)
- Distinct source_file references: 4
- Domains touched: 8 · NO new domain (`aesthetics` anchor)
- Synthesis chunks: 1 (015)
- Unique batch_id: `STORYTELLING_NARRATIVE`
- Extraction: pdftotext + ebook-convert · 0 new dependencies · no OCR

## Validation summary

| Check | Result |
|---|---|
| JSONL parse | PASS |
| Required fields present per line | PASS · 0 missing (all 12 fields) |
| chunk_id uniqueness | PASS · 0 duplicates across 15 chunks |
| batch_id consistency | PASS · single value `STORYTELLING_NARRATIVE` |
| source_file resolution | PASS · 4 files resolve under `storytelling_narrative_extracted/` |
| Counts | 15 chunks · 4 unique sources |

Em-dash sweep: PASS · 0 em-dashes in SNIPED-authored output.

## Additional checks (per operator requirement)

1. **Exactly the 4 STORYTELLING_NARRATIVE sources chunked.** CONFIRMED (Truby / Campbell / Snyder / Block · 4 source_files · per-source 5/4/3/3).
2. **Story / McKee contributed 0 chunks.** CONFIRMED (broken scanned · 0 words · deferred).
3. **Building a StoryBrand contributed 0 chunks.** CONFIRMED (already BATCH_009 · cross-reference only).
4. **life story.docx contributed 0 chunks.** CONFIRMED (personal note · out-of-scope).
5. **Bible contributed 0 chunks and was untouched.** CONFIRMED.
6. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources contributed 0 chunks.** CONFIRMED.
7. **No already-canonical literary / brand / media-business / positioning / decision-judgment source contributed chunks.** CONFIRMED (sources == the 4).
8. **No other raw top-level story/personal note contributed chunks.** CONFIRMED.
9. **No NEW domains.** CONFIRMED · all 8 domains pre-exist (cross-checked against MASTER_CHUNK_MAP.json).
10. **storytelling / narrative / screenwriting / mythology / myth / archetype / hero / religion / spirituality / self-help NOT used as domains.** CONFIRMED · all 8 used domains within the approved set (aesthetics, culture, media-business, brand, operator-doctrine, strategy, ethics, operator-process).
11. **Campbell material cultural/narrative pattern only, not faith/spirituality.** CONFIRMED · the cultural-not-faith clause is present in all 4 Campbell chunks.
12. **The Visual Story included and translated into visual-operator structure patterns.** CONFIRMED · 3 Block chunks · the visual-operator translation clause present in all 3.
13. **CURRENT_OPERATOR_REALITY_BRIEF respected.** CONFIRMED · referenced in all 15 chunks · brief NOT chunked (not a source_file).
14. **Identity optionality guardrail preserved.** CONFIRMED · all 15 chunks · pattern-library / decision-support only · NOT a directive that BJ become a screenwriter / myth-brand guru / novelist / film critic / narrative consultant / self-help storyteller · no final SNIPED / SNIPED Media / BASEPLATE direction.
15. **Scope guard (curated, not screenwriting/mythology chapter summary).** CONFIRMED · 15 chunks from ~389,227 words · representative story-craft / visual-narrative extraction.
16. **Master files unchanged at 1,711.** CONFIRMED · no STORYTELLING_NARRATIVE entry · domain keys still 75 · official 62.
17. **raw/ source files not modified.** CONFIRMED · all sources retain their mtimes (2026-05-16 / 2026-04-26).
18. **No OCR / no new dependencies.** CONFIRMED · pdftotext + ebook-convert (both on PATH).
19. **SNIPED-authored outputs em-dash clean.** CONFIRMED · 0 em-dashes.
20. **Quote discipline.** CONFIRMED · longest direct_quote = 5 words.

## Per-source chunk distribution

| Source | Source-content chunks | + synthesis | source_file total |
|---|---:|---:|---:|
| The Anatomy of Story (Truby) | 4 | 1 (015) | 5 |
| The Hero with a Thousand Faces (Campbell) | 4 | 0 | 4 |
| Save the Cat! (Snyder) | 3 | 0 | 3 |
| The Visual Story (Block) | 3 | 0 | 3 |

## Domain distribution (NO new domain · `aesthetics` anchor)

| Domain | Chunks |
|---|---:|
| aesthetics | 5 |
| operator-doctrine | 3 |
| culture | 2 |
| strategy | 1 |
| ethics | 1 |
| brand | 1 |
| media-business | 1 |
| operator-process | 1 |

## What is canonical now (post-validation)

The 15 chunks are validated and ready for master-consolidation. Until `master-consolidation` runs:
- `MASTER_INDEX.md` still shows 10 batches + 38 mini-batches (1,711 chunks · 62 domains).
- `MASTER_CHUNK_MAP.json` still shows 1,711 total · no STORYTELLING_NARRATIVE entry.

After authorized master-consolidation, the corpus will reflect 10 numbered batches + 39 mini-batches (1,726 chunks · 62 unique domains · NO new domain · bumps: aesthetics +5 to 78, operator-doctrine +3 to 118, culture +2 to 64, strategy +1 to 206, ethics +1 to 52, brand +1 to 39, media-business +1 to 12, operator-process +1 to 101).

## Next recommended action

**Option A · commit STORYTELLING_NARRATIVE artifacts, then authorize `master-consolidation STORYTELLING_NARRATIVE`** (no new domain · new total 1,726).
**Option B · pause for review** of the 15 chunks (especially the Campbell cultural-not-faith framing and the Block visual-operator translation), then authorize commit + consolidation.

After this lane: the next lanes are the remaining Tier-2 clusters (incl the Greene trio: Laws of Human Nature / Mastery / 50th Law), BRAND_CANON, the optional operator-docs cleanup, the fresh current SNIPED brief / CURRENT_IDENTITY principle-only ship, the SPIRITUAL_FOUNDATION decision, and the broken-backlog re-acquisitions.

Stopping here per the operator's execution spec: "Stop after validation and reporting."
