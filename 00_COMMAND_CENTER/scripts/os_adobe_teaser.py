#!/usr/bin/env python3
"""
os_adobe_teaser.py , still-based motion teaser/trailer from one high-res image + title cards.

No video generation. Ken Burns crop-moves (push / pan) on a 4K still, intercut with rendered title
cards, concatenated into a vertical teaser. Deterministic, logged.

  os_adobe_teaser.py build --src HERO --spec beats.json --out CLIP.mp4 [--w 1080] [--h 1920] [--fps 30] [--log LOG]

beats.json = list of beats:
  {"type":"title","kicker":"...","title":"...","subtitle":"...","bg":"ink","dur":2.5}
  {"type":"image","crop":[x0,y0,x1,y1],"move":"in|out|left|right","dur":3.0}   (crop in SOURCE px)
"""
import os, sys, json, argparse, subprocess, tempfile, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
def _layout():
    s = importlib.util.spec_from_file_location("os_adobe_layout", os.path.join(HERE, "os_adobe_layout.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def _asset():
    s = importlib.util.spec_from_file_location("os_adobe_asset", os.path.join(HERE, "os_adobe_asset.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def _kenburns(img, out, w, h, dur, fps, move):
    from PIL import Image
    # pre-scale the (already cropped) frame to a tall canvas matched to target aspect, then zoompan
    big_w, big_h = w*2, h*2
    im = Image.open(img).convert("RGB")
    # cover-fit to big canvas
    iw, ih = im.size; t = big_w/big_h
    if iw/ih > t: cw, ch = int(ih*t), ih
    else: cw, ch = iw, int(iw/t)
    x = (iw-cw)//2; y = (ih-ch)//2
    im.crop((x, y, x+cw, y+ch)).resize((big_w, big_h), Image.LANCZOS).save(out+".frame.png")
    n = max(2, int(dur*fps))
    if move == "in":   z = "min(zoom+0.0009,1.30)"; xe="iw/2-(iw/zoom/2)"; ye="ih/2-(ih/zoom/2)"
    elif move == "out":z = "if(eq(on,0),1.30,max(zoom-0.0009,1.0))"; xe="iw/2-(iw/zoom/2)"; ye="ih/2-(ih/zoom/2)"
    elif move == "left":z="1.18"; xe="(iw-iw/zoom)*(1-on/%d)"%n; ye="ih/2-(ih/zoom/2)"
    elif move == "right":z="1.18"; xe="(iw-iw/zoom)*(on/%d)"%n; ye="ih/2-(ih/zoom/2)"
    else: z="1.12"; xe="iw/2-(iw/zoom/2)"; ye="ih/2-(ih/zoom/2)"
    vf = (f"zoompan=z='{z}':x='{xe}':y='{ye}':d={n}:s={w}x{h}:fps={fps},"
          f"fade=t=in:st=0:d=0.4,fade=t=out:st={max(0,dur-0.4):.2f}:d=0.4,format=yuv420p")
    cmd = ["ffmpeg","-y","-loop","1","-i",out+".frame.png","-t",str(dur),"-r",str(fps),"-vf",vf,
           "-c:v","libx264","-pix_fmt","yuv420p",out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    os.remove(out+".frame.png")
    if r.returncode: raise SystemExit("ffmpeg kenburns failed:\n"+r.stderr[-700:])

def _titleclip(beat, out, w, h, fps):
    L = _layout()
    png = out+".card.png"
    L.titlecard(png, w, h, beat.get("kicker",""), beat.get("title",""), beat.get("subtitle",""), beat.get("bg","ink"))
    dur = beat.get("dur",2.5)
    vf = f"fade=t=in:st=0:d=0.4,fade=t=out:st={max(0,dur-0.4):.2f}:d=0.4,format=yuv420p"
    cmd = ["ffmpeg","-y","-loop","1","-i",png,"-t",str(dur),"-r",str(fps),"-vf",vf,
           "-c:v","libx264","-pix_fmt","yuv420p",out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    os.remove(png)
    if r.returncode: raise SystemExit("ffmpeg title failed:\n"+r.stderr[-700:])

def build(src, spec_path, out, w, h, fps, log=None):
    from PIL import Image
    beats = json.load(open(spec_path))
    src_im = Image.open(src).convert("RGB")
    with tempfile.TemporaryDirectory() as d:
        clips = []
        for i, b in enumerate(beats):
            cp = os.path.join(d, f"c{i:02d}.mp4")
            if b["type"] == "title":
                _titleclip(b, cp, w, h, fps)
            else:
                box = b.get("crop")
                frame = os.path.join(d, f"f{i:02d}.png")
                (src_im.crop(tuple(box)) if box else src_im).save(frame)
                _kenburns(frame, cp, w, h, b.get("dur",3.0), fps, b.get("move","in"))
            clips.append(cp)
        lst = os.path.join(d, "list.txt")
        with open(lst, "w") as f:
            for c in clips: f.write(f"file '{c}'\n")
        cmd = ["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c:v","libx264","-pix_fmt","yuv420p","-movflags","+faststart",out]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode: raise SystemExit("concat failed:\n"+r.stderr[-700:])
    if log: _asset().log_edit(log, "teaser", src, out, f"{w}x{h} {len(beats)} beats", "still-based teaser")
    return out

def main():
    ap = argparse.ArgumentParser(prog="os_adobe_teaser.py"); sub = ap.add_subparsers(dest="cmd")
    b = sub.add_parser("build"); b.add_argument("--src",required=True); b.add_argument("--spec",required=True); b.add_argument("--out",required=True)
    b.add_argument("--w",type=int,default=1080); b.add_argument("--h",type=int,default=1920); b.add_argument("--fps",type=int,default=30); b.add_argument("--log",default="")
    a = ap.parse_args()
    if a.cmd == "build":
        build(a.src, a.spec, a.out, a.w, a.h, a.fps, a.log or None)
        d = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",a.out],capture_output=True,text=True).stdout.strip()
        print(f"teaser -> {a.out}  ({d}s)"); return 0
    ap.print_help(); return 0

if __name__ == "__main__": sys.exit(main())
