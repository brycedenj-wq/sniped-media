#!/usr/bin/env python3
"""
N8N_AUTOMATION_SYSTEMS chunker · 6 n8n workflow JSON exports (The AI Edge)

Reads the 6 normalized extracted txt files and emits N8N_AUTOMATION_SYSTEMS_CHUNKS.jsonl
with the canonical 12-field schema.

Target: 18 chunks (range 15-25 per plan section 4).
Domains per plan section 5 (all pre-existing · no NEW domain):
  automation-blueprint (bulk · workflow architecture + integration/trigger/composition),
  ai-tooling (agent/tool/model-tier/parsing/research-tool),
  operator-process (branching control flow + credential hygiene),
  client-application (opportunity-card -> workflow-build bridge).

No credential values / tokens / secrets / pinData in any chunk · the extracted source already stripped them.
Em-dash sweep (Unicode U+2014) applied to output.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "N8N_AUTOMATION_SYSTEMS_CHUNKS.jsonl"

BATCH_ID = "N8N_AUTOMATION_SYSTEMS"
AUTHOR = "The AI Edge (n8n workflow templates)"
BASE_TAGS = ["n8n", "automation-blueprint", "the-ai-edge", "2026-05-19", "ai-tooling-aging-risk"]

F_VAPI = "ai_phone_call_assistant.txt"
F_RETELL = "n8n_retellai.txt"
F_CHAT = "master_prompt_agent_chat_input.txt"
F_FORM = "master_prompt_agent_form_submission.txt"
F_DEEP = "prompt_writing_agent_deep_reasoning.txt"
F_NORMAL = "prompt_writing_agent_normal_model.txt"

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


PER = "{} · n8n workflow (The AI Edge)"
PAT = "n8n Automation Systems · cross-workflow pattern"

# ===========================================================================
# PER-WORKFLOW ARCHITECTURE (5)
# ===========================================================================

add(1, PER.format("AI Phone Call Assistant"), F_VAPI, "automation-blueprint",
    "AI Phone Call Assistant (VAPI) · end-to-end voice-agent workflow architecture",
    ("A 17-node n8n workflow that wires a VAPI voice agent to an n8n brain. Two webhooks (a Vapi Tool "
     "Trigger and a Vapi End Of Call Report) plus a form trigger feed a langchain AI Agent (gpt-4.1-mini) "
     "that has a Perplexity search tool and an Airtable create-record tool; the agent responds "
     "synchronously via respondToWebhook back to Vapi. A separate path stores the end-of-call report in "
     "Airtable, then runs an IF. An outbound httpRequest POSTs to the VAPI call API to trigger a call from "
     "a form submission. The agent's job: capture the customer's budget, area of interest, and name into "
     "named Airtable columns during the call."),
    ("To put an AI voice agent in front of a business, treat the voice provider (VAPI) as the telephony "
     "layer and n8n as the brain + memory: a webhook hands each turn to an agent equipped with a data tool "
     "(write structured fields) and a research tool, and respondToWebhook returns the reply in real time. "
     "Persist the call outcome to a database for follow-up."),
    ("The supply-side implementation of the responsiveness-AI category B2B_POSITIONING_CLAUDE_OPERATOR "
     "named (chunks 004-005: AI voice receptionist / missed-call text-back). This is the concrete build "
     "behind an OPPORTUNITY_MANAGEMENT_TEMPLATES hopper row with 'Proposed Vendor: n8n'. Pairs with the "
     "BATCH_006 ElevenLabs voice-agent blueprint as the n8n-native cousin."),
    ["You are a helpful assistant, you need to store all of the key information in the Airtable tool that you have access to. Please store the customer's budget and the area they are interested in within the interested in column and the customer name in the customer name column.",
     "httpRequest :: Vapi Call :: method=POST url=https://api.vapi.ai/call",
     "Step 1: Connecting into Vapi | Step 2: Activities Webhook | Step 3: Triggering a call"],
    ["voice-agent", "vapi", "ai-receptionist", "responsiveness-ai", "langchain-agent", "airtable-data-layer"])

add(2, PER.format("n8n & RetellAI"), F_RETELL, "automation-blueprint",
    "n8n & RetellAI · voice-agent workflow architecture with a follow-up branch",
    ("A 23-node workflow · the larger voice-agent sibling, wired to RetellAI. A custom-function webhook "
     "hands turns to the AI Agent (gpt-4.1-mini + Perplexity + Airtable tools), which responds via "
     "respondToWebhook. An activities webhook feeds a Status-of-Call switch that branches to a "
     "User-Hung-Up IF and a Store-End-Of-Call-Report Airtable write; that feeds a 'Follow Up?' LLM chain "
     "(keyed on End Reason + Transcript fields) gated by a structured-output parser and a final IF. An "
     "outbound httpRequest POSTs to the RetellAI create-phone-call API. Same 3-step scaffold as the VAPI "
     "build (connect provider, activities webhook, trigger call)."),
    ("Add a post-call intelligence layer to a voice agent: branch on call status, persist the transcript "
     "and end reason, then run a follow-up decision through an LLM gated by a structured-output schema. "
     "The provider (RetellAI vs VAPI) is swappable; the n8n scaffold (webhook in, agent core, data "
     "persistence, follow-up branch, API out) stays the same."),
    ("The richest responsiveness-AI exemplar in the corpus · directly the B2B missed-call/voice-receptionist "
     "demand made real. The Follow-Up branch is the automated equivalent of the SNIPED capture-to-delivery "
     "follow-up discipline (B7). A cleared OPPORTUNITY_MANAGEMENT_TEMPLATES card with vendor n8n becomes "
     "this build."),
    ["Your objective is to complete the task of storing information into airtable or searching the internet based on the users request. When searching the internet please keep the responses concise (1 -2 sentences max) and easy to understand for the user.",
     "httpRequest :: Call Customer :: method=POST url=https://api.retellai.com/v2/create-phone-call",
     "Status of Call -> ['User Hung Up', 'Store End Of Call Report Info']"],
    ["voice-agent", "retellai", "ai-receptionist", "responsiveness-ai", "follow-up-branch", "structured-output-parser"])

add(3, PER.format("Master Prompt Agent (Chat Input)"), F_CHAT, "automation-blueprint",
    "Master Prompt Agent · chat-input entry orchestrator",
    ("An 8-node workflow (internal name 'Prompt Writing Agent - Text Input'). A chatTrigger receives a "
     "message, a Basic LLM Chain (with a Formatting Brain model + a JSON-structure output parser) "
     "pre-processes it, then a Master Prompt Agent (OpenRouter 'Multi AI Brain') routes the request to one "
     "of two toolWorkflow sub-agents (Normal Models or Deep Reasoning Models) and returns the response to "
     "the user. The master agent's only job is to pick the right sub-workflow and relay the result."),
    ("Build a conversational front door as a thin router: a chat trigger -> a normalize/format pass with a "
     "structured-output parser -> a master agent whose sole responsibility is selecting and invoking the "
     "right specialist sub-workflow. Keep the orchestrator dumb and the specialists deep."),
    ("The multi-entry agent pattern that mirrors the SNIPED skill-routing instinct (a thin dispatcher over "
     "specialist skills · cf. the .claude/skills/ layer). Cluster B is the n8n implementation of a "
     "prompt-engineering agent · the future PROMPT_TEMPLATES_DEEP mini-batch is the prompt-craft content "
     "such an agent would consume."),
    ["You are a master prompt writing agent. You have 2 sub execution workflows that can develop the best prompts for the users depending on if they are wanting to use a deep reasoning model or a normal model. Your objective is to trigger these workflows accordingly and show the response back to the user.",
     "When chat message received -> ['Basic LLM Chain'] -> ['Master Prompt Agent']"],
    ["chat-trigger", "agent-routing", "tool-workflow", "prompt-engineer-agent", "orchestrator"])

add(4, PER.format("Master Prompt Agent (Form Submission)"), F_FORM, "automation-blueprint",
    "Master Prompt Agent · form-submission entry orchestrator",
    ("A 6-node workflow (internal name 'Prompt Engineer Agent - Form Master'). A formTrigger captures the "
     "request, the same Master Prompt Agent (OpenRouter) routes it to the Normal Models or Deep Reasoning "
     "Models toolWorkflow sub-agents, and a form node renders the usable output. It is the form-based "
     "twin of the chat-input orchestrator · same agent core, different entry surface."),
    ("Expose the same agent core through more than one entry surface (chat AND form) so users meet it where "
     "they are, while the routing logic and specialist sub-workflows stay single-sourced. One brain, "
     "multiple front doors."),
    ("Demonstrates the entry-surface-agnostic agent design that the SNIPED operator engine favors: the "
     "logic lives once, the triggers are interchangeable. Pairs with the OPPORTUNITY_MANAGEMENT_TEMPLATES "
     "card -> build pattern (a form is the simplest intake surface)."),
    ["You are a master prompt writing agent. You have 2 sub execution workflows that can develop the best prompts for the users depending on if they are wanting to use a deep reasoning model or a normal model.",
     "Capture Request -> ['Master Prompt Agent'] -> ['Output Prompt/Useable Output']"],
    ["form-trigger", "agent-routing", "tool-workflow", "multi-entry", "prompt-engineer-agent"])

add(5, PER.format("Prompt Writing Agent (Deep Reasoning + Normal tiers)"), F_DEEP, "automation-blueprint",
    "Prompt Writing Agent sub-workflows · deep-reasoning vs normal model tiers",
    ("Two near-identical 6-node sub-workflows, each invoked via an executeWorkflowTrigger (so they run as "
     "callable tools of the master agent). Each runs a Basic LLM Chain 'model selector' that analyses the "
     "request and outputs the single best model name with no extra text, a Set node that specifies the "
     "latest models, then a prompt-writing agent. The Deep Reasoning tier structures output for OpenAI "
     "deep-reasoning models; the Normal tier (model google/gemini-flash-1.5) structures a "
     "Goal/Role/Tone/Formatting/Instructions/Context/Examples scaffold for fast/cost-optimised use."),
    ("Split a capability into model-tier specialists (deep-reasoning vs fast/cheap) behind a common "
     "interface, and let an upstream selector pick the tier per request. Each specialist owns its own "
     "output structure. This keeps cost and latency matched to the task without the caller deciding."),
    ("The model-tier specialization pattern · the operating analog of the SNIPED 'right tool for the right "
     "job' discipline (intel_ai_sentiment hybrid-operator stance) applied inside an automation. Backs the "
     "B2B cognitive-vs-responsiveness frame: match the model to the bottleneck."),
    ["Your Objective is to analyse the request from the user and identify the most suitable model based on the options below for the AI Agent to leverage. You are to output the best model for this use case with no additional information.",
     "You need to structure the prompt in the following way: #Goal/objective ##Role ##Tone ##Formatting ##Instructions ##Context ##Examples (between 5 - 20 inputs and output examples) #Critical Information",
     "When Executed by Another Workflow -> ['Specify the latest Deep Reasoning Models'] -> ['Basic LLM Chain']"],
    ["model-tier-routing", "execute-workflow-trigger", "sub-workflow-as-tool", "prompt-engineer-agent", "ai-tooling"])

# ===========================================================================
# CROSS-CUTTING PATTERNS (13)
# ===========================================================================

add(6, PAT, F_RETELL, "automation-blueprint",
    "Voice-agent integration pattern · the 3-step provider scaffold (connect, activities webhook, trigger call)",
    ("Both voice workflows share an identical 3-step build scaffold documented in their sticky notes: "
     "Step 1 connect into the provider (VAPI or RetellAI), Step 2 stand up an activities webhook to receive "
     "events, Step 3 trigger an outbound call via the provider API. The provider is swappable · VAPI posts "
     "to api.vapi.ai/call, RetellAI to api.retellai.com/v2/create-phone-call · but the n8n shape (inbound "
     "webhook -> agent -> respond, plus an outbound httpRequest to start calls) is constant."),
    ("Standardise voice-agent builds on a provider-agnostic 3-step scaffold: connect the provider, receive "
     "events through an activities webhook, and trigger calls through the provider API. Treat the telephony "
     "vendor as a swappable adapter so the brain (n8n agent + data layer) is reused across VAPI, RetellAI, "
     "or the next provider."),
    ("A reusable SNIPED build blueprint for the responsiveness-AI offer (B2B 004-005). Vendor-agnostic "
     "scaffolding is the leverage move (intel_leverage_logic) · build the brain once, swap the adapter."),
    ["Step 1: Connecting into Vapi / Connecting into Retell AI",
     "Step 2: Activities Webhook",
     "Step 3: Triggering a call"],
    ["voice-agent", "vapi", "retellai", "integration-pattern", "provider-adapter", "responsiveness-ai"])

add(7, PAT, F_VAPI, "ai-tooling",
    "The langchain agent + tool-node pattern · an agent core with a research tool and a data tool",
    ("Across the workflows the recurring AI primitive is a langchain agent wired to a chat model plus "
     "purpose-specific tool nodes: a Perplexity search tool for live research and an Airtable tool for "
     "reading/writing structured records. The model, the research tool, and the data tool all connect INTO "
     "the agent node, which orchestrates them per the system prompt and returns one response."),
    ("Compose an AI agent from a model plus a small set of explicit tools (one for research, one for data) "
     "rather than a monolithic prompt. The agent decides which tool to call; each tool has a single clear "
     "job. This is the durable shape regardless of which model or vendor backs it."),
    ("The canonical agent-with-tools shape · the same hybrid-operator instinct the SNIPED corpus encodes "
     "(AI for retrieval + structured action, not freeform). Extends the BATCH_006 automation-blueprint "
     "domain with the agent+tool primitive."),
    ["Tool nodes: Perplexity Search (perplexityTool) + Create a Record (airtableTool)",
     "OpenAI Chat Model -> ['AI Agent'] ; Perplexity Search -> ['AI Agent'] ; Create a Record -> ['AI Agent']"],
    ["langchain-agent", "agent-tool-pattern", "perplexity-tool", "airtable-data-layer", "ai-tooling"])

add(8, PAT, F_CHAT, "automation-blueprint",
    "Trigger-logic taxonomy · webhook, formTrigger, chatTrigger, executeWorkflowTrigger",
    ("The 6 workflows use four distinct trigger types, each fit to a job: webhook (event from an external "
     "system · e.g. a voice provider's tool call or activities feed), formTrigger (a structured human "
     "submission), chatTrigger (a conversational message), and executeWorkflowTrigger (invocation as a "
     "sub-workflow tool by another workflow). The trigger choice defines the entry contract of the "
     "automation."),
    ("Choose the trigger by who/what initiates: external system -> webhook; human structured input -> form "
     "trigger; conversational input -> chat trigger; composed-by-another-workflow -> executeWorkflow "
     "trigger. The trigger is the automation's interface definition · pick it deliberately, not by habit."),
    ("A reusable decision rule for any SNIPED automation build · the entry contract is a design decision, "
     "not an afterthought. Maps to the operator discipline of defining the interface before the internals."),
    ["chatTrigger :: When chat message received",
     "executeWorkflowTrigger :: When Executed by Another Workflow",
     "webhook :: Retell AI Activities Webhook ; formTrigger :: On form submission"],
    ["trigger-logic", "webhook", "form-trigger", "chat-trigger", "execute-workflow-trigger"])

add(9, PAT, F_FORM, "automation-blueprint",
    "Multi-entry agent orchestration · one agent core behind chat and form front doors",
    ("The Prompt Engineer Agent is exposed through two separate workflows · a chat-input version and a "
     "form-submission version · that both route into the same Master Prompt Agent core with the same two "
     "toolWorkflow sub-agents. The entry surface differs; the routing logic and specialists are "
     "single-sourced."),
    ("Decouple the entry surface from the agent core. Ship multiple thin entry workflows (chat, form, "
     "webhook) that all hand off to one shared agent + specialist set, so behavior stays consistent and is "
     "maintained in one place. New channels are cheap; the brain is not duplicated."),
    ("The entry-surface-agnostic design the SNIPED operator engine favors · logic lives once, triggers are "
     "interchangeable. Lowers the cost of meeting a client on their preferred channel."),
    ["Master Prompt Agent (chat-input) and Master Prompt Agent (form-submission) share the same Normal Models + Deep Reasoning Models toolWorkflow sub-agents",
     "Capture Request -> ['Master Prompt Agent']"],
    ["multi-entry", "agent-routing", "single-source-logic", "orchestrator", "tool-workflow"])

add(10, PAT, F_DEEP, "ai-tooling",
    "Model-tier routing · an upstream selector picks the model before the sub-agent runs",
    ("Inside each sub-workflow a Basic LLM Chain acts as a model selector: it analyses the request and "
     "outputs ONLY the single best model name (no extra text), which a Set node resolves to the latest "
     "model id before the prompt-writing agent runs. The deep-reasoning path selects an OpenAI "
     "deep-reasoning model; the normal path selects a fast/cost-optimised model (e.g. "
     "google/gemini-flash-1.5)."),
    ("Make model selection an explicit, programmatic step: a small selector LLM reads the request and emits "
     "just the model name, decoupling 'which model' from 'do the task.' This lets cost/latency/quality be "
     "tuned per request and the model roster be updated in one Set node without touching the agent."),
    ("The operational form of the B2B cognitive-vs-responsiveness frame and the SNIPED right-tool-for-the-job "
     "discipline · match the model to the request. The selector-as-its-own-step pattern is reusable across "
     "any SNIPED multi-model automation."),
    ["You are to output the best model for this use case with no additional information. E.g. Only output '{{ $json['OpenAI Model'] }}' if they want a very deep reasoning model from OpenAI.",
     "Set :: Specify the latest Deep Reasoning Models / Specify the latest Models"],
    ["model-tier-routing", "model-selector", "ai-tooling", "cost-latency-tuning", "cognitive-vs-responsiveness"])

add(11, PAT, F_CHAT, "automation-blueprint",
    "Sub-workflow-as-tool composition · toolWorkflow + executeWorkflowTrigger",
    ("The master agent treats whole workflows as tools: each specialist is a toolWorkflow node on the "
     "master side and an executeWorkflowTrigger entry on the specialist side. This composes agents like "
     "functions · the orchestrator calls a sub-workflow, the sub-workflow runs its own model + logic and "
     "returns a result · enabling reuse and independent iteration of each specialist."),
    ("Compose automations like software functions: expose a specialist as a callable sub-workflow "
     "(executeWorkflowTrigger) and invoke it from an orchestrator as a toolWorkflow. This gives "
     "encapsulation, reuse, and the ability to evolve a specialist without touching its callers."),
    ("The modular-composition discipline that keeps automations maintainable · the same separation-of-"
     "concerns the SNIPED skill layer (.claude/skills/) uses. A specialist sub-workflow is the automation "
     "analog of a single-responsibility skill file."),
    ["toolWorkflow :: Normal Models ; toolWorkflow :: Deep Reasoning Models",
     "executeWorkflowTrigger :: When Executed by Another Workflow"],
    ["sub-workflow-as-tool", "tool-workflow", "execute-workflow-trigger", "composition", "modularity"])

add(12, PAT, F_RETELL, "ai-tooling",
    "Structured-output parsing as a guardrail · enforcing schema on agent output",
    ("Multiple workflows attach an outputParserStructured node to constrain LLM output to a defined schema "
     "before it flows downstream · the chat orchestrator parses to a JSON structure before routing, and "
     "the RetellAI follow-up branch parses the LLM output before the decision IF. The parser is the "
     "guardrail that makes non-deterministic model output safe to branch on."),
    ("Never branch business logic directly on raw LLM text. Put a structured-output parser between the "
     "model and any downstream decision so the output conforms to a known schema · this is the minimum "
     "guardrail that turns a probabilistic model into a dependable workflow component."),
    ("The guardrail discipline the SNIPED corpus prizes (executing-with-care · gate the non-deterministic). "
     "Structured output before action is the automation equivalent of final-review before ship (B7)."),
    ["outputParserStructured :: Structured Output (RetellAI follow-up) ; JSON Structure (chat orchestrator)",
     "Structured Output -> ['Follow Up?']"],
    ["structured-output-parser", "guardrail", "schema-enforcement", "ai-tooling", "deterministic-branching"])

add(13, PAT, F_RETELL, "operator-process",
    "IF / switch branching control flow · routing on call status and outcome",
    ("The RetellAI workflow shows the control-flow layer: a Status-of-Call switch routes to a User-Hung-Up "
     "IF and a store-report path, and a 'Follow Up?' decision (LLM + structured parser) feeds a final IF. "
     "Branching is keyed on real signals · call End Reason, transcript content, call status · so the "
     "automation reacts differently to a completed call, a hang-up, or a follow-up-needed outcome."),
    ("Encode the decision tree explicitly with switch/IF nodes keyed on concrete signals (status, end "
     "reason, parsed flags) rather than letting an agent implicitly decide everything. Explicit branches "
     "are auditable, testable, and fail predictably · the opposite of a black-box agent."),
    ("Maps to the SNIPED operational-locks + recurring-checklists discipline (B7) · automations must have "
     "explicit, auditable branches, not implicit trust. The follow-up branch is the automated form of the "
     "capture-to-delivery follow-up cadence."),
    ["switch :: Status of Call -> ['User Hung Up', 'Store End Of Call Report Info']",
     "if :: User Hung Up ; chainLlm :: Follow Up? (keyed on End Reason + Transcript)"],
    ["if-switch-branching", "control-flow", "operator-process", "auditable-automation", "follow-up-branch"])

add(14, PAT, F_VAPI, "automation-blueprint",
    "Airtable as the structured data / state layer · memory-by-database",
    ("Airtable is the persistence layer across the voice workflows · an airtableTool lets the agent create "
     "records mid-call (customer name, budget, area of interest into named columns), and an airtable node "
     "stores the end-of-call report (base 'n8n & Vapi Demo', table 'End Of Call Report'). The database, "
     "not the model context, is where durable state lives."),
    ("Give an agent durable memory through a structured database rather than relying on context windows: a "
     "data tool writes fields during the interaction and a separate node persists the outcome record. The "
     "database schema (named columns) is the contract for what the agent must capture."),
    ("Memory-by-database is the dependable alternative to context memory · it pairs with the "
     "OPPORTUNITY_MANAGEMENT_TEMPLATES intake discipline (capture named fields) and the SNIPED Notion-CRM "
     "schema thinking (B7). Note: no dedicated memory node and no MCP node are present · the database tool "
     "IS the memory layer here."),
    ["airtableTool :: Create a Record",
     "airtable :: Store End Of Call Report Info :: base=n8n & Vapi Demo table=End Of Call Report op=create",
     "store the customer's budget and the area they are interested in within the interested in column and the customer name in the customer name column"],
    ["airtable-data-layer", "memory-by-database", "structured-storage", "state-layer", "automation-blueprint"])

add(15, PAT, F_RETELL, "automation-blueprint",
    "httpRequest outbound actions + respondToWebhook synchronous response",
    ("The action layer has two shapes: respondToWebhook returns the agent's reply synchronously to the "
     "voice provider in real time (so the caller hears it during the call), and httpRequest POSTs to the "
     "provider API (api.vapi.ai/call, api.retellai.com/v2/create-phone-call) to trigger outbound calls. "
     "Synchronous respond for the live turn; httpRequest for side-effecting external actions."),
    ("Separate the synchronous response path (respondToWebhook · what the user gets back now) from the "
     "outbound action path (httpRequest · the side effects on external systems). Real-time interactions "
     "need the synchronous return; everything else is an explicit outbound call you can log and gate."),
    ("The request-response vs side-effect separation is the automation form of the SNIPED "
     "executing-with-care principle · synchronous replies are cheap and reversible, outbound API calls are "
     "side-effecting and should be explicit. Reusable for any real-time SNIPED automation."),
    ["respondToWebhook :: Respond to Retell AI / Respond to Vapi",
     "httpRequest :: Call Customer :: method=POST url=https://api.retellai.com/v2/create-phone-call"],
    ["http-request", "respond-to-webhook", "synchronous-response", "outbound-action", "automation-blueprint"])

add(16, PAT, F_VAPI, "operator-process",
    "Credential-reference architecture · named, provider-scoped credentials",
    ("Credentials are referenced by named, provider-scoped entries rather than inline secrets · e.g. "
     "airtableTokenApi/'The AI Edge', openAiApi/'Ops Management', perplexityApi/'The AI Edge', "
     "openRouterApi/'Prompt Engineer Agent'. The same provider can have multiple named credentials scoped "
     "to different purposes (two distinct OpenAI credentials appear). No secret values live in the "
     "workflow JSON · only the reference."),
    ("Scope credentials by purpose and name them meaningfully so access is legible and revocable · never "
     "inline secrets into the workflow. Multiple named credentials per provider let you isolate blast "
     "radius (one per project/agent) and rotate without touching the workflow."),
    ("The ops-hygiene discipline behind any safe SNIPED automation · named, scoped, revocable credentials "
     "map to the operational-locks discipline (B7) and the security-conscious posture the corpus requires. "
     "Confirms why the extraction strips values to names only."),
    ["airtableTokenApi/The AI Edge, openAiApi/Ops Management, perplexityApi/The AI Edge",
     "openRouterApi/Prompt Engineer Agent"],
    ["credential-scoping", "ops-hygiene", "operator-process", "security", "revocable-access"])

add(17, PAT, F_VAPI, "ai-tooling",
    "Perplexity research-tool integration · live-search augmentation of the agent",
    ("A Perplexity search tool is attached to the voice agents so the agent can augment its answers with "
     "live web search during a call, with the instruction to keep responses concise (1-2 sentences) and "
     "easy to understand. Research is a bounded tool the agent calls when needed, not a separate workflow."),
    ("Give an agent a live-search tool when freshness matters, but constrain the output length and clarity "
     "explicitly in the prompt so research augmentation does not bloat a real-time interaction. Bounded, "
     "instructed tool use beats unbounded retrieval."),
    ("The retrieval-augmentation pattern · pairs with the SNIPED hybrid-operator stance (AI for retrieval + "
     "structured action). The conciseness constraint mirrors the SNIPED restraint discipline applied to "
     "machine output."),
    ["perplexityTool :: Perplexity Search",
     "When searching the internet please keep the responses concise (1 -2 sentences max) and easy to understand for the user."],
    ["perplexity-tool", "live-search", "retrieval-augmentation", "ai-tooling", "bounded-tool-use"])

add(18, PAT, F_RETELL, "client-application",
    "The opportunity-card to n8n-workflow-build bridge · demand becomes a build",
    ("These workflows close the 2026-05-19 loop: the OPPORTUNITY_MANAGEMENT_TEMPLATES hopper logs ideas "
     "with a 'Proposed Vendor' column that literally lists n8n, and a cleared one-page opportunity card "
     "(with named sign-off, RAG, dependencies) becomes a build spec · these voice and agent workflows are "
     "what gets built. The B2B responsiveness-AI demand (missed-call/voice receptionist) is implemented "
     "here; the AI Edge credential provenance ties the templates and the workflows to the same source."),
    ("Treat a cleared opportunity card as the spec for a workflow build: the card's expected benefits, "
     "dependencies, and KPIs become the workflow's success criteria, and the hopper's vendor choice (n8n) "
     "becomes the build platform. Intake -> ROI -> card -> readiness gate -> n8n build is one continuous "
     "pipeline."),
    ("The capstone cross-batch link of the 2026-05-19 intake · B2B (demand) -> OPPORTUNITY_MANAGEMENT_"
     "TEMPLATES (intake/ROI/readiness) -> N8N_AUTOMATION_SYSTEMS (build). This is the demand-to-delivery "
     "spine for any SNIPED systems-as-leverage offer · a 3-hop retrieval path now exists end to end."),
    ["Proposed Vendor: n8n (OPPORTUNITY_MANAGEMENT_TEMPLATES hopper) -> a cleared opportunity card -> this workflow build",
     "httpRequest :: Call Customer :: method=POST url=https://api.retellai.com/v2/create-phone-call"],
    ["opportunity-card-to-build", "client-application", "responsiveness-ai", "demand-to-delivery", "systems-as-leverage"])


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
