---
name: kling-production-sop
description: Route and gate an AI motion/video clip so it holds character + world consistency, not random slop. Use when turning a locked character + world into a short dialogue-free motion clip, choosing the video model, preflighting credits, or QA-gating a generated clip before it ships.
---

# kling-production-sop

Produce one short, dialogue-free motion clip of a locked character inside a locked world, gated the same way stills are. Wraps `os_generate.py` (video path) + `os_motion_qa.py`. Generation requires explicit approval; this SOP builds and gates to the edge of spend.

## INVOKE WHEN
- a locked character + world need a motion clip
- "make AXIS move / animate the hero / build a short clip"
- choosing a video model or estimating clip cost
- QA-gating a generated clip before it is allowed to ship

## Inputs
- a VALID CRS slug (character) and a VALID world slug
- a one-scene brief (environment from the world rotation, action, duration in seconds)
- the chosen image hero (image-to-video base) once Phase 1 frames exist
- for the gate: clip observations (sampled-frame invariants + motion rubric scores)

## Outputs
- a preflight credit estimate (no spend) via `os_generate.py prep-video`
- a generation PACKAGE.json (prompt, negatives, model, aspect, gates, cost)
- a MOTION_QA_REPORT.json with verdict SHIP / QUARANTINE and named reasons
- a one-line receipt

## Procedure
1. Confirm `os_crs.py validate <crs>` and `os_world.py validate <world>` both VALID, and the hero is locked (`os_herolock`).
2. Run `os_motion_ready.py check ...` , must be READY (world + pillars + face-match-to-locked-hero + signature + vision + audit). If BLOCKED, do not spend.
3. Condition on the locked hero: `os_generate.py ref-package --hero <url> --kind video` (Seedance start_image). No fresh text-only face for motion.
4. `os_generate.py prep-video <project> <prompt_id> <seconds>` , preflight credits. STOP and ask for approval before any generation.
5. (Only after approval) generate image-to-video via the Higgsfield MCP; `ingest-video` (FAILED-not-complete on bad download, no placeholder).
6. Sample frames, run `os_motion_qa.py gate --crs <crs> --world <world> --clip <file>` , quarantine on any hard failure; identity-hold across sampled frames is checked against the locked hero.

## Gates
- identity-hold (AXIS hard invariants per sampled frame) , HARD
- world-continuity (forbidden elements / off-rotation environment) , HARD
- motion rubric hard-zero (grounding / edge_integrity / temporal_stability / ai_tells) , HARD
- overall motion score >= threshold
- no generation without explicit approval; SHIP = eligible for human taste, never auto-post

## Test
- case: a clean clip (good invariants, clean scene, all motion items 2) returns SHIP.
- case: a clip with an identity-drifted sampled frame, a forbidden element, a hard-zero motion item, or a sub-threshold score returns QUARANTINE with named reasons.
- case: the cost estimator refuses to invent a rate (returns None + UNCONFIRMED) and computes ceil(seconds*rate) when given one.
- regression: `scripts/test_motion.py` (10/0).
