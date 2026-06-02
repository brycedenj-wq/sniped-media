# N8N_AUTOMATION_SYSTEMS source index · 2026-05-19

6 source workflows · 18 chunks · batch_id `N8N_AUTOMATION_SYSTEMS`. 5 distinct `source_file` references (chunk 005 covers both model-tier sub-workflows).

## Sources

| # | Extracted file | Cluster | Chunks referencing it | Original source |
|--:|---|---|---|---|
| 1 | `ai_phone_call_assistant.txt` | A · voice | 001, 007, 014, 016, 017 | `raw/10_REFERENCE/_intake_2026-05-19/automations/AI Phone Call Assistant - Call Workflow.json` |
| 2 | `n8n_retellai.txt` | A · voice | 002, 006, 012, 013, 015, 018 | `raw/10_REFERENCE/_intake_2026-05-19/automations/n8n & RetellAI.json` |
| 3 | `master_prompt_agent_chat_input.txt` | B · prompt agent | 003, 008, 011 | `raw/10_REFERENCE/_intake_2026-05-19/automations/Master Prompt Agent - Chat Input.json` |
| 4 | `master_prompt_agent_form_submission.txt` | B · prompt agent | 004, 009 | `raw/10_REFERENCE/_intake_2026-05-19/automations/Master Prompt Agent - Form Submission.json` |
| 5 | `prompt_writing_agent_deep_reasoning.txt` | B · prompt agent | 005, 010 | `raw/10_REFERENCE/_intake_2026-05-19/automations/Prompt Writing Agent - Deep Reasoning Workflow.json` |
| 6 | `prompt_writing_agent_normal_model.txt` | B · prompt agent | (covered by chunk 005 · extracted, not a standalone source_file) | `raw/10_REFERENCE/_intake_2026-05-19/automations/Prompt Writing Agent - Normal Model Workflow.json` |

Source: The AI Edge n8n workflow templates. Extracted via stdlib zipfile-free `json` parse (no new dependencies); credentials reduced to name references, pinData/secrets stripped; literal-secret scan CLEAN (0 hits).

## Per-chunk concept + domain + source map

| chunk_id | Concept | Domain | source_file |
|---|---|---|---|
| 001 | AI Phone Call Assistant (VAPI) workflow architecture | automation-blueprint | ai_phone_call_assistant.txt |
| 002 | n8n & RetellAI workflow architecture + follow-up branch | automation-blueprint | n8n_retellai.txt |
| 003 | Master Prompt Agent · chat-input orchestrator | automation-blueprint | master_prompt_agent_chat_input.txt |
| 004 | Master Prompt Agent · form-submission orchestrator | automation-blueprint | master_prompt_agent_form_submission.txt |
| 005 | Prompt Writing sub-workflows · deep-reasoning vs normal model tiers | automation-blueprint | prompt_writing_agent_deep_reasoning.txt |
| 006 | Voice-agent integration pattern · 3-step provider scaffold | automation-blueprint | n8n_retellai.txt |
| 007 | Agent + tool-node pattern (research tool + data tool) | ai-tooling | ai_phone_call_assistant.txt |
| 008 | Trigger-logic taxonomy (webhook/form/chat/executeWorkflow) | automation-blueprint | master_prompt_agent_chat_input.txt |
| 009 | Multi-entry agent orchestration (chat + form -> one core) | automation-blueprint | master_prompt_agent_form_submission.txt |
| 010 | Model-tier routing (selector picks model before sub-agent) | ai-tooling | prompt_writing_agent_deep_reasoning.txt |
| 011 | Sub-workflow-as-tool composition (toolWorkflow + executeWorkflowTrigger) | automation-blueprint | master_prompt_agent_chat_input.txt |
| 012 | Structured-output parsing as a guardrail | ai-tooling | n8n_retellai.txt |
| 013 | IF / switch branching control flow | operator-process | n8n_retellai.txt |
| 014 | Airtable as structured data/state layer (memory-by-database) | automation-blueprint | ai_phone_call_assistant.txt |
| 015 | httpRequest outbound + respondToWebhook synchronous response | automation-blueprint | n8n_retellai.txt |
| 016 | Credential-reference architecture (named, scoped) | operator-process | ai_phone_call_assistant.txt |
| 017 | Perplexity research-tool integration (bounded live search) | ai-tooling | ai_phone_call_assistant.txt |
| 018 | Opportunity-card -> n8n-workflow-build bridge | client-application | n8n_retellai.txt |

## Cross-batch reinforcement summary

This mini-batch is the **automation IMPLEMENTATION layer** of the corpus and the build end of the 2026-05-19 demand-to-delivery spine.

| N8N chunk | Link |
|---|---|
| 001, 002, 006 voice agents | B2B 004-005 responsiveness-AI / voice-receptionist demand · the supply-side build |
| 010 model-tier routing | B2B cognitive-vs-responsiveness frame · match the model to the bottleneck |
| 018 card -> build bridge | OPPORTUNITY_MANAGEMENT_TEMPLATES (a cleared card becomes this build) + the full B2B -> OMT -> N8N spine |
| 007, 011 agent+tool / sub-workflow-as-tool | BATCH_006 automation-blueprint + the .claude/skills/ single-responsibility design |
| 012 structured-output guardrail · 013 branching · 016 credential scoping | BATCH_007 final-review / operational-locks / recurring-checklists discipline |
| Cluster B (003-005, 009-011) prompt agent | future PROMPT_TEMPLATES_DEEP (the prompt-craft content the agent consumes · keep separate) |

## Security note

Credential references are NAME-ONLY across all chunks and extracted files: `airtableTokenApi/The AI Edge`, `openAiApi/Ops Management`, `openAiApi/The AI Edge`, `perplexityApi/The AI Edge`, `openRouterApi/Prompt Engineer Agent`. No credential values, tokens, secrets, or pinData are present anywhere in this mini-batch's outputs (scan CLEAN · 0 hits).

## Excluded material (NOT chunked)

| Material | Reason |
|---|---|
| Credential value fields / auth headers / tokens | Stripped to names only · security |
| pinData (cached run data) | Skipped · may contain sample PII/transcripts |
| Node UUIDs / versionId / webhookId / canvas coordinates | Not durable signal |
| Prompt-craft CONTENT (the technique itself) | Belongs to future PROMPT_TEMPLATES_DEEP · this mini-batch chunks the agent IMPLEMENTATION |
| Prompt-template / literary intake sources | Out of scope · not touched |
