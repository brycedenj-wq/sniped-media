#!/usr/bin/env python3
"""
os_tool_reality_check.py , verify TOOL REALITY before any max task. Do not say a tool is unavailable until
checked. Do not say optional if the current standard marks it required.

Reads the live tool registry (os_tool_registry.py json) + the stale-assumption ledger. For each tool it
reports: status (ACTIVE/AMBER/RED/blocked), kind (local/mcp/installed), proof artifact, handoff route if
blocked, and any stale-ledger correction on that topic.

  os_tool_reality_check.py check <family|tool_substring>     , e.g. premiere, blender, adobe, higgsfield
  os_tool_reality_check.py project <project_type>            , reality for every tool the project requires
"""
import os, sys, json, subprocess, csv, importlib.util
HERE=os.path.dirname(os.path.abspath(__file__)); CMD=os.path.dirname(HERE)
def _imp(n):
    spec=importlib.util.spec_from_file_location(n, os.path.join(HERE,n+".py"))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
LIB=_imp("os_library")

FAM_KEYS={
 "higgsfield":["higgsfield","seedance","kling","soul","nano","wan","veo"],
 "adobe":["adobe","photoshop","lightroom","firefly","express"],
 "premiere":["premiere",".cut","quick_cut","capcut"],
 "after_effects":["aerender","after","ae."],
 "figma":["figma"],
 "blender":["blender"],
 "social":["instagram","meta","social","schedul"],
 "photo":["pixieset"],
}
LIBFAM={lib:fams[0] for lib,fams in LIB.LIBRARIES.items()}
PREMIUM={"higgsfield","adobe","premiere","after_effects","figma","blender"}
HANDOFF={"premiere":"PREMIERE_HANDOFF package (EDL + project notes); Premiere is INSTALLED but MCP-authoring is RED",
 "after_effects":"aerender a real .aep, or HyperFrames/ffmpeg titles; AE library is thin (corpus gap)"}

def registry():
    out=subprocess.run(["python3","os_tool_registry.py","json"],cwd=HERE,capture_output=True,text=True,timeout=30).stdout
    return json.loads(out)["tools"]

def stale_for(topic):
    L=os.path.join(CMD,"OS_STALE_ASSUMPTION_LEDGER.csv")
    for r in csv.DictReader(open(L)):
        if r["topic"]==topic or topic in r["topic"]:
            return r
    return None

def report_family(fam,T):
    keys=FAM_KEYS.get(fam,[fam])
    hits={tid:t for tid,t in T.items() if any(k in tid.lower() for k in keys)}
    statuses={t.get("status") for t in hits.values()}
    best = "ACTIVE" if "ACTIVE" in statuses else ("AMBER" if "AMBER" in statuses else ("RED" if "RED" in statuses else "UNKNOWN"))
    print(f"  FAMILY {fam.upper()}  rollup: {best}  ({len(hits)} registry tools)")
    for tid,t in sorted(hits.items(), key=lambda x:x[1].get('status','')):
        print(f"     [{t.get('status','?'):6s}] {tid:26s} {t.get('kind','?'):8s} {t.get('note','')[:50]}")
    st=stale_for(fam)
    if st:
        print(f"     LATEST TRUTH: {st['latest_truth'][:110]}")
        print(f"        source: {st['source_file_or_commit']}")
    if fam in PREMIUM and best!="ACTIVE":
        print(f"     PREMIUM + not fully ACTIVE -> HANDOFF: {HANDOFF.get(fam,'build a handoff or justify skip (blocked/irrelevant/underused)')}")
    if fam in PREMIUM:
        print(f"     RULE: required premium family. Do NOT substitute a local script just because it is easier (OS_NO_DUMB_TOOL_SKIPS.md).")
    return best

def cmd_check(q):
    T=registry()
    if q in FAM_KEYS:
        print(f"TOOL REALITY , family: {q}"); report_family(q,T); return 0
    hits={tid:t for tid,t in T.items() if q.lower() in tid.lower()}
    print(f"TOOL REALITY , match: {q}  ({len(hits)} tools)")
    if not hits: print("  no registry tool matches. Check os_tool_registry.py tools before claiming unavailable."); return 1
    for tid,t in hits.items():
        print(f"  [{t.get('status','?'):6s}] {tid:26s} {t.get('kind','?'):8s} {t.get('note','')}")
        if t.get("proof"): print(f"           proof: {t['proof']}")
    return 0

def cmd_project(pt):
    if pt not in LIB.PROJECTS:
        print(f"unknown project_type: {pt} (options: {', '.join(LIB.PROJECTS)})"); return 2
    T=registry()
    libs=LIB.PROJECTS[pt]
    print(f"TOOL REALITY for project_type: {pt}")
    print(f"required libraries: {', '.join(libs)}\n")
    notready=[]
    for lib in libs:
        fam=LIBFAM.get(lib)
        if not fam: continue
        best=report_family(fam,T)
        if fam in PREMIUM and best=="RED": notready.append(f"{fam} RED , needs handoff")
        print()
    print("TOOL-REALITY VERDICT:")
    if notready:
        for n in notready: print(f"  ! {n}")
        print("  proceed only with the handoff routes above logged in the run proof.")
    else:
        print("  all required families ACTIVE or have a handoff. None may be skipped for local convenience.")
    return 0

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)>=2 and a[0]=="check": sys.exit(cmd_check(a[1]))
    if len(a)>=2 and a[0]=="project": sys.exit(cmd_project(a[1]))
    print(__doc__); sys.exit(1)
