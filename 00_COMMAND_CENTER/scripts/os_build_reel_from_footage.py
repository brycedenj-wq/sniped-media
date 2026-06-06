#!/usr/bin/env python3
"""
os_build_reel_from_footage.py , footage folder -> selects -> shot classify -> edit plan ->
ffmpeg rough cut (16:9 + 9:16) -> auto-run the reference gate. The ffmpeg path is the proven
assembly spine; Premiere/AE (FCPXML handoff), Adobe (grade), Figma (title/end-card) are optional
finish routes emitted as a route plan. Pacing targets come from the format profile.

  os_build_reel_from_footage.py <footage_dir> [--type beauty_fashion] [--seconds 35] [--out DIR] [--hero NAME]

No posting/delivery/hosting. Build + gate only. Doctrine: COMMERCIAL_CRAFT_BENCHMARK_V2.md
"""
import sys, os, re, json, glob, subprocess, argparse
HERE=os.path.dirname(os.path.abspath(__file__))
PROFILE_ASL={"comedy":2.2,"product_spot":2.5,"beauty_fashion":2.6,"luxury_manifesto":5.0,
             "social_teaser":1.4,"bts_personality":4.0,"tutorial":7.0,"commercial":3.0}
def run(c): return subprocess.run(c,capture_output=True,text=True)
def probe(f):
    r=run(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height",
           "-show_entries","format=duration","-of","json",f])
    try: d=json.loads(r.stdout); st=(d.get("streams") or [{}])[0]; fm=d.get("format") or {}
    except: return None
    w,h=st.get("width",0),st.get("height",0)
    a=run(["ffprobe","-v","error","-select_streams","a","-show_entries","stream=codec_type","-of","csv=p=0",f])
    return {"file":f,"w":w,"h":h,"dur":round(float(fm.get("duration") or 0),2),
            "orient":"vertical" if h>w else "horizontal","audio":bool(a.stdout.strip())}
def classify(c):
    d=c["dur"]
    return ("insert" if d<1.5 else "hero" if d>=5 else "medium")
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("footage_dir"); ap.add_argument("--type",default="beauty_fashion")
    ap.add_argument("--seconds",type=int,default=35); ap.add_argument("--out",default=None); ap.add_argument("--hero",default=None)
    a=ap.parse_args()
    if not os.path.isdir(a.footage_dir): print("footage dir not found"); sys.exit(2)
    out=a.out or os.path.join(a.footage_dir,"_reel_build"); os.makedirs(out,exist_ok=True)
    files=[f for f in glob.glob(os.path.join(a.footage_dir,"*")) if f.lower().endswith((".mp4",".mov",".m4v",".mkv"))]
    clips=[c for c in (probe(f) for f in files) if c]
    if not clips: print("no video clips found"); sys.exit(1)
    # selects: drop <1.0s; rank by duration
    selects=sorted([c for c in clips if c["dur"]>=1.0], key=lambda c:-c["dur"])
    for c in selects: c["shot"]=classify(c)
    asl=PROFILE_ASL.get(a.type,3.0)
    # hero = named, else longest
    hero=next((c for c in selects if a.hero and a.hero.lower() in os.path.basename(c["file"]).lower()), None) or (selects[0] if selects else None)
    inserts=[c for c in selects if c is not hero]
    # edit plan: hook (a short punchy insert) -> inserts trimmed ~asl -> hero held (~2.6x asl) -> end
    plan=[]; t=0.0
    hook=min(inserts, key=lambda c:c["dur"]) if inserts else hero
    def beat(c,dur,role):
        nonlocal t; dur=min(dur,c["dur"]); plan.append({"file":os.path.basename(c["file"]),"src":c["file"],"in":0.0,"out":round(dur,2),"role":role,"t":round(t,2)}); t+=dur
    beat(hook, min(asl*0.7, hook["dur"]), "hook")
    for c in inserts:
        if c is hook: continue
        if t>=a.seconds-asl*2.6: break
        beat(c, asl, "insert")
    if hero: beat(hero, asl*2.6, "hero_hold(payoff)")
    json.dump({"type":a.type,"target_s":a.seconds,"asl_target":asl,"plan":plan},open(os.path.join(out,"edit_plan.json"),"w"),indent=2)
    with open(os.path.join(out,"reel_EDL.csv"),"w") as f:
        f.write("t,role,in,out,file\n")
        for b in plan: f.write(f"{b['t']},{b['role']},{b['in']},{b['out']},{b['file']}\n")
    # assemble 16:9 rough cut via ffmpeg
    seg=[]; enc=["-c:v","libx264","-preset","medium","-pix_fmt","yuv420p","-r","30","-c:a","aac","-ar","44100","-ac","2","-shortest"]
    for i,b in enumerate(plan):
        s=os.path.join(out,f"seg_{i:02d}.mp4"); dur=b["out"]-b["in"]
        run(["ffmpeg","-y","-loglevel","error","-ss",str(b["in"]),"-t",str(dur),"-i",b["src"],
             "-f","lavfi","-t",str(dur),"-i","anullsrc=channel_layout=stereo:sample_rate=44100",
             "-vf","scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,format=yuv420p",
             "-map","0:v","-map","1:a"]+enc+[s]); seg.append(s)
    lst=os.path.join(out,"list.txt"); open(lst,"w").write("".join(f"file '{os.path.basename(s)}'\n" for s in seg))
    r169=os.path.join(out,"reel_16x9.mp4")
    run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy",r169])
    r916=os.path.join(out,"reel_9x16.mp4")
    run(["ffmpeg","-y","-loglevel","error","-i",r169,"-vf","scale=-2:1920,crop=1080:1920,format=yuv420p"]+enc[:-1]+[r916])
    # route plan
    route=("ROUTE: ffmpeg = assembly spine (done). Optional finish: Premiere/AE via FCPXML handoff (AME render blocked -> ffmpeg export); "
           "Adobe = grade pass (os_adobe_grade); Figma = title/end-card lockup; ElevenLabs = VO/SFX; music per SOUND_MUSIC_BRIEF.")
    open(os.path.join(out,"ROUTE.txt"),"w").write(route)
    print(f"REEL BUILT [{a.type}] -> {out}")
    print(f"  selects {len(selects)} | hero={os.path.basename(hero['file']) if hero else None} | beats {len(plan)} | 16x9 + 9x16")
    print(f"  {route}")
    print("\n=== GATE ===")
    g=run([sys.executable,os.path.join(HERE,"os_reference_gate.py"),"check",r169,"--type",a.type])
    print(g.stdout or g.stderr)
if __name__=="__main__": main()
