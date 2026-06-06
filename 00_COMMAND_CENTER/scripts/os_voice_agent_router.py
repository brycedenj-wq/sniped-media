#!/usr/bin/env python3
"""
os_voice_agent_router.py , the VOICE / SDR / BOOKING lane router.

A voice task must resolve to a concrete stack + readiness, never a vague "use 11Labs".
This router probes what is actually registered, prints the pipeline for the requested
intent, and reports readiness honestly (ACTIVE / PREFERRED-PENDING / BLOCKED).

  os_voice_agent_router.py status                 , probe the voice stack (what is live)
  os_voice_agent_router.py route "<intent>"       , the stack + pipeline for an intent
  os_voice_agent_router.py routes                 , list the known voice routes

Intents: tts / voiceover, clone, sdr / qualify / outbound-call, book / booking / calendar, support-agent.
No spend. No call is ever placed by this script , it only routes and reports.
"""
import sys, subprocess, shutil, os

HERE = os.path.dirname(os.path.abspath(__file__))

ROUTES = {
    "tts": {
        "name": "VOICEOVER (ElevenLabs TTS)",
        "stack": "ElevenLabs MCP -> (optional) Kling/HeyGen lip-sync",
        "pipeline": [
            "1. Generate VO in ElevenLabs FIRST (professional default), spell out numbers, emotion on full sentences.",
            "2. (optional) feed audio to lip-sync / score downstream.",
        ],
        "needs": ["elevenlabs_mcp"],
    },
    "clone": {
        "name": "VOICE CLONE",
        "stack": "ElevenLabs MCP (voice clone)",
        "pipeline": [
            "1. Record sample in the DELIVERY STYLE you want the clone to use (not neutral).",
            "2. Create clone -> get voice_id.",
            "3. Use voice_id in TTS / agent.",
        ],
        "needs": ["elevenlabs_mcp"],
    },
    "sdr": {
        "name": "AI SDR / OUTBOUND QUALIFY (dangerous: real calls, behind go)",
        "stack": "n8n + ElevenLabs ConvAI (or VAPI/Retell) + Twilio + Airtable",
        "pipeline": [
            "1. Form trigger -> opt-in check -> E.164 phone normalize + first-name extract (LLM).",
            "2. Store to Airtable.",
            "3. POST /v1/convai/twilio/outbound-call {agent_id, agent_phone_number_id, to_number}.",
            "4. Post-call webhook -> transcript_summary -> structured JSON (budget/timeline/...).",
            "5. IF interest high -> Gmail/Slack follow-up. Update Airtable. Confirmation SMS.",
        ],
        "needs": ["elevenlabs_mcp", "n8n", "twilio", "public_webhook", "explicit_go"],
    },
    "book": {
        "name": "BOOKING / CALENDAR",
        "stack": "Google Calendar MCP (live now) OR Cal.com + n8n webhook",
        "pipeline": [
            "1. Availability: Google Calendar list-events in a window -> compute gaps -> offer slots (sync, agent speaks them).",
            "2. On confirm: create event (Google Calendar MCP is CONNECTED now) or Cal.com webhook.",
            "3. Confirmation email/SMS.",
        ],
        "needs": ["google_calendar_mcp"],
    },
    "support": {
        "name": "SUPPORT AGENT (knowledge-base voice agent)",
        "stack": "ElevenLabs ConvAI agent + scraped KB",
        "pipeline": [
            "1. Scrape company info -> format knowledge base.",
            "2. Configure ElevenLabs agent + system prompt.",
            "3. Test call (behind go).",
        ],
        "needs": ["elevenlabs_mcp"],
    },
}

INTENT_KEYWORDS = {
    "tts": ["tts", "voiceover", "voice over", "narration", "speak", "read", "emotional"],
    "clone": ["clone", "my voice", "digital twin", "voice clone"],
    "sdr": ["sdr", "qualify", "outbound", "cold call", "lead", "sales agent", "call leads"],
    "book": ["book", "booking", "calendar", "schedule", "appointment", "meeting", "availability"],
    "support": ["support", "receptionist", "faq", "answer questions", "knowledge base agent"],
}


def mcp_registered(name_substr):
    exe = shutil.which("claude")
    if not exe:
        return None  # unknown
    try:
        out = subprocess.run([exe, "mcp", "list"], capture_output=True, text=True, timeout=30).stdout.lower()
        return name_substr.lower() in out
    except Exception:
        return None


def probe():
    eleven = mcp_registered("elevenlabs")
    gcal = mcp_registered("google calendar") or mcp_registered("calendar")
    n8n = mcp_registered("n8n")
    return {
        "elevenlabs_mcp": eleven,
        "google_calendar_mcp": gcal,
        "n8n": n8n,
        "twilio": False,            # not an MCP; set up inside n8n
        "public_webhook": False,    # operator infra
        "explicit_go": False,       # always requires a human go
    }


def fmt(v):
    return {True: "READY", False: "MISSING", None: "UNKNOWN"}[v]


def status():
    p = probe()
    print("VOICE STACK STATUS (probe):")
    print(f"  ElevenLabs MCP   : {fmt(p['elevenlabs_mcp'])}")
    print(f"  Google Cal MCP   : {fmt(p['google_calendar_mcp'])}")
    print(f"  n8n-mcp          : {fmt(p['n8n'])}")
    print(f"  Twilio (in n8n)  : set up inside n8n (not an MCP)")
    print("  V3 emotional tags: PENDING_DOC (not in corpus; pull from ElevenLabs docs at activation)")
    print("  Music engine     : UNDECIDED (Suno or Udio)")
    print()
    print("Booking is the only voice-adjacent route ACTIVE now (Google Calendar MCP connected).")
    print("TTS/clone/support = PREFERRED-PENDING (ElevenLabs key w/ '11 Agents' write scope).")
    print("SDR outbound = BLOCKED until n8n + Twilio + public webhook + explicit go.")


def route(intent_text):
    t = intent_text.lower()
    pick = None
    for key, kws in INTENT_KEYWORDS.items():
        if any(k in t for k in kws):
            pick = key
            break
    if not pick:
        print(f"No voice route matched '{intent_text}'. Try: tts / clone / sdr / book / support.")
        return
    r = ROUTES[pick]
    p = probe()
    missing = [n for n in r["needs"] if p.get(n) is False or p.get(n) is None]
    if "explicit_go" in r["needs"]:
        missing = list(dict.fromkeys(missing + ["explicit_go"]))
    readiness = "ACTIVE" if not missing else ("BLOCKED" if "explicit_go" in r["needs"] else "PREFERRED-PENDING")
    print(f"ROUTE: {r['name']}")
    print(f"STACK: {r['stack']}")
    print("PIPELINE:")
    for step in r["pipeline"]:
        print(f"  {step}")
    print(f"NEEDS: {', '.join(r['needs'])}")
    print(f"MISSING: {', '.join(missing) if missing else 'none'}")
    print(f"READINESS: {readiness}")
    if missing:
        print("NEXT: create ElevenLabs API key WITH '11 Agents' write scope -> claude mcp add ElevenLabs ... ; register n8n-mcp; no call without explicit go.")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "status":
        status()
    elif cmd == "routes":
        for k, r in ROUTES.items():
            print(f"  {k:8} -> {r['name']}")
    elif cmd == "route":
        if len(sys.argv) < 3:
            print("usage: os_voice_agent_router.py route \"<intent>\"")
            return
        route(" ".join(sys.argv[2:]))
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
