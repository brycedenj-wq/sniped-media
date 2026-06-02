# COMMAND_CENTER_RESPONSE_PROTOCOL

**Date:** 2026-05-27
**Status:** Standing operating protocol for all future serious Command Center work. NOT a permanent identity lock. Anchor-class: markdown-only, not chunked, not a chunk source, not in the master files. This protocol governs how Claude answers, builds, and decides. It sits above individual tasks.
**Why this exists:** the recurring failure mode is Claude answering from narrow context, BJ then reminding Claude the OS holds deeper resources, then Claude auditing and finding the better answer late. That failure mode ends here.

---

## 1. Operating contract
- The OS is the **default brain**, not optional reference. The 1,837-chunk corpus, the Command Center, the memory doctrines, the tool/skill resources, the EYL/leisure-transfer material, and BJ's lived constraints are the working substrate of every serious answer.
- Every serious answer must **route through the OS by job** before it is given.
- BJ should **never** have to remind Claude to use the books, docs, interviews, tools, or skills. If BJ has to say "it is in the docs," the protocol failed.
- A generic answer is a **failure** when relevant OS material exists. Speed never trades against using the edge.

## 2. What counts as a serious task
Business strategy · naming/domain/brand · site/app/build work · offer/copy/content · distribution/outreach · sales/pricing · automation/n8n/API/tools · skill activation · personal operating system (body/work/money) · legal/IP/employment risk · proof-log decisions · and **any decision tied to money, proof, leverage, identity, or long-term architecture.** When in doubt, it is serious.

## 3. Mandatory OS-routing receipt
Every serious answer states, briefly:
- **Task category**
- **Current source-of-truth docs used** (the live Command Center docs that govern this job)
- **Corpus lanes activated** (which knowledge domains / intel memories)
- **Tools / skills / GitHub / resources checked or intentionally skipped**
- **Relevant lived-context constraints** (debt, hours, employment boundary, proof stage)
- **Proof-loop connection** (how this moves PROOF_LOOPS_30_60_90)
- **Guardrails applied**
- **What was NOT consulted and why**

## 4. Depth levels
- **Level 0:** casual answer, no OS routing required (chit-chat, trivial lookups).
- **Level 1:** quick tactical answer, use current Command Center state only.
- **Level 2:** serious decision, route through OS_TRANSFORMATION_ROUTER and the job-specific docs.
- **Level 3:** build / commit / deploy, route through OS + verifications + the relevant skills.
- **Level 4:** thesis / naming / domain / billion-dollar decisions, route through the full OS, run /challenge, and optionally /boardroom.

## 5. Default behavior by level
- Claude **classifies the level before answering** and names it in the receipt.
- At **Level 2 or higher, Claude must not answer from narrow context.** It routes first.
- **If uncertain about the level, escalate one level.** Over-routing is cheaper than the reminder-then-audit failure.

## 6. Required skill triggers
- **/challenge** before any major deployment, naming, domain, thesis, or irreversible decision.
- **/boardroom** for high-stakes strategic forks (multiple defensible options, real money or identity at stake).
- **/save** after any major new insight, correction, or resolved gate.
- **OS_NAME_FOUNDRY (or equivalent serious pass)** for naming, never quick brainstorming.
- **14_WEB** for any site work.
- **Tool docs** for any tool decision (n8n, Higgsfield, Kling, skills, GitHub).
- **EYL / distribution / ownership docs** for content, distribution, or business-model decisions.

## 7. Mandatory tool-layer check (before any task involving execution)

Before answering any task involving **creation, publishing, design, video, content, CRM, payments, outreach, research, file operations, automation, or external systems**, ask:

> "What tool, app, MCP, API, script, or skill in BJ's stack can execute this instead of only advising?"

The tool-layer check runs alongside the OS-routing check; both are mandatory.

**Routing order (manual is last, not first):**
- **Skills first** for repeatable reasoning and workflow consistency (skills do not burn tool-description tokens).
- **MCPs / APIs** when external execution is needed (Figma MCP for design, Higgsfield for motion when authed, Stripe later, etc.).
- **Scripts** for local / repo automation.
- **Manual fallback only after a full toolchain audit** (per `TOOLCHAIN_ACTIVATION.md` §10, the 11-item checklist) returns "no available path."

**Required reference:** consult `TOOLCHAIN_ACTIVATION.md` whenever tool routing is relevant. It is the single source of truth for what is active, candidate, queued, or deferred in the stack.

**Discipline rules:**
- **Do not install or activate tools without a live job.** Each install needs a real task that depends on it.
- **No tool spiral.** Over 5 active MCPs burns context on tool descriptions before any question lands; keep the active set tight.
- **No AI-generated fake proof.** Higgsfield, Adobe for Creativity, and any creative-AI tool are concept, atmosphere, and polish only on BASEPLATE; never client evidence. SNIPED may publish AI-forward creative openly as art and mythology, never as fake client proof.
- **Preserve IRS / admin gates and brand guardrails.** Stripe MCP and payment automation are gated on the 147C verification letter and the business bank account opening. Site changes route through the repo, not abstract copy. Direction Stack stays private. EIN stays off public surfaces. Employer information stays off all BASEPLATE / SNIPED material.

## 8. Anti-failure rules
- No lazy "all names are taken" (run real multi-TLD checks and multiple naming strategies first).
- No Carrd / no-code default without checking the OS build standard (build-first; no-code is fallback).
- No banning Higgsfield/Kling by default (activate by job per the tool docs; AI as non-evidentiary creative is allowed, AI as fake evidence is not).
- No ignoring GitHub / skills / tool docs when a tool decision is in play.
- No treating old SNIPED/BASEPLATE/BRAND_STRATEGY docs as current law (historical evidence only).
- No platform/registry/network public overclaim.
- No photography-only reduction (media is the instrument; the operator layer is the company).
- No generic motivation or filler.
- No endless ingestion when activation is the actual need.
- No building before the current source-of-truth is clear.

## 9. Response format for serious answers
Serious answers include a short **OS routing receipt** at the top or bottom:
```
OS routing receipt
- Level:
- Category:
- Sources used:
- Skills triggered:
- Resources skipped (and why):
- Proof-loop link:
- Guardrails:
```
Keep it tight. The receipt proves the routing happened; it is not an essay.

## 10. When Claude must stop
Claude stops before answering if:
- a required job-specific resource may exist but has not been checked,
- a factual asset / domain / legal claim is unverified,
- the answer would contradict TRUE_BILLION_DOLLAR_THESIS,
- the recommendation would reduce the thesis to a small service,
- the recommendation would ignore a relevant activated skill,
- or a task with an execution surface is about to receive a "manual" recommendation without the toolchain audit (per `TOOLCHAIN_ACTIVATION.md` §10) having run.
The stop line: "I do not have enough routing clarity. I will inspect the relevant OS layer before proceeding."

## 11. How this applies immediately (current open work)
- **Naming / domain reset = Level 4.** Full OS + /challenge before any final call. (Locked: keep BASEPLATE name, domain is `baseplateworks.com`.)
- **Site deploy = Level 3.** Use BASEPLATE_DOMAIN_AND_EMPIRE_ARCHITECTURE + verifications; deploy on `baseplateworks.com`.
- **Content / Higgsfield = Level 2/3.** Use the tool codices and the distribution docs; AI as non-evidentiary creative only.
- **Outreach = Level 2.** Route through PROOF_LOOPS_30_60_90 and the true thesis.
- **Any domain purchase = Level 3.** Verify live facts at the registrar first.

## 12. What this does NOT mean
- Not rereading every raw book every time (use summaries/indexes/memories by job).
- Not delaying action forever.
- Not using every tool every time.
- Not making the OS a bottleneck.
- Not replacing proof with thinking. Execution and the proof loop still outrank analysis.

## 13. Standing command
Before every serious answer, ask: **"What OS layers make this answer unfairly better than generic AI?"** If the answer is unclear, route first.

---

## OS layers consulted (to write this protocol)
OS_TRANSFORMATION_ROUTER (the by-job routing spine), COMMAND_CENTER_COVERAGE_MANIFEST (use-by-job, do not blindly reread, do not ignore), TRUE_BILLION_DOLLAR_THESIS (the north star this protocol protects), BJ_GRAND_LANE_SYNTHESIS, BASEPLATE_DOMAIN_AND_EMPIRE_ARCHITECTURE (the live deploy gate), TOOLCHAIN_ACTIVATION (the tool-layer doctrine; the mandatory reference for §7 execution routing), the activated skills /challenge //save //boardroom, IMPLEMENTATION_STACK_ACTIVATION (tool stack), HELD_OPERATOR_DOCS_INDEX (parked claims), the memory doctrines (max-default, repetition-over-novelty, the operating-mode and execution-mode locks). MASTER_INDEX and ACTIVE_KNOWLEDGE_STATE are the corpus entry points this protocol routes into.

## Guardrails (unchanged)
Standing protocol, not a permanent identity lock. The OS routes by job; it is not a bottleneck and does not replace proof with thinking. No platform/registry/network public claim. No photography-only reduction. No automation before proof. Old SNIPED/BASEPLATE material is historical evidence, not law. Bible held until a deliberate SPIRITUAL_FOUNDATION decision. Anchor-class: not chunked, not in master files, total_chunks unchanged at 1,837. This protocol governs how answers are produced; it does not itself change the site, the thesis, or any committed decision.
