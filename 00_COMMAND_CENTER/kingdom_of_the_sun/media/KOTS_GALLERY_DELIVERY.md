# Kingdom of the Sun · Gallery & Delivery Structure

> Who gets what, where it lives, and how it is named. Owner: Kingdom (executed by BJ if approved). Tool-agnostic; recommended platform below.

---

## Audiences and what each receives

| Audience | Gets | Access | Notes |
|---|---|---|---|
| **Coaches / teams** | Their team's action + team frames, by game | Per-team gallery link | The recruiting-useful set; coaches share with players |
| **Players / families** | Individual player frames | Searchable / by team gallery | Family monetization (prints/downloads) is a **gated** business decision, see system doc |
| **Sponsors** | Their activation proof set | Per-sponsor folder/link | Ties to `KOTS_SPONSOR_MEDIA_DELIVERABLES.md` |
| **Tournament archive** | The permanent best-of: champions, MVP, all-tournament, legacy | Internal `04_ARCHIVE_2026/` | Feeds the site + next-year promo + `../legacy/` |
| **Social** | Export-ready, sized per platform | `03_DELIVERY/social_ready/` | Pulled by the social rail during the week |

---

## Delivery folder tree (under `03_DELIVERY/`)

```
03_DELIVERY/
  coaches_teams/
    Vanguard/           game1/ game2/ ... + team_frames/
    North-Marion/
    ... (one per program)
  families/             by team, individual player frames
  sponsors/
    <sponsor-key>/      signage/ contest/ social/ recap/
  social_ready/         sized exports, dated
```

---

## Naming inside delivery
- Team galleries: `KOTS2026_PHOTO_[MMDD]_[Team]-v-[Team]_[seq].jpg`
- Family/player frames: `KOTS2026_PHOTO_[Team]_[jersey##]_[seq].jpg` (jersey number aids family search)
- Sponsor sets: `KOTS2026_SPONSOR_[MMDD]_[sponsor-key]-[asset]_[seq].jpg`

---

## Platform recommendation
- **A gallery platform** (Pixieset, SmugMug, or a simple Google Drive structure) for coach/team/family delivery: link-per-team, downloadable, optional password.
- **The site** (`/champions`, future `/gallery`) hosts the curated public best-of, not the full take.
- Keep the full raw take internal in `00_INBOX_RAW/`; only selects and edits leave.

---

## Delivery timing
- **During week:** social_ready exports flow nightly.
- **48-72 hrs post-event:** coach/team galleries live (the recruiting window matters, deliver fast).
- **1 week post:** sponsor proof sets delivered with the recap.
- **2 weeks post:** archive closed out, site updated, family galleries posted (if monetization is approved, pricing set then).

---

## Reusable, year over year
This structure is identical each year. Duplicate the tree, swap the year, reload the team list from the coach pipeline (`../coaches/`). The sponsor keys come from the sponsor tracker (`../sponsorship/`). Nothing is rebuilt; it is reloaded.
