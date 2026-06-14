# ALMA LOVE CLUB · FILM BIBLE (holistic rebuild) · 2026-06-13

The v1/v2 cuts read as "different versions pieced together" because the beats were generated piecemeal (drifting garment color, inconsistent character/world/grade). This rebuild generates ONE coherent beat set as a single shoot, locked to fixed references, then gates -> animates -> upscales -> grades -> adversarially verifies.

## LOG LINE
A deadpan woman moves alone through a sun-bleached, empty Beverly Hills. The house always wins. Love is a gamble.

## NON-NEGOTIABLE LOCKS (every beat inherits these)
- CHARACTER: the established synthetic lead, ref `f3173029` in EVERY on-body generation. Golden-tan, short slicked copper crop, gold hoops, big dark 70s sunglasses, deadpan, red lip. Same woman in every frame.
- PRODUCT (exact, true-red): ivory cherry-print STRING-TRIANGLE HALTER bikini. TRUE DEEP WARM RED print, anchor #B84A40 (hue 3-8deg), NOT coral, NOT orange, NOT pink. ONE rhinestone cherry pair on the RIGHT cup only (none on left, none on bottom-front). EXACTLY 3 silver (not gold) engraved dice cubes per tie tail. Side-tie hip bows, cheeky bottom. Garment ref `3a11d999`.
- WORLD: empty sun-bleached Beverly Hills palm boulevard + a black 1972 Mercedes 280SE convertible. Deep saturated blue sky by day; warm headlight key by night. Day -> night arc across the film.
- LOOK: 35mm Kodak Portra, warm hazy noon, hard editorial, deadpan, film grain + halation, vignette. One grade in finish.
- GRAMMAR (Margiela "Mutiny"): hard cuts only, violent wide<->tight scale alternation, earned holds on tableaux (3-4s), handheld-feel, ~2.0s ASL, day-to-night.
- MODEL ROUTING: on-body bikini beats -> `nano_banana` (NON-pro, moderation-safe per [[higgsfield-moderation-bypass]]). World/no-person + product macros -> `nano_banana_pro` for max detail. Animate approved stills via Kling 3.0 i2v (anti-drift). 4K via bytedance upscale.

## BEAT SHEET (one coherent film, ~30s, day -> night)
| # | beat | scale | garment state | action (subject ACTS) | model |
|---|------|-------|---------------|------------------------|-------|
| 1 | DICE MACRO (hook) | XCU | product only | silver dice on tie-tails, rack focus | macro (have: dice v) |
| 2 | ESTABLISH | XWIDE | none | empty boulevard, Mercedes at curb, heat shimmer | pro |
| 3 | HERO | WIDE | full bikini | stands by the Mercedes door, deadpan to camera | non-pro |
| 4 | CHERRY MACRO | XCU | product only | rhinestone cherry, muted sage stem, rack focus | macro (have: cherry v2) |
| 5 | IN-CAR DRIVE | MED | top worn | at the wheel, sunglasses, slow head turn | have (1b294dc2) |
| 6 | WALK | WIDE | full bikini | walks away down the boulevard, boombox behind | non-pro |
| 7 | GAS STATION | MED-WIDE | full bikini | leans on a vintage gas pump, empty Americana | non-pro |
| 8 | PLURAL / CLUB | MED | tops worn | she + ONE distinct friend deal cards on the hood, cash down | non-pro |
| 9 | MIRROR / hood product | CU | product detail | exact product, true-red | macro/PNG |
| 10 | SOLITAIRE | HIGH | full bikini | crouched, deals a hand of cards on the asphalt | non-pro |
| 11 | GAMBLE CARD | card | type | "LOVE IS A GAMBLE." Didot, brand red | motion-gfx |
| 12 | NIGHT PAYOFF | WIDE | full bikini | stands in the Mercedes headlight wash, night | non-pro |
| 13 | END CARD | card | logo | ALMA LOVE CLUB wordmark + TEXT LOVECLUB CTA | motion-gfx |

## PIPELINE GATES (do not advance until passed, fresh-context harness)
1. STILLS gate: character-match to lead + garment-fidelity (true-red, cherry placement, dice) + world continuity. Reject + regen failures.
2. MOTION gate: no wardrobe drift, authored motion (subject acts, not still+push), garment holds.
3. FINISH gate: one grade, audio <= -1 dBTP / ~-14 LUFS, 4K, cards/CTA correct.
4. ADVERSARIAL: every dimension >= 9 floor or named blocker + path.
