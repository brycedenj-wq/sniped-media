---
name: sniped-udemy-ai-accelerants
description: Reference the 7 USE NOW AI workflow accelerants from the Udemy AI course extraction. Use when user wants AI workflow speed-up techniques, asks about specific AI accelerants, or building automation. The 7 are extracted · the rest of the course is hype per the locked stance.
---

# SNIPED Udemy AI Accelerants Skill

The AI accelerants reference. Output target: the specific accelerant for the task.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/UDEMY_AI_TACTICAL_EXTRACTION.md` · 7 USE NOW accelerants

## INVOKE WHEN
- AI workflow speed-up question
- Building automation
- "How do I make this faster with AI"
- Looking up specific accelerant techniques

## OUTPUT
- Which of the 7 accelerants applies
- Application to the current SNIPED task
- Cross-reference to other AI tactical extractions

## REFUSE
- Recommending accelerants outside the 7 (rest is hype per locked stance)
- Recommending re-reading the full source course
- Adding new accelerants without quarterly review


## Inputs
- The current SNIPED task or workflow the user wants to speed up
- Which of the 7 accelerants the user suspects applies (optional)
- Whether the goal is automation, speed, or quality improvement

## Gates
- Mandatory read confirmed: UDEMY_AI_TACTICAL_EXTRACTION.md (the 7 USE NOW accelerants)
- Only accelerants from the locked 7 are recommended; nothing outside the list
- No recommendation to re-read the source Udemy course
- No new accelerants added outside a quarterly review cycle

## Test
- case: User asks: 'How do I make my Lightroom culling plus caption-writing workflow faster using AI?' Expected output: identifies the relevant accelerant from the 7 (e.g., batch-processing or prompt-chaining accelerant), shows exactly how to apply it to the Lightroom-to-caption pipeline, and cross-references sniped-udemy-lightroom-rails if a rail is applicable.
- expected failure: User asks about an AI workflow technique from another course not in the 7. Skill refuses and states the locked stance: only the 7 USE NOW accelerants are canonical; the rest is hype per the locked extraction. Offers to check if the technique maps to one of the 7.
