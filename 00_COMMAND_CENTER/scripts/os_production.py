#!/usr/bin/env python3
"""os-production: campaign-house harness. Every production action has ONE command -> correct log.
new | log-prompt | log-generation | log-vision | log-edit | log-caption | log-export | log-skill
| status | audit | close | dashboard | list"""
import sys, os, csv, time, shutil, re
CC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT=os.path.join(CC,"campaign_house")
SUB=["00_intake","01_character_refs","02_style_refs","03_prompts","04_generations",
     "05_vision_quarantine","06_approved","07_rejected","08_edits","09_exports","10_logs"]
LOGS={
 "10_logs/PROMPT_VERSIONS.csv":"ts,prompt_id,version,stage,model,prompt_file,notes",
 "10_logs/GENERATION_LOG.csv":"ts,gen_id,prompt_id,model,params,credits_est,asset,status",
 "10_logs/VISION_GATE_LOG.csv":"ts,asset,verdict,scores,reviewer",
 "10_logs/EDIT_LOG.csv":"ts,asset,edit,tool,from_version,to_version,notes",
 "10_logs/CAPTION_VOICE_LOG.csv":"ts,asset,caption_file,em_dash,ai_tell,verdict",
 "10_logs/SKILL_EXTRACTION_LOG.csv":"ts,observation,repeat_count,skill_candidate,status",
 "10_logs/PROOF_LOOP_DASHBOARD.md":"# Proof-loop dashboard (proof not faked; not-activated until posted)\n\n| asset_id | channel | posted? | 24h_signal | 7d_signal | kill/keep/scale | notes |\n|---|---|---|---|---|---|---|\n",
}
AI_TELLS=["in today's","that being said","it's worth noting","at its core","delve into","in conclusion","tapestry","testament to"]
def P(s): return os.path.join(ROOT,s)
def lp(s,n): return os.path.join(P(s),"10_logs",n)
def append(s,n,row):
    with open(lp(s,n),"a",newline="") as f: csv.writer(f).writerow(row)
def readlog(s,n):
    fp=lp(s,n); return list(csv.reader(open(fp)))[1:] if os.path.exists(fp) else []
def ls_dir(s,d):
    dd=os.path.join(P(s),d); return [f for f in os.listdir(dd) if f!=".gitkeep"] if os.path.isdir(dd) else []
def new(s):
    if os.path.exists(P(s)): print("exists: "+s); return 1
    for x in SUB: os.makedirs(os.path.join(P(s),x),exist_ok=True); open(os.path.join(P(s),x,".gitkeep"),"w").close()
    for path,hdr in LOGS.items(): open(os.path.join(P(s),path),"w").write(hdr+("" if hdr.endswith("\n") else "\n"))
    open(os.path.join(P(s),"PROJECT.md"),"w").write("# Production project: "+s+"\nCreated: "+time.strftime("%Y-%m-%d")+"\nStatus: active (EXPERIMENT, not a strategy/brand decision)\n")
    print("scaffolded "+s); return 0
def log_prompt(s,pid,ver,stage,model,text):
    pf=pid+"_v"+ver+".txt"; open(os.path.join(P(s),"03_prompts",pf),"w").write(text)
    append(s,"PROMPT_VERSIONS.csv",[time.strftime("%Y-%m-%d %H:%M"),pid,ver,stage,model,pf,""]); print("prompt "+pid+" v"+ver+" logged"); return 0
def log_generation(s,gid,pid,model,params,credits,asset,status):
    if pid not in [r[1] for r in readlog(s,"PROMPT_VERSIONS.csv")]:
        print("BLOCK: prompt_id '"+pid+"' has no PROMPT_VERSIONS record. log-prompt first."); return 1
    if status!="failed": open(os.path.join(P(s),"04_generations",asset),"a").close()
    append(s,"GENERATION_LOG.csv",[time.strftime("%Y-%m-%d %H:%M"),gid,pid,model,params,credits,asset,status]); print("generation "+gid+" logged"); return 0
RUBRIC=["slop","hands","skin","clothing","text","identity","brand","likeness","beat_source"]
def vision_review(s,asset):
    src=os.path.join(P(s),"04_generations",asset)
    if not os.path.exists(src): src=os.path.join(P(s),"05_vision_quarantine",asset)
    print("VISION REVIEW for "+asset+" (path: "+src+")")
    print("Model: Read the asset and score each item PASS/FAIL, then call:")
    print("  os_production.py log-vision "+s+" "+asset+" <PASS|REJECT|NEEDS-HUMAN> \"slop=PASS hands=PASS ...\" [--override \"reason\"]")
    for r in RUBRIC: print("  [ ] "+r)
    return 0
def log_vision(s,asset,verdict,scores,override=""):
    verdict=verdict.upper()
    if verdict not in ("PASS","REJECT","NEEDS-HUMAN","SHIP"):
        print("BLOCK: verdict must be PASS / REJECT / NEEDS-HUMAN"); return 1
    if verdict=="SHIP": verdict="PASS"
    src=os.path.join(P(s),"04_generations",asset)
    if not os.path.exists(src): src=os.path.join(P(s),"05_vision_quarantine",asset)
    if verdict=="PASS": dest="06_approved"
    elif verdict=="REJECT": dest="07_rejected"
    else: dest="05_vision_quarantine"  # NEEDS-HUMAN stays quarantined
    if os.path.exists(src) and os.path.dirname(src)!=os.path.join(P(s),dest):
        shutil.move(src,os.path.join(P(s),dest,os.path.basename(asset)))
    # if a human override flips the model verdict, the reason is mandatory (already passed as override)
    rev = "human-override:"+override if override else "model"
    if verdict in ("PASS","REJECT") and override=="" and "NEEDS-HUMAN" in scores.upper():
        print("note: model flagged NEEDS-HUMAN; logging "+verdict+" without an override reason is discouraged.")
    append(s,"VISION_GATE_LOG.csv",[time.strftime("%Y-%m-%d %H:%M"),asset,verdict,scores,rev]); print("vision "+verdict+" -> "+dest+" ("+rev+")"); return 0
def log_edit(s,asset,edit,tool,fv,tv,notes):
    append(s,"EDIT_LOG.csv",[time.strftime("%Y-%m-%d %H:%M"),asset,edit,tool,fv,tv,notes]); print("edit logged"); return 0
def log_caption(s,asset,caption):
    cf=os.path.splitext(asset)[0]+"_caption.txt"; open(os.path.join(P(s),"09_exports",cf),"w").write(caption)
    em="FAIL" if ("—" in caption) else "PASS"
    tell="FAIL" if any(t in caption.lower() for t in AI_TELLS) else "PASS"
    verdict="PASS" if em=="PASS" and tell=="PASS" else "FAIL"
    append(s,"CAPTION_VOICE_LOG.csv",[time.strftime("%Y-%m-%d %H:%M"),asset,cf,em,tell,verdict])
    print("caption voice-gate: em_dash="+em+" ai_tell="+tell+" -> "+verdict); return 0 if verdict=="PASS" else 1
def log_export(s,asset,fmt,notes):
    import io,contextlib; buf=io.StringIO()
    with contextlib.redirect_stdout(buf): blocked=audit(s)==1
    if blocked: print("BLOCK: audit has blockers, cannot export. Run: os_production.py audit "+s); return 1
    if not [r for r in readlog(s,"CAPTION_VOICE_LOG.csv") if r[1]==asset and r[5]=="PASS"]:
        print("BLOCK: export of '"+asset+"' requires a PASSing caption/voice record. log-caption first."); return 1
    open(os.path.join(P(s),"09_exports",os.path.splitext(asset)[0]+"_"+fmt+".export"),"w").write(notes)
    # proof-loop activation (NOT activated; we are not posting)
    pl=os.path.join(P(s),"10_logs","PROOF_LOOP_DASHBOARD.md")
    concept=""
    pv=readlog(s,"PROMPT_VERSIONS.csv")
    if pv: concept=pv[-1][3]
    with open(pl,"a") as f:
        f.write("| "+asset+" | (no channel) | no | not-activated | not-activated | pending | exported "+time.strftime("%Y-%m-%d")+", not posted |\n")
    print("export logged for "+asset+" + proof-loop row (not activated)"); return 0
def log_skill(s,obs,repeat,cand,status):
    append(s,"SKILL_EXTRACTION_LOG.csv",[time.strftime("%Y-%m-%d %H:%M"),obs,repeat,cand,status]); print("skill candidate logged"); return 0
def vision_scaffold(s,asset):
    src=os.path.join(P(s),"04_generations",asset)
    if not os.path.exists(src): src=os.path.join(P(s),"05_vision_quarantine",asset)
    if not os.path.exists(src): print("BLOCK: asset not found: "+asset); return 1
    # prefilled rubric; person-items default NA (operator/model flips to PASS/FAIL after Reading)
    items=[("slop","?"),("hands","NA"),("skin","NA"),("clothing","NA"),("text","?"),("identity","NA"),("brand","?"),("likeness","?"),("beat_source","?")]
    rf=os.path.join(P(s),"05_vision_quarantine",asset+".rubric.md")
    os.makedirs(os.path.dirname(rf),exist_ok=True)
    with open(rf,"w") as f:
        f.write("# Vision scaffold for "+asset+"\nMODEL: Read "+src+" and set each ? to PASS/FAIL. person-items are NA unless people appear.\n\n")
        for k,v in items: f.write("- "+k+": "+v+"\n")
        f.write("\nThen: os_production.py log-vision "+s+" "+asset+" <PASS|REJECT|NEEDS-HUMAN> \"slop=PASS text=PASS brand=PASS likeness=PASS beat_source=PASS hands=NA skin=NA clothing=NA identity=NA\" [--override \"reason\"]\n")
    print("scaffold written: "+rf); print("ASSET to Read: "+src)
    return 0

def _pl(s): return os.path.join(P(s),"10_logs","PROOF_LOOP_DASHBOARD.md")
def proof_activate(s,asset,channel):
    p=_pl(s); lines=open(p).read().splitlines(); out=[]; hit=False
    for ln in lines:
        if ln.startswith("| "+asset+" "):
            cols=[c.strip() for c in ln.strip("|").split("|")]
            cols[1]=channel; cols[2]="yes"; cols[3]="0 (clock started "+time.strftime("%Y-%m-%d %H:%M")+")"; cols[4]="pending"; cols[6]="ACTIVATED "+time.strftime("%Y-%m-%d %H:%M")
            ln="| "+" | ".join(cols)+" |"; hit=True
        out.append(ln)
    open(p,"w").write("\n".join(out)+"\n")
    print("proof ACTIVATED for "+asset+" on "+channel if hit else "no proof-loop row for "+asset+" (export it first)"); return 0 if hit else 1
def proof_update(s,asset,field,value):
    p=_pl(s); idx={"24h":3,"7d":4,"verdict":5,"notes":6}.get(field)
    if idx is None: print("field must be 24h|7d|verdict|notes"); return 1
    lines=open(p).read().splitlines(); out=[]; hit=False
    for ln in lines:
        if ln.startswith("| "+asset+" "):
            cols=[c.strip() for c in ln.strip("|").split("|")]
            if cols[2]!="yes": print("BLOCK: cannot log signal for un-activated asset (no fake proof). proof activate first."); return 1
            cols[idx]=value; ln="| "+" | ".join(cols)+" |"; hit=True
        out.append(ln)
    open(p,"w").write("\n".join(out)+"\n"); print("proof updated "+field+"="+value if hit else "no row"); return 0 if hit else 1
def proof_status(s):
    p=_pl(s); print(open(p).read() if os.path.exists(p) else "no proof loop"); return 0

def status(s):
    print(s+": prompts="+str(len(ls_dir(s,"03_prompts")))+" gens="+str(len(ls_dir(s,"04_generations")))+
          " quarantine="+str(len(ls_dir(s,"05_vision_quarantine")))+" approved="+str(len(ls_dir(s,"06_approved")))+
          " rejected="+str(len(ls_dir(s,"07_rejected")))+" exports="+str(len([f for f in ls_dir(s,"09_exports") if f.endswith(".export")]))); return 0
def audit(s):
    blockers=[]; warnings=[]
    pv={r[5] for r in readlog(s,"PROMPT_VERSIONS.csv")}
    for f in ls_dir(s,"03_prompts"):
        if f not in pv: blockers.append("prompt file "+f+" has no PROMPT_VERSIONS entry")
    gen={r[6] for r in readlog(s,"GENERATION_LOG.csv")}
    for f in ls_dir(s,"04_generations"):
        if f not in gen: blockers.append("generation "+f+" has no GENERATION_LOG entry")
    vis={r[1] for r in readlog(s,"VISION_GATE_LOG.csv")}
    for f in ls_dir(s,"06_approved"):
        if f not in vis: blockers.append("approved asset "+f+" has no VISION_GATE record")
    cappass={os.path.splitext(r[1])[0] for r in readlog(s,"CAPTION_VOICE_LOG.csv") if r[5]=="PASS"}
    for f in ls_dir(s,"09_exports"):
        if f.endswith(".export"):
            base=re.sub(r"_[^_]+\.export$","",f)
            if base not in cappass: blockers.append("export "+f+" has no PASSing caption/voice check")
    if not os.path.exists(os.path.join(P(s),"10_logs","PROOF_LOOP_DASHBOARD.md")): blockers.append("missing PROOF_LOOP_DASHBOARD")
    approved_base={os.path.splitext(f)[0] for f in ls_dir(s,"06_approved")}
    for a in gen:
        if a in ("_none","") : continue
        if a and a not in vis and os.path.splitext(a)[0] not in approved_base: warnings.append("generation "+a+" awaiting vision gate")
    for f in ls_dir(s,"06_approved"):
        if os.path.splitext(f)[0] not in cappass: warnings.append("approved "+f+" awaiting caption/export")
    if ls_dir(s,"07_rejected"): warnings.append(str(len(ls_dir(s,"07_rejected")))+" rejected asset(s) unresolved")
    print("AUDIT "+s+": "+("CLEAN" if not blockers else "BLOCKED"))
    for b in blockers: print("  BLOCKER: "+b)
    for w in warnings: print("  warning: "+w)
    return 1 if blockers else 0
def close(s):
    if audit(s)!=0: print("CANNOT CLOSE: audit has blockers."); return 1
    pm=os.path.join(P(s),"PROJECT.md"); t=open(pm).read()
    open(pm,"w").write(re.sub(r"Status: .*","Status: CLOSED "+time.strftime("%Y-%m-%d"),t)); print("closed "+s); return 0
def dashboard():
    import io,contextlib
    if not os.path.isdir(ROOT): print("no projects"); return 0
    rows=[]
    for p in sorted(os.listdir(ROOT)):
        b=P(p)
        if not os.path.isdir(b) or not os.path.exists(os.path.join(b,"PROJECT.md")): continue
        closed="CLOSED" in open(os.path.join(b,"PROJECT.md")).read()
        gens=len(ls_dir(p,"04_generations")); appr=len(ls_dir(p,"06_approved")); exp=len([f for f in ls_dir(p,"09_exports") if f.endswith(".export")])
        try: est_cred=sum(float(r[5]) for r in readlog(p,"GENERATION_LOG.csv") if r[5] and r[5] not in ("FAILED","0"))
        except: est_cred=0
        import subprocess as _sp
        cr=_sp.run(["python3",os.path.join(os.path.dirname(os.path.abspath(__file__)),"os_cost.py"),"project",p],capture_output=True,text=True).stdout
        usd=_sp.run(["python3",os.path.join(os.path.dirname(os.path.abspath(__file__)),"os_cost.py"),"rate"],capture_output=True,text=True).stdout
        rate=None
        import re as _re
        rm=_re.search(r"\$([\d.]+)/credit",usd); rate=float(rm.group(1)) if rm else None
        est_usd=("$%.2f"%(est_cred*rate)) if rate else "UNKNOWN"
        am=_re.search(r"USD=\$([\d.]+)",cr); act_usd="$"+am.group(1) if am else "UNKNOWN"
        buf=io.StringIO()
        with contextlib.redirect_stdout(buf): blocked=audit(p)==1
        state="closed" if closed else ("BLOCKED" if blocked else ("awaiting-export" if appr>exp else ("awaiting-vision" if gens>appr+len(ls_dir(p,"07_rejected")) else "active")))
        last=time.strftime("%Y-%m-%d %H:%M",time.localtime(os.path.getmtime(b)))
        rows.append((p,state,gens,appr,exp,int(est_cred),est_usd,act_usd,last))
    out="# OS PRODUCTION DASHBOARD (campaign house)\n\nDaily command center. Generated "+time.strftime("%Y-%m-%d %H:%M")+".\n\n| project | state | gens | approved | exports | est_credits | est_usd | actual_usd | last updated |\n|---|---|---|---|---|---|---|---|---|\n"
    for r in rows: out+="| "+" | ".join(str(x) for x in r)+" |\n"
    cc={}
    for r in rows: cc[r[1]]=cc.get(r[1],0)+1
    out+="\n**Summary:** "+" · ".join(k+"="+str(v) for k,v in cc.items())+"\n"
    open(os.path.join(CC,"OS_PRODUCTION_DASHBOARD.md"),"w").write(out); print("wrote OS_PRODUCTION_DASHBOARD.md ("+str(len(rows))+" projects)"); return 0
def main():
    a=sys.argv; c=a[1] if len(a)>1 else "list"
    f={"new":lambda:new(a[2]),"log-prompt":lambda:log_prompt(a[2],a[3],a[4],a[5],a[6]," ".join(a[7:])),
       "log-generation":lambda:log_generation(a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]),
       "log-vision":lambda:log_vision(a[2],a[3],a[4],a[5] if len(a)>5 and not a[5].startswith("--") else "", (a[a.index("--override")+1] if "--override" in a else "")),
       "vision-review":lambda:vision_review(a[2],a[3]),
       "log-edit":lambda:log_edit(a[2],a[3],a[4],a[5],a[6],a[7]," ".join(a[8:])),
       "log-caption":lambda:log_caption(a[2],a[3]," ".join(a[4:])),
       "log-export":lambda:log_export(a[2],a[3],a[4]," ".join(a[5:])),
       "log-skill":lambda:log_skill(a[2],a[3],a[4],a[5],a[6] if len(a)>6 else "candidate"),
       "vision-scaffold":lambda:vision_scaffold(a[2],a[3]),
       "proof":lambda:({"activate":lambda:proof_activate(a[3],a[4],a[5]),"update":lambda:proof_update(a[3],a[4],a[5],a[6]),"status":lambda:proof_status(a[3])}[a[2]]()),
       "status":lambda:status(a[2]),"audit":lambda:audit(a[2]),"close":lambda:close(a[2]),"dashboard":dashboard}
    if c in f: return f[c]()
    if os.path.isdir(ROOT):
        for p in sorted(os.listdir(ROOT)):
            if os.path.isdir(P(p)): print(" ",p)
    return 0
if __name__=="__main__": sys.exit(main())
