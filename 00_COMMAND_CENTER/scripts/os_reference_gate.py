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
    sub.add_parser("cards"); sub.add_parser("checklist"); sub.add_parser("scorecard"); sub.add_parser("profiles")
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
    # COMMERCIAL_CRAFT_BENCHMARK_V2 , per-FORMAT profiles. Classify the format FIRST.
    # CORRECTION: slow is only a failure when unmotivated (low contrast), repetitive (low uniformity), or no payoff.
    PROFILES={
     "comedy":          {"asl":(1.3,3.5),"cpm_min":12,"contrast":1.8,"payoff":True,"audio":True,"note":"punchline ad: build to a beat, hard cuts on lines"},
     "product_spot":    {"asl":(1.5,4.0),"cpm_min":10,"contrast":2.2,"payoff":True,"audio":True,"note":"product is the longest clean hold; demo->proof->CTA"},
     "beauty_fashion":  {"asl":(1.0,4.5),"cpm_min":10,"contrast":2.0,"payoff":True,"audio":True,"note":"fast texture/detail inserts + a held hero; cut to the track"},
     "luxury_manifesto":{"asl":(3.5,9.0),"cpm_min":3,"contrast":2.2,"payoff":True,"audio":True,"note":"slow is FINE if motivated: needs contrast + a held payoff, not speed"},
     "social_teaser":   {"asl":(0.6,2.5),"cpm_min":16,"contrast":1.6,"payoff":True,"audio":True,"note":"hook in <1s, relentless, one payoff"},
     "bts_personality": {"asl":(2.0,8.0),"cpm_min":5,"contrast":1.4,"payoff":False,"audio":True,"note":"personality carries; looser pacing OK, still needs motion"},
     "tutorial":        {"asl":(4.0,18.0),"cpm_min":2,"contrast":1.2,"payoff":False,"audio":True,"note":"clarity > pace; b-roll over talking-head; no payoff requirement"},
     "commercial":      {"asl":(1.5,6.5),"cpm_min":8,"contrast":2.0,"payoff":True,"audio":True,"note":"generic fallback; classify more specifically when possible"},
    }
    SCORECARD12=["hook_strength","shot_variety","subject_continuity","audio_motivates_cuts","transition_logic",
                 "pacing_asl_by_type","visual_hierarchy","typography_captions","payoff","commercial_clarity",
                 "rewatch_value","premium_feel"]
    if a.cmd=="profiles":
        for t,p in PROFILES.items(): print(f"{t:17} ASL {p['asl'][0]}-{p['asl'][1]}s | cpm>={p['cpm_min']} | contrast>={p['contrast']} | payoff={p['payoff']} | {p['note']}")
        return
    if a.cmd=="scorecard":
        print("EDIT SCORECARD (0 absent / 1 weak / 2 strong / 3 undeniable):")
        for s in SCORECARD12: print(f"  ___/3  {s}")
        print("  ELITE >= 30/36 and no axis at 0-1. Pacing/variety/audio axes are auto-filled by `check`.")
        return
    if a.cmd=="check":
        if not os.path.exists(a.video): print("video not found"); sys.exit(2)
        m=analyze(a.video); P=PROFILES.get(a.type,PROFILES["commercial"]); lo,hi=P["asl"]; aud=has_audio(a.video)
        slow=m["asl"]>hi; fast=m["asl"]<lo; repetitive=m["uniformity"]<0.4; weak_payoff=m["contrast"]<P["contrast"]
        V=[]; notes=[]
        if slow and (repetitive or weak_payoff):
            V.append(f"TOO_SLOW: ASL {m['asl']}s > {hi}s for {a.type} AND {'repetitive holds' if repetitive else 'no held payoff (low contrast)'}")
        elif slow:
            notes.append(f"slow ASL {m['asl']}s (>{hi}s) but MOTIVATED (contrast {m['contrast']}x, varied) , ACCEPTED for {a.type}")
        if fast: V.append(f"TOO_FAST: ASL {m['asl']}s < {lo}s , frenetic for {a.type}")
        if repetitive: V.append(f"TOO_REPETITIVE: uniform shot lengths (uniformity {m['uniformity']} <0.4) , no rhythm")
        if P["payoff"] and weak_payoff: V.append(f"NO_PAYOFF: no held hero beat (contrast {m['contrast']}x < {P['contrast']}) , give the hero the longest clean hold")
        if m["cpm"]<P["cpm_min"]: V.append(f"LOW_SHOT_VARIATION: {m['cpm']} cuts/min < {P['cpm_min']} expected for {a.type}")
        if P["audio"] and not aud: V.append("AUDIO_NOT_MOTIVATING_CUTS: no audio track , an edit must be cut to sound")
        MAN=["WEAK_TRANSITION_LOGIC , every cut motivated (cut-on-action/match/J-L), not unmotivated dissolves?",
             ("AUDIO_NOT_MOTIVATING_CUTS , cuts land on beats + duck before payoff?" if aud else None),
             ("NO_PAYOFF , is the hero/subject the longest cleanest beat near the end?" if P["payoff"] else None),
             "SUBJECT_CONTINUITY , same subject/world/grade across shots?",
             "VISUAL_HIERARCHY , does the eye land where intended each shot?",
             "COPY_VO_NOT_CARRYING , does the line/structure carry, not just pretty footage?"]
        MAN=[x for x in MAN if x]
        refband=""
        if a.ref:
            pth=os.path.join(LIB,a.ref,"pacing.json")
            if os.path.exists(pth):
                rb=json.load(open(pth)); refband=f" | ref '{a.ref}' ASL {rb.get('avg_shot_len_s')}s"
        print(f"VIDEO: {os.path.basename(a.video)} [{a.type}] {P['note']}")
        print(f"  dur {m['dur']}s | shots {m['shots']} | ASL {m['asl']}s (band {lo}-{hi}) | cuts/min {m['cpm']} | contrast {m['contrast']}x | uniformity {m['uniformity']} | audio {'yes' if aud else 'NO'}{refband}")
        if notes: print("  NOTES: "+"; ".join(notes))
        print(f"\nBENCHMARK VERDICTS (auto, format-aware): {V if V else 'no auto-fails'}")
        print("MANUAL CHECKS (card-backed, confirm by eye/ear):")
        for x in MAN: print(f"  [ ] {x}")
        print(f"\nEDIT SCORECARD (score 0-3): {', '.join(SCORECARD12)}  (run `scorecard`)")
        print(f"\nVERDICT: {'PASS (auto)' if not V else 'FAIL , '+str(len(V))+' issue(s)'} for format '{a.type}'. Benchmark: COMMERCIAL_CRAFT_BENCHMARK_V2.md. Classify format FIRST; slow only fails when unmotivated/repetitive/no-payoff.")
        sys.exit(1 if V else 0)
        return
    ap.print_help()
if __name__=="__main__": main()
