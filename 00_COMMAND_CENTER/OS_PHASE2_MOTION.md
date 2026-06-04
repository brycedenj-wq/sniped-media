# PHASE 2 OUTPUT , THE MOTION LAYER (2026-06-04)

> Proof that the OS can control MOTION the same way it now controls character and world. Built and tested to the edge of generation. No clip generated. No credits spent. Stops at the approval line.

## Files created / changed
- `scripts/os_motion_qa.py` , NEW. Motion QA gate (rubric + identity-hold + world-continuity), pure `judge_clip` core.
- `scripts/os_generate.py` , CHANGED. Added `prep-video` (preflight, no spend) + `ingest-video` (FAILED-not-complete on bad/<50KB, no placeholder) + `estimate_video_credits`.
- `scripts/os_crs.py` , CHANGED. Extracted `evaluate_frame`; FIXED identity-hold to score HARD invariants only (soft invariants may vary and must not penalize).
- `scripts/os_world.py` , CHANGED. Extracted `evaluate_scene` shared core.
- `scripts/test_motion.py` , NEW. 10 tests.
- `scripts/test_crs.py` , CHANGED. +2 tests locking soft-invariant variation.
- `.claude/skills/kling-production-sop/SKILL.md` , NEW, born ACTIVE.
- `campaign_house/productions/axis_meridian_motion_001/` , PACKAGE.json + clip_clean.json + clip_fail.json + MOTION_QA_REPORT.json.

## Commands added
- `os_motion_qa.py rubric` , print the rubric.
- `os_motion_qa.py gate --crs <slug> --world <slug> --clip <file> [--threshold 0.75]` , judge a clip.
- `os_generate.py prep-video <project> <prompt_id> <seconds> [--rate] [--threshold]` , preflight credits, no spend.
- `os_generate.py ingest-video --project --prompt --gen --url --credits --model --asset` , safe mp4 ingest.

## Tests run and results
| Suite | Result |
|---|---|
| test_motion.py | 10 / 0 |
| test_crs.py | 17 / 0 |
| test_world.py | 6 / 0 |
| test_skill_substrate.py | 11 / 0 |
| test_production_harness.py | 14 / 0 |
| **Total** | **58 / 0** |

A real bug was found and fixed mid-build: the identity gate scored over ALL invariants, so a frame that held every HARD invariant but varied a SOFT one (hair, brow) was wrongly quarantined , the "clean" real-atom clip failed. Fix = hard-only identity scoring; 2 regression tests now lock it. The failure became a build item, per the rule.

## Motion QA rubric
Each item scored 0 (fail) / 1 (weak) / 2 (clean). HARD items quarantine the clip if scored 0.
- **grounding** [HARD] , feet/contact + shadow anchored; no floating or sliding.
- **edge_integrity** [HARD] , stable silhouette; no warping/melting/boiling edges.
- **temporal_stability** [HARD] , no flicker; no identity morph or texture crawl frame-to-frame.
- **ai_tells** [HARD] , no extra/fused fingers mid-motion, no face warp, no melt.
- **physics** [soft] , plausible body/cloth/hair motion.
- **register** [soft] , motion matches AXIS's composed register.
- **beat_source** [soft] , beats a static hero still as a moving asset (taste-assisted).
- plus **identity-hold** [HARD] (AXIS hard invariants per sampled frame) and **world-continuity** [HARD] (MERIDIAN-HOUSE).
- **SHIP** requires: no identity quarantine, world pass, no HARD motion item == 0, score >= threshold. SHIP = eligible for human taste, never auto-post.

## What gets quarantined (proven on the REAL atom)
The failure clip (`clip_fail.json`) was QUARANTINED with every reason named: identity drift at t3.0 (eye_color, mole, face_geometry), world forbidden element (logos), three HARD-zero motion items (edge_integrity, temporal_stability, ai_tells), motion score 0.286 < 0.75, and an off-palette advisory. The clean clip (`clip_clean.json`) SHIPs (score 1.0, 0 identity quarantines).

## What still requires human taste
- the premise/scene brief and the action choice.
- approving the hero still's face before it becomes the motion base.
- the `beat_source` call and the final cut.
- the kill/keep/scale decision.
- producing the per-frame vision observations that feed the gate (until a vision-extraction pass is wired, a human/vision read fills them).
- the go/no-go on every spend.

## What is now executable (by test, not assertion)
Judge a motion clip on identity-hold + world-continuity + a 7-item motion rubric · quarantine drift/slop with named reasons · preflight video credits without spending · ingest video with no placeholder on failure · all wrapped as the ACTIVE `kling-production-sop` skill. Skill dashboard: ACTIVE = 4 (skill-template, sniped-crs-builder, os-world-bible, kling-production-sop), INSTALLED_INCOMPLETE = 68.

## The exact first motion test package
`campaign_house/productions/axis_meridian_motion_001/PACKAGE.json` , AXIS inside a MERIDIAN-HOUSE Brutalist Monument.
- **Stage 1 hero still:** Nano Banana Pro, 3:4, 1k, count 1. Full prompt + negatives + the 5 invariants to hold (in PACKAGE.json).
- **Stage 2 motion clip:** Seedance 2.0, image-to-video from the hero, 4s, 3:4, 720p std, dialogue-free, composed in-register motion. Full prompt + negatives in PACKAGE.json.
- Gates applied after generation: identity-hold, world-continuity, motion rubric (threshold 0.75).

## Preflight credit / cost estimate (live, no spend)
Grounded by Higgsfield `get_cost` preflight (returns cost without submitting a job) + balance read:
- hero still (Nano Banana Pro, 3:4): **2 credits**
- motion clip (Seedance 2.0, 4s, 3:4, 720p): **18 credits**
- **total first test: 20 credits.** Balance now **881**, would be **861** after.

## STOP , approval required before any generation
Phase 2 is built and proven to the edge of spend. Nothing was generated. The next step is the only one that costs credits, so it waits for an explicit go. See the approval question in chat.
