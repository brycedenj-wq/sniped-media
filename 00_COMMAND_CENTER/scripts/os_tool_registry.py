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
    "os.crs":            {"kind":"local","status":"ACTIVE","call":"scripts/os_crs.py","note":"character reference system (original chars)"},
    "os.world":          {"kind":"local","status":"ACTIVE","call":"scripts/os_world.py","note":"world bible build + gate"},
    "os.face":           {"kind":"local","status":"ACTIVE","call":"scripts/os_face.py","note":"face-lock conditioning"},
    "os.herolock":       {"kind":"local","status":"ACTIVE","call":"scripts/os_herolock.py","note":"locked-hero registry + match"},
    "os.facematch":      {"kind":"local","status":"ACTIVE","call":"scripts/os_facematch.py","note":"face-match readiness gate"},
    "os.motion_qa":      {"kind":"local","status":"ACTIVE","call":"scripts/os_motion_qa.py","note":"motion QA gate"},
    "os.motion_ready":   {"kind":"local","status":"ACTIVE","call":"scripts/os_motion_ready.py","note":"motion readiness check"},
    "os.money_path":     {"kind":"local","status":"ACTIVE","call":"scripts/os_money_path.py","note":"money-readiness rubric"},
    "os.launch_check":   {"kind":"local","status":"ACTIVE","call":"scripts/os_launch_check.py","note":"launch readiness checks"},
    "os.certify":        {"kind":"local","status":"ACTIVE","call":"scripts/os_certify.py","note":"source certification ledger"},
    "os.segment_ledger": {"kind":"local","status":"ACTIVE","call":"scripts/os_segment_ledger.py","note":"token-aware segment coverage"},
    "os.tool_test":      {"kind":"local","status":"ACTIVE","call":"scripts/os_tool_test.py","note":"tool activation test harness"},
    "os.tool_registry":  {"kind":"local","status":"ACTIVE","call":"scripts/os_tool_registry.py","note":"this registry (source of truth)"},
    "os.privacy_gate":   {"kind":"local","status":"ACTIVE","call":"scripts/os_privacy_gate.py","note":"identity/leak gate"},
    "os.vision_gate":    {"kind":"local","status":"ACTIVE","call":"scripts/os_vision_gate.py","note":"visual reject/beat-source gate"},
    "os.name_gate":      {"kind":"local","status":"ACTIVE","call":"scripts/os_name_gate.py","note":".com + brand availability gate"},
    "os.premium_stack_gate":{"kind":"local","status":"ACTIVE","call":"scripts/os_premium_stack_gate.py","note":"premium-stack default-on enforcement; runs before any MAX build"},
    "os.elite_gate":     {"kind":"local","status":"ACTIVE","call":"scripts/os_elite_art_direction_gate.py","note":"rejects merely-clean; 12-dim ELITE/STRONG/GENERIC/REJECT"},
    "os.howto_extract":  {"kind":"local","status":"ACTIVE","call":"scripts/os_howto_extract.py","note":"scan docs by CONTENT (names mislead) -> tool/technique density map + extract"},
    "os.technique_cards":{"kind":"local","status":"ACTIVE","call":"scripts/os_technique_cards.py","note":"SELF-SOLVE layer: how-to cards (problem->technique->steps) gates pull on failure"},
    "os.starthere_convert":{"kind":"local","status":"ACTIVE","call":"scripts/os_starthere_convert.py","note":"Start Here conversion status/backlog/matrix (reads OS archive)"},
    "os.pricing_gate":   {"kind":"local","status":"ACTIVE","call":"scripts/os_pricing_gate.py","note":"value-not-cost, 3-option anchor, floor, premium-as-insurance"},
    "os.offer_builder":  {"kind":"local","status":"ACTIVE","call":"scripts/os_offer_builder.py","note":"Hormozi value equation + grand-slam offer stack"},
    "os.client_fit_gate":{"kind":"local","status":"ACTIVE","call":"scripts/os_client_fit_gate.py","note":"prospect screen FIT/HOLD/PASS (trust + WWP + Mom Test)"},
    "os.proof_to_cash":  {"kind":"local","status":"ACTIVE","call":"scripts/os_proof_to_cash_router.py","note":"proof -> fastest clean cash play + 72h plan; payment follows proof"},
    "os.sales_script":   {"kind":"local","status":"ACTIVE","call":"scripts/os_sales_script.py","note":"VIB DM / discovery / objection / decline (drafts, faceless-safe)"},
    "os.crm_schema":     {"kind":"local","status":"ACTIVE","call":"scripts/os_crm_schema.py","note":"Notion 5-DB + Airtable mirror + dashboard metrics"},
    # ---- game engines (RED until a playable proof exists; see OS_GAME_PIPELINE_DECISION.md) ----
    "engine.godot":      {"kind":"app","status":"RED","call":"-","note":"not installed; FIRST playable-proof candidate. ACTIVE only when a playable build exists"},
    "engine.unreal":     {"kind":"app","status":"RED","call":"-","note":"not installed; later high-ceiling cinematic/game route"},
    "engine.unity":      {"kind":"app","status":"RED","call":"-","note":"not installed; later only if client/mobile/AR forces it"},
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
    # ---- mcp other connected (status from 2026-06-05 post-restart live proof; READ proven = ACTIVE-read, WRITE still gated) ----
    "mcp.figma":   {"kind":"mcp","status":"ACTIVE","call":"mcp__plugin_figma_figma__*","note":"PROVEN whoami (Bryce, pro team) 2026-06-05. Design read/write needs a live file; OWNS design-system + code<->design bridge","role":"design_system"},
    "mcp.airtable":{"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Airtable__*","note":"PROVEN ping->pong + list 2026-06-05. OWNS structured ops data / forecast tables; write (create_records) gated-untested","role":"ops_data"},
    "mcp.notion":  {"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Notion__*","note":"PROVEN get-users (Bryceden Jones) 2026-06-05. OWNS CRM (5-DB schema) + human-readable doctrine surface; CRM write untested","role":"crm_doctrine_surface"},
    "mcp.gdrive":  {"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Google_Drive__*","note":"PROVEN list_recent_files 2026-06-05. OWNS large-asset storage; TEMP-bridge: no writes that anchor personal acct as BASEPLATE","role":"asset_storage","approval":"storage-write"},
    "mcp.gmail":   {"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Gmail__*","note":"PROVEN list_labels 2026-06-05. draft-only; NO send without approval; OWNS inbox triage + draft staging","role":"inbox","approval":"outbound"},
    "mcp.gcal":    {"kind":"mcp","status":"ACTIVE","call":"mcp__claude_ai_Google_Calendar__*","note":"PROVEN list_calendars 2026-06-05. OWNS schedule truth for operator-plan; TEMP-bridge caution on mutations","role":"schedule"},
    "mcp.semrush": {"kind":"mcp","status":"RED","call":"mcp__claude_ai_Semrush__*","note":"CONNECTED but current Semrush plan EXCLUDES MCP data access (proven block 2026-06-05). Unlock: semrush.com/mcp-access. No data until then"},
    "mcp.netlify": {"kind":"mcp","status":"AMBER","call":"mcp__claude_ai_Netlify__*","note":"requires OAuth (authenticate not completed); hosting HELD anyway","approval":"public"},
    "mcp.vercel":  {"kind":"mcp","status":"ACTIVE","call":"mcp__plugin_vercel_vercel__*","note":"PROVEN list_teams 2026-06-05. Deploy/domains route live but HELD behind public-action approval","role":"deploy","approval":"public"},
    # ---- 3D / motion / video native (2026-06-05 post-restart) ----
    "blender.native":{"kind":"mcp","status":"ACTIVE","call":"mcp__blender__*","note":"PROVEN scene-read + render (320x180 PNG -> sandbox) 2026-06-05, port 9876. RUNS LLM CODE UNGATED -> gate FIRST. NOTE: renders to MCP server temp, OS must copy artifact into sandbox; path-gate governs persistence + code constrains net/subprocess/destructive","role":"worldbuild_3d","approval":"sandbox-only"},
    "blender.gated":{"kind":"local","status":"ACTIVE","call":"scripts/os_blender_gate.py","note":"PROVEN allow in-sandbox + deny ~/.ssh 2026-06-05. The security contract for blender.native; logs every action","role":"3d_gate"},
    "local.aerender":{"kind":"local","status":"ACTIVE","call":"/Applications/Adobe After Effects 2026/aerender","note":"PROVEN aerender 26.2.1x2 2026-06-05. CLI title/motion render; needs an .aep project to exercise a real comp","role":"motion_render"},
    "hyperframes":  {"kind":"local","status":"ACTIVE","call":"npx hyperframes","note":"PROVEN doctor v0.6.73 (ffmpeg+chrome ok) 2026-06-05. OWNS code-defined HTML motion/video; Docker only for containerized render","role":"html_motion"},
    "red.premiere": {"kind":"app","status":"AMBER","call":"see mcp.premiere","note":"Premiere Pro 2026 INSTALLED. DIRECT control via mcp.premiere (269-tool MCP + CEP MCP Bridge) = PREFERRED-PENDING. No HEADLESS render (that part only -> FCPXML/EDL bridge). Superseded by mcp.premiere entry."},
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
    "red.spline":   {"kind":"app","status":"RED","call":"-","note":"not installed (use blender.native gated)"},
    "red.unreal":   {"kind":"app","status":"RED","call":"-","note":"not installed"},
    "red.synthesia":{"kind":"app","status":"RED","call":"-","note":"not installed"},
    # ---- manual / human taste (handoff protocol) ----
    "manual.taste_signoff":{"kind":"manual","status":"ACTIVE","call":"operator","note":"final client-ready taste verdict, handoff"},
    "manual.legal":  {"kind":"manual","status":"AMBER","call":"operator+lawyer","note":"legal finalization, NEVER auto"},
    "manual.payment":{"kind":"manual","status":"RED","call":"operator","note":"payment rail, HELD behind approval"},
    # ---- cloned tool repos integrated 2026-06-05 (server-reachable; bridges/new-session pending) ----
    "mcp.premiere":   {"kind":"mcp","status":"AMBER","call":"node ~/premiere-pro-mcp/dist/index.js","note":"DIRECT Premiere control 269 tools; PREFERRED-PENDING (built+registered+CEP installed; needs Premiere open + MCP Bridge Start + new session); gate os_premiere_compliance_gate"},
    "mcp.after_effects":{"kind":"mcp","status":"AMBER","call":"node ~/after-effects-mcp/build/index.js","note":"AE control; PREFERRED-PENDING (built+registered; ScriptUI bridge install MANUAL + new session)"},
    "skill.video_use":{"kind":"skill","status":"AMBER","call":"~/video-use","note":"conversational ffmpeg+PIL edit; cards vuse_*; no proof edit yet"},
    "skill.blender_assembly":{"kind":"skill","status":"ACTIVE","call":"~/Blender-MCP-Assembly-Skill","note":"geometry correctness; cards blasm_*; feeds os_blender_gate"},
    "skill.taste":    {"kind":"skill","status":"ACTIVE","call":"~/taste-skill","note":"anti-slop design; cards taste_*; feeds FIGMA + elite gate"},
    "skill.world_builder":{"kind":"skill","status":"AMBER","call":"~/world-builder","note":"reference->Blender scene; cards wbld_*; needs fal ~$4-6/world spend"},
    "mcp.unreal":     {"kind":"mcp","status":"RED","call":"~/unreal-mcp","note":"Unreal control; OPTIONAL/PENDING, games lane not active"},
    "tool.hyperframes":{"kind":"local","status":"ACTIVE","call":"npx hyperframes","note":"HTML->mp4 titles; HYBRID edit spine; PROVEN"},
}

# ADOBE CAPABILITY MATRIX , Adobe is NOT one blob. 16 discrete capabilities, each with its own
# OS job, relationship to a local script (replace/complement), inputs, artifact, log, gate, proof,
# status, and the smallest safe activation test. Upload to Adobe storage is via os_adobe_cloud handshake
# (prep->init->put->finalize) because Adobe tools reject external URLs and the CLI has no file picker.
ADOBE_CAPABILITIES = {
  "batch_photo_edit":   {"job":"apply locked grade/op to many frames","vs_local":"complement os_adobe_grade (local grade is the daily driver; Adobe for cloud presets)","in":"N assets (<=20)","artifact":"graded set","log":"EDIT_LOG.csv","gate":"os_postproduction_gate","tool":"loop mcp.adobe.image_apply_preset","status":"AMBER","test":"apply 1 preset to the proven DEED asset","proof":"NONE_YET"},
  "social_variations":  {"job":"one hero -> multi-aspect set (1:1/4:5/9:16)","vs_local":"complement os_adobe_reframe (local export specs) ","in":"1 asset + aspects","artifact":"aspect set","log":"EDIT_LOG.csv","gate":"os_postproduction_gate","tool":"mcp.adobe.crop_resize x N","status":"ACTIVE","test":"crop DEED to 4:5","proof":"postproduction crop DEED 1:1 (proven)"},
  "design_from_template":{"job":"start a layout from an Express template","vs_local":"complement os_adobe_layout (local owns the editorial kit; Express for speed drafts)","in":"template query + text","artifact":"filled design","log":"EDIT_LOG.csv","gate":"os_doctrine:layout_type","tool":"mcp.adobe.search_design + fill_text","status":"ACTIVE","test":"search_design 'luxury one-sheet' (read) PROVEN 2026-06-05","proof":"3 templates returned (editorial one-sheet query); fill_text write-half untested"},
  "quick_video_cut":    {"job":"AI highlight reel from clips","vs_local":"complement os_adobe_cut (local owns precise cuts; Adobe for fast auto-reel)","in":"clip assetIds","artifact":"reel mp4","log":"EDIT_LOG.csv","gate":"os_motion_qa","tool":"mcp.adobe.quick_cut","status":"AMBER","test":"needs an uploaded video asset","proof":"NONE_YET"},
  "resize_photo_video": {"job":"resize stills + video to target dims","vs_local":"replace manual resize; complement ffmpeg","in":"asset + dims","artifact":"resized file","log":"EDIT_LOG.csv","gate":"dims check","tool":"mcp.adobe.crop_resize / video_resize","status":"ACTIVE","test":"resize DEED still","proof":"crop_resize proven"},
  "portrait_retouch":   {"job":"select+adjust skin/teeth/eyes selectively","vs_local":"complement Evoto/Lightroom local; IDENTITY edits FORBIDDEN on real people","in":"portrait asset","artifact":"retouched","log":"EDIT_LOG.csv","gate":"os_privacy_gate + identity-edit-ban","tool":"mcp.adobe.select_prompt + adjust","status":"AMBER","test":"select_subject mask on DEED (no identity change)","proof":"NONE_YET"},
  "subject_aware_crop": {"job":"crop keeping subject framed","vs_local":"complement os_adobe_reframe","in":"asset + aspect","artifact":"cropped","log":"EDIT_LOG.csv","gate":"os_postproduction_gate","tool":"mcp.adobe.crop_resize","status":"ACTIVE","test":"done on DEED","proof":"DEED 1:1 (proven)"},
  "remove_background":  {"job":"cutout for mockups/composite","vs_local":"complement os_adobe_composite","in":"asset","artifact":"transparent PNG","log":"EDIT_LOG.csv","gate":"os_postproduction_gate","tool":"mcp.adobe.remove_bg","status":"AMBER","test":"remove_bg on DEED via cloud handshake","proof":"NONE_YET"},
  "generative_expand":  {"job":"outpaint/extend canvas","vs_local":"no local equivalent (only Adobe)","in":"asset + direction","artifact":"expanded","log":"EDIT_LOG.csv","gate":"os_postproduction_gate + generative-approval","tool":"mcp.adobe.generative_expand","status":"AMBER","test":"expand DEED by 10% (spends generative)","proof":"NONE_YET","approval":"generative"},
  "fill_cleanup":       {"job":"fill a selected area","vs_local":"complement os_adobe_composite cleanup; object-removal NOT available (Photoshop/Firefly)","in":"asset + mask","artifact":"filled","log":"EDIT_LOG.csv","gate":"os_postproduction_gate","tool":"mcp.adobe.image_fill_area","status":"AMBER","test":"fill a small mask on DEED","proof":"NONE_YET"},
  "layout_render":      {"job":"InDesign layout -> PDF/PNG","vs_local":"complement os_adobe_layout (local renders PNG via Pillow; Adobe for true InDesign)","in":"layout doc","artifact":"PDF/PNG","log":"EDIT_LOG.csv","gate":"os_doctrine:layout_type","tool":"mcp.adobe.render_layout","status":"AMBER","test":"render a 1-page sample","proof":"NONE_YET"},
  "vector_render":      {"job":"vectorize raster + export Illustrator","vs_local":"no local equivalent","in":"raster/AI file","artifact":"SVG/PNG","log":"EDIT_LOG.csv","gate":"taste","tool":"mcp.adobe.image_vectorize / document_render_vector","status":"AMBER","test":"vectorize a glyph from DEED","proof":"NONE_YET"},
  "pdf_export":         {"job":"PDF convert/merge","vs_local":"complement local Pillow PDF","in":"images/doc","artifact":"PDF","log":"EDIT_LOG.csv","gate":"none","tool":"mcp.adobe.document_convert_pdf / merge_layout","status":"AMBER","test":"merge a 2-row CSV layout","proof":"local Pillow PDF proven; Adobe path untested"},
  "video_resize_only":  {"job":"change video dimensions only","vs_local":"complement ffmpeg/os_adobe_cut","in":"video assetId + dims","artifact":"resized mp4","log":"EDIT_LOG.csv","gate":"os_motion_qa","tool":"mcp.adobe.video_resize","status":"AMBER","test":"needs uploaded video","proof":"NONE_YET"},
  "motion_title_support":{"job":"titles/motion graphics","vs_local":"AE local (aerender) is primary; Adobe MCP has no title tool","in":".aep or text","artifact":"title render","log":"EDIT_LOG.csv","gate":"os_motion_qa","tool":"local.aerender","status":"AMBER","test":"aerender a 1-frame title comp (needs .aep)","proof":"aerender binary proven; no comp yet"},
  "asset_upload_preview":{"job":"get assets into Adobe storage + preview","vs_local":"the enabling handshake (os_adobe_cloud)","in":"local file","artifact":"presignedAssetUrl + preview","log":"os_adobe_cloud stdout","gate":"none","tool":"os_adobe_cloud + asset_initialize/finalize_file_upload","status":"ACTIVE","test":"prep+put+finalize DEED","proof":"DEED upload handshake proven"},
  "media_enhance":      {"job":"speech enhance + media summarize","vs_local":"no local equivalent","in":"audio/video assetId","artifact":"enhanced/summary","log":"EDIT_LOG.csv","gate":"taste","tool":"mcp.adobe.media_enhance_speech / media_summarize","status":"AMBER","test":"summarize a short uploaded clip","proof":"NONE_YET"},
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
        "approval":["public-if-deployed"],"log":"proofcell/form/RESPONSES.csv","validation":"os.form_score","fallback":"manual tally","status":"AMBER","exec":"local","proof":"proofcell/form/","gap":"not deployed (held)","doctrine":["trust_sales","decision_judgment","safety_identity"],"refuses":"not deployed; no public form/posting; no scale before real signal"},
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
        "approval":[],"log":"launch_check log","validation":"deterministic checks","fallback":"manual checklist","status":"ACTIVE","exec":"local","proof":"built this sprint","doctrine":["safety_identity","decision_judgment"],"refuses":"readiness report only; does not authorize any public/launch action"},
    "build_world_3d":{"toolchain":["blender.gated","blender.native"],"inputs":["environment spec (1 of 7 rotation)"],"outputs":["test scene + rendered frame in sandbox"],
        "approval":["sandbox-only"],"log":"blender_sandbox/BLENDER_GATE_LOG.csv","validation":"os_blender_gate + os_world","fallback":"Higgsfield/Seedream plate","status":"ACTIVE","exec":"agent","proof":"blender_sandbox/renders/ (post-restart proof)","gate_note":"native runs ungated -> gate FIRST, sandbox ONLY"},
    "build_private_demo":{"toolchain":["os.campaign","os.adobe_layout","blender.gated","mcp.higgsfield.image"],"inputs":["locked hero + world"],"outputs":["private demo package (no public host)"],
        "approval":["spend-if-generation"],"log":"postproduction/<demo>/10_logs/EDIT_LOG.csv","validation":"os.postproduction_gate + os_privacy_gate","fallback":"static PNG board","status":"AMBER","exec":"agent","proof":"MAX_CAPABILITY_001","gap":"real responsive HTML host held; web-artifacts is HANDOFF","doctrine":["trust_sales","status_culture","safety_identity"],"refuses":"no public host; static package only; no overclaim; no real-client send without go"},
    "run_max_sprint":{"toolchain":["os.campaign","mcp.higgsfield.image","os.adobe_grade","os.adobe_layout"],"inputs":["sprint goal"],"outputs":["max-depth package across modules"],
        "approval":["spend"],"log":"SPEND_LEDGER.csv + EDIT_LOG.csv","validation":"os.postproduction_gate + os_doctrine gate_run","fallback":"per-module manual","status":"ACTIVE","exec":"agent","proof":"campaign_house build"},
    "absorb_new_tool":{"toolchain":["os.tool_registry","os.tool_test"],"inputs":["new tool name + smallest test"],"outputs":["registry row with honest status + route"],
        "approval":[],"log":"OS_TOOL_AND_SKILL_ABSORPTION_BACKLOG.md","validation":"capability_proof_bar (route+artifact+log+gate+repeat)","fallback":"mark AMBER + handoff","status":"ACTIVE","exec":"agent","proof":"this integration pass","doctrine":["automation_toolchain","self_optimization","safety_identity"],"refuses":"will not mark a tool ACTIVE without route+artifact+log+gate+repeat"},
    "create_client_room":{"toolchain":["os.adobe_layout","mcp.gdrive","mcp.notion"],"inputs":["client + assets"],"outputs":["private delivery room (Drive folder + Notion record)"],
        "approval":["storage-write"],"log":"EDIT_LOG.csv","validation":"os_privacy_gate","fallback":"Pixieset (sniped-pixieset-gallery)","status":"AMBER","exec":"agent","proof":"NONE_YET","gap":"no client room built yet"},
    "certify_docs":{"toolchain":["os.certify","os.segment_ledger"],"inputs":["source doc/class"],"outputs":["certified ledger row"],
        "approval":[],"log":"OS_CERTIFICATION_LEDGER.csv","validation":"os_completion_verify (got==total)","fallback":"mark provisional","status":"ACTIVE","exec":"local","proof":"start-here 98/98 certified","doctrine":["self_optimization","decision_judgment"],"refuses":"will not call a source certified unless got==total; pending OCR/read stays pending"},
    # ---- JUDGMENT / DECISION / REVIEW ROUTES (2026-06-05) , read-only, emit a verdict, never silent fallback ----
    "judge_visual_quality":{"doctrine":["visual_grade","decision_judgment","safety_identity"],
        "toolchain":["os.vision_gate"],"inputs":["image/asset path or description"],
        "outputs":["verdict: EXCELLENT / TEMPLATE-LOOKING / REJECT + reasons against the rubric"],
        "approval":[],"log":"vision_gate log","validation":"os_vision_gate (beat-source + one-color + restraint rubric)","fallback":"model rubric read",
        "status":"ACTIVE","exec":"agent","proof":"os_vision_gate built","confidence":"CERTIFIED (visual_direction_luxury + photo_theory)",
        "refuses":"will not call a processed/template frame excellent; strongest != most processed",
        "stop_and_ask":"if the asset is a real person's identity edit, stop , identity edits are forbidden on deliverables"},
    "choose_tool_stack":{"doctrine":["automation_toolchain","decision_judgment","safety_identity"],
        "toolchain":["os.tool_registry"],"inputs":["the job (e.g. cinematic campaign) + constraints"],
        "outputs":["ranked tool stack from ACTIVE tools only + the gaps + handoffs"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"capability_proof_bar (only ACTIVE tools recommended)","fallback":"registry dashboard read",
        "status":"ACTIVE","exec":"agent","proof":"registry is source of truth","confidence":"CERTIFIED (connected_toolchain_default)",
        "refuses":"will not recommend an AMBER/RED tool as if ACTIVE; names the gap instead",
        "stop_and_ask":"if the best stack needs spend or an install, stop and ask before recommending it as the plan"},
    "evaluate_legal_risk":{"doctrine":["safety_identity","decision_judgment","trust_sales"],
        "toolchain":["os.privacy_gate"],"inputs":["the asset/plan/launch + context"],
        "outputs":["risk read: identity/employer/IP/privacy flags + reversibility + what needs a lawyer"],
        "approval":[],"log":"privacy_gate log","validation":"os_privacy_gate + legal_review_needed flag","fallback":"checklist",
        "status":"ACTIVE","exec":"agent","proof":"os_privacy_gate built","confidence":"CERTIFIED (payment_follows_proof + possibility_engine)",
        "refuses":"NOT legal advice; will not finalize anything legal; flags only",
        "stop_and_ask":"ALWAYS stop and route to operator + lawyer for any binding legal step; never auto-finalize"},
    "decide_engine_stack":{"doctrine":["decision_judgment","automation_toolchain","world_character"],
        "toolchain":["os.tool_registry"],"inputs":["the goal (game/film/3d) + ceiling + constraints"],
        "outputs":["engine recommendation (Blender vs Godot vs Unreal vs Unity) + why + proof bar"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"reads engine.* live status; honest RED","fallback":"OS_GAME_PIPELINE_DECISION.md",
        "status":"ACTIVE","exec":"agent","proof":"OS_GAME_PIPELINE_DECISION.md","confidence":"MIXED (decision_judgment certified; engine data current)",
        "refuses":"will not claim any engine ACTIVE; engines are RED until a playable/proof artifact exists",
        "stop_and_ask":"if the recommendation is to INSTALL an engine, stop and ask for explicit approval first"},
    "review_client_readiness":{"doctrine":["trust_sales","safety_identity","layout_type"],
        "toolchain":["os.postproduction_gate","os.privacy_gate"],"inputs":["the package/deliverable"],
        "outputs":["readiness verdict: SHIP / FIX / HOLD + the hardest-to-say-no gaps + privacy flags"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"os.postproduction_gate + os_privacy_gate + hardest_to_say_no rubric","fallback":"manual review",
        "status":"ACTIVE","exec":"agent","proof":"postproduction gate built","confidence":"CERTIFIED (hardest_to_say_no + hospitality)",
        "refuses":"will not pass a package showing internal scaffolding, overclaim, or an identity leak",
        "stop_and_ask":"if it reads SHIP, still stop , a send to a real client needs explicit operator go"},
    "critique_world":{"doctrine":["world_character","narrative_canon","decision_judgment","visual_grade"],
        "toolchain":["os.world","os.vision_gate"],"inputs":["the world/campaign concept + assets"],
        "outputs":["weakness report: mark/tension/lineage/faceless-safety gaps + concrete fixes"],
        "approval":[],"log":"world log","validation":"os_world rubric (ownable mark, tension, lineage, faceless-safe)","fallback":"model rubric",
        "status":"ACTIVE","exec":"agent","proof":"os_world built","confidence":"CERTIFIED (lineage + scene_density)",
        "refuses":"will not bless a generic/tourist world; names what is weak plainly",
        "stop_and_ask":"none , this is internal critique; surface findings, do not act on them without a go"},
    # ---- EXPANDED ACTION ROUTES (2026-06-05) , dedicated routes so the fused brain can ACT ----
    "build_film_pipeline":{"doctrine":["world_character","narrative_canon","visual_grade","motion","safety_identity"],
        "toolchain":["os.crs","os.world","mcp.higgsfield.image","mcp.higgsfield.video","blender.gated","hyperframes","local.aerender","os.adobe_cut"],
        "inputs":["concept/logline","character + world spec"],"outputs":["shot list","generated stills","motion clips","titled + finished trailer package"],
        "approval":["spend"],"log":"campaign_house/<film>/10_logs/EDIT_LOG.csv","validation":"os.motion_qa + os.vision_gate + face/continuity","fallback":"still-based teaser (os.adobe_teaser)",
        "status":"AMBER","exec":"agent","proof":"campaign_house axis_meridian_motion_001","gap":"sound/score is HANDOFF; sustained multi-shot continuity unproven",
        "refuses":"will not claim a finished scored film or guaranteed multi-shot continuity; no sound generation; no public release"},
    "build_game_pipeline":{"doctrine":["world_character","narrative_canon","decision_judgment","automation_toolchain","safety_identity"],
        "toolchain":["os.crs","os.world","blender.gated","engine.godot"],
        "inputs":["game concept","world + character system","core loop spec"],"outputs":["world/character assets (Blender)","design doc","first-playable plan"],
        "approval":["install-engine (explicit)"],"log":"game/<title>/10_logs/BUILD_LOG.csv","validation":"playable-build proof gate","fallback":"asset + design-doc only (no runtime)",
        "status":"RED","exec":"agent","proof":"NONE","gap":"no engine installed; runtime RED",
        "refuses":"GAMES ARE NOT ACTIVE. Will not claim a playable game. Blender provides assets/pre-render only; engine runtime RED until a playable build exists. No engine install without explicit approval"},
    "build_content_engine":{"doctrine":["distribution_hook","automation_toolchain","copy","safety_identity"],
        "toolchain":["os.campaign","mcp.higgsfield.image","os.adobe_layout","hyperframes"],
        "inputs":["hero asset/world","cadence + platform"],"outputs":["repeatable format kit","batch of posts (drafted, not posted)","clip-survival apparatus"],
        "approval":["spend-if-generation"],"log":"postproduction/<engine>/10_logs/EDIT_LOG.csv","validation":"os.postproduction_gate + os_doctrine:distribution_hook","fallback":"single hero + manual cadence",
        "status":"ACTIVE","exec":"agent","proof":"campaign engine built",
        "refuses":"drafts only; no posting/scheduling to live platforms without explicit go"},
    "build_money_move":{"doctrine":["pricing_offer","leverage_ownership","decision_judgment","trust_sales","safety_identity"],
        "toolchain":["os.money_path"],"inputs":["current assets/offers/pipeline"],"outputs":["ranked next money move + reversibility + kill criteria"],
        "approval":[],"log":"money_path log","validation":"deterministic money-path rubric","fallback":"manual decision memo",
        "status":"ACTIVE","exec":"local","proof":"os_money_path built",
        "refuses":"no payment setup, no pricing published, no irreversible commitment; recommendation only"},
    "build_client_pitch":{"doctrine":["trust_sales","strategy_war","pricing_offer","status_culture","safety_identity"],
        "toolchain":["os.adobe_layout","local.pillow"],"inputs":["client + diagnosis","assets"],"outputs":["board + one-sheet -> PDF pitch (private)"],
        "approval":[],"log":"EDIT_LOG.csv","validation":"os_privacy_gate + hardest-to-say-no rubric","fallback":"mcp.adobe.render_layout",
        "status":"AMBER","exec":"local","proof":"MAX_CAPABILITY_001 pitch board","gap":"multi-page deck not templated",
        "refuses":"no overclaim, no internal scaffolding shown, no send to a real client without explicit go"},
    "build_motion_trailer":{"doctrine":["motion","narrative_canon","visual_grade","safety_identity"],
        "toolchain":["mcp.higgsfield.video","hyperframes","local.aerender","os.adobe_cut"],
        "inputs":["hero stills or world","beat list"],"outputs":["titled motion trailer (cut + caption-safe)"],
        "approval":["spend"],"log":"campaign_house/<t>/10_logs/EDIT_LOG.csv","validation":"os.motion_qa","fallback":"still-based os.adobe_teaser",
        "status":"ACTIVE","exec":"agent","proof":"axis_motion_v1.mp4",
        "refuses":"no sound/score generation; a one-shot is a teaser not a trailer; no public release"},
    "build_product_drop":{"doctrine":["pricing_offer","status_culture","leverage_ownership","safety_identity"],
        "toolchain":["os.adobe_composite","blender.gated","os.name_gate"],"inputs":["edition concept","numbered spec"],"outputs":["drop mockups + print spec (validated before any run)"],
        "approval":["validation-before-manufacture"],"log":"EDIT_LOG.csv","validation":"validation_before_manufacture + os_name_gate","fallback":"digital-only edition",
        "status":"AMBER","exec":"agent","proof":"NONE_YET","gap":"no drop validated yet",
        "refuses":"no manufacture before demand proof; no payment/checkout; no public store"},
}

def main():
    ap = argparse.ArgumentParser(prog="os_tool_registry.py"); sub = ap.add_subparsers(dest="cmd")
    t = sub.add_parser("tools"); t.add_argument("--status", default="")
    sub.add_parser("routes"); r = sub.add_parser("route"); r.add_argument("route_id")
    sub.add_parser("dashboard"); sub.add_parser("json"); sub.add_parser("adobe")
    a = ap.parse_args()
    if a.cmd == "tools":
        for tid, t in TOOLS.items():
            if a.status and t["status"] != a.status: continue
            print(f"  [{t['status']:6s}] {tid:28s} {t['kind']:6s} {t['note']}")
    elif a.cmd == "routes":
        for rid, r in ROUTES.items(): print(f"  [{r['status']:6s}] {rid:28s} -> {' + '.join(r['toolchain'])}")
    elif a.cmd == "route":
        print(json.dumps(ROUTES.get(a.route_id, {"error": "unknown route"}), indent=2))
    elif a.cmd == "adobe":
        from collections import Counter
        ac = Counter(c["status"] for c in ADOBE_CAPABILITIES.values())
        print(f"ADOBE CAPABILITIES: {ac['ACTIVE']} ACTIVE / {ac['AMBER']} AMBER / {ac['RED']} RED  (of {len(ADOBE_CAPABILITIES)})")
        for cid, c in ADOBE_CAPABILITIES.items():
            print(f"  [{c['status']:6s}] {cid:22s} job:{c['job']}")
            print(f"           tool:{c['tool']} | gate:{c['gate']} | test:{c['test']} | proof:{c['proof']}")
    elif a.cmd == "dashboard":
        from collections import Counter
        c = Counter(t["status"] for t in TOOLS.values()); rc = Counter(r["status"] for r in ROUTES.values())
        ac = Counter(x["status"] for x in ADOBE_CAPABILITIES.values())
        print(f"TOOLS: {c['ACTIVE']} ACTIVE / {c['AMBER']} AMBER / {c['RED']} RED  (of {len(TOOLS)})")
        print(f"ROUTES: {rc['ACTIVE']} ACTIVE / {rc['AMBER']} AMBER / {rc['RED']} RED  (of {len(ROUTES)})")
        print(f"ADOBE CAPS: {ac['ACTIVE']} ACTIVE / {ac['AMBER']} AMBER / {ac['RED']} RED  (of {len(ADOBE_CAPABILITIES)})")
    elif a.cmd == "json":
        print(json.dumps({"tools": TOOLS, "routes": ROUTES}))
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
