# HIGGSFIELD MAX PLAYBOOK (living doc)

The one doc you open every time you make an AI film, ad, or product video. It is the union of three things: (a) the laws proven by our own production failures, (b) the full Higgsfield tool map verified against our runs, and (c) the genuinely new techniques harvested from 40 reference videos (Higgsfield/Supercomputer creators, After Effects masterclasses, best-commercial refs). It supersedes nothing in `OS_HIGGSFIELD_PRODUCTION_DOCTRINE.md`; it sits on top and is the practical front door. When the doctrine and this doc agree, follow either. When this doc is more specific (it usually is), follow this.

Status: LIVING. Plan: Ultra. Operator works mostly in Claude Code / terminal. No em-dashes anywhere (lifetime rule).

---

## 0. How to use this doc + changelog

**How to use it.**
1. Before any serious film/ad/product job, read Section 1 (THE LAWS) once. They are short on purpose. If you only read one section, read that one.
2. Pick your pipeline in Section 3 and walk it stage by stage. Each stage names the exact tool and the gate that has to pass before you spend on the next stage.
3. Pull prompt structures from Section 4. Do not freehand when a structure exists.
4. Before any batch spend, run the cost preflight in Section 5.
5. When you are unsure whether a step belongs in the terminal, the web app, or Photoshop, Section 6 settles it.
6. Section 2 is the reference encyclopedia. You do not read it front to back; you look up the one tool you are about to use.

**The honest answer to "am I using Higgsfield the max way?"** Mostly no, and the reason is simple: you have been trying to win exactness inside motion and inside one big agentic prompt, which is the one thing the platform cannot do reliably in June 2026. The max way is the opposite. Win the hard parts on stills with your eyes on the web app, lock reusable assets once (Soul, Product, Elements), drive the boring repeatable parts (batch stills, assemble, organize, preflight) through Claude Code, and reserve Photoshop for the guaranteed-exact product print. You are paying for Ultra; the leverage is in the reusable locks and the gates, not in re-rolling.

**Changelog stub.**
- 2026-06-14 v1.0: First consolidation. Baked in the Alma exact-product failures, the full tool map, the 40-video harvest. Authors: OS production lane.
- 2026-06-14 v1.1: Adversarial verify pass (scored v1.0 at 8/10, prevents_our_failures=false). Fixed: added LAW 6 (author the END keyframe + batch-8-and-cull at ~1-in-60-100, the anti-slideshow lever); honest caveat that motion print-hold is UNPROVEN + real-cut-out-PNG-via-Vibe-Motion/AE as the DEFAULT for prominent on-screen exact-product motion; the i2v wardrobe-drift guard for swimwear; the degrade-and-rebuild realism finish as a blocking Stage 2 gate; and Section 8, the pre-flight checklist that writes these scars back upstream. This is the version that prevents all six known failures.
- (add entries here as new proof lands: date, what changed, what failed, the fix. RULE: every hostile-review finding must be written back here AND into the relevant law/stage, or the loop repeats.)

---

## 1. THE LAWS

These are not guidelines. Each one is a scar. Break one and you will repeat a failure we already paid for.

**LAW 1: Win on stills, then animate. Always.**
Identity-locked stills are cheap (Nano Banana Pro ~2 credits) and controllable. Video is expensive (Seedance 720p ~22.5cr/5s, 1080p ~45cr/5s; some plans benchmark a 10s 1080p Seedance run at ~90 credits). A bad concept costs 2 credits to catch on a still, not 90 in motion. Generate the exact frame as a still, gate it, then animate ONLY the approved frame as a start frame. Storyboard the whole thing in stills and get sign-off before the big motion spend.

**LAW 2: THE WALL. Pixel-exact product print inside a moving AI shot is NOT achievable (June 2026).**
AI generation and AI garment-swap REPAINT a print every time and DRIFT it across frames. You cannot hold a real product's exact print pixel-true inside Seedance/Kling motion. You can only win pixel-exact on a STILL (Virtual Try-On of the real product, or a Photoshop composite of the real print). The fix is structural:
- Win the suit/product exact on a still first.
- Gate that still against the real product photos.
- HONEST CAVEAT (do not skip this): subtle i2v motion REDUCES print drift, it does NOT guarantee the print holds. Garment-hold across motion is still unproven; any i2v take can drift the print even with a perfect start frame. So you must verify first/mid/last frames of every take and you must have an escape.
- THE ESCAPE, and the DEFAULT for any beat where the product must be EXACT and is prominent ON SCREEN while moving: do NOT i2v-generate the product. Animate the real cut-out product PNG (transparent) via Vibe Motion or After Effects over the plate. That is real pixels moving = pixel-exact AND moving. i2v-subtle-motion is allowed ONLY for beats where the product is partially concealed, small in frame, or not the subject (the inverse product-visibility-vs-motion law: the more the product fills the frame, the less you let AI move it).
- Reserve every product-detail "buy it" beat as an exact still with a slow Ken Burns push, or the real-PNG-over-plate composite. A slow push on a Photoshop-exact still is both pixel-exact AND moving. That is how you get a moving product shot that is still truthful.

**LAW 3: Lock identity once, reuse the reference everywhere.**
The character stays the character because the reference is LOCKED, not because each prompt re-describes them. Train the Soul once. Build the base + multi-angle character sheet once. Register the Product and Avatar as Elements once. Then every future shot pulls the lock. Re-roll any drifted face; never re-describe to fix drift.

**LAW 4: One swap does one thing.**
A garment swap that is asked to do too much fuses construction (it turned our two-piece into a one-piece) and approximates the print. Constrain hard: "keep image 1 exactly, change ONLY the suit to match image 2, keep it a two-piece." Swap the suit in one pass; place logos/cherry/dice as separate small overlays. Never let one generation re-author the whole garment.

**LAW 5: Never gamble exactness inside a generation.**
Freehand-prompting a print gets you paisley, mottle, or a plausible-but-wrong pattern every time. If the print has to be exact, it comes from the real product pixels (Virtual Try-On or Photoshop), human-gated, never from the model guessing. If a print can be approximate (background texture, a generic garment), prompting is fine. Know which lane the garment is in before you generate.

**LAW 6: Author the END frame. Never let i2v pick the endpoint.**
This is the single biggest defense against the "mid / slideshow of pretty near-stills" read that makes AI film look cheap (it is what made our cut feel like a slideshow). A single still handed to i2v with no end target defaults to a slow push-in, which is NOT a film shot. For every motion beat, author BOTH a start keyframe and an END keyframe (the action's resolved state), then generate start-to-end. The authored end forces a real change across the shot. Direct it by emotion and a physical action, not "she moves." And respect the real hit rate: AI motion lands roughly 1 in 60 to 100, so BATCH 8+ per beat and CULL hard. "Generate 2 or 3 and keep one" is how the slideshow problem sneaks back in.

**THE FAILURE MODES (name it, then fix it).**

| Failure mode (we hit it) | What happened | The fix |
|---|---|---|
| Freehand print prompting | Asked the model for the print in words. Got paisley/mottle, never the real stipple. | Print comes from real pixels: Virtual Try-On or Photoshop composite. Words only for approximate garments. |
| One swap doing too much | Single Nano Banana edit re-authored the whole suit; fused two-piece into one-piece. | One swap, one job. "Change ONLY the suit, keep it two-piece, keep everything else." Logos as separate overlays. |
| Gambling exactness in motion (THE WALL) | Tried to hold the exact print through Seedance/Kling. It drifted/melted. | Win exact on a still, animate subtly, keep print region static, detail beats stay near-still stills with a push. |
| Swimwear moderation flags | Seedance flagged rear/swimwear shots; Marketing Studio failed on swimwear. | Neutral wording, drop nano_banana_pro to non-pro then upscale, route to Kling 3.0 (different filter), or cover the beat with a push on an approved still. |
| Marketing Studio overriding the vibe | Marketing Studio force-converted our cinematic intent into a vertical UGC talking-testimonial on its own avatars. | Marketing Studio is a PRODUCT-FIDELITY test tool and a UGC ad maker, NOT a cinematic tool. For cinematic, use Cinema Studio + Soul. |
| Agentic-laziness / over-trust | Letting Supercomputer auto-run the whole thing in one prompt; garments drifted, no mid-run control. | Confirm-before-run for quality passes; storyboard gate; approve character sheets before any video. Auto-run is for the first throwaway pass only. |
| Slideshow / "mid" / two-day cycling | Handed single near-stills to i2v with no end target; got slow push-ins that read as a slideshow of pretty stills. | LAW 6: author START and END keyframes per beat; emotion + physical-action direction; batch 8+ and cull at ~1 in 60-100. Storyboard a real arc, not a gallery. |
| i2v wardrobe drift (swimwear) | A still that PASSED moderation drifted toward undressed/topless once animated. | Required i2v negative on every swimwear/lingerie beat: "stays fully dressed, top stays ON covering both cups, no wardrobe change, no undressing"; verify first/mid/last frames before keeping the take. |
| Plastic / clean-but-fake still | Animated a still that was composed well but read as AI (too clean, no skin texture). | Win-the-still includes the realism finish: degrade-and-rebuild (skin-texture restore + film grain 20-30 + micro-sharpen 5-10) BEFORE motion. A clean-but-plastic still is not an approved still. |
| Overstated motion print-hold | Believed "keep it near-static" guarantees the exact print survives motion. It does not. | Motion print-hold is UNPROVEN: verify every take's first/mid/last frames; default to the real cut-out PNG via Vibe Motion/AE for any prominent on-screen exact-product motion (LAW 2 escape). |

---

## 2. HIGGSFIELD FULL TOOL MAP

Every model/feature, what it does, when to reach for it, how to MAX it, and what it CANNOT do. Cross-checked against the 40 videos and our own runs.

### 2.1 Identity and character

**Soul (character model).** Train once on 20 to 31 reference photos (solid background, every angle: front, both sides, back of head; expressions: neutral, smile, serious, angry). Returns a reusable `reference_id`. It is the ONLY image model that supports character/avatar fields; switch to any other image model and the character fields disappear. MAX: train once, reuse forever, tag with @ in any Soul-capable prompt. CANNOT: be fixed by re-describing in a prompt; if it drifts, re-roll, do not argue with it. Our locked example: Soul "alma-lead-deadpan."

**Soul Cinema Studio (cinematic stills with the Soul).** Generate identity-faithful cinematic stills with the trained Soul. This is where your hero stills are born. MAX: pick the Soul, prompt the scene like a photographer (Section 4), generate 4, pick by eye. CANNOT: lock an exact product print on its own (that is Virtual Try-On or Photoshop).

**Soul Cast / Casting (structured character builder).** Genre + budget ($100M for premium feel) + era + archetype + outfit (Custom field) + physical details. Returns 4 character variants for ~0.5 credits AND a full character sheet. MAX: use the Casting panel instead of free-form prompting; set genre/budget first to set the production feel, then layer wardrobe and physical detail. The character sheet is the consistency anchor: attach it to every subsequent scene. CANNOT: replace a real-photo Soul if you need a specific real person.

**AI Influencer Studio.** Build a fully fictional photorealistic recurring character from parameter sliders (gender, age, ethnicity, face shape, eyes, hair, accessories, clothing). For fictional brand faces, not real-person continuity. Pin and rename so the same presenter persists across a campaign.

**Character sheet law (the single biggest consistency lever).** Build the full multi-angle sheet (front / three-quarter / profile / full body, or the Casting auto-sheet) FIRST, before any scene or video. Crop the FACE out of the wide shot for the face reference: full-body wide-shot faces render plasticky; an isolated face crop integrates far better.

### 2.2 Image models

**Nano Banana Pro (top photoreal still model, 1K/2K/4K).** Best current still detail. 2K is the sweet spot (not 1080p, not always 4K). MAX: batch 4 at 2K (~2 credits) to pick the winner cheaply; use for multi-image edits, reference-locked edits, garment swaps, multi-view product sheets, scene plates. The 2-image edit is our garment-swap workhorse: [pose still + real product photo] then "keep image 1, change ONLY the suit to match image 2." CANNOT: be trusted to render an exact print freehand; it approximates. Constrain hard. Aspect-ratio gotcha: the LAST image uploaded sets the output aspect ratio; order your inputs deliberately. Moderation can silently block; drop to non-pro then upscale.

**Nano Banana / Nano Banana 2 / 2.5.** Standard high-quality images; non-pro is the moderation-bypass tier for legit swimwear that pro false-flags (drop to non-pro, then 4K upscale). Moderation is on the still, not the i2v.

**Soul (image).** See 2.1. Required for any shot with your locked character.

**GPT Image 2.** Strong general text-to-image, title cards, end cards, storyboards, logos with legible text. The agent fires it autonomously inside Supercomputer for storyboards. Good when you need readable on-image text (a weakness of pure diffusion).

**Seedream / SeaDream 4.0 / 5.0.** Alternative image model, comparable to Nano Banana Pro for some looks. Test the same prompt across it when a Nano Banana result feels off.

**Shots app.** One image to 9 unique camera angles in a grid. Run a hero still through it BEFORE spending on video to get a free shot library, then upscale only the angles you keep (2 credits each).

**Popcorn app.** Upload 1 to 4 reference images, write 4 manual scene descriptions, get locked start-frames for each video beat. The fastest character-to-storyboard path.

**Skin Enhancer app.** Soft / realistic / imperfect skin (~4 credits). "Imperfect" reads more real. Note: output downloads locally, it does not save to the main library.

### 2.3 Video models (the only two that matter, plus context)

**Seedance 2.0 (best overall video, image-to-video).** Cinematic, UGC, product. 5 or 10s, up to 1080p, multi-shot in one run via the "shot switch" keyword, supports audio. Our default motion engine from an approved still. MAX: feed it an approved, gated still as the start frame; author subtle motion; for product hold the print region static. CANNOT: exceed ~15s per clip (a 30s request becomes two stitched 15s clips with consistency/voice drift); hold an exact print through heavy motion; reliably handle more than ~6 "shot switches" in one prompt (it stops generating after ~6). Swimwear/rear shots can moderation-flag; use neutral wording or route to Kling.

**Kling 3.0 (video, best subject consistency) + Kling 3.0 Motion Control.** Different moderation filter from Seedance, so it is the escape hatch when Seedance false-flags. Motion Control drives an AI character from a motion-library actor or a driving performance video and reaches ~17s, side-stepping the 15s cap. MAX: use Kling for subject-consistency-critical shots and as the moderation bypass; use Motion Control for longer continuous performance. CANNOT: still won't hold an exact print in heavy motion (THE WALL applies to all video models).

**VEO 3.1 (context only, available in platform).** Best dialogue/acting delivery and natural audio, but caps at 8s/clip. Reach for it only when a talking performance is the point.

**Sora 2 (context only).** Best physics, candid/viral TikTok realism. Niche.

**Reality check on the video models:** the interface (MCP, Supercomputer, Marketing Studio, Cinema Studio) does NOT change the quality ceiling. The ceiling is the underlying model (Seedance 2.0). Picking a fancier wrapper does not buy you a better frame; picking a better still as the start frame does.

### 2.4 The studios and orchestrators

**Cinema Studio (currently 2.x to 3.5, the cinematic environment).** The serious production environment. Image mode (Casting, Cinematic Locations, Scenes, real camera bodies + lenses + focal length + aperture), Video mode (start frame required, single-shot vs multi-shot, speed ramps, genre presets, emotion sliders), AI Director (paste your whole story, it returns a multi-clip shot list with per-shot camera body/lens/aperture/movement). MAX: lock the location FIRST, then characters; use AI Director for camera logic but write your own action prompts (its output is a starting point, not final); use the emotion slider to escalate across a sequence; chain clips by feeding the previous clip's last 5 seconds as a continuity reference. CANNOT: generate video from text only (start frame is mandatory); exceed 12s/clip in some versions. This is the right tool for cinematic vibe, the opposite of Marketing Studio.

**3D Scene tool (inside Cinema Studio).** Re-renders a still as a Gaussian splat you orbit to find the exact angle, then "capture shot" and generate at full quality. Kills the prompt-for-angle guessing game. The splat preview is intentionally low-res; judge only after capture.

**Marketing Studio (URL-to-ad, product-lock).** Paste a product URL (or upload up to 5 images), pick an avatar, pick a format (UGC, Tutorial, Unboxing, Product Review, Hyper Motion, Virtual Try-On, Wild Card, TV Spot). It auto-scrapes product images and composites them onto the avatar. This is the CLOSEST-to-exact product fidelity in the platform AND the fastest ad on-ramp. MAX: use it for product-fidelity tests and for genuine UGC/social ads; use Hyper Motion for pure product focus (no avatar); use Wild Card for impossible-to-shoot concepts. CANNOT: do cinematic. It force-converts to vertical UGC talking-testimonial on its own avatars and overrode our cinematic intent; it failed on swimwear moderation; avatar emotion is flat. For a film, do not use it.

**Virtual Try-On (the recommended EXACT-on-a-still path).** Put the exact real product on a person on a STILL. On a still, the product-lock is far more reliable than in motion. This is the web path to win LAW 2 without Photoshop. Do it on the web app. Clothing and dresses lock cleanly; bags can mislabel.

**Supercomputer (agentic orchestrator).** A cloud agent that chains research, brand, storyboard, stills, video, stitch, and 30+ connectors (Drive, Notion, Slack, Telegram). Routes between Claude/GPT/Gemini/Grok per task. Useful for: end-to-end research-to-ads pipelines, intro animations from one reference photo, motion-graphics B-roll packages, scheduled/async jobs delivered to Telegram or Drive. MAX: use Confirm-before-run + Sonnet for quality control; approve character sheets before video; store brand identity in long-term memory once; reuse assets by saying "reuse what can be reused." CANNOT: be trusted for precise creative tasks (reviewers found it often unusable for exact work; use direct Cinema Studio / Create Video instead); guarantee garment consistency in auto-run; it is a prototype/pitch engine, not a final-deliverable agency tool. Mode laws: Auto-run for throwaway first pass, Confirm-before-run for the real one. Opus burns the most text credits; default Sonnet.

**Canvas (node-based workflow builder).** Prompt node to Image node to Video node, saved as a reusable workflow you clone for batched catalogs. The recommended structure for repeatable production at scale.

### 2.5 Reference and asset systems

**Elements.** Register a character or product (2 to 3 images, ideally different angles on white background) as a reusable element. Tag with @ in prompts; max 3 elements per prompt. Assign emotion + intensity per element. White-background references are the single biggest quality lever for Elements. Our registered examples: "Alma Love Bikini FULL REF" (18 real photos), custom avatar "Alma Lead Deadpan."

**Mood Board.** Upload 20 to 30 same-style images (or pick a community preset) to set an aesthetic; combine with a Soul for style + identity together.

**Photo Dump.** Style preset + Soul to 15 images in one click.

### 2.6 Finishing and edit-adjacent

**Upscale (Topaz Labs, image 2x/4x/8x; Topaz Video to 2K/4K).** Finishing only. Adds resolution; does NOT rescue a bad source. For video, run Higgsfield's Sora 2 enhancer first to clean artifacts, then Topaz for resolution + 30fps. Upscale the FINAL stitched film once, not each clip (per-clip upscaling multiplies cost).

**Adobe Plugin (Premiere Pro + After Effects + Figma).** The same generate / reframe / remove-background / draw-to-edit / generate-image / upscale tools, inside your editor. Window > Extensions > Higgsfield. MAX: use it to kill the export/upload/wait/download loop; reframe for aspect conversion with subject tracking and no keyframing; the AI-transition recipe (screenshot last frame of clip A + first frame of clip B, generate a bridge). CANNOT: beat the model's quality ceiling; reframe/remove-bg results were "mixed" in independent testing, so verify before relying on them for a deliverable.

**MCP / CLI (Higgsfield in Claude Code).** Runs the same Higgsfield features from the terminal. Does NOT improve quality (same model ceiling). MAX: batch-generate, assemble, organize, preflight. CANNOT: be left on "always allow" safely (it can silently burn hundreds of dollars); always specify exact clip duration; NSFW rejections fail silently in MCP with no reason (go to the web video tab to see why).

**Reframe, Remove Background, Inpaint, Relight, Recast Studio, Change Voice, Translate, Vibe Motion.** Reframe = aspect conversion with tracking. Remove BG = no green screen. Inpaint = unreliable (a person-removal test produced a whole new scene; treat with suspicion). Relight = change mood/grade with no prompt, a post-generation pass. Recast = character/face swap in video (finishing). Change Voice / Translate = preserve lip-sync, genuinely useful. Vibe Motion = motion-graphics/explainer generator (logos, type, infographics, up to ~60s), NOT photoreal i2v: for a product that must be EXACT in motion, animate the real cut-out PNG via Vibe Motion / AE, never i2v-generate it.

### 2.7 The deprecated / avoid list (do not waste credits)
Sora 2 Trends (dead), UGC Factory (old VEO, deprecated), Animate / WAN 2.2 (dead; use Kling Motion Control), Draw to Video (broken), Mixed Media style-transfer (~$10/5s, low utility), Face Swap / Character Swap standalone (~4-year-old quality; use Create Image multi-reference instead), Edit Video / Kling 0.1 (3 to 10s only, inconsistent; edit in a real NLE).

---

## 3. THE MAX PIPELINE (end to end)

This is the spine. Every serious job walks these stages in order. Each stage has its tool and its GATE. You do not advance until the gate passes. This is exactly the structure that made the Alma exact-product SOP can't-fail; it generalizes.

**Stage 0: Story and board (before any generation).**
- Tool: write the five-line core (Situation / Desire / Conflict / Change / Result, from the harvest), then a still storyboard.
- GATE: every planned beat maps to one of the five lines; if it does not, cut it. Log-line first. No generation spend until the board exists.

**Stage 1: Character (lock once, reuse forever).**
- Tool: Soul (real person) or Soul Cast / AI Influencer (fictional). Build the multi-angle character sheet. Crop the face out of the wide shot for the face reference.
- GATE: the sheet holds identity across all angles. Save the `reference_id`. Never retrain mid-project.

**Stage 2: The shot still (cinematic, character-correct, product can be wrong here).**
- Tool: Soul Cinema Studio (or Cinema Studio Scenes: lock LOCATION first, then drop the character). Generate 4, pick by eye. Use Shots app or the 3x3 Contact Sheet mega-prompt for free coverage; use the 3D Scene tool to find the exact angle.
- REALISM FINISH (blocking, part of "win the still"): run the chosen still through the degrade-and-rebuild pass before it counts as approved: skin-texture restore (Skin Enhancer "imperfect", or a manual pass) + film grain 20 to 30 + micro-sharpen 5 to 10. A clean-but-plastic still reads as AI the instant it moves. "Win the still" means win the REALISM, not just the composition.
- GATE: composition + character + lighting are right AND the still passes the realism finish (no plastic skin, has grain). The product/garment does not have to be right yet.

**Stage 3: The EXACT product on the still (the make-or-break stage, LAW 2 + LAW 4).**
Pick ONE path, in this order:
- 3a. Virtual Try-On (web): the still + the registered real product. Most reliable web path. Output a fitted still.
- 3b. Nano Banana Pro 2-image edit: [the still + the real product photo], "keep image 1 exactly, change ONLY the suit to match image 2, keep the construction (two-piece), change nothing else." Place logos/cherry/dice as separate small overlays in follow-up passes.
- 3c. Photoshop (guaranteed exact): mask the garment, place the real print swatch, Transform > Warp to follow the body, set the print layer to Multiply/Overlay so folds and shadows show through, drop opacity to taste, overlay the real logo/cherry/dice. This is pixel-exact because it is the real fabric pixels.
- HARD GATE (never skip): put the still next to the real product photos (front / detail / back). Two-piece? exact stipple, not paisley? logo in the right place? nothing added that shouldn't be there? If any check fails, FIX IT HERE on the still. A wrong product never advances into motion.

**Stage 4: Motion from the approved still (authored start-to-end, print-safe).**
- ROUTE FIRST (LAW 2 inverse law): is the exact product prominent and on screen during this beat's motion? If YES, do NOT i2v it: animate the real cut-out PNG over the plate via Vibe Motion / After Effects (pixel-exact). Only if the product is concealed, small, or not the subject do you use i2v.
- Tool (i2v path): Seedance 2.0 (default) or Kling 3.0 (consistency / moderation escape) with the approved exact still as the START frame AND an authored END keyframe (the action resolved), per LAW 6. Direct by emotion + a specific physical action, never "she moves." Keep torso/print near-static.
- REQUIRED SWIMWEAR/LINGERIE NEGATIVE (every such beat): "stays fully dressed, the top stays ON covering both cups, no wardrobe change, no undressing." A still that passed moderation can still drift undressed once animated.
- BATCH, do not dabble: AI motion lands ~1 in 60 to 100. Generate 8+ takes per beat and CULL hard. "2 or 3 takes" reimports the slideshow problem. Use the previous clip's last frames as a continuity reference to chain shots.
- GATE: whole-watch each kept take end to end AND check its FIRST, MID, and LAST frame for print drift and wardrobe drift. Product still reads as the real thing on all three? No melt, no undress? Keep or re-roll. Use the whole-watch / Gemini hostile-review lane for serious cuts. No self-crowning.

**Stage 5: Product-detail "buy it" beats (exact, moving, near-still).**
- Tool: the Stage 3 exact still + a slow Ken Burns push only (in AE/Premiere/Resolve, or Cinema Studio camera-move-only with empty prompt). Do NOT heavily animate the print. Intercut these pixel-exact detail beats with the Stage 4 AI-motion wides.
- GATE: the push reveals the real product detail with zero drift (it can't drift, it's a real still).

**Stage 6: Assemble + grade + sound.**
- Tool: Premiere/Resolve/CapCut (real NLE, not Higgsfield's Edit Video). One warm master grade (LUT or Lumetri). Diegetic sound + an owned music bed (Suno for owned music). Add film grain for perceived realism. Chain clips that share continuity references so editing is minimal.
- GATE: the cut reads as one piece (uniform resolution, one grade).

**Stage 7: Finish.**
- Tool: Topaz (Sora 2 enhancer first, then Topaz to 2K/4K + 30fps), upscale the FINAL stitched film once.
- GATE: platform masters pass; whole-watch with your eye and the client's eye; adversarial verify before crowning.

---

## 4. PROMPTING PLAYBOOK

The grammar that separates professional output from generic AI. Pulled from the Cannes feature production (108,859 generations) and the cinematographer/creator videos.

### 4.1 Core structures

**Image-to-video minimal prompt (when the still IS the start frame):** describe ONLY camera movement + camera type + character action + audio. Do NOT re-describe the character or setting (the image already defines them). Example: "Shallow depth of field, handheld, the woman attentively listens, no dialogue, beach ambient sound."

**Text-to-video 5-element formula (when you have no start frame):** character + setting + lighting + action + dialogue. But prefer image-to-video for anything serious; text-to-video gives zero control over design or framing.

**Photographer-language image prompt (the realism unlock).** Do NOT write "photorealistic, cinematic, high quality." DO name: camera body + lens + aperture (stopped ~2 from wide open) + grain/film stock + halation/bokeh + a three-quarter angle (beats front-facing) + practical light only + a specific light-spill description. Set camera/lens in the Cinematic Cameras UI rather than in text when possible.

**One shot = one idea.** One main idea + one main action + one main camera strategy per generation. Density beats vagueness: the more you specify when to cut, which angle, who to cut to, the less room the model has to hallucinate.

**Emotional-scene prompting.** Add situational context + anatomical behavior. Weak: "she watches him leave." Strong: name the physical anatomy: "right arm extended, fingers spread, jaw dropped, teeth visible, no tears, lands on hands and knees."

### 4.2 Hard negatives (the AI tells to kill)
- "no text on clothing" and "solid [color] hat" (AI-text on garments/hats is the #1 tell).
- "no dialogue" + a specific ambient descriptor on audio-capable models (Seedance/Kling/VEO invent random dialogue if the audio field is empty). Never leave audio undirected.
- Hard-negative ALL signage/text in the scene (fake "Beverly Books" style signage is a top realism-killer).
- "looking at the camera" only if you want it; omitting it causes off-camera gaze.
- For vehicles: "this is the front of the car, keep this exact angle" or it may drive backwards.
- For swimwear/lingerie i2v: "stays fully dressed, top stays ON covering both cups, no wardrobe change, no undressing" (a moderation-passed still can drift undressed in motion; this is mandatory, not optional).

### 4.3 Consistency and motion hacks
- The word "slowly" / "carefully" is a consistency hack: slow motion renders more faithfully, less warping. Generate slow, speed-ramp later in the NLE.
- Repeat key camera constraints at BOTH the start and end of the prompt ("static camera ... static camera"); the model weights the ends.
- Reduce subjects per shot; frame characters large. Crowds with many small faces deform heavily.
- Spell complex names phonetically for dialogue.
- Wrap spoken lines in quotation marks so the model treats them as dialogue, not action.
- Use a frame coordinate system for placement ("20% X, 30% Y"); ask an LLM to draw a top-down scene map and extract the XY prefix.
- Every location needs one landmark anchor object; reference it to place characters ("to the left of the tree"). Never generate location refs straight front-on; use three-quarters or a corner/CCTV angle for depth. Split front and back location views into two images so the model doesn't grab the wrong one.

### 4.4 The reusable mega-prompts (paste-ready, attach a reference in the UI)

**3x3 Cinematic Contact Sheet (9 angles of one locked subject in one generation):**
```
Analyze the entire movie scene. Identify ALL key subjects present and their spatial relationship. Generate a cohesive 3x3 grid Cinematic Contact Sheet of 9 distinct camera shots of exactly these subjects in the same environment:
Row 1 (Establishing): 1. Extreme Long Shot. 2. Long Shot (head-to-toe). 3. Medium Long Shot (knees up / 3-quarter of object).
Row 2 (Core Coverage): 4. Medium Shot (waist up). 5. Medium Close-Up (chest up). 6. Close-Up (tight on face / front of object).
Row 3 (Details and Angles): 7. Extreme Close-Up (macro on a key feature). 8. Low Angle / Worm's Eye. 9. High Angle / Bird's Eye.
Strict consistency: same people/objects, same clothes, same lighting across all 9. DOF shifts realistically (bokeh in close-ups). Photorealistic textures, consistent cinematic color grade.
```

**9-Scene Sequence (one-line idea to a 9-beat storyboard, consistent subject):**
```
Analyze the input image and identify the main subject(s). Maintain perfect consistency in appearance, proportions, materials, colors, style across all frames. Read the SCENE INPUT and generate a cinematic 9-scene sequence that progresses logically start to finish; each frame is the next meaningful moment. The AI chooses all camera angles. Cinematic lighting, consistent grade, realistic DOF, coherent environmental evolution. No repeated shots.
SCENE INPUT: <one-line scene description>
Frame 1: / Frame 2: / ... / Frame 9:
```

**Garment-exact 2-image edit (Nano Banana Pro, LAW 4):**
```
Keep image 1 exactly as it is: same person, same pose, same face, same background, same lighting. Change ONLY the swimsuit to match image 2. Keep the construction a two-piece. Do not add jewelry or any item not in image 2. Match the print, color, and cut of image 2 precisely.
```

**Color discipline (apply at image generation):** 60/30/10 rule. 60% dominant color, 30% secondary, 10% accent. State it in the prompt or enforce in grade.

### 4.5 Use an LLM as your prompt engineer
Expand a one-line scene idea into a detailed keyframe prompt with Claude before spending a credit ("Give me a detailed keyframe-generation prompt for: [plain scene]"). When a prompt grows long and contradictory, tell Claude to "optimize, study context, and sanitize the prompt." Update only the changed shot in a long shot list rather than re-rendering the whole list. This is standard 2026 workflow.

---

## 5. MODERATION + GOTCHAS + COST DISCIPLINE

### 5.1 Moderation (and the bypasses, for legitimate content)
- Seedance false-flags tender/elderly close-ups and words like "intimate / tender / her face," and flags swimwear/rear shots. Marketing Studio failed on swimwear outright.
- Bypasses for legit content: neutral wording; drop nano_banana_pro to non-pro then 4K upscale (moderation is on the still, not the i2v); route the shot to Kling 3.0 (different filter); or cover the beat with a slow push on an approved still.
- In MCP, NSFW rejections fail SILENTLY with no reason. If an MCP job vanishes, open the web video tab to read the rejection.
- Moderation is reportedly stricter in Western markets; it is provider-side (the model maker), not Higgsfield's choice.

### 5.2 Gotchas (the ones that cost credits or time)
- Cinema Studio video needs a start-frame image; text-only errors out.
- Clip caps: Seedance ~15s, Cinema Studio ~12s, VEO ~8s. A 30s request becomes stitched 15s clips with drift. Use Kling Motion Control (~17s) to break the cap for continuous performance.
- "Shot switch" in Seedance handles ~6 cuts max before it stops generating later shots.
- Nano Banana: the LAST uploaded image sets the output aspect ratio; context drifts within a long session (start a NEW chat rather than correcting in place); downloads degrade dimensions.
- Upscale never rescues a bad source; it only adds resolution.
- Skin Enhancer output does not save to the library (downloads locally).
- Marketing Studio: avatar emotion is flat; complex products (drones) fail where simple consumer products work; product names can mislabel; default is 9:16 vertical UGC.
- Lens selection in Cinema Studio is mandatory before generating (a missing anamorphic selection caused circular artifacts). DOF is set by sensor/camera-body choice, not by a separate aperture control in some versions.

### 5.3 Cost discipline (Ultra plan, but spend like it's yours)
1. Preflight EVERY batch with `get_cost:true` (MCP) before spending.
2. Stills before motion: a bad concept is 2 credits to catch on a still, not 90 in motion.
3. Draft at 720p; upscale once at the end on the stitched file (can save ~half the credits). Cinema Studio sometimes costs the same at 720p and 1080p, so confirm a good prompt at the cheap tier first.
4. Batch images 4-at-a-time (~2 credits) to pick a winner; do not generate 1 at a time.
5. Casting characters (~0.5 credits for 4 + a sheet) beat Nano Banana (~2 to 4 credits/image) for character creation.
6. Use the grid / Contact Sheet for coverage: 9 images for roughly one single-shot's cost.
7. Do NOT re-roll what a 2-minute manual fix solves (a Photoshop print fix beats ten motion re-rolls).
8. Reference cost anchors: GPT Image 2 still ~7 credits; Seedance 10s 1080p ~90 credits; full cinematic commercial (our Alma-class build) ~5,400 credits / ~6 hours, versus a ~$300K agency quote. An hour of finished Cinema Studio footage runs into the thousands of dollars after retakes; budget per usable clip, not per generation.
9. Never set MCP "always allow"; always specify exact clip duration in the MCP call.

---

## 6. CLAUDE CODE (terminal) vs WEB APP vs PHOTOSHOP

The honest division. You asked plainly whether you're using Higgsfield the max way; here is the plain map. The mistake to avoid is trying to do visual-judgment work in the terminal and trying to do batch/assemble work by hand on the web. Match the work to the surface.

**Claude Code / MCP (the terminal). Use for the repeatable, mechanical, batchable.**
- Batch-generate stills and clips from a locked board (after the board is approved on the web).
- Preflight cost (`get_cost`), check balance, organize and rename outputs, wrangle files.
- Assemble: drive Premiere/AE via their MCPs, build the cut, apply the LUT, render.
- Produce the proof pack / receipts.
- NOT for: visual selection, exact product work, anything where you need to SEE and re-roll instantly. Do not leave it on always-allow. Always state exact durations.

**Higgsfield WEB APP (the browser). Use for visual judgment and the modes that need your eye.**
- Train/manage the Soul, register Elements (Product, Avatar).
- Virtual Try-On (the exact-on-a-still path) — do this here, by hand.
- Soul Cinema Studio / Cinema Studio still selection — generate 4, pick by eye, re-roll on sight.
- Marketing Studio modes (product-fidelity tests, UGC ads) — these are visual, mode-driven, web-native.
- The 3D Scene angle-finder, Shots app angle picking, picking takes.
- This is where judgment lives. If you have been driving these from the terminal, that is the part that feels not-max. Move judgment to the web.

**PHOTOSHOP (the exact-print guarantee). Use for the one thing AI cannot do.**
- The guaranteed pixel-exact product print composite on hero + product-detail stills (mask, real swatch, Warp, Multiply/Overlay, real logo overlays).
- Clean plates (Generative Fill, blank prompt) for object removal.
- Any time the print MUST be exact and Virtual Try-On drifts it. This is the floor under LAW 2.

**The one-line rule:** Web app = SEE and choose and try-on. Photoshop = make it exactly real. Claude Code = do it many times, assemble it, prove it. The character Soul, the registered Product, and the Elements are the locks you build once on the web that make the terminal batches cheap and consistent forever.

---

## 7. WHAT THE 40 VIDEOS ADD

The genuinely new, worth-adopting techniques, grouped by theme. (The pure-AE, pure-editing-career, and commercial-compilation videos contributed craft laws, not Higgsfield mechanics; they are folded into the relevant themes below.)

### 7.1 Consistency engineering (the biggest cluster)
- **Character sheet beats face-only.** Front/side/back full sheet gives the model complete identity data; that is why Cinema Studio holds character across shots. Crop the face out of the wide shot for the face reference (wide-shot faces render plasticky).
- **Chain AI outputs, not real photos.** Once you have a good AI image of your character, swap it in as the reference and drop the original real photo. That AI image is the anchor for all future shots.
- **Separate environment from character.** Build a library of environment images first, then composite characters into them with Nano Banana Pro. Consistent world across unlimited shots.
- **Continuity bridge.** Feed the previous clip's last ~5 seconds as a reference for the next clip; seamless continuation, no jump cut. The new scene-by-scene workflow replaces explicit start/end keyframes: upload the previous video as context for the next prompt.
- **Track every character STATE** (injuries, clothing, props, transformation stage) in a sheet before generating. At feature length this script-supervising is mandatory; assets must be labeled in a Canvas or you will grab the wrong skin.

### 7.2 The realism playbook (hyperrealism pipeline)
- **Win the still first (GIGO).** i2v quality is capped by the input still. Nano Banana Pro at 2K is the reference frame.
- **The full hyperreal chain:** consistent images (Nano Banana) to motion (Kling/Seedance) to face fidelity (a trained-subject inpaint) to post (skin/detail enhancers) to grade + film grain in Resolve.
- **Unexpected angles read as authentic;** front-on/expected angles trigger the AI tell. Reference prep (wardrobe, posing, makeup, environments, lighting, props) is ~90% of success.
- **Reference preparation is the work.** Collect references before generating a single frame.

### 7.3 The first-frame / last-frame and keyframe craft (Cinema Studio depth)
- **Author both endpoints.** The start-frame + last-frame method is the primary motion-control lever: author both states rather than letting the model decide the endpoint. The authored END keyframe defeats the i2v push-in default.
- **Start/end for in-camera effects:** generate the "before" state as start frame and the "after" state (e.g. laser reveal) as end frame; let the model animate the transition.
- **Camera-reset trick:** end frame of a generation as the first frame of the next, with the original character still as the end frame, to snap framing back without a cut (the "repeat disturbance" beat).
- **Composite the action AI can't nail:** if the model can't tap a specific icon or hold a prop right, screen-grab a good frame, cut the hand/prop in Photoshop, composite it onto your keyframe, then let the video interpolate from it.
- **Lock the environment plate BEFORE the character;** every downstream scene inherits it. Lens selection is mandatory (missing it caused circular artifacts).

### 7.4 Cameras and lenses (cinematographer intel)
- Two axes decide every body: sensor size (controls DOF range) and film-vs-digital (controls grain/emulation). Decide those two first, then pick a body.
- Top film look: IMAX or Arri SR body + Panavision C Series lens (the Rogue One / Star Wars aesthetic). Canon K35 is the highest-impact lens for backlit emotional shots. Clean baseline: Zeiss Ultra Prime / Cooke S4 / Arri Signature Prime (near-identical in AI). Anamorphic character: Panavision C Series or Hawk V-Lite.
- Test bokeh-differentiating lenses against foliage/lights, never flat backgrounds. The visual selection UI beats text for camera choice. Lens Baby tilt-shift is not implemented in AI; do that in post.

### 7.5 Agentic orchestration (Supercomputer, used correctly)
- Highest-value Supercomputer uses: intro animation from one reference photo; motion-graphics B-roll packages from a script (hook card, clarity card); research-to-ads pipelines; scheduled async jobs to Telegram/Drive.
- Mode laws: Auto-run for the throwaway first pass, Confirm-before-run for the quality pass; default Sonnet, Opus only for the hardest creative narrative; store brand identity in long-term memory once; say "reuse what can be reused" to regenerate only drifted clips; paste the product URL (it scrapes real images).
- It still makes per-asset mistakes; retry the failing asset conversationally. It is a prototype/pitch engine, not a final-deliverable tool. For precise creative work, use direct Cinema Studio.

### 7.6 Marketing Studio reality (when it IS the right tool)
- It is the fastest URL-to-ad on-ramp and the closest product fidelity in the platform: paste URL, pick avatar, pick format, generate. Hyper Motion for pure product focus (no avatar). Wild Card for impossible-to-shoot concepts. Pin/rename Soul 2.0 avatars for campaign continuity.
- It is NOT cinematic and it overrode our cinematic intent; avatar emotion is flat; it failed on swimwear. Use it for UGC/social and fidelity tests, never for a film.

### 7.7 The new infrastructure (Higgsfield inside your tools)
- Adobe Plugin (Premiere/AE/Figma) + MCP (Claude Code) put generate / reframe / remove-bg / draw-to-edit / upscale where you already work, killing the export/upload/wait/download loop. Reframe (subject-tracked aspect conversion, no keyframing) and the AI-transition recipe (last-frame + first-frame to a bridge clip) are the standout time-savers. The interface never beats the model's quality ceiling; verify reframe/remove-bg results before shipping them.

### 7.8 Editing and story craft (from the AE/editing/commercial videos)
- **Story first, five lines before any production:** Situation / Desire / Conflict / Change / Result. Validate every cut against the five lines; cut anything that doesn't map.
- **Sell the feeling, not the product** (luxury-ad logic): structure around desire and mystery; the product is secondary to the emotion.
- **Shot-sequence hook:** multiple clips of one action, equal-length cuts, motion-matched stitching, doubles as opening hook and story engine. Cut scene changes on the music's waveform dips; pick music before you generate so your pacing matches BPM.
- **AE finishing that lifts AI footage:** Force Motion Blur on pre-rendered clips; Lumetri (the only color tool you need) with an S-curve for contrast; Noise ~8% + Posterize Time (6 to 12fps) on an adjustment layer for analog feel; film grain via Screen-blend texture + Curves; F9 Easy Ease on every keyframe; null-stacked cameras for continuous multi-scene moves. Film grain in Resolve/AE is the single cheapest realism upgrade.
- **AI compositing in AE:** roto the live subject and overlap the AI clip by a few frames (not a hard cut) for a cohesive blend; Firefly image-to-video does not default to 1080p (set resolution to match source) and needs a color-match pass.
- **HyperFrames (Claude Code + motion graphics)** is the strongest motion-graphics-on-talking-head path: instruct in plain language ("make this title harder," "turn this into 3 animated points") and it keyframes automatically. These tools make B-roll and assets that go INTO your edit; they do not replace the NLE for pacing, structure, and sound.

---

## 8. PRE-FLIGHT CHECKLIST (run this BEFORE you spend a credit)

The reason we looped for two days: hostile-review findings never got written back into a checklist, so the same failures kept happening. This section closes that loop. Copy it into the job folder and tick every box before generating. If you cannot tick a box, you are not ready to spend.

**Before Stage 2 (stills):**
- [ ] Story locked: five lines (Situation/Desire/Conflict/Change/Result) and every beat maps to one. (Stage 0)
- [ ] Character locked once as a Soul/Element; face cropped from a wide shot for the face ref. (LAW 3)
- [ ] I know, per beat, whether the garment/product must be EXACT or can be approximate. (LAW 5)

**Before Stage 3 (exact product):**
- [ ] Real product reference is registered (Product/Elements) and the real photos are open beside me to gate against.
- [ ] Exact path chosen: Virtual Try-On first, Nano Banana 2-image second, Photoshop guaranteed-exact third. (Stage 3)
- [ ] One swap does one job; logos/cherry/dice are separate overlays. (LAW 4)

**Before Stage 4 (motion) - the stage that bit us hardest:**
- [ ] Still passed the HARD product gate against the real photos (two-piece? exact stipple not paisley? logo placed right? nothing added?). A wrong product NEVER advances. (Stage 3 gate)
- [ ] Still passed the REALISM finish (skin texture, grain 20-30, micro-sharpen 5-10). No plastic still advances. (Stage 2)
- [ ] I ROUTED the beat: product prominent + on screen while moving = real-PNG via Vibe Motion/AE, NOT i2v. (LAW 2 inverse)
- [ ] If i2v: I authored a START and an END keyframe, directed by emotion + physical action. (LAW 6)
- [ ] Swimwear/lingerie beat has the wardrobe-drift negative in the prompt. (Stage 4)
- [ ] I am batching 8+ and culling, not generating 2-3. (LAW 6)
- [ ] Per kept take I will verify FIRST, MID, LAST frames for print drift AND wardrobe drift. (Stage 4 gate)

**Before crowning / sending:**
- [ ] Whole-watched end to end (no 3-frame judgments).
- [ ] Ran the adversarial/second-model hostile review; no self-crown.
- [ ] Any new failure found is written back into the changelog AND the relevant law/stage (close the loop).
- [ ] send_no_send is an explicit operator decision, not assumed.

---

End of playbook. The shortest version of all of it: lock the character once, win the product exact on a still, finish the still for realism, gate it against the real photos, route exact-product-in-motion to a real PNG (not i2v), author the END frame and batch-and-cull, verify first/mid/last for print and wardrobe drift, prove it before you crown it, and do the seeing on the web, the exact-print in Photoshop, the batching in the terminal.

---

## APPENDIX: The 40 source videos (operator-posted, whole-read)

Grouped drops: 1 = Higgsfield/Supercomputer (17), 2 = untagged (3), 3 = After Effects (6), 4 = untagged (11), 5 = best commercial ever (3). Full per-video knowledge extraction lives in the workflow output (wf wrgr2sh09).

- https://youtu.be/kNradaMZ8kk — How to Use Higgsfield AI Like a PRO - AI Marketing Workflow
  End-to-end AI marketing campaign production using Higgsfield Supercomputer: one prompt dri
- https://youtu.be/4mT8s_09DRM — The Only AI Tool You Need in 2026!
  Higgsfield Supercomputer: a cloud-native self-learning agent with 40+ tools that autonomou
- https://youtu.be/qyGXb6HEnCM — Higgsfield's New Supercomputer is AMAZING for Creators
  5 creator workflows unlocked by Higgsfield Supercomputer: an agentic hub that routes betwe
- https://youtu.be/LD7GPdMMjQA — How to Use Higgsfield Supercomputer Better than 99% of People
  Complete walkthrough of Higgsfield Supercomputer: setup, AI skills, Soul ID characters, me
- https://youtu.be/p_oWkEz8sn8 — I Made a Cinema-Grade AI Ad in 5 Hours | Higgsfield Cinema Studio
  End-to-end Cinema Studio 2 workflow for producing a cinematic AI ad: scene/environment ite
- https://youtu.be/Y59LwQNmRJY — Filmmakers Are About to Panic When They See This
  Full walkthrough of Higgsfield Deep Field Cinema Studio 3.0: character building, scene ass
- https://youtu.be/CM35zHjdlGM — Higgsfield Just Released Cinema 2.0 & It's a Game Changer
  Full walkthrough of Higgsfield Cinema Studio 2.0 new features: 3D Scene tool, grid image g
- https://youtu.be/o1RbyGgg-2I — How to Get 100% Out of Higgsfield Cinema Studio 3.5
  End-to-end workflow for building a multi-clip cinematic short inside Higgsfield Cinema Stu
- https://youtu.be/l-rFCkjJzu8 — Higgsfield AI Ultimate Tutorial — EVERY Feature Explained & Reviewed
  Comprehensive walkthrough of every Higgsfield AI feature across image, video, and audio ta
- https://youtu.be/vrN-DSRJSYk — Higgsfield Cinema Studio "Cameras and Lenses" Explained
  Deep-dive from a working cinematographer (10 years live-action) on every camera body and l
- https://youtu.be/qsgDMygRTto — Higgsfield Supercomputer ULTIMATE Tutorial (AI Films, Ads & Automation
  End-to-end walkthrough of Higgsfield Supercomputer: an agentic cloud AI that orchestrates 
- https://youtu.be/6aJ2BneDB5M — How to Make Ultra Realistic AI Videos (28 Best Tips)
  28 pro tips from Higgsfield's Cannes AI feature film (Hell Grind) production covering prom
- https://youtu.be/cksEVv1tArI — Higgsfield AI Ultimate Tutorial (2026)
  Beginner-to-intermediate walkthrough of the full Higgsfield platform: pricing, apps, chara
- https://youtu.be/YLocNj8bbQw — Higgsfield Masterclass Part 1 (AI Cinematography: Scene Stacking to Fi [no transcript]
  A to Z Higgsfield platform walkthrough (Part 1 of 3): scene stacking concept, core feature
- https://youtu.be/AD3lDZS8OL8 — Higgsfield Marketing Studio Review
  A live walkthrough review of Higgsfield's Marketing Studio, demonstrating UGC ads, tutoria
- https://youtu.be/YvznY2cH3TY — Guía Completa: Cómo Hacer Tu Primer Comercial con IA | Higgsfield Mark [no transcript]
  Step-by-step walkthrough for creating your first AI video commercial using Higgsfield Mark
- https://youtu.be/em66Mvt8QLc — A $350,000 AI AD Using Only 1 Tool (2026)
  5-step workflow for making a full cinematic perfume commercial using Higgsfield Cinema Stu
- https://youtu.be/q2FXnNbcrks — What I Wish I Knew Before Buying Higgsfield AI
  Beginner orientation to Higgsfield: the two core workflows (image and video generation), C
- https://youtu.be/W0s_SNmHQcs — I Bought Every Higgsfield Plan So You Don't Have To
  A real-workflow credit-cost breakdown of all four Higgsfield paid tiers (Starter, Plus, Ul
- https://youtu.be/sXgWhKwiUdc — I Created a $1,000,000 Brand Using AI
  End-to-end AI brand building for a clothing brand: logo + product design to full ad suite 
- https://youtu.be/hb2bbfiNBXA — Learn After Effects in 10 Minutes! Beginner Tutorial
  A 10-minute beginner crash course in Adobe After Effects covering the core UI, keyframe an
- https://youtu.be/jFbRZZmMW7c — I'll Teach You After Effects in 60 Minutes...
  Beginner After Effects crash course: composition setup, keyframe animation, track mattes, 
- https://youtu.be/J9bAd28DzTU — Top 20 Best Effects in After Effects
  A ranked overview of the 20 most useful native After Effects effects for motion graphics a
- https://youtu.be/JZGqZWDSVPg — AI Compositing Tutorial in After Effects (Firefly and Runway)
  Three workflows for combining AI-generated video with real live-action footage inside Afte
- https://youtu.be/9os35azf4Jw — How to Start Making AI Videos in 2026 (FULL Guide)
  A full beginner-to-intermediate guide to AI video production organized around three core f
- https://youtu.be/UVrkLPlp83M — Higgsfield AI Just Changed Video Editing Forever! (Now Inside Adobe Pr
  Tutorial showing how to install and use the Higgsfield AI plugin inside Adobe Premiere Pro
- https://youtu.be/9-iSl83dF34 — I Tried AI Video Editing for 8 Days - Here's what DOES work
  8-day test of AI video editing tools: Higgsfield Plugin + Supercomputer, HyperFrames (Clau
- https://youtu.be/954L0eVIdaE — How I Would Learn Video Editing (If I Could Start Over)
  General video editing career roadmap for beginners and intermediate editors: mindset, soft
- https://youtu.be/pdLEHfkwgV8 — The Power of SIMPLE Editing
  Three-part cinematic editing framework for YouTube/content videos: shot sequence, sound de
- https://youtu.be/O0qkkexHqZw — Give me 11min, and i'll improve your editing skills by 176%
  General YouTube video editing philosophy: editing as psychological mind control (attention
- https://youtu.be/O6HOYu_ZEnw — The Complete Guide to Editing like Iman Gadzhi in 2026! (Masterclass)
  After Effects long-form YouTube editing masterclass replicating Iman Gadzhi's design syste
- https://youtu.be/Vl3tFo8Dgvg — Storyboarding for Video Editors (Full Masterclass) [no transcript]
  Full masterclass on the storyboarding process for video editors: from idea to concept to d
- https://youtu.be/NeTJRCycYXQ — The ONLY 5 Lines You Need To Tell Any Story
  A storytelling framework for filmmakers and YouTubers: write exactly five lines (Situation
- https://youtu.be/OImchUDrXsA — If I Were Starting A Video Production Company In 2025, This is What I'
  7-step business framework for starting and growing a video production company: prospect ou
- https://youtu.be/bgU-8newThM — 3 Steps of Video Production
  A ~1.5-minute promotional video by South Florida Video Productions explaining the three st
- https://youtu.be/H2wv0Sog0jo — HYPERREALISM IN AI VIDEOS EXPLAINED | COMPLETE TUTORIAL
  End-to-end hyperrealism pipeline for AI video: consistent image generation, face-swap, ima
- https://youtu.be/-578C3gFepU — Storyboarding - Tomorrow's Filmmakers
  Traditional storyboarding fundamentals for filmmakers: how to draw, structure, and use sto
- https://youtu.be/HSRieuzms24 — World's Funniest Commercials of All Time | Series-1
  A compilation of classic funny TV commercials (Doritos, HSBC, Chicken of the Sea, and othe
- https://youtu.be/K9vFWA1rnWc — Best Advertisement ever-Winner of Best Ad 2014 [no transcript]
  Inspirational advertisement video from 2014 - not a Higgsfield or AI film production tutor
- https://youtu.be/bIRa63nR2mU — Top 10 Most Creative TV Commercials Compilation #1 [no transcript]
  A compilation of 10 traditional live-action TV commercials (Skittles, Doritos, Mercedes, B