#!/usr/bin/env python3
"""
os_reference_ingest.py , turn a reference video (YouTube/Vimeo/local file) into an OS reference package:
metadata, transcript/captions (or audio for STT fallback), keyframes, shot map, pacing map, and a
TEARDOWN scaffold the agent fills with visual-grammar / edit-rhythm / copy / sound notes -> craft cards.

  os_reference_ingest.py <url|file> [--id NAME] [--seconds N] [--res 360]

Deterministic parts run here (download, ffprobe, scene-cut detection, keyframes, pacing math, audio
extract). The QUALITATIVE read (viewing frames, STT, writing principle cards) is the agent's job ,
the script emits the scaffold + exact next actions. Internal study only; references are not re-posted.
Doctrine: OS_REFERENCE_INGESTION_STANDARD.md . Library: OS_COMMERCIAL_CRAFT_LIBRARY.md
"""
import sys, os, re, json, subprocess, argparse, shutil

ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
LIB=os.path.join(ROOT,"REFERENCE_LIBRARY")
INDEX=os.path.join(ROOT,"REFERENCE_LIBRARY_INDEX.md")

def run(cmd, **kw): return subprocess.run(cmd, capture_output=True, text=True, **kw)

def is_url(s): return s.startswith("http://") or s.startswith("https://")

def ytdlp(args):
    # alternate player clients bypass datacenter 403s on the default web client
    return run([sys.executable,"-m","yt_dlp","--no-warnings","--socket-timeout","30",
                "--extractor-args","youtube:player_client=android,web_safari,tv"]+args)

def download(url, outdir, seconds, res):
    base=os.path.join(outdir,"source")
    fmt=f"bestvideo[height<=?{res}]+bestaudio/best[height<=?{res}]/best"
    a=["-f",fmt,"--merge-output-format","mp4","-o",base+".%(ext)s",
       "--write-info-json","--write-auto-subs","--write-subs","--sub-langs","en.*","--convert-subs","srt"]
    if seconds: a+=["--download-sections",f"*0-{seconds}"]
    a+=[url]; r=ytdlp(a)
    vid=None
    for f in os.listdir(outdir):
        if f.startswith("source") and f.endswith((".mp4",".mkv",".webm")): vid=os.path.join(outdir,f)
    return vid, r.returncode, (r.stderr or "")[-600:]

def probe(vid):
    r=run(["ffprobe","-v","error","-select_streams","v:0","-show_entries",
           "stream=width,height,r_frame_rate,duration","-show_entries","format=duration,size",
           "-of","json",vid])
    try: d=json.loads(r.stdout)
    except: d={}
    st=(d.get("streams") or [{}])[0]; fm=d.get("format") or {}
    fr=st.get("r_frame_rate","0/1");
    try: fps=round(eval(fr)) if "/" in fr else float(fr)
    except: fps=0
    return {"width":st.get("width"),"height":st.get("height"),"fps":fps,
            "duration":float(fm.get("duration") or st.get("duration") or 0),
            "size_mb":round(int(fm.get("size",0))/1048576,1) if fm.get("size") else None}

def scene_cuts(vid, thresh=0.3):
    r=run(["ffmpeg","-i",vid,"-filter:v",f"select='gt(scene,{thresh})',showinfo","-f","null","-"])
    times=sorted(set(float(m) for m in re.findall(r"pts_time:([0-9.]+)", r.stderr)))
    return times

def build_shot_map(cuts, dur):
    bounds=[0.0]+[c for c in cuts if 0.0<c<dur]+[dur]
    bounds=sorted(set(round(b,2) for b in bounds))
    shots=[]
    for i in range(len(bounds)-1):
        s,e=bounds[i],bounds[i+1]
        if e-s>=0.15: shots.append((len(shots)+1,s,e,round(e-s,2)))
    return shots

def pacing(shots, dur):
    if not shots: return {"shot_count":0}
    ds=[d for _,_,_,d in shots]
    asl=round(sum(ds)/len(ds),2)
    band=("frenetic <1.5s" if asl<1.5 else "fast 1.5-3s" if asl<3 else "measured 3-6s" if asl<6 else "slow >6s")
    return {"shot_count":len(shots),"avg_shot_len_s":asl,"cuts_per_min":round(len(shots)/(dur/60),1) if dur else 0,
            "min_shot":min(ds),"max_shot":max(ds),"pacing_band":band}

def extract_frames(vid, shots, outdir, cap=24):
    fd=os.path.join(outdir,"frames"); os.makedirs(fd,exist_ok=True)
    step=max(1,len(shots)//cap) if shots else 1
    picked=shots[::step][:cap] if shots else []
    for n,s,e,d in picked:
        mid=round(s+d/2,2)
        run(["ffmpeg","-y","-ss",str(mid),"-i",vid,"-frames:v","1","-q:v","3",
             os.path.join(fd,f"shot_{n:03d}_{mid:0.1f}s.jpg")])
    return fd, len(picked)

def get_transcript(outdir):
    for f in os.listdir(outdir):
        if f.endswith(".srt"):
            raw=open(os.path.join(outdir,f),errors="ignore").read()
            lines=[l for l in raw.splitlines() if l.strip() and not l.strip().isdigit() and "-->" not in l]
            txt=" ".join(dict.fromkeys(lines))
            open(os.path.join(outdir,"transcript.txt"),"w").write(txt)
            return "captions", len(txt)
    return None, 0

def extract_audio(vid, outdir):
    out=os.path.join(outdir,"audio.mp3")
    run(["ffmpeg","-y","-i",vid,"-vn","-q:a","4",out]); return out if os.path.exists(out) else None

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("--id",default=None)
    ap.add_argument("--seconds",type=int,default=0); ap.add_argument("--res",default="360")
    a=ap.parse_args()
    rid=a.id or re.sub(r"[^a-zA-Z0-9]+","_",os.path.basename(a.input))[:40] or "ref"
    outdir=os.path.join(LIB,rid); os.makedirs(outdir,exist_ok=True)
    meta={"ref_id":rid,"input":a.input}
    if is_url(a.input):
        vid,rc,err=download(a.input,outdir,a.seconds,a.res)
        if not vid: print(f"DOWNLOAD FAILED rc={rc}\n{err}"); sys.exit(1)
        ij=[f for f in os.listdir(outdir) if f.endswith(".info.json")]
        if ij:
            info=json.load(open(os.path.join(outdir,ij[0])))
            meta.update({"title":info.get("title"),"channel":info.get("uploader"),
                         "duration_src":info.get("duration"),"url":info.get("webpage_url")})
    else:
        vid=os.path.join(outdir,"source"+os.path.splitext(a.input)[1]); shutil.copy(a.input,vid)
    pr=probe(vid); meta["probe"]=pr
    cuts=scene_cuts(vid); shots=build_shot_map(cuts,pr["duration"]); pc=pacing(shots,pr["duration"])
    # write shot map
    with open(os.path.join(outdir,"shot_map.csv"),"w") as f:
        f.write("shot,start_s,end_s,dur_s\n")
        for n,s,e,d in shots: f.write(f"{n},{s},{e},{d}\n")
    json.dump(pc,open(os.path.join(outdir,"pacing.json"),"w"),indent=2)
    fd,nframes=extract_frames(vid,shots,outdir)
    tkind,tlen=get_transcript(outdir); aud=extract_audio(vid,outdir)
    json.dump(meta,open(os.path.join(outdir,"metadata.json"),"w"),indent=2)
    # teardown scaffold
    td=os.path.join(outdir,"TEARDOWN.md")
    with open(td,"w") as f:
        f.write(f"# REFERENCE TEARDOWN , {meta.get('title',rid)}\n\n")
        f.write(f"> {meta.get('url',a.input)} | src {meta.get('duration_src','?')}s | analyzed {pr['duration']:.1f}s | {pr['width']}x{pr['height']} {pr['fps']}fps\n\n")
        f.write(f"## Computed (deterministic)\n- shots: {pc.get('shot_count')} | ASL: {pc.get('avg_shot_len_s')}s | cuts/min: {pc.get('cuts_per_min')} | band: {pc.get('pacing_band')}\n")
        f.write(f"- frames extracted: {nframes} (frames/) | transcript: {tkind or 'NONE -> run ElevenLabs STT on audio.mp3'} ({tlen} chars) | audio: {'audio.mp3' if aud else 'none'}\n\n")
        f.write("## Agent fills (view frames/ + read transcript, then write SPECIFIC moves, not vibes)\n")
        for h in ["Hook (first 3s move)","Visual grammar (shot types, framing, color/grade, type)",
                  "Edit rhythm (cut motivation, ASL changes, match cuts)","Copy / VO structure (beats, claim, CTA)",
                  "Sound design (music role, sync, silence, stinger)","Transitions (what motivates each)",
                  "Commercial believability (why it sells)","DO NOT COPY (what is brand-specific/legally theirs)"]:
            f.write(f"### {h}\n- \n\n")
        f.write("## -> Craft cards to extract (feed OS_COMMERCIAL_CRAFT_LIBRARY.md)\n- \n")
    # index append
    os.makedirs(LIB,exist_ok=True)
    head="" if os.path.exists(INDEX) else "# REFERENCE LIBRARY INDEX\n\n| ref_id | title | shots | ASL | band | path |\n|---|---|---|---|---|---|\n"
    with open(INDEX,"a") as f:
        if head: f.write(head)
        f.write(f"| {rid} | {meta.get('title',rid)[:48]} | {pc.get('shot_count')} | {pc.get('avg_shot_len_s')}s | {pc.get('pacing_band')} | REFERENCE_LIBRARY/{rid}/ |\n")
    print(f"INGESTED {rid}: {pc.get('shot_count')} shots, ASL {pc.get('avg_shot_len_s')}s, {nframes} frames, transcript={tkind}")
    print(f"  package: {outdir}")
    print(f"  NEXT: view frames/ + read transcript.txt -> fill TEARDOWN.md -> os_commercial_card.py add ...")

if __name__=="__main__": main()
