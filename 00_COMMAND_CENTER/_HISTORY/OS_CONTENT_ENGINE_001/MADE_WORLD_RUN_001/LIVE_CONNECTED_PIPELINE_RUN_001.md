# LIVE CONNECTED VISUAL PIPELINE RUN 001 · MADE WORLD / THE ONE

**Date:** 2026-06-21 · A production-pipeline PROOF executed on the live stack. Free/local tools were actually run; the spend tool (Higgsfield) is staged behind a per-batch approval. Nothing posted, no ads, no payment rails, no global always-allow, no auto-continue. This is NOT a finished campaign and NOT a final asset.

## 1. Connector preflight (live, read-only, run this session)
| tool | status | evidence |
|---|---|---|
| Higgsfield | connected · SPEND-GATED | balance = 1977.62 credits, ultra plan |
| Blender | connected · LIVE (free/local) | default scene returned; built + rendered for real this session |
| Premiere | connected · VERIFIED LIVE | ping ok, v26.3.0 (was UNVERIFIED-LIVE in the ledger; now confirmed) |
| Figma | connected · authed | whoami = Bryce, pro team |
| Adobe | connected · auth | account_type=auth; crop/color/adjust/remove-bg/outpaint available; NO image generation here; needs URL/assetId (local files via picker) |
| After Effects | connector up · needs bridge panel | get-help ok; requires the mcp-bridge-auto panel open in AE + scripts installed; comp-build only, cannot import/render footage |

## 2. Source of truth (brief) for THE ONE
- Object premise: one shallow undivided tray, subtraction applied to the desk-organizer category; the rule (one layer or it stays home) is the product.
- Visual law: object on white, near monochrome, one brass accent, one soft light, one shadow, generous negative space.
- Materials: bone-white ceramic (primary), matte polymer, brushed aluminum.
- Dimensions (built): 240 x 160 x 28 mm, wall 3 mm, floor 4 mm, rim radius r8 (the signature).
- Product behavior: holds only what fits flat in one layer.
- World feel: quiet-luxury editorial, museum-still calm.
- Platform outputs: 9:16, 1:1, 4:5, 2:3, 16:9, email.
- Quality bar: section 9 QA gate; beats a placeholder 10x; "where can I get this."

## 3. Blender base object · BUILT (real renders on disk)
DECISION was YES, and it was executed. A precision tray was modeled (boolean cavity + r8 bevel, 592 verts), 3 materials created, a white studio + soft key/fill + tracked camera set up, EEVEE.
- **QA loop (honest):** the FIRST white-material renders FAILED the gate (blown to pure white, no tonal separation: a white object on a white floor with too-bright ambient). Caught by viewing them, not assumed. Fixed the studio (dimmed world to 0.28, toned floor to light grey, tamed key/fill, slight negative exposure) and re-rendered. v2 renders PASS as base references.
- **Assets in `01_blender/` and `04_selects/`:** `tray_hero_aluminum.png` (cleanest full-form read), `tray_hero_ceramic_v2.png`, `tray_topdown_v2.png`, `tray_macro_ceramic_v2.png`. QA note in `09_qa/blender_base_qa.txt`.
- **Honest grade:** these are correct, framed, geometry-exact BASE references (proportion locked), not elite finals. EEVEE white-on-white is soft and slightly grainy. Their job is to drive the Higgsfield elevation and lock the radius across variants.

## 4. Higgsfield hero batch · STAGED (per-batch approval, not run)
Prompts ready in `../MADE_WORLD_PIPELINE/01_prompts/HIGGSFIELD_BATCH_001.md` (5 stills: hero, variant grid, before/after, placard still, edition still). With the Blender base now built, the batch runs as IMG-TO-IMG / reference on `tray_hero_ceramic_v2.png` + `tray_hero_aluminum.png` to lock geometry and elevate to photoreal material + light. Credit balance live = 1977.62. Estimate ~20-30 credits for batch 001. NOT run: awaiting the per-batch yes.

## 5. Adobe finish pass · STAGED
Adobe is auth and crop/color/adjust are available, but it needs the asset as a URL/assetId (local renders enter via the file picker, which is an operator action). Plan unchanged: crop masters (the ratios), color law (one accent, white sweep >=250), texture cleanup, text-safe zones, compression, platform exports, QA sheets. Executes once there are elite generations to finish (or on the Blender selects via the picker).

## 6. Motion pass (AE / Premiere) · STAGED
Premiere is verified live; AE needs its bridge panel open. Motion comes AFTER the locked hero still (lock the still, then animate, never full-clip one-shot). Plan: a 6s loop (slow quarter-rotate of the locked hero), a 15s Reel/TikTok cut (hook + swap + rule placard + loop), a 30s hero cut, caption-safe lower third, near-silent with one soft click, platform export specs. A Blender turntable of the exact geometry is the lowest-drift motion option and can be rendered free once approved.

## 7. Figma experience · STAGED (build with real assets)
Figma authed. Plan: Home / Drops / `/drops/the-one` / signal-capture, mobile + desktop, with a real design-system library (tokens, type, the 9-grid, vote module, the mark). Build once the elite hero assets exist so it is not a placeholder mock.

## 8. Platform mastering · STAGED
Per the Week 1 package: TikTok / IG Reels / IG carousel / YouTube Shorts / Threads / LinkedIn / Pinterest / email, each with asset + caption + CTA + signal tested. Executes after finals exist.

## 9. QA gate (the standard; the Blender base was run through it this session)
Stops scroll in 1s · looks expensive · looks ownable · no AI gloss · object reads instantly · concept reads without explanation · works across page/grid/post/email · beats placeholder 10x · "where can I get this." Plus the External Visual Proof Gate (a human signs off; Claude is not the final visual authority). The Blender base passes as a reference, NOT as an elite final (it must clear the full gate after the Higgsfield + Adobe passes).

## 10. File structure (created)
`MADE_WORLD_RUN_001/`: `00_brief` · `01_blender` (5 renders) · `02_higgsfield_prompts` · `03_raw_generations` · `04_selects` (4) · `05_adobe_finals` · `06_motion` · `07_figma_exports` · `08_platform_masters` · `09_qa` (QA note) · `10_signal_ledger`.

## 11. Final deliverable summary
- Pipeline map: Blender base (DONE) -> Higgsfield elevation (staged, spend) -> Adobe finish (staged) -> Figma page (staged) -> AE/Premiere motion (staged) -> platform masters -> QA + External Visual Proof Gate.
- Connector status: section 1 (all 6 live; honest limits noted).
- Assets produced: 5 real Blender renders (4 selected), geometry-exact base references; QA loop executed (1 fail caught + fixed).
- Prompts: HIGGSFIELD_BATCH_001.md (ready, img-to-img on the base).
- The exact next approval question before any credit spend: in the chat message.

---
*Live tools exercised: Higgsfield (read-only balance), Premiere (ping), AE (help), Blender (real build + 8 renders), Figma (whoami), Adobe (init + account). Spend tool NOT run. No posting/ads/rails/auto-continue/global-always-allow. Per-batch permission preserved. Base renders are references, not finals.*
