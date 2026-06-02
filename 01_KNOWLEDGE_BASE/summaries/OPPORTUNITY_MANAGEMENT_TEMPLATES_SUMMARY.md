# OPPORTUNITY_MANAGEMENT_TEMPLATES summary · AI Edge templates · 2026-05-19

4 chunks · 2 source files · batch_id `OPPORTUNITY_MANAGEMENT_TEMPLATES` · validated 6/6.

## What this mini-batch covers

Two operator-facing AI-Edge-course templates that together form a complete opportunity-management system: an Excel workbook (`Opp hopper + Biz Case.xlsx` · 4 sheets) and a PowerPoint opportunity-card (`Opportunity Card [Example].pptx` · 2 slides · blank template + filled invoice-automation example). The mini-batch extracts the durable template STRUCTURE and decision discipline, not the sample data. It is the 4th 2026-05-19 mini-batch and the first to exercise the xlsx + pptx extraction pipelines.

4 chunks across 3 domains (no NEW domains):

| # | Concept | Domain | Source |
|--:|---|---|---|
| 001 | The opportunity hopper · goal-aligned intake register with auto-complexity scoring | operator-process | xlsx sheet 1 |
| 002 | The business-case ROI model · FTE cost baseline to cases/time/cost saved to dashboard | commercial-architecture | xlsx sheets 2-4 |
| 003 | The opportunity card · the standard one-page solution brief format | operator-process | pptx slide 1 |
| 004 | Opportunity-to-business-case translation + the implementation-readiness sign-off gate | client-application | pptx slide 2 + xlsx examples |

## Where this mini-batch lands canonically

### New operating templates installed

1. **The opportunity hopper** (chunk 001): a single intake register where every automation/AI idea names the business goal it serves and is AUTO-scored for complexity from five fixed diagnostic questions (standardised process? structured data? manual intervention? frequent exceptions? multiple integrations?). Prioritization becomes consistent, not vibes-based.
2. **The business-case ROI model** (chunk 002): a three-layer financial model (FTE cost baseline -> per-opportunity savings -> portfolio dashboard) that anchors on a cost-per-minute-of-labour and translates time-saved into FTE-saved and dollars-saved. The worked portfolio: 10 opportunities, ~30 FTE, ~$2.06M saved.
3. **The opportunity card** (chunk 003): a one-page brief (changes, benefits, category, feasibility, RAG, timeline, risk, dependencies, owner/analyst/sign-off, To-Be vs Current-State, pain points, KPIs) that makes a portfolio of opportunities comparable at a glance.
4. **The translation + readiness gate** (chunk 004): the chain goal -> logged opportunity -> auto-scored -> ROI case -> one-page card -> named sign-off with RAG + dependencies. Nothing gets built until the owner, approver, dependencies, and current-state baseline are explicit.

### Cross-references opened

- **BATCH_006 operator skill layer:** chunk 002 ↔ the AI Ops Dashboard PRD (opportunity-object schema + ROI-calculator pattern) · this workbook IS the calculator the PRD specified; chunk 001 ↔ the automation-blueprint domain (the hopper is the demand-intake front-end for the blueprints).
- **BATCH_007 operator doctrine / SOPs:** chunk 004 (named sign-off + dependencies + RAG) ↔ the final-review un-delegate-able + capture-to-delivery SLA gates (a readiness gate before build); chunk 003 ↔ the working-draft / brief discipline.
- **B2B_POSITIONING_CLAUDE_OPERATOR (just consolidated):** chunk 001 OPERATIONALIZES the B2B diagnostic (chunks 003-005: AI amplifies the system you already have · diagnose the bottleneck before deploying AI) · the hopper's five complexity questions ARE that diagnostic; chunk 002 ↔ B2B chunk 008 (commercial value); chunk 003 To-Be vs Current-State ↔ B2B chunk 002 (owner-as-integration-layer · which part of the stack stops being manual).
- **Future N8N_AUTOMATION_SYSTEMS (staged, not chunked):** the hopper's vendor column literally lists n8n, Make.com, OpenAI, Claude. This mini-batch is the INTAKE + PRIORITIZATION + ROI front-end; N8N is the IMPLEMENTATION layer. A card that clears the chunk-004 readiness gate becomes a workflow spec. Cross-reference at N8N consolidation.
- **Future BATCH_008 AI/tech canon (NOT started):** these are AI-Edge-course templates; the course books are queued for BATCH_008. Kept here as a reusable methodology mini-batch · cross-reference, do not merge.

### Auto-memory reinforcement

- `intel_pricing_logic.md` ↔ chunk 002 (cost-per-minute anchor · value-based ROI framing).
- The SNIPED executing-with-care discipline ↔ chunk 004 (gate the irreversible · named sign-off before build).

## Domain distribution

| Domain | Chunks | Notes |
|---|---:|---|
| operator-process | 2 | chunks 001 (intake/scoring) + 003 (card format) |
| commercial-architecture | 1 | chunk 002 (ROI model) |
| client-application | 1 | chunk 004 (translation + readiness) |

**No NEW domains introduced.** All 3 used domains pre-exist (operator-process 28, commercial-architecture 18, client-application 3). `strategy` (the optional 4th candidate) was not needed as a primary.

## Extraction-method results

| Source | Method | Result |
|---|---|---|
| `Opp hopper + Biz Case.xlsx` | stdlib zipfile + xml.etree (workbook.xml sheet order via rId, sharedStrings.xml string table, worksheets/sheetN.xml cell grid with `t="s"` resolution + numeric cached values) | 4 sheets · 136 shared strings · 1,936 words extracted |
| `Opportunity Card [Example].pptx` | stdlib zipfile + xml.etree (ppt/slides/slideN.xml in numeric order, `<a:t>` runs per slide, ppt/media ignored) | 2 slides · 2 media files ignored · 416 words extracted |

No new dependencies installed. `openpyxl` / `python-pptx` were not required. Both ZIP+XML containers parsed cleanly with stdlib.

## Excluded material

- Embedded slide images (`ppt/media/` · the 6.27 MB bulk) · not text · ignored by the extractor.
- Spreadsheet formula machinery / number-format / conditional-format XML · only values + headers extracted.
- Specific vendor names + the invoice $-figures · kept only as dated illustration inside chunks · summaries foreground the durable structure.

## Validation

All 6 checks (per `.claude/skills/jsonl-validation/SKILL.md`) PASS:
- JSONL parse · PASS
- Required fields present per line · PASS (all 12 fields · 0 missing)
- chunk_id uniqueness · PASS (0 duplicates across 4 chunks)
- batch_id consistency · PASS (single value `OPPORTUNITY_MANAGEMENT_TEMPLATES`)
- source_file resolution · PASS (both `opp_hopper_biz_case.txt` + `opportunity_card_example.txt` resolve under `opportunity_management_templates_extracted/`)
- Counts · 4 chunks / 2 unique sources

Em-dash sweep: 0 em-dashes in output.

## Deviations from OPPORTUNITY_MANAGEMENT_TEMPLATES_PLAN.md

1. **Final count 4** (target 4 · range 2-5). Exactly on target. The plan's merge option (003+004) and expand option (split scoring) were both declined · the four-chunk map (hopper / ROI model / card / translation-readiness) was the cleanest cut.
2. **Domain split operator-process 2 + commercial-architecture 1 + client-application 1.** No NEW domains. `strategy` was available as a secondary tag but not needed as a primary (matches plan section 4 "strategy only if needed").
3. **No structural deviations.** No source files moved/renamed/deleted. No master files updated. No new dependencies. BATCH_008 not started. No N8N / prompt-template / literary intake touched.

## What this mini-batch enables

1. **A reusable opportunity-management operating system** · intake (hopper) + scoring (auto-complexity) + ROI (business case) + brief (card) + readiness gate (sign-off) · directly usable for SNIPED systems-as-leverage client work.
2. **The xlsx + pptx extraction pipeline is now proven** · the extractor doubles as the reusable spreadsheet/slide extractor for future sources.
3. **The demand-to-build bridge into N8N_AUTOMATION_SYSTEMS is pre-wired** · a card that clears the readiness gate (chunk 004) becomes a workflow spec; the hopper vendor column already names n8n/Make.com/OpenAI/Claude.
4. **The B2B diagnostic gets an instrument** · chunk 001's five complexity questions operationalize the B2B "diagnose the bottleneck before deploying AI" principle.

## End state

`01_KNOWLEDGE_BASE/batches/OPPORTUNITY_MANAGEMENT_TEMPLATES_CHUNKS.jsonl` is canonical and validated. Awaits `master-consolidation` (operator authorization) to be promoted into the master files. No master files were updated in this batch run. New corpus total after consolidation: 884 + 4 = 888 chunks across 7 numbered batches + 4 mini-batches.
