#!/usr/bin/env python3
"""
Write EDGE_AND_OPERATING_DISCIPLINE_CHUNKS.jsonl · 11 chunks (9 source + 2 synthesis) across 3 worksheets.
12-field canonical schema. NO new domain (5 approved existing domains only · personal-operating-code is
a mini-batch slug, NOT a domain, and is not used). Identity-optionality guardrail: sniped_relevance frames
everything as decision-support; the ICP worksheet is method only, never a finalized SNIPED ICP; no final
SNIPED / SNIPED Media / BASEPLATE direction. Em-dash sweep at the end.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "EDGE_AND_OPERATING_DISCIPLINE_CHUNKS.jsonl"

ICP = ("ICP Definition Worksheet", "icp_definition_worksheet.txt")
GOALS = ("Setting Goals", "setting_goals.txt")
WEEKLY = ("Weekly Reflections", "weekly_reflections.txt")
AUTHOR = "The AI Edge (course worksheet)"

DG = "Decision-support / operating-discipline only. This does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction; direction stays undecided and optionality is preserved."
ICP_GUARD = " The ICP worksheet is a METHOD, not a finalized SNIPED ICP; no specific ICP is decided here."

C = []
def add(src, domain, concept, summary, principle, relevance, quotes, tags):
    n = len(C) + 1
    title, sfile = src
    C.append({
        "chunk_id": f"EDGE_AND_OPERATING_DISCIPLINE_{n:03d}",
        "batch_id": "EDGE_AND_OPERATING_DISCIPLINE",
        "source_title": title,
        "source_file": sfile,
        "author": AUTHOR,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": principle,
        "sniped_relevance": relevance,
        "direct_quotes": quotes,
        "tags": tags,
    })

# ---------------- ICP Definition Worksheet · 3 ----------------
add(ICP, "strategy",
    "The four-component ICP framework: define exactly who and why",
    "A proper ideal-customer profile has four parts: firmographics (who they objectively are), the specific scenario (the situation creating urgency), the expensive problem (the costly thing you solve), and why you can reach them (your competitive advantage). Vague targeting ('small businesses') is a red flag; if you cannot name 10 specific companies that fit, the profile is too loose.",
    "Define a customer profile precisely across who, when, what-it-costs-them, and why-you-can-win, until you can name ten real companies that fit.",
    "A focus-and-clarity method for any future commercial direction: be specific about who you serve before acting. Used as a reusable lens." + ICP_GUARD + " " + DG,
    ["A well-defined ICP beats a vague one every time."],
    ["icp", "focus", "targeting", "clarity", "strategy"])

add(ICP, "operator-process",
    "Validate the expensive problem before committing",
    "The worksheet gates the 'expensive problem' through a cost calculation (direct labor + opportunity cost = total monthly/annual cost) and a 5-point validation: is it expensive enough, frequent enough, have they already tried to solve it, can you quantify the ROI, can you prove it works. You need at least 4 of 5 yes answers, otherwise find a more expensive or more frequent problem.",
    "Quantify the cost of the problem and require it to clear an expensive/frequent/already-being-paid-for bar before you build for it.",
    "A qualification-discipline process the operator can apply to any opportunity, independent of the eventual direction. " + DG,
    [],
    ["validation", "qualification", "expensive-problem", "operator-process", "icp"])

add(ICP, "operator-doctrine",
    "Reachability and the edge: only pursue what you can actually reach and want",
    "The fourth component asks why you can win: direct access (people you know by name), credibility/authority (have you done their job, can you speak their language), community access, and referral potential. The reachability checkpoint adds a deciding question: do you WANT to work with these people long-term. Access and genuine fit, not just market size, decide whether a target is worth pursuing.",
    "Choose targets where you have a real reach advantage and genuine long-term interest, not just a large addressable market.",
    "A self-honest focus doctrine: build on the operator's actual edge and energy. A lens for the upcoming direction decision, not a verdict on it. " + DG,
    [],
    ["reachability", "edge", "advantage", "fit", "operator-doctrine"])

# ---------------- Setting Goals · 3 ----------------
add(GOALS, "operator-process",
    "SMART goals, capped at three per quarter",
    "Goals should be Specific, Measurable, Achievable, Realistic, and Time-bound, and capped at three per quarter because more than three splits focus and lowers the odds of finishing any. Vague ('grow my business') and over-ambitious ('1,000 customers in a month') goals both lead to frustration and burnout.",
    "Write at most three SMART goals per quarter; a realistic goal you finish beats an ambitious one you miss.",
    "A goal-setting discipline for energy allocation and focus under limited hours, applied without committing to any particular goal content. " + DG,
    ["A realistic goal you achieve beats an ambitious goal you miss every time."],
    ["smart-goals", "focus", "three-goals", "energy-allocation", "operator-process"])

add(GOALS, "strategy",
    "Goal hierarchy: cascade vision down to this week's actions",
    "Break the 12-month vision into quarterly milestones, then monthly objectives, then this week's specific tasks, so every action traces up to the vision. The connection checkpoint enforces it: if a task does not connect to the bigger goals, do not do it.",
    "Cascade long-term vision into weekly tasks and refuse work that does not trace back up the hierarchy.",
    "A prioritisation lens for spending scarce operator hours on what compounds toward the larger aim, whatever that aim turns out to be. " + DG,
    ["If a task doesn't connect to your bigger goals, don't do it."],
    ["goal-hierarchy", "prioritisation", "cascade", "focus", "strategy"])

add(GOALS, "operator-doctrine",
    "Reality-test goals and build the weekly reflection habit",
    "Each goal is reality-tested with a three-scenario plan (best / realistic / worst), validation questions (do I have the skills, who has done this, what is working in my favour), and a red-flags check (no buffer time, assuming 100 percent productivity, ignoring the learning curve). The framework's keystone is the weekly reflection habit said to separate successful founders from everyone else, with Friday blocked for it.",
    "Pressure-test goals against realistic and worst cases, watch for over-optimism red flags, and protect a fixed weekly reflection slot.",
    "A strategic-patience and judgment doctrine: ground ambitions in reality and institutionalise reflection, supporting the operator's upcoming decisions without pre-making them. " + DG,
    ["build the reflection habit that separates successful founders from everyone else"],
    ["reality-testing", "strategic-patience", "reflection-habit", "judgment", "operator-doctrine"])

# ---------------- Weekly Reflections · 3 ----------------
add(WEEKLY, "operator-process",
    "The weekly review: score, wins, honest reality check, patterns",
    "The weekly review opens with a five-dimension score (progress, energy and focus, learning, action-vs-planning, satisfaction), then specific wins and why they worked, then an unflinching reality check of what fell short and why, then the patterns: are you making the same mistakes or getting stuck in the same places. The emphasis is on what you did, not what happened to you.",
    "Run a fixed weekly review that scores the week, names wins and failures honestly, and surfaces repeating patterns.",
    "A review-cadence process that turns weeks into feedback, applicable to any direction the operator runs. " + DG,
    [],
    ["weekly-review", "reflection", "patterns", "honesty", "operator-process"])

add(WEEKLY, "operator-doctrine",
    "Energy and time audit: where the 168 hours actually went",
    "The audit accounts for the week's 168 hours across revenue-generating activity, learning, networking, admin, and time wasted or unfocused, and separately names what drained energy versus what gave it. It treats attention and energy as the scarce resources to allocate deliberately, not just clock time.",
    "Audit where time and energy actually went each week and reallocate toward what generates value and energises you.",
    "An energy-allocation and standards doctrine for a solo operator with limited hours; a lens, not a prescription for any specific allocation. " + DG,
    [],
    ["energy-audit", "time-audit", "attention", "standards", "operator-doctrine"])

add(WEEKLY, "systems-thinking",
    "The reflection-to-adjustment loop: insights become next week's focus",
    "The review closes a loop: insights (about the market and about yourself) and an accountability check (did you do what you said) feed next week's focus, stop/start lists, and a single highest-impact 'one thing'. A red-flags scan catches avoidance, busy work, planning instead of doing, and decisions made from fear. The point is not perfection but staying honest so you keep moving instead of spinning your wheels.",
    "Convert each week's honest insights into a concrete next-week focus and one highest-impact action, closing a self-correcting loop.",
    "A self-correcting operating loop the operator can run regardless of direction; it compounds judgment over reps. " + DG,
    ["stay honest about what's working and what isn't"],
    ["feedback-loop", "adjustment", "one-thing", "self-correction", "systems-thinking"])

# ---------------- Synthesis · 2 ----------------
add(WEEKLY, "meta-doctrine",
    "SYNTHESIS: the operating-discipline loop (focus to goals to reflection to adjust)",
    "The three worksheets form one loop: define focus (the ICP method), set a small number of cascaded SMART goals, run a weekly reflection that scores progress and audits energy, and adjust next week from what you learned. Run repeatedly, the loop compounds skill and judgment and is the executional engine beneath any strategy.",
    "Operate a repeating loop of focus, small goals, weekly reflection, and adjustment so judgment and skill compound over reps.",
    "The operating-discipline backbone for the operator. It is the practice layer that executes whatever direction is eventually chosen, supplied as decision-support. " + DG,
    [],
    ["synthesis", "operating-discipline", "compounding", "loop", "meta-doctrine"])

add(ICP, "meta-doctrine",
    "SYNTHESIS: load the backend and stay revisable before committing to identity",
    "The worksheets are explicit that the ICP will evolve and that the goal is not perfection on day one but being specific enough to test and learn. Read against the corpus's identity-and-brand optionality guardrails, the discipline is to load the backend (build the reflection and judgment habit, gather real signal) and keep targets revisable, rather than prematurely locking an identity, niche, or brand.",
    "Commit to the discipline of testing and reflecting, not to a fixed identity or niche; keep targeting revisable until the backend is loaded.",
    "Directly reinforces the active identity-optionality guardrails: build the habit, keep choices reversible, and do NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction before the backend is loaded." + ICP_GUARD,
    ["Your ICP will evolve. That's normal."],
    ["optionality", "revisable", "backend-loading", "meta-doctrine", "guardrail"])

# ---------------- write + em-dash sweep ----------------
EM = chr(0x2014)
def sweep(o):
    if isinstance(o, str):
        return o.replace(EM, " · ")
    if isinstance(o, list):
        return [sweep(x) for x in o]
    if isinstance(o, dict):
        return {k: sweep(v) for k, v in o.items()}
    return o

C = [sweep(c) for c in C]
with OUT.open("w", encoding="utf-8") as f:
    for c in C:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

from collections import Counter
dist = Counter(c["domain"] for c in C)
print(f"wrote {len(C)} chunks to {OUT}")
print("domains:", dict(sorted(dist.items(), key=lambda x: -x[1])))
print("em-dashes in output:", sum(json.dumps(c, ensure_ascii=False).count(EM) for c in C))
