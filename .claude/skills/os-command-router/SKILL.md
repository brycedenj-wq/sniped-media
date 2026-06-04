---
name: os-command-router
description: Route every request to the correct operating mode + tools + gates BEFORE answering, inside Bryce's OS. Use at the start of any non-trivial request to classify it (strategy/execution/research/critique/build/writing/design/automation/proof-loop/recovery), decide doctrine + web + tool routing, raise legal/employer-conflict and no-crown flags, pick the cost tier, and emit a one-line routing receipt. Prevents mode-mixing, un-cited claims, premature lane-crowning, identity exposure, and runaway cost.
---

# OS Command Router

Classify the request, then execute in exactly one mode. Emit the routing receipt first.

## Step 1, classify the mode (pick ONE)
- **Strategy** , "what should I / what's possible / which lane / rank options."
- **Execution** , a concrete task that advances state (make/edit/ship a thing).
- **Research** , needs facts, market, or current 2026 data.
- **Critique** , review / red-team / pressure-test an artifact.
- **Build** , create a skill, pipeline, tool, site, or automation.
- **Writing** , copy, article, caption, script (on-voice).
- **Design** , UI, visual, layout, brand asset.
- **Automation** , recurring / scheduled / agentic work.
- **Proof-loop** , design a test with 24h/7d, kill/keep/scale, money path.
- **Recovery / Audit** , something failed, verify completion, repair state.

## Step 2, answer the routing questions
1. Verified doctrine required? (default YES , cite it.)
2. Current web research required? (facts/market/2026-state , YES.)
3. Legal / ethical / employer-conflict risk? (employer-adjacent, identity-exposing, likeness-based, on company time/tools/data , RAISE the gate; may refuse/redirect.)
4. Must refuse to crown a lane? (any strategy/identity question , YES.)
5. Tool route , which MCP/local/web/manual per the tool-routing map (`OS_CAPABILITY_TOOL_ROUTING.md`).
6. Cost tier , haiku (cheap reads) / sonnet (synthesis) / opus (judgment, keep lean).
7. Output format + exit gate(s) for this mode (per `OS_SELF_OPTIMIZATION_ARCHITECTURE.md` Section 3).

## Step 3, emit the routing receipt (one line, before executing)
`ROUTE: mode=<mode> · doctrine=<docs/skills> · web=<yes/no> · risk=<none/legal/employer> · crown=<refuse/na> · tools=<...> · cost=<tier> · gates=<exit gates>`

## Step 4, execute in that mode only
- Strategy NEVER crowns; Execution NEVER invents strategy; Recovery NEVER fakes completion; Writing NEVER uses em-dashes.
- Run the mode's exit gate(s) (see `os-quality-gates`) before declaring done.
- Disclose any unverified-pile dependency. Cite the doctrine/skill/gate used.

## Refusal rule
Refuse only on a Class-A hard constraint (employer conflict, legal/IP/ToS violation, destructive action, credential/payment risk). Otherwise route, do not refuse. When in doubt on employer conflict or identity exposure, flag it and ask before proceeding.

## Pairs with
`os-quality-gates`, `os-token-safe-reader`, `OS_SELF_OPTIMIZATION_ARCHITECTURE.md`, `OS_CAPABILITY_TOOL_ROUTING.md`, and the memory rules (extraction-audit-gate, capability-growth-mandate, full-engagement-before-direction, possibility-engine-optionality).
