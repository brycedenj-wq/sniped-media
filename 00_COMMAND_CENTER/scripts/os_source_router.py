#!/usr/bin/env python3
"""
os_source_router.py - route a decision/query to the right sources across the whole Mac,
without blindly crawling. Reads EXTERNAL_SOURCE_REGISTRY.csv (the source-of-truth map).

  os_source_router.py "Alma Love video edit"
  os_source_router.py "pricing a client package"
  os_source_router.py "brand strategy decision"
  os_source_router.py "photo editing workflow"
  os_source_router.py "use my old SNIPED_OS knowledge"

Rules baked in:
- AI-Brain-Refinery is the execution root and current-state truth.
- SNIPED_OS (~/Downloads/    SNIPED_OS) is high-priority LEGACY/source library, never current truth.
- Newest proven AI-Brain-Refinery state wins on conflict.
- Books/frameworks -> compressed principles (story/psych layer + libraries), not raw book dumps.
- Media folders -> project builders only, not strategy answers.
"""
import csv, os, sys, re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "EXTERNAL_SOURCE_REGISTRY.csv")

# intent -> (source ids in priority order, libraries to load, project routes, read-first hint)
INTENTS = {
    "alma": (["alma_active","command_center","photo_pictures"],
             ["COMMERCIAL_CRAFT_LIBRARY","STORY_PSYCHOLOGY_LAYER","PREMIERE_EDITING_LIBRARY","ADOBE_OPERATOR_LIBRARY"],
             ["video_campaign","photo_post"],
             "ALMA_LOVE_PRODUCTION_001/05_EXPORTS selects+manifests; then commercial craft + story cards. Ignore old SNIPED_OS unless a specific framework is needed."),
    "edit_video": (["alma_active","command_center"],
             ["COMMERCIAL_CRAFT_LIBRARY","STORY_PSYCHOLOGY_LAYER","PREMIERE_EDITING_LIBRARY","AFTER_EFFECTS_MOTION_LIBRARY"],
             ["video_campaign","social_rollout"],
             "the active project's selects + EDIT plan; commercial craft + story gate. Not random old docs."),
    "pricing": (["command_center","sniped_os_legacy","claude_business"],
             ["MONEY_OFFER_LIBRARY","COPYWRITING_LIBRARY","STORY_PSYCHOLOGY_LAYER"],
             ["offer","productized_service"],
             "AI-Brain-Refinery money/offer libraries + pricing skills; SNIPED_OS for historical pricing context only."),
    "strategy": (["command_center","sniped_os_legacy","bj_wiki"],
             ["MONEY_OFFER_LIBRARY","COPYWRITING_LIBRARY","STORY_PSYCHOLOGY_LAYER","PSYCHOLOGY_OPERATOR_LIBRARY"],
             ["brand_ip_system","offer"],
             "current-state docs + canonical-truths first; SNIPED_OS + BJ-WIKI for deep frameworks; newest proven wins on conflict."),
    "brand": (["command_center","bj_wiki","sniped_os_legacy"],
             ["STORY_PSYCHOLOGY_LAYER","CHARACTER_AND_WORLD_LIBRARY","BUYER_DESIRE_LIBRARY","FIGMA_DESIGN_SYSTEM_LIBRARY"],
             ["brand_ip_system"],
             "brand identity + story/character cards; BJ-WIKI second-brain synthesis; SNIPED_OS history."),
    "photo": (["photo_pictures","lightroom_catalog","documents_photography","command_center"],
             ["PHOTO_DIRECTION_LIBRARY","ADOBE_OPERATOR_LIBRARY","VISUAL_STORY_EDITING_LIBRARY"],
             ["photo_post","still_range"],
             "the photo raws + Lightroom catalog for the workflow; photo/editing doctrine for the method. Media folders are builder-only."),
    "book": (["command_center","bj_wiki","sniped_os_legacy"],
             ["STORY_PSYCHOLOGY_LAYER"],
             [],
             "COMPRESSED principles via os_story_gate.py + library cards. Do NOT dump raw books; consult SNIPED_OS/BJ-WIKI only to extend a card."),
    "naming": (["command_center"],
             ["OS_NAMING_LIBRARY"],
             [],
             "the naming engine/library FIRST (OS_NAMING_LIBRARY), not old brainstorm docs."),
    "sniped_legacy": (["sniped_os_legacy","command_center","bj_wiki"],
             ["STORY_PSYCHOLOGY_LAYER","MONEY_OFFER_LIBRARY"],
             [],
             "SNIPED_OS as a LEGACY source library: index/synthesize, never treat as current truth; reconcile against current-state docs."),
}

def detect(q):
    q = q.lower()
    if "alma" in q: return "alma"
    if any(w in q for w in ["photo", "lightroom", "retouch", "grade", "raw "]): return "photo"
    if "naming" in q or "name " in q: return "naming"
    if any(w in q for w in ["video edit","edit","reel","commercial","cut "]): return "edit_video"
    if any(w in q for w in ["pric", "package", "quote", "charge"]): return "pricing"
    if any(w in q for w in ["book", "framework", "principle"]): return "book"
    if any(w in q for w in ["sniped_os", "sniped os", "old sniped", "legacy"]): return "sniped_legacy"
    if "brand" in q: return "brand"
    if any(w in q for w in ["strateg", "decision", "pivot", "should i"]): return "strategy"
    return "strategy"

def load_reg():
    return {r["id"]: r for r in csv.DictReader(open(REG))}

def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    q = " ".join(sys.argv[1:])
    reg = load_reg()
    intent = detect(q)
    ids, libs, projects, readfirst = INTENTS[intent]
    print(f'QUERY: "{q}"   ->  intent: {intent}\n')
    print("RELEVANT FOLDERS (priority order):")
    warn = []
    for sid in ids:
        r = reg.get(sid)
        if not r: continue
        print(f"  [{r['freshness']:>7}] {r['role']:14s} {r['path']}")
        print(f"            use: {r['use_when']}")
        if r["freshness"] in ("legacy","stale","unknown") or r["risk"]=="stale_doctrine_risk":
            warn.append(f"{sid} is {r['freshness']} ({r['risk']}) - do not treat as current truth")
    print("\nREAD FIRST:\n  " + readfirst)
    print("\nIGNORE: ~/Library, **/.git, **/node_modules, **/.cache, **/*.lrdata, secrets; Downloads/Desktop = intake only.")
    print("\nFRESHNESS WARNING:")
    if warn:
        for w in warn: print("  ! " + w)
        print("  ! CONFLICT RULE: if a SNIPED_OS/legacy file conflicts with a newer AI-Brain-Refinery current-state doc, the NEWER PROVEN truth wins.")
    else:
        print("  none - sources are current/active.")
    print("\nSOURCE PRIORITY:  command_center (current) > active_project > BJ-WIKI (memory) > SNIPED_OS (legacy library) > Downloads/Desktop (intake)")
    print("\nDECISION PRINCIPLES / LIBRARIES TO LOAD:")
    print("  " + ", ".join(libs) if libs else "  (none)")
    print("\nPROJECT ROUTES TO ACTIVATE:")
    print("  " + (", ".join(f"os_library.py load {p}" for p in projects) if projects else "(none - read/strategy only)"))

if __name__ == "__main__":
    main()
