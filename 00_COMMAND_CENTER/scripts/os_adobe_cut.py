#!/usr/bin/env python3
"""
os_adobe_cut.py , motion finishing for later (clip in, ship-safe export out). ffmpeg wrapper, logged.

  os_adobe_cut.py run --src CLIP --out CLIP [--start 0] [--dur 4] [--mute] [--size 1080x1920]
                      [--caption-safe] [--fps 30] [--log LOG]
  os_adobe_cut.py probe --src CLIP

--caption-safe pads/letterboxes so the lower ~18% stays clear for burned-in captions, and reports
the safe-area box. --mute strips audio (default keep). Never mutates the source.
"""
import os, sys, json, argparse, subprocess, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
def _asset():
    spec = importlib.util.spec_from_file_location("os_adobe_asset", os.path.join(HERE, "os_adobe_asset.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def probe(src):
    out = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format",
                          "-show_streams", src], capture_output=True, text=True).stdout
    return json.loads(out) if out else {}

def run(src, out, start, dur, mute, size, caption_safe, fps, log_path=None):
    A = _asset(); A.guard_not_inplace(src, out)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    vf = []
    safe_box = None
    if size:
        w, h = [int(v) for v in size.lower().split("x")]
        if caption_safe:
            inner_h = int(h * 0.82)  # keep lower 18% clear
            vf.append(f"scale={w}:{inner_h}:force_original_aspect_ratio=decrease")
            vf.append(f"pad={w}:{h}:(ow-iw)/2:0:color=black")
            safe_box = {"x": 0, "y": int(h*0.82), "w": w, "h": int(h*0.18)}
        else:
            vf.append(f"scale={w}:{h}:force_original_aspect_ratio=decrease")
            vf.append(f"pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=black")
    cmd = ["ffmpeg", "-y"]
    if start: cmd += ["-ss", str(start)]
    cmd += ["-i", src]
    if dur: cmd += ["-t", str(dur)]
    if vf: cmd += ["-vf", ",".join(vf)]
    if fps: cmd += ["-r", str(fps)]
    if mute: cmd += ["-an"]
    cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"  ffmpeg failed:\n{r.stderr[-800:]}")
    params = f"start={start} dur={dur} mute={mute} size={size} caption_safe={caption_safe} fps={fps}"
    if log_path:
        A.log_edit(log_path, "cut", src, out, params,
                   (f"caption-safe box={safe_box}" if safe_box else "motion finish"))
    return out, safe_box

def main():
    ap = argparse.ArgumentParser(prog="os_adobe_cut.py")
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("run"); r.add_argument("--src", required=True); r.add_argument("--out", required=True)
    r.add_argument("--start", type=float, default=0); r.add_argument("--dur", type=float, default=0)
    r.add_argument("--mute", action="store_true"); r.add_argument("--size", default="")
    r.add_argument("--caption-safe", action="store_true"); r.add_argument("--fps", type=int, default=0)
    r.add_argument("--log", default="")
    p = sub.add_parser("probe"); p.add_argument("--src", required=True)
    a = ap.parse_args()
    if a.cmd == "run":
        if not os.path.exists(a.src): print(f"missing src: {a.src}"); return 1
        out, safe = run(a.src, a.out, a.start, a.dur, a.mute, a.size, a.caption_safe, a.fps, a.log or None)
        print(f"cut -> {out}" + (f"  safe-area={safe}" if safe else "")); return 0
    if a.cmd == "probe":
        d = probe(a.src)
        for s in d.get("streams", []):
            if s.get("codec_type") == "video":
                print(f"video {s.get('width')}x{s.get('height')} {s.get('r_frame_rate')} dur={d.get('format',{}).get('duration')}")
        return 0
    ap.print_help(); return 0

if __name__ == "__main__":
    sys.exit(main())
