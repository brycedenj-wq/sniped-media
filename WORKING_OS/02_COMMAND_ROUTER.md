# 02_COMMAND_ROUTER · routing reference

A thin reference for how inputs route. The LIVE engine is the `sniped-command-router` skill (invoke via the Skill tool). Source docs: `SNIPED_OS/00_BRIEF/COMMAND_ROUTER.md` and `EXECUTION_GOVERNOR.md`, plus `00_COMMAND_CENTER/OS_ACTIVATION_INDEX.json`.

## The 15 input types

money_urgency, photo_artifact, active_shoot, business_idea, person_relationship, event_access, tool_decision, raw_material, product_idea, network_opportunity, personal_state_jobrisk, creative_concept, stuck_scattered, gap_fill_acquisition, opportunity_transformation.

## Classifier disambiguation

- Multi-fit: take the higher-stakes or more irreversible type first.
- money vs pricing: a need-cash-now input is money_urgency; a what-to-charge input is a tool/decision.
- tool vs raw_material: a thing to use is tool_decision; a thing to mine is raw_material.
- stuck or scattered: default to stuck_scattered, run a reset, do not start new work.

## Routing algorithm

classify, then input-or-task check, then check STANDING_ORDER and NEXT_ACTION (surface and require an operator override on conflict), then domain dispatch, then corpus retrieve (09), then skill inject (10 and OS_ACTIVATION_INDEX), then the anti-pattern filter, then the proof loop, then the money path if money is in scope.

## Liaison to OS_ACTIVATION_INDEX.json

hard_production_domains, emergency_triggers, serious_keywords, the conductor model, receipt-required-for-serious. The index runs scoped activation. Never dump the whole corpus.

## Anti-pattern filter (refuse)

sample-instead-of-whole-read; re-derivation when a spine already exists; audit-as-substitute-for-action; a new strategy doc when the lock holds.

## Dependency flag

`sniped-command-router` currently resolves from `SNIPED_OS/_skills` via the settings.local.json allowlist. Migration into `.claude/skills` is pending (see 10_SKILLS_INDEX.md).

Updated by: operator instruction when routing logic changes. This file is the reference model; the skill is the live decision engine.
