#!/usr/bin/env python3
"""os-generate: safe generation flow (image + video).
  prep <project> <prompt_id> <cost_credits> [threshold=5]
       validate prompt record (BLOCK if none) + cost<=threshold (BLOCK if over); print prompt + gen_id.
  ingest --project P --prompt PID --gen GID --url URL --credits N --model M --asset name.png
       download (FAILED-not-complete on bad/empty download; NO placeholder asset; failure -> 10_logs/FAILURES.csv).
  prep-video <project> <prompt_id> <seconds> [--rate cr_per_sec] [--threshold cr]
       preflight a video gen: BLOCK if no prompt record; estimate credits = ceil(seconds*rate);
       BLOCK if est>threshold. Rate is ASSUMED until confirmed against live Higgsfield pricing. No spend.
  ingest-video --project P --prompt PID --gen GID --url URL --credits N --model M --asset name.mp4
       download mp4 (FAILED-not-complete on bad/<50KB; NO placeholder asset; failure -> FAILURES.csv)."""
import sys, os, csv, subprocess, time, argparse, math

# Higgsfield video credit rate is ASSUMED here and MUST be confirmed against live pricing
# (show_plans_and_credits / models_explore) before any real spend. Not a fabricated fact.
ASSUMED_VIDEO_RATE_CR_PER_SEC = None  # None => estimator refuses to invent a number
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
def estimate_video_credits(seconds, rate):
    """Pure estimator. Returns (credits:int|None, note). Refuses to invent a rate."""
    if rate is None:
        return None, "rate UNCONFIRMED , confirm cr/sec via Higgsfield plans before spend"
    return int(math.ceil(seconds * rate)), f"est = ceil({seconds}s * {rate} cr/sec)"

def prep_video():
    ap=argparse.ArgumentParser()
    ap.add_argument("project"); ap.add_argument("prompt_id"); ap.add_argument("seconds",type=float)
    ap.add_argument("--rate",type=float,default=ASSUMED_VIDEO_RATE_CR_PER_SEC)
    ap.add_argument("--threshold",type=float,default=20)
    a=ap.parse_args(sys.argv[2:])
    rec=[r for r in readlog(a.project,"PROMPT_VERSIONS.csv") if r[1]==a.prompt_id]
    if not rec: print(f"BLOCK: no PROMPT_VERSIONS record for '{a.prompt_id}'. log-prompt first."); return 1
    est,note=estimate_video_credits(a.seconds,a.rate)
    if est is None:
        print(f"PREFLIGHT (no spend): {a.project}/{a.prompt_id} {a.seconds}s , {note}.")
        print("STOP: cannot estimate credits without a confirmed rate. Confirm live, then re-run with --rate."); return 2
    if est>a.threshold: print(f"BLOCK: est {est}cr > threshold {a.threshold}. Raise threshold explicitly."); return 1
    gid=f"V{int(time.time())%100000}"
    print(f"PREP-VIDEO OK (no spend): {a.project}/{a.prompt_id} {a.seconds}s , {note} = {est}cr (<= {a.threshold}). gen_id={gid}")
    print(f"NEXT (only after approval): generate via MCP, then os_generate.py ingest-video --project {a.project} --prompt {a.prompt_id} --gen {gid} --url <URL> --credits {est} --model <model> --asset <name>.mp4")
    return 0

def ingest_video():
    ap=argparse.ArgumentParser()
    for x in ("project","prompt","gen","url","credits","model","asset"): ap.add_argument("--"+x,required=True)
    a=ap.parse_args(sys.argv[2:])
    dst=os.path.join(CH,a.project,"04_generations",a.asset)
    ok = a.url.startswith("http") and subprocess.run(["curl","-sf","-o",dst,a.url]).returncode==0 and os.path.exists(dst) and os.path.getsize(dst)>=50000
    if not ok:
        if os.path.exists(dst): os.remove(dst)   # NO placeholder asset
        fp=os.path.join(CH,a.project,"10_logs","FAILURES.csv"); new=not os.path.exists(fp)
        with open(fp,"a",newline="") as f:
            w=csv.writer(f)
            if new: w.writerow(["ts","gen_id","prompt_id","url","reason"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M"),a.gen,a.prompt,a.url,"video_download_failed_or_too_small"])
        prod("log-generation",a.project,a.gen,a.prompt,a.model,"FAILED","0","_none","failed")
        print(f"VIDEO DOWNLOAD FAILED -> {a.gen} logged, NO asset, generation marked failed."); return 1
    kb=os.path.getsize(dst)//1024
    print(prod("log-generation",a.project,a.gen,a.prompt,a.model,f"downloaded,{kb}KB",a.credits,a.asset,"raw").stdout.strip())
    print(f"INGEST-VIDEO OK: {a.asset} ({kb}KB) in harness."); return 0

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
    routes={"prep":prep,"ingest":ingest,"prep-video":prep_video,"ingest-video":ingest_video}
    sys.exit(routes[c]() if c in routes else (print(__doc__) or 0))
