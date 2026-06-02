# SNIPED_OS · Final System Status

Date locked: 2026-05-07.
Phase: end of intake / build. Start of execution.
This document is the operating instruction set. Read once, reference forever. Do not expand.

The mode shift has occurred:
- Intake → execution
- Planning → shipping
- Research → revenue
- Architecture → daily reps

If a question can be answered by re-reading something already in `/SNIPED_OS/`, do not generate new strategy. Operate.

---

## 1 · FINAL SYSTEM STATUS

### Fully built (do not rebuild)

**Strategic spine**
- CANONICAL_TRUTHS · 12 truths, locked
- PRODUCTION_OS · folder structure, naming, storage tiering, photo + content pipelines, AI routing, scenario flows
- OPERATIONAL_BACKBONE · what BJ owns forever, what gets delegated, hire triggers
- MONDAY_COCKPIT, SATURDAY_BUILD_BRIEF, EXECUTION_PRIORITIZATION, LEAN_EXECUTION_AUDIT, REVERSE_ROADMAP, recurring_checklists, PARTNERSHIP_PROTOCOL

**Offer + delivery**
- delivery_architecture_v2 · Reset / Sprint / Op Kit / Brand System ladder, prices, scope
- SOP_capture_to_delivery v3 · 5-pass cull with assisted culling + color labels
- SOP_reset_shoot_day, SOP_strategic_free, checklist_pre_shoot_day_of, checklist_post_shoot_same_day
- pixieset_config, SOP_post_delivery
- 9 email templates in `/06_DELIVERY/email_templates/`

**Lightroom operating system**
- lightroom_operating_system.md · catalog, import, color labels, smart collections, mask stack, retouch decision tree, exports
- preset_library.md · 5 develop / 1 metadata / 1 import / 9 export presets defined (build pending)
- retoucher_training_notes.md · Phase B onboarding pack ready

**Outreach**
- SOP_VIB_production · VIB method, cluster targeting, 5-DM sequence
- VIB_caption_library

**Content**
- caption_templates, hook_library, linkedin_pov_bank, sniped_video_philosophy

**Reference layer**
- STRATEGIC_PRINCIPLES · 15-book strategic corpus
- MARKET_INTELLIGENCE
- PHOTOGRAPHY_VAULT_INDEX + 26-file lighting/posing/vision vault in `/10_REFERENCE/lighting_pdfs/`
- UDEMY_AI_TACTICAL_EXTRACTION (7 USE NOW workflow accelerants)
- UDEMY_LIGHTROOM_EXTRACTION (16 USE NOW Lightroom rails)

**Memory layer (22 files indexed in MEMORY.md)**
- 4 base · user role, project, spine, operating constraints
- 18 intel · AI sentiment, positioning, trust mechanics, strategic implications, Trust Equation, Hit Makers, status psychology, WWP proclamations, pricing logic, Perennial Seller, hospitality, leverage, new luxury, Company of One, Berger photo theory, blockbuster strategy, analog premium

### Partially built · usable as-is, mature later under trigger

| Item | Status | Trigger to mature |
|---|---|---|
| Carrd one-pager | Designed in `/14_WEB/` | Activate live + SEO meta pass when ready to drive traffic |
| Notion CRM schemas | Defined in `/04_CRM/` | Set up actual Notion workspace this week (Phase 1 active) |
| Direction Stack book | Outline in `/08_BOOK/` | Q2 2026 active drafting, Q3 2026 launch |
| Art Series references | 5 photographer studies in `/09_ART_SERIES/` | Used at-need for visual direction · do not expand |
| 10-year reverse roadmap | Defined | Quarterly check, not weekly |

### Needs manual install / configure (this week)

1. Build 16 Lightroom presets per `/05_PRODUCTION/preset_library.md` (~90 min)
2. Create master catalog `SNIPED_2026.lrcat` at `/SNIPED_PRODUCTION/_catalogs/`
3. Build 12 Smart Collections per `/05_PRODUCTION/lightroom_operating_system.md` Section 3.4 (~20 min)
4. Set up Notion CRM workspace per `/04_CRM/notion_crm_schemas.md`
5. Configure Pixieset gallery template per `/06_DELIVERY/pixieset_config.md`
6. Backblaze B2 (or rclone-to-Google-Drive) for `/30_HEROES/` + `/50_PROOFS/` + `/80_CONTENT/` cloud backup
7. iCloud Drive sync of `/SNIPED_OS/` folder (so PDFs reach iPad)
8. Add `sniped_backup` rsync function to `~/.zshrc`
9. Restore-drill calendar reminder every 90 days

---

## 2 · ACTIVE TOOL STACK

### Active now (Phase 1)

| Tool | Role | Daily / per-shoot |
|---|---|---|
| Claude Code | Strategic copilot, tactical extraction, memory layer | Daily |
| Lightroom Classic | Cull, develop, mask, decision tree, export | Per shoot |
| Evoto | Skin work post-Lightroom | Per shoot |
| Photoshop | Heavy retouch on Red-label frames only | Rare |
| Topaz Photo AI | Final sharpen on .jpg export | Per shoot |
| Adobe Firefly | Background fill / remove people / atmosphere · utility only | As needed |
| Leonardo AI | Pre-shoot moodboards · internal only | Pre-shoot |
| Pixieset | Client delivery galleries | Per shoot |
| Notion | CRM, Shoots DB, Pipeline, Galleries DB | Daily |
| Carrd | One-pager web presence | Live |
| ChatGPT | Tactical workflows: lead-magnet reverse interview, email batch, persona Q&A, content calendar | As needed |
| Gemini | SEO keyword research only | Monthly |
| iPhone | BTS capture, IG Stories, on-set assistant | Per shoot |
| Google Drive | Cloud backup tier | Auto |
| iCloud Drive | OS file sync to iPad | Auto |
| Camera + lighting kit | Capture | Per shoot |
| DTLA studio | Production anchor | Per shoot |

### Delayed (do NOT activate before trigger)

| Tool | Trigger |
|---|---|
| Buffer / Later (content scheduling) | Phase B start ($3K MRR sustained 2 months) |
| ChatGPT Team Workspace | Retoucher hire (Mo 6-9) |
| ChatGPT Vision batch image review | Cultural Doc shoot >150 frames |
| Lightroom Print Module | Direction Stack book launch (Q3 2026) or edition print pilot |
| Lens Blur effect | Brand System tier only · never Reset |
| Substack | Q2-Q3 2026 (book launch lead-up) |
| Map Module | Cultural Doc hits 10+ LA locations |
| ChatGPT Custom Instructions deep config | Phase B start |
| AI auto-headshots, AI logo, generic AI image gen | NEVER (anti-AI moat absolute) |

---

## 3 · BACKUP + RESILIENCE PLAN

### What lives on the computer + must be backed up

| Asset | Location | Backup tier |
|---|---|---|
| `/SNIPED_OS/` (this OS) | Disk | iCloud Drive (auto) + Google Drive monthly mirror |
| Memory layer | `~/.claude/projects/-Users-sniper/memory/` | iCloud Drive (auto via ~/Library or symlink) + manual git on critical updates |
| `/SNIPED_PRODUCTION/` shoot assets | Hot SSD | Hot SSD + Warm HDD + Cold HDD + Backblaze B2 (Heroes/Selects/Proofs only · RAW stays Hot+Warm only) |
| Lightroom catalog `SNIPED_2026.lrcat` | `/SNIPED_PRODUCTION/_catalogs/` | Lightroom auto-backup folder (last 30 days) + iCloud Drive |
| Lightroom preset `.xmp` exports | `/05_PRODUCTION/_preset_backups/` | iCloud Drive |
| Pixieset client galleries | Pixieset cloud | 14-day expiry · download bundle archived to `/60_DELIVERY/` per shoot before expiry |
| Notion data | Notion cloud | Monthly Notion export to `/04_CRM/_exports/` |
| Carrd page | Carrd cloud | Markdown copy of live copy in `/14_WEB/carrd_one_pager.md` |
| BTS phone footage | Phone | Same-day AirDrop to `/70_BTS/` per shoot |

### The 3-2-1 discipline (modified for cost · per PRODUCTION_OS Section 1.5)

- 3 copies: working SSD + Warm HDD + Cold HDD (Heroes also Cloud)
- 2 media: SSD + spinning disk
- 1 offsite: Cloud (Backblaze B2 or rclone-to-Drive)

Verify monthly. Restore-drill quarterly. The day a backup fails silently is the day you find out.

### Resilience plan: what breaks if Claude Code goes down

**Nothing operational breaks.** The operating system lives on disk, not in Claude.

- Strategic thinking → read `/SNIPED_OS/` files directly. CANONICAL_TRUTHS, PRODUCTION_OS, lightroom_operating_system, OPERATIONAL_BACKBONE, MONDAY_COCKPIT cover 90% of decisions.
- Tactical recall → memory files in `~/.claude/projects/-Users-sniper/memory/` are readable as plain markdown.
- Photo workflow → Lightroom + Evoto + Photoshop are local apps.
- Delivery → Pixieset is web, but galleries already shipped continue working.
- Outreach → VIB SOP is in `/03_OUTREACH/`. Notion CRM holds pipeline.

**What is genuinely Claude-only:** the conversation loop for new strategy, new extraction, new memory writes. None of these are blocking for current operations.

### Offline / manual fallback workflow

- Read `/SNIPED_OS/00_BRIEF/MONDAY_COCKPIT.md` Monday morning. That tells you the week.
- Read `/00_BRIEF/PRODUCTION_OS.md` Section 5 to find the right scenario flow for a shoot.
- Read `/05_PRODUCTION/lightroom_operating_system.md` for any edit decision.
- Read `/03_OUTREACH/SOP_VIB_production.md` for any outreach decision.
- Read `/06_DELIVERY/SOP_post_delivery.md` for any delivery moment.
- Use the 9 email templates in `/06_DELIVERY/email_templates/` directly.
- Notion has offline mode.

The OS reads like a runbook because it is one.

---

## 4 · DAILY EXECUTION LOOP

Total time budget: 1.5 to 2.5 hours per day (lean override · 10-12 hr/week).

| Block | Duration | Action | Tools |
|---|---|---|---|
| Morning · 1 | 5 min | Open MONDAY_COCKPIT (or its weekly equivalent) · confirm today's 1-3 outcomes | Claude Code OR markdown reader |
| Morning · 2 | 15-20 min | VIB outreach: 2-5 messages per `/03_OUTREACH/SOP_VIB_production.md` cadence | Notion + LinkedIn / IG DM |
| Core · edit | 60-90 min | Active shoot edit work · cull, Hero edit, Evoto round-trip, export per `/05_PRODUCTION/lightroom_operating_system.md` | Lightroom + Evoto + (rare) Photoshop |
| Core · content | 15-30 min | One of: write/schedule LinkedIn POV (Tue/Thu), build IG carousel (Wed), draft caption, capture IG Stories during shoot | Phone + Notion or LinkedIn native |
| Close · 1 | 5 min | Update Notion: Shoots DB status, Pipeline status, any new VIB cards | Notion |
| Close · 2 | 2 min | Memory check: anything surprising or load-bearing learned today? Save as memory entry. | Claude Code |

### Daily tool routing (when to reach for what)

| Need | Tool |
|---|---|
| Strategic decision, copy refinement, tactical extraction, memory recall | Claude Code |
| Quick prompt-based output (email batch, content calendar draft, persona Q&A) | ChatGPT |
| SEO keyword research (monthly only · do not over-use) | Gemini |
| Photo edit | Lightroom Classic |
| Skin work | Evoto |
| Heavy retouch / comp | Photoshop (only if decision tree calls) |
| Visual reference / moodboard pre-shoot | Leonardo AI (internal only · never delivered) |
| Background cleanup / atmosphere fill | Adobe Firefly (utility only · never subject) |
| Client gallery delivery | Pixieset |
| Pipeline + CRM + tracking | Notion |
| BTS, IG Stories, on-set notes | iPhone |
| Web presence | Carrd (rarely touched · live state) |

---

## 5 · WEEKLY EXECUTION LOOP

| Day | Action |
|---|---|
| Monday | Read MONDAY_COCKPIT. Set the week's 3 outcomes. Daily loop runs. |
| Tuesday | LinkedIn POV post (7-9 AM PT). Daily loop. |
| Wednesday | IG carousel post. Daily loop. Evening: shoot prep if shooting Thu/Fri. |
| Thursday | LinkedIn POV post (7-9 AM PT). Daily loop. Possible shoot day. |
| Friday | Shoot day if booked. Same-day ingest + backup. |
| Saturday | Saturday Build per `/00_BRIEF/SATURDAY_BUILD_BRIEF.md`. 2-3 hours infrastructure / templates / batch work. NOT new strategy. |
| Sunday | VIB outreach prep · 5-10 messages drafted for the week. Cull + edit batches if shoots from prior week. Quiet day default. |

### Weekly cadence non-negotiables

- 2 LinkedIn POV posts (Tue + Thu)
- 1 IG carousel
- 5-10 VIB outreach messages
- 1 active shoot OR 1 follow-up call OR 1 case study published
- 1 Notion pipeline update
- 1 backup verify (rsync test or restore drill if quarterly tick)

If a week ends without these, the week did not happen.

---

## 6 · PHASE 1 NON-NEGOTIABLES

The minimum viable system. If you do nothing else, do these.

1. **Active Lightroom catalog with locked presets + smart collections.** No edit work happens outside this catalog.
2. **Pixieset delivery within SLA.** Reset = 5 days. Op Kit = 10 days. Strategic Free = 7 days. Never silently late.
3. **Same-day ingest + dual backup.** SD card → SSD → HDD before laptop closes.
4. **VIB outreach cadence.** 5-10 messages per week. The pipeline only fills if you fill it.
5. **2 LinkedIn POV posts per week.** Tuesday and Thursday. The reputation engine runs on cadence.
6. **Notion pipeline updated.** Every shoot logged, every gallery linked, every status moved.
7. **Memory layer maintained.** Surprising learnings get saved. Stale entries get pruned.
8. **Refusal of off-positioning work.** No commodity logos, no AI-generated subjects, no Fiverr-tier deliverables, no scaled-output content. The moat is refused, not earned back.
9. **DTLA studio anchor.** Real space, real shoots, real methodology. The analog premium runs through the studio.
10. **Anti-AI on client work.** Berger / Sax line absolute. AI is utility behind the methodology, never the methodology itself.

---

## 7 · ARCHIVE / DO NOT TOUCH (next 30 days)

These are the temptations to refuse. Flagging them explicitly so they stop calling.

### Stop reading

- The 15 strategic books in `/Users/sniper/Downloads/` (Block, Reedsy, Predictable Revenue, etc.). Memory has the principles. The books are noise now.
- The Photography Masterclass docx (`/10_REFERENCE/lighting_pdfs/`). Slow-burn vision training, 30 min between shoots, NOT a binge target.
- The Udemy AI course gold docx. The 7 USE NOW items are extracted. The rest is hype.
- The Udemy Lightroom course docx. The 16 USE NOW items are locked. The rest is beginner.
- New books, new courses, new YouTube tutorials. Refuse the intake reflex.

### Stop reorganizing

- `/SNIPED_OS/` folder structure. Locked.
- File naming conventions. Locked.
- Memory file organization. Locked.
- The 12 Smart Collections (build them once, do not iterate the rules for at least 90 days).
- The 5 develop presets (build v1, do not tune until quarterly review).

### Stop building

- New SOPs (already exist for every flow that matters)
- New email templates (9 covers Phase 1)
- New caption templates (existing library handles current cadence)
- New memory files (only if surprising and load-bearing · most input is not)
- New Lightroom presets beyond the locked set
- New strategic principles documents

### Stop deferring real work

- The 36 finals from last weekend's 6 shoots. Edit them. Ship them. This week.
- VIB outreach (the pipeline is empty until you fill it)
- Carrd activation (it is built · push it live or move on)
- Notion CRM setup (defined · stand it up this week)

### Hard NO list (next 30 days)

| Temptation | Why refuse |
|---|---|
| Direction Stack book drafting | Q3 2026 launch. Not Q2 yet. Pre-build distribution first. |
| Substack setup | Q2-Q3 2026 trigger. Not now. |
| Retoucher hire research | Mo 6-9 trigger. Pipeline must fill first. |
| Edition print pilot | Phase B+. Not Phase 1. |
| New camera body / new lens / new modifier | Capture is not the bottleneck. Editing is. |
| TikTok / Threads / new platform | Distribution focus is LinkedIn + IG. Adding platforms diffuses. |
| Reading another book | The principles are encoded. Apply them. |
| Building yet another spreadsheet / dashboard | Notion CRM is the system. |
| Re-extracting from a course | Two extractions ship. The rest is wasted. |
| Researching "what other photographers do" | The methodology is the moat. Outside is noise. |

---

## 8 · NEXT 10 ACTIONS IN ORDER

Strict order. Do not skip steps. Do not parallelize unless explicitly noted.

### 1. Build the Lightroom presets (90 min · today or tomorrow)
Open Lightroom Classic. Build 5 develop presets, 1 metadata preset, 1 import preset, 9 export presets per `/05_PRODUCTION/preset_library.md`. Export each as `.xmp` to `/05_PRODUCTION/_preset_backups/`.

### 2. Create master catalog (15 min · same session)
`SNIPED_2026.lrcat` at `/SNIPED_PRODUCTION/_catalogs/`. Set as default. Configure auto-backup to `/SNIPED_PRODUCTION/_catalogs/_backups/`.

### 3. Build 12 Smart Collections (20 min · same session)
Per `/05_PRODUCTION/lightroom_operating_system.md` Section 3.4. Inside Collection Set named `SNIPED · SMART`.

### 4. Run last weekend's 6 shoots through the new pipeline (3-5 hours across this week)
Floor (Track A) for all 36 finals · Reset standard delivery. Do not start Track B creative push until Track A is shipped.

### 5. Deliver to all 6 models (per shoot SLA · this week)
Pixieset gallery per `/06_DELIVERY/SOP_post_delivery.md`. Send delivery email at 9 AM PT.

### 6. Stand up Notion CRM (1 hour · this week)
Per `/04_CRM/notion_crm_schemas.md`. Migrate existing pipeline state into it. From this point, every shoot/lead/follow-up lives in Notion.

### 7. Send 5-10 VIB outreach messages (1-2 hours · this week)
Per `/03_OUTREACH/SOP_VIB_production.md`. LA founder cluster. Use VIB caption library. Track in Notion.

### 8. Pick 6-12 Track B creative push frames from last weekend (2-4 hours · next week)
Compositing, atmosphere, location/sky swap. Maker-led. No AI subjects. Output: portfolio update + LinkedIn POV case study material.

### 9. Publish 1 LinkedIn POV case study (Tue or Thu · next week)
From the Track B creative push frames. Caption per `/07_CONTENT/linkedin_pov_bank.md`. The post teaches, does not sell.

### 10. Verify backup chain end-to-end (30 min · this week)
Run `sniped_backup` rsync. Open one random older shoot from Cold HDD and verify integrity. Confirm Backblaze B2 (or rclone-to-Drive) running on `/30_HEROES/` + `/50_PROOFS/` + `/80_CONTENT/`. Set 90-day calendar reminder for next restore drill.

After action 10, the system is live. Phase 1 cadence runs. Re-audit at $3K MRR sustained 2 months · that is the Phase B trigger and the next legitimate review point.

---

## 9 · The single integrated rule

**Stop building the system. Start running it.** Every artifact required to ship Phase 1 is already in `/SNIPED_OS/`. The 22 memory files cover strategic recall. The 16 Lightroom rails cover edit discipline. The VIB SOP covers outreach. The Pixieset config covers delivery. The Notion CRM covers tracking. Everything else is fake work disguised as preparation. Refuse it.

The next 90 days are reps. Edit. Deliver. Outreach. Post. Track. Repeat. The compounding starts the day you stop adding to the system and start running through it.
