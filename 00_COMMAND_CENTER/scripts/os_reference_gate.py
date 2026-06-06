#!/usr/bin/env python3
"""
os_reference_gate.py , check a built edit/campaign video against the COMMERCIAL_CRAFT cards.
Quantitative checks computed from the video (shot count, ASL, pacing contrast, variety); qualitative
checks printed as a card-backed checklist (the gate CALLS the craft cards). Reference-compliance,
not copying.

  os_reference_gate.py check <video.mp4> [--ref <ref_id>]   # analyze + score
  os_reference_gate.py cards                                 # list loaded craft cards
  os_reference_gate.py checklist                             # the 9-point craft checklist
Doctrine: OS_REFERENCE_INGESTION_STANDARD.md . Cards: OS_COMMERCIAL_CRAFT_CARDS.json
"""
import sys, os, re, json, subprocess, argparse
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(HERE,"..")
CARDS=os.path.join(ROOT,"OS_COMMERCIAL_CRAFT_CARDS.json")
LIB=os.path.join(ROOT,"REFERENCE_LIBRARY")
def cards(): return json.load(open(CARDS)) if os.path.exists(CARDS) else []
def run(c): return subprocess.run(c,capture_output=True,text=True)
def analyze(vid):
    pr=run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",vid])
    dur=float(pr.stdout.strip() or 0)
    r=run(["ffmpeg","-i",vid,"-filter:v","select='gt(scene,0.3)',showinfo","-f","null","-"])
    cuts=sorted(set(float(m) for m in re.findall(r"pts_time:([0-9.]+)",r.stderr) if 0<float(m)<dur))
    b=[0.0]+cuts+[dur]; b=sorted(set(round(x,2) for x in b))
    sh=[round(b[i+1]-b[i],2) for i in range(len(b)-1) if b[i+1]-b[i]>=0.15]
    asl=round(sum(sh)/len(sh),2) if sh else dur
    return {"dur":round(dur,1),"shots":len(sh),"asl":asl,"cpm":round(len(sh)/(dur/60),1) if dur else 0,
            "max_shot":max(sh) if sh else dur,"contrast":round((max(sh)/asl),1) if sh and asl else 1}
def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd")
    c=sub.add_parser("check"); c.add_argument("video"); c.add_argument("--ref")
    sub.add_parser("cards"); sub.add_parser("checklist")
    a=ap.parse_args(); CK=cards()
    if a.cmd=="cards":
        for x in CK: print(f"{x['id']:34} [{x.get('lane','')}] -> {x.get('gate_influenced','')}")
        return
    CHECK=[("hook","first 1-2s earns attention (cc_earn_attention_spectacle_open / cc_anything_but_itself)"),
           ("pacing","ASL in band + product is the longest hold (cc_pacing_contrast_band)"),
           ("transition_motivation","every cut motivated; freeze->product-pause rhythm (cc_freeze_then_product_pause)"),
           ("audio_sync","cuts land on beats; duck before payoff (cc_sound_led_cut)"),
           ("typography","one owned-type title beat, sparse (cc_branded_title_beat)"),
           ("color_grade","consistent grade, on-palette, no auto-WB drift"),
           ("shot_variety","wide/medium/insert/aggressive-angle present (cc_aggressive_angle_is_the_cover)"),
           ("commercial_believability","reads like a real spot a brand would run"),
           ("reference_compliance","principles applied, NOT a reference copied (see each card do_not_copy)")]
    if a.cmd=="checklist":
        for k,d in CHECK: print(f"[ ] {k}: {d}")
        return
    if a.cmd=="check":
        if not os.path.exists(a.video): print("video not found"); sys.exit(2)
        m=analyze(a.video); flags=[]
        if not(1.2<=m["asl"]<=6.5): flags.append(f"pacing: ASL {m['asl']}s outside 1.2-6.5s band")
        if m["contrast"]<2: flags.append(f"pacing: weak contrast (max/asl={m['contrast']}x); product hold not standing out")
        if m["shots"]<4: flags.append(f"shot_variety: only {m['shots']} shots detected; likely too static")
        refband=""
        if a.ref:
            p=os.path.join(LIB,a.ref,"pacing.json")
            if os.path.exists(p):
                rb=json.load(open(p)); refband=f" | ref '{a.ref}' band {rb.get('pacing_band')} ASL {rb.get('avg_shot_len_s')}s"
        print(f"VIDEO: {os.path.basename(a.video)}  dur {m['dur']}s | shots {m['shots']} | ASL {m['asl']}s | cuts/min {m['cpm']} | contrast {m['contrast']}x{refband}")
        print(f"QUANT FLAGS: {flags if flags else 'none'}")
        print(f"\nCARD-BACKED CHECKLIST ({len(CK)} craft cards loaded) , confirm each by eye/ear:")
        for k,d in CHECK: print(f"  [ ] {k}: {d}")
        verdict="PASS (quant)" if not flags else "REVIEW , quant flags above + run checklist"
        print(f"\nVERDICT: {verdict}. Reference-compliance is human-confirmed against the cards; this gate scores structure + prompts the craft checks.")
        return
    ap.print_help()
if __name__=="__main__": main()
