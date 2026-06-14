# Synergy "The Door" V11 (elevated rebuild) - Prompt / Keyframe / Motion Manifest

Governing standard: OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md
Method: authored START->END keyframes -> Kling 3.0 i2v (start->end) -> batch-and-cull -> per-beat adversarial verify. Stills locked before motion. Diegetic sound per beat. One motivated move per shot. Cut on action.

## Identity refs (locked)
- Eleanor: abbf70ab-10b1-4b8e-a983-58c12995191c
- Daughter: 466d64da-2eac-45d5-b263-41506f3002e1
- Caregiver: 7f6adffc-e4e8-48e2-805f-3092213b84e1
- House/door: door4 keyframe (kf_v11/door4.png)

## Style prefix (every keyframe prompt)
"Anti-gloss documentary realism, natural light only, warm domestic tones, shallow depth of field, photoreal natural skin texture, fine film grain, subtle atmospheric haze, no plastic sheen, no text, vertical 9:16."

## Beats (filled during build)
| beat | source | START kf | END kf | motion (gen id) | take kept | beat score | verify run |
|---|---|---|---|---|---|---|---|
| (pending locked plan) | | | | | | | |

## Banked at/near bar (pre-rebuild)
- daughter_2am_decision: START dau_s2 (d57cbd0c) -> END dau_e1 (7a2d40b9) -> ev_dau2 (kept) -> graded EL_dau
- eleanor_recognition_HERO: START ele_s2 (84437b38) -> END ele_e1 (87e76245) -> ev_ele2 (kept) -> graded EL_ele
- caregiver_touch: START 23606bb8 -> motion touch_take2
- warm_door: START door4 (9a6f40c6) -> motion door_take1/2
- end card: title_v5.png (verified contact)

## LOCKED PLAN (from synergy-rebuild-plan-verify wf_c726c462-dc2)
Throughline: A worn-down daughter who fears she's failing her mother lets help through the door, and the first breath she takes in months is the proof that asking was the brave thing.
Final order: daughter_2am_decision -> warm_door -> caregiver_touch -> eleanor_recognition_HERO -> daughter_can_breathe. ~23s.

VO (ElevenLabs, sparse, second person):
1. For months, you carried it alone.
2. Two in the morning, asking if you're failing her.
3. You're not. You just can't do it by yourself.
4. So someone kind walks in.
5. Synergy HomeCare. Now you can breathe.

Beat verdicts (fresh-context hostile, no self-crown):
- eleanor_recognition_HERO: 9.0 KEEP (ev_ele2 -> EL_ele). minor chair/cardigan warp, not disqualifying.
- daughter_2am_decision: 6.5 REGEN (read as falling asleep). Fix: END = awake, eyes-open steadied RESOLVE, mouth closed.
- warm_door: 5.5 REGEN (near-still drift, no swing/arrival). Fix: START near-closed -> END swung open + light bloom + silhouette/hand arrival.
- caregiver_touch: 8.3 (rule-forced regen; operator-kept PROVISIONAL pending full-film verify). Fix if regen: more Eleanor response + clean secondary arm.
- daughter_can_breathe: NEW. START tense daytime (face-lock to 2am) -> END shoulders drop, relief (not smile).

Music: standing gap (Suno not connected). Build with licensed Adobe Stock piano (511566838) as bed; flag owned-music as open. Mix order: VO -9/-12, music ducked (-8/-6, crescendo -2 only on recognition), SFX third. J/L cuts.

Keyframe gen round 1 (pending QA):
- daughter_2am END: ac861811, 69bfba82, 141b140f (ref dau_s2 d57cbd0c)
- warm_door START: 90837a15, 32931a95, f46bf235 (ref door4 9a6f40c6)
- daughter_breathe START: b6f5bca9, dbe8e57f, 7d8f2e33 (ref daughter 466d64da)

## Round-1 keyframe pairs LOCKED + motion firing
- daughter_2am_decision: START d57cbd0c (dau_s2) -> END 69bfba82 (d2am_e2, eyes-open resolve). Motion takes: a5bdf389, b51f0cdb
- warm_door: START 32931a95 (door_s2, near-closed) -> END 52cdecce (door_e3, swung open + silhouette arrival). Motion takes: 7abaea74, f8511c21
- daughter_can_breathe: START 7d8f2e33 (bre_s2) -> END b83589d0 (bre_e1, relief). Motion takes: 23db765b, 619342f9
- KEPT (no regen): eleanor_recognition_HERO = ev_ele2 (9.0). caregiver_touch = touch_take2 (8.3 provisional).
Next: cull motion (endpoint-diff + slop + identity), re-roll any fail, per-beat adversarial verify, then sound+grade+assemble+full verify+deliverables.
