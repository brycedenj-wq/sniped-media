# SOP · Capture to Delivery

**Runbook for every paid shoot from SD card → Pixieset gallery live. 5-business-day SLA for Reset; 10-business-day for Op Kit.**

The 5-day promise is the operational claim that earns the $1,500 price. Treat each step as load-bearing.

---

## Phase 1 · Same day as shoot (within 4 hours of wrap)

- [ ] Power down camera, swap battery to charging dock at home/desk
- [ ] **Ingest** all SD cards to laptop via USB-C reader, copying to `~/SNIPED/shoots/YYYY-MM-DD_[CLIENT]/raw/`
- [ ] **Backup #1** to external SSD `SNIPED-WORKING` (mirror folder structure)
- [ ] **Backup #2** to Google Drive `Sniped Media · Shoots Archive` (auto-sync with Backup & Sync)
- [ ] Verify file count matches across all three locations (laptop / SSD / Drive)
- [ ] **Format SD cards in-camera** (not Finder · in-camera ensures correct filesystem) and put back in camera bag
- [ ] Update Notion Shoots card: Status `Captured` · check `Card backed up`
- [ ] If anything went wrong on set (model missed brief, location issue, gear failure), write a one-line `Notes` entry in Shoots card while it's fresh

**If you skip Phase 1, the entire SLA is at risk.** Same-day ingest is non-negotiable.

---

## Phase 2 · Day 1-2 · Cull pass

> **v3 OVERRIDE (2026-05-07):** Phase 2 now uses the 5-pass system with assisted culling at import and color label routing. Full runbook in `/05_PRODUCTION/lightroom_operating_system.md` Section 4. Catalog is the master `SNIPED_YYYY.lrcat`, NOT a per-shoot catalog. The v1 four-pass text below is preserved for reference but is NOT the deployed workflow.

### v3 (current) · 5-pass cull

- [ ] Open the master catalog: `/SNIPED_PRODUCTION/_catalogs/SNIPED_2026.lrcat`
- [ ] Import via `SNIPED · IMPORT DEFAULT` preset (Smart Previews ON, locked-look applied, copyright applied, assisted culling ON for subject focus + eye focus + auto-reject exposure failures)
- [ ] Set keyword on import (e.g., `Reset`, `FreeCollab`)
- [ ] **Pass 0 (auto):** assisted culling has flagged auto-rejects. Filter to Rejected. Verify no false rejects. Promote any AI-missed keepers via right-click → Mark as Pick.
- [ ] **Pass 1 (Reject refinement):** filter to Unflagged + Picked. X any frames the AI missed. P any keepers. 5-8 min.
- [ ] **Pass 2 (Pick pass):** filter to Picks. Refine the keeper pool. 8-12 min.
- [ ] **Pass 3 (Star pass):** filter to Picks. Number keys: 3 = Proof tier, 4 = Select tier, 5 = Hero candidate. 5-10 min.
- [ ] **Pass 4 (Color label pass):** filter to ⭐⭐⭐⭐⭐ Heroes only. Number key 6 = Red (heavy retouch / Photoshop), 7 = Yellow (standard Evoto pipeline). 2-3 min.
- [ ] Smart Collection `01 · Heroes Pending Retouch` auto-populates with the labeled Heroes
- [ ] Total cull time target: **15-25 minutes** for a Reset shoot.

### v1 (deprecated) · for reference only

- [ ] Open Lightroom Classic. Import the `raw/` folder into a fresh shoot-specific catalog or smart collection
- [ ] Apply the SNIPED import preset (Auto White Balance off, Camera Standard profile, Lens Corrections on, baseline exposure adjusted to taste)
- [ ] **Pass 1 (Blink-pass):** flag every frame with sharp eyes + open eyes + no major blink. Use the X / P keys: P = pick, X = reject. Speed: 1-2 sec per frame.
- [ ] **Pass 2 (Pose-pass):** filter to picks only. Reject any frame where the pose architecture failed (per the 7-point posing system). P picks become the working pool.
- [ ] **Pass 3 (Story-pass):** filter to picks. Star-rate ⭐⭐⭐ for the strongest 30-40% of the pool. These are the candidates for the contracted 20.
- [ ] **Pass 4 (Final selection):** from ⭐⭐⭐ pool, pick the final twenty (20) for the contracted gallery + ten to fifteen (10-15) for the upsell pool. Final selections get ⭐⭐⭐⭐⭐.
- [ ] Total cull time target: **45 minutes** for a Reset shoot. If it takes more, the bottleneck is decisive culling, not technical work.

---

## Phase 3 · Day 1-2 · Cull + 3-tier edit pass

> **v2 OVERRIDE (2026-05-06):** Phase 3 superseded by `/01_OFFERS/delivery_architecture_v2.md` Section 6. The "20 fully retouched · 5-7 hr/Reset" model is retired. New model: AI cull + 3-tier edit pipeline (Proofs · Selects · Heroes) producing 8-12 Heroes + 30-40 Selects + 60-100 Proofs in 2-3.5 hr/Reset. Read v2 Section 6 before editing the next Reset.

The v1 text below is preserved for reference but is NOT the deployed workflow.

### v1 (deprecated) · for reference only

## Phase 3 · Day 2-3 · Edit pass (Lightroom + Evoto + Photoshop)

For each of the 20 contracted images + 10-15 upsell:

**Step A · Lightroom base edit (5-7 minutes per image):**
- [ ] Apply the SNIPED locked-look preset (the v1 preset stack from /05_PRODUCTION/presets/)
- [ ] Manual adjustment: white balance (skin tone is the reference, not gray card)
- [ ] Tone: protect highlights on skin; let background highlights blow if they fight subject
- [ ] HSL tweaks for the locked color block (saturate the dominant tonal family, desaturate competing colors)
- [ ] Crop / straighten · always rule-of-thirds upper-third for the face
- [ ] Export 16-bit TIFF to `~/SNIPED/shoots/YYYY-MM-DD_[CLIENT]/edit-stage/`

**Step B · Evoto AI batch retouch (3-5 minutes per image · runs while you continue Lightroom):**
- [ ] Import TIFFs to Evoto
- [ ] Apply SNIPED retouch preset (Skin: clinical · Pore detail: preserved · Spot removal: high · Eye whitening: low · Teeth whitening: low)
- [ ] Review every face for over-retouching. The clinical-but-not-plastic line is the SNIPED signature.
- [ ] Apply Evoto backdrop overlay (one of the 10 custom overlays) · grain on background only, never on subject
- [ ] Export retouched TIFFs to `~/SNIPED/shoots/YYYY-MM-DD_[CLIENT]/retouched/`

**Step C · Photoshop final pass (2-4 minutes per image · only as needed):**
- [ ] Open in Photoshop only if: (a) frequency separation needed beyond Evoto, (b) compositing required, (c) liquify/proportion adjustment needed, (d) backdrop replacement
- [ ] Save back to `retouched/` overwriting the Evoto export
- [ ] Most Reset frames skip Step C entirely. If you're opening Photoshop for every frame, the Lightroom + Evoto recipe needs tightening.

**Time budget for full edit: 10-15 minutes per delivered image. 20 images = 3.5-5 hours of focused edit time.**

This is the bottleneck flagged in the Operating Brief. If it climbs above 5 hours per Reset, the part-time retoucher hire becomes the priority.

---

## Phase 4 · Day 4 · Export + Pixieset upload

- [ ] Final export from Lightroom (re-import retouched TIFFs):
  - High-res JPG: 300 DPI, sRGB, quality 90, longest edge 4000 px
  - Web JPG: 72 DPI, sRGB, quality 85, longest edge 2048 px
  - Save to `~/SNIPED/shoots/YYYY-MM-DD_[CLIENT]/final/[hi-res|web]/`
- [ ] Upload to Pixieset using the `Reset Gallery Template` (configured per `/06_DELIVERY/pixieset_config.md`)
- [ ] Set 14-day gallery expiry (with 48-hour upsell window separately tracked)
- [ ] Watermark off (deliverables to clients are unwatermarked; only portfolio uses get watermarks)
- [ ] Add the 20 contracted images to `Selections` collection · the 10-15 upsell to `Additional` collection (price tagged at $80/image)
- [ ] Test the gallery: open in incognito, click through all 20, verify download works, verify upsell pricing displays
- [ ] Update Notion Galleries card: Pixieset URL · Delivered date · Expiry date

---

## Phase 5 · Day 5 · Delivery

- [ ] Send delivery email (template in `/06_DELIVERY/email_templates.md`) at **9:00 AM PT** (highest open rates for B2B)
- [ ] Email includes: gallery link, password, 48-hour upsell window note, suggestion for top 3 deployment uses (LinkedIn header, press, deck cover)
- [ ] Send a parallel SMS only if the client opted in: "Your Reset is live. [link]"
- [ ] Update Notion Shoots card: Status `Delivered` · Delivery actual date · Pixieset URL · Hero image upload
- [ ] Update Notion Pipeline card: Status `Reset Delivered` · Last touch · Next action: `Day 30 Op Kit pitch on [date+30]`
- [ ] Trigger the post-delivery SOP (see `SOP_post_delivery.md`)

---

## Phase 6 · Cleanup (within 7 days)

- [ ] Archive the working files: move `raw/` and `edit-stage/` and `retouched/` to the Drive archive · keep `final/` on local SSD
- [ ] Add Hero image to the Lightroom `SNIPED · Portfolio Working` collection for future case study + Art Series cross-reference
- [ ] Tag the Hero image with: client first name, shoot type, dominant Direction Stack protocol applied, dominant aesthetic descriptor (Mono / Commercial / Studio / Editorial / Graphic)

---

## Failure modes (and the recovery)

| Failure | Cause | Recovery |
|---|---|---|
| Cull pass takes >90 min | Too many similar frames; indecision | Force the 4-pass discipline; reject hard on Pass 1; the goal is decisiveness, not democracy |
| Edit time > 15 min per image | Trying to fix capture problems in post | Capture issue must be diagnosed (was it lighting? pose? not enough fill?) and fixed in next shoot, not chased in post |
| SLA missed | Day 1-2 ingestion delayed by paid-job conflict or travel | Communicate **before** delivery date with revised ETA; never go silent. One delayed delivery is a business cost; one ghosted delivery is a reputation cost |
| Pixieset gallery rejection by client | Color reads wrong on their monitor or print spec wrong | Re-export with adjusted color profile (sRGB for web, AdobeRGB for print upon request); replace gallery; never argue color over email |
