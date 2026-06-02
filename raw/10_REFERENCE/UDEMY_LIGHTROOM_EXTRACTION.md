# Udemy Lightroom Course · Tactical Extraction Map

Source: `/Users/sniper/Downloads/lighroom course.docx` (40,785 lines, 222,450 words, 41+ section TOC covering Lightroom Classic + Lightroom CC).

Treatment: workflow / craft extraction. NOT strategy. The course covers Lightroom basics through advanced masking, presets, exports, modules, and AI features. Most of the content is beginner-tier explanation BJ already operates above. The extractable layer is workflow architecture decisions and discipline patterns that deepen the existing PRODUCTION_OS pipeline.

Classification rule: keep only what makes editing faster, cleaner, more consistent, more premium, or onboardable to a future retoucher.

---

## USE NOW · 16 items

### A · Catalog architecture (decisions to lock now)

#### 1. One master catalog per year, NOT per shoot
**Pattern:** annual catalog (e.g., `SNIPED_2026.lrcat`) holds all shoots. Smart Collections do the per-shoot organization. Course confirms this is the pro standard.
**Maps to:** `PRODUCTION_OS.md` Section 1.2 workspace folder structure. Add: `/SNIPED_PRODUCTION/_catalogs/SNIPED_YYYY.lrcat`
**Improves:** consistency · global search across all shoots · year-end archive is one file
**Action:** create `SNIPED_2026.lrcat` if it does not already exist. Migrate any per-shoot catalogs into it.

#### 2. Folder-on-disk discipline matches the catalog
**Pattern:** disk folder structure (YYYY > YYYY-MM-DD_Client_TYPE) IS the import destination. Lightroom mirrors disk, never auto-creates date folders.
**Maps to:** `PRODUCTION_OS.md` Section 1.1 (already locked). Reinforce in import preset.
**Improves:** archive integrity. Disk and catalog never drift.
**Action:** verify Lightroom import preset uses "Add" not "Copy" or "Move" when source is already inside `/SNIPED_PRODUCTION/`. For SD card imports, use "Copy" with custom destination matching the YYYY-MM-DD_Client_TYPE pattern.

#### 3. Smart Previews built on import for travel + speed
**Pattern:** Smart Previews are smaller proxy files Lightroom edits when the original is unavailable. Allow editing without external SSD plugged in.
**Maps to:** Lightroom OS doc · import settings
**Improves:** time on engineering travel weeks (per OPERATIONAL_BACKBONE Section 2 lean-override). BJ can edit on plane, in hotel, between meetings without dragging the SSD.
**Action:** Lightroom Import dialog → File Handling → check "Build Smart Previews." Make this the default in the saved import preset.

### B · Import discipline (one preset, applied every time)

#### 4. Saved import preset with metadata + develop preset + smart previews
**Pattern:** course Section 1 import demonstrates that import settings can be saved as a preset. SNIPED has not been doing this consistently.
**Maps to:** Lightroom OS doc
**Improves:** time + consistency. Import in 30 seconds not 3 minutes.
**Action:** create `SNIPED_IMPORT_DEFAULT` preset with:
- File handling: build Standard previews + Smart Previews
- Don't import suspected duplicates: ON
- Apply during import → Develop Settings: `SNIPED_LOCKED_LOOK_v1`
- Apply during import → Metadata: `SNIPED_COPYRIGHT_2026`
- Apply during import → Keywords: shoot type tag (Reset / FreeCollab / OpKit / BrandSystem / CulturalDoc)

#### 5. Metadata + copyright preset (one-time setup)
**Pattern:** course Section 17643 covers copyright presets. Every photo SNIPED ships should have copyright stamped.
**Maps to:** new file `/05_PRODUCTION/lightroom_metadata_preset.md`
**Improves:** quality (professional polish) + legal hygiene (proof of authorship) + downstream license enforcement
**Action:** create `SNIPED_COPYRIGHT_2026` metadata preset:
- Creator: Bryceden Jones
- Creator URL: snipedmedia.com
- Copyright: © 2026 SNIPED Media. All rights reserved.
- Copyright Status: Copyrighted
- Rights Usage Terms: per Op Kit MSA / collaboration release
- Email: bryceden@snipedmedia.com (or appropriate)
Update the year value annually each January 1.

#### 6. Assisted Culling at import (AI focus + eye filter)
**Pattern:** course Section 2111 demonstrates the new Lightroom assisted culling that auto-rejects out-of-focus, eyes-closed, blink, exposure-mismatch frames at import time.
**Maps to:** `PRODUCTION_OS.md` Section 2.2 cull workflow (currently 30-60 min · this can compress to 15-30 min)
**Improves:** time. Saves 30-45 min on a typical Reset cull.
**Caveat:** assisted culling is not perfect. Use as Pass 0 (auto-reject obvious failures). Manual passes 1-4 still run. Don't trust the AI to make final calls.
**Action:** add Pass 0 to the cull workflow. Verify at the end that no genuine keepers got auto-rejected by checking the rejected pool in grid view at filter strength "low."

### C · Organization system (color labels + smart collections)

#### 7. Color label system locked to production stage
**Pattern:** course Section 1814-2020 covers color labels. SNIPED has been using ratings + flags but not color labels. Color label adds a third dimension that tracks production stage, not just quality.
**Maps to:** Lightroom OS doc · culling section + new addition to PRODUCTION_OS Section 2.2
**Improves:** consistency · downstream routing · retoucher onboarding
**The locked SNIPED color label system:**
| Color | Meaning | When applied |
|---|---|---|
| Red | Heavy retouch / Photoshop comp required | After cull, on Hero candidates needing skin work, comp, liquify |
| Yellow | Standard Evoto pass · default Hero workflow | After cull, on Hero candidates needing only standard pipeline |
| Green | Hero candidate · Brand System / portfolio tier | After Hero edit complete · qualifies for portfolio promotion |
| Blue | VIB asset candidate · pair with another frame | After Hero edit · proof-of-range pair selected |
| Purple | Case study / IG carousel candidate | After Hero edit · narrative content material |
| (none) | Standard select or proof tier | Default · no label needed |

**Action:** apply this system going forward. Update PRODUCTION_OS Section 2.2 to include the color label step after the star pass.

#### 8. Smart Collections automate the routing
**Pattern:** course Section 2376-2507 covers Smart Collections with multi-rule logic. Smart Collections rebuild themselves automatically based on metadata, rating, color label, capture date.
**Maps to:** Lightroom OS doc
**Improves:** consistency · zero manual sorting · retoucher onboarding
**The locked SNIPED smart collection set:**
| Collection | Rule | Purpose |
|---|---|---|
| **00 · Heroes Live** | Rating ⭐⭐⭐⭐⭐ AND color = Green | Portfolio-ready Heroes |
| **01 · Heroes Pending Retouch** | Rating ⭐⭐⭐⭐⭐ AND color = Red OR Yellow | Active edit queue |
| **02 · VIB Pool** | Color = Blue | VIB asset candidates |
| **03 · Case Study Pool** | Color = Purple | LinkedIn POV / IG carousel material |
| **04 · This Month** | Capture date in past 30 days | Active period |
| **05 · Last 90 Days · Active Pipeline** | Capture date in past 90 days | Pipeline window |
| **06 · Selects (4-star)** | Rating = ⭐⭐⭐⭐ | Selects tier output pool |
| **07 · Proofs (3-star)** | Rating = ⭐⭐⭐ | Proofs tier output pool |
| **08 · Cultural Doc Heroes** | Keyword = CulturalDoc AND Rating ⭐⭐⭐⭐⭐ | Cultural Documentation portfolio |
| **09 · Reset Deliveries** | Keyword = Reset AND color = Green | Reset client portfolio |
| **10 · By Lens (Fuji 56)** | Lens = XF 56mm F1.2 | Lens-specific portfolio (per-lens grade calibration) |

**Action:** create these 10 smart collections in the master catalog. Store inside a Collection Set named `SNIPED · SMART`.

### D · Develop discipline (the locked look)

#### 9. SNIPED locked-look develop preset (the visual signature)
**Pattern:** course Sections 23-41 cover every Develop module slider. The professional path is to encode signature looks as develop presets, then deviate per-image, never per-image-from-scratch.
**Maps to:** `/05_PRODUCTION/preset_library.md` (new file)
**Improves:** consistency (every Hero starts from the same baseline) + speed (12-15 min/Hero target requires preset baseline) + onboardability (retoucher gets a defined starting point)
**Action:** lock the v1 preset chain in `/05_PRODUCTION/preset_library.md`. Three core presets:
- `SNIPED_LOCKED_LOOK_v1` (the import-default preset · imports + base WB + lens corrections + tone curve + HSL + calibration)
- `SNIPED_HERO_FINISH_v1` (post-Evoto · subtle clarity drop on skin + grain + final color grade)
- `SNIPED_PROOF_BATCH_v1` (the volume preset for 100-proof tier)

#### 10. Tone Curve as part of the locked look (not per-image)
**Pattern:** course Section 30 (Tone Curve) shows the curve is where signature looks live. SNIPED currently does this per-image · this is a leak.
**Maps to:** `SNIPED_LOCKED_LOOK_v1` preset
**Improves:** consistency. The "SNIPED look" reads consistent across shoots only when the curve is stable.
**Action:** lock one tone curve in the preset. Mild S-curve, slight lift in the shadows for crushed-black avoidance, slight roll in the highlights for skin protection.

#### 11. Color Calibration tab (the underused signature layer)
**Pattern:** course Section 40 (Calibration) is where pro photographers create truly differentiated looks. Most photographers ignore it. The calibration sliders shift the entire color foundation, not just sections.
**Maps to:** `SNIPED_LOCKED_LOOK_v1` preset
**Improves:** quality (genuine signature, not a generic preset) + differentiation (most photographers do not touch calibration)
**Action:** experiment with calibration sliders against 3-5 representative SNIPED frames. Lock the values into the preset. Re-evaluate quarterly.

### E · Masking + retouch routing

#### 12. AI Subject + Background masks for portrait consistency
**Pattern:** course masking sections demonstrate Lightroom's AI subject + background separation, including auto-detect for face, skin, eyes, teeth, hair, sky.
**Maps to:** `lightroom_operating_system.md` masking section
**Improves:** quality (every portrait gets the same mask treatment) + speed (replaces manual brush masking)
**Action:** standardize the SNIPED mask stack on every Hero:
- Mask 1: Subject (AI detect) · slight exposure lift, slight clarity drop
- Mask 2: Face / Skin (AI detect inside subject) · skin tone refinement, gentle softening
- Mask 3: Eyes (AI detect) · whites brightened low (~+8), iris clarity bumped low (~+15)
- Mask 4: Teeth (AI detect, only if visible) · whites brightened low (~+10)
- Mask 5: Background (AI detect) · subtle exposure shift away from subject, color shift toward palette
This stack runs in 60-90 seconds via copy-paste-with-masks once locked.

#### 13. Generative Remove for in-Lightroom cleanup
**Pattern:** course Section 41 covers the Generative AI Remove tool. This replaces basic Photoshop spot work for backgrounds.
**Maps to:** `lightroom_operating_system.md` retouch decision tree
**Improves:** time. Most background distractions clear in Lightroom now without round-tripping to Photoshop.
**Caveat:** generative AI here is utility · same Berger / Sax line from the prior tactical extraction. Never used to generate the subject. Backgrounds and small distractions only.
**Action:** add to retouch decision tree as the first cleanup pass before deciding "do we need Photoshop?"

#### 14. Copy + Paste edit settings with mask propagation
**Pattern:** course covers Copy Edit Settings (Cmd+Shift+C) which now includes masks. AI re-runs the masks on each new image automatically.
**Maps to:** `lightroom_operating_system.md` Hero edit workflow
**Improves:** time. A 20-Hero shoot takes the mask stack once. The other 19 Heroes get the masks pasted with auto re-detection.
**Action:** lock the workflow: edit Hero #1 fully → Cmd+Shift+C with all masks selected → paste to Heroes 2-N → adjust per-frame for face position / WB drift.

### F · Export discipline

#### 15. Saved export presets (one-click to every output spec)
**Pattern:** course Section 16653 covers export presets. SNIPED has export specs locked in PRODUCTION_OS Section 2.6 but not all are saved as Lightroom export presets yet.
**Maps to:** `lightroom_operating_system.md` export section + PRODUCTION_OS Section 2.6
**Improves:** time + consistency. Right-click → Export with Preset = 5-second export.
**Action:** create these 9 export presets matching the locked specs:
- `SNIPED · Hero · JPG Deliverable` (full size, sRGB, Q90)
- `SNIPED · Hero · TIF Master` (full, ProPhoto RGB, LZW)
- `SNIPED · Select · JPG` (full, sRGB, Q85)
- `SNIPED · Proof · JPG` (2400px, sRGB, Q80)
- `SNIPED · IG Carousel Portrait` (1080×1350, sRGB, Q90)
- `SNIPED · LinkedIn POV` (1080×1350, sRGB, Q90)
- `SNIPED · Carrd Selected Work` (2000px, sRGB, Q85)
- `SNIPED · Press Submission` (full, AdobeRGB, Q100 TIF)
- `SNIPED · VIB Asset Pair` (per VIB carousel format)

Each preset writes to its target subfolder inside the shoot folder per PRODUCTION_OS Section 1.1.

### G · Hero promotion discipline

#### 16. Virtual Copy as the "before retouch" snapshot
**Pattern:** course covers Virtual Copies as duplicates without disk overhead. Pro pattern: every Hero candidate gets a Virtual Copy named "_BASE" before any aggressive retouch experiments.
**Maps to:** `lightroom_operating_system.md` Hero workflow
**Improves:** quality (always have the base to revert to) + experimentation (push creative on the copy without losing the floor)
**Action:** discipline rule · before any heavy retouch (red color label work), Cmd+' creates the virtual copy. Name pattern: `[filename]_v0_BASE`. The aggressive edit happens on the original; if the experiment fails, revert to the BASE virtual copy and start over.

---

## DELAY · 4 items (revisit at trigger)

### 1. Print Module workflow
Course covers the Print module deeply. Hold for Direction Stack book launch (Q3 2026) and edition print program (Phase B+). At that point, consult the course's Print module section to lock the print spec workflow.
**Trigger:** Direction Stack book layout begins OR edition print pilot starts.

### 2. Lens Blur effect
Tempting depth-of-field simulation. Risk: reads AI-fake on close inspection, undermines the maker-led moat if used carelessly.
**Trigger:** Brand System tier work where intentional shallow DOF is editorial register. Never for Reset.

### 3. People recognition / face tagging
Privacy concern (auto-uploads to Adobe cloud) plus low workflow value (BJ already knows who is in each frame). Skip for now.
**Trigger:** if archive grows past 5,000 Heroes and finding-by-person becomes a bottleneck.

### 4. Map Module
Geo-organization useful only when Cultural Documentation expands across many neighborhoods. Hold.
**Trigger:** Cultural Documentation hits 10+ distinct LA locations and geographic search becomes useful for planning.

---

## IGNORE · the bulk of the course

These are beginner / consumer-tier sections that would dilute the SNIPED workflow if imported wholesale.

- **Basic crop, exposure, white balance explanations** · BJ operates above this baseline.
- **HDR / panorama merge** · off-positioning for portrait work.
- **Slideshow Module** · zero use case for SNIPED.
- **Web Module** · Carrd handles web. Lightroom Web module is obsolete pattern.
- **Book Module for client-facing photo books** · SNIPED's physical book is the Direction Stack monograph (Q3 2026), not Lightroom's auto-layout module. That book gets designed in InDesign / properly typeset.
- **Course's preset packs (Vintage Vibes, Bold Contrast, etc.)** · consumer-tier looks. SNIPED has its own locked look.
- **Mobile Lightroom app workflows** · BJ is desktop-Classic anchored. Mobile is field-only and does not enter the production pipeline.
- **Quick Develop in Library module** · sloppy editing pattern. Always use full Develop module.
- **Cloud-only catalog (Lightroom CC)** · architecture mismatch with PRODUCTION_OS storage tiering.
- **Generic social media size export presets** without SNIPED brand specs · use the SNIPED-locked presets only.
- **HDR + panorama merge + focus stacking** · off-positioning for portrait practice.
- **Adobe Stock submission workflow** · off-positioning entirely.
- **Tethered shooting tutorial** · low priority for the current solo studio workflow. Phase B+ if a client wants live monitor review on set.
- **Generic photo organization advice** (by year / by event / by family) · SNIPED has its own locked structure.

---

## FUTURE RETOUCHER TRAINING · 5 items

These get bundled into the retoucher onboarding pack (`/05_PRODUCTION/retoucher_training_notes.md`) when the Phase B retoucher hire activates (Mo 6-9 per OPERATIONAL_BACKBONE).

### 1. Library + Develop module navigation walkthrough
The course's Library and Develop module overview lectures are competent foundational material. Onboarding doc references the lecture numbers.

### 2. Color label + Smart Collection logic explanation
Why SNIPED labels what colors what color, what each smart collection feeds. The retoucher learns to work the right pool, not the dumping ground.

### 3. SNIPED preset chain explanation (locked-look + Hero finish + Proof batch)
Where each preset applies, what it does, what NOT to override. The retoucher does not invent · they apply.

### 4. AI mask stack standard
The 5-mask stack from item 12. The retoucher should be able to apply this in 60-90 seconds per Hero without supervision.

### 5. Where to STOP in Lightroom (the handoff line)
The retoucher learns: Lightroom does cull + base develop + AI masks + generative remove. Evoto does skin + body. Photoshop only when the decision tree calls for it. No improvising · escalate ambiguous cases to BJ for the call.

---

## What this course does NOT contain

- No advanced Photoshop retouch (separate course)
- No frequency separation / dodge-and-burn at the level needed for Brand System tier (separate course · the high-end beauty retouching course the user mentioned)
- No commercial color science workflow at the level a Hollywood post house operates
- No tethered live capture professional workflow

These remain gaps the future retouching course (or BJ's existing knowledge) covers.

---

## What ships next (the 6 file changes)

1. **NEW:** `/10_REFERENCE/UDEMY_LIGHTROOM_EXTRACTION.md` (this file)
2. **NEW:** `/05_PRODUCTION/lightroom_operating_system.md` (the practical OS doc)
3. **NEW:** `/05_PRODUCTION/preset_library.md` (the preset catalog)
4. **NEW:** `/05_PRODUCTION/retoucher_training_notes.md` (Phase B onboarding pack)
5. **EDIT:** `/05_PRODUCTION/SOP_capture_to_delivery.md` (add color label step + smart collection routing + import preset reference)
6. **EDIT:** `/00_BRIEF/PRODUCTION_OS.md` (cross-reference lightroom_operating_system.md, add catalog policy)

---

## Single integrated instruction

**The course is a craft-discipline source, not a strategy source. The 16 USE NOW items collapse into one outcome: a single locked Lightroom catalog with one import preset, one metadata preset, one develop preset chain, one color-label system, ten smart collections, one AI mask stack, nine export presets, and one virtual-copy discipline. Once these are locked, every shoot enters and exits Lightroom on the same rails. The retoucher hire becomes onboardable. The 12-15 min/Hero target becomes hittable. The visual signature stabilizes. Refuse the rest.**
