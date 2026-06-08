#!/usr/bin/env python3
"""
os_finish_plan.py - turn a locked selects EDL into a FINISHING plan + handoff packages.
Premiere MCP effect-apply may be broken (QE empty) and AE MCP may lack import/render;
this builds the HANDOFF so finishing happens in Premiere/AE/Chat-Video-Pro by hand,
plus the AE comp spec. Never concludes "Premiere is useless" - it hands off.

  os_finish_plan.py handoff <edl.csv> <footage_dir> <out_dir>
      # writes: CUT_LIST.md, ASSET_LIST.txt, TIMESTAMP_MAP.csv, handoff.fcpxml,
      #         AE_FINISHING_SPEC.md, REVISION_NOTES.md

EDL csv cols: order, clip, in, dur, beat   (Canon clips need 90deg rotation in Premiere)
"""
import sys, os, csv, html

def ffdur(f):
    import subprocess
    try: return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",f],capture_output=True,text=True).stdout.strip() or 0)
    except Exception: return 0.0

def fcpxml(rows, footage_dir):
    # minimal FCPXML 1.9 - 1080x1920 30fps, one spine, clips with in/out
    FR="1001/30000s"  # ~29.97; use 100/3000s style; keep simple frameDuration
    fd="100/3000s"
    assets=[]; clips=[]; seen={}; off=0
    for i,r in enumerate(rows):
        clip=r["clip"]; path=os.path.join(footage_dir, clip)
        if clip not in seen:
            seen[clip]=f"r{len(seen)+2}"
            d=ffdur(path) or 60
            assets.append(f'    <asset id="{seen[clip]}" name="{html.escape(clip)}" src="file://{html.escape(path)}" hasVideo="1" format="r1" duration="{int(d*30)}/30s" start="0s"/>')
        rid=seen[clip]; ins=float(r["in"]); dur=float(r["dur"])
        clips.append(f'        <asset-clip name="{html.escape(clip)}" ref="{rid}" offset="{int(off*30)}/30s" start="{int(ins*30)}/30s" duration="{int(dur*30)}/30s">'
                     f'<note>{html.escape(r.get("beat",""))}</note></asset-clip>')
        off+=dur
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n<fcpxml version="1.9">\n  <resources>\n'
            '    <format id="r1" name="FFVideoFormat1080x1920p30" frameDuration="%s" width="1080" height="1920"/>\n'
            % fd + "\n".join(assets) + "\n  </resources>\n  <library>\n    <event name=\"ALMA_FINISH\">\n      <project name=\"ALMA_FINISH_SEQUENCE\">\n"
            f'        <sequence format="r1" duration="{int(off*30)}/30s">\n          <spine>\n'
            + "\n".join(clips) + "\n          </spine>\n        </sequence>\n      </project>\n    </event>\n  </library>\n</fcpxml>\n")

def cmd_handoff(edl, footage_dir, outd):
    os.makedirs(outd, exist_ok=True)
    rows=list(csv.DictReader(open(edl)))
    # CUT LIST + TIMESTAMP MAP
    with open(os.path.join(outd,"CUT_LIST.md"),"w") as f:
        f.write("# CUT LIST (finishing handoff)\n\n| # | clip | in | dur | beat | rotate |\n| --- | --- | --- | --- | --- | --- |\n")
        for r in rows:
            rot="90deg (Canon shot sideways)" if r["clip"].startswith("D94A") else "none"
            f.write(f"| {r['order']} | {r['clip']} | {r['in']} | {r['dur']} | {r.get('beat','')} | {rot} |\n")
    with open(os.path.join(outd,"TIMESTAMP_MAP.csv"),"w") as f:
        w=csv.writer(f); w.writerow(["order","clip","src_in","dur","timeline_start"]); t=0
        for r in rows:
            w.writerow([r["order"],r["clip"],r["in"],r["dur"],f"{t:.3f}"]); t+=float(r["dur"])
    with open(os.path.join(outd,"ASSET_LIST.txt"),"w") as f:
        for c in sorted({r["clip"] for r in rows}): f.write(os.path.join(footage_dir,c)+"\n")
    with open(os.path.join(outd,"handoff.fcpxml"),"w") as f: f.write(fcpxml(rows, footage_dir))
    with open(os.path.join(outd,"AE_FINISHING_SPEC.md"),"w") as f:
        f.write("""# AE FINISHING SPEC (apply manually or when AE-MCP import/render is built)

## Hook comp (rack focus)
- 1080x1920, 30fps. Import the hook clip. Add **Gaussian Blur** (or Camera Lens Blur).
- Keyframe Blurriness: 28 @ 0.00s -> 0 @ 0.45s (ease out). NO opacity fade (avoids the dark dip).
- Keep the finger-wipe frame visible; freeze-hold the last pose ~0.4s.

## Plate-blur comp (tracked)
- Track the license plate region; apply Gaussian Blur (sigma ~28) + Mosaic, masked to the plate only.
- Enable only over the plate-visible window. Re-verify unreadable after render.

## Logo sting / end-card
- Import poster freeze. Add cream "Alma Love" lockup; fade Opacity 0->100 over 0.55s + Scale 96->100. Add "DEADPAN SUMMER" 0.2s later.

## Caption / lower-third (if used)
- Futura, tracked, fade in/out 0.3s. Restrained, 1-2 beats max.

## Render settings
- H.264, 1080x1920, 30fps, ~20 Mbps, AAC 192k 48k. Loudness target -14 LUFS.
""")
    with open(os.path.join(outd,"REVISION_NOTES.md"),"w") as f:
        f.write("# REVISION NOTES (for Premiere / Chat Video Pro operator)\n\n"
                "- Import handoff.fcpxml into Premiere (File > Import) -> sequence ALMA_FINISH_SEQUENCE.\n"
                "- Canon (D94A*) clips: set Motion > Rotation 90deg (shot sideways) + Scale to fill.\n"
                "- Apply the brand LUT (ALMA_LOVE_signature_look_v1.cube) via Lumetri.\n"
                "- Hook clip: apply the AE rack-focus spec (or Chat Video Pro AI VFX).\n"
                "- Plate: tracked-mask blur per AE spec; re-verify unreadable.\n"
                "- Audio: lay the 80s bed + SFX hits; master to -14 LUFS.\n"
                "- Why handoff: Premiere-MCP apply_effect returns 'Effect not found' (QE list empty); AE-MCP has no import/render. Manual/Chat-Video-Pro is the working premium route.\n")
    print(f"HANDOFF written to {outd}: CUT_LIST.md, TIMESTAMP_MAP.csv, ASSET_LIST.txt, handoff.fcpxml, AE_FINISHING_SPEC.md, REVISION_NOTES.md ({len(rows)} beats)")

if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)>=4 and a[0]=="handoff": cmd_handoff(a[1],a[2],a[3])
    else: print(__doc__)
