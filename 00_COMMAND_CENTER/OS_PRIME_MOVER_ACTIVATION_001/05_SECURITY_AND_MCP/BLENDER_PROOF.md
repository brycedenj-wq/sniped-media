# BLENDER PROOF , gated socket control (2026-06-05)
- Callability: Blender MCP SERVER not registered in Claude Code (config is in Claude Desktop). Add-on socket localhost:9876 = reachable.
- Method: os_blender_socket.py drives the socket; EVERY payload gated by os_blender_gate (sandbox-only, no destructive/network/eval). Non-destructive (new scene, no factory reset).
- Proof run: created scene OS_DEED_PROOF + proof_cube + proof_cam + proof_light, rendered 800x800 -> blender_sandbox/renders/blender_proof.png (191KB). status: ok.
- Gate verdicts proven: DENY .ssh/credentials + destructive code; ALLOW sandbox test; CONFIRM real ops.
- Status: Blender control (gated socket) = ACTIVE (artifact + gate + log + route, repeatable via `os_blender_socket.py proof`).
- Optional next: register the native MCP server in Claude Code (`claude mcp add blender --scope user -- /Users/sniper/.local/bin/uv --directory ~/blender_mcp/mcp run blender-mcp`) + RESTART, for the native MCP tools. Not required , the OS already controls Blender safely.
