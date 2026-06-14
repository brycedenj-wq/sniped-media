# FILM PROOF LAUNCH PLAN (paid-run preflight)
### The real bounded run that flips build_film_pipeline from AMBER to ACTIVE.
Prepared 2026-06-05. Requires explicit spend approval. Nothing here runs until you say go.

---

## Exact concept

A 12-to-15 second vertical teaser for the existing locked world MERIDIAN-HOUSE with the locked hero AXIS. One ownable mark, one color law, faceless-safe. Working title: "THE HOUSE REMEMBERS." This reuses an already-approved, already-identity-gated character, so the run tests the pipeline, not a new character.

## Exact shots (4 shots, 1 sequence)

| # | Shot | Source | Generation |
|---|---|---|---|
| 1 | Title card "THE HOUSE REMEMBERS" | os_adobe_layout / AE | none (local) |
| 2 | AXIS in the monolith room, slow push-in | locked hero still -> Seedance i2v | 1 motion clip (~4s) |
| 3 | Detail: the mark on a surface, rack focus | 1 new still -> Seedance i2v | 1 still + 1 motion clip (~4s) |
| 4 | End card "AXIS / a meridian house file" | os_adobe_layout / AE | none (local) |

## Exact tools

- Stills: `mcp.higgsfield.image` (nano_banana_pro), conditioned on the locked hero (no fresh text-only face).
- Motion: `mcp.higgsfield.video` (Seedance i2v), start-image = approved hero.
- Titles: `local.aerender` (AE comp) or HyperFrames lower-thirds.
- Finish: `os.adobe_cut` (caption-safe), ffmpeg concat.
- Gates: os_facematch, os_motion_qa (fresh obs), os_world continuity, os_privacy_gate, os_postproduction_gate.

## Exact credit estimate (honest, bounded)

- 1 new still (nano_banana_pro): ~2-4 credits.
- 2 motion clips (Seedance, ~4s each at ~18 cr/4s): ~36 credits.
- Retry buffer (1 reroll): ~18 credits.
- **Ceiling for approval: ~60 credits.** I will preflight exact cost with `get_cost` / `balance` before spending and stop if it exceeds the ceiling.

## Exact pass/fail gates

- facematch: vision >= 0.7 AND identity hard-invariants hold -> else QUARANTINE the frame.
- motion_qa: SHIP requires 0 identity quarantine, world pass, no HARD motion item = 0, score >= 0.75.
- world continuity: scene must pass MERIDIAN-HOUSE forbidden/env.
- privacy: 0 leaks, metadata stripped.
- post-production: grade applied + all 7 export sizes present + no banned tokens.
- Human taste: SHIP = eligible for your sign-off, never auto-post.

## Exact artifacts produced

shot stills, 2 motion clips, titled + concatenated teaser (9x16), 7 export sizes, all gate reports, EDIT_LOG + SPEND_LEDGER, manifest, dashboard, and a final film-proof report.

## What makes it ACTIVE

`build_film_pipeline` flips AMBER -> ACTIVE when: fresh generation runs through all gates, motion_qa SHIPs on FRESH observations, the post-production gate returns SHIP (grade + 7 exports), and the teaser passes your taste sign-off. That is the route + artifact + log + gate + repeat bar, met with new material.

## What stays AMBER even after this run

- Sound / score (HANDOFF, no generation tool wired).
- Sustained multi-shot narrative continuity beyond ~15s (this proves a teaser, not a full film).
- Any public release (HELD).

## Go condition

On your explicit "approve ~60 credits for the film proof," I preflight cost, run the 4-shot sequence, gate everything, and report. Until then this stays parked.
