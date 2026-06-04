# START HERE , WAVE 1 (60 small/medium docx, 2026-06-04)

> Orchestrated certify+distill (60 haiku reader agents, ~3M tokens, 0 coverage-unconfirmed). 59 certified with coverage proof; 1 exception (PHOTOGRAPHY_MONEY_GUIDE, json parse-fail -> re-run with Wave 2). Full per-doc distillations in `starthere_results/wave1/*.json`. Harvest is RAW candidates (508 skills/1271 rules) , curate, do not auto-build (chunk-to-skill rule).

## Class distribution
- high_signal_source: 44 | scrape: 4 | transcript: 4 | raw_dump: 2 | artifact: 4 | low_signal: 1
- signal: high 47 | medium 7 | low 5

## Per-doc certification + 1-line doctrine
| doc | class | sig | doctrine (truncated) |
|---|---|---|---|
| Brand_Builders_Playbook | high | h | Brand is the gut feeling customers have about you when absent: the internal reputation shaped by every touchpoint (product, messaging, packaging, behavior, response time). Brand cannot be directly con |
| CLAUDE_CODE_SUPERPOWERS | high | h | Superpowers is a complete software development methodology + agentic skills framework for Claude Code, Codex, Cursor, GitHub Copilot CLI and other coding agents. Core workflow: (1) Brainstorming—Socra |
| Cold_Outreach_Sales_Pipeline_Playb | high | h | Cold outreach is math layered on trust. Math: high-volume targeted sends measured by reply rate, filtered through qualification, converted on calls. Trust: every touchpoint must prove relevance in 5 s |
| Contracts_Legal_Protection_Playboo | high | h | Core thesis: contracts are the business operating system, not legal formalities. Non-negotiable rule: no contract signed = no work. Use LLC entity (separates personal/business liability). Payment stru |
| Copywriting_Playbook | high | h | Copywriting is salesmanship in print: every word moves reader toward one action. Core principles: Rule of One (one reader, one idea, one promise, one CTA); match reader's awareness stage (Unaware/Prob |
| Digital_Products_AI_Services_Playb | high | h | Digital products are the highest-leverage solo operator model: build once, sell infinitely, near-zero marginal cost. AI collapsed production barriers (outline to final PDF in days). Distribution is th |
| Direction_Stack_90Day_Plan | high | h | The Direction Stack is marketed as a diagnostic recovery system (10 protocols) for photographers fixing real failures on set, not as a generic posing guide. Revenue target: 80-165 sales in 90 days at  |
| Evoto_AI_Retouching_Reference | high | h | Evoto AI is a standalone portrait retouching platform (Windows/macOS/iPadS) that replaces 80% of manual skin/face work via AI while preserving texture detail. Core value: collapses per-image retouchin |
| GaryVee_Attention_Operating_System | high | h | Interest Media replaces Social Media as the operating paradigm. Algorithm delivers based on what users care about, not who they follow. Follower count is vanity; organic reach validates creative quali |
| Gemini | high | h | Complete operating system for Sniped Media built on three core principles: (1) Systematized Taste: Systems are repeatable; taste is abstract. Engineering rigor applied to visual direction (10-protocol |
| Gemini_PHOTO_YAP | high | h | SNIPED operator photography mastery via Gemini AI image critique + color physics education. Framework: 8-criterion image analysis (composition/lighting/color/pose/depth/edit/emotional weight/uniquenes |
| Gemini_Sniped_MAster_thread | high | h | Comprehensive operating system for Sniped Media: visual systems studio for LA founders built on engineering discipline, not inspiration. Core frameworks: Direction Stack (10-protocol system for mechan |
| Higgsfield_AI_Operator_Playbook | high | h | AI video production shifts from prompt-and-pray to controlled pipeline management. The operator advantage comes from: (1) Character consistency first: train Soul ID with 20-30 reference photos (varied |
| LA_PHOTOGRPAHY | high | h | LA Photography Operating Manual: 5-lane market structure (Founder Personal Branding: $3k-$20k, recurring; Creator Content Retainer: volume monthly; Talent Portfolio: gateway market; Brand/E-Com Campai |
| MONEY_MONEY_AND_MORE_MONEY_AND_GET | high | h | Core thesis: wealth is not a function of income or talent, but of systems and behavioral sequencing. The document presents 29+ distinct financial operating systems, each addressing a specific life pha |
| MOSTLY_PHOTOGRPAHY_SETS_SET_DESIGN | high | h | Set design is constraint-driven systems architecture, not resource-dependent aesthetics. Core operational logic: (1) STRATEGIC: Define era/mood/narrative before prop selection. (2) OPERATIONAL: Color- |
| Money_Wealth_Getting_Ahead | high | h | Getting ahead is a systems problem, not motivation/time/discipline. Three core moves: eliminate constraints (not optimize around them), make 2-3 correct contrarian bets (not many safe ones), build com |
| PHOTO_PIONEERS_VIDEO_TEXT | high | h | Structured breakdown of 8 master photographers (Robert Frank, Richard Avedon, Annie Leibovitz, Stephen Shore, Fred Herzog, Izis, William Eggleston, Ernst Haas). Each analyzed across 5 dimensions: (1)  |
| Photography_Editing_Playbook | high | h | Photography is 80% execution before opening editing software, 20% post-processing. Linear workflow non-negotiable: concept/planning → direction/shooting → culling → Lightroom global edits → Photoshop  |
| Photography_Revenue_Playbook | high | h | Photography is a business tool, not art. Revenue thesis: specialize in one niche, price on business outcomes (not hours), systematize delivery, layer passive income on active service income. Active re |
| Pixieset_Operations_Reference | high | h | Pixieset is a unified platform replacing 5-6 separate tools (gallery, print fulfillment, CRM, invoicing, contracts, scheduling). Core operational value flows from integration: lead capture → project → |
| SNIPED_Chat_Prompts_Reference | high | h | SNIPED_Chat_Prompts_Reference is an operational template library for two distinct project contexts: the SNIPED Media work (aesthetic/art/content execution) and SNIPED Media Strategic (thinking/plannin |
| SOCIAL_MEDIA_3_0_REFERENCE | high | h | A comprehensive operating manual for content creators grounded in neuroscience (dopamine-prediction mechanics), audience algorithm psychology (topic consistency, sample-testing), and monetization arbi |
| THE_REAL_PLAN_Rebrand_Revenue_Exec | high | h | Strategic rebrand and revenue plan for full-time engineer who shoots photography 10-15 hrs/week. Core diagnosis: systems work but story is invisible. Rebrand voice is Calm Authority (educated, structu |
| The_Adobe_Stack_Manual | high | h | Operating manual for Adobe creative production stack (Firefly, Frame.io, Express, video/audio generation). Core doctrine: right tool at each stage of workflow beats single-tool attempts. Firefly Image |
| The_Attention_Stack | high | h | The Attention Stack is a systematic, repeatable system for content production, distribution, and audience-building in photography. Core doctrine: 1) Interest Media (views > followers, follower count i |
| The_Claude_Stack__1 | high | h | Claude is an operating system (OS), not a chatbot. Context (95%) dominates prompt (5%) in output quality. Five core operating modes: Chat (one-off, exploration), Projects (persistent context across se |
| The_Direction_Shift_Master_v2 | high | h | The Direction Shift is a 6-week, 30-post content campaign for SNIPED Media designed to shift from portfolio-only (100% craft/client work) to story-driven posting. The framework pivots on 6 pillars: Or |
| The_Higgsfield_Codex | high | h | HIGGSFIELD AS VIRTUAL PRODUCTION STUDIO: The platform is architected in three layers (Features/Models/Apps), not a single prompt-in-video-out tool. Seven Laws govern operation: (1) Features First, Mod |
| The_Kling_AI_Codex | high | h | AI video production is a systematic, repeatable engineering discipline, not a creative lottery. The complete operating system: Seven Laws (Quality Chain, Prompt Precision, Consistency, Iteration, Cont |
| The_Offer_Stack | high | h | The Offer Stack is a comprehensive operational manual for building, launching, and scaling commercial offers (digital products, physical products, AI services). Core doctrine: (1) Validate before buil |
| The_Operator_Playbook | high | h | Three-layer operating system for content-driven business: (1) Infrastructure = accounts, security, commerce (setup sequence load-bearing, timezone/currency permanent, 2FA mandatory, Business Portfolio |
| The_Platform_Stack | high | h | LinkedIn and Meta are distinct operating systems requiring specialized setup and ongoing rhythms. OPERATING RULES: (1) Platform infrastructure is load-bearing, not decorative. (2) Identity first on Me |
| The_Production_Stack | high | h | Production Stack: six sequential pre-production layers that form the foundation for direction work. Layers (in order): 1) Moodboard (3-5 pages: title image, tone, hair/makeup/styling, lighting referen |
| The_Revenue_Stack | high | h | Photography business as a tool operating on three revenue layers (Active Service/Semi-Passive/Authority), built sequentially not in parallel. Seven foundational laws: camera as business tool; price on |
| branding_x_clothes_gold | high | h | A comprehensive operational playbook for building apparel/consumer brands across 31+ distinct models/frameworks, each with a structured 8-layer architecture: Strategic Layer (core thesis + underlying  |
| chat_Sniped_MAster_thread | high | h | System-driven business operator framework rooted in existing assets + network leverage. Core: Build from proof (25-30 free shoot submissions that convert), not from zero ideas. Two-lane model: Lane 1  |
| claude_cowork_genius | high | h | Claude Cowork is a desktop AI agent (runs on user's computer, not cloud) that autonomously executes multi-step workflows with direct read/write access to local files and external apps (Gmail, Slack, N |
| claude_for_small_business_organize | high | h | Claude for Small Business (launched May 13, 2025) is a bundle of pre-built connectors and workflows inside Claude Cowork (desktop-only app) aimed at SMB owners with no technical background. Core shift |
| garyvee_gameplan | high | h | The 'Interest Media' thesis: organic algorithmic distribution has replaced follower-based social media. Success requires high-volume daily content, organic-first validation before paid amplification,  |
| kling_3_00 | high | h | Kling 3.0 represents a shift from single-shot AI generation to multi-shot cinematic production. Core workflow: (1) Define character/environment via reference images as 'Elements' (2) Break narrative i |
| legal_contracts_and_service_busine | high | h | STRATEGIC THESIS: Professional contracts are business operating systems that define boundaries, prevent scope creep, ensure cash flow, and shift from reactive problem-solving to proactive expectation- |
| life_story | high | h | Bryce Jones: Tuskegee HBCU engineer (2019), cast-on entry into photography April 2019. Seven-year craft development journey (2019-2026) with ZERO business traction until late 2025. Mechanical engineer |
| using_ai_x_gumroad_x_digital_produ | high | h | DIGITAL PRODUCT SYSTEM ARCHITECTURE. Core: AI-assisted content creation + low-friction platforms (Gumroad, Medium, SamCart) + email list ownership = passive income foundation. Six layered business mod |
| AI_CHANGED_EVERYTHING | transcript | h | Transcript of AlphaGo documentary (DeepMind/Google production). Core substance: (1) Game as AI training platform: Go's 10^170 possible board states makes brute-force computation impossible; intuition- |
| Built_an_AI_SaaS_in_20_min | artifact | h | Build an AI SaaS lead magnet using Claude Code + n8n-MCP in ~20 minutes: (1) Set up n8n-MCP by configuring .mcp.json with n8n API credentials (URL + API key); (2) Install n8n Skills for Claude via plu |
| CLAUDE_CODE_PLUGIN | artifact | m | Ralph Wiggum plugin (official Anthropic) enables autonomous multi-step app development via /ralph-loop. Core pattern: write detailed PRD (product requirements doc) with user stories, success criteria, |
| COURSE_WORK_1_thru_2 | artifact | h | AI Automation Agency Curriculum: Build 10K+/month with <$100 startup. Phase 1 covers: (1) AI landscape & billion-dollar implementation gap; (2) four myths: technical skills not required, market not sa |
| FASHION_KILLA | scrape | l | FASHION_KILLA is a compilation of Reddit posts and YouTube video transcripts on men's fashion basics. Core themes: fit is paramount (90% of style problems solved by proper fit); neutral color palettes |
| FINDING_MODELS_ANYWHERE_OG | transcript | l | This is a collection of video transcripts (10 different creators) showing how to find models for portrait/fashion photography shoots. Operating rules: Instagram hashtag search (e.g. #[city]models), fo |
| Finding_Your_Edge | artifact | m | Interactive assessment framework to identify competitive advantages when starting a venture. Core methodology: map resources (business access, equipment, IP, reach), experience across 3+ industries (r |
| NEW_TAKEOVER_HANDLE_WITH_CARE | scrape | m | Twitter/X thread scrape (AdiiX, @adiix_official polymarket trader + crypto/AI researcher). First half (lines 1-96): high-signal thread on AI-driven market disruptions. Three concrete cases: (1) 3D Gau |
| REMOTION | low_signal | l | Remotion is a React-based framework for programmatic video creation. Integrates with Claude Code as an official skill. Core workflow: prompt → code → rendered video. Installation via `npx create-video |
| THREADS | transcript | m | Threads (Meta's Twitter-alternative) operates on a conversation-graph algorithm that prioritizes replies/interactions over likes/follows. Key growth mechanics: 1) Post frequency 5-7+ times daily for a |
| adobe_goat | scrape | l | This document is a curated scrape of Adobe Creative Cloud learning resources and tutorials. Core content centers on Lightroom Classic and Lightroom on the web: organizing/importing photos (Library mod |
| claude_for_small_business | scrape | m | Claude for Small Business is Anthropic's product package combining connectors + skills + agentic workflows. Core components: 8 named integrations (QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google  |
| set_up_ai | raw_dump | l | Corrupted OCR transcription covering 5 AI automation platforms (N8N, Make.com, Zapier, Apify, ChatGPT) with severe garbling. Usable kernels: N8N free tier starts 20-25 GBP/month (2,500 executions), Pr |
| sniped_figma | transcript | m | AI design workflow combining Claude, Codeex, Claude Design, Figma MCP, and Google Stitch. Token efficiency critical: Codeex uses 3-4x fewer tokens than Claude but produces less polished designs. Claud |
| sniped_os_knowledge_dump | raw_dump | m | n8n workflow architecture for AI agents: router agents dispatch requests to specialized sub-agents (email, blog, research, voice); prompt engineering framework: 3 layers (system, input, action); 6 sys |

## Contradictions surfaced (sample , raw, to reconcile)
- [AI_CHANGED_EVERYTHING] AlphaGo billed as 'learning itself' yet heavily trained on human games first; not purely self-taught
- [AI_CHANGED_EVERYTHING] Move 37 described as 'creative breakthrough' yet commentators later note AlphaGo knew it was a 1-in-10,000 move (suggesting calculation, not creativity in human
- [AI_CHANGED_EVERYTHING] Claims AlphaGo couldn't be beaten, but Game 4 Lee Sedol win proves it has exploitable weaknesses (unclear if these are permanent or version-dependent)
- [AI_CHANGED_EVERYTHING] Anthropomorphization risk: commentators and audience treating AlphaGo as 'he/she' despite being deterministic code; emotional narratives overlay on mechanical p
- [Brand_Builders_Playbook] None detected. The playbook maintains internal consistency across branding, operations, and psychology frameworks.
- [Built_an_AI_SaaS_in_20_m] Claude-generated form dropdowns initially non-functional ('can't click on platforms'); required debugging iteration and code fixes
- [Built_an_AI_SaaS_in_20_m] Data path inconsistency: OpenAI output initially not captured in workflow; required manual prompt addition + path routing fix (item.json.body pattern)
- [Built_an_AI_SaaS_in_20_m] Email formatting variance: initial outputs missed some formatting structure; required iterative fine-tuning of prompt and data passing
- [Built_an_AI_SaaS_in_20_m] Webhook URL placeholder: demo uses placeholder initially; production requires substitution after workflow deployment, adding manual step after auto-generation
- [CLAUDE_CODE_PLUGIN] Video shows Ralph 'completing' dashboard but design had errors requiring fixes (Scrum Master intervention) - claimed autonomy limited by need for human judgment
- [COURSE_WORK_1_thru_2] Tension: 'No credentials needed' vs. 'Build 2-3 free projects first.' Resolution: Free projects are your credential; they replace certifications as proof-of-wor
- [COURSE_WORK_1_thru_2] Tension: 'Niche down to win' vs. 'Market is wide open (1.3M restaurants).' Resolution: Niche within the wide market; compete deep in one vertical, not shallow a
- [COURSE_WORK_1_thru_2] Tension: 'Think big (million-dollar dreams)' vs. 'Start small (10 customers first month).' Resolution: Vision is ambitious; execution is staged by capacity and 
- [COURSE_WORK_1_thru_2] Tension: 'Passion sustains you' vs. 'Discipline beats motivation.' Resolution: Passion = long-term fuel; discipline = daily consistency regardless of mood/resul
- [COURSE_WORK_1_thru_2] Tension: 'AI won't replace all jobs' vs. 'AI is replacing specific tasks.' Resolution: True: some roles gone (manual data entry), but humans still required for 
- [FASHION_KILLA] Skipping graphic tees for maturity vs. some recommendations include vintage graphic tees in proper styling
- [FASHION_KILLA] Tight vs. loose fit debate (skinny jeans discouraged but slim-fit praised)
- [FASHION_KILLA] White canvas shoes always work vs. context/outfit matters
- [FASHION_KILLA] Designer accessories necessary for status vs. budget options work equally well
- [FINDING_MODELS_ANYWHERE_] Some creators say never pay models (TFP only), others recommend gas money/lunch for far distances. Context-dependent on photographer experience level.
- [FINDING_MODELS_ANYWHERE_] Some say DM is 'dead' for model discovery (goes to requests), others report 40%+ success. Likely platform algorithm shift over time.
- [FINDING_MODELS_ANYWHERE_] Retouching expectations differ: some say 'minimal edit to show raw talent,' others expect polished deliverables. Varies by market (US vs. European).
- [FINDING_MODELS_ANYWHERE_] Professional model expectation: some advise 'shoot experienced models only,' others say 'friends/non-models work better for beginning photographer learning.' Bo
- [FINDING_MODELS_ANYWHERE_] Email vs. DM priority: some prioritize email if available, others say Instagram DM is faster. No clear winner.
- [Gemini] Free work is encouraged as 'strategic acquisition' but also framed as dangerous 'free photographer trap'—resolved by strict gating (1 hero image only) and categ

## Weird gold (sample , raw)
- [AI_CHANGED_EVERYTHING] Fan Hui's postmatch breakdown and reentry: 'I am not happy to lose the game, but I will be happy for play in the history' sets template for redemptive framing
- [AI_CHANGED_EVERYTHING] Lee Sedol's Game 4 win felt by crowd as 'we can still hold our own' / national survival moment despite being one game out of five
- [AI_CHANGED_EVERYTHING] Kasparov Deep Blue parallel (lines 430-446): chess had 'multiple approaches to solving intellectual problems'; Go was supposed harder, yet fell in same timefram
- [AI_CHANGED_EVERYTHING] Frank's 'slack move' insight reframes all of Go history: 'lessons will influence how Go is played for the next thousand years' based on single machine preferenc
- [AI_CHANGED_EVERYTHING] Aja Huang (AlphaGo's move executor) simultaneously proud and anxious; his physical body mediates human-machine interface; crowd watches his expressions for sign
- [AI_CHANGED_EVERYTHING] Move 37 aftermath: professional Go community immediately recognized impossibility; players began studying AlphaGo's 'mistakes' as advanced technique
- [Brand_Builders_Playbook] The Brand Gap test: Survey 10 random people for 3 words describing your brand, compare to your internal mission. The gap is your work.
- [Brand_Builders_Playbook] The markup revolution: Revision briefs using visual overlays (circles/arrows on photos) convert success rates dramatically vs. text instructions—universal langu
- [Brand_Builders_Playbook] Micro-influencer arbitrage: 10-20 accounts under 50K followers generate higher engagement than 1 celebrity account; cost near-zero (product seeding vs. paid spo
- [Brand_Builders_Playbook] The 3% Rule as a scaling law: Refining a proven product 3% for your specific tribe costs 10% of R&D vs. inventing new SKUs; converts 3x higher because market al
- [Brand_Builders_Playbook] Compound improvement at rep 50: By 50 reps of the loop (publish-review-improve-repeat), you're unrecognizable to yourself. By rep 100, you're untouchable. Data 
- [Brand_Builders_Playbook] Print-on-Demand as a validation tool: You physically hold the product BEFORE you sell it. POD removes inventory risk but lower margins act as a forcing function
- [Brand_Builders_Playbook] Marketing anchor as anti-fragility: One non-negotiable rule ('never discount,' 'never stock photography,' 'never mass-retail') prevents 100 small brand-erosion 
- [Brand_Builders_Playbook] The founder story is the moat: In a market where anyone can make a decent garment, documented vulnerability and sacrifice build an information asymmetry that pr
- [Built_an_AI_SaaS_in_20_m] 20-minute SaaS delivery achievable for simple workflows: entire lead magnet (workflow + front-end + live server) completed in under 20 minutes with Claude Code 
- [Built_an_AI_SaaS_in_20_m] n8n 2,352 templates pre-trained: AI model has access to real-world workflow patterns covering 99% of automation scenarios; eliminates most 'build from scratch' 
- [Built_an_AI_SaaS_in_20_m] Claude MCP tool coverage: 87% n8n documentation coverage, 63.6% operation coverage, 265 AI-capable tool variants detected; sufficient for most lead magnet use c
- [Built_an_AI_SaaS_in_20_m] Auto-fix + planning mode hybrid: Claude's planning mode produces detailed workflow architecture upfront; validates before code generation; reduces revision cycl
- [Built_an_AI_SaaS_in_20_m] Git repo cloning in Claude Code: ability to clone n8n-skills repo, install globally, keep project clean; skills remain accessible across all projects after clea
- [Built_an_AI_SaaS_in_20_m] n8n_update_partial_workflow batching: single call can update multiple nodes, add connections, remove stale connections; vastly more efficient than sequential up
- [Built_an_AI_SaaS_in_20_m] Webhook data accessibility: $json.body access pattern consistent across all node types; single mental model eliminates node-specific data access confusion
- [CLAUDE_CODE_PLUGIN] Scrum Master operator pattern is the real insight - Ralph requires curator not developer
- [CLAUDE_CODE_PLUGIN] Ralph can run 35 iterations autonomously but a single design decision (black/gold theme) requires /frontend-designs plugin intervention - hard boundary between 
- [CLAUDE_CODE_PLUGIN] Completion promise signature must match exact output string or loop continues indefinitely - fragile but intentional constraint
- [CLAUDE_CODE_SUPERPOWERS] Superpowers teaches junior engineers with 'poor taste, no judgement, no project context, an aversion to testing' how to write good code

## Harvest (raw candidate counts , curate later, DO NOT auto-build)
- skills 508 · gates 388 · workflows 484 · prompts 409 · tools 586 · operating_rules 1271 · content_ideas 738 · contradictions 161 · weird_gold 547
- Per the chunk-to-skill rule: these are CANDIDATES. Promote to skill only if executable + run 3x; to doctrine if reusable; else they stay reference in the per-doc JSON.

## Exceptions
- PHOTOGRAPHY_MONEY_GUIDE.docx (5 seg): haiku emitted malformed JSON. Logged cert_status=exception. Re-run in Wave 2 fixup.