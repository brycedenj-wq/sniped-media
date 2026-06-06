# PREMIERE MCP PROOF

Status flip artifact. Existence of this file is the gate the router/ledger checks to move DIRECT_PREMIERE from PENDING-PROOF to ACTIVE.

- **Proof date:** 2026-06-05 22:31 PDT
- **Verdict:** PASS. Premiere MCP bridge is live and reachable from Claude Code.
- **Bar met:** route + log + repeat (4 distinct read-only calls succeeded, consistent project/version across all).

## Environment verified
- MCP server visible to Claude Code: `mcp__premiere-pro__*` (269 tools) loaded via ToolSearch.
- CEP bridge: real-copy panel `MCPBridgeCEP` (panel id `com.mcp.premiere.bridge.panel`), operator full-quit + relaunched Premiere and started the bridge this session.
- Temp dir present: `/tmp/premiere-mcp-bridge` (exists, owner sniper, created 2026-06-05 22:03).
- Premiere app: Adobe Premiere Pro 2026, version 26.2.2 build 3, `/Applications/Adobe Premiere Pro 2026/Adobe Premiere Pro 2026.app/`.

## Proof calls (read-only, no media import, no edits, no sequence creation)
1. `ping` -> `{connected:true, premiereVersion:"26.2.2", projectName:"NEW.prproj", activeSequence:"None"}`
2. `get_version_info` -> `{version:"26.2.2", buildNumber:"3", isDocumentOpen:true, path:".../Adobe Premiere Pro 2026.app/"}`
3. `get_project_info` -> `{name:"NEW.prproj", path:"/Users/sniper/Documents/Adobe/Premiere Pro/26.0/NEW.prproj", numSequences:0, numItems:0, activeSequence:null}`
4. `get_premiere_state` -> `{project:{name:"NEW.prproj", rootItemCount:0, sequenceCount:0}, sequences:[], activeSequence:null, version:"26.2.2", buildNumber:"3"}`

Consistency check: project name `NEW.prproj`, version `26.2.2`, build `3` matched across all four calls. No errors, no timeouts.

## Scope honored
No media import. No timeline edits. No sequence creation. No creative work. No credits spent. Read-only proof only.

## Route + repeat
- Route: `os_video_edit_router` route `DIRECT_PREMIERE_AUTOMATED`.
- Repeat: 4 independent read calls returned consistent live state in one session.

## What is NOT yet proven (honest boundary)
- Write/edit operations (import, add_to_timeline, create_sequence, export) are NOT proof-tested. They are now AVAILABLE but unproven. Run `os_premiere_compliance_gate` before any MAX edit claim, and do not claim an edit capability until a real edit-and-export proof exists.
- Headless (no-GUI) render remains N/A. FCPXML/EDL is the secondary bridge.
