# Saturday Build Brief · the hands-on layer

**The markdown templates, scripts, captions, hooks, and checklists are built. This brief covers the binary / UI / hardware items only YOU can build. Estimated time: one focused 6-hour Saturday session.**

Run hour-by-hour. Each hour produces something the system uses immediately.

---

## Hour 1 · Storage hardware + folder install

### Hardware to acquire (one-time spend, ~$300-400)

| Item | Spec | Vendor | Cost |
|---|---|---|---|
| Hot SSD | Samsung T7 Shield 2TB OR SanDisk Extreme Pro 2TB | Amazon / B&H | $150-180 |
| Warm HDD | WD Easystore 8TB OR Seagate Expansion 8TB | Best Buy / Amazon | $130-150 |
| Cold HDD (mirror) | Same model as Warm (identical for symmetry) | Same | $130-150 |
| USB-C 3.2 card reader | ProGrade CFexpress + SD reader OR SanDisk Pro | B&H | $40-60 |

**Total: $450-540 one-time.** Optional: Backblaze B2 cloud at $5-15/mo (Phase B+).

### Install steps (60 min)

1. Format Hot SSD as APFS encrypted. Label volume name: `SNIPED_HOT`
2. Format Warm HDD as APFS (no encryption, faster). Label: `SNIPED_WARM`
3. Format Cold HDD as APFS. Label: `SNIPED_COLD`
4. On Hot SSD: create root folder `SNIPED_PRODUCTION/` and inside it `2026/`
5. On Warm HDD: create root folder `SNIPED_PRODUCTION/`
6. On Cold HDD: create root folder `SNIPED_PRODUCTION_ARCHIVE/`
7. In your home directory, symlink: `ln -s /Volumes/SNIPED_HOT/SNIPED_PRODUCTION ~/SNIPED_PRODUCTION` (the scripts assume this path)
8. Test: `~/SNIPED_PRODUCTION/` should now navigate to the SSD when mounted
9. Install scripts:
   ```bash
   mkdir -p ~/bin
   cp /Users/sniper/Downloads/SNIPED_OS/scripts/*.sh ~/bin/
   chmod +x ~/bin/*.sh
   ```
10. Add to `~/.zshrc`:
    ```bash
    export PATH="$HOME/bin:$PATH"
    alias snibak='sniped_backup.sh'
    alias snibak-verify='verify_backup.sh'
    alias snishoot='setup_shoot_folder.sh'
    ```
11. Reload shell: `source ~/.zshrc`
12. Test: `snishoot 2026-06-15 TestClient Reset` should create the 9-subfolder skeleton on the SSD

---

## Hour 2 · Lightroom + Evoto preset stacks

### SNIPED Lightroom presets (3 to build)

**Preset 1 · `SNIPED_Base`** (applied on import, every frame)

Settings to encode:
- White Balance: As Shot (let it adapt; tweak per frame)
- Tone Curve: subtle S-curve (point: shadows -8, darks -5, lights +5, highlights +3)
- Exposure: 0 (do not preset · per-frame)
- Contrast: +10
- Highlights: -25
- Shadows: +15
- Whites: +10
- Blacks: -10
- Vibrance: +8
- Saturation: -5 (slight desaturation matches SNIPED palette)
- Sharpening: Amount 40, Radius 1.0, Detail 25
- Noise reduction: Luminance 10, Color 25
- Lens corrections: Enable Profile Corrections + Remove Chromatic Aberration
- Calibration: per camera body (test on Canon EOS RP first; calibrate)

Save as `SNIPED_Base` in User Presets.

**Preset 2 · `SNIPED_Selects`** (applied during Selects edit · 1-2 min/frame)

Built ON TOP of `SNIPED_Base` with:
- Slightly stronger contrast (+5)
- Slightly cooler white balance (-200 Kelvin from base)
- Black point pull (Blacks -5)
- Subtle clarity (+5)
- One masked adjustment: brighten subject (+0.3 EV via subject-select mask)

Save as `SNIPED_Selects`.

**Preset 3 · `SNIPED_Proofs`** (applied during Proofs batch · 30-45 sec/frame)

Lighter than Selects. Goal: presentable but clearly not Hero-grade.
- Same `SNIPED_Base` baseline
- Skip Selects' masked subject adjustment (too slow for batch)
- Reduce sharpening to 20 (proofs are smaller dimension anyway)
- No clarity boost

Save as `SNIPED_Proofs`.

**Test all three on a known frame.** If a Hero frame run through `SNIPED_Selects` looks worse than the same frame edited individually, the preset is wrong · adjust until the preset gets you 80% there with the remaining 20% as per-frame manual.

### Evoto SNIPED preset

Evoto presets are saved in-app. Build by:
1. Open a representative Hero from a past shoot
2. Configure:
   - Skin retouch: 70% (preserve texture · do not over-smooth)
   - Skin tone evening: 40%
   - Body subtle: 20% (very light · just spinal posture / shoulder symmetry)
   - Eye sharpening: 30%
   - Teeth whitening: 15%
   - Backdrop AI: enabled, "studio backdrop" mode
   - Hair refinement: 25%
3. Save as `SNIPED_Hero_v1`
4. Apply to 3 different past Heroes · adjust if any look over-processed

The 70/40/20/30 numbers are starting points. Tune to your aesthetic over the first 5 paid Resets and lock the values once stable.

---

## Hour 3 · Figma master file (templates + VIB pool)

### Single Figma file, multiple pages

Create one Figma file: `SNIPED · Production Templates`

**Page 1: VIB Master**
- Per `/03_OUTREACH/VIB_figma_spec.md` · 1920×1280 charcoal #1A1A1A canvas
- Left panel: prospect photo placeholder (smart-fill)
- Right panel: SNIPED reference frame placeholder
- Caption blocks below each panel
- Component variants for fast swapping

**Page 2: IG Carousel template (1080×1350 portrait)**
- Frame 1: Hero opening (image fill)
- Frames 2-3: Context (image OR text on matte black)
- Frames 4-5: Process (BTS or alternate angle)
- Frames 6-7: Output variations (deployment crops)
- Frame 8: Closing card · matte black + one-line CTA + small SNIPED logotype
- All frames: SNIPED type system locked (Inter Tight or similar editorial sans)

**Page 3: LinkedIn POV image template (1080×1350)**
- Single image area with subtle 4-6 line caption overlay (optional · most posts use the LinkedIn caption field, not on-image text)

**Page 4: IG Reel cover frame (1080×1920)**
- Vertical Hero crop area
- Optional title bar (used sparingly · 80% of Reels need no on-cover text)

**Page 5: Carrd block templates**
- Hero block (1920×1080)
- Problem block (1920×800)
- Reset CTA block (1920×600)
- Selected Work grid (1920×1200, 6-image grid)

**Page 6: VIB reference pool**
- 12-16 SNIPED archive frames imported and tagged by demographic (M/F, age 20s-50s, dark/light skin, business/creative wardrobe register, studio/on-location)
- Each frame is a Figma component for fast drop-in to the VIB Master

**Time:** 90 min for someone moderately fast in Figma. Faster if you start from `/03_OUTREACH/VIB_figma_spec.md`.

---

## Hour 4 · Notion CRM build

### Per `/04_CRM/notion_crm_schemas.md` · 5 linked databases

**Phase 1 · Build 3 DBs this Saturday:**
1. **Pipeline** (Kanban view + Forecast view + Day-30 trigger view)
2. **Clients** (table view)
3. **Outreach** (Kanban view + Reply rate analytics view)

**Defer to Week 2:**
4. **Shoots**
5. **Galleries**

### Step-by-step (90 min)

1. Create Notion workspace `SNIPED Operating System` (or use existing)
2. Create three new databases per the schema doc
3. Set up the relations between Pipeline ↔ Clients ↔ Outreach
4. Build the formulas:
   - Forecast value: `prop("Estimated value") * (parseInt(replaceAll(prop("Probability"), "[^0-9]", "")) / 100)`
   - Days since last touch: `dateBetween(now(), prop("Last touch"), "days")`
5. Build 3 views per DB:
   - Pipeline: Kanban by Status · Active VIBs (filter Status=Engaged) · Day-30 trigger (filter Status=Reset Delivered AND Days since last touch ≥ 28)
   - Clients: All clients · LinkedIn-warmed (filter Source=LinkedIn) · High-value (filter Lifetime value > $5000)
   - Outreach: This week's sends (filter VIB sent date in last 7 days) · Reply pending (filter Reply status=No reply AND VIB sent date in last 14 days)
6. Create the Operator Dashboard page (top-level Notion page that embeds:
   - VIBs sent this week (count from Outreach)
   - Discovery calls held this week (count from Outreach)
   - Cash collected this week (sum from Pipeline status=Cash Collected)
   - Active Resets in delivery (count from Shoots when built)
7. Test by entering 3 fake rows in each DB · confirm relations work and views filter correctly

### What to enter as the FIRST real data

- Outreach: VIB #1 placeholder (do not send the VIB until this Saturday's build is complete)
- Pipeline: Davis Law / Tracy reactivation card (Status: `Re-engage 90d`)
- Pipeline: Sasha shoot card (Status: `Discovery Booked` if discovery already happened)
- Clients: Larry Bernard, Pearl, Jamie, Hermine (network nodes, not pipeline cards)

---

## Hour 5 · Email + scheduling stack live

### Google Workspace at @snipedmedia.com (15 min)

1. Buy domain if not owned (already owned per spine)
2. Sign up Google Workspace Business Starter ($7.20/mo)
3. Verify domain ownership
4. Migrate one inbox: bj@snipedmedia.com OR bryce@snipedmedia.com
5. Set up email signature:
   ```
   Bryceden Jones
   SNIPED Media · Operator-coded visual systems for LA founders
   2715 S Main St · DTLA
   snipedmedia.com
   ```
6. Update LinkedIn profile email to @snipedmedia.com (credibility upgrade)

### Calendly Pro setup (30 min)

1. Sign up Calendly Pro ($12/mo)
2. Create 3 event types:
   - **10-min Discovery** (cold prospects)
   - **15-min Op Kit Discovery** (Day-30 pitches that converted to a call)
   - **45-min Reset shoot** (after deposit paid)
3. Connect to Google Calendar
4. Set availability: weekday evenings 6-8 PM PT, Saturday 10 AM-4 PM PT
5. Block: engineering travel weeks (sync with Serverfarm calendar)
6. Auto-message after booking: "Confirmed for [DATE] at [TIME]. Reply to confirm. Pre-shoot brief tomorrow."

### Stripe setup (30 min)

1. Connect to LA LLC bank account
2. Create products:
   - Reset deposit: $750
   - Reset balance: $750
   - Sprint full: $750
   - Op Kit deposit: $1,500-2,500 (50% of price)
   - Op Kit balance: same
3. Save invoice templates with line items
4. Test: create a $1 invoice, send to your own email, pay it, verify it lands

### Pixieset Pro (30 min)

1. Sign up Pixieset Pro ($30/mo)
2. Build the master Reset gallery template per `/06_DELIVERY/pixieset_config.md`:
   - 3 collections: Heroes, Selects, Proofs
   - Heroes: download enabled, full-res
   - Selects: download enabled, full-res
   - Proofs: download disabled, "upgrade" UI active
   - Branding: minimal, dark mode, SNIPED type
   - Expiry: Delivery + 14 days
3. Test: create a fake gallery with 5 sample images, deliver to yourself, verify the upgrade UI works

---

## Hour 6 · Final: install the daily reflexes

### Notion mobile app

- Install on phone
- Pin to home screen
- Test logging a fake VIB sent in 30 seconds (this is the friction test · if logging takes 90 sec, the friction will kill consistency)
- Set up widgets: Pipeline, Outreach (mobile widget shows next action)

### Calendar reminders (recurring)

Install these as repeating calendar events:
- **Mon 7-9 PM PT:** Protected Hour (VIB production)
- **Tue 7 AM PT:** Send VIBs #1, #2 + LinkedIn POV draft
- **Wed 7 AM PT:** Send VIBs #3, #4
- **Thu 7 AM PT:** Send VIBs #5, #6 + LinkedIn POV post (alternate week from carousel)
- **Fri 5-6 PM PT:** Pipeline review + week wrap
- **Sun 7-8 PM PT:** Weekly Review (per `/00_BRIEF/templates/weekly_review.md`)
- **Last Mon of every month, 7-9 PM PT:** Constraint Audit (per `/00_BRIEF/templates/monthly_constraint_audit.md`)
- **Quarterly first week, 60 min:** Hook library refresh + LinkedIn POV bank refill if running low

### The Saturday Build commit · final 15 min

- [ ] Folder structure live on SSD (Hour 1)
- [ ] Lightroom + Evoto presets installed (Hour 2)
- [ ] Figma master file with 6 pages (Hour 3)
- [ ] Notion 3 DBs live + dashboard (Hour 4)
- [ ] Google Workspace + Calendly + Stripe + Pixieset all live (Hour 5)
- [ ] Mobile reflexes installed + calendar locked (Hour 6)

If all 6 are checked at end of Saturday: VIB #1 ships Tuesday. Phase 1 is fully operational.

If 4-5 are checked: ship VIB #1 Wednesday or Thursday. Finish remaining hour on Sunday.

If <4 are checked: the Saturday Build runs again next weekend. Do not ship VIB #1 on a half-built system.

---

## Cost summary (one-time vs recurring)

| Category | One-time | Monthly | Annual |
|---|---|---|---|
| Hardware (SSD + 2x HDD + reader) | $450-540 | n/a | n/a |
| Google Workspace | n/a | $7.20 | $86 |
| Calendly Pro | n/a | $12 | $144 |
| Stripe | n/a | 2.9% per txn | scaled |
| Pixieset Pro | n/a | $30 | $360 |
| Notion | n/a | $0 (free tier works for first 90 days) | $0-96 |
| Backblaze B2 (Phase B+) | n/a | $5-15 | $60-180 |
| HelloSign / Dropbox Sign | n/a | $20 | $240 |
| Domain (snipedmedia.com) | n/a | renewal $15/yr | $15 |
| **Total** | **~$500 one-time** | **~$80/mo** | **~$1100/yr** |

This is the total stack cost to run SNIPED through Phase 1 and into Phase B. Every Reset booked at $1,500 covers ~6 months of stack overhead. The cost ratio is correct.

---

## What this brief deliberately did NOT cover

- Camera + lens upgrades (gear is not Phase 1 leverage; current Canon EOS RP + 85mm + 35mm is sufficient)
- Studio rental (DTLA studio at 2715 S Main is the anchor; Larry's space + Peerspace as fallback)
- Lighting upgrades (current setup works; Profoto B10 / Aputure 600d come with Phase B revenue)
- Backup camera body (acquire when first $5K month happens, not before)
- New software subscriptions beyond the locked stack

The architecture is opinionated. Stick to it.

---

## After the Saturday Build

VIB #1 ships next Tuesday. Email templates are at `/06_DELIVERY/email_templates/`. Caption library and hooks at `/07_CONTENT/`. Production checklists at `/05_PRODUCTION/`. Cockpit + audit templates at `/00_BRIEF/templates/`. Scripts at `/scripts/`.

Run `/00_BRIEF/MONDAY_COCKPIT.md` to scaffold the first real operational week.

The system is now infrastructure, not figuring-it-out.
