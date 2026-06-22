---
name: os-vision-reject-gate
description: Visually review any generated frame, video still, product shot, campaign image, or AI composite BEFORE it ships. Use after any image/motion generation and before posting/delivery. Reads the asset and scores it against the slop/hands/skin/clothing-physics/text/identity/brand/likeness/beat-source checklist; any hard-fail = REJECT.
---

# OS Vision Reject-Gate

Before any generated asset ships:
1. Run `scripts/os_vision_gate.py <path>` to emit the checklist (and confirm the file exists).
2. **Read the asset** (Read tool handles images; for video, review key stills) and score EACH item:
   slop · hands · skin (melanin-true, not plastic) · clothing physics · text artifacts · identity consistency (matches CRS) · brand consistency (v3 LUXURY, no teal/orange) · copyright/likeness (owned character only, no celebrity) · beat-source (must beat an honest camera frame).
3. **Verdict: SHIP / FIX / REJECT.** Any hard-fail = REJECT, do not ship. Log a REJECT to the error/quarantine dashboard.

Placeholder for automation: when a vision-model API is wired, this skill calls it per item; until then the model performs the review via Read. Pairs with `os-quality-gates` (beat-source/reject), the campaign-house pipeline stages 7-9, and the visual doctrine in OS_MASTER_DOCTRINE.


## INVOKE WHEN
- "does this image pass" / "is this ready to post" / "gate this composite"
- After any AI generation before delivering or posting an asset
- "check this frame" / "does this clear the slop check"

## Inputs
- Path to the generated image, composite, or video still to review (required)
- CRS or brand brief to cross-check identity and brand consistency against
- Beat-source reference: honest camera frame this asset must outperform

## Outputs
- SHIP / FIX / REJECT verdict with each of the 9 checklist items scored: slop, hands, skin, clothing physics, text artifacts, identity, brand, copyright/likeness, beat-source
- If REJECT: logged entry to error/quarantine dashboard naming the specific failing item(s)
- One-line receipt: e.g. 'Alma_BH_hero_v3.jpg -> SHIP (all 9 pass; skin melanin-true, no text artifacts, beats honest camera frame)'

## Gates
- Slop/hands/skin/clothing-physics/text-artifacts: any hard-fail on these = REJECT, do not ship
- Identity gate: subject must match the locked CRS; face drift = REJECT
- Brand gate: v3 LUXURY palette only, no teal/orange bleed; violation = REJECT
- Copyright/likeness gate: owned character only, no unlicensed celebrity likeness
- Beat-source gate: asset must outperform an honest camera frame at this scene; fails = REJECT

## Test
- case: Operator runs Alma-suit hero through Higgsfield Cinema Studio 3.5 and needs the PNG cleared before IG post. Expected: 9-item scored checklist, final SHIP/FIX/REJECT verdict (e.g. FIX: clothing physics shows collar warp), and if any hard-fail a quarantine log entry naming the exact item.
- expected failure: Invoked without providing an asset path or readable image. Skill halts: 'Cannot gate: no asset path provided. Re-invoke with the file path to the image or video still.'
