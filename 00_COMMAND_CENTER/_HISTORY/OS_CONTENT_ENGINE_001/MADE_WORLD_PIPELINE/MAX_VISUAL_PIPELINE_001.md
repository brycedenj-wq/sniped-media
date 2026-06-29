# MAX VISUAL PIPELINE 001 · MADE WORLD / The Readymade Drop

**Date:** 2026-06-21 · **Rule:** the visual ceiling is elite, no exceptions. CSS/SVG is a wireframe, never a final. No asset is final until it passes the QA gate (section 8) and the External Visual Proof Gate (a human signs off; Claude is not the final visual authority). Nothing is generated, posted, spent, or wired by this document. Higgsfield runs per-batch only, on an explicit per-batch yes (no global always-allow).

## 1. Visual ceiling board (the top 10 standards + measurable "best ever")
The bar is the intersection of these references. Each is described as a measurable standard, not a brand to copy.
1. **Korean brand store / launch quality:** pristine high-key product pages, generous whitespace, one object per viewport, type that breathes. Measurable: >=55% negative space on the hero; one focal object; zero competing elements.
2. **Object-on-white luxury (Aesop/COS/Muji-grade restraint):** seamless white, one object, one shadow. Measurable: background RGB >=250 across the sweep, exactly one soft shadow, one light direction.
3. **Editorial product design (Kinfolk/Cereal stillness):** quiet, considered, anti-busy. Measurable: <=2 type sizes per frame, editorial kerning, no decorative elements.
4. **Gallery-grade web page:** feels like a museum site, not a shop. Measurable: one CTA per screen, thin 1px rules, no store chrome, AA contrast held.
5. **Premium packaging:** debossed mark, foil seal, fiber board. Measurable: tactile material reads in the render (grain, deboss depth), numbered edition seal legible.
6. **Cinematic product motion:** slow macro, single light, rack focus, intent in every frame. Measurable: one move per shot, 24fps clean, color discipline survives motion, no morph/drift.
7. **Social-first visual hooks:** stops the scroll in 1 second at thumbnail size. Measurable: the object reads at 120px; the contradiction is visible before any text.
8. **Material truth:** the surface looks real (machined aluminum, ceramic, matte polymer), not plastic-AI. Measurable: believable specular roll-off, real edge highlights, no uniform sheen.
9. **Proportion signature:** the same exact radius/proportion across every asset. Measurable: the chosen radius (r8) is pixel-identical across hero, variants, page, and edition.
10. **Zero AI tells:** no warped type, extra geometry, melted edges, or gloss haze. Measurable: passes a 200% zoom inspection with no artifact.

"Best ever" = a stranger at thumbnail size says "where can I get this," cannot tell it was AI-assisted, and the object reads instantly without a caption.

## 2. Tool routing map (lead / polish / verify)
| asset type | lead | polish | verify |
|---|---|---|---|
| hero product render | Blender base geometry -> Higgsfield (reference/img-to-img on the base) | Adobe (crop, color law, cleanup) | OS QA gate + External Visual Proof Gate |
| variant grid (r4/r8/r12) | Blender (exact radii) or Higgsfield with locked seed | Adobe (align, even light) | OS QA |
| texture / material closeup | Blender material test (truth) or Higgsfield macro | Adobe (dust/seam cleanup) | OS QA |
| motion loop / turntable | Blender turntable (geometry-exact) OR Higgsfield i2v from the LOCKED still | Adobe/Premiere (grade, caption-safe) | OS QA (motion doctrine: lock still first, no full-clip one-shot swap) |
| drop page image | Higgsfield/Adobe asset | Figma (layout) | OS QA |
| carousel slide | Figma (from the plate) | Adobe (export) | OS QA |
| Pinterest pin (2:3) | Figma/Adobe reframe of the plate | Adobe | OS QA |
| YouTube thumbnail | Figma/Adobe | Adobe | OS QA |
| landing page mock | Figma (assets from Higgsfield/Adobe) | Figma | OS QA |
| email header | Figma/Adobe | Adobe | OS QA |
Readiness (from the ledger): OS authoring READY/no-spend; Higgsfield PROVEN/spend-gated; Adobe crop READY, other Adobe layers AMBER (one handshake test each); Figma UNTESTED in CLI (needs a live file); Blender UNTESTED (app must be open with the MCP add-on). Tool readiness is verified per-asset before reliance.

## 3. Week 1 asset list for THE ONE
- Hero plate (the final tray, the money shot).
- 3 variant plates (r4 tight / r8 chosen / r12 soft), identical light + scale.
- Object detail macro (the single continuous radius + edge + material).
- Scale reference (faceless): the tray beside one everyday object (a pen, a phone) for size, NO hand/face. Decide at QA whether it is needed or it weakens the object-on-white purity.
- Turntable or motion loop (slow quarter-rotate, ~3-5s, from the locked hero).
- Profile grid assets (the 9 tiles: hero + teardown stills in one discipline).
- Landing page hero asset.
- Drop page hero asset.
- Platform crops: 9:16, 1:1, 4:5, 2:3, 16:9.
- Story assets (9:16 cuts of the hero + the rule-of-use placard).
- Email header asset.

## 4. Higgsfield generation batch 001 (capped, per-batch permission)
Full prompts in `01_prompts/HIGGSFIELD_BATCH_001.md`. Summary: 5 stills (hero final, variant grid, before/after pair, rule-of-use placard still, edition/packaging still). Aspect ratios per asset (1:1 + 9:16 crops). Negative prompts on every gen (no text, no logos, no hands, no people, no warped geometry, no plastic sheen, no extra objects, no busy reflections, no AI gloss). Quality criteria = the section 1 ceiling + the section 8 gate. **Credit estimate: ~20-30 credits for batch 001** (~2cr/still per the ledger, x5, plus a re-roll allowance). **Approval checkpoint:** the operator approves THIS batch (prompts + credit estimate + the chosen radius + material) before it runs. **Per-batch only:** no global always-allow; every future batch re-asks.

## 5. Blender role · DECISION: YES (a base object is worth it)
**Why yes:** THE ONE is a precision machined form (one continuous radius, clean walls, exact proportion). Higgsfield freehand will drift the radius, wall thickness, and edge crispness across the hero and the three variants, and the whole brand thesis is that the proportion is the signature. A Blender base gives a pixel-exact master geometry, perfectly consistent 3-angle references, and honest material tests that then drive Higgsfield (as reference/img-to-img) and Figma. It de-risks drift on the one object everything depends on.
**Build spec (ready to run on a go; needs the Blender app open with the MCP add-on, which the ledger lists UNTESTED):**
- Geometry: rounded-rectangle tray. Outer 240 x 160 x 28 mm. Wall 3 mm. Inner floor fillet r6, top rim fillet r8 (the signature). Slight 2-degree draft. One continuous radius, no dividers, no lid.
- Variants: duplicate the base, change only the rim radius to r4 / r8 / r12 for the variant grid.
- Materials (3 options to test): (a) bone-white ceramic (soft subsurface, matte glaze), (b) matte polymer (fine bead-blast finish), (c) brushed aluminum (anisotropic brushed metal, real edge highlights).
- Render: 3 angles, seamless white studio, one soft area light upper-left + a low fill, long quiet shadow. Top-down, 3/4 hero, macro edge. 4K, denoised, color-managed (Filmic/AgX neutral).
- Output: to `02_raw_generations/blender/` as the reference set for Higgsfield + Figma.
**If the operator prefers no Blender:** Higgsfield alone can carry it IF we lock one hero still first and reference-chain every variant to it (accepting some radius drift risk). Blender-first is the higher-ceiling path for a precision object.

## 6. Figma prototype plan (build on a go; assets-real-when-available)
- **Pages:** Home, Drops Archive, `/drops/the-one`, Signal-Capture state (vote + email + the-one-thing), in BOTH mobile-first and desktop frames.
- **Design system (a real Figma library):** color tokens (paper/bone/ink/soft/brass/white), type styles (editorial serif display + wide-tracked sans labels), the 9-grid, components (button, vote module WANT/MAYBE/PASS, email field, the mark, the placard, the drop card), spacing scale, 1px rule.
- **Assets:** use the real Higgsfield/Blender/Adobe finals as they complete; wireframe placeholders only until then, clearly labeled NOT-FINAL.
- Readiness: Figma MCP is UNTESTED in CLI (needs a live Figma file open). Staged to build on a go after the first hero assets exist (a page system with no real hero is a wireframe, not the deliverable).

## 7. Adobe finish pass (the polish checklist)
- Crop masters: cut the platform ratios (9:16, 1:1, 4:5, 2:3, 16:9, email) from the 4K master (Adobe crop is the PROVEN/ready layer).
- Color law: Adobe-neutral base, one accent (brass within range), no teal/orange; measure the white sweep RGB >=250; measure the brass against the token.
- Texture cleanup: remove dust, seams, stray reflections; keep material truth (do not over-smooth into plastic).
- Text-safe zones: caption-safe lower third for 9:16, masthead headroom, legible contrast on every overlay.
- Compression tests: per-platform export settings; check banding on the white sweep and the shadow.
- Platform exports: name and file each to `06_platform_masters/`.
- Final QA sheets: a contact sheet per asset to `07_qa_sheets/` for the External Visual Proof Gate.
(Adobe layers beyond crop are AMBER: one handshake test each before production reliance.)

## 8. Visual QA gate (no asset ships unless it passes ALL)
1. Stops the scroll in 1 second (at 120px thumbnail).
2. Looks expensive (material truth, light discipline, negative space).
3. Looks ownable (the proportion signature + the mark, unmistakably this brand).
4. Avoids generic AI gloss (no warp, no sheen haze, no melted edges; passes 200% zoom).
5. The object reads instantly (one object, one read).
6. The concept reads without explanation (subtraction is visible).
7. Beats the CSS placeholder by 10x (a side-by-side is not close).
8. Works as avatar AND grid tile AND drop-page hero AND ad AND email header (one asset, many crops, all hold).
9. Creates a "where can I get this" reaction.
Plus: passes the External Visual Proof Gate (a named human reviews the contact sheet before anything is called final or public).

## 9. File structure (created)
`MADE_WORLD_PIPELINE/` : `00_references` · `01_prompts` · `02_raw_generations` · `03_selects` · `04_adobe_finals` · `05_figma_exports` · `06_platform_masters` · `07_qa_sheets` · `08_signal_ledger`. The Demand Signal Ledger fields (21) live in `08_signal_ledger` per the Week 1 package.

## 10. Output summary + the next approval question
- **Pipeline map:** Blender base geometry (proportion lock) -> Higgsfield hero + variants (elite plates, per-batch) -> Adobe finish (crop/color/cleanup/masters) -> Figma page system (real assets) -> OS QA gate + External Visual Proof Gate -> platform masters + signal ledger. OS/Claude art-directs, prompts, boards, copy, and QA throughout.
- **First Higgsfield batch:** ready in `01_prompts/HIGGSFIELD_BATCH_001.md` (5 stills, ~20-30 credits, per-batch).
- **Figma page plan:** Home / Drops / the-one / signal-capture, mobile + desktop, with a real design-system library. Build on a go after the hero assets exist.
- **Blender decision:** YES, a base object (the spec in section 5), to lock the proportion before Higgsfield.
- **Adobe finish checklist:** section 7.
- **QA rubric:** section 8 (9 questions + the External Visual Proof Gate).
- **THE EXACT NEXT APPROVAL QUESTION BEFORE SPEND:** see the chat message. It asks you to pick the build order (Blender-base-first vs Higgsfield-direct), confirm the one creative input (chosen radius + material), and approve the capped Higgsfield Batch 001 credit estimate, per-batch only. Nothing runs until you answer.

---
*No posting, ads, payment rails, generation, or spend performed. Higgsfield is per-batch-approved (no global always-allow). Figma/Blender builds are staged on an explicit go (both UNTESTED in our ledger; require the app open). Grounded in the OS visual_grade / layout / world_character doctrine [certified] and the tool ledger. No product crowned.*
