# 01 MASTER CAPABILITY MAP , every layer, all 10 questions

## [RED] Illustrator/InDesign layout layer
1. **Required:** Produce a designed layout deliverable (one-pager, Op Kit, deck slide, drop card, multi-page doc) with type, vector, data-merge, and a render to PDF/PNG from a repeatable template.
2. **Active now:** False  ·  3. **Tested:** not_applicable
4. **Tool/skill:** NONE operationalized. Adobe MCP document_render_layout / document_render_vector / document_merge_data_* and font_recommend / image_vectorize are LIVE as raw tools, but no OS script/skill/template invokes them. No .indd/.ai template or merge-data flow on disk.
5. **Proving artifact:** `NONE`
6. **Breaks if missing:** No repeatable way to lay out the Op Kit one-pager, Pitch deck, Direction Stack book pages, or branded drop cards. Layout deliverables fall back to fully manual GUI work with no template, no data-merge, no version discipline.
7. **Smallest build:** Create one layout template (a JSON/vector spec the Adobe document_render_vector or document_render_layout tool consumes) for a single drop-card or Op Kit one-pager, wrap it in os_layout.py with a data-merge slot (name/role/quote), render one proof PDF/PNG, and log it to 09_exports. One rendered proof = RED to AMBER.
8. **Stay manual (taste):** Type hierarchy, grid/composition, color-on-brand judgment, image selection, and which template a deliverable uses stay manual. Brand restraint (no teal/orange, quiet-luxury) must be human-checked.
9. **Automate:** Data-merge population (name, title, quote, headshot), multi-instance generation (per-person cards), per-format render, and export + version logging from a locked template.
10. **Approval needed:** Operator brand/taste approval on the template design before it is locked, then on first merged batch. Name/brand-availability gate already applies to any new product name printed in a layout.
_flags: missing, needs_adobe_bridge_

## [RED] Premiere/After Effects edit layer
1. **Required:** Assemble/edit a sequence: cut clips on a timeline, trim, sequence, add motion/transitions/titles, render an edited video deliverable (NLE-style edit, not generation).
2. **Active now:** False  ·  3. **Tested:** not_applicable
4. **Tool/skill:** NONE for true edit/sequence. Closest is generative motion: os_generate.py (video path) + os_motion_qa.py + kling-production-sop skill, which PRODUCE and QA-gate clips, they do not edit/sequence them. Adobe MCP video_create_quick_cut / video_resize bridge is LIVE but not wired to any script/skill.
5. **Proving artifact:** `NONE`
6. **Breaks if missing:** No way to turn multiple generated/shot clips into a finished edited piece (multi-shot reel, titled cutdown, platform edit). Motion output stops at single generated clips that pass QA; there is no assembly, no cut, no sequence, no titling step.
7. **Smallest build:** Build os_edit.py that calls the LIVE Adobe video_create_quick_cut to concatenate 2 QA-passed clips from a project's 06_approved into one cutdown, then video_resize per platform, and log it to a new EDIT_LOG row + 09_exports. One logged real cut = the edit layer goes from RED to AMBER.
8. **Stay manual (taste):** Cut rhythm, shot order, in/out points, title timing, music sync, and the final SHIP-or-not creative call stay manual. Motion QA gate already says SHIP means eligible for human taste, not auto-post.
9. **Automate:** Mechanical concat of approved clips, per-platform resize/reframe (9:16 / 4:5 / 1:1 / 16:9), loudness normalize, and writing the export + version log row.
10. **Approval needed:** Explicit spend approval before any generation that feeds the edit (generation is gated to require approval per kling-production-sop). The edit/assemble step itself (no new spend) needs only operator taste approval before posting.
_flags: missing, needs_adobe_bridge, needs_generation_bridge_

## [RED] distribution/content calendar layer
1. **Required:** A repeatable system to plan, queue, and schedule content (IG/LinkedIn/carousel) across a calendar, with platform-calibrated copy attached, so posting cadence is deliberate and trackable rather than ad-hoc.
2. **Active now:** False  ·  3. **Tested:** not_applicable
4. **Tool/skill:** PARTIAL: sniped-caption-writer skill (.claude/skills/sniped-caption-writer/SKILL.md) generates platform-calibrated copy. NO scheduler, NO calendar file, NO posting automation. Higgsfield pipeline's 'schedule' stage is a label with no underlying artifact. Live MCP bridges (Airtable, Notion, Google Calendar, Higgsfield) exist but none are operationalized into an OS content-calendar workflow.
5. **Proving artifact:** `Caption generation only: /Users/sniper/AI-Brain-Refinery/.claude/skills/sniped-caption-writer/SKILL.md (outputs 3 options to chat, no file/queue). Content calendar / scheduler / posting queue artifact: NONE. The only calendar-shaped artifact on disk is KOTS-specific (/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/kingdom_of_the_sun/media/KOTS_GAME_WEEK_CALENDAR.md), not a SNIPED content calendar.`
6. **Breaks if missing:** No posting cadence is enforced or visible. Content gets generated but its release is improvised, untracked, and dependent on operator memory. The proof-loop layer downstream has no upstream feed of what was posted when, so kill/keep/scale signals can never be attributed to a scheduled plan. Distribution (the actual moat per Hit Makers / Blockbuster intel) stays a one-off manual act.
7. **Smallest build:** A single content-calendar CSV template (columns: date, asset_id, channel, caption_ref, status[draft/queued/posted], proof_dashboard_link) under 00_COMMAND_CENTER/, plus a thin os_calendar.py that reads it and prints this-week's queue and flags overdue rows. Optionally back it with the live Airtable/Notion MCP as the editable surface. This closes the gap from zero to a tracked queue without any auto-posting.
8. **Stay manual (taste):** Caption voice, which asset becomes the HERO, sequencing/narrative order of a drop, and the final go/no-go on each post. Taste-governed per v3 LUXURY + caption doctrine.
9. **Automate:** Calendar bookkeeping (what is queued, what is overdue, rolling cadence reminders), status roll-up, and linking each posted asset to its proof dashboard row. Caption first-drafts can be auto-generated then human-edited.
10. **Approval needed:** Operator must approve each post before it goes live (BJ sets launch timing per proof_over_packaging doctrine). Any auto-posting to IG/LinkedIn is blocked_account_manual: it touches BJ's personal accounts and must stay human-triggered. No auto-publish without explicit per-channel sign-off.
_flags: missing, needs_automation, blocked_account_manual_

## [RED] monetization/payment layer
1. **Required:** A repeatable way to actually collect money: a payment link / invoice / checkout that turns a verbal yes (or a print/method buyer) into cleared funds, with the legitimate-link-now doctrine (Stripe/PayPal/Square/personal link) so payment follows proof and never blocks it, plus tracking of revenue in.
2. **Active now:** False  ·  3. **Tested:** untested
4. **Tool/skill:** No payment skill, no Stripe/PayPal/Square/checkout/invoice-generator script anywhere (verified by grep across 00_COMMAND_CENTER/scripts and skills). PROPOSAL_AND_INVOICE_PLAYBOOK.md is a doc only. os_cost.py / os_usage_ledger.py track SPEND out (credits), not revenue in. The proof-cell form collects emails, not payments.
5. **Proving artifact:** `NONE (closest artifacts: /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/PROPOSAL_AND_INVOICE_PLAYBOOK.md is a playbook doc, not a runnable payment system; /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/RESPONSES.csv holds a header row only, zero responses, and os_form_score.py has never run since no SCORE.md exists)`
6. **Breaks if missing:** There is no path from interest to cleared money. A Green discovery call or a print/method buyer cannot be invoiced or charged through any OS artifact; the entire machine can generate proof and demand but cannot capture revenue, so it cannot close the loop it exists to close.
7. **Smallest build:** Stand up one legitimate payment link in the operator's account (Stripe Payment Link or PayPal/Square link) per the payment-follows-proof doctrine, save the link + terms in a /00_COMMAND_CENTER/payments/ folder with a PAYMENTS_CHECKLIST.md (privacy-safe: not real-name-exposed until entity exists), and add a revenue-in column to a ledger so os_cost-style tracking covers money in, not just credits out. Run os_form_score.py once to remove the never-run gap on the demand side.
8. **Stay manual (taste):** Pricing the client vs the labor, holding the $1,500/$2,500 floor, the verbal-price-before-written move, objection handling, and which buyer gets which tier all stay manual (Enns/Maister judgment). The playbook is the guide; a human prices each deal.
9. **Automate:** Invoice/receipt generation from a template, the deposit-invoice-within-24h reliability trigger, and revenue-in logging to a ledger. Mechanical issuance and tracking can be automated once a human sets the price.
10. **Approval needed:** Operator must create the payment account/link (account-level, the OS will not create accounts) and must approve each price before any invoice or link is sent. Bookkeeping-note + admin-cleanup-after-signal per the certified payment-follows-proof waterfall; do not anchor a real-name entity prematurely.
_flags: missing, known_not_operationalized, blocked_account_manual, needs_human_taste_

## [AMBER] Adobe post-production layer (umbrella: Lightroom/Camera Raw grade, Premiere/AE edit, speech/media enhance, render/merge)
1. **Required:** A repeatable, gated OS workflow that applies a graded look, trims/cuts/sequences video, enhances audio, or renders/merges documents THROUGH the live Adobe bridge, logged to EDIT_LOG with from/to versions, so post-production is a controlled pipeline and not manual app work.
2. **Active now:** False  ·  3. **Tested:** untested
4. **Tool/skill:** Live Adobe MCP bridge exists (image_adjust_*, image_apply_preset, video_create_quick_cut, video_resize, media_enhance_speech, document_render_layout/vector, asset_*) but NO OS script, skill, template, or gate wraps it. The grade/retouch skills that exist (sniped-luxury-edit, sniped-evoto-skin-pass, sniped-capture-to-delivery) are manual desktop-app docs, not bridge-operationalized.
5. **Proving artifact:** `NONE. All EDIT_LOG.csv files are header-only / empty: /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/axis_meridian_motion_001/10_logs/EDIT_LOG.csv (1 line), _live_001, _batch_001, _TEMPLATE all 1 line. No os_*.py and no skill references any Adobe MCP tool in an executable path. No rendered/edited Adobe output asset on disk.`
6. **Breaks if missing:** Every grade, cut, audio-clean, and render stays trapped in manual desktop Lightroom/Premiere/Photoshop work with no logged version trail. The campaign-house EDIT stage is a dead folder: clips ship raw-from-Seedance with no trim/sequence/grade pass, and the 'Adobe bridge is live' claim is a raw tool, not a capability. No repeatability, no audit, no proof an edit ever ran.
7. **Smallest build:** Write os_edit.py that wraps two Adobe MCP calls into one gated, logged workflow: (1) apply the v3 LUXURY look to a still via image_apply_preset/image_adjust_* and (2) trim/resize a clip via video_create_quick_cut + video_resize, each writing a from/to row to EDIT_LOG.csv and the output into 08_edits/. Prove with one logged dry-run on axis_motion_v1.mp4 (resize to 9:16) so EDIT_LOG stops being empty.
8. **Stay manual (taste):** The grade itself (the v3 LUXURY look, restraint, no teal/orange) and the edit rhythm/cut points stay human-directed. Taste sets the target; the bridge only executes the agreed adjustment. Skin/identity retouch decisions stay manual per the edit-register doctrine.
9. **Automate:** Mechanical, repeatable steps: applying the locked base preset, aspect-ratio reframes (9:16/4:5/1:1), batch black/white-point + grain match, speech cleanup on talking clips, and document/card render+merge. These should run through os_edit.py and be EDIT_LOG-stamped.
10. **Approval needed:** Human approval of the target look/cut before the bridge runs, and a review of bridge output before it advances to 06_approved. No auto-grade or auto-cut into an approved asset without taste sign-off.
_flags: known_not_operationalized, needs_adobe_bridge, needs_automation_

## [AMBER] Command router
1. **Required:** Classify any incoming request into exactly one mode (strategy/execution/research/critique/build/writing/design/automation/proof-loop/recovery), pick doctrine + web + MCP/local tool route + cost tier + exit gates, raise legal/employer/identity flags, and emit a one-line routing receipt BEFORE answering, so the OS never mode-mixes, over-anchors, or crowns a lane.
2. **Active now:** True  ·  3. **Tested:** untested
4. **Tool/skill:** Skill os-command-router (SKILL.md) + os_gate_injector.py wired as a UserPromptSubmit hook that injects the mode-to-gate map into context before output; references OS_CAPABILITY_TOOL_ROUTING.md and OS_SELF_OPTIMIZATION_ARCHITECTURE.md (both present on disk).
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/.claude/skills/os-command-router/SKILL.md (hook: /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_gate_injector.py, wired in /Users/sniper/AI-Brain-Refinery/.claude/settings.json)`
6. **Breaks if missing:** Requests get answered in the wrong mode (strategy crowns a lane, execution invents strategy, research ships uncited); wrong tool route; cost runs unbounded; no routing receipt to audit why an answer took the shape it did.
7. **Smallest build:** Add a tiny fixture set of labeled example prompts with expected mode+gates and a checker script, so the router classification is test-proven (not just model-judgment). Optionally log each emitted ROUTE receipt to a CSV for an auditable trail.
8. **Stay manual (taste):** The actual mode call on genuinely ambiguous or multi-mode requests, and the refuse-vs-route decision on Class-A constraints. That judgment is the product; do not hard-code it.
9. **Automate:** Pre-prompt injection of the mode-to-gate map (already automated via the UserPromptSubmit hook) and tool-route lookups against OS_CAPABILITY_TOOL_ROUTING.md.
10. **Approval needed:** NONE for routing itself. Operator approval before any route that triggers spend (Higgsfield/Adobe generation) or any employer-adjacent/identity-exposing output the router flags.
_flags: built_untested, needs_human_taste_

## [AMBER] Lightroom/Camera Raw grade layer
1. **Required:** Apply a locked, repeatable graded look (SNIPED v3 LUXURY EDITORIAL) to a RAW/frame: white balance, tone, HSL restraint, 5-mask AI stack, identity-safe skin handling, producing a consistent SNIPED-authored grade.
2. **Active now:** True  ·  3. **Tested:** untested
4. **Tool/skill:** Skill sniped-luxury-edit (manual operator walk) + locked preset file SNIPED_LOCKED_LOOK_v3_LUXURY.xmp. Adobe MCP image_adjust_* bridge LIVE but not wired.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/.claude/skills/sniped-luxury-edit/SKILL.md (and preset at /Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/_preset_backups/SNIPED_LOCKED_LOOK_v3_LUXURY.xmp)`
6. **Breaks if missing:** Grade drifts frame-to-frame, SNIPED authorship becomes inconsistent, skin/identity rules get violated, output stops being recognizably SNIPED. Without the locked preset the whole look is unreproducible.
7. **Smallest build:** Wrap the .xmp slider values + 5-mask stack into an os_grade.py that drives the LIVE Adobe MCP image_adjust_* tools on a sample frame, log a before/after with a numeric skin-drift check (reuse platform-mastering's measured delta), and store one proven dry-run. That converts the manual skill into a tested automated grade.
8. **Stay manual (taste):** Per-frame deviations (WB judgment on hard skin tones, clipped-highlight recovery, whether a frame is Hero vs Select vs Proof, the final Before/After taste call) stay manual. Authorship lives here.
9. **Automate:** The base preset application, the deterministic parts of the 10-step order (crop ratio, default tone offsets, grain, HSL base), and the repeatable 5-mask AI stack on Heroes 2-N via copy-paste propagation.
10. **Approval needed:** NONE for the manual skill today. Before any automated Adobe-bridge grade ships to a client deliverable: operator taste approval on the first batch, plus the identity-AI guardrail (no AI on client-subject identity).
_flags: built_untested, needs_adobe_bridge, needs_human_taste_

## [AMBER] Photoshop/composite layer (locked subject into generated/shot world)
1. **Required:** Composite a LOCKED, graded subject into a generated or shot plate as if same-camera/same-light, then force it through the 8 COMPOSITE_MASTER_QA gates (two-shadow grounding, relight, edge/cutout-tell, sensor match, artifact reject) with proof crops + a 6-axis scorecard before it is called client-ready, logged on disk.
2. **Active now:** False  ·  3. **Tested:** untested
4. **Tool/skill:** composite-master-qa skill (8-gate manual law) + sniped-hero-composite-ceiling + sniped-hero-composite-lite skills (assembly playbooks) + COMPOSITE_MASTER_QA.md standard. Generation plates come from Higgsfield/Seedream bridge. NO script automates the composite; the QA is a manual Read-the-crops-and-score-by-eye judgment, by design.
5. **Proving artifact:** `PARTIAL/NONE. Standard exists: /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/_standards/COMPOSITE_MASTER_QA.md (7.4KB, 8 gates) and skill /Users/sniper/AI-Brain-Refinery/.claude/skills/composite-master-qa/SKILL.md. But NO assembled composite + scorecard exists on disk: no .tif/.tiff composite, no QA scorecard artifact, no logged composite run. The only hero PNG (axis_hero_v2_marked.png) is a mark-injection output, not a subject-into-plate composite.`
6. **Breaks if missing:** Composites get called 'believable' or 'client-ready' on vibes with no proof crops and no scores, which is exactly the failure mode the standard was written to stop. Without a logged run, the composite capability is a doctrine doc, not a proven workflow: the first real client composite would be untested under fire. Floating shadows, cutout tells, and sensor mismatch ship undetected.
7. **Smallest build:** Run ONE composite end-to-end and write the proof to disk: integrate the locked axis hero into a Brutalist-Monument plate, produce the required 5 proof crops + the 6-axis scorecard (lighting/grounding/edge/color/artifact/brand each /10) and a status line (client-ready/internal/rebuild), saved into the project 08_edits/ + a COMPOSITE_QA_SCORECARD.md. That converts the standard from AMBER to a tested GREEN with a single logged pass.
8. **Stay manual (taste):** All of it that matters: the relight read, whether the two shadows feel anchored, whether the subject 'sits' in the plate, brand-fit (does the world compete with the subject), and the final client-ready call. The standard explicitly requires scoring from pixels via human review, never auto-passing.
9. **Automate:** The mechanical supports only: background removal / subject selection (image_remove_background, image_select_subject), feather/defringe, global grain, black/white-point match, and crop generation for the proof set. Assembly judgment and grounding stay manual; the prep crops and sensor-match math can be bridge-assisted.
10. **Approval needed:** Human (operator) sign-off required before any composite is called client-ready or placed in a deck; the skill refuses 'believable'/'client-ready' without proof crops and the six scores. Locked subject grade may never be altered without explicit override.
_flags: built_untested, needs_human_taste, needs_proof_loop_bridge_

## [AMBER] backups
1. **Required:** Durable, automatic, offsite backup of the OS-text brain (doctrine, skills, manifests, ledgers, scripts) so a disk loss does not erase the system, with giant-file exclusion.
2. **Active now:** True  ·  3. **Tested:** proven_dry_run
4. **Tool/skill:** os_backup.sh (safe-path git add, 25MB giant-file abort, commit/push/status/dry-run modes) scheduled by launchd com.bryce.osbackup.plist at 02:30 daily. Manual git history is live (87 commits).
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_backup.sh`
6. **Breaks if missing:** A laptop loss or repo corruption wipes the entire brain. There is NO offsite copy today: the git remote 'osbackup' is NOT SET (os_backup status confirms), so backups are local-commit only, and the nightly launchd job has never run (no /tmp/os_backup.log exists). The single most exposed layer.
7. **Smallest build:** Two commands: (1) git remote add osbackup <private GitHub/GitLab url>; (2) flip the launchd ProgramArguments to call os_backup.sh with 'push' (it currently runs default 'commit', local only). Then trigger one real run to create /tmp/os_backup.log and confirm offsite push. That moves this to GREEN.
8. **Stay manual (taste):** Choosing the private remote host and confirming nothing sensitive (client PII, employer-conflicted material) is in the safe-path glob before the first push.
9. **Automate:** Nightly commit + push and giant-file guard. Script is built; only the schedule-to-push wiring and remote are missing.
10. **Approval needed:** Operator must approve the offsite destination and a privacy scan of staged paths before the first push (PRIVACY_CHECKLIST discipline applies).
_flags: built_untested, needs_automation, known_not_operationalized_

## [AMBER] dashboard/control-room layer
1. **Required:** A single live control surface that shows current proof-cell status, per-rail signal (A/C counts, 24h/7d), keep/kill/scale verdict, gate pass/fail with confidence labels, and the operator's available next approval choices, updated from the actual RESPONSES.csv/SCORE.md state.
2. **Active now:** False  ·  3. **Tested:** untested
4. **Tool/skill:** Static markdown control docs (OS_OPERATOR_HANDOFF.md, proof_dashboard.md, PROOF_LOOP_DASHBOARD.md per project). No script populates them from data. Notion/Airtable MCP bridges available but NOT wired into a dashboard.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_OPERATOR_HANDOFF.md (real, populated control doc) + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_MAX_DEMO_001/09_PROOF_DASHBOARD/proof_dashboard.md (populated gate panel). NOTE: campaign_house/*/10_logs/PROOF_LOOP_DASHBOARD.md are EMPTY header-only tables.`
6. **Breaks if missing:** No single glanceable instrument panel that ties form signal to verdict to next move. The operator would re-derive state from scattered files each session. The proof-loop dashboards stay empty (header-only) and the keep/kill/scale readout lives only inside SCORE.md, not on a tracked control surface.
7. **Smallest build:** A ~30-line script (os_proof_dashboard.py) that reads RESPONSES.csv + SCORE.md and writes the populated PROOF_LOOP_DASHBOARD.md row(s) (asset, posted?, metric, 24h, 7d, verdict). That converts the empty template tables into a live, regenerated panel and closes the gap between the GREEN scoring layer and the static dashboards. Optionally mirror to Notion/Airtable via the live MCP for a remote control room.
8. **Stay manual (taste):** The interpretation line (is this rail worth a bounded next build?) and writing the next-action recommendation. The handoff doc's Section 11 approval choices should stay human-curated, not auto-generated.
9. **Automate:** Regenerating the dashboard tables from RESPONSES.csv/SCORE.md after every ingest+score run. This is pure data-to-markdown rendering and should be a script, not hand-edited.
10. **Approval needed:** None to build or run the local dashboard generator (reads files the OS already owns, no spend, no account). Approval only needed if mirroring to an external Notion/Airtable workspace that could carry identity.
_flags: known_not_operationalized, needs_automation, needs_proof_loop_bridge_

## [AMBER] landing/form layer
1. **Required:** A private, identity-safe landing page that renders the owned-character hero still + motion loop and captures email plus two interest checkboxes (Rail A method, Rail C print), deployable to a generic host without exposing real name/employer/SNIPED.
2. **Active now:** False  ·  3. **Tested:** proven_dry_run
4. **Tool/skill:** Static HTML form (hand-built) + Netlify/Vercel drop config + Tally rebuild spec. Live bridges available but NOT wired: Netlify MCP, Vercel MCP (mcp__plugin_vercel_vercel__deploy_to_vercel).
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/site/index.html (with real assets site/assets/hero.png 1.27MB + site/assets/loop.mp4 1.95MB, netlify.toml, vercel.json, TALLY_SPEC.md, DEPLOY_NOTE.md)`
6. **Breaks if missing:** No surface to put in front of real people, so the entire proof loop (Rails A and C) has no input. Without a live form the ingestion and dashboard layers have nothing to process. The proof clock never starts.
7. **Smallest build:** Operator pastes ONE real endpoint: either rebuild in Tally per TALLY_SPEC.md (2 min, gives private link) OR replace action="REPLACE_WITH_YOUR_FORM_ENDPOINT" in index.html with a Formspree URL and drop site/ on Netlify/Vercel. The HTML and assets are already done; only the endpoint + host wiring remain. Vercel MCP could automate the deploy step once the operator authorizes a non-real-name team.
8. **Stay manual (taste):** Final name promotion (ACHROMAH is pending, not brand-checked), the hero/loop creative selection, the header copy voice, and the decision of WHICH small warm audience to share with. Identity-exposure judgment stays human.
9. **Automate:** The deploy itself (drop site/ via Vercel/Netlify MCP) and a privacy/voice pre-sweep of the page copy can be automated once the operator picks the account.
10. **Approval needed:** Operator must explicitly authorize: creating/using a hosting or form account (account-bound), promoting the name from pending to real, and the share action. Currently hard-parked at the operator line per OS_OPERATOR_HANDOFF.md Section 5.
_flags: built_untested, blocked_account_manual, needs_human_taste_

## [AMBER] privacy/identity/employer-risk layer
1. **Required:** A repeatable, enforced check that nothing shipped (form, site, hero/clip, hosting account, notification inbox, payment method, distribution channel) exposes the operator's real name, SNIPED brand, employer, or personal accounts, including stripping identifying metadata from media assets, before anything goes public.
2. **Active now:** True  ·  3. **Tested:** untested
4. **Tool/skill:** No skill, no gate script. Two manual markdown checklists: PRIVACY_CHECKLIST.md (page + hosting-account + distribution items) and SHARE_CHECKLIST.md (10-step pre-share walk with a proof-clock start date). The certified synthetic character (no real person) is the structural privacy design. No EXIF/metadata-strip script exists.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/PRIVACY_CHECKLIST.md (+ /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/SHARE_CHECKLIST.md)`
6. **Breaks if missing:** Real-name/employer leak via form-owner field, WHOIS on a custom domain, analytics pixel tied to a personal account, asset metadata, or sharing from a real-name account. For a field-engineer-with-employer this is the highest-consequence layer: an identity/employer-overlap leak is hard to reverse and is the one risk the operator explicitly guards.
7. **Smallest build:** Write os_privacy_gate.py that (1) runs exiftool over any asset folder and flags/strips identifying metadata, (2) greps the built site/form HTML for the banned tokens (real name, 'sniped', employer, personal handles) and refuses on a hit, turning the manual checklist into an enforced gate wired before the SHARE step.
8. **Stay manual (taste):** The account-level confirmations only the human can verify (which inbox, which workspace name, who the small warm audience is, the decision to expose identity at all) must stay manual. The checklist itself says 'identity stays uncrowned until YOU choose.'
9. **Automate:** The mechanical scans: EXIF strip, HTML token grep for real-name/employer/SNIPED, WHOIS/custom-domain detector, and a notification-inbox-is-alias assertion. These are deterministic and should block automatically.
10. **Approval needed:** Operator only. No automated share may fire until the human signs the SHARE_CHECKLIST and logs the proof-clock start date. Hard human gate before any public exposure.
_flags: built_untested, known_not_operationalized, needs_human_taste, blocked_legal_privacy_employer_

## [AMBER] startup/legal document layer
1. **Required:** A repeatable system that stages, generates, and tracks the startup/legal docs a one-person media/IP machine needs (entity-formation decision gate, NDA + IP-assignment gates before sharing owned AI-character IP, trademark/name clearance, Terms of Service + Privacy Policy before any public form, cap-table + financial-model tracking), with templates that exist on disk and a doctrine that keeps entity formation from blocking proof.
2. **Active now:** True  ·  3. **Tested:** untested
4. **Tool/skill:** No skill. Plain markdown + CSV: STARTUP_OPERATING_KIT.md (18-doc staging map), STARTUP_DOC_REGISTRY.csv (trackable register with stage/blocks columns), two stub legal docs. os_name_gate.py exists for the name/trademark side. No generator script.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_MAX_DEMO_001/08_STARTUP_DOCS/STARTUP_OPERATING_KIT.md (+ STARTUP_DOC_REGISTRY.csv, _stub_privacy_policy.md, _stub_terms_of_service.md in same folder)`
6. **Breaks if missing:** Going public (form, site, named brand) without ToS/Privacy/trademark clearance creates legal exposure; sharing the owned AXIS/MERIDIAN AI-character IP without NDA + IP-assignment risks losing ownership of the core asset. Without the staging doctrine, entity-formation anxiety blocks proof (the exact failure mode the OS warns against).
7. **Smallest build:** Move the 4 NOW-set items out of the OS_MAX_DEMO_001 demo sandbox into a live /00_COMMAND_CENTER/legal/ folder, and actually write the two missing template stub files that the kit promises but does not have on disk: _stub_nda.md and _stub_ip_assignment.md. Then have a lawyer review the 4 NOW stubs once.
8. **Stay manual (taste):** All legal review, the entity-vs-no-entity decision, and any signature must stay manual. These are stubs labeled [LEGAL-REVIEW-NEEDED]; taste and a real attorney decide, not the OS.
9. **Automate:** The staging/tracking layer: STARTUP_DOC_REGISTRY.csv could be auto-checked at each launch step (a gate that refuses 'go public' until ToS+Privacy rows are marked done). Cap-table and financial-model fields can auto-populate from OS_COST_LEDGER.csv.
10. **Approval needed:** Operator (Bryce) + a real attorney before any stub is treated as final, before entity formation, and before the IP-assignment/NDA gates are relied on. Nothing here is legal advice.
_flags: built_untested, known_not_operationalized, needs_human_taste, blocked_legal_privacy_employer_

## [GREEN] AI generation layer
1. **Required:** Generate images and video from prompts via a real model, with a spend gate before generation and a download/ingest gate after, so cost is bounded and a failed generation never produces a silent placeholder asset. Must operationalize the live generation bridge (Higgsfield/Nano Banana/Seedance) into a repeatable, logged, gated workflow.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_generate.py (prep / prep-video / ingest / ingest-video / ref-package) wrapping the LIVE Higgsfield MCP bridge (generate_image/generate_video); spend bounded by os_cost_guard.py + OS_COST_LEDGER.csv; prompt-construction skills sniped-seedream-prompt and sniped-higgsfield-pipeline plus the plugin higgsfield-generate skill.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_generate.py (prep/ingest gates with FAILURES.csv + NO-placeholder logic); logged real runs at /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/axis_meridian_motion_001/10_logs/GENERATION_LOG.csv (3 rows: axis_hero_v1.png, axis_hero_v2.png 1.8M real PNG, axis_motion_v1.mp4 1.9M real 18-credit video) and /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/_batch_001/10_logs/GENERATION_LOG.csv (3 var_*.png + 1 FAILED row proving the failure path fires)`
6. **Breaks if missing:** Without the prep spend-gate and ingest download-check the OS would spend credits unbounded and write empty/placeholder assets that silently poison the downstream pipeline (the whole proof loop depends on real assets, not zero-byte stubs). No bounded image/video output = no campaign machine.
7. **Smallest build:** Confirm the assumed Higgsfield video credit rate against live show_plans_and_credits so os_generate.py prep-video stops refusing to estimate (ASSUMED_VIDEO_RATE_CR_PER_SEC is intentionally None today); add a thin os_generate.py 'generate' subcommand that calls the MCP directly so the generate step is logged automatically rather than narrated by Claude between prep and ingest.
8. **Stay manual (taste):** Which generation to approve vs reject (the var_a/b/c selection, the v1-vs-v2 hero call), final prompt phrasing for the luxury-editorial register, and the go/no-go on any video spend. Taste decides the keeper; the script only bounds cost and verifies the download.
9. **Automate:** Cost preflight (prep / prep-video threshold block), the download + size-floor check, FAILURES.csv logging, GENERATION_LOG row writing, and cost-ledger updates. All of this is already automated.
10. **Approval needed:** Explicit operator approval for any credit spend above the prep threshold (default 5cr image, 20cr video). The 18-credit axis_motion_v1 video was the first real video spend and required sign-off; prep-video refuses to even estimate without a confirmed live rate.
_flags: active_tested, needs_human_taste, needs_adobe_bridge_

## [GREEN] OS source/certification layer
1. **Required:** Honest, repeatable certification of the corpus by file class with a token-aware coverage truth (certified vs provisional vs characterized vs pending), so strategy only uses proven sources and 'read_verified' claims are auditable.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_certify.py (classifier + 7 metrics), os_completion_verify.py (gate-8 scope enforcer), os_segment_ledger.py, os_book_coverage.py; backed by OS_ENGAGEMENT_MANIFEST.csv + OS_CERTIFICATION_STANDARD.md; skills os-engagement, os-token-safe-reader.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_certify.py + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_CERTIFICATION_LEDGER.csv`
6. **Breaks if missing:** OS silently treats unread/sampled giants as authoritative; 'read_verified' inflates to a false 86%; strategy cites uncertified sources; the corpus loses its truth layer and every downstream answer becomes ungrounded.
7. **Smallest build:** Add a per-file segment ledger so multi-segment sources can move from provisionally_verified to certified (currently 82% of word-volume is provisional with no segment ledger); wire os_certify.py to fail-loud on dashboard/manifest drift.
8. **Stay manual (taste):** Deciding what a source actually MEANS for SNIPED doctrine, and which conflicts to preserve vs resolve. Distillation quality and lineage judgment stay human.
9. **Automate:** Classification, metric computation, ledger regeneration, mismatch/giant/orphan detection, completion-verify exit codes. Already automated; keep it scheduled after any intake.
10. **Approval needed:** NONE to run (read-only to manifest, writes only the ledger). Operator approval needed before promoting a class proof-rule change in OS_CERTIFICATION_STANDARD.md.
_flags: active_tested_

## [GREEN] Quality gates
1. **Required:** A pass/fail gate set that blocks 'done' on hallucination, old-lane anchoring, premature lane-crowning, identity collapse, legal/employer exposure, unproven completion, stale facts, and runaway cost, so no answer or build ships unverified.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** Skill os-quality-gates (11 gates) + THREE wired enforcers in settings.json: os_gate_injector.py (UserPromptSubmit, injects gates), os_stop_check.py (Stop hook, contradiction/drift warning), os_cost_guard.py (PreToolUse on Workflow); plus os_completion_verify.py as the scripted gate-8 enforcer (exit 0/1 on manifest scope).
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/.claude/skills/os-quality-gates/SKILL.md + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_completion_verify.py + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_stop_check.py (all wired in /Users/sniper/AI-Brain-Refinery/.claude/settings.json)`
6. **Breaks if missing:** The OS claims 'done' on unread scopes, ships uncited strategic claims, crowns a lane without proof, exposes identity/employer, or burns spend with no cost ceiling. The completion-verification gate (gate 8) is the single most load-bearing protection against false 'done'.
7. **Smallest build:** Convert the judgment gates (anti-hallucination, proof-before-crowning, optionality, identity-collapse) from prose into a lightweight self-check the model must emit before 'done', and log recurring gate failures to an error dashboard CSV as the SKILL.md prescribes but no file yet implements.
8. **Stay manual (taste):** The judgment gates themselves: whether a claim is truly cited, whether a lane is being crowned, whether optionality is collapsing. These are taste calls that should stay model/operator-applied, not auto-passed.
9. **Automate:** The mechanical gates are already automated and wired: completion-verify (manifest got==total), cost/runaway guard (PreToolUse on Workflow), and stop-time state-contradiction detection. Keep them as hooks.
10. **Approval needed:** NONE to run the gates. A gate FAIL that the operator chooses to override (e.g. ship despite pending pile) requires explicit operator sign-off and disclosure of the unverified dependency.
_flags: active_tested, needs_human_taste_

## [GREEN] analytics/proof-loop layer
1. **Required:** A repeatable loop that captures real-world signal on shipped assets/offers (form responses, post performance), scores it against pre-set KILL/KEEP/SCALE thresholds, and feeds a verdict so hypotheses are decided by evidence not opinion.
2. **Active now:** True  ·  3. **Tested:** proven_dry_run
4. **Tool/skill:** os_form_ingest.py + os_form_score.py (proofcell form pipeline) + PROOF_LOOP.md threshold spec + campaign-house PROOF_LOOP_DASHBOARD.md templates. The form-signal half is real and runnable. The post-performance/social-analytics half is NOT built (no IG/LinkedIn/Semrush ingestion script).
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/os_form_score.py (ran clean, exit 0, wrote SCORE.md), /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/os_form_ingest.py, /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/PROOF_LOOP.md (KILL/KEEP/SCALE thresholds), /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/RESPONSES.csv (schema, 0 data rows), /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/_batch_001/10_logs/PROOF_LOOP_DASHBOARD.md (filled structure, all 'not-activated until posted').`
6. **Breaks if missing:** Without it, every direction (H1-H6 in PROOF_LOOPS_30_60_90.md) stays an unfalsifiable opinion and the OS crowns lanes on confidence instead of evidence, exactly the failure the doctrine forbids. The scoring engine itself works; what breaks is that it is starving: form is undeployed (0 responses) and no social-analytics feed exists, so the loop scores emptiness.
7. **Smallest build:** Two moves: (1) deploy the proofcell form (one of the 3 ready versions in DEPLOY_NOTE.md) so RESPONSES.csv starts filling and os_form_score produces a real verdict. (2) Add an os_post_signal.py that takes a hand-entered or Semrush/manual-export row (asset_id, 24h, 7d) and writes the kill/keep/scale verdict into the PROOF_LOOP_DASHBOARD.md, closing the post-performance half.
8. **Stay manual (taste):** Reading qualitative intent/fit signal (who responds, buyer-type clustering), and the final kill/keep/scale call on borderline cases. Thresholds are pre-set, but interpreting a small-N early signal is taste-governed (the doctrine explicitly says do not crown a rail on early signal).
9. **Automate:** Response ingestion + dedup (os_form_ingest), counting and threshold-verdict scoring (os_form_score), and dashboard roll-up. These are deterministic and should never be done by hand.
10. **Approval needed:** Form deployment touches BJ's own SaaS account (Tally/Formspree/Netlify) and a privacy/share checklist, so it is operator-gated (blocked_account_manual). No 'validation' may be claimed until the link is actually shared with real people (PROOF_LOOP.md rule). Operator authorizes go-live and the share.
_flags: active_tested, needs_proof_loop_bridge, blocked_account_manual, needs_automation_

## [GREEN] archive/learning loop
1. **Required:** A repeatable loop that captures what was read/decided/shipped, reconciles it against a source-of-truth ledger, surfaces contradictions, and persists session state so the OS compounds learning instead of re-deriving it.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_checkpoint.py (manifest->dashboard reconciler + consistency checks) + OS_ENGAGEMENT_JOURNAL.md (append-only decision-delta log) + session-save skill (snapshots to session_saves/) + OS_ENGAGEMENT_MANIFEST.csv as source of truth. OS_DRYRUN_001.md is a logged pipeline self-test.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_checkpoint.py (ran clean: 1260 sources, 910 read_verified=72.2%, consistency CLEAN), /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_ENGAGEMENT_JOURNAL.md (real dated decision-deltas + reconciled contradictions), /Users/sniper/AI-Brain-Refinery/.claude/skills/session-save/SKILL.md backed by 48 real snapshots in /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/session_saves/, /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_ENGAGEMENT_MANIFEST.csv, /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_DRYRUN_001.md.`
6. **Breaks if missing:** Without it the OS loses continuity between sessions, re-reads sources it already covered, and silently carries contradictions (e.g. the Phase-B trigger conflict the journal caught). Coverage/verification percentages drift from reality, and the operator cannot trust any 'full OS' answer because there is no reconciled ledger behind it.
7. **Smallest build:** Already operational. Marginal hardening: wire os_checkpoint --write into the session-save flow (or a SessionStart/Stop hook) so the dashboard is auto-reconciled at every session boundary instead of being run manually, and append a one-line learning-delta to OS_ENGAGEMENT_JOURNAL.md automatically on save.
8. **Stay manual (taste):** Writing the decision-delta itself (what actually changed, what contradiction matters, which assumption got killed) is judgment work. The journal entries are interpretive and should stay human-authored.
9. **Automate:** Manifest->dashboard reconciliation, consistency/duplicate/empty-status checks, coverage-percentage recompute, and session snapshot scaffolding. These are deterministic (os_checkpoint is explicitly no-token) and should run on a hook, not by hand.
10. **Approval needed:** NONE for read-only reconciliation and snapshots (they only write within 00_COMMAND_CENTER and session_saves/). Operator approval is needed only when a reconciled contradiction demands a real decision (e.g. the Phase-B $2K vs $3K conflict), which the journal correctly routes to the operator rather than auto-resolving.
_flags: active_tested_

## [GREEN] character consistency layer
1. **Required:** Define one fully original (non-celebrity) character with hard identity invariants, gate cross-frame identity so the same face survives multiple outputs, screen for real-person likeness leaks, and lock an approved hero as the reusable reference anchor that future stills/video condition on (instead of regenerating a face from text).
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_crs.py (new/validate/sheet/gate/leakcheck/verifycrop), os_herolock.py (locked-hero registry), os_facematch.py (SSIM proxy + authoritative vision score), os_face.py (cv2 face/eye geometry), os_mark.py (signature mole injection); fronted by the os-face-lock skill.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/characters/char_axis_01/CRS.json (4 hard invariants: eye_color, face_geometry, build, complexion; validates VALID); /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/locked_heroes/axis_v2/HERO.json + OS_LOCKED_HERO_REGISTRY.csv (axis_v2 LOCKED); /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/axis_meridian_motion_001/10_logs/FACE_MATCH_LOG.csv (real PASS at vision 0.97 and QUARANTINE at 0.1 both logged); regression /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/test_crs.py (26 pass/0 fail) and test_facelock.py (15 pass/0 fail)`
6. **Breaks if missing:** Without the CRS hard-invariant gate, the locked-hero registry, and the face-match gate, every generation drifts to a new face and there is no original character that survives a campaign. Identity drift and accidental celebrity-likeness leakage (legal/IP risk) go uncaught. The whole one-character-across-many-outputs premise collapses.
7. **Smallest build:** Install a real face-embedding ONNX model so os_facematch can PASS on cosine similarity automatically instead of always escalating to NEEDS-VISION (today the auto layer can only FAIL, never solely PASS, so a human vision read is required on every match). That single swap is already anticipated in the code comments.
8. **Stay manual (taste):** The authoritative is-it-the-same-person vision identity score (0..1), the character's actual aesthetic identity (face/wardrobe/register design in CRS.json), and approving a hero into LOCKED status. SSIM is only a gross-drift screen; the keeper call is human.
9. **Automate:** Invariant completeness validation, leak-pattern scanning, the SSIM gross-drift screen, side-by-side crop generation, gate-report and FACE_MATCH_LOG writing, and refusal to register a hero whose approved/source asset is missing. Already automated.
10. **Approval needed:** Operator sign-off to promote a candidate to LOCKED hero (os_herolock register), and a human vision score before any face-match can reach PASS. No identity-lock of the brand throne is permitted (capability yes, identity-lock no per the OS guardrail).
_flags: active_tested, needs_human_taste, needs_generation_bridge_

## [GREEN] cost/session control: runaway + concurrency guard
1. **Required:** Hard stop on the proven session-drain failure: block concurrent workflow waves and oversized inline scripts at PreToolUse, fail-open on error, with a lock lifecycle (acquire/release/reap/clear, auto-stale).
2. **Active now:** True  ·  3. **Tested:** tested
4. **Tool/skill:** os_cost_guard.py (PreToolUse hook on Workflow, exit 2 = BLOCK, 480KB script cap, /tmp/os_wf.lock) + os_wave_lock.py (acquire/release/reap/status/clear, 90-min auto-stale).
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_cost_guard.py`
6. **Breaks if missing:** Concurrent waves spawn and drain the session/credits (the exact failure this was built for); a runaway 480KB+ embedded plan slips through. Verified live: a fresh lock makes the guard emit BLOCK exit 2, no-lock passes exit 0.
7. **Smallest build:** None. Minor: wire os_wave_lock.py release into the workflow result-handling path so locks clear on completion rather than relying on the 90-min auto-stale (today release is manual/reap-based).
8. **Stay manual (taste):** When to override a legitimately-stuck lock (os_wave_lock clear) vs wait it out.
9. **Automate:** Concurrency block, size cap, lock set, and stale auto-clear are automated. Release-on-completion is the one gap that should be auto-wired.
10. **Approval needed:** NONE. Override (clear) is operator-only by design.
_flags: active_tested_

## [GREEN] cost/session control: session-state save + cold boot
1. **Required:** Snapshot session state before /clear or context-limit, and a cold-start boot brief that loads only the essentials (mission, cert summary, next action, log tail).
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** session-save skill (writes session_saves/<ts>_<slug>.md) + os_boot.py (cold boot brief) + os_session_start.sh which runs os_checkpoint and prints NEXT_ACTION/STANDING_ORDER.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/.claude/skills/session-save/SKILL.md`
6. **Breaks if missing:** Context blows past 70% with no save point and the session's decisions/in-flight tasks are lost on /clear; cold starts reload too much and waste budget.
7. **Smallest build:** None. The session-save skill is read-only and bounded; boot brief runs at SessionStart.
8. **Stay manual (taste):** Slug/intent framing and which decisions are load-bearing enough to capture stay a human call; operator triggers /clear after review (by design, not auto).
9. **Automate:** Boot brief and checkpoint reconciliation at session start are automated. The save itself is operator-triggered intentionally (taste on when to snapshot).
10. **Approval needed:** NONE. Operator triggers /clear manually after reviewing the save.
_flags: active_tested_

## [GREEN] cost: per-run cost ledger
1. **Required:** Log every generation/production run's estimated vs actual credits and dollars, roll up per project, with a credits-are-not-dollars conversion rate.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_cost.py (rate/log/project/report) writing OS_PRODUCTION_COST.csv; os_usage_ledger.py (start/end/predict/parse/report) writing OS_COST_LEDGER.csv.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/OS_PRODUCTION_COST.csv`
6. **Breaks if missing:** Spend drifts invisibly; no per-project credit rollup; estimate accuracy never improves. Already has 2 real production runs and 2 ledger runs logged with actuals.
7. **Smallest build:** Set the USD/credit rate (.prod_cost_rate is currently absent, so all USD reads UNKNOWN): os_cost.py rate set --usd-per-credit <X>. That alone converts the logged credits into real dollars.
8. **Stay manual (taste):** The credit-to-USD rate and the est_cost guess per run are operator inputs (and /usage cannot be auto-read, so end-of-run totals are pasted in by hand).
9. **Automate:** The logging math, rollups, error-pct, and the /usage parser are automated. Run logging is the only manual step and could be wired into os_generate post-run.
10. **Approval needed:** NONE to log. Setting the conversion rate is an operator decision (it changes every reported dollar figure).
_flags: active_tested, needs_human_taste_

## [GREEN] export/versioning layer
1. **Required:** Take an approved asset to a gated, versioned, platform-correct export with a tracked version history and an audit/voice gate before anything is called shippable.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_production.py (log-export, log-edit with from_version/to_version, log-caption voice-gate, audit, dashboard) + campaign_house 00_-10_ stage dirs incl 09_exports + OS_PRODUCTION_REGISTRY.csv. Skill platform-mastering + standard PLATFORM_MASTERING.md add per-surface export discipline.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_production.py (real exports on disk: /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/_batch_001/09_exports/var_a_4x5.export and var_b/var_c, plus _live_001/09_exports/monolith01_4x5.export)`
6. **Breaks if missing:** No gated, versioned, auditable export path. Assets ship unversioned, the caption voice-gate (em-dash / AI-tell check) and audit-blocker gate stop running, and the proof-loop dashboard never gets populated. Version history (PROMPT_VERSIONS, EDIT_LOG from/to_version) collapses.
7. **Smallest build:** Already active. Gap-closers only: (1) log-export currently writes a tiny .export stub, not a real rendered file, so wire it to the platform-mastering crops + (later) the Adobe export bridge to emit actual platform masters; (2) backfill EDIT_LOG (currently zero rows) so version transitions are actually recorded; (3) advance axis_meridian_motion_001 from awaiting_export by logging its first export.
8. **Stay manual (taste):** Per-platform crop/safe-area decisions, the color-vs-B&W call, and the final phone-proof judgment stay manual (platform-mastering enforces human judgment on a phone). Which version is the keeper is a taste call.
9. **Automate:** The gate chain (audit blocker check, caption voice-gate, version stamping), the per-surface resize/reframe set, writing the .export + caption files, and updating OS_PRODUCTION_REGISTRY + PROOF_LOOP_DASHBOARD.
10. **Approval needed:** NONE to run the export harness (it is gated by design). Operator taste approval is required before an exported master is actually posted, and the proof-loop stays not-activated until the operator confirms posting.
_flags: active_tested, needs_human_taste_

## [GREEN] hooks: stop-check / completion-verification
1. **Required:** A gate that refuses or warns on a false 'done' claim by checking the engagement manifest/dashboard as the arbiter (duplicate paths, empty-status rows, dashboard-vs-manifest verified mismatch).
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_stop_check.py (Stop hook, warn-once mode, exit 2) + os_completion_verify.py (CLI gate, exit 1 on pending in scope).
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_stop_check.py`
6. **Breaks if missing:** The OS claims completion while the manifest still has unread/pending sources, re-introducing the 86%-vs-74.4% inflation failure the OS already burned a doctrine lock on.
7. **Smallest build:** None. Optional: have os_completion_verify.py also run from a hook on explicit 'done'/'shipped' phrases, not only by manual CLI call, so the verify gate is enforced not just available.
8. **Stay manual (taste):** Deciding whether a remaining pending pile (needs_ocr / needs_transcription) legitimately blocks 'done' for a given scope, or is an acceptable separate pile.
9. **Automate:** Manifest reconciliation at stop and the duplicate/empty/mismatch detection. Already automated.
10. **Approval needed:** NONE.
_flags: active_tested_

## [GREEN] motion/video layer
1. **Required:** Generate a short motion clip from an approved locked-hero still (image-to-video), QA it for identity-hold + world-continuity + motion artifacts, gate it behind a cost preflight, and log the run with credits, asset, scores, and per-frame face-match before any human-taste approval.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** os_generate.py (prep-video/ingest-video) + os_motion_ready.py (pre-spend readiness gate) + os_motion_qa.py (3-stack QA gate reusing os_crs + os_world) + os_facematch.py (per-frame match to locked hero) + os_herolock.py (reference anchor) + Higgsfield MCP generate_video (Seedance 2.0) as the generation bridge.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/axis_meridian_motion_001/06_approved/axis_motion_v1.mp4 (real 1.9MB / 97 frames / 4.08s) + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/axis_meridian_motion_001/10_logs/MOTION_QA_REPORT.json (verdict SHIP, score 0.929) + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/axis_meridian_motion_001/10_logs/MOTION_FACE_MATCH_LOG.csv (3 frames PASS, vision 0.97/0.95/0.88) + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/axis_meridian_motion_001/10_logs/GENERATION_LOG.csv (Vmotion1 seedance_2_0 18cr downloaded)`
6. **Breaks if missing:** Without this, video output is ungated: identity can drift frame-to-frame, world can break continuity, credits get spent with no preflight cap, and there is no logged proof a clip ever beat the static hero. The whole motion lane reverts to ad-hoc Higgsfield prompts with no QA receipt.
7. **Smallest build:** Replace hand-declared frame observations in motion_clip_obs.json with an automated frame-sampler + vision extractor (ffmpeg already present: extract N frames, Read each, write observed JSON) so os_motion_qa.py judges real pixels, not a manually filled rubric. Add a confirmed Higgsfield cr/sec rate to os_generate.py (currently ASSUMED_VIDEO_RATE_CR_PER_SEC=None) so prep-video stops refusing to estimate.
8. **Stay manual (taste):** Final SHIP-to-post decision (does the clip actually feel like AXIS in register, does it beat the still as a moving asset). The 3 soft rubric items (physics/register/beat_source) and the go/no-go to post stay human. SHIP from the gate means eligible for taste, never auto-post.
9. **Automate:** Frame sampling + per-frame identity scoring, world-continuity check, motion-artifact rubric scoring, cost preflight, FAILURES.csv on bad download, and the generation/face-match/QA logging. All already scripted; only the vision-fill of frame obs is still manual.
10. **Approval needed:** Explicit human approval before any video credit spend (os_generate.py prep-video is no-spend preflight only; the 18cr Seedance run was operator-approved). SHIP verdict requires human taste sign-off before posting.
_flags: active_tested, needs_human_taste, needs_generation_bridge_

## [GREEN] reliability/hooks
1. **Required:** Deterministic lifecycle hooks (SessionStart load, per-prompt gate injection, Stop-time contradiction check) wired into the Claude Code harness so state-loading and quality gates fire automatically, not from memory.
2. **Active now:** True  ·  3. **Tested:** logged_real_run
4. **Tool/skill:** Claude Code hooks in .claude/settings.json: SessionStart -> os_session_start.sh; UserPromptSubmit -> os_gate_injector.py; Stop -> os_stop_check.py; PreToolUse(Workflow) -> os_cost_guard.py.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/.claude/settings.json`
6. **Breaks if missing:** Session starts with no state loaded (NEXT_ACTION/STANDING_ORDER/manifest unread), gates depend on the model remembering them, and 'done' claims ship while the dashboard/manifest are out of sync. The OS reverts to ad-hoc behavior.
7. **Smallest build:** None for existence. Hardening: add a hook self-test (assert all 4 referenced scripts exist + exit-code contract) run by os_backup or a daily check so a renamed/moved script is caught before a live session silently loses a hook.
8. **Stay manual (taste):** Which gates apply to a given request, and whether a flagged contradiction is real corruption vs an acceptable pending pile, stays a judgment call.
9. **Automate:** State load at session start, gate-map injection per prompt, contradiction warning at stop. All already automated via the hook chain.
10. **Approval needed:** NONE to run. Changing settings.json hook wiring should be operator-approved since a bad command bricks every session start.
_flags: active_tested_

## [GREEN] response ingestion/scoring layer
1. **Required:** Normalize a Tally OR Formspree CSV export into a deduped canonical RESPONSES.csv, then score it into per-rail counts (A method, C print, both, by source, intent keywords) and emit a keep/kill/scale verdict per rail against fixed thresholds.
2. **Active now:** True  ·  3. **Tested:** proven_dry_run
4. **Tool/skill:** os_form_ingest.py (column heuristics + email dedup) and os_form_score.py (counts + verdict, writes SCORE.md). Plain Python 3, no external deps.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/os_form_ingest.py + /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/proofcell/form/os_form_score.py (RESPONSES.csv exists as empty header-only template; SCORE.md generated on dry-run then template restored)`
6. **Breaks if missing:** No structured read of incoming signal. Responses would sit as a raw CSV with no dedup, no A/C/both split, no source attribution, no verdict, so keep/kill/scale decisions would be eyeballed and the rail-crowning discipline collapses.
7. **Smallest build:** None for the code itself. The only gap is INPUT: it has never run on a real export (RESPONSES.csv has 0 real rows). To close, feed it the first real Tally/Formspree CSV once the form is live. Optional hardening: a tiny wrapper that auto-detects export deltas so re-ingest is idempotent (dedup already handles this).
8. **Stay manual (taste):** Reading the intent free-text for buyer-type fit and deciding whether a KEEP signal is genuine vs noise. The qualitative fit read should stay human; the script deliberately refuses to crown a rail.
9. **Automate:** The ingest + score run itself (already a one-line invocation each). Could be wired to auto-run when a new CSV lands in a watched folder.
10. **Approval needed:** None to run locally on a CSV the operator provides. It only acts on a file the operator exports and hands it; no account, no network, no spend.
_flags: active_tested, needs_proof_loop_bridge_

## [GREEN] skill lifecycle layer
1. **Required:** A skill activation substrate that scaffolds, lints, installs, and registers skills against a strict 6-point activation contract (installed, discoverable, trigger, inputs/outputs, tests, invokable), with a test suite and a single source-of-truth registry, so no fake capability is counted ACTIVE.
2. **Active now:** True  ·  3. **Tested:** tested
4. **Tool/skill:** os_skill.py (lint/new/install/registry/audit) + test_skill_substrate.py (11 pass/0 fail) -> OS_SKILL_REGISTRY.csv + OS_SKILL_DASHBOARD.md.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/os_skill.py`
6. **Breaks if missing:** Skills get marked ACTIVE on vibes; the OS hallucinates capabilities it does not have. Verified live: audit shows 5 ACTIVE / 68 INSTALLED_INCOMPLETE / 0 DRAFTED / 0 MALFORMED across 73 tracked, registry CSV matches, all 11 substrate tests pass, scaffold-new lints born-compliant.
7. **Smallest build:** None for the substrate. The real backlog: 68 INSTALLED_INCOMPLETE skills need ## Inputs / ## Outputs / a real ## Test each to reach ACTIVE. That is content work per skill, not infra. Each upgrade ships its own test (the contract enforces it).
8. **Stay manual (taste):** Whether a skill's trigger description and test cases actually capture the OS doctrine correctly is human judgment; the linter only checks structure, not whether the skill is GOOD.
9. **Automate:** Linting, status tiering, registry/dashboard generation, and the structural contract check are fully automated and test-backed. Run os_skill.py registry after any skill change.
10. **Approval needed:** NONE to lint/scaffold/register. install --force (overwrites an installed skill) should be operator-confirmed since it deletes the existing copy.
_flags: active_tested, needs_human_taste_

## [GREEN] world bible layer
1. **Required:** Lock one world's visual rules (environments, materials, light logic, color system with palette + forbidden hues, camera language, forbidden elements, recurring motifs, SREF slots, continuity rules) as a structured, machine-gateable bible, then quarantine any proposed scene that breaks a rule, so every output is continuous instead of random.
2. **Active now:** True  ·  3. **Tested:** tested
4. **Tool/skill:** os_world.py (new/validate/continuity/show), fronted by the os-world-bible skill; the continuity core (evaluate_scene) is reused by the motion-QA / motion-readiness gate.
5. **Proving artifact:** `/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/campaign_house/worlds/world_meridian_01/WORLD.json (all 9 categories filled: 3 environments from the locked rotation, locked palette_hex, explicit forbidden_hues + 10 forbidden_elements, 6 continuity rules; validates VALID); regression /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/scripts/test_world.py (6 pass/0 fail, incl. forbidden-element and off-rotation-environment quarantine cases)`
6. **Breaks if missing:** Without the completeness gate and the per-scene continuity gate, generations wander off-palette, off-environment, and into forbidden elements (logos, teal-orange, crowds), and there is no machine check that a scene belongs to the world. Continuity across a chapter collapses and the editorial-restraint moat is unenforceable.
7. **Smallest build:** Wire os_world.py continuity into os_generate.py prep so a scene JSON is auto-checked at prep time (the gate currently exists and is tested but is invoked as a separate manual step rather than inline in the generation preflight). Also populate the 3 sref_style_slots which are still TBD-manual-pull placeholders.
8. **Stay manual (taste):** Authoring the world's actual aesthetic (the MERIDIAN-HOUSE premise, which environments from the 7-rotation, the palette choices, the Meisel/Roversi reference lane) and the hand-pull of the SREF style references. The script enforces rules; a human writes them.
9. **Automate:** 9-category completeness validation, palette/forbidden-hue enforcement, and the per-scene continuity quarantine (forbidden element present or environment off-rotation = hard fail; off-palette hue = advisory). Already automated and shared into the motion gate.
10. **Approval needed:** Operator approval to lock the world bible and to override any continuity quarantine (a quarantined scene should not proceed to spend without an explicit human override). No public/brand name may be assigned to the world without passing the name-availability gate (WORLD.json keeps it a CODENAME).
_flags: active_tested, needs_human_taste_
