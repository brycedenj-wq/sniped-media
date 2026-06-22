---
name: sniped-udemy-lightroom-rails
description: Reference the 16 USE NOW Lightroom rails extracted from the Udemy Lightroom course. Use when user needs a specific Lightroom technique reference, asks about a feature, or wants to look up the canonical SNIPED rail for a develop task. The extraction is the active layer · do not re-read the source course.
---

# SNIPED Udemy Lightroom Rails Skill

The Lightroom rails reference. Output target: the specific rail for the task.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/UDEMY_LIGHTROOM_EXTRACTION.md` · 16 USE NOW Lightroom rails

## INVOKE WHEN
- Lightroom technique reference needed
- "How do I do X in Lightroom"
- Looking up a specific feature
- Cross-referencing the lightroom_operating_system.md with rail-level detail

## OUTPUT
- The specific rail from the 16
- Application to the current task
- Cross-reference to lightroom_operating_system.md if relevant

## REFUSE
- Recommending techniques outside the 16 rails (the rest is beginner per locked stance)
- Suggesting users re-read the full course
- Adding new rails without quarterly review


## Inputs
- The Lightroom develop task or feature the user needs (e.g., masking, color grading, export settings, tone curve)
- Context: portrait retouch, product shoot, editorial grade, or batch export pass
- Any cross-reference needed to lightroom_operating_system.md

## Gates
- Mandatory read confirmed: UDEMY_LIGHTROOM_EXTRACTION.md (the 16 USE NOW rails)
- Only rails from the locked 16 are recommended; nothing outside the list
- No recommendation to re-read the full source Lightroom course
- No new rails added outside a quarterly review cycle

## Test
- case: User asks: 'What is the SNIPED canonical way to use the HSL panel to fix skin tones on a dark-skinned subject in Lightroom?' Expected output: identifies the relevant rail from the 16 covering HSL or skin-tone correction, gives the specific settings or sequence, and cross-references lightroom_operating_system.md if the rail connects to the broader SNIPED grade preset system.
- expected failure: User asks about a Lightroom feature not covered by any of the 16 rails (e.g., a new AI masking beta feature added after the extraction). Skill refuses to improvise and states the locked stance: only the 16 rails are canonical; the rest is beginner-level or untested. Flags it for the next quarterly review.
