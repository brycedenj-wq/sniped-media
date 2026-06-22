---
name: sniped-pricing-decision
description: Run a pricing decision through Blair Enns' 3-option architecture + premium-as-insurance frame. Use when user is preparing a quote, deciding on a proposal price, considering whether to discount, evaluating an Op Kit or Brand System pitch, or asking "what should I charge for X." Holds the $1,500 floor, refuses race-to-bottom moves, frames premium as insurance not cost.
---

# SNIPED Pricing Decision Skill

The Pricing Creativity playbook applied to a specific SNIPED situation. Output target: a 3-option pitch with anchored premium, defensible mid-tier, walkable low tier.

## MANDATORY READING

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_pricing_logic.md` · the Blair Enns 3-option architecture
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_wwp_proclamations.md` · positioning rules
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_status_psychology.md` · why founders pay premium
4. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_referral_handling.md` · Pearl-network floor protocol
5. `/Users/sniper/Downloads/    SNIPED_OS/01_OFFERS/delivery_architecture_v2.md` · the locked ladder (Reset / Sprint / Op Kit / Brand System)

## INVOKE WHEN
- User asks "what should I charge for X"
- User is drafting a proposal or quote
- User is considering discounting
- User mentions a prospect with budget constraints
- User asks about Op Kit, Brand System, or custom-tier pricing

## THE FRAME (from `intel_pricing_logic.md`)
- Three options, always. Never single quotes.
- Anchor premium first, mid second, walkable third
- Premium is positioned as insurance, not cost
- Reset $1,500 = floor. Pearl-network = scope flexes, price holds.
- Discounting destroys positioning · trade scope, never price
- Self-orientation (Trust Equation divisor) destroys deals · stay client-oriented

## OUTPUT
Three-option pitch with:
- Tier name
- Price
- Scope
- Best-for framing
- One-line why-this-tier

Plus: red flags if the prospect's situation suggests off-positioning (volume buyer, race-to-bottom, etc.).

## REFUSE
- Single-quote proposals (always 3 options)
- Discounting (trade scope instead)
- Volume language ("I'll do this many for $X")
- Anchoring below the $1,500 Reset floor
- Premium tier under $10K for Brand System (breaks the ladder)


## Inputs
- Scope description of what the prospect is asking for
- Any budget signal or constraint the prospect mentioned
- Prospect context: founder, brand, event, volume buyer, referral, etc.
- Offer tier under consideration: Reset / Sprint / Op Kit / Brand System
- Whether a discount is being contemplated (triggers refusal gate)

## Gates
- Single-quote proposals are REFUSED (always 3 options per Blair Enns architecture)
- Discounting is REFUSED (trade scope, never price)
- Reset floor of $1,500 is inviolable; no anchor below it
- Brand System premium must stay at or above $10K (ladder integrity); volume language refused regardless of prospect pressure

## Test
- case: Founder asks for personal brand photography and mentions she has 'about $1,200.' Expected: 3-option pitch with walkable low at $1,500 Reset (scope-trimmed, not discounted), mid at Sprint/Op Kit, premium Brand System anchor; red flag on sub-floor stated budget.
- expected failure: User asks to send a single-price quote at $900 to close a cost-sensitive prospect. Skill refuses: below the $1,500 floor, single-quote violates 3-option rule, discounting destroys positioning. No quote drafted.
