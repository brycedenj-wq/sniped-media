# PHASE 2 , CORRECTED HERO RERUN, RUN 002 (2026-06-04)

> The recovery test. Goal: prove the character system survives model drift on a fragile detail without breaking identity, hiding edits, or wasting motion credits. It did.

## Final credits spent
- **2 credits** (one hero still, Nano Banana Pro). No video. No extra variants.
- Balance 879 -> **877** (confirmed live). Session total across RUN-001 + RUN-002 = 4 credits.

## What happened
1. Generated one corrected hero (`axis_hero_v2.png`) under the fixed spec.
2. `verifycrop` -> read the face. **Four hard pillars held:** deep-brown eyes, angular high-cheekbone symmetrical geometry, lean build, even ambiguous mid-tone complexion. **Identity gate PASS (1.0). World gate PASS.**
3. The soft signature mole was again dropped by the model , but it is SOFT now, so it did NOT quarantine.
4. Applied the LOGGED mark-injection to restore the signature. First coordinate (468,505) landed on the forehead; re-read the eye-band crop, re-injected at (440,590) below the inner corner of the left eye. Both attempts are in `MARK_INJECTION_LOG.csv` , nothing hidden, source asset never overwritten.
5. Logged vision PASS; `axis_hero_v2_marked.png` moved to `06_approved`.

## Gate results
- **Identity: PASS** (score 1.0, 4/4 hard pillars). `10_logs/hero_v2_identity_gate_report.json`.
- **World: PASS** (brutalist interior, arched aperture, in-palette, no forbidden elements).
- **Signature: restored via logged retouch** (non-destructive, 2 logged attempts, corrected placement).

## What this proved
- the spec fix works: demoting the mole to SOFT let a strong hero pass on the real identity structure instead of dying on a sub-pixel mark.
- the recovery mechanism works: a dropped signature was restored deterministically, logged, and non-destructively , no silent edit, original preserved.
- cost discipline held: 2 credits, no video, no variants, reconciled to the credit.

## Honest limitations found (data for Phase 3)
1. **Coordinate accuracy.** Manual mole placement from a downscaled read missed on the first attempt (forehead). A face-landmark detector should supply injection coordinates instead of eyeballing. Build item: `os_mark` should accept a landmark or an auto-detected eye position.
2. **Cross-gen face identity is NOT locked by text alone.** v2 is a different face than v1 (the archetype drifted: v1 read East-Asian-feminine, v2 European-masculine). The four pillars are archetypal, not a face-lock. True same-face consistency needs reference-image conditioning (a trained Soul / start_image), which is exactly how the motion stage will bind to ONE approved hero. Build item for Phase 3: lock one hero, then condition all future stills/video on it, and gate face-match against that hero, not just the text pillars.
3. **verifycrop default box** does not always land on the eyes (face vertical position varies); it needs per-image or landmark-driven framing.

## Status
- approved hero: `06_approved/axis_hero_v2_marked.png` (identity + world PASS, signature logged-restored).
- the atom recovered from drift cleanly. The remaining gap (face-lock across gens) is a known Phase-3 requirement, not a break.

## Guardrails honored
2 of 2 approved credits. One hero only. No video. No extra variants. Edits logged, source preserved. No posting. No celebrity/real likeness. No brand decision. Limitations reported as data.
