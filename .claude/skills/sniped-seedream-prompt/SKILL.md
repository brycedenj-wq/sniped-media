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
