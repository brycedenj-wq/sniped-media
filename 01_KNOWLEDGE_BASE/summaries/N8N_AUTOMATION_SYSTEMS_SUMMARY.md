# N8N_AUTOMATION_SYSTEMS summary · 6 n8n workflows · 2026-05-19

18 chunks · 6 source workflows (5 distinct `source_file` references) · batch_id `N8N_AUTOMATION_SYSTEMS` · validated 6/6 · security scan CLEAN.

## What this mini-batch covers

The durable automation-system architecture inside 6 n8n workflow exports (The AI Edge): node patterns, trigger logic, AI-agent routing, voice-agent (VAPI + RetellAI) integration, guardrails, data/state layer, and the build patterns that connect opportunity cards to implemented workflows. It is the 5th 2026-05-19 mini-batch and the supply-side implementation layer of the B2B (responsiveness AI) + OPPORTUNITY_MANAGEMENT_TEMPLATES (a cleared card becomes a build) demand. It extends the BATCH_006 `automation-blueprint` domain (6 -> 17 chunks).

## Workflow clusters discovered

**Cluster A · Voice-agent automation (2 workflows):**
- `AI Phone Call Assistant` (VAPI · 17 nodes) and `n8n & RetellAI` (RetellAI · 23 nodes). Both: webhook(s) + form trigger -> langchain agent (gpt-4.1-mini) with Perplexity research tool + Airtable data tool -> respondToWebhook; an outbound httpRequest triggers the provider call API. RetellAI adds a post-call intelligence branch (Status-of-Call switch -> User-Hung-Up IF / store report -> Follow-Up LLM gated by a structured-output parser). Both document the same 3-step scaffold (connect provider / activities webhook / trigger call). These ARE the responsiveness-AI / AI-voice-receptionist category.

**Cluster B · Prompt Engineer Agent (4 workflows):**
- `Master Prompt Agent - Chat Input` + `Master Prompt Agent - Form Submission` are two entry surfaces (chat + form) into one master agent (OpenRouter) that routes to two toolWorkflow sub-agents. `Prompt Writing Agent - Deep Reasoning` + `Prompt Writing Agent - Normal Model` are the two model-tier sub-workflows (executeWorkflowTrigger), each running a model-selector LLM chain then a tier-specific prompt-writing agent. This is the n8n IMPLEMENTATION of a prompt-engineering agent (the future PROMPT_TEMPLATES_DEEP mini-batch is the prompt-craft CONTENT such an agent consumes · kept separate).

## Chunk map (18)

Per-workflow architecture (5): 001 VAPI phone assistant · 002 RetellAI + follow-up · 003 chat-input orchestrator · 004 form orchestrator · 005 deep-reasoning vs normal model tiers.

Cross-cutting patterns (13): 006 voice-agent 3-step provider scaffold · 007 agent + tool-node pattern · 008 trigger-logic taxonomy · 009 multi-entry orchestration · 010 model-tier routing · 011 sub-workflow-as-tool composition · 012 structured-output parsing as guardrail · 013 IF/switch branching control flow · 014 Airtable as data/state layer (memory-by-database) · 015 httpRequest + respondToWebhook action layer · 016 credential-reference architecture · 017 Perplexity research-tool integration · 018 opportunity-card -> n8n-build bridge.

## Domain distribution

| Domain | Chunks | Notes |
|---|---:|---|
| automation-blueprint | 11 | workflow architecture + integration/trigger/composition (bulk) · roughly triples the BATCH_006 domain (6 -> 17) |
| ai-tooling | 4 | agent+tool, model-tier routing, structured-output guardrail, Perplexity research tool |
| operator-process | 2 | IF/switch branching control flow + credential-hygiene |
| client-application | 1 | opportunity-card -> workflow-build bridge |

**No NEW domains introduced.** All 4 pre-exist. `commercial-architecture` (optional 5th candidate) not needed.

## Cross-references opened

- **BATCH_006 operator skill layer:** directly EXTENDS the `automation-blueprint` domain · the voice agents are the n8n cousins of the B6 ElevenLabs voice-agent blueprint; the agent+tool primitive (007) and sub-workflow-as-tool composition (011) mirror the .claude/skills/ single-responsibility design.
- **BATCH_007 SOPs:** branching control flow (013) + credential scoping (016) map to operational-locks + recurring-checklists; structured-output-before-action (012) mirrors final-review-before-ship; the RetellAI follow-up branch (002, 013) is the automated capture-to-delivery follow-up cadence.
- **B2B_POSITIONING_CLAUDE_OPERATOR:** chunks 001-002 + 006 ARE the responsiveness-AI / voice-receptionist category named in B2B 004-005 · this is the supply-side build of that demand. Model-tier routing (010) operationalizes the B2B cognitive-vs-responsiveness frame.
- **OPPORTUNITY_MANAGEMENT_TEMPLATES:** chunk 018 closes the loop · a hopper row with 'Proposed Vendor: n8n' and a cleared opportunity card become these workflow builds. Shared 'The AI Edge' provenance.
- **Future PROMPT_TEMPLATES_DEEP (staged, not chunked):** Cluster B is the agent IMPLEMENTATION; PROMPT_TEMPLATES_DEEP is the prompt-craft CONTENT it consumes. Complementary · keep separate · cross-reference at that consolidation.

## Auto-memory reinforcement

- `intel_ai_sentiment.md` (hybrid-operator stance) ↔ chunks 007, 010, 017 (right tool / right model / bounded retrieval).
- `intel_leverage_logic.md` ↔ chunk 006 (vendor-agnostic scaffold · build the brain once, swap the adapter).

## Extraction-method results

| Workflow | Output | Words |
|---|---|---:|
| AI Phone Call Assistant - Call Workflow.json | ai_phone_call_assistant.txt | 287 |
| n8n & RetellAI.json | n8n_retellai.txt | 370 |
| Master Prompt Agent - Chat Input.json | master_prompt_agent_chat_input.txt | 227 |
| Master Prompt Agent - Form Submission.json | master_prompt_agent_form_submission.txt | 189 |
| Prompt Writing Agent - Deep Reasoning Workflow.json | prompt_writing_agent_deep_reasoning.txt | 329 |
| Prompt Writing Agent - Normal Model Workflow.json | prompt_writing_agent_normal_model.txt | 323 |

Method: stdlib `json` only · no new dependencies. Each summary captures node inventory, triggers, AI/model nodes (+ system-prompt excerpts), tool nodes, integration nodes, data-flow edges, sticky-note docs, and credential references by name. Credential values, auth headers, tokens, and `pinData` were stripped.

## Security validation

Literal-secret scan (OpenAI/OpenRouter/AWS/Bearer/JWT-style patterns) over all 6 extracted files AND the chunk JSONL: **0 hits · CLEAN.** Credential references appear name-only:
- `airtableTokenApi/The AI Edge`, `openAiApi/Ops Management`, `openAiApi/The AI Edge`, `perplexityApi/The AI Edge`, `openRouterApi/Prompt Engineer Agent`.

No credential values, auth tokens, API keys, bearer tokens, webhook secrets, or pinData are present in any extracted file, chunk, log, summary, or index.

## Validation

All 6 checks PASS: JSONL parse · required fields (12/12) · chunk_id uniqueness (0 dupes / 18) · batch_id single value · source_file resolution (5 distinct files, all resolve) · counts 18 chunks / 5 referenced sources. Em-dash sweep: 0.

## Deviations from N8N_AUTOMATION_SYSTEMS_PLAN.md

1. **Final count 18** (target ~18 · range 15-25). Exactly on target. 5 per-workflow + 13 cross-cutting pattern chunks as mapped.
2. **5 distinct `source_file` references across 6 extracted workflows.** Chunk 005 covers BOTH model-tier sub-workflows (deep-reasoning + normal) and cites the deep-reasoning file as representative, so `prompt_writing_agent_normal_model.txt` is extracted and on disk but not used as a standalone `source_file`. This matches the plan's "the two near-identical sub-workflows share one chunk" decision.
3. **MCP / memory not present.** As the plan anticipated, there is no dedicated MCP node and no dedicated memory node; chunk 014 documents Airtable-as-memory-by-database as the closest analog (not overclaimed).
4. **Domain split automation-blueprint 11 + ai-tooling 4 + operator-process 2 + client-application 1.** No NEW domains. `commercial-architecture` not used.
5. **No structural deviations.** No source JSON modified. No master files updated. No new dependencies. BATCH_008 not started. No prompt-template / literary intake touched.

## What this mini-batch enables

1. A reusable n8n automation blueprint library · voice-agent scaffold, agent+tool primitive, trigger taxonomy, model-tier routing, sub-workflow composition, structured-output guardrail, memory-by-database, credential hygiene.
2. The demand-to-delivery spine is now complete end to end: B2B (demand) -> OPPORTUNITY_MANAGEMENT_TEMPLATES (intake/ROI/readiness) -> N8N_AUTOMATION_SYSTEMS (build). A 3-hop retrieval path exists.
3. The voice-agent builds are the concrete SNIPED responsiveness-AI offer (missed-call/receptionist) ready to spec against a client.
4. The JSON extraction pipeline (with credential stripping) is proven for any future n8n/workflow sources.

## End state

`01_KNOWLEDGE_BASE/batches/N8N_AUTOMATION_SYSTEMS_CHUNKS.jsonl` is canonical and validated. Awaits `master-consolidation`. No master files updated in this run. New corpus total after consolidation: 888 + 18 = 906 chunks across 7 numbered batches + 5 mini-batches.
