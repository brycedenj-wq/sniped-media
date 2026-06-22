---
name: sniped-lean-audit
description: Run the SNIPED Lean Execution Audit · the quarterly check on whether the operation is staying within the 10-12 hr/week lean override constraint. Use quarterly, when feeling overcommitted, or when considering adding surfaces / hires.
---

# SNIPED Lean Audit Skill

The "are we still lean" check. Output target: a clear audit result + the cuts needed if drift detected.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/LEAN_EXECUTION_AUDIT.md` · the locked audit framework
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_operating_constraints.md` · 10-12 hr/week
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_company_of_one.md` · stay-small logic

## INVOKE WHEN
- Quarterly review
- "I'm feeling overwhelmed"
- Considering new initiatives
- "Should I add this surface / hire / tool"

## OUTPUT
- Current weekly hour estimate
- Variance from 10-12 hr target
- If over: what to cut (per the audit hierarchy · admin first, content second, shoot work last)
- If under: what to add (per Phase 1 priorities, not random expansion)

## REFUSE
- Approving over-budget time commitments
- Adding work without cutting equivalent first
- Treating the lean override as flexible (it's locked per BJ's primary income constraint)


## Inputs
- Current weekly hour estimate across all operational surfaces (supplied by operator or reconstructed from active commitments)
- The locked 10-12 hr/week lean override constraint (sourced from LEAN_EXECUTION_AUDIT.md, the locked audit framework)
- List of active initiatives, surfaces, hires, and tools under consideration
- Phase 1 priorities (from intel_company_of_one.md) used only if under-budget to determine what to add

## Gates
- Refuse to approve over-budget time commitments
- Refuse to add work without cutting an equivalent commitment first
- Treat the lean override as locked, not flexible (primary income constraint per LEAN_EXECUTION_AUDIT.md)

## Test
- case: Quarterly review: operator lists 5 active surfaces totaling an estimated 16 hrs/week. Skill reads LEAN_EXECUTION_AUDIT.md (locked audit framework, source of the ceiling and cut logic), feedback_operating_constraints.md, and intel_company_of_one.md. Output shows current estimate 16 hrs, variance +4 to +6 hrs over the 10-12 hr target, and a cut list ordered admin-first / content-second / shoot-last until the estimate falls within the 10-12 hr band. No new surface is approved until the cut is confirmed.
- expected failure: Any of: approving a new hire or surface without cutting equivalent hours first; treating the 10-12 hr ceiling as a suggestion; attributing the 10-12 hr ceiling to feedback_operating_constraints.md rather than to LEAN_EXECUTION_AUDIT.md (the locked audit framework); ordering cuts any way other than admin first, content second, shoot work last.
