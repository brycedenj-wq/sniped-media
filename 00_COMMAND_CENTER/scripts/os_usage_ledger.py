#!/usr/bin/env python3
"""os-usage-ledger: learn cost over time. /usage cannot be read directly, so usage is logged manually.
Usage:
  os_usage_ledger.py start <label> <segments> <model_mix> <est_cost> <start_total_usd>
  os_usage_ledger.py end   <label> <end_total_usd> [tokens]
  os_usage_ledger.py predict <segments> <model_mix>   - estimate $ from history (cost/segment)
  os_usage_ledger.py report                            - accuracy of past estimates"""
import sys, os, csv, time
CC=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED=os.path.join(CC,"OS_COST_LEDGER.csv")
COLS=["ts","label","segments","model_mix","est_cost","start_usd","end_usd","actual_cost","tokens","est_error_pct"]
def rows():
    return list(csv.DictReader(open(LED))) if os.path.exists(LED) else []
def write(rs):
    with open(LED,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=COLS); w.writeheader()
        for r in rs: w.writerow(r)
def main():
    c=sys.argv[1] if len(sys.argv)>1 else "report"
    rs=rows()
    if c=="start":
        _,_,label,seg,mix,est,start=sys.argv[:7]
        rs.append({k:"" for k in COLS}|{"ts":time.strftime("%Y-%m-%d %H:%M"),"label":label,"segments":seg,"model_mix":mix,"est_cost":est,"start_usd":start})
        write(rs); print(f"logged start: {label} (est ${est}, start ${start})"); return 0
    if c=="end":
        label,end=sys.argv[2],sys.argv[3]; tok=sys.argv[4] if len(sys.argv)>4 else ""
        for r in reversed(rs):
            if r["label"]==label and not r["end_usd"]:
                r["end_usd"]=end; r["tokens"]=tok
                try:
                    actual=float(end)-float(r["start_usd"]); r["actual_cost"]=f"{actual:.2f}"
                    if float(r["est_cost"]): r["est_error_pct"]=f"{(actual-float(r['est_cost']))/float(r['est_cost'])*100:+.0f}"
                    print(f"end {label}: actual ${actual:.2f} vs est ${r['est_cost']} ({r['est_error_pct']}%)")
                except Exception as e: print("calc note:",e)
                break
        write(rs); return 0
    if c=="predict":
        seg=float(sys.argv[2]); mix=sys.argv[3]
        done=[r for r in rs if r["actual_cost"] and r["segments"]]
        same=[r for r in done if r["model_mix"]==mix] or done
        if not same: print("no history yet , cannot predict; default ~$0.06/segment (haiku-read tiered)"); return 0
        rate=sum(float(r["actual_cost"])/float(r["segments"]) for r in same)/len(same)
        print(f"predict: {int(seg)} segments x ${rate:.4f}/seg (n={len(same)}, mix~{mix}) = ${seg*rate:.2f}"); return 0
    if c=="parse":
        # paste /usage text via stdin or a file arg; extract the key fields
        import re as _re
        txt=open(sys.argv[2]).read() if len(sys.argv)>2 and os.path.exists(sys.argv[2]) else sys.stdin.read()
        def g(pat):
            m=_re.search(pat,txt,_re.I); return m.group(1) if m else ""
        total=g(r"total cost:?\s*\$?([\d,.]+)")
        sess=g(r"current session[\s\S]{0,40}?(\d+)%")
        reset=g(r"resets?\s+([0-9: ]+[ap]m[^\n(]*)")
        week=g(r"current week \(all models\)[\s\S]{0,40}?(\d+)%")
        son=g(r"sonnet only\)[\s\S]{0,40}?(\d+)%")
        mix=[]
        for mdl in ("haiku","opus","sonnet"):
            # anchor to the real 'claude-<model>-<ver>: ... ($X.XX)' line only
            mm=_re.search(r"claude-"+mdl+r"[-\w.]*:[^\n]*?\(\$([\d,.]+)\)",txt,_re.I)
            mix.append(mdl+":$"+mm.group(1) if mm else mdl+":UNCERTAIN")
        print("PARSED /usage:")
        print("  total_cost=$"+total+" | session="+sess+"% (resets "+reset.strip()+") | week_all="+week+"% | week_sonnet="+son+"%")
        print("  model_mix: "+", ".join(mix))
        print("  -> log a run: os_usage_ledger.py start <label> <segments> '"+("+".join(m.split(':')[0] for m in mix if "UNCERTAIN" not in m) or "haiku+sonnet")+"' <est> "+total)
        print("  -> then after the run: os_usage_ledger.py end <label> <new_total>")
        return 0
    # report
    done=[r for r in rs if r["est_error_pct"]]
    print(f"ledger: {len(rs)} runs, {len(done)} with actuals")
    for r in done[-10:]: print(f"  {r['label']}: est ${r['est_cost']} actual ${r['actual_cost']} ({r['est_error_pct']}%)")
    return 0
if __name__=="__main__":
    if not os.path.exists(LED): write([])
    sys.exit(main())
