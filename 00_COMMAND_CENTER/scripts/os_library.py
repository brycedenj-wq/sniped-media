#!/usr/bin/env python3
"""
os_library.py , the 10 OPERATOR LIBRARIES as VIEWS over the one card store, plus the project-type loader.

Not a second pile. Every library is a filtered view of the technique cards (os_technique_cards.CARDS),
keyed by tool_family. New cards extracted from Start Here docs flow in automatically.

The loader answers: "for THIS kind of project, which libraries must load BEFORE executing?" That loadout
is what the Start Here compliance gate checks against.

  os_library.py list                  , the 10 libraries + card counts
  os_library.py families              , family histogram across the whole card store
  os_library.py show <LIBRARY>        , cards in a library (e.g. ADOBE_OPERATOR_LIBRARY or adobe)
  os_library.py load <project_type>   , libraries that must load for a project type (+ JSON manifest)
  os_library.py projects              , the project-type -> libraries routing table
"""
import sys, os, json, importlib.util

HERE=os.path.dirname(os.path.abspath(__file__))
def _load_cards():
    spec=importlib.util.spec_from_file_location("os_technique_cards", os.path.join(HERE,"os_technique_cards.py"))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.CARDS
CARDS=_load_cards()

# derive tool_family for legacy cards that only have 'tool'/'app'
FAM_FROM_TOOL={
 "adobe":"adobe","photoshop":"adobe","lightroom":"adobe","firefly":"adobe","express":"adobe","evoto":"adobe",
 "higgsfield":"higgsfield","seedance":"higgsfield","kling":"higgsfield","nano":"higgsfield","wan":"higgsfield","veo":"higgsfield","soul":"higgsfield",
 "premiere":"premiere","after effects":"after_effects","ae":"after_effects",
 "figma":"figma","blender":"blender",
}
def fam(c):
    f=c.get("tool_family")
    if f: return f
    t=(c.get("tool") or c.get("app") or "").lower()
    for k,v in FAM_FROM_TOOL.items():
        if k in t: return v
    # heuristic from problem text for the soft families
    p=(c.get("problem","")+" "+c.get("technique","")).lower()
    if any(w in p for w in ["offer","pricing","revenue","value equation","retainer","monetize","package price"]): return "money"
    if any(w in p for w in ["outreach","cold dm","cold email","pipeline","objection","icp","prospect"]): return "sales"
    if any(w in p for w in ["headline","caption","copy","hook line","body copy","story arc"]): return "copy"
    if any(w in p for w in ["reel","instagram","tiktok","algorithm","retention","posting","attention","followers"]): return "social"
    if any(w in p for w in ["posing","lighting setup","location","moodboard","wardrobe","model "]): return "photo"
    if any(w in p for w in ["premiere","cut on","j-cut","l-cut","transition","pacing","timeline"]): return "premiere"
    if any(w in p for w in ["after effects","kinetic type","motion graphic","keyframe title"]): return "after_effects"
    if "figma" in p or "design system" in p: return "figma"
    if "blender" in p or "render" in p: return "blender"
    return "multi"

# the 10 named libraries (+ photo as the 11th since the photo corpus is large)
LIBRARIES={
 "HIGGSFIELD_OPERATOR_LIBRARY":["higgsfield"],
 "ADOBE_OPERATOR_LIBRARY":["adobe"],
 "PREMIERE_EDITING_LIBRARY":["premiere"],
 "AFTER_EFFECTS_MOTION_LIBRARY":["after_effects"],
 "FIGMA_DESIGN_SYSTEM_LIBRARY":["figma"],
 "BLENDER_PRODUCTION_LIBRARY":["blender"],
 "SOCIAL_DISTRIBUTION_LIBRARY":["social"],
 "MONEY_OFFER_LIBRARY":["money"],
 "COPYWRITING_LIBRARY":["copy"],
 "SALES_OUTREACH_LIBRARY":["sales"],
 "PHOTO_DIRECTION_LIBRARY":["photo"],
}
SHORT={lib.split("_")[0].lower():lib for lib in LIBRARIES}  # adobe-> ADOBE_OPERATOR_LIBRARY etc

# named sub-libraries resolved by card-id prefix (operator addendum 2026-06-05)
PREFIX_LIBS={
 "PREMIERE_MCP_OPERATOR_LIBRARY":"premc_",
 "HIGGSFIELD_ADOBE_PLUGIN_LIBRARY":"hfplug_",
 "AUTOEDIT_CREATOR_MODE_LIBRARY":"autoedit_",
}
SHORT.update({"premiere_mcp":"PREMIERE_MCP_OPERATOR_LIBRARY","higgsfield_adobe":"HIGGSFIELD_ADOBE_PLUGIN_LIBRARY","autoedit":"AUTOEDIT_CREATOR_MODE_LIBRARY"})
def cards_in_prefix(pref): return [c for c in CARDS if str(c.get("id","")).startswith(pref)]

# project type -> ordered libraries that MUST load before executing
PROJECTS={
 "video_campaign":["HIGGSFIELD_OPERATOR_LIBRARY","PREMIERE_EDITING_LIBRARY","AFTER_EFFECTS_MOTION_LIBRARY","ADOBE_OPERATOR_LIBRARY","FIGMA_DESIGN_SYSTEM_LIBRARY","SOCIAL_DISTRIBUTION_LIBRARY"],
 "film":["HIGGSFIELD_OPERATOR_LIBRARY","PREMIERE_EDITING_LIBRARY","AFTER_EFFECTS_MOTION_LIBRARY","ADOBE_OPERATOR_LIBRARY","BLENDER_PRODUCTION_LIBRARY"],
 "ad":["HIGGSFIELD_OPERATOR_LIBRARY","ADOBE_OPERATOR_LIBRARY","PREMIERE_EDITING_LIBRARY","AFTER_EFFECTS_MOTION_LIBRARY","FIGMA_DESIGN_SYSTEM_LIBRARY","COPYWRITING_LIBRARY","MONEY_OFFER_LIBRARY"],
 "offer":["MONEY_OFFER_LIBRARY","SALES_OUTREACH_LIBRARY","COPYWRITING_LIBRARY"],
 "deck":["FIGMA_DESIGN_SYSTEM_LIBRARY","COPYWRITING_LIBRARY","MONEY_OFFER_LIBRARY"],
 "social_rollout":["SOCIAL_DISTRIBUTION_LIBRARY","COPYWRITING_LIBRARY","PREMIERE_EDITING_LIBRARY","AFTER_EFFECTS_MOTION_LIBRARY"],
 "productized_service":["MONEY_OFFER_LIBRARY","SALES_OUTREACH_LIBRARY","COPYWRITING_LIBRARY","FIGMA_DESIGN_SYSTEM_LIBRARY"],
 "world_build":["HIGGSFIELD_OPERATOR_LIBRARY","BLENDER_PRODUCTION_LIBRARY","ADOBE_OPERATOR_LIBRARY","FIGMA_DESIGN_SYSTEM_LIBRARY","PHOTO_DIRECTION_LIBRARY"],
 "brand_ip_system":["FIGMA_DESIGN_SYSTEM_LIBRARY","ADOBE_OPERATOR_LIBRARY","MONEY_OFFER_LIBRARY","COPYWRITING_LIBRARY","HIGGSFIELD_OPERATOR_LIBRARY"],
 "still_range":["HIGGSFIELD_OPERATOR_LIBRARY","ADOBE_OPERATOR_LIBRARY","PHOTO_DIRECTION_LIBRARY","BLENDER_PRODUCTION_LIBRARY"],
}
SELLING_TYPES={"ad","offer","deck","productized_service","brand_ip_system"}

def cards_in(fams):
    return [c for c in CARDS if fam(c) in fams]

def cmd_list():
    print("OPERATOR LIBRARIES (views over the one card store)")
    tot=0
    for lib,fams in LIBRARIES.items():
        n=len(cards_in(fams)); tot+=n
        print(f"  {lib:32s} {n:4d} cards   [{','.join(fams)}]")
    print("  -- named sub-libraries (id-prefix views) --")
    for lib,pref in PREFIX_LIBS.items():
        print(f"  {lib:32s} {len(cards_in_prefix(pref)):4d} cards   [{pref}*]")
    print(f"  {'TOTAL CARDS (store)':32s} {len(CARDS):4d}")
    return 0

def cmd_families():
    from collections import Counter
    c=Counter(fam(x) for x in CARDS)
    print("FAMILY HISTOGRAM (whole card store)")
    for k,v in c.most_common(): print(f"  {k:14s} {v}")
    return 0

def cmd_show(name):
    key=name if (name in LIBRARIES or name in PREFIX_LIBS) else SHORT.get(name.lower())
    if not key: print(f"unknown library: {name}\n  options: {', '.join(list(LIBRARIES)+list(PREFIX_LIBS))}"); return 1
    cs=cards_in_prefix(PREFIX_LIBS[key]) if key in PREFIX_LIBS else cards_in(LIBRARIES[key])
    print(f"{key}  ({len(cs)} cards)")
    for c in cs:
        cid=c.get("id","?"); tech=c.get("technique","?"); src=c.get("source") or c.get("source_doc","?")
        print(f"  [{cid}] {tech}  <- {src}")
    return 0

def cmd_load(ptype):
    if ptype not in PROJECTS:
        print(f"unknown project type: {ptype}\n  options: {', '.join(PROJECTS)}"); return 1
    libs=list(PROJECTS[ptype])
    if ptype in SELLING_TYPES or ptype in ("video_campaign","world_build","film"):
        for sell in ("MONEY_OFFER_LIBRARY","SALES_OUTREACH_LIBRARY"):
            if sell not in libs: libs.append(sell+"  (load if the artifact is for selling)")
    print(f"PROJECT TYPE: {ptype}")
    print("LOAD THESE LIBRARIES BEFORE EXECUTING (in order):")
    manifest={"project_type":ptype,"required_libraries":[],"total_cards_available":0}
    for lib in libs:
        base=lib.split("  ")[0]
        n=len(cards_in(LIBRARIES[base])) if base in LIBRARIES else 0
        flag=" (conditional)" if "(" in lib else ""
        print(f"  - {base:32s} {n:4d} cards{flag}")
        if base in LIBRARIES and "(" not in lib:
            manifest["required_libraries"].append(base); manifest["total_cards_available"]+=n
    print("\nMANIFEST (feed to os_starthere_compliance_gate.py):")
    print("  "+json.dumps(manifest))
    return 0

def cmd_projects():
    print("PROJECT TYPE -> REQUIRED LIBRARIES")
    for p,libs in PROJECTS.items():
        print(f"  {p:20s} {', '.join(l.replace('_LIBRARY','').replace('_',' ').title() for l in libs)}")
    return 0

if __name__=="__main__":
    a=sys.argv[1:] or ["list"]
    cmd=a[0]
    if cmd=="list": sys.exit(cmd_list())
    if cmd=="families": sys.exit(cmd_families())
    if cmd=="show" and len(a)>1: sys.exit(cmd_show(a[1]))
    if cmd=="load" and len(a)>1: sys.exit(cmd_load(a[1]))
    if cmd=="projects": sys.exit(cmd_projects())
    print(__doc__); sys.exit(1)
