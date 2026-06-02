# Track B Creative Push · One-Frame Walkthrough

The Gress 5-step playbook executed on one frame. Use this as the runbook for your first Track B comp from last weekend's 6 shoots. Time budget: 60-90 min for frame #1 (you are learning the assembly), 30-45 min once the muscle memory locks.

If something below assumes a tool you don't have open, open it. Do not skim · execute.

---

## Step 0 · Pick the frame (5 min)

Filter `SNIPED_2026.lrcat` to the smart collection `02 · VIB Pool` OR open last weekend's shoots one by one. Pick ONE frame that meets ALL of these criteria:

- ⭐⭐⭐⭐⭐ rated (Hero candidate)
- Subject is sharp · eyes in focus, hands not blurred
- Subject occupies 40-70% of the frame (not full close-up, not tiny silhouette)
- Studio backdrop is clean enough to mask cleanly (no busy patterns, no falloff confusion)
- Subject's lighting is directional (you can identify the key light direction in 2 seconds · this matters because the AI background must be lit consistently)
- The subject's pose suggests a context (looking off-camera, walking forward, gesture mid-action). A static eyes-into-camera headshot is harder to comp · save those for v2.

**Apply Blue color label.** This locks it into VIB Pool smart collection. Note the file name. From now on this doc refers to it as `[FRAME]`.

---

## Step 1 · Lightroom prep (10 min)

Working in the master catalog. Frame is already developed via `SNIPED_LOCKED_LOOK_v1` import preset. Now refine for compositing:

1. **Crop to 16:9 horizontal.** Even if your final delivery is 4:5 portrait, work in 16:9 for the comp because background plates from Firefly / Nano Banana generate in landscape and look better when composed wide. You will re-crop at export.

2. **White balance manual pass.** Match the COLOR TEMPERATURE you want the final scene to read. If you want a sunset / golden-hour cinematic, push WB warmer (~6200K). If you want urban / cool / blue-hour, push cooler (~5000K). The subject WB and the background plate must agree or Harmonize will fight you in Photoshop.

3. **Subject mask polish.** Apply the locked 5-mask AI stack from `/05_PRODUCTION/lightroom_operating_system.md` Section 6.1. Even though Photoshop will do the final mask, doing the AI mask polish in Lightroom first gives you cleaner subject-vs-background separation to send into Photoshop.

4. **Exposure on subject.** Lift subject exposure +0.10 to +0.30 if the studio capture is slightly under. Background plates tend to be brighter; the subject must hold against a brighter scene without crushing.

5. **Export as 16-bit TIFF · ProPhoto RGB · full resolution.** Destination: `/SNIPED_PRODUCTION/2026/[shoot folder]/30_HEROES/_track_b_workspace/[FRAME]_v1_BASE.tif`

You should have a clean TIFF with the subject correctly exposed, AI-masked, ready for Evoto.

---

## Step 2 · Evoto skin pass (5 min)

Light pass. Track B is not Brand System tier. The skin should read as "polished but real."

1. Open the TIFF in Evoto.
2. Apply your locked SNIPED Evoto preset (skin clinical · pore detail preserved · spot removal high · eye whitening low · teeth whitening low).
3. Review at 100% on the face. Click any blemishes Evoto missed.
4. Skip body work for now. Skip dodge-and-burn. Track B's ceiling is the comp, not the skin.
5. Export as 16-bit TIFF, same destination, name `[FRAME]_v2_EVOTO.tif`.

---

## Step 3 · Generate the background plate (15-20 min)

**UPDATED 2026-05-12**: Primary tools are now Higgsfield Soul, Seedream 5.0, and Nano Banana Pro (NOT Firefly alone). See `/05_PRODUCTION/composite_environment_rotation_v1.md` for the 7-environment vocabulary and locked prompt templates · use those FIRST, the 3 Firefly options below are legacy/backup.

### Primary path (2026-05-12 onward)
1. Pick an environment from the 7-environment rotation (Brutalist Monument / Industrial Minimal / Monochromatic Void / Sculptural Gallery / Cinematic Urban / Organic Surreal / Futurist Editorial)
2. Use the locked prompt template from `composite_environment_rotation_v1.md`
3. Tool selection per `sniped-ai-image-tool-pick` skill:
   - **Higgsfield Soul** · best for atmospheric environments (Brutalist Monument, Cinematic Urban)
   - **Seedream 5.0 Lite** · best for HEX-precise palette control + camera cheat codes
   - **Nano Banana Pro (via Gemini)** · best for narrative urban + likeness-preserving variants
4. NO subject in prompt · "empty interior, no people, no subjects"
5. Export PNG (2048px long edge, sRGB) for Photoshop · per the universal export step in rotation doc

### Legacy backup (Firefly-direct, for reference)
Pick ONE of the 3 register options below based on what the subject's pose and lighting are asking for. Don't generate all three · pick one.

### Option A · Cinematic golden hour (Firefly)

Tool: Adobe Firefly (firefly.adobe.com).

Prompt (paste verbatim, replace bracketed direction if needed):
```
Wide cinematic background plate, [downtown Los Angeles rooftop OR Malibu cliffs OR Pacific Coast Highway], golden hour, 35mm lens, f/2.8, warm backlight from camera left, soft bokeh, anamorphic feel, atmospheric haze, no people, no foreground subjects, horizontal 16:9, photographic realism, subtle film grain, shot on Arri Alexa
```

Settings:
- Aspect ratio: 16:9
- Style: Photo
- Generate 4 variations
- Pick the one with light direction matching your subject's key light. Download at max res.

### Option B · Urban dramatic / blue hour (Nano Banana Pro via Gemini)

Tool: Google Gemini (gemini.google.com) with image generation. If you have Freepik subscription, Nano Banana Pro lives there.

Prompt:
```
Photographic background plate. Wide horizontal 16:9. Urban scene at blue hour, downtown skyline at dusk, no people, motion blur from passing cars, neon signage in mid-distance providing color motivation from camera right, $f/2.0$, ISO 800, shot on Sony A7R V, 35mm prime, soft cinematic grain, no foreground subjects, atmospheric depth, slight rain mist
```

Note: the `$f/2.0$` syntax with dollar signs improves photographic realism in Nano Banana per the source doc. Keep them.

Generate 4 variations. Pick the one where the dominant light direction matches your subject. Download max res.

### Option C · Studio-extension subtle (Firefly)

When you don't want to relocate the subject · just push the studio register. Use this when the subject's pose and lighting are tight to the original capture and you only want atmosphere.

Prompt:
```
Photographic background plate, dark moody studio environment, deep shadows on left, soft warm spill from upper-right window, dust motes in the air, atmospheric haze, 16:9 horizontal, no people, no subjects, photographic realism, shot on medium format, $f/2.8$, subtle film grain, abstract minimal background suitable for portrait compositing
```

Generate 4. Pick. Download.

### Quality check before moving on

- The plate is at least 1500px on the long edge (Firefly typically delivers ~2048px now, Nano Banana 2K)
- Light direction in the plate matches your subject's key light (within 30 degrees)
- The plate has depth (foreground bokeh, mid-ground subject space, background falloff)
- The plate's color temperature is in the same family as your Lightroom WB choice from Step 1

If any of these fail, regenerate before opening Photoshop. Do not try to fix a wrong-direction plate in Photoshop · regenerate.

Save the chosen plate to: `/SNIPED_PRODUCTION/2026/[shoot folder]/30_HEROES/_track_b_workspace/[FRAME]_plate.png`

---

## Step 4 · Upscale the plate (5 min)

The plate is too small for full-res composite. Upscale.

Open the plate in **Topaz Photo AI**. Use the Standard model at 4x. Output as 16-bit TIFF. Save as `[FRAME]_plate_upscaled.tif`.

Alternative: Photoshop > Filter > Neural Filters > Super Zoom at 4x with Sharpening 15. Topaz is cleaner for plates · use Topaz.

---

## Step 5 · Photoshop assembly (30-45 min · the load-bearing step)

Open Photoshop (the latest version with Neural Filter Harmonize · usually Photoshop beta has the freshest version, but production Photoshop also has it).

### 5.1 · Set up the document
1. File > Open > `[FRAME]_v2_EVOTO.tif`
2. Image > Image Size · note the dimensions
3. File > Place Linked > select `[FRAME]_plate_upscaled.tif`
4. Transform the plate to fully cover the canvas. Position it BEHIND the subject layer (drag in Layers panel below the subject).

### 5.2 · Convert subject to Smart Object (so re-edits in Lightroom can re-link)
1. Right-click the subject layer in Layers panel
2. "Convert to Smart Object"

### 5.3 · Mask the subject (the make-or-break step)
1. Select the subject layer
2. Top toolbar: Select > Subject. Photoshop's AI selects the person.
3. Click the mask icon at the bottom of the Layers panel (rectangle with circle inside). The subject is now isolated, plate visible behind.
4. Click the mask, then go Select > Select and Mask
5. View Mode: Overlay (red shows masked-out area)
6. Use the Refine Edge brush (second from top in left toolbar) and paint along the hair edges. This catches translucent strands.
7. Output to: New Layer with Layer Mask. OK.

### 5.4 · Hair edge cleanup (the John Gress trick)
1. Click the new mask
2. Pick a 100% hard brush, white color
3. Set blend mode to **Overlay** (not Normal · this is the trick)
4. Paint along hair edges where strands look translucent. The Overlay blend firms them without over-selecting background.
5. Switch to black brush, same Overlay blend, clean any over-selected background.

### 5.5 · Harmonize (the silent unlock)
1. Select the subject layer (the new layer Photoshop just made, with the mask)
2. Filter > Neural Filters > Harmonize
3. Drop down "Reference Image" · pick the background plate layer
4. Default strength is 75. Scale to **50%** for first pass.
5. OK.

The subject's color temperature, contrast, and exposure now sample from the background plate. This is what makes the comp stop reading as a comp.

### 5.6 · Add edge light (rim from the plate's dominant color)
Use the eyedropper to sample the brightest highlight color in the plate (likely warm orange/gold for golden-hour, cyan/blue for blue-hour, etc.).

1. New layer above subject. Name: `edge_light`.
2. Hold Option/Alt and click the subject's mask, drag to copy onto this new layer.
3. With the picked color, soft brush 60-100px, paint highlights along the side of the subject that faces the plate's dominant light direction.
4. Layer blend mode: **Overlay**.
5. Double-click the layer thumbnail. Layer Style dialog. At the bottom, "Blend If" gray slider:
   - Drag the BLACK slider on "This Layer" to the right (~85). Hold Option, drag the right half of the slider further right (~135). This restricts edge light to mid-tones and highlights only.
6. OK.

The subject now has light spilling from the plate's direction.

### 5.7 · Unifying grain layer
1. New layer above everything. Name: `grain`.
2. Edit > Fill > 50% Gray.
3. Blend mode: **Overlay**.
4. Filter > Noise > Add Noise. Amount: 8-12%. Distribution: Gaussian. Monochromatic checked.
5. OK.

This unifies the subject and plate under one grain texture · key for "this looks photographed" feel.

### 5.8 · Color wash (subtle unification)
1. New layer above grain. Name: `color_wash`.
2. Sample a mid-tone from the plate background (the dominant atmospheric color · golden, cyan, magenta, whatever).
3. Edit > Fill > Foreground Color. Fill the layer.
4. Blend mode: **Color**.
5. Opacity: start 0%, scrub up to **3-7%**. Stop where it just barely tints the whole image.

### 5.9 · Vignette / focus pull
1. New adjustment layer (half-circle icon at bottom of Layers): Exposure.
2. Drag Exposure slider down to **-0.30 to -0.50**.
3. Click the adjustment layer's mask. With a soft black brush (hardness 0, opacity 50%), paint over the SUBJECT'S FACE only.

This darkens the whole frame except the face · viewer's eye locks to the subject.

### 5.10 · Catchlight enhancement
1. New layer above all. Name: `catchlights`.
2. Tiny hard white brush (5-10px, depending on eye size in frame).
3. Click directly on the existing catchlight in each eye to brighten.
4. Blend mode: **Overlay**.
5. If too strong: lower opacity to 50%.

### 5.11 · Final review
1. Hide all your effect layers (eye icon). Show the unedited subject + plate. Read it.
2. Show all layers. Read it.
3. Toggle Harmonize layer on/off. The image should snap together when on.
4. If anything reads fake: Harmonize strength too high (drop to 30%), edge light too saturated (drop opacity), grain too coarse (lower to 6%).

### 5.12 · Save and export
1. File > Save As > `[FRAME]_v3_COMP.psd` (full layered file · keep this for re-edits)
2. File > Export > Export As > JPEG, Quality 90, sRGB. Name: `[FRAME]_v3_COMP_export.jpg`
3. Save to `/SNIPED_PRODUCTION/2026/[shoot folder]/30_HEROES/`

---

## Step 6 · Re-import to Lightroom + apply Hero Finish (5 min)

1. In Lightroom, navigate to `/30_HEROES/`. Right-click > Synchronize Folder. The new comp .jpg appears.
2. Apply `SNIPED_HERO_FINISH_v1` preset (final grain + skin protection + tone curve roll · per `/05_PRODUCTION/preset_library.md` Section 1.2).
3. Compare against the original frame side-by-side.
4. Apply Green color label (Hero Live).
5. Apply Purple color label IN ADDITION (Case Study Pool · this is going on LinkedIn).

---

## Step 7 · Quality bar before posting

Hold the comp at arm's length on the screen. Squint. Ask:

- Does the light direction read consistent? (If subject is lit camera-left and plate is lit camera-right, you have a fail · regenerate plate or flip horizontally.)
- Does the depth feel real? (Subject crisp, plate falling off · good. Both crisp · the plate needs blur added with Lens Blur effect.)
- Does the color temperature read unified? (Subject reading neutral while plate reads warm = Harmonize wasn't strong enough. Crank to 65%.)
- Does the seam at the subject's edge read fake? (Too crisp · Gaussian Blur 0.5px on the mask. Too soft · sharpen the mask edge.)

If any answer is "no," fix that ONE thing. Don't fix five things at once.

---

## Step 8 · Output use

This frame becomes:
- Portfolio update · add to Carrd selected work
- LinkedIn POV case study · "What compositing does to a studio shoot when the methodology runs first." Use the post to teach, not sell.
- IG carousel material · pair with the Track A original as a 2-frame "before / ceiling" comparison post
- VIB asset · pair with another Track A clean frame from the same shoot for the proof-of-range VIB

---

## Time targets

| Step | Target | Acceptable max |
|---|---|---|
| 0 · Pick frame | 5 min | 10 min |
| 1 · Lightroom prep | 10 min | 15 min |
| 2 · Evoto pass | 5 min | 10 min |
| 3 · Plate generation | 15 min | 25 min |
| 4 · Upscale | 5 min | 10 min |
| 5 · Photoshop assembly | 30 min | 60 min (first time only) |
| 6 · Re-import + finish | 5 min | 10 min |
| 7 · Quality review | 5 min | 10 min |
| **Total · first frame** | **80 min** | **140 min** |
| **Total · second frame onward** | **40 min** | **75 min** |

If your first frame goes 140 min, the assembly muscle is what's slow. The plate generation and Lightroom prep should be tight from frame 1.

---

## What can go wrong (and the fix)

| Symptom | Likely cause | Fix |
|---|---|---|
| Subject reads pasted-on | Harmonize off or too low | Harmonize at 60-75%, regenerate plate if WB mismatched |
| Hair edges look chopped | Refine Edge brush not used, or no Overlay-mode hair pass | Re-enter Select and Mask, refine hair, redo overlay-pass |
| Plate looks like a video game | Wrong AI model for register · Midjourney too stylized | Regenerate in Firefly (atmospheric) or Nano Banana (narrative) |
| Light direction wrong | You picked the wrong plate variation | Regenerate · this isn't fixable in Photoshop |
| Color cast wrong | Color wash too saturated or wrong family | Lower color_wash opacity to 3%, or change the sampled color |
| Skin reads waxy | Evoto pass too aggressive | Re-do step 2 with lighter Evoto preset |
| Background blurry but subject also blurry | The plate didn't upscale correctly | Re-run Topaz at 4x or use a different plate |

---

## After you ship frame #1

1. Save the .psd · this is your reference comp for future frames
2. Look at the frame after 24 hours · fresh eyes catch what tired eyes miss
3. If the comp holds up at 24 hours, post it. If not, identify the ONE thing that reads off, fix only that, re-export.
4. Do NOT iterate frame #1 forever. Ship at "good enough." Frame #2 will be better. Frame #5 will be the SNIPED Track B house style.

---

## The single rule for this walkthrough

**Execute in order. Do not skip steps. Do not improvise the assembly · the order is what makes Harmonize work.** The first frame teaches the muscle. The fifth frame becomes the SNIPED ceiling. The 36-finals batch is your live training set.
