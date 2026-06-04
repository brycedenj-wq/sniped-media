# PHASE 2 SPEC FIX , identity recovery from model drift (2026-06-04)

> RUN-001 lesson applied: a sub-pixel signature mark must not be a HARD gate. The character system now recovers from model drift without breaking identity, hiding edits, or wasting motion credits.

## Changes
1. **Mole demoted HARD -> SOFT** in `char_axis_01/CRS.json`. The TRUE identity structure is four HARD pillars: **eye_color, face_geometry, build, complexion**. The mole is a `signature_detail`, not a gate.
2. **Mark-injection stage** , `scripts/os_mark.py inject` restores a dropped signature deterministically: writes a NEW asset (never overwrites the source) and a mandatory `MARK_INJECTION_LOG.csv` row. Silent/in-place/reasonless edits are refused.
3. **Tight identity-verification frame** , sheet plan now has **15 frames** (frame 15 = `identity_lock_tight`, a face-only macro). New `os_crs.py verifycrop <image>` produces a deterministic face crop+zoom so face-level invariants are checkable (formalizes RUN-001's manual crop).
4. **Gate logic** , already hard-only; demoting the mole means a missing signature no longer quarantines while the four pillars still do.
5. **Guard fix** , the identity-leak patterns were globally case-insensitive, so `[A-Z]` matched lowercase and "model drift" looked like a real name. Capital-letter name detection is now case-sensitive via scoped `(?i:...)` flags.

## Tests (all green)
| Suite | Result |
|---|---|
| test_crs.py | 26 / 0 |
| test_mark.py | 8 / 0 |
| test_world.py | 6 / 0 |
| test_motion.py | 10 / 0 |
| test_skill_substrate.py | 11 / 0 |
| test_production_harness.py | 14 / 0 |
| **Total** | **75 / 0** |

New regression coverage proves: missing mole + 4 pillars hold -> NOT quarantined; wrong eyes/face/build/complexion -> still quarantines; injected mark must be a new logged asset (no silent/in-place edit); "model drift" no longer false-flags while "actor Smith" still does.

## Docs updated
`char_axis_01/CRS.json` (+ regenerated 15-frame SHEET_PLAN), `sniped-crs-builder` skill (still ACTIVE), production `PACKAGE.json` v2, `OS_SKILL_DASHBOARD.md`. AXIS CRS re-validates VALID (4 hard pillars, leak-clean).

## Result
The atom can now absorb model drift on a fragile detail and recover via a logged retouch, without lowering the real identity bar. Cleared for the one approved corrected hero rerun (2 credits).
