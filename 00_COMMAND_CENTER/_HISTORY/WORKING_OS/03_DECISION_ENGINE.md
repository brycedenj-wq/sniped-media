# 03_DECISION_ENGINE · decision and prioritization reference

A thin reference for how the OS makes hard calls. LIVE engines: `sniped-decide`, `boardroom` (multi-agent deliberation), and `adversarial-verify` (serious-work QA), invoked via the Skill tool. Source: `SNIPED_OS/00_BRIEF/DECISION_TOOLKIT.md`, `sniped-canonical-truths`, `sniped-execution-prioritization`, `00_COMMAND_CENTER/OS_ACTIVATION_INDEX.json`.

## Canonical truths (every decision inherits these)

proof over theory; action first, not a report; NEVER SAMPLE (whole-read and whole-watch); hard production runs through a harness, not a single thread; cite the doctrine, skill, or gate used; disclose any unverified pile; today's proof plus the operator's live instruction override old docs.

## Decision frameworks (invoke when)

premortem (risk), Fermi (estimation), Munger two-track (trade-offs), superforecasting (prediction), signal-noise-Bayesian (noisy data), cognitive-bias-audit (thinking errors), bad-strategy-audit (strategy quality), shadow-test (unproven hypothesis).

## Seriousness classifier

Serious = a hard production domain (film, photo_composite, editing_retouch, brand_campaign, web_build) OR two or more domains touched OR a serious keyword present. Serious work produces an OS_RECEIPT.md and runs through a harness. One agent may not select, cut, grade, review, and crown its own work.

## Harness dispatch

- boardroom: multi-agent deliberation, contradictory counsel, high-stakes strategy.
- adversarial-verify: QA on serious work, whole-reads, contradiction hunting.
- single-thread: casual drafting and low-risk notes only.

## Emergency dispatch

Emergency keywords (deadline, right now, time-boxed) trigger `emergency-drop-protocol`: cut SCOPE not quality; never relax identity, legal, vision-reject, or brand-core gates; label the output honestly.

## State liaison

A decision that contradicts STANDING_ORDER or NEXT_ACTION is surfaced and requires an operator override before proceeding.

## Dependency flag

`sniped-decide` currently resolves from `SNIPED_OS/_skills` via the allowlist. Migration into `.claude/skills` is pending (see 10_SKILLS_INDEX.md).

Updated by: operator instruction when decision logic changes. Serious decisions emit an OS_RECEIPT.md noting which frameworks were applied.
