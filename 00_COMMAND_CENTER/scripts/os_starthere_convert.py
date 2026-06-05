#!/usr/bin/env python3
"""
os_starthere_convert.py , Start Here is OPERATING SOURCE CODE, not documents to summarize.

A doc is not "done" when read/certified/summarized. It is done only when CONVERTED into operating
behavior: doctrine rule / technique card / workflow / tool route / gate / quality standard / skill /
script / dashboard field / failure-fix recipe / prompt pattern / reusable command / handoff , or a
deliberate DISCARD. This tool measures conversion HONESTLY by cross-referencing:
  - the content map (tool/technique density per doc, by content not name)  [os_howto_extract]
  - the technique-card registry (which docs actually became cards)         [os_technique_cards]
  - the certification ledger (which docs were merely certified)            [OS_CERTIFICATION_LEDGER]
and emits the conversion matrix + the high-leverage backlog.

  os_starthere_convert.py status [folder]    , conversion status per doc + matrix CSV
  os_starthere_convert.py backlog            , unconverted high-value docs, priority-ranked
"""
import os, sys, csv, argparse, importlib.util, glob

HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
# SOURCE OF TRUTH is the OS archive (survives deletion of the Downloads originals).
_ARCH=os.path.join(os.path.dirname(ROOT),"01_KNOWLEDGE_BASE","STARTHERE_SOURCE_ARCHIVE","_raw_files")
_DL="/Users/sniper/Downloads/    SNIPED_OS/start here"
SRC_DEFAULT=_ARCH if os.path.isdir(_ARCH) else _DL
MATRIX=os.path.join(ROOT,"OS_STARTHERE_TO_OPERATING_CODE_MATRIX.csv")
CERT=os.path.join(ROOT,"OS_CERTIFICATION_LEDGER.csv")
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(HERE,n+".py")); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

# priority by tool family (Adobe first per operator)
PRIORITY={"photoshop":1,"lightroom":1,"camera raw":1,"premiere":1,"after effects":1,"firefly":1,"adobe":1,
          "figma":2,"blender":3,"higgsfield":4,"seedance":4,"nano banana":4,"kling":4,"sora":4,"runway":4,
          "midjourney":4,"express":5}

def card_sources():
    tc=_m("os_technique_cards"); srcs=set()
    for c in tc.CARDS:
        for tok in c["source"].replace("+"," ").split():
            srcs.add(tok.strip().lower())
    return srcs

def cert_names():
    names=set()
    if os.path.exists(CERT):
        for row in csv.reader(open(CERT,errors="ignore")):
            if row: names.add(os.path.basename(row[0]).lower())
    return names

def classify(name, tools, carded, certed):
    base=name.lower().replace(".docx","").replace(".txt","").replace(" ","_")
    # did any technique card cite this doc?
    is_card=any(base[:14] in s or s in base for s in carded if len(s)>5)
    if is_card: return "TECHNIQUE_CARDED"
    if name.lower() in certed: return "CERTIFIED_ONLY"
    return "READ_ONLY"

def priority(tools):
    if not tools: return 9
    return min(PRIORITY.get(t,6) for t in tools)

def build():
    how=_m("os_howto_extract"); carded=card_sources(); certed=cert_names()
    files=sorted(glob.glob(os.path.join(SRC_DEFAULT,"*.docx"))+glob.glob(os.path.join(SRC_DEFAULT,"*.txt")))
    rows=[]
    for f in files:
        txt=how.extract_any(f)
        if not txt: continue
        tools,tech,w=how.density(txt)
        name=os.path.basename(f)
        status=classify(name,tools,carded,certed)
        rows.append({"doc":name,"words":w,"top_tools":";".join(sorted(tools,key=lambda t:-tools[t])[:4]),
                     "priority":priority(tools),"conversion_status":status})
    rows.sort(key=lambda r:(r["priority"], -r["words"]))
    return rows

def cmd_status():
    rows=build()
    with open(MATRIX,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["doc","words","top_tools","priority","conversion_status"]); w.writeheader(); w.writerows(rows)
    from collections import Counter
    c=Counter(r["conversion_status"] for r in rows)
    print(f"START HERE conversion , {len(rows)} docs")
    for k,v in c.items(): print(f"  {k:18s} {v}")
    print(f"\nmatrix -> {MATRIX}")
    print("\nTop priority docs + status:")
    for r in rows[:18]:
        print(f"  P{r['priority']} [{r['conversion_status']:16s}] {r['doc'][:46]:46s} {r['top_tools']}")
    return 0

def cmd_backlog():
    rows=[r for r in build() if r["conversion_status"]!="TECHNIQUE_CARDED"]
    rows=[r for r in rows if r["top_tools"]]
    print("CONVERSION BACKLOG (unconverted, has tool how-to, priority-ranked):")
    for r in rows[:30]:
        print(f"  P{r['priority']} {r['doc'][:48]:48s} {r['top_tools']}")
    return 0

def main():
    ap=argparse.ArgumentParser(prog="os_starthere_convert.py"); sub=ap.add_subparsers(dest="cmd")
    sub.add_parser("status"); sub.add_parser("backlog")
    a=ap.parse_args()
    if a.cmd=="status": return cmd_status()
    if a.cmd=="backlog": return cmd_backlog()
    ap.print_help(); return 1

if __name__=="__main__": sys.exit(main())
