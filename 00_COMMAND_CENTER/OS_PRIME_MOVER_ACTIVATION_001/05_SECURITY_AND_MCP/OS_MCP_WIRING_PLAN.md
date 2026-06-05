# OS MCP WIRING PLAN , Blender + After Effects (security decision required) 2026-06-05
> Auto-mode correctly BLOCKED me from cloning + wiring these as startup MCP servers. They run code locally and one runs LLM-generated code UNGATED. You must consciously accept the tradeoff. Below: the exact plan, the risks, and three ways to proceed. Nothing was installed.

## THE RISK (read before choosing)
- **Blender MCP** (Blender Foundation): its own docs say it "executes LLM-generated code in Blender WITHOUT any guards." That is arbitrary code execution on your Mac. It can read/modify/delete files and reach the network.
- **After Effects MCP** (Dakkshin, third-party from a tweet): a local node server Claude Code launches; runs ExtendScript in AE; has filesystem access.
- Both would be wired into Claude Code's STARTUP config, so they run automatically, with this private OS repo (and any keys in it) reachable.
- Mitigation posture if you proceed: run Blender on NON-sensitive scenes only; gate every Blender action through a human ok; keep secrets out of the working tree; treat these as power tools, not background daemons.

## PREREQUISITES (also not yet installed)
- `uv` (for blender-mcp) , `brew install uv`.
- Clone `https://projects.blender.org/lab/blender_mcp.git` to $HOME ; install the Blender add-on IN Blender 5.1+ (Preferences > Add-ons, or the .mcpb from the release).
- Clone `https://github.com/Dakkshin/after-effects-mcp.git` ; `npm install && npm run build && npm run install-bridge` ; open AE > Window > mcp-bridge-auto.jsx > tick Auto-run.

## THE CONFIG (what gets added , via `claude mcp add`, not hand-editing)
- Blender: `claude mcp add blender --scope user -- uv --directory $HOME/blender_mcp/mcp run blender-mcp`
- After Effects: `claude mcp add after-effects --scope user -- node $HOME/Developer/after-effects-mcp/build/index.js`
(Restart Claude Code after, so the servers load. They appear in `claude mcp list`.)

## THREE WAYS TO PROCEED (pick one)
1. **YOU run it (safest authorship).** You paste the commands above yourself. You are the human authorizing untrusted-code integration. I then verify + gate.
2. **I run it, with your explicit ok.** Reply "yes, clone + wire Blender + AE MCP, I accept the code-execution risk" (and add a Bash allow rule if you want it smooth). I do the installs + `claude mcp add` + write the gates.
3. **Keep them as HANDOFF (no MCP wiring).** Safest. Blender/AE stay manual apps; the OS preps the brief and gates the artifact you bring back. Zero new code-exec surface. (HyperFrames + video-use already cover most motion/edit needs without this.)

## RECOMMENDATION
Start with #3 for now (you lose almost nothing , HyperFrames does motion-graphics, video-use does editing, both lower-risk). Wire Blender only when a real 3D drop is the job, behind a gate, on a throwaway scene. Wire AE only if HyperFrames can't do a specific motion.

## VERIFY AFTER RESTART (whichever path)
- `claude mcp list` shows blender / after-effects = Connected.
- Blender running with the add-on enabled; AE open with the panel auto-running.
- Run one tiny gated test (e.g., "create a 1m cube") before anything real.
