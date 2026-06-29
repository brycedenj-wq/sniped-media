> **Retired 2026-06-28.** One or more OS_* systems referenced in this document were retired during the OS repository convergence and moved to `_HISTORY/` or `_ARCHIVE/`. Those references are historical and no longer active. See `CONVERGENCE_PLAN_2026-06-28.md`.

# DECISIONS INDEX

The OS decision log. The `decisions/` folder existed but was empty (OS_TAKEOVER Phase 4 finding); real decisions were scattered across flat files in the command center. This index points to them in place (no files moved) and defines the standard decision-record schema so future decisions are logged consistently.

**Rule:** every founder-level or lane decision gets a record here (or a linked file) with the why, not just the what. A decision without recorded options + rationale + kill-criteria is not logged.

## Standard decision-record schema
```
DECISION <id>
- date:                 # absolute date
- decision:             # the call made, one line
- options_considered:   # the real alternatives, not just the chosen one
- rationale:            # why this option (the why, not the what)
- reversibility:        # reversible | costly-to-reverse | one-way-door
- kill_criteria:        # the signal that would reverse or stop this
- outcome_status:       # open | acting | done | reversed | superseded
- source_file:          # where the full record lives (if a separate file)
```

## Indexed decisions (in place, not moved)
| id | decision (one line) | source file | status |
|----|---------------------|-------------|--------|
| lane-discovery | Forward mission = lane discovery; older projects = capability proof/archive | `LANE_DISCOVERY_LEDGER.md` | acting |
| capability-decisions | Which capabilities to build vs defer | `OS_CAPABILITY_DECISIONS.md` | acting |
| game-pipeline | Higgsfield image-to-3D game pipeline adopted (Gridiron Royale proven) | `OS_GAME_PIPELINE_DECISION.md` | done |
| grand-money-play | The primary monetization play | `OS_GRAND_MONEY_PLAY_DECISION.md` + `_ANSWER.md` | acting |
| public-wrapper | Public wrapper / packaging decision | `PUBLIC_WRAPPER_DECISION.md` | open |
| kin-and-light | KIN AND LIGHT direction call (2026-06-02) | `KIN_AND_LIGHT_DECISION_2026-06-02.md` | done |
| decision-judgment | Decision-judgment process plan | `DECISION_JUDGMENT_PLAN.md` | reference |
| alma-video-retire | Alma video lane RETIRED + refunded $300; PHOTO lane is the live work | memory `alma-realistic-3model-pivot` + `NEXT_ACTION.md` guard | done (one-way) |
| corpus-mission | Continuous refinery: metabolize all intentional sources to SCHEDULED=0 | `OS_REFINERY_AUTONOMY_001/REFINERY_MASTER_STATE.json` + memory `continuous-refinery-mission` | done (books + docs reconciled 2026-06-21) |
| ii-exception | Intelligent Investor excerpt -> EXCEPTION (no-spend, no acquisition) | `OS_CERT_WAVE_002D/control/close_dispositions.json` | done |
| videos-exception | 6 photography videos -> EXCEPTION (transcription needs spend; operator chose no-spend) | `OS_DOCS_TOOLING_001/OS_RECEIPT.md` | done (reversible if a Whisper key is added) |

## Open / pending decisions (need an operator call)
- Whether to add a Whisper key to enable the 6 EXCEPTION videos (currently no-spend EXCEPTION).
- Whether to execute the remaining OS_TAKEOVER structural fixes (complete the 68 INSTALLED_INCOMPLETE skills; archive-zone move; routine piloting).

## How to add a decision
Append a record using the schema above (inline here for small decisions, or a linked `*_DECISION.md` for large ones) and add a row to the index table. Do not bury a decision only in chat or a project file.
