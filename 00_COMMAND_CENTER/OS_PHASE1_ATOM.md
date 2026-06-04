# PHASE 1 OUTPUT , THE CHARACTER + WORLD ATOM (2026-06-04)

> The first real atom the 2026 production machine stands on: one original character, one world, one visual language, one reference system, one consistency gate. Consistency is defined and gated IN CODE, never claimed from doctrine. No generation performed. No credit spent.

## Files created
- `scripts/os_crs.py` , Character Reference System engine (new / validate / sheet / gate / leakcheck / show). Negation-aware identity-leak guard.
- `scripts/os_world.py` , World Bible engine (new / validate / continuity / show).
- `scripts/test_crs.py` , 15 tests, 0 fail.
- `scripts/test_world.py` , 6 tests, 0 fail.
- `campaign_house/characters/char_axis_01/CRS.json` , the original character spec (VALID).
- `campaign_house/characters/char_axis_01/SHEET_PLAN.json` , the 14-reference sheet PLAN (plan only).
- `campaign_house/characters/char_axis_01/consistency/gate_report.json` , a real gate run.
- `campaign_house/worlds/world_meridian_01/WORLD.json` , the original world bible (VALID).

## Skills created (both born ACTIVE under the contract)
- `sniped-crs-builder` , ACTIVE (installed, discoverable, trigger, inputs, outputs, tests, invokable).
- `os-world-bible` , ACTIVE (same six criteria).

## Tests passed / failed
| Suite | Result |
|---|---|
| test_crs.py | 15 / 0 |
| test_world.py | 6 / 0 |
| test_skill_substrate.py | 11 / 0 |
| test_production_harness.py | 14 / 0 |
| **Total** | **46 / 0** |

One failure was found and fixed mid-build: the identity-leak guard flagged the spec's own responsible disclaimer ("not resembling any real person"). Fix = negation-aware guard; a new regression test now locks both directions (disclaimer passes, "looks like <Name>" still fails). The failure became a build item, per the rule.

## The original character , AXIS (codename `char_axis_01`)
Fully original synthetic figure, not derived from or resembling any real or public person. Public name deferred to the name-availability gate (not a brand decision).
- **Face/body:** androgynous, ageless late-20s read; angular symmetrical bone structure, high cheekbones; deep-brown eyes; signature mole ~1cm below the inner-left eye; matte natural-texture skin; even ambiguous mid-tone complexion; 5'10 lean-athletic.
- **Wardrobe/palette:** charcoal wool overcoat, bone cotton, raw-hem black trousers, matte leather; charcoal/bone/graphite + sparing oxblood. No logos, no pattern.
- **Lighting/camera:** single soft 45deg key, 1:8 fill, deep falloff, chiaroscuro; 85mm portrait f1.8-2.8, 50mm environmental; eye-level or slightly below; negative space.
- **Expressions/poses:** four-register set (composed-neutral default, slow-burn intensity, near-imperceptible smile, contemplative); contrapposto / seated forward-lean / mid-stride / hands-in-pockets.
- **Identity invariants (the consistency anchor):** 5 HARD , eye_color, mole_below_left_eye, face_geometry, build, complexion. 2 soft , brow_weight, hair_style.
- **Variation rules:** hair, wardrobe (within palette), environment, expression, pose MAY vary; the 5 hard invariants MUST NOT.

## The original world , MERIDIAN-HOUSE (codename `world_meridian_01`)
Monumental, quiet, architectural world; a single figure in vast bone-white and concrete space; editorial stillness over cinematic drama.
- **Environments (3 anchors from the locked 7-env rotation):** Brutalist Monument, Monochromatic Void, Sculptural Gallery. One per chapter.
- **Materials:** board-formed concrete, bone plaster, brushed steel, smoked glass, wool, oxblood leather.
- **Light logic:** one dominant cool north source, hard-soft hybrid, deep shadow tolerance, raking; no gels, no flare.
- **Color system:** Adobe Neutral foundation; charcoal/bone/graphite/oxblood; FORBIDDEN: teal-orange, neon, saturated primaries, warm golden wash.
- **Camera language:** editorial restraint, 50/85mm, static or slow, negative space, architectural symmetry.
- **Forbidden elements (10):** logos, text overlay, crowds, busy props, lens flare, teal-orange, plastic-skin tells, real-brand objects, visible modern screens, stock gloss.
- **Recurring motifs:** lone figure dwarfed by space; raking light on bare surface; one oxblood accent per frame max; bone-meets-concrete; aperture as frame-within-frame.
- **SREF/style slots:** 3 slots (primary editorial / brutalist architectural / grain) , all TBD-manual-pull (no in-OS Midjourney route yet).
- **Continuity rules (6):** one environment per chapter; palette locked, oxblood once per frame; consistent light direction per sequence; AXIS the only recurring human; no forbidden elements; sref slots fixed per chapter.

## The consistency gate (proven on the real atom)
`os_crs.py gate` compares per-frame observed invariants to the spec. On the real character: `hero_v1` scored 1.0 (pass); `drift_v2` (green eyes, no mole, round face) scored 0.571 and was QUARANTINED, naming the 3 hard failures. Hard-invariant mismatch OR score < threshold = quarantine, no silent pass. The world has a parallel continuity gate (forbidden element / off-rotation environment = quarantine), also proven.

## What remains MANUAL
- pulling the 3 SREF/style codes by hand from Midjourney (no in-OS route; world slots marked TBD).
- the actual generation of the 14 reference frames (requires approved credit spend , not done).
- producing the per-frame observations that feed the consistency gate (a vision pass over generated frames; until then the gate is proven on declared observations).
- covert-leak judgment: the guard catches obvious real/celebrity references; subtle ones remain the operator's call.
- the public name for AXIS and MERIDIAN-HOUSE (name-availability gate, later).

## What is now EXECUTABLE (proven by test, not asserted)
- define an original character as a structured, validated spec , `os_crs.py` (VALID on the real atom).
- refuse real/celebrity-leak inputs , negation-aware guard (15/0).
- plan a 14-reference sheet , `os_crs.py sheet` (plan only).
- gate cross-frame identity drift , `os_crs.py gate` (quarantines real drift).
- define a world as 9 validated rule categories , `os_world.py` (VALID on the real atom).
- gate scene continuity , `os_world.py continuity` (quarantines forbidden elements / off-rotation envs).
- both wrapped as ACTIVE invokable skills.

## Updated skill dashboard
ACTIVE = **3** (skill-template, sniped-crs-builder, os-world-bible) · INSTALLED_INCOMPLETE = 68 · DRAFTED = 0 · MALFORMED = 0 · total tracked = 71. Source of truth: `OS_SKILL_REGISTRY.csv`; view: `OS_SKILL_DASHBOARD.md`. No bulk activation; only contract-complete skills counted.

## Next-phase recommendation
**Phase 2 , Video/motion, gated by this atom.** Build `os_generate` video path + `os_motion_qa.py` + `kling-production-sop` (born ACTIVE). The first motion test must render AXIS in a MERIDIAN-HOUSE environment and pass both the identity-consistency gate (same character) and the motion-QA gate (grounding/edges/physics/identity-hold) before anything ships. That is also the moment a generation pass is first required , so before Phase 2 produces real frames, I will STOP and ask for explicit approval to spend credits (preflighted cost first). Until then, Phase 2 builds the engine + gates + skill and tests them on synthetic frame observations, exactly as Phase 1 did.

## Guardrails honored
No real likeness. No celebrity. No employer data/tools/relationships/identity leakage. No old lane. No brand decision (names are codename placeholders pending the name gate). No posting. No credit spent. No bulk skill activation. Nothing marked done without a passing test.
