# Notion CRM · 5-database schema

**One-page setup target. Build in 60-90 minutes, then run cards manually for the first 30 days. No automation until manual flow shows friction.**

Every database below has the same minimum view convention: `All` (table) · `Active` (filter excludes archived/lost) · `Mine This Week` (filter on Next Action Date this week).

---

## DB 1 · Pipeline (the kanban)

**Purpose:** every prospect, lead, and deal in one board. Kanban view is primary.

**Properties:**

| Field | Type | Options / Notes |
|---|---|---|
| Name | Title | Format: `[First Last] · [Company]` (e.g. `Marcus Chen · Strata Health`) |
| Status | Select | `Target` `Engaged` `Discovery Booked` `Proposal Sent` `Reset Booked` `Reset Delivered` `Op Kit Pitched` `Op Kit Booked` `Op Kit Delivered` `Brand System Pitched` `Brand System Booked` `Closed Lost` `Re-engage 90d` |
| Tier | Select | `Reset` `Op Kit` `Brand System` `Free Collab` `Free Community` `Free Access` |
| Trigger | Multi-select | `LinkedIn post` `Job change` `Funding` `New role <60d` `Founded <2yr` `Hiring signal` `Industry news` `Referral` `Event coverage` `Inbound DM` `Inbound site` |
| VIB sent | Date | Date the VIB went out |
| Next action | Text | Single sentence verb-first action |
| Next action date | Date | Drives the `Mine This Week` view |
| Last touch | Date | Auto-updated when a card moves status (manual for now) |
| Source channel | Select | `LinkedIn DM` `LinkedIn comment` `IG DM` `IG profile` `Site form` `Referral` `In-person` `Email` |
| Lane | Multi-select | `LinkedIn cold` `LinkedIn warm referral` `Lane 1 Promoter` `Lane 2 Community` `Lane 3 Sports` `Lane 4 Local Biz` `Inbound site` `IG inbound` · per `/13_NETWORK/access_and_community_architecture.md` (v1.1) |
| Source person | Relation → Clients | If this card came from another client's referral; drives `Referrals out` rollup on Clients DB |
| Estimated value | Number (USD) | Reset = 1500, Op Kit = 4000 (early), Brand System = 12500. Used for forecast totals. |
| Probability | Select | `Cold (10%)` `Warm (25%)` `Discovery booked (40%)` `Proposal out (60%)` `Booked (95%)` `Delivered (100%)` |
| Forecast value | Formula | `prop("Estimated value") * (parseInt(replaceAll(prop("Probability"), "[^0-9]", "")) / 100)` |
| Days since last touch | Formula | `dateBetween(now(), prop("Last touch"), "days")` |
| Client (relation) | Relation → Clients | Many-to-one |
| Outreach (relation) | Relation → Outreach | One-to-many |
| Notes | Text | Anything qualitative |

**Views:**
1. `Board by Status` (kanban grouped by Status, sorted by Next action date)
2. `Mine This Week` (table, filter: `Next action date` is this week, sort: ascending)
3. `Forecast` (table, filter: Status not in `Closed Lost`/`Re-engage 90d`, group by Tier, sum Forecast value)
4. `Stale` (table, filter: `Days since last touch` > 14 AND Status not in `Closed Lost`/`Re-engage 90d`)
5. `Re-engage 90d` (table, filter: Status = `Re-engage 90d` AND `Days since last touch` > 90)
6. `By Lane · Forecast` (table, group by Lane, sum Forecast value) · quarterly review insight: which engine is producing pipeline

---

## DB 2 · Clients

**Purpose:** the human/business record. Survives across multiple pipelines (e.g. Tracy at Davis Law re-engages 90d → next pipeline card links here).

| Field | Type | Notes |
|---|---|---|
| Name | Title | First Last |
| Company | Text | |
| Role | Text | |
| LinkedIn URL | URL | |
| Email | Email | |
| Phone | Phone | Optional |
| Address | Text | Optional, for shipping prints / banquets / on-location |
| Referral source | Relation → Clients | If they came from another client |
| Referrals out | Rollup | Count of clients with this person as referral source |
| Lifetime value (LTV) | Rollup | Sum of `Cash collected` from related Pipeline cards |
| First touch date | Date | |
| Tags | Multi-select | `Founder` `Operator` `Attorney` `Pastor` `Coach` `Promoter` `Artist` `Athlete` `Brand` `Family/Personal` `Repeat client` |
| Pipelines (relation) | Relation → Pipeline | One-to-many |
| Shoots (relation) | Relation → Shoots | One-to-many |
| Galleries (relation) | Relation → Galleries | One-to-many |
| Notes | Text | |

**Views:**
1. `All Clients` (table, sort: First touch date desc)
2. `Top LTV` (table, sort: LTV desc, top 20)
3. `Repeat clients` (filter: Tags contains `Repeat client`)
4. `Referral sources` (filter: Referrals out > 0, sort desc)

---

## DB 3 · Shoots

**Purpose:** every time the camera comes out. Includes paid, free, and personal/Art Series.

| Field | Type | Options / Notes |
|---|---|---|
| Shoot ID | Title | `YYYY-MM-DD · [Client/Series] · [Type]` (e.g. `2026-07-15 · Emmanuel 33rd Sunday · Free Community`) |
| Date | Date | |
| Type | Select | `Reset` `Op Kit` `Brand System` `Free Collab` `Free Community` `Free Access` `Personal` `Art Series` `Cultural Documentation` |
| Lane | Multi-select | Same options as Pipeline.Lane · per `/13_NETWORK/access_and_community_architecture.md` |
| Status | Select | `Scheduled` `Captured` `Editing` `Delivered` `Upsold` `Archived` |
| Location | Text | |
| Studio | Select | `Jamie's Vibrant Eye DTLA` `Larry Bernard's` `On-Location` `Peerspace` `Other` |
| Wardrobe brief sent | Checkbox | |
| Call sheet sent | Checkbox | |
| Card backed up | Checkbox | Same-day SD ingest + 2 backups |
| Contracted images | Number | 20 default for Reset |
| Edit hours actual | Number | Track per shoot to spot the bottleneck |
| Delivery target date | Date | `Date + 5 days` for Reset |
| Delivery actual date | Date | |
| SLA met | Formula | `if(empty(prop("Delivery actual date")), "·", if(prop("Delivery actual date") <= prop("Delivery target date"), "✅", "❌"))` |
| Pixieset URL | URL | |
| Upsell images count | Number | |
| Upsell revenue | Number (USD) | |
| Cash collected (total) | Number (USD) | Tier price + upsell |
| Hero image (for archive) | Files | One image, the strongest frame, for the case-study + Art Series cross-reference |
| Client (relation) | Relation → Clients | |
| Pipeline (relation) | Relation → Pipeline | |
| Gallery (relation) | Relation → Galleries | |
| Notes | Text | |

**Views:**
1. `Active SLA` (filter: Status in `Captured`/`Editing`, sort: Delivery target date asc) · daily check
2. `Day-30 Op Kit pitch trigger` (filter: Status = `Delivered` AND `dateBetween(now(), prop("Delivery actual date"), "days")` >= 30 AND Type = `Reset`)
3. `Edit-hours moving avg` (table, last 12 shoots, sort: Date desc)
4. `Free shoot ledger` (filter: Type starts with `Free`)
5. `Art Series progress` (filter: Type = `Art Series`)

---

## DB 4 · Outreach

**Purpose:** every VIB sent. Drives the weekly volume metric and the conversion-rate signal.

| Field | Type | Options / Notes |
|---|---|---|
| VIB ID | Title | `YYYY-MM-DD · [Recipient last name] · [Company]` |
| Recipient | Text | |
| Recipient role | Text | |
| Company | Text | |
| LinkedIn URL | URL | |
| Trigger used | Select | Same options as Pipeline.Trigger |
| Protocol named | Select | `01 Claw Hands` `02 Locked Shoulders` `03 Squared` `04 Pinned Arms` `05 Soft Jawline` `06 Spinal Collapse` `07 Forced Smile` `08 Transition Freeze` `09 No Presence` `10 Full Shutdown` |
| VIB sent date | Date | |
| Loom included | Checkbox | Yes only when trigger event |
| Reply | Select | `No reply` `Read no reply` `Yes · info` `Yes · call` `Declined polite` `Declined hostile` `Removed/blocked` |
| Reply date | Date | |
| Reply latency hours | Formula | `dateBetween(prop("Reply date"), prop("VIB sent date"), "hours")` |
| Discovery call date | Date | |
| Pipeline (relation) | Relation → Pipeline | Linked when reply = `Yes` |
| Notes | Text | |

**Views:**
1. `This week's sends` (filter: VIB sent date is this week)
2. `Pending follow-up` (filter: Reply = `No reply` AND VIB sent date >= 5 days ago AND <= 10 days ago)
3. `Conversion funnel` (table, group by Reply, count) · used in Monday weekly review
4. `By trigger` (table, group by Trigger used, sum count) · quarterly TAM refresh insight
5. `By protocol` (table, group by Protocol named) · see which protocols generate replies

---

## DB 5 · Galleries

**Purpose:** Pixieset gallery state + upsell tracking. Lightweight; most lives in Pixieset itself, this is the index.

| Field | Type | Notes |
|---|---|---|
| Gallery name | Title | Mirrors Pixieset gallery name |
| Pixieset URL | URL | |
| Client (relation) | Relation → Clients | |
| Shoot (relation) | Relation → Shoots | |
| Delivered date | Date | |
| Expiry date | Date | Default: Delivered + 14 days for Reset; upsell window is first 48h |
| Upsell window status | Formula | `if(dateBetween(prop("Expiry date"), now(), "hours") <= 0, "Expired", if(dateBetween(now(), prop("Delivered date"), "hours") <= 48, "🔴 Active 48h", "Closed-window"))` |
| Upsell sequence sent | Multi-select | `Email 1 (delivery)` `Email 2 (24h)` `Email 3 (44h, last call)` |
| Upsell revenue | Number (USD) | |
| Conversion % | Formula | `(prop("Upsell revenue") / 80)` (count of $80 upsell images) |
| Notes | Text | |

**Views:**
1. `Active 48h windows` (filter: Upsell window status = `🔴 Active 48h`) · daily check during active galleries
2. `Closed windows · revenue tally` (filter: Upsell window status = `Expired`, sum Upsell revenue, group by month)
3. `Upsell email queue` (filter: Active 48h AND Email 3 not sent)

---

## Dashboard page (top of CRM)

A single Notion page titled `📊 Operator Dashboard`. Place at the top of the CRM workspace.

**Section 1 · This Week's Numbers**
Linked-database blocks displaying counts/sums from the live data:
- `VIBs sent this week` → Outreach count, filter VIB sent date is this week. **Target: 3+.**
- `Discovery calls held this week` → Pipeline count, filter Status = `Discovery Booked` and Last touch is this week.
- `Cash collected this week` → Shoots sum of Cash collected, filter Date or Delivery actual date is this week.
- `Pixieset upsell windows active` → Galleries filter Upsell window status = `🔴 Active 48h`.

**Section 2 · Active SLAs**
Embedded Shoots view: `Active SLA`. One glance shows what's overdue.

**Section 3 · Day-30 Op Kit pitch triggers**
Embedded Shoots view: `Day-30 Op Kit pitch trigger`. Each card here is an Op Kit pitch waiting to happen.

**Section 4 · Stale pipeline**
Embedded Pipeline view: `Stale` (>14 days no touch). Triage Mondays.

**Section 5 · Edit-hours moving average**
Embedded Shoots view: `Edit-hours moving avg`. Watch this number; if it climbs, the bottleneck is here.

**Section 6 · Forecast**
Embedded Pipeline view: `Forecast`. Sum of Forecast value by Tier. Realistic 90-day revenue surface.

**Section 7 · Re-engage queue**
Embedded Pipeline view: `Re-engage 90d`. Quarterly working list.

---

## Build sequence (60-90 minutes)

1. Create the 5 databases as **inline databases** in one Notion page called `🎯 Sniped CRM`.
2. Add properties as listed above. Don't skip the formula columns; they're load-bearing.
3. Wire the relations (5 minutes).
4. Build the views per database (15 minutes).
5. Create the Dashboard page above the CRM page. Embed views via `/Linked database`.
6. Add 5 dummy cards to Pipeline to test the views render.
7. Delete dummies. Add the actual 10 first-target prospects from the LA founder list in /03_OUTREACH/target_list_seed.md (Phase 2 gap · populate during Week 1).

**What NOT to do:**
- Don't add Zapier/automations yet. Move cards manually for 30 days. Feel the flow first.
- Don't add more properties. Every field above is load-bearing; everything else is friction.
- Don't add tasks/calendar/reminders inside Notion. Calendar lives in Google Calendar (Calendly auto-creates events). Reminders live in the `Next action date` column.
- Don't try to track personal expenses, debt, or tax in here. That goes in /12_FINANCIAL with its own setup.
