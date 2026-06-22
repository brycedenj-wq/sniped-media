---
name: sniped-wwp-positioning
description: Apply Blair Enns' Win Without Pitching proclamations to a SNIPED positioning, sales, or selectivity decision. Use when user is considering a deal, drafting offer language, choosing whether to take a client, evaluating a referral, refining the pitch deck, or asks "should I take this work" / "is this on-brand." The 12 proclamations are the textbook for SNIPED's lane.
---

# SNIPED Win Without Pitching Skill

The premium-creative-services positioning playbook applied to SNIPED's specific situation. Output target: a clear yes/no with the proclamation that decided it.

## MANDATORY READING

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_wwp_proclamations.md` · the 12 proclamations
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_positioning_phrases.md` · phrase bank + failure modes
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_pricing_logic.md` · pricing as positioning lever

## INVOKE WHEN
- "Should I take this client / project?"
- "Is this on-brand?"
- "Can I just do X for cheaper this once?"
- Drafting Carrd copy, Op Kit pitch, MSA language
- A referral comes in that feels off-lane
- Deciding to walk from a deal
- "We can compete on price for this one"

## THE 12 PROCLAMATIONS (the lens)
Per `intel_wwp_proclamations.md`. Most-applicable to SNIPED daily situations:

1. **We will be selective.** Refuse off-positioning work. Refusal is positioning.
2. **We will replace presentations with conversations.** Don't pitch · diagnose.
3. **We will rethink what we sell.** SNIPED sells methodology + outcome, not photos.
4. **We will not be experts in everything for everyone.** LA founder portraits, full stop.
5. **We will not write proposals.** Three-option pitches per `intel_pricing_logic.md`.
6. **We will diagnose before we prescribe.** Direction Stack runs first.
7. **We will rethink the sales call.** The call is mutual qualification.
8. **We will be slow to enrich, quick to fire.** Bad-fit clients destroy positioning.
9. **We will not be afraid to give away our thinking.** LinkedIn POVs are the teaching layer.
10. **We will replace the salesperson with the expert.** BJ talks to leads, not a sales hire.
11. **We will charge for diagnostics.** Op Kit / Brand System tiers separate diagnostic from execution.
12. **We will have a point of view.** Refusal-positioning lever (anti-AI on client deliverables).

## OUTPUT
- Which 1-2 proclamations are most relevant
- The yes/no recommendation
- The specific language for declining (if no) or the angle (if yes)

## REFUSE
- Recommending compromise-of-positioning moves "just this once"
- Volume language ever
- Discounting framing ("but they could be a great client")
- Generic "go for it" advice without proclamation reference


## Inputs
- The deal, referral, or request being evaluated (what was asked, by whom, at what price point)
- The positioning question: should I take it, how should I price it, should I decline, or what language to use
- Any draft offer language, pitch deck copy, or MSA clause to audit
- Context: is this a one-off exception request or a pattern

## Gates
- Mandatory reads confirmed: intel_wwp_proclamations.md + intel_positioning_phrases.md + intel_pricing_logic.md
- Decision anchored to a specific proclamation number, not generic advice
- No 'just this once' compromise-of-positioning moves in the output
- No volume language or discounting framing in any output copy
- Price reduction never recommended as a trust or conversion lever

## Test
- case: User says: 'A referral from a Pearl-network contact: a non-LA founder wants headshots for his LinkedIn, budget $400. Should I take it?' Expected output: cites Proclamation 1 (We will be selective) and Proclamation 4 (LA founder portraits, full stop) for a clear no. Returns specific decline language that preserves the relationship, and recommends routing through the Pearl referral-handling protocol.
- expected failure: User says 'just tell me if I should do this' with no deal description, no prospect context, and no positioning question. Skill refuses to give a yes/no without data and asks for: what was requested, by whom, at what price, and whether anything feels off-lane.
