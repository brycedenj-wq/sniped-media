# AXIS_ELITE_001 failures
- BLENDER set v1 rendered underlit/mis-framed (mostly black, only floor lit). Weak direction.
- BLENDER MCP connection DROPPED after first render (localhost:9876 unreachable) before the v2 relight could render. HOLD spatial_continuity until Blender + MCP server restarted. Justified per premium-stack gate (tool dropped mid-run).
- Continuing run with reachable premium stack (Higgsfield range + symbol system) so the run keeps moving.

## Blender look-dev , honest status (2026-06-05)
- ROUTE + GATE + GEOMETRY: PROVEN. Diagnostics confirm a correct nested-arch brutalist hall (archFront y=7, archBack y=15, full walls/floor/ceiling, figure stand-in). Gated socket route works.
- USABLE PLATE: NOT YET. 5 render attempts (v1 dark, v3/v4 flat-flooded, v5 black, v6 not rendered). Root cause = blind look-dev: I can view RENDERS but the viewport screenshot serializer is BROKEN in this addon build ("Unterminated string"), so I cannot see the scene to art-direct light/camera efficiently.
- SOCKET INSTABILITY: the 9876 server dropped 3x mid-session (after screenshot calls). Auto Start relaunches on Blender open but does not re-arm a mid-session drop.
- DECISION: HOLD spatial_continuity for this run (justified: tool look-dev loop unavailable + socket unstable). Do NOT ship a weak plate. Resume the instant the socket is stable; the geometry is built and ready to light.

## BLENDER_PROOF_002 verdict (2026-06-05, post App-Nap fix)
- STABILITY: socket held UP across ~9 consecutive calls this session (App Nap fix + Auto Start working). Earlier drops were pre-fix. Stability effectively proven for >10 min active use.
- PIPELINE: every capability executed cleanly , geometry, boolean arches, concrete/bone materials, spot (shaft), area fill, VOLUMETRIC HAZE, DEPTH OF FIELD, EEVEE render. The tool works end-to-end through the gated route.
- COMPOSED PLATE: NOT achieved in 7 attempts (v1 dark, v3/v4 flat, v5 black, v7 haze-whiteout, v8 lit-but-uncomposed). ROOT CAUSE = no visual feedback loop: the add-on viewport screenshot serializer is broken ("Unterminated string"), so camera/light art-direction is blind trial-and-error.
- WHAT BLENDER ADDS (proven to execute) vs 2D: true 3D geometry + controllable camera + real DEPTH OF FIELD + VOLUMETRIC HAZE/atmosphere + REPEATABLE spatial continuity. 2D/Higgsfield cannot give frame-to-frame spatial truth or art-directed DOF/volumetrics.
- VERDICT: Blender = USEFUL_NOW (not REQUIRED_NOW) for the next sellable package. The 2D range is already elite and carries it. Blender becomes REQUIRED_NOW for true spatial continuity the moment a visual feedback loop exists.
- THE REAL FIX (next Blender action, not more blind renders): implement a CONTACT-SHEET SWEEP , render N camera/light presets into one montage the model CAN view (renders work; only the live screenshot is broken). That restores the feedback loop OS-side. Alternatively fix the add-on screenshot serializer.

## BLENDER , FIXED (object-space win, 2026-06-05)
- After 11 hall attempts (blind look-dev failing), pivoted to OBJECT-SPACE per expert judgment.
- RESULT: axis_monolith_v2.png , charcoal monolith on bone plinth, 3-point studio light, clean embossed square mark, oxblood wax-seal, true DOF, real contact shadow. Composed + sharp in 2 iterations.
- WHAT FIXED IT (from "use blender like this.docx" how-to): 3-point lighting, depth-of-field, and rendering TECHNICAL plan/section/elevation views to stop guessing camera-vs-geometry. The doc was applied, not just ledgered.
- LESSON: Blender = elite + reliable in OBJECT-SPACE (marks, seals, plinths, product/drop mockups, 3D type) in 1-2 iterations. A full brutalist HALL is low-ROI vs 2D Higgsfield (already elite) , defer hall to 2D, use Blender for objects + spatial reference.
- SOCKET: held UP across the entire session (~20 calls) after the App Nap fix. Stability PROVEN >10 min.
- VERDICT UPDATE: blender object-space = ACTIVE-PROVEN. blender hall = DEFERRED (2D better). Blender REQUIRED_NOW for 3D symbol objects / drop mockups; USEFUL_LATER for spatial continuity once a viewport-feedback fix exists.
