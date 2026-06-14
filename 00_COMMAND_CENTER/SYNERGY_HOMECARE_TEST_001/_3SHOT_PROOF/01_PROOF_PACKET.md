# Synergy "The Door" · 3-Shot Competence Proof · Proof Packet

**Question:** are we competent to make Synergy as a REAL AI film now (not stills panning)?
**Method:** generate the 3 beats The Door v2 FAILED (performance done as frozen stills), then judge with a fresh-context adversarial harness, not self-scoring.

## What was generated (v1)
Kling 3.0 pro i2v, 9:16, silent, from locked start stills. ~32 credits.
- SHOT1 daughter 2am (scene-opening action) - start `SB_V02_daughter_awake.png`
- SHOT2 Eleanor recognition (emotional performance / hero) - start `SB_V07_song_recognition.png`
- SHOT3 together turn (transition / resolution) - start `SB_V11_together.png`

## Verify harness (no self-crowning)
`synergy-3shot-verify` workflow (run `wf_d3ef5572-148`), 16 fresh-context agents, 4 axes per shot (cinema-vs-animatic / identity+slop / performance-truth / client-safe), whole-watch every frame, then per-shot + competence synthesis.

## Scores (adversarial)
| shot | type | verdict | score | cinema? |
|---|---|---|---|---|
| 1 daughter 2am | scene-opening action | cinema-pass | 8.0 | yes |
| 2 Eleanor recognition | emotional performance (hero) | **animatic-fail** | **3.0** | **no** |
| 3 together turn | transition / resolution | cinema-pass | 7.5 | yes |
| | | **avg** | **6.17** | 2 of 3 |

## What this PROVES (the real signal)
- **Identity-lock is solved.** All three shots held identity across every frame (Eleanor's freckle cluster + nose-bridge spots stable fr_001-028; two distinct people in shot 3 never merged or swapped). os-face-lock via Kling 3.0 i2v from a locked still WORKS.
- **Anti-slop is solved.** No face morph/melt, no waxy skin, no teeth/eye artifacts, no melting/merging hands across all three. Real aged documentary skin. The thing that usually kills AI film is handled.
- **Real cinema is achievable.** Shots 1 and 3 clear the Push-In Law with genuine subject-carried change (shot 1: phone raised->lowered, gaze open->down->closed, irreversible subject actions; shot 3: a real almost-smile blooms + the caregiver's hand travels in and clasps).
- **On-brief tone holds.** Anti-gloss, documentary, lived-in, client-safe, zero corporate-healthcare sheen on all three.

## What FAILED (honest)
- **Shot 2, the hero, is an animatic-fail (3/10).** fr_001 and fr_028 are emotionally identical (same blank, distant, window-ward gaze, neutral mouth); the ONLY change across 28 frames is the camera tightening. This is the exact still + push-in the proof existed to retire. It is NOT slop (identity + skin are clean) - it is performance-absence: the subtle prose prompt let the lens do the work.
- **Shot 3 skipped its titular action.** Eleanor faces the caregiver from frame one; the scripted "turn from the window" never happens. It still passes as cinema (the smile + hand-settle are real), but the named action was not staged, which caps it at 7.5.
- **Shot 1 read as fatigue, not decision.** The "decides not to call" plays as sleepless surrender; close but the decision is not a legible action on the hand/face.

## Honest verdict
**competent = FALSE (for now). overall_call = regenerate-specific-shots. NOT cleared to build the full film.**
We proved we CAN make real, slop-free, identity-stable AI cinema (2 of 3), but the single hardest beat (the hero recognition) fell back into a push-in. Per the hard law, no full film until the 3-shot proof passes. Next: fix the production METHOD, regenerate Shot 2 (and re-head Shot 3's turn), re-verify, then greenlight.

## Method fixes (the diagnosis, before scaling)
1. **Lock END keyframes, not just start frames.** Author the final expression (smile bloomed, eyes welled, head turned) and drive i2v start->end so the model is FORCED to perform an arc. (This is the core fix; being applied to Shot 2 now.)
2. **Performance verbs are a hard prompt requirement on every character clip** (eyes focus, eyes well, breath parts lips, 3-5 degree head turn, single-corner almost-smile). Reject any clip whose first and last frames are emotionally identical.
3. **Push-in is support-only.** Add a Push-In Law gate to the QA harness that diffs fr_first vs fr_last for subject delta (gaze/mouth/head/hands) and auto-fails clips whose only delta is framing.
4. **Stage the named action.** If the beat is "turn from the window" or "decides not to call," the subject must START pre-action and PERFORM it on camera. Block over-shoulder/over-window framing that hides the action.
5. **Budget 2-3 takes per emotional beat and select the strongest performed arc** instead of crowning a first take.
6. **Keep Kling 3.0 i2v as the engine** (identity + anti-gloss skin held clean) and run every beat through adversarial-verify / Gemini on the FRAMES, endpoint-diff first, before any scale-up.

## UPDATE: Shot 2 v2 (method fix applied + re-verified)
Applied the prescribed fix to the hero: authored an identity-consistent END keyframe (nano_banana_pro, recognition bloomed, freckles/cardigan/room confirmed consistent) and regenerated Shot 2 as a FORCED start->end arc (Kling 3.0 i2v start_image+end_image) with performance verbs and the camera held. Re-verified by a fresh-context harness (`synergy-shot2-reverify`, run `wf_8d43b463-013`), endpoint-diff test first.

Result: **cinema-pass, 7.5/10 (was 3.0 animatic-fail). +4.5.** Endpoint-diff PASSES: fr_001 (slack, distant, head away) vs fr_028 (head turned to camera, eyes present/welling, faint single-corner near-smile); peak at fr_015-020 = lips part into a soft "oh" of recognition, sustained across frames (not a one-frame flicker); framing actually loosens at the tail, so the change cannot be attributed to a push-in. Identity 9, no slop, no teeth-melt in the open-mouth frames. **method_fix_works = TRUE.**

### Revised scoreboard (proof PASSES at the cinema bar)
| shot | verdict | score |
|---|---|---|
| 1 daughter 2am | cinema-pass | 8.0 |
| 2 Eleanor recognition (v2) | cinema-pass | 7.5 |
| 3 together turn | cinema-pass | 7.5 |
| | **avg** | **~7.7, 3 of 3 cinema** |

### Competence verdict (the answer to the question)
**YES, we are competent to make Synergy as a real AI film.** All three of the exact beats The Door failed now read as real, subject-performed cinema, identity-locked and slop-free, at a client-safe documentary tone. And the METHOD that makes performance shots reliable is now proven and repeatable (below).

This is competence (cinema, not stills) = PASSED. It is not yet the 9/10 client-ready FINISH per beat (current ~7.5-8); that is a polish + finishing matter, not a competence question. overall_call = **proceed-to-full-film** using the locked method, with the per-beat 9-floor polish + music baked in.

### The proven method (THE reusable win)
For any character PERFORMANCE beat: (1) lock a START still (face-lock), (2) author an END keyframe in the target expression/pose from that still, (3) i2v start->end on Kling 3.0 pro with explicit performance VERBS and "camera held / no push-in," (4) gate with adversarial frame-verify whose FIRST test is the endpoint-diff (fr_first vs fr_last subject delta; auto-fail if only framing changed), (5) budget 2-3 takes and select the strongest arc. A single start-still + prose prompt lets the lens default to a push-in; the END keyframe forces the arc.

## EXCELLENCE PASS (Option 2) RESULT: BLOCKED, do not scale

Goal was to take the 3 shots from cinema-pass to the 9 floor (all >=8.5, hero >=9). It did NOT pass. Honest finding: my first polish pass REGRESSED the set, and the hero ceilings below 9.

### Full scoreboard (every version, adversarially scored)
| shot | v1 | v2 | v3 (polish) | v4 (corrected) | best |
|---|---|---|---|---|---|
| 1 daughter decision | 8.0 | - | 6.8 | - | **v1 8.0** |
| 2 Eleanor hero | 3.0 | 7.5 | 7.3 | 6.5 | **v2 7.5** |
| 3 together turn | 7.5 | - | 3.5 | - | **v1 7.5** |
| best-of avg | | | | | **~7.67** |

Pass condition (all >=8.5, hero >=9): NOT met in any version. Hero never cleared ~7.5 across FOUR attempts.

### Why the polish v3 regressed (my three errors, measured)
1. **Shot 1 (8.0 -> 6.8):** I authored an END keyframe with EYES CLOSED. On video that reads as FALLING ASLEEP, not a conscious decision/acceptance. The phone also flipped face-on mid-clip = object/hand/mouth morph slop at the emotional center. Eyes-closed is the wrong target for a conscious beat.
2. **Shot 2 hero (7.5 -> 7.3 -> 6.5):** a single FULL-PEAK end keyframe + a LONGER (8s) clip back-loaded the arc (Kling holds the start, snaps near the end). v4 shortened to 5s which fixed back-loading but FLATTENED the arc (blank -> faint near-smile only), and the welling never rendered (the "wet eyes" in the keyframe read as ordinary window specular, not a tear film, and would not survive i2v regardless).
3. **Shot 3 (7.5 -> 3.5):** nano_banana_pro would NOT break Eleanor from the reference's forward pose, so the START frame never actually showed her looking out the window. With no window-gaze to turn FROM, the turn was impossible and Kling defaulted to a 100% push-in. Confirmed exactly the risk I flagged before animating.

### The hero ceiling (the real blocker)
A restrained AI recognition beat WITH VISIBLE WELLING/TEARS tops out ~7.5 with the nano-keyframe + Kling-i2v method as executed, because: (a) text-prompted keyframes do not produce a convincing wet lower-lid + lacrimal catch-light distinct from ambient window specular; (b) Kling defaults to a small softening + push rather than a large felt delta. Identity-lock and anti-slop stayed clean throughout (that engine is solid); the gap is performance intensity + the tear detail.

### Named path to maybe crack 9 (uncertain, more spend) - for operator decision
1. **Hand-EDIT an end reference** with actual wet lower lids + a separate tear catch-light (not text-generated), lower the practical window key so a lid-rim tear film catches light, and animate welling as a VERB ("lids glisten and fill over the last 1.5s, one blink to spread").
2. **Key a subject-performed 4-beat micro-arc** (blank -> registers/turns off window -> brow-lift + welling onset -> faint almost-smile + small head turn), push-in reduced so the face leads.
3. **Or pivot the hero beat** to something AI performs more reliably (the hand-squeeze, a mouthed lyric) instead of micro-welling.

### Creative reframe worth a decision
The brief asks for RESTRAINT ("makes a room go quiet"), NOT melodrama. The client_safe axis scored the restrained hero 8.7. The 9-gate is currently held on VISIBLE TEARS, which may be over-spec for this brief. Real question for the operator: is the 9-floor "visible welling tears" or "a room goes quiet"? If the latter, a restrained present hero (~8.7 client-safe) may be the correct read and the tear-detail is a rubric artifact, not a real miss.

### Verdict
**STILL BLOCKED. Do not greenlight. Do not scale.** Best-of set is ~7.67 (8.0 / 7.5 / 7.5), below the 8.5/9 floor. The hero is the binding constraint. Next step is an operator decision (hand-edited tear frame vs hero-beat pivot vs accept restrained read), not another blind reroll. Credits protected: stopped at ~65 remaining rather than guess-burning.

## Standing gaps (before any client send)
- Owned music (Suno) not connected. No client send ships silent.
- Diegetic sound design (room tone, needle drop, breath) is a finishing pass, not yet on these silent proofs.
- Per-beat lift to the 9 floor: hold the recognition peak 2-3 frames longer + more ocular bloom (shot 2); stage the literal turn-from-window (shot 3); add a legible decision micro-beat (shot 1). All are polish, not method failures.
