# PROOF DASHBOARD · V3 LA (access-first, low-audience)

Proof, not vibes. Carries forward V2's dashboard (`V2_BUILD/PROOF_DASHBOARD.md`) and tunes it for an LA proof sprint where the audience is UNKNOWN and the play is access-first, not post-and-hope (`TRIP_CAMPAIGN_V3.md` §A.3). Because reach numbers are not the proof here, the reach tier is de-emphasized and the response/access tier leads. Local CSV today (Airtable untested, held in the ledger).

The headline is the opened-room access receipt; everything else supports it. The job is to open ONE real room in LA and prove the 10k Campaign Universe Buildout offer (`OFFER_PROTOTYPE.md` proof section; `ACCESS_RECEIPT_PLAN.md`).

Constraints: zero spend, zero generation, zero posting, no naming, no crown, no em-dashes, no hype. Reach-tier numeric thresholds stay UNKNOWN until `{AUDIENCE}` drops; the access-tier targets are given as an operator-adjustable default because access count is the real proof here, not reach.

---

## HEADLINE METRIC (load-bearing): ROOMS OPENED + ACCESS RECEIPT

The single number that decides whether the offer is proven: count of real rooms opened in LA, each with a valid access receipt (`V2_BUILD/ACCESS_RECEIPT_TEMPLATE.md`; `ACCESS_RECEIPT_PLAN.md` §1, §6). A room is a meeting taken, an intro made, a capture granted, or a conversation toward a paid step, traced to the campaign. No room opened, no proof, regardless of content quality or reach. This is the one thing a creative director, an agency, and an AI operator cannot show.

The minimum the sprint must produce is at least one real opened room with a valid receipt. Until that exists, the offer carries as a prototype, never crowned. This metric has no UNKNOWN: one real opened room is the floor, and it does not depend on audience size, which is exactly why it leads when the audience is unknown.

Headline kill threshold: zero rooms opened with a valid receipt by Day 14 = "this sprint did not fire," logged honestly. The offer is not proven on this sprint. Because the operator lives in LA, the proof cell stays open; the next sprint runs with a warmer runway. Never fabricate a room to clear the threshold (`ACCESS_RECEIPT_PLAN.md` §6).

---

## TIER ORDER, V3 (access leads, reach de-emphasized)

V2 ran reach as tier 2, response as tier 3, cash as tier 4. V3 reorders for a low, unknown audience: the ACCESS/RESPONSE tier leads under the headline, and the REACH tier is demoted to a supporting read, because reach numbers cannot be the proof when the audience is unknown (`TRIP_CAMPAIGN_V3.md` §A.3).

| Tier | What it measures | When | Kill threshold | Depends on |
|---|---|---|---|---|
| TIER 1 · BUILD PROOF | each scaffold passed its gate: offer locked, roster assembled and fit-screened, micro-offer hooks ready, world continuity holds | pre-sprint, binary | a scaffold that cannot pass its gate before the sprint does not ship into the field | none (binary, ready now) |
| TIER 2 · ACCESS / RESPONSE PROOF (LEADS) | touches made, reply rate, positive replies, meetings booked, rooms opened, access receipts logged | live and ongoing | access-count default below (operator-adjustable); a sprint that misses the access floor is the headline kill | access count is the proof, not audience size |
| TIER 3 · REACH PROOF (DE-EMPHASIZED) | assets published, views, manual save-rate / comprehension read; a supporting read only, never the proof | live, if posting is approved | UNKNOWN: a floor on save-rate / comprehension, set only if and when `{AUDIENCE}` baseline is known; not a sprint kill on its own | `{AUDIENCE}` |
| TIER 4 · CASH PROOF | real yes, proposal sent, paid; hold the 10k floor, trade scope not price | post | UNKNOWN: a minimum committed-next-step count by Day 14, set once the operator sets the goal | sprint goal |

If pixels ship, each frame logs a vision-reject pass, no self-crown (`os-vision-reject-gate`; `APPROVAL_LIST.md` gate f).

---

## THE 14-DAY ACCESS-COUNT TARGET (operator-adjustable DEFAULT)

Reach numbers are not the proof here, so the dashboard sets ACCESS-COUNT targets instead, stated as a sane default the operator can adjust. These are not crowned numbers; they are a starting structure for a 14-day access-first sprint, clearly operator-adjustable. The operator sets the real numbers; these exist so logging has a floor to read against on Day 1.

| Lane | Default 14-day target (operator-adjustable) | Kill threshold |
|---|---|---|
| Approved roster size (FIT + HOLD) | 15 to 25 screened targets | fewer than 8 roster-ready FIT/HOLD rows = the roster is too thin to run; widen discovery before any outreach |
| Touches made (after operator go) | 10 to 15 approved touches across the sprint | fewer than 5 touches by Day 7 = the outreach lane is stalled; surface to operator |
| Positive replies | 2 to 4 positive replies | zero positive replies by Day 10 across all approved touches = the angle or target set is wrong; revise before more sends |
| Rooms opened (the headline) | at least 1 valid opened room; 2 to 3 is a strong sprint | zero rooms with a valid receipt by Day 14 = "this sprint did not fire," logged honestly |
| Conversations toward a paid step | at least 1 | zero by Day 14 = access opened but did not move toward cash; note honestly, do not crown the offer |

These defaults assume an access-first, manual, low-audience sprint. The headline (at least one valid opened room) is the only non-negotiable floor; everything above it is the operator's to tune. Do not invent a reach number; a guessed reach threshold would falsify the kill logic (`V2_BUILD/PROOF_DASHBOARD.md` what-is-UNKNOWN). The access counts are defaults precisely because access, not reach, is what proves the offer.

---

## CSV SCHEMA (start logging now)

Three local CSV files. Create them at first use; do not pre-populate with invented rows. Carries V2's schema with an LA neighborhood field added to rooms.csv.

### A · rooms.csv (the headline, the access receipts)

```
room_id,date,what_it_was,who,role_decision_capacity,cohort,la_neighborhood_cluster,campaign_trace,warmth_path,next_paid_step,consent,status
```

- room_id: R001, R002, ...
- what_it_was: meeting_taken | intro_made | capture_granted | conversation_toward_paid_step
- who: name or `{TARGET}` placeholder until real (logged locally only, never posted)
- cohort: moment_holder | under_built | venue_scene_gatekeeper
- la_neighborhood_cluster: the LA cluster the room happened in (logged locally)
- campaign_trace: the exact angle / post / artifact that produced the room (no trace, not a valid receipt)
- warmth_path: already_warm | pre_warmed | cold_but_fit | ladder_r1 | ladder_r2 | ladder_r3 | ladder_r4
- next_paid_step: the committed next step, or none_yet
- consent: yes | not_applicable
- status: open | advancing | stalled | closed_won | closed_lost

### B · outreach.csv (tier 2 access/response, leads)

```
touch_id,date,target,cohort,angle_used,channel,word_count,sent_approved,replied,positive_reply,meeting_booked,became_room_id
```

- target: `{TARGET}` placeholder or real (local only); links to `la_target_roster.csv` (`LA_TARGET_DISCOVERY_ROSTER_METHOD.md`)
- angle_used: which outreach angle / pillar
- channel: dm | cold_email
- word_count: must be under 80 for a first touch (copy gate)
- sent_approved: yes only after operator go (no row marked sent without it, `APPROVAL_LIST.md` gate b)
- became_room_id: the rooms.csv id if this touch opened a room (the trace link)

### C · content.csv (tier 3 reach, de-emphasized, only if posting approved)

```
asset_id,date,pillar,format,posted_approved,views,save_rate_manual,comprehension_read,vision_reject_pass,became_touch_or_room
```

- pillar: which of the five pillars (`TRIP_CAMPAIGN_V3.md` §A.3)
- posted_approved: yes only after operator go (`APPROVAL_LIST.md` gate c)
- vision_reject_pass: pass | fail (no self-crown), required if the asset is a pixel render
- became_touch_or_room: the touch_id or room_id this asset led to, if any (the content-to-room trace)

---

## HOW THE TIERS CONNECT (V3)

In V2 the chain ran content -> outreach -> rooms with reach leading. In V3, with an unknown audience, content is the documentation layer, not the engine: the engine is access. The chain reads access-first: a screened roster (`la_target_roster.csv`) drives a touch (outreach.csv) that opens a room (rooms.csv); content (content.csv) DOCUMENTS that it happened. The headline reads off rooms.csv. Outreach is the lead supporting tier; content is a de-emphasized record. A room with no upstream trace is a contact, not a campaign proof (`V2_BUILD/PROOF_DASHBOARD.md` how-the-tiers-connect; `TRIP_CAMPAIGN_V3.md` §A.3).

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/PROOF_DASHBOARD.md` headline, tiers, what-is-UNKNOWN, CSV schema
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/ACCESS_RECEIPT_TEMPLATE.md` receipt validity, field-to-CSV map
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md` proof section, trade-scope-not-price
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/TRIP_CAMPAIGN_V3.md` access-first documentation role, honesty gate
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/LA_TARGET_DISCOVERY_ROSTER_METHOD.md` roster schema
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/ACCESS_RECEIPT_PLAN.md` what counts as a room, receipt spec
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/APPROVAL_LIST.md` send, posting, pixel gates
