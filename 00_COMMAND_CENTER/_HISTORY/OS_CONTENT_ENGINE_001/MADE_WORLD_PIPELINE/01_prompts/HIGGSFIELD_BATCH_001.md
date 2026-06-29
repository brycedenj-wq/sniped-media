# HIGGSFIELD BATCH 001 · THE ONE (per-batch approval required, not yet run)

Model: nano_banana_pro (drop to nano_banana non-pro then 4K upscale if moderation false-positives, though a desk tray should not trip it). Spend: per-batch only, no global always-allow. Estimate: ~20-30 credits (5 stills at ~2cr, plus a re-roll allowance). If a Blender base is built first, pass the Blender render as the reference image and use img-to-img to lock geometry; otherwise run text-to-image and lock the hero first, then reference-chain the rest.

GLOBAL STYLE (prepend to every prompt): "Editorial product still, seamless pure-white studio sweep, one object only, top-down or eye-level, soft single-source light from upper left with one long low-contrast shadow, quiet-luxury restraint, generous negative space, museum catalogue quality, photoreal material truth, shot on a 100mm macro, color-neutral (no teal, no orange)."

GLOBAL NEGATIVE (append to every prompt): "no text, no lettering, no logo, no brand mark, no hands, no people, no fingers, no reflections clutter, no busy background, no props, no dividers, no compartments, no lid, no warped geometry, no melted edges, no extra objects, no plastic AI sheen, no gloss haze, no oversaturation, no duplicate object, no watermark."

QUALITY CRITERIA (all must hold): white sweep RGB >=250; exactly one soft shadow; one continuous rim radius, crisp clean edges; believable material (no plastic-AI sheen); reads at a 120px thumbnail; passes 200% zoom with zero artifact; the proportion identical to the chosen variant.

---
### Image 1 · HERO (the money shot) · 1:1 master + 9:16 crop
"[GLOBAL STYLE] A single shallow undivided rectangular desk tray, one continuous gentle rim radius, no dividers, no lid, no labels, [CHOSEN MATERIAL: bone-white matte ceramic | matte bead-blast polymer | brushed aluminum], resting alone dead center on a seamless white surface, top-down three-quarter angle, soft long shadow to lower right, the only object in the frame. [GLOBAL NEGATIVE]"

### Image 2 · VARIANT GRID · 1:1
"[GLOBAL STYLE] Three identical shallow rectangular trays in one even row on seamless white, same material and same light, the ONLY difference is the rim corner radius: left tight, center medium, right soft. Equal spacing, identical scale, catalogue grid, top-down. [GLOBAL NEGATIVE]"

### Image 3 · BEFORE / AFTER PAIR · 1:1
"[GLOBAL STYLE] Two objects side by side on seamless white at identical scale and light: left, a busy molded organizer tray with many small compartments; right, a single empty shallow undivided tray. The only variable is the subtraction. Top-down, clean. [GLOBAL NEGATIVE]"

### Image 4 · RULE-OF-USE PLACARD STILL · 1:1 + 4:5
"[GLOBAL STYLE] The single shallow tray on seamless white with a small blank typeset placard card standing beside it (card left intentionally blank for text to be added later in Adobe), generous negative space, calm editorial composition, the status-object beauty shot. [GLOBAL NEGATIVE] (note: leave the placard blank, text is added in Adobe, never generated)"

### Image 5 · EDITION / PACKAGING STILL · 1:1
"[GLOBAL STYLE] A minimal bone-colored fiber-board box with a subtle deboss and a small round brass-foil seal, lid partly removed to half-reveal the single shallow tray inside on white tissue, quiet-luxury unboxing-as-object, one soft light, one shadow, no hands. [GLOBAL NEGATIVE] (the deboss and seal carry no readable text, mark is added in Adobe)"

---
APPROVAL CHECKPOINT: do not run until the operator (a) picks the build order (Blender-base-first or Higgsfield-direct), (b) confirms the chosen radius (r4/r8/r12) and the chosen material, and (c) approves the ~20-30 credit estimate for THIS batch only. After the run: selects to `03_selects/`, Adobe finish to `04_adobe_finals/`, contact sheet to `07_qa_sheets/`, then the QA gate + External Visual Proof Gate before anything is called final.
