# EDGE_AND_OPERATING_DISCIPLINE source index · 2026-05-23

3 source files · 11 chunks · batch_id `EDGE_AND_OPERATING_DISCIPLINE`. NO NEW domain. The 2 synthesis chunks (010-011) cite a representative worksheet file. All sources from `raw/13_OPERATING_DISCIPLINE/`.

## Sources

| # | Extracted file | Title · Author | Source-content chunks | Original source |
|--:|---|---|---|---|
| 1 | `icp_definition_worksheet.txt` | ICP Definition Worksheet · The AI Edge | 001-003 (3) + 011 synthesis | `raw/13_OPERATING_DISCIPLINE/ICP Definition Worksheet.pdf` |
| 2 | `setting_goals.txt` | Setting Goals · The AI Edge | 004-006 (3) | `raw/13_OPERATING_DISCIPLINE/Setting Goals.pdf` |
| 3 | `weekly_reflections.txt` | Weekly Reflections · The AI Edge | 007-009 (3) + 010 synthesis | `raw/13_OPERATING_DISCIPLINE/Weekly Reflections.pdf` |

Extracted via pdftotext -layout · no OCR · no new dependencies · 5,277 words total (INTERNAL chunk-authoring reference only).

## Net-new confirmation

The 3 worksheets verified net-new: 0 source_file/source_title hits across all `*_CHUNKS.jsonl`. (Finding Your Edge.pdf and COURSE WORK 1 thru 2.docx, from the sibling `05_AI_EDGE_COURSE/` folder, ARE already chunked in BATCH_008 as `finding_your_edge.txt` / `course_work_1_thru_2.txt` and were excluded.)

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source |
|---|---|---|---|
| 001 | The four-component ICP framework: define exactly who and why | strategy | icp |
| 002 | Validate the expensive problem before committing | operator-process | icp |
| 003 | Reachability and the edge: only pursue what you can reach and want | operator-doctrine | icp |
| 004 | SMART goals, capped at three per quarter | operator-process | goals |
| 005 | Goal hierarchy: cascade vision down to this week's actions | strategy | goals |
| 006 | Reality-test goals and build the weekly reflection habit | operator-doctrine | goals |
| 007 | The weekly review: score, wins, honest reality check, patterns | operator-process | weekly |
| 008 | Energy and time audit: where the 168 hours actually went | operator-doctrine | weekly |
| 009 | The reflection-to-adjustment loop: insights become next week's focus | systems-thinking | weekly |
| 010 | SYNTHESIS: the operating-discipline loop (focus to goals to reflection to adjust) | meta-doctrine | weekly (synthesis) |
| 011 | SYNTHESIS: load the backend and stay revisable before committing to identity | meta-doctrine | icp (synthesis) |

## Domain distribution (NO NEW domain · 5 approved domains only)

operator-process 3 · operator-doctrine 3 · strategy 2 · meta-doctrine 2 · systems-thinking 1 = 11.

`personal-operating-code` is a mini-batch slug, NOT a domain, and was NOT used (using it would have introduced a new domain). `ethics` and `ai-tooling` were not warranted.

## Identity optionality guardrail

All 11 chunks carry the guardrail in `sniped_relevance`: this lane does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction. The ICP Definition Worksheet is chunked as the ICP-definition METHOD, never as a finalized SNIPED ICP (chunks 001 and 011 state this explicitly). The lane actively reinforces optionality: chunk 011 ties the worksheets' "your ICP will evolve / be specific enough to test and learn" to the corpus's load-the-backend-before-committing discipline.

## Cross-batch reinforcement summary

| Chunk(s) | Link |
|---|---|
| 001-003 ICP method | BATCH_009_EXPANSION (Christensen JTBD · the demand counterpart) + B2B_POSITIONING (discovery) + Finding Your Edge (BATCH_008, the prerequisite assessment) |
| 004-006 goals | INTELLECTUAL_ARTIST_FRAME (disciplined time) + PERSONAL_OPERATING_CODE (values into practice) |
| 007-009 weekly review | operator-doctrine / operator-process (BATCH_007) + the reflection cadence |
| 010 discipline loop | the executional engine beneath any strategy in the corpus |
| 011 optionality | CURRENT_IDENTITY_AND_BRAND_OPTIONALITY guardrails (load the backend, stay revisable) |

## Copyright-safe quote discipline

All three are © The AI Edge / Agera Management LTD course worksheets. `direct_quotes` are SHORT illustrative lines only (longest 13 words). 6 of 11 chunks carry a quote; 5 paraphrase. Extracted full text is internal reference.

## Excluded / deferred material (NOT chunked)

| Material | Reason |
|---|---|
| The_Operator_Playbook.docx · GaryVee_Attention_Operating_System.docx | DEFERRED · content/distribution lane (social-media + content systems) |
| Business_Operations_Playbook.docx | DEFERRED · business-ops/legal/finance lane |
| Money_Wealth_Getting_Ahead.docx | DEFERRED · money/ownership lane |
| sniped_context_tools_only.docx | DEFERRED · SNIPED-specific current-state context · likely overlaps SNIPED OS Knowledge Dump |
| Finding Your Edge.pdf · COURSE WORK 1 thru 2.docx | EXCLUDED · already chunked in BATCH_008 |
| recovery/acquisition items · CURRENT_IDENTITY_AND_BRAND_OPTIONALITY sources | Out of scope · 0 chunks |
