---
name: os-world-bible
description: Define and gate the world a character lives in (environments, materials, light logic, color system, camera language, forbidden elements, motifs, SREF slots, continuity rules) so every output is continuous instead of random. Use when establishing a new world, locking the visual language, or checking a proposed scene for continuity before a campaign-house run.
---

# os-world-bible

Lock one world's rules as a structured, gateable bible, then check every scene against it. Wraps `00_COMMAND_CENTER/scripts/os_world.py`.

## INVOKE WHEN
- a new world / visual language is needed for the campaign house
- "lock the world / set the look rules / what's allowed in this world"
- before generating a scene, to check it is continuous with the world
- when a frame feels off-world and you need to know which rule it broke

## Inputs
- `slug` , id for the world
- the 9 rule categories: environments, materials, light_logic, color_system (palette_hex + forbidden_hues), camera_language, forbidden_elements, recurring_motifs, sref_style_slots, continuity_rules
- optional: a proposed scene (JSON) to gate

## Outputs
- `campaign_house/worlds/<slug>/WORLD.json` , the validated world bible
- a continuity verdict per scene (pass / quarantine with named rule break)
- a one-line receipt

## Procedure
1. `os_world.py new <slug>` , scaffold the 9 categories.
2. Fill WORLD.json. Pull environments from the locked 7-environment rotation; set color_system foundation + palette + forbidden hues (e.g. teal/orange banned); make forbidden_elements explicit; leave sref_style_slots as TBD-manual-pull until pulled by hand.
3. `os_world.py validate <slug>` , must return VALID.
4. Per scene: `os_world.py continuity <slug> --scene FILE` , quarantine on forbidden element or off-rotation environment.

## Gates
- completeness gate: all 9 categories non-empty; palette_hex + forbidden_hues required
- continuity gate: forbidden element present OR environment not in rotation -> quarantine (off-palette hue = advisory warn)
- no generation here; this defines and gates only

## Test
- case: `os_world.py new t01` then `validate t01` on the empty scaffold returns INVALID; after filling all 9 categories it returns VALID.
- case: a scene containing a forbidden element (e.g. "logos") is QUARANTINED; a scene with an environment outside the rotation is QUARANTINED; a clean scene passes.
- expected failure: a world missing forbidden_hues fails validation.
- regression: `scripts/test_world.py` (6/0).
