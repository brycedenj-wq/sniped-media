# Kingdom of the Sun · Coach Pipeline System (master)

> Built 2026-06-01. Reusable infrastructure, not a 2026 list. It runs every year: reset stages, reload the 16-team field, move every program from invited to fully ready.
>
> **This is invitation-only.** We do not collect signups. We manage 16 invited programs through a confirmation and readiness flow. The tournament lives or dies by this pipeline.

This folder holds:
1. `KOTS_COACH_SYSTEM.md` (this doc) · the stages, the readiness definition, the missing-field list, ownership, how to use both trackers
2. `KOTS_COACH_PIPELINE_OPERATOR.csv` · the full backend tracker (all detail, all 16 teams)
3. `KOTS_COACH_PIPELINE_DAD.csv` · the simple dad-facing version (5 columns, usable on a phone)
4. `KOTS_COACH_COMM_FLOW.md` · the invitation-only communication sequence + templates

---

## 1. The 8 status stages (the spine)

Every team moves through these in order. The status column always shows the **furthest milestone reached**.

| # | Stage | What it means | Done when |
|---|---|---|---|
| 1 | **Invited** | Formal invitation extended | Coach has received the invite (call + written) |
| 2 | **Verbal** | Coach said yes informally | Verbal commitment on the date |
| 3 | **Confirmed** | Commitment in writing | Written confirmation received by the deadline |
| 4 | **Roster received** | Official roster in hand | Players, numbers, grades for program + announcer + site |
| 5 | **Travel info received** | Arrival logistics known | Arrival day, party size, bus/flight |
| 6 | **Hotel info received** | Lodging settled | Where they stay, or hotel-block help resolved |
| 7 | **Media assets received** | Brand assets in | Team logo + team photo (+ headshots if available) for site/program/stream |
| 8 | **Fully ready** | Green across the board | Stages 3 through 7 all complete |

**Fully ready** is the only finish line. A team is not "done" at confirmed. It is done when it is confirmed, rostered, travel-known, hotel-known, and media-in. That gap is exactly what an invitation-only tournament has to manage and a registration form never does.

---

## 2. Ownership (Lane A, all of it)

The coach pipeline is **100% Lane A tournament ops**, owned by dad / the committee / the tournament director. There is no sponsor or media business in this folder.

One thin seam: the **media assets** collected at stage 7 (team logos, photos) feed the website BJ is building. That is the only point of contact, and even there the *ask* comes from the tournament, not from BJ. The site simply consumes what the pipeline collects. No Lane B work lives here.

---

## 3. The two trackers, and when to use each

- **`KOTS_COACH_PIPELINE_DAD.csv`** · 5 columns: team, coach name, phone, status, next action. This is what dad actually works from. Glanceable, phone-friendly, no clutter. He updates status and next action as he talks to coaches.
- **`KOTS_COACH_PIPELINE_OPERATOR.csv`** · the full backend: every contact field, every received flag, dates, owner, notes. This is the source of truth. The dad version is a simplified mirror of it.

Keep the operator file as truth. The dad file is the lightweight surface. When you pick a tool (Sheets / Airtable / Notion), the operator CSV is the import; the dad version becomes a filtered view of the same data.

---

## 4. The 2026 field (10 named, 6 to complete)

| # | School | City / State | Status |
|---|---|---|---|
| 1 | Vanguard (HOST) | Ocala, FL | Invited / host |
| 2 | North Marion | Citra, FL | Invited |
| 3 | Windermere Prep | Windermere, FL | Invited |
| 4 | P.K. Yonge | Gainesville, FL | Invited |
| 5 | Peachtree Ridge | Suwanee, GA | Invited |
| 6 | Viera | Viera, FL | Invited |
| 7 | Tallahassee Godby | Tallahassee, FL | Invited |
| 8 | Wildwood | Wildwood, FL | Invited |
| 9 | Wekiva | Apopka (Orlando), FL | Invited |
| 10 | South Lake | Groveland, FL | Invited |
| 11-16 | TBA | TBA | Invite pending |

All 10 are set to **Invited** as a safe default. Dad should advance any that are already verbal or confirmed. City/state are seeded; coach contacts are blank for dad to fill.

---

## 5. Missing-info list to complete the 16-team field

What we need from dad to close the field and start building the schedule:

1. **Are the final 6 already chosen, or still being decided?**
2. If chosen: the **6 school names + their coach contacts**.
3. If not chosen: the **selection criteria, who decides, and a target date** to lock them.
4. For the 10 named: each **coach name, phone, email**, and the **true status** (are any already confirmed, or all just invited?).
5. The **confirmation deadline** dad wants to set (the date a verbal must become written, so the bracket can be built).
6. Any **declines or replacements** already in motion.

The bracket, the schedule, and the site teams grid all wait on a closed field. This list is the unlock.

---

## 6. How the system reruns each year

1. **Off-season:** reset all statuses to blank, carry forward returning programs as the first invites.
2. **Invite window (summer / early fall):** extend all 16 invites, named teams first, fill the field early before schedules lock.
3. **Confirmation window:** drive verbals to written confirmations by the deadline.
4. **Readiness window (fall to December):** collect rosters, travel, hotel, and media in waves.
5. **Final week:** every team must read Fully Ready. Anything short is the call list.
6. **Post-event:** note which programs to re-invite first next year. Relationships compound.
