# OPPORTUNITY_MANAGEMENT_TEMPLATES complete · AI Edge templates · 2026-05-19

## Status

**Extraction:** complete (2 of 2 sources · 0 failures · xlsx 1,936 words + pptx 416 words · stdlib zipfile + xml.etree · no new dependencies · no OCR).
**Chunking:** complete (4 chunks · exactly on the target 4 · inside the 2-5 planned range).
**Validation:** 6/6 PASS per `.claude/skills/jsonl-validation/SKILL.md`.
**Master files:** NOT updated (per operator instruction · awaits `master-consolidation`).

## Artifacts produced

| File | Path | Status |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/OPPORTUNITY_MANAGEMENT_TEMPLATES_CHUNKS.jsonl` | written · 4 chunks · validated |
| Extracted xlsx | `01_KNOWLEDGE_BASE/batches/opportunity_management_templates_extracted/opp_hopper_biz_case.txt` | written · 1,936 words |
| Extracted pptx | `01_KNOWLEDGE_BASE/batches/opportunity_management_templates_extracted/opportunity_card_example.txt` | written · 416 words |
| Extraction script | `scripts/extract_opportunity_management_templates.py` | written · stdlib zipfile + xml.etree |
| Chunk writer | `scripts/write_opportunity_management_templates_chunks.py` | written |
| Extraction log | `00_COMMAND_CENTER/batch_logs/OPPORTUNITY_MANAGEMENT_TEMPLATES_EXTRACTION_LOG.md` | written |
| Summary | `01_KNOWLEDGE_BASE/summaries/OPPORTUNITY_MANAGEMENT_TEMPLATES_SUMMARY.md` | written |
| Source index | `01_KNOWLEDGE_BASE/indexes/OPPORTUNITY_MANAGEMENT_TEMPLATES_SOURCE_INDEX.md` | written |
| Completion marker | `00_COMMAND_CENTER/batch_logs/OPPORTUNITY_MANAGEMENT_TEMPLATES_COMPLETE.md` | this file |

## Headline numbers

- Sources extracted: 2 (1 xlsx · 4 sheets · + 1 pptx · 2 slides)
- Chunks: 4 (planned range 2-5 · target 4 · landed 4)
- Domains touched: 3 (operator-process 2 + commercial-architecture 1 + client-application 1 · no NEW domains)
- Unique batch_id: `OPPORTUNITY_MANAGEMENT_TEMPLATES`
- Extraction: stdlib zipfile + xml.etree · 0 new dependencies

## Validation summary

| Check | Result |
|---|---|
| JSONL parse | PASS |
| Required fields present per line | PASS · 0 missing (all 12 fields) |
| chunk_id uniqueness | PASS · 0 duplicates across 4 chunks |
| batch_id consistency | PASS · single value `OPPORTUNITY_MANAGEMENT_TEMPLATES` |
| source_file resolution | PASS · both txt resolve under `opportunity_management_templates_extracted/` |
| Counts | 4 chunks · 2 unique sources |

Em-dash sweep: PASS · 0 em-dashes in output.

## Extraction-method results

| Source | Method | Result |
|---|---|---|
| `Opp hopper + Biz Case.xlsx` | stdlib zipfile + xml.etree (workbook sheet order via rId, sharedStrings, per-sheet cell grid with shared-string + numeric resolution) | 4 sheets · 136 shared strings · 1,936 words |
| `Opportunity Card [Example].pptx` | stdlib zipfile + xml.etree (slides in numeric order, `<a:t>` runs per slide, media ignored) | 2 slides · 2 media files ignored · 416 words |

No new dependencies installed (`openpyxl` / `python-pptx` not required · `pandoc` cannot read xlsx/pptx as input).

## Domain distribution

| Domain | Chunks |
|---|---:|
| operator-process | 2 |
| commercial-architecture | 1 |
| client-application | 1 |

## Chunk-by-chunk map

| chunk_id | Concept | Domain | Source |
|---|---|---|---|
| 001 | The opportunity hopper · goal-aligned intake + auto-complexity scoring | operator-process | xlsx sheet 1 |
| 002 | The business-case ROI model · FTE baseline to cost saved to dashboard | commercial-architecture | xlsx sheets 2-4 |
| 003 | The opportunity card · one-page solution brief format | operator-process | pptx slide 1 |
| 004 | Opportunity-to-business-case translation + implementation-readiness sign-off gate | client-application | pptx slide 2 + xlsx examples |

## Excluded material categories

| Category | Disposition |
|---|---|
| Embedded slide images (`ppt/media/` · 6.27 MB bulk) | EXCLUDED · not text · ignored by extractor |
| Spreadsheet formula machinery / number formats | EXCLUDED · values + headers only |
| Specific vendor names + invoice $-figures | Kept only as dated illustration · structure is the durable signal |
| N8N / prompt-template / literary intake | OUT OF SCOPE · not touched |

## Deviations from OPPORTUNITY_MANAGEMENT_TEMPLATES_PLAN.md

1. **Final count 4** (target 4 · range 2-5). Exactly on target. The merge option (003+004) and expand option (split scoring) were both declined · the four-chunk cut (hopper / ROI model / card / translation-readiness) was cleanest.
2. **Domain split operator-process 2 + commercial-architecture 1 + client-application 1.** No NEW domains. `strategy` available as a secondary tag but not used as a primary (matches plan section 4).
3. **No structural deviations.** No source files moved/renamed/deleted. No master files updated. No new dependencies installed. BATCH_008 not started. No N8N / prompt-template / literary intake touched.

## What is canonical now (post-validation)

The 4 chunks in `OPPORTUNITY_MANAGEMENT_TEMPLATES_CHUNKS.jsonl` are validated and ready for master-consolidation. Until `master-consolidation` runs:
- `MASTER_INDEX.md` still shows 7 batches + 3 mini-batches (884 chunks).
- `MASTER_CHUNK_MAP.json` still shows 884 total chunks.
- `ACTIVE_KNOWLEDGE_STATE.md` next-action recommendation still names OPPORTUNITY_MANAGEMENT_TEMPLATES (now executed, pending consolidation).

After authorized master-consolidation, the corpus will reflect 7 numbered batches + 4 mini-batches (888 chunks).

## Next recommended action

**Option A · commit OPPORTUNITY_MANAGEMENT_TEMPLATES artifacts, then authorize `master-consolidation OPPORTUNITY_MANAGEMENT_TEMPLATES`.** New corpus total: 888 chunks.

**Option B · pause for review.** Hold the commit, review the 4 chunks (especially the xlsx/pptx extraction fidelity), then authorize commit + consolidation.

After OPPORTUNITY_MANAGEMENT_TEMPLATES consolidates, the next mini-batch (per `STAGING_PLAN_2026-05-19_INTAKE.md` section 5) is **N8N_AUTOMATION_SYSTEMS** (6 n8n JSON workflows · 15-25 chunks), then `PROMPT_TEMPLATES_DEEP`, before the literary-canon passes and BATCH_008.

Stopping here per the operator's execution spec: "Stop after validation and reporting."
