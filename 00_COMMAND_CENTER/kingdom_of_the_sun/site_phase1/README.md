# Kingdom of the Sun · Phase 1 site (credibility / recruitment)

Static, data-driven, mobile-first. Built to grow into Phase 2 and Phase 3 without a rewrite.

## Structure
- `index.html` · semantic sections, empty containers filled by the render layer.
- `assets/styles.css` · mobile-first, design tokens = locked Crown identity (navy/gold/orange/cream).
- `assets/app.js` · component-style render functions. Reads `window.SITE`, hard-codes nothing.
- `config/site-data.js` · the SINGLE content source. Edit this to change the site.
- `assets/` · crown emblem (concept), official logo (heritage, untouched), Haley founder photo, favicon.

## How to update content
Edit `config/site-data.js` only. Teams, schedule, history, sponsors, contact all live there.

## Phase upgrade points (marked in code with PHASE 2 / PHASE 3 comments)
- PHASE 2: split `site-data.js` into JSON files and `fetch()` them; add real 16-team field, static bracket, team/player pages, media gallery, sponsor pages.
- PHASE 3: connect `teams` / `schedule` / a `games` table to Supabase (Postgres + realtime) or a Google Sheet; live bracket + scores; protected `/admin` for score entry; bracket auto-advancement; recaps; uploads; social-graphic output. The render layer stays; only the data source changes.

## Placeholders (nothing invented)
Exact 2026 dates, dad phone/email, entry fee, full team list, domain, registration form link, photo credit, site credit. All marked in `config/site-data.js`.

## To deploy (NOT done yet, awaiting approval)
1. Fill the placeholders in `config/site-data.js` (at minimum: registration target + photo/site credit).
2. Decide domain (real domain vs free temp URL).
3. Host the folder on Netlify or Vercel (drag-and-drop the folder, or connect a repo). Static, no build step.
4. Point the printed QR card at the resulting URL.

## Not built yet (by design)
Live scoring, admin login, database, accounts, uploads, social-graphic generation, interactive real-time bracket.
