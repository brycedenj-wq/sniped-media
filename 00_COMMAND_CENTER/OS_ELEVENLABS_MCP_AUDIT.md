# OS ELEVENLABS MCP AUDIT

> Surveyed 2026-06-06. Status: **PREFERRED-PENDING** (not registered; one key away).

## What exists
- No ElevenLabs MCP registered (claude mcp list: absent). A nested copy lives at `~/Documents/BJ-WIKI/elevenlabs-mcp` (do not double-register).
- The OS has the voice-agent **blueprint** carded: ElevenLabs ConvAI + Twilio outbound-call n8n workflow (`POST /v1/convai/twilio/outbound-call`), post-call webhook -> transcript-summary -> structured JSON -> Airtable.

## Activation (the exact step)
1. ElevenLabs dashboard: create an API key **with the "11 Agents" / Agents write scope enabled** (the SDR/agent calls fail without it , this is the #1 gotcha).
2. `claude mcp add ElevenLabs -e ELEVENLABS_API_KEY=<key> -- uvx elevenlabs-mcp`
3. New Claude session.
4. Smallest safe proof: list voices / get user subscription (read-only, no character spend). That is the ACTIVE proof. Do NOT auto-generate audio or place a call.

## Capability once ACTIVE
TTS, voice clone, SFX, ConvAI agents, outbound calling (via Twilio). Professional default chain (carded): generate VO in ElevenLabs FIRST, then lip-sync/score downstream; clone with the delivery style you want.

## Known GAP (do not fake)
ElevenLabs **V3 emotional-tag syntax** (e.g. inline tags) and the **subtle / moderate / aggressive tag modes**, plus the exact UI location of the "11 Agents" scope toggle, are NOT in the OS corpus. They live in ElevenLabs' own docs. Pull and card them at activation time. Flagged in os_voice_agent_router as `V3_TAGS_PENDING_DOC`.

## Music engine
Undecided: Suno or Udio. Pick one before the sound lane is called complete. ElevenLabs covers VO + SFX, not melody/singing.

## Security
networked (API calls billed per character/minute). The full outbound-call SDR loop is networked/dangerous (real phone minutes, public webhook) , behind explicit go only. Redact the blueprint creator's leftover Airtable credential before any import.

## Route / gate
os_voice_agent_router.py (route) + os_audio_stack_gate.py (readiness gate). Cards: elv_* (7).
