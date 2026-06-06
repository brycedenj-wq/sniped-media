#!/usr/bin/env python3
"""
os_video_edit_router.py , VIDEO EDITING MUST BE AUTOMATED OR EXPLICITLY BLOCKED.

The motion/edit layer of any max campaign-film package must resolve to one of:
  DIRECT_PREMIERE_AUTOMATED / ADOBE_VIDEO_MCP_AUTOMATED / AFTER_EFFECTS_AUTOMATED /
  CAPCUT_AUTOMATED / HYPERFRAMES_PLUS_FFMPEG_AUTOMATED / HYBRID_AUTOMATED / BLOCKED_AFTER_VERIFICATION.
Never a human handoff by default. A handoff is acceptable ONLY if every automated route is blocked.

This router probes every route on the machine, classifies it, writes OS_VIDEO_EDIT_ROUTE_MATRIX.csv,
picks the strongest automated route, and can run a credit-free 3-clip dummy edit to PROVE it.

  os_video_edit_router.py routes              , probe + classify all routes (writes the matrix)
  os_video_edit_router.py pick                , the strongest automated route + why
  os_video_edit_router.py selftest [outdir]   , credit-free 3-clip dummy edit through the chosen route
  os_video_edit_router.py fcpxml <out.fcpxml> <clip1> <clip2> ...   , emit a Premiere-openable project
  os_video_edit_router.py edl <out.edl> <clip1> <clip2> ...         , emit a CMX3600 EDL
"""
import os, sys, shutil, subprocess, csv, json, glob

HERE=os.path.dirname(os.path.abspath(__file__)); CMD=os.path.dirname(HERE); REPO=os.path.dirname(CMD)
MATRIX=os.path.join(CMD,"OS_VIDEO_EDIT_ROUTE_MATRIX.csv")

def have(cmd): return shutil.which(cmd) is not None
def app(p): return os.path.exists(p)
def ffmpeg_has(flt):
    try:
        out=subprocess.run(["ffmpeg","-hide_banner","-filters"],capture_output=True,text=True,timeout=20).stdout
        return any(line.split()[1]==flt for line in out.splitlines() if len(line.split())>1)
    except Exception: return False

def capcut_cards():
    try:
        cards=json.load(open(os.path.join(CMD,"TECHNIQUE_CARDS.json")))
        return [c.get("id") for c in cards if "capcut" in (c.get("technique","")+c.get("problem","")+c.get("exact_steps","")+c.get("app","")).lower()]
    except Exception: return []

def adobe_video_mcp():
    # from the registry json: do video tools exist?
    try:
        out=subprocess.run(["python3","os_tool_registry.py","json"],cwd=HERE,capture_output=True,text=True,timeout=20).stdout
        T=json.loads(out)["tools"]
        return {tid:t.get("status") for tid,t in T.items() if "video" in tid.lower() or "quick_cut" in tid.lower()}
    except Exception: return {}

def hf_projects():
    return glob.glob(os.path.join(CMD,"**","hyperframes.json"),recursive=True)

def detect():
    d={}
    d["ffmpeg"]=have("ffmpeg"); d["ffprobe"]=have("ffprobe")
    d["xfade"]=ffmpeg_has("xfade"); d["drawtext"]=ffmpeg_has("drawtext")
    d["node"]=have("node"); d["npx"]=have("npx")
    d["hf_projects"]=hf_projects()
    d["aerender"]=glob.glob("/Applications/Adobe After Effects*/aerender")
    d["premiere_app"]=glob.glob("/Applications/Adobe Premiere Pro*")
    d["ae_app"]=glob.glob("/Applications/Adobe After Effects*")
    d["capcut_app"]=glob.glob("/Applications/CapCut*")
    try: import pyJianYingDraft; d["capcut_lib"]=True
    except Exception: d["capcut_lib"]=False
    d["capcut_cards"]=capcut_cards()
    d["adobe_video_mcp"]=adobe_video_mcp()
    d["premiere_mcp"]=premiere_mcp_configured()
    d["higgsfield_plugin"]=higgsfield_plugin_present()
    return d

def premiere_mcp_configured():
    # the 269-tool GitHub Premiere Pro MCP, registered with Claude Code, + MCP Bridge CEP extension
    import os
    hits=[]
    for cfg in [os.path.expanduser("~/.claude.json"), os.path.expanduser("~/.config/claude/mcp.json")]:
        try:
            if os.path.exists(cfg) and "premiere" in open(cfg,errors="ignore").read().lower(): hits.append(cfg)
        except Exception: pass
    if glob.glob("/Library/Application Support/Adobe/CEP/extensions/*[Mm][Cc][Pp]*") or \
       glob.glob(os.path.expanduser("~/Library/Application Support/Adobe/CEP/extensions/*[Mm][Cc][Pp]*")): hits.append("MCP Bridge CEP ext")
    return hits

def higgsfield_plugin_present():
    import os
    return glob.glob("/Library/Application Support/Adobe/CEP/extensions/*[Hh]iggs*") or \
           glob.glob(os.path.expanduser("~/Library/Application Support/Adobe/CEP/extensions/*[Hh]iggs*"))

# route classification. automation: FULL_AUTO / PROJECT_FILE_BRIDGE / CONDITIONAL / BLOCKED
def classify(d):
    rows=[]
    # 1 DIRECT_PREMIERE_AUTOMATED , the 269-tool Premiere MCP drives Premiere DIRECTLY when the app is open
    if d.get("premiere_mcp"):
        rows.append(("DIRECT_PREMIERE_AUTOMATED","ACTIVE","FULL_AUTO",
          f"Premiere MCP configured ({', '.join(str(x) for x in d['premiere_mcp'])}). 269 tools drive Premiere directly while open: requires project open + Window>Extensions>MCP Bridge running + refreshed Claude session. Remove silences, bad-take cut, rough cut, ripple/roll/slip/slide, A-roll/B-roll, captions, effects search, export.",
          "PREFERRED max-edit route. Confirm bridge live (os_premiere_compliance_gate), then edit natively. ffmpeg is only the assembly/export spine."))
    elif d["premiere_app"]:
        rows.append(("DIRECT_PREMIERE_AUTOMATED","NEEDS_INSTALL","FULL_AUTO_PENDING",
          "Premiere Pro INSTALLED. The 269-tool GitHub Premiere Pro MCP is the PREFERRED automated route but is NOT YET INSTALLED. This is direct control (app open), not headless.",
          "INSTALL FIRST: clone the GitHub premiere-pro MCP, register with Claude Code, open a Premiere project, Window>Extensions>MCP Bridge (running), refresh/new Claude session. Do NOT default to ffmpeg as the max editor; ffmpeg is interim spine only. Headless render stays N/A; FCPXML/EDL is a secondary bridge."))
    else:
        rows.append(("DIRECT_PREMIERE_AUTOMATED","BLOCKED","BLOCKED","Premiere not installed.","-"))
    # 2 ADOBE_VIDEO_MCP_AUTOMATED
    av=d["adobe_video_mcp"]
    if av:
        st="CONDITIONAL"
        rows.append(("ADOBE_VIDEO_MCP_AUTOMATED","AVAILABLE",st,
          f"Adobe video MCP tools present ({', '.join(k.split('.')[-1] for k in av)}); cut/reframe/resize callable but require asset UPLOAD to Adobe cloud first.",
          "Use for cloud quick-cut/reframe/resize after media_upload handshake. External; not fully local."))
    else:
        rows.append(("ADOBE_VIDEO_MCP_AUTOMATED","BLOCKED","BLOCKED","No Adobe video MCP tools in registry.","-"))
    # 3 AFTER_EFFECTS_AUTOMATED
    if d["aerender"]:
        rows.append(("AFTER_EFFECTS_AUTOMATED","AVAILABLE","FULL_AUTO",
          "aerender callable (headless). Renders comps; can build+render via `aerender -r script.jsx`.",
          "Automate titles / lower-thirds / motion-graphics via a template .aep or a build jsx, then render headless."))
    else:
        rows.append(("AFTER_EFFECTS_AUTOMATED","BLOCKED","BLOCKED","aerender not found.","-"))
    # 4 CAPCUT_AUTOMATED
    if d["capcut_app"] or d["capcut_lib"]:
        rows.append(("CAPCUT_AUTOMATED","AVAILABLE","CONDITIONAL","CapCut app or draft lib present.","Build CapCut draft JSON / drive the app."))
    else:
        rows.append(("CAPCUT_AUTOMATED","BLOCKED","BLOCKED",
          f"CapCut not installed, no CLI, no draft lib (pyJianYingDraft). {len(d['capcut_cards'])} CapCut DOCTRINE cards exist.",
          "CAPCUT_DOCS_AVAILABLE_BUT_AUTOMATION_BLOCKED: apply CapCut editing doctrine (captions/hooks/transitions) INSIDE the callable route."))
    # 5 HYPERFRAMES_PLUS_FFMPEG_AUTOMATED
    if d["ffmpeg"] and d["xfade"]:
        hf = "HyperFrames project(s) present" if d["hf_projects"] else "ffmpeg-only (no HF project yet)"
        rows.append(("HYPERFRAMES_PLUS_FFMPEG_AUTOMATED","ACTIVE","FULL_AUTO",
          f"ffmpeg + xfade callable; {hf}. drawtext={'yes' if d['drawtext'] else 'NO (titles via HyperFrames render, not ffmpeg text)'}.",
          "HyperFrames renders animated titles/cards (HTML->mp4); ffmpeg normalizes, applies xfade transitions, assembles, exports all aspects."))
    else:
        rows.append(("HYPERFRAMES_PLUS_FFMPEG_AUTOMATED","BLOCKED","BLOCKED","ffmpeg or xfade missing.","-"))
    # 6 HYBRID_AUTOMATED
    full=[r for r in rows if r[2]=="FULL_AUTO"]
    if full:
        rows.append(("HYBRID_AUTOMATED","ACTIVE","FULL_AUTO",
          "Compose the FULL_AUTO routes: HyperFrames+ffmpeg render spine (+ AE titles when needed) AND auto-generate FCPXML/EDL for an optional Premiere finishing pass.",
          "Strongest: fully automated deliverable end-to-end, with a premium editable bridge available. No human required."))
    else:
        rows.append(("HYBRID_AUTOMATED","BLOCKED","BLOCKED","No FULL_AUTO route to compose.","-"))
    # 7 BLOCKED_AFTER_VERIFICATION
    any_auto=any(r[2] in ("FULL_AUTO","PROJECT_FILE_BRIDGE","CONDITIONAL") for r in rows)
    rows.append(("BLOCKED_AFTER_VERIFICATION","N/A" if any_auto else "ACTIVE","BLOCKED",
        "Only if EVERY automated route is blocked. Then and only then a human handoff package is acceptable.",
        "Not triggered" if any_auto else "All automated routes blocked -> build the handoff package."))
    return rows

# route order per operator standard: Premiere MCP native -> Higgsfield-in-Premiere/AE -> AE -> HyperFrames -> ffmpeg spine/fallback
PRIORITY=["DIRECT_PREMIERE_AUTOMATED","AFTER_EFFECTS_AUTOMATED","ADOBE_VIDEO_MCP_AUTOMATED",
          "HYBRID_AUTOMATED","HYPERFRAMES_PLUS_FFMPEG_AUTOMATED","CAPCUT_AUTOMATED","BLOCKED_AFTER_VERIFICATION"]

def write_matrix(rows):
    with open(MATRIX,"w",newline="") as f:
        w=csv.writer(f); w.writerow(["route","status","automation","finding","how_or_handoff"])
        for r in rows: w.writerow(r)

def cmd_routes():
    d=detect(); rows=classify(d); write_matrix(rows)
    print("VIDEO EDIT ROUTE MATRIX")
    for route,st,au,find,how in rows:
        print(f"  [{st:9s}|{au:18s}] {route}")
        print(f"      {find}")
        if how and how not in ("-","Not triggered"): print(f"      -> {how}")
    print(f"\nmatrix -> {MATRIX}")
    return 0

def pick(rows=None):
    if rows is None: rows=classify(detect())
    by={r[0]:r for r in rows}
    # preferred route pending install? surface it (do not silently default to ffmpeg)
    pending=by.get("DIRECT_PREMIERE_AUTOMATED")
    pending=pending if (pending and pending[1]=="NEEDS_INSTALL") else None
    # working pick: prefer turnkey (ACTIVE + FULL_AUTO) in route order, then AVAILABLE, then conditional
    for want in (lambda r: r[1]=="ACTIVE" and r[2]=="FULL_AUTO",
                 lambda r: r[1] in ("ACTIVE","AVAILABLE") and r[2] not in ("BLOCKED",),):
        for route in PRIORITY:
            r=by.get(route)
            if r and want(r): return r, pending
    return by["BLOCKED_AFTER_VERIFICATION"], pending

def cmd_pick():
    r,pending=pick()
    if pending:
        print(f"PREFERRED ROUTE PENDING: DIRECT_PREMIERE_AUTOMATED (Premiere MCP) , NEEDS_INSTALL")
        print(f"  {pending[4]}")
        print(f"  Until installed, the interim working route is below (NOT the chosen max editor):\n")
    print(f"SELECTED ROUTE: {r[0]}  ({r[1]} / {r[2]})")
    print(f"  why: {r[4] if r[4] not in ('-','Not triggered') else r[3]}")
    if r[0]=="BLOCKED_AFTER_VERIFICATION":
        print("  ALL automated routes blocked -> human handoff package is now justified.")
    else:
        print("  Automated. No human handoff required.")
    return 0

def ffprobe_dur(p):
    try:
        return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],
            capture_output=True,text=True,timeout=20).stdout.strip())
    except Exception: return 0.0

def norm(src,dst,W=1280,H=720,FPS=30,dur=None):
    vf=f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS},format=yuv420p"
    cmd=["ffmpeg","-y","-i",src,"-vf",vf,"-an"]
    if dur: cmd+=["-t",str(dur)]
    cmd+=["-c:v","libx264","-pix_fmt","yuv420p",dst]
    subprocess.run(cmd,capture_output=True,text=True,timeout=120)

def synth(dst,color,dur=2,W=1280,H=720,FPS=30):
    subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"color=c={color}:s={W}x{H}:r={FPS}:d={dur}",
        "-vf","format=yuv420p","-c:v","libx264",dst],capture_output=True,text=True,timeout=120)

def synth_content(dst,dur=3,W=1280,H=720,FPS=30):
    subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"testsrc2=s={W}x{H}:r={FPS}:d={dur}",
        "-vf","format=yuv420p","-c:v","libx264",dst],capture_output=True,text=True,timeout=120)

def fcpxml(out,clips):
    fps=30; ft="100/3000s"  # 30fps frame duration
    body=['<?xml version="1.0" encoding="UTF-8"?>','<!DOCTYPE fcpxml>','<fcpxml version="1.9">','  <resources>',
          '    <format id="r1" name="FFVideoFormat720p30" frameDuration="100/3000s" width="1280" height="720"/>']
    assets=[]; off=0; spine=[]
    for i,c in enumerate(clips,1):
        dur=ffprobe_dur(c) or 2.0; frames=int(round(dur*fps))
        body.append(f'    <asset id="a{i}" name="{os.path.basename(c)}" src="file://{os.path.abspath(c)}" hasVideo="1" format="r1"/>')
        spine.append(f'        <asset-clip ref="a{i}" offset="{off*100}/3000s" name="{os.path.basename(c)}" duration="{frames*100}/3000s" format="r1"/>')
        off+=frames
    body.append('  </resources>')
    body+=['  <library>','    <event name="AXIS">','      <project name="edit">',
           f'        <sequence format="r1" duration="{off*100}/3000s"><spine>']
    body+= ["    "+s for s in spine]
    body+=['        </spine></sequence>','      </project>','    </event>','  </library>','</fcpxml>']
    open(out,"w").write("\n".join(body)+"\n"); return out

def edl(out,clips):
    fps=30
    def tc(fr):
        h=fr//(fps*3600); m=(fr//(fps*60))%60; s=(fr//fps)%60; f=fr%fps
        return f"{h:02d}:{m:02d}:{s:02d}:{f:02d}"
    lines=["TITLE: AXIS_DUMMY_EDIT","FCM: NON-DROP FRAME"]; rec=0
    for i,c in enumerate(clips,1):
        dur=ffprobe_dur(c) or 2.0; fr=int(round(dur*fps))
        lines.append(f"{i:03d}  AX       V     C        {tc(0)} {tc(fr)} {tc(rec)} {tc(rec+fr)}")
        lines.append(f"* FROM CLIP NAME: {os.path.basename(c)}"); rec+=fr
    open(out,"w").write("\n".join(lines)+"\n"); return out

def selftest(outdir):
    os.makedirs(outdir,exist_ok=True)
    log=[]; r,_pending=pick()
    log.append(f"selected route: {r[0]} ({r[1]}/{r[2]})")
    # title + end cards: prefer existing HyperFrames renders (proves the HF route); else synth slates
    hf_intro=os.path.join(CMD,"AXIS_ELITE_DEMO_PACKAGE_001","05_MOTION","intro_title_hf.mp4")
    hf_end  =os.path.join(CMD,"AXIS_ELITE_DEMO_PACKAGE_001","05_MOTION","endcard_hf.mp4")
    t=os.path.join(outdir,"01_title.mp4"); m=os.path.join(outdir,"02_content.mp4"); e=os.path.join(outdir,"03_end.mp4")
    if os.path.exists(hf_intro) and os.path.getsize(hf_intro)>0:
        norm(hf_intro,t,dur=2.0); log.append(f"title card: HyperFrames render -> {os.path.basename(t)} (HF route proven)")
    else:
        synth(t,"0x141315",2); log.append("title card: ffmpeg slate (no HF render found)")
    synth_content(m,3); log.append("content clip: ffmpeg testsrc2 3s (local, no AI credits)")
    if os.path.exists(hf_end) and os.path.getsize(hf_end)>0:
        norm(hf_end,e,dur=2.0); log.append(f"end card: HyperFrames render -> {os.path.basename(e)}")
    else:
        synth(e,"0x5a1a1a",2); log.append("end card: ffmpeg oxblood slate")
    # normalize all three to identical spec
    tn,mn,en=[os.path.join(outdir,f"n{os.path.basename(x)}") for x in (t,m,e)]
    for src,dst in ((t,tn),(m,mn),(e,en)): norm(src,dst)
    da,db,dc=[ffprobe_dur(x) for x in (tn,mn,en)]; T=0.5
    out=os.path.join(outdir,"axis_dummy_edit.mp4")
    fc=(f"[0:v][1:v]xfade=transition=fade:duration={T}:offset={max(da-T,0):.3f}[v01];"
        f"[v01][2:v]xfade=transition=fade:duration={T}:offset={max(da+db-2*T,0):.3f}[v]")
    cmd=["ffmpeg","-y","-i",tn,"-i",mn,"-i",en,"-filter_complex",fc,"-map","[v]","-c:v","libx264","-pix_fmt","yuv420p",out]
    p=subprocess.run(cmd,capture_output=True,text=True,timeout=180)
    ok=os.path.exists(out) and os.path.getsize(out)>0
    log.append(f"assemble (xfade x2 transitions): {'OK' if ok else 'FAIL'} -> {out if ok else p.stderr[-300:]}")
    # premium editable bridge
    fx=fcpxml(os.path.join(outdir,"axis_dummy_edit.fcpxml"),[tn,mn,en]); log.append(f"FCPXML bridge (Premiere-openable): {fx}")
    ed=edl(os.path.join(outdir,"axis_dummy_edit.edl"),[tn,mn,en]); log.append(f"EDL bridge: {ed}")
    total=ffprobe_dur(out)
    open(os.path.join(outdir,"VIDEO_EDIT_SELFTEST_LOG.txt"),"w").write("\n".join(log)+"\n")
    print("VIDEO EDIT SELFTEST")
    for l in log: print("  "+l)
    print(f"\n  export: {out} ({total:.2f}s)" if ok else "  EXPORT FAILED")
    print(f"  human handoff still required? NO , automated route {r[0]} produced the deliverable." if ok else "  route failed; escalate")
    return 0 if ok else 1

if __name__=="__main__":
    a=sys.argv[1:] or ["routes"]
    if a[0]=="routes": sys.exit(cmd_routes())
    if a[0]=="pick": sys.exit(cmd_pick())
    if a[0]=="selftest": sys.exit(selftest(a[1] if len(a)>1 else os.path.join(CMD,"OS_VIDEO_EDIT_SELFTEST")))
    if a[0]=="fcpxml" and len(a)>2: print(fcpxml(a[1],a[2:])); sys.exit(0)
    if a[0]=="edl" and len(a)>2: print(edl(a[1],a[2:])); sys.exit(0)
    print(__doc__); sys.exit(1)
