# Synergy "The Door" · Overnight Film Build · Production Plan + Backlog

**Mandate:** overnight autonomous build (all approved). Wake up to the strongest possible send-ready short. Resources: Higgsfield ~350-560 cr (expert: Kling 3.0 pro), Adobe ~1000 cr (Stock music licensing + grade), ElevenLabs free (TTS VO + SFX). nano_banana_pro unlimited for keyframes.
**Send-ready is POSSIBLE tonight:** music gap SOLVED via Adobe Stock licensed audio (Thinking of You, 511566838, 2:45 piano, in `_FILM_BUILD/music/`).
**Standard:** real, anti-gloss documentary, restrained, "makes a room go quiet." 9:16 master + 16:9 YouTube. No slop, no identity drift, no stock-healthcare sheen. Every beat hostile-verified, best-of (not latest). No self-crowning.

## Method (locked, proven)
Per beat: brute-force nano keyframes (START + authored END, derive-END-from-START for continuity/two-shots) -> QA by eye (identity+slop) -> Kling 3.0 pro i2v start->end with verb-first performance prompt + camera-held -> whole-watch + endpoint-diff -> hostile verify -> best-of. Keyframe-first; minimal video rerolls.

## Beat list (~42s target, 9:16)
| # | beat | ~sec | source/plan | state |
|---|---|---|---|---|
| 1 | phone LIGHTS 2am (insert) | 2.5 | generate insert (screen wakes, hand edge) | TODO |
| 2 | DAUGHTER decision (recast younger) | 4 | START DAU_start_58 -> END fc3770d4 (deriving) | KEYFRAMES NEARLY READY |
| 3 | carry: pills + night drive | 4 | 2 generated inserts | TODO |
| 4 | DOOR opens / caregiver arrives (HINGE) | 3 | generate (dark->light, steps in) | TODO |
| 5 | bag down / settles | 2.5 | generate | TODO |
| 6 | coffee + record needle | 3 | generate insert | TODO |
| 7 | ELEANOR recognition (HERO) | 5 | best-of: v5 (real arc) vs reroll 78572f16 (mouth-closed) | VERIFY PENDING |
| 8 | HANDS / connection (touch-led) | 4 | together best-of OR tight hand insert | IN PROGRESS |
| 9 | coast / place breath | 2.5 | generate (Cape Fear water/marsh) | TODO |
| 10 | DAUGHTER exhale payoff | 4 | generate (younger daughter, daylight, shoulders drop) | TODO |
| 11 | together button | 3 | best-of together | IN PROGRESS |
| 12 | TITLE card | 2.5 | graphic: "Synergy HomeCare of Cape Fear / Let us carry it with you" | TODO |

## Sound
- VO: ElevenLabs TTS, warm woman ~45-55, second person, ~70 words (script in 02_WINNER_SCRIPT). Sparse.
- Music: Adobe Stock "Thinking of You" piano (licensed) under the whole cut, ducked under VO.
- SFX: ElevenLabs text_to_sound_effects (phone buzz, door, footsteps, bag, coffee pour, needle drop, room tone).

## Asset registry
- Refs (uploaded media_ids): Eleanor SB_V07=abbf70ab; caregiver two-shot SB_V11=cc4fbdd6; daughter REF_03=466d64da.
- Eleanor recognition END keyframe (scored 9): ELE_smile_1 = gen 2b44e218.
- Daughter recast START: DAU_start_58 = gen 58c9a4da; END deriving = fc3770d4.
- Together start: 811e4643; ENDs: 7d65a940 (gentle), 27cf61ac/df5a1abc (turn attempts).
- Music: _FILM_BUILD/music/Thinking_of_You_511566838.wav (165s).

## Overnight loop
generate beat keyframes (parallel) -> animate -> whole-watch -> verify -> mark best-of in this table -> next beat. When all beats >=8 and hero >=8.5: assemble (ffmpeg) -> VO+SFX+music -> hostile verify full cut -> 9:16 + 16:9 export -> proof packet -> morning verdict (honest score, no pre-crown).

## Honest gate
Do NOT crown 10/10. Morning deliverable = the built film + its real verified score + send/no-send. If a beat can't clear 8 by morning, cut it (tighter cut > weak beat).

---
## BUILD STATUS (live, 2026-06-09 ~05:35) - bridges GREEN (Premiere+AE+Figma+Adobe+EL+HF)
ANIMATED (videos, need download+verify):
- hero Eleanor: v5 (d310f4f7, real arc) + mouth-closed reroll (78572f16) -> best-of
- daughter recast decision: 30912c7f (START 58c9a4da -> END fc3770d4) [rendering]
- together v2: 16ed7885 (prior); turn attempts pending
KEYFRAMES rendering (collect via show_generations):
- daughter exhale payoff: 9eac4799, fb969ecf, bcb6866c (ref 466d64da)
- phone 2am insert: 12a75982, 4a3458b3
- coffee+record insert: 697f0bc5, 4845a621
- coast breath: 239e56b5, 40840c1f
- door START (dim, light edging): 023d383b, 966f5a81 (house 0455c326)
- door END (caregiver enters, light floods): 563e9ebe, 0fb06d77 (caregiver 7f6adffc)
UPLOADED REFS: Eleanor SB_V07=abbf70ab, REF_01=29ab70a4; caregiver SB_V11=cc4fbdd6, REF_02=7f6adffc; daughter REF_03=466d64da; house REF_04=0455c326.
TODO: bag-down beat; pills/drive carry inserts; title card (AE); animate door/coffee/coast/exhale; pick together connection; ASSEMBLE in Premiere; AE titles+grade; VO (EL TTS); SFX; music bed (Thinking_of_You.wav); hostile verify full cut; 9:16+16:9 export; Figma review board; proof packet + honest score.
NEXT ACTION on wake: show_generations -> download new keyframes -> QA by eye -> animate beats (Kling pro) -> continue.

## BUILD STATUS update ~05:40 - connective beats ANIMATING (Kling pro)
- phone insert: 33843c29 | door/hinge: 64c659e2 | coffee: 8d72c215 | coast: 809c6391 | daughter exhale: fa6cef2f
- daughter decision: 30912c7f | hero: d310f4f7(v5)+78572f16(mouth-closed) | together: 16ed7885 + matched pair 811e4643->7d65a940
- chosen keyframes saved in _FILM_BUILD/shots/kf/
NEXT: download all videos -> frames -> whole-watch -> hostile verify full set -> best-of -> Premiere assemble -> AE title -> VO+SFX+music -> 9:16+16:9 -> Figma board -> proof packet + honest score.

## BUILD STATUS ~06:20 - v5 (connection beat CUT)
- v3 master: BLOCKED/5 (title typo, Eleanor drift, coffee text, grade jump, no manifest) -> all fixed.
- v4 master: BLOCKED/5.5 - NEW never-relax fails were in the regenerated CONNECTION beat only (caregiver identity mismatch vs door + climax hand-melt).
- DECISION: cut the connection beat (a tighter clean cut beats a slop beat; removes both never-relax fails at once). v5 = phone, daughter, door, coffee(clean), hero(longest+warm), coast, title. 25.8s, -17.6 LUFS.
- v5 hostile verify: wf_4ccdf1c4-98b (in progress) -> record honest score + send/no-send.
