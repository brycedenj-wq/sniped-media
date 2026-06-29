# TRIP CAMPAIGN V2 · THE MASTER (variable-driven)

This is the V2 master. V1 (`V1_BUILD/TRIP_CAMPAIGN_V1.md`) locked the commercial spine and shrank the blanks to three real trip facts. V2 takes the next step: it stops treating destination, dates, and audience as blanks to stall on and treats them as SWAPPABLE VARIABLES. The campaign is fully built now. It resolves to concrete the moment those three facts drop in.

The job has not changed and is stated everywhere: the job is not to make travel content. It is to open ONE real room and prove the 10k Campaign Universe Buildout offer. The opened room plus its access receipt is the load-bearing proof (`OFFER_PROTOTYPE.md` proof section; `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §1).

Constraints in force: zero spend, zero generation, zero posting, no naming (placeholders only), no crown, no em-dashes, no hype. Face-independent (real models, characters, world faces, wardrobe, objects, places, POV, hands, body, and the operator's voice, taste, and story are allowed; the operator's face is never the load-bearing reason it works) (`V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` field 9).

---

## PART A · THE VARIABLE SYSTEM

V2's whole design is here. Every place the campaign needs a real fact is a named variable, not a blank. When the operator drops the value, it flows everywhere the variable appears in one pass. Use these EXACT tokens in every V2 file.

### A.1 · Variable key

| Token | Meaning | Current value | Class |
|---|---|---|---|
| `{DEST}` | The destination, the city or region the trip lands in | UNKNOWN | primary (operator drops) |
| `{DATES}` | The trip start and end, as real calendar dates | UNKNOWN | primary (operator drops) |
| `{AUDIENCE}` | The current audience: platforms, rough size, how warm | UNKNOWN | primary (operator drops) |
| `{TARGET}` | A single screened target on the roster | RESOLVED by method, downstream of `{DEST}` + `{DATES}` | derived |
| `{THEIR_THING}` | That target's real input: their launch, drop, tour, world, idea | RESOLVED by method, per `{TARGET}` | derived |
| `{THEIR_MOMENT}` | That target's dated moment that creates the trigger | RESOLVED by method, per `{TARGET}` | derived |
| `{SUBJECT}` | Who or what is on camera (model, character, object, place, POV) | operator-chosen, face-independent | locked posture |
| `{OBJECT}` | The running object that recurs across the trip's assets | operator-chosen recognition anchor | locked posture |
| `{THRESHOLD}` | The repeated place-edge: a door, a gate, a counter, a window the work returns to | operator-chosen recognition anchor | locked posture |
| `{DAY_N}` | The relative day index from arrival (D0 = arrival day) | RESOLVED by `{DATES}` | derived |

Occasion is already resolved: operator-chosen proof trip, no fixed event unless the operator names one (`V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` field 3). The offer fork is already resolved: Campaign Universe Buildout is active, BASEPLATE is parked as a one-line redirect (`V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` ledger A1).

### A.2 · Propagation table (variable to every place it fills)

This is the load-bearing table of V2. Each row says: when this variable drops, exactly these slots go concrete. Nothing fills until the value lands; nothing stays blank that this table can fill.

| Variable | Drops in | Propagates to (every slot it fills) |
|---|---|---|
| `{DEST}` | a city / region | the geography and scenes in `TARGET_DISCOVERY_METHOD.md` §1; the candidate-sourcing channels (geotags, local hashtags, venue rosters, event calendars in the area) §3; the roster's `{TARGET}` names; the cliche-to-avoid list for the place; the location daylight rig and wardrobe lane in the shot/styling layer; the venue / scene access points in `ACCESS_RECEIPT_TEMPLATE.md`; the `{THRESHOLD}` candidate set the operator picks from |
| `{DATES}` | start + end calendar dates | every `{DAY_N}` in `DAY_BY_DAY_RUNBOOK.md` (D-14 through D+7 become real dates); the pre-warm window (D-14 to D-1); the on-ground loop count (D0 to D{n}); the trip-bounded deadline; the mid-trip mark that fires the cold-access ladder; the event-calendar window in `TARGET_DISCOVERY_METHOD.md` §3; the reachable-in-window line of the fit screen; the date field default in `ACCESS_RECEIPT_TEMPLATE.md` |
| `{AUDIENCE}` | platforms + rough size + warmth | the post routing and platform per asset; the pillar ratio; the warm-window starting list in `DAY_BY_DAY_RUNBOOK.md` D-14; the already-warm-in-location bucket in `TARGET_DISCOVERY_METHOD.md`; every numeric threshold and every kill number in `PROOF_DASHBOARD.md` tiers 2, 3, 4 (reach, response, cash) |
| `{TARGET}` | one screened person/brand/venue | one roster row; one thesis-sentence fill; the named target in each `{DAY_N}` morning signal; the WHO field in each access receipt |
| `{THEIR_THING}` | their real input | the value-first micro-offer built for them; the outreach angle's Only-Them line; the campaign artifact the trip builds |
| `{THEIR_MOMENT}` | their dated moment | the trigger-event field of the fit screen; the reason-to-meet timing; the deadline the micro-offer points at |
| `{SUBJECT}` | who/what on camera | the shot list subject; the styling subject; the post's visible content |
| `{OBJECT}` | the running object | the recurring recognition element across assets; one continuity anchor in the world layer |
| `{THRESHOLD}` | the place-edge | the repeated framing the trip returns to; the second continuity anchor |
| `{DAY_N}` | derived from `{DATES}` | every dated line in the runbook |

Reading rule: `{DEST}` and `{DATES}` together resolve `{TARGET}` / `{THEIR_THING}` / `{THEIR_MOMENT}` (you cannot screen a real target without a place and a window). `{DATES}` alone resolves every `{DAY_N}`. `{AUDIENCE}` alone resolves the dashboard numbers and the post routing. None of the three depends on the other two, so the operator can drop them in any order and the resolved set fills in dependency order.

---

## PART B · THE CONCRETE V2 CAMPAIGN STRUCTURE

### B.1 · Thesis (active offer baked in)

The trip is a wedge, not the product. It converts physical presence in one place into one opened room, real relationships, and a proof artifact, on the lane the operator already owns (`V1_BUILD/TRIP_CAMPAIGN_V1.md` thesis; `OFFER_PROTOTYPE.md` commercial thesis).

The offer is Campaign Universe Buildout: take any real input a person brings (a trip, a concert, an artist, a brand, an idea, a script, a character, a world, a launch) and build the whole machine around it, concept through proof dashboard, handed over built and owned. The buyer is an artist or concert with a moment coming, a brand with a launch, or a founder with a world and no machine, screened in-lane, can-say-yes, cares-about-the-outcome, low-self-orientation; a price-shopper is a pass (`OFFER_PROTOTYPE.md` who-this-serves; `V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` field 5).

Thesis sentence, written in tokens so it resolves on drop-in:

> On this trip, the operator shows up in `{DEST}` as the one who can build the whole campaign machine around a real input, so `{TARGET}` (an artist, brand, or founder with `{THEIR_MOMENT}` coming) gets `{THEIR_THING}` turned into a built, owned campaign machine, and that opened room becomes the access receipt that proves the offer.

Three properties the thesis holds (each gates the copy): outcome-first (lead with the target's result, never the trip or a bio), in-lane and scope-traded (10k proven floor, 25k entertained, 50k+ anchor; trade scope, never price), face-independent (the access receipt, not a face, is the load-bearing proof) (`OFFER_PROTOTYPE.md` tier sections, trade-scope-not-price).

### B.2 · The five pillars

The five repeatable content angles, carried as the V1 content half intends them, each doing two jobs at once: recognition (the work is recognizably one body of work) and access (each angle gives a real reason a `{TARGET}` opens a room). Posts are the byproduct; the room is the point (`V1_BUILD/TRIP_CAMPAIGN_V1.md` component 5; `V1_BUILD/ACCESS_RECEIPT_PLAN.md` §6).

1. THE BUILT-FOR-THEM TEARDOWN. A short, specific frame of where `{THEIR_THING}` is leaving reach on the table, built before any ask. Recognition: shows the operator thinks in campaigns, not posts. Access: it is the value-first micro-offer that earns the meeting (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §3).
2. THE PLACE-EDGE SERIES. The work returns to `{THRESHOLD}` in `{DEST}`, the same place-edge across days. Recognition: a repeated frame makes a scattered trip read as one body. Access: being physically at the `{THRESHOLD}` where the scene gathers is rung 1 of the cold-access ladder.
3. THE RUNNING-OBJECT THREAD. `{OBJECT}` recurs across assets as the continuity anchor. Recognition: the object is the through-line nobody else can copy cheaply. Access: a tangible built piece (the object, or a one-pager carrying it) is the show-dont-ask walk-in, rung 2 of the ladder.
4. THE OUTCOME-FIRST PROOF NOTE. Each asset states the target's outcome, never the operator's bio. Recognition: it reads as a campaign brain, not a portfolio. Access: it is the language that converts a warm reply toward a paid step.
5. THE HONEST-RECEIPT POST (post-trip only, approval-gated). What actually moved, with the access receipt as the spine. Recognition: proof, not vibes. Access: it is the case-study asset that turns the prototype into a sellable offer (`OFFER_PROTOTYPE.md` proof-cell link).

Pillar ratio is set when `{AUDIENCE}` drops (post routing depends on platforms and warmth). Until then the five pillars stand; the mix waits.

### B.3 · The access-first spine

Every component points at the one room. The spine, in order, is the same machine V1 built, now keyed to variables (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §2, §3, §4):

1. Warmest-first sequence: already-warm in `{DEST}` during `{DATES}`, then pre-warmed targets, then cold-but-fit. Work warm before cold.
2. The value-first micro-offer: each `{TARGET}` gets a free, specific piece built for `{THEIR_THING}`, delivered before any ask. The micro-offer is the CTA; the meeting is the pivot.
3. The cold-access ladder (5 rungs): go where the scene gathers, the show-dont-ask walk-in, capture the micro-contact with same-day follow-up, downgrade the ask never the price, the honest stop. Fires on the trigger in §B.4.
4. The receipt: every opened room logs one row the same day with its campaign trace, in `PROOF_DASHBOARD.md` rooms.csv. No trace, no valid receipt.

What counts as a room (unchanged from V1): a meeting taken, an intro made, a capture granted, or a conversation toward a paid step, traced to the campaign. A like, a follow, a generic "keep in touch," or a hallway hello with no next step does not count (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §1).

### B.4 · The honesty gate and the ladder trigger

Each on-ground day ends with the same honesty gate V1 set: did a room open, logged with its trace, or did no room move (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §4, §6). The cold-access ladder fires when the gate reports no room moved for two days running, OR the mid-trip mark (set by `{DATES}`) is reached with zero rooms opened. If the full ladder runs and no room opens by the trip's end, that is logged as "access leg did not fire." Never fabricate a room. Never post a fake receipt. The honesty is part of the moat.

### B.5 · What changed, V1 to V2

| Dimension | V1 | V2 |
|---|---|---|
| The three facts | three remaining blanks, marked UNKNOWN | three named variables with a propagation table; UNKNOWN is a value, not a stall |
| Target discovery | a fit screen and warmest-first sequence, but named targets waited on destination with no procedure | a destination-agnostic, runnable discovery method that produces a target roster CSV the day `{DEST}` lands |
| The runbook | a daily loop described in prose | a date-relative runbook keyed to `{DAY_N}` that becomes real dates the instant `{DATES}` drop |
| The receipt | a receipt spec (fields described) | a fillable copy-paste template with two worked examples and the honest-stop rule baked in |
| Resolution | operator answers three blanks, then a rebuild pass | operator drops three values, the propagation table fills every slot in one pass, no rebuild |
| Offer fork | surfaced and flagged | resolved: Campaign Universe Buildout active, BASEPLATE parked as a one-line redirect |

The room-opening machine, the warmest-first sequence, the cold-access ladder, the proof-dashboard structure, and the approval boundary are unchanged. V2 makes the inputs swappable, not the machine.

### B.6 · The BASEPLATE redirect (parked, one line)

BASEPLATE is parked, not active. One-line redirect: if the operator says "this trip is a BASEPLATE B2B dossier trip," swap the offer layer (Campaign Universe Buildout becomes the dossier, price re-anchors to $2,500 to $4,000), the target layer (artist/brand/founder becomes staffing-firm decision-makers), and the copy layer (angles re-point to the staffing-firm problem); the access-receipt logic, warmest-first sequence, cold-access ladder, dashboard, and approval boundary do not change (`V1_BUILD/TRIP_CAMPAIGN_V1.md` BASEPLATE fork; `V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` ledger A1).

---

## PART C · DROP-IN RESOLUTION

The operator drops `{DEST}` + `{DATES}` + `{AUDIENCE}`. The whole campaign goes concrete in one pass, in this dependency order:

1. `{DATES}` lands. Every `{DAY_N}` in `DAY_BY_DAY_RUNBOOK.md` becomes a real calendar date. The pre-warm window, the loop count, the trip deadline, and the mid-trip ladder-trigger date all resolve.
2. `{DEST}` lands. `TARGET_DISCOVERY_METHOD.md` runs: geography and scenes defined, candidate channels searched, fit screen applied, warmest-first ranked. The output is the target roster CSV, which resolves `{TARGET}`, `{THEIR_THING}`, `{THEIR_MOMENT}` per row. The `{THRESHOLD}` candidate set surfaces for the operator to pick. The location rig and wardrobe lane set.
3. `{AUDIENCE}` lands. `PROOF_DASHBOARD.md` numeric thresholds and kill numbers resolve. Post routing and the pillar ratio set.
4. Operator picks the recognition anchors: `{SUBJECT}`, `{OBJECT}`, `{THRESHOLD}` (face-independent; the operator's taste, not a face). These are choices, not lookups, so they are confirmed in the same pass, not discovered.

After the pass, nothing carries a token except by deliberate choice. No file needs a rebuild. The scaffold was built to resolve, not to be rewritten.

Approval boundary holds: condition-met is eligible, not authorized. After resolution, every send, post, generation, and naming runs only on the operator's explicit go (`V1_BUILD/TRIP_CAMPAIGN_V1.md` status). This is a recommendation, not an authorization.

---

## THE ONE RULE, IN VOICE

Every day, the question is not what to post. It is what room got opened, and whether it traces to this campaign. The posts are the byproduct. The room is the point. The cold-access ladder is the plan for the day no room moved, so the proof leg has a real path, not a hope.

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/TRIP_CAMPAIGN_V1.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/INTAKE_FILLED_AND_LEDGER.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/ACCESS_RECEIPT_PLAN.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/PROOF_DASHBOARD.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md`
- V2 siblings: `TARGET_DISCOVERY_METHOD.md`, `DAY_BY_DAY_RUNBOOK.md`, `ACCESS_RECEIPT_TEMPLATE.md`, `PROOF_DASHBOARD.md`, `THREE_FACTS_BEFORE_ACTION.md`
