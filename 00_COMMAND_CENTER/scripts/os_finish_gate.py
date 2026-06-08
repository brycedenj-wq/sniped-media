#!/usr/bin/env python3
"""
os_finish_gate.py - the FINISHING excellence gate. PASS != excellent.
Scores a finished edit against 11 axes + the client-ready checklist.

  os_finish_gate.py score <video.mp4>        # ffprobe facts + the 11-axis scorecard template
  os_finish_gate.py checklist                # the client-ready checklist (all must be YES)
  os_finish_gate.py axes                     # the 11 excellence axes

A "PASS" on os_reference_gate.py only clears the craft floor. CLIENT-READY requires the checklist.
"""
import sys, subprocess, json

AXES = [
    "hook_clarity", "story_arc", "best_moment_usage", "product_visibility",
    "continuity", "transition_motivation", "premium_grade", "audio_sync",
    "plate_privacy_cleanup", "rewatch_value", "client_readiness",
]
CHECKLIST = [
    "plate blur done (unreadable, proof board exists)",
    "wrong people / BTS removed (no yellow shirt, red tracksuit, 2nd model)",
    "product inserts do not break the world (real/clean, no AI hands/anatomy)",
    "hook reads clearly within the first 1.5s",
    "audio synced + legal (licensed/synth, -14 LUFS)",
    "final review board exists",
    "revision/handoff package exists",
]

def ffprobe(v):
    def g(stream, ent):
        try:
            return subprocess.run(["ffprobe","-v","error","-select_streams",stream,"-show_entries",ent,"-of","default=nw=1:nk=1",v],
                                  capture_output=True,text=True).stdout.strip()
        except Exception: return "?"
    dur=g("v:0","format=duration"); w=g("v:0","stream=width"); h=g("v:0","stream=height")
    fps=g("v:0","stream=r_frame_rate"); acodec=g("a:0","stream=codec_name")
    return {"duration":dur,"resolution":f"{w}x{h}","fps":fps,"audio":acodec or "none"}

def cmd_score(v):
    f=ffprobe(v)
    print(f"FINISH GATE - {v}\n")
    print(f"  facts: {f['duration']}s | {f['resolution']} | {f['fps']} | audio={f['audio']}")
    vert = f["resolution"].endswith("1920") or f["resolution"].startswith("1080")
    print(f"  resolution check (9:16 1080x1920): {'OK' if f['resolution']=='1080x1920' else 'CHECK'}")
    print("\n  11-AXIS EXCELLENCE SCORECARD (score 0-3 each; >=2 to clear, 3 = excellent):")
    for a in AXES: print(f"    [ ] {a}")
    print("\n  RULE: os_reference_gate PASS = craft floor only. CLIENT-READY needs the checklist below.")
    cmd_checklist()

def cmd_checklist():
    print("\n  CLIENT-READY CHECKLIST (ALL must be YES):")
    for c in CHECKLIST: print(f"    [ ] {c}")
    print("\n  If any is NO -> NOT client-ready (regardless of a craft-gate PASS).")

def cmd_axes():
    print("FINISHING EXCELLENCE AXES (0-3):")
    for a in AXES: print(f"  - {a}")

if __name__=="__main__":
    a=sys.argv[1:]
    if not a: print(__doc__)
    elif a[0]=="score" and len(a)>1: cmd_score(a[1])
    elif a[0]=="checklist": cmd_checklist()
    elif a[0]=="axes": cmd_axes()
    else: print(__doc__)
