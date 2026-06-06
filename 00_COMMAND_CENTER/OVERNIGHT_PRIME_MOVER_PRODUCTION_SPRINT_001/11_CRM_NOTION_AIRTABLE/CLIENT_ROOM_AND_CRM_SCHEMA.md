# SOLE HOUSE · THE OPS LAYER BLUEPRINT
## Client Room (Notion) + CRM Schema (Airtable) · build-ready

Tagline lock: **We do not make you better. We make you the only one.**

This is the back-of-house operating system for a 72-hour Repositioning Sprint. It exists so the work feels already true and already expensive the moment a HOUSE opens its room, and so the operator runs one HOUSE at a time without dropping a thread. Two surfaces:

- **The Client Room (Notion):** the room the buyer walks into. One per engagement. Carries the claim, the world, the schedule, the approvals, and the sealed handoff.
- **The CRM (Airtable):** the operator-only spine. Pipeline, engagements, asset tracker, contacts, proof tracker. The buyer never sees it.

Faceless on both sides. No operator face, no client face, no shoot. All names below are placeholder constructs (HOUSE-0001, etc.). No real client data.

Build rules carried from the brief:
- One HOUSE at a time (capacity gate). A second active engagement cannot enter PRODUCTION while one is live.
- Price published, scope published and closed. One recut only. No revisions inside the 72-hour window.
- No claim, no build. The Sole Claim must clear the positioning gate at Hour 0 before any world renders.
- Every deliverable clears the OS max-readiness gate before handoff.
- Clean disqualify for any buyer needing real faces or regulated human-trust imagery.

---

## PART 1 · THE NOTION CLIENT ROOM

### 1.1 What it is

A single Notion teamspace template, duplicated per engagement and renamed to the HOUSE codename. The room is the premiere venue, not a project folder. It opens dim and sealed, and reveals as the sprint advances. The owner-operator (the buyer) gets share access to the top page; the operator working pages stay private.

Visual register inside the room: Ink black ground (`#0A0A0B`), Bone white text (`#EDE8DD`), SOLE brass accents (`#A8843C`) on the Seal and section dividers only. Didone display register for page titles, quiet grotesque for body. The Singular Seal sits locked-and-embossed at the top of the room cover and strikes to live at handoff.

### 1.2 Page tree (duplicate this exact structure per HOUSE)

```
SOLE HOUSE · [HOUSE CODENAME]            ← room cover. Seal locked. Status pill. Countdown to Hour 72.
│
├── 00 · The Sole Claim                  ← the verdict. One sentence, board-ready. The only bespoke unit.
│     ├── The Claim (the one sentence)
│     ├── Positioning Doctrine (one page)
│     │     ├── Who you are the only one for
│     │     ├── The enemy you reject
│     │     └── The new category name
│     └── Positioning Gate result (PASS / NO BUILD)
│
├── 01 · The World Bible                 ← The Vault Room, configured to this HOUSE.
│     ├── World statement (how the Vault Room reads for this business)
│     ├── Palette lockup (5 hex swatches, fixed)
│     ├── Type system (didone display + grotesque body)
│     ├── Motif kit (top-light plinth, vault-door ring, redaction bar, archive drawer)
│     ├── The 12 to 16 stills (embedded gallery, each watermarked with the Seal)
│     └── The Singular Seal (this HOUSE's lockup)
│
├── 02 · The Deliverables                ← the sealed system. One block per artifact.
│     ├── The Sole Claim + Doctrine (link to 00)
│     ├── Brand World Bible (link to 01)
│     ├── The Manifesto Film (60 to 90s, embed + download)
│     ├── The Category Brief (Repositioning Deck, Seal on cover)
│     ├── The Live Landing (Vercel URL + Figma source)
│     └── The Offer + Booking Layer (premium copy + n8n flow status)
│
├── 03 · The 72-Hour Timeline           ← the schedule, public-facing. Premiere countdown.
│     └── (full schedule below in §1.4)
│
├── 04 · Approvals                       ← the two gates the buyer touches. Nothing else is open.
│     ├── Gate A · The Sole Claim sign-off (Hour 6)
│     ├── Gate B · Pre-render direction sign-off (Hour 24)
│     └── The one recut request (single field, closes at Hour 60)
│
└── 05 · The Handoff                     ← sealed at Hour 72. Timestamped. Change-log. Seal strikes live.
      ├── The timestamped handoff record
      ├── Change-log (every recut and direction note, dated)
      ├── Final deliverable links (all six, gate-cleared)
      ├── Max-readiness gate confirmation
      └── The Seal · struck from locked to live
```

### 1.3 Page-by-page spec

**00 · The Sole Claim.** Opens with the one sentence in didone display, centered on ink black, brass underline. Below it the one-page doctrine in three locked sub-blocks. A callout at the bottom shows the positioning gate result as a hard pill: `PASS` (brass) or `NO BUILD` (redaction-bar grey). If `NO BUILD`, every page below 00 stays collapsed and locked. This enforces "no claim, no build" structurally, not just procedurally.

**01 · The World Bible.** The Vault Room configured, never reinvented. Palette and type are fixed templates, copied not authored. The stills gallery is a Notion gallery view of the asset records (mirrored read-only from Airtable, see §2.4). Each still carries the Seal watermark. A locked callout states: the world does not vary, only the claim and copy do. This is the visible expression of the visual-drift discipline.

**02 · The Deliverables.** Six toggle blocks, one per artifact, each showing: status pill, preview/embed, download link, and gate state. A deliverable block stays collapsed-and-greyed until its asset record clears the max-readiness gate. The buyer watches the system assemble itself in real time, sealed piece by sealed piece.

**03 · The 72-Hour Timeline.** Public-facing schedule (§1.4). Rendered as a Notion timeline/board with a live countdown callout to Hour 72. Frames the work as a premiere with a fixed curtain.

**04 · Approvals.** The only place the buyer acts. Two sign-off gates and one recut request, each a single decisive field. No open-ended comment threads, no revision sprawl. The recut field hard-closes at Hour 60. This is where closed scope becomes felt, not just stated.

**05 · The Handoff.** Sealed at Hour 72. A single timestamped record, a dated change-log, all six final links, the max-readiness confirmation, and the Seal animation strikes from locked to live. After handoff the room becomes read-only archive. This is the single timestamped handoff with change-log from the commercial chassis.

### 1.4 The 72-hour schedule (lives on page 03)

Fixed three-day machine. Times are relative hours from kickoff (Hour 0).

| Block | Hours | What happens | Buyer touchpoint | Internal artifact |
|---|---|---|---|---|
| **Day 0 · Intake + Verdict** | 0 to 6 | Intake closed. Disqualify check (faces / regulated trust). The Sole Claim drafted and run through the positioning gate (7 Powers / Win Without Pitching). | Gate A sign-off at Hour 6 | Claim + Doctrine, gate result |
| **Day 1 · Direction** | 6 to 24 | World Bible configured to the claim. Still direction locked. Film script written, AI voice cast (ElevenLabs). Deck and landing wireframes set. | Gate B sign-off at Hour 24 | Direction lock, script, wireframes |
| **Day 1 to 2 · Production** | 24 to 48 | 12 to 16 Vault Room stills rendered (Higgsfield plates, Blender hero-object). Film assembled, scored, graded (Premiere + After Effects). Capacity gate active: one HOUSE only. | none (heads-down) | Stills, film cut, deck build |
| **Day 2 to 3 · Assembly** | 48 to 60 | Deck finalized with Seal on cover. Landing built in Figma, shipped live on Vercel. Offer copy rewritten, n8n booking flow wired. Recut window open. | one recut request, closes Hour 60 | Live landing, booking flow, deck |
| **Day 3 · Seal + Handoff** | 60 to 72 | All six deliverables through max-readiness gate. Change-log finalized. Sealed handoff record written. Seal strikes locked to live. | Handoff delivered at Hour 72 | Sealed system, change-log |

Sovereign tier adds, after Hour 72: scheduled go-live, embargo email, n8n countdown trigger, the Seal strike timed to the buyer's launch date, and the machined brass Singular Seal shipped to the desk. These are scheduled launch-day ops the operator owns end to end, not a live scramble.

---

## PART 2 · THE AIRTABLE CRM SCHEMA

Base name: **SOLE HOUSE · OPS**. Five tables, linked. Operator-only. Field types use Airtable's literal type names so this builds directly.

Table map and links:
- **Pipeline** (one row per opportunity) links to **Contacts** and converts to **Engagements**.
- **Engagements** (one row per 72-hour sprint) links to **Pipeline**, **Contacts**, **Deliverables**, **Proof**.
- **Deliverables / Asset Tracker** links to **Engagements**.
- **Contacts** links to **Pipeline** and **Engagements**.
- **Proof Tracker** links to **Engagements** and **Deliverables**.

### 2.1 Table: PIPELINE (stages)

One row per opportunity, from first signal to won or lost. This is where the one-HOUSE-at-a-time gate is watched.

| Field | Type | Notes / select options |
|---|---|---|
| Opportunity ID | Formula | `"PIP-" & RECORD_ID()` surrogate, or autonumber-prefixed |
| HOUSE Codename | Single line text | placeholder until won, e.g. HOUSE-0001 |
| Stage | Single select | `Signal`, `Qualifying`, `Disqualified`, `Sole Claim Pitch`, `Proposal Sent`, `Verbal Yes`, `Booked`, `Won`, `Lost` |
| Tier Targeted | Single select | `Sprint $7,500`, `Signature $14,000`, `Sovereign $25,000+` |
| Deal Value | Currency | USD |
| Primary Contact | Link to Contacts | the owner-operator (economic buyer) |
| ICP Type | Single select | `Established Business`, `Funded Founder (launch moment)` |
| Category / Vertical | Single select | `Law Firm`, `Medspa`, `Boutique Builder`, `Financial Advisor`, `Specialty Agency`, `Other` |
| Faces Disqualifier | Single select | `Clear (faceless-safe)`, `Needs Real Faces (DISQUALIFY)`, `Regulated Trust Imagery (DISQUALIFY)`, `Pending Check` |
| Positioning Gate Pre-Read | Single select | `Strong claim available`, `Weak claim`, `No claim found (no build)`, `Not assessed` |
| Sales Wedge Used | Single select | `Price/Time vs Agency`, `Category Education`, `Both`, `Inbound (no wedge)` |
| Incumbent Anchored Against | Single line text | the slow expensive agency named in the pitch |
| Probability | Percent | operator estimate |
| Expected Close | Date | |
| Next Action | Single line text | |
| Next Action Date | Date | |
| Source | Single select | `Referral`, `Inbound Landing`, `Outbound`, `Network`, `Repeat / Expansion` |
| Linked Engagement | Link to Engagements | populated on Won |
| Lost Reason | Single select | `Price`, `Timing`, `Needed Faces`, `No Strong Claim`, `Chose Agency`, `Went Quiet`, `Other` |
| Created | Created time | |
| Last Activity | Last modified time | |

Views to build: `Active Pipeline` (Stage is not Won/Lost/Disqualified), `One-HOUSE Gate` (filter Stage = Booked or Won, grouped to confirm only one is in PRODUCTION), `Disqualified Log`, `By Tier`.

### 2.2 Table: ENGAGEMENTS (the 72-hour sprints)

One row per sold sprint. The operating spine of a live HOUSE. The capacity gate lives in the Sprint Status field.

| Field | Type | Notes / select options |
|---|---|---|
| HOUSE Codename | Single line text | primary field, e.g. HOUSE-0001 |
| Linked Pipeline | Link to Pipeline | source opportunity |
| Primary Contact | Link to Contacts | |
| Tier | Single select | `Sprint $7,500`, `Signature $14,000`, `Sovereign $25,000+` |
| Contract Value | Currency | USD |
| Sprint Status | Single select | `Booked (queued)`, `Intake`, `Claim Locked`, `In Production`, `Assembly`, `Sealed`, `Handed Off`, `On Hold`, `Cancelled` |
| Capacity Gate | Formula | flag if more than one row has Sprint Status of `Intake`/`Claim Locked`/`In Production`/`Assembly` at once |
| Kickoff (Hour 0) | Date with time | |
| Handoff Due (Hour 72) | Formula | `DATEADD({Kickoff (Hour 0)}, 72, 'hours')` |
| Sole Claim | Long text | the one sentence (mirrors Notion 00) |
| Positioning Gate Result | Single select | `PASS`, `NO BUILD`, `Pending` |
| Gate A · Claim Sign-off | Single select | `Awaiting`, `Approved`, `Revise` |
| Gate A Time | Date with time | target Hour 6 |
| Gate B · Direction Sign-off | Single select | `Awaiting`, `Approved`, `Revise` |
| Gate B Time | Date with time | target Hour 24 |
| Recut Used | Checkbox | one recut only; true after the single recut is consumed |
| Recut Window Closed | Checkbox | hard close at Hour 60 |
| Deliverables | Link to Deliverables | the six artifacts |
| Proof Records | Link to Proof | |
| Max-Readiness Gate | Single select | `Not Run`, `Pass`, `Fail (blocked)` |
| Handoff Timestamp | Date with time | the single timestamped handoff |
| Change-Log | Long text | every recut + direction note, dated |
| Seal State | Single select | `Locked (embossed)`, `Struck (live)` |
| Notion Room URL | URL | link to the Client Room |
| Sovereign · Exclusivity Category | Single line text | category held exclusive this quarter (Sovereign only) |
| Sovereign · Launch Date | Date with time | scheduled go-live for drop ops |
| Sovereign · Brass Seal Shipped | Checkbox | machined object shipped to desk |
| Payment Status | Single select | `Unpaid`, `Deposit Paid`, `Paid in Full`, `Refunded` |

Views: `Live HOUSE` (Sprint Status in Intake..Assembly), `Sprint Board` (kanban by Sprint Status), `Queue` (Booked queued), `Sovereign Ops` (Tier = Sovereign), `Handoff Archive`.

### 2.3 Table: DELIVERABLES / ASSET TRACKER

One row per asset inside an engagement. Each of the six deliverables is one or more asset rows. Stills are tracked individually so the 12-to-16 count is enforced and each carries the Seal watermark check.

| Field | Type | Notes / select options |
|---|---|---|
| Asset ID | Formula | `"AST-" & RECORD_ID()` |
| Asset Name | Single line text | e.g. "Vault Still 07 · plinth top-light" |
| Engagement | Link to Engagements | |
| Deliverable Type | Single select | `Sole Claim + Doctrine`, `World Still`, `Manifesto Film`, `Category Brief Deck`, `Live Landing`, `Offer + Booking Flow`, `Seal Asset`, `90-Day World Pack (Signature)`, `Drop Ops Asset (Sovereign)` |
| Production Stack | Single select | `Higgsfield`, `Blender`, `Premiere`, `After Effects`, `ElevenLabs`, `Figma`, `Vercel`, `n8n`, `Mixed` |
| Status | Single select | `Not Started`, `Direction Locked`, `Rendering`, `In Review`, `Recut Pending`, `Max-Readiness Gate`, `Approved`, `Shipped` |
| Seal Watermark | Single select | `Required`, `Applied`, `N/A` |
| Vault Room Compliance | Single select | `On-world`, `Drift flagged (fix)`, `N/A` |
| Recut Flag | Checkbox | true if this asset is the consumed recut |
| Max-Readiness Result | Single select | `Not Run`, `Pass`, `Fail` |
| File Link | URL | render / export location |
| Notion Mirror | Checkbox | true once surfaced read-only in the Client Room |
| Owner Step | Single select | `Operator`, `Awaiting Buyer Sign-off`, `Sealed` |
| Due Hour | Number | relative sprint hour the asset is due (e.g. 48) |
| Notes | Long text | |
| Last Updated | Last modified time | |

Views: `Asset Board` (kanban by Status), `Stills Count` (filter Deliverable Type = World Still, grouped by Engagement to confirm 12 to 16), `Drift Watch` (Vault Room Compliance = Drift flagged), `Gate Queue` (Status = Max-Readiness Gate), `Shippable` (Status = Approved).

### 2.4 Asset tracker spec (how it operates)

- **Count enforcement.** The `Stills Count` view groups World Still rows per engagement. A sprint cannot move to Sealed until that count is 12 to 16. This is a build-time check, not a vibe.
- **Drift discipline.** Every World Still and film frame carries a `Vault Room Compliance` value. Anything marked `Drift flagged` blocks the parent deliverable. The Vault Room is the moat; drift is the primary failure mode, so it is a tracked field, not a judgment call.
- **Seal coverage.** `Seal Watermark` = `Required` on every World Still and the film's final frame and the deck cover. The asset cannot reach `Approved` while a required Seal is unapplied.
- **Gate before ship.** No asset reaches `Shipped` without `Max-Readiness Result` = `Pass`. The `Gate Queue` view is the operator's pre-handoff checklist.
- **Notion mirror.** `Notion Mirror` flips true when the asset is surfaced read-only in the Client Room gallery (§1.3, page 01/02). This keeps the buyer-facing room and the operator tracker in sync without giving the buyer the CRM.
- **One recut, traced.** Exactly one asset across the engagement may carry `Recut Flag` = true. Once set, the engagement's `Recut Used` checkbox flips. The closed-scope promise is enforced at the row level.

### 2.5 Table: CONTACTS

One row per human. Faceless-safe: no photos, no headshots, no identity imagery stored. Names below are placeholders.

| Field | Type | Notes / select options |
|---|---|---|
| Contact Name | Single line text | placeholder, e.g. "Owner · HOUSE-0001" |
| Role | Single select | `Owner-Operator (economic buyer)`, `Founder`, `Referrer`, `Board / Banker / Acquirer (deck recipient)`, `Other` |
| Business Name | Single line text | placeholder |
| Vertical | Single select | `Law Firm`, `Medspa`, `Boutique Builder`, `Financial Advisor`, `Specialty Agency`, `Other` |
| Revenue Band | Single select | `$500K to $1M`, `$1M to $5M`, `$5M+`, `Unknown` |
| ICP Type | Single select | `Established Business`, `Funded Founder` |
| Email | Email | |
| Phone | Phone number | |
| Linked Pipeline | Link to Pipeline | |
| Linked Engagements | Link to Engagements | |
| Relationship Source | Single select | `Referral`, `Inbound`, `Outbound`, `Network`, `Repeat` |
| Status | Single select | `Cold`, `In Conversation`, `Active HOUSE`, `Past HOUSE`, `Do Not Pursue` |
| Photo / Face Stored | Single select | `None (faceless-safe)` (the only valid value; guards the constraint) |
| Notes | Long text | |
| Created | Created time | |

Views: `Buyers` (Role = Owner-Operator/Founder), `Referrers`, `Active HOUSEs`, `Past HOUSEs (referral + expansion targets)`.

### 2.6 Table: PROOF TRACKER

One row per piece of evidence the system worked. This is the engine that turns a delivered sprint into the next sale: testimonials, the verdict the owner now repeats, measurable lift, named-client permission, and case-study assets. Faceless-safe: proof is the claim and the outcome, never a face.

| Field | Type | Notes / select options |
|---|---|---|
| Proof ID | Formula | `"PRF-" & RECORD_ID()` |
| Engagement | Link to Engagements | |
| Proof Type | Single select | `Sole Claim Quote (owner repeats it)`, `Testimonial`, `Outcome Metric`, `Named-Client Permission`, `Case Study Asset`, `Referral Generated`, `Expansion / Upsell`, `Press / Premiere Reaction` |
| Headline | Single line text | the one-line proof, e.g. the claim the owner now uses in sales |
| Outcome Metric | Single line text | e.g. "won 3 deals at full price", "stopped competing on price" |
| Strength | Single select | `Signal`, `Solid`, `Flagship` |
| Permission to Publish | Single select | `Granted (named)`, `Granted (anonymized)`, `Pending`, `Denied` |
| Faceless-Safe Check | Single select | `Clear (no face, no regulated imagery)`, `Needs Review` |
| Linked Asset | Link to Deliverables | the case-study artifact, if produced |
| Quote / Detail | Long text | verbatim proof copy |
| Collected Date | Date | |
| Use In | Multiple select | `Landing`, `Sales Deck`, `Outbound`, `Sovereign Category Audit`, `Internal Only` |
| Status | Single select | `Captured`, `Cleared for Use`, `Published`, `Archived` |

Views: `Flagship Proof` (Strength = Flagship, Permission granted), `Publishable` (Status = Cleared/Published, Faceless-Safe = Clear), `Pending Permission`, `Referral Engine` (Proof Type = Referral/Expansion).

### 2.7 Proof tracker spec (how it operates)

- **The verdict is the asset.** The highest-value proof is `Sole Claim Quote`: the owner now repeats the one sentence in their own sales conversations. That row is worth more than any metric because it proves the product (a verdict repeated for years) landed. Tag these `Flagship` when confirmed.
- **Capture window.** A proof row is opened at handoff (Hour 72) and a follow-up is scheduled at +30 and +90 days to collect outcome metrics and testimonials. The +90 capture feeds Signature's 90-day world pack and Sovereign's category audit.
- **Permission gates publishing.** No proof moves to `Published` without `Permission to Publish` = Granted and `Faceless-Safe Check` = Clear. This protects both the client's identity and the operator's faceless construction.
- **Proof routes to revenue.** The `Use In` field sends cleared proof to the landing, the sales deck, and outbound. `Referral Generated` and `Expansion / Upsell` rows route back into Pipeline as new opportunities (Source = Repeat / Expansion), closing the loop from delivery to next sale.
- **Premium needs proof.** Premium price is the proof of a category of one, and Flagship proof rows are what let the operator hold the $7,500 floor and pitch Sovereign at $25,000+ without discounting.

---

## PART 3 · HOW THE TWO SURFACES SYNC

- **Notion = stage. Airtable = engine.** The buyer lives in the Client Room; the operator lives in the CRM. Nothing crosses except read-only mirrors.
- **One source of truth per fact.** The Sole Claim, the schedule, the six deliverable statuses, and the handoff timestamp live in Airtable and surface read-only in Notion. The buyer never edits CRM data.
- **Gates are shared.** Gate A (Hour 6), Gate B (Hour 24), and the single recut request are the only buyer-write actions, captured in Notion page 04 and written back to the Engagement record's gate fields.
- **The Seal is the sync signal.** When the Engagement's `Seal State` flips from `Locked` to `Struck` and `Max-Readiness Gate` = `Pass`, the Notion room's Handoff page (05) reveals and the Seal strikes live. One symbol, one numeral, one client, one timestamped handoff.

No real client data is stored in this blueprint. All HOUSE codenames, contacts, and proof entries shown are placeholder constructs for build purposes only.
