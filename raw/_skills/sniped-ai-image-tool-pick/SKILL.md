---
name: sniped-ai-image-tool-pick
description: Pick the right AI image tool for a specific SNIPED task · Seedream 5.0/4.5, Higgsfield Soul, Nano Banana Pro, Firefly, ChatGPT image gen, Photoshop Generative Fill with Reference Image. Use when user has a generation/edit task and isn't sure which tool to reach for.
---

# SNIPED AI Image Tool Pick Skill

The tool-routing skill. Output target: clear pick with the reasoning.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md` · the tool-to-task matrix
2. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md`
3. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md`
4. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/PHOTOSHOP_GENERATIVE_FILL_REFERENCE_IMAGE_EXTRACTION.md`

## INVOKE WHEN
- "Which AI tool should I use for X"
- Starting an AI-assisted task
- Comparing tools for a specific job

## OUTPUT
- The recommended tool
- Why (per the tool-to-task matrix)
- Backup option if primary fails
- Specific prompt template / settings (delegate to specific skill: seedream-prompt, higgsfield-pipeline)

## REFUSE
- Recommending tools for tasks that violate identity rule
- Generic "try them all" advice
- Tools that don't fit SNIPED's locked direction
