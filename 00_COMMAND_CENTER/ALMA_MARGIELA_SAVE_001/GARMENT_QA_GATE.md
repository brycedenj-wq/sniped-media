# GARMENT QA GATE · Alma Love cherry bikini
Reusable pass/fail gate. Run BEFORE accepting any product-visible generation and AGAIN after grade. Gate against SWIMSUIT_PRODUCT_ATLAS.md + GARMENT_FIDELITY_RULES.md. A beautiful wrong bikini is a FAIL.

## INPUTS
- The shot/frame to gate.
- The controlling real photo (from SHOT_GARMENT_SOURCE_MAP.md).
- The shot tier: product-critical or secondary.

## CHECKLIST (mark PASS / FAIL / NOT-RESOLVABLE per item)
1. COLOR: print-red reads in the warm-red family (#B84A40 anchor, hue 3-8deg). G slightly above B. Not coral, not pink, not washed.
2. PRINT: coral-rust feather-fan dotted-plume swirl on warm ivory (not solid, not snakeskin).
3. TOP: string-triangle halter, unstructured cups, thin self-fabric binds.
4. CHERRY PLACEMENT: ONE rhinestone cherry on the RIGHT cup only. NO left-cup cherry. NO front-bottom cherry. (product-critical: enforce; secondary: tolerate flat-vs-rhinestone but no EXTRA cherries in close read)
5. CHERRY STYLE: raised rhinestone-pave (two berries + muted stem), not a large flat-printed graphic. (product-critical only)
6. BACK: center-back rhinestone cherry charm below the back-band bow; cheeky-brazilian cut. (only if back in frame)
7. BOTTOM: low-rise high-cut cheeky, side-tie hip bows high on the bone, capped tails.
8. DICE: 3 silver (not gold) engraved dice cubes per visible tie tail, recessed pips, frayed tip. (only if tie ends in frame)
9. IDENTITY: no necklace/cuffs reproduced as garment.

## THRESHOLDS
- PRODUCT-CRITICAL shot is CLIENT-SAFE only if items 1-5 (and 6/8 when in frame) all PASS. Any FAIL = REGEN.
- SECONDARY shot is CLIENT-SAFE if items 1-3 PASS and item 4 has no EXTRA cherries visible at the shot's distance; flat-vs-rhinestone (5) and exact dice count (8) may be NOT-RESOLVABLE and still pass.
- ANY wrong base color (white instead of ivory), absent print, or wrong-garment = FAIL, not client-safe, regardless of distance.

## VERDICT FORMAT (log per shot)
shot | tier | items_failed | verdict PASS/WARN/FAIL | client_safe yes/no | fix (grade-only / regen / drop)

## CURRENT STATE (2026-06-13, logged)
9 of 10 product-visible shots client-safe. m06 (in-car) is the only FAIL/not-client-safe (wrong garment) and must regen. m04/m09 are the real product (reference standard). See SHOT_GARMENT_SOURCE_MAP.md for the full per-shot log.
