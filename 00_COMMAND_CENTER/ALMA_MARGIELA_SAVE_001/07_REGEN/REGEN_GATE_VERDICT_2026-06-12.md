# REGEN GARMENT + VISION GATE · 3 start-stills · 2026-06-12
Hostile gate against SWIMSUIT_PRODUCT_ATLAS.md + GARMENT_QA_GATE.md before any i2v animation credits. Default = flag. Full-res (2752x1536) source PNGs inspected, not the 1200px view_ previews. Product-critical crops viewed for cherry placement, color hue, faces, hands.

## VERDICT TABLE
| still | beat | color (warm-red family) | cherry placement | cast / faces | AI artifacts | verdict | i2v-start ready | client-safe |
|---|---|---|---|---|---|---|---|---|
| view_INCAR_tank_e91d9a32 | in-car, white tank | n/a (tank state) | n/a · tank graphic correct | matches lead register, deadpan editorial, clean face | hand-on-wheel coherent, no melt | PASS | YES | yes |
| view_PLURAL_club_ff9b9236 | two women, bikinis, cards | warm-red, G-B +20/+24, NOT pink, warm edge | RIGHT woman has a cherry on BOTTOM-FRONT (atlas-forbidden) | both women coherent, distinct, no melt | card faces AI-soft, hands ok | WARN-FAIL (placement) | YES (with caveat) | conditional |
| view_ESTAB_2edeec0d | empty street establishing | n/a (no garment) | n/a | no people (correct) | signage legible, Merc geometry clean, palms clean | PASS | YES | yes |

## PER-STILL DETAIL
### 1. INCAR (tank) · PASS · APPROVED
- Tank graphics ON-BRAND: white rib tank, lowercase "alma love club" text correctly placed center, red halftone DICE graphic lower-left, cherry/dice graphic lower-right. Matches real tank ref _94A2938.jpg.
- Cast: slicked auburn hair, gold hoops, deadpan editorial expression. Reads as the same casting register as CAST_T2 / lead. Face clean (symmetric eyes, no warp).
- AI check: hand on wheel rests on rim, fingers wrap naturally, no extra-finger/melt at full res. Forearm geometry plausible.
- Clean i2v start frame: yes. Replaces the old m06 FAIL cleanly.

### 2. PLURAL (club) · WARN-to-FAIL on placement · CONDITIONAL
- Color: both suits read warm-red feather-fan on ivory. Sampled print zones G-B = +20 to +24 (G above B = correct warm-red; NOT pink). Sits at the warm/coral edge of the band but does not cross into coral/orange. Color PASSES.
- Cherry PLACEMENT ERROR: the RIGHT woman (camera-right) has a prominent rhinestone cherry pair on her bikini BOTTOM-FRONT (low waistband / pelvic panel). The atlas is explicit: cherry belongs on the RIGHT CUP only and "There is NO front-bottom cherry." This is a wrong-placement / extra-cherry error, not a scale-ambiguity. Left woman's cup is print-only at this scale (no extra cherry on her).
- Anatomy: both women coherent and distinct (not duplicated faces, no melt). Faces glamorous, symmetric. PASS on anatomy.
- Hands/cards: card-dealing hands mostly coherent; no gross extra-finger melt; playing-card faces are AI-soft/indistinct (typical). Acceptable for a wide beat.
- Net: this is a real product-truth violation (bottom-front cherry). Per the gate, a wrong cherry placement at a resolvable scale is a fidelity FAIL on that woman, even though color + anatomy pass. The cherry IS resolvable here (it is large and front-and-center), so this does not get the WARN-tolerant pass reserved for unresolvable scale.

### 3. ESTAB · PASS · APPROVED
- Clean Americana establishing: palm-lined boulevard, double-yellow centerline, empty street, no people, no garment.
- Signage: "BEVERLY DR..." reads legibly (not gibberish scramble); striped awning + storefronts coherent. Background signage softer but not prominent-gibberish.
- Car: black classic Mercedes (matches the convertible in other beats), correct hood-star, round wheels, coherent panels; license plate an indistinct smudge (acceptable for establishing). Palms clean, perspective coherent.
- Clean i2v start frame: yes.

## APPROVED TO ANIMATE
- INCAR (tank): APPROVED.
- ESTAB: APPROVED.
- PLURAL: HOLD. Color + casting + anatomy are good and the beat is strong, but the right woman's bottom-front cherry is an atlas violation. Two options: (a) accept as a SECONDARY beat only if the cherry is masked/painted out of the bottom-front before lock, or (b) reroll the right-woman garment.

## REROLL PROMPT (PLURAL right woman only · if not patching)
"Two women in matching warm-red cherry-print string bikinis (true warm-red feather-fan/dotted-plume swirl on warm ivory, hue ~5deg, NOT coral, NOT pink) on the hood of a black classic Mercedes convertible, palm-lined Beverly street, golden hour, dealing playing cards. CRITICAL GARMENT TRUTH: each bikini has exactly ONE small rhinestone cherry pair on the wearer's RIGHT CUP ONLY (upper-inner near cleavage). NO cherry on the bikini bottom, NO cherry on the front waistband, NO cherry on the left cup, NO extra cherries anywhere. Bikini bottoms are plain feather-fan print with side-tie hip bows and silver (not gold) dice-bead tie ends. Editorial deadpan, glossy 1990s glamour, clean hands and clean playing cards."

## CROPS (evidence, /tmp/alma_gate/)
INCAR_upper, INCAR_face, INCAR_armwheel · PLURAL_right_full (bottom-front cherry visible), PLURAL_left_cup, PLURAL_hands, PLURAL_leftface · ESTAB_signage, ESTAB_car, ESTAB_right.
