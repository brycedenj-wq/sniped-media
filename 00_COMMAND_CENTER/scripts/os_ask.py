#!/usr/bin/env python3
"""
os_ask.py , the front door. Ask the OS a production/money/copy/sales problem in plain words; it returns the
operating answer in one shape: CARD + SOURCE DOC + LIBRARY ROUTE + GATE + NEXT ACTION.

This is what makes the Start Here docs OPERATING CODE instead of reference: the technique comes back
applied, sourced, routed to its library, tied to the gate it satisfies, with the next move.

  os_ask.py "poster feels template"
  os_ask.py "motion feels like a moving still" --n 2
"""
import sys, os, importlib.util, re
HERE=os.path.dirname(os.path.abspath(__file__))
def _imp(n):
    spec=importlib.util.spec_from_file_location(n, os.path.join(HERE,n+".py"))
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
LIB=_imp("os_library")
CARDS=LIB.CARDS

LIB_OF_FAM={fams[0]:lib for lib,fams in LIB.LIBRARIES.items()}
STOP=set("the a an to of in on for and or is it feels like need needs my our this that with not no".split())

def score(card,terms):
    hay=" ".join([card.get("problem",""),card.get("technique",""),card.get("symptom",""),
                  card.get("when_to_use",""),card.get("quality_failure_prevented","")]).lower()
    return sum(1 for w in terms if len(w)>2 and w in hay)

FAM_WORDS={"higgsfield":"HIGGSFIELD_OPERATOR_LIBRARY","adobe":"ADOBE_OPERATOR_LIBRARY","photoshop":"ADOBE_OPERATOR_LIBRARY",
 "lightroom":"ADOBE_OPERATOR_LIBRARY","premiere":"PREMIERE_EDITING_LIBRARY","after effects":"AFTER_EFFECTS_MOTION_LIBRARY",
 "figma":"FIGMA_DESIGN_SYSTEM_LIBRARY","blender":"BLENDER_PRODUCTION_LIBRARY","social":"SOCIAL_DISTRIBUTION_LIBRARY",
 "money":"MONEY_OFFER_LIBRARY","offer":"MONEY_OFFER_LIBRARY","copy":"COPYWRITING_LIBRARY","sales":"SALES_OUTREACH_LIBRARY","outreach":"SALES_OUTREACH_LIBRARY"}
SKIP_WORDS={"skip","skipped","underused","unused","missing","not used","credits not","was skipped","ignored","forgot"}

def ask(q,n=1):
    ql=q.lower()
    print(f"ASK: {q}")
    # tool-skip / underuse questions are COMPLIANCE questions: point at the library + the gate
    if any(s in ql for s in SKIP_WORDS):
        for w,lib in FAM_WORDS.items():
            if w in ql:
                cnt=len(LIB.cards_in(LIB.LIBRARIES[lib]))
                print(f"  COMPLIANCE: '{w}' under-used. That is the {lib} ({cnt} cards).")
                print(f"  LIBRARY  os_library.py show {lib}")
                print(f"  GATE     os_starthere_compliance_gate.py check <proof.json>  (will FAIL the run until {lib} is loaded AND >=1 of its cards is used)")
                print(f"  NEXT     load {lib}, apply its cards, list it in libraries_loaded, then re-run the gate")
                break
    terms=[w for w in re.sub(r"[^a-z0-9 ]"," ",ql).split() if w not in STOP]
    ranked=sorted(((score(c,terms),c) for c in CARDS), key=lambda x:-x[0])
    ranked=[(s,c) for s,c in ranked if s>0][:n]
    if not ranked:
        print("  no card matched. Queue an extraction from the relevant Start Here doc, or widen the query.")
        return 1
    for s,c in ranked:
        f=LIB.fam(c); lib=LIB_OF_FAM.get(f,"(multi: load by sub-tool)")
        steps=c.get("exact_steps") or c.get("steps","")
        gate=c.get("gate_it_fixes","none") or "none"
        nxt=c.get("example_command") or c.get("route_it_activates") or "apply the steps, then re-run the relevant gate"
        src=c.get("source_doc") or c.get("source","?")
        print(f"\n  CARD     [{c.get('id','?')}] {c.get('technique','?')}")
        print(f"  SOURCE   {src}  (seg: {c.get('source_segment','-')})")
        print(f"  LIBRARY  {lib}  (tool_family: {f}; app: {c.get('app') or c.get('tool','?')})")
        print(f"  GATE     {gate}")
        print(f"  STEPS    {steps[:400]}")
        if c.get("prompt_pattern"): print(f"  PROMPT   {c['prompt_pattern'][:240]}")
        print(f"  NEXT     {nxt}")
    return 0

if __name__=="__main__":
    args=[a for a in sys.argv[1:]]
    n=1
    if "--n" in args:
        i=args.index("--n"); n=int(args[i+1]); del args[i:i+2]
    if not args: print(__doc__); sys.exit(1)
    sys.exit(ask(" ".join(args),n))
