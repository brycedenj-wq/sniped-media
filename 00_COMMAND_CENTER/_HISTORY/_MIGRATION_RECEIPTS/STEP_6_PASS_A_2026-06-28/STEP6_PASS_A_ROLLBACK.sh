#!/usr/bin/env bash
# Reverse Step 6 Pass A: strip the retirement banners (restore docs to pre-banner text).
# Self-contained: removes only the added banner line + following blank line per .md,
# and the _convergence_note field from RUN_STATE.json. No other content is affected.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
CC=00_COMMAND_CENTER

MD_FILES=(
  "$CC/OS_CURRENT_STATE.md"
  "$CC/OS_ROUTER_INDEX.md"
  "$CC/CONTEXT_BOOT_CARD.md"
  "$CC/OS_SESSION_CONTINUITY.md"
  "$CC/decisions/DECISIONS_INDEX.md"
  "$CC/OS_ARCHIVE_ZONE_PROPOSAL.md"
  "$CC/OS_TAKEOVER_PHASES_001/OS_EXECUTIVE_ASSISTANT_STRUCTURE_AUDIT.md"
  "$CC/OS_TAKEOVER_PHASES_001/OS_ROUTINE_SETUP_PLAN.md"
  "$CC/OS_TAKEOVER_PHASES_001/OS_SKILL_UPGRADE_AUDIT.md"
  "$CC/CLAUDE_OVERLOAD_MASTERCLASS_001/CLAUDE_SEND_PACKET.md"
  "$CC/CLAUDE_OVERLOAD_MASTERCLASS_001/OS_RECEIPT.md"
  "$CC/CLAUDE_OVERLOAD_MASTERCLASS_001/OS_ROUTINE_SETUP_PLAN.md"
  "$CC/CLAUDE_OVERLOAD_MASTERCLASS_001/OS_TAKEOVER_UPGRADE_PLAN.md"
  "$CC/OS_TOOL_CEILING_AUDIT/OS_WORLD_CLASS_STACK.md"
  "$CC/NEXT_ACTION.md"
)

for f in "${MD_FILES[@]}"; do
  if [ -f "$f" ] && head -1 "$f" | grep -qE '^> \*\*(Retired 2026-06-28|Active mission: OS repository convergence)'; then
    tail -n +3 "$f" > "$f.rbtmp" && mv "$f.rbtmp" "$f"
    echo "stripped banner: ${f#"$CC"/}"
  else
    echo "skip (no banner): ${f#"$CC"/}"
  fi
done

RS="$CC/OS_TAKEOVER_PHASES_001/RUN_STATE.json"
if [ -f "$RS" ] && grep -q '"_convergence_note"' "$RS"; then
  grep -v '"_convergence_note"' "$RS" > "$RS.rbtmp" && mv "$RS.rbtmp" "$RS"
  python3 -m json.tool "$RS" >/dev/null && echo "removed _convergence_note (valid JSON): RUN_STATE.json"
fi

echo "Step 6 Pass A rollback complete."
