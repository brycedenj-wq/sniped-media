# TARGET DISCOVERY METHOD · destination-agnostic, runnable the day `{DEST}` lands

A repeatable procedure to find and screen targets for ANY `{DEST}`. It does not name a place, a person, or a brand. It is the machine that produces a target roster the moment the operator drops `{DEST}` (and `{DATES}`, which bounds the reachable window). It upgrades V1's fit screen and warmest-first sequence (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §2) into a runnable sourcing procedure.

The job this serves: open ONE real room and prove the 10k Campaign Universe Buildout offer. This method finds the person whose room is worth opening. Posts are the byproduct (`OFFER_PROTOTYPE.md` proof section).

Constraints in force: zero spend, zero generation, zero posting, no naming (placeholders only), no crown, no em-dashes, no hype. Face-independent. Nothing sends without the operator (`V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` field 9).

---

## STEP 0 · Inputs this method needs

- `{DEST}` (required to run): sets the geography and every sourcing channel.
- `{DATES}` (required to screen reachability): sets the event-calendar window and the reachable-in-window line of the fit screen.
- `{AUDIENCE}` (optional, improves warmth ranking): the already-warm-in-location bucket reads off the operator's current audience graph.

Until `{DEST}` lands, this file is the procedure, not a roster. Do not invent a place to run it early.

---

## STEP 1 · Define the geography and the scenes the buyer type gathers in

The buyer type is fixed (it does not depend on `{DEST}`): an artist or concert with a moment coming, a brand with a launch, a founder with a world and no machine, in-lane, can-say-yes, cares about the outcome (`OFFER_PROTOTYPE.md` who-this-serves). What changes per `{DEST}` is WHERE that type physically gathers.

For the dropped `{DEST}`, map these scene types (the rooms the buyer type is already in):

- MUSIC / TOUR scenes: venues, green rooms, listening sessions, label nights, festival side-events in the `{DATES}` window.
- LAUNCH / BRAND scenes: pop-ups, product-drop events, showrooms, demo days, market activations.
- FOUNDER / CREATOR scenes: coworking hubs, founder dinners, creator houses, accelerator demo nights, local studio collectives.
- VENUE / GATEKEEPER scenes: the physical places (a venue, a gallery, a studio, a club) whose operator can grant `capture_granted` access or refer a `{TARGET}`.

Output of Step 1: a short list of named scenes in `{DEST}` (each becomes a candidate `{THRESHOLD}` and a cold-access-ladder rung-1 location).

---

## STEP 2 · The cliche-to-avoid pass (per `{DEST}`)

Before sourcing, list the obvious, generic, postcard version of `{DEST}` and rule it out of the work. The Only-Them test applies to place as well as person: if the angle could be any tourist's, it is cut (`OFFER_PROTOTYPE.md` why-this-beats-an-agency). This protects recognition and keeps `{SUBJECT}` / `{OBJECT}` / `{THRESHOLD}` specific to the real scene, not the brochure.

---

## STEP 3 · Candidate-sourcing channels (run all that apply for `{DEST}`)

Each channel produces raw candidates. Log every candidate to the roster CSV before screening; screen in Step 4.

1. GEOTAGS. The `{DEST}` location tags on the operator's platforms; pull accounts posting recent in-lane work from the place.
2. LOCAL HASHTAGS. Scene-specific tags for `{DEST}` (music, launch, founder, venue tags), not generic city tags.
3. EVENT CALENDARS IN THE `{DATES}` WINDOW. Venue listings, festival schedules, launch-event and demo-day calendars that fall inside `{DATES}`. An event in the window is a `{THEIR_MOMENT}` candidate.
4. FOUNDER / CREATOR COMMUNITIES. Accelerator cohorts, creator houses, studio collectives, founder dinners local to `{DEST}`.
5. VENUE ROSTERS. Who is booked, showing, or launching at the `{DEST}` venues during `{DATES}`. The booking IS the trigger moment.
6. MUTUAL-FOLLOW GRAPH. Accounts in `{DEST}` who already share follows with the operator's `{AUDIENCE}` (the warmest cold targets).
7. WARM-NODE REFERRALS. Ask the operator's existing warm contacts: who do you know in `{DEST}` with a moment coming. A referral path is the highest-warmth source.

Output of Step 3: a raw candidate list, every row tagged with the channel it came from.

---

## STEP 4 · The fit screen (run on every candidate before it enters the roster)

Five gates, all from V1's fit screen plus the offer's client-fit fields (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §2; `OFFER_PROTOTYPE.md` client-fit screen). Each candidate scores FIT, HOLD, or PASS.

| Gate | Question | Fail = |
|---|---|---|
| IN-LANE | Does the machine actually serve `{THEIR_THING}` (a real input with taste behind it)? | PASS |
| CAN SAY YES | Decision capacity, or can refer one move to a decision-maker? | HOLD if referrer-only, PASS if neither |
| CARES ABOUT OUTCOME | Low self-orientation, wants the moment built, not cheap content? | PASS (price-shopper) |
| REACHABLE IN WINDOW | Physically reachable in `{DEST}` during `{DATES}`? | HOLD (off-window but warm) or PASS |
| HAS A TRIGGER MOMENT | Is there a `{THEIR_MOMENT}` (a launch, drop, tour, show) on the calendar? | HOLD if none yet, PASS if no plausible moment |

Verdict rule: FIT = all five pass. HOLD = one or two recoverable gaps (off-window, referrer-only, moment not yet dated). PASS = in-lane fails, or price-shopper, or unreachable with no warm path. A PASS is removed before the trip, never discounted during it.

---

## STEP 5 · Per-target capture (fill these for every FIT and HOLD)

For each surviving target, capture the fields that make the outreach real and Only-Them:

- ONLY-THEM FACT: one fact true for this target and no one else, on this trip, in this place. This is what makes the reason-to-meet impossible to copy-paste (`OFFER_PROTOTYPE.md` Only-Them test).
- `{THEIR_THING}`: their real input (the launch, drop, tour, world, idea).
- `{THEIR_MOMENT}`: the dated moment that creates the trigger, with its date inside `{DATES}` where possible.
- The value-first micro-offer hook: the one specific free piece worth building for `{THEIR_THING}` (a teardown of where their rollout leaves reach on the table, a frame for `{THEIR_MOMENT}`, a single biggest-gap map). The full micro-offer is built only on the operator's go.

No Only-Them fact, no FIT. A target with no fact specific to them is a generic contact, not a screened target.

---

## STEP 6 · Warmest-first ranking

Rank the FIT and HOLD targets so the warm rooms get worked first and the cold-access ladder is spent only when warm rooms do not move (`V1_BUILD/ACCESS_RECEIPT_PLAN.md` §2). Rank order:

1. ALREADY-WARM IN-LOCATION: already engaging the operator's `{AUDIENCE}`, and in `{DEST}` during `{DATES}`. Cheapest rooms, touch first.
2. PRE-WARMABLE: reachable for one to two weeks of real pre-trip engagement before any cold touch.
3. COLD-BUT-FIT: fit-screened, no warmth yet, reached with an Only-Them reason-to-meet.

Within each tier, rank by trigger-moment proximity to `{DATES}` (a `{THEIR_MOMENT}` inside the window outranks one outside it).

---

## STEP 7 · Output, the target roster CSV

One file, `target_roster.csv`, created the day `{DEST}` lands. Do not pre-populate with invented rows. Exact column schema:

```
target_id,name_or_placeholder,channel_source,scene_type,cohort,decision_capacity,in_lane,can_say_yes,cares_outcome,reachable_in_window,has_trigger_moment,fit_verdict,warmth_tier,only_them_fact,their_thing,their_moment,micro_offer_hook,outreach_status
```

- target_id: T001, T002, ...
- name_or_placeholder: the real name (logged locally only, never posted) or `{TARGET}` placeholder until real.
- channel_source: geotag | local_hashtag | event_calendar | founder_community | venue_roster | mutual_follow | warm_referral
- scene_type: music_tour | launch_brand | founder_creator | venue_gatekeeper
- cohort: moment_holder | under_built | venue_scene_gatekeeper (mirrors the dashboard cohort field, `PROOF_DASHBOARD.md` rooms.csv)
- decision_capacity: decision_maker | referrer_only | unknown
- in_lane / can_say_yes / cares_outcome / reachable_in_window / has_trigger_moment: yes | no | hold
- fit_verdict: fit | hold | pass
- warmth_tier: already_warm | pre_warmable | cold_but_fit
- only_them_fact: one line, the fact true only for them
- their_thing: their real input
- their_moment: the dated trigger moment (date inside `{DATES}` where possible)
- micro_offer_hook: the one specific value-first piece worth building for them
- outreach_status: not_started | pre_warming | touched | replied | room_opened (links to `PROOF_DASHBOARD.md` outreach.csv and rooms.csv)

A row is roster-ready only when fit_verdict is fit or hold AND only_them_fact, their_thing, and a micro_offer_hook are all filled. A row missing the Only-Them fact is a contact, not a screened target.

---

## HOW TO RUN IT, THE DAY `{DEST}` LANDS

1. Run Step 1 (scenes) and Step 2 (cliche pass) for `{DEST}`.
2. Run Step 3 across every applicable channel, logging raw candidates.
3. Run Step 4 fit screen on each; drop PASS.
4. Run Step 5 capture on every FIT and HOLD.
5. Run Step 6 ranking.
6. Write `target_roster.csv` with the Step 7 schema.
7. Hand the warmest-first roster to `DAY_BY_DAY_RUNBOOK.md` D-14 (pre-warm window). Nothing sends without the operator.

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/ACCESS_RECEIPT_PLAN.md` §1, §2, §3
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md` who-this-serves, client-fit screen, Only-Them test
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` fields 5, 9
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/PROOF_DASHBOARD.md` rooms.csv, outreach.csv schema
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/TRIP_CAMPAIGN_V2.md` variable key, propagation table
