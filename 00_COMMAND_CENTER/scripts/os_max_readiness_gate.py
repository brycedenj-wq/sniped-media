#!/usr/bin/env python3
"""
os_max_readiness_gate.py , the umbrella gate. Nothing is MAX / ELITE / COMPLETE / READY unless ALL hold:
  1. current state loaded (fresh OS_BOOT_REPORT.md)
  2. project libraries loaded (Start Here compliance)
  3. relevant tools checked (tool reality)
  4. underused tools logged
  5. cards used
  6. gates passed
  7. artifacts exist
  8. blocked tools have handoff routes
  9. stale assumptions checked

Run os_current_state_boot.py first, then fill a proof.json (extends the compliance proof):
  + "current_state_loaded": true        (or the gate re-runs boot)
  + "tools_checked": true
  + "stale_checked": true
  + "claim": "the MAX/ELITE claim being made"   (auto-run through the stale gate)

  os_max_readiness_gate.py check <proof.json>
  os_max_readiness_gate.py template <project_type>
"""
import os, sys, json, subprocess, datetime
HERE=os.path.dirname(os.path.abspath(__file__)); CMD=os.path.dirname(HERE)
def runrc(cmd):
    p=subprocess.run(cmd,cwd=HERE,capture_output=True,text=True,timeout=60)
    return p.returncode,p.stdout+p.stderr

def fresh_boot(max_age_h=24):
    rep=os.path.join(CMD,"OS_BOOT_REPORT.md")
    if not os.path.exists(rep): return False,"OS_BOOT_REPORT.md missing , run os_current_state_boot.py"
    age=(datetime.datetime.now()-datetime.datetime.fromtimestamp(os.path.getmtime(rep))).total_seconds()/3600
    if age>max_age_h: return False,f"OS_BOOT_REPORT.md stale ({age:.0f}h old) , re-run os_current_state_boot.py"
    return True,f"boot report fresh ({age:.1f}h)"

def check(proof_path):
    P=json.load(open(proof_path))
    fails=[]; oks=[]
    print("MAX READINESS GATE\n")

    # 1. current state loaded
    if P.get("current_state_loaded"):
        ok,msg=fresh_boot()
        (oks if ok else fails).append(f"current_state_loaded: {msg}")
    else:
        ok,msg=fresh_boot()
        if ok: oks.append(f"current_state_loaded (auto): {msg}")
        else: fails.append(f"current_state NOT loaded: {msg}")

    # 2-8. Start Here compliance (libraries/cards/artifacts/blocked-handoff)
    rc,out=runrc(["python3","os_starthere_compliance_gate.py","check",proof_path])
    print(out.strip()); print()
    (oks if rc==0 else fails).append(f"start_here_compliance: {'PASS' if rc==0 else 'FAIL (see above)'}")

    # 3. tools checked
    (oks if P.get("tools_checked") else fails).append(f"tools_checked: {'yes' if P.get('tools_checked') else 'NO , run os_tool_reality_check.py project <type>'}")

    # 9. stale assumptions checked
    claim=P.get("claim","")
    if P.get("stale_checked") or claim:
        if claim:
            rc2,out2=runrc(["python3","os_stale_assumption_gate.py","check",claim])
            if rc2==1 and "BLOCKED" in out2:
                fails.append(f"stale_assumption: BLOCKED , the claim matches a corrected stale assumption:\n{out2.strip()}")
            else:
                oks.append("stale_assumption: claim clear of corrected stale assumptions")
        else:
            oks.append("stale_checked: asserted")
    else:
        fails.append("stale_assumptions NOT checked: set stale_checked or provide claim")

    verdict="READY" if not fails else "NOT READY"
    print("="*60)
    print(f"MAX READINESS VERDICT: {verdict}")
    print("PASSED:")
    for o in oks: print(f"  + {o}")
    if fails:
        print("BLOCKERS (cannot call this MAX/ELITE/COMPLETE/READY):")
        for f in fails: print(f"  X {f}")
    return 0 if verdict=="READY" else 1

def template(pt):
    rc,out=runrc(["python3","os_starthere_compliance_gate.py","template",pt])
    try: base=json.loads(out)
    except: print(out); return 1
    base.update({"current_state_loaded":True,"tools_checked":True,"stale_checked":True,
                 "claim":"<the MAX/ELITE/READY claim, e.g. 'AXIS video_campaign is MAX'>"})
    print(json.dumps(base,indent=2)); return 0

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)>=2 and a[0]=="check": sys.exit(check(a[1]))
    if len(a)>=2 and a[0]=="template": sys.exit(template(a[1]))
    print(__doc__); sys.exit(1)
