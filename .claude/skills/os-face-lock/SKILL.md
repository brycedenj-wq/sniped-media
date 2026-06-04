---
name: os-face-lock
description: Keep one original character the SAME face across stills, edits, and motion. Use when locking an approved hero as the reference anchor, checking whether a new frame still looks like the hero, conditioning generation on the hero, or running the pre-video readiness gate before spending motion credits.
---

# os-face-lock

Turn an approved still into the reference anchor so future assets condition on THAT face instead of regenerating from text. Wraps `os_herolock.py`, `os_facematch.py`, `os_face.py`, `os_motion_ready.py`, and `os_generate.py ref-package`.

## INVOKE WHEN
- an approved hero should become the locked reference ("lock this hero")
- "does this still look like AXIS?" , a face-match check against the locked hero
- generating a continuity-critical still/clip (must condition on the hero, not text)
- before any video spend , the motion-readiness gate

## Inputs
- a CRS slug + world slug + an approved hero asset (and its preserved source)
- a candidate frame to check against the locked hero
- a vision identity score (0..1) for the face-match call
- scene + frame observations for the readiness gate

## Outputs
- a locked-hero record (`os_herolock register`) with all paths + gate reports + allowed use cases
- a face-match verdict (PASS / QUARANTINE / NEEDS-VISION) + side-by-side crop
- a reference-conditioned generation package (start_image / identity reference)
- a motion-readiness verdict (READY / BLOCKED) across all six gates

## Procedure
1. Lock: `os_herolock.py register --hero-id ... --approved ... --source ... --usecases "still-reference;video-start-image;identity-gate-anchor"`.
2. Match: `os_facematch.py gate --hero <approved> --candidate <frame> --out side.png`; read the side-by-side; re-run with `--vision-score`. PASS needs auto >= floor AND vision >= threshold.
3. Condition: `os_generate.py ref-package --hero <url> --kind image|video` , continuity assets condition on the hero (no fresh text-only face).
4. Ready: `os_motion_ready.py check ...` , READY only if world + pillars + face-match + signature + vision-gate + harness-audit all pass. Do NOT spend video credits until READY.

## Gates
- face-match: auto SSIM proxy can only SCREEN gross drift; the vision identity score is authoritative (no faked face recognition)
- herolock: refuses to register if the approved or source asset is missing (source must be preserved)
- motion-readiness: BLOCKED unless all six gates pass; it is the pre-spend checkpoint
- mark-injection (via os_mark --anchor inner_left_eye): landmark-placed, non-destructive, logged

## Test
- case: face-match returns PASS only with auto>=floor AND vision>=threshold; gross structural mismatch quarantines on the floor; missing vision -> NEEDS-VISION.
- case: herolock refuses a missing approved/source asset; a valid register stores the anchor use cases.
- case: motion-ready is BLOCKED if any one gate fails (audit, face-match, pillars, world, signature, vision) and READY only when all pass.
- case: ref-package video uses the start_image role; image conditions on the hero.
- regression: `scripts/test_facelock.py` (15/0).
