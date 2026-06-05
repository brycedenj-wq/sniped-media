# OS IMMEDIATE TOOL TESTS , run today, safe local/internal artifacts only
> Not just docs. These routes were exercised now. Artifacts in `tool_tests/`.

| route | tool | result | artifact | note |
|---|---|---|---|---|
| Adobe deeper #1 | image_remove_background | PASS | tool_tests/deed_adobe_cutout.png (RGBA) | true AI cutout, transparent |
| Adobe deeper #2 | image_generative_expand (Firefly) | PASS | tool_tests/deed_adobe_banner.jpg (2005x1400) | seamlessly extended the stacks into a wide banner |
| Adobe (prior) | image_crop_and_resize | PASS | DEED 1:1 crop | subject-aware |
| HTML / landing | HTML/CSS + Chrome headless | PASS | tool_tests/landing/index.html + landing_rendered.png | real responsive page, rendered in a browser, not hosted |
| PDF / deck | local Pillow PDF | PASS | tool_tests/DEED_DECK.pdf (5pp) | banner + poster + one-sheet + decision board + studio sheet |
| proof-loop / data | os_form_ingest + os_form_score | PASS | tool_tests/proofloop/SCORE.md | scored a sample CSV; parked RESPONSES.csv restored after |
| data / CRM | Airtable list_bases (read-only) | PASS | base "AI EDGE DEMO" returned | connection proven; write held (would mutate your account) |
| design / Figma | figma-desktop get_metadata | FAIL (connect) | none | Figma app not open -> becomes a HANDOFF (see protocols) |
| video / edit | ffmpeg / os_adobe_cut | PASS (prior) | DEED trailer | frame-accurate assembly |
| local automation | os_engine one-command | PASS (prior) | DEED + REMAINS kits | full chain from one intent |

## What this changed
- Adobe cloud layers PROVEN ACTIVE now: crop_resize, remove_background, generative_expand (3, up from 1).
- HTML/landing route PROVEN ACTIVE locally (Chrome headless is a real local renderer = new USE_NOW tool).
- Airtable READ proven (connection live).
- Figma reclassified TEST -> HANDOFF (app must be open).
- No credits spent (Adobe + local + read-only). No identity exposure. No mutation of external accounts.

## UPDATE (second pass)
| route | tool | result | note |
|---|---|---|---|
| design / Figma | figma-desktop get_metadata/get_screenshot | TIMEOUT (app open) | reachable now (was "unable to connect"); route needs a FRAME SELECTED in a /design/ file. Status: TEST_NOW, needs selection. |
| DOCTRINE FUSION | os_doctrine.py (NEW) | BUILT + PROVEN | gate REJECTED the 3 weak copies I hand-fixed earlier, PASSED the rewrite; 9 domains. |
| DOCTRINE in engine | os_engine doctrine_copy stage | WIRED + PROVEN | engine FLAGGED its own auto-derived fragment copy on a live run. The OS now self-polices against the books. |
