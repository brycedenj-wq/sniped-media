# GARMENT FIDELITY RULES · Alma Love cherry bikini
Hard law: the world can be stylized, the product cannot be guessed. Every product-visible generation and grade obeys these. A beautiful wrong bikini is a failed commercial.

## LOCKED (must reproduce exactly, never stylized away)
1. COLOR: true warm red, print-red anchor #B84A40 (hue ~3-8deg). Ivory base #D5CAC9 to #CFC1BE. Keep G slightly above B. Never coral (hue >18deg), never pink (B>G), never washed/peach.
2. CHERRY: ONE rhinestone-pave cherry pair on the RIGHT cup only. NO cherry on the left cup. NO cherry on the front bottom panel. ONE rhinestone cherry charm at center-back waistband. Raised rhinestone, not flat-printed.
3. PRINT: coral-rust feather-fan dotted-plume swirl on ivory. Not solid, not snakeskin, not flat tropical leaf.
4. CONSTRUCTION: string-triangle halter (unstructured cups), low-rise high-cut cheeky side-tie bottom, hip bows high on the bone with long capped tails.
5. DICE HARDWARE: exactly 3 silver (never gold) engraved dice cubes per tie tail, recessed pips, random values, frayed fabric tips. Visible where the tie ends are in frame.

## ALLOWED TO STYLIZE (the world, not the product)
- Lighting, world, location, grade mood, grain, halation, camera motion, the Mercedes, palms, gas station, night neon. These are the stylized layer.
- The garment color may shift with diegetic light WITHIN the warm-red family (golden hour warmer, night deeper) but must never cross into coral (hue >18) or pink (B>G).

## THE RECURRING AI ERROR TO KILL
AI on-body beats render the cherries as LARGE FLAT-PRINTED graphics baked into the fabric AND add a non-existent cherry on the bottom-front panel. This is wrong on two counts (flat not rhinestone; extra cherries). Fix priority: regen close-ups; at wide/medium distance the error is mitigated and grade-only is acceptable for secondary shots.

## DISTANCE TIERS (how strict per shot)
- PRODUCT-CRITICAL (tight/close, product is the subject): every locked rule must read correctly. Cherry style, count, placement, dice, color all enforced. Regen if wrong.
- SECONDARY (wide/medium/night, product incidental): color family + construction must be right; the flat-vs-rhinestone cherry and exact dice count are not resolvable and are tolerated. Grade-only.

## GENERATION RULES
- Always feed the real control frames as reference (per the source map). Never use the asset folder as general inspiration.
- For on-body regens, lock the garment from _94A2655 (front) / _94A2806 (back) / _94A2812 (cherry) / _94A2810 (dice).
- After any generation, run GARMENT_QA_GATE.md before accepting. Gate again after grade.

## GRADE RULES (true cherry-red correction)
- Target the print-red to #B84A40 family. If a beat reads coral/peach (golden hour, raw WB), pull hue from ~18deg toward ~5deg and hold saturation; keep G slightly above B.
- Do not crush the ivory to pure white; hold it warm at #D5CAC9.
- Apply the correction per-beat so all beats share one product color across the cut (the day-vs-night tone split must close).
