---
name: sniped-positioning-phrases
description: Run a piece of SNIPED copy through the positioning phrase bank + 5 failure modes + refusal-positioning lever. Use when user is finalizing Carrd copy, an Op Kit one-pager, a Pitch deck, a LinkedIn POV, or asks "does this read on-brand" / "is this language right." Output is a phrase-level diagnostic and rewrite.
---

# SNIPED Positioning Phrases Skill

The copy-level lens. Output target: copy that uses the locked phrase bank, avoids the 5 failure modes, and leverages the refusal-positioning lever.

## MANDATORY READING

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_positioning_phrases.md` · phrase bank + 5 failure modes
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/intel_wwp_proclamations.md` · positioning rules
3. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_visual_direction_luxury_editorial.md` · voice context
4. `/Users/sniper/.claude/CLAUDE.md` · the em-dash ban + other global rules

## INVOKE WHEN
- Finalizing Carrd copy
- Op Kit / Brand System one-pager copy review
- Pitch deck copy
- LinkedIn POV draft before publishing
- Email template review
- "Does this language read SNIPED"
- ANY user-facing text before it ships

## THE FRAME

### The 5 failure modes (from `intel_positioning_phrases.md`)
1. Premature pitching
2. Generic compliments (in outreach)
3. Volume language
4. Begging tone (high self-orientation)
5. Multi-CTA messes

### The refusal-positioning lever
"We refuse X" reads more confident than "We do Y." Refusal language IS premium positioning. Examples:
- "We don't shoot every founder" beats "We work with select founders"
- "We refuse to use AI on subjects" beats "We use real photography"
- "We don't do volume" beats "We do premium"

### Global voice rules (from `/Users/sniper/.claude/CLAUDE.md`)
- **No em-dashes EVER.** Lifetime ban. Use colons, periods, parentheses, or arrows instead.
- No emojis unless explicitly requested
- Avoid: "obsessed," "stunner," "fire," "literally," "honestly" as crutch words

## OUTPUT
- The current copy's failure mode(s) identified
- The phrase-level rewrite
- One refusal-positioning move if appropriate
- Em-dash scan + replacement if any found

## REFUSE
- Approving copy with em-dashes (always rewrite)
- Approving copy that triggers any of the 5 failure modes
- Generic "this looks good" reviews
- Letting begging tone or volume language through


## Inputs
- The draft copy to be reviewed: Carrd page, Op Kit one-pager, pitch deck slide, LinkedIn post, or email template
- Context for the copy: intended audience and the action it is driving
- intel_positioning_phrases.md read result (phrase bank + 5 failure modes)
- intel_wwp_proclamations.md read result (selectivity and refusal rules)

## Gates
- Em-dash gate: any em-dash found is a hard block -- rewrite before approving, no exceptions (global lifetime ban)
- Failure-mode gate: copy triggering any of the 5 failure modes is refused as-is and rewritten, never approved
- No-generic-approval gate: 'this looks good' with no diagnostic is refused -- every review must name what passed and what was fixed
- Refusal-lever gate: any 'we work with select...' or 'we use real...' construction must be tested against the refusal form before the copy ships

## Test
- case: Operator submits Carrd hero copy: 'We work with select founders to create amazing photography that helps them stand out. We offer headshots, brand shoots, and team photos -- reach out to learn more!' Expected output: failure modes flagged = generic compliments ('amazing'), volume language ('headshots, brand shoots, and team photos' list), multi-CTA ('reach out to learn more' after a service list); rewrite using refusal lever ('We don't shoot every founder') and a single CTA; em-dash scan = 0 found.
- expected failure: Operator submits copy that contains an em-dash and says 'approved, just post it.' Skill refuses to pass the copy as-is. Outputs the em-dash replacement immediately and re-runs the full failure-mode diagnostic before any approval is issued.
