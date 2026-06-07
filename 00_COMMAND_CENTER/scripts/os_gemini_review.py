#!/usr/bin/env python3
"""
os_gemini_review.py - the SECOND-MODEL (Gemini CLI) review lane. READ-ONLY.

Gemini is a hostile reviewer / second set of eyes / commercial-grade quality gate.
It NEVER edits files, never becomes source of truth, never crowns anything final.
See OS_SECOND_MODEL_LANE_STANDARD.md + GEMINI_USAGE_POLICY.md.

  os_gemini_review.py bundle <hero.mp4> <out_dir> [--tiles 6x6 --step 0.8]
      # build the review bundle: contact sheet (CONTACT_SHEET.jpg) for the cut.
      # (text bundle .md is assembled by the caller / the Alma driver.)

  os_gemini_review.py run <bundle_md> <out_basepath> [--image <contact_sheet.jpg>] [--cwd <repo>]
      # run gemini read-only on the bundle, save <out_basepath>.json and .md (the response).
      # invokes: gemini -p "<prompt incl. @bundle and image ref>" --output-format json

Guarantees: only `gemini -p ... --output-format json` is ever called (non-interactive,
no edit-approval path). Verifies totalCalls/edits are 0 in the returned stats and flags if not.
"""
import sys, os, json, subprocess, glob

def sh(cmd): return subprocess.run(cmd, capture_output=True, text=True)

def contact_sheet(hero, outdir, tiles="6x6", step=0.8):
    os.makedirs(outdir, exist_ok=True)
    tmp = os.path.join(outdir, "_cs_frames"); os.makedirs(tmp, exist_ok=True)
    for f in glob.glob(os.path.join(tmp,"*.jpg")): os.remove(f)
    dur = float(sh(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",hero]).stdout.strip() or 0)
    t, k = 0.0, 0
    while t < dur:
        o = os.path.join(tmp, f"{k:03d}.jpg")
        sh(["ffmpeg","-nostdin","-v","error","-ss",f"{t:.2f}","-i",hero,"-frames:v","1","-vf","scale=220:-1","-y",o])
        if os.path.exists(o):
            sh(["magick",o,"-gravity","South","-background","black","-splice","0x18","-font","/System/Library/Fonts/Helvetica.ttc",
                "-fill","#7CFC00","-pointsize","15","-annotate","+0+1",f"{t:.1f}s",o])
        t += step; k += 1
    out = os.path.join(outdir, "CONTACT_SHEET.jpg")
    sh(["montage"]+sorted(glob.glob(os.path.join(tmp,"*.jpg")))+["-tile",tiles,"-geometry","+3+3","-background","gray12",
        "-font","/System/Library/Fonts/Helvetica.ttc","-fill","white","-pointsize","20",
        "-title",f"{os.path.basename(hero)} {dur:.1f}s @{step}s",out])
    for f in glob.glob(os.path.join(tmp,"*.jpg")): os.remove(f)
    os.rmdir(tmp)
    print(f"contact sheet -> {out} ({dur:.1f}s, {k} frames @{step}s)")
    return out

REVIEW_PROMPT = """You are a HOSTILE commercial-director reviewing a swimwear brand commercial (ALMA LOVE, deadpan-luxury, Beverly Hills, no dialogue, music-driven). You are the second set of eyes whose job is to stop the team from settling. Read the review bundle file @{bundle} and the attached contact sheet image. Be brutal, specific, and EVIDENCE-BASED (cite timestamps from the bundle). Do not be polite.

Return STRICT JSON only, with EXACTLY these keys:
{{
 "brutal_score_out_of_10": <number>,
 "keep_list": [{{"t":"<timestamp>","why":"<reason>"}}],
 "cut_or_fix_list": [{{"t":"<timestamp>","problem":"<what>","fix":"<how>"}}],
 "missed_best_moments": ["<beat + why it should be in>"],
 "hook_reads": {{"verdict":"yes|no|weak","why":"<reason>"}},
 "speaker_gag_clear": {{"verdict":"yes|no|unclear","why":"<reason>"}},
 "product_inserts_same_world": {{"verdict":"yes|no","why":"<reason>"}},
 "wrong_person_bts_plate_issue": {{"found":"yes|no","where":"<timestamps>","detail":"<what>"}},
 "commercial_grade_or_social_rough": "<commercial-grade|social rough cut>",
 "v5_edit_plan": ["<exact ordered step>"],
 "what_claude_is_rationalizing": ["<thing the team is likely settling on or excusing>"],
 "tool_routing": {{"premiere":"use|avoid + why","after_effects":"use|avoid + why","higgsfield":"use|avoid + why","adobe":"use|avoid + why","ffmpeg":"use|avoid + why"}}
}}
Only output the JSON object. No prose before or after."""

def run(bundle_md, out_base, image=None, cwd=None):
    cwd = cwd or os.getcwd()
    bundle_rel = os.path.relpath(bundle_md, cwd)
    prompt = REVIEW_PROMPT.format(bundle="./"+bundle_rel)
    if image:
        prompt += f"\n\nThe contact sheet image is at: {os.path.relpath(image, cwd)} (read it as visual evidence)."
    cp = subprocess.run(["gemini","-p",prompt,"--output-format","json"], cwd=cwd, capture_output=True, text=True)
    raw = cp.stdout.strip()
    with open(out_base+".json","w") as f: f.write(raw)
    # parse wrapper -> response text -> try to parse inner JSON
    resp, stats_ok = raw, None
    try:
        wrap = json.loads(raw)
        resp = wrap.get("response", raw)
        tools = wrap.get("stats",{}).get("tools",{})
        stats_ok = (tools.get("totalCalls",0)==0)
    except Exception: pass
    with open(out_base+".md","w") as f:
        f.write(f"# Gemini second-model review (raw response)\n\nREAD-ONLY tool calls by Gemini: {'0 (clean)' if stats_ok else 'CHECK stats'}\n\n```\n{resp}\n```\n")
    print(f"gemini review -> {out_base}.json + .md | exit={cp.returncode} | gemini-edits={'0 OK' if stats_ok else 'VERIFY'}")
    if cp.returncode!=0: print("STDERR:", cp.stderr[:400])

if __name__=="__main__":
    a=sys.argv[1:]
    def opt(name,d=None):
        if name in a: i=a.index(name); v=a[i+1]; del a[i:i+2]; return v
        return d
    tiles=opt("--tiles","6x6"); step=float(opt("--step","0.8")); image=opt("--image"); cwd=opt("--cwd")
    if not a: print(__doc__)
    elif a[0]=="bundle" and len(a)>2: contact_sheet(a[1],a[2],tiles,step)
    elif a[0]=="run" and len(a)>2: run(a[1],a[2],image,cwd)
    else: print(__doc__)
