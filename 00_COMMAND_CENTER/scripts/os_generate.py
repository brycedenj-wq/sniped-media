#!/usr/bin/env python3
"""os-generate: collapse the generation flow into safe enforced steps.
  prep <project> <prompt_id> <cost_credits> [threshold=5]
      validates the prompt record exists (BLOCK if not), enforces cost<=threshold (BLOCK if over),
      prints the prompt text + a gen_id. -> Claude then calls Higgsfield generate_image + job_status.
  ingest <project> <prompt_id> <gen_id> <url> <credits> <model> <asset_name>
      downloads (mark FAILED if download fails, not complete), places into 04_generations,
      runs log-generation, logs cost (credits). If the asset lands, it is IN the harness automatically."""
import sys, os, csv, subprocess, time
HERE=os.path.dirname(os.path.abspath(__file__))
def prod(*a): return subprocess.run(["python3",os.path.join(HERE,"os_production.py"),*a],capture_output=True,text=True)
def readlog(project,name):
    fp=os.path.join(os.path.dirname(HERE),"campaign_house",project,"10_logs",name)
    return list(csv.reader(open(fp)))[1:] if os.path.exists(fp) else []
def prep():
    project,pid,cost=sys.argv[2],sys.argv[3],float(sys.argv[4]); thr=float(sys.argv[5]) if len(sys.argv)>5 else 5
    prompts=readlog(project,"PROMPT_VERSIONS.csv")
    rec=[r for r in prompts if r[1]==pid]
    if not rec: print(f"BLOCK: no PROMPT_VERSIONS record for '{pid}'. Run os_production.py log-prompt first."); return 1
    if cost>thr: print(f"BLOCK: cost {cost} credits > threshold {thr}. Raise threshold explicitly to proceed."); return 1
    pf=rec[-1][5]; ptext=open(os.path.join(os.path.dirname(HERE),"campaign_house",project,"03_prompts",pf)).read()
    gen_id=f"G{int(time.time())%100000}"
    print(f"PREP OK: project={project} prompt={pid} cost={cost}cr (<= {thr}). gen_id={gen_id}")
    print("PROMPT_TEXT>>>"); print(ptext); print("<<<PROMPT_TEXT")
    print(f"NEXT: Claude calls Higgsfield generate_image with this prompt, polls job_status, then:")
    print(f"  os_generate.py ingest {project} {pid} {gen_id} <url> {int(cost)} <model> <asset_name>.png")
    return 0
def ingest():
    project,pid,gid,url,credits,model,asset=sys.argv[2:9]
    dst_dir=os.path.join(os.path.dirname(HERE),"campaign_house",project,"04_generations")
    dst=os.path.join(dst_dir,asset)
    rc=subprocess.run(["curl","-sf","-o",dst,url]).returncode
    if rc!=0 or not os.path.exists(dst) or os.path.getsize(dst)<1000:
        # download failed -> log as FAILED, not complete
        if os.path.exists(dst): os.remove(dst)
        prod("log-generation",project,gid,pid,model,"download_failed",credits,asset+".FAILED","failed")
        print(f"DOWNLOAD FAILED for {url} -> generation {gid} marked FAILED (not complete)."); return 1
    kb=os.path.getsize(dst)//1024
    r=prod("log-generation",project,gid,pid,model,f"downloaded,{kb}KB",credits,asset,"raw")
    print(r.stdout.strip())
    print(f"INGEST OK: {asset} ({kb}KB) in harness. Next: os_production.py vision-auto {project} {asset}")
    return 0
if __name__=="__main__":
    c=sys.argv[1] if len(sys.argv)>1 else "help"
    sys.exit(prep() if c=="prep" else ingest() if c=="ingest" else (print(__doc__) or 0))
