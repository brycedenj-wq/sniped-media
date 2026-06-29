# PROOF DASHBOARD · V2 (variable-keyed)

Proof, not vibes. Carries forward V1's dashboard (`V1_BUILD/PROOF_DASHBOARD.md`) and keys the numeric thresholds to `{AUDIENCE}` and the trip goal. The columns are concrete now; the numbers resolve the moment `{AUDIENCE}` drops (`V2_BUILD/TRIP_CAMPAIGN_V2.md` propagation table). Local CSV today (Airtable untested, held in the ledger).

The headline is the opened-room access receipt; everything else supports it. The job is to open ONE real room and prove the 10k Campaign Universe Buildout offer (`OFFER_PROTOTYPE.md` proof section).

Constraints: zero spend, zero generation, zero posting, no naming, no crown, no em-dashes, no hype. Numeric thresholds stay UNKNOWN until `{AUDIENCE}` and the trip goal land. The structure and exact columns are fixed now.

---

## HEADLINE METRIC (load-bearing): ROOMS OPENED + ACCESS RECEIPT

The single number that decides whether the offer is proven: count of real rooms opened on the ground, each with a valid access receipt (`V2_BUILD/ACCESS_RECEIPT_TEMPLATE.md`; `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §5). A room is a meeting taken, an intro made, a capture granted, or a conversation toward a paid step, traced to the campaign. No room opened, no proof, regardless of content quality. This is the one thing a creative director, an agency, and an AI operator cannot show.

The minimum the trip must produce is at least one real opened room with a valid receipt. Until that exists, the offer carries as a prototype, never crowned. This metric has no UNKNOWN: one real opened room is the floor and it does not depend on audience size.

Headline kill threshold: zero rooms opened with a valid receipt by `{DATES}` end = "access leg did not fire," logged honestly. The offer is not proven on this trip. The next attempt needs a warmer runway or a different target set. Never fabricate a room to clear the threshold.

---

## SUPPORTING TIERS (each lane tied to a kill threshold)

Four tiers under the headline. Each lane carries a kill threshold so a dead lane is dropped, not nursed (`V1_BUILD/PROOF_DASHBOARD.md` supporting tiers).

| Tier | What it measures | When | Kill threshold | Depends on |
|---|---|---|---|---|
| TIER 1 · BUILD PROOF | each scaffold passed its gate: offer locked, copy bank passed the copy gate, world continuity holds, roster assembled and fit-screened | pre-trip, binary | a scaffold that cannot pass its gate before the trip does not ship into the field | none (binary, ready now) |
| TIER 2 · REACH PROOF | assets published, views, manual save-rate / comprehension read (the virality predictor is a pre-post estimate, not public signal) | live | UNKNOWN: a floor on save-rate / comprehension, set once `{AUDIENCE}` baseline is known | `{AUDIENCE}` |
| TIER 3 · RESPONSE PROOF | reply rate, positive replies, calls booked | live and post | UNKNOWN: a floor on positive-reply rate per N touches, set once `{AUDIENCE}` baseline is known | `{AUDIENCE}` + goal |
| TIER 4 · CASH PROOF | real yes, proposal sent, paid; hold the floor, trade scope not price | post | UNKNOWN: a minimum committed-next-step count by `{DATES}` end, set once the goal is known | trip goal |

If pixels ship, each frame logs a vision-reject pass, no self-crown (`V1_BUILD/PROOF_DASHBOARD.md`; `os-vision-reject-gate`).

---

## WHAT IS UNKNOWN AND WHY

Every numeric target and every tier-2-to-4 kill threshold is UNKNOWN until `{AUDIENCE}` (platforms, rough size, how warm) and the trip goal land. A reply rate or a save rate has no meaning without a baseline. The columns and fields are fixed now so logging starts the moment the trip starts; only the numbers wait. Do not invent a threshold; a guessed number would falsify the kill logic (`V1_BUILD/PROOF_DASHBOARD.md` what-is-UNKNOWN).

The headline is the exception: one real opened room with a valid receipt is the floor, independent of audience size.

---

## CSV SCHEMA (start logging now)

Three local CSV files. Create them at first use; do not pre-populate with invented rows.

### A · rooms.csv (the headline, the access receipts)

One row per opened room. Mirrors the receipt template (`V2_BUILD/ACCESS_RECEIPT_TEMPLATE.md`).

```
room_id,date,what_it_was,who,role_decision_capacity,cohort,campaign_trace,warmth_path,next_paid_step,consent,status
```

- room_id: R001, R002, ...
- what_it_was: meeting_taken | intro_made | capture_granted | conversation_toward_paid_step
- who: name or `{TARGET}` placeholder until real (logged locally only, never posted)
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

- target: `{TARGET}` placeholder or real (local only); links to target_roster.csv (`V2_BUILD/TARGET_DISCOVERY_METHOD.md`)
- angle_used: which of the outreach angles / pillars
- channel: dm | cold_email
- word_count: must be under 80 for a first touch (copy gate)
- sent_approved: yes only after operator go (no row marked sent without it)
- became_room_id: the rooms.csv id if this touch opened a room (the trace link)

### C · content.csv (tier 2, reach proof)

One row per published asset. Only used if and when posting is approved.

```
asset_id,date,pillar,format,posted_approved,views,save_rate_manual,comprehension_read,vision_reject_pass,became_touch_or_room
```

- pillar: which of the five pillars (`V2_BUILD/TRIP_CAMPAIGN_V2.md` §B.2)
- posted_approved: yes only after operator go
- vision_reject_pass: pass | fail (no self-crown), required if the asset is a pixel render
- became_touch_or_room: the touch_id or room_id this asset led to, if any (the content-to-room trace)

---

## HOW THE TIERS CONNECT

content.csv feeds outreach.csv feeds rooms.csv. The whole point is the trace chain: a published asset (C) draws a touch (B) that opens a room (A). The headline reads off A. B and C exist to explain how A happened and to catch a dead lane early via its kill threshold. A room with no upstream trace is a contact, not a campaign proof (`V1_BUILD/PROOF_DASHBOARD.md` how-the-tiers-connect).

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/PROOF_DASHBOARD.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/ACCESS_RECEIPT_PLAN.md` §5
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md` proof section, trade-scope-not-price
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/ACCESS_RECEIPT_TEMPLATE.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/TARGET_DISCOVERY_METHOD.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/TRIP_CAMPAIGN_V2.md` propagation table, five pillars
