# OPPORTUNITY_MANAGEMENT_TEMPLATES mini-batch plan · 2026-05-19

Plan only. No extraction, no chunking, no master-file updates, no BATCH_008 start, no commit. Stops after this plan is written.

This mini-batch extracts the durable operating templates + decision structures from two AI-Edge-course opportunity-management assets (an Excel opportunity-hopper + business-case workbook and a PowerPoint opportunity-card template). It is the 4th 2026-05-19 mini-batch and the second in the commercial / operator-process lane (after B2B_POSITIONING_CLAUDE_OPERATOR). Its primary secondary purpose is to validate the xlsx + pptx extraction pipelines, which the corpus has not exercised before.

---

## 0 · Headline

- **Sources:** `Opp hopper + Biz Case.xlsx` (75.7 KB · 4 sheets) + `Opportunity Card [Example].pptx` (6.27 MB · 2 slides · the size is embedded images, which we ignore). BOTH CONFIRMED on disk.
- **Extraction method:** stdlib `zipfile` + `xml.etree.ElementTree`. xlsx and pptx are both ZIP+XML containers, so text extracts with NO new dependencies. `openpyxl` and `python-pptx` are NOT installed, and `pandoc` cannot read xlsx/pptx as input · the stdlib path is the correct, dependency-free route (honors STAGING_PLAN section 8 "no new dependencies beyond what's already on PATH").
- **Estimated yield:** 2-5 chunks · target 4.
- **Domains:** operator-process, commercial-architecture, client-application (strategy available as a secondary tag if needed). ALL EXIST. No NEW domains.
- **Provenance:** both assets are "The AI Edge" course templates (the pptx footer reads "The AI Edge ©"). The same course's books are queued for BATCH_008. These are the operator-facing TEMPLATES, kept here as a reusable methodology mini-batch · cross-reference BATCH_008, do not merge into it.

---

## 1 · Source files confirmed on disk

| Role | Path | Size | Type | Status |
|---|---|---:|---|---|
| Workbook | `raw/10_REFERENCE/_intake_2026-05-19/opportunity_management/Opp hopper + Biz Case.xlsx` | 75.7 KB | Microsoft Excel 2007+ | EXISTS · 4 sheets |
| Slides | `raw/10_REFERENCE/_intake_2026-05-19/opportunity_management/Opportunity Card [Example].pptx` | 6.27 MB | Microsoft PowerPoint 2007+ | EXISTS · 2 slides + 2 media |

Both were staged in commit `215ffce` (2026-05-19 intake raw staging pass). Neither has been extracted or chunked.

---

## 2 · File types + extraction method decision

A read-only content peek (stdlib `zipfile` to stdout · no files written) was run on both files during planning.

### xlsx · `Opp hopper + Biz Case.xlsx` · 4 sheets

| Sheet | What it is |
|---|---|
| 1. Opportunity Hopper | Intake register. Columns: ID, Aligned to Goal, Title, Description, 5 complexity-scoring yes/no questions (process standardised? data structured? manual intervention? frequent exceptions? multiple integrations?) -> Complexity (AUTO), Time to Complete (mins), Volume/month, Time spent/month (min + hrs), Proposed Solution, Proposed Vendor, Process Re-engineering Required, Feasibility, Key Stakeholder Name/Email, Date Logged, Date Signed Off, Developed by. 10+ example rows (OPP-001..010) mapping business goals (Make More money / Stop spending / Grow in market / Improve processing times / Enabling scaling) to use-cases to solution types (Automation / Chatbot / AI / RPA) to vendors (Microsoft / BluePrism / Voiceflow / Celonis / Make.com / n8n / OpenAI / Claude). |
| 2. Business Case - Fundamentals | FTE cost baseline model: working days/year, holiday, hours/shift, efficiency, total FTE, total spend on FTE, cost per FTE / per hour / per minute, by business area. |
| 3. Business Case | ROI model: reduction in cases (%), new monthly case total, estimated time saving per case (%), new time per case, cases saved annually, time saved annually (min + hrs), FTE saved, cost saved, by business team. |
| 4. Business Case Dashboard | Rollup: number of opportunities identified, avg % reduction in cases + time, savings by team, complexity breakdown (low/med/high), solution-type breakdown (AI/Automation/Chatbot), feasibility breakdown, total value. |

**Method:** stdlib `zipfile` + `xml.etree.ElementTree`. Read `xl/workbook.xml` (sheet names + order), `xl/sharedStrings.xml` (string table · 136 strings confirmed), and `xl/worksheets/sheet1..4.xml` (cell refs + values, resolving `t="s"` shared-string indices and inline numerics). Render each sheet as a text block (sheet-name header + non-empty rows, tab- or pipe-delimited). No new dependencies.

### pptx · `Opportunity Card [Example].pptx` · 2 slides

| Slide | What it is |
|---|---|
| 1 | The BLANK opportunity-card template: ID | Solution Title, Description, Changes Required (3 points), Expected Benefits (Time Saving / Cost Saving / FTE Equivalent), Category (AI/Automation/Chatbot), Feasibility (H/M/L), RAG status (Green/Amber/Red), Est Timeline (Days/Weeks/Months), Risk (H/M/L), Dependencies, Executive Summary of Solution, Process Owner / Business Analyst / Sign-off / Date roles, To-Be vs Current State, Executive Summary of process, Key Pain Points, Process KPIs (number of cases, time period, avg time/case, complexity, number of FTE, dependencies). |
| 2 | A FILLED worked example: "Automation of Invoice Processing" (RPA bot · 10 min/invoice time saving · $20,000 cost saving · 1 FTE equivalent · Medium feasibility · 300 invoices/month · 15 min/invoice · 3 FTE involved · ERP-integration + invoice-rules dependencies · named Process Owner/BA/Sign-off). |

**Method:** stdlib `zipfile` + `xml.etree.ElementTree`. Iterate `ppt/slides/slide1.xml` + `slide2.xml` in numeric order, extract `<a:t>` text runs grouped per slide, render "Slide N" text blocks. Ignore `ppt/media/` (the 6.27 MB is embedded images · not text). No new dependencies.

**Pipeline-validation note:** this is the FIRST mini-batch to extract xlsx + pptx. The extraction script doubles as the reusable xlsx/pptx extractor for the future N8N_AUTOMATION_SYSTEMS (JSON) and any later spreadsheet/slide sources.

---

## 3 · Estimated chunk yield · 2-5 chunks · target 4

Mapped from the durable methodology in the two assets. The example rows / filled slide are durable as DEMONSTRATIONS of the translation pipeline, not as disposable sample data.

| # | Working concept | Source | Domain (primary) | Notes |
|--:|---|---|---|---|
| 001 | The opportunity hopper · intake + auto-complexity scoring · goal-aligned use-case register | xlsx sheet 1 | operator-process | The 5-question complexity auto-score + feasibility + solution-type/vendor taxonomy + goal-alignment column. The intake discipline. |
| 002 | The business-case ROI model · FTE cost baseline to cases/time/cost saved · dashboard rollup | xlsx sheets 2-4 | commercial-architecture | The 3-layer financial model: FTE costing fundamentals -> per-opportunity savings -> portfolio dashboard (total value, savings by team, complexity/type/feasibility breakdowns). |
| 003 | The opportunity card · one-page solution brief format | pptx slide 1 | operator-process | The standard fields: ID/title/description/changes/benefits/category/feasibility/RAG/timeline/risk/dependencies + To-Be vs Current State + KPIs + sign-off roles. The communication artifact. |
| 004 | Opportunity-to-business-case translation + implementation readiness | xlsx OPP examples + pptx slide 2 | client-application | The end-to-end pipeline: business goal -> logged opportunity -> auto-scored complexity/feasibility -> ROI business case -> one-page card -> named sign-off (Process Owner / BA / approver) + RAG + dependencies. The readiness gate before build. |

**Merge options:** 003 + 004 collapse into one card-plus-worked-example chunk (yields 3); 001 + 002 are distinct (intake vs financial model) and should stay separate. **Expand option:** split a dedicated prioritization/scoring chunk out of 001 (the complexity AUTO + feasibility + dashboard ranking) for 5. Recommendation: target 4 as mapped; acceptable range 3-5.

---

## 4 · Approved domains / tags

All candidate domains ALREADY EXIST. No NEW domains. Counts at 884-chunk state:

| Domain | Current count | Use in this mini-batch |
|---|---:|---|
| operator-process | 28 | primary on 001 (intake/scoring) + 003 (card format) |
| commercial-architecture | 18 | primary on 002 (ROI/business-case model) |
| client-application | 3 | primary on 004 (translation + readiness) |
| strategy | 97 | available as a secondary tag only if a chunk needs it (prioritization-as-strategy); no primary expected |

**Recommended tag bank** (free-text `tags`):
`opportunity-hopper`, `intake-register`, `complexity-scoring`, `auto-score`, `feasibility-rating`, `prioritization`, `business-case`, `roi-model`, `fte-cost-baseline`, `cost-saved`, `time-saved`, `dashboard-rollup`, `opportunity-card`, `one-page-brief`, `rag-status`, `to-be-vs-current-state`, `process-kpis`, `implementation-readiness`, `sign-off-gate`, `use-case-intake`, `automation-vs-chatbot-vs-ai`, `vendor-taxonomy`, `the-ai-edge`, `template`, `ai-tooling-aging-risk`.

**Aging note:** the vendor names (BluePrism, Voiceflow, Celonis, Make.com, n8n, OpenAI, Claude) and the AI-Edge-course framing age; the intake/scoring/ROI/card STRUCTURE does not. Chunk summaries should foreground the durable template structure and treat specific vendors/examples as dated illustration. Carry an `ai-tooling-aging-risk` tag + the 2026-05-19 source date.

---

## 5 · How this mini-batch connects to the rest of the corpus

### BATCH_006 operator skill layer
- Chunk 002 (ROI / business-case model) ↔ the B6 AI Ops Dashboard PRD (opportunity-object schema + ROI-calculator pattern already chunked). This mini-batch is the spreadsheet INSTANTIATION of that PRD's calculator. Direct structural pair.
- Chunk 001 (intake + scoring) ↔ B6 automation-blueprint domain · the hopper is the demand-intake front-end for the blueprints.

### BATCH_007 operator doctrine / SOPs
- Chunk 004 (implementation readiness + sign-off gate) ↔ B7 recurring_checklists + the final-review / approval discipline · the RAG + named-sign-off + dependencies are a readiness gate analogous to the SNIPED capture-to-delivery SLA gates.
- Chunk 003 (one-page card) ↔ B7 working-draft / brief formats · a standard communication artifact.

### B2B_POSITIONING_CLAUDE_OPERATOR (just consolidated)
- Chunk 001 (auto-complexity scoring · "is the process standardised / data structured / manual intervention") OPERATIONALIZES the B2B chunk 003-005 diagnostic ("AI amplifies the system you already have" + cognitive-vs-responsiveness + the missed-call gap). B2B says diagnose the bottleneck before deploying AI; this hopper IS the diagnostic instrument. Strong demand-side pairing.
- Chunk 002 (cost-saved ROI) ↔ B2B chunk 008 (productization / commercial value framing).

### Future N8N_AUTOMATION_SYSTEMS (staged, not chunked)
- The hopper's vendor/solution-type taxonomy literally lists n8n, Make.com, OpenAI, Claude. The opportunity-card + business-case are the front-end that feeds the n8n workflow builds. This mini-batch is the INTAKE + PRIORITIZATION + ROI layer; N8N_AUTOMATION_SYSTEMS is the IMPLEMENTATION layer. Cross-reference at N8N consolidation: hopper opportunity -> scored -> business case -> card -> n8n workflow build.

### Future BATCH_008 AI / tech canon (NOT started)
- These are AI-Edge-course TEMPLATES; the AI Edge Course books are queued for BATCH_008. Keep the templates here as a reusable methodology mini-batch · cross-reference BATCH_008, do not merge.

---

## 6 · Deliverables (produced in the EXTRACTION + CHUNK session · NOT now)

| Deliverable | Path | Notes |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/OPPORTUNITY_MANAGEMENT_TEMPLATES_CHUNKS.jsonl` | 2-5 chunks · batch_id `OPPORTUNITY_MANAGEMENT_TEMPLATES` · 12-field canonical schema |
| Extracted source dir | `01_KNOWLEDGE_BASE/batches/opportunity_management_templates_extracted/` | holds `opp_hopper_biz_case.txt` + `opportunity_card_example.txt` |
| Summary | `01_KNOWLEDGE_BASE/summaries/OPPORTUNITY_MANAGEMENT_TEMPLATES_SUMMARY.md` | what it covers · where it lands · cross-references |
| Source index | `01_KNOWLEDGE_BASE/indexes/OPPORTUNITY_MANAGEMENT_TEMPLATES_SOURCE_INDEX.md` | per-chunk concept + domain + source-sheet/slide map |
| Extraction log | `00_COMMAND_CENTER/batch_logs/OPPORTUNITY_MANAGEMENT_TEMPLATES_EXTRACTION_LOG.md` | sources in / extracted out / failures |
| Completion marker | `00_COMMAND_CENTER/batch_logs/OPPORTUNITY_MANAGEMENT_TEMPLATES_COMPLETE.md` | status · validation summary · deviations |
| Extraction script | `scripts/extract_opportunity_management_templates.py` | NEEDED · stdlib zipfile + xml.etree · xlsx (sheets via sharedStrings + cell grid) + pptx (slides via `<a:t>` runs) -> normalized `.txt`. No new deps. |
| Chunk writer | `scripts/write_opportunity_management_templates_chunks.py` | NEEDED · hand-authored chunk emit + em-dash sweep via `chr(0x2014)`. Mirror `scripts/write_b2b_positioning_claude_operator_chunks.py`. |

### Schema decisions (recommended · finalized at chunk-write time)
- `batch_id`: `OPPORTUNITY_MANAGEMENT_TEMPLATES`
- `chunk_id` pattern: `OPPORTUNITY_MANAGEMENT_TEMPLATES_001` ... `_005`
- `source_title`: `Opportunity Hopper + Business Case · The AI Edge` (xlsx chunks) · `Opportunity Card template · The AI Edge` (pptx chunks)
- `author`: `The AI Edge (course templates)` · these are course-provided operator templates, not single-authored prose
- `source_file`: normalized lowercase-snake-case · `opp_hopper_biz_case.txt` (xlsx) and `opportunity_card_example.txt` (pptx)

---

## 7 · Explicit exclusions

| Material | Disposition |
|---|---|
| Embedded slide images (`ppt/media/` · the 6.27 MB bulk) | EXCLUDE · not text · ignored by the stdlib extractor |
| Spreadsheet styling / formula internals (number formats, conditional-format XML) | EXCLUDE · extract VALUES + headers only, not the formula machinery |
| Specific vendor names + the invoice $-figures | KEPT only as dated illustration inside the relevant chunk · summaries foreground the durable structure |
| N8N / prompt-template / literary intake sources | OUT OF SCOPE · not touched |

---

## 8 · What this planning session does NOT do

- No extraction. The planning peek used stdlib `zipfile` to stdout only · no extracted files written.
- No chunking. No JSONL writes.
- No master-file updates (`MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched).
- No script files written.
- No BATCH_008 start.
- No N8N / prompt-template / literary intake touched.
- No source files moved/renamed/deleted.
- No commit.

---

## 9 · Recommended next operation

Authorize the extraction + chunk session per the locked 7-step SOP (steps 5-6):
1. Run `scripts/extract_opportunity_management_templates.py` · stdlib zipfile + xml.etree on both files into `opportunity_management_templates_extracted/`.
2. Hand-author 2-5 chunks (target 4) per the section 3 map.
3. Run `jsonl-validation` (6 checks) + em-dash sweep.
4. Write summary + source index + logs + completion marker.
5. Stop after validation + reporting · await `master-consolidation` authorization.

After this mini-batch consolidates (target 884 -> 886-889), the next queued mini-batch per `STAGING_PLAN_2026-05-19_INTAKE.md` section 5 is `N8N_AUTOMATION_SYSTEMS` (6 n8n JSON workflows · 15-25 chunks), then `PROMPT_TEMPLATES_DEEP`, before the literary-canon passes and BATCH_008.

---

## 10 · Revision log

- **rev 1 (2026-05-19 · this version):** First plan for the OPPORTUNITY_MANAGEMENT_TEMPLATES mini-batch. Both sources confirmed on disk. Read-only stdlib peek run on both (4 xlsx sheets · 2 pptx slides). Extraction method: stdlib zipfile + xml.etree (no new deps · openpyxl/python-pptx not installed, pandoc cannot read xlsx/pptx). 2-5 chunk estimate · target 4. All candidate domains (operator-process, commercial-architecture, client-application, strategy) confirmed pre-existing · no NEW domains. Cross-references mapped to B6 AI Ops Dashboard PRD, B7 readiness gates, B2B_POSITIONING_CLAUDE_OPERATOR (the hopper operationalizes the B2B diagnostic), and future N8N_AUTOMATION_SYSTEMS (intake/ROI front-end to the workflow builds). Provenance: AI Edge course templates · cross-reference BATCH_008, do not merge.
