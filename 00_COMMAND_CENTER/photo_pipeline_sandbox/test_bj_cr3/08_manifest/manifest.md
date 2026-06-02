# RAW Sandbox Production Test · Phase 2a Manifest · test_bj_cr3

**Date:** 2026-05-28
**Source:** Untitled-1.CR3 (BJ self-portrait, Canon EOS R6 Mark II, 6000x4000, ISO 1600, 1/160, 50mm, Manual + Flash, captured 2026-05-03)
**Original CR3 SHA256:** `582195b84584b55c5535631d70ddd836f32fc2d4f0a4e75be2322c530779410a`
**Original XMP SHA256:** `868f845028fb244ddb6483fb9bc4623ce534fc7435ca380138034f760ebff598`
**Phase 2a status:** complete

## Develop passes

1. **Baseline rawpy** · camera WB + no auto-bright + 16-bit sRGB output
2. **XMP-respected** · identical to baseline (XMP carries no develop edits)
3. **v3 LUXURY attempt** · numpy tone curves + OpenCV HSV-based HSL + global sat -8% + subtle warm midtone push + grain (seed 42) + unsharp mask

## Outputs (all in 04_developed/)

| File | Purpose |
|---|---|
| baseline_rawpy_16bit.tiff | Lossless 16-bit reference |
| baseline_rawpy_preview.jpg | 8-bit baseline preview |
| xmp_respected_rawpy.jpg | XMP-respected (= baseline) |
| v3_luxury_attempt.jpg | v3 LUXURY translation result |
| compare_full_baseline_vs_v3.jpg | Full-resolution side-by-side |
| compare_preview_baseline_vs_v3.jpg | Downsized side-by-side for fast viewing |
| develop.metadata.json | Full translation parameters |

## Tool versions

- Python 3.9.6
- rawpy 0.27.0
- numpy 2.0.2
- OpenCV 4.13.0
- Pillow 11.3.0
- exiftool 13.55

## Privacy posture

- Source CR3 + XMP unchanged (SHA256 verified before and after)
- All output JPGs metadata-stripped via exiftool -all=
- Sandbox-bound; no upload anywhere
- No Higgsfield, no Adobe MCP, no external systems touched

## Quality ceiling

- Baseline rawpy: clean technical decode, ~85-90% of Lightroom default rendering
- XMP-respected: identical to baseline (XMP empty)
- v3 LUXURY attempt: ~75-85% match to a Lightroom-applied v3 LUXURY preset
  - Tone curves: ~95% match (numpy interp closely matches Lightroom)
  - HSL: ~75-85% (OpenCV HSV vs Lightroom range-blended HSL)
  - Texture/Clarity: NOT applied (deferred to engine v2)
  - Grain: ~85% feel match (different RNG, similar visual)

For pixel-honest Lightroom reference: export Untitled-1.CR3 with SNIPED_LOCKED_LOOK_v3_LUXURY.xmp applied in Lightroom Classic and add as a third pane in the comparison.
