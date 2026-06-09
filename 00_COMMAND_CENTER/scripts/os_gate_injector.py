#!/usr/bin/env python3
"""os-gate-injector: UserPromptSubmit hook. THE EVERY-TURN BRIDGE.

Reads the user's prompt from stdin, classifies it via the activation index (os_activate.py),
and injects the EXACT activation set (authority doc + skills + docs + gates + tools + hard laws)
for that task, so the whole OS body fires as one unit instead of sitting unused. Falls back to
the static gate map if classification fails or no domain matches. Output goes into context
before the model answers."""
import sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))

STATIC = """[OS GATE INJECTOR] Classify the request via os-command-router, then apply the gates for that mode BEFORE answering:
- Strategy/Proof-loop: optionality-protection, proof-before-crowning, anti-old-lane-anchoring, identity-collapse, anti-hallucination(cite).
- Build/Automation: legal-risk, employer-conflict, completion-verification, cost/runaway, output-usefulness.
- Research: source-freshness, anti-hallucination(cite + date).
- Writing: voice (NO em-dashes, no AI-tell transitions), output-usefulness, identity-collapse.
- Design: visual reject/beat-source gates (os-vision-reject-gate), brand consistency.
- Recovery/Audit: completion-verification (manifest is the arbiter), reliability.
RULES: cite the doctrine/skill/gate used; disclose any unverified-pile dependency; do NOT crown a lane; today's proof + the operator's instruction override old docs."""

def main():
    raw = ""
    try:
        raw = sys.stdin.read()
    except Exception:
        pass
    prompt = ""
    try:
        prompt = (json.loads(raw) or {}).get("prompt", "") if raw.strip().startswith("{") else raw
    except Exception:
        prompt = raw
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("os_activate", os.path.join(HERE, "os_activate.py"))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        idx = m.load()
        if m.classify(prompt or "", idx):
            print(m.manifest(prompt or "", idx))
            return
    except Exception as e:
        sys.stderr.write(f"[os-gate-injector] activation fallback: {e}\n")
    print(STATIC)

if __name__ == "__main__":
    main()
