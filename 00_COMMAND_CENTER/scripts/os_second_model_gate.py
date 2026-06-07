#!/usr/bin/env python3
"""
os_second_model_gate.py - reconcile a second-model (Gemini) review against EVIDENCE.

The second model is a critic, NOT the source of truth. A Gemini note becomes a V5
action ONLY if Claude can back it with footage / brief / director-correction evidence.
This gate turns the raw review into a reconciliation scaffold and enforces that rule.

  os_second_model_gate.py reconcile <gemini_review.json> <out.md>
      # parse the Gemini JSON response, emit a reconciliation table:
      # CLAIM | GEMINI SAID | EVIDENCE (footage/brief/correction) | VERDICT accept/reject/partial | V5 ACTION
      # every row defaults to NEEDS-EVIDENCE until Claude fills it.

  os_second_model_gate.py checklist
      # the accept/reject rules for second-model notes
"""
import sys, json

RULES = [
 "Accept ONLY if a timestamped frame / EDL / brief / director-correction backs the note.",
 "Reject if Gemini contradicts verified footage (director-label-is-truth-until-disproven).",
 "Partial if the problem is real but Gemini's fix is wrong; keep problem, replace fix.",
 "Never let Gemini crown anything final or make a delivery call.",
 "A lower score from Gemini is a prompt to re-verify, not an automatic truth.",
]

def grab(resp):
    # resp may be a dict already, or a string containing a JSON object
    if isinstance(resp, dict): return resp
    s = resp.strip()
    a, b = s.find("{"), s.rfind("}")
    if a>=0 and b>a:
        try: return json.loads(s[a:b+1])
        except Exception: return None
    return None

def reconcile(injson, out):
    raw = open(injson).read()
    review = None
    try:
        wrap = json.loads(raw)
        review = grab(wrap.get("response", wrap))
    except Exception:
        review = grab(raw)
    L = ["# SECOND-MODEL RECONCILIATION (Gemini vs evidence)\n",
         "Rule: a Gemini note becomes a V5 action ONLY if footage/brief/correction backs it. "
         "Gemini is a critic, not source of truth.\n"]
    if not review:
        L.append("\n**Could not parse Gemini JSON. Inspect the raw .json by hand.**\n")
        open(out,"w").write("\n".join(L)); print(f"reconcile -> {out} (UNPARSED)"); return
    score = review.get("brutal_score_out_of_10","?")
    L.append(f"\n**Gemini brutal score: {score}/10**\n")
    L.append("\n| # | Gemini claim | Evidence (footage / brief / correction) | Verdict | V5 action |")
    L.append("| --- | --- | --- | --- | --- |")
    rows=[]
    def add(tag, txt): rows.append((tag, str(txt).replace("|","\\|")[:240]))
    for q in ("hook_reads","speaker_gag_clear","product_inserts_same_world","wrong_person_bts_plate_issue","commercial_grade_or_social_rough"):
        if q in review: add(q, json.dumps(review[q]) if isinstance(review[q],(dict,list)) else review[q])
    for item in review.get("cut_or_fix_list",[])[:30]:
        add("cut/fix", f"{item.get('t','')}: {item.get('problem','')} -> {item.get('fix','')}")
    for m in review.get("missed_best_moments",[])[:20]: add("missed", m)
    for r in review.get("what_claude_is_rationalizing",[])[:20]: add("settling?", r)
    for i,(tag,txt) in enumerate(rows,1):
        L.append(f"| {i} | **{tag}**: {txt} | _NEEDS-EVIDENCE_ | _pending_ | _pending_ |")
    L.append("\n## Gemini V5 edit plan (raw, to be evidence-checked)\n")
    for s in review.get("v5_edit_plan",[]): L.append(f"- [ ] {s}")
    L.append("\n## Tool routing (Gemini opinion, advisory)\n")
    tr = review.get("tool_routing",{})
    for k,v in (tr.items() if isinstance(tr,dict) else []): L.append(f"- **{k}**: {v}")
    L.append("\n## Accept/reject rules\n")
    for r in RULES: L.append(f"- {r}")
    open(out,"w").write("\n".join(L))
    print(f"reconcile -> {out} ({len(rows)} claims to evidence-check, Gemini score {score}/10)")

def checklist():
    print("SECOND-MODEL ACCEPT/REJECT RULES:")
    for r in RULES: print("  -",r)

if __name__=="__main__":
    a=sys.argv[1:]
    if not a: print(__doc__)
    elif a[0]=="reconcile" and len(a)>2: reconcile(a[1],a[2])
    elif a[0]=="checklist": checklist()
    else: print(__doc__)
