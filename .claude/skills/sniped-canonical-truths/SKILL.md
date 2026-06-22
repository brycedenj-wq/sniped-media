---
name: sniped-canonical-truths
description: Reference the 12 SNIPED Canonical Truths · the locked strategic spine that governs all major decisions. Use when user is making a strategic decision, drafting positioning copy, evaluating a pivot temptation, or asks "is this on-strategy." These 12 truths are non-negotiable and supersede tactical opinions.
---

# SNIPED Canonical Truths Skill

The strategic spine. Output target: surface which of the 12 truths apply to the situation and what they constrain.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/CANONICAL_TRUTHS.md` · the 12 truths
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/project_sniped_spine.md` · the locked spine memory

## INVOKE WHEN
- "Is this on-strategy"
- Major positioning / offer / lane decision
- Pivot temptations
- Drafting Carrd / pitch deck copy
- Reviewing a decision that feels off

## OUTPUT
- Which 1-3 truths apply
- The constraint each truth puts on the decision
- The yes/no with truth-citation

## REFUSE
- Recommendations that contradict any of the 12
- "Just this once" exceptions
- Tactical workarounds that violate strategic truths


## Inputs
- The specific decision, copy draft, or pivot temptation being evaluated
- Enough context to identify which of the 12 canonical truths are in tension with the proposed action

## Gates
- Must read CANONICAL_TRUTHS.md (the 12 truths) before any output
- Must read project_sniped_spine.md (locked spine memory) before ruling
- Refuse any recommendation that contradicts any of the 12 truths, even if tactically convenient
- Refuse 'just this once' exception framing (the truths are explicitly non-negotiable)
- Refuse tactical workarounds that achieve a truth-violating outcome by a different path

## Test
- case: User is considering a discounted rate for a referral client to close the deal faster. They ask: 'Is this on-strategy?' Expected output: 1-2 canonical truths governing pricing/positioning are surfaced, the constraint each puts on the discount is stated, and the ruling is NO with citations, not a soft hedge.
- expected failure: User provides a decision with no surrounding context (e.g., 'Is this a good idea?' with no detail). Skill cannot map to any of the 12 truths without knowing what 'this' is. Must request the specific decision or copy before proceeding.
