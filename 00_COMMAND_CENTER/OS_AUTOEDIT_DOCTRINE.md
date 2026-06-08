# OS AUTOEDIT DOCTRINE · build our own, do not buy

Doctrine, not a purchase. Chat Video Pro / AutoEdit / OpusClip etc. are paid operator-side tools. We do NOT buy them. We build the same capability stack from our own engines so it runs headless, inside our OS, on our terms. Locked 2026-06-07.

## Principle
Every paid auto-editor is the same pipeline under the hood: **ingest -> selects -> bad-take cleanup -> best-moment detection -> beat grid -> rough-cut build -> VFX/transition apply -> revision package.** We already own engines for most of it. Where we don't, we build the missing piece, not a subscription.

## Our equivalent stack (capability -> our engine)

| AutoEdit capability | Our engine / route | State |
|---|---|---|
| Automatic selects map | Mode B: `os_visual_selects_engine.py` (dense filmstrips, action-peak/freeze per clip). Mode A: transcript select pass. | ✅ Mode B built |
| Bad-take cleanup | reject rules (wrong person, BTS, AI anatomy, broken plate) in the selects CSV + the finishing checklist | ✅ rules exist (V4 repair) |
| Best-moment detection | dense-watch verdicts (HERO/PRIMARY/INSERT/ALT) + director-label-is-truth-until-disproven | ✅ doctrine |
| Beat grid | BPM half-beat snap (Alma: 112 BPM -> 0.267857s grid) | ✅ proven |
| Rough-cut builder | EDL -> ffmpeg assembly spine; `os_finish_plan.py` for the handoff | ✅ built |
| VFX / transition applier | brand transition pack (`alma_transitions.sh`, rolodex); rack-focus, plate blur, end-card via ffmpeg/AE | ✅ working route |
| Color grade / LUT | brand `.cube` via ffmpeg `lut3d` (Premiere `apply_lut` when QE DOM cooperates) | ✅ working route |
| Auto scene-detect (long footage) | Premiere `scene_edit_detection` (when live) or ffmpeg `select=gt(scene\,x)` | 🟡 ffmpeg works |
| Revision package | `os_finish_plan.py handoff` (FCPXML, cut list, timestamp map, asset list, AE spec, revision notes) | ✅ built |
| Excellence gate | `os_finish_gate.py` (11 axes + client-ready checklist) | ✅ built |

## What to build next (the gaps, build not buy)
1. **One-call auto rough-cut** — wrap selects CSV -> beat-snap -> ffmpeg assembly into a single `os_autocut.py` so a locked selects map renders a rough cut unattended.
2. **Mode A silence/filler cleanup** — transcript-driven silence + filler-word removal pass (the auto-editor headline feature) for the first dialogue job.
3. **Transition/VFX library as data** — the transition rolodex as a JSON applied by index, so the VFX applier is selectable, not hand-coded per cut.

## Rules
- Never buy an auto-editor we can build. Document the exact capability gap before considering any tool.
- Operator-side paid panels (Chat Video Pro Color Grade / AI VFX) are a manual fallback only, logged, never an automated dependency.
- Everything routes through the finishing department: `OS_FINISHING_DEPARTMENT_STANDARD.md`. No em-dashes.
