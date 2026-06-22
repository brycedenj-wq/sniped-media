---
name: sniped-assistant-task-routing
description: Route a task to the SNIPED marketing/admin assistant per the locked SOP_assistant.md scope. Use when user wants to delegate something, asks "should I have my assistant do this," or needs to draft assistant instructions. Assistant does lead sourcing + CRM mgmt + reply triage. Does NOT send outreach copy, draft pitches, simulate BJ's voice, or touch financial/strategic-only docs.
---

# SNIPED Assistant Task Routing Skill

The "does this go to the assistant" decision skill. Output target: a clear yes/no with routing instructions.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/03_OUTREACH/SOP_assistant.md` · the assistant's working manual
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_referral_handling.md` · Pearl network protocol the assistant supports
3. `/Users/sniper/Downloads/    SNIPED_OS/03_OUTREACH/SOP_discovery_to_close.md` · what BJ owns vs assistant

## INVOKE WHEN
- "Can I have my assistant do X"
- Drafting assistant task instructions
- Reviewing assistant output before deployment
- Onboarding clarification questions

## OUTPUT
Route the task:
- **YES, delegate** + draft the assistant-facing instruction
- **NO, BJ-only** + reason why (per the "what NEVER gets outsourced" list in `PRODUCTION_OS.md` Section 4.5)

The assistant DOES:
- Lead sourcing (LinkedIn / IG / referrals research)
- CRM updates (Notion)
- Reply triage on cold prospects
- Visual gap drafting (NOT final copy)
- Trigger event search

The assistant does NOT:
- Send outreach copy
- Draft pitches in BJ's voice
- Touch financial data / memory layer / strategic-only docs
- Make pricing decisions
- Respond to warm leads
- Anything in the OPERATIONAL_BACKBONE.md Section 2 "BJ owns forever" list

## REFUSE
- Delegating tasks on the "BJ owns forever" list
- Drafting assistant instructions that would access banned docs
- Volume / spray work (the assistant respects positioning rules too)


## Inputs
- The specific task to be evaluated for delegation (described in plain language or as a draft instruction)
- Enough context to classify it against the assistant scope: lead sourcing, CRM, reply triage, visual gap drafting, or trigger-event search
- Optional: whether the task involves BJ's voice, financial data, warm leads, or the memory layer (instant disqualifiers)

## Gates
- Must read SOP_assistant.md before any routing decision
- Must read feedback_referral_handling.md to verify Pearl network protocol before routing referral-adjacent tasks
- Must cross-check against SOP_discovery_to_close.md to confirm what BJ owns in the sales lane
- Refuse any task on the 'BJ owns forever' list regardless of convenience argument
- Refuse drafting assistant instructions that would give the assistant access to financial data, the memory layer, or strategic-only docs

## Test
- case: User asks: 'Can my assistant handle the initial cold-prospect inbox triage and flag the warm ones for me?' Expected output: YES delegate for reply triage and flagging (within SOP scope), NO for responding to warm leads (BJ-only), with a draft assistant instruction covering the triage step only.
- expected failure: User asks the assistant to draft a pitch in BJ's voice for a named prospect. Skill must refuse: drafting pitches in BJ's voice is explicitly on the 'assistant does NOT' list. Output cites the SOP_assistant.md ban and redirects to BJ doing the pitch with assistant research as input.
