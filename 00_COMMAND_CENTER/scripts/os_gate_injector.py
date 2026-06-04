#!/usr/bin/env python3
"""os-gate-injector: UserPromptSubmit hook. Injects the mode->gate map BEFORE output starts,
so the model never has to remember which gates apply. Output goes into context."""
print("""[OS GATE INJECTOR] Classify the request via os-command-router, then apply the gates for that mode BEFORE answering:
- Strategy/Proof-loop: optionality-protection, proof-before-crowning, anti-old-lane-anchoring, identity-collapse, anti-hallucination(cite).
- Build/Automation: legal-risk, employer-conflict, completion-verification, cost/runaway, output-usefulness.
- Research: source-freshness, anti-hallucination(cite + date).
- Writing: voice (NO em-dashes, no AI-tell transitions), output-usefulness, identity-collapse.
- Design: visual reject/beat-source gates (os-vision-reject-gate), brand consistency.
- Recovery/Audit: completion-verification (manifest is the arbiter), reliability.
RULES: cite the doctrine/skill/gate used; disclose any unverified-pile dependency; do NOT crown a lane; today's proof + the operator's instruction override old docs.""")
