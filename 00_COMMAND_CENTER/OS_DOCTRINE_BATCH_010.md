## DOCTRINE ENTRIES (deduped)

**D-001: Cadence and Locks as Runtime Infrastructure**
Three-gate rhythm (daily / weekly / monthly) is not optional. Sunday weekly review (20 min), Monday planning cockpit, monthly constraint audit (60 min) are standing gates. Operating locks (7 + addenda) are hard rails; decision toolkit sequences inside them, does not reopen them. Anti-drift disciplines: repetition over novelty, proof over packaging, maximum-by-default, action not report, session start/end protocol. Source: CADENCE_AND_LOCKS.md.

**D-002: Command Router as Default Operating Layer**
Input-first classification is the default session posture. Router answers the actual input, does not collapse all inputs into the active proof loop. 11 input categories dispatched to appropriate skill/SOP. Source: STANDING_ORDER.md, NEXT_ACTION.md.

**D-003: Session Start/End Protocol (reinforced)**
Start: read CURRENT_STATE.md, ACTIVE_THREADS.md, SESSION_LOG.md tail, check _inbox/admin/. End: update three fields (active proof loop, recent ships, next proof loops). Mission line and phase status do not update except at locked decision points. Staleness trigger: >24h. Source: STANDING_ORDER.md, NEXT_ACTION.md.

**D-004: Phase 1 Throttle and Phase B Gate**
Phase 1 ceiling: $0-3K MRR, 10-12 hr/week solo, AWS day job as income floor. Phase B triggers at $3K MRR sustained 2 consecutive months. No expansion, no hire before trigger. Source: STANDING_ORDER.md.

**D-005: Fulfillment-as-Renewal**
Post-delivery asset bundle IS the renewal closing move. Proof + real numbers + branded recap = premium-buyer renewal lever without re-selling. Aligns with hospitality layer (service = what promised; hospitality = more than expected) and status psychology (sponsor sees brand on broadcast; renewal is status-maintenance). Source: KOTS_SPONSOR_MEDIA_DELIVERABLES.md.

**D-006: KOTS Institutional Governance Model**
Builder (Bryce) constructs systems; authority-wielder (Coach Jones/Principal/Committee) pushes. Tournament owns brand, accounts, sponsor relationships. BJ owns execution + photo/video/sponsor/licensing revenue lines. Flat production fee covers trip cost (set with committee); upside via 5+ revenue lines BJ prices and runs. Archive compounding is the institutional moat, not seasonal deliverable. Sources: KOTS_LANE_B_ROLE.md, KOTS_FOR_DAD_COVER.md.

**D-007: KOTS Sponsorship Architecture (locked)**
5-tier model: CROWN $5K / COURT $2.5K / SIDELINE $1K / COMMUNITY $300 / IN-KIND. A la carte add-ons. Sponsor outreach owned by school committee (not Eric/BJ). Price authority gates on dad confirmation. Renewal window: deliver assets within 1 week post-event, renew conversation immediately with "here is your year, hold your spot for next year." Sources: KOTS_SPONSOR_PACKET.md, KOTS_SPONSOR_MEDIA_DELIVERABLES.md.

**D-008: KOTS Gallery and Media Delivery Architecture**
Six audience lanes: coaches/teams (48-72 hr, recruiting-critical), players/families (jersey-searchable, monetization gated 2 weeks post-event), sponsors (proof sets within 1 week), tournament archive (curated), social real-time (nightly exports), internal intake (raw never escapes 00_INBOX_RAW/). Reusable annual infrastructure: swap year + reload team/sponsor list, structure identical year-over-year. Source: KOTS_GALLERY_DELIVERY.md.

**D-009: KOTS Post-Event Recap as Institutional Artifact**
Recap distributes across 4 surfaces: public site (SEO), sponsor PDFs (renewal driver), social carousel/reel, internal archive. Timing: champion post night-of, social series days 1-5 of next month, sponsor deliverables week 1, site/archive week 2. Each recap seeds the next year (champion roll grows, archive thickens, sponsor proof drives renewals). Source: KOTS_POST_EVENT_RECAP.md.

**D-010: Soul ID Training Protocol (identity-locked generation)**
5-20 face photos (varied angles, no sunglasses, no filters) trigger CLI workflow. Proof artifact: soul reference ID + training cost in receipt file. Downstream: --soul-id flag on text2image_soul_v2 and soul_cinematic. Photo source files gitignored; only receipt/audit trail tracked. Anti-AI-on-client rule unchanged: soul training is internal concept-film work, not client-facing. Source: soul_id_op_refs/README.md.

**D-011: v3 LUXURY Python Pipeline Quality Ceiling**
rawpy + numpy + OpenCV achieves 75-85% fidelity to Lightroom native. Tone curves track tightly (~95%). HSL range mapping is the constraint (OpenCV HSV vs. Lightroom proprietary blend). The gap is not a blocker if operator approves quality floor. Engine v2 closes via texture/clarity passes. v3 LUXURY is now code-portable. Source: Phase 2a Sandbox Manifest.

**D-012: SNIPED Content Philosophy (locked authority spec)**
Photography is the entry point; the actual product is methodology, taste, direction, access, infrastructure, authority, IP, network, and media leverage. Negative space defines the brand. 5 content categories (Commercial / Authority / Cultural Documentation / Art Series / BTS-Process) feed each other across time. Commercial revenue funds the compounding engine. 7-filter decision gate before posting. 10-year test filters every output. Sources: SNIPED_CONTENT_PHILOSOPHY.md, SNIPED_OS_OPERATING_BRIEF.md.

**D-013: SNIPED Video Philosophy (6 formats, locked)**
Video serves stills, not algorithm. Stills are primary deliverable; video documents the making. Exception: Cultural Documentation Essays (Year 2+) are video-primary. Pacing: 6-12 cuts/min (Cultural Doc, Annual) vs. 15-22 cuts/min (Direction Stack POV). Sound = 30-50% structural weight. "Never Happens" checklist: 20 banned patterns (drum-hit cuts, POV titles, talking-head BJ, CapCut transitions, fake film grain, teal-orange-grain-LUT presets). Editor executes doctrine; BJ briefs and approves. Source: sniped_video_philosophy.md.

**D-014: Chapter Rollout Doctrine (locked 2026-05-12)**
One universal chapter formula for all subjects. Build frame count drives rollout length (1 look = 3 posts; 2 looks = 4 posts; 3+ looks = 5 posts max). Mandatory elements: Composite HERO (one per chapter), Chapter Card (B&W, IG collab post). Breathing gaps: 1-3 days per chapter type; 5-7 days for heavy chapters. 50% chapter content cap per 30-day window. Card anatomy locked (paper warm masthead #F5EFE6, Playfair Display Black wordmark, editorial chapter line, B&W at -1 saturation / +0.08 contrast / +0.02 exposure). Source: Chapter Rollout Doctrine v1.

**D-015: Abloh Design Principles (7 canon rules for operator optionality)**
(1) Find design language DNA via earliest creative memories. (2) 3% editing: slight modification of existing forms. (3) Output must have reason to exist beyond consumption. (4) Tourist meets Purist: knowledge serves collective, not self. (5) Work-in-progress releases iteration; perfectionism paralyzes. (6) Lineage is infrastructure: position inside art history, not outside it. (7) Use factories as suppliers for art. Maps directly to SNIPED's quiet luxury restraint, Lineage Doctrine, and scene-density thinking. Source: Virgil Abloh Harvard GSD Lecture Transcript.

**D-016: Leibovitz Methodology (concept-first directing)**
Four load-bearing criteria: Narrative (8.8), Signature (8.6), Pose (8.5), Composition (8.3). Depth consistently low (5.9), accepted as cost of body-environment integration on one plane. Starting point: thesis statement before palette lock. Subject as co-conspirator. Art-historical reference as directing tool (Vermeer, Sargent, Renaissance quotations). Most-copied mistake: imitators reproduce warm light and miss the concept. Borrow: concept-first reflex + body-in-environment. Do not borrow: painterly grade (muddies SNIPED color-blocking). Source: Study_AnnieLeibovitz.md.

**D-017: SNIPED Operating Brief v1.2 (primary spine doc)**
Three-engine simultaneity: Revenue (paid shoots + Reset ladder), Audience (IG + LinkedIn POV), Reputation (community/promoters/cultural doc). IG is co-equal to LinkedIn, not optional. Direction Stack protocols are the IP moat, not photos. Offer ladder: Reset $1,500 / Sprint $750 (warm only) / Op Kit $3-8K / Brand System $10K+. VIB method: static Figma board, DM under 80 words, Loom escalation for high-intent, animated content post-conversion only. Field engineer income floor: $102K. Edit window is the real bottleneck. Source: SNIPED_OS_OPERATING_BRIEF.md v1.2.

**D-018: Market Intelligence (corpus-validated, 332K+ words)**
Four photographer market layers: commodity / aspirational-middle / specialist / named. 10 anti-patterns in unsuccessful operators. Three trust loops: teaching loop, body-of-work loop, founder-network loop. Anti-AI positioning is appreciating (not defensive) in 2026: move from parenthetical to primary positioning lever in all copy by Q3. Pricing hold: corpus screams that photographers who survive held pricing through pressure. Platform: LinkedIn = buyer surface; Threads = peer-validation (not buyer space). Source: MARKET_INTELLIGENCE.md.

**D-019: Memory Snapshot Discipline**
43 live memory files in ~/.claude/projects/-Users-sniper/memory/ (gitignored, auto-loaded). Backup: copy folder to dated zip, store on private cloud + USB. Restore: copy folder back. State on disk = state exists; lost memory folder is real loss. project_sniped_spine.md employer-clean guardrail: raw content off-git. Source: MEMORY_SNAPSHOT/README_MANIFEST.md.

**D-020: SNIPED SEO and AI Visibility Strategy**
AI search (AEO/GEO) is a distinct visibility lever separate from traditional rankings. Three pillars: Structure, Authority, Presence. Princeton GEO research: statistics +37%, sources +40%, quotes +30%, keyword-stuffing -10%. Platform-specific: Google Overviews, ChatGPT, Perplexity, Claude, Copilot citation behaviors differ. E-E-A-T signals align with Trust Equation. Schema markup + structured data align with photography theory (ambiguity of photograph + metadata as context). If SNIPED ships portfolio + Direction Stack book, run AI Visibility Audit on snipedmedia.com first to baseline citations. Source: website-seo.md.

---

## DECISION JOURNAL (batch 010)

**DJ-010-01: KOTS Sponsor Outreach Timing**
Outreach owned by school committee (not Eric/BJ), starts Oct 1 2026, closes by Dec 1. Committee chair or school revenue officer is the task owner, not Eric. Decouples Eric from sponsor-hunting loop.

**DJ-010-02: KOTS Sponsorship Authority Gate**
Price tiers are not final until Eric confirms authority to negotiate and money structure is set (KOTS System doc sections 6 and 7). Contact line must be updated if Principal or committee chair holds authority (not Eric solo). Doc does not ship until gate clears.

**DJ-010-03: KOTS Domain Decision Pending**
Real domain vs. temp free URL must be decided before QR card print/distribution. Locks site phase 1 deploy approval.

**DJ-010-04: KOTS Site Phase 1 Placeholder Audit Required**
Registration target, credits, photo clearance, 2026 tournament dates, dad contact, entry fee, team list must be filled before deploy. Placeholder audit is a blocker.

**DJ-010-05: Family Monetization Gate**
Family gallery monetization pricing/permissions are a gated business decision set 2 weeks post-event, not automatic. Public site hosts curated best-of, not full take.

**DJ-010-06: Anti-AI Copy Register Upgrade**
Move anti-AI from parenthetical to primary positioning lever in all copy (Carrd, LinkedIn POV, VIB captions, Op Kit MSA, Day-30 pitch). Timing: now.

**DJ-010-07: LinkedIn POV Cadence**
Minimum 3/week (not 1/week). Exposure compounding mechanic + broadcast-not-virality pattern both require this frequency. If broadcast stays 100 followers, Substack deferral becomes permanent deferral.

**DJ-010-08: Direction Stack Book Launch Timing**
Do not accelerate before 3-5 Resets are closed. Market Intelligence Section 11 Implication 9 warns against workshop-rescue before body of work is real. Q3 2026 timing confirmed safe.

**DJ-010-09: v3 LUXURY Python Pipeline Operator Decision**
The 15-25% gap between Python translation and Lightroom native is not a blocker if operator approves quality floor. Operator review required: side-by-side comparison vs. Lightroom reference before production deployment.

**DJ-010-10: HIGH_LEVEL_CONVOS Extraction Gate**
File staged at raw/07_CONTENT/high_level_convos.docx (684,626 words, SHA256 verified). Extraction and chunking gated on operator authorization. Bible firewalled (not staged). Total chunks remain 1,430 (no creep).

**DJ-010-11: Whoopi Recreation Test (Leibovitz Validation)**
Week 6 checkpoint: name thesis statement before palette lock, identify art-historical reference, pose subject inside reference, body+environment on one compositional plane. Rerun 8-criteria audit on output. Strong scores expected: narrative, signature, pose, composition. Weak depth (5.9) is acceptable per Leibovitz precedent. Do not import warm painterly grade.

**DJ-010-12: KOTS Fee Gate**
Committee approval of BJ's production fee number is the only remaining action gate for KOTS Lane B. Everything else is BJ's operation. EIN correction gate blocks payment infrastructure; fee settlement deferred until EIN/147C resolved.

**DJ-010-13: CURRENT_OPERATOR_REALITY_BRIEF Guardrails**
Do not close on SNIPED Media as final vessel. Do not assume Baseplate is locked. Do not force photography, AI, or consulting as the answer. Remain in hypothesis-generation mode until market signal is clear. Keep building backend (Claude Code OS, field-operator intelligence, pain observation).

---

## MASTER-DOCTRINE ADDITIONS

**MDA-001: Fulfillment-as-Renewal (new)**
Post-delivery asset bundle is the renewal closing move. Proof + real numbers + branded recap replaces re-selling. Pairs with hospitality layer and status psychology. Applies to SNIPED client work, KOTS sponsors, any recurring client relationship.

**MDA-002: Abloh Output Reason Gate (new)**
Every output answers: does it have reason to exist? Does it serve the collective, not self? Gates consumption-cycle thinking. Parallel to SNIPED Execution Governor "does this thicken the scene?"

**MDA-003: Lineage as Infrastructure (reinforced + formalized)**
Position inside art history (or cultural tradition), not outside it. Mentorship (dead, peer, younger) is design discipline. Abloh's framework formalizes what the Lineage Doctrine states operationally: the work documents from inside. Add: "knowledge serves the collective" as a mission-check for institutional work (KOTS principal conversation frame).

**MDA-004: Concept-First Before Palette-First (Leibovitz import)**
Name the thesis statement before locking palette on any portrait or chapter shoot. Identify art-historical reference (optional). Pose subject inside the reference. This is a pre-shoot reflex, not a creative exercise. SNIPED leads with monochromatic palette discipline (palette-first); import concept-first as the upstream step that makes palette meaningful.

**MDA-005: Video Pacing as Metric (quantified)**
6-12 cuts/minute for Cultural Doc and Annual formats. 15-22 cuts/minute for Direction Stack POV. Creator-reel default is 25-40 cuts/minute. Refusal of creator-reel tempo is now a named metric, not just a vibe. Sound = 30-50% structural weight; ambient capture + voiceover desynchronization are structural, not optional polish.

**MDA-006: AI Visibility as Distinct Distribution Channel (new)**
AI search (Perplexity, Claude, ChatGPT, Google Overviews) operates on citation-based visibility, not ranking. Schema markup + structured data + statistics + quotes + source attribution drive AI citations. Track SNIPED citation rate monthly as a scene-density signal (which LA founder circles recognize SNIPED). LinkedIn posts should embed structured data for AI citation. This is a distribution partner for authority positioning, not a replacement for traditional SEO.

**MDA-007: Archive as Institutional Moat (reinforced)**
One growing archive, improving website, sponsor proof that actually ships = the institutional moat. Applies to KOTS (50-year archive compounds), SNIPED (10-year body-of-work arc), Baseplate (founder journey documentation). Archive equity is not seasonal refresh; it is the compounding asset that makes renewal, authority, and premium pricing defensible.

---

## SKILLS TO EXTRACT

**SE-001: sniped-chapter-rollout**
Inputs: subject name, look count, environment assignment from 7-rotation. Outputs: post sequence with captions, breathing gap calendar, HERO composite brief, Card production brief (Figma template variant selector). Triggers on any new subject intake.

**SE-002: sniped-card-production**
Inputs: source image path, chapter number, subject name, environment label. Outputs: Figma Card variant spec (masthead color, wordmark, editorial line, desaturation params, hairline/imprint). Maps to template at figma.com/design/AiMtRfT8W33yZRf4khjnds. Automates 3-5 min production step per card.

**SE-003: sniped-video-philosophy**
Reference skill for briefing motion work. Inputs: shoot date, format type (6 options), editor assignment. Outputs: editor brief template filled (Section 12 of doctrine), "Never Happens" checklist pre-flight, platform spec (aspect ratio, length, cadence). Deployed when BJ or editor needs to brief a new video piece, or when motion work needs doctrine review.

**SE-004: leibovitz-concept-first-audit**
Pre-shoot reflex skill. Inputs: subject name, shoot brief. Outputs: thesis statement (1 sentence), art-historical reference (optional), pose architecture note, integration method (body+environment or SNIPED studio clinical), post-shoot 8-criteria audit rubric (narrative, signature, pose, composition, light, edit, depth, concept delivery). Reusable on SNIPED shoots, KOTS founder sessions, any portrait.

**SE-005: kots-gallery-delivery**
Inputs: shoot date, coach roster, sponsor list, site curation criteria. Outputs: pre-built folder tree, naming templates, timing schedule (social nightly, coach 48-72 hr, sponsor 1 week, archive 2 weeks), reuse checklist for annual reload. Annual infrastructure skill; swap year + reload lists, structure identical year-over-year.

**SE-006: sniped-ai-visibility-audit**
Inputs: domain (snipedmedia.com), target AI platforms. Outputs: baseline citation report across Google Overviews, ChatGPT, Perplexity, Claude, Copilot; schema markup gaps; structured content pattern recommendations; monthly tracking setup. Trigger: before Direction Stack book launch and quarterly thereafter.

**SE-007: rawpy-batch-develop (candidate, Phase 2)**
Inputs: CR3 source folder, XMP preset file, quality floor approval (operator gate). Outputs: batch-developed TIFFs at 75-85% Lightroom fidelity, metadata JSON per file, SHA256 integrity log. Production-lock only after operator side-by-side review of Python vs. Lightroom reference.

---

## CONTRADICTIONS FLAGGED

**CF-001: NEXT_ACTION.md staleness vs. execution governor discipline**
NEXT_ACTION.md is 5+ days old as of batch read (Kennedie shoot listed as upcoming; shoot completed 2026-05-30). Execution Governor requires staleness trigger at >24h. The doc that houses the governance rule for freshness is itself stale. Not a doctrine contradiction, but an operational discipline failure. Resolution: read CURRENT_STATE.md to establish actual next action; treat NEXT_ACTION.md as expired.

**CF-002: CURRENT_OPERATOR_REALITY_BRIEF vs. OS architecture locks**
The brief (2026-06-02) explicitly states: do not close on SNIPED Media as final vessel, do not assume Baseplate is locked, do not force photography or AI as the answer. This is in tension with the "Repetition over Novelty / Architecture is built / Next 90 days are reps" lock (2026-05-12) and the SNIPED_OS_OPERATING_BRIEF v1.2 as the canonical spine. If the operator is still in hypothesis-generation mode (per the brief), the existing architecture and locked doctrine may be premature commitments. This is a genuine contradiction requiring operator resolution. Two possible readings: (a) the brief is a self-permission-slip for exploratory thinking while the OS continues running in parallel; (b) the brief signals architecture is not as locked as the May 12 locks suggest. Flagged for explicit operator decision.

**CF-003: KOTS contact authority ambiguity**
KOTS_SPONSOR_PACKET.md lists Eric Jones (eric.jones@marion.k12.fl.us) as the primary sponsor contact. KOTS_INSTITUTIONAL_REFRAME.md and KOTS_FOR_DAD_COVER.md both establish that the school committee/Principal model should be the operating governance. If sponsorship authority has moved to a committee chair or school revenue officer, the contact line is wrong. No resolution yet: blocked on Eric confirming authority structure. Flagged as a live gap in the sponsor packet before external send.

**CF-004: LinkedIn cadence discrepancy**
SNIPED_CONTENT_PHILOSOPHY.md states 1 LinkedIn POV/week (Tue/Thu 7-9 AM PT) as the cadence target. STRATEGIC_PRINCIPLES.md (Section MASTER-DOCTRINE DELTA) states LinkedIn POV cadence should be minimum 3/week. Reconciliation: 1/week is the Phase 1 conservative floor given field-engineer constraint; 3/week is the broadcast-compounding optimal. The minimum-viable cadence for Phase 1 must be explicitly chosen and locked. Flagged for operator decision.

---

## NEW POSSIBILITIES OPENED

**NP-001: Baseplate as Institutional Event Systems Builder**
KOTS governance architecture (5-tier sponsorship, media delivery, gallery monetization, booster club, revenue share) is a repeatable system. If Baseplate takes advisory/operational role for similar institutional events (tournaments, conferences, school programs), sponsorship sales + fulfillment becomes a profit center or subcontract opportunity. The KOTS build is the proof-of-concept.

**NP-002: Python rawpy Pipeline as Track B Creative Engine**
v3 LUXURY at 75-85% fidelity to Lightroom native opens a code-portable batch development path. If operator approves quality floor, SNIPED can batch-develop full shooting sessions without Adobe/Lightroom in the runtime stack. Supports downstream decisions on dependency architecture and potential editorial automation for high-volume shoots.

**NP-003: AI Citation as Brand Distribution Channel**
SNIPED authority assets (Direction Stack, cultural documentation, methodology articles) can generate AI citations across Perplexity, Claude, ChatGPT, Google Overviews. Monthly citation rate tracking becomes a proxy for brand penetration in specific LA cultural circles, independent of follower counts. This is a scene-density measurement tool, not just an SEO metric.

**NP-004: Concept-First Directing as Teachable IP (Baseplate curriculum)**
The Leibovitz 8-criteria audit + Abloh 3% editing + thesis-statement-before-palette reflex are teachable frameworks. Baseplate curriculum could include a "Mentorship Architecture" unit using Abloh's mentor-list methodology (Corbusier, Donald Judd, Peter Saville, Rem Koolhaas) as the model. Students build their own lineage map + directing audit tool.

**NP-005: KOTS Archive as Cultural Documentation Asset**
50+ years of tournament records, NBA alumni lineage (Embiid, Howard, Brown; coaches Mazzulla, Hurley), and Marion County school infrastructure constitute a pre-existing cultural documentation archive. A Cultural Documentation Essay (SNIPED video format 3) anchored to Kingdom of the Sun aligns SNIPED's reputation engine with KOTS institutional positioning simultaneously.

**NP-006: Operator Reality Hypothesis Space (pre-architecture)**
The CURRENT_OPERATOR_REALITY_BRIEF opens a hypothesis space that is explicitly not photography-only: AI tools for field engineers, documentation infrastructure, local-business AI enablement, operator image systems, planning intelligence, service automation, hybrid consulting. The Claude Code OS being built is itself a proof-of-concept that the operator can build leverage-layer systems. If the system is the product (per SNIPED Content Philosophy), the OS build itself could become an offer to other field engineers or operators.

**NP-007: Sponsor Renewal Engine as Recurring Revenue Model**
KOTS_SPONSOR_MEDIA_DELIVERABLES.md establishes a fulfillment-as-renewal mechanic that generates $10-15K/year in repeatable sponsorship revenue (3x COURT + 1x COMMUNITY + add-ons) if the committee executes outreach and the school owns the relationship. This is non-project-dependent recurring revenue anchored to an annual institutional event, independent of BJ's active production capacity.
