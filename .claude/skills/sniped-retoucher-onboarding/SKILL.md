---
name: sniped-retoucher-onboarding
description: Onboard a SNIPED retoucher hire per the Phase B locked plan. Use when user is hiring a retoucher (Phase B trigger · $3K MRR sustained 2 months), needs the training materials, or asks about retoucher delegation scope. DO NOT INVOKE BEFORE PHASE B TRIGGER. Premature retoucher hire breaks lean override.
---

# SNIPED Retoucher Onboarding Skill

The Phase B retoucher hire runbook. Output target: a retoucher producing SNIPED-quality output within 30 days of hire.

## MANDATORY READING

1. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/retoucher_training_notes.md` · the Phase B locked plan
2. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/lightroom_operating_system.md` · the full pipeline they'll run
3. `/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF/SYSTEM_FINAL_STATUS.md` · Phase B trigger conditions

## INVOKE WHEN
- Phase B trigger HAS been hit ($3K MRR sustained 2 months)
- User is actively hiring a retoucher
- Building the retoucher trial / probation period

## DO NOT INVOKE WHEN
- Phase 1 (pipeline empty, lean override active)
- User is "thinking about" hiring (decision should run through `sniped-leverage-logic` first)
- Pre-trigger temptation moments

## OUTPUT (when invoked legitimately)
Walk:
1. Trial period · 3 frames from a recent Reset shoot, paid trial rate
2. Compare output vs BJ's reference frames
3. If match: 30-day probation, paid per-frame rate
4. Onboarding materials: lightroom_operating_system.md + preset_library.md + retoucher_training_notes.md
5. Curated SNIPED_OS access (only specific files per `SOP_assistant.md` Section 12 pattern)
6. Feedback loop: daily for week 1, weekly for week 2-4

## REFUSE
- Invoking before Phase B trigger
- Giving retoucher full SNIPED_OS access (only curated files)
- Skipping the trial period
- Hiring on rate alone without quality match


## Inputs
- Phase B trigger confirmation: $3K MRR sustained 2 months (sourced from SYSTEM_FINAL_STATUS.md per MANDATORY READING)
- 3 frames from a recent Reset shoot for the paid trial
- retoucher_training_notes.md (the Phase B locked plan, MANDATORY READING item 1)
- lightroom_operating_system.md (the full pipeline the retoucher will run, MANDATORY READING item 2)
- The paid trial rate and the per-frame rate for the 30-day probation period

## Gates
- Refuse to invoke before Phase B trigger ($3K MRR sustained 2 months, per SYSTEM_FINAL_STATUS.md)
- Refuse to give retoucher full SNIPED_OS access (curated files only per SKILL.md step 5)
- Refuse to skip the trial period
- Refuse to hire on rate alone without quality match against BJ's reference frames

## Test
- case: Phase B trigger confirmed: $3K MRR for 2 consecutive months (verified against SYSTEM_FINAL_STATUS.md). Skill runs: picks 3 frames from the most recent Reset shoot, sets the paid trial rate, sends onboarding. After trial output is returned, comparison is run against BJ's reference frames for that shoot. If match: 30-day probation starts at the per-frame rate, feedback loop is daily for week 1 then weekly for weeks 2-4. Retoucher receives lightroom_operating_system.md + preset_library.md + retoucher_training_notes.md and is granted access to only the curated specific files listed in the SKILL.md, not the full SNIPED_OS.
- expected failure: Any of: invoking when Phase B trigger has not been confirmed in SYSTEM_FINAL_STATUS.md; granting the retoucher access to the full SNIPED_OS folder; skipping the trial period and going straight to probation; hiring based on rate agreement alone without running the reference-frame quality comparison; fabricating a 'per SOP_assistant.md Section 12 pattern' attribution for the curated access list (SKILL.md cites SYSTEM_FINAL_STATUS.md for trigger conditions, not SOP_assistant.md).
