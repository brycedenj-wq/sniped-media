#!/usr/bin/env python3
"""
os_execution_graph.py , THE CAPSTONE. One task in -> the whole organism's execution chain out.

This is the layer that makes the OS answer as ONE thing. It fuses every router that already exists:
  prime_router      -> which MODULES wake
  doctrine_router   -> which DOCTRINES load + at what confidence
  tool_router       -> which ROUTE (toolchain) runs
  tool_registry     -> the live ACTIVE/AMBER/RED status of every tool in that toolchain
  skill registry    -> which custom SKILL matches
  gates             -> doctrine gate + route validation + standing safety floor

For any task it produces the chain and answers the 10 organism questions:
  1 doctrine  2 tool  3 skill  4 script  5 connector  6 gate
  7 artifact  8 dashboard/log  9 failure-rule  10 human approval line.

REFUSAL IS BUILT IN. If any tool in the chosen route is not ACTIVE, the graph marks the step BLOCKED
and reports the blocker instead of pretending it can run. Visible/connected != ACTIVE != runnable.

  os_execution_graph.py graph "<task text>"      , full execution chain (human-readable)
  os_execution_graph.py graph "<task>" --json     , machine-readable chain
  os_execution_graph.py command <name>            , graph for a named one-command-layer command
"""
import os, sys, csv, json, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILL_CSV = os.path.join(ROOT, "OS_SKILL_REGISTRY.csv")

def _m(n):
    s = importlib.util.spec_from_file_location(n, os.path.join(HERE, n + ".py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

# The named top-level commands the OS understands -> the route that fulfills each.
COMMANDS = {
    "make campaign package": "make_campaign_package",
    "build film pipeline": "build_film_pipeline",
    "build game pipeline": "build_game_pipeline",
    "build content engine": "build_content_engine",
    "build money move": "build_money_move",
    "build client pitch": "build_client_pitch",
    "build private demo": "build_private_demo",
    "build proof loop": "create_proof_loop",
    "activate tool": "absorb_new_tool",
    "certify source": "certify_docs",
    "build launch readiness": "run_launch_readiness_check",
    "build motion trailer": "build_motion_trailer",
    "build product drop": "build_product_drop",
    "create world": "build_world_3d",
    "generate motion": "generate_motion",
    "edit video": "cut_video",
    "build pitch deck": "build_pitch_deck",
    "track leads": "track_leads",
    "create client room": "create_client_room",
    "run money path": "score_money_path",
    "run max sprint": "run_max_sprint",
}

def match_skill(text):
    if not os.path.exists(SKILL_CSV): return None
    t = text.lower(); best, score = None, 0
    with open(SKILL_CSV) as f:
        for row in csv.DictReader(f):
            if row.get("status") != "ACTIVE": continue
            hay = (row.get("name","") + " " + row.get("description","")).lower()
            s = sum(1 for w in set(t.split()) if len(w) > 3 and w in hay)
            if s > score: best, score = row["name"], s
    return best if score else None

def graph(text, route_id=None):
    prime = _m("os_prime_router"); droute = _m("os_doctrine_router")
    trouter = _m("os_tool_router"); reg = _m("os_tool_registry")

    kernel = _m("os_intelligence_kernel"); dg = _m("os_doctrine_graph"); fusion = _m("os_corpus_fusion")
    g = dg.load()

    modules = prime.classify(text)
    doctrines = droute.route(text)["doctrines"]
    rid = route_id or trouter.classify(text)
    plan = trouter.plan(rid)
    r = reg.ROUTES.get(rid, {})

    # FUSED LAYER , activate graph nodes (9 doctrine domains + the NEW corpus nodes by keyword)
    active_nodes = {d["domain"] for d in doctrines if d["domain"] in g.get("nodes", {})}
    tl = text.lower()
    NODE_KW = {"strategy_war":["strateg","position","compete","war","pitch"],
               "decision_judgment":["decide","decision","judge","evaluate","risk","choose","whether"],
               "leverage_ownership":["leverage","own","equity","media","ip","money move","monetize"],
               "founder_operations":["operate","scal","hire","founder","turnaround","run the","office"],
               "status_culture":["status","luxury","premium","culture","brand"],
               "automation_toolchain":["tool","stack","automat","pipeline","route","mcp","engine"],
               "narrative_canon":["story","narrative","film","script","character","world","game"],
               "self_optimization":["improve","optimi","failure","certif","fuse","learn"]}
    for nid, kws in NODE_KW.items():
        if nid in g.get("nodes", {}) and any(k in tl for k in kws): active_nodes.add(nid)
    source_families = {}
    for nid in active_nodes:
        nd = g["nodes"].get(nid, {})
        source_families[nid] = {"families": nd.get("families", []), "atoms": len(nd.get("atoms", [])),
                                 "neighbors": [n for n, _ in dg.neighbors(g, nid)]}
    contradictions = []
    for c in dg.CONTRADICTIONS:
        blob = (c["a"] + c["b"] + " ".join(c["nodes"])).lower()
        if set(c["nodes"]) & active_nodes or any(w in blob for w in tl.split() if len(w) > 4):
            contradictions.append({"id": c["id"], "when": c["when"]})

    # 2/4/5 tools, scripts, connectors + live status; REFUSE on non-ACTIVE.
    chain = []
    blockers = []
    for tid in r.get("toolchain", []):
        tdef = reg.TOOLS.get(tid, {})
        st = tdef.get("status", "RED")
        kind = tdef.get("kind", "?")
        chain.append({"tool": tid, "kind": kind, "status": st, "call": tdef.get("call"),
                      "role": tdef.get("role"), "approval": tdef.get("approval")})
        if st != "ACTIVE":
            blockers.append(f"{tid} is {st} (not ACTIVE) , {tdef.get('note','')[:60]}")
    if r.get("status") and r.get("status") != "ACTIVE":
        blockers.append(f"route '{rid}' is {r.get('status')} (not ACTIVE){' , gap: ' + r['gap'] if r.get('gap') else ''}")
    runnable = len(blockers) == 0 and r.get("status") == "ACTIVE"

    # 6 gates = route validation + per-module gates + doctrine rubric checks
    module_gates = sorted({g for mid in modules for g in prime.MODULES.get(mid, {}).get("gates", [])})
    gates = list(dict.fromkeys([r.get("validation")] + module_gates)) if r.get("validation") else module_gates

    # 9 failure rules from the awake modules
    failure_rules = [prime.MODULES[mid]["failure"] for mid in modules if mid in prime.MODULES]

    # 10 approval lines = route approvals + tool approvals + standing safety floor
    approvals = set(r.get("approval", []))
    for c in chain:
        if c["approval"]: approvals.add(c["approval"])
    standing = ["no real identity / employer overlap", "no public action without explicit go",
                "payment + legal finalization held", "spend logged + ceiling respected"]

    return {
        "task": text,
        "route": rid,
        "route_status": r.get("status"),
        "runnable": runnable,
        "blockers": blockers,
        "always_on_kernel": kernel.compact(),
        "fused_nodes": sorted(active_nodes),
        "source_families": source_families,
        "contradictions_checked": contradictions,
        "answers": {
            "1_doctrine_to_load": [f"{d['domain']} ({d['confidence']})" for d in doctrines],
            "2_tools": [c["tool"] for c in chain],
            "3_skill_to_invoke": match_skill(text),
            "4_scripts": [c["tool"] for c in chain if c["kind"] == "local"],
            "5_connectors": [c["tool"] for c in chain if c["kind"] == "mcp"],
            "6_gates": gates,
            "7_artifact": r.get("outputs"),
            "8_dashboard_log": r.get("log"),
            "9_failure_rules": failure_rules,
            "10_approval_lines": sorted(approvals) + standing,
        },
        "modules_awake": modules,
        "toolchain_detail": chain,
        "route_doctrine": r.get("doctrine"),
        "refuses": r.get("refuses"),
        "proof": r.get("proof"), "gap": r.get("gap"),
    }

def render(g):
    print(f"TASK: {g['task']}")
    print(f"ROUTE: {g['route']}  (route status: {g['route_status']})")
    verdict = "GO , all tools ACTIVE" if g["runnable"] else "BLOCKED , refuse until proven"
    print(f"RUNNABLE: {verdict}")
    if g["blockers"]:
        print("  BLOCKERS:")
        for b in g["blockers"]: print(f"   x {b}")
    print("\nFUSED LAYER (the whole corpus active):")
    print("  always-on kernel: LOADED (11 law categories)")
    fam_total = sum(len(v["families"]) for v in g["source_families"].values())
    print(f"  fused nodes: {', '.join(g['fused_nodes']) or '-'}")
    print(f"  source families activated: {fam_total} across {len(g['source_families'])} nodes")
    for nid, v in g["source_families"].items():
        if v["families"]:
            print(f"    {nid}: {', '.join(v['families'][:5])}{' ...' if len(v['families'])>5 else ''} (+{v['atoms']} atoms)")
    if g["contradictions_checked"]:
        print("  contradictions navigated:")
        for c in g["contradictions_checked"]: print(f"    [{c['id']}] {c['when'][:90]}")
    else:
        print("  contradictions: none triggered")
    a = g["answers"]
    print("\nTHE 10 ANSWERS (one organism):")
    print(f"  1 doctrine -> {', '.join(a['1_doctrine_to_load'])}")
    print(f"  2 tools    -> {', '.join(a['2_tools']) or '-'}")
    print(f"  3 skill    -> {a['3_skill_to_invoke'] or '-'}")
    print(f"  4 scripts  -> {', '.join(a['4_scripts']) or '-'}")
    print(f"  5 connect  -> {', '.join(a['5_connectors']) or '-'}")
    print(f"  6 gates    -> {', '.join(g_ for g_ in a['6_gates'] if g_) or '-'}")
    print(f"  7 artifact -> {', '.join(a['7_artifact']) if a['7_artifact'] else '-'}")
    print(f"  8 log/dash -> {a['8_dashboard_log'] or '-'}")
    print(f"  9 failure  -> {' | '.join(a['9_failure_rules']) or '-'}")
    print(f" 10 approval -> {'; '.join(a['10_approval_lines'])}")
    if g.get("refuses"): print(f"\nREFUSES TO CLAIM: {g['refuses']}")
    print(f"modules awake: {', '.join(g['modules_awake'])}")
    if g.get("route_doctrine"): print(f"route doctrine nodes: {', '.join(g['route_doctrine'])}")
    if g.get("gap"): print(f"known gap: {g['gap']}")
    print("pipeline: input -> modules -> doctrine(load) -> toolchain -> gates -> artifact -> log -> dashboard -> learning loop")

def main():
    ap = argparse.ArgumentParser(prog="os_execution_graph.py"); sub = ap.add_subparsers(dest="cmd")
    g = sub.add_parser("graph"); g.add_argument("text"); g.add_argument("--json", action="store_true")
    c = sub.add_parser("command"); c.add_argument("name"); c.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.cmd == "graph":
        res = graph(a.text)
        print(json.dumps(res, indent=2)) if a.json else render(res)
    elif a.cmd == "command":
        rid = COMMANDS.get(a.name.lower())
        if not rid:
            print(f"unknown command. known: {', '.join(COMMANDS)}"); return 2
        res = graph(a.name, route_id=rid)
        print(json.dumps(res, indent=2)) if a.json else render(res)
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
