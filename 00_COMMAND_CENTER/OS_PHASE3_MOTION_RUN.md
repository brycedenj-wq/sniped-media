# PHASE 3 , FIRST MOTION CLIP RUN (2026-06-04)

> The real test: can the locked-hero + reference-conditioned pipeline hold identity through video? It did. Built gates ran on a real Seedance clip; identity held through a head turn.

## Spend
- **18 credits** (one 4s Seedance 2.0 clip). Balance 877 -> **859** (confirmed). Session total: 22 credits (2 + 2 + 18). No variants, no second clip, no posting.

## What ran
1. Uploaded the marked hero to Higgsfield (`media_upload` + `media_confirm`) -> media_id `491cedf0...`.
2. Generated ONE clip: Seedance 2.0, 4s, 3:4, 720p, **start_image = the locked hero** (reference-conditioned), dialogue-free composed-motion prompt.
3. Ingested into the harness (`ingest-video`, 1.9MB real mp4, no placeholder).
4. Sampled 10 frames (t0..t3.9, dense over the turn) via ffmpeg.
5. Ran identity-hold, world-continuity, motion-QA, and per-frame face-match vs the locked hero.

## Gate results , the clip SHIPS (per gates)
- **Identity-hold:** PASS. The 4 hard pillars held across all sampled frames; 0 identity quarantines.
- **Face-match vs locked hero (vision-confirmed):** PASS at t0 (0.97), t2 (0.95), t3.9 (0.88). At t3.9 the auto SSIM proxy fell to 0.197 (below the different-person baseline) purely from the **head turn / pose**; vision confirmed it is the same person. This is the designed behaviour: the proxy screens, vision decides.
- **World-continuity:** PASS. Stayed inside MERIDIAN-HOUSE brutalist concrete; no forbidden elements.
- **Motion-QA:** SHIP, score **0.929**. No hard-zero items. The head turn was smooth , no melting, warping, or face morph in the sampled frames.

## What held
- **Identity held through motion.** Reference-conditioning on the locked hero kept the same face, bone structure, complexion, and both moles from frontal through a 3/4 turn toward the light. This is the core thing Phase 3 set out to prove.
- World, register, and composition stayed in-spec.
- Cost discipline: one clip, 18 credits, reconciled.

## What did NOT fully pass / honest caveats (logged, not hidden)
- **temporal_stability scored 1 (weak), not 2.** A mild WARM color drift over the 4s (cooler start -> warmer end) , a soft grade inconsistency, not a hard fail. It did not quarantine but it is real.
- **Sampled-frame assessment, not full playback.** Identity/motion were judged from 10 sampled frames; brief inter-frame flicker or sub-second warps between samples cannot be fully ruled out by this method. A full-playback human pass is the final taste step before any use.
- **Audio defaulted ON.** `generate_audio` was true by model default; I did not request audio. Dialogue-free intent holds (no speech), but the asset carries model audio that should be stripped before any real use.

## Verdict
- **The locked-hero + reference-conditioned motion pipeline CAN hold identity through video.** Proven on a real clip, gated, logged, shippable. The approved clip is at `06_approved/axis_motion_v1.mp4`.
- This is the first end-to-end proof that one original synthetic character stays consistent across stills, edits, AND motion , the thing that makes a one-person campaign house real.

## Next cheapest corrections (not run; for when you choose)
- strip the default audio (free, ffmpeg `-an`).
- neutralize the warm color drift (free, a grade pass in DaVinci/Lightroom on export).
- if temporal stability ever fails harder: lower motion magnitude or shorten the turn (re-gen cost, only on approval).
- swap the SSIM proxy for an ONNX face-embedding model so the auto layer survives pose (the standing Phase-3 build item).

## Guardrails honored
18 of 18 approved credits. One clip. No variants. No regeneration to "fix." No posting. Identity gated against the locked hero. Caveats reported as data.
