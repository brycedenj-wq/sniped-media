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
    import statistics
    stdev=round(statistics.pstdev(sh),2) if len(sh)>1 else 0
    uniformity=round(stdev/asl,2) if asl else 0  # low (<0.4) = monotone/repetitive
    return {"dur":round(dur,1),"shots":len(sh),"asl":asl,"cpm":round(len(sh)/(dur/60),1) if dur else 0,
            "max_shot":max(sh) if sh else dur,"contrast":round((max(sh)/asl),1) if sh and asl else 1,
            "uniformity":uniformity,"durations":sh}
def has_audio(vid):
    r=run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=codec_type","-of","csv=p=0",vid])
    return bool(r.stdout.strip())
def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd")
    c=sub.add_parser("check"); c.add_argument("video"); c.add_argument("--ref"); c.add_argument("--type",default="commercial")
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
    # COMMERCIAL_CRAFT_BENCHMARK_V1 bands (ASL low,high) by content type
    BANDS={"commercial":(1.5,6.5),"comedy":(1.5,3.5),"story":(3.0,5.5),"cinematic":(3.0,6.5),"tutorial":(4.0,17.0)}
    if a.cmd=="check":
        if not os.path.exists(a.video): print("video not found"); sys.exit(2)
        m=analyze(a.video); lo,hi=BANDS.get(a.type,BANDS["commercial"]); aud=has_audio(a.video)
        V=[]  # named benchmark verdicts
        if m["asl"]>hi: V.append(f"TOO_SLOW: ASL {m['asl']}s > {hi}s {a.type} ceiling")
        if m["asl"]<lo: V.append(f"TOO_FAST: ASL {m['asl']}s < {lo}s (frenetic for {a.type})")
        if m["uniformity"]<0.4: V.append(f"TOO_REPETITIVE: shot lengths uniform (uniformity {m['uniformity']}, <0.4) , no rhythm")
        if m["contrast"]<2: V.append(f"NO_COMMERCIAL_PAYOFF(quant): no held hero beat (max/asl {m['contrast']}x <2) , confirm a product hold near the end")
        if m["cpm"]<6 and a.type!="tutorial": V.append(f"LOW_SHOT_VARIATION: {m['cpm']} cuts/min , likely too few shot types")
        if not aud: V.append("AUDIO_NOT_MOTIVATING_CUTS: no audio track , an edit must be cut to sound")
        MAN=["WEAK_TRANSITION_LOGIC , every cut motivated? (cut-on-action/match/J-L, not unmotivated dissolves)",
             "AUDIO_NOT_MOTIVATING_CUTS , do cuts land on beats + duck before payoff?" if aud else None,
             "NO_COMMERCIAL_PAYOFF , is the product the longest, cleanest beat near the end?",
             "COPY_VO_NOT_CARRYING , does the line/structure carry, or is it just pretty footage?"]
        MAN=[x for x in MAN if x]
        refband=""
        if a.ref:
            p=os.path.join(LIB,a.ref,"pacing.json")
            if os.path.exists(p):
                rb=json.load(open(p)); refband=f" | ref '{a.ref}' ASL {rb.get('avg_shot_len_s')}s ({rb.get('pacing_band')})"
        print(f"VIDEO: {os.path.basename(a.video)} [{a.type}]  dur {m['dur']}s | shots {m['shots']} | ASL {m['asl']}s | cuts/min {m['cpm']} | contrast {m['contrast']}x | uniformity {m['uniformity']} | audio {'yes' if aud else 'NO'}{refband}")
        print(f"\nBENCHMARK VERDICTS (auto): {V if V else 'no auto-fails'}")
        print(f"MANUAL CHECKS (confirm by eye/ear, card-backed):")
        for x in MAN: print(f"  [ ] {x}")
        print(f"\n{len(CK)} craft cards loaded. Full craft checklist:")
        for k,d in CHECK: print(f"  [ ] {k}: {d}")
        print(f"\nVERDICT: {'PASS (auto)' if not V else 'FAIL , '+str(len(V))+' benchmark issue(s) above'}. Benchmark: COMMERCIAL_CRAFT_BENCHMARK_V1.md. Auto checks structure; manual checks confirm craft + no-copy.")
        sys.exit(1 if V else 0)
        return
    ap.print_help()
if __name__=="__main__": main()
