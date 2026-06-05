# MAX CAPABILITY MAP , OS creative production ceiling (2026-06-04)
> What the OS can actually make right now, using LOT 00 4K as the test object. ACTIVE = a script/gate/log proves it and it repeats. Internal only. No new AI generation in this run (all artifacts are reversible local work on the existing 4K still).

## RED / AMBER / GREEN creative dashboard
**18 ACTIVE · 2 AMBER · 1 RED** across 21 outputs. See `artifacts/10_proof_dashboard.png`.
- ACTIVE: hero still, poster, title card, story/reel crop, web hero, print proof, one-sheet, lookbook, landing visual, motion teaser (still-based), still-based trailer, thumbnail, caption set, drop mockup, social carousel, pitch board, proof dashboard, mini world bible.
- AMBER: video cutdown (single-clip only), automation hooks (scripts logged, no one-command pipeline yet).
- RED: AI-generated motion of the character (needs Higgsfield approval).

## The ceiling, in one line
The OS can take ONE high-res hero and produce a full campaign kit , poster, title card, landing, carousel, one-sheet, lookbook, print drop, a 14s motion teaser, a pitch board, and a dashboard , entirely from local, logged, repeatable scripts, in the locked editorial look. The ceiling is a complete still-driven campaign system. The next ceiling is generated motion.

## Category map (can we do it now / tool / proof / smallest artifact / manual / automate / 10x)
| # | category | now | tool | proof artifact | stays manual | automate later | 10x unlock |
|---|---|---|---|---|---|---|---|
| 1 | Hero still | YES | Higgsfield + os_adobe_grade + gate | lot00_4k SHIP | concept/taste | done | 4K default + face-lock reuse |
| 2 | Poster | YES | os_adobe_layout poster | 01_poster.png | headline taste | done | A/B mastheads, motion poster |
| 3 | Title card | YES | os_adobe_layout titlecard | 02_titlecard.png | copy | done | animated lower-thirds |
| 4 | Story/reel crop | YES | os_adobe_reframe | 03_exports/story_9x16 | focal pick | done | subject auto-detect focus |
| 5 | Web hero | YES | os_adobe_reframe | web_hero_3x2 | , | done | responsive set |
| 6 | Print proof | YES | os_adobe_reframe print_4x5 | print export | paper choice | done | CMYK soft-proof + bleed |
| 7 | One-sheet | YES | os_adobe_layout onesheet | 07_onesheet.png | copy | done | data-merge variants |
| 8 | Lookbook page | YES | os_adobe_layout lookbook | 08_lookbook.png | sequencing | multi-page book | InDesign-grade spreads |
| 9 | Landing visual | YES | os_adobe_layout landing | 03_landing_hero.png | headline/CTA | done | real responsive HTML export |
| 10 | Short motion teaser | YES | os_adobe_teaser | 04_teaser_9x16.mp4 | beat choice | done | generated motion beats |
| 11 | Still-based trailer | YES | os_adobe_teaser | 04_teaser (14s) | story order | done | sound design + voice |
| 12 | Video cutdown | PARTIAL | os_adobe_cut | cut_test_9x16 | edit taste | multi-clip sequence | real AI clips to assemble |
| 13 | Thumbnail | YES | os_adobe_layout | 13_thumbnail.png | hook | done | CTR A/B variants |
| 14 | Caption set | YES | world-bible voice | caption.md | voice (taste) | template bank | tone variants per platform |
| 15 | Product/drop mockup | YES | layout + composite | 05_drop_mockup.png | product choice | template kit | true 3D/scene mockups |
| 16 | Social carousel | YES | os_adobe_layout carousel | 06_carousel/ | story arc | done | auto-slice from one-sheet |
| 17 | Internal pitch board | YES | os_adobe_layout board | 09_pitch_board.png | curation | done | live auto-refresh from registry |
| 18 | Proof dashboard | YES | local render | 10_proof_dashboard.png | , | os_proof_dashboard.py | live data-bound dashboard |
| 19 | Campaign / mini world bible | YES | OS docs | 05_WORLD_BIBLE.md | authorship | , | generated style frames per law |
| 20 | Automation hooks | PARTIAL | os_adobe_* + EDIT_LOG | EDIT_LOG.csv | gate verdicts | one-command os_campaign pipe | end-to-end one-shot pipeline |

## What actually looks impressive
The campaign poster (Didot masthead over the tagged-ancestor wall), the 14s teaser (the push into the legible LOT 00 tag is the money shot), and the pitch board (one page that reads like a real campaign deck).

## What still looks weak
Landing headline contrast over the bright window; the carousel is solid but template-plain; the drop mockup is a clean card, not a true 3D scene; all motion is still-based (no real movement of the subject).

## What tools were used
Higgsfield (the one 4K still, prior approval), os_adobe_grade/composite/reframe/layout/teaser/cut, os_postproduction_gate, Pillow, ffmpeg (zoompan/fade/concat), Didot/Baskerville/Arial. All local + logged.

## What was automated vs needed taste
Automated: grade, color-law, reframe, layout typesetting, Ken Burns moves, concat, gate checks, logging. Needed taste: the concept, the headline/caption copy, beat order, focal points, curation.

## What to build overnight to raise the ceiling
1. `os_campaign.py` , one command: hero in, full kit out (poster+title+landing+carousel+teaser+board+dashboard), gated. Closes the AMBER automation-hook gap.
2. `os_adobe_layout.py landing-html` , export a real responsive HTML hero, not just a PNG preview.
3. First AI motion (needs approval) , one Higgsfield clip so os_adobe_cut assembles a real cutdown (moves category 12 AMBER->ACTIVE, 21 RED->ACTIVE).
