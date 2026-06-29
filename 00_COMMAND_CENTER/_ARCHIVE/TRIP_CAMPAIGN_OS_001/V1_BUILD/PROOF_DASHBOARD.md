# PROOF DASHBOARD · structure and CSV schema

Proof, not vibes. Local CSV today (Airtable untested, held in the ledger). This upgrades `v0_parts/strategy.md` §5 and `sections/ops.md` §13. The headline is the opened-room access receipt; everything else supports it.

Constraints: zero spend, zero generation, zero posting, no naming, no crown, no em-dashes, no hype. Numeric thresholds stay UNKNOWN until [CURRENT AUDIENCE] and the trip goal land. The structure and the exact columns are fixed now; the numbers wait on the intake.

---

## HEADLINE METRIC (load-bearing): ROOMS OPENED + ACCESS RECEIPT

The single number that decides whether the offer is proven: count of real rooms opened on the ground, each with a valid access receipt (`OFFER_PROTOTYPE.md` proof section; `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §5). A room is a meeting taken, an intro made, a capture granted, or a conversation toward a paid step, traced to the campaign. No room opened, no proof, regardless of content quality. This is the one thing a creative director, an agency, and an AI operator cannot show.

The headline reads off the rooms CSV below. The minimum the trip must produce is at least one real opened room with a valid receipt; until that exists, the offer carries as a prototype, never crowned.

---

## Supporting tiers

Four tiers under the headline (`sections/ops.md` §13.1). Each lane carries a kill threshold so a dead lane is dropped, not nursed (`sections/ops.md` §13.3).

- TIER 1 · BUILD PROOF (pre-trip, binary). Each scaffold passed its gate: offer locked, copy bank passed the copy gate, world continuity holds, outreach list assembled and fit-screened. Kill threshold: a scaffold that cannot pass its gate before the trip does not ship into the field.
- TIER 2 · REACH PROOF (live). Assets published, views, manual save-rate / comprehension read. The virality predictor is a pre-post estimate, not public signal. Numeric thresholds UNKNOWN until [CURRENT AUDIENCE] lands. Kill threshold: UNKNOWN (set as a floor on save-rate / comprehension once the baseline audience is known).
- TIER 3 · RESPONSE PROOF (live and post). Reply rate, positive replies, calls booked. Numeric thresholds UNKNOWN until [CURRENT AUDIENCE] and goal land. Kill threshold: UNKNOWN (set as a floor on positive-reply rate per N touches once the baseline is known).
- TIER 4 · CASH PROOF (post). Real yes, proposal sent, paid. Hold the floor, trade scope not price (`OFFER_PROTOTYPE.md` trade-scope-not-price). Numeric thresholds UNKNOWN until goal lands. Kill threshold: UNKNOWN (set as a minimum committed-next-step count by trip end once the goal is known).

If pixels ship, each frame logs a vision-reject pass, no self-crown (`sections/ops.md` §13.2, W5).

---

## What is UNKNOWN and why

Every numeric target and every tier-2-to-4 kill threshold is UNKNOWN until the baseline lands. Tier 2, 3, 4 thresholds all need [CURRENT AUDIENCE] (platforms, rough size, how warm) and the trip goal to be set; a reply rate or a save rate has no meaning without a baseline. The columns and fields are fixed now so logging starts the moment the trip starts; only the numbers wait (`v0_parts/strategy.md` §5; `INTAKE_FILLED_AND_LEDGER.md` field 6). Do not invent a threshold; a guessed number would falsify the kill logic.

The headline metric is the exception: it has no UNKNOWN. One real opened room with a valid receipt is the floor, and that does not depend on audience size.

---

## CSV schema (start logging now)

Three local CSV files. Create them at first use; do not pre-populate with invented rows.

### A · rooms.csv (the headline, the access receipts)

One row per opened room. Mirrors the receipt spec in `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §5.

```
room_id,date,what_it_was,who,role_decision_capacity,cohort,campaign_trace,warmth_path,next_paid_step,consent,status
```

- room_id: R001, R002, ...
- what_it_was: meeting_taken | intro_made | capture_granted | conversation_toward_paid_step
- who: name or [TARGET NAME] placeholder until real (logged locally only, never posted)
- cohort: moment_holder | under_built | venue_scene_gatekeeper
- campaign_trace: the exact angle / post / artifact that produced the room (no trace, not a valid receipt)
- warmth_path: already_warm | pre_warmed | cold_but_fit | ladder_r1 | ladder_r2 | ladder_r3 | ladder_r4
- next_paid_step: the committed next step, or none_yet
- consent: yes | not_applicable
- status: open | advancing | stalled | closed_won | closed_lost

### B · outreach.csv (tier 3, response proof)

One row per touch.

```
touch_id,date,target,cohort,angle_used,channel,word_count,sent_approved,replied,positive_reply,call_booked,became_room_id
```

- angle_used: which of the ten angles (`V1_BUILD/OUTREACH_10.md`)
- channel: dm | cold_email
- word_count: must be under 80 for a first touch (copy gate)
- sent_approved: yes only after operator go (no row marked sent without it)
- became_room_id: the rooms.csv id if this touch opened a room (the trace link)

### C · content.csv (tier 2, reach proof)

One row per published asset. Only used if and when posting is approved.

```
asset_id,date,pillar,format,posted_approved,views,save_rate_manual,comprehension_read,vision_reject_pass,became_touch_or_room
```

- posted_approved: yes only after operator go
- vision_reject_pass: pass | fail (W5, no self-crown), required if the asset is a pixel render
- became_touch_or_room: the touch_id or room_id this asset led to, if any (the content-to-room trace)

---

## How the tiers connect

content.csv feeds outreach.csv feeds rooms.csv. The whole point is the trace chain: a published asset (C) draws a touch (B) that opens a room (A). The headline reads off A. B and C exist to explain how A happened and to catch a dead lane early via its kill threshold. A room with no upstream trace is a contact, not a campaign proof.

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/v0_parts/strategy.md` §5, §6
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/sections/ops.md` §13
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/ACCESS_RECEIPT_PLAN.md` §5
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` field 6
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/OUTREACH_10.md` (content half, angle copy)
