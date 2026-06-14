Now I'll deliver the synthesized leverage plan. This is a pure synthesis task over the extractions you provided, so no further tool calls are needed.

---

# DEADPAN SUMMER · FINISHING LEVERAGE PLAN

Single prioritized AE/Premiere/Adobe pass for the Alma Love 100% AI luxury swimwear spot (16:9, ~25-30s). Each problem below names the best technique, a backup, exact steps with params, and where it sits in the render order. Em-dashes are not used anywhere.

## The one structural decision that unlocks everything

Build the master as a **Premiere sequence of AE-finished shots**, not a flat ffmpeg stack. Per-shot AE comps handle compositing/2.5D/tell; Premiere holds the global grade + final encode. This is forced by the AI-composite extractions (color WILL drift shot to shot) and by the two-tier master/deliver discipline. Concretely:

- Each AI clip becomes its own AE comp. Inside it: precompose the raw clip, then stack fixes on adjustment layers above it.
- AE shots render out **Lossless or ProRes 422 HQ** (never H.264) so we do not stack compression before the master.
- Premiere holds ONE Lumetri adjustment layer over the whole sequence for the unified grade, then exports ProRes master + H.264 deliverable.

Single-compression law: only the final Premiere export is H.264.

---

## P1 · CRISP REAL PRINT ON THE MOVING SUIT (hardest wall #1)

**Verdict: do NOT try to displacement-map the real product print onto the moving body across motion.** None of the six tutorials actually teach non-rigid cloth tracking (mocha/mesh-warp), the extractions say so explicitly three times. Attempting tracked-cloth print transfer on a 25s spot is the highest-effort, lowest-yield move in the whole project. The realistic crisp-print win is upstream + grade, not a per-frame AE composite.

**Best technique (highest leverage): fix the print at the STILL stage, then upscale, then push saturation/contrast back into the coral in the grade.** Three stacked levers, in order:

1. **Generation-side print plate (cheapest, do first).** Generate the suit/print as a separate high-res plate (Nano Banana Pro / Seedream) using the real product photo as reference with the line "in the same visual style as the uploaded reference photo," then animate START to END between two product-accurate frames (Firefly/Higgsfield Seedance i2v) so the print never has to be re-derived in motion. The crisp feather-fan must exist in the source frame; AE cannot invent stipple that the AI never rendered.
2. **Upscale every selected clip BEFORE the timeline** via Higgsfield `upscale_video` (MCP, headless) to 2K/4K. The extraction is explicit: this "brings the texture in the fabric and the sharpness on the edges back," not just bigger pixels. Run it against your existing Topaz step and keep whichever resolves the feather-fan stipple crisper. This is the single biggest real-print lever available from these videos.
3. **HSL-Secondary the coral in Lumetri** to make the soft wash read crisp. In Premiere, on the global Lumetri adjustment layer: HSL Secondary, key the coral suit (eyedropper + refine the H/S/L sliders, tighten the mask with Denoise/Blur low), then raise that selection's Saturation +15 to +30, Contrast +10 to +20, and Sharpen modestly. This pushes the print from "soft coral wash" toward "crisp coral-red" without touching the cream backdrop. Hard-key it tight so skin does not get oversaturated.

**Backup (hero stills only, not motion):** Photoshop/Firefly generative cleanup on a single hero frame: `image_select_by_prompt` "the bikini print" then regenerate a crisper stipple, producing one corrected still. Only viable on near-static deadpan frames. Do not trust it across motion (it mutates frame to frame and is not product-exact).

**Explicitly NOT worth doing for a 25s spot:** 3D Camera Tracker print-pinning (solves camera motion, not cloth warp), Fractal-Noise displacement of the real print onto the body, track-matte print overlay driven by a hand-keyed mask. All three are in the extractions as "the video does not teach the part we need." Skip them.

---

## P2 · HAND / FINGER MELT (hardest wall #2)

**Verdict: the cheapest fix is generation-side avoidance; AE/plugin patching is the fallback, and it is a tracked-cover, not a true repair.**

**Best technique (do FIRST, before any patching): generate the melt away.** Two levers from the AI-video-2026 extraction:

1. **Frame hands large and slow.** AI deforms small/fast hands and crowds; it animates big single subjects cleanly. Compose hero beats medium / medium-close / full-body single-subject, hands kept large and slow when visible.
2. **One slow deliberate action per clip.** Prompt "the model slowly and deliberately [single hand action], deadpan, holding the pose; static locked camera" at both the start and end of the prompt. One subject + one action + the word "slow" is the explicit anti-melt lever. Fewer melted hands means less for AE to ever touch.

**Best repair technique when a hero frame still melts: Higgsfield Draw-to-Edit, on near-still deadpan frames only.** Circle the bad hand, prompt "replace with a clean relaxed hand, coral-on-cream bikini, deadpan." It is generative so it drifts across motion and is NOT product-exact, so use it only where the hand is nearly static, then re-verify against the real product photo. We drive this headless via Higgsfield MCP rather than the panel UI.

**Backup (true cover): roto-isolated tracked patch in AE.**
1. Photoshop/Firefly: pull one clean frame, `image_select_by_prompt` "left hand fingers" then generative fill with a BLANK prompt to reconstruct a clean hand region, producing a patch still.
2. In AE: import the AI clip + the patch plate. Run **3D Camera Tracker** (Perspective) on the shot, drop a track null on the hand surface, parent the patch layer to that null so it locks to the move.
3. Stack the patch layer ABOVE the clip; matte it to the hand region (track-matte / Set Matte) so only the patched area shows; feather the matte edge 2-4px; overlap the patch 2-4 frames at each cut so the swap reads cohesive.

This is honest about its ceiling: it covers melt, it does not non-rigidly track fingers. Reserve it for the one or two prominent hero shots where melt is unavoidable. Do not roto every clip.

**Order: avoid in generation → Draw-to-Edit on stills → tracked patch only for the worst prominent shot.**

---

## P3 · KILL THE AI TELL (read as real 35mm)

**Best technique: one ADJ_FILM adjustment layer at the top of each AE comp carrying the full optical stack.** This is the correct AE structure (the "critical"-rated extraction) so every shot gets identical de-digitizing in one place. Build the stack in this render order on ADJ_FILM:

1. **Optics Compensation** (Distort), enable Reverse Lens Distortion, Field of View ~8-15 for a subtle real-lens barrel/edge curvature. Keyframe FOV a hair during any push for lens-breathing.
2. **Glow** (Stylize) on a duplicated top layer, Glow Based On = Color Channels, raise Glow Threshold so ONLY highlights bloom, low Glow Radius, then **Screen** blend the duplicate. This is the golden-hour halation on the cream backdrop and skin highlights. Halation is the single most convincing 35mm tell here.
3. **Chromatic aberration** (not a named single effect in the videos, build it): tiny per-channel offset, strongest at frame edges, to pair with the Optics Compensation barrel.
4. **CC Vignette** (or Lumetri vignette) gentle Amount, warm edge falloff, pulls eye to the deadpan model.
5. **Add Grain** (Noise & Grain), pick a film-stock preset, low Intensity, Blend With Original ~40-60. This is the real grain pass, applied LAST over the graded look. Use Remove Grain first only on a clip with ugly digital noise before regraining.
6. **CC Force Motion Blur** on any 2.5D-animated still layer or any too-crisp AI clip so fast camera/parallax moves gain natural blur, killing the slideshow stutter that flags AI.

**Backup / placeholder:** plain **Noise** at 3-8%, Color Noise off, on the adjustment layer. The extraction is explicit that this is a placeholder, not real grain. Use only if Add Grain is unavailable.

**Explicitly NOT worth doing:** Posterize Time on hero footage (it is stop-motion stylization, the OPPOSITE of photoreal deadpan luxury). Allowed only on a title element if you want it to feel less digitally perfect. Warp Stabilizer only on a clip with genuine unwanted drift, Smoothness low + "Crop Less / Smooth More" to avoid the rubbery tell. Most clips are already locked, so skip stabilizer by default.

---

## P4 · REAL MOTION ON STILLS (2.5D, not a slideshow push-in)

**Best technique (defeats the push-in at the source): authored START to END image-to-video.** This is our proven lock-stills-then-animate law, confirmed by three separate extractions (Firefly first/last frame, Higgsfield first/last frame, the AI-2026 guide). Take a product-accurate Seedream still as FIRST frame and a hand-authored END keyframe still (deadpan model in final pose) as LAST frame, feed both to Higgsfield Seedance `generate_video` (`start_image` + `end_image`) with performance verbs and "static locked camera" bookended in the prompt. The motion is interpolated between two correct frames instead of a single still being pushed. Generate every clip at exact 16:9 master resolution so no stretch distorts the suit. Generate slow, then retime in Premiere (`speed_change` / `set_clip_speed_qe`, frame blending on) to hit the deadpan rhythm.

**Backup / supplement (true 2.5D in AE) for any beat that needs in-camera parallax:**
1. Cut the still into depth slices (Higgsfield `remove_background` or Firefly `image_remove_background` for the model; background as its own layer).
2. Create a NULL. Parent all slices to it. Offset slices at different depths.
3. Keyframe ONLY the null's Position/Scale for the camera move. Keep it tiny and eased (the extraction's 95→100 over ~1s restraint is exactly the luxury register we want).
4. **Easy Ease (F9)** on every keyframe, set BEZIER interpolation with ~33-85% influence so the move reads like an operated camera, not a linear robot move.
5. **Motion Tile** (Stylize) with Mirror Edges on any pushed/panned slice so the move never reveals transparent edges.
6. **Camera Lens Blur** (Blur & Sharpen) on far-parallax layers, animate Blur Radius low to slightly higher across the push to fake a real shallow-DOF rack; soft iris shape for organic bokeh on cream-backdrop speculars.
7. **CC Force Motion Blur** so the parallax move carries natural blur.

**Order: prefer authored i2v for hero motion; reserve AE 2.5D for the one or two beats that need genuine camera parallax the i2v cannot give.**

---

## P5 · FINISHING GRADE (warm coral-on-cream golden hour, consistent)

**Best technique: ONE Premiere Lumetri instance on a single adjustment layer over the whole sequence, copied across all shots.** We have full Premiere MCP (`color_correct` / `apply_lut` / `add_adjustment_layer`), so the master grade lives there, not per-clip in AE. Build it:

1. **Color Wheels:** lift/gamma toward amber, shadows slightly cool. Establishes golden hour.
2. **Curves:** gentle S on RGB for film contrast; Red channel up in highlights, Blue down in shadows for warmth; soft shoulder for highlight roll-off (the analog tell).
3. **HSL Secondary:** key the coral suit, push its Saturation/Contrast (shared with the P1 crisp-print move above, this is the same key, do it once).
4. **Lumetri vignette:** gentle, warm edge falloff (can live here instead of the AE CC Vignette if you want a single vignette source).

Copy the same Lumetri instance across all shots for unity. Because AI-clip color drifts, this step is mandatory, not optional, the extraction confirms it.

**Per-shot correction in AE only when a single clip is off-palette before it reaches Premiere:** AE Curves on that shot's adjustment layer to neutralize, then let the global Lumetri do the look. Do not grade the look twice.

**Upstream help (reduces how much Lumetri must rescue):** at the still stage, use "in the same visual style as the uploaded reference photo" so coral-on-cream golden-hour holds shot to shot before any grade.

**Explicitly NOT worth doing:** AE Hue/Saturation as the grade tool (it is the weaker tool; we are color-led, not B&W). AE Fill on the suit (flattens print detail, violates product-lock). Use Fill only to force the exact brand coral hex on the TITLE.

---

## P6 · TITLE / END CARD ("Alma Love / DEADPAN SUMMER")

**Best technique: build the type in AE, animate restrained, motion-blur it, nest it as a reusable end-card precomp.**

1. Set type. Use Adobe `font_recommend` for the right face. Apply **Fill** (Generate) to force the exact brand coral hex.
2. **Stroke-only shape layer** (Rectangle, Fill = None, Stroke = Solid, coral-on-cream) for the card frame; keyframe Trim Paths / Stroke Width for a draw-on.
3. **Luma track matte:** put graded footage inside the "DEADPAN SUMMER" letters for an editorial reveal (text as matte).
4. Keyframe **Position + Opacity** on the title; **Easy Ease (F9)** every keyframe so it reads premium, not robotic. Tiny moves only.
5. **CC Light Sweep** (Generate) on the wordmark, keyframe Center across the word for ONE slow luxury shimmer. Keep it very subtle.
6. **Pre-compose** the whole build into a reusable end-card precomp.

**Backup for a kinetic word reveal:** animated **Mask Path** wipe with Easy Ease.

**Explicitly NOT the tool:** Higgsfield in-panel Generate Image (no type/motion-design control). Build the card in AE text, not the plugin.

---

## P7 · HIGGSFIELD-INSIDE-PREMIERE: what it actually unlocks for us

**Honest verdict from the extraction: for our pipeline, near-zero net-new, because we already drive the same six operations headless via Higgsfield MCP + Premiere MCP + AE MCP.** The plugin's only real headline is killing the export/upload/download loop, which our MCP control already does scripted. So:

- Do NOT install the plugin to chase the integration; we already have the capability via MCP.
- DO use the underlying Higgsfield operations (headless) in our edit: `upscale_video` before timeline (P1), `generate_video` start/end for in-between beats (P4), `remove_background` for 2.5D slices (P4), Draw-to-Edit for hand patches on stills (P2).
- The plugin does NOT solve P3 (35mm tell), P5 (grade), or P1 (crisp print across motion). Those are still ours to build in AE/Lumetri. The extraction states this directly.

The one place the panel could be worth a manual click is Draw-to-Edit on a hero frame if the MCP path is awkward; otherwise stay headless.

---

## P8 · AI-VIDEO 2026 BEST PRACTICE: levers we are missing

Net-new workflow levers worth adopting (all from the extractions, mapped to our spot):

1. **Generate at exact 16:9 master resolution at the generation step** so no clip is ever stretched (stretch distorts the suit). This is a defensive must, the Firefly extraction names aspect-mismatch as the known AI-composite failure.
2. **Upscale before timeline, not after.** Stated order. Higgsfield `upscale_video` → into Premiere, never the reverse.
3. **Generate slow, retime in editor.** Cleaner generation, then Premiere `speed_change` with frame blending to hit deadpan rhythm.
4. **Repeat camera intent at start AND end of every prompt** to lock the static camera so AE owns the parallax, not the model.
5. **Single-compression discipline:** AE shots out Lossless/ProRes, only the final Premiere export goes H.264.
6. **Roto-reuse:** keep rotoscoped/patch frames and reuse them rather than redoing, per the compositing extraction.

**Explicitly NOT worth doing (low ROI for 25s):** Runway Aleph relight/restyle on anything containing the product (it regenerates pixels and mutates the coral-on-cream print, violating product-lock; only safe on product-free background plates, and it is a manual web tool outside our stack). Auto-reframe / vertical derivation is only relevant if you cut a 9:16 promo later, not for the hero 16:9. Omni-reference character sheet is marginal (we already lock identity via Soul/keystone, and the extraction admits the result is blurry).

---

## CONSOLIDATED RENDER ORDER (execute top to bottom)

| # | Stage | Where | Action |
|---|-------|-------|--------|
| 1 | Generate | Higgsfield/Seedream | Hands large + slow, one action, static-camera bookended prompt, "same visual style as reference," **at 16:9 master res** |
| 2 | Author motion | Higgsfield Seedance | START→END i2v between two product-accurate frames; generate slow |
| 3 | Upscale | Higgsfield MCP | `upscale_video` to 2K/4K **before timeline**; compare vs Topaz, keep crisper |
| 4 | Per-shot AE comp | AE | Precompose clip; ADJ_FILM on top |
| 5 | Hand repair (only if needed) | Higgsfield Draw-to-Edit / AE tracked patch | Stills only; verify vs product photo |
| 6 | 2.5D (only beats that need it) | AE | Null-parented depth slices, Motion Tile mirror, Camera Lens Blur rack, Easy Ease |
| 7 | 35mm tell | AE ADJ_FILM | Optics Comp → Glow(Screen) halation → CA → CC Vignette → Add Grain → Force Motion Blur |
| 8 | Render shots | AE | **Lossless / ProRes 422 HQ** (no H.264) |
| 9 | Assemble | Premiere | Sequence the AE shots; retime slow clips with frame blending |
| 10 | Global grade | Premiere Lumetri (one adj layer, copied across) | Color Wheels amber → Curves S + warm roll-off → **HSL Secondary key coral, push sat/contrast (P1 crisp-print)** → vignette |
| 11 | End card | AE end-card precomp | Type + Fill coral hex, stroke frame, luma matte, Light Sweep, Easy Ease |
| 12 | Master + deliver | Premiere | ProRes master, then single H.264 deliverable |

## THE TWO LEVERAGE CALLS, STATED PLAINLY

- **P1 crisp print:** the win is upstream + grade (correct source frame → Higgsfield upscale before timeline → Lumetri HSL-Secondary on the coral), NOT a tracked displacement-map of the real print onto the moving body. None of these six tutorials teach the cloth-tracking that would require; building it for a 25s spot is the worst effort-to-yield move available. Skip it.
- **P2 hands:** avoid in generation first (large + slow + single action), repair only the one or two prominent hero shots, and accept that every AE/plugin repair is a tracked cover, not a true finger-track. Do not roto every clip.