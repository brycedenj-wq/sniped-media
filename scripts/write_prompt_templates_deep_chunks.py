#!/usr/bin/env python3
"""
PROMPT_TEMPLATES_DEEP chunker · 6 unique AI-Edge prompt-template PDFs

Reads the 6 normalized extracted txt files and emits PROMPT_TEMPLATES_DEEP_CHUNKS.jsonl
with the canonical 12-field schema.

Target: 12 chunks (range 10-15 per plan section 4).
Domains per plan section 5 (all pre-existing · no NEW domain):
  prompt-engineering (bulk · 11) + ai-tooling (1 · the prompt-writing-agent / N8N bridge).
operator-process / automation-blueprint available only as secondary tags.

Dedupe: 1 chunk per unique technique · the 2 md5-duplicate PDFs contributed 0 chunks (not extracted).
6 unique source_files referenced.

Em-dash sweep (Unicode U+2014) applied to output.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "PROMPT_TEMPLATES_DEEP_CHUNKS.jsonl"

BATCH_ID = "PROMPT_TEMPLATES_DEEP"
AUTHOR = "The AI Edge (prompt-technique templates)"
BASE_TAGS = ["prompt-engineering", "prompt-template", "the-ai-edge", "2026-05-19", "ai-tooling-aging-risk"]

F_IC = "prompt_template_in_context.txt"
F_TG = "prompt_template_thought_generation.txt"
F_PD = "prompt_template_problem_decomposition.txt"
F_SCB = "prompt_template_self_criticism_basic.txt"
F_SCA = "prompt_template_self_criticism_advanced.txt"
F_CT = "prompt_template_combining_techniques.txt"

chunks = []


def add(num, source_title, source_file, domain, concept, summary, principle, relevance, quotes, tags):
    chunks.append({
        "chunk_id": f"{BATCH_ID}_{num:03d}",
        "batch_id": BATCH_ID,
        "source_title": source_title,
        "source_file": source_file,
        "author": AUTHOR,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": principle,
        "sniped_relevance": relevance,
        "direct_quotes": quotes,
        "tags": BASE_TAGS + tags,
    })


PT = "Prompt Template · {} · The AI Edge"
SYN = "Prompt Templates Deep · cross-template pattern"

# ===========================================================================
# PER-TECHNIQUE (6)
# ===========================================================================

add(1, PT.format("In-Context Learning"), F_IC, "prompt-engineering",
    "In-context learning · few-shot prompting · show examples, then ask",
    ("The few-shot pattern: before asking the model to produce output, give it 2-3 worked examples of "
     "the desired format/tone, then pose the actual task. The template shows it across content creation "
     "(example social posts -> write a new one), customer service (example polite responses -> handle a "
     "new complaint), data analysis (example summaries -> summarise a new dataset), and education "
     "(example lesson-plan formats -> build a new one). The examples carry the format and voice the model "
     "should imitate, so the instruction stays short."),
    ("When output format or tone matters, lead with 2-3 concrete examples of exactly what good looks "
     "like, then state the new task. Examples teach format faster and cheaper than describing it. Keep "
     "the examples representative of the variety you want, not just one case."),
    ("The cheapest quality lever for any SNIPED AI surface · captions, DMs, client deliverables · feed "
     "the model the SNIPED voice via examples rather than long instructions. Pairs with the BATCH_006 "
     "prompt-engineering packs and the carousel-attribution discipline (examples make voice consistent)."),
    ["Here are examples of polite responses: ... Now, write a response to a customer complaining about late delivery.",
     "Here are examples of summaries: ... Now, summarise the following data and highlight one key trend."],
    ["few-shot", "in-context-learning", "examples-then-ask", "format-transfer", "voice-consistency"])

add(2, PT.format("Thought Generation"), F_TG, "prompt-engineering",
    "Thought generation · Chain-of-Thought (CoT) + Thread-of-Thought (ThoT) reasoning scaffolds",
    ("Two reasoning scaffolds. Chain-of-Thought (CoT) asks the model to reason step by step toward an "
     "answer (calculate total cost, compare, decide; or identify audience, pick selling points, choose "
     "channels, write a tagline). Thread-of-Thought (ThoT) structures the reasoning into explicitly "
     "numbered Step 1/Step 2/Step 3/Step 4 stages (identify the problem, propose short-term fixes, "
     "propose a long-term strategy, evaluate feasibility). Both force the model to externalise "
     "intermediate reasoning rather than jump to an answer."),
    ("For any task with reasoning or multiple dependent decisions, instruct the model to think step by "
     "step (CoT) or to work through explicit numbered stages (ThoT). Externalised intermediate steps "
     "raise answer quality and make the output auditable. Use ThoT when the stages are known in advance, "
     "CoT when the path is open."),
    ("The reasoning-scaffold backbone for SNIPED AI-assisted analysis and planning · step-by-step output "
     "is auditable (a SNIPED operating value · gate the non-deterministic). The N8N deep-reasoning "
     "sub-agent produces exactly this kind of staged output."),
    ["Break down your reasoning step by step: 1. Calculate the total cost of the items. 2. Compare the total cost with the amount John has. 3. Determine if John can afford all the items.",
     "Step 1: Identify the main problem. Step 2: Suggest two short-term solutions. Step 3: Propose one long-term strategy. Step 4: Evaluate the feasibility of each solution and recommend the best approach."],
    ["chain-of-thought", "cot", "thread-of-thought", "thot", "reasoning-scaffold", "step-by-step"])

add(3, PT.format("Problem Decomposition"), F_PD, "prompt-engineering",
    "Problem decomposition · Least-to-Most (LtM) + Plan-and-Solve (PaS) + Plan-of-Thought (PoTh)",
    ("Three decomposition techniques for complex tasks. Least-to-Most (LtM) starts with the simplest "
     "sub-tasks and builds to the complex (identify steps, reduce time per step, recommend tools, build "
     "the optimised workflow). Plan-and-Solve (PaS) splits the prompt into an explicit 'Plan first' phase "
     "then a 'Then execute' phase (plan: determine costs, identify revenue, consider risks; execute: "
     "build the budget, secure funding). Plan-of-Thought (PoTh) follows a fixed structured-step template "
     "(define market, identify selling points, build a timeline, propose strategies). All break one big "
     "ask into ordered, smaller asks."),
    ("Decompose a complex task before asking the model to solve it: order sub-tasks simplest-first (LtM), "
     "or separate planning from execution explicitly (PaS), or follow a fixed structured-step template "
     "(PoTh). Decomposition prevents the model from skipping steps and makes each part checkable."),
    ("The structuring discipline behind any SNIPED AI workflow that tackles multi-part deliverables · "
     "maps to the OPPORTUNITY_MANAGEMENT_TEMPLATES intake (break a problem into scored sub-steps) and the "
     "N8N model-tier sub-workflows. PaS (plan-then-execute) mirrors the SNIPED Saturday-build / Monday-"
     "cockpit plan-before-act cadence (B7)."),
    ["Plan first: 1. Categorise feedback into three groups... Then execute: 1. Summarise the feedback analysis. 2. Suggest two specific improvements for the business.",
     "Start with the simplest tasks and move to the more complex: 1. Identify the steps... 4. Create a new, optimised workflow for the team."],
    ["problem-decomposition", "least-to-most", "ltm", "plan-and-solve", "pas", "plan-of-thought", "poth"])

add(4, PT.format("Self-Criticism (Basic)"), F_SCB, "prompt-engineering",
    "Self-criticism (basic) · Self-Evaluation (SE) + Self-Refine (SR) + Chain-of-Verification (COVE)",
    ("Three first-pass self-correction techniques applied to output the model just produced. "
     "Self-Evaluation (SE) asks the model to review and grade its own draft against criteria (does it "
     "define the audience? are channels appropriate? suggest two improvements). Self-Refine (SR) asks it "
     "to rewrite for a specific improvement (more persuasive, add concrete benefits, simplify jargon). "
     "Chain-of-Verification (COVE) asks it to cross-check the draft against the source for accuracy "
     "(ensure metrics match, no achievements missing, align tone). All run AFTER a first draft exists."),
    ("Never ship a model's first draft. Add a second pass that evaluates against explicit criteria (SE), "
     "refines for a named improvement (SR), or verifies against the source data (COVE). The self-critique "
     "pass catches the errors the first pass introduces and is nearly free to add."),
    ("The output-quality guardrail layer · the prompt-craft form of the SNIPED final-review un-delegate-"
     "able (B7) and executing-with-care discipline. COVE (verify against source) is the prompt analog of "
     "fact-checking a deliverable before it goes to a client."),
    ["Review the product launch plan you just created and evaluate: 1. Does it clearly define the target audience? ... 3. Suggest two ways to make the plan more impactful.",
     "Cross-check the summary you wrote for accuracy by: 1. Ensuring all key metrics match the data provided. 2. Confirming that no major achievements or challenges are missing."],
    ["self-criticism", "self-evaluation", "se", "self-refine", "sr", "chain-of-verification", "cove", "prompt-guardrail"])

add(5, PT.format("Self-Criticism (Advanced)"), F_SCA, "prompt-engineering",
    "Self-criticism (advanced) · System-2-Attention (S2A) + Rephrase-and-Respond (RaR) + Re-reading (RE2)",
    ("Three advanced self-correction techniques. System-2-Attention (S2A) instructs deliberate, careful "
     "consideration of all relevant aspects before answering (carefully consider all aspects of "
     "retention... then list strategies with reasoning; or think deeply about benefits/audience/edge "
     "before generating taglines). Rephrase-and-Respond (RaR) asks the model to rephrase its output to "
     "hit specific qualities (clear, engaging, on-brand). Re-reading (RE2) asks it to re-read and confirm "
     "completeness and accuracy against the source. These deepen the self-critique beyond the basic pass."),
    ("For high-stakes output, force deliberate processing: instruct the model to consider all aspects "
     "carefully before answering (S2A), to rephrase toward named qualities (RaR), or to re-read and "
     "confirm against the source (RE2). Slower, more deliberate prompting buys higher-quality output "
     "where it matters."),
    ("The premium-tier output discipline · S2A (deliberate consideration) is the prompt analog of the "
     "SNIPED restraint-over-volume + measure-twice-cut-once posture. Pairs with the N8N deep-reasoning "
     "model-tier (reserve the slow, careful path for tasks that warrant it)."),
    ["Carefully consider all aspects of customer retention, including loyalty programmes, personalised communication, and pricing strategies.",
     "Re-read your summary and confirm: 1. All major achievements and challenges are included. 2. Key metrics... are accurately represented. 3. The summary aligns with the original data."],
    ["self-criticism", "system-2-attention", "s2a", "rephrase-and-respond", "rar", "re-reading", "re2", "deliberate-prompting"])

add(6, PT.format("Combining Techniques"), F_CT, "prompt-engineering",
    "Combining techniques · chaining CoT + Problem Decomposition + Self-Criticism in one prompt",
    ("The capstone pattern: stack multiple techniques in a single numbered prompt. The template chains "
     "(1) Chain-of-Thought to outline a plan step by step, (2) Problem Decomposition to break one section "
     "into sub-parts, and (3) Self-Criticism to review and refine the whole. Applied to a marketing plan, "
     "a feedback-improvement plan, a training programme, an expansion strategy, and a sales analysis. "
     "Order matters: generate with CoT, structure with decomposition, then quality-gate with "
     "self-criticism."),
    ("Compose a high-quality prompt by chaining techniques in sequence: reason it out (CoT), break the "
     "hard part down (decomposition), then self-critique the result (verification/refine). One prompt "
     "that generates, structures, and checks beats three disconnected asks. The self-criticism step is "
     "always last · it is the gate."),
    ("The full prompt-engineering stack · this IS what a SNIPED prompt-writing agent should output, and "
     "exactly what the N8N Cluster B Master Prompt Agent + deep-reasoning sub-agent assemble. The "
     "generate -> structure -> verify chain mirrors the SNIPED build -> structure -> final-review flow."),
    ["1. CoT: 'Outline the marketing plan step by step...' 2. Problem Decomposition: 'Focus on the Key Messaging section. Break it down into three main points...' 3. Self-Criticism: 'Review the entire plan to ensure it aligns with the product's goals...'",
     "3. Self-Criticism: 'Cross-check the improvement plan against the feedback data. Ensure all major issues have been addressed and propose refinements if necessary.'"],
    ["combining-techniques", "technique-chaining", "cot", "problem-decomposition", "self-criticism", "prompt-stack"])

# ===========================================================================
# CROSS-CUTTING SYNTHESIS (6)
# ===========================================================================

add(7, SYN, F_CT, "prompt-engineering",
    "The prompt-technique taxonomy · the full abbreviation map as a reference index",
    ("A single index of the prompt techniques across the templates: Few-Shot (in-context examples), CoT "
     "(Chain of Thought) + ThoT (Thread of Thought) for reasoning, LtM (Least-to-Most) + PaS "
     "(Plan-and-Solve) + PoTh (Plan-of-Thought) for decomposition, SE (Self-Evaluation) + SR "
     "(Self-Refine) + COVE (Chain-of-Verification) for basic self-criticism, and S2A (System-2-Attention) "
     "+ RaR (Rephrase-and-Respond) + RE2 (Re-reading) for advanced self-criticism. The families group "
     "into four jobs: teach format, reason, decompose, self-correct."),
    ("Keep a named taxonomy of prompt techniques and select by job: teach format (few-shot), reason "
     "(CoT/ThoT), decompose (LtM/PaS/PoTh), self-correct (SE/SR/COVE/S2A/RaR/RE2). Naming the technique "
     "makes prompt design a deliberate selection rather than improvisation."),
    ("The reference index for any SNIPED prompt-engineering work · a lookup table the operator (or a "
     "prompt-writing agent) consults to pick the right technique per task. Extends the BATCH_006 "
     "prompt-engineering domain with a technique-level vocabulary."),
    ["Few-Shot; CoT; ThoT; LtM; PaS; PoTh; SE; SR; COVE; S2A; RaR; RE2",
     "four jobs: teach format, reason, decompose, self-correct"],
    ["technique-taxonomy", "reference-index", "prompt-vocabulary", "technique-selection"])

add(8, SYN, F_IC, "prompt-engineering",
    "The Task + structured-Prompt scaffold · the common reusable shape across every template",
    ("Every template shares one shape: name the Task in one line (what to produce), then write a Prompt "
     "as a numbered, structured instruction that applies a technique. The Task frames intent; the "
     "numbered Prompt enforces structure and completeness. This Task + structured-Prompt pairing is the "
     "reusable container that all the techniques plug into."),
    ("Write every reusable prompt as Task (one-line intent) + Prompt (numbered, structured steps). The "
     "numbering forces the model to address each requirement and makes the output checkable item by item. "
     "Standardising the container makes a library of prompts comparable and composable."),
    ("The template-standard for a SNIPED prompt library · mirrors the OPPORTUNITY_MANAGEMENT_TEMPLATES "
     "one-page-card discipline (a standard container makes a portfolio comparable) and the SNIPED brief "
     "format (B7). A consistent prompt scaffold is what lets a prompt-writing agent mass-produce quality."),
    ["Task: Write a social media post for a tech company about AI trends.",
     "the Task frames intent; the numbered Prompt enforces structure and completeness"],
    ["task-prompt-scaffold", "prompt-structure", "reusable-template", "numbered-instruction"])

add(9, SYN, F_SCA, "prompt-engineering",
    "Self-criticism as a guardrail layer · the verify-before-ship pass across basic and advanced",
    ("Across both self-criticism templates, the durable principle is a mandatory second pass that gates "
     "output before it ships: evaluate against criteria (SE), refine for a named quality (SR/RaR), or "
     "verify against the source (COVE/RE2), with S2A adding deliberate up-front consideration. "
     "Self-criticism is not a technique among equals · it is the guardrail that turns probabilistic "
     "first-draft output into dependable output, and in the combining-techniques template it is always "
     "the final step."),
    ("Treat self-criticism as a required gate, not an optional polish. Every prompt that produces "
     "client-facing or decision-bearing output should end with a verify/refine pass against explicit "
     "criteria or the source data. The gate is cheap; shipping an unchecked first draft is expensive."),
    ("The prompt-craft embodiment of the SNIPED final-review un-delegate-able (B7) and the "
     "executing-with-care principle · gate the non-deterministic before it reaches a client. The N8N "
     "structured-output parser is the automated cousin of this manual gate."),
    ["Review the entire plan to ensure it aligns with the product's goals and resonates with the target audience. Suggest improvements if needed.",
     "Cross-check the insights against the raw sales data to ensure accuracy and completeness."],
    ["self-criticism", "prompt-guardrail", "verify-before-ship", "final-review", "quality-gate"])

add(10, SYN, F_TG, "prompt-engineering",
    "The reasoning-scaffold family · when to use step-by-step vs plan-first vs least-to-most",
    ("CoT, ThoT, LtM, PaS, and PoTh are one family of ordering scaffolds, differentiated by when the "
     "structure is known. Use CoT when the reasoning path is open and you want the model to work it out "
     "step by step; ThoT/PoTh when the stages are known and fixed; LtM when complexity should build from "
     "simplest to hardest; PaS when planning should be explicitly separated from execution. The choice is "
     "about how much structure the task's shape can supply up front."),
    ("Match the reasoning scaffold to the task's shape: open path -> CoT; known stages -> ThoT/PoTh; "
     "build-up complexity -> LtM; plan-then-do -> PaS. They are not interchangeable; picking the right "
     "one is most of the prompt-design decision for any multi-step task."),
    ("A decision rule for SNIPED AI-assisted multi-step work · the same plan-before-act / right-structure-"
     "for-the-task instinct the operator engine uses. The N8N model-selector chain makes an analogous "
     "choice (which model) that this makes for structure (which scaffold)."),
    ["Step by step, build a marketing strategy (LtM); Plan first... Then execute (PaS); Follow these structured steps (PoTh)",
     "Break down your reasoning step by step (CoT)"],
    ["reasoning-scaffold", "scaffold-selection", "cot", "pas", "ltm", "decision-rule"])

add(11, SYN, F_CT, "ai-tooling",
    "Prompt-writing-agent substrate · the content the N8N Prompt Engineer Agent produces and consumes",
    ("These templates are the prompt-craft CONTENT layer for the N8N_AUTOMATION_SYSTEMS Cluster B "
     "Prompt Engineer Agent: the Master Prompt Agent routes a request to a deep-reasoning or normal "
     "model-tier sub-workflow that PRODUCES a structured prompt · and the structured prompt it should "
     "produce is exactly one of these (or a combining-techniques chain). The technique taxonomy is the "
     "agent's toolbox; the Task+Prompt scaffold is its output format; self-criticism is its built-in "
     "quality gate."),
    ("Encode a prompt-writing capability as: a technique taxonomy (the toolbox) + a Task+Prompt scaffold "
     "(the output format) + a mandatory self-criticism gate (the quality check). An agent with those "
     "three can mass-produce reliable prompts. The craft and the automation are two halves · the templates "
     "are the craft, the n8n workflow is the engine."),
    ("Closes the prompt loop in the corpus: PROMPT_TEMPLATES_DEEP is the CRAFT, N8N_AUTOMATION_SYSTEMS "
     "Cluster B is the IMPLEMENTATION. Together they let SNIPED stand up a prompt-engineering agent whose "
     "output quality is governed by named techniques + a self-criticism gate. Cross-references "
     "N8N_AUTOMATION_SYSTEMS chunks 003-005, 010."),
    ["the Master Prompt Agent routes to deep-reasoning vs normal model-tier sub-workflows that develop the best prompts",
     "1. CoT ... 2. Problem Decomposition ... 3. Self-Criticism (the structured output a prompt-writing agent assembles)"],
    ["prompt-writing-agent", "n8n-bridge", "ai-tooling", "agent-substrate", "craft-vs-implementation"])

add(12, SYN, F_IC, "prompt-engineering",
    "Few-shot vs zero-shot economics · in-context examples as the cheapest quality lever",
    ("Few-shot prompting (a handful of examples in the prompt) is the lowest-effort, lowest-cost way to "
     "raise output quality: it transfers format, tone, and standard without fine-tuning, extra tooling, "
     "or long instructions. Across the templates, the in-context examples do the heavy lifting that would "
     "otherwise require verbose rules. The trade is a slightly longer prompt for a large quality gain."),
    ("Reach for few-shot examples before reaching for longer instructions, fine-tuning, or more complex "
     "tooling. A few representative examples are the cheapest, fastest quality lever available, and they "
     "make the output's voice and format predictable. Spend the prompt budget on examples, not adjectives."),
    ("The leverage move for SNIPED AI output (intel_leverage_logic · cheapest input for the biggest "
     "quality gain) · a few SNIPED-voice examples beat paragraphs of voice description. The economical "
     "default before escalating to deep-reasoning model tiers or bespoke tooling."),
    ["Here are examples of posts: ... Now, write a post highlighting how AI improves decision-making in business.",
     "examples carry the format and voice the model should imitate, so the instruction stays short"],
    ["few-shot", "zero-shot", "prompt-economics", "cheapest-quality-lever", "leverage"])


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
        OUT_JSONL.write_text(text.replace(em_char, " · "), encoding="utf-8")
    else:
        print("No em-dashes in output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
