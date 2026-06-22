---
name: sniped-seedream-prompt
description: Construct a Seedream 5.0 / 4.5 image generation prompt using SNIPED's locked palette + camera cheat codes + the 7-environment rotation. Use when user needs a Seedream prompt for plate generation, style transfer, or identity-preserving composite. References `/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md`.
---

# SNIPED Seedream Prompt Skill

The Seedream prompt construction skill. Output target: a copy-paste-ready Seedream prompt aligned to v3 LUXURY direction.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md` · the 6 prompting tricks + 4 SNIPED templates
2. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/composite_environment_rotation_v1.md` · the 7-environment vocabulary

## INVOKE WHEN
- User wants a Seedream prompt
- Plate generation for a SNIPED composite
- Style transfer between SNIPED frames
- "How do I prompt Seedream for X"

## OUTPUT
- The full Seedream prompt (HEX palette + camera cheat code + environment + register)
- Which Seedream version (5.0 Lite for plates, 4.5 for identity preservation)
- Negative prompt
- Aspect ratio + variations recommendation

## REFUSE
- Prompts that generate SNIPED subjects (identity rule)
- Prompts without HEX palette + camera cheat code
- Generic Seedream prompts that ignore the locked direction


## Inputs
- Use case: plate generation, style transfer, or identity-preserving composite
- SEEDREAM_TACTICAL_EXTRACTION.md at /Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/ (6 prompting tricks + 4 SNIPED templates, per SKILL.md MANDATORY READING)
- composite_environment_rotation_v1.md at /Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/ (the 7-environment vocabulary)
- The subject, scene intent, and any locked SNIPED HEX palette values

## Gates
- Refuse prompts that generate SNIPED subjects (identity rule)
- Refuse prompts without HEX palette + camera cheat code included
- Refuse generic Seedream prompts that ignore the locked direction from SEEDREAM_TACTICAL_EXTRACTION.md

## Test
- case: Request: 'Give me a Seedream prompt for a plate of a golden-hour outdoor scene to composite with a SNIPED hero.' Skill reads SEEDREAM_TACTICAL_EXTRACTION.md (6 prompting tricks + 4 SNIPED templates) and composite_environment_rotation_v1.md (7-environment vocabulary). Output includes: full prompt with the locked SNIPED HEX palette values embedded, a named camera cheat code from the extraction doc, the golden-hour outdoor environment from the 7-environment rotation, the correct register, version routed to Seedream 5.0 Lite (plate gen), a negative prompt, and aspect ratio + variations recommendation. No SNIPED subject identity generated.
- expected failure: Any of: producing a prompt that generates a SNIPED subject (identity rule breach); omitting the HEX palette or the camera cheat code from the output; ignoring the 7-environment vocabulary from composite_environment_rotation_v1.md; fabricating that the file lives in a path other than /Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md; producing a generic Seedream prompt without reading the mandatory source files first.
