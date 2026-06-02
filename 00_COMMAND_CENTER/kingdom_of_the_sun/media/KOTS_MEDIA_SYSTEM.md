# Kingdom of the Sun · Media Operations System (master)

> Built 2026-06-01. The 2026 media system for the tournament. Reusable infrastructure, not a one-year plan. Runs every December: reset, capture, deliver, archive, repeat.
>
> **Framing (locked):** Kingdom owns the tournament media system. NFHS owns the live-stream rail. BJ may own official photo/media execution if the committee approves. SNIPED methods can inform capture and edit quality; SNIPED strategy does not enter this domain.

This folder holds:
1. `KOTS_MEDIA_SYSTEM.md` (this doc) · the five rails, ownership, folders, naming, gating
2. `KOTS_GAME_WEEK_CALENDAR.md` · the Dec 27-31 content calendar
3. `KOTS_SHOT_LIST.md` · the full tournament coverage shot list
4. `KOTS_GALLERY_DELIVERY.md` · delivery structure for coaches, teams, families, sponsors, archive
5. `KOTS_SPONSOR_MEDIA_DELIVERABLES.md` · what media each sponsor tier receives
6. `KOTS_POST_EVENT_RECAP.md` · the post-event recap package
7. `KOTS_LANE_B_ROLE.md` · BJ's media/builder role (internal, not a public offer)
8. `KOTS_MEDIA_TRACKER.csv` · the reusable asset + deliverable tracker

---

## 1. The five rails (clear separation)

Media is not one bucket. Five rails, each with its own owner, purpose, source, and destination. They must not blur.

| Rail | Owner | What it is | Source | Goes to |
|---|---|---|---|---|
| **1. NFHS Live Stream** | **NFHS Network** | Live broadcast of every game | NFHS Pixellot cameras (already in the gym) | Watch link on the site; promoted on social |
| **2. Official Photography** | Kingdom (executed by BJ if approved) | Stills: action, portraits, awards, sponsors, legacy, BTS | On-site photographer | Galleries, social, sponsor deliverables, archive |
| **3. Social Content** | Kingdom (tournament accounts) | Real-time + recap posts and graphics | Photography + NFHS clips + score graphics | IG, X, Facebook |
| **4. Sponsor Deliverables** | Kingdom (fulfillment) | Post-event proof assets per sponsor | Photography + broadcast + social | Each sponsor, by tier |
| **5. Historical Archive** | Kingdom | The year's permanent record | Best of all rails | Site history, next-year promo, the legacy layer |

**The line that matters:** the tournament does **not** produce or own the live stream. NFHS does. We integrate it (embed the link, promote it), we do not build it. Everything else (photo, social, sponsor, archive) is Kingdom-owned media the tournament controls.

---

## 2. Ownership & lane discipline

- **Kingdom owns the system.** The calendar, the accounts, the galleries, the archive, the sponsor fulfillment.
- **NFHS owns the stream rail.** Selling anything on the broadcast is a separate, gated question (NFHS usually controls its own ad inventory; confirm before promising sponsors broadcast placement).
- **BJ (Lane B) may own execution** of photography + the website/digital + the content system build, **if the committee approves the role.** See `KOTS_LANE_B_ROLE.md`. Internal only, not a public offer.
- **SNIPED is not in this domain.** Capture/cull/edit *quality discipline* can be borrowed quietly (shoot to a plan, back up same-day, deliver clean). SNIPED's *strategy, positioning, pricing, and offers* do not appear here. This is tournament media, native to the Kingdom.

---

## 3. Folder structure (reusable, year-based)

```
KOTS_MEDIA/2026/
  00_INBOX_RAW/            card offloads, by day + card (never edit here)
  01_SELECTS/             culled keepers
  02_EDITED/              final edits, by category
      game_action/
      portraits_teams/
      awards_ceremony/
      sponsors/
      legacy_details/
      behind_the_scenes/
  03_DELIVERY/            export-ready, by audience
      coaches_teams/<team>/
      families/
      sponsors/<sponsor>/
      social_ready/
  04_ARCHIVE_2026/        the year's permanent set (champions, all-tournament, best-of) -> feeds legacy/
  05_GRAPHICS/            score tiles, bracket art, templates
```

Each year duplicates the `2026/` tree as `2027/`, etc. The archive folder is the bridge to `../legacy/`.

---

## 4. Naming conventions (locked)

`KOTS2026_[RAIL]_[MMDD]_[subject]_[seq].ext`

- **RAIL:** PHOTO · SOCIAL · SPONSOR · ARCHIVE · GFX
- Examples:
  - `KOTS2026_PHOTO_1228_Vanguard-v-NorthMarion_0042.jpg`
  - `KOTS2026_SPONSOR_1230_AdventHealth-signage_003.jpg`
  - `KOTS2026_ARCHIVE_1231_Champion-trophy_011.jpg`
  - `KOTS2026_GFX_1229_score-tile_QF2.png`
- Teams use the short school name (no mascot). Sponsors use the tracker's sponsor key. Keep sequence zero-padded.

---

## 5. Gating map: build now vs gated

**Build now (no gate, all infrastructure):**
- This whole system, the calendar, the shot list, the gallery structure, naming, trackers, templates, the deliverables map, the recap spec.
- Social account setup and content templates.
- The archive structure and the legacy tie-in.

**Gated on dad / committee approval:**
- **BJ's official media role + pay structure** (the Lane B comp). Gated, internal only.
- **Selling photos to families** (monetization of the family gallery). A business decision, not assumed.
- **Selling anything on the NFHS broadcast** (confirm NFHS allows it first).
- **Putting the official Crown on deliverables** (brand is concept until the committee blesses it; until then deliverables use the heritage mark or text).
- **Any sponsor-facing send** (deliverables go out under tournament authority).

**The rule:** the entire media machine can be built, staffed in plan, and templated now. What is gated is BJ getting paid for it, selling anything, and anything that leaves under the tournament's name.
