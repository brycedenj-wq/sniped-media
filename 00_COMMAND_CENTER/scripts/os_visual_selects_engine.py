#!/usr/bin/env python3
"""
os_visual_selects_engine.py - MODE B selects engine for VISUAL / non-dialogue footage
(fashion, commercial, music-driven). The visual equivalent of a transcript Story Cutter:
instead of reading spoken word, it watches the FRAMES.

Pipeline: dense timestamp-burned filmstrips -> human/AI marks action-peak + freeze per clip
-> selects CSV. This is the durable version of the Alma deep-watch method.

  os_visual_selects_engine.py strips <footage_dir> <out_dir> [--step 0.4]
      # one timestamp-burned filmstrip per clip (Canon auto-transpose), for dense watching
  os_visual_selects_engine.py fine <clip> <a> <b> <out.jpg> [--step 0.25]
      # fine strip of an action window (pin the exact peak/freeze)
  os_visual_selects_engine.py scaffold <footage_dir> <selects.csv>
      # write the MODE B selects CSV template (cols below) for every clip

CSV cols: filename, shot_category, best_start, action_peak, best_freeze, best_end,
          wrong_person, clean_product, bts, anatomy_warp, plate, verdict, note
Verdicts: HERO / PRIMARY / INSERT / ALT / MAYBE / REJECT.
Rule: do NOT call a clip MAYBE if it contains a mandatory moment - watch it first.
"""
import sys, os, subprocess, glob, csv

FONT = "/System/Library/Fonts/Helvetica.ttc"

def is_canon(name): return os.path.basename(name)[:4].upper().startswith("D94A") or name.upper().endswith(".MP4") and "D94A" in name.upper()

def dur(f):
    try: return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",f],capture_output=True,text=True).stdout.strip() or 0)
    except Exception: return 0.0

def clips(d):
    out=[]
    for ext in ("*.MP4","*.MOV","*.mp4","*.mov"): out+=glob.glob(os.path.join(d,ext))
    return sorted(set(out))

def strip(f, out, step=0.4):
    d=dur(f); n=max(1,int(d/step)); rot="transpose=2," if "D94A" in os.path.basename(f).upper() else ""
    tmp=f"/tmp/vse_{os.path.basename(f)}"; os.makedirs(tmp,exist_ok=True)
    os.system(f"rm -f {tmp}/*.jpg")
    t=0.0; k=0
    while t<d:
        o=f"{tmp}/{k:03d}.jpg"
        subprocess.run(["ffmpeg","-nostdin","-v","error","-ss",f"{t:.2f}","-i",f,"-frames:v","1","-vf",f"{rot}scale=160:-1","-y",o],capture_output=True)
        if os.path.exists(o):
            subprocess.run(["magick",o,"-gravity","South","-background","black","-splice","0x16","-font",FONT,"-fill","#7CFC00","-pointsize","14","-annotate","+0+0",f"{t:.1f}",o],capture_output=True)
        t+=step; k+=1
    subprocess.run(["montage"]+sorted(glob.glob(f"{tmp}/*.jpg"))+["-tile","8x","-geometry","+2+2","-background","gray15","-font",FONT,"-fill","white","-pointsize","16","-title",f"{os.path.basename(f)} {d:.1f}s @{step}s",out],capture_output=True)
    os.system(f"rm -rf {tmp}")
    return os.path.exists(out)

def cmd_strips(d, outd, step):
    os.makedirs(outd,exist_ok=True); cs=clips(d); ok=0
    for f in cs:
        o=os.path.join(outd, os.path.splitext(os.path.basename(f))[0]+".jpg")
        if strip(f,o,step): ok+=1
    print(f"MODE B strips: {ok}/{len(cs)} -> {outd}")

def cmd_scaffold(d, out):
    cols=["filename","shot_category","best_start","action_peak","best_freeze","best_end","wrong_person","clean_product","bts","anatomy_warp","plate","verdict","note"]
    w=csv.DictWriter(open(out,"w"),fieldnames=cols); w.writeheader()
    for f in clips(d):
        w.writerow({"filename":os.path.basename(f),"verdict":"MAYBE","note":f"unwatched - dur {dur(f):.1f}s; run strips + watch before verdict"})
    print(f"MODE B selects scaffold -> {out} ({len(clips(d))} clips, all MAYBE until watched)")

if __name__=="__main__":
    a=sys.argv[1:]
    step=0.4
    if "--step" in a: i=a.index("--step"); step=float(a[i+1]); del a[i:i+2]
    if not a: print(__doc__)
    elif a[0]=="strips" and len(a)>2: cmd_strips(a[1],a[2],step)
    elif a[0]=="fine" and len(a)>4:
        f,A,B,o=a[1],float(a[2]),float(a[3]),a[4]; # simple fine strip
        tmp="/tmp/vse_fine"; os.makedirs(tmp,exist_ok=True); os.system(f"rm -f {tmp}/*.jpg"); t=A;k=0
        rot="transpose=2," if "D94A" in os.path.basename(f).upper() else ""
        while t<=B:
            o2=f"{tmp}/{k:03d}.jpg"; subprocess.run(["ffmpeg","-nostdin","-v","error","-ss",f"{t:.2f}","-i",f,"-frames:v","1","-vf",f"{rot}scale=220:-1","-y",o2],capture_output=True)
            if os.path.exists(o2): subprocess.run(["magick",o2,"-gravity","South","-background","black","-splice","0x22","-font",FONT,"-fill","#7CFC00","-pointsize","18","-annotate","+0+1",f"{t:.2f}",o2],capture_output=True)
            t+=step; k+=1
        subprocess.run(["montage"]+sorted(glob.glob(f"{tmp}/*.jpg"))+["-tile","8x","-geometry","+2+2","-background","gray15","-title",f"{os.path.basename(f)} {A}-{B}s @{step}s",o],capture_output=True)
        print(f"fine strip -> {o}")
    elif a[0]=="scaffold" and len(a)>2: cmd_scaffold(a[1],a[2])
    else: print(__doc__)
