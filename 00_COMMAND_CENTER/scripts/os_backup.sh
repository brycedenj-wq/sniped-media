#!/bin/zsh
# os-backup: nightly OS-text preservation. Commits doctrine/skills/manifests/dashboards/scripts only.
# Books/media/raw/giant files are excluded by .gitignore (verified before add). Never force-adds.
REPO="/Users/sniper/AI-Brain-Refinery"
cd "$REPO" || exit 1
MODE="${1:-commit}"
REMOTE_NAME="osbackup"   # set with: git remote add osbackup <private-url>
if [ "$MODE" = "status" ]; then
  echo "[os-backup status] branch=$(git branch --show-current)  last=$(git log --oneline -1 2>/dev/null)"
  if git remote get-url "$REMOTE_NAME" >/dev/null 2>&1; then
    echo "  remote '$REMOTE_NAME': $(git remote get-url $REMOTE_NAME)"
    git fetch "$REMOTE_NAME" >/dev/null 2>&1; echo "  ahead/behind: $(git rev-list --left-right --count $REMOTE_NAME/$(git branch --show-current)...HEAD 2>/dev/null || echo 'n/a')"
  else echo "  remote '$REMOTE_NAME': NOT SET (add with: git remote add $REMOTE_NAME <private-url>)"; fi
  exit 0
fi
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
if [ "$MODE" = "dry-run" ]; then echo "[os-backup dry-run] would commit:"; git diff --cached --name-only; git reset -q; exit 0; fi
if git diff --cached --quiet; then echo "[os-backup] no OS-text changes ($TS)"; exit 0; fi
git commit -q -m "os-backup $TS (nightly OS-text)
Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
echo "[os-backup] committed $TS."
if [ "$MODE" = "push" ]; then
  if git remote get-url "$REMOTE_NAME" >/dev/null 2>&1; then git push "$REMOTE_NAME" HEAD && echo "[os-backup] pushed to $REMOTE_NAME"; else echo "[os-backup] push skipped: remote '$REMOTE_NAME' not set"; fi
else echo "[os-backup] local only. run with 'push' once a remote is set."; fi
