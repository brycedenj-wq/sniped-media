# SNIPED Preset Library

The locked preset catalog for Lightroom Classic. Each preset is built once, named per the convention below, exported to `.xmp` for backup, and never silently re-tuned. Versioning is explicit: `_v1`, `_v2`, etc.

Cross-references:
- Where presets apply: `/05_PRODUCTION/lightroom_operating_system.md`
- Output specs: `/00_BRIEF/PRODUCTION_OS.md` Section 2.6
- Source course context: `/10_REFERENCE/UDEMY_LIGHTROOM_EXTRACTION.md`

---

## 1. Develop presets (5 total)

### 1.1 SNIPED_LOCKED_LOOK_v1

The base layer. Applied via the import preset to every photo on import.

**Settings included:**
- Profile: Camera Standard (Fuji default · re-evaluate per camera body)
- White Balance: As Shot (per-image override)
- Lens corrections: Profile ON, Chromatic Aberration ON
- Tone curve: SNIPED locked S-curve
  - Shadows: lift +5 (no crushed black)
  - Darks: -3
  - Lights: -3
  - Highlights: roll -8 (skin protection)
- HSL: SNIPED locked color block (refine per quarterly review)
- Color Calibration: SNIPED signature shifts
- Sharpening: 40
- Noise reduction: 25 color (default)
- Effects: vignette OFF, grain OFF
- Settings NOT included (per-image only): exposure, contrast, saturation, vibrance, masks, crop

**Build action:** open a representative SNIPED Hero, set the values above, save as develop preset with name `SNIPED_LOCKED_LOOK_v1` in group `SNIPED · Locked`.

### 1.2 SNIPED_HERO_FINISH_v1

Applied AFTER Evoto round-trip, before final export.

**Settings included:**
- Final grain: amount 12, size 25, roughness 50 (subtle, only visible at 100% zoom)
- Final tone curve roll (additional skin protection): highlights -3
- Final saturation: -2 (skin protection against Evoto over-saturation)
- Final clarity on background: -5 (atmospheric softening)

**Build action:** open a post-Evoto Hero, set values, save as `SNIPED_HERO_FINISH_v1` in group `SNIPED · Locked`.

### 1.3 SNIPED_PROOF_BATCH_v1

For the volume Proof tier. Applied via batch synchronize after star-rating proofs.

**Settings included:**
- Lighter version of locked-look (less aggressive curve)
- Sharpening 30 (slightly less than Hero · Proofs are smaller export)
- Slight clarity +5 (proofs need some pop · they are gallery-thumbnail tier)

**Build action:** save as `SNIPED_PROOF_BATCH_v1` in group `SNIPED · Locked`.

### 1.4 SNIPED_CULTURAL_DOC_v1

For Cultural Documentation work. Different register from commercial Heroes.

**Settings included:**
- Profile: Camera Eterna or Camera Classic Chrome (per Fuji film simulation register)
- Tone curve: stronger contrast than Locked Look (cultural doc reads more documentary)
- HSL: muted greens, lifted oranges (skin tones in environmental light)
- Slight grain: amount 18 (slightly stronger than Hero Finish · documentary register)

**Build action:** save as `SNIPED_CULTURAL_DOC_v1` in group `SNIPED · Locked`.

### 1.5 SNIPED_BW_EDITORIAL_v1

For black-and-white editorial register (Op Kit / Brand System tier).

**Settings included:**
- Convert to B&W ON
- B&W Mix: orange +30, yellow +20, blue -20 (skin glow · sky drama)
- Tone curve: stronger S-curve than color presets
- Grain: amount 25, size 30 (intentional film register)

**Build action:** save as `SNIPED_BW_EDITORIAL_v1` in group `SNIPED · Locked`.

---

## 2. Metadata preset (1 total · update annually)

### 2.1 SNIPED_COPYRIGHT_2026

| Field | Value |
|---|---|
| Creator | Bryceden Jones |
| Creator URL | snipedmedia.com |
| Creator Email | bryceden@snipedmedia.com (or actual production address) |
| Copyright | © 2026 SNIPED Media. All rights reserved. |
| Copyright Status | Copyrighted |
| Rights Usage Terms | Per signed agreement (Op Kit MSA, Reset agreement, or model release). Unauthorized use prohibited. |
| Creator City | Los Angeles |
| Creator State / Province | California |
| Creator Country | USA |

**Build action:** Lightroom Library → Metadata panel → Preset dropdown → Edit Presets → fill the IPTC fields → save as `SNIPED_COPYRIGHT_2026`.

**Annual update:** January 1 each year, duplicate this preset as `SNIPED_COPYRIGHT_YYYY` and update the year in the copyright string. Set new preset as the import default.

---

## 3. Import preset (1 total)

### 3.1 SNIPED · IMPORT DEFAULT

Saved at the bottom of the Lightroom Import dialog.

| Section | Setting |
|---|---|
| File handling | Build Standard previews · Build Smart Previews ✅ · Don't import suspected duplicates ✅ |
| File renaming | OFF (file rename only at export, never on RAW) |
| Apply during import → Develop Settings | `SNIPED_LOCKED_LOOK_v1` |
| Apply during import → Metadata | `SNIPED_COPYRIGHT_YYYY` (current year) |
| Apply during import → Keywords | (leave blank · enter manually per import: `Reset`, `FreeCollab`, etc.) |
| Destination (SD card import) | Custom: `/SNIPED_PRODUCTION/YYYY/YYYY-MM-DD_Client_TYPE/10_RAW/` |
| Assisted Culling | Subject focus ✅, Eye focus (eyes open) ✅, Auto-reject exposure issues ✅ |

**Build action:** configure the Import dialog with all of the above, then click the dropdown at bottom of dialog → "Import Preset → Save Current Settings as New Preset" → name `SNIPED · IMPORT DEFAULT`.

---

## 4. Export presets (9 total)

All defined and saved in Lightroom's Export dialog. Each writes to a specific subfolder inside the shoot folder.

### 4.1 SNIPED · Hero · JPG Deliverable

| Setting | Value |
|---|---|
| Export location | Specific folder · `/30_HEROES/` (relative to current shoot folder, or set per-shoot) |
| File naming | `SNIPED_YYYY-MM-DD_Client_HERO_###.jpg` |
| File format | JPEG |
| Color space | sRGB |
| Quality | 90 |
| Image sizing | Don't enlarge · resize OFF (keep full ~6000px) |
| Resolution | 300 dpi |
| Output sharpening | Standard for Screen |
| Metadata | All except camera/RAW/lens info (the locked-look preset stays on the master · Heroes ship clean) |
| Watermark | OFF |

### 4.2 SNIPED · Hero · TIF Master

| Setting | Value |
|---|---|
| Export location | `/30_HEROES/` |
| File format | TIFF |
| Color space | ProPhoto RGB |
| Bit depth | 16 |
| Compression | LZW (lossless) |
| Image sizing | Don't enlarge · resize OFF |
| Watermark | OFF |

### 4.3 SNIPED · Select · JPG

| Setting | Value |
|---|---|
| Export location | `/40_SELECTS/` |
| File format | JPEG |
| Color space | sRGB |
| Quality | 85 |
| Image sizing | Don't enlarge · resize OFF |
| Watermark | OFF |

### 4.4 SNIPED · Proof · JPG

| Setting | Value |
|---|---|
| Export location | `/50_PROOFS/` |
| File format | JPEG |
| Color space | sRGB |
| Quality | 80 |
| Image sizing | Resize to fit · long edge · 2400 px |
| Watermark | OFF |

### 4.5 SNIPED · IG Carousel Portrait

| Setting | Value |
|---|---|
| Export location | `/80_CONTENT/` |
| File format | JPEG |
| Color space | sRGB |
| Quality | 90 |
| Image sizing | Resize to fit · width and height · 1080 × 1350 |
| Watermark | OFF |

### 4.6 SNIPED · LinkedIn POV

| Setting | Value |
|---|---|
| Export location | `/80_CONTENT/` |
| File format | JPEG |
| Color space | sRGB |
| Quality | 90 |
| Image sizing | Resize to fit · width and height · 1080 × 1350 |
| Watermark | OFF |

### 4.7 SNIPED · Carrd Selected Work

| Setting | Value |
|---|---|
| Export location | (manual · not per-shoot · use `/SNIPED_OS/14_WEB/exports/`) |
| File format | JPEG |
| Color space | sRGB |
| Quality | 85 |
| Image sizing | Long edge · 2000 px |
| Watermark | OFF |

### 4.8 SNIPED · Press Submission

| Setting | Value |
|---|---|
| Export location | (manual per submission) |
| File format | TIFF or high-quality JPEG (per recipient spec) |
| Color space | Adobe RGB (default) or sRGB (per spec) |
| Quality | 100 |
| Image sizing | Don't enlarge · resize OFF |
| Watermark | OFF |
| Metadata | All including IPTC contact (press needs to credit) |

### 4.9 SNIPED · VIB Asset Pair

| Setting | Value |
|---|---|
| Export location | `/03_OUTREACH/VIB_assets/` |
| File format | JPEG |
| Color space | sRGB |
| Quality | 90 |
| Image sizing | Per VIB carousel format (locked in `/03_OUTREACH/SOP_VIB_production.md`) |
| Watermark | OFF |

---

## 5. Preset hygiene

- Build each preset once. Test against 3-5 representative frames before locking.
- Export each preset to `/05_PRODUCTION/_preset_backups/` as `.xmp` after build. Re-import if catalog corrupts.
- Quarterly review: open one Hero from the prior quarter, dry-run the locked-look preset against it, verify the look still reads correct. If yes, no change. If no, build `_v2` (do not edit `_v1` in place).
- Never delete a preset · disable instead. Old presets are version history.

---

## 6. The single rule

**One signature. Built into the preset chain. Applied invisibly via the import default. Refined per-image, not invented per-image.** The visual register of SNIPED reads consistent because the foundation is locked. Every deviation is a deliberate choice, not a forgotten setting.
