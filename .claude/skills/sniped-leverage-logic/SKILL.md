---
name: sniped-leverage-logic
description: Apply Naval Ravikant's 3-leverage frame (labor / capital / code+media) to a SNIPED decision about adding a hire, surface, tool, or system. Use when user is considering hiring (retoucher, assistant, VA), expanding offers, adding a new platform, building new infrastructure, or asks "should we add this." Defaults to code+media leverage (the permissionless kind) over labor leverage (requires management).
---

# SNIPED Leverage Logic Skill

The "what kind of leverage am I actually adding" frame. Output target: a clear ruling on whether the proposed add is leverage or drag, and which kind.

## MANDATORY READING

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_leverage_logic.md` · 3 forms of leverage
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_company_of_one.md` · stay-small as strategy
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_operating_constraints.md` · 10-12 hr/week, leverage-first
4. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/OPERATIONAL_BACKBONE.md` · what BJ owns forever

## INVOKE WHEN
- "Should I hire a retoucher / assistant / VA?"
- "Should I add this surface / platform / offer?"
- Considering new tool subscription
- "Should I outsource X?"
- Building new infrastructure / SOP
- Growth temptations that require management overhead

## THE FRAME (the 3 leverages)
1. **Labor** · humans doing work for you. Requires management. Permission-required. Best when scale demands it (Phase B+ retoucher).
2. **Capital** · money working for you. SNIPED has no capital play in Phase 1.
3. **Code + media** · permissionless leverage. SOPs, presets, content, automations, the OS itself. **Default to this in Phase 1.**

The hierarchy:
- Code + media: unlimited scale, no management, no permission
- Capital: scales with cash, modest management
- Labor: management overhead grows linearly with team

For SNIPED Phase 1 (10-12 hr/week, lean override): every "should I add X" decision defaults to code+media. Labor only when Phase B trigger ($3K MRR sustained 2 months) opens capacity.

## OUTPUT
- What kind of leverage the proposed add is
- Whether it fits SNIPED's current phase
- Specific code+media alternative if labor was proposed
- The Phase trigger that would unlock labor if it's truly the right answer

## REFUSE
- Recommending labor hires in Phase 1 (before $3K MRR sustained 2 months)
- "Just outsource it" without framing the management overhead
- Adding tools that require new manual workflows (anti-leverage)
- Treating capital deployment as available when it isn't


## Inputs
- The specific proposed add: a hire (retoucher, VA, assistant), new platform, tool subscription, SOP build, or outsource decision
- intel_leverage_logic.md (3 forms of leverage, read on invocation)
- intel_company_of_one.md (stay-small as strategy, read on invocation)
- feedback_operating_constraints.md (10-12 hr/week constraint + Phase B trigger, read on invocation)
- OPERATIONAL_BACKBONE.md (what BJ owns permanently, read on invocation)

## Gates
- Labor hires are refused in Phase 1 (before $3K MRR sustained 2 months) per the locked phase trigger
- Any tool that creates a new manual workflow must be classified as anti-leverage and refused
- Code+media alternatives must be specific and actionable (e.g. 'build a retouch SOP + Evoto preset chain'), not generic
- Capital deployment is unavailable in Phase 1 and must not be recommended
- 'Just outsource it' framing without naming the management overhead cost is refused

## Test
- case: BJ asks 'Should I hire a retoucher for $500/month to free up edit time?' Expected output: classify as labor leverage, confirm Phase 1 lock (not at $3K MRR yet), name a specific code+media alternative (Evoto preset chain + batch LR workflow), and state the exact MRR trigger that would make the hire worth evaluating.
- expected failure: User says 'I want to add a new tool' without naming which tool or what problem it solves. Skill must ask for the specific proposed add before classifying leverage type, because the classification depends on whether the tool creates or eliminates manual workflows.
