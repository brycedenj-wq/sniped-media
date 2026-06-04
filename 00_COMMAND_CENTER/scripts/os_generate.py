#!/usr/bin/env python3
"""os-generate: safe generation flow.
  prep <project> <prompt_id> <cost_credits> [threshold=5]
       validate prompt record (BLOCK if none) + cost<=threshold (BLOCK if over); print prompt + gen_id.
  ingest --project P --prompt PID --gen GID --url URL --credits N --model M --asset name.png
       download (FAILED-not-complete on bad/empty download; NO placeholder asset; failure -> 10_logs/FAILURES.csv),
       place into 04_generations, log-generation, cost. If asset lands, it is in the harness automatically."""
import sys, os, csv, subprocess, time, argparse
HERE=os.path.dirname(os.path.abspath(__file__)); CH=os.path.join(os.path.dirname(HERE),"campaign_house")
def prod(*a): return subprocess.run(["python3",os.path.join(HERE,"os_production.py"),*a],capture_output=True,text=True)
def readlog(p,n):
    fp=os.path.join(CH,p,"10_logs",n); return list(csv.reader(open(fp)))[1:] if os.path.exists(fp) else []
def prep():
    project,pid,cost=sys.argv[2],sys.argv[3],float(sys.argv[4]); thr=float(sys.argv[5]) if len(sys.argv)>5 else 5
    rec=[r for r in readlog(project,"PROMPT_VERSIONS.csv") if r[1]==pid]
    if not rec: print(f"BLOCK: no PROMPT_VERSIONS record for '{pid}'. log-prompt first."); return 1
    if cost>thr: print(f"BLOCK: cost {cost} > threshold {thr}. Raise threshold explicitly."); return 1
    pf=rec[-1][5]; ptext=open(os.path.join(CH,project,"03_prompts",pf)).read()
    gid=f"G{int(time.time())%100000}"
    print(f"PREP OK: {project}/{pid} cost={cost}cr (<= {thr}). gen_id={gid}")
    print("PROMPT_TEXT>>>"); print(ptext); print("<<<PROMPT_TEXT")
    print(f"NEXT: Claude generates via MCP, then: os_generate.py ingest --project {project} --prompt {pid} --gen {gid} --url <URL> --credits {int(cost)} --model <model> --asset <name>.png")
    return 0
def ingest():
    ap=argparse.ArgumentParser(); 
    for x in ("project","prompt","gen","url","credits","model","asset"): ap.add_argument("--"+x,required=True)
    a=ap.parse_args(sys.argv[2:])
    dst=os.path.join(CH,a.project,"04_generations",a.asset)
    ok = a.url.startswith("http") and subprocess.run(["curl","-sf","-o",dst,a.url]).returncode==0 and os.path.exists(dst) and os.path.getsize(dst)>=1000
    if not ok:
        if os.path.exists(dst): os.remove(dst)   # NO placeholder asset
        fp=os.path.join(CH,a.project,"10_logs","FAILURES.csv")
        new=not os.path.exists(fp)
        with open(fp,"a",newline="") as f:
            w=csv.writer(f); 
            if new: w.writerow(["ts","gen_id","prompt_id","url","reason"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M"),a.gen,a.prompt,a.url,"download_failed_or_bad_url"])
        prod("log-generation",a.project,a.gen,a.prompt,a.model,"FAILED","0","_none","failed")
        print(f"DOWNLOAD FAILED -> {a.gen} logged to FAILURES.csv, NO asset created, generation marked failed."); return 1
    kb=os.path.getsize(dst)//1024
    print(prod("log-generation",a.project,a.gen,a.prompt,a.model,f"downloaded,{kb}KB",a.credits,a.asset,"raw").stdout.strip())
    print(f"INGEST OK: {a.asset} ({kb}KB) in harness."); return 0
if __name__=="__main__":
    c=sys.argv[1] if len(sys.argv)>1 else "help"
    sys.exit(prep() if c=="prep" else ingest() if c=="ingest" else (print(__doc__) or 0))
