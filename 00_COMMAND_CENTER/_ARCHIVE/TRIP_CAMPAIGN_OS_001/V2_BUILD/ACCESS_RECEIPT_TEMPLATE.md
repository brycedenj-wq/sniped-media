# ACCESS RECEIPT TEMPLATE · fillable

A fillable template, not a plan. The opened room plus its receipt is the single load-bearing proof of the whole campaign, the one thing a creative director, an agency, and an AI operator cannot show (`OFFER_PROTOTYPE.md` proof section; `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §5). Fill one block per opened room, the same day it opens. Then log the matching row in `rooms.csv` (`PROOF_DASHBOARD.md`).

A room is opened when a real person, in the real world, on this trip, takes a real next step traceable to the campaign. A like, a follow, a generic "keep in touch," or a hallway hello with no next step does not count (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §1).

Constraints: zero spend, zero generation, zero posting, no naming in any public surface (real names logged locally only), no crown, no em-dashes, no hype. Face-independent. Nothing posts without the operator.

---

## THE COPY-PASTE BLOCK

Copy this block, fill every field, the day the room opens.

```
RECEIPT NUMBER:        R___                          (sequential: R001, R002, ...)
DATE:                  ____-__-__                     (within {DATES})
ROOM TYPE:             [ ] meeting  [ ] intro  [ ] capture granted  [ ] conversation toward a paid step
WHO + ROLE:            ___________________            (real name + decision capacity, logged locally only)
CONSENT:               [ ] yes  [ ] not applicable    (required for any capture)
WHAT MOVED (one line): ___________________            (the single real next step that happened)
CAMPAIGN TRACE:        ___________________            (the exact post / DM / artifact that produced it)
NEXT PAID STEP + DATE: ___________________ / ____-__-__   (or "none yet")
PROOF ARTIFACT:        ___________________            (optional: file path / link, local only)
HONEST STATUS:         [ ] opened  [ ] partial  [ ] did not fire
```

A receipt is VALID only when ROOM TYPE, WHO, DATE, and CAMPAIGN TRACE are all real and filled. A block missing the trace is not a receipt; it is a contact. No trace, no valid receipt.

---

## EXAMPLE RECEIPT 1 (variables shown, so the shape is clear)

```
RECEIPT NUMBER:        R001
DATE:                  {DATES start} + 2
ROOM TYPE:             [x] meeting
WHO + ROLE:            {TARGET} (moment_holder, decision-maker for {THEIR_THING})
CONSENT:               [ ] not applicable    (no capture, a conversation)
WHAT MOVED (one line): {TARGET} agreed to a working session on {THEIR_MOMENT} after seeing the teardown.
CAMPAIGN TRACE:        the built-for-them teardown (pillar 1), sent D{DAY_N} as the value-first micro-offer.
NEXT PAID STEP + DATE: send the scoped 10k Campaign Universe Buildout proposal / {DATES end} + 3
PROOF ARTIFACT:        local note of the session, no public post
HONEST STATUS:         [x] opened
```

## EXAMPLE RECEIPT 2 (a partial, downgraded-ask room)

```
RECEIPT NUMBER:        R002
DATE:                  {DATES start} + 4
ROOM TYPE:             [x] intro
WHO + ROLE:            a {venue_scene_gatekeeper} at {THRESHOLD} (referrer to a real decision-maker)
CONSENT:               [ ] not applicable
WHAT MOVED (one line): the gatekeeper offered to connect the operator to {TARGET} who is launching {THEIR_THING}.
CAMPAIGN TRACE:        cold-access ladder rung 1 (went where the scene gathers) + rung 4 (downgraded the ask to a referral).
NEXT PAID STEP + DATE: confirm the warm intro, then send the micro-offer / {DATES start} + 5
PROOF ARTIFACT:        none
HONEST STATUS:         [x] partial
```

A referral to a real decision-maker IS an opened room and logs with its trace; that is scope-trade applied to access, never a discount (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §4 rung 4).

---

## THE HONEST-STOP RULE (never fabricate a room)

If the full cold-access ladder runs and no room opens by the trip's end, log it as a real result, not a content problem:

```
RECEIPT NUMBER:        R000 (none opened)
DATE:                  {DATES end}
ROOM TYPE:             none
HONEST STATUS:         [x] did not fire
NOTE:                  access leg did not fire. The offer is not yet proven on this trip. Next attempt needs
                       a warmer pre-trip runway or a different target set. No fabricated room logged.
```

Never log a room that did not open. Never post a fake receipt. The honesty is part of the moat; a faked receipt destroys the one thing competitors cannot show (`OFFER_PROTOTYPE.md` proof section; `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §4 rung 5). A "did not fire" entry is the truth, and the truth is what makes the real receipts worth anything.

---

## FIELD-TO-CSV MAP (logging the same row)

Each receipt block maps to one `rooms.csv` row (`PROOF_DASHBOARD.md` schema A):

| Receipt field | rooms.csv column |
|---|---|
| RECEIPT NUMBER | room_id |
| DATE | date |
| ROOM TYPE | what_it_was |
| WHO + ROLE | who, role_decision_capacity |
| (target cohort) | cohort |
| CAMPAIGN TRACE | campaign_trace |
| (which warmth rung) | warmth_path |
| NEXT PAID STEP | next_paid_step |
| CONSENT | consent |
| HONEST STATUS | status (opened -> open/advancing, partial -> open, did not fire -> not logged as a room) |

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/ACCESS_RECEIPT_PLAN.md` §1, §4, §5
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md` proof section, trade-scope-not-price
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/PROOF_DASHBOARD.md` rooms.csv schema
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/TRIP_CAMPAIGN_V2.md` variable key
