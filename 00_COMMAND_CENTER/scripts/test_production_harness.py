#!/usr/bin/env python3
"""Regression suite for the production harness. No credits. Run before any future change.
Sets up throwaway _test_* projects, asserts each gate, cleans up."""
import subprocess, os, sys, shutil, csv
HERE=os.path.dirname(os.path.abspath(__file__)); CH=os.path.join(os.path.dirname(HERE),"campaign_house")
def run(script,*a): return subprocess.run(["python3",os.path.join(HERE,script),*a],capture_output=True,text=True)
def prod(*a): return run("os_production.py",*a)
def gen(*a): return run("os_generate.py",*a)
PASS=0; FAIL=0; LOG=[]
def check(name,cond):
    global PASS,FAIL
    if cond: PASS+=1; LOG.append(f"  PASS  {name}")
    else: FAIL+=1; LOG.append(f"  FAIL  {name}")
def setup(slug):
    if os.path.exists(os.path.join(CH,slug)): shutil.rmtree(os.path.join(CH,slug))
    prod("new",slug)
def teardown(slug):
    if os.path.exists(os.path.join(CH,slug)): shutil.rmtree(os.path.join(CH,slug))

T="_test_harness"
setup(T)
# 1 missing prompt blocks generation
r=prod("log-generation",T,"G1","NOPROMPT","nano","p","1","x.png","raw"); check("missing-prompt blocks", "BLOCK" in r.stdout)
prod("log-prompt",T,"P1","1","hero","nano","a clean concrete object, no people, no text")
# 2 over-budget blocks (os_generate prep)
r=gen("prep",T,"P1","99","5"); check("over-budget blocks", "BLOCK" in r.stdout)
# 3 bad URL failure + 4 no fake asset
r=gen("ingest","--project",T,"--prompt","P1","--gen","GBAD","--url","http://bad.invalid/x.png","--credits","1","--model","nano","--asset","bad.png")
check("bad-url -> FAILED", "FAILED" in r.stdout)
check("failed ingest creates no asset", not os.path.exists(os.path.join(CH,T,"04_generations","bad.png")))
check("failure logged", os.path.exists(os.path.join(CH,T,"10_logs","FAILURES.csv")))
# 5 export blocks before caption pass (make a fake approved asset via a real local file)
fa=os.path.join(CH,T,"06_approved","real.png"); open(fa,"w").write("x"*2000)
# log a vision record so audit is clean for it
prod("log-vision",T,"real.png","PASS","slop=PASS text=PASS brand=PASS likeness=PASS beat_source=PASS hands=NA skin=NA clothing=NA identity=NA")
r=prod("log-export",T,"real.png","4x5","x"); check("export blocks before caption", "BLOCK" in r.stdout)
prod("log-caption",T,"real.png","Clean stone. One light.")
r=prod("log-export",T,"real.png","4x5","x"); check("export works after caption", "export logged" in r.stdout)
# 6 proof update blocks before activation
r=prod("proof","update",T,"real.png","24h","999 saves"); check("proof update blocks pre-activation", "BLOCK" in r.stdout)
# 7 clean removes trash, keeps records
open(os.path.join(CH,T,"04_generations","junk.FAILED"),"w").close()
open(os.path.join(CH,T,"00_intake","empty.tmp"),"w").close()
prod("clean",T)
check("clean removed .FAILED", not os.path.exists(os.path.join(CH,T,"04_generations","junk.FAILED")))
check("clean removed empty", not os.path.exists(os.path.join(CH,T,"00_intake","empty.tmp")))
check("clean kept approved/export", os.path.exists(fa) and any(f.endswith(".export") for f in os.listdir(os.path.join(CH,T,"09_exports"))))
check("clean kept prompt record", os.path.exists(os.path.join(CH,T,"03_prompts","P1_v1.txt")))
# 8 audit clean + registry/dashboard agree
r=prod("audit",T); check("audit clean after valid flow", "CLEAN" in r.stdout)
prod("registry"); 
reg={row["project"]:row for row in csv.DictReader(open(os.path.join(os.path.dirname(HERE),"OS_PRODUCTION_REGISTRY.csv")))}
check("registry lists test project", T in reg)
teardown(T); prod("registry")
print("\n".join(LOG)); print(f"\nRESULT: {PASS} pass / {FAIL} fail")
sys.exit(0 if FAIL==0 else 1)
