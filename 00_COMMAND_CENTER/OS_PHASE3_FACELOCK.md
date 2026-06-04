# PHASE 3 , FACE-LOCK + REFERENCE-CONDITIONING (2026-06-04)

> The build that turns an archetype into ONE consistent character. Text pillars define a type; the approved hero is now the reference anchor. Built and tested to the edge of generation. No video generated. No credits spent beyond the 4 already used for the two heroes.

## What was built
1. **Locked-hero registry** , `os_herolock.py`. Records approved path, source path, face crop, identity crop, mark-injected path, approved date, gate reports, and allowed use cases. Refuses to register if the approved or source asset is missing (source must be preserved). Registry: `OS_LOCKED_HERO_REGISTRY.csv`; record: `campaign_house/locked_heroes/<id>/HERO.json`.
2. **Face-match gate** , `os_facematch.py` + `os_face.py` (cv2 Haar). "Does this still look like the hero?" Honest two-part design: an SSIM proxy on cv2-aligned face crops SCREENS gross drift (can only fail, never solely pass), and a required vision identity score is authoritative. No faked face recognition (no embedding model is installed; the hook is there for when one is added).
3. **Reference-conditioned generation** , `os_generate.py ref-package`. Continuity-critical stills/clips condition on the locked hero (`start_image` / identity reference), never fresh text-only faces.
4. **Landmark mark-injection** , `os_mark.py --anchor inner_left_eye` uses cv2 eye detection to place the signature deterministically (no manual guessing); still non-destructive and logged. Manual `--x/--y` remains as fallback.
5. **Motion-readiness gate** , `os_motion_ready.py`. Composite pre-video checkpoint: world + 4 hard pillars + face-match-to-locked-hero + signature(present or logged-injection) + vision-gate + harness-audit. READY only if ALL pass.
6. **Skill** , `os-face-lock` (born ACTIVE). `kling-production-sop` updated to require readiness + reference-conditioning.

## Tests (all green)
| Suite | Result |
|---|---|
| test_facelock.py | 15 / 0 |
| test_crs.py | 26 / 0 |
| test_world.py | 6 / 0 |
| test_motion.py | 10 / 0 |
| test_mark.py | 8 / 0 |
| test_skill_substrate.py | 11 / 0 |
| test_production_harness.py | 14 / 0 |
| **Total** | **90 / 0** |

## Proven on the REAL hero (no spend)
- **Face-match discriminates:** locked hero vs the same person -> PASS (auto 0.98, vision 0.97); locked hero vs a DIFFERENT face (v1) -> QUARANTINE (auto 0.30 could NOT tell them apart, vision 0.10 caught it). This is exactly why the vision layer is authoritative and the proxy only screens.
- **Auto-anchor works:** cv2 placed the mole anchor at the detected inner-left-eye (476,596), matching the hand-corrected point , landmark placement, not guessing.
- **Locked hero registered:** `axis_v2` , approved `axis_hero_v2_marked.png`, source preserved, crops + gate reports recorded, anchors for still-reference / video-start-image / identity-gate-anchor.
- **Motion-readiness READY:** all six gates pass on the approved hero. (Surfaced and fixed a real artifact: registry crops placed inside `06_approved` polluted the harness audit; moved them into the hero record, audit went CLEAN.)

## Skill dashboard
ACTIVE = **5** (skill-template, sniped-crs-builder, os-world-bible, kling-production-sop, os-face-lock). INSTALLED_INCOMPLETE = 68.

## What still requires human taste / vision
- the face-match identity score (the authoritative call) is vision-read, not automated , by design until a face-embedding model is added.
- approving the locked hero in the first place.
- the kill/keep/scale and final-cut decisions.

## Honest limitation carried forward
The face-match proxy is structural (SSIM), not identity embeddings. It cannot, alone, distinguish two different faces in the same pose/lighting (0.30 for a different person). The gate is correct because vision is required, but a real face-embedding model (e.g. an ONNX ArcFace) would let the auto layer carry more of the load. Build item: drop in an embedding model and switch the proxy to cosine similarity, keeping vision as the tie-breaker.

## The gate is now closed before spend
`os_motion_ready.py` returns READY for the locked hero. Per the rule, the first video spend happens ONLY after Phase 3 passes , which it now does. The next action is the single 4-second clip, reference-conditioned on the locked hero, and it still requires an explicit spend approval (preflighted at 18 credits). See the approval question.
