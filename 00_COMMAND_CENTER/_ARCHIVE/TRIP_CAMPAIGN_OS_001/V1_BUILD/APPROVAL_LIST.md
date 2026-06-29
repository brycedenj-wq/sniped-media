# APPROVAL LIST · what needs the operator's explicit go before it happens

Every action below is gated. Nothing on this list runs until the operator says go. This holds the standing approval boundary: condition-met is eligible, not authorized (`OFFER_PROTOTYPE.md` no-payment-rails-without-a-go; `INTAKE_FILLED_AND_LEDGER.md` field 8). No spend, no generation, no posting, no naming, no crown until the matching item is unblocked.

Constraints: zero spend, zero generation, zero posting, no naming, no crown, no em-dashes, no hype.

---

## (a) Facts to confirm

These unblock the whole build. The first three are the only real blanks; the fourth is a routing decision.

- THE THREE MISSING FACTS. What: [DESTINATION], [DATES], [CURRENT AUDIENCE] (platforms, rough size, how warm). Why gated: no mined file could answer them, and inventing them would falsify the targets, the deadline, and every numeric threshold (`INTAKE_FILLED_AND_LEDGER.md` fields 1, 2, 6). What unblocks: the operator answers the three. Resolving [DESTINATION] also resolves the named targets [TARGET NAME]; resolving [CURRENT AUDIENCE] resolves the dashboard tier-2-to-4 thresholds and their kill thresholds.
- THE CONCRETE OCCASION (optional, sharpens purpose). What: is there a real event, client, scout, or relationship behind the trip, or is it operator-chosen? Why gated: the campaign-level purpose is inferred; the concrete occasion is a one-line fact only the operator has (`INTAKE_FILLED_AND_LEDGER.md` field 3). What unblocks: one line from the operator.
- THE BASEPLATE-VS-CAMPAIGN-UNIVERSE FORK. What: confirm the trip sells Campaign Universe Buildout (the V1 default), not the BASEPLATE B2B staffing dossier at $2,500 to $4,000. Why gated: this is a real conflict surfaced, not auto-resolved; the two lanes have different offers, targets, and prices (`INTAKE_FILLED_AND_LEDGER.md` ledger A1; `TRIP_CAMPAIGN_V1.md` BASEPLATE fork). What unblocks: the operator confirms Campaign Universe Buildout, or says redirect to BASEPLATE (which swaps the offer / target / price layer and leaves the engine intact).
- THE BANNER POSTURE (depends on naming, see (e)). What: whether the trip runs under BASEPLATE, a personal identity, or a fresh placeholder. Why gated: the banner is UNKNOWN and the no-naming rule holds regardless (`INTAKE_FILLED_AND_LEDGER.md` field 7). What unblocks: the operator picks the posture; until then V1 runs under a neutral placeholder.

---

## (b) Any spend

- GENERATION CREDITS. What: any image or motion generation (Higgsfield, Soul, etc.) for the hero asset set or any content. Why gated: zero-spend default, no standing cap (`INTAKE_FILLED_AND_LEDGER.md` field 8; `OFFER_PROTOTYPE.md` no-spend). What unblocks: the operator's explicit go and, if wanted, a stated credit or dollar cap.
- OUTREACH TOOLING. What: any paid CRM, outreach platform, or sending tool. Why gated: same zero-spend posture; whether a tool is already live is UNKNOWN (`INTAKE_FILLED_AND_LEDGER.md` field 8). What unblocks: the operator's go plus a named tool, or confirmation the local CSV is enough for now.

---

## (c) Any outreach send

- FIRST-TOUCH DMs AND COLD EMAILS. What: sending any of the ten angles (`V1_BUILD/OUTREACH_10.md`) to any target. Why gated: no send before the written one-page ICP exists, the target is fit-screened, and the copy passes the gate (single CTA, under 80 words, no link, plain text, outcome-first, no hype, no em-dashes), and even then only on the operator's go (`v0_parts/strategy.md` §3.1, §3.3; `OFFER_PROTOTYPE.md` no-payment-without-go). What unblocks: ICP written, target fit-screened FIT, copy gate passed, operator says send. A row is marked sent in `outreach.csv` only after the go.
- SAME-DAY VALUE FOLLOW-UPS. What: the same-day micro-offer follow-up to a real-world contact (cold-access ladder rung 3). Why gated: it is still an outbound send. What unblocks: operator go (can be a standing per-trip go for warm same-day follow-ups if the operator grants it explicitly).

---

## (d) Any posting

- PUBLISHING ANY ASSET. What: posting any still, motion, or script to any platform. Why gated: zero-posting default; reach proof only exists after approved publishing, and the audience baseline is UNKNOWN (`INTAKE_FILLED_AND_LEDGER.md` field 6; `OFFER_PROTOTYPE.md` no-posting). What unblocks: operator go per asset (or a stated per-pillar standing go). A row is marked posted in `content.csv` only after the go.

---

## (e) Any naming

- ANY PUBLIC NAME OR BANNER. What: naming the offer, the trip banner, a product, or the construct publicly. Why gated: no-naming rule is in force; the banner posture is UNKNOWN and BASEPLATE is only a 30-day test wrapper, not a permanent lock (`INTAKE_FILLED_AND_LEDGER.md` field 7; `BASEPLATE_CANONICAL_STATEMENT.md`). What unblocks: the operator picks the banner posture and approves the specific name. Until then, placeholders only.

---

## (f) Any pixel render (W5)

- ANY HERO ASSET OR CONTENT FRAME. What: rendering the scoped hero asset set or any pixel content. Why gated: it is generation spend (see (b)) and it must pass the vision-reject gate with no self-crown before it counts (`sections/ops.md` §13.2, W5; `PROOF_DASHBOARD.md` content.csv vision_reject_pass). What unblocks: operator go on the spend, then each frame logs a vision-reject pass (pass / fail), no self-crown. A failed frame does not ship.

---

## The single next move

The operator answers the three missing facts ([DESTINATION], [DATES], [CURRENT AUDIENCE]) and confirms the Campaign-Universe-vs-BASEPLATE fork. That one reply turns every UNKNOWN concrete and unblocks the build sequence. Everything else stays gated until its matching item above is unblocked.

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/INTAKE_FILLED_AND_LEDGER.md` fields 1, 2, 3, 6, 7, 8; ledger A1
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md` (no spend / no posting / no payment without go)
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/v0_parts/strategy.md` §3.1, §3.3
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/sections/ops.md` §13.2 (W5)
- `00_COMMAND_CENTER/BASEPLATE_CANONICAL_STATEMENT.md`
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/TRIP_CAMPAIGN_V1.md` (BASEPLATE fork)
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V1_BUILD/PROOF_DASHBOARD.md` (content.csv vision-reject)
