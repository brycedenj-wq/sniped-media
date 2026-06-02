# Photoshop Generative Fill + Reference Image · Tactical Extraction

Source: `/99_VAULT/_intake_archive_2026-05-12/photoshop .docx`
Distilled: 2026-05-12

Photoshop's Reference Image feature (new in 2026) lets Generative Fill be guided by an image instead of (or in addition to) a text prompt. This is the load-bearing technique for SNIPED's background-replacement composite workflow (Path A in `/05_PRODUCTION/composite_environment_rotation_v1.md`).

---

## Why Reference Image matters for SNIPED

Text-only Generative Fill gives you a generic Brutalist interior. With a Tadao Ando reference image attached, Generative Fill targets that specific architectural register · concrete texture, light direction, negative space ratio, scale.

Before: "Brutalist concrete architecture" prompt → generic result
After: Same prompt + Tadao Ando interior reference image → Tadao Ando-quality output

This collapses the gap between Path A (PS Generative Fill, faster) and Path B (External AI plate + composite, more control). Path A with Reference Image is now ~80% of Path B's quality at 20% of the time.

---

## The Reference Image workflow

### Step 1 · Make selection
- Open the still in Photoshop
- Select Subject (top menu Select → Subject)
- Invert selection (`Cmd+Shift+I`) so the background is now selected
- Refine Edge on hair if needed (Select → Select and Mask → Refine Edge brush)

### Step 2 · Open Generative Fill
- With background selected, click Generative Fill in the contextual taskbar at the bottom
- OR menu: Edit → Generative Fill

### Step 3 · Add Reference Image
- In the Generative Fill panel, look for the reference image icon (paperclip or image-plus)
- Click → upload your reference (e.g., Tadao Ando interior photo)
- The reference image now appears as a thumbnail in the panel

### Step 4 · Add prompt (optional but recommended)
- Even with a reference image, text prompts add register guidance
- Example: "Brutalist concrete interior, warm shaft light, deep negative space, atmospheric haze, A24 luxury campaign aesthetic"

### Step 5 · Choose model
Photoshop 2026 offers multiple generative models:
- **Adobe Firefly** · default. Reference Image works here. Best for SNIPED's photographic register.
- **Firefly Image 3** · newer, supports Reference Image
- **Nano Banana** · integrated but DOES NOT yet support Reference Image (per source doc)

Use **Adobe Firefly** for Reference Image workflows until Nano Banana adds support.

### Step 6 · Generate
- Photoshop returns 3 variations
- Each generation costs 1 credit
- Browse variations in the Properties panel

### Step 7 · Pick + accept
- Pick the variation that best holds the reference register
- Accept (clicks the checkmark in the taskbar)

---

## Reference Image use cases for SNIPED

### Background replacement with environment reference
Primary use. Select background → invert → Reference Image of target environment (e.g., Tadao Ando concrete) → Generative Fill with prompt.

### Wardrobe / styling change
The source doc demonstrates replacing a tank top with a custom T-shirt using a reference image of the T-shirt design. SNIPED application: change wardrobe color/style without re-shooting.

**Caveat for SNIPED:** wardrobe changes may shift how the subject reads. Test against the locked v3 LUXURY palette before approving.

### Lighting reference
Use a reference image with the lighting direction/quality you want. Generative Fill samples the lighting from the reference. Useful for: when the original capture's lighting reads flat, use a reference with stronger shaft light.

### Color palette transfer
Reference image with target palette → Generative Fill blends toward that palette in the masked area. Less precise than direct HSL/Color Grading in Lightroom, but useful for environmental color washes.

---

## When Reference Image FAILS

- **Identity preservation:** if you accidentally include subject in the masked area, the reference image will guide regeneration of the subject. Always Select Subject → Invert first.
- **Style mismatch:** if the reference image's color/lighting is wildly different from the original, output reads disconnected. Match reference register to your shoot register before generating.
- **Multiple references:** Photoshop can only use one reference image per generation. To blend multiple references, pre-process them in another tool or run sequential generations.

---

## Reference Image SNIPED prompt templates (paired with the 7-environment rotation)

For each of the 7 environments in `/05_PRODUCTION/composite_environment_rotation_v1.md`, the Reference Image workflow:

| Environment | Reference image source | Text prompt addendum |
|---|---|---|
| Brutalist Monument | Tadao Ando interior, Pawson House, Chipperfield museum | "Brutalist concrete interior, warm shaft light, A24 luxury aesthetic" |
| Industrial Minimal | Saint Laurent backstage photos, modern steel-and-concrete galleries | "Industrial minimal interior, soft practical light, restrained atmosphere" |
| Monochromatic Void | Avedon studio backgrounds, gradient seamless backdrops | "Infinite seamless monochromatic background, gradient light" |
| Sculptural Gallery | David Zwirner / Gagosian / Hauser & Wirth gallery interiors | "Sparse white gallery interior, plinths, spotlighting" |
| Cinematic Urban | Michael Mann Collateral stills, neo-noir LA night scenes | "LA urban scene at dusk, sodium vapor, restrained noir atmosphere" |
| Organic Surreal | Petra Collins or Erik Madigan Heck editorial spreads | "Organic surreal atmospheric scene, fabric, haze, dream-state" |
| Futurist Editorial | Apple campaign photography, Hypebeast editorial spreads | "Impossible-geometry editorial environment, reflective premium materials" |

Save 3-5 reference images per environment in `/SNIPED_OS/05_PRODUCTION/_composite_references/` organized by environment. Build the library once, reuse forever.

---

## Cost note

Each Generative Fill or Generative Expand = 1 Adobe credit. Adobe Creative Cloud Photography plan includes a monthly credit allocation. Track usage if running many variations.

For SNIPED Phase 1 cadence (1-2 hero composites per week), credit usage stays well within plan.

---

## Cross-references

- `/05_PRODUCTION/composite_environment_rotation_v1.md` · the 7-environment world-building vocabulary (Reference Image is the execution mechanic for Path A)
- `/05_PRODUCTION/track_b_frame_walkthrough.md` · the full composite SOP (Path B)
- `/_skills/sniped-hero-composite-lite/SKILL.md` · the 45-min lite lane workflow
- `/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md` · the broader tool matrix
- Memory: `[[sniped-composite-environment-rotation-v1]]` · the 7-environment locked rotation
