# Lightroom Operating System · SNIPED

The practical operating layer for Lightroom Classic inside SNIPED's production pipeline. This document defines the catalog architecture, import discipline, organization system, develop preset chain, masking stack, retouch decision tree, and export discipline.

This is a runbook, not a tutorial. If a step is unclear, the underlying mechanic is in the Udemy Lightroom course (Section references in `/10_REFERENCE/UDEMY_LIGHTROOM_EXTRACTION.md`). This doc tells you what SNIPED does, not how Lightroom works.

**v3 LUXURY SUPERSESSION (2026-05-12 · Lock 1 + Lock 7 of OPERATING_LOCKS):**
- The locked base preset is now `SNIPED_LOCKED_LOOK_v3_LUXURY` (Adobe Neutral base · quiet luxury editorial restraint · Meisel/Roversi lane)
- v1 (`SNIPED_LOCKED_LOOK_v3_LUXURY` · Adobe Portrait base) is RETIRED
- v3 LUXURY is the ONLY editing style going forward · no alt edits, no experimental branches, no client-specific re-grades
- The mask kit (Section 6) stays · the BASE profile is what changed
- HEX palette locked: #2A2A2E shadow · #B8956E skin · #C9B7A3 mid · #F5EFE6 highlight
- Camera profile: Adobe Neutral (NOT Adobe Portrait · NOT Camera Standard · NOT Adobe Color)
- See `/05_PRODUCTION/_preset_backups/SNIPED_LOCKED_LOOK_v3_LUXURY.xmp` for the preset XMP
- See `/00_BRIEF/OPERATING_LOCKS_2026-05-12.md` for the rationale

Where this doc references `SNIPED_LOCKED_LOOK_v3_LUXURY` or "Adobe Portrait" or "Camera Standard," READ v3 LUXURY · Adobe Neutral. The v1 references below are legacy artifacts pending full sweep but the operating decision is locked.

Cross-references:
- Strategic shape and time targets: `/00_BRIEF/PRODUCTION_OS.md` Section 2
- Step-by-step procedural detail: `/05_PRODUCTION/SOP_capture_to_delivery.md`
- Preset definitions: `/05_PRODUCTION/preset_library.md`
- Future retoucher onboarding: `/05_PRODUCTION/retoucher_training_notes.md`

---

## 1. Catalog architecture

### 1.1 One master catalog per year

- Path: `/SNIPED_PRODUCTION/_catalogs/SNIPED_YYYY.lrcat`
- All shoots in a year live in this catalog. Smart Collections do per-shoot organization.
- Why: global search across the year, single backup target, archive is one file.
- Year-over-year: at January 1, create `SNIPED_2027.lrcat` from a duplicate of the previous year's catalog with Heroes-only retained. Selects + Proofs from prior year remain in the prior catalog (still readable, just not in the current working catalog).

### 1.2 Backup discipline (catalog level)

- Lightroom catalog backup: every launch (auto-prompted on quit). Set to `/SNIPED_PRODUCTION/_catalogs/_backups/`.
- Keep last 30 days of catalog backups. Older auto-purge.
- Catalog file lives on Hot SSD. Never on cloud sync (catalog file conflicts under sync).

### 1.3 Catalog hygiene (quarterly)

- Delete unused develop presets quarterly
- Optimize catalog (File → Optimize Catalog) quarterly
- Smart Previews older than 12 months on archived shoots: discard (frees disk)
- Verify Smart Collection rules still match the locked SNIPED system (Section 3)

---

## 2. Import discipline

### 2.1 The locked import preset

Name: `SNIPED · IMPORT DEFAULT`

| Setting | Value |
|---|---|
| File handling | Add (if already in `/SNIPED_PRODUCTION/`) OR Copy (if from SD card) |
| Build previews | Standard |
| Build Smart Previews | ✅ ON |
| Don't import suspected duplicates | ✅ ON |
| Apply Develop preset | `SNIPED_LOCKED_LOOK_v3_LUXURY` |
| Apply Metadata preset | `SNIPED_COPYRIGHT_2026` (update annually) |
| Apply Keywords | shoot-type tag (manually entered per import: `Reset`, `FreeCollab`, `OpKit`, `BrandSystem`, `CulturalDoc`, etc.) |
| Destination (SD card import) | `/SNIPED_PRODUCTION/YYYY/YYYY-MM-DD_Client_TYPE/10_RAW/` |
| Assisted Culling at import | Subject focus + Eye focus (eyes open) ✅ ON |

### 2.2 Why Smart Previews

Smart Previews are the SNIPED travel-mode unlock. They let BJ edit on the road without the SSD plugged in. Cost: ~2-5 GB per typical shoot of Smart Previews. Benefit: every engineering travel week becomes potential edit time.

### 2.3 Import keywords (locked vocabulary)

Always tag at import. Keywords drive Smart Collections (Section 3):

- **Shoot type:** `Reset`, `Sprint`, `OpKit`, `BrandSystem`, `FreeCollab`, `FreeCommunity`, `FreeAccess`, `Personal`, `ArtSeries`, `CulturalDoc`, `BTSDay`
- **Subject role (optional):** `Founder`, `Operator`, `Artist`, `Institution`, `Couple`, `Group`
- **Cluster (optional, when applicable):** `LA-Founder`, `Series-A`, `Series-B`, `LA-Black-Founder`
- **Visual register (optional):** `Mono`, `Commercial`, `Studio`, `Editorial`, `Graphic` (the 3-of-5 aesthetic filter)

Keywords are append-only. Do not delete a keyword unless it was a typo. Future Smart Collections rely on them.

---

## 3. Organization system

### 3.1 Color label vocabulary (locked)

| Color | Meaning | Stage |
|---|---|---|
| Red | Heavy retouch / Photoshop comp required | Post-cull, on Hero candidates |
| Yellow | Standard Evoto pass · default Hero workflow | Post-cull, on Hero candidates |
| Green | Hero candidate · portfolio / Brand System tier | Post-Hero edit |
| Blue | VIB asset candidate · paired with another frame | Post-Hero edit |
| Purple | Case study / IG carousel candidate | Post-Hero edit |
| (none) | Standard Select or Proof | Default |

Color labels stack with star ratings. Both run.

### 3.2 Star rating vocabulary (locked, do not change)

| Stars | Meaning |
|---|---|
| ⭐⭐⭐⭐⭐ | Hero candidate / Hero (after edit) |
| ⭐⭐⭐⭐ | Select tier |
| ⭐⭐⭐ | Proof tier |
| ⭐⭐ | Hold for review (rare) |
| ⭐ | (not used in SNIPED · noise) |
| (none) | Unprocessed or rejected (X flag) |

### 3.3 Flag vocabulary

| Flag | Meaning |
|---|---|
| Pick (P) | Used during Pass 1 Pick pass · upgrades to star rating in Pass 3 |
| Reject (X) | Permanent reject · auto-hidden in working filters |
| Unflagged | Default / pending decision |

### 3.4 Smart Collection set (locked)

All inside one Collection Set named `SNIPED · SMART`. Build once in `SNIPED_2026.lrcat`, applies forever.

| # | Collection | Rule |
|---|---|---|
| 00 | Heroes Live | Rating ⭐⭐⭐⭐⭐ AND color = Green |
| 01 | Heroes Pending Retouch | Rating ⭐⭐⭐⭐⭐ AND (color = Red OR color = Yellow) |
| 02 | VIB Pool | Color = Blue |
| 03 | Case Study Pool | Color = Purple |
| 04 | This Month | Capture date is in past 30 days |
| 05 | Last 90 Days | Capture date is in past 90 days |
| 06 | Selects (4-star) | Rating = ⭐⭐⭐⭐ |
| 07 | Proofs (3-star) | Rating = ⭐⭐⭐ |
| 08 | Cultural Doc Heroes | Keyword = CulturalDoc AND Rating ⭐⭐⭐⭐⭐ |
| 09 | Reset Deliveries | Keyword = Reset AND color = Green |
| 10 | By Lens · Fuji 56mm | Lens = "XF 56mm F1.2 R WR" (or BJ's actual lens nomenclature) |
| 11 | Needs Photoshop | Color = Red |

These are the only smart collections. Resist adding more · they multiply complexity.

### 3.5 Manual Collection sets (per-shoot delivery)

Inside a separate Collection Set named `SNIPED · DELIVERIES · 2026`:
- One sub-collection per shoot, named: `YYYY-MM-DD_Client_TYPE`
- Contains: ⭐⭐⭐⭐⭐ Heroes for that shoot, the manual hand-picked group
- This is what gets exported to Pixieset

Manual collections are output-facing. Smart collections are pipeline-facing. Both run.

---

## 4. Cull workflow (compressed via assisted culling)

### Pass 0 · Assisted cull (at import, automatic)

Lightroom AI auto-flags rejects on subject focus + eye focus + exposure + duplicates.
Time: 0 manual minutes. Saves 30-45 min vs. manual Pass 1.

After import, briefly review the auto-rejects in Library Filter set to "Rejected." Look for false rejects (genuinely good frames the AI missed). Right-click → Mark as Pick to recover.

### Pass 1 · Manual reject pass (refinement)

- Filter to: Unflagged + Picked (hide auto-rejects)
- Press X on any frame the AI missed (genuinely unusable)
- Press P on any frame that should advance
- Time: 5-8 min

### Pass 2 · Star rating

- Filter to: Picks only
- Number keys 3 / 4 / 5 to rate Proof / Select / Hero candidate
- Time: 10-15 min

### Pass 3 · Color label

- Filter to: ⭐⭐⭐⭐⭐ only
- For each Hero candidate, apply color label per Section 3.1:
  - Red: needs Photoshop / heavy comp
  - Yellow: standard Evoto pipeline
- Time: 2-3 min

### Pass 4 · Hero count check

- Filter to: ⭐⭐⭐⭐⭐ only
- Count: target 8-12 Heroes per Reset (per `/01_OFFERS/delivery_architecture_v2.md` Section 2)
- If count > 12: prune to 12 by promoting lower candidates back to ⭐⭐⭐⭐ Select
- If count < 8: review ⭐⭐⭐⭐ Selects for promotion candidates

Total cull time target: **15-25 minutes per Reset** (down from 30-60 min in PRODUCTION_OS Section 2.2 prior).

---

## 5. Develop workflow

### 5.1 The base layer (auto, on import)

Every photo lands with `SNIPED_LOCKED_LOOK_v3_LUXURY` already applied via the import preset. This includes:
- Camera profile (Adobe Neutral · LOCKED per v3 LUXURY supersession · was Camera Standard or Adobe Color in v1)
- Lens corrections ON
- Chromatic aberration removal ON
- White balance: As Shot (manual override per-image)
- Tone curve: SNIPED locked S-curve
- HSL: SNIPED locked color block
- Color Calibration: SNIPED signature shifts
- Sharpening: 40 (raw default)
- Noise reduction: 25 color (default)

The base layer sets the visual signature. Per-image work is deviation, not creation.

### 5.2 Per-image adjustment order (locked)

For Hero edits, work this order. Do not skip steps. Do not jump around.

1. **Crop** (always rule-of-thirds upper-third for face)
2. **White Balance manual** (refine if As Shot is off)
3. **Tone basic** (exposure, contrast, highlights, shadows, whites, blacks)
4. **Presence** (texture: 0 to slight negative for skin · clarity: -10 to 0 for skin · vibrance: small positive · saturation: leave 0 unless intentional)
5. **HSL refinement** (per-image deviations from preset HSL)
6. **Detail / Noise** (verify defaults appropriate · only adjust if problem visible)
7. **Lens corrections / Transform** (verify no geometry issues)
8. **Effects** (vignette: usually skip for SNIPED · grain: skip unless editorial register call)
9. **Masking** (Section 6)
10. **Final review** (toggle Before/After with `\` key · is the edit doing what it should?)

### 5.3 Time targets

| Output tier | Time per frame |
|---|---|
| Hero (full pipeline) | 12-15 min |
| Select | 1-2 min |
| Proof | 30-45 sec (batch) |

Hero time over 25 min: stop. Either downgrade to Select or escalate to Photoshop.

---

## 6. Masking stack (the AI subject + face standard)

### 6.1 The locked SNIPED mask stack

Apply on every Hero. Order matters · the masks compound.

| # | Mask | Tool | Adjustment |
|---|---|---|---|
| 1 | Subject | AI · Select Subject | Slight exposure +0.10 to +0.20 · slight clarity -5 |
| 2 | Face skin | AI · Select Person → Face Skin | Skin tone refine · gentle softening (texture -10) · slight warm shift |
| 3 | Eyes | AI · Select Person → Eye Sclera + Iris/Pupil | Sclera: whites lift +8 (NOT more · over-whitening reads fake). Iris: clarity +15, slight saturation +5 |
| 4 | Teeth (if visible) | AI · Select Person → Teeth | Whites lift +10, slight desaturation of yellow |
| 5 | Background | AI · Select Subject → Invert | Subtle exposure -0.20, color shift toward palette, slight vignette via radial |

Total mask stack time: 60-90 sec per Hero once locked.

### 6.2 Generative Remove for in-Lightroom cleanup

Use BEFORE deciding "do we need Photoshop?"

Best for:
- Background distractions (chairs, signs, light stands, coiled cables)
- Wall blemishes and texture mismatches
- Small skin issues that Evoto won't catch (stray hair, eye floater)

Not for:
- Anything that changes the subject's identity (nose, jaw, body shape)
- Compositing larger than 5% of frame
- Anything that should be a Photoshop job

### 6.3 Copy-paste mask propagation

After Hero #1 is fully edited:
1. Cmd+Shift+C (Copy Settings)
2. Check: Develop settings + Masks
3. Cmd+Shift+V on Heroes 2-N
4. Lightroom auto-re-runs the AI subject detection on each new image
5. Per-image touch up: WB drift, exposure for face position, mask refinement

This is the load-bearing speed unlock. A 12-Hero shoot takes the mask stack once, not 12 times.

---

## 7. Retouch decision tree (the load-bearing question)

For each Hero candidate after Lightroom develop is complete, walk this tree:

```
Q1: Is the frame structurally clean (no major comp, no liquify, no body work)?
  └─ YES → Q2
  └─ NO  → ROUTE: Lightroom + Evoto + Photoshop (red label confirmed)

Q2: Did Lightroom Generative Remove handle the small distractions?
  └─ YES → Q3
  └─ NO (still has 2+ distractions) → ROUTE: Lightroom + Photoshop (skip Evoto for distractions, Evoto first for skin if needed)

Q3: Does the skin need professional retouch beyond AI masks?
  └─ YES → ROUTE: Lightroom → Evoto → back to Lightroom for Hero finish
  └─ NO  → ROUTE: Lightroom only (Hero finish preset, export)

Q4 (optional): Is this a Brand System tier frame requiring frequency separation, dodge-and-burn, or compositing?
  └─ YES → ROUTE: Lightroom → Evoto → Photoshop → back to Lightroom for final export
  └─ NO  → already routed by Q3
```

### What makes a frame worth full retouch (Q4 yes)

- Brand System tier client (not Reset, not Op Kit basic)
- The frame is a Hero (Green color label promoted)
- The frame is one of 8-12 in the deliverable set, not 30+
- The frame is a face-forward portrait at 70%+ frame size where skin reads at full detail
- The frame is a portfolio anchor candidate (will appear on Carrd, in Op Kit pitches, in case studies)
- The client paid Brand System tier pricing OR the shoot was strategic free where SNIPED gets reach in trade

A Reset frame DOES NOT trigger Q4 yes. Reset is Lightroom + Evoto. Period.

### What "before Evoto" means

Before Evoto = Lightroom finishes:
- All develop work
- All AI masks
- All generative removes
- Crop locked
- WB locked
- Color grade locked
- Skin frequency NOT yet refined (Evoto's job)

Evoto receives a 16-bit TIF at full res with all of the above already applied. Evoto only does skin work and body refinement.

### What "after Evoto" means

After Evoto = Lightroom Hero Finish:
- Re-import Evoto's TIF output
- Apply `SNIPED_HERO_FINISH_v1` preset (final grain + final saturation tweak + final tone curve roll)
- Final crop verification
- Export per `SNIPED · Hero · JPG Deliverable` preset

### What Evoto is for

- Skin retouch (blemishes, texture, pore preservation, dark circles, gentle wrinkle reduction)
- Backdrop color change / refinement within studio register (change the in-camera backdrop color to optimize per model's outfit / skin tone)
- Backdrop cleanup (wrinkles in vinyl, color banding, distractions)
- Backdrop replacement to another solid color or simple textured background (still studio register · NOT a fake environment)
- Body subtle (gentle reshape · never aggressive)
- Eye / teeth refinement on top of Lightroom masks if needed

### What Photoshop is for

ONLY when the studio register breaks · the subject is being placed into a generated cinematic environment with depth / perspective / lighting story:
- Full environment compositing (Gress Track B playbook · subject in a stadium, rooftop, hotel suite, urban tunnel, etc.)
- Frequency separation beyond Evoto's capability
- Liquify / proportion adjustment (rare · use with extreme restraint, never on Reset)
- Dodge-and-burn at editorial register (Brand System tier, portfolio anchor)
- Manual hair masking when AI fails on a complex composite

NEVER:
- Generic skin work (that's Evoto)
- Color grading (that's Lightroom)
- Backdrop color changes within studio register (that's Evoto)
- Backdrop cleanup (that's Evoto)
- Spot removal (that's Lightroom Generative Remove)
- Eye whitening (that's Lightroom mask)
- Anything that could be done in Lightroom in 60 seconds or Evoto in 30 seconds

### The Evoto vs Photoshop line

- **Evoto** · the studio register stays. The shot is still "founder in studio." Backdrop color, cleanup, refinement happen here.
- **Photoshop** · the studio register breaks. The shot is "founder in a different environment." Full compositing with Harmonize + edge lights + grain unification happens here.

---

## 8. Export discipline

### 8.1 Export presets (locked)

All defined in `/05_PRODUCTION/preset_library.md` Section 4. Built once in Lightroom, used forever.

The 9 SNIPED export presets:
1. `SNIPED · Hero · JPG Deliverable`
2. `SNIPED · Hero · TIF Master`
3. `SNIPED · Select · JPG`
4. `SNIPED · Proof · JPG`
5. `SNIPED · IG Carousel Portrait`
6. `SNIPED · LinkedIn POV`
7. `SNIPED · Carrd Selected Work`
8. `SNIPED · Press Submission`
9. `SNIPED · VIB Asset Pair`

### 8.2 Export destination discipline

Each preset writes to a defined subfolder inside the shoot folder:
- Heroes (JPG + TIF) → `/30_HEROES/`
- Selects → `/40_SELECTS/`
- Proofs → `/50_PROOFS/`
- Content (carousel, POV) → `/80_CONTENT/`

The destination is part of the preset. No manual folder selection.

### 8.3 What never gets exported

- Watermarked output (the work signs itself)
- Sub-1080px web exports (collapses brand register)
- AdobeRGB for web (color shifts on browsers · always sRGB for web/social)
- Anything from a Smart Preview only (must have original or 1:1 preview to export · Lightroom warns on this)

---

## 9. The single integrated rule

**Lightroom is the spine. Evoto is the skin specialist. Photoshop is the surgeon. AI is the assistant.** Most frames live entirely inside Lightroom. Some travel to Evoto. Few visit Photoshop. None get generated.

Speed comes from the locked rails: one catalog, one import preset, one develop preset, one mask stack, one decision tree, nine export presets. Discipline comes from refusing to deviate without reason.
