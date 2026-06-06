#!/usr/bin/env python3
"""
os_higgsfield_compliance_gate.py , does a production actually use the Higgsfield SUPER-STACK?

The Higgsfield Codex/Operator standard: Higgsfield is a virtual production STUDIO, not a prompt box.
A run is operator-compliant only if it ran the sequential pipeline. This gate scores the 11 pipeline
elements. A pretty generation that skipped the stack is NON-COMPLIANT, no matter how clean.

Statuses per item: USED / MISSING / BLOCKED / NOT_NEEDED(reason).
MCP-callability (so MISSING vs BLOCKED is honest):
  callable via MCP: Soul ID train (show_characters), Elements (show_reference_elements), Soul Cast / Soul
  Cinema models (generate_image), model routing (models_explore), Start/End frame (generate_video medias),
  Upscale (upscale_video), reframe, Cinema models + presets (presets_show), Marketing Studio.
  WEB-APP ONLY (BLOCKED via MCP -> handoff): Shots (9-angle), Angles, Skin Enhancer, Popcorn storyboard,
  Vibe Motion, Cinema Studio Director Panel UI.

  os_higgsfield_compliance_gate.py score --used "soul_id,upscale,..."   , verdict
  os_higgsfield_compliance_gate.py rubric
"""
import sys, argparse
ITEMS = {
 "soul_id":        ("Locked identity: trained Soul ID OR saved Element (not raw ref each time)","MCP-callable: show_characters train / show_reference_elements"),
 "char_ref_sheet": ("Character reference sheet (Soul Cast)","MCP-callable: generate_image model=soul_cast"),
 "location_sheet": ("Location reference sheet","MCP-callable: generate_image"),
 "prop_sheet":     ("Prop sheet: multi-angle orthographic of recurring objects (ledger/mark/seal)","MCP-callable: generate_image"),
 "shot_library":   ("Shot library: 1 image -> 9 angles (Shots) / Angles","WEB-APP (BLOCKED via MCP -> handoff or approximate by prompted angles)"),
 "skin_enhancer":  ("Skin Enhancer texture-consistency pass","WEB-APP (BLOCKED via MCP -> handoff)"),
 "start_end_frame":("Start Frame + End Frame logic for motion (clean cuts)","MCP-callable: generate_video medias start_image+end_image"),
 "model_routing":  ("Model-by-shot: WAN(continuity)/Kling(performance)/Seedance(action)","MCP-callable: models_explore + generate_video model"),
 "seedance_struct":("Seedance prompt structure: shot count+duration+aspect+timed segments+camera behavior+negative constraints","prompt discipline"),
 "upscale":        ("Upscale after generation","MCP-callable: upscale_video (Topaz)"),
 "edit_export":    ("Export into a real editing workflow (Premiere/AE) not ffmpeg-only","Premiere/AE present; handoff route"),
}
def score(used):
    u={x.strip() for x in used.split(",") if x.strip()}
    n=len(ITEMS); have=0
    print("HIGGSFIELD OPERATOR COMPLIANCE")
    for k,(desc,route) in ITEMS.items():
        st="USED" if k in u else "MISSING"
        if k in u: have+=1
        print(f"  [{st:7s}] {k:16s} {desc}")
    pct=round(100*have/n)
    verdict = "OPERATOR-COMPLIANT" if have>=9 else ("PARTIAL" if have>=5 else "NON-COMPLIANT (generation, not a studio production)")
    print(f"\n  {have}/{n} pipeline elements used ({pct}%) -> {verdict}")
    if have<n:
        print("  build the missing elements before calling the package max-stack. See OS_HIGGSFIELD_SUPERSTACK_REBUILD.md")
    return 0 if verdict=="OPERATOR-COMPLIANT" else 1
def main():
    ap=argparse.ArgumentParser(prog="os_higgsfield_compliance_gate.py"); sub=ap.add_subparsers(dest="cmd")
    s=sub.add_parser("score"); s.add_argument("--used",default=""); sub.add_parser("rubric")
    a=ap.parse_args()
    if a.cmd=="score": return score(a.used)
    if a.cmd=="rubric":
        for k,(d,r) in ITEMS.items(): print(f"  {k:16s} {d}\n        route: {r}");
        return 0
    ap.print_help(); return 1
if __name__=="__main__": sys.exit(main())
