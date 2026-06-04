#!/bin/zsh
# os-backup: nightly OS-text preservation. Commits doctrine/skills/manifests/dashboards/scripts only.
# Books/media/raw/giant files are excluded by .gitignore (verified before add). Never force-adds.
REPO="/Users/sniper/AI-Brain-Refinery"
cd "$REPO" || exit 1
TS=$(date "+%Y-%m-%d %H:%M")
# stage only safe OS-text paths (never -A)
git add .gitignore \
  "00_COMMAND_CENTER/OS_"*.md "00_COMMAND_CENTER/OS_"*.csv \
  "00_COMMAND_CENTER/scripts/" "00_COMMAND_CENTER/_standards/" \
  .claude/skills/ .claude/settings.json \
  CLAUDE.md AGENTS.md 2>/dev/null
# safety: refuse if any staged file > 25MB (no giants in the brain repo)
BIG=$(git diff --cached --name-only | while read f; do [ -f "$f" ] && [ $(stat -f%z "$f" 2>/dev/null || echo 0) -gt 26214400 ] && echo "$f"; done)
if [ -n "$BIG" ]; then echo "[os-backup ABORT] giant file staged: $BIG"; git reset -q; exit 1; fi
if git diff --cached --quiet; then echo "[os-backup] no OS-text changes ($TS)"; exit 0; fi
git commit -q -m "os-backup $TS (nightly OS-text)
Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
echo "[os-backup] committed $TS. (cloud mirror: set a private remote + 'git push' to enable off-machine)"
