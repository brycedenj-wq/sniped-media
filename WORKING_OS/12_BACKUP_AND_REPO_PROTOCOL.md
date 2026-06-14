# 12_BACKUP_AND_REPO_PROTOCOL · git, backup scope, and the hook fix

## Git state
- Repo root: `/Users/sniper/AI-Brain-Refinery` (the only git repo in the system).
- Cadence: nightly os-backup commits (text and state).
- Bloat: `.git` is about 4.4G because binary media has been committed into history. The actual knowledge text is about 595M. A bloat cleanup is documented, not approved; do not act on it without operator approval.

## CRITICAL FIX (applied 2026-06-14, Phase 1)
`00_COMMAND_CENTER/scripts/os_session_start.sh` searched `"$CC/../00_BRIEF"`, which resolves to `/Users/sniper/AI-Brain-Refinery/00_BRIEF` (does NOT exist), so it fell through on every boot to the STALE `SNIPED_OS/00_BRIEF` state (May 29). The fresh Jun 10 `00_COMMAND_CENTER/NEXT_ACTION.md` was never read.
- The fix (line 9): the search list changed from `"$CC/../00_BRIEF" "...SNIPED_OS/00_BRIEF"` to `"$CC" "...SNIPED_OS/00_BRIEF"`.
- Effect: NEXT_ACTION now resolves from `00_COMMAND_CENTER` (fresh Jun 10). STANDING_ORDER still falls back to SNIPED_OS because no Refinery copy exists yet (created in Phase 2).
- This change lives on branch `claude/working-os-phase1` and is NOT committed (operator commit gate).

## Branch protocol
Claude works on `claude/*` branches only. main and master are protected. Claude pushes `claude/*` branches only and commits only when the operator asks.

## Backup scope
- In nightly: state, config, small docs, the WORKING_OS layer, 01_KNOWLEDGE_BASE text.
- Excluded (or should be, via .gitignore): ALMA_LOVE_PRODUCTION_001 media (about 6.5G), cloned repos, legacy batches/indexes/outputs, large raw/ files. Reason: bloat, build speed, and the read-only-source principle.

## Media storage
`ALMA_LOVE_PRODUCTION_001` (about 6.5G) is parked external asset storage, not a codebase artifact.

Updated by: manual when the hook fix is committed (record it), when the backup scope changes, or when the .git bloat is addressed (record the size after cleanup).
