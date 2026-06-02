# Evoto · Tactical Extraction Map

Sources:
- `/Users/sniper/Downloads/evoto ai youtube only.docx` (~28K lines · YouTube reviewer transcripts on the latest Evoto features)
- `/Users/sniper/Downloads/evoto ai only source.docx` (~11K lines · Evoto's official feature pages)
- `/Users/sniper/Downloads/EVOTO GOAT .docx` (~11K lines · Evoto Instant + tethered + projects + integrations)

Treatment: tactical capability map. Evoto's 2026 feature set is much wider than the "skin only" framing in the original SNIPED OS docs. This extraction corrects that and locks Evoto's actual role in SNIPED's workflow.

BJ has been using Evoto for 2-3 years. This doc isn't introducing Evoto · it's catching the SNIPED OS up to Evoto's current capabilities so the doc layer stops contradicting BJ's calibrated practice.

---

## What I had wrong (correction record)

The SNIPED OS docs (PRODUCTION_OS + lightroom_operating_system) framed Evoto as:
- "skin retouch + backdrop AI + body subtle"
- Routed all background work to Photoshop
- Routed all compositing to Photoshop
- Treated Lightroom as the spine and Evoto as the skin specialist

**The correction:**
- Evoto handles skin + body + backgrounds + color match + frequency separation + sculpt dodge & burn + tethered shooting + culling + project management + cloud sync
- Photoshop is now reserved for FULL ENVIRONMENT compositing only (Track B Gress playbook)
- Lightroom remains the SNIPED catalog spine, but Evoto is a parallel deep-edit layer, not a downstream-only one

---

## USE NOW · 8 capability shifts

### 1. AI Color Match with masking (the headline feature)

**What it does:** upload a reference image (your own finished Hero, OR a screenshot of a cinematic look), Evoto matches the current photo's color/tone to it. The new feature: mask the application separately on subject vs. skin vs. eyes vs. clothes vs. background.

**Maps to:** SNIPED look propagation across batches.

**Improves:**
- Time (one-click batch consistency)
- Quality (SNIPED look stays consistent across a 36-frame delivery)
- Control (mask the color match to subject only · keep background neutral, OR vice versa)

**Action:** build a SNIPED Color Match library in Evoto:
- Upload 5-10 of your strongest finished Heroes as reference images
- Tag by register (commercial, editorial, mono, studio, graphic)
- For new Heroes: pick the closest matching reference, apply Color Match, fine-tune via masking
- Optional: build a "Cinematic Looks" sub-library by screenshotting Hollywood film stills and uploading those for editorial register work

### 2. Backdrop color change / replace / cleanup (already your domain)

**What it does:** AI Background Color Changer, AI Background Replacer, AI Background Cleaner, Studio Backdrop cleaner (vinyl wrinkles, color banding, distractions).

**Maps to:** the 36 finals delivery · the optimize-backdrop-per-model move you've been doing for 2-3 years.

**Improves:** quality (clean, intentional backdrop) + time (faster than Photoshop comp).

**Action:** for the 36 finals, this is your primary backdrop tool. Do NOT route to Photoshop for backdrop color work. Photoshop only enters when the studio register fully breaks (Track B environmental swap).

### 3. AI Transform · one-click perspective / horizon correction

**What it does:** straightens skewed architecture, off-horizon shots, low-angle building distortion. One click.

**Maps to:** any frame where geometry is off after capture.

**Improves:** time (replaces manual Lightroom Transform fiddling).

**Action:** add to per-frame post-Evoto pass for any frame that needs straightening. Run before Color Match.

### 4. Frequency Separation + Sculpt Dodge & Burn (built-in)

**What it does:** the Photoshop Brand System tier retouch moves are now in Evoto. Frequency separation (skin texture preservation while removing tone unevenness) and sculpt-mode dodge and burn (contour the face / body via AI-detected zones).

**Maps to:** Brand System tier and Op Kit tier Heroes that previously would need a Photoshop round-trip for advanced skin work.

**Improves:** time (skip the Photoshop trip for skin-only Brand System work) + workflow consistency (work stays in Evoto · single round-trip from Lightroom).

**Action:** for Brand System tier Heroes, run frequency separation in Evoto BEFORE deciding "do we need Photoshop?" Photoshop only enters now for full environmental comp (Track B), not for skin frequency separation.

### 5. AI Culling (alternative to Lightroom assisted cull)

**What it does:** Smart Photo Selection with adjustable sensitivity for closed eyes, blur, exposure, duplicates.

**Maps to:** Pass 0 of the 5-pass cull from `/05_PRODUCTION/lightroom_operating_system.md` Section 4.

**Improves:** time (parallel to Lightroom assisted cull).

**Caveat:** Lightroom has this too. Don't double-cull. Pick one tool per shoot. Lightroom's assisted cull already runs at import time per the locked OS · Evoto's culling is an option for shoots imported directly to Evoto (e.g., during tethered sessions).

**Action:** keep Lightroom culling for the standard SNIPED catalog workflow. Use Evoto culling only when working entirely inside Evoto (tethered shoot day, no Lightroom round-trip needed).

### 6. Tethered shooting (wired USB / OTG, or wireless FTP)

**What it does:** camera shoots directly into Evoto with preset auto-applied within ~3 seconds. Real-time edit during the shoot. Side-by-side raw vs. edited compare for client review on set.

**Compatibility:** Canon, Sony, Nikon, Fuji, Panasonic, Leica, Olympus.

**Maps to:** future shoot days where live client review on set adds value (Op Kit / Brand System tier with founder-on-set).

**Improves:** quality (real-time tonal/expression review) + client experience (founder sees the look immediately) + post-shoot speed (most edits already applied at capture).

**Action:** Phase B+ activation. Phase 1 keep current shoot day workflow (no tethering). When the first paid Op Kit / Brand System shoot lands and you want the on-set review experience, activate Evoto tethering with the Fuji rig.

### 7. AI Color Looks (built-in cinematic presets)

**What it does:** built-in style library · film inspired, natural wedding tones, B&W, luxury texture, matte. The reviewer specifically mentioned "luxury texture" and "matte" as workhorses.

**Maps to:** alternate looks for editorial work · supplements the SNIPED locked-look v2.

**Improves:** quality (variety) + speed (one-click try-on of different registers).

**Caveat:** these are starting points, not endpoints. Apply, then refine via Color Match masking + per-image work.

**Action:** test "luxury texture" and "matte" against 3 SNIPED frames. If either reads on-brand, save it as a SNIPED-tagged preset variant.

### 8. Cloud sync + cross-device (500 GB free for FW2026)

**What it does:** Evoto Cloud Space syncs edits between Windows, Mac, iPad. Edit on iPad while traveling, finish on desktop.

**Maps to:** the engineering travel weeks per OPERATIONAL_BACKBONE.

**Improves:** flexibility (BJ can edit between meetings, on planes, in hotel rooms · without dragging the SSD).

**Caveat:** if Evoto cloud sync is on, it pulls edited files to cloud · separate from Adobe Cloud. Two separate cloud setups. Don't double-pay or get confused.

**Action:** sign up for FW2026 promo (500 GB free) · use as the parallel cloud for Evoto-side work + iPad mirror.

---

## DELAY · 4 items (revisit at trigger)

### 1. Lightroom Catalog support inside Evoto
Evoto's marketing says it now supports Lightroom catalogs natively. Reviewer Salison Kata calls it "the Lightroom killer." Worth testing in Phase B+ · could replace Lightroom Classic as the catalog spine. Don't migrate now · the SNIPED Lightroom catalog was just built and locked.
**Trigger:** Phase B start ($3K MRR sustained 2 months) AND a tested side-by-side comparison.

### 2. Evoto Instant + Project Management
Project-level cloud organization for events / schools / weddings. NOT current SNIPED ICP (founders, operators, artists, cultural doc subjects · not high-volume school/event).
**Trigger:** if SNIPED ever expands into event coverage at volume.

### 3. Participant Mode + QR code sorting
School photography workflow with auto-sorting by QR code per student. Off-positioning for SNIPED entirely.
**Trigger:** never (different ICP).

### 4. Gallery Monetization (Evoto Instant pricing models)
Evoto's built-in gallery sales (3 pricing models). SNIPED uses Pixieset (already locked).
**Trigger:** if Pixieset becomes inadequate AND Evoto's gallery monetization beats it on UX or fee structure. Not now.

---

## IGNORE · the off-positioning features

These exist in Evoto but should NEVER touch SNIPED client work · they violate the "subject is real" line.

- **Hair color changer** · changes the model's hair color. Unauthorized identity change.
- **Skin tone changer** (full body skin tone shift) · changes the model's actual skin tone. Off-positioning, racially fraught, anti-Berger.
- **Makeup applier (full looks)** · the makeup that's there is real (Hermine MUA work). Adding fake makeup falsifies the shoot.
- **Tattoo remover** · unauthorized identity change unless the model explicitly asked for it (rare · then it's a per-frame call, not a default).
- **AI Image Extender (uncrop)** · risky on portraits · generates content beyond the original frame · effectively faking what was outside the camera's view.
- **AI Open Eyes** · opens closed eyes via AI generation. Falsifies the moment. The frame either had open eyes or it didn't.
- **AI Smile Filter** · generates smiles on neutral faces. Falsifies expression. Anti-Berger.
- **AI Facial Expression Changer** · changes the expression. Same.
- **Eye color changer** · changes iris color. Unauthorized identity change.
- **Body editor at aggressive settings** · already noted in the OS as "subtle, never on Reset." Holds. Liquify is fine for waist/hip subtle correction; aggressive reshape is off.

The single rule for these: **the methodology runs first. Evoto is utility behind the methodology. Anything that changes who the model IS rather than how the photo READS · is off the table.**

---

## CORRECTIONS to existing SNIPED OS docs

### `/00_BRIEF/PRODUCTION_OS.md` Section 4.1

**Old:** Evoto = "skin retouch + backdrop AI + body subtle"
**New:** Evoto = skin + body subtle + backdrop color change/replace/cleanup within studio register + AI Color Match (style propagation) + AI Color Looks (built-in cinematic presets) + frequency separation + sculpt dodge & burn + AI Transform (one-click straighten) + tethered shooting (Phase B+) + AI Culling (alternative to LR · use one or the other per shoot)

### `/05_PRODUCTION/lightroom_operating_system.md` Section 7 · Retouch decision tree

**Old line that was wrong:** "Photoshop ONLY: frequency separation beyond Evoto's capability, compositing, liquify, dodge-and-burn, manual hair masking"

**New line:** Photoshop is reserved for full environment compositing only (Track B Gress playbook). Frequency separation + dodge-and-burn now happen in Evoto. Compositing within studio register (backdrop color/swap/cleanup) happens in Evoto. Photoshop enters only when the subject is being placed in a fully different environment with depth, perspective, and lighting story.

### `/00_BRIEF/PRODUCTION_OS.md` Section 4.5 · "What never gets outsourced"

Add: **Hero promotion to Green** stays BJ-only. Evoto's AI culling can identify candidates but the GREEN label (Hero approved) is BJ's call · the methodology is on-the-line at that decision.

---

## Updated tool routing · the corrected map

| Need | Tool | Notes |
|---|---|---|
| Catalog · master library | Lightroom Classic | Locked spine. SNIPED_2026.lrcat. |
| Cull (Pass 0 auto-reject) | Lightroom assisted cull at import | Standard. |
| Cull (alternative · tethered Evoto sessions) | Evoto AI Culling | When working entirely in Evoto. |
| Develop (RAW base, tone curve, HSL, calibration) | Lightroom Classic | Locked-look v2 preset. |
| Per-image WB / exposure / contrast | Lightroom Classic | Histogram-driven 6-step. |
| AI mask stack (Subject / Face / Eyes / Teeth / Background) | Lightroom Classic | 5-mask locked stack. |
| Generative Remove (small distractions) | Lightroom Classic | In-frame cleanup. |
| Skin retouch | Evoto | Locked SNIPED Evoto preset. |
| Body subtle (waist/hips refinement) | Evoto | Per-image, never aggressive. |
| Backdrop color change | Evoto | Background Color Changer or AI Background Replacer. |
| Backdrop cleanup (wrinkles, banding) | Evoto | Studio Backdrop cleaner. |
| Frequency separation | Evoto | Brand System tier. (Was Photoshop · now Evoto.) |
| Sculpt dodge & burn | Evoto | Brand System tier. (Was Photoshop · now Evoto.) |
| AI Transform (straighten architecture) | Evoto | One-click. |
| Color Match across batch | Evoto AI Color Match | Use SNIPED Hero references for batch consistency. |
| Cinematic / film look application | Evoto AI Color Looks | "Luxury texture," "matte" worth testing. |
| Final grade / hero finish | Lightroom Classic | `SNIPED_HERO_FINISH_v1` preset. |
| Export (Pixieset deliverables) | Lightroom Classic | 9 SNIPED export presets. |
| FULL environment compositing | Photoshop | Track B Gress playbook only · subject placed in generated stadium / rooftop / hotel etc. |
| Tethered shooting (Phase B+) | Evoto | Wired USB or wireless FTP · all major cameras. |
| Cross-device editing on the road | Evoto Cloud Space | 500 GB FW2026 promo. |

---

## What this changes for tonight's edit session on the 36 finals

You're cleared to edit the way you've been editing for 2-3 years. The locked OS now matches your practice:

1. Lightroom · develop + masks + cleanup
2. Evoto · skin + backdrop color optimization (per model · matching outfit/skin tone) + Color Match for batch consistency
3. Lightroom · Hero finish + export

No Photoshop on these 36. Photoshop is reserved for the 6-12 Track B portfolio frames later (full environmental swap to a different location).

Send the optimized-backdrop deliverables confidently. This is pro-tier studio register work, not "tacky background change."

---

## Single integrated instruction

**Evoto in 2026 is the deep-edit layer of SNIPED's pipeline. Lightroom owns the catalog, develop foundation, masks, and export. Evoto owns skin, body subtle, backdrop optimization, color match, frequency separation, dodge & burn, AI Transform. Photoshop is reserved for full environment compositing only · Track B Gress playbook · subject in a generated cinematic environment with depth, perspective, and lighting story. The Berger / Sax line holds: subject is real, photographer was present, methodology ran. Evoto's identity-changing features (hair color, skin tone, AI smile, eye color, full makeup, expression changer, image extender) are absolutely off the table for SNIPED client work. The methodology decides what stays and what shifts · Evoto is the tool that executes the shifts.**
