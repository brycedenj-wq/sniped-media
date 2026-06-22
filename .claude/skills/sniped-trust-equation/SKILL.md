---
name: sniped-trust-equation
description: Diagnose a client / prospect situation through David Maister's Trust Equation · T = (Credibility + Reliability + Intimacy) / Self-Orientation. Use when user describes a stuck deal, a cooling lead, a difficult client conversation, or asks "why isn't this prospect moving" / "what's wrong with this pitch." Identifies which divisor is dragging trust down, recommends specific corrective moves.
---

# SNIPED Trust Equation Skill

The B2B premium-service trust formula applied to a specific SNIPED situation. Output target: a diagnostic of where trust is leaking and what to fix.

## MANDATORY READING

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_trust_equation.md` · the C+R+I/S formula
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_trust_mechanics.md` · 8 trust signals + 5 anti-patterns
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_wwp_proclamations.md` · positioning context

## INVOKE WHEN
- A prospect is stuck or cooling
- A pitch isn't converting
- A client conversation feels off
- User asks "what am I doing wrong here"
- User is about to send important outreach and wants a sanity check
- Case study / authority asset is being designed

## THE FRAME
T = (C + R + I) / S
- **C · Credibility**: do they believe you can do the work? Built via proof, named clients, articulate methodology.
- **R · Reliability**: do they believe you'll deliver? Built via on-time delivery, clear communication, predictable cadence.
- **I · Intimacy**: do they feel safe with you? Built via vulnerability, specificity, demonstrated understanding of their world.
- **S · Self-Orientation**: how much are YOU at the center of the conversation? Higher S = lower trust. Self-promotion, "I" language, talking about your needs all destroy the denominator.

The fastest trust kills come from self-orientation (high S), not low C/R/I.

## OUTPUT
- Which variable is the weakest in the situation
- Specific evidence from the user's description
- One concrete move to repair it
- One move to avoid that would make it worse

## REFUSE
- Generic "be more confident" / "follow up more" advice
- Recommending tactics that raise S (self-promotion-heavy outreach)
- Ignoring the math when user reframes as "should I just lower price" (price isn't in the equation)


## Inputs
- User description of the stuck/cooling situation (deal stage, what was said, prospect behavior)
- Which of C/R/I/S the user suspects is the problem (optional, may be wrong)
- Any recent outreach copy or pitch language (optional, to diagnose S level)
- Prospect cluster: LA founder, Series-A, referral, etc.

## Gates
- Mandatory reads confirmed: intel_trust_equation.md + intel_trust_mechanics.md + intel_wwp_proclamations.md
- Diagnosis cites specific evidence from the user description, not generic assumptions
- No output recommends price reduction (price is not in the equation per REFUSE block)
- No output recommends self-promotion tactics that raise S
- Corrective move is singular and actionable, not a list of generic suggestions

## Test
- case: User says: 'I sent the Reset proposal to a Series-A founder three days ago. She was warm on the call but now no reply.' Expected output: identify whether the leak is R (no predictable follow-up cadence set), I (call did not establish safe vulnerability), or S (proposal was I/me-heavy). Returns one corrective move (e.g., a short I-noticed-something message referencing her specific world) and one thing to avoid (e.g., do not send a pushy 'just checking in' that raises S).
- expected failure: User provides no situation detail, only 'my prospect isn't converting.' Skill refuses to diagnose and asks: which of the 4 trust variables do you suspect is low, what did the last interaction look like, and what have you sent them?
