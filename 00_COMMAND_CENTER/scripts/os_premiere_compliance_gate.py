#!/usr/bin/env python3
"""
os_premiere_compliance_gate.py , no video campaign / teaser / ad / edit is MAX / ELITE / COMPLETE until it
proves the Premiere native route was checked. Premiere is NOT optional and ffmpeg/HyperFrames is NOT the
default max edit system. (Source: Premiere MCP 269-tool transcripts, operator paste 2026-06-05.)

The Premiere Pro MCP (GitHub, 269 tools) DIRECTLY controls Premiere while it is open, via:
  project open -> Window > Extensions > MCP Bridge running -> new/refreshed Claude session.
That is real automated control. Headless render is the only blocked part.

Checks a proof.json:
  premiere_mcp_checked (bool)         , did we check the Premiere MCP route at all?
  premiere_installed (bool)           , Premiere app present?
  premiere_open (bool/None)           , project open? (None = not verified)
  mcp_bridge_running (bool/None)      , Window>Extensions>MCP Bridge live?
  sequence_readable (bool) OR sequence_block_reason (str)
  premiere_tools_used (list) OR premiere_skip_reason ("BLOCKED:..." / "IRRELEVANT:...")
  used_local_because_easier (bool)    , if true -> FAIL

  os_premiere_compliance_gate.py check <proof.json>
  os_premiere_compliance_gate.py template
"""
import sys, json, glob

def check(p):
    P=json.load(open(p)); fails=[]; oks=[]; warns=[]
    print("PREMIERE COMPLIANCE")
    installed = bool(glob.glob("/Applications/Adobe Premiere Pro*")) or P.get("premiere_installed")
    print(f"  premiere installed (verified on disk): {bool(glob.glob('/Applications/Adobe Premiere Pro*'))}")
    if not P.get("premiere_mcp_checked"): fails.append("Premiere MCP route NOT checked (run os_video_edit_router.py pick / os_tool_reality_check)")
    else: oks.append("Premiere MCP route checked")
    if not installed: fails.append("Premiere not installed AND not flagged installed in proof")
    else: oks.append("Premiere installed")
    # bridge requirements
    po=P.get("premiere_open"); br=P.get("mcp_bridge_running")
    if po is True and br is True: oks.append("Premiere project open + MCP Bridge running (direct control available)")
    else:
        warns.append(f"Premiere MCP not confirmed live (project_open={po}, mcp_bridge_running={br}). If using Premiere MCP, both must be true + refreshed Claude session.")
    # sequence readable or blocked with reason
    if P.get("sequence_readable"): oks.append("active sequence/timeline readable")
    elif P.get("sequence_block_reason"): oks.append(f"sequence not read, reason given: {P['sequence_block_reason']}")
    else: fails.append("sequence neither readable NOR blocked-with-reason (read it or state the exact blocker)")
    # premiere tools used or skipped with reason
    used=P.get("premiere_tools_used") or []
    skip=P.get("premiere_skip_reason","")
    if used: oks.append(f"Premiere tools used: {', '.join(used)}")
    elif skip.startswith(("BLOCKED:","IRRELEVANT:")): oks.append(f"Premiere skipped with valid reason: {skip}")
    else: fails.append("Premiere tools neither used NOR skipped with BLOCKED:/IRRELEVANT: reason")
    # the cardinal sin
    if P.get("used_local_because_easier"): fails.append("FAIL: local scripts used instead of Premiere only because they were easier (OS_NO_DUMB_TOOL_SKIPS)")
    verdict="PASS" if not fails else "FAIL"
    print(f"\n  VERDICT: {verdict}")
    for o in oks: print(f"   + {o}")
    for w in warns: print(f"   ! {w}")
    for f in fails: print(f"   X {f}")
    return 0 if verdict=="PASS" else 1

def template():
    print(json.dumps({
      "premiere_mcp_checked":True,"premiere_installed":True,"premiere_open":True,"mcp_bridge_running":True,
      "sequence_readable":True,"sequence_block_reason":"",
      "premiere_tools_used":["remove_silences","ripple_delete","generate_captions","export"],
      "premiere_skip_reason":"","used_local_because_easier":False},indent=2))
    return 0

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)>=2 and a[0]=="check": sys.exit(check(a[1]))
    if a and a[0]=="template": sys.exit(template())
    print(__doc__); sys.exit(1)
