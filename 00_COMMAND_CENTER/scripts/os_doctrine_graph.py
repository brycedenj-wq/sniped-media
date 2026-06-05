#!/usr/bin/env python3
"""
os_doctrine_graph.py , query the fused doctrine graph + the preserved contradictions.

The graph (OS_DOCTRINE_GRAPH.json, built by os_corpus_fusion) is how ideas connect ACROSS sources.
This tool reads it and the contradiction register so the router can, for any task, pull a node, its
cross-source neighbors, and any live tension that must be navigated (not flattened).

  os_doctrine_graph.py nodes                 , list nodes + source counts
  os_doctrine_graph.py node <id>             , one node: law, families, atoms, neighbors
  os_doctrine_graph.py neighbors <id>        , fused neighbors of a node
  os_doctrine_graph.py contradictions        , the preserved tensions + when each side applies
  os_doctrine_graph.py check "<task>"        , contradictions relevant to a task
"""
import os, sys, json, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH = os.path.join(ROOT, "OS_DOCTRINE_GRAPH.json")

# Preserved contradictions , recorded with WHEN each side applies. Never flattened.
CONTRADICTIONS = [
  {"id":"depth_vs_reach","a":"scene-density / company-of-one: depth over breadth, stay small",
   "b":"blockbuster / hit-mechanics: bet big, concentrate for maximum reach",
   "when":"Default to depth for the SNIPED craft + client base. Switch to big-bet reach ONLY for a hero asset (Direction Stack book, named-client anchor) where distribution is the point.",
   "nodes":["status_culture","leverage_ownership","distribution_hook"]},
  {"id":"build_new_vs_repetition","a":"capability-growth mandate: every source yields new skills/upgrades",
   "b":"repetition-over-novelty: architecture is built, ban new frameworks, run reps",
   "when":"Grow CAPABILITY (tools, gates, routes) always. Freeze new STRATEGY/identity frameworks; the cathedral exists. New != strategy churn.",
   "nodes":["self_optimization","founder_operations"]},
  {"id":"max_depth_vs_lean_hours","a":"maximum-by-default: ship the deepest possible work every time",
   "b":"operating-constraints: design for limited hours, leverage-first, never assume full-time",
   "when":"Max DEPTH of the artifact, achieved through leverage/automation, not through max HOURS. Depth is a quality bar, not a time budget.",
   "nodes":["automation_toolchain","founder_operations"]},
  {"id":"old_docs_vs_proof","a":"the OS preserves memory; old docs are evidence (court-weighted)",
   "b":"today's proof decides; nothing previously made is 'the answer'",
   "when":"Old docs INFORM and are raw material to beat. Live proof + the operator's instruction OVERRIDE old docs on any conflict.",
   "nodes":["decision_judgment","self_optimization"]},
  {"id":"locked_spine_vs_optionality","a":"the spine has locked decisions / canonical truths",
   "b":"possibility engine: protect optionality, do not lock identity before the kingdom exists",
   "when":"Lock the OPERATING SPINE (method, gates, safety). Keep the IDENTITY/throne open; identity emerges from proof, not brainstorm.",
   "nodes":["safety_identity","strategy_war"]},
  {"id":"ai_world_vs_ai_identity","a":"hybrid-operator: use AI for world-construction / IG creative engine",
   "b":"anti-identity-AI: never AI the client's face/body on deliverables",
   "when":"AI builds worlds, plates, environments freely. AI never touches a real person's identity on a client deliverable. The line is identity, not the tool.",
   "nodes":["world_character","safety_identity","visual_grade"]},
]

def load():
    if not os.path.exists(GRAPH): return {"nodes":{}, "edges":[]}
    return json.load(open(GRAPH))

def neighbors(g, nid):
    out = []
    for e in g["edges"]:
        if e["from"] == nid: out.append((e["to"], e["fusion"]))
        elif e["to"] == nid: out.append((e["from"], e["fusion"]))
    return out

def main():
    ap = argparse.ArgumentParser(prog="os_doctrine_graph.py"); sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("nodes"); n = sub.add_parser("node"); n.add_argument("id")
    nb = sub.add_parser("neighbors"); nb.add_argument("id")
    sub.add_parser("contradictions"); c = sub.add_parser("check"); c.add_argument("task")
    a = ap.parse_args(); g = load()
    if a.cmd == "nodes":
        for nid, nd in g["nodes"].items(): print(f"  {nid:20s} {nd['source_count']:2d} sources , {nd['law']}")
    elif a.cmd == "node":
        nd = g["nodes"].get(a.id)
        if not nd: print("unknown node"); return 2
        print(f"NODE {a.id}\n law: {nd['law']}\n extends: {nd['extends_domain']}")
        print(f" families ({len(nd['families'])}): {', '.join(nd['families'])}")
        print(f" atoms ({len(nd['atoms'])}): {', '.join(nd['atoms'])}")
        print(" neighbors:")
        for nb_, why in neighbors(g, a.id): print(f"   <-> {nb_}: {why}")
    elif a.cmd == "neighbors":
        for nb_, why in neighbors(g, a.id): print(f"  {a.id} <-> {nb_}: {why}")
    elif a.cmd == "contradictions":
        for c in CONTRADICTIONS:
            print(f"\n[{c['id']}]\n  A: {c['a']}\n  B: {c['b']}\n  WHEN: {c['when']}")
    elif a.cmd == "check":
        t = a.task.lower(); hit = []
        for c in CONTRADICTIONS:
            blob = (c["a"]+c["b"]+" ".join(c["nodes"])).lower()
            if any(w in blob for w in t.split() if len(w) > 4): hit.append(c)
        print(f"{len(hit)} contradiction(s) relevant to: {a.task}")
        for c in hit: print(f"  [{c['id']}] {c['when']}")
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
