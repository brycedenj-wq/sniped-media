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
