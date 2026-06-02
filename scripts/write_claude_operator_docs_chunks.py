#!/usr/bin/env python3
"""
CLAUDE_OPERATOR_DOCS chunk writer · loose AI/Claude operator docs.
Schema: chunk_id, batch_id, source_title, source_file, author, domain, concept, summary,
        usable_principle, sniped_relevance, direct_quotes, tags. ID pattern CLAUDE_OPERATOR_DOCS_NNN.
Domains reused (all pre-existing · operator-approved): ai-tooling, operator-process, meta-doctrine,
strategy, client-application, automation-blueprint, prompt-engineering. NO new domain.
Copyright-safe SHORT illustrative quotes only. Em-dash swept. gumroad = light coverage (3).
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "CLAUDE_OPERATOR_DOCS_CHUNKS.jsonl"

C = []


def add(src, title, author, domain, concept, summary, usable, relevance, quotes, tags):
    C.append({"source_title": title, "source_file": src, "author": author, "domain": domain,
              "concept": concept, "summary": summary, "usable_principle": usable,
              "sniped_relevance": relevance, "direct_quotes": quotes, "tags": tags})


# ===================== Claude_Operating_Manual.docx (5) =====================
S = "claude_operating_manual.txt"; T = "The Claude Operating Manual"; A = "SNIPED (operator-authored · synthesized)"
add(S, T, A, "meta-doctrine", "AI superiority is context architecture, not prompting skill",
    "The manual's core thesis: the operator who spends time building a workspace with the right context files, skills, and command workflows beats the one writing clever prompts in a blank chat, every time. The lever is the environment you give the AI, not the wording of the request.",
    "Invest in context architecture (files, project knowledge, CLAUDE.md, skills) before investing in prompt wording; the environment is the durable advantage.",
    "Reframes SNIPED's whole AI practice: the moat is the configured workspace, not prompt cleverness, which is why the OS corpus and skills exist.",
    "AI superiority is not prompting skill. It's context architecture.",
    ["context-architecture", "claude-as-os", "operator-leverage", "meta-doctrine"])
add(S, T, A, "ai-tooling", "Claude is an operating system you configure, not a chatbot you ask",
    "The manual insists on a mental-model shift: stop treating Claude as a question-answer box and start treating it as an OS you set up to run your work. The difference between mediocre output and senior-team-member output is how much relevant context Claude has before you ask anything.",
    "Configure Claude as a standing work environment per domain rather than opening a fresh blank chat each time.",
    "Justifies SNIPED's investment in a persistent, configured Claude workspace over ad-hoc prompting.",
    "It's an operating system you configure to run your work.",
    ["claude-as-os", "mental-model", "configuration", "ai-tooling"])
add(S, T, A, "operator-process", "Workspaces are the unit of organization",
    "A workspace is a folder holding context files, skills, commands, and a CLAUDE.md that orients the AI to who you are, what you are working on, and how you want things done. One workspace per business, project, or domain.",
    "Organize AI work into one configured workspace per domain, each with its own CLAUDE.md and context set.",
    "Maps directly onto the AI-Brain-Refinery + SNIPED_OS structure: a workspace per domain with a CLAUDE.md is exactly how this corpus is run.",
    "Workspaces are the unit of organization.",
    ["workspace", "claude-md", "organization", "operator-process"])
add(S, T, A, "automation-blueprint", "Skills are reusable automation packages",
    "A skill is a markdown file of step-by-step instructions for a specific workflow, loaded on demand and invoked by name. Skills encode institutional knowledge so a workflow runs the same way every time without re-explaining it.",
    "Encode any repeated AI workflow as a named skill file so it runs consistently and compounds over time.",
    "This is precisely the SNIPED skills pattern (source-inventory, batch-extraction, jsonl-validation, etc.); the manual is the doctrine behind the corpus's own tooling.",
    "",
    ["skills", "reusable-automation", "institutional-knowledge", "automation-blueprint"])
add(S, T, A, "prompt-engineering", "The AI needs better information, not better instructions",
    "A simple prompt with deep context (uploaded files, project knowledge, CLAUDE.md) outperforms an elaborate prompt with no context. The bottleneck is information supplied, not instruction phrasing.",
    "When output is weak, add context before rewriting the prompt; supply the AI the information it is missing.",
    "Sharpens the boundary with PROMPT_TEMPLATES_DEEP: prompt craft matters, but context supply matters more; the two lanes are complementary, not competing.",
    "The AI doesn't need better instructions. It needs better information.",
    ["context-beats-prompting", "information-supply", "prompt-engineering"])

# ===================== The_Claude_Stack (1).docx (7) =====================
S = "the_claude_stack.txt"; T = "The Claude Stack (Stack series, Vol. V)"; A = "SNIPED (operator-authored)"
add(S, T, A, "strategy", "The operating layer that lets one person run all four Stacks at once",
    "The Claude Stack is the fifth volume beneath Direction, Production, Revenue, and Attention. The first four are craft systems that each demand daily practice; run by hand, one person runs out of hours by about month three. This volume is the leverage layer that makes running all four simultaneously possible.",
    "Treat the AI-leverage layer as the prerequisite that makes the rest of the operating system runnable by a solo operator, not an optional add-on.",
    "Names the structural role of AI in SNIPED: the leverage layer that lets one person operate a photography business at agency scale.",
    "It is the operating layer that makes all four possible to run at the same time by one person.",
    ["claude-stack", "leverage-layer", "solo-operator", "strategy"])
add(S, T, A, "strategy", "AI as force multiplier roughly doubles throughput",
    "The Stack frames AI not as a chatbot but as a force multiplier: every other volume produces at roughly twice the throughput once the Claude layer is in place. The gain is leverage on existing work, not new work.",
    "Measure the AI layer by the throughput it adds to existing systems, targeting a step-change (roughly 2x), not marginal speedups.",
    "Quantifies the SNIPED leverage thesis and sets the bar for whether an AI investment is worth it: it should roughly double a system's output.",
    "Every other volume produces at roughly twice the throughput once this one is in place.",
    ["force-multiplier", "throughput", "leverage", "strategy"])
add(S, T, A, "ai-tooling", "Projects and persistent context",
    "Part III covers projects as persistent-context containers: context that lives across sessions (project knowledge, uploaded references, standing instructions) so the AI does not start cold each time. Persistence is what turns a chat into an operating environment.",
    "Put recurring references and standing instructions into persistent project context so the AI carries them across every session.",
    "Backs SNIPED's continuity discipline (THE_SPINE, CANONICAL_TRUTHS, session saves): persistent context is how the operating system survives between sessions.",
    "",
    ["projects", "persistent-context", "continuity", "ai-tooling"])
add(S, T, A, "ai-tooling", "Claude Code in a terminal: workspace-based work",
    "Part V covers Claude Code as terminal-based, workspace-anchored work, with a `.claude/` directory holding agents and configuration. It is the build-and-execute surface that operates directly on the workspace's files.",
    "Use Claude Code for workspace-anchored build/execute work where the AI operates on real files, reserving chat for ideation.",
    "Connects to BATCH_006's Claude Code Superpowers chunks: the Stack is the operator-practice layer over those primitives.",
    "",
    ["claude-code", "terminal", "workspace", "ai-tooling"])
add(S, T, A, "automation-blueprint", "Skills are atoms, commands are molecules, and skills compound",
    "Skills are the reusable unit of automation; a photographer with twenty working skills has effectively built a team of specialists. The tenth skill takes fifteen minutes because skills are a vocabulary you teach the system once and reuse forever.",
    "Build a growing library of small named skills; the marginal cost falls and the compounding capability rises with each one.",
    "Validates the SNIPED skill-build queue: skills compound into a de-facto team, the highest-leverage form of operator IP.",
    "Skills are atoms. Commands are molecules.",
    ["skills", "commands", "compounding", "automation-blueprint"])
add(S, T, A, "operator-process", "Commands are one-liner automations on a file pattern",
    "Part VII covers commands: one-liner invocations (such as a weekly-report command) that run a defined automation on demand or on a schedule. Commands wrap multi-step work behind a single trigger.",
    "Wrap recurring multi-step operator tasks behind a single command so they run on a trigger instead of by hand.",
    "Maps to SNIPED's recurring operating cadence (weekly reports, MVMM loop): commands turn the cadence into one-trigger automations.",
    "",
    ["commands", "one-liner-automation", "cadence", "operator-process"])
add(S, T, A, "operator-process", "Sub-agents and agent teams: specialist delegation, hub-and-spoke",
    "Part VIII covers sub-agents: specialist agents each with their own prompt, tool access, and scope, reporting back to a parent in a hub-and-spoke pattern. Delegation solves output-quality and context-window problems by giving each task a focused specialist.",
    "Delegate distinct tasks to scoped sub-agents that report to a coordinating parent, rather than overloading one general context.",
    "Describes how SNIPED can run an outreach-writer, an editor, and a researcher as scoped sub-agents under one operator, mirroring the agency model.",
    "Sub-agents report back to the parent only. Hub-and-spoke.",
    ["sub-agents", "agent-teams", "delegation", "operator-process"])

# ===================== claude cowork genius.docx (4) =====================
S = "claude_cowork_genius.txt"; T = "Claude Cowork Genius (walkthrough)"; A = "SNIPED (operator-authored · transcript)"
add(S, T, A, "ai-tooling", "Claude desktop's three modes: chat, co-work, and code",
    "The walkthrough distinguishes Claude desktop's three tabs: chat (quick questions), co-work (autonomous real work without coding), and code (for developers). Most people live in chat and never use the surface built for actual work.",
    "Match the Claude surface to the job: chat for quick questions, co-work for autonomous multi-step work, code for builds.",
    "Helps SNIPED route work to the right Claude surface instead of defaulting every task to a blank chat.",
    "Three tabs: chat, co-work, and code.",
    ["claude-desktop", "co-work", "modes", "ai-tooling"])
add(S, T, A, "meta-doctrine", "Copy-pasting in chat is terrible for real work",
    "The core critique: living in chat mode (ask, copy the text, manually do something with it) is fine for quick questions but a poor fit for real work, because the human becomes the integration layer shuttling output by hand.",
    "Stop being the manual copy-paste integration layer; move multi-step work into a mode where the AI executes, not just answers.",
    "Reinforces SNIPED's leverage stance: the operator's time should not be spent shuttling AI output by hand.",
    "Fine for quick questions, terrible for real work.",
    ["anti-pattern", "copy-paste", "integration-layer", "meta-doctrine"])
add(S, T, A, "operator-process", "Co-work mode runs real work without technical skills",
    "Co-work mode lets a non-developer hand the AI a real task and have it work autonomously, sitting between chat (too manual) and code (needs technical skills). It is the practical surface for an operator who is not an engineer.",
    "Use co-work mode to delegate real multi-step tasks without writing code, reserving the code surface for genuine builds.",
    "Fits the SNIPED operator profile: high-leverage AI work without needing to be an engineer.",
    "",
    ["co-work", "no-code", "delegation", "operator-process"])
add(S, T, A, "ai-tooling", "Let the AI produce the artifact, not just describe it",
    "The walkthrough's payoff is having Claude produce the finished artifact (document, asset, output) directly rather than returning text the human then assembles. The unit of work shifts from answer to deliverable.",
    "Aim each AI task at a finished artifact, not a description the operator must still assemble.",
    "Aligns with SNIPED's deliverable focus: the AI should hand back the thing, not instructions for making the thing.",
    "",
    ["artifact-output", "deliverable", "leverage", "ai-tooling"])

# ===================== ai after ramon.docx (5) =====================
S = "ai_after_ramon.txt"; T = "AI After Ramon (founder walkthrough)"; A = "SNIPED (operator-authored · transcript)"
add(S, T, A, "strategy", "AI makes a business better, cheaper, faster, and less risky",
    "The founder frames every AI application against four axes: does it make the business better, cheaper, faster, or less risky for the customer? The frame keeps AI adoption tied to concrete business value rather than novelty.",
    "Screen every proposed AI use against better / cheaper / faster / less-risky before building it.",
    "A clean qualification frame SNIPED can put in front of clients, complementing the opportunity-hopper scoring.",
    "How we use AI to make our business better, cheaper, faster, and less risky for our customers.",
    ["four-axis-frame", "business-value", "ai-adoption", "strategy"])
add(S, T, A, "client-application", "Commoditized automations versus differentiated ones",
    "The founder separates commoditized automations (the things anyone can learn from YouTube) from the differentiated ones that require deep understanding of the specific business systems. The value sits in the differentiated work.",
    "Do not sell commoditized automations as premium work; compete on the differentiated automations that require understanding the client's specific systems.",
    "Backs SNIPED's process-mapping-as-IP stance: the defensible work is the business-specific automation, not the generic one.",
    "",
    ["commoditized-vs-differentiated", "moat", "process-understanding", "client-application"])
add(S, T, A, "client-application", "Drop AI into an existing, working sales process",
    "One example applies an AI setter to an already-good sales process: AI amplifies a working motion rather than replacing it. The precondition is that the underlying process already works.",
    "Apply AI to processes that already work, to amplify them; do not use AI to paper over a broken process.",
    "Reinforces the SNIPED + Human + Machine principle (reimagine, do not pave the cow path): fix the process first, then amplify with AI.",
    "",
    ["sales-motion", "amplify-not-replace", "working-process", "client-application"])
add(S, T, A, "strategy", "Use AI to take risk out of the business",
    "The least-discussed axis is risk: AI can reduce the risk in a business (consistency, coverage, reduced single-point-of-failure on staff) so an offer can be framed as risk-free to the customer. Risk reduction is itself a sellable outcome.",
    "Frame AI deliverables partly as risk reduction (consistency, coverage, resilience), not only as speed or cost.",
    "Adds a third sales axis to SNIPED's outcome framing beyond revenue and saved hours: de-risking the client's operation.",
    "",
    ["risk-reduction", "resilience", "outcome-framing", "strategy"])
add(S, T, A, "operator-process", "Automate the workflow you understand best first",
    "The founder's guidance: the person who best understands a workflow is best positioned to automate it, so start by automating one portion of your own day where you have the deepest understanding. Understanding precedes automation.",
    "Begin automation where your own understanding is deepest; map and automate one part of your day before scaling out.",
    "A concrete starting rule for SNIPED engagements and self-tooling: depth of understanding, not glamour, picks the first automation.",
    "",
    ["start-where-you-know", "workflow-automation", "sequencing", "operator-process"])

# ===================== using ai x gumroad x digital products.docx (3 · LIGHT) =====================
S = "using_ai_x_gumroad_digital_products.txt"; T = "Using AI x Gumroad x Digital Products"; A = "SNIPED (operator-authored)"
add(S, T, A, "strategy", "Decouple authoring from publishing to build a digital-asset library",
    "The doc frames AI-assisted publishing (Amazon KDP / print-on-demand) as decoupling authoring from publishing to build a high-margin, inventory-free library of informational products generating passive income.",
    "Treat informational products as a decoupled, inventory-free asset library where AI lowers the authoring cost.",
    "A monetization-surface reference for SNIPED's productized-IP thinking (the Direction Stack books, card systems), kept light here.",
    "By decoupling authoring from publishing, one can build a high-margin, scalable library of informational products.",
    ["digital-products", "decoupling", "passive-income", "strategy"])
add(S, T, A, "strategy", "Profit-first publishing: chase market demand, not creative expression",
    "The underlying strategy is profit-first: pick niches by market demand rather than creative preference, and use AI-assisted generation plus low-cost outsourcing to maximize volume and speed.",
    "When the goal is monetization, let validated market demand pick the niche; reserve creative expression for the brand work.",
    "A useful counter-frame SNIPED can hold consciously: the productized-IP lane is demand-led, distinct from the craft-led photography work.",
    "Focus on market demand (niches) rather than creative expression.",
    ["profit-first", "demand-led", "monetization", "strategy"])
add(S, T, A, "client-application", "Validate a niche against real competitor earnings before producing",
    "The operational layer validates a niche by researching high-ranking products and estimating competitor earnings before producing anything, so production follows evidence of demand.",
    "Validate demand with competitor-earnings evidence before producing a digital product, not after.",
    "Mirrors SNIPED's reality-check discipline (Finding Your Edge, opportunity readiness): evidence of paying demand precedes the build.",
    "",
    ["niche-validation", "demand-evidence", "pre-production", "client-application"])

# ===================== synthesis (2 · cite representative real files) =====================
add("claude_operating_manual.txt", "CLAUDE_OPERATOR_DOCS cross-source synthesis", "SNIPED synthesis", "meta-doctrine",
    "Context architecture is the meta-lever across every Claude-operator doc",
    "The Operating Manual, the Claude Stack, and the cowork walkthrough converge on one idea: the operator's job is to configure the environment (workspace, persistent context, skills, commands, sub-agents) so the AI arrives at any task already oriented. Prompting is downstream of context architecture.",
    "Spend operator time building the configured environment; the configured environment, not the prompt, is what compounds.",
    "Unifies this mini-batch into one SNIPED principle: architect the workspace, and the leverage follows across every engagement.",
    "",
    ["synthesis", "context-architecture", "meta-lever", "meta-doctrine"])
add("the_claude_stack.txt", "CLAUDE_OPERATOR_DOCS cross-source synthesis", "SNIPED synthesis", "strategy",
    "These docs are the practical HOW under BATCH_008's augmentation thesis",
    "Where BATCH_008's canon argues that human-plus-machine augmentation beats replacement, these operator docs show the concrete implementation: Claude configured as an OS, run as a force multiplier, with skills and sub-agents as the team. The canon supplies the why; the Claude Stack supplies the how.",
    "Pair the BATCH_008 augmentation principle with this mini-batch's concrete configuration moves when designing any client AI deliverable.",
    "Ties the loose Claude-operator docs to the AI/tech canon: the same hybrid-operator thesis, now at the level of daily practice.",
    "",
    ["synthesis", "augmentation-implementation", "force-multiplier", "strategy"])

# ---- emit ----
em = chr(0x2014)
lines = []
for i, ch in enumerate(C, start=1):
    lines.append({
        "chunk_id": f"CLAUDE_OPERATOR_DOCS_{i:03d}",
        "batch_id": "CLAUDE_OPERATOR_DOCS",
        "source_title": ch["source_title"],
        "source_file": ch["source_file"],
        "author": ch["author"],
        "domain": ch["domain"],
        "concept": ch["concept"],
        "summary": ch["summary"],
        "usable_principle": ch["usable_principle"],
        "sniped_relevance": ch["sniped_relevance"],
        "direct_quotes": ch["direct_quotes"],
        "tags": ch["tags"],
    })

swept = 0
for rec in lines:
    for k, v in rec.items():
        if isinstance(v, str) and em in v:
            rec[k] = v.replace(em, " · "); swept += 1
        elif isinstance(v, list):
            nl = []
            for item in v:
                if isinstance(item, str) and em in item:
                    nl.append(item.replace(em, " · ")); swept += 1
                else:
                    nl.append(item)
            rec[k] = nl

OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in lines) + "\n", encoding="utf-8")
print(f"Wrote {len(lines)} chunks to {OUT.name}")
print(f"Em-dashes swept: {swept}")
from collections import Counter
print("Domain distribution:", dict(sorted(Counter(r["domain"] for r in lines).items())))
print("Source distribution:")
for k, v in sorted(Counter(r["source_file"] for r in lines).items()):
    print(f"  {v:3d}  {k}")
