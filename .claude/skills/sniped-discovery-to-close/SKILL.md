---
name: sniped-discovery-to-close
description: Walk SNIPED's BJ-side post-VIB closing playbook. Use when a VIB prospect responded yes, when user is on a discovery call, drafting a discovery follow-up, building the proposal, or asks "how do I close this deal." The discovery → diagnose → proposal → close sequence. Replaces presentations with conversations. Diagnoses before prescribing.
---

# SNIPED Discovery-to-Close Skill

The conversion mechanics from warm prospect to signed Reset / Op Kit / Brand System. Output target: a closed deal that fits the lane.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/03_OUTREACH/SOP_discovery_to_close.md` · the locked playbook
2. `/Users/sniper/Downloads/    SNIPED_OS/01_OFFERS/delivery_architecture_v2.md` · the offer ladder
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_wwp_proclamations.md` · proclamations 2, 6, 7, 11 (conversations, diagnose-before-prescribe, sales call as qualification, charge for diagnostics)
4. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_trust_equation.md` · keep self-orientation low
5. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_pricing_logic.md` · 3-option architecture

## INVOKE WHEN
- VIB prospect responded yes to one-pager
- Discovery call is booked
- Building the proposal
- Drafting closing follow-up
- "How do I move this from interested to signed"

## OUTPUT FLOW
1. **Discovery call structure** (30 min) · per the locked SOP
   - First 5 min: rapport + their context (NOT pitch)
   - Next 15 min: Direction Stack diagnostic (the 5 questions)
   - Next 5 min: surface what you heard, name the methodology fit
   - Last 5 min: hand-off · "I'll send a 3-option proposal in 24-48 hrs"

2. **Proposal** (within 48 hrs) · 3-option per `sniped-pricing-decision` skill
   - Anchored premium, defensible mid, walkable third
   - No 1-quote proposals
   - Sent via email with PDF attachment + Pixieset reference link

3. **Follow-up cadence**
   - Day +1: confirm receipt
   - Day +3: gentle check-in if no response
   - Day +7: clarifying question, not pressure
   - Day +14: walk away message ("not the right timing · happy to revisit")

4. **Close moment** · once verbal yes
   - Send contract via DocuSign / signed PDF
   - Deposit request (50% Reset / 30% Op Kit / 30% Brand System)
   - Calendar invite for shoot

## REFUSE
- Pitch-first discovery calls (always diagnose first)
- Single-quote proposals
- Closing aggressive language
- Lowering price to close · trade scope per `feedback_referral_handling`
- Closing prospects who don't fit the lane (refuse cleanly, don't force fit)


## Inputs
- VIB prospect name and the signal that triggered this step (responded yes to one-pager / call booked / verbal interest expressed)
- Any intel on the prospect: business type, what they saw, what they said
- Current funnel stage: pre-call prep / active call support / proposal draft / follow-up cadence / close moment

## Gates
- No pitch-first discovery calls: diagnosis must precede any prescription (WWP proclamation 6)
- No single-quote proposals: 3-option architecture required per sniped-pricing-decision
- No price reduction to close: trade scope instead; no aggressive closing language above the Day +14 walk-away ceiling
- Prospects who do not fit the lane must be refused cleanly, not force-fit into a product

## Test
- case: A founder named Darius responded yes to the VIB one-pager and a discovery call is booked for tomorrow. Expected output: a 30-min run-of-show with specific time blocks (5 min rapport / 15 min Direction Stack / 5 min surface-what-you-heard / 5 min hand-off), the exact hand-off line, and a reminder that the proposal goes out within 48 hrs with 3 options anchored to Op Kit as mid-tier.
- expected failure: If no prospect context is provided and the operator only says 'help me close,' the skill must ask what stage the deal is at and who the prospect is before producing any collateral. A generic discovery script without a named prospect and known stage is a refusal condition.
