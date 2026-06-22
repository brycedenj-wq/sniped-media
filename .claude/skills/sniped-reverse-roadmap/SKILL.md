---
name: sniped-reverse-roadmap
description: Reference SNIPED's 10-year reverse roadmap to evaluate whether a current decision aligns with the Year 10 vision. Use during quarterly reviews, when considering major pivots, or asks "where does this lead long-term." Defaults to the locked roadmap · refuses ad-hoc redesign.
---

# SNIPED Reverse Roadmap Skill

The 10-year-back lens. Output target: a check that the current move serves the Year 10 endpoint.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/REVERSE_ROADMAP.md` · the 10-year reverse
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/project_sniped_meta_thesis.md` · the thesis driving the roadmap

## INVOKE WHEN
- Quarterly review
- Major pivot consideration
- "Where does this lead in 5+ years"
- Year 10 vision check

## OUTPUT
- Year 10 endpoint per the roadmap
- The decision's alignment (advances / neutral / regresses)
- What the next 12-24 months should produce to stay on track

## REFUSE
- Redrawing the roadmap ad-hoc
- Treating Year 1-2 tactical moves as roadmap-level questions
- Ignoring the roadmap because "things change"


## Inputs
- The specific decision or move being evaluated (e.g. 'should we add a corporate headshot tier')
- Current phase / timeframe context (so Year 10 distance can be measured)
- REVERSE_ROADMAP.md at ~/Downloads/    SNIPED_OS/00_BRIEF/REVERSE_ROADMAP.md (mandatory read)
- project_sniped_meta_thesis.md from memory (mandatory read)

## Gates
- REFUSE: redrawing or amending the roadmap on-the-fly (locked doc, not a drafting surface)
- REFUSE: treating Year 1-2 tactical moves (pricing tweak, single-post copy) as roadmap-level questions
- REFUSE: dismissing the roadmap because 'things change' without operator-authorized revision
- Gate: both mandatory files must be read before any alignment verdict is issued

## Test
- case: Operator asks: 'We have a corporate client offering $5K for team headshots. Should we take it?' Expected output: skill reads REVERSE_ROADMAP + meta-thesis, returns the Year 10 endpoint (e.g. named-artist brand / premium solo-founder lane), maps the corporate headshot offer to 'neutral-to-regresses' (commoditizes the tier, dilutes selectivity signal), states what the next 12 months should produce instead (e.g. 3 anchor clients at $5K+ in the founder lane), delivers a one-line verdict.
- expected failure: User asks 'Can you rewrite the roadmap to include a real-estate photography lane?' Skill must refuse: redrawing the roadmap ad-hoc is a locked refuse condition. Response: surface the refusal and instruct operator to authorize a roadmap revision session separately.
