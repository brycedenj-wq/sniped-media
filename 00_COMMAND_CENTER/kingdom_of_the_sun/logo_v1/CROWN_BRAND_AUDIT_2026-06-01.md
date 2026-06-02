# Crown / Sun Rays · Brand Pass & Use-Case Audit (2026-06-01)

> A pre-deploy audit of the 2026 refreshed identity against real use cases. The goal is to **refine the existing Crown system, not restart it.** The mark is good. It has two fixable weak points at small sizes.

---

## 0. Brand hierarchy (locked)

- **Crown / Sun Rays = PRIMARY 2026 identity.** The modern, forward-facing face: website header, favicon, cards, sponsor deck, program cover, apparel, social.
- **Old Florida + basketball logo = HERITAGE mark only.** Used respectfully in History/archive context to honor the original. It never acts as the brand and never appears in forward-facing chrome (header, favicon, cards, deck covers).

This audit covers the Crown only. The legacy mark is frozen as-is for heritage use.

---

## 1. The mark, described

A gold crown whose points double as sun rays, with an orange sun disc at the center and a base bar beneath. Navy / gold / orange / cream palette. Strong concept: it reads as both a **crown** (Kingdom) and a **sunrise** (Sun) at once. That dual meaning is the system's biggest strength and is worth protecting through every refinement.

---

## 2. Use-case audit

| # | Use case | Verdict | Finding |
|---|---|---|---|
| 1 | **Website header** | STRONG | Crown at ~30px gold-on-navy reads clean and distinct. No change needed. |
| 2 | **Favicon (16px)** | WEAK · needs variant | At 16px the five thin spikes merge into a gold blob and the sun disc nearly disappears. At 32px it recovers. The full mark is too detailed for the smallest sizes. |
| 3 | **Business card** | STRONG | The stacked lockup and QR-card layout are clean and premium. |
| 4 | **Sponsor deck** | STRONG | Crown + wordmark cover reads like a real property. Good. |
| 5 | **Program cover** | STRONG · with gap | Works on solid navy. Missing a **reversed / on-photo variant** for covers placed over photography. |
| 6 | **Shirt / embroidery** | AT RISK | Thin spike tips, the thin base bar, and the small sun disc are all embroidery hazards. Thin elements blow out or fill in at chest size. Needs an embroidery-safe variant. |
| 7 | **One-color print** | STRONG | The solid silhouette with the sun as a knockout ring holds cleanly in single ink. Good for stamps, fax-grade, etching. |
| 8 | **Small-size legibility** | AT RISK | Same root cause as the favicon: below ~24px the spike separation and the sun disc both collapse. |

**Two root issues, not eight:**
- **(A) Five thin spikes merge at small sizes.** Elegant large, mushy small.
- **(B) The sun disc is too small** to survive small sizes, one-color at tiny scale, and embroidery.

Everything in the WEAK / AT RISK rows traces back to these two.

---

## 3. Refinements (refine, do NOT redo)

Ranked. None of these change the identity, they harden it.

1. **Small-size / favicon variant.** A simplified mark for <=24px: thicken the spikes (or reduce to 3-4 bolder points), enlarge the sun disc, drop the base bar. Keep the full five-spike mark for >=32px. Test at literal 16px before sign-off.
2. **Embroidery-safe variant.** Rounded, thicker spike tips; enforce a minimum stroke width; base bar optional; one-color. Gold-on-navy and navy-on-gold both.
3. **Strengthen the sun disc** in the primary mark, slightly. Marginally larger and higher-contrast so it is unmistakably "the sun," which also fixes small-size and one-color survival. Subtle, keeps the identity.
4. **Make the base bar optional.** Full lockup keeps it (it reads as the court/foundation). Favicon, app icon, and small embroidery drop it.
5. **Add missing variants:** reversed (navy-on-gold), all-cream, and an on-photo version (hairline keyline or soft shadow) for program covers over photography.
6. **Codify the rules:** minimum sizes (mark not below ~20px digital; lockup minimum width), clear space, and a short do-not list (no recoloring the sun, no stretching, no old-logo-plus-Crown lockups).
7. **Kill stale collateral copy.** The concept board, the stacked lockup, and the validation board still read **"52nd Annual" / "52 YEARS."** Dad confirmed **53rd**. Regenerate all collateral to 53rd before anything ships.
8. **Wire the Crown favicon into the live site** so the browser tab is Crown-branded (done in this pass).

---

## 4. Deliverables when refinements are greenlit

A tightened Crown set, all from the existing geometry (`build.py`), not a redraw:
- `crown_primary` (refined disc), `crown_reversed`, `crown_onecolor`, `crown_favicon_small`, `crown_embroidery`
- Updated stacked + horizontal lockups, corrected to **53rd Annual**
- Favicon export set (16 / 32 / 48 / 180 / .ico) + the site app icon
- A one-page brand mini-guide: palette, type, min sizes, clear space, do / do-not

---

## 5. Bottom line

The Crown / Sun Rays direction is sound and worth keeping. It is premium, it carries the crown-plus-sun idea cleanly, and it already works for header, cards, deck, and one-color. The only real work before deploy is **hardening the small end** (favicon, embroidery, small-size) by simplifying a variant and strengthening the sun disc, plus **correcting the 52nd to 53rd** across the collateral. No restart. A focused refinement pass.

---

## 6. Refinement EXECUTED (2026-06-01) · before / after

Status: **DONE.** Refined from the existing `build.py` geometry (Crown of Sun Rays v1.1 → v1.2). No redraw.

| Issue (before) | Fix (after) | Result |
|---|---|---|
| Favicon at 16px: 5 thin spikes merged into a gold blob, sun disc vanished | New 3-peak favicon variant, single thick bar, enlarged disc | At real 16px it now reads as a crown with a clear sun disc. Verified at 16px and 24px. |
| Embroidery: thin spike tips + thin lower bar + small disc = stitch hazards | New `embroidery_*` variant: 3 fat peaks, one thick bar, no fragile detail, enlarged disc | Stitch-safe gold-on-navy and one-thread versions |
| Sun disc too small for small-size / one-color | Disc enlarged across all three geometry levels (full sun r 21 → 24, moat 27 → 30; simple/emb larger) | Stronger, unmistakable "sun"; survives one-color and small sizes |
| Missing reversed / cream / on-photo variants | Added `reversed_navy_on_gold`, `cream_on_navy`, `on_photo_gold` (transparent + soft shadow) | Full coverage for any background incl. photographic program covers |
| Stale "52nd / 52 YEARS" in concept board, validation board, lockups | All corrected to **53rd** (hero lines reframed to "The Original. Since 1974.") | No stale edition copy remains in the system |
| No exported kit | `kit/png/` (all variants @512, primary @1024) + `kit/favicon/` (16/32/48/64/180 + favicon.ico) | Deploy-ready |

Refreshed collateral re-rendered: `KOTS_2026_Refresh_Concept_v2.png`, `validation_board.png`. Live site updated: `site/public/crown.svg` (full mark, nav + hero) and `site/app/icon.svg` (refined favicon).

## 7. Usage rules (locked)

- **Primary mark:** `primary_gold_on_navy` (5-peak). Use at **>= 32px**. Header, deck, program, cards, large.
- **Small size (<= 24px):** use the **favicon variant** (`favicon_navybg` / `favicon_creambg`), never the 5-peak mark.
- **Embroidery / patches / stitched apparel:** use the **embroidery variant** only. Minimum 1 inch chest height.
- **One-color print:** `onecolor_navy` or `onecolor_gold` (sun renders as a knockout).
- **On photography:** `on_photo_gold` (carries a soft shadow for separation). Keep the crown over a calmer area of the image.
- **Reversed / light grounds:** `reversed_navy_on_gold` on gold; `inverse_navy_on_cream` on cream.
- **Clear space:** one main-bar height on all sides. **Do not** recolor the sun disc, stretch the mark, add effects, or ever lock the old Florida logo beside the Crown.
- **Hierarchy:** Crown = primary 2026 identity everywhere forward-facing. The old Florida + basketball logo is heritage-only (History / archive context).
