---
name: sniped-crs-builder
description: Build and gate a Character Reference System for a fully ORIGINAL (non-real, non-celebrity) character so it survives multiple outputs. Use when defining a new character, building a 14-reference sheet, locking identity invariants, or checking cross-frame consistency before any campaign-house generation run.
---

# sniped-crs-builder

Define one original character as a structured, gateable spec, then prepare it for generation without ever claiming consistency from doctrine. Wraps `00_COMMAND_CENTER/scripts/os_crs.py`.

## INVOKE WHEN
- a new original character is needed for the campaign house
- "build the character / lock the look / make a reference sheet"
- before any image or video run that must keep one identity stable
- when checking whether generated frames held the identity (consistency gate)

## Inputs
- `slug` , kebab/underscore id for the character
- character design intent (face, body, wardrobe, palette, lighting, camera, expressions, poses)
- the identity invariants that must NEVER change (the consistency anchor)
- optional: frame observations (JSON) from an approved generation pass, for the gate

## Outputs
- `campaign_house/characters/<slug>/CRS.json` , the validated structured spec
- `SHEET_PLAN.json` , the 14-reference sheet plan (PLAN ONLY, no generation)
- `consistency/gate_report.json` , per-frame pass/quarantine with named hard failures
- a one-line receipt of what was defined/gated

## Procedure
1. `os_crs.py new <slug>` , scaffold (refuses real/celebrity-leak names).
2. Fill CRS.json. The TRUE identity structure is FOUR HARD pillars: eye_color, face_geometry, build, complexion. Fragile micro-details (e.g. a small mole) are SOFT signature_details, never hard gates (RUN-001 lesson).
3. `os_crs.py validate <slug>` , must return VALID before proceeding.
4. `os_crs.py sheet <slug>` , write the 15-ref PLAN (includes frame 15, the tight identity-lock verify crop). STOP here; generation requires approved credit spend (ask first).
5. After an approved generation pass: `os_crs.py verifycrop <image>` to get a checkable face crop, read it, collect frame observations, run `os_crs.py gate <slug> --frames FILE`.
6. If a signature detail dropped but the 4 pillars held, restore it with the LOGGED stage `os_mark.py inject --src ... --out ... --x --y --reason ... --log MARK_INJECTION_LOG.csv` (never overwrites the source, always logged).

## Gates
- identity-leak guard: refuses real-person / celebrity references (covert leaks remain the operator's call)
- completeness gate: no field empty, >=1 hard invariant, must_not_vary populated
- consistency gate: a HARD-pillar mismatch quarantines; a missing SOFT signature does NOT
- mark-injection discipline: signature retouch must write a new asset + a log row; silent/in-place edits are refused
- no generation without explicit approval

## Test
- case: `os_crs.py new t01` then `validate t01` on the empty scaffold returns INVALID; after filling all fields with >=1 hard invariant, `validate` returns VALID.
- case: a frame whose observed eye_color/face/build/complexion differs from a hard pillar is QUARANTINED by `gate`, and the report names the hard failure.
- case: a frame missing only the SOFT signature (mole) but holding the 4 pillars is NOT quarantined.
- expected failure: `new` with a name like "looks like <celebrity>" is REFUSED and writes nothing.
- regression: `scripts/test_crs.py` (26/0) + `scripts/test_mark.py` (8/0).
