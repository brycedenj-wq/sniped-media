# MAX BLENDER PASS 001 · THE ONE (geometry truth before visual elevation)

**Date:** 2026-06-21 · Doctrine applied: Blender Assembly Skill (`Blender-MCP-Assembly-Skill-main/SKILL.md`, whole-read) + the "use blender like this" method (`use blender like this.docx`, method spine extracted: concept-refs first, model parametrically, Meshy only for AI-concept objects, clean topology, optimize before export, Blender as geometry truth). Meshy NOT used (correct: THE ONE is exact parametric geometry). No Higgsfield spend. No posting.

## What changed from the first Blender run
| first run | max pass |
|---|---|
| rough single tray, no rigor | full assembly rigor: connection map, size=2 cubes, transform_apply in-loop, clean topology (remove_doubles + recalc normals), finalize, audit |
| dimensions implicit | measured + VERIFIED: all variants exactly 240 x 160 x 28 mm via verify_bounds |
| transforms unaudited | audit_all PASS: every mesh rotation (0,0,0), scale (1,1,1), origin set to geometry |
| one rim radius | r4 / r8 / r12 variants built as separate clean meshes (964 verts each) |
| 1 material, washed out white renders | 4 materials (ceramic / polymer / aluminum / clay) + a washout-FIXED studio |
| no file saved | .blend saved (geometry truth on disk) |
| no clay / silhouette / turntable | clay form render, shape render, 18-frame seamless turntable encoded to 6s mp4 |

## Updated Blender file
`MADE_WORLD_RUN_001/01_blender/THE_ONE_max.blend`

## Renders produced (01_blender/)
- `max_hero_ceramic_v2.png` (hero 3/4, ceramic, reads clean)
- `max_mat_polymer.png`, `max_mat_aluminum.png` (material comparison, hero angle; + ceramic hero)
- `max_clay_hero.png` (clay form render)
- `max_macro_rim.png` (rim/corner macro)
- `max_radius_macro_r4.png`, `_r8.png`, `_r12.png` (identical-framing corner macros = the radius comparison)
- `max_silhouette.png` (shape read, grey-form-on-white)
- `turntable/` (18 frames) + `06_motion/turntable_6s.mp4` + `turntable_loop.mp4`
- superseded/failed: the white-on-white top-down grid and the first hero (washout; kept only as a QA record)

## r4 / r8 / r12 comparison (honest)
Geometry is correct and distinct (bevel width 4 / 8 / 12 mm, verified). VISUALLY the difference is SUBTLE on a 240 mm tray, even in the corner macro (r4 vs r12 read nearly the same). Recommendation: r8 (balanced). If you want a radius difference that is legible and ownable as a design language, widen the spread (for example r2 sharp / r10 / r20 soft-bowl) and I will re-render. The geometry truth supports any radius instantly.

## Material comparison
Ceramic (soft, quiet-luxury), polymer (matte warm), aluminum (reads most premium, highest edge contrast). All rendered at the hero angle for direct comparison.

## Turntable status
Rendered: an 18-frame seamless 360 loop at 540px, encoded locally to `06_motion/turntable_6s.mp4` (and a 1.5s `turntable_loop.mp4`). A full 24fps 144-frame version is renderable on request (it was capped here to avoid a long blocking render).

## Lighting fix (washout solved)
Root cause of the earlier blown-white renders: a white object on a brightly lit white background with EEVEE clipping. Fix: mid-grey seamless background (0.34) + world strength 0.18 + reduced key/rim/fill + exposure -0.6 + a rim/kicker light for top-edge separation + GTAO contact shadow. The white ceramic now separates on both lit and shadow sides.

## Blender QA verdict (the operator's 6 criteria)
- object reads instantly: PASS (hero, clay, macro)
- proportions clean: PASS (measured + verified 240x160x28)
- rim radius visible: PARTIAL (visible in macro; the 4/8/12 mm DIFFERENCE is subtle, see recommendation)
- no blown white: PASS (after the fix; early washouts caught and corrected)
- no generic render gloss: PASS (matte materials; minor EEVEE grain in deep shadow only)
- works as product / icon / landing hero / social first frame: PARTIAL. Works as a clean REFERENCE for all of those. As a FINAL elite social first frame it is a reference, not the beauty shot. The elite photoreal final is the Higgsfield elevation on this base, then Adobe finish.

## Honest status
The Blender geometry-truth base is BUILT, MEASURED, AUDITED, SAVED, and rendered into a clean reference set with an honest QA loop (washout caught and fixed; radius-legibility limit named). These are references, not elite finals. NOT a final asset, NOT client-ready.

## Exact approval question before Higgsfield spend
See the chat message: confirm the radius (r8, or widen the spread) and the material (ceramic / polymer / aluminum), and approve the capped Higgsfield Batch 001 (~20-30 of 1977.62 credits, per-batch only, img-to-img on these locked references). Nothing spends until you answer.
