---
name: operator-review
description: Apply BJ's operating system to an OUTSIDE situation (a client, person, business, decision, offer, content system, or operating problem) and return an operator-grade diagnosis with a proof-first action plan. Use whenever BJ runs /operator-review, or asks to "run the Command Center on" someone else's situation, diagnose a client/prospect, or pressure a third party's business problem. This is an internal service-delivery skill: it lets BJ deliver his OS as a service to others. It is not a public product, it does not expose the private corpus, and it never claims the OS is magic or guaranteed.
disable-model-invocation: false
---

# Operator Review

Run BJ's operating system on someone else's situation and return a diagnosis plus a proof-first plan, in BJ's register: leverage-first, proof-first, no fluff, premium, honest. This is the first proprietary, client-facing skill and the seed of the future productized brain. Treat it as a service-delivery instrument BJ uses by hand, not an app and not a promise.

## What this skill is and is not
- **Is:** BJ's method applied to an outside problem. The corpus and advisor canon are the *method*; they are not the outsider's answer and are never quoted to them.
- **Is not:** a reveal of the private Command Center, a public product, or a guarantee. Never imply the OS is magic, proprietary AI, or a sure thing. The honesty is the credibility.

## Inputs
The outside situation: who they are, what they do, what they say the problem is, any numbers or constraints they shared. If critical context is missing (their real goal, their money model, their stage), ask one or two sharp questions before diagnosing rather than guessing.

## Steps (run in order)
1. **Classify** the client/problem type (e.g. positioning, pricing, offer, distribution, ops/leverage, hiring, build, trust/credibility, decision-fork).
2. **Separate stated problem from real problem.** What they asked is rarely the constraint. Name both.
3. **Route through the relevant OS lanes by job** (per `00_COMMAND_CENTER/OS_TRANSFORMATION_ROUTER.md` and `COMMAND_CENTER_COVERAGE_MANIFEST.md`): pull the matching corpus lanes from `01_KNOWLEDGE_BASE/MASTER_INDEX.md` and the relevant chunks. Use the method; do not surface the private docs themselves.
4. **Activate the right advisors/doctrines** from the canon (the `intel_*` memories): pricing/positioning to Enns (`intel_wwp_proclamations`, `intel_pricing_logic`); trust to Maister (`intel_trust_equation`, `intel_trust_mechanics`); leverage/stay-small to Naval/Jarvis (`intel_leverage_logic`, `intel_company_of_one`); distribution/launch to Thompson/Elberse (`intel_hit_mechanics`, `intel_blockbuster_strategy`); premium/status to de Botton + New Luxury + Sax (`intel_status_psychology`, `intel_new_luxury`, `intel_analog_premium`); client experience to Guidara (`intel_hospitality_layer`). Seat only the relevant ones.
5. **Pressure-test** the situation the way `/challenge` does: where does the obvious move drift, contradict sound doctrine, or rest on an untested assumption? For a high-stakes fork, run the multi-lens pass the way `/boardroom` does (seat 3 to 5 advisors, surface where they disagree).
6. **Find the highest-leverage constraint:** the one thing that, if moved, unlocks the most. Not a list, the single binding constraint.
7. **Diagnose:** state what is actually going on, plainly.
8. **Give the first 3 to 5 proof-first moves:** cheap, real-world tests and actions, ordered, that produce evidence fast. Bias to contact with reality over more planning.
9. **State what not to do:** the tempting moves that waste time or money here.
10. **State what data/proof would change the recommendation:** name the evidence that would flip the call, so the advice stays honest and falsifiable.

For durable outputs worth keeping (a repeatable client pattern, a sharp framing), offer to `/save` it to memory. Do not auto-write.

## Required output format
```
## Situation summary
[2-4 sentences, neutral.]

## Stated problem vs real problem
- Stated: [what they said]
- Real: [the actual constraint, named]

## OS routing receipt
- Level: [2-4]
- Category: [problem type]
- Lanes activated: [corpus lanes / MASTER_INDEX sections, by job]
- Advisor/doctrine lenses: [the intel_ memories actually used]
- Skipped (and why): [what you did not consult]
- Guardrails applied: [the relevant ones below]

## Diagnosis
[Plain. What is actually going on.]

## Highest-leverage constraint
[The single binding constraint.]

## Recommendation
[The call, 1-3 sentences. Clearly the recommendation, distinct from the diagnosis.]

## First 3 to 5 proof-first moves
1. [cheap, real, ordered]
...

## What not to do
- [tempting time/money wasters here]

## Proof that would change the call
- [the evidence that would flip the recommendation]

## Guardrails / uncertainty
[What is unknown, where the advice is a hypothesis not a guarantee, and the one or two questions worth answering next.]
```
Keep diagnosis, recommendation, proof-needed, and next-action visibly separate. Never blur "what I think is going on" with "what they should do" with "what would prove it."

## Guardrails (hard)
- **Read-only against the corpus.** Never write to `01_KNOWLEDGE_BASE/` (no chunking, no master mutation, no new domains), never touch `raw/`, never touch the held Bible (`SPIRITUAL_FOUNDATION`).
- **Never reveal or quote the private Command Center contents** to an outsider. The corpus is the method, not a handout. No private strategy, no internal doc text, no BASEPLATE internal plans leaked.
- **No employer confidential or internal information.** Industry knowledge and BJ's own experience are fine; the employer's pricing, architecture, procedures, client lists, or tooling are not. Apply the employment-boundary guardrails from `CURRENT_STATE.md`.
- **No fake certainty.** Every recommendation is a hypothesis until the proof move confirms it. Say so. Never imply the OS guarantees an outcome or is magic.
- **No generic advice.** If you cannot ground a point in a real lane or advisor doctrine, cut it. Generic answers defeat the purpose of the skill.
- **No platform/registry overclaim, no photography-only reduction, no automation before proof** in any recommendation you give.
- **Service-delivery first, not a public product.** This skill is how BJ delivers his OS by hand to a client. It is the seed of the eventual product, not the product. Do not present it as an app or a guarantee.
- This skill diagnoses and recommends; it does not commit, deploy, or mutate anything.

## How this fits the OS
This is the first proprietary skill that turns the internal operating skills (`/challenge`, `/save`, `/boardroom`) outward: the same machinery, pointed at someone else's problem, delivered as a service. Per `CURRENT_STATE.md` and `TRUE_BILLION_DOLLAR_THESIS.md`, the productized/app version is an earned later layer; this hand-delivered service is what proves the demand first. Run it; do not build the app ahead of the proof.
