# OS Elevated AI Film Doctrine

Engrained 2026-06-09 from 7 reference films, all whole-watched/whole-read end to end (transcripts pulled, cleaned, and read in full in the main thread after two workflow fan-outs failed on subagent network/runtime). No sampling. Lessons below are what the films actually teach, cited to source.

## Why this exists
The Synergy HomeCare "The Door" build reached "competent but mid" (operator verdict: "we not making cinema rn ... too mid"). The cause is structural, not cosmetic: animating single stills with tiny i2v drift and gluing them with cross-dissolves over VO plus piano is a slideshow. These references define the bar and how to reach it with the AI stack.

## The 7 sources
| # | Film | Len | What it teaches best |
|---|---|---|---|
| 1 | Dan Mace, How to Master the Art of Filmmaking | 2h49m | Story, log line, music as 40%, diegetic sound, the full edit method, grade, mix |
| 2 | Creating with Conor, The Only AI Filmmaking Workflow | 15m | Higgsfield Cinema Studio: story-first, saved character/location/prop elements, video-reference continuity, emotion settings, explicit action verbs, one music track |
| 3 | Camp Films, Basics of Cinematography | 19m | Composition, depth, 3-point light, movement vocabulary, white balance, color theory |
| 4 | Alfie Vaughan, Film Making Basics in 8 min | 8m | Shot sizes, rule of thirds, 180 rule, lens compression, match on action, pacing, mics, avoid cheesy transitions |
| 5 | StudioBinder, Film Blocking | 5m | Blocking via space, shapes, lines, and subtext |
| 6 | Sam Newton, Solo Filmmaking / cinematic brand doc | 16m | Emotional brand documentary about a real person: feeling-first, music-first, coached VO, coverage, layered subtle sound, simple LUT grade |
| 7 | Higgsfield AI, 3 Hours of Making an AI Film (Watch Me Fail) | 3h06m | The REAL AI build at the bar: Claude shot-list skill, style prefix, reference sheets, Seedance 2.0, batch-and-cull, spatial-layout prompt blocks, emotion-not-action direction, natural light + env SFX only, edit as you go |

## A. Story and pre-production (Mace, Sam, Conor, Higgsfield)
1. Lock the LOG LINE before generating a single frame. Formula (Mace): problem, intention to overcome, obstacle, solution. It is your compass for every later decision. Conor and Higgsfield say the same: lock the STORY first or you get disconnected clips, not a film.
2. A great story has 4 parts (Mace): identifiable characters, a significant moment or event, authentic emotion, and specifics. Reduce to 3 acts: impact (attention), influence (communicate), persuasion (transformation).
3. Personify ONE (Mace's sea-turtle and Nera rule): make the audience identify with one human, then scale to the number. Do not lead with statistics.
4. Feeling first (Sam): decide how it should FEEL, choose the music to that feeling, then write the voiceover to the music. The subject's own voice, coached for inflection, beats a narrator.
5. Add a time constraint / urgency to the obstacle (Mace) to make it engaging.

## B. Shot grammar and camera (Camp, Alfie, Mace, Higgsfield)
6. Use shot sizes with intent and escalate wide to tight: establishing/EWS to set geometry, WS, MS, MCU, CU, ECU for emotion. Do not shoot everything wide (Alfie: "do not do this").
7. Compose: rule of thirds, eyeline on the upper third looking INTO the frame, lead room. Build depth (foreground, midground, background) and frame-within-a-frame (a doorway). Flat, centered, even = mid (Camp).
8. Lens intent: long lens compresses and creates intimacy; wide exaggerates space. Use a focus pull to direct the eye.
9. 180-degree rule for two subjects; over-the-shoulder for dialogue.
10. Motion must be MOTIVATED: pan/tilt to reveal, dolly/track to follow, push-in to close emotional distance. "Movement should serve the story" (Camp). For real human moments, feel the motion (Mace prefers honest handheld over fake-smooth gimbal). Still plus push-in is NOT a film shot.

## C. Blocking (StudioBinder)
11. Stage with meaning. Space encodes power and importance (distance from lens). Shapes carry emotion: circle safe/inclusive, square boxed-in, triangle aggressive with an apex. Lines: vertical = power, horizontal = submission (Godfather Fredo). Block AGAINST the dialogue to create subtext.

## D. Lighting (Camp, Alfie, Higgsfield)
12. Three-point: key at ~45 degrees, softer fill opposite, rim/back light for separation. Low-key (high contrast) for mood; put practicals in the frame. Higgsfield's consistency rule: natural light only, key from sky and windows.
13. Consistent white balance across every shot.

## E. Color (Camp, Mace)
14. Color is emotion. White balance first, then grade. Mace's actual grade is SIMPLE and disciplined: shoot log, apply one conversion LUT to Rec709, then a little contrast and saturation, on EVERY clip, balanced frame by frame. A palette that pops but stays consistent. A tint slapped on flat plates is not a grade.

## F. Editing (Mace, Sam, Alfie)
15. Organize obsessively (folders, selects, scenes, master). Reduce, reduce, reduce.
16. The 1:30 opening formula (Mace): impact (first 5-7s, the hook line, the strongest image), hook (7-30s, a reason to care), communicate (30-90s, the story). Nail this first; the rest flows.
17. Coverage rule (Sam): every setup gets one wide, one medium, one tight, one other. It gives the edit room to breathe.
18. Cut ON action; match on action. Avoid built-in cheesy transitions (Alfie). Dissolves are a deliberate, rare device for a time or emotion jump, never default glue.
19. Pacing curve: longer, slower cuts to open, tighter as tension builds, a held beat on the payoff.
20. Kill darlings via the log line. If a beautiful shot does not serve the line, cut it.

## G. Sound and music (Mace, Sam, Higgsfield, Alfie)
21. Music is ~40% of the film (Mace). Use one track with a recurring MOTIF; tease it, hold the buildup long so the crescendo actually lands. Music amplifies the story; if viewers compliment the music or the edit, the story lost (Mace).
22. Build a DIEGETIC layer from the real location and layer SFX (Sam: mute the music and the film should still be fully sound-designed; use multiple layered sounds, not one whoosh). Room tone under every shot, plus authored foley (door, footsteps, fabric, breath, kettle, clock).
23. Mix order and levels (Mace): vocals first (enhance, around -9 to -12 dB), music second (duck under vocals, around -2 dB, lift only for the crescendo), SFX/ambience third. Use J and L cuts so sound leads or trails the picture.
24. Generate with environmental SFX only and NO music in the model output (Higgsfield); add owned/licensed music in post so tracks do not change at every cut.

## H. The AI-specific workflow (Conor, Higgsfield) - this is the part we were getting wrong
25. Pipeline order: STORY, then ASSETS (characters, locations, props built and SAVED as reusable reference elements), then VIDEO with those elements tagged in every prompt. Consistency comes from reusing saved elements, not re-describing.
26. STYLE PREFIX: one locked block defining style, lighting, color, composition, and audio, prepended to every shot prompt so a whole film (or a whole team) stays consistent (Higgsfield).
27. Use a Claude shot-list skill: feed the script, split into shots, generate model-tailored prompts, keep a living shot list you can edit per shot.
28. Reference sheets with spatial context: build a location as multiple views (front plus a reverse angle, combined into one reference image) so the video model understands the space and stops inventing doors.
29. Lock the STILL perfectly before animating. Nano Banana Pro: batch 4, fix via prompt not by hand, fight the plasticky look with keywords (atmospheric haze, film grain, crushed blacks for shadow depth, practical light). The video model inherits the still's flaws, so a perfect still saves video credits.
30. Video (Seedance 2.0 / Kling): batch 8 and cull hard. The real hit rate is about 1 in 60 to 1 in 100. Use a spatial-layout block in the prompt to fix camera placement. Direct EMOTION, not action ("slow it barely reads as walking, like being dragged forward by grief," not "walks sadly"). Force ONE continuous motion or the model inserts its own cuts. Reference order matters.
31. Edit AS YOU GO with the music on the timeline; use L and J cuts; salvage a near-miss with frame-dup removal (B-roll only, you lose the audio).
32. Brutal iteration IS the standard, not a failure: 72 generations for one 10-second shot; about 8 of 800 assets made the cut. Quality = volume of authored attempts times ruthless selection. Plan credits and time for it.

## I. Why Synergy "The Door" reads mid (diagnosis against the above)
- Breaks 25, 26, 28, 30: no saved-element consistency discipline, no style prefix, no spatial-layout authoring, single near-still i2v with default drift instead of authored motion. This is the number one tell.
- Breaks 6, 7, 17: a string of similar medium portraits, no wide-to-tight escalation, no depth staging, no real coverage.
- Breaks 10, 18: unmotivated micro-motion and all-dissolve glue instead of motivated moves and cuts on action.
- Breaks 11: no blocking with subtext (the new caregiver-touch beat is the first shot that has real blocking, which is why it works).
- Breaks 22, 23: VO plus piano with no diegetic layer, no foley, no room tone.
- Breaks 14: an ffmpeg tint instead of a disciplined per-clip grade.

## J. The biggest single move
Stop generating single near-still i2v shots. For every beat: author a START and an END keyframe (subject has performed, camera has arrived), generate START to END with a spatial-layout block and emotion-driven direction, batch 8-plus and cull, and design real blocking and one motivated camera move into each shot. Wrap it in a diegetic sound layer and the 1:30 story formula. That alone converts slideshow into film.

## K. Elevated Synergy "The Door" rebuild (concrete)
Treat it as a tight 5 to 6 shot emotional brand documentary (Sam's model) executed as an AI film at the Higgsfield bar.
- Log line: a worn-down family caregiver at 2am fears she is failing; Synergy steps in; for the first time she can breathe, because someone is in the home caring for her mother.
- Keep what already clears the bar: the Eleanor recognition hero (photoreal, real face), the NEW caregiver-hand-on-shoulder touch beat (real blocking, clean hand, both identities), and the NEW warm clean door.
- Rebuild each remaining beat with an authored END keyframe and ONE motivated move (push-in on the 2am face as the decision lands; a slow dolly past a foreground doorframe into the lit room; a rack focus from the phone to the mother's door).
- Add the diegetic layer: 2am room tone, phone buzz, the door, footsteps, a kettle, fabric, a held breath. Duck the licensed piano under the VO; lift it only at the recognition crescendo.
- Re-grade with one LUT plus small per-clip contrast and saturation, skin protected, consistent across all shots.
- Cut on action, hard cuts on the beats (phone buzz, door, recognition), one dissolve maximum for the time jump.
- Run it through the role-scoped harness (worldbuild, keyframe-select, grade, sound, edit) and end with adversarial verify before any send.

## Status
Engrained from full whole-reads. Apply on the next Synergy rebuild and pressure-test in use; refine this doc as the stack changes. Related: [[ai-cinema-production-doctrine]], [[ai-performance-shot-method]], [[higgsfield-production-doctrine]], REAL_FILM_PRODUCTION_OS.md.
