# ADVERTISING_RECOVERY complete · recovered advertising/copywriting canon · 2026-05-24

## Status

**Extraction:** complete (3 of 3 recovered sources · 0 failures · ~193,712 words · pdftotext + ebook-convert · no OCR · no new dependencies).
**Chunking:** complete (16 chunks · inside the ~14-18 target · within the 10-22 range · 1 synthesis chunk).
**Validation:** 6/6 PASS per `.claude/skills/jsonl-validation/SKILL.md` + 18 additional checks PASS.
**Master files:** NOT updated (per operator instruction · awaits `master-consolidation`). NO new domain to register.
**Identity optionality:** preserved · advertising/copywriting is a decision-support + execution layer only · NOT a directive that BJ become a copywriter or run an agency · no final SNIPED / SNIPED Media / BASEPLATE direction.
**Bible:** NOT touched, staged, chunked, or included.

## Artifacts produced

| File | Path | Status |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/ADVERTISING_RECOVERY_CHUNKS.jsonl` | written · 16 chunks · validated |
| Extracted dir | `01_KNOWLEDGE_BASE/batches/advertising_recovery_extracted/` | 3 normalized .txt |
| Extraction script | `scripts/extract_advertising_recovery.py` | written |
| Chunk writer | `scripts/write_advertising_recovery_chunks.py` | written |
| Extraction log | `00_COMMAND_CENTER/batch_logs/ADVERTISING_RECOVERY_EXTRACTION_LOG.md` | written |
| Summary | `01_KNOWLEDGE_BASE/summaries/ADVERTISING_RECOVERY_SUMMARY.md` | written |
| Source index | `01_KNOWLEDGE_BASE/indexes/ADVERTISING_RECOVERY_SOURCE_INDEX.md` | written |
| Completion marker | `00_COMMAND_CENTER/batch_logs/ADVERTISING_RECOVERY_COMPLETE.md` | this file |

## Headline numbers

- CORE sources extracted: 3 of 3 (Ogilvy / Sugarman / Halbert · recovered files only)
- Chunks: 16 (target ~14-18 · range 10-22 · landed 16)
- Distinct source_file references: 3
- Domains touched: 12 · NO new domain (`copywriting` anchors)
- Synthesis chunks: 1 (016)
- Unique batch_id: `ADVERTISING_RECOVERY`
- Extraction: pdftotext + ebook-convert · 0 new dependencies · no OCR

## Validation summary

| Check | Result |
|---|---|
| JSONL parse | PASS |
| Required fields present per line | PASS · 0 missing (all 12 fields) |
| chunk_id uniqueness | PASS · 0 duplicates across 16 chunks |
| batch_id consistency | PASS · single value `ADVERTISING_RECOVERY` |
| source_file resolution | PASS · 3 files resolve under `advertising_recovery_extracted/` |
| Counts | 16 chunks · 3 unique sources |

Em-dash sweep: PASS · 0 em-dashes in SNIPED-authored output.

## Additional checks (per operator requirement)

1. **Exactly the 3 recovered sources chunked.** CONFIRMED (Ogilvy / Sugarman / Halbert).
2. **Caples contributed 0 chunks.** CONFIRMED (still scanned · excluded).
3. **Old scanned Confessions PDF contributed 0 chunks.** CONFIRMED (used the `_RECOVERED` pdf only).
4. **Hey, Whipple, Squeeze This contributed 0 chunks.** CONFIRMED (different book · out of scope).
5. **Bible contributed 0 chunks and was untouched.** CONFIRMED.
6. **No other advertising-folder file contributed chunks.** CONFIRMED.
7. **No recovery item outside these 3 contributed chunks.** CONFIRMED.
8. **CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources contributed 0 chunks.** CONFIRMED.
9. **No already-canonical batch source contributed chunks.** CONFIRMED (net-new vs BATCH_009).
10. **No NEW domains.** CONFIRMED · all 12 domains pre-exist.
11. **marketing / persuasion NOT used as domains.** CONFIRMED.
12. **Master files unchanged at 1,455.** CONFIRMED · no ADVERTISING_RECOVERY entry · domain keys still 75.
13. **raw/ source files not modified.** CONFIRMED.
14. **No OCR / no new dependencies.** CONFIRMED · pdftotext + ebook-convert (already on PATH).
15. **SNIPED-authored outputs em-dash clean.** CONFIRMED · 0 em-dashes.
16. **Quote discipline.** CONFIRMED · longest direct_quote = 5 words.
17. **CURRENT_OPERATOR_REALITY_BRIEF respected.** CONFIRMED · referenced in all 16 chunks · brief NOT chunked.
18. **Identity optionality guardrail preserved.** CONFIRMED · all 16 chunks · decision-support + execution layer only · not a directive that BJ become a copywriter or run an agency · no final SNIPED / SNIPED Media / BASEPLATE direction.

## Per-source chunk distribution

| Source | Source-content chunks | + synthesis | source_file total |
|---|---:|---:|---:|
| Confessions of an Advertising Man (Ogilvy) | 6 | 1 (016) | 7 |
| The Adweek Copywriting Handbook (Sugarman) | 5 | 0 | 5 |
| The Boron Letters (Halbert) | 4 | 0 | 4 |

## Domain distribution (NO new domain · `copywriting` anchors)

| Domain | Chunks |
|---|---:|
| copywriting | 4 |
| brand-psychology | 2 |
| brand | 1 |
| positioning | 1 |
| offer-design | 1 |
| sales-flow | 1 |
| meta-advertising | 1 |
| commercial-architecture | 1 |
| content-strategy | 1 |
| strategy | 1 |
| operator-process | 1 |
| ethics | 1 |

## Deviations from ADVERTISING_RECOVERY_PLAN.md

1. **Final count 16** (target ~14-18). On target.
2. **1 synthesis chunk** (016) per the allowance.
3. **Agency-running (Ogilvy) + honesty threads included** as operator-process (005) + ethics (006) per the "where warranted" allowance.
4. **Domain distribution** content-faithful · `copywriting` heaviest (4); all existing domains; marketing/persuasion not used.
5. **No structural deviations.** No master files updated. No new dependencies. No OCR. Caples / old scan / Hey Whipple / Bible excluded.

## What is canonical now (post-validation)

The 16 chunks are validated and ready for master-consolidation. Until `master-consolidation` runs:
- `MASTER_INDEX.md` still shows 10 batches + 20 mini-batches (1,455 chunks · 62 domains).
- `MASTER_CHUNK_MAP.json` still shows 1,455 total · no ADVERTISING_RECOVERY entry.

After authorized master-consolidation, the corpus will reflect 10 numbered batches + 21 mini-batches (1,471 chunks · 62 unique domains · NO new domain).

## Next recommended action

**Option A · commit ADVERTISING_RECOVERY artifacts, then authorize `master-consolidation ADVERTISING_RECOVERY`** (no new domain · new total 1,471).
**Option B · pause for review** of the 16 chunks (especially the operator-process/ethics inclusions and the synthesis chunk), then authorize commit + consolidation.

Stopping here per the operator's execution spec: "Stop after validation and reporting."
