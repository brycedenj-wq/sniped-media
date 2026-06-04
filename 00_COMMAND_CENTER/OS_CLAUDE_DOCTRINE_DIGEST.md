# Claude/Agent/Tool Operating Doctrine, harvested from verified corpus (2026-06-04)

PROMPTING PATTERNS, AGENT/WORKFLOW ORCHESTRATION, TOOL-ROUTING/MCP, MODEL-SELECTION/COST, CONTEXT/TOKEN DISCIPLINE, EVALUATION/CRITIQUE, RELIABILITY/RECOVERY, OPTIMIZATION

---

## PROMPTING PATTERNS

**Structural Frameworks**
- TCREI (Task/Constraint/Role/Example/Intent): 4-pass minimum on all AI-generated outputs; foundational across extraction, validation, and copy workflows. [OS_CAPABILITY_MAP lines 1264, 360-435; OS_CAPABILITY_TOOL_ROUTING]
- 6-part prompt architecture: Subject + Action + Environment + Art Style + Lighting + Camera Specs. Technical vocabulary carries 80% of photorealism; vague aesthetics carry almost nothing. [Nano Banana doc]
- 3-part prompt structure: Stage / Task / Rules. Few-shot examples = single most effective technique; concrete instantiation beats abstract description. [Claude_Operating_Manual.txt]
- Hook-first communication: Hook 8 words + Context 3-5 lines + Deployment + CTA. [OS_CAPABILITY_MAP Copy section]

**Constraint Patterns**
- Constraint-first over open-ended: "Keep X identical, change Y" beats open-ended generation. Specificity beats creativity in edit instructions. [Nano Banana doc]
- Role/context/examples embedded before ideation: embed operator voice, lineage authority, prose patterns first. [OS_CAPABILITY_MAP lines 2103-2795]
- Six-part constraint frame: fix one binding constraint monthly; subordinate everything else. [OS_CAPABILITY_MAP lines 360-435]
- Empty-prompt-first gate: reverse verbose-prompt default; context-aware fill dominates. 6-attempt cap before manual escalation. [OS_DOCTRINE_BATCH_012 MA-02; OS_CAPABILITY_MAP line 766]
- Reference density as entropy control: 3-14 reference images plus annotation-driven editing replaces prompt gambling. More references = less hallucination. [Nano Banana doc]

**Advanced Prompt Techniques**
- Metaprompting at scale: LLMs used as prompt architects to expand vague scene descriptions into high-specificity production prompts. Decouples prompt quality from manual labor. [Nano Banana doc]
- JSON-prompt standardization: converts prompt engineering into system engineering; enables batch processing without manual per-session crafting. [Nano Banana doc]
- Gemini Gems as Creative Director Layer: preprocesses vague intent into 100-word technical prompts. 3-word request → production-ready prompt. [Nano Banana doc]
- Composite prompt building via CoT + decomposition + self-critique before dispatch to Higgsfield/Adobe. [OS_CAPABILITY_TOOL_ROUTING]
- Prompt method router (LtM/PaS/PoTh): classify per sniped-prompt-method-router before execution. [OS_CAPABILITY_MAP line 1264]
- promptimizer skill: diagnoses core gap in drafts (vague goal / missing format / buried info) then rewrites rather than patches. Run before any generative task. [OS_DOCTRINE_NEWFILES.txt seg 3]

**Context Architecture Supremacy**
- 95/5 rule: workspace architecture = 95% leverage; prompt refinement = 5% (linear return). Month 6: 5x throughput vs chat-only. Month 12: 10x. Prioritize workspace over prompt tuning. [Claude Stack doc; Claude guide]
- Avoid chatbot mode: long message history dilutes instructions by 26%, causing drift. Minimal history + maximum upfront context = maximum clarity. [Claude guide]

---

## AGENT/WORKFLOW ORCHESTRATION

**Session Protocol (load-bearing)**
- Session start: read CURRENT_STATE.md + ACTIVE_THREADS.md + SESSION_LOG.md tail + STANDING_ORDER + NEXT_ACTION + admin inbox. [feedback_execution_mode.md UPDATED 2026-05-12; OS_CAPABILITY_MAP lines 2103-2795]
- Session end: update CURRENT_STATE.md + ACTIVE_THREADS.md + SESSION_LOG.md + save drafted DMs. State not on disk = does not exist. [feedback_execution_mode.md]
- Standing orders eliminate session-start ambiguity: read STANDING_ORDER + NEXT_ACTION every execution. [OS_CAPABILITY_MAP]
- Execution Governor: 12-step runtime dispatch. Default response is ACTION not report inside SNIPED_OS. [feedback_execution_governor.md LOCKED 2026-05-29; OS_DOCTRINE_BATCH_002]

**Multi-Stage Orchestration**
- 9-phase operator sequence: Chat 7 days → Projects week 2 → Claude Code weeks 3-4 → Skills/Commands weeks 5-8 → Sub-agents weeks 9-12 → MCPs weeks 9-16 → Cowork/Dispatch month 4 → Teams month 5+ → Workspace-as-Asset year 1+. [The_Claude_Stack.txt]
- 7-step operator rollout (non-skippable): workspace folder structure + CLAUDE.md Day 1 → first skills Day 1 → command patterns tested Week 1 → sub-agent orchestration Week 2 → MCP integration Week 2-3 → automation triggers Month 2+. Skip phases = foundation failure. [Claude_Operating_Manual.txt]
- Gate-based routing before execution: composite-master-qa, over-processing-gate, presence-reject-gate mandatory pre-delivery. [OS_CAPABILITY_MAP Production section]
- Fire-triage hierarchy: distribution blocking revenue > product blocking distribution > revenue model > ops > competition. [OS_CAPABILITY_MAP lines 2103-2795]

**Sub-Agent Architecture**
- Single agent first; sub-agent only if single fails. Complexity budget: 2 (single) / 6 (sub-agents, hub-spoke) / 8+ (agent teams). Over-engineering = token waste = quality failure. [OS_CAPABILITY_MAP lines 1260; Claude Stack doc]
- 4 sub-agent personas: content-writer (brand voice), research-specialist (leads, casting, competitor intel), operations-agent (Gmail, Calendar, invoicing), book-drafter (long-form). MCP scoped per agent. [OS_CAPABILITY_MAP line 1260; The_Claude_Stack.txt]
- Sub-agents for parallel bulk work: N simultaneous tasks. Sweet spot 100-200 item batches. Context stays clean (summaries only). Beyond 200, use Zapier/Make. [Cowork Genius]
- Do not spawn sub-agent only to gather context and return output. Keep context-dependent work in same session to preserve reasoning coherence. [Claude guide]
- Git worktrees + /loop for parallel independent branches. [OS_CAPABILITY_MAP line 1262]

**Workflow Automation Patterns**
- Skills = persistent reusable markdown workflow files, not inline prompts. Single markdown: trigger + inputs + output spec + numbered steps. Write once, reuse forever. Wrap at 7+ step complexity. [OS_CAPABILITY_MAP; Claude_Operating_Manual.txt; Cowork Genius]
- Commands = markdown chaining multiple skills one-line. Typical: /morning-briefing, /new-shoot, /weekly-content, /pitch-prep, /post-shoot. Saves 10-20 hrs/week. [The_Claude_Stack.txt; Claude_Operating_Manual.txt]
- Three-State Workflow (Negative/Empty > Positive > Morph): one composite environment + 7 subject variations = 7 campaigns from one prompt investment. [Nano Banana doc]
- 5-bucket skill classification: activate-now / convert-to-skill / reference-only / defer-until-tool / reject-bloat. [OS_CAPABILITY_MAP lines 360-435; sniped-skill-intake]
- Task repetition maturity ladder: one-off request > folder-based multi-session > project with soft/hard memory > skill-wrapped workflow > scheduled skill (automated). [Cowork Genius]
- Plugin worthiness gate (2 of 3): build only if repeats weekly+, multi-step complexity, client-facing or brand-sensitive. Otherwise stay manual. [Cowork Genius]
- If built manually 3+ times, capture as skill/command. [Claude guide]

**Dispatch Leverage Test**
- Any task definable in a command/skill should be dispatched, not done synchronously. Can this run while operator is on set/transit? If yes, must be in dispatch queue. [Claude Stack doc]
- Remote routines (Code-level, 24/7): run on Anthropic servers, survive computer sleep/off. GitHub and API triggers supported. [Cowork Genius]

---

## TOOL-ROUTING/MCP

**Connected Toolchain Default (load-bearing rule)**
- 11-step toolchain audit mandatory BEFORE manual execution is authorized. Sequence: Claude Code skills > MCP tools > Zapier/n8n > Instantly/Super Search > sub-agents > community skills (90K+) > scripts/cron > browser-assisted > Vercel serverless > existing connectors > manual. [feedback_connected_toolchain_default.md LOCKED 2026-05-28; OS_CAPABILITY_TOOL_ROUTING]
- TOOLCHAIN_ACTIVATION.md is single source of truth for tool decisions. [OS_CAPABILITY_MAP line 2796]
- skills-sh-finder mandatory pre-build check (90,000+ community skills) before any custom automation. [OS_CAPABILITY_MAP line 1266; OS_DOCTRINE_NEWFILES.txt line 275-276]
- Manual-only exceptions: LinkedIn commenting (requires real insight), Direction Stack discovery (non-delegable), final image selection (editorial judgment), high-stakes negotiation. [OS_CAPABILITY_TOOL_ROUTING]

**MCP Priority Sequence**
- Drive > Gmail > Calendar > Perplexity > Notion > Apify > Stripe > CRM > Slack > Canva. Start read-only; grant write access only when needed. Token overhead: auto-search kicks in when MCP descriptions exceed 10% of context window. [The_Claude_Stack.txt; Claude_Operating_Manual.txt]
- Tool precedence: MCP-native > API > webhook > manual. [OS_CAPABILITY_MAP lines 360-435]
- Three-step discovery pattern: search_bases (or discovery tool) > get_report_schema > execute_report. [OS_CAPABILITY_MAP lines 360-435; Airtable/Semrush pattern]

**Specific Tool Routing**
- Adobe MCP (mcp__claude_ai_Adobe_for_creativity): default for composite background + environment cleanup; identity layer stays manual. [OS_CAPABILITY_MAP lines 360-435]
- Figma MCP: mandatory; community forks rejected. [OS_CAPABILITY_MAP line 785]
- Higgsfield: approved for IG hero composite, carousel consistency, BTS UGC, Op Kit hero shots, pre-vis briefs; banned for client deliverables, subject identity generation, Portfolio anchor replacements. [OS_DOCTRINE_BATCH_012 D-21]
- Seedream version picker locked: 5.0 Lite (plates), 4.5 (portraits), Nano Banana Pro (identity composites). [OS_DOCTRINE_BATCH_012]
- Evoto routing: studio-only scope gate; non-studio routes to composite. [OS_CAPABILITY_MAP Production section]
- Blender MCP: TCP socket server, null-byte JSON protocol, deferred job poller for long renders (up to 1-hour timeout). MCP spec: type/execute/code/strict_json + null byte. Response: status/result/stdout/stderr + null byte. [OS_DOCTRINE_NEWFILES.txt seg 2]

**Connector vs Browser Automation**
- Pre-built connectors (Gmail, Drive, Notion, Airtable, Slack) faster and safer. Browser automation grants full account access = risk surface. Granular permission controls (read-only, block delete) default. [Cowork Genius]

---

## MODEL SELECTION/COST

**Routing by Task Type (canonical)**
- Opus 4.7: strategic decisions, full-OS synthesis, major strategic bets, swarm-consensus anchor. [OS_CAPABILITY_MAP lines 1257; OS_DOCTRINE_BATCH_012 D-27; OS_DOCTRINE_DOCXWAVE_shelf3]
- Sonnet 4.6: standard task execution, VIB drafts, caption writing, skill invocation, content velocity, tactical work. [OS_CAPABILITY_MAP line 1258; OS_DOCTRINE_BATCH_012 D-27]
- Haiku 4.5: sub-agent batch, data-heavy low-stakes, CRM hygiene, commodity operations running locked SOPs. [OS_CAPABILITY_MAP line 1259; OS_DOCTRINE_BATCH_012 D-27; OS_DOCTRINE_DOCXWAVE_shelf3]
- Context-heavy orchestration = Opus/Sonnet. Commodity operations = Haiku. Visual work = Claude with vision (screenshot QA gates). [Claude_Operating_Manual.txt]

**Phase Unlock Gates**
- Phase B+ unlocks Cowork (cockpit/VIB prep) and Computer Use (Lightroom, Pixieset, Notion, pipelines). Native Claude image/video not yet shipped; Higgsfield/Seedream remain primary external tools. [OS_DOCTRINE_BATCH_012 D-27]

**Cost Discipline**
- "Drunk intern" mental model for 3D AI: Claude 3D useful for procedural workflows + organization, not autonomous photorealistic output. Frames expectation boundary. [OS_DOCTRINE_NEWFILES.txt line 37]
- Blender environment cost: $8 per full environment generation. 7-environment rotation = ~$56/chapter. Trackable, not unknown. [OS_DOCTRINE_NEWFILES.txt line 34, 65]
- Swarm-consensus: ~$0.02-0.10/call frontier (4 expensive models) vs cheap tier (5-8 fast models, 10-50x cheaper). [OS_DOCTRINE_NEWFILES.txt seg 3]
- Validate cheap-model output before scaling; "no automation before proof" gate = validate before deploying at volume. [OS_CAPABILITY_MAP lines 360-435]

---

## CONTEXT/TOKEN DISCIPLINE

**Full-OS Engagement Protocol**
- OS Engagement Protocol: 2,361 sources (1,145 text + 1,216 books) tracked on live dashboard; full coverage proven before "full OS" answer trusted. [feedback_os_engagement_protocol.md LOCKED 2026-06-03]
- Full-OS synthesis required on every big ask: existing docs are raw material, not answers. Nothing previously made is "the answer." [feedback_full_os_synthesis_every_answer.md LOCKED 2026-06-02]
- Read whole before partial answers: every source doc whole-read + distilled, not chunked. Chunks only matter if retrieved + used. Coverage manifest proof required. [feedback_read_whole_then_distill.md LOCKED 2026-06-02]

**Standing State Files as Context**
- CLAUDE.md: 200-500 lines, role + operating rules + failure modes + reference links. [Claude Stack doc]
- /context (brand/SOPs/voice), /skills (reusable workflows), /commands (skill chains), /outputs, /reference, /plans. [Claude_Operating_Manual.txt]
- Hard memory (manually managed markdown: learnings.md, memory.md at project level) + soft memory (auto 24-hour sweep). Combined: no loss of nuance plus persistent institutional knowledge. [Cowork Genius]

**Token Economy Design**
- 200k ceiling enforces minimal chat history. Lazy loading: pull context on demand after second-brain setup. Auto-compaction: Claude condenses automatically. Multi-instance juggling: parallel Claude instances on separate features. [Claude guide]
- Fresh session per task minimizes context bloat. Exception: strategy synthesis sessions require whole-OS read first. [Claude guide]
- OS corpus retrieval routed through MASTER_INDEX + grep/jq; cite [BATCH_NNN_chunk_NNN]. [OS_CAPABILITY_MAP line 1267]
- Wave 1 synthesis layer as query boundary: raw intake 500K+ is last resort. Sequence: WAVE_1_INTAKE_SUMMARY > GAP_REGISTER > SOURCE_LEDGER > topic maps > raw. [OS_DOCTRINE_BATCH_002 Principle 25]
- Context ceiling for Blender: extended sessions hit context walls (2-hour donut example crashed at 60%). Deferred job architecture mitigates by returning quickly while long-running ops poll separately. [OS_DOCTRINE_NEWFILES.txt line 36]
- Five-layer persistent context stack: global instructions > project-level > session-level > skill definition > task prompt. Each layer narrows scope; reduces repetition and context loss. [Cowork Genius]

**Doctrine-as-Code**
- If state isn't on disk and invokable (skills, commands, hooks, cron), it doesn't operationally exist. Docs are dead letters without execution layer. [Claude guide; OS_DOCTRINE_BATCH_002 Principle 8]

---

## EVALUATION/CRITIQUE

**Multi-Gate QA Cascades**
- Composite Master QA: 9-11 gates mandatory; 6-axis scorecard (lighting/grounding/edge-hair/color-marry/artifact/brand-fit), each minimum 8/10. Gates 9-11 = client-ready ceiling (DoF/lens match, perspective, directional color bleed). [OS_CAPABILITY_MAP; OS_CAPABILITY_TOOL_ROUTING LOCKED 2026-06-02]
- Pre-delivery reject gate stack: sprezzatura-check + over-processing-gate + gesture-audit + color-relationship-check, sequential. [OS_CAPABILITY_TOOL_ROUTING]
- Photo QA gate: 8-criterion 1-10 matrix; emotional weight + uniqueness both 6+ minimum. [OS_CAPABILITY_MAP Production section]
- Strongest photograph != most processed: automated output must beat source visually, not just complete task. Failed cleanup artifacts worse than honest studio context. [feedback_strongest_photograph_not_most_processed.md LOCKED 2026-05-28]
- 5-checkpoint gate on iterative generative outputs: no seam, tonal match within 5%, no hallucinated objects, no texture loops, maintained DoF. [OS_CAPABILITY_TOOL_ROUTING; OS_DOCTRINE_BATCH_012 D-19]

**Self-Critique Loops**
- S2A/RaR/RE2 sequence: any LLM-generated copy embeds minimum one self-criticism pattern in the originating prompt. [OS_CAPABILITY_MAP Batch Bf1-shelf19]
- Newspeak Compression Test: "Could this describe a competitor unchanged?" Yes = failed specificity. Run before positioning exits. [OS_CAPABILITY_MAP Batch Bf1-shelf19]
- Specificity gate: parenthetical micro-details create ambient credibility. "77.6%" beats "most." Exact names, exact outcomes, exact context in case studies. [Nano Banana doc; OS Doctrine Shelf 20]

**Strategic Stress-Testing**
- Swarm-consensus validation: 4+ models via OpenRouter + aggregation + minority-view flagging before Direction Stack embedding or major bets. [OS_CAPABILITY_MAP line 1225; OS_DOCTRINE_NEWFILES.txt seg 3]
- Boardroom multi-expert advisor pattern: stress-tests proposition. [OS_CAPABILITY_MAP Strategy section]
- Pre-decision cognitive bias gate: HALT diagnostic (Hungry/Angry/Lonely/Tired) on high-stakes choices. Any fail = defer decision, recover state first. [OS_CAPABILITY_MAP line 1192; OS_DOCTRINE_Boron Letters]
- sniped-premortem: failure scenarios 12 months forward; mandatory for commitments >30 days or >$500. [OS_CAPABILITY_MAP Strategy section]
- Cognitive bias gate vs. 25 Munger misjudgments + 17 CBT patterns. [OS_CAPABILITY_MAP Strategy section]

**Naming + Evaluation Gates**
- Name gate before ship: .com available, no major brand conflict, phonetic under 4 syllables, signals position without explanation, passes cannibalization check. [Claude Stack doc; feedback_name_availability_gate.md LOCKED 2026-06-02]
- 5-anchor Neumeier evaluation (Distinctiveness/Relevance/Memorability/Extendibility/Depth) before any Card ships. [OS_CAPABILITY_MAP line 431]
- H1-H6 framework + Keep/Kill/Iterate anti-hiding check. [OS_CAPABILITY_MAP sniped-proof-loop-review]
- Hook/Retain/Reward gate: every Chapter Card, LinkedIn post, Cultural Doc must pass all three. Fail on any: revise before scheduling. [Shelf 14 / 100M Leads]

**Validation Infrastructure**
- Provide Claude with self-verification tools (unit tests, E2E, linting, browser automation, performance traces). Without validation, AI output cannot self-correct. [Claude guide]
- Eval-driven skill regression gate: every skill update tested against rubric before production. Quality score drops vs. prior version = revert. Never ship degraded skill. [Cowork Genius]
- 95% rule: AI achieves 90-95% autonomy; human polish on final 5-10% saves 2-4 hours per task. [Claude guide]
- Post-extraction validation: line count = chunk count = header count; schema complete; chunk_id unique. [OS_CAPABILITY_MAP jsonl-validation line 367]

---

## RELIABILITY/RECOVERY

**State Machine Discipline**
- State on disk is source of truth: STANDING_ORDER.md, NEXT_ACTION.md, SESSION_LOG.md, ACTIVE_THREADS.md, CURRENT_STATE.md are the nervous system. Sessions begin reading, sessions end updating. [OS_DOCTRINE_BATCH_002 Principle 8]
- Stale-state protocol: 16-day gap in ACTIVE_THREADS = execution-governor failure, flagged at Monday Cockpit. [OS_CAPABILITY_MAP lines 2103-2795]
- Open-loop check: detects threads stale 7+ days at session start. Hard stop gate. [OS_CAPABILITY_MAP; OS_DOCTRINE_BATCH_002]
- Proof log validation weekly: REAL PROOF (money + named outcome + access); reject "praise" or "send info." [OS_CAPABILITY_TOOL_ROUTING; OS_CAPABILITY_MAP line 383]

**Automation Safety Gates**
- Automation-before-proof is a named anti-pattern. Only deploy after workflow manual-tested and stable. Zapier/n8n/Airtable triggers restricted to proof-earned phase. [OS_CAPABILITY_MAP lines 1236-1240; OS_CAPABILITY_TOOL_ROUTING]
- Musk de-automation doctrine: question/delete/simplify sequence before automating. Batch before individual on every repeatable operation. [OS_CAPABILITY_MAP]
- Ingest as propose-and-await: never auto-mutate; no OS mutation without BJ approval. [OS_CAPABILITY_MAP]
- Never ship raw AI output: automation handles drafting/batching; human review gate mandatory before client-facing output. [Cowork Genius]
- Proof-before-skill, proof-before-memory: no gap moves to skill/memory write until run once live. [OS_DOCTRINE_BATCH_002 Principle 17]

**Autonomy Modes + Hooks**
- Ask (gates risky), Edit (normal), Bypass/YOLO (disposable only, never OS-level), Plan (pure strategy). Pre/post/post-fail hooks intercept actions. Hooks not maintained manually; ask Claude to add them. [Claude guide]
- Cron + scheduled agents: standing orders execute without founder intervention. [Claude guide]

**Naming and Registry Discipline**
- Named-system registry: name/lock date/version/disk location on every recurring workflow after 2+ uses. Anonymous systems degrade. [OS_CAPABILITY_MAP S10]
- Requirement-owner gate: every SOP step has named owner or is deletion candidate. [OS_CAPABILITY_MAP]
- Barnacles doctrine: quarterly prune unused/revenue-free/complexity-without-moat OS components. [OS_CAPABILITY_MAP]
- Handle-suitcase gate: locked doctrine tested in last 90 days? Live behavior or repeated phrase? [OS_CAPABILITY_MAP]

**Known Gaps (open reliability risks)**
- CF-011: Synthesis vs. Repetition-Over-Novelty tiebreaker missing. When full OS synthesis contradicts locked 90-day rep freeze, no protocol exists. Recommended: synthesis at session start, then freeze applies unless external forcing function. Needs codification in EXECUTION_GOVERNOR. [OS_CAPABILITY_MAP lines 3402-3506]
- CF-001 through CF-020: twenty documented contradictions requiring human decision authority (pricing tiers, ICP bifurcation, messaging registers, payment splits, proof-ordering gating). No automated resolution. [OS_CAPABILITY_MAP lines 3402-3506]
- No end-to-end skill wraps C1 outbound loop; component SOPs exist but orchestration is manual. Candidate: sniped-outbound-c1-tech-ops. [OS_DOCTRINE_BATCH_012]
- Higgsfield MCP activation unclear vs. Ren cadence dependency. [OS_DOCTRINE_BATCH_012]
- Coordinator manual does not yet exist in SNIPED_OS; build before hiring, not during. [Shelf 14]

---

## OPTIMIZATION

**Architecture Over Activity**
- Repetition over novelty (locked): architecture is built. Next 90 days are reps. New frameworks/SOPs/refinements banned. Run the office. [feedback_repetition_over_novelty.md LOCKED 2026-05-12]
- Concentration beats architecture: 15% (VIB + Reset + LinkedIn POV) deployed consistently beats 85% perfectionism. [OS_DOCTRINE_BATCH_002 Principle 24]
- Composability is leverage multiplier: write once, reuse infinitely. OS is composable software stack, not a library. [Claude guide; Senge + Dixon converge]
- Designer matters more than captain: workspace architecture determines outcomes, not individual skill. Bryce shifts from shoot director to system architect. [Senge; Claude guide]
- Output-first rule: every asset has defined output goal before creation. "Post for presence" fails. [OS_CAPABILITY_MAP A3_shelf5]

**Phase-Gating and Sequencing**
- Gate sequencing, not parallelism: composite assembly > QA gate > platform mastering > publishing (mandatory sequence). [OS_CAPABILITY_TOOL_ROUTING]
- Coenus Stop-Signal: default action on KNOWN work within current thematic goal; apply stop before NEW work outside goal. [OS_CAPABILITY_MAP Bf1-shelf16]
- Ebb-and-flow scheduling: inward sprint (proof/production/OS) alternates outward sprint (outreach/content/VIB). Not balanced, cyclical. [OS_CAPABILITY_MAP Bf1-shelf19]
- Magic Cycle framing: Cycle 1 (Remarkable), Cycle 2 (Milk), Cycle 3 (Reinvest). Track quarterly. [OS_CAPABILITY_MAP Bf2-shelf04]
- Limiting step scheduling: multi-step projects begin identifying longest/constrained step; fictional schedules otherwise. [OS_CAPABILITY_MAP Bf1-shelf12]
- Vision timeline discipline: 5-10yr sight-line. SNIPED calibrated: 2026-2028 = cathedral build, 2028-2031 = proof distribution, 2031+ = adjacent lanes. Current decisions evaluated against 2028 position. [Claude Stack doc / Ries/Trout]

**Operator Role Discipline**
- Default action over report: inside SNIPED_OS, default response shape is action not report. [feedback_execution_governor.md LOCKED 2026-05-29]
- Operator-led + AI-assist beats agentic full-auto for visual output: multiple independent sources confirm Claude assists but human decides every 15-30 min. Adobe connectors underperform manual (4-min AI wait vs 13-sec manual fix). [OS_DOCTRINE_NEWFILES.txt seg 1]
- Full engagement before direction: do not crown a lane from partial OS reads; checkpoints REPORT not SELL. [feedback_full_engagement_before_direction.md LOCKED 2026-06-03]
- Possibility engine / optionality protect: OS must not collapse operator into one identity. Identity emerges from proof, not brainstorm. [feedback_possibility_engine_optionality.md LOCKED 2026-06-03]
- Architecture locked; operation is primary. Claude role in SNIPED: Maintain/Surface/Audit/Condense, not generate unprompted. [OS_DOCTRINE_BATCH_002 Principle 5]

**Calibration and Forecasting**
- Calibration discipline: all forecasts (revenue/conversion/pipeline/calendar) ship with confidence level + post-mortem cycle. [OS_CAPABILITY_MAP Batch-012]
- Culminating-point audit: quarterly depth-peak check; if past diminishing returns, trigger deepen-vs-transition decision. [OS_CAPABILITY_MAP]
- Benjamin Activation Gate: every OS doc read produces visible action or decision logged. Zero doc-read-without-action tolerance. [OS_CAPABILITY_MAP lines 2103-2795]
- Doctrine lived vs. written: shared mental models must be tested operationally, not just read. Pre-shoot mental models session (30 min) is the fix. [Senge]

CLAUDE/AI AGENT OPERATING INTELLIGENCE DIGEST
==============================================

## PROMPTING PATTERNS

**Structural frameworks:**
- TCREI (Task, Context, References, Evaluate, Iterate): four revision passes minimum before shipping. References step shows examples of the standard. [Doc 48, OS_DOCTRINE_BATCH_018]
- Pyramid Principle: governing thought first, evidence/arguments/detail follow. Apply universally to strategic and operational communication. [OS_DOCTRINE_BATCH_018]
- SB7 Framework as prompt skeleton: Character / Problem (three levels: external, internal, philosophical) / Guide / Plan (3-6 steps) / CTA (direct + transitional) / Failure Avoided / Success Achieved. [Shelf 9, Building a Storybrand]
- Three-Level Problem Architecture: name all three problem levels in every marketing/positioning prompt. Omitting any level leaves conversion on the table. [Shelf 9]
- Six-part strategic kernel: Diagnosis + Guiding Policy + Coherent Action only. Bad strategy = fluff, mistaking goals for strategy, failure to face challenge. [STRATEGIC_THINKING_FRAMEWORKS]
- Five-awareness-stages routing: Unaware > Problem Aware > Solution Aware > Product Aware > Most Aware. [Copywriting_Playbook]
- Rule of One: one reader, one idea, one promise, one CTA. [Copywriting_Playbook]
- PAS narrative structure: Problem, Agitate, Solve. [Copywriting_Playbook]
- WAT framework: Workflow (what runs), Agent (who reasons), Tools (what it uses). Highest-value framing addition per Doc 48. [Doc 48, SERIES_5_INTAKE]

**In-context learning:**
- Few-shot minimum: two domain-matched examples establish replication pattern. One sets tone only. Examples placed AFTER context, BEFORE task instruction. [Prompt Template - In Context-2.pdf, Shelf 17]
- Domain-matching mandatory: customer-service examples must match customer-service register. Cross-domain examples break replication. [Shelf 17]
- No chain-of-thought or explicit instruction needed when examples carry sufficient format signal. [Shelf 17]

**Directional and constraint-first prompting:**
- Directional language beats feature specs: "Expensive, restrained, handcrafted" outperforms feature lists. Claude translates intent to specifics better than humans specify. [Seg 9]
- Constraint-as-asset: lock era, palette, spatial rules, and medium constraints FIRST. "Generate X in Y environment with Z visual era." Unlimited options produce dilute results. [Set Design, Shelf 9]
- Example over description: feed 3-5 reference artifacts. AI finds synergies. Prose description requires 10x iteration. [Figma doc, Seg 4]
- One Core Emotion as quality gate: define the single feeling the output should evoke, reverse-engineer all decisions around it. [Figma doc, Seg 10]
- Loss framing at moderate dosage: 30% of argument volume. Kahneman: 2-3x more motivating than gain framing alone. [Shelf 9, Building a Storybrand]
- Concision as authored-signal: demand "extremely concise" in planning/commit artifacts. Sacrifice grammar for brevity. Brevity reads authored, not AI-generated. [Seg 9]

**Session discipline:**
- Plan-Mode-first: iterate specs before execution, approve before build. [Doc 48]
- Skill candidate threshold: when giving same instructions 3+ times, that is a skill candidate. [Doc 48]
- CLAUDE.md discipline: mandatory project configuration, top-to-bottom priority, ~300 lines target. Route lean claude.md content to external files. Never manually edit. [Doc 48]
- /prime command at session start: reads claude.md + context folder. [Doc 48]
- Session architecture: stateless sessions + reusable command files + tools/scripts/skills = automation. [Doc 48]
- Standing order never goes stale beyond 24 hours. If state is not on disk, it does not exist. [OS_DOCTRINE_BATCH_020, THE_SPINE]
- Input-first classification before loading STANDING_ORDER. Classify input type first, then route. [OS_DOCTRINE_BATCH_020]
- Action-first default: sessions should produce more file writes than file reads. [OS_DOCTRINE_BATCH_020]

**Framing and voice:**
- Framing as execution variable: same objective event produces different energy cascades depending on narrative frame chosen. Select deliberately before client conversation. [Winters/88-Laws, Shelf 3]
- Calm Authority voice architecture: operator not consultant, specific, declarative, no buzzwords. [THE_REAL_PLAN, Shelf 7]
- No em-dashes, no buzzwords. Scan before every ship. [CLAUDE.md global rule, OS_DOCTRINE_BATCH_020]
- Copy approval gate: em-dash detected = rewrite, never approval. [OS_DOCTRINE_BATCH_020]

---

## AGENT/WORKFLOW ORCHESTRATION

**Architecture patterns:**
- Multi-agent by discipline: Business / Infrastructure / Creative / Narrative as specialist agents, not monolithic all-context sessions. Reduces hallucination, enables parallel workstreams. [Seg 18]
- Skill dependency chain is sequential: capture-to-delivery calls luxury-edit > evoto > composite-ceiling or lite > pixieset-gallery > post-delivery > notion-crm-update. [OS_DOCTRINE_BATCH_020]
- Full-shoot-day pipeline chain is architecturally runnable as single orchestration wrapper, surfacing decision points only where human judgment required. [OS_DOCTRINE_BATCH_020]
- 3-layer operating architecture: Truth (decisions/rules) / Engine (expert chats advising) / Tool (executing platforms). [Sniped_Media_Controlled_Architecture_v1]
- Chat registry: define clear ownership per stream, not free-floating. [Controlled_Architecture, SNIPED_Chat_Prompts_Reference]
- V2MOM alignment at agent level: Vision / Values / Methods / Obstacles / Metrics pre-named before releasing multi-turn workflow. [Predictable Revenue, Shelf 9]
- Founding concentration, distributed maintenance: one operator sets architecture under near-absolute authority during initialization; once set, team maintains it. Single-mode governance past initialization triggers tyranny. [Machiavelli, Discourses on Livy, Shelf 17]

**Accuracy and sequencing:**
- Accuracy decay: 90% per-step accuracy drops to 59% after 5 steps. Step separation is critical. [Doc 48]
- Sequence is non-negotiable: gated progression beats parallel execution on complex systems. [OS_DOCTRINE_BATCH_018]
- Baton Integrity at every handoff: document context explicitly at each pass. Receiving agent must see full prior output + decision rationale before operating. [Predictable Revenue, Shelf 9]
- Specialization over generalism: if a Claude agent task spends more than 20% on a secondary function, split it. Mixing reduces output quality by 30% within one turn. [Predictable Revenue, Shelf 9]

**Planning and batch execution:**
- Plan before execute; batch after lock: planning mode (explore, surface questions, lock architecture), then auto-accept batch mode: 5+ small changes per prompt, approve as one unit. Fewer tokens, more coherent output. [Segs 9, 18]
- Backward-design funnel before prose/production: 15-min free-write > 30-min mind map > structured outline. Collapses "do I have a concept?" ambiguity before committing effort. [Published, Shelf 5]
- Premortem as standard pre-launch: every major workflow requires failure-mode enumeration before execution calendar locks. [OS_DOCTRINE_BATCH_018]
- Two-pass generation (discovery + refinement): low-resolution brainstorm pass + high-fidelity refinement using polished start frames. [Kling 3.00, Shelf 5]
- Asset-first production: build 4-7 angle character sheets before generating a single output. One-time setup cost enables infinite variation without drift. [Kling 3.00]

**Session persistence:**
- PRD + CLAUDE.md + Task Manager log + isolated sub-agent windows per discipline. Session-start reads context; session-end records completion before clearing. [Segs 18, 9]
- Session-to-session persistence via Task Manager .md files. Granular refinement on CURRENT_STATE/ACTIVE_THREADS/SESSION_LOG pattern. [Seg 8]
- Notion CRM updates within 24 hours of any pipeline state change. Single source of truth, no deferred updates. [OS_DOCTRINE_BATCH_020]
- Contrarian red-team loop: Opus subagent disagreeing with operator's leaning can extend into phase-level checkpoint governance. [OS_DOCTRINE_BATCH_020]

**Automation mechanics:**
- Hooks as lightweight automation: session-start, pre-tool, post-tool, message-sent triggers enable layered automations without full agent loops. Silent by default. [Seg 8]
- Multi-instance parallel work: separate instances in iTerm split panes by feature/project. [Doc 48]
- Agent deployment options: cloud routines (Anthropic) = 15 runs/day max on Max plan, 1-hr minimum interval. /loop loops free under Cloud Code, session-scoped. Modal/trigger.dev for deterministic workloads. Choose by autonomy + availability needs. [Seg 8]
- Trigger taxonomy + Langchain agent + tool-node composition (N8N). Multi-entry orchestration + model-tier routing via BasicLLMChain selector. [N8N_AUTOMATION_SYSTEMS_PLAN]
- Sub-workflow-as-tool composition + structured-output parsing guardrails. Airtable as memory-by-database architecture. [N8N_AUTOMATION_SYSTEMS_PLAN]
- Day-45 trigger as automated Claude task: post-delivery workflows require scheduled Claude prompting via cron/scheduled agent. Not manual. Not ad-hoc. [Predictable Revenue, Shelf 9]
- Metric cascade as standing Claude output: brief Claude monthly to pull five metrics (leads / conversion / pipeline / close rate / revenue by source). Fewer metrics, faster signal. [Predictable Revenue, Shelf 9]

**Intelligence timing:**
- In mutual stalemate, the side learning opponent's true condition first wins. Information advantage converts comparable situations into decisive victories. Applies to pitch timing, VIB outreach, partnership vetting. [Machiavelli, Shelf 17]
- Institutional renewal rhythm: 10-year maximum between visible enforcement events (policy execution, concrete reps). Missing renewal cycles cause rot, not stability. [Machiavelli, Shelf 17]

---

## TOOL-ROUTING / MCP

**Routing hierarchy:**
- Tool-first routing: connector > API > MCP > skill > script > browser. Manual is fallback after toolchain audit returns no path. [CONNECTED_TOOLCHAIN_DEFAULT, multiple sources]
- 7-question operating standard: check toolchain before manual work. [feedback_connected_toolchain_default]
- AI tool selection gated: Seedream 5.0 refused for identity preservation (face shift issue); use 4.5 or Nano Banana Pro. [OS_DOCTRINE_BATCH_020]
- Platform selection for video: Higgsfield for stability and multi-clip documentary consistency. Kling Omni for dialogue and voice consistency. Decision locked at intake, not mid-production. [Kling 3.00]
- AI tool role assignment: Kling for motion / Gemini for brainstorm+image / Claude for written. [Sniped_Media_Marketing_Operating_System]
- Multi-tool orchestration over monolithic replacement: cheap iteration tool (Stitch/ChatGPT) for concept > Claude for production hi-fi > specialized tool (Codeex) for downstream > Figma for polish + handoff. No unicorn tool exists. [Figma doc, Seg 1]
- Tool-first routing WITH cost hierarchy: Stitch/ChatGPT (concept) > Claude Code (design/complex layout) > Codeex (dev implementation). Do not start with expensive tool. [Figma doc, Segs 1-2]

**Hard identity gate:**
- Generative Fill (not identity generation) as the AI routing rule: AI approval for backgrounds, environments, prop extensions, spatial elements, surgical editing ONLY. AI generation never approved for face, body, skin texture. Gate is non-negotiable in the agent prompt itself. [Set Design, OS_DOCTRINE_BATCH_020]
- No full subject generation. Subject must be a real captured photograph. [OS_DOCTRINE_BATCH_020]
- Surgical edit workflow > full generation: region select first, then toggle model, then targeted text prompt, then review. [Set Design, Shelf 9]

**MCP routing matrix:**
- Few-shot stub builder skill + MCP routing: pull 2 known-good examples from corpus > generate reusable template stub > invoke via Gmail MCP for high-touch outreach, Adobe MCP for composite environments, Notion MCP for doctrine logging. [Shelf 17]
- Renewal-audit checklist writes to Notion via MCP. Casting doctrine ledger to Airtable with Zapier automations. Renewal calendar via Google Calendar recurring events. Video intelligence via Higgsfield MCP on competitor analysis. [Shelf 17 connector matrix]
- Instant MCP candidates for SNIPED OS: Airtable (physical card inventory), Adobe (Direction Stack book pipeline), Notion (optionality tracker), Instantly (analog-signal outreach), Figma (Chapter Card system), Google Drive (analog asset vault), Gmail (delivery loop). [Shelf 3]
- Higgsfield repositioned to full Claude-integrated content factory via MCP: 4-stage pipeline (research, content plan, generation, Meta Ads schedule). Earlier framing as motion-only is outdated. [OS_DOCTRINE_BATCH_019]
- Higgsfield credit spend requires per-batch approval. No "always allow" global gate. [OS_DOCTRINE_BATCH_020]
- Tool-routing is a decision table. No generic "best AI tool." Each has locked purpose. Routing by task nature + identity constraints + output register + speed/ceiling trade-off. [OS_DOCTRINE_BATCH_019]
- Infrastructure-first before volume: SPF/DKIM/DMARC + warmup + 30/inbox/day cap before launching cold email. [Cold_Outreach_Sales_Pipeline_Playbook]

**Tool upgrade test:**
- New tools should free human capacity (operator judgment, direction, craft), not hollow it. Tools that deskill the operator fail. Tools that amplify irreducible judgment pass. [Sax/Revenge-of-Analog, Davidson-Rees-Mogg, Shelf 3]

---

## MODEL SELECTION / COST

- Use Haiku for sub-agents on data-heavy tasks, routing, metric rollups, list-building, template filling, and iteration loops. Opus for synthesis decisions and strategy. Sonnet for production hi-fi. Don't overspend on high-token-volume commodity work. [SERIES_5_INTAKE, Shelf 9]
- Tiering for cost/quality: cheap model for reads, strong model for distill/consolidation. [OS_DOCTRINE_BATCH_019]
- Model-tier routing via BasicLLMChain selector in N8N. [N8N_AUTOMATION_SYSTEMS_PLAN]
- Token efficiency hierarchy: cheap iteration (Stitch/ChatGPT) for concept phases. Mode-based workflow: spend hours in one mode (code OR design) then intentional jump. Reduces context thrashing. [Figma doc, Segs 2, 5]
- /compact at 60% context. [SERIES_5_INTAKE]
- Route lean claude.md to external files to preserve context window. [SERIES_5_INTAKE]

---

## CONTEXT / TOKEN DISCIPLINE

- Read whole, then distill (not chunk): every doc/book read whole (segment if huge with coverage-manifest proof), never sampled. Read-whole-once then distill to dense usable doctrine you actually load. Chunks only matter if retrieved and used. [feedback_read_whole_then_distill, LOCKED 2026-06-02]
- Full-OS synthesis every answer: big SNIPED asks = fresh synthesis crunching entire OS via orchestration. Never hand back existing doc. Existing docs are raw material to beat. [feedback_full_os_synthesis_every_answer, LOCKED 2026-06-02]
- Maximum-by-default rule: every task ships max creative/strategic depth by default. Pull from every relevant doc in OS corpus. No baseline-vs-premium tier offers. [feedback_max_default]
- OS Engagement Protocol: whole-read + distill + proven-coverage before any "full OS" answer is trusted. Scale: 2,361 source documents (1,145 text + 1,216 books). Five steps: inventory, prove coverage per doc, label sampling as PREVIEW, distill each to usable doctrine, roll up to master doctrine. [OS_DOCTRINE_BATCH_019]
- Window-limited distillations labeled as PREVIEW: when extracting from summaries/abridged sources, mark as PREVIEW not doctrine. Full-text read required before adoption. [OS_DOCTRINE_BATCH_019]
- Organize by use, not by topic: information and assets organized by where they will actually be used, not subject matter. Actionability is the criterion. [OS_DOCTRINE_BATCH_018]
- Analytics intelligence inputs: tell AI "this data represents [context + plan tiers + user segments]" before analysis. Business context amplifies AI usefulness more than raw schema. [Seg 3]
- Evidence density over process talk: outbound citations 3-5 per piece. Named author + freshness dates raise trust signal. [OS_DOCTRINE_BATCH_019]
- Content evidence density (claim-level): every non-obvious claim in a self-contained paragraph with measurement, scope, source named in same chunk. [OS_DOCTRINE_BATCH_019]
- Junk room warning: growth without ruthless culling traps the operator. Quarterly doc/prompt/skill culling required, not optional. [Grace Coddington, Figma doc, Shelf 16]

---

## EVALUATION / CRITIQUE

**Gates and checklists:**
- Grunt Test Gate as prompt eval standard: before shipping any Claude output (copy, brief, positioning), apply 5-second clarity test. Can a stranger answer in 5 seconds what you offer / how it helps / what they do next? If no, return to Claude with "re-brief per Grunt Test, add three answers explicitly." [Building a Storybrand, Shelf 9]
- Pre-gate checklist over post-output review: build the gate into the prompt itself. Example ICP Red-Flag Gate: confirm budget signal present, no recent competitor install, internal champion identified, timeline real, no churn history. Any red flag = route to Check Back Quarterly bin. [Predictable Revenue, Shelf 9]
- 8-criterion QA matrix: Composition, Lighting, Color Palette, Subject Pose/Presence, Depth/Dimensionality, Edit/Grading, Emotional Weight, Uniqueness. Scored 1-10. Emotional weight + uniqueness must both clear 6 for hero-post designation. [Gemini PHOTO YAP, Shelf 5]
- Few-Shot Quality Gate: before batch output from template, verify both examples match domain tone/format exactly. If not, rebuild stub before running. [Prompt Template, Shelf 17]
- Middle-Path Gate: before any partnership, pricing, or creative compromise, classify: full integration, full exclusion, or pernicious middle? Dangerous middle always flagged for explicit review. [Machiavelli, Shelf 17]
- Property-Seizure Gate (Spoils Gate): before compensation or deliverable structure, confirm no promised assets might require reversal. Clawing back actual possession = permanent resentment. [Machiavelli, Shelf 17]
- Renewal-Deficit Gate: monthly checklist of which doctrine has NOT been actively demonstrated (not documented) in 10 months. Not documented. Demonstrated. [Machiavelli, Shelf 17]
- Sowell Test Gate: "Compared to what? At what cost? What evidence?" Mandatory three-question gate before any policy or decision. [OS_DOCTRINE_BATCH_018]
- Multi-pass quality assurance: screenshot > analyze > refine (3+ passes before handoff). Embed 95% confidence verification steps directly into to-do list, not post-hoc. [SERIES_5_INTAKE]

**Frameworks:**
- Two-track analysis: rational forces + psychological tendencies simultaneously. [Mental_Models_Worldly_Wisdom_FRAMEWORKS]
- Inversion protocol: map all failure modes; what would guarantee failure? [Mental_Models_Worldly_Wisdom_FRAMEWORKS, STRATEGIC_THINKING_FRAMEWORKS]
- Inversion as mandatory risk layer: before committing to any plan, list all ways to guarantee opposite outcome. Run premortem before execution, not after. [OS_DOCTRINE_BATCH_018]
- Framework Orchestrator Principle: diagnose with one lens, evaluate with another, check for bias with a third. [OS_DOCTRINE_BATCH_018]
- Multi-Framework Synthesis: complex decisions require multiple frameworks firing in sequence. Contradictions between frameworks are the most valuable output. [OS_DOCTRINE_BATCH_018]
- Proof audit: have-vs-need matrix. Inject proof adjacent to CTAs at friction points. 95/5 content framework. [Proof_Inventory]
- Signal hierarchy: strong positive = existing behavior + spending + workaround. Weak positive = acknowledges but hasn't solved. Misleading = compliments + hypothetical. Strong negative = not in top 3 concerns. [CUSTOMER_DISCOVERY_FRAMEWORKS]
- Five evaluation gates locked for SNIPED: Analog Premium Gate (scarcity/tactility/ownership), Institutional Senility Gate (real problem vs ceremonial), Momentum Curve Gate (pre/post-inflection), Sovereign Identity Gate (preserve optionality/possibility), Skill Attribution Gate (judgment unmistakably present). [OS_DOCTRINE_REREAD_shelf03]
- Conflict Arc check mandatory: Hook / Rising Action / Conflict (unexpected reversal) / Comeback / Payoff. Missing reversal = not memorable. [Save the Cat, Kling 3.00]
- Authority Signal Stacking Order: empathy before competence. Audience's internal problem FIRST (emotional validation), THEN competence (stats, case studies). Reverse order kills conversion. [Building a Storybrand, Shelf 9]
- Five-Question Testimonial Extraction: what was the problem before? What frustration did it create? What changed? Moment of realization? Life after transformation? 3-5x conversion weight over generic compliments. [Building a Storybrand, Shelf 9]
- Feedback Loops Calibrate Everything: predictions without tracking degrade into overconfidence. Commit to measuring actuals against predictions (Brier scores). [OS_DOCTRINE_BATCH_018]
- Bayesian Update Discipline: every major forecast must have documented prior, evidence log, and posterior. Beliefs update incrementally. [OS_DOCTRINE_BATCH_018]
- Causal chain documentation required alongside activity metrics: outreach/social/metrics can generate engagement correlation without revenue causation (eBay example: $100M ad spend, negative ROI). [Prediction Machines, Shelf 16]
- Human judgment pass non-negotiable: after automated creative batch, human identifies flatness/tension/rhythm gaps and adds interaction per flat section. Tool for exploration; human for felt sense. [Seg 9]

**Anti-patterns (never do):**
- Never measure Claude agent output by activity (tokens spent, iterations) instead of results (qualified outcome, conversion rate). [Predictable Revenue, Shelf 9]
- Never let a Claude agent spend more than 20% on a secondary function. [Predictable Revenue]
- Never ship Claude-generated copy without running Grunt Test. [Building a Storybrand]
- Never generate AI identity (face, body, skin) regardless of quality. [Set Design]
- Never add a new Claude workflow/tool/surface until existing surfaces are producing measurable signal. [Predictable Revenue]
- Never send referral triggers manually or ad-hoc. Schedule them into automation. [Predictable Revenue, Set Design]
- Design Anticipates 3 Moves: ask "does this work at macro scale AND micro scale?" Constantly shift zoom. [Figma doc, Seg 6]

---

## RELIABILITY / RECOVERY

**State and gates:**
- 6 valid permission gates only. All other pauses are anti-patterns. [OS_DOCTRINE_BATCH_020]
- RED/YELLOW/GREEN gate: GREEN = 1+ paid + 1+ room opened. YELLOW = strong pull unpaid. RED = 0 paid + 0 rooms after 15 convos, pivot. [EXECUTION_RUN, THESIS_PRESSURE_TEST]
- Proof-log discipline: every interaction = data. REAL PROOF = money + named outcome + access. FAKE INTEREST = praise / "send info" / no door. [EXECUTION_RUN]
- Single-variable iteration: change one lever only after 3 matching signals, not daily rewrites. [EXECUTION_RUN]
- Top 1 priority always picked. No equal-priority lists. No Phase 2 work while Phase 1 is blocked. [OS_DOCTRINE_BATCH_020]
- Hard stops gate quality: no paid ads / no new platforms / no discounts / no mixing feeds / no announcements before proof. [Direction_Stack_90Day_Plan]
- Non-ship discipline: not rebuilding / not writing UX spec / not waiting for perfect / not adding before tier 1 done. [SNIPED_Site_Polish_Pass]

**Momentum and resistance:**
- Resistance taxonomy (Pressfield via Winters): manufactured excuses are identifiable and consistent. Identification + execution anyway is the countermeasure. [Winters/88-Laws, Shelf 3]
- Momentum curve physics: effort-to-result ratio inverted before and after inflection. Pre-inflection: high effort, low visible result. Post-inflection: lower incremental effort, compound returns. Most people quit pre-inflection. [Winters/88-Laws, Shelf 3]
- Evaluate abandonment via momentum diagnostic before strategy change: has initiative cleared inflection point? If still uphill, is failure reason resistance (execute through) or genuine constraint (redesign)? [Winters/88-Laws, Shelf 3]
- Consistency as underrated power: hammer on same wall constantly; wall falls. Most failure is inconsistent execution, not bad strategy. Novelty-seeking is enemy of wall-breaking. [Winters/88-Laws]
- Coerced agreements null at pressure relief: only freely adopted commitments hold at scale. Any partnership requiring pressure to close is fragile from day one. [Machiavelli, Shelf 17]
- Character lock as casting/pattern filter: individuals and orgs repeat patterns. Two-strike rule theoretically anchored: patterns are sticky, not incidental. [Machiavelli, Shelf 17]
- Temporize only on slow-burn disorders that can die naturally. Force-cure only when disorder is acute and capability to cure is clear. Half-hearted force accelerates harm. [Machiavelli, Shelf 17]

**Delegation hard stops:**
- Assistant delegation scope = lead sourcing, CRM management, reply triage only. Hard stops: assistant does NOT send copy, reply to leads, or touch strategy. Retain voice, pricing, close dynamics. [OS_DOCTRINE_BATCH_019]

**Cognitive vs responsiveness AI:**
- Cognitive AI (Claude/ChatGPT) amplifies desk work. Responsiveness gaps (missed calls, 30%+ revenue leak) are the real bottleneck, not cognitive layer. [B2B_POSITIONING_CLAUDE_OPERATOR_PLAN]
- Amplifier-not-fixer framing: AI integrates inside business stack, not visited as tool. [B2B_POSITIONING_CLAUDE_OPERATOR_PLAN]

**Institutional:**
- Institutional senility self-check: apply to OS annually. Which processes are productive? Which are ceremonial? Which are eating production hours without generating client value? Disdain is leading indicator. [Davidson-Rees-Mogg/Sovereign-Individual, Shelf 3]
- Secret-credit prohibition as team scaling rule: keep all advancement public. No private patron-client loops inside operators. Private loyalty accumulation = tyranny gestation in small teams. [Machiavelli, Shelf 17]
- Ownership as foundation: everything is your responsibility, even events outside control. Eliminates victim loops that drain execution energy. [Winters/88-Laws]

---

## OPTIMIZATION

**Leverage and reuse:**
- Modular-output arbitrage: structure Claude prompts to output modular, reusable components (mood board master template, BTS shot list, testimonial template). Leverage output across multiple channels. [Set Design, Shelf 9]
- One-Liner Memorization Loop: if Claude generates a brand positioning one-liner, embed it in every output surface: DM opener, email signature, website header, case study intro, LinkedIn bio. Leverage compounds. [Building a Storybrand, Shelf 9]
- Element tagging + library storage beats prompt-by-prompt regeneration. Platform consolidation (single aggregator) beats subscription fatigue. [Kling 3.00]
- Batch automation (Google Flow + Chrome extension) for parallel image/video generation. One session produces a week of content. [Kling 3.00]
- Grid-to-video workflow: create 3x3 grid storyboard, upload as visual reference. Tool deconstructs into 9 sequential shots with visual consistency. Eliminates per-shot prompting overhead. [Kling 3.00]
- PreViz before generation: insert a planning step first (SketchUp spatial pre-visualization for depth, light anchors) before Firefly/Flux generation. Prevents CGI sterility, saves iteration loops. [Set Design, Shelf 9]

**System design:**
- Judgment as irreducible human work: AI provides prediction (cheap, scaling); humans specify payoff functions (scarce, compounding). Design the constraint (what good looks like) before releasing the tool. [Prediction Machines, Shelf 16]
- Whoever specifies what good looks like owns the value. Execution layer (AI, crew, code) is a complement. Judgment layer (payoff function, design system constraint, editorial conviction, causal model) is the moat. [Prediction Machines, Genghis Khan, Shelf 16]
- Human-defined constraints first, AI applies within: variable library, design tokens, payoff function specification = human work. AI hallucinates full system scope on import. Train AI sequentially on human-locked decisions. [Figma doc, Seg 3]
- Spec-driven development enables AI to do 80% of the build. Interview protocol (AI asks clarifying questions to surface hidden assumptions) is the blind-spot-surfacing layer. [SERIES_5_INTAKE]
- Ritual and repetition encode authority: locked component systems + reusable prompt skills prevent drift. Repetition reduces cognitive load and enables scaling without deliberation overhead. [Genghis Khan, Figma doc]
- Skills architecture is formalization of standing orders and routing manifest patterns. Custom Claude skills encode SOPs and persist across sessions/team members. Every recurring task routed to automation; every creative decision held by operator. [Doc 48, SERIES_5_INTAKE]
- Skill abstraction as doctrine-packaging: encode operating frameworks (decision logic, visual direction, trust mechanics) as Claude .md skills for reuse across contexts without re-prompting. [Seg 18]

**Distribution as optimization layer:**
- Broadcast now includes AI answer engines: articles structured for LLM extraction are a distribution play, not just SEO. Perplexity weights outbound citations + recency. Google AI Overviews weights structured data + Q-A pairing. ChatGPT/Claude weights self-contained, well-attributed claims. [OS_DOCTRINE_BATCH_019, SERIES_5_INTAKE]
- Citation-first SEO: AI queries now prioritize "cited as authoritative source in AI answers" over traditional SERP ranking. Six-word queries trigger AI overviews 77% of the time. [SERIES_5_INTAKE]

**Right-size tools:**
- Right-size analytics tool to job: Plausible (1KB script, CSV export, data ownership, one-line setup) vs GA for simple operator tracking. Tool waste if you only need week-1 retention + funnel. [Segs 2, 15, 17]
- Week-1 retention as launch metric: talk to users first; analytics illuminate after product-market readiness. Week-1 retention cohort is single most actionable number at launch. [Seg 2]
- Deployment options trade complexity vs control: VM (full control, high ops), PaaS/Cloud Run (hybrid, cost-efficient), Kubernetes (overkill), serverless (cheap, no websockets, cold-start). Cloud Run + minimum instances = operator-scale balance. [Seg 16]
- Vercel pricing trap at scale: works at low-traffic niche. At high traffic, cost-to-convenience ratio inverts. [Seg 1]
- Cheap Levers Before Expensive Ones: exhaust low-cost options before investing in high-cost resources. Applies to token spend and feature complexity. [OS_DOCTRINE_BATCH_018]
- Four-Lever Revenue Priority Order (transfers to resource prioritization): Price increase > Frequency > Transaction size > Acquisition. Acquisition is last resort. [OS_DOCTRINE_BATCH_018]

PROMPTING PATTERNS

- Task-to-decomposition method matching (LtM/PaS/PoTh) before prompt construction. Mismatched method degrades output predictably. [Prompt Template]
- Decomposition-first rule: break task into three modular sub-problems before applying step-by-step reasoning. Prevents premature synthesis. [Prompt Template - Combining Techniques]
- Composite prompt architecture: CoT (reasoning trace) + Problem Decomposition (three sub-problems) + Self-Critique (re-anchor against source brief). Sequence in that order; interleaving degrades each. [Prompt Template - Combining Techniques]
- Constraint-by-count eliminates sprawl: "three channels, two improvements" beats open-ended lists. Forced count forces judgment. [Prompt Template]
- Five-element prompt architecture (WHAT + STYLE + LIGHTING + ENVIRONMENT + TECHNICAL DETAILS): vague prompts produce inconsistent variants; five-element prompts produce tight aligned results. [Photoshop tutorials / Shelf 2]
- Brief-as-doorway (inspiration, not specification) opens possibility space. Over-specification kills serendipity. [Truth, Lies & Advertising]
- Persona assignment as output lever: "tell AI who it is" + explicit variance directives reshape output away from median-chasing. [Co-Intelligence / Shelf 2]
- Constraint-seeded generation: locked environments + seeded prompt architecture beat open-ended generative prompts. Biological seeding within constraint boundaries outperforms freeform. [Daugherty & Wilson / Human + Machine]
- Granularity principle: smaller iterative selections per generation, not compound requests. [Photoshop tutorials]
- Context architecture outranks prompt engineering. How Claude is configured (workspace, skill packages, project briefs, sub-agent structure) is the meta-lever. [MDA-006 / Batch 007]
- Corpus as language accelerator: corpus gives language, work gives proof, reps give judgment. Corpus compresses time to legible first offer; does not replace proof. [OS_DOCTRINE_BATCH_005]
- Read-whole-then-distill: load entire source doc before partial extraction. Chunks only valuable if retrieved and used later. [feedback_read_whole_then_distill / Caesar shelf]
- Genre clarity is load-bearing: title, authorship, framing must be embedded in artifact header, not left to reader inference. [Caesar / Shelf 10]
- Third-person framing + embedded causality embeds meaning without explicit claim. [Caesar / Shelf 10]
- Assume audience is smart; talk-down copy fails. Partner, not target. [Truth, Lies & Advertising]
- Character-based directing replaces mechanical instruction: backstory/movement prompts over body-part directives. Context over command. Generalizes to AI and human direction. [FINDING MODELS / Shelf 11]
- Scenario-based targeting (day-in-the-life: economic buyer, end user, technical buyer; before/after states; consequences) informs prompt specificity. [Moore / Crossing the Chasm]
- Reference competitor frame: every prompt requires both market alternative (incumbent) and product alternative (peer disruptor). Without both, position is unintelligible. [Moore]
- Singular priority discipline: force one thing. Vagueness cascades as diffusion; clarity cascades acceleration. [AMP IT UP / Slootman]

---

AGENT / WORKFLOW ORCHESTRATION

- 9-step OS_TRANSFORMATION_ROUTER: mandatory meta-protocol for every major task: detect category, select doctrine lanes + tactical docs + tool docs, load operator context, perform task, report all resources consulted + any skipped, escalate if routing unclear. [OS_DOCTRINE_BATCH_005]
- Plan-then-Execute bifurcation: plan phase produces structure, execute phase produces deliverables. [Prompt Template]
- Phase-gated delivery model: always end phases with working piece, not document. Build in order of leverage. Measurement from Phase 1. Handoff designed, not discovered. [The_Install_Methodology_v1]
- Standing order + next action dispatch: inside OS context, default to ACTION not report. Read STANDING_ORDER + NEXT_ACTION at session start. [feedback_execution_governor]
- Full OS synthesis requirement: big SNIPED asks trigger fresh synthesis crunching ENTIRE OS via orchestration. Existing docs are raw material to beat, never the answer. [feedback_full_os_synthesis_every_answer]
- Two-file state discipline: CURRENT_STATE.md (canonical truth) + ACTIVE_THREADS.md (thread log). Read at session start, update at end. If state not on disk, it does not exist. [OS_DOCTRINE_BATCH_005]
- 30/60/90 proof-log checkpoints: 30-day (cheapest signal: real conversations, offers, payment?), 60-day (repeatable demand, inbound/referral pull?), 90-day (case studies, retained demand, buyer pulling for systems?). [OS_DOCTRINE_BATCH_005]
- Proof log admin formalized: admin = data entry only, flag inbound replies immediately, never interpret R/Y/G or thesis signal. [OS_DOCTRINE_BATCH_005]
- Sub-agent delegation patterns require focused brief + gate discipline, not open-ended prompts. Handoff artifacts must explain "what happens next" at every gate. [D-043 / Batch 007]
- Default response shape is action, not report. Every response must name a next action or flag sequencing concern. [D-008 / Batch 007]
- Multi-source insight convergence (quantitative + instinct + cultural signal + proof) before any decision. Single-source verdicts are blocked. [Truth, Lies & Advertising]
- MELDS Framework (Daugherty & Wilson): Mindset, Experimentation, Leadership, Data, Skills. [Human + Machine]
- Eight Fusion Skills: Rehumanizing time, Responsible normalizing, Judgment integration, Intelligent interrogation, Bot-based empowerment, Holistic melding, Reciprocal apprenticing, Relentless reimagining. [Daugherty & Wilson]
- Relentless Reimagining Test: Does proposed workflow automate an outdated process or enable a reimagined one? Wave 3 collaboration (new models) is higher value than Wave 2 (speed + scale of existing flows). [Daugherty & Wilson]
- Four gears sequence (Moore): Engagement > Acquisition > Enlistment > Monetization. Monetization too early stalls engine. Establish reference density before scaling conversion moves. [Moore]
- Chasm gate (Moore): Before any new agent capability or tool adoption: (1) identifiable economic buyer? (2) compelling reason to buy? (3) whole product deliverable in 3 months? (4) competitor already fortified? Fail all four = do not enter. [Moore]
- Jagged frontier mapping: explicitly divide production into inside-frontier (delegate to AI) and outside-frontier (human required). Frontier shifts as capability advances. [Co-Intelligence / Shelf 2]
- Centaur vs. Cyborg models: Centaur = clear division of labor; Cyborg = integrated intertwined effort passing fragments back and forth. Both valid; neither requires full delegation. [Co-Intelligence]
- Repeatability before scaling: no team expansion or collaborator locks until 3-5 shoot PMF with same model/MUA chemistry proven. [AMP IT UP + feedback_payment_follows_proof]
- Blueprint consistency enforcement: maintain consistent agent decision logic across invocations. Deviations on two or more dimensions (source, reward, control style) trigger 2.3x failure rate in founder contexts. [Wasserman / Shelf 18]
- Three Rs equilibrium for collaborations: Relationships + Roles + Rewards must stay aligned. Mismatching social-logic teams with equitable splits or business-logic teams with equal splits causes implosion by year 2. [Wasserman]
- Also Boughts Purity Doctrine: first audience cohort seeds the platform recommendation model. Wrong-audience early-stage promotion poisons algorithm for months. Seed with precision inside your scene first. [Book 2 / Fayet]
- Operate on one channel/tool at a time before scaling. Scatter = zero attribution, wasted effort. [Book 2]

---

TOOL-ROUTING / MCP

- Connected toolchain default: tool-first routing (connector/API/MCP/skill/script/browser). Manual is fallback after toolchain audit returns no path. [feedback_connected_toolchain_default / multiple sources]
- Tool-routing priority stack: Skills first, MCPs second, Scripts third, Manual only after full toolchain audit returns no path. [D-010 / Batch 007]
- Bot-based empowerment as labor allocation: every task a bot can handle (scheduling, note-taking, sequencing, tagging, organization) routes to a bot. Protects high-judgment operator time. [Daugherty & Wilson]
- Missing Middle Routing: pre-evaluate new tools with Wave 2 vs. Wave 3 test before accumulation. Prevents toolchain bloat optimizing obsolete workflows. [Daugherty & Wilson]
- Minimal buildable workflow: Inquiry > Paid > Delivered > Upsold. Pixieset is integrating hub. Automation-before-proof anti-pattern: n8n + video engine later; proof loop core first. [OS_DOCTRINE_BATCH_005]
- Metadata embedding via MCP: Notion + Drive auto-populate metadata header (title, genre, author, lock date, version). Airtable named-system registry (one row per named system, queryable, survives session resets). Gmail headers standardized. [Caesar / Shelf 10 connector opportunities]
- Named systems are IP: if a workflow recurs 2+ times, name it + lock it + version it. Anonymous recurring workflows disappear. [J.Crew / Shelf 10]
- Organizational coinvention gate: no new tool added until organizational coinventions (process, training, doctrine) are scoped and scheduled. Each dollar of tool investment catalyzes 9-10 dollars of required organizational capital. [Brynjolfsson / Second Machine Age]
- Airtable for named-system registry, Notion/Drive for metadata headers, Gmail for transmission framing, Google Calendar for logistics gates. [Shelf 10 MCP opportunities]

---

MODEL SELECTION / COST

- Skill-biased routing: nonroutine cognitive (ideation, pattern recognition, complex communication) and nonroutine manual work route to Claude/humans. Routine tasks route to tools/automation. [Brynjolfsson / Second Machine Age]
- Human complementarity model: weak human + machine + better process > strong computer. Process layer (methodology, doctrine, workflow) is the decisive variable, not raw model strength. [Brynjolfsson]
- Cheap vs. strong trade-off: cost-efficient models for Wave 2 tasks (asset organization, templating, straightforward data retrieval). Reserve strong models for low-data creativity, ethical judgment, strategic reimagining. [Daugherty & Wilson]
- Cheap fast routing for support/review/low-stakes: use faster model for agent-to-agent handoff when task does not require full reasoning. [Shelf feedback]
- Choose tools/agents by operational values + taste alignment, not pedigree. Hire/partner for philosophy + taste before credentials. [J.Crew / Shelf 10]

---

CONTEXT / TOKEN DISCIPLINE

- Pattern library vs. operative doctrine distinction: pattern libraries inform, they do not constrain. Operative doctrine (CANONICAL_TRUTHS, operating locks, EXECUTION_GOVERNOR) constrains. No pattern library finalizes brand/company/identity. [OS_DOCTRINE_BATCH_005]
- Context preservation on handoff: when tool output passes to next agent step, maintain explicit context about what the previous step discovered, decided, or ruled out. Do not start fresh per handoff. [Daugherty & Wilson]
- Session disk protocol: state only exists if written to disk. Session start: read CURRENT_STATE → ACTIVE_THREADS → SESSION_LOG tail. Session end: update all three. [feedback_execution_mode]
- Coverage manifest proof for big reads: when reading large docs, provide segment list showing what was read, not just sampling. [read_whole_then_distill]
- Load standing orders/execution governors on session start. Thin OS references per task (relevant doc, not full corpus). Skip analysis/report mode; default to action. [feedback_execution_governor / Shelf 11]
- Read-by-job, not read-everything: 11-doc default stack per task; gap-driven inspection only when summary is generic. [D-024 / Batch 007]
- Non-chunked anchors: CURRENT_OPERATOR_REALITY_BRIEF held as anchor-only, never chunked as doctrine. [OS_DOCTRINE_BATCH_005]
- Condensation discipline: no new strategy docs unprompted, one fact per doc, active surface stays small. [D-005 / Batch 007]
- Proof-phase execution vs. structural decision triage: default-to-action is correct for proof execution (shooting, outreach, content, production). Default-to-action is NOT correct for structural decisions (equity, roles, capital). These require deliberate gate-setting. [Wasserman / Shelf 18]

---

EVALUATION / CRITIQUE

- Standards-raise mental model (Jobs-bar): "Thrilled?" not "acceptable?" Every artifact is hardest-to-say-no-to by default. [AMP IT UP / Slootman]
- Goodhart's Law check: when a measure becomes a target, it ceases to be a good measure. Behavioral outcomes are targets. Vanity proxies are monitoring signals only. [Daugherty & Wilson / Shotton]
- Behavioral proof over stated preference: track what agents/users actually do, not what they say they prefer. Survey responses are inverse predictors of behavior. [Shotton / Choice Factory]
- Proof loop as scoreboard: only valid signal is money + named role. Compliments without money do not count. [D-027 / Batch 007]
- No-fabricate guardrail: never invent pilots, clients, testimonials, case studies, metrics. Never log praise as payment. Single fabricated entry destroys scoreboard + procurement buyer trust. [OS_DOCTRINE_BATCH_005]
- Drift detection always-on with eight pattern triggers; surface without softening. Three overrides per week on same theme signals deeper drift. Challenge contract is non-optional. [D-002, D-004 / Batch 007]
- Brief-as-doorway gate: does this open or close possibility? If it answers every question, it is spec not brief. Fail = rewrite. [Truth, Lies & Advertising]
- Insight-convergence gate: confirm at least three signal sources before strategic decision. Single-source blocked. [Truth, Lies & Advertising]
- Constraint-count gate: open-ended lists must receive count constraint. No count = no output. [Prompt Template]
- Apparatus durability gate: before publishing any artifact, does it carry its own framing? If title were stripped + replaced by stranger, would it survive? Does title + opening paragraph establish genre, author, intent? [Caesar / Shelf 10]
- Tester protocol: before scaling any new prompt format, output structure, or tool workflow, run 3-5 defined testers with explicit success signals. Pass threshold before committing. [Greene / Brynjolfsson]
- Reference artifact gate: every agent output destined for external use must produce a documented proof artifact (case study, before/after, schema proof) before shipping. [Moore]
- Legitimate authority check: authority compounds faster from verified wins than from declared expertise. Proof runs the direction; data informs, not leads. [Caesar / Shelf 10]
- Operative vs. reference intelligence flag: label docs as OPERATIVE (actively used), UPDATES (extends existing), or REFERENCE (intelligence layer). [Shelf 4 / docxwave pattern]
- Version conflict detection: when multiple docs claim ownership of same domain (pricing tiers, Direction Stack revisions, follow-up timing), flag explicitly with RECOMMENDATION. Audit timestamps; treat latest as operative, flag older for retirement. [OS_DOCTRINE_DOCXWAVE]
- Consumer-intelligence gate: copy/DM/caption treating audience as demographic bucket fails. Rewrite assumes smart reader. [Truth, Lies & Advertising]
- Decomposition-method gate: classify complex task as LtM/PaS/PoTh before writing prompt. [Prompt Template]
- Tutorial-to-asset conversion rule: every tutorial consumed must produce persistent OS asset within same week or resource deleted. [OS_DOCTRINE_BATCH_005]
- Tactic deployment only after four fundamentals locked: (a) target market precise, (b) product matching expectations, (c) platform mechanics literacy, (d) owned audience layer (email). Pre-foundation effort wastes downstream spend. [Book 2 / Fayet]

---

RELIABILITY / RECOVERY

- 7-step Batch SOP with pre-flight stub checks mandatory: Inventory > Plan > Authorize > Stage > Extract > Chunk/Validate > Consolidate/Session-Save. Never skip. Corpus verification via 3-way reconciliation: header field = batch.chunk_count = JSONL line count. If any fails, halt and escalate. [D-013, D-045 / Batch 005 + 007]
- Verification-before-staging: files pass read-only checkpoint before staging. No staging without authorization. [D-012 / Batch 007]
- Algorithm aversion reality: people forgive human errors more than algorithmic ones. Solutions: guardrails (bounded decision space), human checkpoints (transparency), minimize moral crumple zones (accountability aligns with actual control), enable worker agency (ability to second-guess). [Daugherty & Wilson]
- Explainability as strategy: transparent hybrid processes are both ethical and commercially correct. [Daugherty & Wilson]
- Data supply chain ownership: 90% of AI training time is data prep, not algorithms. Own data quality, tiering (hot/cold), access breadth, velocity, discovery. [Daugherty & Wilson]
- Logistics are law: skipping gates invites hostility even from allies. Procedure protects outcome. Casting call doctrine, MUA confirms, wardrobe gates, two-strike rules. [Caesar / Shelf 10]
- Failure + narrative control: have a brief, honest, circumstances-aware acknowledgment on disk for every major setback. Absence of narrative becomes a vacuum enemies fill. [Caesar / Shelf 10]
- Infrastructure debt is invisible until velocity demanded: quarterly audit of every workflow manual or via workaround. Identify constraint before it becomes crisis. [J.Crew / Shelf 10]
- Soul ID deferral as first-class decision gate: do NOT train permanent identity on transitional-state photos. Resume only on explicit approval signal. [OS_DOCTRINE_BATCH_005]
- Reject gate mandatory: strongest output beats most-processed output. Failed cleanup artifacts worse than honest studio context. [feedback_strongest_photograph / multiple sources]
- Non-destructive assembly: every generative operation creates a new layer + layer masks allow rollback without touching source. Reference original image each iteration, not previous generation. [Photoshop tutorials / Shelf 2]
- Never hallucinate friction: payment/entity structure follows proof. Admin imperfection = cleanup, not money blocker. [feedback_payment_follows_proof]
- Dynamic equity model for agent roles: contract terms handle knowns, vesting clauses handle foreseeable changes, trust handles surprises. Roles should be milestone-conditional, not static. [Wasserman / Shelf 18]
- Motivation consistency as decision filter: before any structural commitment (hiring, capital, partnership), name the decision motivation lane (wealth vs. control). Inconsistency produces 80%+ failure-to-achieve-either-outcome. [Wasserman]
- Driver/passenger test for collaborators/tools: "Does absence hurt results?" Swap passengers fast; do not coach. [AMP IT UP / Slootman]

---

OPTIMIZATION

- Constraint as creative superiority: locked environments beat random AI prompts because explicit constraint pushes output off median. [Shelf 2 + Daugherty & Wilson]
- Recombinant innovation: new value from recombining existing blocks, not inventing from scratch. Marginal expertise (field engineer + photographer + founder) beats pure specialists. Processing capacity (testing more combinations faster) is the constraint, not idea scarcity. [Brynjolfsson]
- Horizontal engine logic: one core competency applied across multiple output surfaces/registers. Revenue scales per surface; moat is architecture not tool. [EVOTO / Shelf 11]
- Batch as defensible revenue layer: single-image is commodity/prestige signal. Batch is sticky, defensible tier. Separate pricing tier before pitch. [EVOTO / Shelf 11]
- Whole-product completion (Moore): core product + expected ecosystem + augmented layer + potential layer. Raw outputs are components. Integration to whole-product standard required before release. [Moore]
- Intangible capital (Brynjolfsson): every prompt architecture, documented output, methodology, and prompt-refinement iteration is organizational capital. File and review quarterly. [Brynjolfsson]
- Repetition over novelty: mastery via process, boredom tolerance. Sustained attack beats innovation chasing. [Greene + Brynjolfsson + SNIPED doctrine]
- Maximum-by-default: every task ships max creative/strategic depth. Pull from entire corpus. No baseline-vs-premium tier offers. [D-006 / Batch 007 + feedback_max_default]
- Comps treadmill kills iteration: require explicit values-based rationale (lineage, scene density, constraint) rather than "it worked before." [J.Crew / Shelf 10]
- Read-Through Lifetime Value math: series profitability requires full-arc accounting, not single-sale ACoS. Changes acquisition-cost targets and scaling timing. [Book 2 / Fayet]
- Automation maturity progression: Wave 1 (exact process replication) → Wave 2 (speed + scale of existing flows) → Wave 3 (adaptive human-machine collaboration, new business models). Always evaluate whether you are building Wave 2 or Wave 3. [Daugherty & Wilson]
- Comparison set framing: before major decisions (pricing, positioning, model selection), ask what comparison set the recipient is using. Reframe the category before discussing features. [Shelf 1]
- Positioning ceiling gate (quarterly audit): is brand language a subset of larger category? Protect optionality; do not crown prematurely. Snowflake "Data Warehouse" to "Data Cloud" lesson. [AMP IT UP / Slootman]
- Execution precedes strategy inversion: start with execution discipline proof, then evaluate strategy validity. Strategy pivot only after PMF repeatability proven. [AMP IT UP / Slootman]
- Lineage moat beats aesthetic moat: distinguish between aesthetic moat (temporary, copyable) and lineage moat (embedded, non-copyable without years of presence). Invest in lineage layer. [J.Crew / Shelf 10]
- Equalizing effect and moat shift: AI amplifies weak workers most. Skill gaps collapse. Premium-for-execution moat dies. Moat must shift to taste/lineage/embodied judgment that AI cannot replicate unguided. [Co-Intelligence / Shelf 2]
- Marketplace compliance language: name platform/context (Instagram compliant, Amazon product-image compliant), not generic skill (professional editing). Specificity converts. [EVOTO / Shelf 11]
- Explicit negative promise gate (client-facing AI copy): name what does NOT happen with identity data. Specific refusal outperforms vague assurance. [EVOTO / Shelf 11]
- Redundant trust anchors on every touchpoint: privacy/identity protection + delivery speed + output quality + process ease. Addresses three buyer anxieties simultaneously. [EVOTO / Shelf 11]