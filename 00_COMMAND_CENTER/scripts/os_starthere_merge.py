#!/usr/bin/env python3
"""
os_starthere_merge.py , fold workflow-extracted cards into the one card store.

Reads the starthere-operationalize workflow output (tasks/<id>.output JSON: {result:{perDoc:[{doc,cards,note}]}}),
normalizes each card, assigns a unique id, dedupes against the existing store by (technique+source),
appends to TECHNIQUE_CARDS.json, and bumps OS_STARTHERE_OPERATIONALIZATION.csv conversion_status to CONVERTED.

  os_starthere_merge.py <workflow_output.json>
"""
import sys, os, json, re, csv
HERE=os.path.dirname(os.path.abspath(__file__)); CMD=os.path.dirname(HERE)
JSON_STORE=os.path.join(CMD,"TECHNIQUE_CARDS.json")
CSVF=os.path.join(CMD,"OS_STARTHERE_OPERATIONALIZATION.csv")
NOTES=os.path.join(CMD,"OS_STARTHERE_COVERAGE_NOTES.md")

def slug(s):
    return re.sub(r"[^a-z0-9]+","_",(s or "").lower()).strip("_")[:40]

def main(wf_out):
    top=json.load(open(wf_out))
    res=top.get("result",top)
    perDoc=res.get("perDoc",[])
    store=json.load(open(JSON_STORE)) if os.path.exists(JSON_STORE) else []
    have_ids={c.get("id") for c in store}
    have_key={(slug(c.get("technique","")), slug(c.get("source_doc") or c.get("source",""))) for c in store}
    added=0; per_doc_added={}; notes=["# Start Here Extraction Coverage Notes\n"]
    for d in perDoc:
        doc=d.get("doc","?"); cards=d.get("cards",[]) or []; note=d.get("note","")
        notes.append(f"- **{doc}** , {len(cards)} cards. {note}")
        dc=slug(doc)[:18]; n_this=0
        for i,c in enumerate(cards):
            tech=c.get("technique",""); key=(slug(tech), slug(doc))
            if key in have_key: continue
            cid=f"{c.get('tool_family','x')}_{dc}_{slug(tech)[:18]}_{i}"
            base="".join(cid.split());
            while base in have_ids: base+="_x"
            card=dict(c); card["id"]=base; card["source_doc"]=doc
            card.setdefault("steps", c.get("exact_steps",""))
            card.setdefault("tool", c.get("app",""))
            card.setdefault("source", doc)
            store.append(card); have_ids.add(base); have_key.add(key); added+=1; n_this+=1
        per_doc_added[doc]=n_this
    json.dump(store, open(JSON_STORE,"w"), indent=1, ensure_ascii=False)
    open(NOTES,"w").write("\n".join(notes)+"\n")
    # update CSV conversion_status
    if os.path.exists(CSVF):
        rows=list(csv.DictReader(open(CSVF)))
        for r in rows:
            if per_doc_added.get(r["doc"],0)>0 or r["conversion_status"] in ("USE","USED"):
                # mark CONVERTED if it now has cards (USE docs that got >=1) ; keep USED as CONVERTED too
                if per_doc_added.get(r["doc"],0)>0:
                    r["conversion_status"]="CONVERTED"; r["reason"]=f"{per_doc_added[r['doc']]} cards extracted this pass"
        with open(CSVF,"w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    print(f"merged {added} new cards from {len(perDoc)} docs -> {JSON_STORE} (store now {len(store)})")
    print(f"coverage notes -> {NOTES}")
    z=[d for d,n in per_doc_added.items() if n==0]
    if z: print(f"docs that yielded 0 new cards ({len(z)}): {', '.join(z[:15])}{'...' if len(z)>15 else ''}")

if __name__=="__main__":
    if len(sys.argv)<2: print(__doc__); sys.exit(1)
    main(sys.argv[1])
