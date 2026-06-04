#!/usr/bin/env python3
"""os-production: scaffold + manage a campaign-house production project. Nothing gets lost,
every prompt/decision/asset is versioned and logged. Assets (binaries) are gitignored; logs are tracked.
Usage:
  os_production.py new <project-slug>     - scaffold a fresh project tree + log headers
  os_production.py list                   - list projects + their status
  os_production.py status <project-slug>  - show counts (assets, gate records, approved/rejected)"""
import sys, os, csv, datetime
ROOT=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"campaign_house")
SUB = ["00_intake","01_character_refs","02_style_refs","03_prompts","04_generations",
       "05_vision_quarantine","06_approved","07_rejected","08_edits","09_exports","10_logs"]
LOGS = {
 "10_logs/PROMPT_VERSIONS.csv": "ts,prompt_id,version,stage,model,prompt_text_ref,notes",
 "10_logs/GENERATION_LOG.csv": "ts,gen_id,prompt_id,model,params,credits_est,asset_path,status",
 "10_logs/VISION_GATE_LOG.csv": "ts,asset,verdict,slop,hands,skin,clothing,text,identity,brand,likeness,beat_source,reviewer,notes",
 "10_logs/EDIT_LOG.csv": "ts,asset,edit,tool,from_version,to_version,notes",
 "10_logs/CAPTION_VOICE_LOG.csv": "ts,asset,caption_ref,voice_gate,em_dash_check,ai_tell_check,verdict",
 "10_logs/SKILL_EXTRACTION_LOG.csv": "ts,observation,repeat_count,skill_candidate,status",
 "10_logs/PROOF_LOOP_DASHBOARD.md": "# Proof-loop dashboard\n\n| asset | posted? | metric | 24h | 7d | kill/keep/scale |\n|---|---|---|---|---|---|\n",
}
def new(slug):
    base=os.path.join(ROOT,slug)
    if os.path.exists(base): print(f"exists: {base}"); return 1
    for s in SUB: os.makedirs(os.path.join(base,s),exist_ok=True); open(os.path.join(base,s,".gitkeep"),"w").close()
    for path,hdr in LOGS.items():
        fp=os.path.join(base,path); open(fp,"w").write(hdr+("\n" if not hdr.endswith("\n") else ""))
    open(os.path.join(base,"PROJECT.md"),"w").write(f"# Production project: {slug}\nCreated: {datetime.date.today()}\nStatus: active (EXPERIMENT, not a strategy/brand decision)\n\nTree: intake -> character_refs -> style_refs -> prompts -> generations -> vision_quarantine -> approved/rejected -> edits -> exports. Logs in 10_logs/.\n")
    print(f"scaffolded {base}\n  "+" ".join(SUB))
    return 0
def lst():
    if not os.path.isdir(ROOT): print("no projects"); return 0
    for p in sorted(os.listdir(ROOT)):
        b=os.path.join(ROOT,p)
        if os.path.isdir(b): print(f"  {p}")
    return 0
def status(slug):
    b=os.path.join(ROOT,slug)
    if not os.path.isdir(b): print("no such project"); return 1
    def n(d): dd=os.path.join(b,d); return len([f for f in os.listdir(dd) if f!=".gitkeep"]) if os.path.isdir(dd) else 0
    print(f"{slug}: generations={n('04_generations')} quarantine={n('05_vision_quarantine')} approved={n('06_approved')} rejected={n('07_rejected')} exports={n('09_exports')}")
    return 0
if __name__=="__main__":
    c=sys.argv[1] if len(sys.argv)>1 else "list"
    if c=="new": sys.exit(new(sys.argv[2]))
    if c=="status": sys.exit(status(sys.argv[2]))
    sys.exit(lst())
