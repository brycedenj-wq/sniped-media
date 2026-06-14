# CLIENT VISION ATTRACTION GATE (V2, operator-locked 2026-06-13)
Technical continuity is NOT enough. The lead and film must carry LA luxury sex appeal + deadpan awkward humor, with the product as the hero. Gate the IDENTITY before any V2 insert is generated.

## THE BAR (all must hold, simultaneously)
same woman across the cut + EXACT coral-on-cream real product suit + LA/Beverly Hills summer sex appeal + luxury swimwear confidence + deadpan awkward personality + brand-safe (sexy not pornographic) + product stays the hero.

## THE LEAD MUST FEEL LIKE
- she belongs in LA / Beverly Hills summer (warm sun, palms, Mercedes, rich-girl weirdness)
- she can SELL swimwear (presence, not a random AI mannequin)
- she has face/card/poster presence
- confident, stylish, slightly strange, expensive
- sex appeal WITHOUT breaking brand safety
- deadpan: serious, mannequin-still, never mugging

## HARD REJECTS (any = fail)
necklace, wrist bandana, any non-spec styling; suit not exact coral-on-cream; pornographic/explicit; random/weak/flat mannequin with no presence; wrong woman; gold hoops inconsistent across beats.

## NOT-A-PASS RULES (operator)
- technically consistent woman with no sex appeal = NOT a pass.
- sexy shot with the wrong suit = NOT a pass.
- beautiful shot with the wrong woman = NOT a pass.
- funny beat with no luxury = NOT a pass.
- luxury beat with no deadpan personality = NOT a pass.

## V2 PROCESS (do not skip steps)
1. CAST + build IDENTITY_CASTING_SHEET: 6-12 stills, varied (front / side / back / by car / by palm / poster / close / medium / wide), same hair + face + body energy, BARE NECK, no non-spec styling, LA luxury swimwear energy + sex appeal + deadpan.
2. CASTING JUDGE (fresh-context harness): same woman? LA vibe? sex appeal? luxury swimwear? deadpan awkwardness? brand-safe? product-seller? -> PASS/FAIL. If FAIL on presence/attraction, RECAST a stronger lead (do not lock a weak-but-consistent frame).
3. Only after PASS: TRAIN/LOCK Soul V2 on the approved lead frames.
4. RE-RENDER V2 inserts using Soul V2 identity + garment Element (132fd9cb) + the client-vision prompt (LA luxury sex appeal + deadpan), correct beat/location/prop, authored motion per mode.
5. GATE every insert on BOTH: technical (identity continuity, product fidelity coral-on-cream, no text/tells, no wrong objects) AND client-vision (LA vibe, sex appeal, deadpan tone, luxury).
6. REASSEMBLE V2 only from clips passing BOTH gates. Restore the towel comedy peak. 4K text/plate sweep. Re-run alma-final-verify. Crown only on a clean >=9/10.

## CASTING VERDICT (2026-06-13, harness alma-casting-attraction-gate): PASS 7.7/10. Lead LOCKED (same woman + LA sex appeal + luxury + deadpan + brand-safe + product-seller, all sub-criteria PASS). Defects = hygiene not casting.
SOUL TRAINING SET (prop-clean): cast1_closeup (f7779d2c, primary face), cast2_medium (511b00cc, support), cast4_palm_low (824d1c63, low weight) + new clean anchors below. cast0/cast3/cast5/cast6 = reference-only (drink/dog contamination).
CARRY-FORWARD NEGATIVES (every Soul gen + insert): "iced drink, cocktail, cup, glass, beverage in hand; dog, bulldog, pet, animal; necklace, jewelry, wrist bandana, readable text, signage, logo". POSITIVES: "same woman, red lip, aviator sunglasses, coral-on-cream cherry-print swimsuit, warm golden-hour".
TODO before client floor: clean drink-free dog-free keystone + one clean full-product front tile; confirm identity at higher res.

## LOCKS (V2)
- LEAD: Soul V2 `soul_id = 2d31efbd-34b7-4714-9e01-2a4360e4e067` (alma-lead-deadpan), training on 6 clean anchors (f7779d2c, 511b00cc, 824d1c63, 21f32aa2, 3f42af5b, d38871f1). Use with model `soul_2` (or soul_cinema_studio). ~10 min to ready.
- SUIT: garment Element `132fd9cb-f743-4a50-aee8-1a7f4a492906` (embed <<<...>>> in motion prompts; Seedance/Kling lock).
- WORLD: Beverly Hills palm boulevard + black 1972 Mercedes, warm golden hour.
- TONE: deadpan luxury, mannequin-still, never mugging.

## V2 INSERT RE-RENDER PLAN (after Soul ready)
Re-render the weak first-pass beats Soul-locked + correct beat/location/prop + authored motion + carry-negatives:
- b01 lens-wipe (front reveal), b02 step-in (low feet, NO desert), b03 speaker (PROP must read as a speaker, fidget gag), b04 hand-on-BUTTON (real speaker button macro, NO car hood, NO bandana), b05 kick (boulevard NOT desert), b08 leash POV (flat 0.5x wide NOT porthole, TAN leash + bulldog ok here), b14 rearview (solo lipstick), b16 cigarette (tight, color hold). RESTORE b10 towel (concealment, plate-clean). Optionally a fresh gas WORLD beat with motion.
Method per beat: generate keyframe = model soul_2 + soul_id 2d31efbd + describe coral-on-cream suit + carry-negatives -> Seedance i2v from that keyframe + Element <<<132fd9cb>>> + micro(luxury)/authored(chaos) motion -> gate technical + attraction -> keep only dual-pass.
HEROES carry over (re-check vs attraction): b18 poster, b12 palm-beauty, b09 back-reveal, b06 walk-off; b15 recline likely re-render (verify flagged off-model). End card ships as-is.
Then reassemble V2 (16:9) -> mild coral-on-cream unify grade -> music + SFX + end card -> 4K text/plate sweep -> re-run alma-final-verify -> crown only on clean >=9/10. send_no_send stays NO.

## LOCK ORDER: cast the lead -> lock the lead (Soul) -> lock the suit (Element) -> lock the world (Beverly Hills) -> lock the tone (deadpan luxury) -> gate before assembly.
## CARRY-OVER (keep, already gated technical + product): heroes b18 poster, b12 palm-beauty, b09 back-reveal, b06 walk-off, b15 recline (re-check against the attraction gate; the verify flagged recline as off-model, so recline likely re-renders). End card ships as-is.
