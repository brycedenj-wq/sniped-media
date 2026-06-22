# ARCHIVE ZONE PROPOSAL (proposal only - NO files moved)

Phase 4 audit finding: there is no formal archive zone; retired/closed lanes are preserved in-place and mixed with active work, so a fresh session cannot tell active from done at a glance. This proposes a structure and a no-move interim. Moving files is a SEPARATE operator-approved action; this pass moves nothing.

## Proposed structure (when the operator approves a move pass)
`00_COMMAND_CENTER/_archives/` with subfolders:
- `retired_lanes/` - lanes that are dead/refunded (do not influence new work).
- `closed_programs/` - finished waves/programs kept for audit (read-only).
- `demos/` - one-off demo packages.

## Interim (no move) - mark, do not move
Until a move is approved, each candidate keeps a top-level `_ARCHIVED.md` marker (like KEN FILM already has `_STATUS_SHELVED.md`). This index is the source of truth for active-vs-archived; nothing is relocated.

## Candidates (verify before any move; status from memory/receipts)
| candidate | path | reason | marker present? |
|-----------|------|--------|-----------------|
| KEN FILM (Alma video lane) | `~/Downloads/KEN FILM/` | RETIRED + refunded $300 | YES (`_STATUS_SHELVED.md`) |
| FMO / Synergy creative test | `00_COMMAND_CENTER/` refs | DEMOTED 2026-06-10 (back burner) | no |
| THE MEANTIME 001 | `00_COMMAND_CENTER/THE_MEANTIME_001_PER_DIEM/` | closed as FAIL-evidence (capability proof) | no |
| Closed cert waves 002-A..G | `00_COMMAND_CENTER/OS_CERT_WAVE_002*/` | reconciled + receipts; keep read-only | receipts present |
| Docs/tooling program | `00_COMMAND_CENTER/OS_DOCS_TOOLING_001/` | reconciled 50/50 | receipt present |
| Demo packages | `OS_MAX_DEMO_001/`, `OS_PRIVATE_DEMO_PACKAGE_001/` | one-off demos | no |

## Rules
- This is a PROPOSAL. No deletion, no move in this pass.
- Archived lanes do NOT influence new work unless the operator asks for lessons-learned.
- Closed cert waves stay reachable read-only (their control files are the resume/audit trail).
- A future move pass requires explicit operator go and would itself produce a receipt + update NEXT_ACTION + the router.

## Recommended next step
Operator decides: (a) approve the `_ARCHIVED.md` marker pass (low-risk, no move), then (b) optionally a later move pass into `_archives/`.
