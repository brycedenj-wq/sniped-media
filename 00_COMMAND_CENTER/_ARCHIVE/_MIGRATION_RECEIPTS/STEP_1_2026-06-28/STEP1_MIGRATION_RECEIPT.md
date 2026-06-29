# STEP 1 MIGRATION RECEIPT · 2026-06-28

**Migration:** Convergence Plan Step 1 (archive the dead work-product directories).
**Contract:** `00_COMMAND_CENTER/CONVERGENCE_PLAN_2026-06-28.md`, Section 9, Step 1.
**Branch:** `claude/working-os-phase1`
**Status:** EXECUTED and VERIFIED. Not committed. Step 2 not begun.
**Destination shelf:** `00_COMMAND_CENTER/_ARCHIVE/`

This is a permanent audit-trail record. It accompanies `STEP1_ARCHIVE_MANIFEST.tsv`, `STEP1_ROLLBACK_MANIFEST.sh`, and `STEP1_POST_MIGRATION_RUNTIME_REPORT.md` in this package.

---

## 1 · What moved (exact directories, method, file counts)

19 directories, 321 files total, all relocated into `00_COMMAND_CENTER/_ARCHIVE/`.

Method note: `git mv` operates only on version-controlled files. 13 of the 19 directories were untracked in git (never committed), so `git mv` could not move them. Per operator decision, untracked directories were moved with a plain reversible `mv` (no deletion), and the 6 tracked directories were moved with `git mv`. Both mechanisms are reversible and non-destructive.

| # | Directory | Method | Files |
|---|---|---|---|
| 1 | OS_CERT_WAVE_002A | mv | 1 |
| 2 | OS_CERT_WAVE_002B | mv | 1 |
| 3 | OS_CERT_WAVE_002B_CODEX_SHADOW | mv | 2 |
| 4 | OS_CERT_WAVE_002C | mv | 1 |
| 5 | OS_CERT_WAVE_002D | mv | 13 |
| 6 | OS_CERT_WAVE_002D_CODEX_SHADOW | mv | 1 |
| 7 | OS_CERT_WAVE_002E | mv | 23 |
| 8 | OS_CERT_WAVE_002F | mv | 15 |
| 9 | OS_CERT_WAVE_002G | mv | 8 |
| 10 | OS_GAP_CLOSURE_WAVE_001 | mv | 9 |
| 11 | OS_GAP_CLOSURE_WAVE_001B | mv | 7 |
| 12 | OS_PRODUCTION_CLEANUP_001 | mv | 3 |
| 13 | TRIP_CAMPAIGN_OS_001 | mv | 54 |
| 14 | OS_MAX_DEMO_001 | git mv | 23 |
| 15 | OS_PRIVATE_DEMO_PACKAGE_001 | git mv | 30 |
| 16 | OS_MAX_CREATIVE_ACTIVATION_001 | git mv | 13 |
| 17 | OS_CAPABILITY_AUDIT_2026-06-04 | git mv | 6 |
| 18 | OS_CONDENSATION_AUDIT_001 | git mv | 1 |
| 19 | OS_OVERNIGHT_MAX_OPERATING_SPRINT_001 | git mv | 110 |

Tracked (git mv): 6 directories. Untracked (mv): 13 directories. See `STEP1_ARCHIVE_MANIFEST.tsv` for the machine-readable list.

---

## 2 · Baseline vs post-migration checks

All five runtime checks were captured before the first move (baseline) and after the last move (post). Identical results: no change.

| Check | Baseline | Post-migration |
|---|---|---|
| Kernel fixtures (`AI_PRODUCTION_OS/tests/run_fixtures.py`) | ALL 12 PASS | ALL 12 PASS |
| Fail-closed Stop hook (`AI_PRODUCTION_OS/os_stop_hook.py`) | exit 0 | exit 0 |
| Fail-open Stop hook (`scripts/os_stop_check.py`) | exit 0 | exit 0 |
| Router / gate-injector (`scripts/os_gate_injector.py`) | exit 0 | exit 0 |
| Governed-project precondition (LATERRE/renders/finish) | exit 0 | exit 0 |

Per-move verification during the run: each of the 19 moves passed a live-hook smoke check (both Stop hooks + gate-injector all exit 0) plus a dangling-reference grep (zero) before the loop advanced. The loop was set to halt on any anomaly; it did not halt.

---

## 3 · Harmless stale reference (disclosed, not modified)

`scripts/os_tool_test.py:16` carries a default argument:

```
ap.add_argument("--outdir", default=os.path.join(CC, "OS_OVERNIGHT_MAX_OPERATING_SPRINT_001", "01_TOOLCHAIN", "route_tests"))
```

This default now points at a moved directory. `os_tool_test.py` is NOT wired (it is absent from `.claude/settings.json` and is not on any live hook path), so this stale default has no runtime effect. It is a manual CLI default only. Per the migration constraints, `scripts/` was not modified. This reference can be redirected later in the deferred Step 7 code sprint.

---

## 4 · Runtime behavior remained unchanged

The post-migration runtime is identical to baseline (Section 2). Both Stop hooks remain wired, the router (`OS_ACTIVATION_INDEX.json` + `os_gate_injector.py`) is untouched, the kernel is intact, and the one governed project (LATERRE) still governs. Zero wired dangling references remain across the full surface (`settings.json`, `AI_PRODUCTION_OS`, `OS_ACTIVATION_INDEX.json`, `.claude/agents`, `.claude/workflows`, wired `scripts/`).

Note on glob scope: `_ARCHIVE/` is still inside the repo root, so it remains within `os_stop_check.py`'s recursive glob, but `mv`/`git mv` preserve file mtimes, so nothing newly trips that hook's 2-hour filter, and that hook is fail-open. Verified: it still exits 0.

---

## 5 · What was NOT touched

No runtime code, settings, kernel, scripts, or project files were modified. Specifically untouched:

- `.claude/settings.json` (the sole hook registry)
- `00_COMMAND_CENTER/AI_PRODUCTION_OS/` (the governance kernel)
- `00_COMMAND_CENTER/scripts/` (the legacy wired runtime)
- `00_COMMAND_CENTER/THE_HOUSE/` (the LATERRE project)
- `OS_ACTIVATION_INDEX.json` (the router of record)

The only repository changes from this task are: (a) 19 directories relocated into `_ARCHIVE/`, and (b) this receipt package.

---

## 6 · Rollback instructions

Full Step 1 is reversible. To reverse every move, run the rollback manifest from the repository root:

```
bash 00_COMMAND_CENTER/_ARCHIVE/_MIGRATION_RECEIPTS/STEP_1_2026-06-28/STEP1_ROLLBACK_MANIFEST.sh
```

The manifest issues `mv … back` for the 13 untracked directories and `git mv … back` for the 6 tracked directories, restoring each to `00_COMMAND_CENTER/`. The 6 tracked moves are also reversible via `git checkout` / `git reset` since they are staged (uncommitted) renames. No deletions were performed, so no file recovery is required.

---

## 7 · Current git status summary

- Renamed (`R`) index entries into `_ARCHIVE/` (the 6 tracked dirs' files): 67
- Untracked (`??`) directories now under `_ARCHIVE/` (the 13 moved dirs + this receipts package): 14
- New plain-delete (`D`) entries naming any of the 19 directories: 0
- Nothing committed by this task. (The repository had substantial pre-existing uncommitted changes before this migration; those are unrelated and were not touched.)

---

## 8 · Step gate

**Step 2 has not begun.** Step 1 is executed and verified only. Proceeding to Step 2, or committing Step 1, each requires separate explicit operator authorization.
