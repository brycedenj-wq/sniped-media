# SNIPED Operating System v1 · LEGACY

Source: Aesthetic + Edit System Build chat export. Migrated to SNIPED_OS as canonical reference 2026-05-12.

**Important:** The BASE PRESET in this doc (Adobe Portrait + saturated grading) is RETIRED. Current preset is v3 LUXURY (Adobe Neutral, quiet luxury editorial restraint). See `/05_PRODUCTION/lightroom_operating_system.md` and `/05_PRODUCTION/_preset_backups/SNIPED_LOCKED_LOOK_v3_LUXURY.xmp` for the active preset.

What remains active doctrine from v1:
- The 6-mask kit
- The 10 named texture overlays (Sniped_01 through Sniped_10)
- The general portrait mask best practices
- The critical craft discoveries (rim/fill trap, floating full-body, atmospheric depth, grid sequence, client vs grid edit)

What is retired from v1:
- The Adobe Portrait base profile
- The +30 Blue Primary Saturation Calibration trick
- The HSL orange +5 sat / +10 lum punch
- The Color Grading Highlights hue 40 / Shadows hue 220 wash
- Any "Sniped Prestige Base" or $12,500 Founder Kit references (those were Gemini hallucinations, never real)

---

## Starting point

Came in after running a Gemini audit. Aesthetic_Statement_v1 already existed and held up: monochromatic color blocking, clinical retouch, severe posing, color/edit/pose as strengths, depth as weakness. The audit wasn't the problem. The problem was the editing rabbit hole Gemini sent down: "Sniped Prestige Base" preset, "color physics matrices," elaborate green spill mask gymnastics. Discarded all of it.

The aesthetic statement didn't need updates. What needed building was the actual workflow underneath it.

---

## What was built

### SNIPED Operating System doc

One-line aesthetic, 5 layers (foundation, texture, light, color physics, finishing), Lightroom recipe, hero moves, on-set checklist, full pipeline, what-this-isn't section. Saved to project knowledge.

### SNIPED Base Preset (v1 LEGACY · RETIRED · superseded by v3 LUXURY)

Profile Adobe Portrait, Contrast +10, Highlights -15, Shadows +15, Whites +10, Blacks -10, classic S curve no lifted blacks, HSL orange +5 sat -5 lum +10 + greens/aquas sat -20, Color Grading Highlights hue 40 sat 8 / Shadows hue 220 sat 8 blending 50, Calibration Blue Primary Saturation +30, Clarity +5, NO global grain (grain only on background mask), Sharpening 40 mask 50, NR Lum 10, lens + chromatic aberration ON.

**This preset is retired.** Use v3 LUXURY (Adobe Neutral base) for all new work.

### Mask kit (6 saved masks · STILL ACTIVE)

1. **AI Subject Mask** · Sharpening +20, NR -10
2. **AI Background Mask + grain** · 35/25/50
3. **Fake Rim** · Subject mask intersected with Linear Gradient from unlit side. Exposure +0.30 Highlights +15 Whites +10
4. **Skin Glow / Melanin Anchor via Point Color** · Sample skin midtone, Sat -5 to -10, Lum +10 to +15, Range 30
5. **BG Smooth** · Texture -50, Clarity -30, Sharpness -50
6. **BG Color Shift** · Rescue only

### 10 custom texture overlay PNGs

Generated via ChatGPT and Gemini image gen. Named `Sniped_01_Dust_Light` through `Sniped_10_Vertical_Damaged`. Used in Evoto Backdrop Changer at 15-25% opacity.

### General portrait mask best practices

The universal stack: AI Subject (sharpening), AI Background (darken/smooth/grain), Point Color (skin glow), AI People Iris (sharpen +20-25, Clarity +10), Linear Gradient (light shaping). 5 masks max. Save as presets.

- **Point Color** identified as the most underused tool with highest leverage
- **Radial Gradient** flagged as the trap mask most operators overuse

---

## Key decisions

### No global grain. Grain only on background mask.

Discovered the Evoto overlay PNG buries Lightroom global grain anyway, so global grain is wasted compute.

### Different edits for client vs grid post.

- **Client gets clean baseline:** color-corrected, retouched, no stylized grading
- **Grid gets full SNIPED stylization:** background swap, overlay, grain, full mask kit

### Photoshop NOT in routine workflow.

Use Lightroom Generative Remove or Evoto Backdrop Replace by default. Photoshop only as last resort using the PiXimperfect method:

1. Subject mask, expand 50px
2. Content-Aware Fill
3. Gaussian blur backdrop 120-160px
4. Add noise back via 50% gray overlay layer with Add Noise filter
5. Blend If to control noise in highlights

This is the backdrop rescue protocol. Not the default.

### Discarded the "SNIPED Prestige Base" and $12,500 Founder Kit pricing.

Both came from a different chat or Gemini's invention. Not real positioning. Pricing canon: Reset $1,500, Sprint $750 (warm-network only), Op Kit $3-8K, Brand System $10K+.

### Focus is new work, not archive rescue.

5-10 archive rescues planned max, then move forward.

---

## The realignment moment

Mid-chat: "maybe I need to put the camera down... idk."

Pulled back. Named the pressure of chasing 9 masters and comparing to fuckapic / timtadder / jpwphoto. Clarified the real goal: "I just want to make money and have good fire pics edit wise and story wise." Not museum tier. Reframed the entire workflow around that. The pressure to be in MoMA was someone else's voice.

---

## What was discovered (CRITICAL CRAFT NOTES · still active)

### The post pipeline has a ceiling.

Raws at 38-52/80 ceiling out at 63-65/80 after the full edit pipeline. Pipeline is doing real work (10-25 point jumps) but it can't take a B-tier raw to an A-tier finish. **The ceiling lives on set, not in post.**

### Hard light without fill or rim is the trap.

The frames that worked (Jasmine black-on-black, cream-on-black hero, navy editorial) all had one of three:
1. Rim from behind
2. Negative fill on shadow side
3. A tight crop making the merge intentional

The frames that struggled had none. **Going forward: build rim or kicker into the setup before the first frame.**

### The floating full-body problem.

Cropping the floor completely out removes the visual gravity anchor. Brain reads "floating." Three fixes (decision tree):

1. **Keep 5-10% floor visible at bottom**
2. **Paint a contact shadow under feet** (AI Background Mask, brush ellipse, exposure -0.50 to -0.80)
3. **Crop tighter to mid-thigh, never on the joint**

Old default of "crop floor out on every full-body" was producing floaters for years. Repeatable decision tree now.

### Atmospheric depth is a recurring gap.

Depth and dimensionality consistently scored lower than color/signature across audits. **Fix: add an atmospheric plane between subject and backdrop in studio work.** Build a found-color discipline alongside the locked-palette method.

### Different shoots need different aesthetic lanes.

Full-body editorial silhouette is a different lane than tight SNIPED portrait crops. Both can hold on the grid as long as the operating system underneath holds (color block, signature, texture, sharp subject).

### The BG Smooth mask doesn't fix real wrinkles.

Only kills micro-texture. Real wrinkles or seams need Generative Remove first, PiXimperfect Photoshop method as fallback.

### Grid sequence logic.

Color stories must diverge while system underneath holds. **Posting two dark moody sets back-to-back kills momentum.** Example sequence: Wed Jasmine (black tonal) → Sat red-on-teal (graphic complementary) → Tue cream-on-brown (warm soft) → Fri brown-on-black or weekend hero.

---

## Original action items (status as of doc migration · 2026-05-12)

- ~~Run all 14 black-on-black frames through synced workflow~~ (status unknown · check archive)
- ~~Apply masks across batch, export 7 client deliverables + 3 grid posts~~ (status unknown · check archive)
- ~~Send raw + navy edit + drafted prompt to edit expert for floating problem feedback~~ (status unknown)
- **Build rim/kicker into weekend shoot setup before first frame** · STILL ACTIVE · apply Sunday 5/17
- ~~Update SNIPED Operating System doc to reflect Evoto-handles-both-grain-and-scratches discovery~~ (this doc captures it)

---

## What the chat was NOT for going forward (still applies)

- Re-running the aesthetic audit (done, locked in Aesthetic_Statement_v1)
- Building more elaborate Lightroom recipes to fake what should be done on set
- Chasing other photographers' aesthetics (jpwphoto's hyper-luminous celebrity look is a different operator with a different kit)
- Per-image hand-holding when the system can be applied as a batch

---

## Migration notes

- Base preset retired. New canon: v3 LUXURY (Adobe Neutral). See `/05_PRODUCTION/_preset_backups/SNIPED_LOCKED_LOOK_v3_LUXURY.xmp`.
- Mask kit, texture overlays, and craft discoveries: STILL ACTIVE. Apply to v3 LUXURY-graded frames the same way.
- Client vs grid edit distinction: STILL ACTIVE.
- No-global-grain rule: STILL ACTIVE.
- Photoshop-as-last-resort: STILL ACTIVE.
- Rim/kicker on-set build: STILL ACTIVE, apply to every shoot day including 5/17.

---

## What this doc is NOT

- The current preset. v3 LUXURY supersedes the v1 base. Reference `/05_PRODUCTION/lightroom_operating_system.md` for current canon.
- A pricing doc. Pricing canon is in `/01_OFFERS/` and `/00_BRIEF/CANONICAL_TRUTHS.md`.
- A full SOP. SOPs live in `/05_PRODUCTION/SOP_*.md`.
