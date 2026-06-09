# REAL_FILM_PRODUCTION_OS (LOCKED 2026-06-08)

**The translation layer: RESOURCE → RULE → SHOT DECISION → TOOL EXECUTION → QA.**

Status: STANDING DOCTRINE for all AI film/commercial/brand-story/visual production. Built because v1/v2 of "The Door" were an **animatic** (stills + push-ins) dressed as a film. The resources were used as background, not compiled into production decisions. This document is the compiler. It sits ABOVE `OS_AI_CINEMA_PRODUCTION_DOCTRINE.md` (the loop), `OS_HIGGSFIELD_PRODUCTION_DOCTRINE.md` (the tool stack), `cinema-worldbuilder` + `banana-pro-director` (the grammar skills).

Sources compiled: cinema-worldbuilder SKILL.md (5-mode cinematography grammar), banana-pro-director SKILL.md (character/asset discipline), HIGGSFIELD OG written guide (the lock is the look, stack roles), Scene_Sequence_Prompts (coverage methods), and the documented failure of The Door v1/v2.

---

# THE CORE DISTINCTION (read first)
A **film shot** shows a SUBJECT performing an ACTION that CHANGES across the shot's duration. A **photograph** shows a state. Animating a photograph with a push/zoom/pan/parallax does not make it a film shot. It makes it a moving photograph.
- Cinema = change driven by the SUBJECT (a face that shifts, a hand that reaches, a body that turns, a door that opens).
- Animatic = change driven only by the CAMERA over a static subject.
The standard is not "beautiful." The standard is **cinematic**. If it feels like stills in a timeline, it fails.

---

# TASK 1 — OPERATING LAWS (resource → rule)
Each law is phrased as a decision rule, with its source. These are not summaries; they fire during production.

## Story structure
- **S1. But/Therefore, never And-Then.** Every beat connects to the next by tension or consequence. If two beats are joined by "and then," cut one. (STORY_GATE; storytelling layer.)
- **S2. Open the loop in the first 3 seconds, close it at the end.** Name the question the viewer is asking by 0:03; pay it off at the button. (story_open_loop_hook.)
- **S3. One emotional target per film, named before writing.** Write the single feeling in one sentence; every shot serves it or dies. (story_emotional_target.)
- **S4. Withhold, then reveal.** Relief, recognition, payoff are earned by delay, not handed out early. (psy_withhold_reveal.)

## Scene construction
- **SC1. A scene is a unit of change, not a location.** A scene exists to move one value from state A to state B (alone → accompanied, dread → relief). If nothing changes, it is set dressing, not a scene.
- **SC2. Pick the cinema MODE per scene before any shot** (M1 Narrative / M2 Studio / M3 Action / M4 Performance / M5 Atmospheric). Mode locks body/lens/movement/grade. (cinema-worldbuilder mode-select.)
- **SC3. Energy over position.** Build a scene from what bodies and forces are DOING, not where they sit. Physics over geometry. (cinema-worldbuilder Universal Rule 12.)

## Blocking (who moves where, and why)
- **B1. Every figure in frame has an intention and a physical action expressing it.** No one stands to be looked at. If a character is only "present," give them a verb or cut them.
- **B2. Blocking changes the frame.** A character enters, crosses, reaches, sits, leaves. Movement of the subject through space is the primary motion; camera is secondary.
- **B3. Stage for the lens.** Wide (32-40mm) for full-body blocking and entrances; medium (50-55mm) for two-person exchange; tight (75mm) for the single beat; 85-100mm for the detail. (cinema-worldbuilder lens guide.)

## Camera movement
- **CM1. The camera moves for a reason the SUBJECT gives it.** Motivated moves only: follow an action, reveal on a turn, settle on a stillness. An unmotivated push/zoom is amateur. (Commercial Craft V2 "motivated only"; edit_motivated_only.)
- **CM2. Mode dictates movement.** M1 handheld with breath + occasional slow dolly; M3/M4 shaky throughout, no stabilized shots; M2 locked + optional 4-6" push; M5 locked or extremely slow drift. Do not freehand camera language. (cinema-worldbuilder per-mode specs.)
- **CM3. A push-in is a seasoning, not a meal.** It can intensify a subject already acting. It cannot BE the action. (See the Push-In Law, Task 7.)

## Subject performance
- **P1. Performance is motion.** The subject must DO something observable: an expression shift, a breath, eyes welling, a hand tightening, a step. A held neutral face for 6 seconds is a portrait, not a performance. (The Door failure; banana "the character is the character.")
- **P2. One performance verb per shot, minimum.** Name it before generating (turns, reaches, exhales, freezes, remembers). If you can't name the verb, the shot has no performance.
- **P3. Micro over macro for emotional beats.** Recognition, relief, grief read in the eyes and mouth corners over 2-4 seconds. Generate FOR that change; QA that the change is visible start-to-end.

## Shot coverage
- **CV1. Cover every key moment in at least 3 sizes** (wide/medium/tight) so the edit has options and the eye gets variety. (Scene_Sequence 3x3 contact-sheet method.)
- **CV2. The hero beat gets its own clean isolation** (the longest, tightest, most-motivated hold). One genuinely strong angle per scene. (Commercial Craft V2 "one aggressive hero angle.")
- **CV3. Build coverage cheaply first.** Use the 3x3 cinematic contact sheet (9 angles of a locked subject in one generation) and the 9-scene sequence to plan coverage BEFORE spending video credits. (HIGGSFIELD_REUSABLE_MEGA_PROMPTS.)

## Shot-to-shot continuity
- **C1. The lock is the look.** Identity (face/bone/body/skin/hair) is locked via a canonical reference sheet; outfit/hair/makeup swap freely. Same person every shot or the shot is killed. (banana-pro-director; HIGGSFIELD guide; os-face-lock.)
- **C2. One grade, one light logic, one world.** Every shot shares color, contrast, grain, and light direction so it reads as one film, not a prompt collage.
- **C3. Cut on motion / match on action.** Continuity of movement across a cut hides the seam and carries energy. (cinema-worldbuilder cut triggers: hard cut, smash cut, match cut.)
- **C4. Screen direction and eyelines hold** across a scene (entering from the same side, looking the consistent way).

## Editing rhythm
- **E1. Classify the format, then apply its ASL band.** Emotional brand film = motivated holds, hero is the longest hold, contrast >= 2.2x against the fastest beat. Speed is never the goal. (Commercial Craft Benchmark V2.)
- **E2. Jagged edge, not monotone.** Vary shot lengths; a uniform ASL reads amateur. (story_rhythm_variety.)
- **E3. Every cut is motivated** by a line, a sound, an action, or a reveal. No dissolves to fill time. (edit_motivated_only.)
- **E4. The hero hold is the longest; the montage beats are the shortest.** Pacing contrast IS the craft signal.

## Sound design
- **SD1. Diegetic first: every action has its sound.** Door latch, bag set down, coffee pour, needle drop, breath, fabric, room tone. Build the sound from the action in frame. (cinema-worldbuilder diegetic audio rule.)
- **SD2. Music is owned and separate.** Never put music in a generation prompt (Seedance/Kling audio is diegetic). Final emotional score is owned (Suno or equivalent); scratch swells are placeholder only. (AI cinema doctrine point 7.)
- **SD3. The film must work MUTED.** Hook and payoff read with sound off (captions + image). If it only works with VO, the picture is failing. (vertical-native rule; The Door QA.)

## AI video generation prompting
- **AV1. Prompt ACTION across the duration, not a description of a picture.** The Dynamic Description states every action/gesture/camera move/focus rack over time; the Static Description holds what does not change. (cinema-worldbuilder output format.)
- **AV2. No names, no brands, no meta-commentary, no medium references, no music** in the prompt. Pure visible-thing description. (cinema-worldbuilder Universal Rules 6-11.)
- **AV3. State runtime explicitly; label per-shot timing inline** for multi-cut. (cinema-worldbuilder runtime rules.)
- **AV4. Route prompts through the skills, do not freehand.** Image work → banana-pro-director; motion → cinema-worldbuilder (pick the mode). (Higgsfield doctrine.)
- **AV5. If a content filter false-flags a shot, reword neutrally or switch engine** (Seedance ↔ Kling 3.0). Do not fall back to a still. (The Door Eleanor case.)

## Image-to-video vs text-to-video (the decision the OS kept getting wrong)
- **IV1. Image-to-video (keyframe) when identity/world must stay locked** to an approved still (recurring character, established set). Start-frame = the locked still; prompt the action that follows. This is the default for character continuity.
- **IV2. Text-to-video when there is no locked subject** (an abstract insert, a weather plate, a generic environment) and identity continuity does not matter.
- **IV3. Image-to-video does NOT mean "animate a portrait."** The start frame is a STARTING point for an action, not the whole shot held still. If the subject does not change from start frame to end, you used i2v wrong.
- **IV4. Keyframe (start+end image) when you need a specific change** between two known states (closed eyes → open; door shut → open). Kling supports start_image + end_image.
- **IV5. Transitional insert / memory beat** can be a designed still or a soft move, but it must be LABELED as such and must not carry a scene's action or climax. (Push-In Law.)

## When a still push-in is allowed → see Task 7 (the law).

## When a shot FAILS as cinema (kill criteria)
A shot fails and must be killed or regenerated if ANY is true:
- **F1.** The only motion is camera (push/zoom/pan/fake parallax) over a static subject, on a non-insert beat.
- **F2.** The subject does nothing: no expression change, no gesture, no movement start-to-end.
- **F3.** It does not read muted (needs VO to mean anything).
- **F4.** It does not advance the story (removing it changes nothing).
- **F5.** Identity drifts, grade mismatches, or it reads as a different world.
- **F6.** It is AI-uncanny (plastic skin, melted hands, wrong physics) or stock-gloss.
- **F7.** You cannot answer "why does the camera move?" and "why do we cut here?"

---

# TASK 2 — THE PRODUCTION GRAMMAR (every film runs all 14 stages, in order)
No stage may be skipped. No heavy video credits spend before Stage 7 is approved.

1. **Client brief interpretation** — what they actually want under the words; the register; the failure modes to avoid. Output: brief read.
2. **Story intention** — the single sentence: what this film makes the viewer believe/feel/do.
3. **Emotional arc** — the value journey (state A → state B) with the turn. But/therefore mapped.
4. **Action-only script** — the film written as VERBS (Task 4 method). No camera, no VO yet. Just what happens.
5. **Scene beats** — group actions into scenes (units of change); assign the cinema MODE to each.
6. **Shot coverage map** — for each beat: sizes needed, the hero angle, screen direction. Use the 3x3 contact-sheet / 9-scene methods to plan cheaply.
7. **Moving-shot generation plan** — for each shot, the performance verb + camera move + duration. **GATE: operator sign-off here before spending.**
8. **Tool choice per shot** — t2v / i2v-keyframe / start+end keyframe / transitional insert / practical (Task 5 method). Engine per shot (Seedance/Kling/banana plate).
9. **Edit blueprint** — order, ASL plan, hero hold, cut motivations, where it breathes.
10. **Sound design map** — the diegetic sound per action + the owned-music plan (Suno).
11. **Watch pass** — /watch the assembled cut; note what actually moves vs what is static.
12. **Hostile film review** — Gemini second-model, reconciled against the brief (accept/reject with evidence).
13. **Rebuild list** — the failing shots (by the Task-1 kill criteria), top-leverage first.
14. **Final gate** — score against os-quality-gates + Commercial Craft 12-axis + this OS. **9/10 floor or a named+accepted gap.** Ship the proof packet.

---

# TASK 7 — THE PUSH-IN LAW (permanent)
**A still image with a push-in is not a film shot.**

It is allowed ONLY as one of:
- a **memory** beat (a remembered/imagined image, clearly coded as such),
- an **insert** (object/detail: a phone, a pill organizer, a photograph),
- a **product detail** shot,
- a **transition** between scenes,
- an **intentional photograph / poster moment** (a deliberate frozen image with narrative reason).

It **cannot** carry: emotional climax, character realization/recognition, or scene action. Those require the SUBJECT to move (i2v with a real performance verb, or keyframe start→end, switching engine if a filter blocks it).

**The standard is cinematic, not beautiful. If it feels like stills in a timeline, it fails.**

---

# MASTER AUTHORITY — STACK REGISTRY + GATE MAP
This document is the master authority for AI film. The full compiled stack (every resource, its laws, redundancy labels, reconciled hierarchy, and gaps) is `FULL_FILM_STACK_COMPILATION.md`. Authority order when anything conflicts:
**REAL_FILM_PRODUCTION_OS → OS_AI_CINEMA_PRODUCTION_DOCTRINE → {OS_HIGGSFIELD_PRODUCTION_DOCTRINE + OS_FINISHING_DEPARTMENT_STANDARD} → grammar skills → benchmarks/libraries → tools.**

## Which resource/gate runs at which stage (no stage runs naked)
| Stage | Resource(s) that must fire |
|---|---|
| 1 brief | brief read; STORY layer |
| 2 story intention | STORY_GATE; story_emotional_target |
| 3 emotional arc | story but/therefore; withhold/reveal |
| 4 action/verb script | this OS (verb rule) |
| 5 scene beats + mode | cinema-worldbuilder mode-select; os-world-bible |
| 6 coverage map | Scene_Sequence (3x3 / 9-scene); banana-pro-director sheets; os-face-lock anchor |
| 7 moving-shot plan (SPEND GATE) | this OS push-in law; os-face-lock motion-ready gate; kling-production-sop preflight; operator sign-off |
| 8 tool per shot | Higgsfield doctrine (i2v/t2v/keyframe; Seedance↔Kling); banana-pro-director / cinema-worldbuilder prompts |
| 9 edit blueprint | Commercial Craft Benchmark V2; OS_AUTOEDIT_DOCTRINE; craft library |
| 10 sound map | cinema-worldbuilder diegetic audio; ElevenLabs SFX; owned music (Suno) |
| 11 watch | /watch skill; os-vision-reject-gate; kling-production-sop motion QA |
| 12 hostile review | second-model Gemini lane |
| 13 rebuild list | this OS kill criteria (F1-F7) |
| 14 final gate | os-quality-gates; Commercial Craft 12-axis; platform-mastering; "PASS is not excellent" 9/10 floor |

## Auto-application
Every film project loads this OS by default and runs the 14 stages with the gates above. Memory `[[real-film-production-os]]` carries it. Composes with [[ai-cinema-production-doctrine]] and [[higgsfield-production-doctrine]]. Full registry: `FULL_FILM_STACK_COMPILATION.md`.
