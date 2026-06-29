# APPROVAL LIST · the exact gate before any action

Nothing in V3 acts on the world without an explicit operator go. The campaign is built and ready to run, but condition-met is eligible, not authorized (`V2_BUILD/TRIP_CAMPAIGN_V2.md` Part C approval boundary). This file is the gate: six things that are blocked by default, why each is blocked, and what unblocks it. Approval lives at the boundary, not in the middle of a run (`AGENTS.md` orchestration law 4).

Constraints in force across all of V3: zero spend, zero generation, zero posting, no naming (real names logged locally only, never invented), no crown, no em-dashes, no hype. Face-independent. The access receipt is the load-bearing proof (`TRIP_CAMPAIGN_V3.md`; `OFFER_PROTOTYPE.md`).

---

## (a) THE TARGET ROSTER

- What it is: the named target list that `LA_TARGET_DISCOVERY_ROSTER_METHOD.md` produces, `la_target_roster.csv`, with real LA people, brands, and venues from live discovery.
- Why gated: no cold contact happens until the operator approves the named list. The method finds and screens candidates; it does not authorize reaching out to them. A screened roster is a recommendation, not a permission to contact. No named targets are invented; named entities need operator confirmation from real discovery.
- What unblocks it: the operator reviews the warmest-first roster and approves which rows are live. Only approved rows move to outreach (gate b). An unapproved row stays research-only.

## (b) ANY SEND (DM OR EMAIL)

- What it is: any outbound touch, a DM or a cold email, including the value-first micro-offer when it is delivered to a target.
- Why gated: a send is an action in the world against a real person. The micro-offer can be built as a draft, but it is not delivered without a go. No outreach.csv row is marked sent without the operator's go (`PROOF_DASHBOARD.md` outreach.csv sent_approved).
- What unblocks it: the operator approves the specific touch (target, angle, copy under 80 words for a first touch). Approval is per send or per approved batch, never a standing blanket. The send happens only after the roster (gate a) is approved.

## (c) ANY POSTING

- What it is: publishing any asset to any platform, including any of the five pillars and the post-sprint honest-receipt post.
- Why gated: the audience is unknown and the play is access-first, not post-and-hope; posting is the documentation layer, not the engine, and it is approval-gated so nothing public ships by default (`TRIP_CAMPAIGN_V3.md` §A.3). The pillar ratio and post routing also stay unset until `{AUDIENCE}` drops.
- What unblocks it: the operator approves the specific asset and where it posts. No content.csv row is marked posted without the go (`PROOF_DASHBOARD.md` content.csv posted_approved).

## (d) ANY SPEND

- What it is: any cost, generation credits, tools, subscriptions, ads, anything that draws money.
- Why gated: V3 runs at zero spend until the operator approves otherwise. Discovery, screening, drafting, and dashboard logging are all zero-spend; anything that costs money is blocked by default (`TRIP_CAMPAIGN_V3.md` constraints).
- What unblocks it: the operator explicitly approves the specific spend with an amount. No standing budget; each spend is its own go.

## (e) ANY NAMING

- What it is: writing any real named person, brand, or venue into any V3 artifact, or naming the offer as a crowned product.
- Why gated: no fabricated named targets, ever. Categories and types are used until the operator confirms real names from live discovery (`LA_TARGET_CATEGORIES_25.md` uses types only). Real names, when confirmed, are logged locally only, never posted. The offer is not named as proven until the proof exists (no crown, `OFFER_PROTOTYPE.md` what-must-not-be-promised).
- What unblocks it: the operator supplies and confirms the real names from discovery (which also satisfies gate a for the roster). Naming the offer as proven unblocks only when a real opened room with a valid receipt exists.

## (f) ANY PIXEL RENDER (W5)

- What it is: generating any image or motion asset, the W5 pixel-render stage.
- Why gated: zero generation until the operator approves it, and any pixel render also draws spend (gate d). A render is not the proof here; the access receipt is. Pixels are downstream of an opened room, not a substitute for one (`TRIP_CAMPAIGN_V3.md` §A.3; `PROOF_DASHBOARD.md` tier 3).
- What unblocks it: the operator approves the specific render and its spend. If pixels ship, each frame logs a vision-reject pass, no self-crown (`os-vision-reject-gate`; `PROOF_DASHBOARD.md` content.csv vision_reject_pass).

---

## THE SINGLE NEXT MOVE

Run `LA_TARGET_DISCOVERY_ROSTER_METHOD.md` today as read-only research, zero spend and zero sends, to produce a draft warmest-first `la_target_roster.csv` of screened LA target candidates (types and placeholders, no invented names). Then bring that roster to the operator for gate (a) approval. Nothing else moves until that list is approved.

---

## SOURCES CITED
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V2_BUILD/TRIP_CAMPAIGN_V2.md` Part C approval boundary
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/OFFER_PROTOTYPE.md` what-must-not-be-promised, no-crown, no-spend
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/TRIP_CAMPAIGN_V3.md` constraints, access-first documentation role
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/LA_TARGET_DISCOVERY_ROSTER_METHOD.md` roster, sends, naming
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/LA_TARGET_CATEGORIES_25.md` types-not-named-entities
- `00_COMMAND_CENTER/TRIP_CAMPAIGN_OS_001/V3_BUILD/PROOF_DASHBOARD.md` sent_approved, posted_approved, vision_reject_pass
- `AGENTS.md` orchestration law 4 (approval at the boundary)
