# OS HIGGSFIELD PRODUCTION DOCTRINE (adopted 2026-06-08)

Status: **LOCKED STANDARD. Auto-applies to every AI image/video generation task.** This is not a doc to "post," it is the operating system for how SNIPED builds AI image and video. Source: the "HIGGSFIELD OG MUST USE" doctrine (Joey's system) + the two installed skills + hard-won notes from the Synergy "The Door" build. Composes with [[premium-stack-maximization-law]] and `os-face-lock`.

## The core thesis (why this exists)
One-off prompts waste credits and drift identity. "Every tool is a fresh argument; every chat is a new thing." The fix is a **repeatable system**: locked grammar for building scenes, building characters, putting characters in scenes, and building multi-shot videos with the characters held consistent. We never freehand a Higgsfield prompt again when a skill covers it.

## The adopted system = two skills (route through these, do not freehand)
1. **`banana-pro-director`** = the IMAGE asset builder (Higgsfield Banana Pro / Soul Cinema / GPT-2). Strict order:
   (1) single-image character outfit on white seamless = the locked base reference → (2) 6-panel multi-angle character sheet off that base → (3) scene plates (with or without characters). Locked hyperreal stack (pores, subsurface scattering, strand hair, fabric weave, Kodak Vision3). GPT-2 for face/chest-up detail.
2. **`cinema-worldbuilder`** = the SEEDANCE VIDEO director. Character gate first, then pick one of 5 cinema modes (Narrative / Studio-Editorial / Action / Performance / Atmospheric), each with locked camera/lens/movement/grade, **diegetic audio only (never music/lyrics in the prompt)**, pre-prompt 5-line confirmation, runtime baked in.

**The loop:** build/lock character (banana-pro-director) → generate scene/coverage stills → animate with cinema-worldbuilder Seedance prompts, attaching the locked refs in the Higgsfield UI. Text prompt and image reference are separate; image attachment happens in Higgsfield, never inside the prompt text.

## The credit-efficiency law (proven on Synergy "The Door")
1. **Stills before motion, always.** Identity-locked stills are cheap (nano_banana_pro ~2 credits) and controllable. Video is expensive (Seedance 720p ~22.5cr/5s, 1080p ~45cr/5s). Generate the exact frame as a still first, QA it, then animate ONLY approved frames. A bad concept costs 2 credits to catch, not 22.
2. **Preflight every spend.** Use `get_cost:true` before any batch.
3. **Lock identity once, reuse the reference everywhere.** Pass the locked still as `medias` role `image` (stills) / `start_image` (video). Re-roll any drifted face.
4. **Uniform resolution per film** so shots read as one piece; upscale at export rather than mixing tiers.
5. **Storyboard-gate before the big spend.** Build the full still storyboard, get sign-off, then animate.

## Reusable mega-prompts (see `HIGGSFIELD_REUSABLE_MEGA_PROMPTS.md`)
- **3x3 Cinematic Contact Sheet:** one input image → 9 locked-consistency shots (ELS, LS, MLS, MS, MCU, CU, ECU, low-angle, high-angle). Credit-efficient full coverage of a subject in a single generation.
- **9-Scene Sequence:** one scene input → a logical 9-frame cinematic progression, consistent character/grade, AI chooses angles.

## New infrastructure (2026-06-08): Higgsfield is now INSIDE the tools
Higgsfield now runs natively inside **Figma** (seven pro tools: Image & video generation, Angles, Mockup Studio, Expand, Remove BG, Relight), **After Effects**, and **Premiere Pro**. No exports, no switching. Prefer in-app Higgsfield when it removes a round-trip (e.g. Remove BG / Relight / Expand inside the editor instead of bouncing files). This strengthens the premium-stack law: the whole chain (generate → composite → grade → finish) can live inside Adobe/Figma.

## Hard-won operational notes (from the Synergy run)
- **Seedance NSFW filter false-flags** tender/elderly close-ups and words like "intimate," "tender," "her face." Use neutral wording, or route the shot to **Kling 3.0** (different filter), or cover with a slow push on the still.
- nano_banana_pro reference passing works via `medias:[{value:<job_id|url>, role:"image"}]`; multi-reference (2+ faces) works for two-shots.
- A decline-preset retry uses `declined_preset_id` when the API suggests a preset you do not want.
- **Anti-gloss law for documentary/real registers:** natural light only, real skin (pores, age spots), age-accurate, handheld feel, muted warm grade, lived-in spaces, no studio glamour, no one smiling at camera. The fastest way to fail a "real" brief is AI sheen.

## The full stack (from the written master guide, screenshots saved)
Joey's written companion ("Claude Skills to Help You Prompt Seedance 2.0 and Nano Banana Pro to Waste Less Credits", 19-page screenshot set saved in `REFERENCE_LIBRARY/higgsfield_og/written_guide/`) names the complete stack:
- **Soul Cinema / Soul Cast** = character faces + outfit references.
- **Nano Banana Pro** = character sheets, fuses, scene plates.
- **Seedance 2.0** = every video generation (now does 1080p).
- **Tiger Video** = final pieces / finishing.
- **Suno** = the music track (this is the answer to our Synergy music gap: Suno for owned music, not the blocked ElevenLabs Music API).
- **Ten Claude skills** drive it all. We currently have TWO installed (banana-pro-director, cinema-worldbuilder); the other ~8 are not yet in hand. Get them from the same source when available.

**The one principle under everything (the lock is the look):** lock the canonical reference sheet (front / three-quarter / profile / full-body plates) that defines face, bone structure, body, skin tone, hair color, identity markers. Everything else (outfit, hairstyle, makeup, accessories) swaps freely. The character stays the character because the reference is locked, not because each prompt re-describes them. This is why we build the base + 6-panel sheet FIRST (banana-pro-director Steps 1-2) before any scene or video.

## How this is wired (holistic adoption)
- The two skills auto-trigger on any image/video/Seedance/Nano-Banana/character/scene request via their descriptions. That IS the auto-application.
- This doctrine is the standard they compose under; cite it on any AI-production task.
- Raw sources saved in `00_COMMAND_CENTER/REFERENCE_LIBRARY/higgsfield_og/` (the original doc, transcript, scene-sequence PDF).
- Memory `[[higgsfield-production-doctrine]]` records this as the locked default for future sessions.
