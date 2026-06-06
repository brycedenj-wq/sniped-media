# OS NO DUMB TOOL SKIPS

LOCKED 2026-06-05. A relevant premium tool skipped only because a local script is easier = FAIL. Premium tools must be CHECKED before any local fallback. This is the rule that stopped the OS from quietly shipping local-shortcut work and calling it MAX.

## The standard
For every serious output, the run proof must declare, per relevant premium tool:
- **used** , the tool ran; name the artifact it produced.
- **skipped** , the tool did not run; one of three reasons MUST be given:
  - **blocked** , cannot call it (MCP/headless limitation). Requires a HANDOFF route (e.g. Premiere installed but MCP-authoring RED -> PREMIERE_HANDOFF package).
  - **irrelevant** , the project genuinely does not need it (state why).
  - **underused** , it was available and relevant but only lightly used (log it; this is a warning, not a pass).
- **proof artifact** , the file the tool produced (or the handoff package if blocked).
- **gate result** , which gate this satisfied.

"Local was easier/faster" is NOT a valid skip reason. If a premium tool is required by the project type (os_library.py load <type>) and was skipped for convenience, the run FAILS.

## Premium families (default-on for MAX work)
higgsfield, adobe, premiere, after_effects, figma, blender. (Per OS_PREMIUM_STACK_STANDARD.md, premium stack is DEFAULT-ON unless proven otherwise.)

## Decision table
| Situation | Verdict |
| --- | --- |
| Premium tool used, artifact exists | PASS |
| Premium tool blocked, handoff package built | PASS (with handoff logged) |
| Premium tool genuinely irrelevant, reason stated | PASS |
| Premium tool available + relevant, lightly used | WARN (underused, log it) |
| Premium tool skipped because local was easier | FAIL |
| Premium tool called "unavailable" without a reality check | FAIL (run os_tool_reality_check.py first) |
| Tool called "optional" when current standard marks it required | FAIL |

## Enforced by
- os_tool_reality_check.py (status + handoff per tool/family/project)
- os_premium_stack_gate.py (premium-stack verdicts incl. REJECT: LOCAL SHORTCUT)
- os_starthere_compliance_gate.py (library loadout + blocked-needs-handoff)
- os_max_readiness_gate.py (umbrella, blocks the MAX claim)

## Reference failure
AXIS run: used local ffmpeg + 1 Higgsfield element, skipped Premiere/AE/Adobe-post/Figma/Social because local was faster. Compliance gate verdict: NOT READY. This is the exact pattern this standard bans.
