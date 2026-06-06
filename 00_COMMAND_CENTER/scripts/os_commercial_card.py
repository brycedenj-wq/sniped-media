#!/usr/bin/env python3
"""
os_commercial_card.py , manage the COMMERCIAL_CRAFT card store (OS_COMMERCIAL_CRAFT_CARDS.json).
Cards turn a reference teardown into a repeatable editing/copy/design/audio move the gates can call.

  os_commercial_card.py list [--lane L] [--gate G]
  os_commercial_card.py show <id>
  os_commercial_card.py add --id ID --lane L --problem .. --principle .. --move .. [--when ..] [--evidence ..] [--route ..] [--gate ..] [--dontcopy ..]
  os_commercial_card.py render-md   # rewrite OS_COMMERCIAL_CRAFT_LIBRARY.md from the cards
Schema per card: id, lane, problem, when_to_use, principle, exact_move, timestamp_evidence, tool_route, gate_influenced, do_not_copy.
"""
import sys, os, json, argparse
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(HERE,"..")
CARDS=os.path.join(ROOT,"OS_COMMERCIAL_CRAFT_CARDS.json")
MD=os.path.join(ROOT,"OS_COMMERCIAL_CRAFT_LIBRARY.md")
def load():
    return json.load(open(CARDS)) if os.path.exists(CARDS) else []
def save(c): json.dump(c,open(CARDS,"w"),indent=2)
def render_md(cards):
    L=["# OS COMMERCIAL CRAFT LIBRARY","",
       "> Repeatable editing/copy/design/audio moves extracted from ingested references + operator doctrine. Each card is callable by `os_reference_gate.py`. NOT inspiration; specific moves. Build references with `os_reference_ingest.py`, add cards with `os_commercial_card.py add`.",
       f"","**{len(cards)} cards.**",""]
    for c in cards:
        L+=[f"## {c['id']}  ({c.get('lane','')})",
            f"- **Problem:** {c.get('problem','')}",
            f"- **When to use:** {c.get('when_to_use','')}",
            f"- **Principle:** {c.get('principle','')}",
            f"- **Exact move:** {c.get('exact_move','')}",
            f"- **Evidence:** {c.get('timestamp_evidence','')}",
            f"- **Tool route:** {c.get('tool_route','')}",
            f"- **Gate influenced:** {c.get('gate_influenced','')}",
            f"- **Do NOT copy:** {c.get('do_not_copy','')}",""]
    open(MD,"w").write("\n".join(L)); return len(cards)
def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd")
    l=sub.add_parser("list"); l.add_argument("--lane"); l.add_argument("--gate")
    s=sub.add_parser("show"); s.add_argument("id")
    a=sub.add_parser("add")
    for f in ["id","lane","problem","principle","move","when","evidence","route","gate","dontcopy"]: a.add_argument("--"+f,default="")
    sub.add_parser("render-md")
    args=ap.parse_args(); cards=load()
    if args.cmd=="list":
        for c in cards:
            if args.lane and args.lane not in c.get("lane",""): continue
            if args.gate and args.gate not in c.get("gate_influenced",""): continue
            print(f"{c['id']:34} [{c.get('lane',''):16}] {c.get('principle','')[:80]}")
        return
    if args.cmd=="show":
        c=next((x for x in cards if x["id"]==args.id),None)
        print(json.dumps(c,indent=2) if c else "not found"); return
    if args.cmd=="add":
        cards=[x for x in cards if x["id"]!=args.id]
        cards.append({"id":args.id,"lane":args.lane,"problem":args.problem,"when_to_use":args.when,
          "principle":args.principle,"exact_move":args.move,"timestamp_evidence":args.evidence,
          "tool_route":args.route,"gate_influenced":args.gate,"do_not_copy":args.dontcopy})
        save(cards); render_md(cards); print(f"added {args.id}; {len(cards)} cards"); return
    if args.cmd=="render-md":
        print(f"rendered {render_md(cards)} cards -> OS_COMMERCIAL_CRAFT_LIBRARY.md"); return
    ap.print_help()
if __name__=="__main__": main()
