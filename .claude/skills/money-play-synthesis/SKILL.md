---
name: money-play-synthesis
description: Turn any money / product / venture / cash-play / AI-business / automation / scale question into ranked, doctrine-and-tool-grounded cash plays with honest tool-readiness labels. Use when the operator asks how to make money, what product or venture to build, for a cash play, an offer, pricing, monetization, recurring revenue, an AI business, automation, or how to scale. Auto-fires via the money_play domain in OS_ACTIVATION_INDEX; this skill is its invokable entry. NOT for delivering an already-chosen product (just build it) or non-money creative work.
---

# Money Play Synthesis

The OS already holds the money/offer/pricing/copy/status/creator/leverage doctrine, the Start Here and AI-money plays, the connector list, and the tool-readiness layer. This skill makes the OS USE them automatically for any money question, instead of generic strategy. Authority: `00_COMMAND_CENTER/OS_MONEY_PLAY_GATE.md`.

VALUE CHAIN (default frame): corpus = ingredients, OS = kitchen, owned world/product = the meal, audience/revenue = market response. The deliverable is an OWNED output built FROM the corpus. Do NOT recommend selling internal ingredients (SREF/prompt/doctrine packs, book summaries, workflow notes, field manuals, the OS) unless the operator explicitly asks. Default ranking = quality of owned asset, speed to test, low manual effort, employer safety, monetization potential, $300k path.

## INVOKE WHEN
- The operator asks how to make money, for a cash play, a product/venture to build, an offer, pricing, monetization, recurring revenue, an AI business, automation, or scaling.
- A money/product/venture answer is about to be given from generic reasoning instead of bound doctrine + a concrete tool advantage.
- Do NOT invoke for executing an already-chosen build, or for non-money creative production.

## Inputs
- The money/product/venture question.
- Bound doctrine: `OS_MONEY_OFFER_DOCTRINE.md`, `OS_OFFER_STACK.md`, `OS_PRICING_GATE.md`, `OS_STARTHERE_DOCTRINE.md`, `MONEY_PLAYS_OS_x_TOOLS_2026-06-02.md`, `OS_CAPABILITY_TOOL_ROUTING.md`, `CREATOR_AI_PRODUCTION_FIELD_MANUAL/FIELD_MANUAL.md`, `_reference/COLD_OUTREACH_ATOMS.md`, `_reference/COPY_DOCTRINE_CAPLES_TESTED_ADVERTISING.md`.
- Tool basis: `OS_TAKEOVER_PHASES_001/OS_TOOL_READINESS_LAYER.md` + `OS_TOOL_APP_INTEGRATION_LEDGER.csv`.
- Operator assets/access (the project capsule or packet, never permanent OS).

## Steps
1. Route through the money doctrine stack (offer/pricing/copy/status/trust/creator/leverage).
2. Retrieve the bound Start Here / AI-money / workflow / connector / tool-readiness material. No source re-runs.
3. For every play build a SOURCE + TOOL BASIS line: doctrine used, exact source file, confidence label, tool/connector, readiness label, manual-work-removed, how the OS executes it.
4. Label each tool: ready | untested | approval-gated | spend-gated | unavailable (grounded in the ledger, never invented). A play needing spend/send/deploy is not ready.
5. Rank by speed to money + repeatability + low manual effort + employer safety + OS/tool leverage (dual-primary = speed + low effort).
6. Downgrade bespoke service labor unless explicitly chosen; require fixed intake + fixed output; kill custom-puzzle-per-sale, SNIPED-Media/photo default, and anything that does not feed the owned faceless world.
7. Return exact offers (3-option anchor), exact messages (copy-clean), delivery steps, automation path, kill criteria, and $300k/year math. Serious asks run as a Workflow (generators -> hostile rank -> build -> adversarial verify -> receipt).

## Outputs
- Top N ranked cash plays + a top 3 to test this week.
- Per play: offer, buyer, message, price, delivery, automation/templating path, source+tool basis, readiness, kill criteria.
- $300k/year math (honest margin) and a single strongest next action. No lane crowned.

## Gates
- money-play-gate self-check: source_and_tool_basis_table_present, readiness_labels_honest, ranked_by_speed_and_low_effort, bespoke_downgraded, offers_messages_steps_automation_kill_300k_present, no_crown, no_em_dash.
- proof-before-price, floor-held, anti-hallucination(cite with confidence label), employer-conflict, no spend/send/deploy/post/generation before a real yes + operator approval.

## Test
- case: "what is the fastest low-effort way to make money with my skills and AI" -> `os_activate.py` fires domain=money_play with OS_MONEY_PLAY_GATE authority + the tool-readiness docs + injected pricing/trust/copy doctrine; the answer carries a source+tool basis table with honest readiness labels, ranks by speed+low-effort, downgrades bespoke, and ends with $300k math + a next action. No lane crowned.
- expected failure: a play labeled "ready" that actually needs Higgsfield spend or a Gmail send, OR a play with no doctrine/tool citation, must be downgraded or relabeled, not shipped. A casual non-money prompt (e.g. "edit this photo") must NOT trigger money mode (verified: stays light-touch).
