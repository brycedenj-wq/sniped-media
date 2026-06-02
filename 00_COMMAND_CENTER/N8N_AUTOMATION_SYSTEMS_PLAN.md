# N8N_AUTOMATION_SYSTEMS mini-batch plan · 2026-05-19

Plan only. No extraction, no chunking, no master-file updates, no BATCH_008 start, no commit. Stops after this plan is written.

This mini-batch extracts durable automation-system patterns from the 6 n8n JSON workflows in the 2026-05-19 intake. It is the 5th 2026-05-19 mini-batch and the supply-side implementation layer that the B2B_POSITIONING_CLAUDE_OPERATOR (responsiveness AI) and OPPORTUNITY_MANAGEMENT_TEMPLATES (a cleared opportunity card becomes a workflow spec) mini-batches set up. It extends the BATCH_006 `automation-blueprint` domain.

---

## 0 · Headline

- **Sources:** 6 n8n workflow exports (JSON) · 99 KB total · ALL CONFIRMED on disk. 2 thematic clusters: voice-agent automation (VAPI + RetellAI) and a multi-entry Prompt Engineer Agent.
- **Extraction method:** stdlib `json` · parse each workflow and emit a normalized text summary (node inventory, triggers, AI/model nodes + system-prompt excerpts, tool nodes, integrations, data-flow edges, sticky-note docs). NO new dependencies. STRIP credential value fields + auth headers; keep credential reference NAMES only.
- **Credential safety:** all 6 files passed a literal-secret scan CLEAN (0 hits). Credential references are name-only (e.g. `airtableTokenApi/The AI Edge`, `openRouterApi/Prompt Engineer Agent`) · these are n8n credential IDs + display names, not secret values. The extractor must still strip any value fields defensively.
- **Estimated yield:** 15-25 chunks · target ~18.
- **Domains:** automation-blueprint, operator-process, ai-tooling, client-application (commercial-architecture available if needed). ALL EXIST. No NEW domains.

---

## 1 · Source files confirmed on disk

| # | File | Size | Internal workflow name | Nodes |
|--:|---|---:|---|---:|
| 1 | `AI Phone Call Assistant - Call Workflow.json` | 18.6 KB | AI Phone Call Assistant - Call Workflow | 17 |
| 2 | `n8n & RetellAI.json` | 28.8 KB | n8n & RetellAI | 23 |
| 3 | `Master Prompt Agent - Chat Input.json` | 12.4 KB | Prompt Writing Agent - Text Input | 8 |
| 4 | `Master Prompt Agent - Form Submission.json` | 15.7 KB | Prompt Engineer Agent - Form Master | 6 |
| 5 | `Prompt Writing Agent - Deep Reasoning Workflow.json` | 11.8 KB | Prompt Engineer Agent - Deep Reasoning | 6 |
| 6 | `Prompt Writing Agent - Normal Model Workflow.json` | 11.7 KB | Prompt Engineer Agent - Normal model | 6 |

All in `raw/10_REFERENCE/_intake_2026-05-19/automations/`. Staged in commit `215ffce`. Neither extracted nor chunked.

**Filename vs internal-name note:** files 3-6 have a slight filename/internal-name drift (`Master Prompt Agent - Chat Input` is internally "Prompt Writing Agent - Text Input"; the 4 prompt files all carry "Prompt Engineer Agent" internal names). Chunks will record both; `source_file` uses the on-disk filename normalized.

---

## 2 · Per-workflow purpose (inferred from filename + top-level JSON + node types + sticky notes)

A read-only structural peek (stdlib `json` to stdout · no files written) was run on all 6.

### Cluster A · Voice-agent automation (The AI Edge)

**1. AI Phone Call Assistant - Call Workflow** (17 nodes · VAPI). 2 webhooks + a formTrigger feed a langchain `agent` (OpenAI chat model) equipped with a Perplexity research tool and an Airtable data tool; an IF branch + an httpRequest trigger the outbound call; respondToWebhook returns the result. 6 sticky notes document a 3-step scaffold: **Connecting into Vapi → Activities Webhook → Triggering a call.** Agent system prompt: "You are a helpful assistant, you need to store all of the key information in the Airtable tool that you have access to." Credentials: Airtable / OpenAI / Perplexity (name-only).

**2. n8n & RetellAI** (23 nodes · RetellAI · the larger sibling). 2 webhooks, 2 IFs, a switch, 2 httpRequests, a langchain `agent` (2 OpenAI chat models) with Perplexity + Airtable tools, a structured-output parser, a chainLlm, a formTrigger, respondToWebhook. Same 3-step sticky-note scaffold: **Connecting into Retell AI → Activities Webhook → Triggering a call.** Includes a "Follow Up?" branch keyed on call End Reason / Transcript fields. Agent prompt is a template placeholder ("<REPLACE WITH YOUR AGENT INSTRUCTION> ... storing information into airtable"). Credentials: Airtable / OpenAI x2 / Perplexity (name-only).

These two ARE the "AI voice receptionist / missed-call text-back / responsiveness AI" category named in B2B chunks 004-005. The VAPI and RetellAI variants are two implementations of the same inbound/outbound voice-agent pattern.

### Cluster B · Prompt Engineer Agent (multi-entry orchestrated AI agent)

**3. Master Prompt Agent - Chat Input** (8 nodes). A chatTrigger feeds a langchain `agent` (OpenRouter models) that has 2 `toolWorkflow` sub-agents, plus a chainLlm and a structured-output parser. The chat entry point. Agent prompt: "You are a master prompt writing agent. You have 2 sub execution workflows that can develop the best prompts..."

**4. Master Prompt Agent - Form Submission** (6 nodes). A formTrigger + form feed the same master `agent` (OpenRouter) with 2 `toolWorkflow` sub-agents. The form entry point / orchestrator. Same master-agent prompt.

**5. Prompt Writing Agent - Deep Reasoning** (6 nodes). An `executeWorkflowTrigger` (so it runs as a callable sub-workflow tool) → a Basic LLM Chain that "analyse[s] the request and identif[ies] the most suitable model" → a `set` → the "Deep Reasoning Prompt Writing" agent (OpenRouter). The deep-reasoning model-tier sub-agent.

**6. Prompt Writing Agent - Normal Model** (6 nodes). Identical shape to #5 but the "Normal model" tier. The normal-tier sub-agent.

Cluster B is a multi-entry (chat + form) master agent that routes to two model-tier sub-workflows (deep-reasoning vs normal) via `toolWorkflow` / `executeWorkflowTrigger`. NOTE: this overlaps thematically with the future PROMPT_TEMPLATES_DEEP mini-batch (8 prompt-craft PDFs) but is distinct · Cluster B is the n8n IMPLEMENTATION of a prompt-engineering agent; PROMPT_TEMPLATES_DEEP is the prompt-craft CONTENT. Keep separate, cross-reference.

### Theme-coverage check (vs operator brief)

| Theme | Present? | Where |
|---|---|---|
| Workflow architecture | Yes | all 6 (node DAGs + connections) |
| Trigger logic | Yes | webhook, formTrigger, chatTrigger, executeWorkflowTrigger |
| AI-agent routing | Yes | langchain.agent + toolWorkflow routing; chat-vs-form entry; deep-vs-normal model tiers |
| VAPI / Retell / voice-agent | Yes | workflows 1 (VAPI) + 2 (RetellAI) |
| MCP / dynamic brain / memory | Partial | NO dedicated MCP node and NO dedicated memory node; the agent + tool-node pattern is the closest "dynamic brain" analog · this will be noted, not overclaimed |
| Guardrails | Yes | structured-output parser (outputParserStructured) + IF/switch routing |
| Data tables / structured storage | Yes | Airtable (airtable + airtableTool nodes) as the state/data layer |
| Automation blueprint logic | Yes | all 6 |
| Opportunity-card -> workflow-build link | Yes | these are the OMT "Proposed Vendor: n8n" build targets |

---

## 3 · Extraction method

stdlib `json` only · NO new dependencies. For each of the 6 workflows the extractor writes a normalized text summary capturing:

- Workflow name (filename + internal name) and node count.
- Node inventory: for each node, `type` + `name` + the durable non-secret parameters (model name, tool name, IF/switch conditions, httpRequest method + URL host, Airtable base/table references, form field labels).
- Trigger nodes called out explicitly (webhook / formTrigger / chatTrigger / executeWorkflowTrigger).
- AI/model nodes: model identifier + a system-prompt excerpt (the agent instruction · durable IP).
- Tool nodes: Perplexity, Airtable, toolWorkflow targets.
- Data-flow edges: the `connections` graph rendered as `source -> [targets]`.
- Sticky-note documentation verbatim (the human-readable workflow narration).

**Security handling:** STRIP the `credentials` blocks to NAMES only (provider + display name · e.g. `openRouterApi/Prompt Engineer Agent`); never emit credential value fields. Strip any `httpHeaderAuth` / `Authorization` header values and any inline tokens. The literal-secret scan is already clean (0 hits across all 6), but the extractor strips defensively. `pinData` (cached run data) is skipped to avoid leaking sample PII.

Output: one normalized `.txt` per workflow in `01_KNOWLEDGE_BASE/batches/n8n_automation_systems_extracted/`.

---

## 4 · Estimated chunk yield · 15-25 chunks · target ~18

A mix of per-workflow architecture chunks and the higher-value cross-cutting reusable-pattern chunks.

### Per-workflow architecture (5 chunks · the two near-identical model-tier sub-workflows share one)

| # | Chunk | Domain |
|--:|---|---|
| 1 | AI Phone Call Assistant (VAPI) · end-to-end voice-agent workflow architecture | automation-blueprint |
| 2 | n8n & RetellAI · voice-agent workflow architecture + follow-up branch | automation-blueprint |
| 3 | Master Prompt Agent · chat-input entry orchestrator | automation-blueprint |
| 4 | Master Prompt Agent · form-submission entry orchestrator | automation-blueprint |
| 5 | Prompt Writing Agent sub-workflows · deep-reasoning vs normal model tiers (the two near-identical sub-agents as one model-tier-routing chunk) | automation-blueprint |

### Cross-cutting reusable patterns (~10-15 chunks · the durable layer)

| # | Chunk | Domain |
|--:|---|---|
| 6 | Voice-agent integration pattern · the 3-step scaffold (connect provider -> activities webhook -> trigger call) · VAPI vs RetellAI as two implementations | automation-blueprint |
| 7 | The langchain agent + tool-node pattern · agent core with a research tool (Perplexity) + a data tool (Airtable) | ai-tooling |
| 8 | Trigger-logic taxonomy · webhook / formTrigger / chatTrigger / executeWorkflowTrigger · when to use which | automation-blueprint |
| 9 | Multi-entry agent orchestration · chat + form entry points routing to one agent core | automation-blueprint |
| 10 | Model-tier routing · a Basic-LLM-Chain selector picks deep-reasoning vs normal model before the sub-agent runs | ai-tooling |
| 11 | Sub-workflow-as-tool composition · toolWorkflow + executeWorkflowTrigger to compose agents | automation-blueprint |
| 12 | Structured-output parsing as a guardrail · outputParserStructured enforcing schema on agent output | ai-tooling |
| 13 | IF / switch branching control flow · routing on call End Reason / conditions (the "Follow Up?" branch) | operator-process |
| 14 | Airtable as the structured data/state layer · the agent reads/writes a base as memory-by-database | automation-blueprint |
| 15 | httpRequest as the outbound action layer · triggering the VAPI/Retell APIs + respondToWebhook for synchronous voice response | automation-blueprint |
| 16 | Credential-reference architecture · named, provider-scoped credentials ("The AI Edge" / "Ops Management" / "Prompt Engineer Agent") · ops/security hygiene | operator-process |
| 17 | Perplexity research-tool integration · live-search augmentation of the agent | ai-tooling |
| 18 | The opportunity-card -> n8n-workflow-build bridge · these workflows ARE the OMT "Proposed Vendor: n8n" build targets and the B2B responsiveness-AI category | client-application |

That is 18 mapped chunks. Range 15-25 leaves room to split (e.g. VAPI vs Retell credential/webhook differences) or merge (e.g. fold 17 into 7) at chunk-write time. Target ~18.

---

## 5 · Approved domains / tags

All candidate domains ALREADY EXIST. No NEW domains. Counts at 888-chunk state:

| Domain | Current count | Use in this mini-batch |
|---|---:|---|
| automation-blueprint | 6 | primary on the workflow-architecture + integration/trigger/composition chunks (the bulk) · roughly triples this thin BATCH_006 domain |
| ai-tooling | 14 | primary on the agent/tool/model-tier/parsing chunks |
| operator-process | 30 | primary on branching control flow + credential-hygiene chunks |
| client-application | 4 | primary on the opportunity-card -> workflow-build bridge chunk |
| commercial-architecture | 19 | available as a secondary tag only if a chunk frames the build as a sellable deliverable; no primary expected |

**Recommended tag bank:** `n8n`, `automation-blueprint`, `voice-agent`, `vapi`, `retellai`, `ai-receptionist`, `responsiveness-ai`, `langchain-agent`, `agent-tool-pattern`, `perplexity-tool`, `airtable-data-layer`, `trigger-logic`, `webhook`, `form-trigger`, `chat-trigger`, `execute-workflow-trigger`, `tool-workflow`, `sub-workflow-as-tool`, `model-tier-routing`, `structured-output-parser`, `guardrail`, `if-switch-branching`, `http-request`, `respond-to-webhook`, `credential-scoping`, `prompt-engineer-agent`, `opportunity-card-to-build`, `the-ai-edge`, `ai-tooling-aging-risk`.

**Aging note:** n8n node type names, the langchain node namespace, VAPI/RetellAI API specifics, and OpenRouter/OpenAI model names age fast; the workflow PATTERNS (trigger taxonomy, agent+tool, model-tier routing, sub-workflow composition, structured-output guardrail, data-layer-as-memory) do not. Every chunk carries `ai-tooling-aging-risk` + the 2026-05-19 source date; summaries foreground the durable pattern and treat node/version/model specifics as dated illustration.

---

## 6 · How this mini-batch connects to the rest of the corpus

### BATCH_006 operator skill layer
- This mini-batch directly EXTENDS the BATCH_006 `automation-blueprint` domain (currently 2 chunks: AI Content Strategy Generator + ElevenLabs voice agent · roughly triples it). The voice-agent workflows (chunks 1-2, 6) are the n8n-native cousins of the B6 ElevenLabs voice agent. The agent+tool pattern (chunk 7) pairs with the B6 prompt-engineering packs.

### BATCH_007 SOPs
- The IF/switch follow-up branching (chunk 13) and the credential-scoping hygiene (chunk 16) map to the B7 recurring_checklists + operational-locks discipline · automation must have explicit branches and scoped access, not implicit trust.

### B2B_POSITIONING_CLAUDE_OPERATOR
- Chunks 1-2 + 6 (voice agents) ARE the "responsiveness AI · AI voice receptionist · missed-call text-back" category named in B2B chunks 004-005. This mini-batch is the SUPPLY-SIDE implementation of the demand B2B framed. Strongest cross-batch link in the 2026-05-19 set.

### OPPORTUNITY_MANAGEMENT_TEMPLATES
- Chunk 18 (opportunity-card -> workflow-build bridge) closes the loop: the OMT hopper's "Proposed Vendor: n8n" rows and the cleared opportunity card become these exact workflow builds. OMT is the intake/ROI/readiness front-end; this mini-batch is the build. The "The AI Edge" credential names here match the AI-Edge-course provenance of the OMT templates.

### Future PROMPT_TEMPLATES_DEEP (staged, not chunked)
- Cluster B (the Prompt Engineer Agent · chunks 3-5, 9-11) is the n8n IMPLEMENTATION of a prompt-engineering agent; PROMPT_TEMPLATES_DEEP (8 prompt-craft PDFs) is the prompt-craft CONTENT. They are complementary: the agent here would CONSUME the templates there. Keep separate · cross-reference at PROMPT_TEMPLATES_DEEP consolidation.

---

## 7 · Deliverables (produced in the EXTRACTION + CHUNK session · NOT now)

| Deliverable | Path | Notes |
|---|---|---|
| Chunks JSONL | `01_KNOWLEDGE_BASE/batches/N8N_AUTOMATION_SYSTEMS_CHUNKS.jsonl` | 15-25 chunks · batch_id `N8N_AUTOMATION_SYSTEMS` · 12-field canonical schema |
| Extracted source dir | `01_KNOWLEDGE_BASE/batches/n8n_automation_systems_extracted/` | 6 normalized `.txt` (one per workflow · credentials stripped to names) |
| Summary | `01_KNOWLEDGE_BASE/summaries/N8N_AUTOMATION_SYSTEMS_SUMMARY.md` | what it covers · where it lands · cross-references |
| Source index | `01_KNOWLEDGE_BASE/indexes/N8N_AUTOMATION_SYSTEMS_SOURCE_INDEX.md` | per-chunk concept + domain + source-workflow map |
| Extraction log | `00_COMMAND_CENTER/batch_logs/N8N_AUTOMATION_SYSTEMS_EXTRACTION_LOG.md` | sources in / extracted out / failures / secret-scan result |
| Completion marker | `00_COMMAND_CENTER/batch_logs/N8N_AUTOMATION_SYSTEMS_COMPLETE.md` | status · validation summary · deviations |
| Extraction script | `scripts/extract_n8n_automation_systems.py` | NEEDED · stdlib json · per-workflow node/trigger/agent/tool/edge/sticky summary · credential-value strip. No new deps. |
| Chunk writer | `scripts/write_n8n_automation_systems_chunks.py` | NEEDED · hand-authored chunk emit + em-dash sweep via `chr(0x2014)`. Mirror `scripts/write_opportunity_management_templates_chunks.py`. |

### Schema decisions (recommended · finalized at chunk-write time)
- `batch_id`: `N8N_AUTOMATION_SYSTEMS`
- `chunk_id` pattern: `N8N_AUTOMATION_SYSTEMS_001` ... `_0NN`
- `source_title`: `<workflow name> · n8n workflow (The AI Edge)` for per-workflow chunks; `n8n Automation Systems · cross-workflow pattern` for the pattern chunks
- `author`: `The AI Edge (n8n workflow templates)`
- `source_file`: normalized lowercase-snake-case `.txt` per workflow (e.g. `ai_phone_call_assistant.txt`, `n8n_retellai.txt`, `master_prompt_agent_chat_input.txt`, `master_prompt_agent_form_submission.txt`, `prompt_writing_agent_deep_reasoning.txt`, `prompt_writing_agent_normal_model.txt`). Cross-workflow pattern chunks cite the most representative workflow file (each pattern is grounded in a real on-disk source so jsonl-validation check 5 passes).

---

## 8 · Explicit exclusions

| Material | Disposition |
|---|---|
| Credential value fields / auth tokens / API keys | EXCLUDE · strip to NAMES only · literal-secret scan already clean (0 hits) |
| `pinData` (cached run data) | EXCLUDE · may contain sample PII / transcripts · not extracted |
| n8n internal IDs (node UUIDs, versionId, webhookId) | EXCLUDE from chunks · not durable signal |
| Exact node x/y canvas coordinates | EXCLUDE · layout noise |
| Prompt-craft CONTENT (the technique of prompt writing) | OUT OF SCOPE · belongs to the future PROMPT_TEMPLATES_DEEP mini-batch · this mini-batch chunks the AGENT IMPLEMENTATION, not the prompt-craft itself |
| Prompt-template / literary intake sources | OUT OF SCOPE · not touched |

---

## 9 · What this planning session does NOT do

- No extraction. The planning peek used stdlib `json` to stdout only · no extracted files written.
- No chunking. No JSONL writes.
- No master-file updates (`MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` untouched).
- No script files written.
- No BATCH_008 start.
- No prompt-template / literary intake touched.
- No source files moved/renamed/deleted.
- No new dependencies.
- No commit.

---

## 10 · Recommended next operation

Authorize the extraction + chunk session per the locked 7-step SOP (steps 5-6):
1. Run `scripts/extract_n8n_automation_systems.py` · stdlib json on all 6 workflows into `n8n_automation_systems_extracted/` (credentials stripped to names · pinData skipped).
2. Hand-author 15-25 chunks (target ~18) per the section 4 map.
3. Run `jsonl-validation` (6 checks) + em-dash sweep + a credential-leak re-scan on the chunk output.
4. Write summary + source index + logs + completion marker.
5. Stop after validation + reporting · await `master-consolidation` authorization.

After this mini-batch consolidates (target 888 -> ~903-913), the next queued mini-batch per `STAGING_PLAN_2026-05-19_INTAKE.md` section 5 is `PROMPT_TEMPLATES_DEEP` (8 prompt-template PDFs · 10-15 chunks), before the literary-canon passes and BATCH_008.

---

## 11 · Revision log

- **rev 1 (2026-05-19 · this version):** First plan for the N8N_AUTOMATION_SYSTEMS mini-batch. All 6 workflows confirmed on disk. Read-only stdlib peek run on all 6 (node types, sticky notes, agent prompts, credential refs). 2 clusters identified: voice-agent (VAPI + RetellAI) + Prompt Engineer Agent (chat/form entry -> deep/normal model-tier sub-workflows). Credential-safety scan CLEAN (0 literal secrets · refs are name-only). Extraction method: stdlib json with defensive credential/value + pinData stripping (no new deps). 15-25 chunk estimate · target ~18. All candidate domains (automation-blueprint, operator-process, ai-tooling, client-application, commercial-architecture) confirmed pre-existing · no NEW domains. Cross-references mapped to B6 automation-blueprint (extends it), B7 SOPs, B2B (supply-side of the responsiveness-AI demand), OMT (a cleared card becomes a build), and future PROMPT_TEMPLATES_DEEP (the agent consumes those templates · keep separate).
