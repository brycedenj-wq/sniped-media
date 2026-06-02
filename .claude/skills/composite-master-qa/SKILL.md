---
name: composite-master-qa
description: Force every SNIPED campaign composite through the COMPOSITE_MASTER_QA gates before it can be called believable, shown to a client, or placed in a deck. Use when compositing a locked subject into any generated or shot world (Higgsfield / Seedream plates, backplate drops), when a hero needs a physics + art-director pass, when scoring grounding / shadows / heels / edge / sensor-match, or when the user says "QA this composite", "run the composite laws", "is this client-ready", "did the physics pass". Subject grade stays LOCKED; the work is environment integration only. Enforces two-shadow grounding, relight, transparent-heel handling, surface displacement, cutout-tell kill, sensor match, hard artifact rejection, and the 6-axis scorecard. Refuses "believable" claims without proof crops and scores.
---

# Composite Master QA

You are running the SNIPED campaign composite law. The full standard is:
`00_COMMAND_CENTER/_standards/COMPOSITE_MASTER_QA.md` (canonical) and the mirror copy inside the active project folder. Read the canonical file first; it is the source of truth and may have been updated.

## Prime directive

The subject's graded TIFF/PNG (color, skin, contrast, identity) is LOCKED. Never reinterpret, flatten, or re-skin the subject. Everything you do is ENVIRONMENT INTEGRATION: make the locked subject sit inside the plate as if captured by the same camera, same light, same ground. If a step would change the subject's color or skin, it is out of scope.

## How to run

1. Read the canonical `COMPOSITE_MASTER_QA.md` for the current 8 gates and scoring rubric.
2. For each hero, integrate (or re-integrate) against all 8 gates:
   - G1 biological reality (flyaways, pores, garment edges)
   - G2 relight to the plate (rim/wrap, direction, bounce, warmth)
   - G3 two-shadow grounding (contact flush + cast anchored, plate-matched, never pure black, never detached)
   - G4 surface interaction (sink + displacement on soft ground, occlusion on hard ground)
   - G5 transparent/reflective objects (clear acrylic heels: warm ground reflection, refraction, occlusion)
   - G6 kill the cutout tell (0.5-1px feather, defringe, light wrap)
   - G7 sensor match (black/white point, contrast, temp, then ONE global grain)
   - G8 artifact rejection (hard reject AI-fill smear, warped geometry, stretched pixels, barcode sky, melted plants, repeated textures)
3. Produce the required proof for every hero (no shortcuts):
   - final no-text hero
   - final text / drop-card
   - 100% hair/edge crop
   - 100% feet/shadow (contact-point) crop
   - before/after (studio frame to campaign)
   - QA scorecard: lighting, grounding, edge, color marriage, artifact scan, brand fit (each /10)
   - status: client-ready / internal-only / rebuild
4. ACTUALLY LOOK at the 100% crops with the Read tool before scoring. Score from the pixels, not from intent. Client-ready requires every axis >= 8 and no Gate-8 reject.
5. Concept discipline: a pretty AI plate is not a concept. Brand fit fails if the world competes with the product or is a generic plate with no drop logic.

## Refusals

- Refuse to call anything "believable" or "client-ready" without the proof crops and the six scores.
- Refuse to reinterpret the locked subject grade.
- Refuse to pass a hero with a floating / detached shadow, a sterile clear-heel, or any Gate-8 artifact.

## Mandatory close-out (durability)

After any phase that changes a hero or its status, you MUST:
1. Update the project `SESSION_STATE.md` (objective, files, passed, failed, per-hero status, next step, commands).
2. If the project folder is a git repo, commit the milestone with a one-line message naming the phase and the new status.

This is non-optional. It is the habit that makes a restart never lose the work.
