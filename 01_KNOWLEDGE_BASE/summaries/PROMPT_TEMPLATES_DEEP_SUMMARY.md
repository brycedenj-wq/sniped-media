# PROMPT_TEMPLATES_DEEP summary · 6 AI-Edge prompt-template PDFs · 2026-05-19

12 chunks · 6 unique source files (8 PDFs staged, 2 md5-duplicates excluded) · batch_id `PROMPT_TEMPLATES_DEEP` · validated 6/6.

## What this mini-batch covers

Durable prompt-craft patterns from 6 unique AI-Edge prompt-technique cheat sheets: in-context learning, thought generation, problem decomposition, self-criticism (basic + advanced), and combining techniques. It is the 6th and final 2026-05-19 mini-batch, the prompt-craft CONTENT layer that the N8N_AUTOMATION_SYSTEMS Cluster B prompt-engineer agent produces and consumes. It extends the BATCH_006 `prompt-engineering` domain (8 -> 19 chunks).

12 chunks across 2 domains (no NEW domains):

| # | Concept | Domain | Source |
|--:|---|---|---|
| 001 | In-context learning · few-shot prompting | prompt-engineering | in_context |
| 002 | Thought generation · CoT + ThoT | prompt-engineering | thought_generation |
| 003 | Problem decomposition · LtM + PaS + PoTh | prompt-engineering | problem_decomposition |
| 004 | Self-criticism (basic) · SE + SR + COVE | prompt-engineering | self_criticism_basic |
| 005 | Self-criticism (advanced) · S2A + RaR + RE2 | prompt-engineering | self_criticism_advanced |
| 006 | Combining techniques · CoT + decomposition + self-criticism chained | prompt-engineering | combining_techniques |
| 007 | The prompt-technique taxonomy · full abbreviation map | prompt-engineering | combining_techniques |
| 008 | The Task + structured-Prompt scaffold | prompt-engineering | in_context |
| 009 | Self-criticism as a guardrail layer (verify-before-ship) | prompt-engineering | self_criticism_advanced |
| 010 | The reasoning-scaffold family · when CoT vs PaS vs LtM | prompt-engineering | thought_generation |
| 011 | Prompt-writing-agent substrate · the N8N bridge | ai-tooling | combining_techniques |
| 012 | Few-shot vs zero-shot economics · cheapest quality lever | prompt-engineering | in_context |

## Technique abbreviation map (as found in the source)

- **Few-Shot** (In Context Learning) · examples-then-ask
- **CoT** Chain-of-Thought · **ThoT** Thread-of-Thought (Thought Generation)
- **LtM** Least-to-Most · **PaS** Plan-and-Solve · **PoTh** Plan-of-Thought (Problem Decomposition)
- **SE** Self-Evaluation · **SR** Self-Refine · **COVE** Chain-of-Verification (Self-Criticism Basic)
- **S2A** System-2-Attention · **RaR** Rephrase-and-Respond · **RE2** Re-reading (Self-Criticism Advanced)

Note: the source uses ThoT (Thread-of-Thought), not Tree-of-Thought, and places PoTh (Plan-of-Thought) under Problem Decomposition. Chunked faithfully to the source.

## Where this mini-batch lands canonically

### New prompt-craft installed

1. **Few-shot / in-context learning** (001, 012): examples-then-ask is the cheapest quality lever; lead with 2-3 representative examples to transfer format and voice.
2. **Reasoning scaffolds** (002, 010): CoT for open paths, ThoT/PoTh for known stages, LtM for build-up, PaS for plan-then-execute. Match the scaffold to the task's shape.
3. **Problem decomposition** (003): break one big ask into ordered smaller asks (LtM/PaS/PoTh).
4. **Self-criticism as a gate** (004, 005, 009): a mandatory second pass (SE/SR/COVE/S2A/RaR/RE2) that verifies/refines before shipping. Always the final step.
5. **Combining techniques** (006): chain generate (CoT) -> structure (decomposition) -> verify (self-criticism) in one prompt.
6. **The Task + structured-Prompt scaffold** (008): the reusable container all techniques plug into.
7. **The technique taxonomy** (007): a named lookup table for deliberate technique selection.

### Cross-references opened

- **BATCH_006 operator skill layer:** directly EXTENDS the `prompt-engineering` domain (8 -> 19) · technique-level complement to the B6 framework-level prompt packs (TCREI, framework-orchestrator, pyramid-structured-communication).
- **N8N_AUTOMATION_SYSTEMS Cluster B (prompt-engineer agent):** chunk 011 is the explicit bridge · these templates are the CONTENT the N8N Master Prompt Agent + deep-reasoning/normal sub-workflows produce. The taxonomy is the agent's toolbox, the Task+Prompt scaffold is its output format, self-criticism is its quality gate. CRAFT (here) + IMPLEMENTATION (N8N) are two halves.
- **OPPORTUNITY_MANAGEMENT_TEMPLATES:** the decomposition discipline (003) ↔ the hopper's break-into-scored-sub-steps intake; the Task+Prompt scaffold (008) ↔ the one-page-card standard container.
- **BATCH_007 SOPs:** self-criticism-as-gate (009) ↔ the final-review un-delegate-able + executing-with-care; PaS plan-then-execute (003) ↔ the Saturday-build / Monday-cockpit plan-before-act cadence.
- **Future BATCH_008 AI/tech canon:** these are AI-Edge-course templates; the course books are queued for BATCH_008. Keep here as prompt-craft mini-batch · cross-reference, do not merge. With this batch, all AI-Edge non-book artifacts (n8n workflows, opportunity templates, prompt templates) are chunked; only the AI Edge books remain.

### Auto-memory reinforcement

- `intel_leverage_logic.md` ↔ chunk 012 (few-shot as cheapest input for biggest quality gain).
- `feedback_carousel_attribution.md` ↔ chunk 001 (examples make voice consistent and attributable).

## Domain distribution

| Domain | Chunks | Notes |
|---|---:|---|
| prompt-engineering | 11 | the 6 per-technique + taxonomy/scaffold/guardrail/reasoning-family/economics chunks · roughly doubles the BATCH_006 domain (8 -> 19) |
| ai-tooling | 1 | the prompt-writing-agent / N8N-bridge chunk (011) |

**No NEW domains introduced.** Both pre-exist. `operator-process` and `automation-blueprint` were available as secondary candidates but not needed as primaries.

## Duplicate handling

8 PDFs staged; md5 confirmed 2 true-duplicate pairs:
- `Combining Techniques-2.pdf` == `Combining Techniques-3.pdf` (md5 `0f54f23559...`)
- `Self Criticism (Advanced)-2.pdf` == `Self Criticism (Advanced)-3.pdf` (md5 `d62b67512e...`)

Only the 6 unique canonical PDFs were extracted (the `-3` of each duplicate pair was used). The 2 `-2` duplicate copies were SKIPPED entirely · they contributed 0 chunks, were not extracted to txt, and remain untouched in `raw/`. No duplicate-template chunking: exactly 1 chunk per unique technique + synthesis chunks; 6 unique `source_file` values referenced.

## Extraction-method results

| Unique PDF | Output | Words |
|---|---|---:|
| In Context-2.pdf | prompt_template_in_context.txt | 303 |
| Thought Generation-2.pdf | prompt_template_thought_generation.txt | 314 |
| Problem Decomposition.pdf | prompt_template_problem_decomposition.txt | 317 |
| Self Criticism (Basic)-3.pdf | prompt_template_self_criticism_basic.txt | 269 |
| Self Criticism (Advanced)-3.pdf | prompt_template_self_criticism_advanced.txt | 266 |
| Combining Techniques-3.pdf | prompt_template_combining_techniques.txt | 420 |

Method: `pdftotext -layout` (Poppler) · no OCR · no new dependencies. Promo header/footer lines (skool.com / "Join My AI & Automation Community") stripped as noise. All 6 cleared the 100-word sanity floor · 0 OCR-deferred.

## Validation

All 6 checks PASS: JSONL parse · required fields (12/12) · chunk_id uniqueness (0 dupes / 12) · batch_id single value · source_file resolution (6 distinct, all resolve) · counts 12 chunks / 6 sources. Em-dash sweep: 0.

## Deviations from PROMPT_TEMPLATES_DEEP_PLAN.md

1. **Final count 12** (target ~12 · range 10-15). Exactly on target · 6 per-technique + 6 cross-cutting synthesis (taxonomy, Task+Prompt scaffold, self-criticism guardrail, reasoning-scaffold family, prompt-writing-agent/N8N bridge, few-shot economics). The optional 12th chunk (few-shot economics) was kept.
2. **Domain split prompt-engineering 11 + ai-tooling 1.** No NEW domains. operator-process / automation-blueprint not used as primaries (matches plan section 5 "only if needed").
3. **Source-abbreviation fidelity.** The operator brief mentioned "tree-of-thought" and "program-of-thought"; the source actually uses ThoT (Thread-of-Thought) and PoTh (Plan-of-Thought under decomposition). Chunked faithfully to the source, noted here.
4. **No structural deviations.** No source PDFs modified. The 2 duplicate copies skipped (0 chunks). No master files updated. No new dependencies. BATCH_008 not started. No literary intake touched.

## What this mini-batch enables

1. A reusable prompt-technique library · named techniques, a standard Task+Prompt container, and a self-criticism gate · directly usable for any SNIPED AI surface.
2. Closes the prompt loop: PROMPT_TEMPLATES_DEEP (craft) + N8N_AUTOMATION_SYSTEMS Cluster B (implementation) let SNIPED stand up a prompt-engineering agent governed by named techniques + a quality gate.
3. Completes the 2026-05-19 mini-batch sequence · all 6 mini-batches (IAF, POC, B2B, OMT, N8N, PTD) shipped and (pending this consolidation) consolidated. All AI-Edge non-book artifacts are now chunked.

## End state

`01_KNOWLEDGE_BASE/batches/PROMPT_TEMPLATES_DEEP_CHUNKS.jsonl` is canonical and validated. Awaits `master-consolidation`. No master files updated in this run. New corpus total after consolidation: 906 + 12 = 918 chunks across 7 numbered batches + 6 mini-batches.
