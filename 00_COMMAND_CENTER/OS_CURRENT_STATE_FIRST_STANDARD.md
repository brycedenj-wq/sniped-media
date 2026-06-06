# OS CURRENT STATE FIRST , the standard

LOCKED 2026-06-05. The OS must stop acting from yesterday's truth. Before any strategy, build, audit, money decision, creative run, tool decision, or MAX claim, it loads current state and verifies tool reality. **Newest committed truth wins.**

## Why this exists (the disease it cures)
- Tools were marked missing after they were proven (Premiere, Blender).
- Old SNIPED kept resurfacing after it was archived.
- Premiere was skipped because of stale detection.
- Adobe was treated as optional after the premium-stack standard changed.
- Start Here was treated as reference after it became operating code.
- Local scripts were used when premium tools should have been checked.
- Newer committed truth was not loaded before decisions.

## Boot order (run os_current_state_boot.py)
1. OS_CURRENT_STATE.md
2. NEXT_ACTION.md
3. latest git commit log
4. latest capability dashboard (OS_CAPABILITY_COVERAGE_MATRIX.md)
5. latest tool registry (os_tool_registry.py)
6. OS_STARTHERE_OPERATIONALIZATION_DASHBOARD.md
7. technique-card library status (TECHNIQUE_CARDS.json)
8. os_library.py load <project_type>
9. latest premium-stack standard (OS_PREMIUM_STACK_STANDARD.md)
10. latest money router state (OS_GRAND_MONEY_PLAY_DECISION_ANSWER.md)
11. latest failure ledger (OS_FAILURE_LEDGER.csv)
12. latest stale-assumption ledger (OS_STALE_ASSUMPTION_LEDGER.csv)

Any boot artifact OLDER than the latest commit is flagged POSSIBLY STALE and must be refreshed before it is trusted.

## The rules
1. **Newest truth wins.** A newer committed artifact overrides older context. Blender RED -> ACTIVE. Premiere missing -> installed. Old SNIPED active -> archived. Start Here reference -> operating code. Adobe optional -> required. Latest proof/standing-order wins, every time.
2. **Tool reality check.** For every max task verify connected / installed / callable / ACTIVE / AMBER / RED / blocked / changed-since-last-run / proof artifact / handoff route. Do not say unavailable until checked. Do not say optional if the current standard marks it required. (os_tool_reality_check.py)
3. **No dumb tool skips.** For every serious output: premium tools used, premium tools skipped, reason skipped, blocked vs irrelevant vs underused, proof artifact, gate result. A relevant premium tool skipped only because local scripts are easier = FAIL. (OS_NO_DUMB_TOOL_SKIPS.md)
4. **Project-type library boot.** Before executing, run `os_library.py load <project_type>` (video_campaign / film / ad / offer / deck / social_rollout / productized_service / world_build / brand_ip_system / still_range). The result sets required libraries + compliance expectations.
5. **MAX / ELITE / COMPLETE / READY claims** require all of: current state loaded, project libraries loaded, relevant tools checked, underused tools logged, cards used, gates passed, artifacts exist, blocked tools have handoff routes, stale assumptions checked. Enforced by os_max_readiness_gate.py.

## The command sequence (every serious task)
```
python3 00_COMMAND_CENTER/scripts/os_current_state_boot.py            # load current state
python3 00_COMMAND_CENTER/scripts/os_tool_reality_check.py project <type>   # tool reality
python3 00_COMMAND_CENTER/scripts/os_library.py load <type>           # required libraries
python3 00_COMMAND_CENTER/scripts/os_stale_assumption_gate.py check "<any assumption>"
# ... do the work behind the cards/gates ...
python3 00_COMMAND_CENTER/scripts/os_max_readiness_gate.py check <proof.json>   # before any MAX claim
```

## Files in this layer
- OS_CURRENT_STATE_FIRST_STANDARD.md (this doc)
- os_current_state_boot.py -> OS_BOOT_REPORT.md
- os_tool_reality_check.py
- os_stale_assumption_gate.py + OS_STALE_ASSUMPTION_LEDGER.csv
- OS_NO_DUMB_TOOL_SKIPS.md
- os_max_readiness_gate.py
- OS_FAILURE_LEDGER.csv
