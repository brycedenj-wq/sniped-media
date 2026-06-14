# HIGGSFIELD INDISTINGUISHABLE-FROM-REAL CINEMA PLAYBOOK
## Synthesized from 15 product/tutorial digests · for the Alma Love Club team

This is the de-duplicated craft spine. It assumes you already passed image-quality and are losing the realism war at the level of tells (signage, skin, physics, motion drift) and at the level of authored cinema (composed light, intentional camera, blocking). Everything below is prescriptive. Nothing is optional on a deliverable.

---

## 0. THE ONE LAW THAT GOVERNS EVERYTHING

**Garbage in, garbage out. The video model holds the first frame; it cannot save a weak first frame.** Across every Cinema Studio digest the same truth repeats: you spend your time on the still, then animate. A still that is photoreal, correctly lit, correctly framed, and free of tells will animate into a photoreal clip. A "mid" still animates into a mid clip with motion artifacts stacked on top. So realism is won 80% in the keyframe and 20% in the motion prompt. The Alma cut reads mid because the establishing plates were treated as throwaway, not as the load-bearing frame.

---

## 1. WHICH FEATURES AND MODELS TO USE (AND WHY)

Route by job. Do not default to one tool.

| Job | Use | Why |
|---|---|---|
| Photoreal still / keyframe with real camera language | **Cinema Studio (image mode) → Cinematic Cameras** | This is the only path that lets you pick camera body, lens, focal length, aperture. It bakes intentional composition and depth at every level instead of the flat, dead-center, evenly-lit "AI hallway" look. A generation is ~1/8 to 1/2 credit, so iterate freely. |
| Best photoreal motion (the hero video model) | **Seedance 2.0** (15s max, up to full HD) | Named in the digests as the current best video model. Holds first-frame texture and lighting logic, real debris/physics. This is your default for the Alma car-and-street beats. |
| Director-grade per-shot control inside one clip | **Cinema Studio 3.5 (multi-shot manual)** | Up to 6 scenes / 12s, per-scene camera move + speed ramp + emotion + genre. Use when you need authored blocking inside a single generation. |
| Dialogue / lip-sync / spoken line | **Kling 3.0** or **Veo 3.1** | If a beat needs a spoken word with believable acting. (Alma is largely non-verbal, so this is minor.) |
| Locking the model's identity across the whole spot | **Soul ID (train once) + Elements** | Train Alma's face on 5-6+ clean multi-angle stills → one reference_id reused in every shot so she is the same person in every frame and six months later. Elements does the same for objects (the Mercedes, the cherry bikini). |
| Establishing-plate variety from one generation | **Grid generation (2x2 / 3x3 / 4x4)** in image mode | Nine boulevard variants in one gen; upscale only the winner. Cheap idea machine for the establishing street. |
| Exact angle without re-rolling prompts | **3D Scene access** (Cinema Studio 2+) | Generate the plate, enter the low-res 3D/splat view, fly the camera to the exact angle, capture shot → high-res. This is how you nail a specific establishing composition deterministically instead of gambling on prompts. |
| Cleanup of artifacts after the fact | **Video upscale → Sora 2 enhancer**, then Topaz to 2K/4K, optionally 30fps | Removes glitches/distortion that survive generation. Always the final step, never a fix for a broken plate. |

**On Supercomputer:** It is an orchestration agent (pick the LLM brain, fan out to all models, memory + connectors). It is excellent for end-to-end *ideation, brand-kit, storyboard, batch* work and for goal-mode batching. But the honest digest verdict is clear: for a single indistinguishable-cinema shot, Supercomputer "tries to bite more than it can chew" and stitches multi-clip audio that sounds like three different people. **Do not let Supercomputer author your hero realism shots. Author them by hand in Cinema Studio / Seedance.** Use Supercomputer only for the boring scaffolding (concepts, shot lists, batch variants), never to crown the final cut.

---

## 2. THE CONCRETE PHOTOREAL GENERATION WORKFLOW

This is the locked pipeline. Run it in order for every beat.

1. **Lock identity first.** Train Soul ID on Alma (5-6 clean stills, varied angles, white/neutral background). Build Elements for the black Mercedes and the cherry-print bikini (2-3 reference angles each, white background). Now every shot can `@tag` the same face, same car, same suit.
2. **Build the location as a reusable asset.** Cinema Studio → Locations. Write one *detailed* boulevard description (you will reuse it across every street shot, so over-specify). Save it. **Never generate the location head-on / front-facing** (the model loses depth perception and you get the flat plate). Shoot three-quarter or a high corner CCTV-style angle.
3. **Set an anchor in the location.** Every location needs a fixed anchor object (a specific palm, a storefront column, a curb cut) so you can place the car and Alma by reference ("Mercedes parked to the right of the corner palm") and keep camera placement consistent shot to shot.
4. **Compose the keyframe in Cinema Studio image mode with Cinematic Cameras.** Pick the camera body, lens, focal length, aperture deliberately (Section 4). Generate 4. If the angle is wrong, use 3D Scene to fly to it rather than re-rolling.
5. **Run the KILL-AI-TELLS checklist on the still (Section 3) BEFORE animating.** A tell in the still becomes a tell in motion plus drift. Fix the still or regenerate it. This is the gate the Alma cut skipped.
6. **Animate at 720p** (1080p is ~2x the cost). Keep the whole project at 720p, upscale once at the end. Use the keyframe as start frame; for continuity, attach the **last ~5 seconds of the previous clip** as reference so the next shot starts exactly where the last ended (no jump cut, no drift).
7. **Single vs multi-shot:** single-shot for held, performance/atmosphere beats (most of Alma); multi-shot only for action or cuts. Even in single-shot you can define what happens at each second for max control.
8. **Iterate by salvage, not by re-roll.** First batch rarely works. If you like the first 5s and hate the last 10s, tell it to change only the last 10s. A failed 15s generation usually contains 2 good seconds: cut those out and keep them.
9. **Stitch, color, upscale.** Assemble in Premiere/CapCut, grade for a single consistent look across all beats (the day-to-night arc must feel like one roll of film), then Sora-2 enhance + Topaz upscale once.

---

## 3. THE KILL-AI-TELLS CHECKLIST (HARD GATE — run on every still and every clip)

No beat ships until every line passes. This is the section that fixes "mid."

**A. Signage / text (the Alma killer).**
- The model cannot spell on small or background text. Do not let it try. **Prompt rule: "no text on signage, no text on storefronts, no text on clothing, no logos, no readable lettering."** Bake this into the style prefix so it is on every generation by default.
- Where the world genuinely needs a sign, the storefront in your retro Beverly Hills must read as *deliberately blank, abstract, or pattern-only* awnings and glass, OR you place the real text yourself: composite a clean, correctly-kerned vintage sign in Photoshop/After Effects over a blank awning. Never accept model-rendered words in frame.
- Far-background signage should be thrown out of focus (shallow depth of field) so any residual scribble is unreadable. Half the fix is optical: if the lens blurs it, the gibberish dies.
- Final check: pause every frame. Any glyph a viewer could try to read is a fail.

**B. Plastic skin.**
- Cause: too much light on the face + over-clean render. Fix in prompt with anatomical and skin specificity (pores, fine texture, faint imperfection, natural specular falloff), and use **practical light only**.
- Post: run the **Skin Enhancer** in "realistic" or "imperfect" mode. Small imperfections read as real; flawless reads as CGI.
- For Alma specifically (bikini = lots of skin in frame): match skin sheen to the daylight; sweat/sheen must be subtle and directional, not a uniform gloss.

**C. Morphing / identity drift.**
- Use Soul ID + Elements so the face/car/suit are locked assets, not re-rolled each shot.
- Carry the last 5s of the prior clip as a reference into the next.
- When a wide shot makes the face plasticky or off-model, cut the face from the character sheet's clean close-up and use that as the face reference.
- Track state across the day-to-night arc (hair, suit, car position, light direction) so nothing pops between cuts. "Script supervise" the continuity.

**D. Physics.**
- Name the materials and what they do. The model defaults to wrong physics (debris reacting while a drink doesn't, a "drink can" smoking, hair frozen). Specify: car suspension settle, heat shimmer off asphalt, fabric and hair moving with the actual wind/motion, reflections tracking across the Mercedes paint as the camera moves.
- For props with hidden geometry (here: how the bikini ties, how a hand grips the door handle) make a **prop sheet** of the tricky part so the model stops guessing.

**E. Over-clean / "too perfect" look (the deepest tell).**
- This is why polished frames read fake. Counter it everywhere: **prompt like a photographer, not a describer.** Specify film stock, grain, halation, slight bloom, lens flare, gentle vignetting, bokeh, a real aperture. A 1970s Americana spot should carry visible film grain and warm halation.
- Choose **practical light only** (sun, sky bounce, neon, headlamps, shop windows) so light belongs to the scene instead of the floating "extra light source from behind" that makes a subject look pasted in.
- Allow imperfection: a handheld micro-shake, a slightly imperfect framing, a dust mote, an over-exposed highlight. Perfection is the tell; controlled imperfection is the cure.

**F. Motion artifacts / FPS.**
- Review frame by frame; one bad frame kills a shot.
- If FPS drops and the clip stutters (18fps when you asked 24), delete duplicated frames.
- Run the final through Sora-2 enhance to clear residual distortion.

---

## 4. PROMPT / CAMERA / LIGHTING CRAFT FOR REALISM

**Prompt like a cinematographer, in this density:** one shot = one main idea + one main action + one main camera move. Do not overload (conflicting durations and stacked edits make the model hallucinate; when a prompt gets long, have it sanitized/optimized). Structure every prompt as:

`[subject + identity tag] + [action with anatomical/physical specificity] + [blocking vs the anchor] + [camera body, lens, focal length, aperture] + [camera move] + [practical lighting + direction + color temp] + [film stock/grain/halation/lens character] + [negative: no text, no logos, no extra light sources]`

**Lighting laws:**
- Practical only. Name the source and where it falls ("low golden sun camera-left raking across the hood, warm bounce filling the shadow side, no fill from behind").
- 60/30/10 color discipline: 60% dominant, 30% secondary, 10% accent — the cinematic balance. For Alma day: sun-bleached pavement/white as dominant, the black Mercedes and cherry-red as the 30/10 punch.
- The day-to-night arc is a lighting story: author the key direction and color temp shifting warm-noon → golden → dusk magenta → night neon/headlamp across the beats so it reads as one continuous evening.

**Camera laws:**
- Always pick a real lens/aperture; never leave it default. Shallow depth of field is both a look and a tell-killer (kills background signage).
- Never establish a location front-on. Three-quarter or high-corner for depth.
- Start every dialogue/multi-subject sequence with an establishing or medium shot so the model locks positions; closeups after that inherit correct geometry.
- If you don't know what camera a reference look used, feed a frame of your favorite 1970s film to Claude and ask which camera/lens/stock, then port those tokens into the prompt.

**Get the prompt from an LLM, deliberately.** Start with "give me a detailed keyframe prompt: I want a [simple description]" → let Claude expand to the photographer-grade prompt. Saves credits by avoiding bad rolls. Cinema Studio's built-in AI Director does the same and will also propose the camera body/lens/aperture/move per shot — use it as a starting plan, never as the final.

---

## 5. EXACT NEXT ACTIONS TO RE-PRODUCE THE WEAK ALMA BEATS

Priority is the establishing street with the fake signage, because that is the frame that brands the whole spot as AI.

**Step 1 — Build the asset library (do once).**
- Train **Soul ID: Alma** from her best clean stills.
- Build **Element: Black Mercedes** (front 3/4, side, rear 3/4 on white).
- Build **Element: Cherry-print bikini** (front, back, detail on white) and a **prop sheet** for how it ties.
- Save **Location: 1970s Beverly Hills boulevard** with one over-detailed description and a named anchor (e.g., "the corner palm").

**Step 2 — Fix the establishing street (the signage beat).**
- In Cinema Studio image mode + Cinematic Cameras, generate the boulevard **three-quarter, never head-on**, with anamorphic-friendly glass (e.g., 35-40mm vintage prime, ~f2, grand-format film look, warm low sun).
- In the prompt, hard-negative: **"no text, no readable signage, no logos, no lettering on storefronts or awnings; background storefronts abstract and out of focus."** Push shallow DOF so the whole storefront row sits in soft bokeh.
- Use **grid 3x3** to get nine boulevard variants in one gen; upscale only the cleanest, sign-free one.
- For any storefront that *must* read as a sign, leave it blank in-generation and **composite a clean retro sign yourself** in Photoshop/AE over the blank awning. Never let the model render the word.
- Use **3D Scene** to fly to the exact establishing angle you storyboarded, then capture at high res.
- **Run Section 3 on this still.** It only passes when there is zero readable glyph anywhere, the skin (if Alma is in frame) is non-plastic, light is practical-only, and there is visible grain/halation.

**Step 3 — Animate the establishing beat.**
- 720p, Seedance 2.0 (or Cinema Studio 3.5 single-shot), keyframe as start frame.
- Motion prompt: a slow authored push or lateral dolly along the boulevard, heat shimmer off the asphalt, reflections tracking across the Mercedes paint, palms drifting in light wind, Alma's hair and the cherry fabric moving with the air. One camera move, named lens, practical light. Negative-prompt text again at the video stage.
- Generate a small batch; salvage the best 2-5 seconds rather than chasing a perfect 15.

**Step 4 — Re-produce the remaining weak beats** the same way: rebuild each weak plate to indistinguishable quality first (identity tags + Cinematic Cameras + tell-checklist), carry the last 5s of the prior clip as reference for continuity, hold the day-to-night light story, then animate at 720p.

**Step 5 — Finish.**
- Stitch in order; the start-where-last-ended discipline means minimal cutting.
- Grade once for a single 1970s film register across all beats (warm, grainy, saturated cherry/black/cream).
- Sora-2 enhance → Topaz to 2K/4K, optional 30fps. Frame-by-frame final QA against Section 3.

**Step 6 — Adversarial verify before crowning.** Per the harness law: a fresh-context / second-model pass (the Gemini hostile-critic lane) must try to break the result and confirm there is no readable signage, no plastic skin, no morph, no physics tell, no over-clean giveaway. The author of the shots does not get to declare them indistinguishable. Only the Verify gate crowns the cut.

---

### One-line summary for the team
Win realism in the still (Cinema Studio + Cinematic Cameras + locked Soul ID/Elements), kill every tell on the still before animating (especially: negative-prompt all text and composite real signs yourself, shallow-DOF the background, practical-light-only, force grain/imperfection), animate at 720p with last-5s continuity on Seedance 2.0, upscale once, and let an adversarial second model — not the author — confirm it is indistinguishable.

---

Files for the orchestrator: the digest task (#10) is complete; the apply task (#11) is the Section 5 execution plan above. Source transcripts read in full at `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/HIGGS_LEVELUP/transcripts/` (all 15). No file was written — this playbook is the return value.
