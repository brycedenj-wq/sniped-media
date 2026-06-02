# Treatment A · SNIPED Cultural Doc Cover Art proof package

**Date:** 2026-05-29
**Source master:** `07_hero/FINAL_hero_v8_tiff_master.tiff` (16-bit TIFF, 6022 × 4014, 151 MB)
**Source export (working copy):** `07_hero/FINAL_hero_v8_tiff_pipeline.jpg` (8-bit JPG, 7.3 MB)
**Status:** PROOF PACKAGE · 15 layouts + contact sheet · for direction selection · NOT production-final

## Goal

Turn the preserved photograph (`v8`) into an authored SNIPED cultural artifact. The image is the source material; the cover-art treatment is the authored layer. The orange field carries the identity; typography is restrained.

## Source decisions (locked)

- Photograph is preserved · no face / body / skin / fisheye / orange / studio context modified.
- No object removal · the C-stand and studio gear remain as documentary context.
- No new image generation · no Higgsfield, no generative AI.
- No publish · sandbox only.
- No commit · awaiting BJ approval.

## Format matrix (5 formats × 3 typography directions = 15 layouts)

### Formats and intended use

| Format | Aspect | Crop anchor | Intended use |
|---|---|---|---|
| 3:4 Cultural Doc | 3 W : 4 H | center | Cultural Doc episode hero card, print edition cover, About-page hero portrait |
| 1:1 IG card | 1:1 | center | IG carousel hero card, profile grid anchor, square print edition |
| 4:5 IG feed | 4:5 | center | IG feed portrait post (Meta's preferred portrait aspect) |
| 9:16 Story | 9:16 | center | IG Story, TikTok hero, vertical hero card |
| 16:9 Web hero | 16:9 | upper-third anchor | Web hero, LinkedIn POV banner, YouTube card, OpenGraph |

### Crop logic

All crops preserve BJ centered (or upper-third for 16:9 to keep face above fold). All crops preserve the fisheye barrel distortion. All crops preserve the orange backdrop as the dominant field. No content removed inside the frame.

### Typography directions

| Direction | Type position | Type size | Voice |
|---|---|---|---|
| **A · Minimal bottom-left** | small block at bottom-left | small (3-4% of image height) | restrained, understated, editorial · the photograph leads, typography acknowledges |
| **B · Oversized SNIPED wordmark** | giant SNIPED centered at top in orange field | large (up to 14% of image height) | declarative, authored, brand-forward · the wordmark carries the identity, photo holds the bottom |
| **C · Archival / contact-sheet caption** | monospace multi-line caption at bottom-left | small (1.5% of image height) | museum-archive register · contact-sheet annotation feel, BJ's signature plate |

### Typography lock

- **Main mark:** SNIPED (Helvetica Bold, all caps)
- **Episode marker:** CULTURAL DOC · 001 (Helvetica Regular, tracking acknowledged via spacing)
- **Author line:** Bryceden Jones (Helvetica Regular, lighter weight visual via color)
- **Direction C extended:** UNTITLED-1.CR3 + 2026·05·03 LA (mono caption, evokes the contact-sheet origin)
- **Color:** warm cream (#F2EADC) for accent type, slightly desaturated cream (#DACFBB) for secondary
- **No motivational copy. No fake publication header. No decorative graphics. No cheesy magazine treatment.**

## Files in this proof package

```
10_cover_art_v1/
├── 3x4_doc/
│   ├── A_minimal_3x4_doc.jpg
│   ├── B_oversized_3x4_doc.jpg
│   └── C_archival_3x4_doc.jpg
├── 1x1_ig/
│   ├── A_minimal_1x1_ig.jpg
│   ├── B_oversized_1x1_ig.jpg
│   └── C_archival_1x1_ig.jpg
├── 4x5_ig/
│   ├── A_minimal_4x5_ig.jpg
│   ├── B_oversized_4x5_ig.jpg
│   └── C_archival_4x5_ig.jpg
├── 9x16_story/
│   ├── A_minimal_9x16_story.jpg
│   ├── B_oversized_9x16_story.jpg
│   └── C_archival_9x16_story.jpg
├── 16x9_web/
│   ├── A_minimal_16x9_web.jpg
│   ├── B_oversized_16x9_web.jpg
│   └── C_archival_16x9_web.jpg
├── contact_sheet_all_layouts.jpg
└── MANIFEST.md
```

## Privacy posture

- All output JPGs metadata-stripped via exiftool
- Source CR3 + XMP unchanged (SHA256 verified)
- Sandbox-bound
- No upload anywhere
- No Higgsfield credits spent on this phase

## Production path after direction selection

This is a PROOF package. Type rendered via local PIL is editorially readable but not print-grade. After BJ selects winning direction(s):

1. Recreate winners in Figma via Figma MCP for true type rendering
2. Apply proper kerning / tracking / hanging punctuation
3. Export from Figma at print-grade resolution (300 DPI · 24×36 inch target = 7200×10800 px)
4. Sign-off for print edition or final social use

The proof package's purpose is to validate **which direction works**, not to be the deliverable itself.

## Reject-gate notes

Per `feedback-strongest-photograph-not-most-processed`: each layout must visually beat the source photograph as an artifact (not just match it · be more authored). If no direction visually beats the source for any given format, that format gets dropped or reworked.
