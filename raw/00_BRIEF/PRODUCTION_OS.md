# Production OS · SNIPED execution mechanics

**The operational layer. How the work moves through the system. No philosophy. No strategy. Just routing, files, hands, tools, sequencing.**

This doc sits alongside CANONICAL_TRUTHS.md (strategic anchor) as the operational anchor. Existing SOPs (`/05_PRODUCTION/`, `/06_DELIVERY/`, `/03_OUTREACH/`) cover specific procedures; this doc covers the architecture they live inside, plus the gaps not yet captured (folder structure, naming, storage, content pipeline, AI routing, delegation specs, templates, automations).

Read this once. Reference Section 5 (operational flows) and Section 7 (templates + automations) repeatedly.

---

## 1. Workspace + storage architecture

### 1.1 Production folder structure (per shoot)

Every shoot gets one root folder, structured identically. Located on the working SSD at `/SNIPED_PRODUCTION/YYYY/`.

```
/SNIPED_PRODUCTION/
  /2026/
    /2026-05-18_Sasha_FreeCollab/
      00_BRIEF/        · pre-shoot brief, contract, model release, mood ref
      10_RAW/          · untouched .CR3 files from SD card
      20_CULLED/       · Lightroom catalog (.lrcat) + smart previews
      30_HEROES/       · final retouched .tif (master) + .jpg (deliverable)
      40_SELECTS/      · color-graded .jpg only
      50_PROOFS/       · batch-graded .jpg only
      60_DELIVERY/     · Pixieset upload bundles (zipped per tier)
      70_BTS/          · phone footage (.mp4), still grabs, audio (.wav)
      80_CONTENT/      · Reel renders, carousel exports, captions.md
      90_NOTES/        · post-shoot notes (what worked, what didn't)
```

This structure is locked. Every shoot produces all 9 subfolders even if some stay empty. Empty subfolders signal "did not happen this shoot," not "lost in the system."

### 1.2 Workspace folder structure (existing, do not change)

```
/SNIPED_OS/                    · the operating system (this is where you are)
/SNIPED_PRODUCTION/            · all shoot assets (NEW · separate from OS)
/SNIPED_ARCHIVE/               · cold storage (mirrored HDD)
/SNIPED_CONTENT_LIBRARY/       · evergreen content templates + ready-to-post
```

Critical: `/SNIPED_OS/` (strategy + SOPs) is separate from `/SNIPED_PRODUCTION/` (asset files). Assets do not pollute the OS folder. Strategy does not pollute the asset folder.

### 1.3 Naming conventions

**Shoot folder:** `YYYY-MM-DD_ClientLastName_TYPE`
- Type values: `Reset`, `Sprint`, `OpKit`, `BrandSystem`, `FreeCollab`, `FreeCommunity`, `FreeAccess`, `Personal`, `ArtSeries`, `CulturalDoc`, `BTSDay`
- Example: `2026-06-15_DavisLaw_Reset`

**File names within folders:**
| Type | Pattern |
|---|---|
| Hero (master) | `SNIPED_2026-06-15_DavisLaw_HERO_001.tif` |
| Hero (deliverable) | `SNIPED_2026-06-15_DavisLaw_HERO_001.jpg` |
| Select | `SNIPED_2026-06-15_DavisLaw_SEL_001.jpg` |
| Proof | `SNIPED_2026-06-15_DavisLaw_PRF_001.jpg` |
| BTS clip | `SNIPED_2026-06-15_DavisLaw_BTS_001.mp4` |
| Carousel export | `SNIPED_2026-06-15_DavisLaw_CAR-IG_01.jpg` (frames numbered 01-08) |
| Reel render | `SNIPED_2026-06-15_DavisLaw_REEL.mp4` |
| Caption file | `SNIPED_2026-06-15_DavisLaw_CAPTIONS.md` |

**Reasoning:** SNIPED prefix lets you find any file from a global search. Date + client + type lets you sort chronologically and filter. Three-digit sequence handles up to 999 frames per type per shoot. No spaces, no special characters except hyphens and underscores.

**Naming rule for content originals:** never rename a RAW file. Only outputs get the SNIPED naming pattern.

### 1.4 Storage tiering

| Tier | Location | Contents | Capacity | Cost |
|---|---|---|---|---|
| **Hot** | Working SSD (1-2TB Samsung T7 / SanDisk Extreme Pro) | Last 60 days of shoots · current edits | 1-2TB | $100-200 one-time |
| **Warm** | Primary HDD (8TB external · Seagate or WD) | Last 12 months · all delivered work | 8TB | $150 one-time |
| **Cold** | Mirror HDD (8TB external · stored at home, NOT in studio bag) | Year+ archive | 8TB | $150 one-time |
| **Cloud** | Backblaze B2 OR rclone to Google Drive | Everything from /30_HEROES/ + /50_PROOFS/ + /80_CONTENT/ | Variable | $5-15/mo |

**Critical rule:** RAW files (`/10_RAW/`) live on Hot+Warm only. Cloud cost for RAW backup is too high relative to recovery value (you can reshoot before you can re-pay $50/month for years to keep RAWs in cloud). Heroes, Selects, Proofs, content exports go to cloud.

### 1.5 Backup discipline (3-2-1 rule, modified for cost)

After every shoot, before closing the laptop:

1. SD card → Hot SSD ingest (working copy)
2. Hot SSD → Warm HDD mirror (rsync command, 5 min)
3. Card stays full and unformatted until both copies verified
4. After delivery: HDD → Cold HDD mirror (manual, monthly batch)
5. After delivery: Heroes/Selects/Proofs → cloud (auto via Backblaze B2 watch folder)
6. Card formatted only after step 5 complete

The mirror command (one shell function, alias it in `.zshrc`):
```bash
sniped_backup() {
  rsync -avh --progress "$1" /Volumes/SNIPED_WARM/SNIPED_PRODUCTION/
}
```

Restore drill: every 90 days, attempt to restore one random shoot from cold or cloud to verify backups work. Calendar reminder.

---

## 2. Photo pipeline (capture → archive)

The full procedural detail lives in `/05_PRODUCTION/SOP_capture_to_delivery.md`. This section documents the workflow shape; the SOP documents step-by-step actions.

The Lightroom-specific runbook (catalog architecture, import preset, color label vocabulary, smart collections, AI mask stack, retouch decision tree, export presets) lives in `/05_PRODUCTION/lightroom_operating_system.md`. The preset definitions live in `/05_PRODUCTION/preset_library.md`. The retoucher onboarding pack (Phase B trigger) lives in `/05_PRODUCTION/retoucher_training_notes.md`.

**Catalog policy:** one master catalog per year at `/SNIPED_PRODUCTION/_catalogs/SNIPED_YYYY.lrcat`. Smart Collections do per-shoot organization. Per-shoot catalogs are NOT used (they fragment search and break the 12-collection smart system).

### 2.1 Ingest (15 min after every shoot, same day, non-negotiable)

1. Card → USB-C reader (no laptop card slot · slower)
2. Photo Mechanic Plus auto-import OR Lightroom Classic import to `/10_RAW/`
3. Verify file count matches camera display
4. Run `sniped_backup` to mirror HDD
5. Confirm both copies bit-identical (Photo Mechanic verify)
6. Eject card, label "DO NOT FORMAT" until next shoot day
7. Notion: Shoots DB → status `Captured`

### 2.2 Cull (15-25 min, same day or next morning · compressed via assisted culling)

Lightroom Classic, five-pass system. Pass 0 is automatic at import; Passes 1-4 are manual.

| Pass | Action | Tool | Time per shoot |
|---|---|---|---|
| 0 · Assisted cull | AI auto-rejects OOF, eyes-closed, blink, exposure failures | Lightroom Assisted Culling at import | 0 manual min (saves 30-45 min) |
| 1 · Reject refinement | Verify auto-rejects · X any AI-missed failures | `X` key | 5-8 min |
| 2 · Pick pass | Mark P for keepers | `P` key | 8-12 min |
| 3 · Star pass | Rate 3-5 stars on Picks (3 = Proof, 4 = Select, 5 = Hero candidate) | Number keys | 5-10 min |
| 4 · Color label pass | On 5-star candidates, label Red (heavy retouch) or Yellow (standard pipeline) | Number keys 6-9 | 2-3 min |

Output: Smart Collection `01 · Heroes Pending Retouch` auto-populates with the 5-star Red + Yellow frames (per `/05_PRODUCTION/lightroom_operating_system.md` Section 3.4). Target Hero count per shoot type per `/01_OFFERS/delivery_architecture_v2.md` Section 2.

### 2.3 Hero edit (12-15 min/Hero, target time)

Each Hero runs through the locked workflow defined in `/05_PRODUCTION/lightroom_operating_system.md` Sections 5-7. Summary stack:

1. Lightroom locked-look applied on import (`SNIPED_LOCKED_LOOK_v1` preset · WB, tone curve, HSL, lens correction, calibration)
2. Per-image develop adjustments in locked order (Section 5.2 of the OS doc)
3. AI mask stack: 5 masks per `/05_PRODUCTION/lightroom_operating_system.md` Section 6.1 (Subject, Face Skin, Eyes, Teeth, Background)
4. Generative Remove for in-Lightroom cleanup of background distractions
5. Decision tree (Section 7 of the OS doc): route Yellow → Evoto, route Red → Photoshop
6. After Evoto round-trip: apply `SNIPED_HERO_FINISH_v1` preset
7. Export via `SNIPED · Hero · JPG Deliverable` and `SNIPED · Hero · TIF Master` presets to `/30_HEROES/`
8. Topaz Photo AI sharpen pass on .jpg only (export step)
9. After delivery, change color label to Green (Heroes Live)

Per Hero target: 12-15 min. If a Hero exceeds 25 min, stop, ship as-is or downgrade to Select. Time-cap discipline > perfection.

### 2.4 Select edit (1-2 min/Select)

Selects do NOT get Evoto, do NOT get Photoshop. Selects get:
- Lightroom base preset
- Color grading from preset stack
- Export `.jpg` to `/40_SELECTS/`

If a Select is tempted into Hero territory mid-edit, that's drift. Either commit it to Hero scope (and the time cost) or ship as Select.

### 2.5 Proof edit (30-45 sec/Proof)

Lightroom batch action:
- Apply SNIPED Proofs preset (light grade, slightly less than Selects)
- Batch export to `/50_PROOFS/`

100 proofs × 45 sec = 75 min. The Proofs tier is volume work. Run in background while doing other tasks.

### 2.6 Export standards (locked)

| Tier | Format | Color Space | Resolution | Compression | Watermark |
|---|---|---|---|---|---|
| Hero (deliverable) | .jpg | sRGB | Full (~6000px long edge) | Quality 90, no resize | None |
| Hero (master archive) | .tif | ProPhoto RGB | Full | LZW lossless | None |
| Select | .jpg | sRGB | Full | Quality 85, no resize | None |
| Proof | .jpg | sRGB | 2400px long edge | Quality 80 | None |
| IG Carousel | .jpg | sRGB | 1080×1350 (portrait) OR 1080×1080 (square) | Quality 90 | None |
| IG Reel cover | .jpg | sRGB | 1080×1920 | Quality 90 | None |
| LinkedIn POV image | .jpg | sRGB | 1080×1350 | Quality 90 | None |
| Carrd Selected Work | .jpg | sRGB | 2000px long edge | Quality 85 | None |
| Press / submission | .tif or high-res .jpg | Adobe RGB or sRGB | Full | Per recipient spec | None |

Watermarks: never on hero work. They cheapen the perception. Pixieset has gallery-level watermark protection if abuse is a concern; SNIPED brand identity comes from the work, not from a watermark.

### 2.7 Delivery (20-30 min, Day 5 of Reset SLA)

Per `/06_DELIVERY/pixieset_config.md`:
1. Pixieset master Reset gallery template → duplicate
2. Heroes collection: download enabled, full-res, visible
3. Selects collection: download enabled, full-res, visible
4. Proofs collection: gallery view only, download disabled, "upgrade to Hero" UI on each frame
5. 14-day expiration set
6. Send delivery email per `/06_DELIVERY/SOP_post_delivery.md` Day-0 template
7. Notion: Shoots DB → status `Delivered`, log gallery URL, Pipeline → `Reset Delivered`

### 2.8 Archive (Day 30 after delivery)

After upgrade window closes:
1. Move shoot folder from Hot SSD → Warm HDD (rsync mirror)
2. Verify Warm copy matches Hot (rsync --dry-run --checksum)
3. Delete Hot copy (now living on Warm + Cold + Cloud for Heroes/Selects/Proofs)
4. Update Notion: Shoots DB → `Archived`
5. RAW files: stay on Warm + Cold only (no cloud)

---

## 3. Content pipeline (one shoot → 8 outputs)

Every Reset is briefed pre-shoot to produce these outputs, not just the client gallery. This is the operational layer the audience_engine.md doc names without specifying.

### 3.1 BTS capture (during shoot day)

Phone clipped to small tripod or handheld by Hermine MUA / Pearl / collaborator if present. Capture during natural beats:
- 3 setup shots (lighting being adjusted, modifiers, the empty set before subject)
- 2 subject-arrives moments (handshake, brief intro)
- 5 in-action clips (you directing, subject reacting, the protocol diagnostic moment)
- 2 between-frames clips (subject relaxing, the in-between moment per Aesthetic v1 growth edge)
- 1 final-frame moment (the last shot taken, you nodding)

Total: ~15 clips, 5-15 sec each. Files saved to phone. Same-day AirDrop to laptop into `/70_BTS/`.

**No talking-to-camera Bryce footage during paid client shoots** (client experience first). Talking-to-camera Bryce content gets captured on dedicated BTS Content Days (Section 5.5).

### 3.2 Reel production (BTS Cut format · 30-60 sec)

Per `/07_CONTENT/sniped_video_philosophy.md` Format 1 spec:
1. Open CapCut on iPad or laptop
2. Import BTS clips from `/70_BTS/`
3. Cut to 6-9 clips, 3-7 sec each
4. Music: locked rotation of 5-7 tracks from CapCut's royalty-free pool (build the rotation once, reuse · brand consistency)
5. No text overlays beyond opening name/title card
6. Color grade clips to match SNIPED palette (subtle desaturation, contrast bump)
7. Export 1080×1920 .mp4 to `/80_CONTENT/`
8. Caption draft saved to `/80_CONTENT/CAPTIONS.md`

Target time: 30-45 min/Reel.

### 3.3 IG Carousel production (8-frame template)

Slot 1: Hero frame · 1080×1350 portrait
Slots 2-7: 4-6 additional Heroes or context frames
Slot 8: Closing card (matte black with one-line CTA)

Build in Figma OR pre-built Lightroom export preset for 1080×1350 crop. Save preset, never re-build.

### 3.4 LinkedIn POV production (single image)

1 Hero from `/30_HEROES/`, cropped to 1080×1350 portrait. Caption per the LinkedIn POV bank rotation (`/07_CONTENT/linkedin_pov_bank.md`). Posted Tue or Thu, 7-9 AM PT.

### 3.5 IG Stories (live, same day)

Phone-native. 5-8 stories during shoot day. Stickers: location (DTLA), music sticker, occasional poll ("which crop · A or B?"). Stories are not edited, not exported, not archived. They run live and expire. Highlights reel curates the best 6-10 per quarter (1 hour quarterly task).

### 3.6 Caption framework

All captions follow this scaffold:

```
HOOK (one line · the protocol or insight named)

CONTEXT (3-5 lines · why it matters)

DEPLOYMENT (1-2 lines · where this shows up in the buyer's reality)

CTA or close (1 line · "DM SNIPED for the diagnostic" or just "·")
```

Caption library (existing): `/03_OUTREACH/VIB_caption_library.md` for VIB-side. LinkedIn POV bank for content-side captions.

### 3.7 Hook library (build once, rotate)

Top hooks for protocol-named LinkedIn:
- "Most LA founder photos fail at one specific layer."
- "There are 10 protocols. Most photographers don't run any of them."
- "The camera reads two layers. Most founders fail one or both."
- "The fix isn't a better photographer."
- "Pricing isn't the problem. Direction is."
- "Headshots fail in the same 6 mechanical and 4 psychological ways."

Top hooks for cultural documentation:
- "I shot a [institution] this week."
- "[Subject's name]. [Role]. [Context]."
- "What gets photographed gets remembered."
- "The body of work tells you what mattered."

Top hooks for BTS Reels (caption + on-screen):
- "Setting up for a Reset."
- "10-protocol diagnostic in motion."
- "The 90-second opener."

Maintain in `/07_CONTENT/hook_library.md` (build when you have 5 minutes; not before VIB #1 ships).

### 3.8 Scheduling logic

| Platform | Tool | Cadence | Auto-schedule lead time |
|---|---|---|---|
| LinkedIn POV | LinkedIn native scheduler | Tue + Thu, 7-9 AM PT | Draft same morning, post live |
| LinkedIn carousel | LinkedIn native scheduler | 1x/week (alternate week from POV) | Draft Sunday, schedule Monday |
| IG Carousel | Buffer or Later | 1x/week | Schedule 24-48h ahead |
| IG Reel | Buffer or Meta Business Suite | 2-3x/week (per audit recommendation) | Schedule 24-48h ahead |
| IG Stories | Phone native | Live during shoots | None (live only) |
| TikTok | Native or Buffer | Cross-post Reels with TikTok-native first 3 sec | Same day as IG Reel |
| YouTube Shorts | Native | Cross-post Reels | Same day as IG Reel |

Phase 1 starts manual posting. Buffer/scheduling tools enter at Phase B trigger.

### 3.9 Repost / recycle logic

Every piece of content recycles:
- LinkedIn POV from 6 months ago → reposted with one updated insight (LinkedIn algorithm doesn't penalize)
- IG Carousel hero frames → re-used as LinkedIn single-frame after 90 days
- BTS Reel → cropped to 9:16 still and posted as IG single-frame after 30 days
- Cultural Doc carousel → essay-formatted Substack post (Q3+) after 60 days

Never re-post identical content within 30 days on the same platform. Across platforms: same day or 7 days later is fine.

---

## 4. AI tool routing

### 4.1 Photo AI stack

| Tool | Role | When to use | When NOT to use |
|---|---|---|---|
| Lightroom Classic | Cull, base color, tone, masked adjustments, Generative Remove for in-LR cleanup | Every shoot | n/a |
| Evoto | Skin retouch + body subtle + backdrop color change/replace/cleanup within studio register + AI Color Match (batch style propagation) + AI Color Looks (built-in cinematic presets) + frequency separation (Brand System tier) + sculpt dodge & burn + AI Transform (one-click straighten) + tethered shooting (Phase B+) | Every Hero · primary backdrop + skin + advanced retouch tool | Selects, Proofs |
| Topaz Photo AI | Sharpening + denoise on output, upscaling AI background plates | Hero export step + Track B comp upscaling | Selects, Proofs (waste) |
| Photoshop | Final compositing, frequency separation, Track B AI-background-plate assembly (Neural Filter Harmonize + edge lights + grain + color wash · per Gress 5-step playbook in `/10_REFERENCE/AI_PHOTOGRAPHERS_TACTICAL_EXTRACTION.md`) | Red-label frames + Brand System tier + Track B creative push on collab/portfolio | Routine work (Evoto handles) |
| Adobe Firefly | Background plate generation · soft cityscape, atmospheric, beach, color wash · for Track B compositing | Track B creative push only | Subject generation (NEVER · Berger violation) |
| Google Nano Banana Pro (via Gemini or Freepik) | Background plate generation · narrative scenes (stadium, hotel, urban, tunnel) with structured prompting | Track B creative push when scene needs photographic plausibility | Subject generation (NEVER) |
| Midjourney | Background plate · stylized / artistic register only | Track B when register is intentionally stylized | Subject generation (NEVER) |
| Leonardo AI / Gemini reprompting | Pre-shoot moodboards · Direction Stack Protocol 2-3 alignment | Internal pre-shoot only | Delivered work (NEVER · pre-viz is alignment, not output) |
| Capture One | Color-critical commercial work (Op Kit, Brand System) | Phase B+ option | Phase 1 (Lightroom is enough) |

**The Camp B rule (absolute):** AI tools are utility behind the methodology. They generate inputs (backgrounds, moodboards, plates). They never generate the subject. They never replace the photographer's eye. The Track B creative push pipeline (real subject + AI background plate + Photoshop assembly) is the documented professional workflow per the Gress playbook. Berger / Sax / Petty validation in `/10_REFERENCE/intel_ai_photographer_market.md`.

### 4.2 Content AI stack

| Tool | Role | When | Never |
|---|---|---|---|
| Claude (this) | LinkedIn POV draft, caption polish, brief drafting, email composition, SOP writing | Daily | Don't let it write final voice without BJ pass |
| ChatGPT | Backup when Claude rate-limited | Backup | Same |
| Gemini | Idea generation, broad research | Light use | Don't use for SNIPED voice |
| CapCut | Reel editing | Same-day post-shoot | n/a |
| Premiere Pro | Long-form (Cultural Doc essay video, future Founder Profile) | Phase B+ | Phase 1 BTS Cuts (CapCut is enough) |
| Veed.io / Descript | Auto-caption Reels, voiceover transcription | Reels with captions | n/a |
| ElevenLabs | Voiceover synthesis | Cultural Doc essays only (Phase B+) | VIBs (creepy), client deliverables |
| Pixelcut / Canva | Quick design (Carrd graphics, deck slides) | Light use | Brand assets (use Figma) |
| Figma | VIB master, Carrd assets, IG carousel templates, brand assets | Daily | n/a |

### 4.3 Strategy AI stack

| Tool | Role |
|---|---|
| Claude | Strategic analysis, doc audits, decision pressure-testing, partnership-protocol work |
| ChatGPT | Brainstorm + alternative perspective |
| Gemini | Deep research with Google integration |

Rule: One AI per task type. Don't cross-validate by running the same prompt across all three. That's fake-productive thinking.

### 4.4 AI image + motion stack (REPOSITIONED 2026-05-12)

#### Image generation (still composites · for IG creative engine, never client work)

| Tool | When | Never |
|---|---|---|
| **Seedream 5.0 Lite** (via fal.ai) | Plate generation for Track B composites · HEX palette + camera cheat codes work | Subject generation (identity rule) |
| **Seedream 4.5** (via fal.ai) | Identity-preserving composite when face must hold (better than 5.0 for faces) | Client deliverables |
| **Nano Banana Pro** (via Gemini) | Identity-preserving composite, urban narrative plates | Client deliverables |
| **Higgsfield Soul** | Plate generation, Image Pack (multiple hero variations from one subject) | Subject generation |
| **Adobe Firefly Fill & Expand** (in Photoshop) | Background replacement with Reference Image · the lite composite primary | Client deliverables |
| **Photoshop Generative Fill** | Same as Firefly above, in the Photoshop layer | Same |
| **ChatGPT Image Gen** | Brand boards, multi-perspective ref, iterative art-director mode | Subject in client work |

See: `/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md`, `/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md`, `/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md`, `/10_REFERENCE/PHOTOSHOP_GENERATIVE_FILL_REFERENCE_IMAGE_EXTRACTION.md`.

#### Higgsfield Content Factory (orchestration · Phase B+ activation)

When Higgsfield MCP is installed in Claude, the 4-stage Content Factory pipeline (research → plan → generate → schedule to Meta Ads) becomes available. For SNIPED-internal content velocity, NOT a parallel brand. See `/10_REFERENCE/HIGGSFIELD_TACTICAL_EXTRACTION.md`.

#### Animation / motion AI stack (unchanged)

| Tool | When | Never |
|---|---|---|
| Kling AI | Post-conversion delivery moments (Reset client surprise asset) | Cold prospect outreach (creepy) |
| **Higgsfield Marketing Studio** | Motion content + UGC reels (still: Phase B+ for parallel brand consideration) | Cold prospect outreach |
| **Seedance 2** | Video gen from stills (paired with Image Pack pipeline) | Client deliverables |
| Runway ML | Cultural Doc essay motion (Phase B+) | Client deliverables without permission |
| Pika Labs | Optional alternative | Same |

### 4.5 What NEVER gets outsourced (to AI or humans)

Per `/00_BRIEF/OPERATIONAL_BACKBONE.md` Section 2:
- Direction Stack diagnostic on every shoot
- 90-second on-set opener
- Pricing decision (holding the price)
- Methodology refinement
- Year-10 vision decisions
- Top-network relationship conversations (Larry, Pearl, Tracy, top 5 client referrers)
- Aesthetic call (which frames make Hero, Select, Proof)
- The decision to decline
- Substack essay voice (Q3+)
- Book authorship

### 4.6 What SHOULD be delegated to AI ASAP (free leverage)

- Hero edit retouch (Evoto already doing this, expand usage)
- Caption first drafts (Claude)
- Email first drafts (Claude)
- Pre-shoot brief drafting (Claude, fed shoot details)
- Notion DB property formula construction (Claude)
- Reel auto-captions (Veed/Descript)
- Color batch processing (Lightroom presets · this is "AI" via deterministic algorithm)
- LinkedIn POV scheduling decisions (just use the bank rotation, no AI needed; rule replaces decision)

---

## 5. Operational flows (per scenario)

Each scenario maps day-by-day actions. Times shown in BJ-time-investment, not elapsed time.

### 5.1 Paid Reset client (10 days end-to-end · 7-day SLA)

| Day | Action | Time | Surface |
|---|---|---|---|
| -10 | Booking confirmed via Calendly + Stripe deposit paid | auto | Stripe + Calendly |
| -10 | Notion: Pipeline → `Reset Booked`, Shoots DB row created | 5 min | Notion |
| -7 | Calendly auto-sends pre-shoot brief email (Phase B+ · manual until then) | 10 min manual / 0 auto | Email template `/06_DELIVERY/email_templates/01_pre_shoot_brief.md` |
| -3 | Wardrobe + location + parking confirmation reply check | 10 min | Email |
| -1 | Final logistics text/email + weather check | 5 min | Phone/email |
| 0 (shoot day) | Pre-arrival: studio prep, lighting set, gear check (45 min) | 45 min | Studio |
| 0 | Shoot: 90-sec opener + 45-min session + Direction Stack diagnostic | 45 min | Studio |
| 0 | Same-day: ingest + backup (Section 2.1, 2.2) | 15 min | Laptop |
| 0 | BTS phone footage AirDropped to `/70_BTS/` | 5 min | Phone+laptop |
| 0 | Notion: Shoots → `Captured` | 1 min | Notion |
| 1-2 | Cull (Section 2.2) | 30-60 min | Lightroom |
| 2-4 | Hero retouch · 10-12 Heroes × 12-15 min = 2-3 hr | 2-3 hr | LR + Evoto + PS |
| 3-5 | Select edit (Section 2.4) | 30-45 min | Lightroom |
| 4-5 | Proof export (Section 2.5, run in background) | 5 min active / 75 min passive | Lightroom |
| 5 | Pixieset upload + delivery email | 30 min | Pixieset + email |
| 5 | Notion: Shoots → `Delivered`, log Pixieset URL | 2 min | Notion |
| 5 | BTS Reel cut + posted (Section 3.2) | 45 min | CapCut + IG |
| 7 | Day-7 testimonial ask | 5 min | Email/DM |
| 14-21 | Carousel + LinkedIn case-study post (with subject permission) | 60 min | Figma + IG + LinkedIn |
| 19 | 14-day upgrade window closing reminder to client | 2 min | Email |
| 30 | Day-30 Op Kit pitch (per `/06_DELIVERY/SOP_post_delivery.md`) | 20 min | DM/email |
| 30 | Archive shoot folder (Section 2.8) | 5 min | rsync |
| 90 | Re-engagement check / referral ask | 10 min | Email |

**Total BJ time per Reset: ~7-9 hours.** This is the operational baseline. Hours above this number = drift; hours below = cutting corners on quality.

### 5.2 Strategic Free Collab (compressed Reset)

Per `/05_PRODUCTION/SOP_strategic_free.md` Collab section.

| Day | Action | Time |
|---|---|---|
| -5 | Schedule + Collab Agreement signed (`/02_CONTRACTS/01_collab_agreement.md`) | 15 min |
| 0 | Shoot 60-90 min (smaller scope vs Reset) | 60-90 min |
| 0 | Same-day ingest + backup | 15 min |
| 1 | Cull (smaller volume · 20-30 min) | 30 min |
| 2-3 | 3-5 Heroes retouched | 60-75 min |
| 3 | 15-25 Selects edited | 30-45 min |
| 5-7 | Pixieset light gallery delivered (Heroes + Selects only · no Proofs upgrade tier for free work) | 30 min |
| 7 | Testimonial / referral ask | 5 min |
| 14-21 | 1 IG carousel + LinkedIn POV (with subject's permission) | 60 min |
| 30 | Archive | 5 min |

**Total BJ time per Collab: ~4 hours.** Cap. If a Collab demands more, downgrade scope or convert to Sprint ($750).

### 5.3 Community Free shoot (institutional)

Per `/05_PRODUCTION/SOP_strategic_free.md` Community section + `/13_NETWORK/access_and_community_architecture.md` Lane 2.

| Day | Action | Time |
|---|---|---|
| -7 | Scout + permission confirm with institution lead | 30 min |
| -1 | Pre-event prep (gear pack, second body if needed) | 20 min |
| 0 | Multi-hour event capture (3-5 hrs · candid + named-subject portraits) | 3-5 hr |
| 0 | Same-day ingest + backup | 30 min |
| 1-3 | Cull (200-500 frames, slower) | 60-90 min |
| 5-10 | 5-10 named-subject Heroes + 30-50 institutional Selects + 60-100 Proofs | 3-5 hr |
| 14 | Deliver Pixieset gallery + 2-3 framed prints to institution lead (reciprocity) | 60 min |
| 14-21 | IG carousel + LinkedIn essay (with permission) | 90 min |
| Q3+ | Substack essay (when Substack live) | 2-3 hr |

**Total BJ time per Community shoot: ~12-15 hr.** This is the volume Phase 1 lean override caps at quarterly.

### 5.4 Founder/Editorial shoot (Op Kit · Phase B+)

Same procedural structure as Reset, expanded:
- Pre-shoot brief: longer, includes 3-5 looks and license schedule
- Shoot: 2-3 hr session
- Heroes deliverable: 25-35
- Selects: 80-120
- Proofs: 150+
- Delivery SLA: 7 days
- Edit time: 5-7 hr per Op Kit
- Commercial license schedule attached to MSA per `/02_CONTRACTS/03_operator_kit_msa.md`

### 5.5 Dedicated BTS Content Day (audit recommendation · NEW)

Currently not in the architecture. The content/marketing audit flagged this as missing. One day per quarter (or per month in Phase B+):

| Block | Action | Output |
|---|---|---|
| Hour 1 | Studio set up · 1 backdrop, 1 lighting pattern | n/a |
| Hour 1.5 | Self-portrait setup OR collaborator (Hermine, Pearl, repeat model paid hourly) | n/a |
| Hour 2-4 | Shoot multiple "operator-on-set" frames + capture talking-head footage (3-5 short clips · Bryce explaining one protocol each) | Raw footage in `/70_BTS/` |
| Same evening | CapCut: 3 Reels (one per protocol explained), each 30-60 sec | 3 Reels in `/80_CONTENT/` |
| Same evening | Caption drafts via Claude using hook library (Section 3.7) | `/80_CONTENT/CAPTIONS.md` |
| Next day | Schedule: 1 Reel/week for next 3 weeks | Scheduled in Buffer |

**Total: ~6 hours, produces ~3 weeks of native short-form content.** This is the highest-ROI content day in the calendar.

### 5.6 VIB Campaign Week (production sprint · existing SOP)

Per `/03_OUTREACH/SOP_VIB_production.md` + lean override (6 VIBs/week).

| Day | Action | Time |
|---|---|---|
| Mon eve (Protected Hour) | Identify 6 LA founders + diagnose protocols + assemble VIB Figma boards | 90 min |
| Tue AM | Send 2 VIBs (LinkedIn DM + image) | 15 min |
| Wed AM | Send 2 VIBs | 15 min |
| Thu AM | Send 2 VIBs | 15 min |
| Fri eve | Pipeline review · log replies in Notion · queue Discovery calls | 30 min |
| Sat | (no VIB work · either Reset shoot or content day) | n/a |
| Sun | (no VIB work · recovery / personal) | n/a |

**Total VIB-week time: ~3 hr/week.** This stacks with shoot days + content days within the 10-12 hr/week budget.

---

## 6. Delegation-ready specifications

Each future hire spec includes: when to hire, what they touch, permission level, quality control, indicative cost.

### 6.1 Retoucher (first hire candidate · Mo 6-9)

**Trigger to hire:** edit-hours-per-Reset moving average crosses 5 hours OR 4+ Resets booked in same month.

**Tools required:** Lightroom Classic + Evoto + Photoshop (own subscriptions, BJ does not provision). Adobe license remains BJ's.

**Cloud access:** Dropbox folder (paid Dropbox tier · $12/mo) per shoot:
- Read+write on `/20_CULLED/` and `/30_HEROES/` for the active shoot only
- No access to `/00_BRIEF/` (contains client brief and contract)
- No access to `/SNIPED_OS/` (operating system)
- No access to Notion CRM
- No access to Pixieset
- No access to Stripe / financial

**Tasks:**
- Retouch passes 1-3 on every Hero per `/05_PRODUCTION/SOP_capture_to_delivery.md`
- Apply SNIPED Evoto preset stack
- Output `.tif` master to `/30_HEROES/` shared folder
- Slack/Notion message: "Heroes pass 3 complete on [Shoot ID]"

**BJ retains:**
- Pass 4 (final aesthetic call)
- Hero count selection
- Final `.jpg` export
- Pixieset upload
- Delivery email

**Quality control:** BJ reviews every Hero before Pixieset upload. Reject criteria: skin retouch over-smoothed (loss of texture), backdrop AI artifacting, color shift from base preset. Three rejected Heroes in one shoot triggers retoucher conversation.

**Indicative cost:** $40-80/Hero or $30-50/hour. Budget for 10-12 Heroes/Reset = $400-960/Reset retoucher cost. Reset margin remains $500-1000 after retoucher fee.

### 6.2 Content / Reel editor (Mo 9-12)

**Trigger:** ≥4 Reels/week target sustained for 1 month → bottleneck on BJ time.

**Tools required:** CapCut Pro / Premiere Pro / Veed.io. Editor's own subscriptions.

**Cloud access:**
- Read+write on `/70_BTS/` and `/30_HEROES/` for shoot folders BJ assigns
- Read+write on `/80_CONTENT/` for output
- No CRM access, no Pixieset, no client emails

**Tasks:**
- BTS Reel cuts per format spec (`/07_CONTENT/sniped_video_philosophy.md` Format 1)
- Talking-head Reel cuts (from BTS Content Day footage)
- IG Reel cover frame design
- Caption draft (BJ approves)

**BJ retains:**
- Final approval on every Reel before posting
- All voice/tone decisions
- Music selection (use locked rotation)
- Posting itself (until Mo 12+ when SM VA absorbs)

**Quality control:** BJ approves every Reel. Rejection criteria: drift from SNIPED visual register, gimmicky cuts (drum-hit edits, fake film grain, teal-and-orange color), text-overlay clutter. Three rejected Reels = conversation.

**Indicative cost:** $50-100/Reel or $25-40/hour. Budget for 4 Reels/week = $200-400/week. Triggers when content-attributable revenue covers cost (case studies + LinkedIn-driven Resets).

### 6.3 Social media VA (Mo 12+)

**Trigger:** $5K/month sustained for 2 consecutive months + BJ at content-bottleneck on scheduling/engagement layer.

**Tools required:** Buffer Pro or Later, LinkedIn drafting access (not posting), Notion view-only for Pipeline, IG Stories drafting access.

**Cloud access:**
- Read on `/80_CONTENT/` (ready-to-post content)
- Read on `/SNIPED_CONTENT_LIBRARY/` (templates + recyclable content)
- Buffer / Later admin access
- LinkedIn drafting access (BJ retains posting auth)
- No Notion write access on Pipeline
- No client communication
- No pricing conversations ever
- Read-only on testimonials and case studies for repurposing

**Tasks:**
- Schedule pre-approved content per BJ calendar
- Monitor IG inbox + LinkedIn inbox · escalate to BJ within 4 hr for any DM
- Repost / recycle older content per Section 3.9
- Comment-engagement layer on LA founder posts (BJ-defined target list, BJ-approved comment library only)
- Monthly metrics report (followers, engagement, reach, CTR)

**BJ retains:**
- Cold DM sending (always · trust signal)
- All client conversations
- Pricing conversations
- New content authorship
- Comment-library approval (no AI-generic comments)

**Quality control:** every BJ-impersonated comment must come from a pre-approved library OR get BJ approval. AI-generic comments = fired.

**Indicative cost:** $20-30/hr or $1500-2500/mo for ~15-20 hr/week.

### 6.4 General VA (Mo 12+)

**Trigger:** BJ at admin/calendar/research-bottleneck for 2 consecutive weeks despite running the system.

**Tools required:** Notion, Google Workspace, Calendly admin, HelloSign, basic email.

**Cloud access:**
- Notion full read on Pipeline / Clients / Outreach / Shoots / Galleries
- Notion write on Outreach (logging) and Calendar (scheduling)
- Calendly admin (event setup, not approval)
- HelloSign (sending pre-approved templates)
- Email triage (read inbox, flag urgent for BJ)
- No financial systems
- No content systems

**Tasks:**
- LA founder list research per BJ-defined criteria
- Calendar management (engineering blocks, SNIPED blocks, recovery)
- Pre-shoot logistics (location confirms, parking, weather)
- Contract dispatch (HelloSign template send, BJ signs)
- Invoice followup on overdue
- Quarterly TAM refresh research (segmenting list)

**BJ retains:**
- Decision on whether a researched founder is worth a VIB
- Strategic call on prospects
- Discovery calls
- Pricing
- Deal decisions

**Indicative cost:** $15-25/hr · ~10 hr/week · $600-1000/month.

### 6.5 Bookkeeper (Mo 9+ OR first $5K month, whichever first)

**Tools:** QuickBooks Self-Employed or Wave (~$15/mo), read-only on Stripe + bank.

**Tasks:** monthly P&L, expense categorization, quarterly tax estimates, year-end docs for CPA. Communicates monthly via Notion entry.

**BJ retains:** banking decisions, pricing, financial strategy.

**Indicative cost:** $50-150/month for a solo-photographer-grade workload.

### 6.6 Permission matrix (one-page reference)

| Asset | BJ | Retoucher | Content Editor | SM VA | General VA | Bookkeeper |
|---|---|---|---|---|---|---|
| `/SNIPED_OS/` | RW | n/a | n/a | n/a | R (specific docs) | n/a |
| `/SNIPED_PRODUCTION/{shoot}/00_BRIEF/` | RW | n/a | n/a | n/a | R (logistics only) | n/a |
| `/SNIPED_PRODUCTION/{shoot}/10_RAW/` | RW | n/a | n/a | n/a | n/a | n/a |
| `/SNIPED_PRODUCTION/{shoot}/20_CULLED/` | RW | RW | n/a | n/a | n/a | n/a |
| `/SNIPED_PRODUCTION/{shoot}/30_HEROES/` | RW | RW | R | n/a | n/a | n/a |
| `/SNIPED_PRODUCTION/{shoot}/40_SELECTS/` | RW | n/a | n/a | n/a | n/a | n/a |
| `/SNIPED_PRODUCTION/{shoot}/50_PROOFS/` | RW | n/a | n/a | n/a | n/a | n/a |
| `/SNIPED_PRODUCTION/{shoot}/60_DELIVERY/` | RW | n/a | n/a | n/a | n/a | n/a |
| `/SNIPED_PRODUCTION/{shoot}/70_BTS/` | RW | n/a | RW | R | n/a | n/a |
| `/SNIPED_PRODUCTION/{shoot}/80_CONTENT/` | RW | n/a | RW | R | n/a | n/a |
| Notion Pipeline | RW | n/a | n/a | R | RW (status only) | n/a |
| Notion Clients | RW | n/a | n/a | n/a | RW | n/a |
| Notion Shoots | RW | n/a | n/a | n/a | RW | n/a |
| Notion Outreach | RW | n/a | n/a | n/a | RW | n/a |
| Notion Galleries | RW | n/a | n/a | R | RW | n/a |
| Pixieset | RW | n/a | n/a | n/a | n/a | n/a |
| Stripe | RW | n/a | n/a | n/a | n/a | R |
| HelloSign | RW | n/a | n/a | n/a | RW (send only) | n/a |
| Calendly | RW | n/a | n/a | n/a | RW | n/a |
| LinkedIn (BJ) | RW | n/a | n/a | RW (draft) | n/a | n/a |
| Instagram (SNIPED) | RW | n/a | n/a | RW | n/a | n/a |
| Email (BJ) | RW | n/a | n/a | n/a | R (triage) | n/a |
| Bank account | RW | n/a | n/a | n/a | n/a | R |
| QuickBooks | R | n/a | n/a | n/a | n/a | RW |

**Legend:** RW = read+write · R = read only · n/a = no access.

---

## 7. Templates + automations

### 7.1 Templates to build NOW (Week 1-2)

**Email templates** (one per file in `/06_DELIVERY/email_templates/`):
- `01_pre_shoot_brief.md`
- `02_day0_delivery.md`
- `03_day1_upsell.md`
- `04_day2_upsell_final.md`
- `05_day7_testimonial.md`
- `06_day19_window_closing.md`
- `07_day30_opkit_pitch.md`
- `08_day90_reengagement.md`
- `09_referral_ask.md`

**Caption templates** (one file at `/07_CONTENT/caption_templates.md`):
- LinkedIn POV scaffold (4 variants per Series A/B/C/D)
- IG Carousel scaffold
- IG Reel description scaffold
- IG Stories caption shortlist
- BTS Reel caption template

**Visual templates** (Figma):
- IG Carousel 8-frame template (1080×1350 portrait)
- LinkedIn POV image template (1080×1350)
- Reel cover frame template (1080×1920)
- Carrd block templates (Hero, Problem, Reset, CTA)

**Workflow templates:**
- Pre-shoot day-of checklist (printable PDF in `/05_PRODUCTION/`)
- Post-shoot same-day checklist (PDF)
- Weekly review template (Notion DB template)
- Monthly Constraint Audit template (Notion)

**Time to build all of the above: one Saturday, ~6 hours.** Pays back forever.

### 7.2 Templates to build Mo 2-3

- Op Kit MSA pre-filled variants (3 use cases)
- Brand System scoping doc template (Phase B+)
- Sprint package one-pager (warm-referral marketing collateral)
- Cultural Documentation institution outreach email template
- Press / publication submission template

### 7.3 Automations Phase 1 (manual everything · current)

The architecture intentionally runs manual for first 30-60 days. Reasoning: feel the friction before automating. Per `/00_BRIEF/SNIPED_OS_OPERATING_BRIEF.md` v1.1 C6.

**No automations active.** Manual:
- Pre-shoot brief send (paste from template)
- Pixieset upload (manual)
- Day-0/1/2/7/30 emails (calendar reminders + manual send)
- Notion card moves (manual)
- Stripe invoice creation (manual from template)

### 7.4 Automations Phase B (Mo 4-6 · trigger: $3K/mo × 2 + 5 Resets delivered)

Build only after manual flow has proven friction:

| Automation | Tool | Build time | Saves |
|---|---|---|---|
| Calendly → Stripe deposit invoice | Zapier | 30 min | 10 min/booking |
| Calendly → 24h pre-shoot brief auto-send | Zapier or Calendly native | 45 min | 15 min/booking |
| Pixieset → 14-day window expiry reminder | Pixieset built-in (just enable) | 5 min | 5 min/Reset |
| Stripe payment → Notion Pipeline status auto-move | Zapier | 30 min | 5 min/payment |
| Calendly → Google Calendar block-out | Calendly native | 5 min | continuous |

**Total: ~2 hours of build for ~30 min/Reset saved at scale.**

### 7.5 Automations Phase C (Mo 7-12)

| Automation | Tool | Saves |
|---|---|---|
| Notion weekly metrics dashboard | Notion formulas (no Zapier) | 30 min/week |
| LinkedIn POV scheduling | Buffer or LinkedIn native | 20 min/week |
| IG Reel scheduling | Buffer or Meta Business Suite | 15 min/week |
| Day-7 testimonial trigger (from Pixieset delivery) | Zapier | 10 min/Reset |
| Day-30 Op Kit pitch trigger | Zapier (with manual approval gate) | 10 min/Reset |

### 7.6 Automations Phase D (Year 2+ · do not build before)

- Quarterly TAM refresh script (Python + LinkedIn search APIs · likely manual + VA)
- Cohort analysis on past Reset clients (manual quarterly is fine until 50+ clients)
- Multi-touch DM automation (this becomes spam fast · BJ hands-on indefinitely)

### 7.7 Quality control checkpoints

Every loop has a single checkpoint where work pauses for BJ approval before advancing:

| Loop stage | Checkpoint | Approver | Failure action |
|---|---|---|---|
| Cull → Heroes | BJ picks 5★ Heroes from cull pool | BJ | Reduce scope or extend SLA |
| Hero retouch (when delegated) | Pass 4 review before Pixieset upload | BJ | Reject + retoucher conversation |
| Pixieset upload | URL test (open in incognito) before sending email | BJ | Fix gallery, then send |
| Reel post (when delegated) | Final view before scheduling | BJ | Reject or re-cut |
| LinkedIn POV send | BJ posts directly | BJ | n/a |
| VIB DM send | BJ sends every cold DM | BJ | n/a |
| Op Kit pitch | BJ writes, sends from BJ inbox | BJ | n/a |
| Pricing conversation | BJ in every conversation | BJ | n/a |

---

## 8. Time-waste prevention map

### 8.1 Top 10 friction points (the things that will eat hours)

| # | Friction | Hours/month wasted | Resolution |
|---|---|---|---|
| 1 | Hunting for files across drives | 3-5 | Folder structure + naming convention (Section 1) |
| 2 | Re-explaining wardrobe to clients | 2-3 | Pre-shoot brief template (Section 7.1) |
| 3 | Drafting emails from scratch | 4-6 | Email template library (Section 7.1) |
| 4 | Manually picking which Hero ships | 2-3 | Cull discipline + Hero count cap (Section 2.2) |
| 5 | Re-creating IG carousel layouts | 2-3 | Figma carousel template (Section 7.1) |
| 6 | Hunting for Reel music | 1-2 | Locked rotation of 5-7 tracks (Section 3.2) |
| 7 | Forgetting Day-7 / Day-30 follow-ups | 4-6 | Calendar reminders Phase 1 → Zapier Phase C (Section 7.5) |
| 8 | Re-writing captions from scratch | 3-5 | Caption framework + Claude assist (Section 3.6) |
| 9 | Lightroom slowness | 2-4 | SSD working drive + smart previews (Section 1.4) |
| 10 | Choosing what to post when | 2-3 | Calendar template + Buffer (Section 3.8) |

**Total potential savings: 25-40 hours/month** by closing all 10. That is ~3-4x the SNIPED weekly hour budget. Most of these resolutions are one Saturday's build.

### 8.2 The Saturday Build (one focused session, ~6 hours)

Single block to close 8 of 10 friction points:

| Hour | Task |
|---|---|
| 1 | Folder structure + naming convention installed on SSD + Warm HDD |
| 2 | Email template library (9 templates per Section 7.1) |
| 3 | Caption framework + LinkedIn POV scaffolds (Series A/B/C/D variants) |
| 4 | Figma templates: IG Carousel + LinkedIn POV + Reel cover |
| 5 | Lightroom presets stack (base, Selects, Proofs) + Evoto SNIPED preset |
| 6 | Notion DB templates · Weekly Review + Monthly Audit |

**Output of one Saturday: the entire production system runs frictionless from this point forward.** Schedule this Saturday before VIB #1 ships if possible. If not, schedule the Saturday after the first Reset closes.

---

## 9. Quick-reference index

When you need... | Open this section
---|---
A new shoot folder created correctly | Section 1.1 + 1.3
Backup discipline reminder | Section 1.5
Hero edit time benchmark | Section 2.3
Export specs | Section 2.6
One shoot → 8 outputs workflow | Section 3 (entire)
Caption scaffold | Section 3.6 + 3.7
What AI tool for what task | Section 4
Reset client day-by-day | Section 5.1
BTS Content Day playbook | Section 5.5
Hiring a retoucher | Section 6.1
Permission matrix | Section 6.6
What to template this Saturday | Section 7.1 + 8.2
What to automate when | Section 7.3 → 7.6
What's eating my hours | Section 8.1

---

**This OS is built for a 10-12 hr/week operator running a creative production company in pockets across an engineer's schedule. It runs the same whether BJ is on a Toronto data center floor or in DTLA. Every workflow is designed to fit a 2-hour evening block, a 4-hour Saturday block, or a 15-minute lunch break.**

The architecture is locked. The execution mechanics are now also locked. From here forward: run the OS. Refine specific procedures inside `/05_PRODUCTION/`, `/06_DELIVERY/`, `/03_OUTREACH/` as friction surfaces.
