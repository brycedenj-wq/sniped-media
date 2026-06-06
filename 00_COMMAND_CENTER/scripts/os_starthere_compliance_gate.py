#!/usr/bin/env python3
"""
os_starthere_compliance_gate.py , no project is MAX / ELITE / COMPLETE / READY until it PROVES it used the
operating layer. This is the gate that breaks the loop of "pretty output that skipped the stack".

It checks a run-proof JSON against the project type's required library loadout (os_library.PROJECTS):
  - which libraries were loaded (and were the required ones loaded?)
  - which cards were used (a loaded library with zero cards used = UNDERUSED)
  - which tools were used, and for any not used: is there a blocked+handoff reason? (skip without reason = FAIL)
  - what artifacts were created (must exist on disk)
  - what gates passed
  - what remains underused

Verdict READY only if: every required library loaded AND used, >=1 artifact exists, no dumb tool skip.

  os_starthere_compliance_gate.py check <proof.json>
  os_starthere_compliance_gate.py template <project_type>   , print a blank proof to fill in
"""
import sys, os, json, importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
def _imp(name):
    spec=importlib.util.spec_from_file_location(name, os.path.join(HERE,name+".py"))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
LIB=_imp("os_library")

def check(proof_path):
    P=json.load(open(proof_path))
    pt=P.get("project_type")
    if pt not in LIB.PROJECTS:
        print(f"unknown project_type: {pt} (options: {', '.join(LIB.PROJECTS)})"); return 2
    required=LIB.PROJECTS[pt]
    loaded=set(P.get("libraries_loaded",[]))
    used_ids=set(P.get("cards_used",[]))
    tools_used=set(t.lower() for t in P.get("tools_used",[]))
    blocked={b["tool"].lower():b for b in P.get("tools_blocked",[]) if b.get("tool")}
    artifacts=P.get("artifacts",[])
    gates=P.get("gates_passed",[])

    # cards per library actually used
    def lib_cards(lib): return {c.get("id") for c in LIB.cards_in(LIB.LIBRARIES.get(lib,[]))}
    fails=[]; warns=[]; lines=[]
    print(f"START HERE COMPLIANCE , project_type: {pt}")
    print("REQUIRED LIBRARY LOADOUT:")
    for lib in required:
        avail=lib_cards(lib)
        was_loaded= lib in loaded
        used_here= used_ids & avail
        status="OK" if (was_loaded and used_here) else ("LOADED-UNUSED" if was_loaded else "NOT LOADED")
        if not was_loaded: fails.append(f"{lib} not loaded")
        elif not used_here: warns.append(f"{lib} loaded but 0 cards used (UNDERUSED)")
        print(f"  [{status:14s}] {lib:32s} {len(used_here)}/{len(avail)} cards used")

    # artifacts must exist
    print("ARTIFACTS:")
    if not artifacts: fails.append("no artifacts produced")
    real=0
    for a in artifacts:
        ex=os.path.exists(a); real+=ex
        try: sz=os.path.getsize(a) if ex else 0
        except: sz=0
        if ex and sz==0: warns.append(f"artifact is 0 bytes: {a}")
        print(f"  [{'EXISTS' if ex else 'MISSING':6s}] {a}{'' if sz else ' (0 bytes)' if ex else ''}")
    if artifacts and real==0: fails.append("artifacts listed but none exist on disk")

    # tool skip discipline: required-library tools not used must have a blocked+handoff reason
    print("GATES PASSED:", ", ".join(gates) if gates else "(none claimed)")
    if P.get("tools_blocked"):
        print("BLOCKED TOOLS (with handoff):")
        for b in P["tools_blocked"]:
            ok=bool(b.get("reason") and b.get("handoff"))
            if not ok: fails.append(f"tool '{b.get('tool')}' marked blocked without reason+handoff")
            print(f"  [{'OK' if ok else 'BAD':3s}] {b.get('tool')} , {b.get('reason','NO REASON')} -> {b.get('handoff','NO HANDOFF')}")

    verdict = "READY" if not fails else "NOT READY"
    print(f"\nVERDICT: {verdict}")
    if fails:
        print("BLOCKERS (fix before calling this MAX/ELITE/COMPLETE):")
        for f in fails: print(f"  X {f}")
    if warns:
        print("UNDERUSED / WARNINGS:")
        for w in warns: print(f"  ! {w}")
    if verdict=="READY" and not warns:
        print("  full loadout used, artifacts on disk, no dumb tool skips.")
    return 0 if verdict=="READY" else 1

def template(pt):
    if pt not in LIB.PROJECTS:
        print(f"unknown project_type: {pt} (options: {', '.join(LIB.PROJECTS)})"); return 2
    req=LIB.PROJECTS[pt]
    t={"project_type":pt,"libraries_loaded":req,"cards_used":["<card_id>","..."],
       "tools_used":["<tool>","..."],
       "tools_blocked":[{"tool":"<tool>","reason":"<why MCP/headless cannot>","handoff":"<the handoff package built instead>"}],
       "artifacts":["<absolute path>","..."],"gates_passed":["elite_art_direction","higgsfield_compliance","..."]}
    print(json.dumps(t,indent=2)); return 0

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)>=2 and a[0]=="check": sys.exit(check(a[1]))
    if len(a)>=2 and a[0]=="template": sys.exit(template(a[1]))
    print(__doc__); sys.exit(1)
