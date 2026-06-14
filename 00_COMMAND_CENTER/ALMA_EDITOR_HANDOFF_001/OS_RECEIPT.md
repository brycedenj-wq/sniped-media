# OS_RECEIPT - Alma in-house reel V5 (7-role harness) + orchestrator decision

Supersedes the V4 receipt (archived: OS_RECEIPT_V4_archived.md).

## Layer 1 - scan
- domain film | serious=True | mode=MAX. Harness-mandatory law: NOT single-threaded.
- Pipeline = the `alma-v5` workflow (`.claude/workflows/alma-v5.workflow.js`), run id `wf_cebfe65a-73f`.

## The harness (the 10 required proof items)

### 1. Harness name
`alma-v5` dynamic workflow. 6 phases: Moment-verify -> Grade+brand -> Synthesize-spec -> Build -> Verify -> Verdict.

### 2. Agents spawned
24 fresh-context agents. 1.16M subagent tokens, 776 tool uses, ~25 min wall clock.

### 3+4. Role of each + what each contributed
- **Orchestrator (me):** pinned the GOAL + 9 hard constraints into every agent prompt (defends goal drift), owns the final decision, wrote this receipt. Did NOT let any agent crown its own work.
- **14 Moment agents (sonnet, parallel):** one per V4 cut entry. Whole-watched each clip (no sampling) and reported the truth. Contribution = they CAUGHT THE MATERIAL: idx2 IMG_9510 body 0.82 / thirst HIGH / claimed lens-wipe FALSE (3 accidental lens occlusions); idx4 D94A3317 "deadpan pose" does NOT exist (continuous motion + rear-pivot, body 0.82); idx9/10 IMG_9523 = a SECOND different-faced model (identity blocker) + false wipe; idx1 body 0.6; idx5 body 0.75 redundant. They also tightened every in/out and confirmed the real hero (D94A3316 eye-contact, body ~0.15).
- **Grade agent (sonnet):** measured pre-grade B-R per clip (IMG_9510 +24, D94A3320 +30, IMG_9524 +16, IMG_9523 +19, IMG_9542 +11 cool; D94A3317 -4 warm), set ONE master target B-R -2, emitted per-clip colortemperature+eq corrections that bring held shots to a -3..+3 spread. This is the V4 grade fix landing on the held shots.
- **Brand/taste agent (opus):** flagged body-forward beats [1,2,5,8,10], hero_is_longest_hold=FALSE, set transition_policy=honest_hardcut, placed red wordmark at open + SWIM lockup at close.
- **Synthesis agent (opus):** merged all three into a deterministic BUILD_SPEC; honestly DROPPED 7 of 14 beats (thirst / no-such-moment / false-wipe / second-model identity blocker), leaving 7 segments ~15.5s; flagged that even at every agent's fullest window the keep-set totals only ~17.5s.
- **Build agent (sonnet):** ran ffmpeg, produced V5. Mechanically clean: correct Canon transpose=2, per-clip grade before LUT, brand-layer alpha fade on first path, one honest red-fabric whip kept at seg5.
- **5 Adversarial-verify skeptics (opus, parallel):** identity/grade/craft/truth/slop, each whole-watched V5 + measured numerically. All 5 refuted client-ready.
- **Verdict agent (opus):** synthesized -> blocked / 3 / no-send.

### 5. Conflicts and resolution
- **Brand vs Moment on the hero:** brand nominated IMG_9533 as the strongest face hold; moment agent measured IMG_9533 has a 42-unit within-shot B-R swing + a lip-gloss gesture that breaks the deadpan hold. RESOLVED by synthesis in favor of D94A3316 (idx11) as hero: cleaner sustained eye contact, body 0.15 vs 0.42, no grade-drift risk. IMG_9533 dropped.
- **"Walk-in" beat:** idx2 dropped (false wipe + thirst); the walk/entrance read reassigned to the car-exit movement beat (idx3 D94A3320, corrected window 7.6s) + the real red whip (idx7).
- **Orchestrator vs Verdict (I overrule part of the score):** 2 of 5 skeptics labeled real-camera motion blur and the intentional red-fabric whip as "AI generative melt / anatomy morph / identity drift." That is FALSE on real footage (confirmed by eye: one model, no morph; the red frame at ~9s is the one honest in-camera wipe). The "B-R swing ~76-120" they measured is a measurement artifact on a frame deliberately filled with red garment, not a grade failure on held shots. Those blockers are struck. The grade-lock fix actually LANDED on held shots (-3..+3).

### 6. Final V5 export
`ALMA_REEL_INHOUSE_V5_MOMENT_CUT.mp4` (1080x1920, 30fps, 13.83s, 26.6MB) + `_web.mp4`. Exists, plays, clean encode.

### 7. Watch pass
All 5 verify agents whole-watched (>=2-3fps full coverage). Orchestrator also eyeballed a 14-frame contact sheet: real footage, one model, grade consistent across held shots, hero clean, brand layer present, the cut is genuinely thirst-forward (full-body bikini by convertible in the large majority of frames).

### 8. Adversarial-verify result
5/5 refuted. Raw verdict: blocked / 3 / no-send.

### 9. Rating + why (orchestrator's corrected call)
- **~4.5/10 as a cut** (correcting the two hallucinated AI-melt blockers; raw panel said 3). Mechanically clean, grade landed on held shots, one honest wipe, real hero. Capped by the real failures below.
- The deeper, more important finding is NOT about the cut. It is about the MATERIAL.

### What CHANGED because the OS activated (the real win)
The harness PROVED, with measured per-clip evidence from independent fresh-context agents, that **these 62 clips are a bikini-by-the-convertible shoot, not expensive-deadpan material.** After honestly removing every thirst / no-such-moment / false-wipe / second-model beat, only ~14-17s of keepable material remains, and even that leans body-forward. The OS did not produce an oversold cut and call it done; it surfaced the true ceiling of the footage. That is the answer to the weeks-long loop: not "the editor is bad" but "the promised deliverable cannot be honestly cut from this material."

### Gates passed / failed
- PASS: pipeline ran end to end with real role separation; no self-crowning; Canon orientation correct; grade lock landed on held shots (-3..+3); one honest in-camera wipe; identity holds in the BUILT cut (two-model beats dropped); no actual morph/melt.
- FAIL (real): (1) DURATION 13.83s, not 30s - because honest selection leaves only ~14-17s of usable material. (2) NO AUDIO - Suno owned-music still not connected. (3) THIRST-FORWARD - body framing is the majority of shots; expensive-deadpan needs material that mostly is not in these 62 clips. (4) Brand layer rendered but small/low-contrast over body content; needs a cleaner card treatment.
- FALSE-FAIL struck by orchestrator: "AI generative melt / anatomy morph / identity drift" - mis-applied AI-slop lens to real camera footage.

### What blocks 10/10
The footage ceiling. To make a true 30s expensive-deadpan Alma reel you need MORE non-body, face/attitude, deadpan-hold material than exists in these 62 clips, plus owned music (Suno). Within the current material the honest maximum is a ~12-15s deadpan micro-cut.

### 10. VERDICT
**no-send / draft.** V5 is not client-ready and not the 30s deliverable. The decision is NOT "iterate the cut again" - it is a material decision (below). The harness and quality loop are proven: independent agents diagnosed the same material problem with numbers, and the verify phase refused to crown weak work (even over-refused, which I corrected). Send to client/social = NO.

## Decision required from operator
1. **Accept the honest micro-cut:** lock a ~12-15s deadpan reel from the 7 clean beats (hero D94A3316 + car-exit + real red whip + departure), add Suno music, ship as a short. Drops the "30s" promise.
2. **Get more material:** a small re-shoot or pull of face/attitude/deadpan, body-under-30% footage, then re-run `alma-v5`.
3. **Wait for the human editor cut** and hybridize the best of both, then re-run the harness on the hybrid.

Plus the standing blocker: **Suno (owned music) is not connected** - no client reel ships silent.

## Harness defects found this run (to fix before next serious run)
1. **Adversarial-verify over-triggers AI-slop on real footage.** The identity + slop axes assumed generative content and called motion blur / a real red-fabric whip "AI melt / anatomy morph." Fix applied: the verify axes now state the source is REAL CAMERA FOOTAGE and must distinguish in-camera motion blur / intentional transitions from generative melt; measure grade on HELD frames, exclude frames dominated by a single in-frame colored object (transitions).
2. **Grade measurement on transition frames is meaningless.** B-R on a frame that is ~all red garment is not a grade fault. The grade axis now excludes transition frames from the spread test.
