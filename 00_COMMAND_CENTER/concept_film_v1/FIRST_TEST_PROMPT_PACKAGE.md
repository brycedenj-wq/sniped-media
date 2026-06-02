# FIRST_TEST_PROMPT_PACKAGE · BASEPLATE Concept Film v2

**Date:** 2026-05-28
**Status:** Runnable prompt package for the first 3-keyframe stills test. Anchor-class working draft. Not chunked. Not committed.
**Parent doc:** `00_COMMAND_CENTER/BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md` (v2)
**Doctrine:** Test the visual world (palette + operator + wordmark + literal baseplate motif) before committing credits to motion. Stills first; motion only after stills pass.

---

## Permission gate (locked)

**ASK before every generation in this test.** Do not set "always allow" globally. Treat this 3-still test as ONE permission unit (approve the batch as a whole). Subsequent tests are per-batch decisions.

If the Higgsfield MCP exposes a credit-cost preview, surface the estimate to BJ before running. If it does not, BJ approves on a per-batch basis using the Higgsfield UI's own credit display.

---

## What this test produces

3 keyframe stills, 16:9, 1 variation each (start with 1; if model wants 2-4 variants per call, set to 2 max):
1. Shot 1 still · THE OPERATOR, PRE-DAWN
2. Shot 3 still · THE CRAFT (with the literal industrial baseplate object)
3. Shot 6 still · THE WORDMARK

Skipping Shot 2 (motion-heavy), Shot 4 (Kling 3.0 motion), Shot 5 (overhead motion) in this first pass. Stills land first; motion follows after.

---

## Model, aspect, and global settings

- **Model:** Nano Banana Pro
- **Post-process:** Skin Enhancer on Shots 1 and 3 only (Shot 6 is type, no skin)
- **Aspect ratio:** 16:9
- **Variation count:** 1 per shot (2 max if the model defaults to multi-variant)
- **Soul ID:** if BJ has trained `@op`, use it for Shots 1 and 3. If not, use the archetypal operator described in the prompt; flag the result for "Soul ID needed before motion" if the character read is weak.
- **Reference images:** none for v1 stills (baseline test of the prompt language alone).

---

## MASTER STYLE block (paste into every prompt above the shot-specific copy)

> Cinematic anamorphic, large-format look. Palette locked: onyx black `#0F0F0F`, concrete grey `#8C8C8C`, single accent of blueprint blue `#0055FF`. Industrial precision, architectural brutalism, data-center-schematic mood. Low-key restrained lighting, deep shadow, soft volumetric haze. Quiet-luxury editorial, premium, serious. Subtle 35mm grain.
>
> NEGATIVE: no teal-and-orange grading, no cartoon, no 3D-render look, no stock-corporate vibe, no logos, no text artifacts, no warm skin glow, no shallow-dof bokeh-blur fashion-portrait look, no servers, no racks, no cabling, no equipment labels, no signage.

---

## Shot 1 prompt · THE OPERATOR, PRE-DAWN

**Aspect:** 16:9. **Model:** Nano Banana Pro. **Skin Enhancer:** yes (post). **Soul ID:** `@op` if trained, archetypal operator otherwise. **Output name:** `BASEPLATE_concept_v2_shot01_pre-dawn_v1.png`

> [MASTER STYLE]
>
> Wide composition. A lone man at a minimal steel desk in a vast dark industrial space. One screen glows faint blueprint-blue `#0055FF` on his face. The man is `@op`: still, focused, calm. Wearing a heavy work jacket in charcoal/deep grey, no logos, no patches, sleeves rolled, no watch. The space around him is cavernous, concrete and steel, mostly in deep shadow with subtle volumetric haze. Eye-level frame. Quiet command before the world wakes. Industrial precision, architectural brutalism, data-center-schematic mood. No racks, no servers, no equipment, no signage.
>
> Aspect 16:9, anamorphic large-format, subtle 35mm grain, low-key restrained lighting.

---

## Shot 3 prompt · THE CRAFT

**Aspect:** 16:9. **Model:** Nano Banana Pro. **Skin Enhancer:** yes (post). **Soul ID:** `@op` if trained, archetypal hands otherwise. **Output name:** `BASEPLATE_concept_v2_shot03_the-craft_v1.png`

> [MASTER STYLE]
>
> Tight insert. The desk surface in soft fill light. In the foreground, a machined steel industrial baseplate (mounting slab, brushed surface, four visible bolt holes, approximately 12 by 18 inches, slightly off-center, soft specular highlights on the edges). In the middle ground, deliberate hands at work on a clean keyboard or the proof document itself, editor's precision, sleeves rolled. In the background, a screen with a clean image being composed and a proof document taking shape, blueprint-blue `#0055FF` UI accents on the screen. No teal, no orange, no warm skin glow, no shallow-dof macro-blur. Onyx/concrete/blueprint-blue only.
>
> Composition reads left to right: baseplate in foreground, hands at center, screen at back.
>
> Aspect 16:9, anamorphic large-format, subtle 35mm grain, low-key restrained lighting.

---

## Shot 6 prompt · THE WORDMARK

**Aspect:** 16:9. **Model:** Nano Banana Pro. **Skin Enhancer:** no (type only). **Soul ID:** not used. **Output name:** `BASEPLATE_concept_v2_shot06_wordmark_v1.png`

> Pure onyx black background `#0F0F0F`. Centered, the word **BASEPLATE** in clean industrial type (Space Grotesk or equivalent geometric sans, semi-bold, restrained tracking, no kerning issues, no extra text artifacts). Beneath the wordmark, a single blueprint-blue `#0055FF` underline drawn left to right, 1pt to 2pt weight, restrained width (roughly 60% of wordmark width). Below the underline, smaller mono-style credit text reads: `Bryceden Jones, operator.` Below that on the same baseline group, optional one-line tagline in concrete grey `#8C8C8C`: `The operating layer underneath.`
>
> Render TWO variants: (A) with the tagline, (B) without the tagline. Both with the named-operator credit.
>
> NEGATIVE: no extra text, no logo lock-up, no decorative elements, no glow effects, no shadows, no client list, no CTA, no URL, no kerning artifacts, no garbled letters.
>
> Aspect 16:9.

---

## Output naming convention

Saved to `00_COMMAND_CENTER/concept_film_v1/outputs/` (BJ creates this dir or it gets created by the MCP if it has filesystem write):
- `BASEPLATE_concept_v2_shot01_pre-dawn_v1.png`
- `BASEPLATE_concept_v2_shot03_the-craft_v1.png`
- `BASEPLATE_concept_v2_shot06_wordmark_v1_A.png` (with tagline)
- `BASEPLATE_concept_v2_shot06_wordmark_v1_B.png` (without tagline)

If the MCP saves to Higgsfield's own gallery instead of local disk, BJ downloads the four PNGs to `concept_film_v1/outputs/` after the run.

---

## Evaluation rubric (run on each returned frame)

For each PNG, answer yes or no:

1. **Palette discipline.** Onyx `#0F0F0F`, concrete grey `#8C8C8C`, blueprint blue `#0055FF` only? Any teal or orange anywhere? Any warm tones? Any other accent color?
   - PASS = onyx/concrete/blueprint only, deep shadow held.
   - FAIL = any teal-orange leak, any warm cast, any extra color.

2. **Operator character (Shots 1 and 3).** Reads as gravitas, restraint, "off the floor"? Charcoal/black jacket, no logos, no watch, no jewelry? Or does it read warm-portrait, stock-corporate, or fashion-editorial?
   - PASS = restrained, operator-coded.
   - FAIL = warmth, gloss, or "lifestyle creator" energy.

3. **Architectural brutalism (Shot 1).** The space reads as structural and abstract industrial? Or as generic AI data-center with racks and cables creeping in?
   - PASS = concrete and steel, deep shadow, no equipment.
   - FAIL = racks, cabling, servers, labels, signage.

4. **Literal baseplate object (Shot 3).** The machined steel slab with bolt holes is clearly visible in foreground? Reads as an engineering object, not a vague metal panel? Brushed surface, four bolt holes legible?
   - PASS = recognizable as an industrial mounting baseplate.
   - FAIL = vague metal blob, ornamental shape, or absent.

5. **Wordmark legibility (Shot 6).** BASEPLATE letters clean, no kerning artifacts, no garbled glyphs? Blueprint-blue underline draws clean and uniform? Named-operator credit legible? Tagline legible (variant A)?
   - PASS = type renders without artifacts.
   - FAIL = any letter distortion, extra characters, kerning glitches, broken underline.

6. **Soul ID need (post-test).** Does the archetypal operator read strongly enough in Shots 1 and 3, or do the figures feel generic? If generic, BJ trains Soul ID before motion generation.
   - PASS = character has weight and specificity (Soul ID optional for motion).
   - FAIL = generic figure (Soul ID required before motion).

**Note (2026-05-28):** Soul ID training is deferred per the Soul ID · DELAYED section in `BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md`. The archetypal-operator outcome is now the locked register until Soul training resumes. Rubric item 6 is no longer a gate; the "soft-fail" reading from the first-test rubric is reinterpreted as the intended outcome.

---

## Decision tree after the test

- **All 5 frames pass (Shots 1, 3, 6A, 6B, all rubric items) →** lock the visual world. Proceed to Shot 2 + Shot 4 motion test in a new batch (separate permission gate).
- **3-4 frames pass →** iterate the failing prompts (tighten the negative block, adjust the operator styling line, refine the baseplate object description). Re-run the failing shots only. Hold motion until all stills land.
- **0-2 frames pass →** step back. Either the MASTER STYLE block needs sharpening (rare; the v2 doc went through audit) or Nano Banana Pro is not the right model for this register. Test one alternative model on Shot 1 before broader changes.

**Note (2026-05-28):** Motion test (Shot 2 + Shot 4) proceeds with archetypal / partial-identity per the Soul ID delay decision in `BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md`. Soul ID is not a gate to the motion batch. Motion prompts should follow the non-face-forward operating constraint (silhouette / hands / shadow / environment / scale).

---

## What this test does NOT do

- Does NOT generate motion (Shots 2, 4, 5 are deferred until stills land).
- Does NOT use reference images (baseline test of the prompt language alone).
- Does NOT commit any frame to public use. All outputs are concept atmosphere only.
- Does NOT touch SNIPED surfaces. BASEPLATE-only.
- Does NOT replace the dossier as proof. This is brand atmosphere, not evidence.

---

## Guardrails (carry through every production batch)

- AI is atmosphere, not evidence. No fake client proof, no fake facilities, no fake crews, no fake metrics, no fake testimonials.
- No platform/registry/network public claim anywhere in the film or its caption.
- No photography-only reduction. The film is BASEPLATE atmosphere; SNIPED is separate.
- No SNIPED merge. The asset never crosses to snipedmedia or SNIPED handles.
- No employer-sensitive imagery. No real secure floors, no equipment labels, no badges, no facility identifiers.
- Permission gates ON for every credit-spending generation. Never set "always allow" globally.
- Brand-bible palette only (onyx / concrete / blueprint blue). No teal-and-orange grading.
- Anchor-class: not chunked, not in master files, total_chunks unchanged at 1,837.
