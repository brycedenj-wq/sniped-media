#!/usr/bin/env python3
"""
os_premium_stack_gate.py , premium stack is DEFAULT-ON for max work.

The operating standard: for any serious/max output (campaign, film, pitch, proof package, client demo,
money-facing asset, launch asset, trailer, deck, world, brand system) the OS assumes the PREMIUM stack
is required unless it proves otherwise IN WRITING. Local scripts are allowed only when faster AND
quality-equivalent-or-better, and that must be justified per need. A skipped premium tool with no
justification is a logged failure, not a default.

Runs BEFORE a max build (plan) and AFTER / on a retro (audit).

  os_premium_stack_gate.py needs <task_type>
  os_premium_stack_gate.py plan <task_type>
  os_premium_stack_gate.py audit <task_type> --used "need1,need2" [--justified "need=reason;..."] [--log L]

Verdicts:
  FULL PREMIUM STACK REQUIRED
  PREMIUM STACK PARTIAL, JUSTIFIED
  HOLD FOR TOOL ACTIVATION
  REJECT: UNDERBUILT
  REJECT: TOOL UNDERUSE
  REJECT: LOCAL SHORTCUT USED WHERE PREMIUM TOOL WAS REQUIRED
"""
import sys, os, csv, time, json, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
def _reg():
    s = importlib.util.spec_from_file_location("os_tool_registry", os.path.join(HERE, "os_tool_registry.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

# each capability NEED -> the premium tool(s) that satisfy it (in registry id form) + the local fallback.
# A local fallback is acceptable ONLY with a written justification that it is quality-equivalent-or-better.
NEED_TOOLS = {
  "premium_generation":  {"premium": ["mcp.higgsfield.image", "mcp.higgsfield.video"], "local": ["os.adobe_teaser"]},
  "post_production":      {"premium": ["mcp.adobe.remove_bg", "mcp.adobe.generative_expand", "mcp.adobe.select_prompt", "mcp.adobe.crop_resize"], "local": ["os.adobe_grade", "os.adobe_composite"]},
  "edit_pacing":         {"premium": ["local.aerender", "mcp.adobe.quick_cut"], "local": ["os.adobe_cut", "local.ffmpeg"]},
  "motion_design":       {"premium": ["local.aerender", "hyperframes"], "local": ["os.adobe_layout"]},
  "spatial_continuity":  {"premium": ["blender.native", "blender.gated"], "local": []},
  "layout_excellence":   {"premium": ["mcp.figma", "mcp.adobe.render_layout"], "local": ["os.adobe_layout"]},
  "client_polish":       {"premium": ["mcp.figma", "mcp.adobe.render_layout"], "local": ["os.adobe_layout", "local.pillow"]},
  "proof_loop":          {"premium": ["mcp.airtable", "mcp.notion", "mcp.gdrive"], "local": ["os.form_ingest"]},
}

# which needs a max task TYPE must consider (the default-on profile)
TASK_PROFILES = {
  "film":          ["premium_generation","post_production","edit_pacing","motion_design","spatial_continuity","layout_excellence","client_polish","proof_loop"],
  "campaign":      ["premium_generation","post_production","layout_excellence","client_polish","proof_loop"],
  "trailer":       ["premium_generation","edit_pacing","motion_design","post_production","proof_loop"],
  "pitch_deck":    ["layout_excellence","client_polish","proof_loop"],
  "brand_system":  ["premium_generation","layout_excellence","client_polish","spatial_continuity"],
  "proof_package": ["premium_generation","post_production","client_polish","proof_loop"],
  "client_demo":   ["premium_generation","post_production","layout_excellence","client_polish","proof_loop"],
  "world":         ["premium_generation","spatial_continuity","post_production","layout_excellence"],
  "launch_asset":  ["premium_generation","post_production","client_polish","proof_loop"],
}

def tool_status(reg, tid):
    return reg.TOOLS.get(tid, {}).get("status", "RED")

def cmd_needs(task):
    prof = TASK_PROFILES.get(task)
    if not prof: print(f"unknown task. types: {', '.join(TASK_PROFILES)}"); return 2
    print(f"NEEDS for max task '{task}':")
    for n in prof: print(f"  {n:20s} <- premium: {', '.join(NEED_TOOLS[n]['premium'])}")
    return 0

def cmd_plan(task):
    reg = _reg(); prof = TASK_PROFILES.get(task)
    if not prof: print(f"unknown task. types: {', '.join(TASK_PROFILES)}"); return 2
    print(f"PREMIUM STACK PLAN , task '{task}'")
    hold = []
    for n in prof:
        prem = NEED_TOOLS[n]["premium"]
        statuses = [(t, tool_status(reg, t)) for t in prem]
        active = [t for t, s in statuses if s == "ACTIVE"]
        line = "ACTIVE" if active else "NEEDS ACTIVATION"
        if not active: hold.append(n)
        print(f"  {n:20s} {line:18s} {', '.join(f'{t}[{s}]' for t,s in statuses)}")
    verdict = "FULL PREMIUM STACK REQUIRED" if not hold else "HOLD FOR TOOL ACTIVATION"
    print(f"\nVERDICT: {verdict}")
    if hold: print(f"  blocked needs (activate or justify a fallback): {', '.join(hold)}")
    return 0

def cmd_audit(a):
    reg = _reg(); prof = TASK_PROFILES.get(a.task)
    if not prof: print(f"unknown task. types: {', '.join(TASK_PROFILES)}"); return 2
    used = {x.strip() for x in (a.used or "").split(",") if x.strip()}
    justified = {}
    for pair in (a.justified or "").split(";"):
        if "=" in pair:
            k, v = pair.split("=", 1); justified[k.strip()] = v.strip()
    rows = []; underuse = []; shortcut = []; underbuilt = []
    for n in prof:
        prem = NEED_TOOLS[n]["premium"]
        active_prem = [t for t in prem if tool_status(reg, t) == "ACTIVE"]
        if n in used:
            rows.append((n, "PREMIUM USED")); continue
        if n in justified:
            rows.append((n, f"SKIPPED, JUSTIFIED: {justified[n][:50]}")); continue
        # skipped, not justified
        if active_prem:
            # a premium tool was available + relevant + not used + not justified
            if NEED_TOOLS[n]["local"]:
                rows.append((n, f"LOCAL SHORTCUT / UNUSED PREMIUM ({active_prem[0]})")); shortcut.append(n); underuse.append(n)
            else:
                rows.append((n, f"UNBUILT (premium {active_prem[0]} available, unused)")); underbuilt.append(n); underuse.append(n)
        else:
            rows.append((n, "UNBUILT + premium not active (HOLD)")); underbuilt.append(n)
    if shortcut:
        verdict = "REJECT: LOCAL SHORTCUT USED WHERE PREMIUM TOOL WAS REQUIRED"
    elif underuse:
        verdict = "REJECT: TOOL UNDERUSE"
    elif underbuilt:
        verdict = "REJECT: UNDERBUILT"
    elif justified:
        verdict = "PREMIUM STACK PARTIAL, JUSTIFIED"
    else:
        verdict = "FULL PREMIUM STACK USED"
    print(f"PREMIUM STACK AUDIT , task '{a.task}': {verdict}")
    for n, s in rows:
        flag = "OK " if s.startswith("PREMIUM USED") or s.startswith("SKIPPED, JUST") else "!! "
        print(f"  {flag}{n:20s} {s}")
    if underuse: print(f"\n  UNDERUSED (log to OS_TOOL_UNDERUSE_LEDGER): {', '.join(underuse)}")
    if underuse or underbuilt:
        print("  SELF-SOLVE (apply, do not ship underbuilt):")
        for n in (underuse or underbuilt):
            print(f"    os_technique_cards.py solve \"{n.replace('_',' ')}\"")
    if a.log:
        os.makedirs(os.path.dirname(a.log), exist_ok=True)
        new = not os.path.exists(a.log)
        with open(a.log, "a", newline="") as f:
            w = csv.writer(f)
            if new: w.writerow(["ts","task","verdict","underused","underbuilt"])
            w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), a.task, verdict, ";".join(underuse), ";".join(underbuilt)])
    return 0 if verdict.startswith(("FULL", "PREMIUM STACK PARTIAL")) else 1

def main():
    ap = argparse.ArgumentParser(prog="os_premium_stack_gate.py"); sub = ap.add_subparsers(dest="cmd")
    n = sub.add_parser("needs"); n.add_argument("task")
    p = sub.add_parser("plan"); p.add_argument("task")
    au = sub.add_parser("audit"); au.add_argument("task"); au.add_argument("--used", default=""); au.add_argument("--justified", default=""); au.add_argument("--log", default="")
    a = ap.parse_args()
    if a.cmd == "needs": return cmd_needs(a.task)
    if a.cmd == "plan": return cmd_plan(a.task)
    if a.cmd == "audit": return cmd_audit(a)
    ap.print_help(); return 1

if __name__ == "__main__": sys.exit(main())
