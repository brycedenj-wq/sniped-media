# DAY-BY-DAY RUNBOOK · date-relative, keyed to `{DAY_N}`

A runbook written in relative offsets so it works the instant `{DATES}` drop. When the operator drops the start and end dates, every `{DAY_N}` becomes a real calendar date and the loop count sets itself (`V2_BUILD/TRIP_CAMPAIGN_V2.md` propagation table). It carries forward the V1 daily loop and honesty gate (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §4, §6).

The job, every single day: open ONE real room and prove the 10k Campaign Universe Buildout offer. The access move is the load-bearing step each day. Posts are the byproduct (`OFFER_PROTOTYPE.md` proof section; `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §6).

Constraints in force: zero spend, zero generation, zero posting, no naming (placeholders only), no crown, no em-dashes, no hype. Face-independent. Nothing sends or posts without the operator (`V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` field 9).

Key: D0 = arrival day in `{DEST}`. D{n} = departure day (n = trip length minus one, set by `{DATES}`). Negative offsets are pre-trip; positive past D{n} are post-trip. The mid-trip mark = the midpoint between D0 and D{n}, set by `{DATES}`.

---

## PHASE 1 · PRE-TRIP (D-14 to D-1)

The warm runway. The goal is to land in `{DEST}` with rooms already warming, not cold. This phase resolves the moment `{DEST}` lands (it needs the roster) and `{DATES}` land (it sets D-14 as a real date).

### D-14 · Discovery and roster
- Run `TARGET_DISCOVERY_METHOD.md` end to end for `{DEST}` in the `{DATES}` window. Produce `target_roster.csv`, warmest-first.
- Confirm the recognition anchors with the operator: `{SUBJECT}`, `{OBJECT}`, `{THRESHOLD}` (face-independent; the operator's taste, not a face).
- Confirm `{AUDIENCE}` so the pillar ratio and post routing can set, and the dashboard numeric thresholds can resolve (`PROOF_DASHBOARD.md`).

### D-13 to D-8 · Warm window
- Open real engagement with the already-warm and pre-warmable tiers: real comments, real reads on their work, no pitch (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §2). One to two weeks of genuine attention before any cold touch.
- For each top `{TARGET}`, draft (do not send) the value-first micro-offer built for `{THEIR_THING}`. Hold for the operator's go.

### D-7 to D-2 · Pre-warm sends and meeting-setting
- On the operator's go only: send the first-touch outreach to pre-warmed targets. Copy gate per touch: single CTA, under 80 words, no link, plain text, outcome-first, no hype, no em-dashes (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §3). Log each to `outreach.csv`.
- Move any positive reply toward a set meeting inside the `{DATES}` window. Aim to land with at least one meeting on the calendar.
- A positive reply gets a response inside 30 minutes (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §2).

### D-1 · Final set
- Confirm any set meetings. Re-rank the roster by warmth and trigger-moment proximity to `{DATES}`.
- Pre-stage the show-dont-ask artifact for the top targets (a one-pager, a phone-ready cut, the frame of `{THEIR_THING}` already started). Carry it on the ground (ladder rung 2).

Honesty gate (pre-trip): if zero meetings are set and zero positive replies by D-1, that is logged. It does not stop the trip; it raises the cold-access ladder's priority from D0.

---

## PHASE 2 · ON-GROUND (D0 to D{n})

The daily loop, run every day from arrival to departure. The access move is the load-bearing step. Same loop each day; the targets and the warmth path change.

### The daily loop (run D0 through D{n})

1. MORNING SIGNAL + NAMED ACCESS TARGET. Pick today's warmest unworked `{TARGET}` from the roster. Name the one room you intend to open today and the value-first micro-offer built for `{THEIR_THING}`. One named target, not a vague hope.
2. MIDDAY WORK + THE ACCESS MOVE + LOG THE RECEIPT. Do the access move: send the micro-offer (operator go), take the meeting, make the intro, ask for the capture, or move a warm reply toward a paid step. Respond to any positive reply inside 30 minutes. When a room opens, log the receipt row the same day with its campaign trace, using `ACCESS_RECEIPT_TEMPLATE.md`, into `rooms.csv`. No trace, no valid receipt.
3. EVENING BUILD + ONE POST. Build one piece of the campaign artifact for `{THEIR_THING}` (the real machine, not a mockup). Produce at most one post (byproduct, operator go to publish), routed per `{AUDIENCE}` and pulling one of the five pillars. The post exists to draw a touch that becomes a room, not for its own sake.
4. END-OF-DAY HONESTY GATE. Ask: did a room open today, logged with its trace? If yes, log it. If no, log "no room moved." Check the escalation conditions below.

### The escalation (binds to the honesty gate, no new metric)

The cold-access ladder fires when the gate reports:
- NO ROOM MOVED FOR TWO DAYS RUNNING, or
- THE MID-TRIP MARK REACHED WITH ZERO ROOMS OPENED.

Either fires the ladder, run in order (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §4): (1) go where the scene gathers (be physically at the `{THRESHOLD}` / venue / event the `{TARGET}` is in), (2) the show-dont-ask walk-in (carry the built artifact), (3) capture the micro-contact, same-day follow-up, (4) downgrade the ask never the price (a 10-minute coffee, a referral; a referral to a real decision-maker IS an opened room), (5) the honest stop. Do not wait for the last day.

Guardrails every day: value-first only, no mass-DM, no fabrication, consent for any capture, face-independent, nothing posts or sends without the operator.

---

## PHASE 3 · POST-TRIP (D+1 to D+7)

Turn the opened room into a proof artifact and a paid step. Resolves on the same `{DATES}`.

### D+1 to D+2 · Harvest
- Reconcile `rooms.csv`, `outreach.csv`, `content.csv`. Confirm every receipt has a real campaign trace; a row without a trace is a contact, downgraded, not a receipt (`PROOF_DASHBOARD.md`).
- Assemble the built campaign artifact for `{THEIR_THING}` as the portfolio piece (concept through proof dashboard).

### D+3 to D+4 · Payoff
- For each opened room, deliver the value promised and move to the committed NEXT_PAID_STEP (proposal to send, follow-up call booked, scope to scope).
- Draft the honest-receipt post (pillar 5), the case-study asset, on the operator's go only.

### D+5 to D+7 · Close and reconcile
- Send proposals on the operator's go. Hold the floor, trade scope not price (`OFFER_PROTOTYPE.md` trade-scope-not-price).
- Reconcile the dashboard against its kill thresholds (`PROOF_DASHBOARD.md`). Mark the headline: at least one real opened room with a valid receipt = the offer carries past prototype on this trip; zero = "access leg did not fire," logged honestly, the offer is not yet proven, and the next attempt needs a warmer runway or a different target set.

Honest-stop rule for the whole runbook: never fabricate a room, never post a fake receipt. A failed access leg is a real result, not a content problem (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §4 rung 5).

---

## HOW IT RESOLVES ON `{DATES}`

Drop start and end dates and: D-14 through D-1 become real pre-trip dates, D0 through D{n} become the on-ground loop days (count set by trip length), the mid-trip mark gets a date, and D+1 through D+7 become the post-trip dates. No rebuild; the offsets fill.

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/ACCESS_RECEIPT_PLAN.md` §2, §3, §4, §6
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md` proof section, trade-scope-not-price
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` field 9
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/TRIP_CAMPAIGN_V2.md` propagation table, five pillars, access-first spine
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/TARGET_DISCOVERY_METHOD.md` roster
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/ACCESS_RECEIPT_TEMPLATE.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/PROOF_DASHBOARD.md`
