# OPPORTUNITY_MANAGEMENT_TEMPLATES source index · 2026-05-19

2 source files · 4 chunks · batch_id `OPPORTUNITY_MANAGEMENT_TEMPLATES`.

## Sources

| # | Extracted file | Chunks | Range | Original source |
|--:|---|---:|---|---|
| 1 | `opp_hopper_biz_case.txt` | 2 | OPPORTUNITY_MANAGEMENT_TEMPLATES_001 - 002 | `raw/10_REFERENCE/_intake_2026-05-19/opportunity_management/Opp hopper + Biz Case.xlsx` |
| 2 | `opportunity_card_example.txt` | 2 | OPPORTUNITY_MANAGEMENT_TEMPLATES_003 - 004 | `raw/10_REFERENCE/_intake_2026-05-19/opportunity_management/Opportunity Card [Example].pptx` |

Source: The AI Edge (course templates). xlsx = 4 sheets (Opportunity Hopper · Business Case - Fundamentals · Business Case · Business Case Dashboard · 136 shared strings · 1,936 words). pptx = 2 slides (blank opportunity-card template + filled invoice-automation example · 416 words · embedded media ignored). Extracted via stdlib zipfile + xml.etree (no new dependencies).

## Per-chunk concept + domain + source map + cross-reference

| chunk_id | Concept | Domain | Source | Primary cross-references |
|---|---|---|---|---|
| 001 | The opportunity hopper · goal-aligned intake + auto-complexity scoring | operator-process | xlsx sheet 1 (Opportunity Hopper) | B2B_POSITIONING_CLAUDE_OPERATOR 003-005 (diagnose before deploying) + B6 AI Ops Dashboard PRD + future N8N vendor taxonomy |
| 002 | The business-case ROI model · FTE baseline to cost saved to dashboard | commercial-architecture | xlsx sheets 2-4 (Fundamentals + Business Case + Dashboard) | B6 AI Ops Dashboard PRD ROI-calculator + intel_pricing_logic + B2B chunk 008 |
| 003 | The opportunity card · one-page solution brief format | operator-process | pptx slide 1 (blank template) | B7 working-draft/brief discipline + B2B chunk 002 (To-Be vs Current-State) |
| 004 | Opportunity-to-business-case translation + implementation-readiness sign-off gate | client-application | pptx slide 2 (worked example) + xlsx OPP rows | B7 final-review un-delegate-able + B2B chunk 007 (implementation gap) + future N8N (card -> workflow spec) |

## Source-part routing

### xlsx · `Opp hopper + Biz Case.xlsx`

| Sheet | Chunk | Disposition |
|---|---|---|
| 1. Opportunity Hopper | 001 | intake register + 5-question auto-complexity score + vendor/solution-type taxonomy |
| 2. Business Case - Fundamentals | 002 | FTE cost baseline (days, hours, efficiency, cost-per-minute) |
| 3. Business Case | 002 | per-opportunity ROI (cases/time/FTE/cost saved) |
| 4. Business Case Dashboard | 002 | portfolio rollup (total value by team / complexity / solution type / feasibility) |

### pptx · `Opportunity Card [Example].pptx`

| Slide | Chunk | Disposition |
|---|---|---|
| 1 (blank template) | 003 | the standard card fields (benefits, category, feasibility, RAG, timeline, risk, dependencies, sign-off roles, To-Be vs Current-State, KPIs) |
| 2 (invoice example) | 004 | the worked translation + readiness gate (named owner/analyst/sign-off + dependencies) |
| embedded media (`ppt/media/`) | none | EXCLUDED · images · ignored |

## Cross-batch reinforcement summary

This mini-batch is the **opportunity-intake + prioritization + ROI + readiness layer** for AI/automation work. It is the demand-side instrument that operationalizes the B2B_POSITIONING_CLAUDE_OPERATOR diagnostic and the front-end that feeds the future N8N_AUTOMATION_SYSTEMS implementation builds.

| OMT chunk | Forward / lateral link |
|---|---|
| 001 hopper (auto-complexity score) | B2B 003-005 diagnostic · the instrument that decides candidacy |
| 002 ROI model | B6 AI Ops Dashboard PRD calculator · the spreadsheet instantiation |
| 003 card | B7 brief discipline · standard decision artifact |
| 004 readiness gate | future N8N_AUTOMATION_SYSTEMS · a cleared card becomes a workflow spec |

## Excluded material (NOT chunked)

| Material | Reason |
|---|---|
| Embedded slide images (`ppt/media/`) | Not text · ignored by the stdlib extractor |
| Spreadsheet formula machinery / formats | Only values + headers extracted |
| Specific vendor names + invoice $-figures | Kept only as dated illustration · structure is the durable signal |
| N8N / prompt-template / literary intake | Out of scope · not touched |
