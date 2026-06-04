# COMPOSITE_MASTER_QA · the campaign composite law

Canonical standard. Every SNIPED campaign composite (subject dropped into any generated or shot world) passes through these gates before it can be called believable, shown to a client, or placed in a deck. No exceptions, no "the workflow technically worked" passes.

Invoke as the `/composite-master-qa` skill. Mirror copy travels with each project (e.g. the Alma proof folder).

---

## Prime directive

The subject grade is LOCKED. The graded TIFF/PNG (color, skin, contrast, identity) is the base and is never reinterpreted, flattened, or re-skinned. All work under this law is ENVIRONMENT INTEGRATION only: making the locked subject sit inside the plate as if captured by the same camera, in the same light, on the same ground.

If a step would change the subject's color or skin, it is out of scope. Fix the environment, not the person.

---

## The 8 gates (all must pass)

### Gate 1 · Biological reality (subject edge + skin)
- Preserve flyaways and organic edge tension. Do NOT make hair helmet-perfect. Only remove individual hairs that cross eyes, lips, or read as distracting across the face.
- Preserve pores and skin micro-texture at 100% zoom. No waxy / plastic / commercial-volume Evoto skin.
- Protect garment and material edge complexity (lace, fringe, straps, ties, sheer). Do not simplify or gum up complex edges.

### Gate 2 · Relight to the plate
- Every plate has its own light logic. Read it: highlight direction, key warmth, bounce color, shadow flavor.
- Add believable rim / light wrap on hair, shoulders, arms, legs, and garment edges that matches the plate. Warm golden-hour plate to warm rim; cool plate to cool rim.
- The subject may not stay front-lit cool studio against a warm directional world.

### Gate 3 · Two-shadow grounding
- Every foot / contact point gets TWO shadows:
  - CONTACT shadow: tight, dark, flush directly under the sole/heel. No gap between sole and shadow.
  - CAST shadow: originates AT the sole (never offset / detached), extends in the plate's shadow direction, matches the plate's shadow softness, blur, opacity, and color.
- A detached or floating shadow blob is WORSE than no shadow and is an automatic fail.
- NO pure black shadows. Shadow color is sampled from the ground, darkened, never #000.

### Gate 4 · Surface interaction
- On sand / dirt / grass: sink the contact point slightly and create a displacement lip around the shoe base. Feet do not sit on top of a soft surface.
- On hard surfaces (tile / deck / road): occlusion darkening where the contact point meets the ground.

### Gate 5 · Transparent / reflective objects (e.g. clear acrylic heels)
- Clear acrylic / glass / patent surfaces cannot keep sterile studio reflections.
- Add warm ground-color reflection, slight refraction / distortion of the surface seen through the clear material, and proper occlusion where the object meets the ground.

### Gate 6 · Kill the cutout tell
- Subtle mask feather, 0.5 to 1 px depending on output size. No razor-sharp sticker perimeter.
- Defringe dark halos around hair, arms, legs.
- Add light wrap where bright sky / pool / window light would naturally bleed onto the subject edge.

### Gate 7 · Sensor match
- Match black point, white point, contrast curve, color temperature, and atmospheric softness between subject and plate.
- After everything is married, apply ONE global micro-grain / noise layer across the entire final so subject and world feel captured through the same sensor.

### Gate 8 · Artifact rejection (hard reject)
Any of these = automatic reject, rebuild or recrop the plate:
- AI generative-fill smear (e.g. stretched top/bottom of an over-extended crop)
- warped / melted geometry, broken architecture
- stretched pixels, repeated textures (repeated sand / foliage / brick)
- "barcode sky" banding
- melted / warped plants

---

## Ceiling gates (9-11) · master-tier, required for client-send

Gates 1-8 get a hero to LITE (feed-believable, daily IG, internal proof). Gates 9-11 are what separate LITE from CEILING (no software tell at 100% on phone, no embarrassment if a creative director zooms in). A client-send hero must pass all 11. The OpenCV/script chain is LITE; the ceiling pass is Photoshop + Camera Raw.

### Gate 9 · DOF / lens match
- The subject cannot be tack-sharp in a world with its own focus falloff. Build one believable shared focal plane: subject, foreground deck, mid plants, and far background must read as captured by a single lens.
- Depth-aware blur (more blur with distance from the subject plane), a hair of optical softness on the subject so it is not razor-crisp against soft surroundings, matched bokeh character.

### Gate 10 · Perspective / camera-height match
- Subject scale, foot plane, horizon line, and environment geometry must agree on one camera height and focal length. Check foreshortening against the plate's vanishing/horizon before any polish. If they disagree, fix placement first; no finish rescues a perspective mismatch.

### Gate 11 · Directional color bleed
- Not an even light-wrap band. Real, directional environmental light transfer: warm bounce from a warm deck onto the lower legs, cool fill from water/sky on the shadow side, foliage kiss only where geometry justifies it. Subject skin identity stays LOCKED; bleed lives on clipped low-opacity layers, never a skin regrade.
- extra or malformed limbs, fingers, teeth

---

## Scoring (per hero, each out of 10)

Score these nine axes. The first six gate LITE; axes 7-9 gate CEILING.

1. Lighting (relight match to plate)
2. Grounding (contact + cast, no float)
3. Edge (cutout invisibility, hair, defringe)
4. Color marriage (sensor / black point / temp match)
5. Artifact scan (Gate 8 clean)
6. Brand fit (concept discipline, see below)
7. DOF / lens match (Gate 9)
8. Perspective / camera-height match (Gate 10)
9. Directional color bleed (Gate 11)

Status values:
- LITE / INTERNAL: axes 1-6 >= 8. Feed-believable, daily IG, internal proof. NOT a client-send.
- CEILING / CLIENT-READY: ALL nine axes >= 8, no Gate-8 reject, and it survives a 100% phone zoom with no software tell. Only this tier goes to a client.
- REBUILD: a gate fails hard (e.g. floating heel, perspective mismatch). Do not show.

---

## Concept discipline

Physics passing is necessary, not sufficient. Brand fit also scores:
- The world must serve the brand and the product, not compete with it. If a prop (e.g. a red car) steals attention from the product (the swimsuit), control it.
- A pretty AI plate is not a concept. The world must be an intentional brand drop, or it fails brand fit even if the physics are perfect.

---

## Required proof (no "believable" without it)

For every hero, deliver:
- final no-text hero
- final text / drop-card version
- 100% crop of hair / edge
- 100% crop of feet / shadow (the contact point)
- before/after: studio frame to campaign
- QA scorecard (the six axes above)
- explicit status: client-ready / internal-only / rebuild

A summary that says "all believable" without the crops and scores is rejected on sight.

---

## Mandatory close-out (durability)

After any phase that changes a hero or its status, the operator updates the project `SESSION_STATE.md` (objective, files, passed, failed, per-hero status, next step, commands) and, if the project folder is a git repo, commits the milestone. This is non-optional and is why a restart never loses the work.
