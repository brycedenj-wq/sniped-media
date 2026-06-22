---
name: sniped-strategic-implications
description: Run a major SNIPED strategic decision through the 10 corpus-validated strategic implications. Use when user is doing the quarterly Constraint Audit, considering a Phase trigger, evaluating whether to take on a new initiative, or asks "is this the right strategic move." This is the heavyweight strategic frame · invoke for decisions that span quarters / phases, not weekly questions.
---

# SNIPED Strategic Implications Skill

The corpus-validated decision frame for major strategic moves. Output target: a yes/no on the strategic move with which implication(s) decided it.

## MANDATORY READING

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_strategic_implications.md` · the 10 implications
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/project_sniped_meta_thesis.md` · BJ's locked thesis
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/project_sniped_spine.md` · 12 canonical truths
4. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/CANONICAL_TRUTHS.md` · the strategic spine
5. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/SYSTEM_FINAL_STATUS.md` · master plan

## INVOKE WHEN
- Quarterly Constraint Audit
- Phase trigger evaluation ($3K MRR sustained 2 months → Phase B)
- "Should we expand into X" decisions
- Major pivot questions
- Capital deployment decisions (when applicable)
- Direction Stack book chapter strategic decisions
- "Is this the right strategic move" for a Phase-level question

## THE FRAME
The 10 corpus-validated implications (from `intel_strategic_implications.md`) are the decision frame for any move that spans quarters or phases. They synthesize the 15-book strategic corpus into 10 yes/no tests.

Don't invoke for:
- Daily / weekly tactical questions (use other skills)
- Phase 1 cadence decisions (already locked)
- Pricing / outreach / content decisions (use specific skills)

INVOKE only for moves that change the SNIPED architecture · new phase, new lane, new offer tier, new business surface, major pivot.

## OUTPUT
- Which 2-3 of the 10 implications are most relevant
- The yes/no recommendation
- The specific evidence from the corpus that decides it
- The phase / trigger that would change the answer if no today

## REFUSE
- Invoking for daily tactical questions (over-engineering)
- Generic strategic advice without implication references
- Recommending major pivots before Phase 1 ships
- "Sounds like a great idea" without running it through the 10


## Inputs
- The specific strategic move being evaluated (must be phase-level or architecture-level: new offer tier, new lane, Phase trigger, capital deployment, major pivot)
- Current Phase and MRR context (e.g. Phase 1, $1,200 MRR) so phase-gating can apply
- intel_strategic_implications.md, project_sniped_meta_thesis.md, project_sniped_spine.md, CANONICAL_TRUTHS.md, SYSTEM_FINAL_STATUS.md (all mandatory reads)
- The specific question: 'is this the right strategic move' or 'should we trigger Phase B'

## Gates
- REFUSE: invoking for daily or weekly tactical questions (pricing tweak, single post, outreach message) — direct to the appropriate specific skill
- REFUSE: generic strategic advice without citing specific implication numbers from intel_strategic_implications.md
- REFUSE: recommending major pivots or new phases before Phase 1 has shipped its core deliverables
- REFUSE: 'sounds like a great idea' conclusions that skip running the move through all 10 implications
- Gate: all 5 mandatory files read before any recommendation is issued

## Test
- case: Operator asks: 'We've hit $3K MRR for two consecutive months. Should we trigger Phase B and add a retainer offer?' Expected output: skill reads all 5 mandatory files, confirms the Phase B trigger condition is met ($3K MRR sustained 2 months), runs the move through the 10 implications, identifies the 2-3 most decisive ones (e.g. leverage, constraint, positioning), delivers a yes/no with the deciding implication named, cites the specific canonical truth or corpus source that decides it, names what must be true before Phase B launches (e.g. Reset pipeline stable, delivery SLA met).
- expected failure: Operator asks: 'Should I post a carousel or a reel this week?' Skill must refuse: this is a weekly tactical question, not a phase-level strategic move. Response: redirect to the appropriate skill (e.g. sniped-caption-writer or sniped-blockbuster-strategy) and explain the threshold for invoking strategic-implications.
