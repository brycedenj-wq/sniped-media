# WAVE 2 MOTION + PRODUCT-FIDELITY GATE · 2026-06-13
Harness: alma-motion-product-gate (25 agents, 17 clips, fresh judge + adversarial verify per clip). Truth = real EVOTO product + atlas. Law = PRODUCT_FIDELITY_MOTION_LAW.md.

## HEADLINE (honest)
0 of 6 hero product beats survived. The motion stage degraded product fidelity that the keyframes had held. The 8 clips that pass are all B-ROLL inserts (garment not in frame, or product-correct but static). The film CANNOT assemble yet: we have inserts but no product heroes.

## VERDICT TABLE
| beat | tier | verdict | the defect (why) |
|---|---|---|---|
| b01 lens-wipe | critical | KEEP_BROLL | product PERFECT across all 3 frames, but subject static after the wipe = transition/insert only, not a hero |
| b02 step-in | secondary | KEEP_BROLL | feet/calves only, garment not in frame; clean arrival insert |
| b03 speaker | critical | KEEP_BROLL | suit holds but color bleaches pinkish under sun + too wide to read cherry/dice; supporting wide only |
| b04 button | secondary | KEEP_BROLL | hand only; dice-bow palette-consistent; detail insert |
| b05 kick | secondary | KEEP_BROLL | ankle only; real kick arc; insert |
| b08 tug+dog | secondary | KEEP_BROLL | no garment in frame; bracelet on wrist (flag); lifestyle insert |
| b14 rearview | secondary | KEEP_BROLL | face only, no garment; atmosphere insert |
| b16 cigarette | secondary | KEEP_BROLL | product correct, but only smoke moves (static); 1-2s cutaway only |
| b06 walk-off (BACK HERO) | critical | **CUT** | PRINT MUTATED: bottom became scattered cherry-novelty print on cool white, not feather-fan on warm ivory. Wrong fabric. |
| b07 handcuff | secondary | **CUT** | WRONG GARMENT entirely: dark-burgundy cherry-print sleeve cuff at the wrist, not the bikini tie |
| b09 trunk reveal (BACK HERO) | critical | **CUT** | color coral/salmon (hue>18) + center-back rhinestone cherry charm ABSENT. (this was the proof clip; it failed the back-charm + color) |
| b10 towel | critical | **CUT** | color peach/rose-gold + a GOLD CHAIN necklace imported + print unconfirmable at width |
| b12 palm-beauty (FRONT HERO) | critical | **CUT** | color collapsed to dark burgundy, ivory ground gone, print unreadable, near-static |
| b13 bikini-top (THE PRODUCT) | object | **CUT** | print became floral/tropical (not feather-fan), coral, dice absent, exits frame |
| b15 recline | critical | **REROLL** | suit itself CORRECT (warm-red, cherry right cup, print holds) but a NECKLACE is on the body |
| b17 gas station | critical | **REROLL** | wide framing hides print/cherry (critical = unverifiable is fail) + near-static |
| b18 poster (FRONT HERO) | critical | **REROLL** | necklace imported + color drifted coral/salmon + push-in only |

## KEEP / REROLL / CUT
- KEEP_BROLL (8, product-safe, INSERT ONLY, never a product hero): b01, b02, b03, b04, b05, b08, b14, b16.
- REROLL (3, fixable): b15 (kill necklace), b17 (tighter framing + motion), b18 (kill necklace + color lock + motion).
- CUT / full re-do (6, product fundamentally wrong): b06, b07, b09, b10, b12, b13.

## ROOT CAUSES (so the re-do actually fixes it)
1. COLOR: keyframes rendered coral (grade-deferred). MOTION AMPLIFIED it to salmon / rose-gold / burgundy under diegetic light. Per the law, a coral hero = CUT, NOT a grade note. So color must be TRUE warm-red #B84A40 IN the keyframe before animating, not fixed later.
2. PRINT MUTATION in motion: Seedance hallucinated the fabric over 5s (feather-fan -> cherry-novelty on b06; -> floral on b13). Start-image alone did not hold the print.
3. NECKLACE INHERITED: the keystone (KF18, job 49271d5b) carries the real model's larimar pendant; front beats chained to it inherited it (b15, b18; b10 grew a gold chain). The keystone itself must be regenerated necklace-free.
4. WIDE FRAMING: b03/b17 too wide -> print/cherry unresolvable -> critical-tier auto-fail.
5. STATIC MOTION on correct product (b01, b16): product fine, no performance -> demoted to B-roll.

## THE FIX (hero re-do, stronger locks per the law) - next work block
1. SOURCE FRAMES: regenerate the 9 hero/reroll keyframes (b06,b09,b12,b18 front+back heroes; b10 towel; b13 top; b03,b17; + necklace-free keystone) with HARD negatives (no necklace/pendant/chain; no coral/salmon/peach/burgundy; no cherry-novelty/floral print) and the real graded product as reference; then POST-RECOLOR the print region to #B84A40 so the start frame is true warm-red. Re-chain to a necklace-free, color-true keystone.
2. GARMENT ELEMENT LOCK: create a Seedance reference Element from the real product (show_reference_elements) and pass it to each hero motion gen for print/color continuity.
3. SHORTER DURATION 3-4s on heroes to cut drift.
4. TIGHTER FRAMING (medium/3-4) on b03/b17 so print+cherry read; add an authored motion verb (weight shift, quarter-turn) to defeat static.
5. RE-GATE every re-done clip through this same harness before it is allowed near assembly or Topaz.

## STATUS: NO-SEND. NO-ASSEMBLE. Heroes blocked on the re-do above. The 8 B-roll inserts are banked and product-safe. Topaz only after a clip passes.
