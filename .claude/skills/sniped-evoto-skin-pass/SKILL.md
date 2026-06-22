---
name: sniped-evoto-skin-pass
description: Run SNIPED's locked Evoto skin work pass per the tactical extraction. Use when a frame has cleared Lightroom and routed to Evoto in the retouch decision tree. Skin retouch (blemishes, texture, dark circles, gentle wrinkle pull), backdrop cleanup (vinyl wrinkles, banding), backdrop replacement (same studio register only), gentle body refinement.
---

# SNIPED Evoto Skin Pass Skill

The Evoto leg of the pipeline. Output target: polished-but-real skin that holds up at 100% zoom, no waxy artifacts.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/10_REFERENCE/EVOTO_TACTICAL_EXTRACTION.md` · Evoto playbook
2. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/lightroom_operating_system.md` Section 7 · retouch decision tree (what Evoto IS and ISN'T for)
3. Memory: `[[feedback-edit-register-bifurcation]]` · skin texture rules

## INVOKE WHEN
- Frame routed to Evoto per the retouch decision tree (Q3 yes)
- "What Evoto settings should I use"
- Training on the SNIPED Evoto preset
- Debugging Evoto output

## OUTPUT
Walk:
1. Import 16-bit TIF from Lightroom (NOT JPG · destroys gradients)
2. Apply locked SNIPED Evoto preset (skin clinical · pore detail preserved · spot removal high · eye whitening LOW · teeth whitening LOW)
3. Review at 100% on face · click any blemishes Evoto missed
4. Backdrop cleanup if needed (wrinkles in vinyl, color banding)
5. Backdrop replacement if requested · same studio register only (different color OK, different environment NO · that's Photoshop)
6. Gentle body refinement · NEVER aggressive
7. Export 16-bit TIF, suffix `_evoto`, route back to Lightroom for Hero Finish

## EVOTO IS NOT FOR
- Compositing (Photoshop)
- Color grading (Lightroom)
- Studio-register-breaking work (Photoshop)
- Aggressive liquify (refused entirely)
- Identity changes (BANNED per identity rule)

## REFUSE
- Eye/teeth whitening above the locked low setting (reads fake)
- Body work on Reset frames (Reset = clinical skin only)
- Backdrop replacement that breaks studio register
- Skin smoothing that strips pore detail


## Inputs
- 16-bit TIF exported from Lightroom (NOT JPG: destroys gradients)
- Retouch routing confirmation: Q3 = yes in the retouch decision tree
- Frame type: Reset (skin-clinical only) vs. Op Kit / Brand System (allows backdrop cleanup and gentle body work)
- Any specific blemishes or backdrop issues flagged by the operator

## Gates
- 16-bit TIF input required: starting from a JPG is a gate violation
- Eye whitening and teeth whitening must remain at locked LOW setting; above-low reads fake and is refused
- No body work on Reset frames and no backdrop replacement that breaks studio register (different color allowed, different environment is Photoshop)
- No compositing, color grading, or aggressive liquify in Evoto: those are Photoshop and Lightroom lanes respectively
- Skin smoothing must preserve pore detail: stripping pore detail is a gate violation

## Test
- case: A Reset frame has cleared Lightroom and is routed to Evoto (Q3 = yes). There are 3 blemishes the healing brush missed and the vinyl backdrop has a horizontal wrinkle. Expected output: 7-step walkthrough starting with 16-bit TIF import, SNIPED locked preset applied, 100% zoom blemish review + manual spot clicks for the 3 missed blemishes, backdrop wrinkle cleanup, export as _evoto TIF back to Lightroom. Eye/teeth whitening confirmed at LOW.
- expected failure: If the input file is a JPG (not 16-bit TIF), the skill must refuse to proceed and instruct the operator to re-export from Lightroom as 16-bit TIF before the Evoto pass begins.
