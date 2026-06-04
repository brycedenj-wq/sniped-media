#!/usr/bin/env python3
"""os-batch: one driver for cohort production. MCP generate/poll stays Claude's; everything else automated.
  dry-run <project> <prompt_id> <count> <threshold>     validate + cost gate + plan, NO spend
  ingest  <project> <prompt_id> --urls a,b,c --names x,y,z --credits-each N --model M
          batch-ingest each (failed download -> FAILED, no placeholder) + auto vision-scaffold each
  finalize <project> --manifest <file.csv: asset,verdict,scores,caption>
          per row: log-vision, log-caption, log-export(auto-audit); then audit + dashboard"""
import sys, os, csv, subprocess, argparse
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
if __name__=="__main__":
    c=sys.argv[1] if len(sys.argv)>1 else "help"
    sys.exit({"dry-run":dry_run,"ingest":ingest,"finalize":finalize}.get(c,lambda:(print(__doc__) or 0))())
