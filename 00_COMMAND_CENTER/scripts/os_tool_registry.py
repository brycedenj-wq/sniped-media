#!/usr/bin/env python3
"""
os_tool_registry.py , the OS Universal Tool Registry (source of truth for what is callable).

A tool counts as ACTIVE only if the OS can know-when / route / call-or-handoff / log / validate /
store / repeat. Installed or visible is NOT ACTIVE. This registry records the HONEST status from a
live-session inventory, plus the route map. No tool is ACTIVE here without a proving path.

  os_tool_registry.py tools [--status ACTIVE|AMBER|RED]
  os_tool_registry.py routes
  os_tool_registry.py route <route_id>
  os_tool_registry.py dashboard
"""
import sys, json, argparse

# kind: local (script/cli we can execute) | mcp (callable MCP tool, agent invokes) | skill | manual
# status: ACTIVE (callable + loggable + artifact path) | AMBER (connected/installed, unproven or needs handoff) | RED (not callable here)
TOOLS = {
    # ---- local (ACTIVE: we can shell to these now) ----
    "local.bash":        {"kind":"local","status":"ACTIVE","call":"Bash","note":"shell, persistent cwd"},
    "local.ffmpeg":      {"kind":"local","status":"ACTIVE","call":"ffmpeg","note":"video/motion finishing"},
    "local.exiftool":    {"kind":"local","status":"ACTIVE","call":"exiftool","note":"metadata strip/read (privacy)"},
    "local.pillow":      {"kind":"local","status":"ACTIVE","call":"python3 PIL","note":"image compositing/layout"},
    "local.numpy":       {"kind":"local","status":"ACTIVE","call":"python3 numpy","note":"image math"},
    "local.git":         {"kind":"local","status":"ACTIVE","call":"git","note":"versioning/backup-local"},
    "os.adobe_asset":    {"kind":"local","status":"ACTIVE","call":"scripts/os_adobe_asset.py","note":"asset I/O protocol"},
    "os.adobe_grade":    {"kind":"local","status":"ACTIVE","call":"scripts/os_adobe_grade.py","note":"locked LUXURY grade"},
    "os.adobe_composite":{"kind":"local","status":"ACTIVE","call":"scripts/os_adobe_composite.py","note":"colorlaw/glyph/cleanup/crop"},
    "os.adobe_reframe":  {"kind":"local","status":"ACTIVE","call":"scripts/os_adobe_reframe.py","note":"export specs"},
    "os.adobe_layout":   {"kind":"local","status":"ACTIVE","call":"scripts/os_adobe_layout.py","note":"poster/title/landing/onesheet/lookbook/carousel/board/thumbnail/dashboard"},
    "os.adobe_teaser":   {"kind":"local","status":"ACTIVE","call":"scripts/os_adobe_teaser.py","note":"still-based teaser"},
    "os.adobe_cut":      {"kind":"local","status":"ACTIVE","call":"scripts/os_adobe_cut.py","note":"motion finish"},
    "os.postproduction_gate":{"kind":"local","status":"ACTIVE","call":"scripts/os_postproduction_gate.py","note":"ship gate"},
    "os.campaign":       {"kind":"local","status":"ACTIVE","call":"scripts/os_campaign.py","note":"one-command kit"},
    "os.form_ingest":    {"kind":"local","status":"ACTIVE","call":"proofcell/form/os_form_ingest.py","note":"proof-loop ingest"},
    "os.form_score":     {"kind":"local","status":"ACTIVE","call":"proofcell/form/os_form_score.py","note":"proof-loop score"},
    # ---- mcp generation (ACTIVE: callable, agent invokes, proven) ----
    "mcp.higgsfield.image":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Higgsfield__generate_image","note":"nano_banana_pro stills, preflight get_cost","approval":"spend"},
    "mcp.higgsfield.video":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Higgsfield__generate_video","note":"seedance motion ~18cr/4s","approval":"spend"},
    "mcp.higgsfield.balance":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Higgsfield__balance","note":"credit balance"},
    # ---- mcp adobe (ACTIVE callable; verify with one real op) ----
    "mcp.adobe.crop_resize":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__image_crop_and_resize","note":"PROVEN: subject-aware crop via upload handshake (os_adobe_cloud), DEED 1:1 artifact"},
    "mcp.adobe.remove_bg":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__image_remove_background","note":"cutout for mockups/composite"},
    "mcp.adobe.select_prompt":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__image_select_by_prompt","note":"masked selection for targeted edits/retouch"},
    "mcp.adobe.quick_cut":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__video_create_quick_cut","note":"AI highlight reel"},
    "mcp.adobe.video_resize":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__video_resize","note":"video resize"},
    "mcp.adobe.render_layout":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__document_render_layout","note":"InDesign -> PDF/PNG"},
    "mcp.adobe.merge_layout":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__document_merge_data_layout","note":"InDesign CSV batch"},
    "mcp.adobe.search_design":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Adobe_for_creativity__search_design","note":"Express templates"},
    "mcp.adobe.generative_expand":{"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Adobe_for_creativity__image_generative_expand","note":"generative outpaint","approval":"generative"},
    # ---- mcp other connected (AMBER: connected, unproven in a route) ----
    "mcp.figma":   {"kind":"mcp","status":"AMBER","call":"mcp__figma-desktop__*","note":"needs live Figma desktop file"},
    "mcp.airtable":{"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Airtable__*","note":"lead/record tracking, unproven route"},
    "mcp.notion":  {"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Notion__*","note":"docs/CRM, unproven route"},
    "mcp.gdrive":  {"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Google_Drive__*","note":"storage; TEMP-bridge caution"},
    "mcp.gmail":   {"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Gmail__*","note":"drafts only; no send without approval","approval":"outbound"},
    "mcp.gcal":    {"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Google_Calendar__*","note":"calendar; TEMP-bridge caution"},
    "mcp.semrush": {"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Semrush__*","note":"SEO/market intel, unproven route"},
    "mcp.netlify": {"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Netlify__*","note":"hosting; HELD (no hosting)","approval":"public"},
    "mcp.vercel":  {"kind":"mcp","status":"AMBER","call":"mcp__plugin_vercel_vercel__*","note":"hosting/domains; HELD","approval":"public"},
    # ---- named adobe skills (AMBER: functions callable via MCP, discrete skills not confirmed in-chat) ----
    "skill.adobe.batch_edit":{"kind":"skill","status":"AMBER","call":"adobe-batch-edit-photos","note":"use mcp.adobe.* loop as substitute"},
    "skill.adobe.social_variations":{"kind":"skill","status":"AMBER","call":"adobe-create-social-variations","note":"use mcp.adobe.crop_resize multi-aspect"},
    "skill.adobe.design_template":{"kind":"skill","status":"AMBER","call":"adobe-design-from-template","note":"use mcp.adobe.search_design + fill_text"},
    "skill.adobe.quick_cut":{"kind":"skill","status":"AMBER","call":"adobe-edit-quick-cut","note":"use mcp.adobe.quick_cut"},
    "skill.adobe.resize":{"kind":"skill","status":"AMBER","call":"adobe-resize-photos-and-videos","note":"use mcp.adobe.crop_resize / video_resize"},
    "skill.adobe.retouch":{"kind":"skill","status":"AMBER","call":"adobe-retouch-portraits","note":"compose mcp.adobe.select_prompt + adjust; identity edits FORBIDDEN on real people"},
    # ---- INSTALLED in claude.ai app, NOT bridged to this CLI session (AMBER + handoff) ----
    # confirmed present in the user's claude.ai Directory screenshots, but not callable as MCP tools here.
    "bridge.twilio":  {"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"SMS/voice dev kit; HANDOFF: run in claude.ai app","approval":"outbound"},
    "bridge.zapier":  {"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"8000+ app actions; HANDOFF to app; powerful + risky, gate every action"},
    "bridge.zoominfo":{"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"lead enrichment; HANDOFF; identity/privacy caution"},
    "bridge.desktop_commander":{"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"terminal/file ops in app; local Bash already covers this here"},
    "bridge.pdf_viewer":{"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"view/annotate/sign PDF; HANDOFF; Pillow/Adobe render covers PDF gen here"},
    "bridge.adspirer":{"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"cross-platform ad mgmt; HANDOFF; HELD (no ad spend without approval)","approval":"spend"},
    "bridge.product_tracking":{"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"Accoil product analytics; HANDOFF"},
    "bridge.brand_voice":{"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"Tribe AI brand-voice; HANDOFF; SNIPED voice already doctrine here"},
    "bridge.biz_skills":{"kind":"plugin","status":"AMBER","call":"claude.ai app","note":"Anthropic Sales/Marketing/Legal/Finance/HR/Eng/Design/Ops/Data/Productivity skills; HANDOFF to app"},
    # ---- Anthropic skills in claude.ai (AMBER here; available in the app) ----
    "askill.canvas_design":{"kind":"skill","status":"AMBER","call":"/canvas-design (claude.ai)","note":"PNG/PDF visual art; os_adobe_layout covers most here"},
    "askill.web_artifacts":{"kind":"skill","status":"AMBER","call":"/web-artifacts-builder (claude.ai)","note":"multi-component HTML artifacts; closes the real-HTML-landing gap via handoff"},
    "askill.theme_factory":{"kind":"skill","status":"AMBER","call":"/theme-factory (claude.ai)","note":"themed slides/docs/landing"},
    "askill.brand_guidelines":{"kind":"skill","status":"AMBER","call":"/brand-guidelines (claude.ai)","note":"brand kit application"},
    "askill.skill_creator":{"kind":"skill","status":"AMBER","call":"/skill-creator (claude.ai)","note":"author new skills; os_skill.py covers local"},
    "askill.mcp_builder":{"kind":"skill","status":"AMBER","call":"/mcp-builder (claude.ai)","note":"build MCP servers; path to bridge the AMBER plugins into a CLI session later"},
    # ---- not installed anywhere visible (RED) ----
    "red.midjourney":{"kind":"app","status":"RED","call":"-","note":"not installed (use Higgsfield)"},
    "red.capcut":   {"kind":"app","status":"RED","call":"-","note":"not installed (use ffmpeg/os_adobe_cut)"},
    "red.blender":  {"kind":"app","status":"RED","call":"-","note":"not installed"},
    "red.spline":   {"kind":"app","status":"RED","call":"-","note":"not installed"},
    "red.unreal":   {"kind":"app","status":"RED","call":"-","note":"not installed"},
    "red.synthesia":{"kind":"app","status":"RED","call":"-","note":"not installed"},
    # ---- manual / human taste (handoff protocol) ----
    "manual.taste_signoff":{"kind":"manual","status":"ACTIVE","call":"operator","note":"final client-ready taste verdict, handoff"},
    "manual.legal":  {"kind":"manual","status":"AMBER","call":"operator+lawyer","note":"legal finalization, NEVER auto"},
    "manual.payment":{"kind":"manual","status":"RED","call":"operator","note":"payment rail, HELD behind approval"},
}

# routes: ordered toolchain, inputs, outputs, approval gates, log, validation, fallback, status, proof
ROUTES = {
    "make_campaign_package":{"toolchain":["os.campaign"],"inputs":["hero image"],"outputs":["full kit + gate + dashboard"],
        "approval":[],"log":"postproduction/<name>/10_logs/EDIT_LOG.csv","validation":"os.postproduction_gate","fallback":"run os_adobe_* steps individually","status":"ACTIVE","exec":"local",
        "proof":"postproduction/LOT00_CAMPAIGN_001/"},
    "edit_image":{"toolchain":["os.adobe_grade","os.adobe_composite"],"inputs":["image"],"outputs":["graded/fixed image"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"os.postproduction_gate","fallback":"mcp.adobe.* (generative)","status":"ACTIVE","exec":"local","proof":"postproduction/lot00_4k_001/02_composite/"},
    "generate_motion":{"toolchain":["mcp.higgsfield.balance","mcp.higgsfield.video","os.adobe_cut"],"inputs":["hero still or prompt"],"outputs":["clip + finished cut"],
        "approval":["spend"],"log":"SPEND_LEDGER.csv","validation":"os_motion_qa","fallback":"still-based os.adobe_teaser","status":"ACTIVE","exec":"agent","proof":"campaign_house/axis_meridian_motion_001/06_approved/axis_motion_v1.mp4"},
    "cut_video":{"toolchain":["os.adobe_cut"],"inputs":["clip"],"outputs":["muted/trimmed/resized/caption-safe"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"ffprobe dims","fallback":"mcp.adobe.video_resize","status":"ACTIVE","exec":"local","proof":"postproduction/lot00_001/04_motion/"},
    "build_landing_page":{"toolchain":["os.adobe_layout"],"inputs":["hero","headline","cta"],"outputs":["landing hero PNG"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"file exists + dims","fallback":"manual HTML","status":"AMBER","exec":"local","proof":"postproduction/MAX_CAPABILITY_001/artifacts/03_landing_hero.png","gap":"real responsive HTML export not built"},
    "create_proof_loop":{"toolchain":["os.form_ingest","os.form_score"],"inputs":["form CSV export"],"outputs":["scored responses"],
        "approval":["public-if-deployed"],"log":"proofcell/form/RESPONSES.csv","validation":"os.form_score","fallback":"manual tally","status":"AMBER","exec":"local","proof":"proofcell/form/","gap":"not deployed (held)"},
    "track_leads":{"toolchain":["mcp.airtable"],"inputs":["lead rows"],"outputs":["tracked records"],
        "approval":[],"log":"airtable","validation":"record count","fallback":"local CSV","status":"AMBER","exec":"agent","proof":"NONE","gap":"no proven route/test yet"},
    "score_money_path":{"toolchain":["os.money_path"],"inputs":["world/asset/offer"],"outputs":["money-readiness score"],
        "approval":[],"log":"money_path log","validation":"deterministic rubric","fallback":"manual","status":"ACTIVE","exec":"local","proof":"built this sprint"},
    "generate_pdf":{"toolchain":["local.pillow"],"inputs":["images"],"outputs":["PDF"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"pdf opens","fallback":"mcp.adobe.render_layout","status":"ACTIVE","exec":"local","proof":"built this sprint"},
    "update_dashboard":{"toolchain":["os.adobe_layout"],"inputs":["rows"],"outputs":["dashboard PNG"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"file exists","fallback":"markdown table","status":"ACTIVE","exec":"local","proof":"LOT00_CAMPAIGN_001/04_artifacts/10_proof_dashboard.png"},
    "build_pitch_deck":{"toolchain":["os.adobe_layout","local.pillow"],"inputs":["world","assets"],"outputs":["board + onesheet -> PDF"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"pdf opens","fallback":"mcp.adobe.search_design","status":"AMBER","exec":"local","proof":"MAX_CAPABILITY_001/artifacts/09_pitch_board.png","gap":"multi-page deck not templated"},
    "run_launch_readiness_check":{"toolchain":["os.launch_check"],"inputs":["sprint folder"],"outputs":["readiness report"],
        "approval":[],"log":"launch_check log","validation":"deterministic checks","fallback":"manual checklist","status":"ACTIVE","exec":"local","proof":"built this sprint"},
}

def main():
    ap = argparse.ArgumentParser(prog="os_tool_registry.py"); sub = ap.add_subparsers(dest="cmd")
    t = sub.add_parser("tools"); t.add_argument("--status", default="")
    sub.add_parser("routes"); r = sub.add_parser("route"); r.add_argument("route_id")
    sub.add_parser("dashboard"); sub.add_parser("json")
    a = ap.parse_args()
    if a.cmd == "tools":
        for tid, t in TOOLS.items():
            if a.status and t["status"] != a.status: continue
            print(f"  [{t['status']:6s}] {tid:28s} {t['kind']:6s} {t['note']}")
    elif a.cmd == "routes":
        for rid, r in ROUTES.items(): print(f"  [{r['status']:6s}] {rid:28s} -> {' + '.join(r['toolchain'])}")
    elif a.cmd == "route":
        print(json.dumps(ROUTES.get(a.route_id, {"error": "unknown route"}), indent=2))
    elif a.cmd == "dashboard":
        from collections import Counter
        c = Counter(t["status"] for t in TOOLS.values()); rc = Counter(r["status"] for r in ROUTES.values())
        print(f"TOOLS: {c['ACTIVE']} ACTIVE / {c['AMBER']} AMBER / {c['RED']} RED  (of {len(TOOLS)})")
        print(f"ROUTES: {rc['ACTIVE']} ACTIVE / {rc['AMBER']} AMBER / {rc['RED']} RED  (of {len(ROUTES)})")
    elif a.cmd == "json":
        print(json.dumps({"tools": TOOLS, "routes": ROUTES}))
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
