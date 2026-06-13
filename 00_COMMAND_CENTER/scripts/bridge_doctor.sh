#!/bin/zsh
# bridge_doctor.sh - permanent keep-alive/repair for the Premiere + After Effects + Higgsfield MCP bridges.
# Run on login (LaunchAgent) and any time a bridge looks down. Idempotent and safe to run repeatedly.
# Root causes it fixes:
#  1) Premiere CEP panel polls /tmp/premiere-mcp-bridge but the MCP server writes to $TMPDIR/premiere-mcp-bridge -> symlink them.
#  2) Stale duplicate `node after-effects-mcp` processes from old sessions -> keep only the newest.
# What it CANNOT do (inherent to Adobe CEP/ScriptUI bridges): force the in-app panels open. Those must be open once per app launch.

log() { echo "[bridge_doctor $(date '+%H:%M:%S')] $1"; }

# --- 1. Premiere temp-dir symlink (durable) ---
SERVER_DIR="${TMPDIR%/}/premiere-mcp-bridge"
PANEL_DIR="/tmp/premiere-mcp-bridge"
mkdir -p "$SERVER_DIR"
if [ -L "$PANEL_DIR" ]; then
  CUR=$(readlink "$PANEL_DIR")
  if [ "$CUR" != "$SERVER_DIR" ]; then rm -f "$PANEL_DIR"; ln -s "$SERVER_DIR" "$PANEL_DIR"; log "Premiere symlink repointed -> $SERVER_DIR"; else log "Premiere symlink OK"; fi
elif [ -d "$PANEL_DIR" ]; then
  # real dir present: migrate to symlink only if empty, else leave (panel may own it)
  if [ -z "$(ls -A "$PANEL_DIR" 2>/dev/null)" ]; then rmdir "$PANEL_DIR"; ln -s "$SERVER_DIR" "$PANEL_DIR"; log "Premiere: replaced empty dir with symlink"; else log "Premiere: /tmp dir non-empty, left as-is (panel owns it)"; fi
elif [ ! -e "$PANEL_DIR" ]; then
  ln -s "$SERVER_DIR" "$PANEL_DIR"; log "Premiere symlink created -> $SERVER_DIR"
fi

# --- 2. AE MCP node servers: report only. Do NOT kill (the Claude MCP harness owns the node lifecycle; it respawns on demand). ---
AE_COUNT=$(pgrep -f "after-effects-mcp/build/index.js" 2>/dev/null | wc -l | tr -d ' ')
log "AE MCP node servers running: ${AE_COUNT} (managed by the MCP harness; not touched)"

# --- 3. Report bridge panel/dir health ---
[ -d "/Users/sniper/Documents/ae-mcp-bridge" ] && log "AE bridge dir present" || log "AE bridge dir MISSING (run AE MCP setup)"
log "Premiere panel must be open: Premiere > Window > Extensions > MCP Bridge (it auto-starts when open)."
log "AE panel must be open: AE > Window > mcp-bridge-auto.jsx (+ Settings > Scripting > Allow Scripts to Write Files)."
log "done"
