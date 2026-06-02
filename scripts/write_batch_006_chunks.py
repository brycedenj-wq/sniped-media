#!/usr/bin/env python3
"""
BATCH_006 chunker · operator-engine skill layer (rev 2)

Reads 01_KNOWLEDGE_BASE/batches/batch_006_extracted/ (108 files) and emits
01_KNOWLEDGE_BASE/batches/BATCH_006_CHUNKS.jsonl with the canonical 12-field schema.

Target: ~115 chunks (range 100-125).
  - 50 SNIPED skill chunks (1 per skill, +1 extra for the 3 longest → 53)
  - 1  SKILL_BUILD_QUEUE meta chunk
  - 50 Claude50 framework prompt chunks
  - 7  Claude/AI tool workflow chunks
  - 3  automation blueprint chunks
  Total: 114

Approved domains (BATCH_006 enum, operator approval per BATCH_006_PLAN.md rev 2):
  EXISTING: operator-doctrine, aesthetics, production-sop, outreach-sop, pricing,
            client-application, meta-doctrine, strategy
  NEW:      prompt-engineering, ai-tooling, automation-blueprint, operator-process
"""

import json
import re
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
EXTRACTED = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_006_extracted"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_006_CHUNKS.jsonl"

BATCH_ID = "BATCH_006"
AUTHOR_SNIPED = "BJ / SNIPED Media"
AUTHOR_CLAUDE50 = "Claude AI Skills 50-Pack (external framework prompts)"
AUTHOR_EDGE = "The AI Edge community (third-party tutorial / PRD source)"


# ----- domain assignments -----

SNIPED_DOMAIN = {
    "sniped-canonical-truths": "operator-doctrine",
    "sniped-direction-stack": "operator-doctrine",
    "sniped-execution-prioritization": "operator-process",
    "sniped-monday-cockpit": "operator-process",
    "sniped-lean-audit": "operator-process",
    "sniped-reverse-roadmap": "operator-doctrine",
    "sniped-strategic-implications": "strategy",
    "sniped-hospitality-layer": "operator-doctrine",
    "sniped-partnership-protocol": "operator-doctrine",
    "sniped-assistant-task-routing": "operator-process",
    "sniped-pre-shoot-prep": "production-sop",
    "sniped-shoot-day-reset": "production-sop",
    "sniped-shoot-day-strategic-free": "production-sop",
    "sniped-post-shoot-same-day": "production-sop",
    "sniped-capture-to-delivery": "production-sop",
    "sniped-retoucher-onboarding": "production-sop",
    "sniped-production-os": "production-sop",
    "sniped-pixieset-gallery": "production-sop",
    "sniped-post-delivery": "production-sop",
    "sniped-udemy-lightroom-rails": "production-sop",
    "sniped-vib-outreach": "outreach-sop",
    "sniped-caption-writer": "outreach-sop",
    "sniped-discovery-to-close": "outreach-sop",
    "sniped-notion-crm-update": "outreach-sop",
    "sniped-pricing-decision": "pricing",
    "sniped-wwp-positioning": "pricing",
    "sniped-art-series": "client-application",
    "sniped-luxury-edit": "aesthetics",
    "sniped-hero-composite-ceiling": "aesthetics",
    "sniped-hero-composite-lite": "aesthetics",
    "sniped-evoto-skin-pass": "aesthetics",
    "sniped-higgsfield-pipeline": "aesthetics",
    "sniped-seedream-prompt": "aesthetics",
    "sniped-lighting-vault": "aesthetics",
    "sniped-ai-image-tool-pick": "ai-tooling",
    "sniped-udemy-ai-accelerants": "ai-tooling",
    "sniped-perennial-seller": "strategy",
    "sniped-new-luxury": "strategy",
    "sniped-company-of-one": "strategy",
    "sniped-trust-equation": "strategy",
    "sniped-hit-mechanics": "strategy",
    "sniped-trust-mechanics": "strategy",
    "sniped-status-psychology": "strategy",
    "sniped-ai-sentiment": "strategy",
    "sniped-ai-photographer-market": "strategy",
    "sniped-analog-premium": "strategy",
    "sniped-photo-theory": "strategy",
    "sniped-positioning-phrases": "strategy",
    "sniped-blockbuster-strategy": "strategy",
    "sniped-leverage-logic": "strategy",
}

CLAUDE50_DOMAIN = {
    # prompt-engineering · explicitly prompt-craft frameworks
    "prompt-engineering-tcrei": "prompt-engineering",
    "framework-orchestrator": "prompt-engineering",
    "pyramid-structured-communication": "prompt-engineering",
    "success-message-design": "prompt-engineering",
    "calm-authority-voice-calibration": "prompt-engineering",
    "copywriting-rule-of-one-awareness-staging": "prompt-engineering",
    "second-brain-code-para": "prompt-engineering",
    "professional-portrait-direction": "prompt-engineering",
    # meta-doctrine · decision / judgment frameworks
    "premortem-analysis": "meta-doctrine",
    "fermi-estimation": "meta-doctrine",
    "munger-two-track-decision-analysis": "meta-doctrine",
    "signal-noise-forecasting-bayesian": "meta-doctrine",
    "superforecasting-workflow": "meta-doctrine",
    "cognitive-bias-audit": "meta-doctrine",
    "bad-strategy-audit": "meta-doctrine",
    "shadow-test-pre-launch-validation": "meta-doctrine",
    # strategy · positioning / market frameworks
    "seven-powers-strategic-position-assessment": "strategy",
    "strategy-kernel-development": "strategy",
    "counter-positioning-diagnosis": "strategy",
    "create-destroy-strategy-stress-test": "strategy",
    "customer-segment-slicing": "strategy",
    "industry-dynamics-assessment": "strategy",
    "comparative-advantage-resource-allocation": "strategy",
    "market-evaluation-scorecard": "strategy",
    "revenue-growth-diagnostic": "strategy",
    "business-resilience-audit": "strategy",
    "economic-incentive-policy-analysis": "strategy",
    "hoshin-kanri-goal-alignment": "strategy",
    "freelance-platform-optimization": "strategy",
    "photography-business-system": "strategy",
    "business-entity-credit-architecture": "strategy",
    # operator-process · operating-process frameworks
    "lean-transformation-diagnostic": "operator-process",
    "value-stream-improvement-pdca": "operator-process",
    "system-analysis-intervention-design": "operator-process",
    "creative-resistance-turning-pro": "operator-process",
    # outreach-sop · sales / outreach frameworks
    "cold-email-campaign-architecture": "outreach-sop",
    "linkedin-growth-lead-generation": "outreach-sop",
    "mom-test-customer-conversation": "outreach-sop",
    "consultative-selling-system": "outreach-sop",
    "tactical-negotiation-ackerman-empathy": "outreach-sop",
    "negotiation-leverage-black-swan": "outreach-sop",
    "social-media-content-strategy": "outreach-sop",
    # ai-tooling · AI infrastructure / setup
    "ai-agent-architecture-wat": "ai-tooling",
    "ai-code-website-build-pipeline": "ai-tooling",
    "meta-business-infrastructure-setup": "ai-tooling",
    "server-farm-commissioning": "ai-tooling",
    "epms-site-analysis": "ai-tooling",
    # automation-blueprint · executable workflow blueprints
    "ai-video-production-pipeline": "automation-blueprint",
    "video-editing-assembly-line": "automation-blueprint",
    "preset-sync-export-photo-editing": "automation-blueprint",
}


# ----- SNIPED skill SNIPED-relevance lines (mapped by primary domain) -----

DOMAIN_RELEVANCE = {
    "operator-doctrine": "Operator-engine primitive · directly enforces a locked SNIPED doctrine (the canonical-truth layer, the methodology spine, the hospitality layer, or the partnership protocol). Skill is invokable when an operator decision tests the spine.",
    "operator-process": "Operator-process primitive · runs a weekly / daily / per-decision execution ritual (Monday cockpit, lean audit, execution prioritization, assistant task routing). Anchors the operating cadence.",
    "production-sop": "Production SOP primitive · runs a specific shoot-day or post-shoot workflow (pre-shoot prep, reset shoot day, strategic-free day, post-shoot same-day, capture-to-delivery, retoucher onboarding, production OS, Pixieset gallery, post-delivery, Lightroom rails). Operationalizes the locked production discipline.",
    "outreach-sop": "Outreach SOP primitive · runs the locked VIB cadence, caption library, discovery-to-close path, or Notion CRM update. Operationalizes the two-channel outbound + zero-cannibalization rule.",
    "pricing": "Pricing primitive · runs the $1,500 floor + scope-flexes rule + 3-option proposal anchor + walk-away discipline (Enns proclamations). Defends the floor in any pricing conversation.",
    "client-application": "Client-application primitive · runs the SNIPED Art Series recreation methodology against any client direction. Anchors the audit-then-recreate path.",
    "aesthetics": "Aesthetics primitive · runs a specific edit / composite / lighting / prompt-tool pipeline (luxury edit, hero composite ceiling, hero composite lite, Evoto skin, Higgsfield, Seedream, lighting vault). Defends the v3 LUXURY aesthetic discipline.",
    "ai-tooling": "AI tooling primitive · runs an image-tool pick or AI accelerant workflow. Pairs with the hybrid-operator AI stance (AI for inputs, never for identity).",
    "strategy": "Strategic primitive · surfaces a positioning / status / signaling / hit-mechanics / leverage rule on demand. Cross-applies to any strategic decision.",
    "prompt-engineering": "Prompt-engineering primitive · runs a foundational prompt-design framework (TCREI, framework-orchestrator, pyramid communication, calm authority voice, copywriting rule of one). Improves prompt quality across every other skill invocation.",
    "automation-blueprint": "Automation-blueprint primitive · a directly-executable workflow (video assembly, preset sync, content-strategy generator, voice agent). Operator engine can invoke as-is.",
    "meta-doctrine": "Meta-doctrine primitive · runs a decision / judgment framework (premortem, fermi, signal-noise, Munger two-track, bias audit). Cross-applies to any pivotal decision.",
}


# ----- frontmatter parser -----

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Supports single-line and multi-line YAML."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 4)
    if end < 0:
        return {}, text
    fm_block = text[4:end].strip()
    body = text[end + 4:].lstrip("\n")
    fm = {}
    current_key = None
    current_lines = []
    for line in fm_block.split("\n"):
        m = re.match(r"^([a-zA-Z_-]+):\s*(.*)$", line)
        if m and not line.startswith("  "):
            if current_key:
                fm[current_key] = "\n".join(current_lines).strip().lstrip("|").strip()
            current_key = m.group(1)
            current_lines = [m.group(2)] if m.group(2) else []
        else:
            current_lines.append(line.strip())
    if current_key:
        fm[current_key] = "\n".join(current_lines).strip().lstrip("|").strip()
    return fm, body


def extract_section(body: str, header: str) -> str:
    """Pull the body of an H1/H2/H3 section."""
    lines = body.split("\n")
    out = []
    in_section = False
    for line in lines:
        if re.match(rf"^#{{1,3}}\s*{re.escape(header)}", line, re.IGNORECASE):
            in_section = True
            continue
        if in_section and re.match(r"^#{1,3}\s", line):
            break
        if in_section:
            out.append(line)
    return "\n".join(out).strip()


def squeeze(text: str, max_chars: int = 800) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_chars]


def body_summary(body: str, max_chars: int = 600) -> str:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip() and not p.strip().startswith("#")]
    joined = " ".join(paragraphs)
    return squeeze(joined, max_chars)


# ----- chunk builders -----

chunks = []
chunk_id_counter = 0


def add_chunk(**kw):
    global chunk_id_counter
    chunk_id_counter += 1
    kw["chunk_id"] = f"BATCH_006_{chunk_id_counter:03d}"
    kw["batch_id"] = BATCH_ID
    chunks.append(kw)


def build_sniped_skill_chunk(slug: str, fm: dict, body: str, source_file: str, extra_chunk: bool = False):
    """Build 1 (or 2 for the longest) chunks for a SNIPED skill."""
    domain = SNIPED_DOMAIN.get(slug, "operator-doctrine")
    name = fm.get("name") or slug
    description = fm.get("description") or ""
    invoke = extract_section(body, "INVOKE WHEN") or extract_section(body, "Invoke When")
    output_spec = extract_section(body, "OUTPUT") or extract_section(body, "Output")
    refuse = extract_section(body, "REFUSE") or extract_section(body, "Refuse")
    mandatory = extract_section(body, "MANDATORY READING") or ""

    summary_lines = []
    if description:
        summary_lines.append(description)
    if invoke:
        summary_lines.append("Invoke when: " + squeeze(invoke, 350))
    if output_spec:
        summary_lines.append("Output: " + squeeze(output_spec, 250))
    summary = " ".join(summary_lines)

    usable_principle = (
        squeeze(refuse, 400) if refuse
        else "Run the skill on invocation, follow MANDATORY READING, produce the OUTPUT spec exactly, refuse out-of-lane requests."
    )

    quotes = []
    if description:
        quotes.append(squeeze(description, 200))
    if refuse:
        first_refuse = refuse.split("\n")[0].lstrip("- ").strip()
        if first_refuse:
            quotes.append("Refuse: " + squeeze(first_refuse, 150))

    tags = ["sniped-skill", slug, domain]
    if "operator" in slug or domain in ("operator-doctrine", "operator-process"):
        tags.append("operator-engine")

    add_chunk(
        source_title=name,
        source_file=source_file,
        author=AUTHOR_SNIPED,
        domain=domain,
        concept=f"SNIPED skill · {name}",
        summary=summary,
        usable_principle=usable_principle,
        sniped_relevance=DOMAIN_RELEVANCE.get(domain, "Operator-engine primitive."),
        direct_quotes=quotes,
        tags=tags,
    )

    if extra_chunk:
        # Second chunk for the 3 longest skills: the mandatory-reading + body methodology.
        extended_summary_lines = []
        if mandatory:
            extended_summary_lines.append("Mandatory reading: " + squeeze(mandatory, 400))
        method_section = body_summary(body, 600)
        if method_section:
            extended_summary_lines.append("Methodology: " + method_section)
        extended_summary = " ".join(extended_summary_lines) or body_summary(body, 700)
        add_chunk(
            source_title=name,
            source_file=source_file,
            author=AUTHOR_SNIPED,
            domain=domain,
            concept=f"SNIPED skill · {name} · extended methodology",
            summary=extended_summary,
            usable_principle="Read the MANDATORY READING references on every invocation; the skill is a thin shell over those source docs.",
            sniped_relevance=DOMAIN_RELEVANCE.get(domain, "Operator-engine primitive.") + " Extended chunk captures the per-invocation reading discipline.",
            direct_quotes=[],
            tags=tags + ["extended-methodology"],
        )


def build_claude50_chunk(slug: str, fm: dict, body: str, source_file: str):
    """Build 1 chunk for a Claude50 framework prompt."""
    domain = CLAUDE50_DOMAIN.get(slug, "prompt-engineering")
    name = fm.get("name") or slug
    description = fm.get("description") or ""
    purpose = extract_section(body, "Purpose")
    when_to_use = extract_section(body, "When to Use")
    workflow = extract_section(body, "Workflow")
    output_format = extract_section(body, "Output Format")
    constraints = extract_section(body, "Constraints")

    summary_parts = []
    if purpose:
        summary_parts.append("Purpose: " + squeeze(purpose, 300))
    if when_to_use:
        summary_parts.append("Use when: " + squeeze(when_to_use, 200))
    if workflow:
        summary_parts.append("Workflow: " + squeeze(workflow, 400))
    summary = " ".join(summary_parts) or squeeze(description, 600)

    usable_principle = (
        squeeze(constraints, 350) if constraints
        else "Execute the workflow steps in order against the user's input; emit the Output Format exactly."
    )
    if output_format:
        usable_principle = "Output Format: " + squeeze(output_format, 300) + " · " + usable_principle

    sniped_rel = DOMAIN_RELEVANCE.get(domain, "Framework prompt usable as a Claude skill.")

    quotes = []
    if description:
        first_line = description.split("\n")[0].strip()
        if first_line:
            quotes.append(squeeze(first_line, 200))

    tags = ["claude50", "framework-prompt", slug, domain]

    add_chunk(
        source_title=name,
        source_file=source_file,
        author=AUTHOR_CLAUDE50,
        domain=domain,
        concept=f"Framework prompt · {name}",
        summary=summary,
        usable_principle=usable_principle,
        sniped_relevance=sniped_rel,
        direct_quotes=quotes,
        tags=tags,
    )


def build_skill_build_queue_chunk(body: str, source_file: str):
    add_chunk(
        source_title="SKILL_BUILD_QUEUE",
        source_file=source_file,
        author=AUTHOR_SNIPED,
        domain="meta-doctrine",
        concept="SNIPED skill-build queue · meta-doctrine for how the operator-engine skills are designed",
        summary=(
            "Prioritized build order for the SNIPED skill suite. Discipline rules: "
            "one skill per source, reference (do not duplicate) source docs, frontmatter "
            "name + description is load-bearing because it determines whether Claude picks "
            "the skill, MANDATORY READING in every skill, refuse drift in every skill. "
            "Built status as of 2026-05-12: 28 of ~50 packs shipped across Tier 1 (6/6 complete) "
            "and Tier 2 strategic intel (17/17 complete), with skill numbering preserved."
        ),
        usable_principle=(
            "Five rules for any new SNIPED skill: (1) one skill per source · do not combine; "
            "(2) reference do not duplicate · skills READ source docs at invocation, do not copy content; "
            "(3) frontmatter is load-bearing · name + description decide if Claude picks the skill; "
            "(4) MANDATORY READING section in every skill · skill activation = read X, Y, Z before any output; "
            "(5) refuse drift · each skill names its lane and refuses out-of-lane requests."
        ),
        sniped_relevance=(
            "Meta-doctrine for the operator engine itself. When designing a new skill, run through "
            "these five rules. When auditing the existing 50, this is the gate."
        ),
        direct_quotes=[
            "One skill per source · don't combine.",
            "Frontmatter is load-bearing. name + description decide if Claude picks the skill.",
            "MANDATORY READING section in every skill.",
        ],
        tags=["sniped-skill", "skill-build-queue", "meta-doctrine", "operator-engine"],
    )


# ----- supporting-doc chunks (P3 tool workflows + P4 automation blueprints) -----

SUPPORTING_DOCS = [
    {
        "source_file": "intake__claude_code_superpowers.md",
        "source_title": "Claude Code · Superpowers plugin",
        "author": AUTHOR_EDGE,
        "domain": "ai-tooling",
        "chunks": [
            {
                "concept": "Claude Code Superpowers plugin · what it installs",
                "summary": (
                    "Superpowers is an agentic-skills plugin for Claude Code that enforces a "
                    "proper development workflow: brainstorm → write plan → execute plan with "
                    "TDD, sub-agents, code review, and git worktree isolation. 43K+ GitHub stars; "
                    "officially in the Anthropic marketplace. Two install methods: official "
                    "Anthropic marketplace (easiest) or GitHub repo add. Core commands: "
                    "/superpowers, brainstorm, write plan, execute plan."
                ),
                "usable_principle": (
                    "When using Claude Code on any non-trivial build, install Superpowers and "
                    "use brainstorm → write plan → execute plan instead of free-form prompting. "
                    "TDD, sub-agents, code review, and isolated git branches become enforced, "
                    "not optional."
                ),
                "sniped_relevance": (
                    "Direct upgrade to the operator engine when SNIPED builds or extends any AI tool. "
                    "The brainstorm → plan → execute discipline mirrors the SNIPED Direction Stack "
                    "and the 100Q audit pattern."
                ),
                "direct_quotes": [
                    "Superpowers plugin enforces a proper development workflow with brainstorming, planning, TDD, sub-agents, code review, and git worktree isolation.",
                ],
                "tags": ["claude-code", "superpowers", "ai-tooling", "operator-engine", "tdd", "git-worktree"],
            },
            {
                "concept": "Claude Code Superpowers · demo workflow + honest pros/cons",
                "summary": (
                    "Walkthrough demo: a Notion-style web app built from a vague prompt by going "
                    "vague-prompt → brainstorm → PRD → design docs → detailed implementation plan → "
                    "phased execution with sub-agents. Integrates with frontend-design plugin, "
                    "Supabase backend, Vercel hosting. Pros: dramatically better outputs and "
                    "structure, especially on existing repos. Cons: still needs human oversight "
                    "for edge cases, UI polish, and security reviews."
                ),
                "usable_principle": (
                    "Treat Superpowers as a discipline-enforcer not an autonomy-grant. Human review "
                    "is mandatory at edge cases, UI polish, and security. The plugin removes chaos "
                    "from iteration but does not remove the operator from the loop."
                ),
                "sniped_relevance": (
                    "Maps to the SNIPED un-delegate-ables ledger: methodology + final review stay "
                    "with the operator; structured execution can be plugin-enforced."
                ),
                "direct_quotes": [
                    "dramatically better outputs & structure (especially on existing repos), but still needs human oversight for edge cases, UI polish, security reviews",
                ],
                "tags": ["claude-code", "superpowers", "ai-tooling", "operator-engine", "human-in-loop"],
            },
        ],
    },
    {
        "source_file": "intake__claude_code_plugin.md",
        "source_title": "Claude Code · Plugin (Ralph Wiggum technique)",
        "author": AUTHOR_EDGE,
        "domain": "ai-tooling",
        "chunks": [
            {
                "concept": "Claude Code plugin · Ralph Wiggum technique",
                "summary": (
                    "The Ralph Wiggum technique loops Claude Code until a promise-tag completion "
                    "signal is emitted. Single-overnight build pattern. Plugin extends Claude Code "
                    "with the loop primitive plus the promise-tag completion convention. Use case: "
                    "build a complete dashboard or app in one unattended overnight session."
                ),
                "usable_principle": (
                    "Define a promise-tag (e.g., <promise>DASHBOARD_COMPLETE</promise>) and tell "
                    "Claude Code to loop until that tag is emitted. The plugin handles iteration "
                    "and completion-detection. Operator returns to a finished artifact."
                ),
                "sniped_relevance": (
                    "Unblocks SNIPED build initiatives that previously required operator-supervised "
                    "iteration. Maps cleanly to the Saturday Build cadence."
                ),
                "direct_quotes": [
                    "When complete, output: <promise>DASHBOARD_COMPLETE</promise>",
                ],
                "tags": ["claude-code", "ralph-wiggum", "ai-tooling", "loop", "promise-tag"],
            },
        ],
    },
    {
        "source_file": "intake__ai_ops_dashboard_prd.md",
        "source_title": "AI Ops Dashboard · PRD",
        "author": AUTHOR_EDGE,
        "domain": "ai-tooling",
        "chunks": [
            {
                "concept": "AI Ops Dashboard PRD · the showcase build spec",
                "summary": (
                    "PRD for a complete AI Opportunity Management Dashboard: tracks, evaluates, "
                    "prioritises AI automation opportunities. Single overnight Ralph Wiggum build. "
                    "Stack: React + Tailwind + Recharts as a single HTML file with no build step. "
                    "4 epics: Kanban board, ROI calculator, portfolio dashboard, priority matrix. "
                    "Data model: opportunity objects with title / description / department / status / "
                    "priority / ROI fields (hours/week, hourly rate, employees affected, "
                    "implementation cost) plus calculated savings + ROI. localStorage persistence."
                ),
                "usable_principle": (
                    "PRD pattern for single-file React showcase builds: define success criteria up "
                    "front, list epics with explicit completion conditions, define data model "
                    "before architecture, persist to localStorage, end with a promise-tag completion "
                    "signal. Bias to no build step for demo speed."
                ),
                "sniped_relevance": (
                    "Template for any SNIPED-internal tooling build. The data-model-first PRD "
                    "discipline maps to the SNIPED 100Q audit pattern of locking schema before "
                    "execution."
                ),
                "direct_quotes": [
                    "Single overnight Ralph Wiggum session",
                    "Self-contained dashboard ready to demo",
                ],
                "tags": ["ai-ops-dashboard", "prd", "ai-tooling", "ralph-wiggum", "react", "single-html"],
            },
            {
                "concept": "AI Ops Dashboard · ROI-calculator epic + opportunity-object schema",
                "summary": (
                    "Data model for the opportunity object: id (uuid), title, description, "
                    "department, status (identified / evaluating / approved / implementing / "
                    "complete), priority (low / medium / high), ROI fields (hoursPerWeek, hourlyRate, "
                    "employeesAffected, implementationCost), calculated fields (monthlySavings, "
                    "yearlySavings, roiPercentage). The ROI calculator pulls hours and rate inputs, "
                    "outputs monthly / yearly savings and ROI percentage against implementation cost."
                ),
                "usable_principle": (
                    "Any operator-engine tool that scores AI automation opportunities should use "
                    "this 5-status + 3-priority + ROI-percentage schema as the baseline. Tracks "
                    "the same vectors a SNIPED Lean Audit asks about."
                ),
                "sniped_relevance": (
                    "Direct schema for the SNIPED Lean Audit + Monday Cockpit · which AI opportunities "
                    "to push, which to park, which to kill. Maps the 9-factor founder-purchase logic "
                    "into AI-investment terms."
                ),
                "direct_quotes": [],
                "tags": ["ai-ops-dashboard", "roi-calculator", "schema", "ai-tooling", "lean-audit"],
            },
        ],
    },
    {
        "source_file": "intake__built_an_ai_saas_in_20_min.md",
        "source_title": "Built an AI SaaS in 20 min · Claude Code + n8n",
        "author": AUTHOR_EDGE,
        "domain": "ai-tooling",
        "chunks": [
            {
                "concept": "Claude Code + n8n · 20-minute AI SaaS pattern",
                "summary": (
                    "Build pattern: Claude Code generates the frontend (Astro / React) + n8n hosts "
                    "the AI workflow (webhook → LLM call → response). The 20-minute claim is for the "
                    "shell; data integrations and UX polish live downstream. Decoupling pattern: "
                    "the frontend never holds the API key; the n8n webhook proxies all LLM calls. "
                    "Two automation blueprints (content-strategy generator + ElevenLabs voice agent) "
                    "are direct examples of this pattern."
                ),
                "usable_principle": (
                    "When SNIPED needs to ship a new AI-powered tool fast, follow the pattern: "
                    "Claude Code for the frontend, n8n for the workflow, webhook between them. "
                    "Never expose API keys in the frontend. Treat the n8n graph as the contract."
                ),
                "sniped_relevance": (
                    "Operator engine extension pattern. The same pattern is used by the two "
                    "automation blueprints in this batch (AI Content Strategy Generator, ElevenLabs "
                    "voice agent). Anchors the SNIPED AI-tooling stance."
                ),
                "direct_quotes": [
                    "Claude Code + n8n",
                ],
                "tags": ["claude-code", "n8n", "ai-saas", "ai-tooling", "webhook", "decoupling"],
            },
            {
                "concept": "Claude Code + n8n · operator engine extension primitives",
                "summary": (
                    "Operator-engine extension primitives demonstrated by the 20-minute SaaS build: "
                    "(1) n8n as the durable workflow layer · trigger nodes, LLM nodes, response nodes, "
                    "persistence nodes; (2) Claude Code as the frontend / glue layer; "
                    "(3) the webhook contract as the API surface; (4) the system prompt as the "
                    "behavior contract."
                ),
                "usable_principle": (
                    "Treat n8n workflows as durable contracts; treat Claude Code output as "
                    "regeneratable scaffolding. The workflow is the IP; the frontend is the wrapper. "
                    "When the workflow changes, regenerate the frontend."
                ),
                "sniped_relevance": (
                    "Reinforces the SNIPED methodology-as-IP doctrine. The workflow is what BJ owns "
                    "forever (Section 2 of OPERATIONAL_BACKBONE); the frontend can be regenerated."
                ),
                "direct_quotes": [],
                "tags": ["claude-code", "n8n", "ai-saas", "ai-tooling", "methodology-as-ip"],
            },
        ],
    },
    {
        "source_file": "intake__remotion.md",
        "source_title": "Remotion · React-based video automation",
        "author": AUTHOR_EDGE,
        "domain": "automation-blueprint",
        "chunks": [
            {
                "concept": "Remotion · video automation primitive",
                "summary": (
                    "Remotion is a React-based video automation framework. Build videos as React "
                    "components, render to mp4 via the CLI. Use cases: programmatic chapter cards, "
                    "auto-generated video templates with dynamic data, Remotion + Claude Code for "
                    "vague-prompt-to-video pipelines."
                ),
                "usable_principle": (
                    "When SNIPED needs templated video output at scale (chapter cards, social "
                    "video templates, Cultural Doc lower-thirds), Remotion is the framework. "
                    "Compose video as React, render headless. Avoid manual Premiere passes for "
                    "templated work."
                ),
                "sniped_relevance": (
                    "Maps to the SNIPED video philosophy and the Attention Stack 7×7 cutdown workflow. "
                    "Remotion can templatize the cutdown."
                ),
                "direct_quotes": [],
                "tags": ["remotion", "video-automation", "react", "automation-blueprint", "claude-code"],
            },
        ],
    },
    {
        "source_file": "intake__automation_ai_content_strategy_generator.json",
        "source_title": "Automation · AI Content Strategy Generator (Lead Magnet)",
        "author": AUTHOR_EDGE,
        "domain": "automation-blueprint",
        "chunks": [
            {
                "concept": "n8n blueprint · 30-day content strategy generator",
                "summary": (
                    "n8n workflow: webhook POST /content-strategy → GPT-5.2 system prompt (expert "
                    "content strategist) → response in HTML with Strategy Overview, 30-day content "
                    "calendar (numbered list with day, title, description, content type), Optimal "
                    "Posting Times, Content Mix Strategy (educational / entertaining / promotional / "
                    "community), 5 Quick Wins. User template fills niche, content goals, posting "
                    "frequency, platforms. Lead-magnet shape: client gets a personalized strategy "
                    "in exchange for the input form."
                ),
                "usable_principle": (
                    "Pattern: webhook → LLM with detailed system prompt → structured HTML output. "
                    "System prompt does the heavy lifting; user template is a thin variable substitution. "
                    "Lead-magnet conversion lives in the perceived personalization."
                ),
                "sniped_relevance": (
                    "Directly executable lead-magnet pattern. Could be adapted for SNIPED to gate "
                    "a Direction Stack mini-diagnostic as a lead magnet. Pattern is portable to any "
                    "SNIPED capture surface."
                ),
                "direct_quotes": [
                    "You are an expert content strategist with years of experience helping creators and businesses grow their audience.",
                ],
                "tags": ["n8n", "automation-blueprint", "lead-magnet", "content-strategy", "webhook", "gpt"],
            },
        ],
    },
    {
        "source_file": "intake__automation_elevenlabs_voice_agent.json",
        "source_title": "Automation · ElevenLabs voice agent (lead qualification)",
        "author": AUTHOR_EDGE,
        "domain": "automation-blueprint",
        "chunks": [
            {
                "concept": "n8n blueprint · ElevenLabs voice agent that calls and qualifies leads",
                "summary": (
                    "n8n workflow: trigger → ElevenLabs conversational AI agent places outbound calls "
                    "→ structured qualification questions → captures call transcript and answers → "
                    "writes to CRM or sheet. Production pattern for outbound voice-based lead "
                    "qualification at scale."
                ),
                "usable_principle": (
                    "When SNIPED tests voice-based outbound (not currently in the two-channel doctrine "
                    "but a future option), this is the blueprint. Treat the agent persona as the "
                    "extension of operator voice · NOT a replacement for the operator's direct "
                    "presence in qualified conversations."
                ),
                "sniped_relevance": (
                    "Future-option blueprint. Currently OUT of scope per the locked two-channel "
                    "outbound doctrine (LinkedIn VIB + cold email). Documented here as a primitive "
                    "the operator engine can invoke if the doctrine changes."
                ),
                "direct_quotes": [],
                "tags": ["n8n", "elevenlabs", "voice-agent", "automation-blueprint", "lead-qualification"],
            },
        ],
    },
]


# ----- main -----

def main():
    # P1: SKILL_BUILD_QUEUE
    fp = EXTRACTED / "_skills__skill_build_queue.md"
    build_skill_build_queue_chunk(fp.read_text(encoding="utf-8"), fp.name)

    # P1: 50 SNIPED skills
    extra_chunk_slugs = {"sniped-caption-writer", "sniped-vib-outreach", "sniped-luxury-edit"}
    for slug in SNIPED_DOMAIN:
        fname = f"_skills__{slug.replace('-', '_')}.md"
        fp = EXTRACTED / fname
        if not fp.exists():
            print(f"WARN missing SNIPED skill: {fname}")
            continue
        text = fp.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        build_sniped_skill_chunk(slug, fm, body, fname, extra_chunk=(slug in extra_chunk_slugs))

    # P2: 50 Claude50 framework prompts
    for slug in CLAUDE50_DOMAIN:
        fname = f"claude50__{slug.replace('-', '_')}.md"
        fp = EXTRACTED / fname
        if not fp.exists():
            print(f"WARN missing Claude50: {fname}")
            continue
        text = fp.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        build_claude50_chunk(slug, fm, body, fname)

    # P3+P4: hand-authored supporting docs
    for doc in SUPPORTING_DOCS:
        for spec in doc["chunks"]:
            add_chunk(
                source_title=doc["source_title"],
                source_file=doc["source_file"],
                author=doc["author"],
                domain=spec.get("domain", doc["domain"]),
                concept=spec["concept"],
                summary=spec["summary"],
                usable_principle=spec["usable_principle"],
                sniped_relevance=spec["sniped_relevance"],
                direct_quotes=spec["direct_quotes"],
                tags=spec["tags"],
            )

    # Write JSONL
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"Wrote {len(chunks)} chunks to {OUT_JSONL}")

    # Em-dash sweep on output (Unicode U+2014, replaced with middle dot)
    em_char = chr(0x2014)
    text = OUT_JSONL.read_text(encoding="utf-8")
    em_count = text.count(em_char)
    if em_count:
        print(f"WARNING: {em_count} em-dashes in output. Sweeping.")
        text = text.replace(em_char, " · ")
        OUT_JSONL.write_text(text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
