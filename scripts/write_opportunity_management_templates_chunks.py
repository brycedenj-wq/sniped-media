#!/usr/bin/env python3
"""
OPPORTUNITY_MANAGEMENT_TEMPLATES chunker · AI Edge opportunity-management templates

Reads the two extracted txt files and emits OPPORTUNITY_MANAGEMENT_TEMPLATES_CHUNKS.jsonl
with the canonical 12-field schema.

Target: 4 chunks (range 2-5 per plan section 3).
Domains per plan section 4 (all pre-existing · no NEW domain):
  operator-process (001 intake/scoring + 003 card format) ·
  commercial-architecture (002 ROI model) ·
  client-application (004 translation + readiness).
strategy is available as a secondary tag only · not used as a primary.

Source files:
  opp_hopper_biz_case.txt        -> chunks 001, 002 (xlsx · 4 sheets)
  opportunity_card_example.txt   -> chunks 003, 004 (pptx · 2 slides)

Em-dash sweep (Unicode U+2014) applied to output.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "OPPORTUNITY_MANAGEMENT_TEMPLATES_CHUNKS.jsonl"

BATCH_ID = "OPPORTUNITY_MANAGEMENT_TEMPLATES"
AUTHOR = "The AI Edge (course templates)"
TITLE_XLSX = "Opportunity Hopper + Business Case · The AI Edge"
TITLE_PPTX = "Opportunity Card template · The AI Edge"
SRC_XLSX = "opp_hopper_biz_case.txt"
SRC_PPTX = "opportunity_card_example.txt"

BASE_TAGS = ["opportunity-management", "the-ai-edge", "template", "2026-05-19", "ai-tooling-aging-risk"]

chunks = []


def add_chunk(num, source_title, source_file, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags):
    chunks.append({
        "chunk_id": f"{BATCH_ID}_{num:03d}",
        "batch_id": BATCH_ID,
        "source_title": source_title,
        "source_file": source_file,
        "author": AUTHOR,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": usable_principle,
        "sniped_relevance": sniped_relevance,
        "direct_quotes": direct_quotes,
        "tags": BASE_TAGS + tags,
    })


# ---------------------------------------------------------------------------
# Chunk 1 · Opportunity Hopper · intake + auto-complexity scoring (xlsx sheet 1) · operator-process
# ---------------------------------------------------------------------------
add_chunk(
    num=1,
    source_title=TITLE_XLSX,
    source_file=SRC_XLSX,
    domain="operator-process",
    concept="The opportunity hopper · goal-aligned intake register with auto-complexity scoring",
    summary=(
        "A structured intake register for automation / AI opportunities. Every candidate gets an ID, a "
        "business goal it is aligned to (Make more money / Stop spending so much / Grow in market / "
        "Improve processing times / Enabling scaling), a title and description. Complexity is "
        "AUTO-scored from five yes/no diagnostic questions: is the process standardised, is the data "
        "structured and consistent, does it require manual intervention, are there frequent exceptions "
        "or edge cases, and does it rely on multiple system integrations. The register then captures "
        "time-to-complete, monthly volume, derived time-spent-per-month, a proposed solution + vendor, "
        "whether process re-engineering is required, a feasibility rating, the key stakeholder, dates "
        "logged and signed off, and the developing analyst. Solution types resolve to Automation / "
        "Chatbot / AI / RPA against a vendor taxonomy (Microsoft, BluePrism, Voiceflow, Celonis, "
        "Make.com, n8n, OpenAI, Claude)."
    ),
    usable_principle=(
        "Run every automation/AI idea through one intake register before building. Force each entry to "
        "name the business goal it serves, then auto-score complexity from a fixed five-question "
        "diagnostic (standardised process? structured data? manual intervention? frequent exceptions? "
        "many integrations?) so prioritization is consistent and not vibes-based. Capture volume + "
        "time-per-case up front so the ROI case can be computed later from the same row."
    ),
    sniped_relevance=(
        "Operationalizes the B2B_POSITIONING_CLAUDE_OPERATOR diagnostic (chunks 003-005: AI amplifies "
        "the system you already have · diagnose the bottleneck before deploying AI). The hopper IS that "
        "diagnostic instrument · the five complexity questions decide whether a process is even a "
        "candidate. Pairs with the BATCH_006 AI Ops Dashboard PRD opportunity-object schema and feeds "
        "the future N8N_AUTOMATION_SYSTEMS builds (the vendor column literally lists n8n / Make.com / "
        "OpenAI / Claude). The goal-alignment column maps to the SNIPED single-thread / mission-first "
        "discipline (B7 MONDAY_COCKPIT)."
    ),
    direct_quotes=[
        "Is the process standardised? | Is the data structured and consistent? | Does the process require manual intervention? | Are there frequent exceptions or edge cases? | Does the process rely on multiple system integrations? | Complexity (AUTO)",
        "ID | Aligned to Goal: | Title | Description | ... | Proposed Solution | Proposed Vendor | Process Re-engineering Required? | Feasibility | Key Stakeholder Name | Date Logged | Date Signed Off | Developed by: Business Analyst",
    ],
    tags=[
        "opportunity-hopper", "intake-register", "complexity-scoring", "auto-score",
        "feasibility-rating", "use-case-intake", "prioritization", "vendor-taxonomy",
        "automation-vs-chatbot-vs-ai", "goal-alignment",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 2 · Business-case ROI model + dashboard (xlsx sheets 2-4) · commercial-architecture
# ---------------------------------------------------------------------------
add_chunk(
    num=2,
    source_title=TITLE_XLSX,
    source_file=SRC_XLSX,
    domain="commercial-architecture",
    concept="The business-case ROI model · FTE cost baseline to cases/time/cost saved to portfolio dashboard",
    summary=(
        "A three-layer financial model that turns a logged opportunity into a defensible ROI case. "
        "Layer 1 (Fundamentals) builds the labour cost baseline: working days per year minus holiday "
        "gives working days per FTE, times hours per shift and an efficiency factor gives total hours "
        "worked, and per-business-area FTE counts times cost-per-FTE derive cost-per-hour and "
        "cost-per-minute. Layer 2 (Business Case) applies a per-opportunity reduction-in-cases percent "
        "and time-saving-per-case percent to compute cases saved annually, time saved annually, FTE "
        "saved, and cost saved. Layer 3 (Dashboard) rolls the portfolio up: number of opportunities, "
        "total FTE saved, total cost saved, average percent reductions, savings by team, and total "
        "value broken down by complexity, solution type, and feasibility. The worked portfolio shows 10 "
        "opportunities yielding ~30 FTE and ~$2.06M saved."
    ),
    usable_principle=(
        "Express every automation case in money, not enthusiasm. Anchor on a cost-per-minute of labour "
        "derived from a real FTE baseline (days, hours, efficiency, cost per FTE), then translate "
        "time-saved-per-case into cases-saved, FTE-saved, and dollars-saved. Roll individual cases into "
        "a portfolio dashboard so prioritization is by total value, not by who shouts loudest. The "
        "cost-per-minute anchor is the unit that makes any process improvement comparable."
    ),
    sniped_relevance=(
        "The spreadsheet instantiation of the BATCH_006 AI Ops Dashboard PRD ROI-calculator pattern · "
        "the PRD specified the calculator, this model IS it. The cost-per-minute-of-labour anchor is a "
        "commercial-architecture primitive reusable for any SNIPED time-savings or efficiency pitch, "
        "and pairs with intel_pricing_logic (value-based framing) + B2B_POSITIONING_CLAUDE_OPERATOR "
        "chunk 008 (commercial value). Useful when sizing the dollar value of a SNIPED systems-as-"
        "leverage offer for a client."
    ),
    direct_quotes=[
        "Total Number of FTE | 75 | Total Spend on FTE | 3975000 ... Cost Per Hour ... Cost Per Min",
        "Reduction in cases? (%) | ... | Estimated Time Saving per case (%) | ... | Cases Saved Annually | Time Saved Annually | FTE Saved | Cost Saved",
        "Number of Opportunities Identified | 10 ... FTE Saved | 30.27 ... Cost Saved | 2062599",
    ],
    tags=[
        "business-case", "roi-model", "fte-cost-baseline", "cost-per-minute",
        "cost-saved", "time-saved", "dashboard-rollup", "portfolio-prioritization", "total-value",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 3 · Opportunity card · one-page solution brief format (pptx slide 1) · operator-process
# ---------------------------------------------------------------------------
add_chunk(
    num=3,
    source_title=TITLE_PPTX,
    source_file=SRC_PPTX,
    domain="operator-process",
    concept="The opportunity card · the standard one-page solution brief format",
    summary=(
        "A single-page communication artifact that presents a scored opportunity for a decision. The "
        "front captures the solution: ID and title, description, the changes required (3 bullets), "
        "expected benefits (time saving / cost saving / FTE equivalent), category (AI / Automation / "
        "Chatbot), feasibility (High/Medium/Low), an overall RAG status (Green / Amber / Red), "
        "estimated timeline (Days / Weeks / Months), risk (High/Medium/Low), dependencies, and an "
        "executive summary of the solution, with named Process Owner, Business Analyst, and sign-off "
        "roles plus a date. The back captures the process being changed in a To-Be vs Current-State "
        "split: executive summary of the process, key pain points, and process KPIs (number of cases, "
        "time period, average time per case, complexity, number of people involved, dependencies)."
    ),
    usable_principle=(
        "Compress every opportunity into one standard card before asking for a decision: what changes, "
        "what it saves (time / cost / FTE), how feasible and how risky, how long, what it depends on, "
        "and who owns and signs off. Always pair the To-Be with the Current State and the pain points "
        "so the reader sees the gap, not just the proposal. A consistent one-pager makes a portfolio of "
        "opportunities comparable at a glance."
    ),
    sniped_relevance=(
        "A reusable brief format that maps to the SNIPED working-draft / brief discipline (B7) and the "
        "hospitality-grade clarity of client-facing artifacts. The RAG + risk + dependency + named "
        "sign-off fields are a readiness gate analogous to the B7 capture-to-delivery SLA gates. The "
        "To-Be vs Current-State framing pairs with the B2B owner-as-integration-layer chunk (002): the "
        "card shows the owner exactly which part of the stack stops being manual."
    ),
    direct_quotes=[
        "Expected Benefits | Time Saving: | Cost Saving: | FTE Equivalent: | Category | AI / Automation / Chatbot | Feasibility | High/Medium/Low | Green/Amber/Red | Est Timeline | Days/Weeks/Months | Risk | Any dependencies:",
        "Process Owner | Business Analyst | Providing Sign off | Date",
        "To Be | Current State | Executive Summary of process: | Key Pain Points in the process: | Process Key Performance Indicators (KPI)",
    ],
    tags=[
        "opportunity-card", "one-page-brief", "rag-status", "to-be-vs-current-state",
        "process-kpis", "solution-brief", "feasibility-rating", "risk-rating", "decision-artifact",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 4 · Opportunity-to-business-case translation + implementation readiness (pptx slide 2 + xlsx examples) · client-application
# ---------------------------------------------------------------------------
add_chunk(
    num=4,
    source_title=TITLE_PPTX,
    source_file=SRC_PPTX,
    domain="client-application",
    concept="Opportunity-to-business-case translation + the implementation-readiness sign-off gate",
    summary=(
        "The end-to-end pipeline that turns a vague 'use AI for the business' wish into a build-ready, "
        "signed-off case, shown by the worked invoice-processing example. The chain: a business goal "
        "becomes a logged opportunity, auto-scored for complexity and feasibility, costed into an ROI "
        "business case (the example: 10 min saved per invoice, $20,000 cost saving, 1 FTE equivalent, "
        "300 invoices per month at 15 minutes each, 3 people involved), then compressed onto a one-page "
        "card with a Current-State vs To-Be split, key pain points (high error rates, delayed approvals, "
        "high staff workload), explicit dependencies (ERP integration, invoice-rule finalisation), and "
        "named accountability (Process Owner Alex, Business Analyst Fred, sign-off Jane, dated). The "
        "readiness gate is the named sign-off plus RAG plus dependencies · nothing gets built until "
        "those are filled."
    ),
    usable_principle=(
        "Translate every client AI request into the same readiness chain before building: goal -> "
        "logged opportunity -> auto-scored complexity/feasibility -> ROI case -> one-page card -> named "
        "sign-off with RAG and dependencies. Refuse to start the build until the owner, the approver, "
        "the dependencies, and the current-state baseline are explicit. Naming the dependencies and the "
        "accountable owner is what separates a real implementation from a demo."
    ),
    sniped_relevance=(
        "The client-application translation layer for SNIPED systems work: it is the readiness gate "
        "before any AI build, the inverse-facing companion to the B2B implementation-gap chunk (007 · "
        "agent-inside-the-business requires connecting the core operational tool). The named-sign-off + "
        "dependency-list discipline maps to the SNIPED final-review un-delegate-able (B7) and the "
        "executing-with-care principle (gate the irreversible). It is the demand-to-build bridge into "
        "the future N8N_AUTOMATION_SYSTEMS mini-batch: a card that clears this gate becomes a workflow "
        "spec."
    ),
    direct_quotes=[
        "Automation of Invoice Processing ... Time Saving: 10 min per invoice | Cost Saving: $20,000 | FTE Equivalent: 1 FTE",
        "Process Owner: Alex | Business Analyst: Fred | Providing Sign off: Jane | Date: <Today>",
        "Key Pain Points: High error rates due to manual data entry. Delayed approvals resulting in late vendor payments. High workload for finance staff, reducing time for strategic tasks.",
    ],
    tags=[
        "implementation-readiness", "sign-off-gate", "business-case-translation",
        "client-application", "current-state-vs-to-be", "named-accountability",
        "dependency-list", "worked-example", "n8n-demand-signal",
    ],
)


# ===========================================================================
# Write JSONL + em-dash sweep
# ===========================================================================

def main():
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"Wrote {len(chunks)} chunks to {OUT_JSONL}")

    em_char = chr(0x2014)
    text = OUT_JSONL.read_text(encoding="utf-8")
    em_count = text.count(em_char)
    if em_count:
        print(f"WARNING: {em_count} em-dashes in output. Sweeping.")
        text = text.replace(em_char, " · ")
        OUT_JSONL.write_text(text, encoding="utf-8")
    else:
        print("No em-dashes in output.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
