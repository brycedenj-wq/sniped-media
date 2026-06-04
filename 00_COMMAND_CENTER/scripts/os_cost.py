#!/usr/bin/env python3
"""os-cost: per-run cost ledger. Credits are NOT dollars.
  rate [usd_per_credit]                 set or show the conversion rate (USD UNKNOWN until set)
  log <run_id> <project> <model> <credits_est> <credits_actual> [usd_est] [usd_actual]
  project <project>                     rollup credits + USD (USD from rate if not explicit, else UNKNOWN)
  report"""
import sys, os, csv, time
CC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED=os.path.join(CC,"OS_PRODUCTION_COST.csv"); RATE=os.path.join(CC,".prod_cost_rate")
COLS=["ts","run_id","project","model_tool","credits_est","credits_actual","usd_est","usd_actual"]
def rows(): return list(csv.DictReader(open(LED))) if os.path.exists(LED) else []
def write(rs):
    with open(LED,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=COLS); w.writeheader(); [w.writerow(r) for r in rs]
def get_rate():
    return float(open(RATE).read().strip()) if os.path.exists(RATE) else None
def main():
    c=sys.argv[1] if len(sys.argv)>1 else "report"
    if c=="rate":
        sub=sys.argv[2] if len(sys.argv)>2 else "show"
        if sub=="set":
            val=None
            if "--usd-per-credit" in sys.argv: val=sys.argv[sys.argv.index("--usd-per-credit")+1]
            elif len(sys.argv)>3: val=sys.argv[3]
            if not val: print("usage: os_cost.py rate set --usd-per-credit <X>"); return 1
            open(RATE,"w").write(val); print(f"rate set: ${val}/credit"); return 0
        if sub=="show" or sub=="":
            r=get_rate(); print(f"rate: {'$'+str(r)+'/credit' if r else 'UNKNOWN (set with: os_cost.py rate set --usd-per-credit <X>)'}"); return 0
        # backward-compat: bare number
        try: float(sub); open(RATE,"w").write(sub); print(f"rate set: ${sub}/credit"); return 0
        except: print("usage: os_cost.py rate set --usd-per-credit <X> | rate show"); return 1
    if c=="log":
        rid,proj,model,ce,ca=sys.argv[2:7]; ue=sys.argv[7] if len(sys.argv)>7 else ""; ua=sys.argv[8] if len(sys.argv)>8 else ""
        r=get_rate()
        if not ue and r and ce: ue=f"{float(ce)*r:.4f}"
        if not ua and r and ca: ua=f"{float(ca)*r:.4f}"
        rs=rows(); rs.append({"ts":time.strftime("%Y-%m-%d %H:%M"),"run_id":rid,"project":proj,"model_tool":model,
                              "credits_est":ce,"credits_actual":ca,"usd_est":ue or "UNKNOWN","usd_actual":ua or "UNKNOWN"})
        write(rs); print(f"logged {rid}: {ca}cr actual (usd_actual={ua or 'UNKNOWN'})"); return 0
    if c=="project":
        proj=sys.argv[2]; pr=[r for r in rows() if r["project"]==proj]
        cred=sum(float(r["credits_actual"] or 0) for r in pr)
        rate=get_rate()
        usd=[float(r["usd_actual"]) for r in pr if r["usd_actual"] not in ("","UNKNOWN")]
        if usd: total="$"+format(sum(usd),".2f")
        elif rate: total="$"+format(cred*rate,".2f")+" (est from rate)"
        else: total="UNKNOWN"
        print(f"{proj}: {cred:.0f} credits actual | USD={total} (runs={len(pr)})"); return 0
    for r in rows()[-10:]: print(f"  {r['run_id']} {r['project']} {r['credits_actual']}cr usd={r['usd_actual']}")
    return 0
if __name__=="__main__":
    if not os.path.exists(LED): write([])
    sys.exit(main())
