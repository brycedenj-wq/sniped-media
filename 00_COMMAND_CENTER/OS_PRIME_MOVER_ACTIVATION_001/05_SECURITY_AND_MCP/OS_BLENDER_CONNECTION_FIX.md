# OS BLENDER CONNECTION , never silently drop again (2026-06-05)
> The add-on socket (9876) had stopped, so the OS route failed. Fixed on both sides.

## BLENDER SIDE (your app) , makes it come back automatically
- Preferences > Add-ons > MCP > **Auto Start = ON** (confirmed in your screenshot). The server now starts whenever Blender launches.
- Do NOT click "Stop MCP Server". If you ever restart Blender, Auto Start brings 9876 back on its own.
- Network > "Allow Online Access" ON (also confirmed) , fine; the socket is localhost-only regardless.

## OS SIDE , never fail silently, and alert on drop
1. **Health gate (built):** every Blender route now preflights `os_blender_socket.py health`. If 9876 is down, the OS STOPS with a clear message ("Start MCP Server"), instead of a silent failure.
2. **Watchdog (armed):** a background monitor pings 9876 every 20s and EXITS the moment it drops, which pings you immediately , so a drop is caught in real time, not discovered later.
3. **Re-prove anytime:** `python3 00_COMMAND_CENTER/scripts/os_blender_socket.py proof` re-renders the gated cube; `... health` shows up/down.

## STATUS
- Server: UP. Route: re-proven (blender_proof.png re-rendered). Auto Start: ON. Health gate: live. Watchdog: armed.

## ROOT CAUSE FOUND (2026-06-05 14:01) , macOS App Nap
The watchdog caught a real drop ~7 min after backgrounding Blender. Cause: **macOS App Nap** throttles/suspends background apps; it paused Blender's modal timer, which runs the 9876 socket server -> server stopped accepting -> Connection refused. When Blender was focused it worked; backgrounded, it napped.

### FIX APPLIED (persistent)
`defaults write org.blenderfoundation.blender NSAppSleepDisabled -bool YES`
(was unset = App Nap allowed = the bug). Now App Nap is disabled for Blender, so the socket server survives in the background.

### ACTION REQUIRED (once): QUIT AND REOPEN BLENDER
The setting takes effect on the next Blender launch. After you relaunch:
- Auto Start brings 9876 back up.
- App Nap no longer suspends it -> it stays up while backgrounded.
- I re-arm the watchdog to confirm it holds.

### FALLBACK (only if it still drops after the App Nap fix + relaunch)
Check the add-on's Idle settings (Idle Delay 5s / Timer Interval Idle) , raise/disable if the server idles out. But App Nap is the standard cause and the likely full fix.
