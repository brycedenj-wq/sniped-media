---
name: sniped-partnership-protocol
description: Evaluate a partnership / collab / co-marketing / referral arrangement against SNIPED's locked partnership protocol. Use when someone proposes a collab, a partnership offer comes in, or considering trade arrangements. The Pearl-network handling lives here too.
---

# SNIPED Partnership Protocol Skill

The "should we partner" decision. Output target: a yes/no with terms or a clean decline.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/PARTNERSHIP_PROTOCOL.md` · the locked protocol
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_referral_handling.md` · Pearl network rules
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_wwp_proclamations.md` · selectivity rules

## INVOKE WHEN
- Partnership offer received
- Collab proposal
- Co-marketing arrangement
- "Should we work with X"
- Referral chain decisions

## OUTPUT
- Yes/no with terms
- The lane fit check
- Scope trade negotiation (per Pearl network: scope flexes, price holds at $1,500 floor)
- Clean decline language if no

## REFUSE
- Partnerships that compromise positioning
- Free work for "exposure" without specific trade value
- Cross-promotion with off-positioning brands
- Partnerships violating the WWP "we will be selective" proclamation


## Inputs
- The incoming proposal: who is offering, what they are proposing (collab / co-marketing / referral / trade)
- Their positioning relative to SNIPED (brand, price tier, audience overlap)
- Whether any trade value or referral chain is on the table
- PARTNERSHIP_PROTOCOL.md read result (locked yes/no criteria)
- Pearl network rules and WWP selectivity proclamations (from mandatory memory files)

## Gates
- Positioning gate: partnership must not compromise SNIPED positioning (per WWP proclamations)
- Price-floor gate: scope may flex but price never drops below $1,500 (Pearl network rule)
- No-free-work gate: exposure-only trade without specific quantifiable value = automatic No
- Off-positioning brand gate: cross-promotion with brands outside SNIPED's tier = automatic No

## Test
- case: A mid-tier lifestyle brand DMs offering to feature SNIPED on their 40k-follower IG in exchange for a free half-day shoot. Expected output: No decision. Rationale: free work for exposure with no price floor met, cross-promotion at unclear tier; clean decline language drafted.
- expected failure: Proposal arrives with no information about the partner's brand, audience, or what they are offering. Skill halts: cannot evaluate lane fit or price floor without knowing the trade terms. Asks operator for the proposal details before proceeding.
