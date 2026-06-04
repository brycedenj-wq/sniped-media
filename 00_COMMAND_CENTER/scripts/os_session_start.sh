#!/bin/zsh
# os-session-start: auto-run at session start. Reconcile manifest->dashboard, consistency check, load live state.
CC="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER"
echo "=== OS SESSION START (enforced) ==="
python3 "$CC/scripts/os_checkpoint.py" 2>/dev/null
echo ""
echo "## NEXT_ACTION / STANDING_ORDER:"
for f in NEXT_ACTION STANDING_ORDER; do
  for d in "$CC/../00_BRIEF" "/Users/sniper/Downloads/    SNIPED_OS/00_BRIEF"; do
    [ -f "$d/$f.md" ] && { echo "[$f]"; head -8 "$d/$f.md"; break; }
  done
done
echo ""
echo "## journal tail (last 6 lines):"
tail -6 "$CC/OS_ENGAGEMENT_JOURNAL.md" 2>/dev/null
echo "=== END OS SESSION START ==="
