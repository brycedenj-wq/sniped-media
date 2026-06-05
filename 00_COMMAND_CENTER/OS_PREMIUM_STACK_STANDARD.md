# OS PREMIUM STACK STANDARD
### Premium stack is DEFAULT-ON for max work. Local shortcuts must prove themselves.
LOCKED 2026-06-05. Supersedes any prior "use the cheapest path" behavior for max/serious outputs.

## The rule

For any serious output , campaign, film, pitch, proof package, client demo, money-facing asset, launch asset, trailer, deck, world, brand system , the OS assumes the PREMIUM stack is REQUIRED unless it proves otherwise in writing. The mission is undeniable work, not saved pennies. Credits that materially raise quality are spent within the authorized run budget. Refill is on the table when the work justifies it.

This does NOT mean every tool runs blindly. It means every max task runs `os_premium_stack_gate.py` FIRST, and every skipped premium tool carries a written justification or is logged as a failure in `OS_TOOL_UNDERUSE_LEDGER.csv`.

## The premium stack

- Higgsfield / Seedance / Nano Banana , premium generation + motion
- Adobe for Creativity (cloud) , cleanup, fill, expand, retouch, crop, resize, color, background, subject selection (Photoshop/Lightroom-style)
- Adobe InDesign/Illustrator render , layout + vector
- After Effects (aerender) + HyperFrames , edit pacing, titles, transitions, kinetic type, motion graphics
- Blender , spatial continuity, 3D objects, sets, product/drop mockups, camera control
- Figma , design systems, layout hierarchy, pitch boards, decks, client-facing polish
- Notion , command room / project room / doctrine + client wiki
- Airtable , proof-loop tracking, CRM, asset registry, signal DB
- Google Drive , delivery / archive (Gmail/Calendar only when approved)
- Vercel / Netlify , only when hosting is explicitly approved
- local scripts , only when faster AND quality-equivalent-or-better, justified per need

## Need -> required tool (default-on)

| If the artifact needs | Premium tool considered REQUIRED |
|---|---|
| edit pacing | Premiere/After Effects/HyperFrames (not just ffmpeg) |
| motion design | After Effects / HyperFrames |
| layout excellence | Figma and/or InDesign-style Adobe render (not Pillow template) |
| spatial / world continuity | Blender (one real set, true angles) |
| cleanup / expand / retouch / compositing | Adobe cloud tools |
| client-facing polish | Figma / deck / layout tools |
| a proof loop | Airtable / Notion / Drive |

If the OS skips one because "local scripts are enough," it MUST prove local is better for THIS artifact, not just easier.

## The gate verdicts (os_premium_stack_gate.py)

- FULL PREMIUM STACK REQUIRED , plan mode, the task needs the full stack and it is ACTIVE
- PREMIUM STACK PARTIAL, JUSTIFIED , some needs skipped with written, valid reasons
- HOLD FOR TOOL ACTIVATION , a required tool is AMBER/RED/needs setup
- REJECT: UNDERBUILT , a needed capability is simply absent
- REJECT: TOOL UNDERUSE , an available premium tool was relevant and unused, unjustified
- REJECT: LOCAL SHORTCUT USED WHERE PREMIUM TOOL WAS REQUIRED , local used where premium was required

## The new MAX definition

A run may NOT call itself MAX unless ALL of these were CONSIDERED and recorded:
premium generation, premium post-production, premium edit/motion, Figma/design-system, Blender/spatial, Adobe cloud, proof-loop/ops. Every skipped tool has a written justification. Every underused tool is logged as a failure. Clean-but-not-excellent fails. A "moving still" is not a film.

## Enforcement order
1. `os_premium_stack_gate.py plan <task>` before building.
2. Build with the full stack (or justify each skip).
3. `os_premium_stack_gate.py audit <task> --used ... --justified ...` after.
4. `os_elite_art_direction_gate.py score ...` for taste.
5. Underuse -> `OS_TOOL_UNDERUSE_LEDGER.csv`. Only then may a run be called MAX.
