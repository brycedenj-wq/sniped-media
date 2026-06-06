# FIGMA DECK SOURCE REPORT (2026-06-06)

> The editable Figma source now matches the buyer PDF. Live build via `use_figma` on file `o0fuh72mlvOPi8ZTYPGbCR` (https://www.figma.com/design/o0fuh72mlvOPi8ZTYPGbCR).

## Status: COMPLETE , 12/12 slide frames
Verified via `figma.currentPage.children` (frameCount 12):
01 Cover · 02 Problem · 03 The Sole Claim · 04 Proof of World · 05 Seal Hero · 06 Teaser · 07 Offer · 08 Process · 09 Anti-Agency · 10 Pricing Ladder · 11 Proof · 12 Next Step.

## Design system (real, in-file)
- **Color variables** (`sole/color`): ink #0A0A0B, bone #EDE8DD, brass #A8843C, concrete #6B6B6E (scoped: FRAME_FILL / TEXT_FILL / STROKE).
- **Type:** Bodoni Moda (didone display, the engraved-nameplate register) + Archivo (grotesque body/eyebrow). Eyebrows tracked +12%.
- **Components/motifs in use:** the Singular Seal mark (brass ring + concentric ring + numeral-1 bar), brass hairline cards (pricing + process + offer), seal-ring bullets, two-column comparison.
- **Grid:** 1920x1080 frames, 140px side margins, eyebrow@120 / headline@200 pattern.

## Image slots (drop-in fills, not yet uploaded)
Slides 04/05/06 carry named, hairline-framed image-fill rectangles where the rendered assets drop in:
- 04 Proof of World: 2x2 slots (S01 / S05 / S09 / S11).
- 05 Seal Hero: the Blender Singular Seal alpha.
- 06 Teaser: the 70s film poster + play control.
The final composited images already exist in the buyer PDF; in Figma they are specified slots (upload via `upload_assets` + image fill is the one remaining mechanical step, not a design decision).

## Export
- The buyer-facing deliverable is the Chrome-rendered PDF (real Didot/Bodoni + final images): `08_DESIGN_DECK/deck/SOLE_CATEGORY_BRIEF_DECK.pdf`.
- The Figma file is the EDITABLE SOURCE (tokens + type + 12 frames). Per-frame export (screenshot or PDF) reproduces the deck; the two are the same design language in source + deliverable form.

## Verdict
Figma deck source = COMPLETE and editable (12 frames, token system, premium render confirmed by screenshot). No longer "static PDF only." Remaining mechanical step: upload the 3 image fills (drop-in), optional since the PDF carries the final composites.
