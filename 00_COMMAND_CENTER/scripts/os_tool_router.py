#!/usr/bin/env python3
"""
os_tool_router.py , routes a task to a toolchain using the registry. Classifies intent, returns the
plan (toolchain, inputs, outputs, approval gates, log, validation, fallback, status, proof). For
local-exec routes it can hand the caller the exact command; for agent/MCP routes it emits a handoff.

  os_tool_router.py classify "<task text>"      , map free text to a route
  os_tool_router.py plan <route_id>             , full routing plan
  os_tool_router.py routes                       , list routes
"""
import sys, json, os, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
def _reg():
    s = importlib.util.spec_from_file_location("os_tool_registry", os.path.join(HERE, "os_tool_registry.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

# intent keywords -> route id. Specific multi-word phrases score higher and win over broad fallbacks.
INTENTS = {
    "make_campaign_package": ["campaign package", "campaign house", "full kit"],
    "build_film_pipeline": ["film pipeline", "film", "movie", "short film", "cinematic film"],
    "build_game_pipeline": ["game pipeline", "game", "video game", "playable"],
    "build_content_engine": ["content engine", "content factory", "content system", "posting cadence"],
    "build_money_move": ["money move", "next money", "money move", "revenue move", "make money"],
    "build_client_pitch": ["client pitch", "pitch a client", "client proposal", "pitch the client"],
    "build_private_demo": ["private demo", "demo package", "private client demo", "private demo package"],
    "build_motion_trailer": ["motion trailer", "trailer", "make a trailer"],
    "build_product_drop": ["product drop", "edition drop", "print drop", "merch drop", "product edition"],
    "build_pitch_deck": ["pitch deck", "deck", "investor"],
    "edit_image": ["edit image", "grade", "color", "retouch", "fix image", "composite", "cleanup"],
    "generate_motion": ["generate video", "motion clip", "video clip", "animate", "seedance"],
    "cut_video": ["cut video", "trim", "resize video", "caption-safe", "reel cut"],
    "build_landing_page": ["landing page", "web hero", "hero section"],
    "create_proof_loop": ["proof loop", "build a proof loop", "validate demand", "signups"],
    "track_leads": ["track leads", "crm", "lead list", "contacts"],
    "score_money_path": ["money path", "money readiness", "sellable"],
    "absorb_new_tool": ["activate tool", "activate a tool", "absorb tool", "new tool", "wire a tool"],
    "certify_docs": ["certify source", "certify a source", "certify doc", "certify the"],
    "build_world_3d": ["3d world", "build a world", "create world", "blender world", "environment"],
    "generate_pdf": ["pdf", "export pdf", "one-sheet pdf"],
    "update_dashboard": ["status board", "control room"],
    "run_launch_readiness_check": ["launch readiness", "readiness", "go-live check", "launch check"],
}

def classify(text):
    t = text.lower()
    best, score = None, 0
    for rid, kws in INTENTS.items():
        s = sum(2 if kw in t else 0 for kw in kws)
        if s > score: best, score = rid, s
    return best or "make_campaign_package"

def plan(route_id):
    reg = _reg(); r = reg.ROUTES.get(route_id)
    if not r: return {"error": f"unknown route: {route_id}"}
    chain = [{"tool": tid, **{k: reg.TOOLS.get(tid, {}).get(k) for k in ("kind", "status", "call")}} for tid in r["toolchain"]]
    runnable = all(reg.TOOLS.get(tid, {}).get("kind") == "local" or tid.startswith("os.") or tid.startswith("local.") for tid in r["toolchain"])
    return {
        "route": route_id, "status": r["status"], "exec": r.get("exec"),
        "toolchain": chain, "inputs": r["inputs"], "outputs": r["outputs"],
        "approval_gates": r["approval"], "log": r["log"], "validation": r["validation"],
        "fallback": r["fallback"], "proof": r.get("proof"), "gap": r.get("gap"),
        "locally_runnable": runnable,
        "handoff": None if runnable else "requires agent to invoke MCP tool, then log result back via SPEND_LEDGER/EDIT_LOG",
    }

def main():
    ap = argparse.ArgumentParser(prog="os_tool_router.py"); sub = ap.add_subparsers(dest="cmd")
    c = sub.add_parser("classify"); c.add_argument("text")
    p = sub.add_parser("plan"); p.add_argument("route_id")
    sub.add_parser("routes")
    a = ap.parse_args()
    if a.cmd == "classify":
        rid = classify(a.text); print(rid); print(json.dumps(plan(rid), indent=2))
    elif a.cmd == "plan":
        print(json.dumps(plan(a.route_id), indent=2))
    elif a.cmd == "routes":
        for rid in _reg().ROUTES: print(rid)
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
