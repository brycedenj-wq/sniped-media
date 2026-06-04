# PLATFORM_MASTERING · the export law

Canonical standard. A campaign hero is NOT finished when the composite passes `COMPOSITE_MASTER_QA`. It is finished when the **platform masters** pass. This law governs how one approved hero becomes per-surface masters.

Invoke as the `/platform-mastering` skill. Runs after `/composite-master-qa`. Mirror copy travels with each project.

---

## Prime rule

Do NOT export one flat master and crop it everywhere. Each platform is a different viewing environment (aspect, UI safe areas, viewing size, intent). Re-compose or crop **intentionally** per platform.

The subject grade stays LOCKED. Platform mastering touches only output/export (crop, safe area, contrast, sharpening, text) and, where the composite is rebuilt per aspect, the same environment-marriage integration that already passed QA. Never re-grade skin.

---

## Surfaces and their rules

| Surface | Aspect | Crop / safe area | Output finish | Text |
|---|---|---|---|---|
| Story | 9:16 | Face below top UI (~8%), feet above bottom UI (~12%); extra vertical environment headroom | Higher sharpening + contrast (small viewing size) | Clean default; native stickers, not baked |
| Feed | 4:5 | Tighter full-body composition, distinct from story | Mobile sharpening + slight contrast | Clean default; baked only for a drop announcement |
| Square | 1:1 | Full body with side environment, or intentional 3/4 | Mobile sharpening | Usually clean |
| Deck | 16:9 | Cinematic, environment on both sides, room for native type | Light sharpening (large viewing) | None baked; deck software adds type |
| Proof | source ratio | Studio frame beside campaign, equal height | Neutral | Label only |

Story and feed are NOT the same crop at two ratios. Re-compose them.

---

## Hard rules

1. Do not export one flat master and crop it everywhere. Re-compose or crop intentionally per platform.
2. Story, feed, square, deck, and proof each get their own safe area, contrast, sharpening, and text rules.
3. **Clean / no-text is the default for posting.** Baked text is only for drop cards, deck slides, or intentional ad graphics.
4. When color confidence is in question, **measure skin drift numerically** (interior body skin, source vs composite, RGB).
5. **If skin shifts hue or temperature, fail the export.** A uniform brightness lift on all channels (no hue/temp move) is acceptable; an uneven channel shift is a fail.
6. If color passes but feels weak, **test platform sharpening and contrast first**. Do not hide a weak export inside B&W.
7. **B&W is an editorial / prestige sidecar, not the default drop asset**, unless the brand concept specifically calls for B&W. Color leads conversion when the brand identity is built on color.

---

## Skin-drift test (the numeric check)

Sample interior body skin (alpha eroded ~25px to exclude rim/wrap edges; warm-skin mask) in the locked source vs the final composite. Report mean RGB of both and the delta.
- Uniform delta across R/G/B (e.g. +3/+3/+3) = brightness lift only, no identity change = PASS.
- Uneven delta (hue/temp shift, e.g. +8R/+1G/-4B) = the environment is pulling her tone = FAIL the export, reduce the marriage strength on the subject.

---

## Required output (per approved hero)
- `M_story_color_clean`, `M_feed_color_clean`, `M_square_color_clean`, `M_deck_color_clean`, clean high-res master
- one B&W editorial sidecar
- text versions ONLY for drop card / deck / ad
- side-by-side phone proofs (color vs B&W; platform set)
- the measured skin-drift line

A hero is shippable only when its platform masters pass. Update SESSION_STATE + commit the milestone after the mastering pass.

---

## Locked decision · Alma Love Club BH hero (2026-06-02)

Measured skin drift: +2.8 / +2.8 / +2.9 RGB (uniform, no hue/temp shift) -> color preserves her identity exactly; color does NOT fail.

- **Color = lead drop / conversion hero.** (B&W flattens the pink Beverly Hills Hotel palette, which is ALC's identity.)
- **B&W = one prestige / editorial sidecar only.**
- Best casual follow-up to Kenn: clean color FEED master (`M_feed_color_clean.jpg`).
- Best for posting: clean color STORY master (`M_story_color_clean.jpg`).
- Deck: 16:9 color master (`M_deck_color_clean.jpg`) with deck-native typography.
- Before/after proof (`BH_v2_before_after.jpg`) stays as the credibility asset.
