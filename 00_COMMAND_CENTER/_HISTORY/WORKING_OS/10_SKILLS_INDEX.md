# 10_SKILLS_INDEX · the skill ecosystem map

The single source of truth for where skills live and which need migration. Two skill roots exist today; the goal is one (Refinery only).

## Roots
- Canonical: `/Users/sniper/AI-Brain-Refinery/.claude/skills` (78 skills registered).
- Frozen source: `/Users/sniper/Downloads/    SNIPED_OS/_skills` (57 skills). The runtime must not depend on this for skill resolution.
- Router map and registry: `00_COMMAND_CENTER/OS_ACTIVATION_INDEX.json`. Audit tool: `00_COMMAND_CENTER/scripts/os_index_audit.py` (target: zero unregistered).

## REQUIRES MIGRATION (7 skills, loaded from Downloads, open call)
These resolve ONLY from `SNIPED_OS/_skills` via the settings.local.json Read allowlist. If Downloads moves or unmounts, the router loses them:
sniped-article, sniped-command-router, sniped-decide, sniped-operator-plan, sniped-os-execution-governor, sniped-project-ingestion, sniped-skill-intake.
Phase 2 copies them into `.claude/skills`, runs os_index_audit.py, then drops the allowlist. Recommendation: keep the SNIPED_OS copies as frozen source, just stop loading from them.

## Refinery-only (orchestration and production harness, about 28)
batch-extraction, master-consolidation, source-inventory, staging-plan, session-save, save, os-command-router, os-engagement, os-face-lock, os-quality-gates, os-token-safe-reader, os-vision-reject-gate, os-world-bible, boardroom, jsonl-validation, model-casting-protocol, kling-production-sop, emergency-drop-protocol, platform-mastering, composite-master-qa, brand-validation-machine, operator-review, challenge, banana-pro-director, cinema-worldbuilder, skill-template, watch, sniped-crs-builder.

## Cross-root (about 50 sniped-* skills, byte-duplicated in both roots)
Present in BOTH `.claude/skills` and `SNIPED_OS/_skills` (spot-checked identical). The Refinery copy is canonical; the SNIPED_OS copies are mirror/source.

Updated by: manual on skill add or migration, or a post-install hook calling os_index_audit.py. Record the audit result and timestamp here.
