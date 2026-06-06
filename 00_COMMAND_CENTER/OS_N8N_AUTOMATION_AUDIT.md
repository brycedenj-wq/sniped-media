# OS N8N AUTOMATION AUDIT

> Surveyed 2026-06-06. Status: **PREFERRED-PENDING** (n8n-mcp built, unregistered).

## What exists
- `~/n8n-mcp` , MCP server bridging Claude to n8n's node library (1,851 nodes, 2,352 templates). `dist/` built, `node_modules` present.
- `~/n8n-skills` , 7 Claude Code skill packs teaching correct n8n workflow construction (expressions, MCP tool patterns, 5 architecture patterns).
- `~/self-hosted-ai-starter-kit` , Docker compose for a local n8n + Ollama + Qdrant + Postgres stack.

## What n8n does in the OS
The **workflow/automation backbone**. It is where the voice/SDR/booking lane actually runs: form trigger -> qualify -> outbound voice call -> post-call webhook -> structured extract -> Airtable -> booking (Cal.com/Google Calendar) -> confirmation SMS/email. n8n-mcp lets Claude **build and validate those workflows** without hand-wiring the UI.

## Activation tiers (smallest first)
1. **n8n-mcp knowledge tier** (no n8n instance, no Docker): `claude mcp add n8n-mcp -- node ~/n8n-mcp/dist/mcp/index.js` -> new session. Proof: ask it to search the ElevenLabs node + validate a node config. This unlocks workflow *authoring* with zero infra.
2. **n8n-skills tier**: register the skill packs; proof: `/n8n-workflow-patterns` designs a booking workflow with correct `$json.body` expressions.
3. **Live n8n tier** (Docker): only if you want a running instance. `docker compose config` dry-run first; then `docker compose up`. Networked, opens ports 5678/11434/6333/5432 , bind to 127.0.0.1.

## Key facts (carded)
- Webhook data lives under `$json.body` (the #1 n8n gotcha).
- `$fromAI()` lets the agent fill structured fields from unstructured transcripts.
- Router-agent pattern: cheap model routes to specialist agents.
- Guardrails both before (input) and after (output) the agent.
- Calendar availability = Google Calendar list-events in a window -> agent computes gaps -> returns slots (async=OFF so the agent can speak them).

## Security
networked. Live n8n + public webhooks = inbound exposure. Header-auth the MCP HTTP endpoint if ever exposed. Self-hosted kit secrets in `.env` (N8N_ENCRYPTION_KEY set once, never rotate). The full SDR call loop is dangerous (real calls) , behind explicit go.

## Route / gate
os_voice_agent_router.py routes the SDR/booking flow; os_audio_stack_gate.py checks readiness. Cards: n8n_* + the voice blueprint cards.
