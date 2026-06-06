#!/usr/bin/env python3
"""
os_audio_stack_gate.py , the SOUND / AUDIO lane readiness gate.

Before any deliverable claims a sound/voice layer, this gate checks the audio stack is
actually present and reports PASS / BLOCK with the exact missing piece. Mirrors the other
compliance gates: it refuses an over-claim, it does not do creative work.

  os_audio_stack_gate.py check          , gate the audio/voice lane (PASS / BLOCK + reasons)
  os_audio_stack_gate.py check --voice  , stricter: require a live voice agent path too

No spend. No audio generated. Probe + verdict only.
"""
import sys, subprocess, shutil


def mcp_registered(sub):
    exe = shutil.which("claude")
    if not exe:
        return None
    try:
        out = subprocess.run([exe, "mcp", "list"], capture_output=True, text=True, timeout=30).stdout.lower()
        return sub.lower() in out
    except Exception:
        return None


CHECKS = [
    # (label, probe_fn, required_for_base, fix)
    ("ElevenLabs MCP (TTS/VO/agents)", lambda: mcp_registered("elevenlabs"), True,
     "create API key WITH '11 Agents' write scope -> claude mcp add ElevenLabs -e ELEVENLABS_API_KEY=<key> -- uvx elevenlabs-mcp -> new session"),
    ("Music engine chosen (Suno/Udio)", lambda: False, True,
     "decide Suno or Udio; ElevenLabs covers VO+SFX but not melody/singing"),
    ("V3 emotional tags documented", lambda: False, False,
     "pull V3 inline-tag syntax + subtle/moderate/aggressive modes from ElevenLabs docs (not in corpus)"),
    ("n8n-mcp (for SDR/booking flows)", lambda: mcp_registered("n8n"), False,
     "claude mcp add n8n-mcp -- node ~/n8n-mcp/dist/mcp/index.js -> new session"),
    ("Google Calendar MCP (booking)", lambda: mcp_registered("calendar"), False,
     "already connected via claude.ai Google Calendar"),
]


def check(strict_voice=False):
    results = []
    for label, fn, base_req, fix in CHECKS:
        ok = fn()
        results.append((label, ok, base_req, fix))

    print("AUDIO / VOICE STACK GATE")
    print("-" * 60)
    base_blockers = []
    voice_blockers = []
    for label, ok, base_req, fix in results:
        mark = {True: "PASS", False: "MISS", None: "????"}[ok]
        tag = "(required)" if base_req else "(optional)"
        print(f"  [{mark}] {label} {tag}")
        if base_req and ok is not True:
            base_blockers.append((label, fix))
        if strict_voice and ("ElevenLabs" in label or "n8n" in label) and ok is not True:
            voice_blockers.append((label, fix))

    print("-" * 60)
    blockers = base_blockers + [b for b in voice_blockers if b not in base_blockers]
    if not blockers:
        verdict = "PASS , audio stack ready" + (" (voice-agent path live)" if strict_voice else "")
        print(f"VERDICT: {verdict}")
        return 0
    print("VERDICT: BLOCK , the sound/voice lane is SEEDED, not live. Fix:")
    for label, fix in blockers:
        print(f"  - {label}: {fix}")
    print("Do NOT claim a sound/voice layer is shipped until these PASS. Live calls require explicit go.")
    return 1


def main():
    strict = "--voice" in sys.argv
    if len(sys.argv) >= 2 and sys.argv[1] == "check":
        sys.exit(check(strict_voice=strict))
    print(__doc__)


if __name__ == "__main__":
    main()
