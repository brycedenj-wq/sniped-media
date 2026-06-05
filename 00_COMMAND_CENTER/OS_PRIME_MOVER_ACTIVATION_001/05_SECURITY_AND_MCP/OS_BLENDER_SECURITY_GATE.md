# OS BLENDER SECURITY GATE , controlled activation only (2026-06-05)
> Blender MCP runs LLM-generated Python with NO built-in guards (its own docs). The OS therefore NEVER lets it touch anything but a sandbox, and gates every action. Built: os_blender_gate.py + this sandbox. Tested: it DENIES .ssh/credentials + destructive code, ALLOWS only the sandbox test scene, CONFIRMS before any real op.

## THE RULES (enforced by os_blender_gate.py)
- SANDBOX ONLY: `OS_PRIME_MOVER_ACTIVATION_001/05_SECURITY_AND_MCP/blender_sandbox/`. Any path outside = DENY.
- NO credential paths (.ssh/.aws/.env/keychains/tokens/.git) = DENY (proven on /Users/sniper/.ssh/id_rsa).
- NO destructive or network code (rmtree/remove/subprocess/socket/urllib/eval/exec/quit) = DENY (proven).
- NO OS-root writes, NO private-repo traversal.
- DELETE = never allowed.
- Anything beyond a harmless test scene (create/modify/export/python) = CONFIRM (per-action human ok).
- Every action LOGGED to blender_sandbox/BLENDER_GATE_LOG.csv. Artifact proof required.

## ACTIVATION STATE
- os_blender_gate.py: BUILT + TESTED (ACTIVE).
- Blender MCP server: NOT WIRED (correct , it is the ungated-code surface). Status: HANDOFF/WIRE, gated.
- Blender.app: installed. uv: not installed.

## EXACT STEPS TO WIRE IT SAFELY (stop-at-restart line)
1. `brew install uv`
2. `cd $HOME && git clone https://projects.blender.org/lab/blender_mcp.git`
3. Install the Blender add-on IN Blender (Preferences > Add-ons, or the .mcpb from the release).
4. Register the server, ROUTED THROUGH THE GATE (do not point it at the repo root):
   `claude mcp add blender --scope user -- uv --directory $HOME/blender_mcp/mcp run blender-mcp`
5. RESTART Claude Code (servers load on start). STOP HERE , this is your line.
6. First proof (gated): create a deed certificate / archive-drawer / plinth scene in the sandbox, render ONE frame, export to the sandbox, log it. Nothing else until that proof exists.

## IF IT CANNOT BE WIRED SAFELY
Keep it HANDOFF: you drive Blender manually on a sandbox scene; the OS preps the spec and gates the exported frame. Substance Text-to-3D (Adobe credits) is the lower-risk 3D path.
