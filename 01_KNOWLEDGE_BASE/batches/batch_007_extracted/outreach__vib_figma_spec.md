# Visual Infrastructure Board (VIB) · Figma source spec

The VIB is the only outbound asset SNIPED Media uses cold. Build the master Figma file once, then duplicate per prospect. Total per-VIB time after master is built: **5–8 minutes**.

---

## Canvas

- **Frame size:** 1920 × 1280 px (single artboard, named `VIB · [LASTNAME]`)
- **Background fill:** `#1A1A1A` (charcoal · DO NOT change)
- **Grid:** 60 px outer margin, 80 px gutter between panels
- **Export preset:** PNG, 1x, sRGB. (Figma default JPG compresses skin tones unevenly.)

## Layer architecture (master file)

```
🟦 VIB · [LASTNAME]
├── 📁 BG
│   └── ▢ background-charcoal (#1A1A1A, full bleed)
├── 📁 LEFT-PANEL
│   ├── ▢ panel-bg-left (790×900, x:60, y:170)
│   ├── 🖼 prospect-photo (placeholder layer, fits panel-bg-left exactly)
│   ├── ⌽ panel-label-left ("THEIR LINKEDIN PHOTO" · uppercase · 12pt · letter-spacing 0.18em · #888888 · positioned 24px above panel)
│   └── ⌽ caption-left (caption block · positioned 24px below panel)
├── 📁 RIGHT-PANEL
│   ├── ▢ panel-bg-right (790×900, x:1070, y:170)
│   ├── 🖼 sniped-reference (placeholder layer, fits panel-bg-right exactly)
│   ├── ⌽ panel-label-right ("SNIPED REFERENCE FRAME" · same style as left)
│   └── ⌽ caption-right (caption block · same position rules)
├── 📁 HEADER
│   └── ⌽ headline (single line · 36pt · #F2F2F2 · positioned y:80)
└── 📁 FOOTER
    └── ⌽ footer-context ("[CONTEXT NOTE] · 1 frame from a SNIPED session · methodology: 10-protocol Direction Stack" · 11pt · #666666 · y:1200)
```

**No watermark. No SNIPED logo. No URL. The work is the asset.**

## Typography

- **Headline:** Inter (or system equivalent) · 36pt · Medium · #F2F2F2 · letter-spacing -0.01em
- **Panel labels:** Inter · 12pt · Medium · uppercase · letter-spacing 0.18em · #888888
- **Captions:** Inter · 16pt · Regular · #D8D8D8 · line-height 1.4
- **Footer:** Inter · 11pt · Regular · #666666 · line-height 1.4

If Inter is unavailable, fall back to: Helvetica Neue → Helvetica → SF Pro. Never Arial. Never anything decorative.

## Image rules (HARD)

**Left panel · prospect photo:**
- Pulled directly from their LinkedIn profile (right-click → save image as · use the largest version available)
- **Never edited.** No crop adjustment beyond fit-to-panel. No color correction. No retouching. No animation. No AI rendering.
- If the photo is square: center it in the 790×900 panel; the gray panel bg shows top + bottom.
- If the photo is 4:3 or rectangular: fit to width, center vertically.
- This is the rule that separates the VIB from gimmick outreach. The contrast is the message; tampering with their photo collapses the not-creepy test.

**Right panel · SNIPED reference frame:**
- Pulled from the SNIPED archive. Demographic match (same gender, similar age, similar build, similar wardrobe register).
- Aesthetic match (one of the 5 recurring descriptors: Monochromatic, Commercial, Studio, Editorial, Graphic).
- Pre-edited to SNIPED standard (Evoto retouch, color block, severe pose).
- Fits 790×900 with the subject anchored upper third (rule of thirds, top-third line).

## Reference frame pool · build this index in /03_OUTREACH/VIB_reference_pool/

Build a curated subdirectory of SNIPED reference frames pre-categorized:

```
/03_OUTREACH/VIB_reference_pool/
  ├── M_30s_dark-skin_business-casual_studio.jpg
  ├── M_40s_light-skin_suit_studio.jpg
  ├── M_30s_dark-skin_creative_on-location.jpg
  ├── F_30s_dark-skin_executive_studio.jpg
  ├── F_40s_light-skin_creative_studio.jpg
  ├── M_50s_any_executive_dark-bg.jpg
  └── ... (target: 12-16 reference frames covering the LA founder spread)
```

Each frame is named `[gender]_[age]_[skin]_[register]_[setting].jpg`. When prepping a VIB, pick the closest match. If no match exists, do not run the VIB; the demographic mismatch defeats the contrast.

---

## Caption rules

Each panel has a caption block. **Same structure on both sides** so the contrast is parallel.

**Caption template:**
```
PROTOCOL: [#NN · Protocol Name]
OBSERVATION: [one sentence, neutral, descriptive]
DEPLOYMENT IMPACT: [one sentence, where this shows up]
```

The Direction Stack protocol is the diagnostic vocabulary. Both panels use the same protocol; the left names the failure, the right names the corrected state.

**Example (Protocol 02 · Locked Shoulders):**

LEFT caption:
```
PROTOCOL: 02 · LOCKED SHOULDERS
OBSERVATION: Shoulders elevated and braced toward the camera.
DEPLOYMENT IMPACT: Reads as defensive on a website "About" page.
```

RIGHT caption:
```
PROTOCOL: 02 · LOCKED SHOULDERS
OBSERVATION: Shoulders dropped and rotated 12° from camera plane.
DEPLOYMENT IMPACT: Reads as confident on a press deck or LinkedIn.
```

## Headline rules

The headline is one short line, never longer than 60 characters. It names the gap, not the offer.

**Headline templates (rotate per VIB · pick the one matching the trigger):**

- `Your LinkedIn photo · Your visual operating level`
- `Where the camera's reading is below your business`
- `One frame · two readings · no overlap`
- `LinkedIn photo · founder's visual debt`
- `What the lens reads vs what you sell`

## Footer line

Always one of:

- `1 frame from a SNIPED session · methodology: 10-protocol Direction Stack`
- `Reference frame from a [city / industry] founder session · Sniped Media`
- (No CTA, no URL, no booking link. The conversation lives in the DM, not on the asset.)

---

## Per-VIB workflow (after master file is built)

1. Open Figma master, duplicate frame, rename `VIB · [LASTNAME]`.
2. Replace `prospect-photo` placeholder with their LinkedIn image (right-click → save → drag in).
3. Replace `sniped-reference` placeholder from the matched reference pool file.
4. Identify the dominant Direction Stack protocol they exhibit. Update both caption blocks with that protocol.
5. Update headline (pick from rotation).
6. Update footer (which session the right frame came from).
7. Export PNG @ 1x to `/03_OUTREACH/sent/YYYY-MM-DD_LASTNAME.png`.
8. Log in Outreach DB.
9. Send via LinkedIn DM with the matching script from `VIB_caption_library.md`.

---

## What this asset is NOT

- Not animated. Animated VIBs come ONLY post-conversion as Kling/Higgsfield delivery moments.
- Not a sales pitch. No price. No deliverables list. No bullet points.
- Not branded. No logo. No URL. The work is the brand.
- Not a critique. Tone is neutral diagnostic, never "your photo is bad."
- Not personalized prose. The structure stays consistent; only the prospect photo + protocol name changes.

The asset proves the operator's eye. The DM proves the operator's voice. The 10-min call proves the operator's mind. The shoot proves the system.
