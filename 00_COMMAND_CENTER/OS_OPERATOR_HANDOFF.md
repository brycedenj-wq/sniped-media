# OPERATOR HANDOFF , PROOF CELL 001 (2026-06-04)

> The machine is paused, documented, and ready for your next manual action. Nothing is hosted, shared, generated, named, or strategized. This is the one document you need.

## 1. CURRENT PROOF-CELL STATUS
- **Proof Cell 001 = BUILT and PARKED.** A certified, gated, reusable owned-character asset stack + a private test package + a deployment-ready (not deployed) form for Rails A (method) and C (print).
- **Spend this phase: $0.** No new generation. No posting. No domain. No account. No DMs. No public name. No real identity exposed. No rail crowned.
- **Name: PENDING.** Placeholder `ACHROMAH` (whois-clear, brand checklist NOT done). Internal codenames: character `AXIS`, world `MERIDIAN-HOUSE`.
- **Clock not started.** It is NOT validation until you share the link with real people.

## 2. ALL ARTIFACT PATHS (under `00_COMMAND_CENTER/`)
- Certified assets: `campaign_house/axis_meridian_motion_001/06_approved/axis_hero_v2_marked.png` + `axis_motion_v1.mp4`
- Architecture + cell: `OS_OPERATING_ARCHITECTURE_v1.md` · `OS_PROOFCELL_001.md` · `OS_PROOFCELL_001_PACKAGE.md`
- Form (deployable site): `proofcell/form/site/index.html` + `site/assets/{hero.png,loop.mp4}` + `site/vercel.json`
- Form config: `proofcell/form/netlify.toml`
- Form specs: `proofcell/form/TALLY_SPEC.md` · `DEPLOY_NOTE.md`
- Checklists: `proofcell/form/SHARE_CHECKLIST.md` · `PRIVACY_CHECKLIST.md`
- Proof tracking: `proofcell/form/RESPONSES.csv` (empty template) · `PROOF_LOOP.md`
- Scripts: `proofcell/form/os_form_ingest.py` · `os_form_score.py`
- This handoff: `OS_OPERATOR_HANDOFF.md`

## 3. SAFE TO OPEN LOCALLY (no risk)
- `file://.../proofcell/form/site/index.html` , renders the form + asset pair in your browser. Collects nothing (placeholder endpoint). Private.
- Any `.md` doc, `RESPONSES.csv`, the certified PNG/MP4. All read-only previews.

## 4. SAFE TO MANUALLY WIRE (your account, your call)
- Rebuild the form in Tally (per `TALLY_SPEC.md`) , gives a private link.
- OR add your own Formspree endpoint to `site/index.html` and drop `site/` on Netlify/Vercel.
- Run `os_form_ingest.py` + `os_form_score.py` locally on any CSV export.

## 5. NOT ALLOWED YET (blocked until you explicitly decide)
- Buying a domain · finalizing the public name · ANY posting/ads/distribution · fresh generation (new still ~2cr / clip ~18cr) · sending DMs · anything touching your real name, employer, SNIPED, or personal accounts.

## 6. EXACT STEPS , TALLY VERSION (recommended, ~2 min)
1. tally.so → New form. Title: `ACHROMAH` (no real name).
2. Add a text/header block: paste the header copy from `TALLY_SPEC.md`.
3. Add Field 1 , Checkbox: `Send me the breakdown of how this consistent character system was built.` (not required).
4. Add Field 2 , Checkbox: `Tell me if the first frame becomes available as a limited print.` (not required).
5. Add Field 3 , Email: label `email` (REQUIRED).
6. Add Field 4 , Short text: `what do you make? (optional)` (not required).
7. Add Field 5 , Hidden field: `source`, default `private_link`.
8. Submit button text: `Get the first frames`. Confirmation: "Got it. You will get one note when there is something worth seeing. No spam."
9. Settings: no custom domain; notifications to a fresh alias inbox; free tier; no real-name workspace.
10. Get the private share link. STOP. Do not share until you run the checklists (Section 10/11).

## 7. EXACT STEPS , STATIC FORMSPREE VERSION
1. Create a Formspree (or Basin) form in YOUR account → copy the endpoint URL.
2. Open `proofcell/form/site/index.html`, replace `action="REPLACE_WITH_YOUR_FORM_ENDPOINT"` with that URL. Save. (Only edit needed.)
3. Host `site/`: drag the `site/` folder onto app.netlify.com/drop, OR run `vercel deploy` inside `site/`. Use the auto subdomain. No custom domain.
4. Test-submit yourself once → confirm it lands in Formspree → delete that test row.

## 8. HOW TO EXPORT RESPONSES
- Tally: form → Submissions → Export → CSV.
- Formspree: form → Submissions → Export CSV.
- Save the CSV anywhere (e.g. `~/Downloads/export.csv`).

## 9. HOW TO INGEST + SCORE
```
cd 00_COMMAND_CENTER/proofcell/form
python3 os_form_ingest.py ~/Downloads/export.csv     # appends to RESPONSES.csv (dedup by email; handles Tally OR Formspree)
python3 os_form_score.py                              # writes SCORE.md (A / C / both / source / intent + verdict)
```

## 10. KEEP / KILL / SCALE
| signal | KILL | KEEP | SCALE |
|---|---|---|---|
| Rail A (method) | 0 in 14 days of sharing | any genuine signup on $0 in 7 days | 25+ → build the method product |
| Rail C (print) | 0 in 14 days | any print-interest signup | 300 → open a capped print run (validation-before-manufacture gate) |
| intent | , | qualitative fit read | one buyer-type cluster → tighten positioning |
Rule: not validation until shared. Do not crown a rail on early signal.

## 11. APPROVAL CHOICES AVAILABLE NEXT (pick when ready; each is one go)
- A. Wire + privately share the form (Tally or static) , starts the real proof loop for A + C.
- B. Authorize fresh generation (new still ~2cr / clip ~18cr) , only if you want net-new assets.
- C. Approve posting (Rail B media) , needs your go; not built yet.
- D. Run the brand checklist to promote a name from pending → real.
- E. Hold , leave everything parked.

## 12. WHAT THE OS DOES AFTER YOU PROVIDE A CSV EXPORT
1. Ingest it (`os_form_ingest.py`) → normalized rows in `RESPONSES.csv`.
2. Score it (`os_form_score.py`) → A / C / both counts, source attribution, intent patterns.
3. Apply keep/kill/scale (Section 10) and report the verdict per rail , with confidence labels, no rail crowned.
4. If a rail hits SCALE, propose the next bounded build for THAT rail (e.g., method-product draft, or the print-run gate) , and stop at your approval line again.
5. Update the proof-loop dashboard + current-state. No strategy rerun unless you ask.

## STATUS: PAUSED. Ready for your next manual action.
