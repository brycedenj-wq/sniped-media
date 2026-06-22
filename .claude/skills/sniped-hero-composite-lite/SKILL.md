---
name: sniped-hero-composite-lite
description: Run SNIPED's 45-minute lite hero composite workflow. Use when user wants to create a hero composite frame for IG portfolio / IG carousel without the full Track B Photoshop ceremony. Pulls from Seedream 5.0, Higgsfield, or Nano Banana Pro for plate generation or full composite, applies v3 LUXURY EDITORIAL direction, preserves subject identity (face/body/skin untouched rule). For portfolio anchor / Direction Stack book frames, use sniped-hero-composite-ceiling skill instead.
---

# SNIPED Hero Composite · Lite Lane Skill

The lite lane bypasses ~80% of the Photoshop assembly in `/05_PRODUCTION/track_b_frame_walkthrough.md`. Uses AI image gen tools (Seedream 5.0, Higgsfield Image Pack, Nano Banana Pro) for plate or full composite generation. Output target: IG hero, IG carousel, LinkedIn case study asset. NOT for: Direction Stack book frames, portfolio anchor pieces (those go through the ceiling lane).

---

## MANDATORY READING ON INVOCATION

Read in this order before drafting any prompt or workflow step:

1. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_visual_direction_luxury_editorial.md` · the locked v3 luxury direction (governs every prompt)
2. `/Users/sniper/.claude/projects/-Users-sniper/memory/feedback_edit_register_bifurcation.md` · identity rules (face/body/skin untouched, hair styling variable)
3. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md` · Seedream prompting tricks, locked HEX palette, 4 SNIPED templates
4. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md` · Higgsfield Image Pack + MCP usage
5. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md` · Nano Banana Pro likeness preservation + tool matrix

After reading, ask the user:

> "Which lane?
> 1. **Studio extension** · subject stays in studio, plate adds atmospheric depth (Seedream Template A)
> 2. **Scene placement** · subject placed into a new environment, identity preserved (Nano Banana Pro)
> 3. **Image Pack** · multiple hero variations from one subject upload (Higgsfield)
> 
> And: do you have the Evoto TIFF ready, or are we starting from Lightroom?"

---

## THE 45-MINUTE WORKFLOW

| Step | Tool | Time |
|---|---|---|
| 1. LR develop + AI mask stack + Generative Remove | Lightroom Classic with v3 LUXURY preset | 10 min |
| 2. Evoto skin pass (light · Track B level, not Brand System) | Evoto | 5 min |
| 3. Plate gen OR full composite | Seedream 5.0 / Higgsfield Image Pack / Nano Banana Pro | 10-15 min |
| 4. Identity check on output (face/body/skin must match exactly) | Manual eye | 2 min |
| 5. Light Photoshop pass (hair flyaway cleanup, edge refine ONLY · no Harmonize ceremony) | Photoshop | 10 min |
| 6. Re-import LR, apply v3 LUXURY, export per locked presets | Lightroom | 5 min |

**Total: ~45 min** vs Track B Photoshop ceiling lane's 60-80 min.

---

## THREE RULES THAT CANNOT BREAK

### 1. SUBJECT IDENTITY HOLDS

Face, body, skin texture, body proportions · all real, all untouched. Hair styling can vary (per `feedback_edit_register_bifurcation`).

If the AI output shifts the subject's identity at all · regenerate. Never ship a frame where the face has been changed.

### 2. NO TEAL/ORANGE GRADING. NO CINEMATIC THEATRICS.

Every prompt uses the locked v3 LUXURY palette:
- Deep shadow: `#2A2A2E`
- Cool shadow accent: `#3D4B5C`
- Mid skin: `#B8956E`
- Mid environment: `#C9B7A3`
- Cream highlight: `#F5EFE6`

Camera cheat code default: "Mamiya 7 medium format, Kodak Portra 400 grain"

Reference register: Loewe campaign, Mert and Marcus, Paolo Roversi. NOT Tadder, NOT jpwphoto.

### 3. WORKFLOW IS NOT FOR CLIENT DELIVERABLES

This skill outputs to:
- IG hero post
- IG carousel
- LinkedIn POV case study asset

Never to:
- Client gallery (anti-AI rule on client work per `intel_ai_sentiment` memory)
- Direction Stack book frames (those need ceiling lane Photoshop assembly)
- Op Kit / Brand System tier deliverables

If the user asks to apply this skill to a client deliverable · refuse and route to Track A standard pipeline.

---

## OUTPUT

When the user has chosen lane + provided Evoto TIFF (or LR-ready frame):

1. Draft the AI tool prompt using the locked palette + camera cheat code + lane-specific template
2. Wait for user to generate output and share result
3. Run identity check (or guide user through it)
4. If pass: walk through Photoshop light pass (Step 5) and re-import + export (Step 6)
5. If fail: diagnose what shifted, suggest regeneration prompt tweak
6. After export: save DM draft template for the IG post caption using v3 luxury voice
7. Append session entry to `/00_BRIEF/SESSION_LOG.md`

---

## WHAT TO REFUSE

- "Let's go with teal/orange this time" · No. Direction is locked.
- "Apply this to a Reset client's frames" · No. Lite lane is IG creative engine only.
- "Use Seedream 5.0 for portrait identity preservation" · Switch to Seedream 4.5 or Nano Banana Pro. 5.0 has face shift.
- "Generate the subject too" · No. Subject must be real captured photograph.

---

## FILES + CROSS-REFERENCES

```
sniped-hero-composite-lite/
├── SKILL.md                ← you are here
└── workflow.md             ← detailed step-by-step (if needed for first-time use)
```

Cross-references (read on invocation as listed above):
- `feedback_visual_direction_luxury_editorial.md` memory
- `feedback_edit_register_bifurcation.md` memory  
- `intel_ai_sentiment.md` memory
- `/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md`
- `/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md`
- `/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md`
- `/05_PRODUCTION/track_b_frame_walkthrough.md` (the ceiling lane, for comparison)

The subject's actual frames live in the user's `/SNIPED_PRODUCTION/2026/[shoot]/` folders · not in the skill. Skill is the runbook, frames are the material.


## Inputs
- Subject frame: Evoto TIFF ready OR Lightroom-ready RAW (real captured photograph, not AI-generated)
- Chosen lane confirmed: Studio Extension (Seedream Template A), Scene Placement (Nano Banana Pro), or Image Pack (Higgsfield)
- Target surface confirmed as IG hero, IG carousel, or LinkedIn case study asset (not client or Direction Stack book)
- v3 LUXURY palette and camera cheat code accepted as locked direction (no teal/orange override)

## Gates
- Identity check: face, body, skin texture, proportions must match the real photograph -- any shift triggers regeneration
- v3 LUXURY palette locked -- teal/orange grading is a hard refusal
- Seedream 5.0 must NOT be used for portrait identity (face shift risk) -- route to 4.5 or Nano Banana Pro
- Subject must be a real captured photograph -- AI-generated subjects are refused
- Output must not be a client deliverable or Direction Stack book frame

## Test
- case: BJ has an Evoto TIFF and wants an IG hero composite placing the subject in a new outdoor scene via Scene Placement. Expected output: Nano Banana Pro prompt with v3 LUXURY palette + Mamiya 7 cheat code, identity check pass, Photoshop light pass for hair edge, LR export, DM caption draft, SESSION_LOG entry appended.
- expected failure: User requests the output go into a client's Pixieset gallery. Skill must refuse and route to Track A standard pipeline, citing the anti-AI rule on client deliverables.
