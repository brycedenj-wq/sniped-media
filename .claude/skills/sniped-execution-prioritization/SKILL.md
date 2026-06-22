---
name: sniped-execution-prioritization
description: Prioritize between competing SNIPED execution items using the locked prioritization framework. Use when user has multiple active tasks competing for attention, asks "what should I do first / next," or feels overwhelmed by the work queue.
---

# SNIPED Execution Prioritization Skill

The which-task-now decision skill. Output target: a clear top-3 with the reasoning.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/EXECUTION_PRIORITIZATION.md` · the locked framework
2. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/CURRENT_STATE.md` · blocking items + next action
3. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/ACTIVE_THREADS.md` · in-progress threads

## INVOKE WHEN
- "What should I do first / next"
- Multiple competing tasks
- "I'm overwhelmed"
- Decision paralysis moments

## OUTPUT
- Top 3 priority items right now
- Reasoning per the locked framework (revenue-impact / blocking / phase-alignment)
- What to defer or kill

## REFUSE
- Equal-priority lists (always pick a top 1)
- Adding new tasks to the queue without first finishing the top 3
- Recommending non-Phase-1 work when Phase 1 is blocked


## Inputs
- The live queue of competing tasks (verbally stated or extracted from ACTIVE_THREADS.md)
- CURRENT_STATE.md: what is currently blocked and what the declared next action is
- EXECUTION_PRIORITIZATION.md: the locked framework (revenue-impact / blocking / phase-alignment axes)
- Optional: operator's stated time budget or energy level for the session

## Gates
- TOP-1 must be singular -- no equal-priority output allowed
- No new tasks added to queue before top-3 are addressed
- Non-Phase-1 work deferred when Phase-1 has any blocking item (per REFUSE clause)
- Reasoning must cite the locked framework axis, not intuition

## Test
- case: Operator has 4 active threads: client gallery delivery, Direction Stack caption batch, Higgsfield Image Pack run, and a new prospect DM draft. Ask: 'what do I do first?' Expected output: ranked top-3 with client delivery ranked #1 (revenue-impact axis), Image Pack #2 (phase-alignment), caption batch #3; prospect DM deferred with explicit reason.
- expected failure: Input arrives with no CURRENT_STATE.md readable and no verbal queue provided -- skill must surface that it cannot rank without the blocking-item context and refuse to output a generic priority list.
