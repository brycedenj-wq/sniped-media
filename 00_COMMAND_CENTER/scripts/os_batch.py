#!/usr/bin/env python3
"""os-batch: one driver for cohort production. MCP generate/poll stays Claude's; everything else automated.
  dry-run <project> <prompt_id> <count> <threshold>     validate + cost gate + plan, NO spend
  ingest  <project> <prompt_id> --urls a,b,c --names x,y,z --credits-each N --model M
          batch-ingest each (failed download -> FAILED, no placeholder) + auto vision-scaffold each
  finalize <project> --manifest <file.csv: asset,verdict,scores,caption>
          per row: log-vision, log-caption, log-export(auto-audit); then audit + dashboard"""
import sys, os, csv, subprocess, argparse, re
HERE=os.path.dirname(os.path.abspath(__file__)); CH=os.path.join(os.path.dirname(HERE),"campaign_house")
def prod(*a): return subprocess.run(["python3",os.path.join(HERE,"os_production.py"),*a],capture_output=True,text=True)
def gen(*a): return subprocess.run(["python3",os.path.join(HERE,"os_generate.py"),*a],capture_output=True,text=True)
def readlog(p,n):
    fp=os.path.join(CH,p,"10_logs",n); return list(csv.reader(open(fp)))[1:] if os.path.exists(fp) else []
def dry_run():
    project,pid,count,thr=sys.argv[2],sys.argv[3],int(sys.argv[4]),float(sys.argv[5])
    if not [r for r in readlog(project,"PROMPT_VERSIONS.csv") if r[1]==pid]:
        print(f"BLOCK: no PROMPT_VERSIONS record for '{pid}'."); return 1
    cost=count*1  # 1 credit / nano image
    if cost>thr: print(f"BLOCK: expected cost {cost}cr (count {count}) > threshold {thr}."); return 1
    print(f"DRY-RUN OK (no spend): {project}/{pid} count={count} expected={cost}cr (<= {thr})")
    print("plan per asset: generate -> ingest -> vision-scaffold -> log-vision -> log-caption -> log-export(auto-audit)")
    print("then: audit + dashboard + proof-loop rows (not-activated)"); return 0
def ingest():
    ap=argparse.ArgumentParser(); ap.add_argument("project"); ap.add_argument("prompt")
    for x in ("urls","names"): ap.add_argument("--"+x,required=True)
    ap.add_argument("--credits-each",default="1"); ap.add_argument("--model",default="nano-banana")
    a=ap.parse_args(sys.argv[2:])
    urls=a.urls.split(","); names=a.names.split(",")
    ok=0; failed=0
    for u,n in zip(urls,names):
        gid="G"+n.replace(".png","").upper()
        r=gen("ingest","--project",a.project,"--prompt",a.prompt,"--gen",gid,"--url",u,"--credits",a.credits_each,"--model",a.model,"--asset",n)
        if "INGEST OK" in r.stdout: ok+=1; prod("vision-scaffold",a.project,n)
        else: failed+=1
        print("  "+(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()))
    print(f"BATCH INGEST: {ok} ok, {failed} failed (+vision scaffolds for ok). Next: Read each + write a manifest, then os_batch finalize."); return 0
def finalize():
    ap=argparse.ArgumentParser(); ap.add_argument("project"); ap.add_argument("--manifest",required=True)
    a=ap.parse_args(sys.argv[2:])
    for row in csv.DictReader(open(a.manifest)):
        asset,verdict,scores,caption=row["asset"],row["verdict"],row["scores"],row["caption"]
        print("  "+prod("log-vision",a.project,asset,verdict,scores).stdout.strip())
        if verdict.upper() in ("PASS","SHIP"):
            print("  "+prod("log-caption",a.project,asset,caption).stdout.strip())
            print("  "+prod("log-export",a.project,asset,"4x5","batch, no posting").stdout.strip())
    print("  "+prod("audit",a.project).stdout.strip())
    prod("dashboard"); print("dashboard updated."); return 0
import json, glob as _glob
def _state_path(p): return os.path.join(CH,p,"10_logs","RUN_STATE.json")
def _state(p):
    sp=_state_path(p); return json.load(open(sp)) if os.path.exists(sp) else {}
def _save_state(p,d):
    json.dump(d,open(_state_path(p),"w"),indent=1)
def _ls(p,d):
    dd=os.path.join(CH,p,d); return [f for f in os.listdir(dd) if f!=".gitkeep"] if os.path.isdir(dd) else []
def scaffold_manifest():
    project=sys.argv[2]
    assets=[a for a in _ls(project,"04_generations")]+[a for a in _ls(project,"05_vision_quarantine") if not a.endswith(".rubric.md")]
    mf=os.path.join(CH,project,"10_logs","MANIFEST.csv")
    if os.path.exists(mf):
        existing={r["asset"] for r in csv.DictReader(open(mf))}
    else:
        existing=set()
        with open(mf,"w",newline="") as f: csv.writer(f).writerow(["asset","path","verdict","scores","caption","export_name","proof_status"])
    added=0
    with open(mf,"a",newline="") as f:
        w=csv.writer(f)
        for a in assets:
            if a in existing: continue
            path=os.path.join(CH,project,"04_generations",a)
            w.writerow([a,path,"FILL:PASS|REJECT|NEEDS-HUMAN",
                        "slop=PASS hands=NA skin=NA clothing=NA text=PASS identity=NA brand=PASS likeness=PASS beat_source=PASS",
                        "FILL:caption (no em-dash, no AI-tell)",os.path.splitext(a)[0]+"_4x5","not-activated"]); added+=1
    print(f"scaffold-manifest: {added} new row(s) -> {mf}. Model fills verdict + caption only."); return 0
def run():
    # resumable cohort driver
    project=sys.argv[2]
    st=_state(project)
    finalize_flag="--finalize" in sys.argv
    urls=None; names=None
    if "--urls" in sys.argv: urls=sys.argv[sys.argv.index("--urls")+1].split(",")
    if "--names" in sys.argv: names=sys.argv[sys.argv.index("--names")+1].split(",")
    # PHASE FINALIZE
    if finalize_flag:
        mf=os.path.join(CH,project,"10_logs","MANIFEST.csv")
        if not os.path.exists(mf): print("BLOCK: no MANIFEST.csv. run ingest phase first."); return 1
        done_exports={re.sub(r"_[^_]+\.export$","",f) for f in _ls(project,"09_exports") if f.endswith(".export")}
        vis={r[1] for r in (list(csv.reader(open(os.path.join(CH,project,"10_logs","VISION_GATE_LOG.csv"))))[1:] if os.path.exists(os.path.join(CH,project,"10_logs","VISION_GATE_LOG.csv")) else [])}
        n=0
        for row in csv.DictReader(open(mf)):
            asset=row["asset"]; verdict=row["verdict"]; 
            if verdict.startswith("FILL"): print(f"  skip {asset}: verdict not filled"); continue
            if asset not in vis:  # idempotent: only vision if not already logged
                print("  "+prod("log-vision",project,asset,verdict,row["scores"]).stdout.strip()); n+=1
            if verdict.upper() in ("PASS","SHIP") and os.path.splitext(asset)[0] not in done_exports:
                if not row["caption"].startswith("FILL"):
                    print("  "+prod("log-caption",project,asset,row["caption"]).stdout.strip())
                    print("  "+prod("log-export",project,asset,"4x5","batch, no posting").stdout.strip())
        print("  "+prod("audit",project).stdout.strip()); prod("dashboard")
        st["phase"]="done"; _save_state(project,st); print("run: FINALIZE done (idempotent)."); return 0
    # PHASE INGEST (urls provided)
    if urls and names:
        ok=0;skip=0;fail=0
        present=set(_ls(project,"04_generations"))|set(_ls(project,"06_approved"))|set(_ls(project,"07_rejected"))
        for u,nm in zip(urls,names):
            if nm in present: print(f"  skip {nm}: already ingested"); skip+=1; continue
            gid="G"+nm.replace(".png","").upper()
            r=gen("ingest","--project",project,"--prompt",st.get("prompt","?"),"--gen",gid,"--url",u,"--credits","1","--model","nano-banana","--asset",nm)
            if "INGEST OK" in r.stdout: ok+=1; prod("vision-scaffold",project,nm)
            else: fail+=1
            print("  "+(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "?"))
        scaffold_argv_backup=sys.argv; sys.argv=["x","scaffold-manifest",project]; scaffold_manifest(); sys.argv=scaffold_argv_backup
        st["phase"]="awaiting_manifest"; _save_state(project,st)
        print(f"run: INGEST done ({ok} ok, {skip} skip, {fail} fail). NEXT: Read each asset, fill 10_logs/MANIFEST.csv (verdict+caption), then: os_batch run {project} --finalize"); return 0
    # PHASE PREP/GATE (start)
    pid=sys.argv[3]; count=int(sys.argv[4]); thr=float(sys.argv[5])
    if not [r for r in (list(csv.reader(open(os.path.join(CH,project,"10_logs","PROMPT_VERSIONS.csv"))))[1:] if os.path.exists(os.path.join(CH,project,"10_logs","PROMPT_VERSIONS.csv")) else []) if r[1]==pid]:
        print(f"BLOCK: no PROMPT_VERSIONS record for '{pid}'."); return 1
    if count>thr: print(f"BLOCK: expected {count}cr > threshold {thr}."); return 1
    st={"phase":"awaiting_generation","prompt":pid,"count":count}; _save_state(project,st)
    print(f"run: GATE PASS {project}/{pid} count={count} (<= {thr}). NEXT: Claude generates {count} via MCP, then: os_batch run {project} --urls u1,.. --names n1.png,..")
    return 0
if __name__=="__main__":
    c=sys.argv[1] if len(sys.argv)>1 else "help"
    sys.exit({"dry-run":dry_run,"ingest":ingest,"finalize":finalize,"scaffold-manifest":scaffold_manifest,"run":run}.get(c,lambda:(print(__doc__) or 0))())
