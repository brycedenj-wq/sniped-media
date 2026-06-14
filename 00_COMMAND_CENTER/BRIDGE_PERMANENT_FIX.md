# MCP BRIDGE PERMANENT FIX · Premiere + After Effects + Higgsfield
Installed 2026-06-13. Goal: stop reconnecting every session.

## Root causes (what actually kept breaking)
1. PREMIERE: the CEP panel polls `/tmp/premiere-mcp-bridge` but the MCP server writes to `$TMPDIR/premiere-mcp-bridge`. If the symlink between them is missing (or broke on reboot), commands never reach the panel = ping timeout. The panel itself also has to be open (it auto-starts the bridge when open).
2. AFTER EFFECTS: the bridge actually works (the result file gets real data; the "stale" warning is a cosmetic freshness heuristic, not a disconnect). The real nuisance was multiple stale `node after-effects-mcp` processes from old sessions. The panel must be open in AE with "Allow Scripts to Write Files" on.
3. HIGGSFIELD: not a bridge problem at all. It is a remote connector and has been reliable all session. The only stops are content-moderation (NSFW) flags, which are content, not connection.

## The permanent fix (installed)
- `00_COMMAND_CENTER/scripts/bridge_doctor.sh`: idempotent repair. Ensures the Premiere `/tmp -> $TMPDIR` symlink, reports AE node + panel health. Safe to run anytime. It does NOT kill node processes (the Claude MCP harness owns that lifecycle; killing them disconnects the AE server).
- LaunchAgent `~/Library/LaunchAgents/com.sniped.bridgedoctor.plist`: runs the doctor on login and every 5 minutes, so the Premiere symlink is always present. Logs to `/tmp/bridge_doctor.log`.

## The one thing that cannot be automated (inherent to Adobe bridges)
The in-app panels must be OPEN once per app launch. There is no external way to force a CEP/ScriptUI panel open.
- Premiere: Window > Extensions > MCP Bridge (it shows "Running, polling" and auto-starts the bridge when open).
- After Effects: Window > mcp-bridge-auto.jsx, and Settings > Scripting & Expressions > "Allow Scripts to Write Files and Access Network" ON.
Once those panels are open, the LaunchAgent keeps the plumbing healthy and you should not need to reconnect.

## If a bridge ever looks down
1. Run: `zsh /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/bridge_doctor.sh`
2. Confirm the in-app panel is open (above).
3. Premiere only: if still timing out, click Stop Bridge then Start Bridge in the MCP Bridge panel.
4. AE only: if tools show disconnected in Claude, the MCP server node was lost; re-enable the After Effects connector in Claude so the harness respawns it.

## Current state at install
- Premiere: CONNECTED (project ALMA_LOVE_CLUB_FINISH.prproj loaded).
- After Effects: MCP server was lost during this repair (an over-aggressive kill, since removed from the script). Re-enable the AE connector in Claude to bring it back. Not blocking the 16:9 finish (AE MCP only builds comps from scratch; the video finish runs through Premiere).
- Higgsfield: connected, 511 credits.
