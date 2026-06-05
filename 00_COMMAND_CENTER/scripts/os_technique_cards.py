#!/usr/bin/env python3
"""
os_technique_cards.py , the SELF-SOLVE layer. How-to docs become applied fixes the OS reaches for.

The operator's standard: every doc is how-to game; with the docs + skills + tools, the OS must self-solve
its own problems , no bottlenecks. This holds technique cards extracted from the certified how-to docs.
When a gate fails or a need is weak, the OS calls `solve "<problem>"` and APPLIES the matching card,
instead of shipping underbuilt work or asking the operator.

Cards are extracted, not invented , each cites its source doc. Append more via new extractions.

  os_technique_cards.py list [--tool adobe|blender|higgsfield|figma]
  os_technique_cards.py solve "<problem text>"      , the card(s) that fix it
  os_technique_cards.py card <id>
"""
import sys, argparse

# id, tool, problem(keywords it solves), technique, steps, source
CARDS = [
 {"id":"ff_prompt_formula","tool":"adobe","problem":"flat generic image, vague prompt, not photoreal, slop",
  "technique":"Firefly image prompt formula (literal, not chatbot)",
  "steps":"[Subject][Action][Angle][Lighting][Background][Color palette][Style][Image type] + camera (300mm prime, f/4, ISO, shutter, film grain). Emotional words set tone. Never say 'generate/create'. Min viable = subject+descriptor+keyword but write more.",
  "source":"The_Adobe_Stack_Manual"},
 {"id":"ff_model_pick","tool":"adobe","problem":"which model, portrait quality, photoreal humans",
  "technique":"Model 4 vs Ultra","steps":"Default Model 4. Use Ultra ONLY for photoreal landscapes, detailed human portraits, medium groups. Ultra is slower. Text rendering: neither is great.","source":"The_Adobe_Stack_Manual"},
 {"id":"ff_visual_intensity","tool":"adobe","problem":"too stylized or too flat, want raw realism or magazine polish",
  "technique":"Visual Intensity slider","steps":"Left = raw snapshot realism. Right = magazine polish. Start middle. Keep left for realism, right for stylized. Match prompt to slider; don't fight controls.","source":"The_Adobe_Stack_Manual"},
 {"id":"ff_consistency","tool":"adobe","problem":"inconsistent look across frames, need same style, continuity",
  "technique":"Style + Composition Reference + Seeds","steps":"Style Reference = pull color/light/mood from an image. Composition Reference = lock layout. Combine for same look+layout, new subject. Same prompt+settings+seed = consistent iterations; change seed = new variation.","source":"The_Adobe_Stack_Manual"},
 {"id":"ff_gen_expand","tool":"adobe","problem":"weak crop, wrong aspect ratio, need cinematic wide, reformat",
  "technique":"Generative Expand","steps":"Reformat one image to multiple aspect ratios / extend canvas with matching generated content. Via Express Quick Action, Photoshop, or Generative Expand API for batch. Generate at target res; do not upscale low-res.","source":"The_Adobe_Stack_Manual"},
 {"id":"ff_gen_fill","tool":"adobe","problem":"need to add remove or replace an element, composite an object, cleanup",
  "technique":"Generative Fill","steps":"Add/remove/replace parts of an image with a text prompt (Photoshop or Express, Firefly-powered, commercially safe). For compositing a symbol object: fill or place, then match light/grade.","source":"The_Adobe_Stack_Manual"},
 {"id":"ff_frame_chain","tool":"adobe","problem":"video too short, need longer clip, sequence",
  "technique":"Frame chaining","steps":"Generate clip -> take its LAST frame -> use as START image of next clip -> repeat -> stitch in Premiere. Crop/adjust each handoff frame in Express/Premiere for consistency. For loops: provide first AND last frame.","source":"The_Adobe_Stack_Manual"},
 {"id":"ff_video_formula","tool":"adobe","problem":"weak video prompt, video not cinematic",
  "technique":"Firefly Video prompt formula","steps":"[Visual style][Subject][Action][Location][Lighting][Color grade][Shot Size][Camera Angle][Camera Motion][Aesthetic]. Min 8 words. Provide first+last frame for coherence. Don't let Style Preset fight the prompt.","source":"The_Adobe_Stack_Manual"},
 {"id":"ff_sound","tool":"adobe","problem":"need sound, soundtrack, sfx, voiceover, the sound gap",
  "technique":"Firefly audio","steps":"Generate Soundtrack: upload clip, align VIBE first then STYLE, get 4 duration-matched options. SFX: one sound per prompt, stack tracks for a soundscape. Speech: emotion on full sentences, spell out numbers, no brackets. Cannot do melody/singing.","source":"The_Adobe_Stack_Manual"},
 {"id":"chain_campaign_hero","tool":"adobe","problem":"build a campaign hero asset, ad, end to end",
  "technique":"Campaign hero chain","steps":"1 Firefly Ultra + Style Ref, 5-10 variants. 2 pick + Generate Similar. 3 Photoshop retouch + gen-fill + grade. 4 Express Brand Kit + resize all channels. 5 Frame.io tag+share for approval. 6 revise. 7 approve -> branded Share.","source":"The_Adobe_Stack_Manual"},
 {"id":"chain_personalize","tool":"adobe","problem":"need many variants, batch, scale, 100 versions",
  "technique":"Personalization at scale","steps":"Hero in PS/Firefly -> Firefly Services API (Generative Expand + Generative Match) for 100-1000 variants -> lock brand via Custom Model/Style Kit -> batch export via Express templates -> Frame.io by Collection.","source":"The_Adobe_Stack_Manual"},
 {"id":"bl_object_space","tool":"blender","problem":"blender frame flat black not composing, hall fails, render dead",
  "technique":"Win in object-space + light camera-facing faces","steps":"Object scenes (marks/seals/plinths/product) light to elite in 1-2 iters; vast halls are low-ROI vs 2D. KEY: a light whose rays travel toward the camera-facing faces (sun pointing +toward camera side) or faces render black. 3-point: key area + fill + rim.","source":"use_blender_like_this + AXIS_ELITE proof"},
 {"id":"bl_no_guess_views","tool":"blender","problem":"guessing camera, can't see scene, screenshot broken, blind",
  "technique":"Technical plan/section/elevation + contact sheet","steps":"Render ortho TOP + SIDE + FRONT to read the layout like an architect, then place the hero camera with certainty. For look-dev, render a contact sheet of N camera/light presets into one montage and judge real pixels. Renders are the feedback loop when the live screenshot is broken.","source":"AXIS_ELITE proof"},
 {"id":"bl_haze_dof","tool":"blender","problem":"blender not cinematic, no depth, no atmosphere",
  "technique":"Volumetric haze + DOF + dark world","steps":"Dark world so apertures read as voids. Confine a Principled-Volume haze cube to BEYOND the subject (not around the camera, or it whiteouts). Camera DOF: focus_object=subject, f-stop 2.5-4. Structured passes: scene/camera -> props -> light truss -> stage light+haze.","source":"use_blender_like_this"},
 {"id":"hf_continuity","tool":"higgsfield","problem":"identity drift, reuse hero, start image, motion from still",
  "technique":"Condition on locked hero via job_id","steps":"Upload locked hero once (media_upload+confirm). For stills use medias role 'image'; for seedance i2v use role 'start_image'. A prior generation's job_id can be passed directly as the media value (no re-upload). nano_banana_pro 4k=4cr.","source":"AXIS proof + Higgsfield"},
 {"id":"hf_literal","tool":"higgsfield","problem":"preset recommendation, nsfw false flag, wasted credit",
  "technique":"Force literal + reroll","steps":"If it offers a preset, re-call with declined_preset_id to generate your literal direction. seedance can false-flag nsfw on solo figures , re-prompt 'fully-clothed, no people besides…' and budget one reroll. Preflight cost with get_cost.","source":"AXIS proof"},
 # ---- converted from series 3 download (Adobe motherlode) , Photoshop compositing/retouch/grade ----
 {"id":"ps_light_integration","tool":"adobe","problem":"composite looks pasted, element not integrated, flat composite, layers don't sit",
  "technique":"Light integration via curves clipping masks + painted light/shadow","steps":"Per element: curves adjustment layer + CLIPPING MASK (clip to the layer). One curves up = light, one down = shadow; on each, invert mask (Ctrl+I) to black, then paint with a soft low-flow white brush only where light/shadow falls. Add rim light on lit edges. The brightest point = the main light source. This is what makes a composite read as one photograph.","source":"series_3_download"},
 {"id":"ps_color_match","tool":"adobe","problem":"subject color doesn't match background, warm subject on cool bg, composite color off",
  "technique":"Neural Filters Harmonization + Depth Blur","steps":"Select subject layer -> Filter > Neural Filters > Harmonization -> pick the background layer -> adjust strength (matches subject tones to bg). For realistic depth: Filter > Neural Filters > Depth Blur on bg, lower focal distance so focus sits at the subject plane. Match horizon line to subject's camera height first.","source":"series_3_download"},
 {"id":"ps_dodge_burn","tool":"adobe","problem":"flat skin, no form, body lacks light shape, retouch dodge burn",
  "technique":"Non-destructive dodge & burn (two curves)","steps":"Two curves layers: TOP set to blend SCREEN (dodge), BOTTOM set to MULTIPLY (shadow). On each, fill mask black (Ctrl+I). Paint WHITE at 10-15% opacity, soft brush. Ctrl+click the subject layer to LOAD AS SELECTION so paint is constrained to the subject (not the ground). Build form: inner/underside darker, sun-facing lighter.","source":"series_3_download"},
 {"id":"ps_grounding_shadow","tool":"adobe","problem":"subject floating, no contact shadow, doesn't sit on ground, weak spatial",
  "technique":"Contact + soft grounding shadow","steps":"Edge: add layer mask, soft black brush to rough the hard cut edge at contact points. Big soft shadow: elliptical marquee -> new layer -> fill dark brown -> Gaussian blur (~75-100px) -> free-transform flat under the feet/base -> blend MULTIPLY -> opacity ~20%. Paint away excess.","source":"series_3_download"},
 {"id":"ps_glow_emissive","tool":"adobe","problem":"light source has no glow, no emissive, flat light, no atmosphere",
  "technique":"Painted glow with blend modes","steps":"New layer near the source. Color-pick a warm tone from the source. Soft brush a blob. Blend mode Overlay or Linear Light (scroll modes to compare). Reinforce near the source for falloff. This is the cheap way to make any light feel emissive.","source":"series_3_download"},
 {"id":"ps_camera_raw_grade","tool":"adobe","problem":"final image not graded, look not unified, needs final polish, generic grade",
  "technique":"Camera Raw final grade (non-destructive)","steps":"Group layers (Ctrl+G), duplicate (Ctrl+J), keep original below, merge the top group. Crop (C, enter) to clear edge junk first. Filter > Camera Raw: vibrance, temperature, grain, vignette, s-curve, color grade (split-tone). Easy to overdo , set it, walk away, return and re-judge. Hold the one-accent discipline.","source":"series_3_download"},
 # ---- converted from last lightroom hopefully (Lightroom grade/retouch) ----
 {"id":"lr_local_masking","tool":"adobe","problem":"distracting bright area, uneven exposure, sky too bright, local grade lightroom",
  "technique":"Lightroom local masking","steps":"Masking panel: AI Select Subject / Select Sky for instant local masks; Radial gradient over a hot/bright distraction -> lower exposure + saturation to kill it; Linear gradient for skies/edges. Grade locally, not just globally. The brightest point should be the subject, not a corner leaf.","source":"last_lightroom_hopefully"},
 {"id":"lr_remove_tool","tool":"adobe","problem":"blemish, distraction, stray object, cleanup, spot removal",
  "technique":"Lightroom Remove tool (generative)","steps":"Remove tool with 'use generative AI' ON. Brush slightly larger than the blemish/object. STACK multiple removes in one generation (mark several spots, then generate once). Non-destructive, faster than Photoshop for simple cleanup.","source":"last_lightroom_hopefully"},
 {"id":"lr_grade_order","tool":"adobe","problem":"grade order, how to color grade, look not unified, raw to look",
  "technique":"Lightroom grade order","steps":"White balance first -> exposure/contrast -> tone curve (s-curve, lift/crush) -> HSL (target/mute hues) -> Color Grading (split-tone: cool shadows, warm or neutral highlights, hold one accent) -> Calibration for deep base shifts. Texture/Clarity/Dehaze sparingly. Quiet-luxury = restraint.","source":"last_lightroom_hopefully"},
 # ---- converted from sniped figma (design system) ----
 {"id":"fig_design_system","tool":"figma","problem":"template feel, no design system, weak typography, generic layout, no hierarchy",
  "technique":"Figma design system","steps":"Build the system, not a one-off: type pairing (one display + one grotesk) + a type SCALE; an 8pt grid; color + spacing TOKENS as variables; COMPONENTS with VARIANTS; AUTO-LAYOUT for everything; constraints for responsive. Owned system = kills the magazine-template look. Reuse, never rebuild per asset.","source":"sniped_figma"},
 {"id":"fig_pitch_board","tool":"figma","problem":"weak pitch board, deck not premium, board repetitive, client polish",
  "technique":"Figma pitch board / deck","steps":"Frames on the grid; locked brand components; ONE masthead + one idea per frame; deliberate hierarchy + negative space; show RANGE (wide/detail/object/face), never the same shot 4x. Build from the design-system components so it reads authored, not assembled.","source":"sniped_figma"},
 # ---- more series 3 (retouch + edit) ----
 {"id":"ps_frequency_separation","tool":"adobe","problem":"skin retouch, blotchy skin, even tone without losing texture, portrait retouch",
  "technique":"Frequency separation","steps":"Duplicate layer x2. Low layer = Gaussian blur (tone/color). High layer = Apply Image to keep texture (pores). Heal/clone tone on the LOW layer to fix blotches/shadows WITHOUT destroying pore texture. Identity edits forbidden on real clients; this is tone-evening only.","source":"series_3_download"},
 {"id":"pr_pacing","tool":"adobe","problem":"moving still, trailer flat, no rhythm, edit pacing, cut not cinematic",
  "technique":"Premiere/edit pacing","steps":"A trailer needs CUTS, not one shot. Cut on motion and on the beat. Vary shot length for rhythm (fast build, hold the hero). J/L cuts: let audio lead or trail the picture for flow. Kill dead frames at head/tail. A single move = teaser, never call it a trailer.","source":"series_3_download"},
]

# merge in converted cards from the sprint (workflow agents write TECHNIQUE_CARDS.json)
import json as _json, os as _os
_JSON=_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),"TECHNIQUE_CARDS.json")
if _os.path.exists(_JSON):
    try:
        _ext=_json.load(open(_JSON))
        _have={c["id"] for c in CARDS}
        for c in _ext:
            if c.get("id") and c["id"] not in _have:
                # normalize to the minimal fields solve() needs
                c.setdefault("problem",""); c.setdefault("technique",""); c.setdefault("steps",c.get("exact_steps","")); c.setdefault("tool",c.get("app","")); c.setdefault("source",c.get("source_doc",""))
                CARDS.append(c); _have.add(c["id"])
    except Exception: pass

def cmd_list(tool):
    for c in CARDS:
        if tool and c["tool"]!=tool: continue
        print(f"  [{c['tool']:10s}] {c['id']:20s} , {c['technique']}")
    return 0
def cmd_solve(q):
    ql=q.lower(); scored=[]
    for c in CARDS:
        s=sum(1 for w in set(ql.replace(',',' ').split()) if len(w)>3 and (w in c['problem'] or w in c['technique'].lower()))
        if s: scored.append((s,c))
    scored.sort(key=lambda x:-x[0])
    if not scored: print(f"no card for: {q}  (extract one from the how-to docs and append)"); return 1
    print(f"SELF-SOLVE for: {q}")
    for s,c in scored[:3]:
        print(f"\n[{c['id']}] ({c['tool']}) {c['technique']}  <- {c['source']}")
        print(f"  {c['steps']}")
    return 0
def cmd_card(cid):
    for c in CARDS:
        if c["id"]==cid:
            print(f"[{c['id']}] {c['tool']} , {c['technique']}\nproblem: {c['problem']}\nsteps: {c['steps']}\nsource: {c['source']}"); return 0
    print("unknown card"); return 1

def main():
    ap=argparse.ArgumentParser(prog="os_technique_cards.py"); sub=ap.add_subparsers(dest="cmd")
    l=sub.add_parser("list"); l.add_argument("--tool",default="")
    s=sub.add_parser("solve"); s.add_argument("q")
    c=sub.add_parser("card"); c.add_argument("id")
    a=ap.parse_args()
    if a.cmd=="list": return cmd_list(a.tool)
    if a.cmd=="solve": return cmd_solve(a.q)
    if a.cmd=="card": return cmd_card(a.id)
    ap.print_help(); return 1

if __name__=="__main__": sys.exit(main())
