# OS Foundation Upgrade · why our AI films read "mid" and the disciplined fix

Authored 2026-06-13 by the head of craft, synthesized from 9 whole-watched tutorials (editing, story, storyboarding, production, AI hyperrealism). This is canon. It sits above the per-job docs and beside `OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md` (which came from reference films); this doc comes from the craft tutorials and names the process and the laws.

Operator verdict that triggered this: "our foundation and fundamentals suck." The evidence agrees: hostile whole-watch scores stuck at 6.8 to 7.2 over many iterations, with the same recurring failures every time (print drift, magenta cast, hand melt, reads-as-AI, weak spine and rhythm, generate-before-plan).

Source note, kept honest: only ONE of the nine videos (Yaroflasher, "Hyperrealism in AI Videos Explained") carries real technical hyperrealism levers. The other eight are story, edit, and process craft. So the hyperrealism playbook below leans hard on that one source plus our own proven OS laws; do not pretend the editing-mindset videos taught us lens and grain.

---

## 1. THE DIAGNOSIS (the root, not the symptoms)

We are world-class at the tool and amateur at the foundation, and we have the order of operations exactly backwards: we generate first and then try to author a story, a rhythm, and realism in post, which is building a house on sand. Every recurring failure is downstream of that one inversion. Print drift, hand melt, and the magenta cast happen because we let the model freehand whole scenes per shot with no locked reference and no finishing pass, instead of locking the product and identity OUTSIDE the unreliable generator and re-adding real-camera imperfection deliberately. The films read "mid" because they are a checklist of pretty near-still clips with no motivated cuts, no open loop, and no diegetic sound, so the edit calls attention to its own craft instead of disappearing into a feeling. And we keep re-discovering the same failures because our reflection step (the hostile review) never writes itself back into a permanent pre-flight checklist, so iteration loops instead of compounding. The fix is not a better model. The fix is to move all the authored decisions upstream of the first generation and to make hyperrealism a dedicated finishing stage, not a prompt.

---

## 2. THE NEW PROCESS · story → board → generate → edit → finish

The disease, named plainly: we currently skip STORY and BOARD and jump straight to GENERATE, then patch endlessly in post. That stops now. The pipeline is five gated stages. No stage may be patched downstream; if an upstream stage is wrong, you go back, you do not paper over it in the edit. Approval lives at the boundaries between stages, never mid-fan-out.

| # | Stage | What gets locked | The GATE (nothing proceeds until this passes) |
|---|-------|------------------|------------------------------------------------|
| 1 | **STORY** | Log line + 3-chapter spine + target emotion per beat + audience answer | A one-paragraph spine (who / want / turn / payoff), a target feeling per beat, and the audience answer are written and operator-approved. No prompt fires before this exists. |
| 2 | **BOARD** | Complete shot-by-shot board: every angle, RED action (start→end), BLUE camera move, START-frame + END-box for any push, one-line description per panel; the final track chosen with BPM + marked dips; cuts placed on dips | A panel exists for every shot, each annotated with subject action and a named camera move, and each carrying a one-line sentence that will become the generation prompt. The board is the prompt source AND the QA reference. |
| 3 | **GENERATE** | Frozen reference pack first (suit/print plate, pose set, location plate, lighting mood board, props), then win each STILL (skin pass + grain/detail pass + approval) BEFORE motion, then i2v to the board's start/end frames | Reference pack approved on disk; every hero still is finished and approved; the swimsuit print is a locked trained/PNG asset, not re-prompted per shot. A raw still never goes straight to motion. |
| 4 | **EDIT** | A-roll cut locked to the board and the track; every cut motivated by "what should the viewer feel next?"; one open loop in the first 2 seconds; pacing tagged per beat | The A-roll order is approved against the board panel-by-panel BEFORE any grade, effect, or AI-tell fix. Foundation before decoration. |
| 5 | **FINISH** | Realism finishing pass (skin-texture restore + film grain + micro-sharpen), one locked master grade across every clip, full diegetic + transition sound design, then adversarial whole-watch | Realism pass + single master grade + sound design all present and measured; adversarial-verify / Gemini lane runs against the board and the laws; at least one revision round logged before any master is crowned. |

The throughput rule that ties it together: judge each asset pass/fail against intended use, retry only the FAILED shots individually, ship the passing rest. Never re-run a whole film to fix one shot.

---

## 3. THE LAWS (permanent · adopt all)

Each law ends with the failure it kills.

1. **No generation spend until the story spine is locked.** A one-paragraph spine (who / want / turn / payoff) + target emotion per beat + audience answer is written and approved first. → kills generate-before-plan; kills weak story spine.
2. **No generation spend until the whole film is boarded shot-by-shot.** Every beat, every angle, every move on paper (stick figures count); the board is the prompt source and the QA reference. → kills generate-before-plan; kills on-the-fly invention.
3. **A static frame is not a shot. Every board panel carries RED subject action (start→end) and BLUE camera move.** That annotation IS the i2v prompt: subject verb + named camera move + authored end keyframe. → kills the slideshow-of-near-stills AI-tell; kills the "push-in is not a shot" failure.
4. **Lock the product and identity OUTSIDE the generator. The swimwear print is a real cut-out PNG / trained reference, composited or inpainted, never re-prompted per shot.** One locked variable per generation; pin face/print/environment by reference on every other axis. → kills print drift; kills new-melt-per-fix.
5. **Win the still before motion, and the still is a multi-pass build, not one generation.** Base → skin/realism pass → grain/detail/sharpen finish → approval → only then i2v. GIGO: the video model can only animate the realism you hand it. → kills reads-as-AI; kills hand melt (clean the geometry in the still, then add texture).
6. **Hyperrealism is a dedicated finishing pass, not a prompt.** Re-add real-camera imperfection on every hero frame: skin-texture restore, film grain, micro-sharpen at low values; build a SNIPED preset and measure skin before/after. → kills the clean-but-AI "midjourney look."
7. **One locked master grade across every clip, measured clip-to-clip; derive overlay colors from a real in-frame value.** No per-clip eyeballed grading; sample the actual key palette, do not invent a hex. → kills the magenta cast and stray-cast class of grade errors.
8. **Every cut is motivated by "what should the viewer FEEL next?" Write that line in the EDL before choosing the cut.** You are building an emotional experience, not arranging footage. → kills the checklist-of-pretty-shots rhythm.
9. **Motion never fully stops between beats; peak the speed graph on the cut.** Shot B is already accelerating across the cut as shot A settles; build continuity inside the generation via start/end frames and bounded multi-shot prompts (cap shot-switches ~6). → kills the slideshow read.
10. **Open one curiosity loop in the first 2 seconds, paid off only at the end.** Withhold the full reveal (the suit, the face, the destination); audit the board for "what question is open here?" → kills the flat, no-hook spine.
11. **Diegetic sound is a realism lever, not a garnish. Layer SFX locked to on-screen motion under every shot, as a gated stage.** Fabric, water, footsteps, room tone, whoosh-on-cut; three balanced layers (dialogue clear → SFX → music that never buries the rest). → kills the silent-slideshow AI-tell from the audio side.
12. **Cut your darlings. If a shot does not serve the story emotion, cut it no matter how expensive the generation was.** → kills keeping weak-but-costly AI shots; kills bloat.
13. **Restraint is the craft: less is more. Strip gratuitous moves, effects, over-grading; if a shot needs a gimmick to be interesting, the shot is weak, fix the shot.** Over-processing is itself an AI tell. → kills the over-cooked, attention-on-its-own-craft read.
14. **The best edit is invisible. The hostile rubric's top axis is "did it make me feel something / could I not look away," and any shot drawing attention to its own AI move is a deduction, not a plus.** → kills "that editing was cool" (which means we missed).
15. **Reflection must update the process. Every verified failure becomes a permanent pre-flight checklist item.** When a generator thread starts drifting, abandon it and restart from the locked reference pack; do not patch-prompt a contaminated context. → kills the loop where we re-discover the same failures forever.

---

## 4. HYPERREALISM PLAYBOOK (our #1 technical gap, ordered by impact)

This is the part the operator means by "make AI footage read real." Ordered cheapest-and-highest-impact first. Most of the win is in still-frame preparation and a dedicated make-it-real pass, NOT in the video model.

1. **Degrade-and-rebuild finishing pass on every hero still (HIGHEST LEVER).** Generate clean, then re-introduce real-camera imperfection: skin-texture restore (fix plastic skin, restore pores and fine hair, dial wrinkles per shot), film grain (Magnific-style detail 30-50%, grain 20-30, sharpen 5-10, export at 100%). The raw output "still looks AI generated" until this pass. Build it once as a SNIPED preset. This single change attacks print-drift and the AI-tell at the same time and sits on stills we already make.
2. **Win the still before motion; never animate a raw generation.** The image is a sequential multi-pass build: base → realism/skin pass → grain/detail/sharpen → approval. The i2v model only animates the realism you hand it.
3. **Lock identity and product as a trained subject / real PNG, not per-shot prompting.** A trained reference (3 prepped images is enough) or a real cut-out beats re-prompting on consistency, quality (no upload/download downgrade), and safety-block bypass. The swimsuit print is pixel-stable, not re-hallucinated each shot.
4. **Skin and micro-texture are the #1 realism tell.** Uniform smoothness reads fake; restored pores, fine hair, and slight imperfection read real. Clean the geometry first (fix moles/melts in generative fill), THEN add texture. Crop-verify at 100% per our composite-master-qa.
5. **Final grade + subtle film grain baked into the master.** A standing finishing step on every deliverable, applied last in Premiere/AE. "Always gives a more realistic feel."
6. **Unexpected poses and camera angles read authentic; safe, symmetric, catalog-frontal poses read fake.** Curate an off-axis / candid / mid-gesture pose reference block and drive i2v start/end frames from it.
7. **Build continuity and shot-switches inside the generation.** Bounded multi-shot prompts (cap ~6 switches) and flipped start/end frames produce coverage and "infinite shots without cuts," so the edit is assembly not rescue. Reinforces our authored-END-keyframe method that defeats the i2v push-in default.
8. **Prep 90% before generating: a frozen reference library is the foundation of realism.** Actors/faces, wardrobe + every accessory, poses, makeup, hair, environment plates, lighting mood boards, props. Locked as files, approved, before a single clip.
9. **Route by tool strength per stage, not loyalty.** Best-still vs best-identity-lock vs best-finishing vs best-i2v vs best-lip-sync are different engines; write an explicit per-stage routing map for each job and swap without sentiment.
10. **Manage generator context as a reset discipline.** Stale hidden context corrupts later outputs; when print/face/lighting starts drifting, start a fresh thread from the locked pack rather than patch-prompting on top.

---

## 5. APPLIED TO ALMA NOW · the 5 highest-leverage changes to the Deadpan Summer cut

Apply these to the current cut immediately, in this order:

1. **Lock the swimwear print as a real cut-out PNG asset and composite/inpaint it into every shot.** Stop letting any model freehand the garment in motion. This is the single move that kills our #1 recurring failure (print drifts / reads fake). One locked variable per generation; pin print, face, and environment by reference on every other axis. (Laws 4, 5; Playbook 1, 3.)
2. **Run the degrade-and-rebuild realism pass on every hero still before re-cutting.** Skin-texture restore + film grain + micro-sharpen at low values, crop-verified at 100%, before any frame is animated or re-graded. This is the cheapest score lever and it attacks both the AI-tell and the magenta-cast class at once. (Law 6; Playbook 1, 2, 4.)
3. **Lay down one locked master grade across the whole cut and measure it clip-to-clip; derive any overlay color from a real coral-on-cream in-frame value.** No per-clip eyeballing, no invented hex. This is exactly the discipline that caught the magenta cast; make it standing, not a save. (Law 7.)
4. **Rebuild the cut for motivated rhythm and continuity: write "viewer should feel ___" on every beat, open one withheld reveal in the first 2 seconds (the full suit / the destination), and land every cut on a speed peak so motion never dead-stops.** Default to longer luxury holds, but tighten any beat that drags. This is the fix for "slideshow of near-stills" and the deadpan that currently reads flat instead of expensive. (Laws 3, 8, 9, 10.)
5. **Add the diegetic + transition sound-design pass as a gated stage before the next hostile watch.** Water, fabric, footsteps, room tone, whoosh-on-cut, three balanced layers under a single owned track. Silent or music-only cuts read fake and this is a repeat gap in our reviews. Then run adversarial-verify against the board and these laws, with one revision round logged before anything is crowned. (Laws 11, 14, 15; Process stage 5.)

Do not chase 10/10 on every beat: designate 2 to 3 HERO beats that get the full perfection budget (print, realism pass, hand fixes, grade) and keep the connective beats merely clean, so effort concentrates where the hostile reviewer actually looks.
