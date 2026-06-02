#!/usr/bin/env python3
"""
BATCH_007 chunker · locked doctrine + SOPs + working drafts + outreach/delivery/content/commercial operator docs

Reads 01_KNOWLEDGE_BASE/batches/batch_007_extracted/ (55 files) and emits
01_KNOWLEDGE_BASE/batches/BATCH_007_CHUNKS.jsonl with the canonical 12-field schema.

Target: ~128 chunks (range 115-135).
  - 14 doctrine sources -> ~37 chunks (P1)
  - 13 production SOP sources -> ~29 chunks (P2)
  -  7 outreach SOP sources -> ~16 chunks (P3)
  - 11 delivery sources -> ~13 chunks (P4)
  -  7 content sources -> ~26 chunks (P5)
  -  3 commercial singletons -> ~7 chunks (P6)
  Total: ~128

Approved 9-domain enum for BATCH_007 (BATCH_007_PLAN.md §9 · operator approval applied):
  EXISTING: operator-doctrine, operator-process, production-sop, outreach-sop,
            aesthetics, content-strategy, commercial-architecture
  NEW (approved): delivery-sop

STALE-FLAG tags applied per BATCH_007_PLAN.md §5:
  - legacy-adobe-portrait-pending-sweep
  - stale-hero-count-8-vs-10-12
  - stale-phase-b-trigger-3k-vs-2k
  - legacy-language-sweep-pending
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
EXTRACTED = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "batch_007_extracted"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_007_CHUNKS.jsonl"

BATCH_ID = "BATCH_007"
AUTHOR_BJ = "BJ / SNIPED Media"

chunks = []
chunk_id_counter = 0


def add_chunk(source_title, source_file, domain, concept, summary, usable_principle,
              sniped_relevance, direct_quotes, tags):
    global chunk_id_counter
    chunk_id_counter += 1
    chunks.append({
        "chunk_id": f"BATCH_007_{chunk_id_counter:03d}",
        "batch_id": BATCH_ID,
        "source_title": source_title,
        "source_file": source_file,
        "author": AUTHOR_BJ,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": usable_principle,
        "sniped_relevance": sniped_relevance,
        "direct_quotes": direct_quotes,
        "tags": tags,
    })


# ===========================================================================
# P1 · Locked doctrine · 14 sources · ~37 chunks
# ===========================================================================

# CANONICAL_TRUTHS.md · 188L · 3 chunks
add_chunk(
    source_title="Canonical Truths · SNIPED Media OS",
    source_file="brief__canonical_truths.md",
    domain="operator-doctrine",
    concept="The 12 Canonical Truths · highest-tier doc · loaded at every session start",
    summary=(
        "The 12 locked truths that override all other docs on conflict. Anchored 2026-05-06. "
        "Truth 1: three engines (Revenue / Audience / Reputation), not two. Truth 2: Instagram is "
        "co-equal with LinkedIn (cultural gravity vs business authority). Truth 3: lane is premium "
        "AND accessible, not expensive and inaccessible. Truth 4: delivery philosophy is controlled "
        "abundance (60-100 proof + 10-12 Hero + 30-40 Select + upgrade paths). Truths 5-12 cover "
        "operator coding, methodology moat, body-of-work cadence, the locked $1,500 Reset floor, "
        "Cultural Doc as compounding asset, end-to-end control, refusal as positioning, the "
        "Direction Stack as proprietary methodology, and Lock 10 (architecture is correct · "
        "execution is the only frontier)."
    ),
    usable_principle=(
        "When a doc contradicts a canonical truth, the canon wins until the other doc is updated. "
        "Read this file at every session start. Never relax any of the 12 truths."
    ),
    sniped_relevance=(
        "The strategic spine. Every SNIPED operating decision tests against these 12. This is the "
        "doc the sniped-canonical-truths skill (B6) reads at invocation."
    ),
    direct_quotes=[
        "These 12 truths override all other docs where they conflict.",
        "The lane is NOT $5,000 portrait sessions for celebrities. The lane is also NOT $300 commodity headshots.",
    ],
    tags=["canonical-truths", "operator-doctrine", "spine", "read-at-session-start", "lock-10"],
)
add_chunk(
    source_title="Canonical Truths · the three-engine architecture",
    source_file="brief__canonical_truths.md",
    domain="operator-doctrine",
    concept="Three engines simultaneously · Revenue + Audience + Reputation · with phase-shifted weights",
    summary=(
        "SNIPED runs three distinct engines, each with its own mechanics, metrics, and surfaces. "
        "Revenue Engine: paid shoots (Reset / Sprint / Op Kit / Brand System / Pixieset upsell) · "
        "the cash flow layer. Audience Engine: Instagram + BTS + LinkedIn POV · the cultural gravity "
        "/ discovery layer. Reputation Engine: community work + artists + promoters + LA access + "
        "Cultural Doc + founder/operator trust · the named-figure layer. Phase 1 lean override "
        "prioritizes Revenue; Phase B+ expands Audience and Reputation."
    ),
    usable_principle=(
        "Never collapse the three engines into one. Each has its own KPI and time budget. The "
        "previous Engine A/B framing flattened Audience and Reputation and is deprecated."
    ),
    sniped_relevance=(
        "Anchors the SNIPED operating model. The 3-engine mapping ties to the B4 STRATEGIC_PRINCIPLES "
        "Section 6 three-engine-to-source mapping (Trust Equation / Hit Makers / Status Anxiety)."
    ),
    direct_quotes=[
        "Audience is what someone sees scrolling; Reputation is what someone says about SNIPED when SNIPED isn't in the room.",
    ],
    tags=["three-engines", "operator-doctrine", "revenue-engine", "audience-engine", "reputation-engine", "phase-shift"],
)
add_chunk(
    source_title="Canonical Truths · the locked $1,500 floor + controlled abundance",
    source_file="brief__canonical_truths.md",
    domain="operator-doctrine",
    concept="Reset $1,500 floor + delivery philosophy · controlled abundance not scarcity, not chaos",
    summary=(
        "The lane is premium AND accessible. Reset is $1,500 cold quote, Sprint is $750 warm-network "
        "only, Op Kit $3-8K, Brand System $10K+. Delivery model: 60-100 frame curated proof gallery, "
        "10-12 Hero edits (full clinical retouch), 30-40 Selects (color-graded social-utility), "
        "upgrade paths (Select-to-Hero $60 within 14-day window). Not one-image scarcity, not "
        "raw-dump chaos. Refusal as positioning: saying no to off-lane shoots is what defines the lane."
    ),
    usable_principle=(
        "Floor holds at $1,500. Scope flexes, price does not. Sprint is NEVER cold-pitched · only "
        "warm-network via Notion CRM path. Delivery follows the locked HERO/SELECT/PROOF 3-tier model."
    ),
    sniped_relevance=(
        "The commercial backbone. Pairs with B3 Enns pricing canon + B4 9-factor founder purchase "
        "decomposition + B6 sniped-pricing-decision skill."
    ),
    direct_quotes=[
        "Pricing reflects this: the Reset at $1,500 (the cold quote)",
        "Curated proof gallery (60-100 frames, batch-graded)",
    ],
    tags=["reset-floor", "operator-doctrine", "controlled-abundance", "hero-select-proof", "scope-flexes-price-holds"],
)

# THE_SPINE.md · 354L · 4 chunks
add_chunk(
    source_title="THE SPINE · portable continuity doc",
    source_file="brief__the_spine.md",
    domain="operator-doctrine",
    concept="THE SPINE · paste-into-any-AI portable doc that restores full SNIPED operating context",
    summary=(
        "The everlasting portable doc. Sections 1-16: WHO (operator identity), 12 canonical truths, "
        "meta-thesis (locked 2026-05-07), locked visual direction (2026-05-12), 10 protocols (Direction "
        "Stack), VIB structure, outreach math + phase gates, casting call doctrine, LinkedIn comment "
        "execution, SNIPED OS craft layer, 7 composite environments, voice rules (LIFETIME locked · "
        "no em-dashes), continuity protocol, key relationships, active prospects, deep references."
    ),
    usable_principle=(
        "Paste THE SPINE into any AI session that doesn't have SNIPED auto-memory loaded. The doc "
        "restores 16 sections of operating context in one paste. Treat as the failover doc when "
        "Claude Code isn't available."
    ),
    sniped_relevance=(
        "The continuity primitive. Backs the project_sniped_spine_portable auto-memory record."
    ),
    direct_quotes=[
        "Paste into any AI (ChatGPT/Gemini) to restore full SNIPED operating context if Claude Code is unavailable.",
    ],
    tags=["the-spine", "operator-doctrine", "portable-doc", "continuity", "session-failover"],
)
add_chunk(
    source_title="THE SPINE · the 10 Direction Stack protocols",
    source_file="brief__the_spine.md",
    domain="operator-doctrine",
    concept="The 10 protocols that constitute the Direction Stack methodology",
    summary=(
        "The Direction Stack is 10 named protocols, not a 5-question diagnostic alone. The 10 protocols "
        "structure every Reset shoot from pre-shoot intake through post-delivery upsell. Each protocol "
        "names the locked behavior + the refuse-condition. Together they constitute the SNIPED "
        "methodology moat (what BJ owns forever per OPERATIONAL_BACKBONE Section 2 · the methodology-as-IP)."
    ),
    usable_principle=(
        "The Direction Stack is the methodology, not just the 5 questions. The 10 protocols are "
        "the full operating system. Reference them by number when designing or auditing a shoot."
    ),
    sniped_relevance=(
        "The methodology moat. Pairs with B6 sniped-direction-stack skill (which invokes against this) "
        "and B4 SYNTHESIS Moat 4 (methodology-as-IP)."
    ),
    direct_quotes=[],
    tags=["direction-stack", "10-protocols", "operator-doctrine", "methodology-moat"],
)
add_chunk(
    source_title="THE SPINE · VIB structure + outreach math + phase gates",
    source_file="brief__the_spine.md",
    domain="operator-doctrine",
    concept="VIB Visual Identity Brief structure + the locked 6/week cadence + phase-gate triggers",
    summary=(
        "VIB is a 2-panel Figma comparison frame (founder's current visual presence vs SNIPED-grade "
        "rebuild). 6 VIBs/week is the locked cadence (was 3/week in v1, recalibrated). Phase gates: "
        "Phase 1 = lean override (Revenue dominates); Phase B trigger = $2K MRR sustained 3 months "
        "(per 100Q audit recalibration, was $3K x 2); Phase C = scale-but-stay-small per Year-10 "
        "destination state of 4-7 person team."
    ),
    usable_principle=(
        "6 VIBs/week. Send only to ICP-qualified leads (4 of 4 criteria). Phase B trigger is $2K x 3 "
        "(not $3K x 2 from the legacy spine doc). Year-10 is 4-7 people · not bigger."
    ),
    sniped_relevance=(
        "The outbound execution math. Pairs with B6 sniped-vib-outreach skill + 03_OUTREACH/SOP_VIB_production."
    ),
    direct_quotes=[],
    tags=["vib", "outreach-math", "phase-gates", "6-per-week", "phase-b-trigger-2k-3-months"],
)
add_chunk(
    source_title="THE SPINE · voice rules + continuity protocol",
    source_file="brief__the_spine.md",
    domain="operator-doctrine",
    concept="Voice rules (LIFETIME locked) + continuity protocol for context restoration",
    summary=(
        "Voice rules: no em-dashes anywhere ever, no influencer-grade copy, no AI-fluff phrases "
        "(unlock potential / supercharge / dive deep / level up), severity over warmth as default "
        "register, refusal-positioning preferred over feature-marketing. Continuity protocol: at "
        "session start read CURRENT_STATE.md, ACTIVE_THREADS.md, SESSION_LOG.md tail; at session "
        "end update all three plus save drafted DMs. If state isn't on disk, it doesn't exist."
    ),
    usable_principle=(
        "Lifetime rule: no em-dashes in ANY output. Session start = read 3 ephemeral docs. Session "
        "end = update 3 ephemeral docs. State that isn't on disk doesn't exist."
    ),
    sniped_relevance=(
        "Voice + continuity discipline. Pairs with feedback_execution_mode auto-memory."
    ),
    direct_quotes=[
        "If state isn't on disk, it doesn't exist.",
    ],
    tags=["voice-rules", "no-em-dashes", "continuity-protocol", "session-discipline", "lifetime-locked"],
)

# THE_LINEAGE_DOCTRINE.md · 132L · 2 chunks
add_chunk(
    source_title="The Lineage Doctrine · LOCKED 2026-05-12",
    source_file="brief__the_lineage_doctrine.md",
    domain="operator-doctrine",
    concept="The 5 lineages SNIPED works FROM INSIDE · not single-visit cultural tourism",
    summary=(
        "5 lineages: (1) Black church; (2) HBCU intellectual; (3) Southern athletic; (4) Engineering "
        "/ first-gen professional; (5) LA Black founder culture. SNIPED documents from INSIDE these "
        "lineages, not from outside. Single-visit cultural tourism is REFUSED. The doctrine is the "
        "ethical defense against the categorical trap of Black-joy / Black-trauma / Black-culture "
        "as marketing categories."
    ),
    usable_principle=(
        "If a subject sits outside the 5 lineages, refuse. If a subject sits inside but requires "
        "single-visit tourism, refuse. The lineage doctrine governs Cultural Doc + subject selection. "
        "Specificity (specific people in specific institutions on specific days) is the ethical "
        "discipline."
    ),
    sniped_relevance=(
        "Cultural Doc lane backbone. Pairs with B6 sniped-art-series skill + B5 Day on personal "
        "documentary lineage + feedback_lineage_doctrine auto-memory."
    ),
    direct_quotes=[
        "Single-visit cultural tourism REFUSED.",
    ],
    tags=["lineage-doctrine", "operator-doctrine", "5-lineages", "cultural-doc", "anti-tourism", "specificity"],
)
add_chunk(
    source_title="The Lineage Doctrine · the categorical-trap defense",
    source_file="brief__the_lineage_doctrine.md",
    domain="operator-doctrine",
    concept="Refuse the categorical traps · specificity is the ethical discipline",
    summary=(
        "Black-joy as a marketing category flattens subjects into a saleable feeling. Black-trauma "
        "extracts pain for editorial credit. Black-culture generalizes specificity into a brand. "
        "SNIPED documents specific people in specific institutions on specific days. The 10-year "
        "test for cultural documentation: would the subject, 10 years from now, feel honored looking "
        "back at the frame and caption? If no, don't publish."
    ),
    usable_principle=(
        "Specificity over category. The 10-year subject-honor test is the publish gate."
    ),
    sniped_relevance=(
        "The ethical discipline. Pairs with B5 ethics domain (Sontag on non-intervention)."
    ),
    direct_quotes=[
        "Would the subject, 10 years from now, looking back at this frame and this caption, feel honored?",
    ],
    tags=["lineage-doctrine", "specificity", "10-year-test", "ethics", "anti-categorical-flattening"],
)

# OPERATING_LOCKS_2026-05-12.md · 188L · 3 chunks
add_chunk(
    source_title="Operating Locks · LOCKED 2026-05-12",
    source_file="brief__operating_locks_2026_05_12.md",
    domain="operator-doctrine",
    concept="The locked decisions register · 10 named locks governing 2026 operations",
    summary=(
        "10 locks anchored 2026-05-12. Lock 1: v3 LUXURY EDITORIAL is the only edit register. "
        "Lock 2: B&W Card dual-register (Chapter Card B&W, HERO posts color). Lock 3: Lineage Doctrine "
        "5 lineages · no single-visit tourism. Lock 4: scene-density thinking IN, audience-growth OUT. "
        "Lock 5: refusal-positioning. Lock 6: 6 VIBs/week cadence. Lock 7: Adobe Neutral base "
        "profile (NOT Portrait, NOT Standard). Lock 8: Reset $1,500 floor + scope flexes. Lock 9: "
        "Cultural Doc + Reputation Engine compounding. Lock 10: architecture is correct · "
        "execution is the only frontier · no new strategic frameworks."
    ),
    usable_principle=(
        "These 10 locks supersede any earlier doctrine. Lock 10 specifically bans architecture "
        "refinement · run the office, don't redesign it."
    ),
    sniped_relevance=(
        "The locked decisions register. Pairs with B4 operational-locks domain + B6 sniped-canonical-truths."
    ),
    direct_quotes=[],
    tags=["operating-locks", "operator-doctrine", "lock-10", "v3-luxury", "execution-only-frontier"],
)
add_chunk(
    source_title="Operating Locks · the maximum-by-default rule + carousel attribution",
    source_file="brief__operating_locks_2026_05_12.md",
    domain="operator-doctrine",
    concept="Maximum-by-default + carousel-attribution discipline · subordinate operating rules",
    summary=(
        "Every task ships max creative + strategic depth by default. No baseline-vs-premium tier "
        "offers. Just ship the best. Carousel attribution rule: never include carousel / social "
        "copy in SNIPED output without explicit attribution to a prior chat session that produced it."
    ),
    usable_principle=(
        "Default to the best output. Never tier outputs into baseline vs premium. Always cite "
        "prior chat sources for carousel material."
    ),
    sniped_relevance=(
        "Pairs with feedback_max_default + feedback_carousel_attribution auto-memory records."
    ),
    direct_quotes=[],
    tags=["operating-locks", "maximum-by-default", "carousel-attribution"],
)
add_chunk(
    source_title="Operating Locks · the 12 moat surfaces + 65+ named refusals",
    source_file="brief__operating_locks_2026_05_12.md",
    domain="operator-doctrine",
    concept="The 12 moat surfaces + 65+ named refusals · structural differentiation catalog",
    summary=(
        "12 moat surfaces: 65+ named refusals, longitudinal commitment, hybrid AI stance, methodology-as-IP, "
        "cross-medium reference depth, phase-trigger lifecycle, 3-engine model, network-as-inheritance, "
        "drift-detection nested loops, 9-photographer canon study system, cultural lineage authorship, "
        "10-year-test filter. The 65+ refusals are the named-no catalog that constitutes the lane."
    ),
    usable_principle=(
        "When auditing a decision, route it through the 12 moat surfaces · which surfaces does this "
        "decision strengthen, which does it weaken?"
    ),
    sniped_relevance=(
        "Pairs with B4 moat-surfaces domain (5 chunks · SYNTHESIS Section 11)."
    ),
    direct_quotes=[],
    tags=["operating-locks", "12-moat-surfaces", "65-refusals", "named-refusals"],
)

# THE_OPERATOR_CODED_DEFINITION.md · 141L · 2 chunks
add_chunk(
    source_title="The Operator-Coded Definition",
    source_file="brief__the_operator_coded_definition.md",
    domain="operator-doctrine",
    concept="What 'operator' specifically means to SNIPED · the coded identity claim",
    summary=(
        "Operator = builds the system, owns the leverage, refuses delegation of methodology + final "
        "review, ships the work end-to-end. NOT influencer (audience-as-output), NOT artist-purist "
        "(craft-without-distribution), NOT consultant (advice-without-execution). The coded definition "
        "anchors the SNIPED-Operator-coded identity claim · DTLA-anchored · Florida-raised · "
        "Engineering-trained · Methodology-first · Body-of-work-driven."
    ),
    usable_principle=(
        "When the question is about what SNIPED IS or who BJ is in the work, refer to the operator-coded "
        "definition. The identity claim is non-negotiable."
    ),
    sniped_relevance=(
        "The identity-spine doc. Pairs with B6 sniped-canonical-truths skill + B4 brand-psychology."
    ),
    direct_quotes=[],
    tags=["operator-coded", "operator-doctrine", "identity-claim", "un-delegate-ables"],
)
add_chunk(
    source_title="The Operator-Coded Definition · un-delegate-ables ledger",
    source_file="brief__the_operator_coded_definition.md",
    domain="operator-doctrine",
    concept="The un-delegate-ables · what only BJ does, ever",
    summary=(
        "Un-delegate-ables: methodology design + final review + pricing decisions + named-subject "
        "relationships + Direction Stack execution + Cultural Doc cadence + the spine update process. "
        "Everything else is operator-engine-extension (skills, assistants, automations). The ledger "
        "is the boundary between leverage and control."
    ),
    usable_principle=(
        "When designing leverage (skills, assistant SOPs, automations), check against the "
        "un-delegate-ables. If a proposed delegation crosses into the ledger, refuse."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-assistant-task-routing + the methodology-moat doctrine."
    ),
    direct_quotes=[],
    tags=["un-delegate-ables", "operator-coded", "operator-doctrine", "delegation-boundary"],
)

# LEAN_EXECUTION_AUDIT.md · 385L · 4 chunks
add_chunk(
    source_title="Lean Execution Audit · findings",
    source_file="brief__lean_execution_audit.md",
    domain="operator-process",
    concept="Lean audit findings · operator-process diagnostic snapshot",
    summary=(
        "The lean audit identifies where the SNIPED operating system has slack, drift, or "
        "premature optimization. Output: a list of overrides (VIB cadence raised to 6/week from "
        "3/week, Phase B trigger recalibrated to $2K x 3 from $3K x 2, Engine A/B model deprecated "
        "to three-engine model). The lean override is the Phase 1 default · prioritize revenue, "
        "compress non-load-bearing process, ship the named-recommendation list weekly."
    ),
    usable_principle=(
        "Run the lean audit before adding ANY new process. If the existing system has slack, fix "
        "that first. Override decisions are the canonical answer when older docs disagree."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-lean-audit skill + B4 100Q recalibration chunks."
    ),
    direct_quotes=[],
    tags=["lean-audit", "operator-process", "override-discipline", "phase-1-lean"],
)
add_chunk(
    source_title="Lean Execution Audit · the 100Q recalibration overrides",
    source_file="brief__lean_execution_audit.md",
    domain="operator-process",
    concept="The 100Q-driven overrides that supersede older spine docs",
    summary=(
        "Named overrides: VIB cadence 3->6/week, Phase B trigger $3K x 2 -> $2K x 3, Engine A/B "
        "-> three-engine model, Hero count 8 -> 10-12, Adobe Portrait -> Adobe Neutral base profile, "
        "Sprint $750 NEVER cold-pitched (warm-only via Notion CRM), Bishop Peters decommissioned "
        "as near-term anchor, Tally chapter intake parked (Mode 1 DM template wins), BASEPLATE "
        "spelling correction (was 'Bass Plate')."
    ),
    usable_principle=(
        "When a decision needs a number or a name, check the lean audit overrides FIRST · they "
        "supersede the legacy spine. Older docs that disagree are stale until swept."
    ),
    sniped_relevance=(
        "The recalibration roll-call. Pairs with B4 doctrine_conflicts_resolved + B4 SYNTHESIS contradictions."
    ),
    direct_quotes=[],
    tags=["lean-audit", "100q-recalibration", "operator-process", "override-list"],
)
add_chunk(
    source_title="Lean Execution Audit · the 2026 win conditions",
    source_file="brief__lean_execution_audit.md",
    domain="operator-process",
    concept="The 5 measurable 2026 win conditions",
    summary=(
        "2026 win conditions (5 targets): (1) 12 paid shoots completed; (2) $15K BASEPLATE firewall "
        "trigger reached; (3) 16 chapters published (chapter rollout doctrine cadence); (4) 5 named "
        "founder portraits delivered; (5) the Direction Stack book interim PDF shipped. Forbes 30 "
        "under 30 is the 2027 external-proof target · not 2026."
    ),
    usable_principle=(
        "These 5 targets are the 2026 measurable outcomes. Anything else in 2026 is non-load-bearing."
    ),
    sniped_relevance=(
        "Pairs with B4 100Q win conditions + Lock 10 (execution is the only frontier)."
    ),
    direct_quotes=[],
    tags=["lean-audit", "2026-win-conditions", "5-measurable-targets", "baseplate-firewall"],
)
add_chunk(
    source_title="Lean Execution Audit · the named-recommendation queue",
    source_file="brief__lean_execution_audit.md",
    domain="operator-process",
    concept="The weekly named-recommendation queue · what ships this week, parked, or killed",
    summary=(
        "The lean audit produces a weekly queue of named recommendations · ship-this-week (1-3 items), "
        "park (deferred but not killed), kill (decommissioned). The queue is the bridge between the "
        "doctrine layer and weekly execution. Monday Cockpit + Saturday Build Brief reference it."
    ),
    usable_principle=(
        "Maintain the named-recommendation queue weekly. Reference it in Monday Cockpit (this week's "
        "shipping) and Saturday Build Brief (this weekend's build cycle)."
    ),
    sniped_relevance=(
        "The operator-process bridge between doctrine and weekly execution."
    ),
    direct_quotes=[],
    tags=["lean-audit", "named-recommendation-queue", "operator-process", "weekly-cadence"],
)

# MONDAY_COCKPIT.md · 155L · 2 chunks
add_chunk(
    source_title="Monday Cockpit · weekly operator ritual",
    source_file="brief__monday_cockpit.md",
    domain="operator-process",
    concept="Monday cockpit · the weekly operator-start ritual that loads the work-week",
    summary=(
        "Monday morning ritual: 30-60 min. Load state (CURRENT_STATE + ACTIVE_THREADS + last week's "
        "SESSION_LOG tail), set 1-3 ship-this-week items from the named-recommendation queue, "
        "schedule the VIB-block windows (6 VIBs/week), confirm shoot bookings for the week, "
        "name the 1 thing that must happen for the week to be a win. Closes with a 10-year-test "
        "pass · does this week's work compound or just spin?"
    ),
    usable_principle=(
        "Every Monday: 30-60 min. Load state, name 1-3 ship items, schedule VIB blocks, name the "
        "one-thing-that-must-happen. Skip the ritual = drift."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-monday-cockpit skill + the operator-cadence layer."
    ),
    direct_quotes=[],
    tags=["monday-cockpit", "operator-process", "weekly-ritual", "ship-this-week"],
)
add_chunk(
    source_title="Monday Cockpit · the one-thing-that-must-happen filter",
    source_file="brief__monday_cockpit.md",
    domain="operator-process",
    concept="The one-thing filter · single load-bearing weekly outcome",
    summary=(
        "Each week names ONE thing that, if it happens, makes the week a win regardless of what "
        "else does or doesn't ship. The one-thing is usually a named external proof (a shoot delivered, "
        "a VIB acceptance, a published chapter, a named-figure conversation booked). Internal-only "
        "deliverables rarely qualify."
    ),
    usable_principle=(
        "Name the one-thing on Monday. By Friday, did the one-thing happen? Yes = win. No = audit "
        "what blocked it · the block is the operating intel for next week."
    ),
    sniped_relevance=(
        "Single-load-bearing-outcome discipline. Pairs with B2 Bryar/Carr single-threaded leadership."
    ),
    direct_quotes=[],
    tags=["monday-cockpit", "one-thing", "single-threaded-week", "operator-process"],
)

# SATURDAY_BUILD_BRIEF.md · 329L · 3 chunks
add_chunk(
    source_title="Saturday Build Brief · the build-cycle doc",
    source_file="brief__saturday_build_brief.md",
    domain="operator-process",
    concept="Saturday build brief · the weekend build-cycle that compounds infrastructure",
    summary=(
        "Saturday is the locked weekly build day · operator-infrastructure work, not client work. "
        "The brief structures 4-6 hours into focused build blocks · skill packs / SOPs / chapter "
        "cards / Direction Stack book chapters / automation blueprints / VIB Figma updates. The "
        "Saturday output is what compounds; Mon-Fri output is what cash-flows."
    ),
    usable_principle=(
        "Saturday = build, not ship. 4-6 hours focused. No client work, no email, no DMs. The "
        "compounding asset is built here."
    ),
    sniped_relevance=(
        "The operator-build cadence. Pairs with Saturday-as-deep-work principle + Bryar/Carr "
        "single-threaded leadership."
    ),
    direct_quotes=[],
    tags=["saturday-build", "operator-process", "build-vs-ship", "compounding-cadence"],
)
add_chunk(
    source_title="Saturday Build Brief · the priority-stack template",
    source_file="brief__saturday_build_brief.md",
    domain="operator-process",
    concept="Saturday priority stack · 3-tier build template",
    summary=(
        "Saturday priority stack: Tier 1 = the one named-build that ships this Saturday "
        "(load-bearing). Tier 2 = the named-build that ships this month (in-progress, not "
        "load-bearing this week). Tier 3 = the named-build that is queued (parked, ready to "
        "promote when Tier 1 ships). Saturdays alternate between code+content builds and "
        "system+doctrine builds."
    ),
    usable_principle=(
        "Saturday produces exactly 1 Tier-1 shipped artifact. Anything else is bonus. Tier-2 "
        "advances by some increment. Tier-3 stays parked until promoted."
    ),
    sniped_relevance=(
        "Tier discipline. Pairs with B2 Thiel narrow-monopoly + B4 Lock 10 (execution focus)."
    ),
    direct_quotes=[],
    tags=["saturday-build", "priority-stack", "tier-discipline", "operator-process"],
)
add_chunk(
    source_title="Saturday Build Brief · the close-out ritual",
    source_file="brief__saturday_build_brief.md",
    domain="operator-process",
    concept="Saturday close-out · session-save before exiting the build day",
    summary=(
        "End Saturday with a session-save: what shipped (Tier 1 artifact), what advanced (Tier 2), "
        "what's queued for next Saturday (Tier 3 promotion candidates). Update SESSION_LOG.md, "
        "ACTIVE_THREADS.md, MONDAY_COCKPIT.md so Monday loads the right state. The save is the "
        "continuity primitive."
    ),
    usable_principle=(
        "Never end Saturday without the session-save ritual. The save is what makes Monday possible."
    ),
    sniped_relevance=(
        "Continuity primitive. Pairs with feedback_execution_mode session-end protocol."
    ),
    direct_quotes=[],
    tags=["saturday-build", "session-save", "continuity-protocol", "operator-process"],
)

# SYSTEM_FINAL_STATUS.md · 340L · 4 chunks
add_chunk(
    source_title="System Final Status · doctrine snapshot",
    source_file="brief__system_final_status.md",
    domain="operator-doctrine",
    concept="System final status · canonical state of the SNIPED operating system as of locking date",
    summary=(
        "The system-final-status snapshot captures the SNIPED operating system at the canonical "
        "locking moment. Headers cover: identity claim, 3-engine architecture, locked offer ladder, "
        "Direction Stack methodology, VIB cadence, Lineage Doctrine, visual direction lock, "
        "production OS, delivery architecture v2, Cultural Doc lane, the 12 canonical truths, the "
        "10 operating locks, the 2026 win conditions, the named-refusals catalog."
    ),
    usable_principle=(
        "When the question is 'what is the canonical state of X right now?', SYSTEM_FINAL_STATUS "
        "is the answer. Treat as the single-paragraph orientation doc."
    ),
    sniped_relevance=(
        "The state-orientation doc. Pairs with B4 doctrine-meta domain."
    ),
    direct_quotes=[],
    tags=["system-final-status", "operator-doctrine", "state-snapshot", "doctrine-orientation"],
)
add_chunk(
    source_title="System Final Status · the canonical offer ladder",
    source_file="brief__system_final_status.md",
    domain="commercial-architecture",
    concept="Locked offer ladder · Reset / Sprint / Op Kit / Brand System + Strategic Free + Cultural Doc",
    summary=(
        "Offer ladder: Reset = $1,500 cold-quote 5-hour single-direction shoot (10-12 Hero + 30-40 "
        "Select + 60-100 Proof). Sprint = $750 warm-network only 2-hour single-direction shoot. "
        "Op Kit = $3-8K multi-direction + brand-system entry. Brand System = $10K+ multi-shoot "
        "campaign + Direction Stack consultation. Strategic Free = Community (institutional · "
        "$0 + paid family portraits) + Access (event coverage · $0 + commercial introduction). "
        "Cultural Doc = compounding-engine output, not a transactional offer."
    ),
    usable_principle=(
        "All 5 commercial tiers + Strategic Free + Cultural Doc are the full surface. Nothing else "
        "exists. Refuse $300 commodity headshots and $5,000+ celebrity sessions."
    ),
    sniped_relevance=(
        "The commercial backbone. Pairs with delivery_architecture_v2 + B6 sniped-pricing-decision skill."
    ),
    direct_quotes=[],
    tags=["offer-ladder", "commercial-architecture", "reset-1500", "sprint-750", "op-kit", "brand-system", "strategic-free"],
)
add_chunk(
    source_title="System Final Status · the named-refusals catalog (65+)",
    source_file="brief__system_final_status.md",
    domain="operator-doctrine",
    concept="The 65+ named refusals · what SNIPED specifically does NOT do",
    summary=(
        "65+ named refusals catalog (the named-no list). Categories: visual register (no teal/orange, "
        "no fake film grain, no Sedona dust, no influencer grading), commercial (no $300 headshots, "
        "no commodity packages, no agency-volume pricing), lane (no off-LA shoots, no off-lineage "
        "tourism, no celebrity-only work), production (no raw-dump delivery, no over-promised "
        "turnaround, no AI-generated identity), positioning (no founder-as-product flattening, no "
        "Black-joy/trauma/culture as marketing category), operations (no full-time hires before "
        "$15K BASEPLATE, no offices, no salesteam, no agency model)."
    ),
    usable_principle=(
        "Refusal as positioning · the 65+ named-no catalog is the lane. Each refusal is a load-bearing "
        "boundary. Cross a refusal = drift."
    ),
    sniped_relevance=(
        "Pairs with B4 moat-surfaces (refusal as #1 moat) + B3 Sax analog premium framing."
    ),
    direct_quotes=[],
    tags=["named-refusals", "65-refusals", "operator-doctrine", "refusal-positioning", "lane-discipline"],
)
add_chunk(
    source_title="System Final Status · BASEPLATE firewall + Year-10 destination",
    source_file="brief__system_final_status.md",
    domain="operator-doctrine",
    concept="BASEPLATE $15K firewall + Year-10 4-7 person team destination",
    summary=(
        "BASEPLATE = the $15K/month MRR firewall. Before BASEPLATE: lean override, no full-time "
        "hires, no offices, no agency expansion. After BASEPLATE: open hiring of operator-engine-extension "
        "roles (assistant, retoucher). Year-10 destination = 4-7 person team intentionally small · "
        "Jarvis Company-of-One discipline + Naval freedom-as-goal + Thorndike capital-allocation."
    ),
    usable_principle=(
        "Do not cross the BASEPLATE firewall before $15K MRR is sustained. Year-10 is 4-7 people, "
        "not bigger. Refuse the agency-scale temptation."
    ),
    sniped_relevance=(
        "Pairs with B3 Jarvis + B4 100Q Q83 dual-track + B4 100Q Q100 simplest-winning-SNIPED."
    ),
    direct_quotes=[],
    tags=["baseplate-firewall", "year-10-destination", "operator-doctrine", "4-7-person-team", "anti-scale"],
)

# OPERATOR_QUESTIONS_2026-05-13.md · 267L · 3 chunks
add_chunk(
    source_title="Operator Questions 2026-05-13 · question bank",
    source_file="brief__operator_questions_2026_05_13.md",
    domain="operator-process",
    concept="Operator question bank · the open + answered + escalated questions register",
    summary=(
        "The operator-question register is the running list of decisions awaiting input, decisions "
        "needing escalation (legal / accountant / Bishop conversations), and the answered-questions "
        "log. Used in weekly sessions to surface decision-blockers that have piled up. Question bank "
        "is operator-facing only · not in client-facing materials."
    ),
    usable_principle=(
        "Every operator question gets a status (open / answered / escalated / parked). Weekly "
        "review pulls open questions to the surface. Anything open for 4+ weeks gets force-decided."
    ),
    sniped_relevance=(
        "The decision-surface bridge. Pairs with B4 operational-locks + the lean execution audit."
    ),
    direct_quotes=[],
    tags=["operator-questions", "question-bank", "operator-process", "decision-surface"],
)
add_chunk(
    source_title="Operator Questions · the 2026-05-13 open list",
    source_file="brief__operator_questions_2026_05_13.md",
    domain="operator-process",
    concept="Snapshot of open operator questions as of 2026-05-13 (point-in-time)",
    summary=(
        "Open questions as of 2026-05-13: Direction Stack PDF canonical confirmation, OCR_RECOVERY "
        "authorization (4 photography sources blocked on ocrmypdf install), photographer films "
        "transcription authorization (8 mp4s blocked on Whisper), GetHookd source acquisition, "
        "13_OPERATING_DISCIPLINE PDF worksheet text-density check, brand-strategy mini-batch "
        "authorization, SOP_assistant_v3.docx vs .md dedupe."
    ),
    usable_principle=(
        "Point-in-time snapshot of open decisions. Use to track which questions still need operator "
        "input. Many of these unblock specific future batches."
    ),
    sniped_relevance=(
        "The blocker-tracking layer. Pairs with MASTER_CHUNK_MAP next_batch_candidates blocked queues."
    ),
    direct_quotes=[],
    tags=["operator-questions", "open-list", "blockers", "2026-05-13"],
)
add_chunk(
    source_title="Operator Questions · the force-decide rule",
    source_file="brief__operator_questions_2026_05_13.md",
    domain="operator-process",
    concept="Force-decide rule · 4-week timeout on any open question",
    summary=(
        "If a question stays open for 4+ weeks without movement, the operator force-decides at the "
        "next Monday Cockpit. Force-decision can be: answer it, kill it, or formally park it (with "
        "an explicit re-surface trigger). What can NOT happen: leaving the question silently open. "
        "Silent-open is drift."
    ),
    usable_principle=(
        "4-week timeout. Force-decide at week 5 Monday. Force-decide options: answer / kill / park-with-trigger."
    ),
    sniped_relevance=(
        "Anti-drift discipline. Pairs with B4 5-nested-drift-detection-loops + Lock 10."
    ),
    direct_quotes=[],
    tags=["operator-questions", "force-decide-rule", "anti-drift", "4-week-timeout"],
)

# PARTNERSHIP_PROTOCOL.md · 182L · 2 chunks
add_chunk(
    source_title="Partnership Protocol · the decision framework",
    source_file="brief__partnership_protocol.md",
    domain="operator-doctrine",
    concept="Partnership protocol · the gating framework for partnership / collab / joint-venture asks",
    summary=(
        "Partnership protocol: 4 gating questions. (1) Does this partnership strengthen the SNIPED "
        "methodology moat? (2) Does it cross the un-delegate-ables? (3) Does it sit inside the 5 "
        "lineages? (4) Does it strengthen scene-density in a specific LA cultural circle? If any "
        "answer is no, refuse. The protocol applies to every collab / co-production / institutional "
        "partnership ask."
    ),
    usable_principle=(
        "Run the 4 gating questions before agreeing to any partnership. 1 No = decline cleanly. "
        "Trade scope, never price. Don't be precious · SNIPED isn't too big for the program."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-partnership-protocol skill + feedback_referral_handling auto-memory."
    ),
    direct_quotes=[],
    tags=["partnership-protocol", "operator-doctrine", "4-gating-questions", "decline-cleanly"],
)
add_chunk(
    source_title="Partnership Protocol · referral handling",
    source_file="brief__partnership_protocol.md",
    domain="operator-doctrine",
    concept="Pearl-network referral handling · floor holds, scope flexes",
    summary=(
        "Referrals (including Pearl-network) get the same gating as cold leads but with warmer "
        "tone + faster decline-or-accept turnaround. The $1,500 floor holds. Scope flexes (fewer "
        "Heroes, shorter session, narrower direction) to fit a smaller budget if the lineage / "
        "scene-density fit is strong. Trade scope, never price."
    ),
    usable_principle=(
        "Referrals are not exemptions. Floor holds. Scope flexes. Decline cleanly when off-scope."
    ),
    sniped_relevance=(
        "Pairs with feedback_referral_handling auto-memory."
    ),
    direct_quotes=[],
    tags=["partnership-protocol", "referral-handling", "floor-holds", "scope-flexes"],
)

# recurring_checklists.md · 139L · 2 chunks
add_chunk(
    source_title="Recurring Checklists · daily + weekly rituals",
    source_file="brief__recurring_checklists.md",
    domain="operator-process",
    concept="Recurring daily + weekly operator-process checklists",
    summary=(
        "Daily checklist (Mon-Fri): morning state-load, VIB block (1-2 sent), CRM hygiene (assistant "
        "owns), end-of-day session log update. Weekly: Monday Cockpit (load week), Wed 1-hr lean "
        "audit (drift check), Saturday Build (4-6 hrs build day), Sunday rest (no SNIPED). The "
        "checklists are the operator-engine cadence."
    ),
    usable_principle=(
        "Daily + weekly checklists are not optional. Skipping checklists = drift. The cadence is "
        "the operating system."
    ),
    sniped_relevance=(
        "The operator-cadence baseline. Pairs with Monday Cockpit + Saturday Build Brief."
    ),
    direct_quotes=[],
    tags=["recurring-checklists", "operator-process", "daily-cadence", "weekly-cadence"],
)
add_chunk(
    source_title="Recurring Checklists · the Sunday rest discipline",
    source_file="brief__recurring_checklists.md",
    domain="operator-process",
    concept="Sunday rest · the rest-is-load-bearing rule",
    summary=(
        "Sundays are a no-SNIPED day. No emails, no DMs, no docs, no edits, no scheduling. Rest is "
        "load-bearing for the operator-engine quality. The discipline mirrors Bezos Day 1 (compound "
        "energy through rest) + Munger sit-on-your-ass investing (the right pace produces the right "
        "outcomes)."
    ),
    usable_principle=(
        "Sunday = no SNIPED, period. Schedule client work Mon-Sat only. Rest is the leverage."
    ),
    sniped_relevance=(
        "The operator-energy discipline. Pairs with B2 Bezos Day 1 + B2 Munger sit-on-your-ass."
    ),
    direct_quotes=[],
    tags=["recurring-checklists", "sunday-rest", "operator-process", "rest-is-load-bearing"],
)

# templates/monthly_constraint_audit.md · 160L · 2 chunks
add_chunk(
    source_title="Monthly Constraint Audit · template",
    source_file="brief__monthly_constraint_audit.md",
    domain="operator-process",
    concept="Monthly constraint audit template · what's bottlenecking the system this month",
    summary=(
        "Monthly audit template: identify the 1 named binding constraint this month (the one thing "
        "that, if relaxed, would unlock the most output). Constraints rotate: capital / time / "
        "skill / network / equipment / morale. The audit produces 3 outputs: the named constraint, "
        "the 1 named relaxation lever for next month, the named cost (what gets de-prioritized to "
        "relax the constraint)."
    ),
    usable_principle=(
        "Run the audit at month-end. Name ONE binding constraint. Name ONE relaxation lever. Name "
        "the cost. Anything else is dilution."
    ),
    sniped_relevance=(
        "Theory of Constraints applied to SNIPED operations. Pairs with B3 Holiday + Naval long-game."
    ),
    direct_quotes=[],
    tags=["monthly-constraint-audit", "operator-process", "theory-of-constraints", "1-binding-constraint"],
)
add_chunk(
    source_title="Monthly Constraint Audit · the cost-of-relaxation discipline",
    source_file="brief__monthly_constraint_audit.md",
    domain="operator-process",
    concept="Naming the cost · what gets deprioritized to relax this month's constraint",
    summary=(
        "Every constraint relaxation has a cost (time, attention, money, opportunity). The audit "
        "demands the cost be named explicitly. If the cost can't be named, the relaxation isn't real "
        "· it's wishful thinking. Examples: relaxing the time constraint costs Saturday build hours; "
        "relaxing the capital constraint costs the BASEPLATE firewall integrity."
    ),
    usable_principle=(
        "Name the cost before relaxing the constraint. If you can't name it, the relaxation isn't "
        "decided · it's daydreamed."
    ),
    sniped_relevance=(
        "Operator-decision honesty. Pairs with B4 anti-patterns catalog + B2 Munger inversion."
    ),
    direct_quotes=[],
    tags=["monthly-constraint-audit", "cost-of-relaxation", "operator-process", "decision-honesty"],
)

# templates/weekly_review.md · 124L · 1 chunk
add_chunk(
    source_title="Weekly Review · template",
    source_file="brief__weekly_review.md",
    domain="operator-process",
    concept="Weekly review template · Friday close-out · captures the week's signal vs noise",
    summary=(
        "Weekly review template (run Friday 4-5 PM): (1) Did the one-thing-that-must-happen happen? "
        "(2) What shipped vs what was named to ship Monday? (3) What's the operating intel from this "
        "week (drift signals, lock validations, named-refusals invoked)? (4) Next week's Monday-cockpit "
        "candidate one-thing. Output: a single short paragraph in SESSION_LOG.md."
    ),
    usable_principle=(
        "Friday weekly review = single short paragraph in SESSION_LOG. Never skip. Skipping = drift."
    ),
    sniped_relevance=(
        "The Friday close-out ritual. Pairs with Monday Cockpit (which loads Friday's output)."
    ),
    direct_quotes=[],
    tags=["weekly-review", "operator-process", "friday-close-out", "session-log"],
)


# ===========================================================================
# P2 · Production SOPs · 13 sources · ~29 chunks
# ===========================================================================

# casting_call_doctrine_v1.md · 375L · 4 chunks
add_chunk(
    source_title="Casting Call Doctrine v1",
    source_file="production__casting_call_doctrine_v1.md",
    domain="production-sop",
    concept="Casting call doctrine v1 · the 24/48/wardrobe/two-strike disciplines for collab shoots",
    summary=(
        "Casting call operating doctrine, MIGRATED 2026-05-12 from May 1-3 production retro. "
        "Disciplines: 24-hour confirmation, tier-2 standby pre-stage, wardrobe photo requirement, "
        "two-strike rule on no-shows, 48-hour MUA confirm, all production days defined BEFORE the "
        "form launches. Apply before any future casting call (next target: Sunday 5/17 shoot)."
    ),
    usable_principle=(
        "Locked v1 disciplines. Never run a casting call without confirming all 6 disciplines are in place."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-shoot-day-strategic-free + feedback_casting_call_doctrine auto-memory."
    ),
    direct_quotes=[],
    tags=["casting-call", "production-sop", "24-hour-confirm", "two-strike-rule", "tier-2-standby"],
)
add_chunk(
    source_title="Casting Call Doctrine · 24-hour confirmation + tier-2 standby",
    source_file="production__casting_call_doctrine_v1.md",
    domain="production-sop",
    concept="The 24-hour confirmation discipline + tier-2 standby pre-staging",
    summary=(
        "24-hour confirmation: every confirmed model must re-confirm 24 hours before the shoot. "
        "Non-response = drop to standby. Tier-2 standby: 2-3 backup models pre-staged with same "
        "wardrobe specs, ready to fill 4-hour window. Standby compensation: $0 if not called, "
        "$50 stipend if called inside 4 hours."
    ),
    usable_principle=(
        "24-hour confirm or drop. Always pre-stage tier-2 standby. Stipend the standby if called."
    ),
    sniped_relevance=(
        "Operationalizes the collab-shoot reliability discipline. Pairs with two-strike rule."
    ),
    direct_quotes=[],
    tags=["casting-call", "24-hour-confirm", "tier-2-standby", "production-sop"],
)
add_chunk(
    source_title="Casting Call Doctrine · wardrobe photo + 48-hour MUA confirm",
    source_file="production__casting_call_doctrine_v1.md",
    domain="production-sop",
    concept="Wardrobe photo requirement + 48-hour MUA confirmation",
    summary=(
        "Wardrobe photo requirement: every confirmed model submits photos of all wardrobe options "
        "48 hours before shoot. BJ approves wardrobe before shoot day · no day-of surprises. "
        "MUA 48-hour confirm: MUA confirms attendance + arrival time + supply check 48 hours before. "
        "MUA non-confirm = reschedule the shoot, not the MUA."
    ),
    usable_principle=(
        "No wardrobe photo = no slot. No MUA 48-hr confirm = reschedule, not replace."
    ),
    sniped_relevance=(
        "Wardrobe + MUA reliability discipline. Pairs with sniped-pre-shoot-prep skill."
    ),
    direct_quotes=[],
    tags=["casting-call", "wardrobe-photo", "48-hour-mua-confirm", "production-sop"],
)
add_chunk(
    source_title="Casting Call Doctrine · two-strike rule + production-days-locked",
    source_file="production__casting_call_doctrine_v1.md",
    domain="production-sop",
    concept="Two-strike no-show rule + production-days-locked-before-form-launch",
    summary=(
        "Two-strike rule: first no-show = warning + standby tier drop. Second no-show = permanent "
        "block. The rule applies across casting calls, not per-call. Production-days-locked: all "
        "shoot days are defined BEFORE the casting form launches. Operator does not let model "
        "availability set the schedule."
    ),
    usable_principle=(
        "Two strikes = out. Lock days first, then launch the form. Never let models set the schedule."
    ),
    sniped_relevance=(
        "Reliability + operator-control discipline. Pairs with un-delegate-ables ledger."
    ),
    direct_quotes=[],
    tags=["casting-call", "two-strike-rule", "production-days-locked", "production-sop"],
)

# ch02_mimi_production_brief_v1.md · 177L · 2 chunks
add_chunk(
    source_title="CH02 Mimi Production Brief v1",
    source_file="production__ch02_mimi_production_brief_v1.md",
    domain="production-sop",
    concept="Reference production brief · CH02 Mimi · the template form for chapter-rollout shoots",
    summary=(
        "CH02 Mimi is the locked reference template for chapter-rollout production briefs. Structure: "
        "subject snapshot, Direction Stack 5 answers, wardrobe spec, location lock, light + lens "
        "plan, shot list (10-12 Hero candidates), Cultural Doc cluster (if applicable), upsell "
        "candidates. Used as the structural template for future chapter production briefs."
    ),
    usable_principle=(
        "Use CH02 Mimi as the structural template for every chapter production brief. Update with "
        "subject-specific Direction Stack answers + shot list."
    ),
    sniped_relevance=(
        "The production-brief template. Pairs with chapter_intake_v1 + chapter_rollout_doctrine_v1."
    ),
    direct_quotes=[],
    tags=["ch02-mimi", "production-brief-template", "production-sop", "chapter-rollout"],
)
add_chunk(
    source_title="CH02 Mimi Production Brief · the shot-list structure",
    source_file="production__ch02_mimi_production_brief_v1.md",
    domain="production-sop",
    concept="Shot list structure · 10-12 Hero candidates pre-locked, not improvised",
    summary=(
        "Shot list specifies 10-12 Hero candidate frames BEFORE the shoot. Each candidate names: "
        "body architecture, pose register, light intent, the one intentional element, the chapter "
        "narrative tie-in. Improvising the shot list on shoot day is forbidden. Improvising within "
        "the named frames is encouraged."
    ),
    usable_principle=(
        "Pre-lock 10-12 Hero candidates. Improvise within frames, not across them. Shot list = "
        "the spine of the shoot."
    ),
    sniped_relevance=(
        "Pre-shoot rigor. Pairs with sniped-pre-shoot-prep + casting_call_doctrine."
    ),
    direct_quotes=[],
    tags=["shot-list", "10-12-heroes", "production-sop", "pre-shoot-discipline"],
)

# chapter_intake_v1.md · 261L · 3 chunks
add_chunk(
    source_title="Chapter Intake v1",
    source_file="production__chapter_intake_v1.md",
    domain="production-sop",
    concept="Chapter intake form + process · the discovery-to-production bridge for chapter shoots",
    summary=(
        "Chapter intake captures: subject context (work + culture + Direction Stack 5 answers), "
        "wardrobe direction, location options, narrative cluster (which chapter card this serves), "
        "Direction Stack pre-shoot diagnostic results, scheduling. Mode 1 DM template is the 80% "
        "default intake path (per 100Q Q97). Tally form is parked, not deleted."
    ),
    usable_principle=(
        "Mode 1 DM template is canonical for 80% of intakes. Tally form is parked. Run the full "
        "intake before the production brief."
    ),
    sniped_relevance=(
        "The pre-production bridge. Pairs with sniped-chapter-intake (not yet a skill, candidate)."
    ),
    direct_quotes=[],
    tags=["chapter-intake", "mode-1-dm-template", "production-sop", "discovery-to-production"],
)
add_chunk(
    source_title="Chapter Intake · the Direction Stack 5-answer pre-shoot diagnostic",
    source_file="production__chapter_intake_v1.md",
    domain="production-sop",
    concept="Direction Stack 5-question diagnostic · run during intake, not on shoot day",
    summary=(
        "The 5-question Direction Stack diagnostic is run BEFORE the shoot, during intake · not on "
        "shoot day. Each of the 5 questions calibrates one dimension of the final output: chapter, "
        "mood, wardrobe-implication, pose-implication, light-implication. The 5 answers drive the "
        "production brief shot list."
    ),
    usable_principle=(
        "Run the 5 questions during intake. Never on shoot day · shoot day is execution, not "
        "discovery."
    ),
    sniped_relevance=(
        "The Direction Stack methodology in operational form. Pairs with B6 sniped-direction-stack skill."
    ),
    direct_quotes=[],
    tags=["chapter-intake", "direction-stack-5", "production-sop", "pre-shoot-diagnostic"],
)
add_chunk(
    source_title="Chapter Intake · the narrative-cluster tie-in",
    source_file="production__chapter_intake_v1.md",
    domain="production-sop",
    concept="Narrative cluster · how each chapter ties to a Cultural Doc / Reputation Engine asset",
    summary=(
        "Every chapter shoot ties to a narrative cluster: which Cultural Doc lane it serves, which "
        "named-figure relationship it advances, which lineage it documents from inside. Intake "
        "captures the cluster explicitly. Shoots without a cluster tie-in are flagged for refusal "
        "or re-scoping."
    ),
    usable_principle=(
        "Every chapter shoot needs a named narrative-cluster tie-in. No tie-in = re-scope or refuse."
    ),
    sniped_relevance=(
        "Narrative discipline. Pairs with Lineage Doctrine + Cultural Doc lane + Reputation Engine."
    ),
    direct_quotes=[],
    tags=["chapter-intake", "narrative-cluster", "production-sop", "cultural-doc-tie-in"],
)

# checklist_post_shoot_same_day.md · 103L · 1 chunk
add_chunk(
    source_title="Post-Shoot Same-Day Checklist",
    source_file="production__checklist_post_shoot_same_day.md",
    domain="production-sop",
    concept="Post-shoot same-day checklist · the locked actions before sleep on shoot day",
    summary=(
        "Same-day actions: backup raw to 2 locations (local SSD + cloud), import to Lightroom catalog "
        "with the locked naming convention, run cull pass 1 (technical · sharpness + exposure · 200 -> 100), "
        "tag named-figure subjects, draft 1 BTS social post (if Cultural Doc cluster), send same-day "
        "thank-you to subject + MUA, log shoot stats in CRM. All before sleep."
    ),
    usable_principle=(
        "Same-day checklist is non-negotiable. Backup, import, cull pass 1, thank-you, CRM log. "
        "Before sleep. Always."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-post-shoot-same-day skill + SOP_capture_to_delivery."
    ),
    direct_quotes=[],
    tags=["post-shoot-same-day", "production-sop", "backup-discipline", "cull-pass-1"],
)

# checklist_pre_shoot_day_of.md · 109L · 1 chunk
add_chunk(
    source_title="Pre-Shoot Day-Of Checklist",
    source_file="production__checklist_pre_shoot_day_of.md",
    domain="production-sop",
    concept="Pre-shoot day-of checklist · the locked checks before the shoot starts",
    summary=(
        "Day-of checks (90 min before subject arrives): gear power + storage + backups, lights + "
        "modifiers + grip + stands, color-check card + gray card, location lighting test, wardrobe "
        "rack staged, MUA station ready, subject arrival timing confirmed, water + snacks staged, "
        "Direction Stack 5 answers reviewed, shot list printed."
    ),
    usable_principle=(
        "90 min before subject arrives, run the day-of checklist top-to-bottom. No exceptions."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-pre-shoot-prep skill."
    ),
    direct_quotes=[],
    tags=["pre-shoot-day-of", "production-sop", "90-min-before", "checklist-discipline"],
)

# composite_environment_rotation_v1.md · 303L · 3 chunks
add_chunk(
    source_title="Composite Environment Rotation v1 · LOCKED 2026-05-12",
    source_file="production__composite_environment_rotation_v1.md",
    domain="aesthetics",
    concept="7-environment composite rotation · one per chapter · constrained world-building",
    summary=(
        "7 locked composite environments: (1) Brutalist Monument; (2) Industrial Minimal; (3) "
        "Monochromatic Void; (4) Sculptural Gallery; (5) Cinematic Urban; (6) Organic Surreal; "
        "(7) Futurist Editorial. One environment per chapter. Constrained world-building beats "
        "random AI prompts. Each environment has a locked palette + spatial signature + light intent."
    ),
    usable_principle=(
        "Rotate through the 7 environments by chapter. Do not invent new environments without "
        "explicit operator-doctrine extension. Constrained > random."
    ),
    sniped_relevance=(
        "Pairs with feedback_composite_environment_rotation auto-memory + B6 sniped-higgsfield-pipeline."
    ),
    direct_quotes=[
        "Constrained world-building beats random AI prompts.",
    ],
    tags=["composite-environment-rotation", "aesthetics", "7-environments", "constrained-world-building"],
)
add_chunk(
    source_title="Composite Environment Rotation · the 7 environments named",
    source_file="production__composite_environment_rotation_v1.md",
    domain="aesthetics",
    concept="Per-environment palette + spatial signature + light intent",
    summary=(
        "Brutalist Monument: poured concrete + steel + diffused overhead. Industrial Minimal: white "
        "walls + concrete floors + single hard window. Monochromatic Void: single-color seamless + "
        "subject in negative space. Sculptural Gallery: museum-grade white cube + raking light. "
        "Cinematic Urban: night LA exteriors + practical light + restrained color. Organic Surreal: "
        "natural elements (water, smoke, fabric) + theatrical light. Futurist Editorial: high-contrast "
        "synthetic + chrome + electric color."
    ),
    usable_principle=(
        "Each environment is a complete brief. The locked specs prevent drift mid-chapter."
    ),
    sniped_relevance=(
        "Operationalizes the IG creative engine without abandoning aesthetic discipline."
    ),
    direct_quotes=[],
    tags=["composite-environment-rotation", "aesthetics", "brutalist", "monochromatic-void", "cinematic-urban"],
)
add_chunk(
    source_title="Composite Environment Rotation · the chapter-card mapping rule",
    source_file="production__composite_environment_rotation_v1.md",
    domain="aesthetics",
    concept="One environment per chapter · enforced at chapter-card design time",
    summary=(
        "Each chapter binds to exactly one environment. The chapter card (B&W dual-register per "
        "Lock 2) inherits the environment's spatial signature. HERO posts within the chapter render "
        "in full v3 LUXURY color but stay within the environment palette. Environment is the visual "
        "spine of the chapter."
    ),
    usable_principle=(
        "One chapter = one environment. No mid-chapter environment switches. Card = B&W, HERO = "
        "color, both inherit the environment palette."
    ),
    sniped_relevance=(
        "Pairs with feedback_bw_card_dual_register + chapter_rollout_doctrine_v1 (B1)."
    ),
    direct_quotes=[],
    tags=["composite-environment-rotation", "chapter-card-mapping", "aesthetics", "v3-luxury"],
)

# lightroom_operating_system.md · 408L · 4 chunks (with stale-flag on Adobe Portrait body refs)
add_chunk(
    source_title="Lightroom Operating System · v3 LUXURY supersession header",
    source_file="production__lightroom_operating_system.md",
    domain="production-sop",
    concept="LR OS v3 LUXURY supersession · the canonical edit register",
    summary=(
        "v3 LUXURY SUPERSESSION (2026-05-12, Lock 1 + Lock 7): SNIPED_LOCKED_LOOK_v3_LUXURY is the "
        "only edit going forward. Adobe Neutral base profile (NOT Adobe Portrait, NOT Camera Standard, "
        "NOT Adobe Color). Quiet luxury editorial restraint · Meisel/Roversi/Mert & Marcus lane. "
        "Body of doc references to Adobe Portrait / Camera Standard are LEGACY ARTIFACTS pending "
        "full sweep · operating decision is locked."
    ),
    usable_principle=(
        "Use v3 LUXURY · Adobe Neutral. Where the doc body says Adobe Portrait or Camera Standard, "
        "READ v3 LUXURY · Adobe Neutral. No alt edits, no experimental branches, no client-specific "
        "re-grades."
    ),
    sniped_relevance=(
        "Pairs with B4 doctrine_conflicts_resolved + feedback_visual_direction_luxury_editorial + "
        "B6 sniped-luxury-edit skill."
    ),
    direct_quotes=[
        "v3 LUXURY is the ONLY editing style going forward",
        "no alt edits, no experimental branches, no client-specific re-grades",
    ],
    tags=["lightroom-os", "v3-luxury", "production-sop", "adobe-neutral", "supersession-header"],
)
add_chunk(
    source_title="Lightroom Operating System · the 5-pass cull",
    source_file="production__lightroom_operating_system.md",
    domain="production-sop",
    concept="5-pass cull · technical to mental · Shore's 3 levels operationalized",
    summary=(
        "5-pass cull: Pass 1 technical (sharpness + exposure · 200 -> 100 same-day). Pass 2 depictive "
        "(framing + composition + crop · 100 -> 50). Pass 3 mental (which frames carry the chapter "
        "narrative · 50 -> 20). Pass 4 Hero candidates (full v3 LUXURY pipeline candidates · 20 -> 12). "
        "Pass 5 Hero finals (deliverable count, 10-12). Maps to Shore's three-level analysis "
        "(physical / depictive / mental) from B5."
    ),
    usable_principle=(
        "Run the 5 passes in order. Never skip. Pass 1 is same-day; passes 2-5 are next-day."
    ),
    sniped_relevance=(
        "The cull operationalization. Pairs with B5 Shore three-level analysis + B6 sniped-capture-to-delivery."
    ),
    direct_quotes=[],
    tags=["lightroom-os", "5-pass-cull", "production-sop", "shore-three-levels"],
)
add_chunk(
    source_title="Lightroom Operating System · the v1 legacy references (body)",
    source_file="production__lightroom_operating_system.md",
    domain="production-sop",
    concept="Body-of-doc v1 references · LEGACY · superseded by v3 LUXURY supersession header",
    summary=(
        "The body of the LR OS doc references Adobe Portrait base profile, Camera Standard, HSL "
        "orange punch, and v1 preset stack. These references are LEGACY ARTIFACTS pending full sweep "
        "(per the supersession header at top of doc). The canonical answer is v3 LUXURY · Adobe Neutral. "
        "Operators reading the doc must read the supersession header first."
    ),
    usable_principle=(
        "Where the body references Adobe Portrait / Camera Standard / HSL orange punch · READ v3 "
        "LUXURY · Adobe Neutral. Operating decision is locked even though the body text is not "
        "yet fully swept."
    ),
    sniped_relevance=(
        "Documented audit-trail of the v1 -> v3 LUXURY supersession. Pairs with B4 SYNTHESIS Contradiction 2."
    ),
    direct_quotes=[
        "Where this doc references SNIPED_LOCKED_LOOK_v3_LUXURY or 'Adobe Portrait' or 'Camera Standard,' READ v3 LUXURY · Adobe Neutral.",
    ],
    tags=["lightroom-os", "production-sop", "legacy-adobe-portrait-pending-sweep", "v1-legacy", "audit-trail"],
)
add_chunk(
    source_title="Lightroom Operating System · the mask stack + Hero timing",
    source_file="production__lightroom_operating_system.md",
    domain="production-sop",
    concept="Mask stack speed unlock · 12-Hero shoot takes the mask stack once, not 12 times",
    summary=(
        "Mask stack is the load-bearing speed unlock. Build the mask stack once per shoot (subject "
        "mask + face mask + skin mask + sky/background mask + texture mask). Apply across all 12 "
        "Heroes. Hero (full pipeline): 12-15 min per frame. Select (color-graded only): 3-4 min. "
        "Proof (batch-graded): 30 sec via preset sync. A 12-Hero shoot = ~3 hours at v3 LUXURY pipeline."
    ),
    usable_principle=(
        "Build the mask stack ONCE. Apply across the 12 Heroes. 12-Hero shoot = ~3 hours, not 12 x "
        "15 min."
    ),
    sniped_relevance=(
        "The speed-unlock primitive. Pairs with sniped-luxury-edit skill + retoucher_training_notes."
    ),
    direct_quotes=[
        "A 12-Hero shoot takes the mask stack once, not 12 times.",
    ],
    tags=["lightroom-os", "mask-stack", "12-15-min-per-hero", "production-sop", "speed-unlock"],
)

# preset_library.md · 249L · 2 chunks
add_chunk(
    source_title="Preset Library · v3 LUXURY locked + 6 secondary presets",
    source_file="production__preset_library.md",
    domain="aesthetics",
    concept="Preset library · what each .xmp is for and when to invoke",
    summary=(
        "Locked preset library: SNIPED_LOCKED_LOOK_v3_LUXURY (primary · Adobe Neutral base · quiet "
        "luxury editorial). Secondaries: SNIPED_HERO_FINISH_v1 (final pass on selected Heroes), "
        "SNIPED_PROOF_BATCH_v1 (batch grade for proofs), SNIPED_BW_EDITORIAL_v1 (chapter cards · "
        "B&W dual-register), SNIPED_CULTURAL_DOC_v1 (Cultural Doc lane register). Retired: v1 + v2 "
        "(Adobe Portrait base · superseded by v3 LUXURY)."
    ),
    usable_principle=(
        "Primary v3 LUXURY first. Then secondary by use case. v1 and v2 are RETIRED · do not invoke."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-luxury-edit + lightroom_operating_system.md supersession."
    ),
    direct_quotes=[],
    tags=["preset-library", "aesthetics", "v3-luxury", "retired-v1-v2", "secondary-presets"],
)
add_chunk(
    source_title="Preset Library · invocation order + the no-alt-edits rule",
    source_file="production__preset_library.md",
    domain="aesthetics",
    concept="Preset invocation order + the no-alt-edits enforcement",
    summary=(
        "Preset invocation order per frame: v3 LUXURY base -> mask stack -> SNIPED_HERO_FINISH (Heroes "
        "only) -> export. For Cultural Doc lane: v3 LUXURY base -> SNIPED_CULTURAL_DOC + restrained-color "
        "discipline -> export. For chapter cards: SNIPED_BW_EDITORIAL -> export. NEVER mix preset "
        "stacks within a single chapter or single client deliverable. No alt edits."
    ),
    usable_principle=(
        "One preset stack per deliverable category. Never mix. v1/v2 are retired · do not invoke."
    ),
    sniped_relevance=(
        "Aesthetic discipline enforcement. Pairs with Lock 1 + Lock 2."
    ),
    direct_quotes=[],
    tags=["preset-library", "aesthetics", "invocation-order", "no-alt-edits"],
)

# retoucher_training_notes.md · 208L · 2 chunks
add_chunk(
    source_title="Retoucher Training Notes · the operator-engine handoff",
    source_file="production__retoucher_training_notes.md",
    domain="production-sop",
    concept="Retoucher training · what the operator delegates + what stays un-delegated",
    summary=(
        "Retoucher receives: Lightroom v3 LUXURY pipeline output (mask stack applied), the locked "
        "preset library, the 5-pass cull notes, the clinical-retouch rubric (skin unified · color "
        "casts equalized · pore detail preserved · no plastic smoothing). Retoucher does NOT receive: "
        "Direction Stack methodology, final-review authority, pricing decisions, named-subject "
        "context. The handoff line is the un-delegate-ables ledger."
    ),
    usable_principle=(
        "Retoucher does technical retouch only. Methodology, direction, final review stay with the "
        "operator. The handoff line is the un-delegate-ables."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-retoucher-onboarding skill + un-delegate-ables ledger."
    ),
    direct_quotes=[],
    tags=["retoucher-training", "production-sop", "operator-handoff", "un-delegate-ables"],
)
add_chunk(
    source_title="Retoucher Training Notes · clinical-retouch rubric",
    source_file="production__retoucher_training_notes.md",
    domain="production-sop",
    concept="Clinical retouch rubric · skin unified, pore detail preserved, no plastic smoothing",
    summary=(
        "Clinical retouch rubric (4 rules): (1) skin unified · even tone across face/neck/hands; "
        "(2) color casts equalized · no green/magenta drift in shadows; (3) pore detail preserved · "
        "frequency-separation, NOT skin-smoothing filters; (4) no plastic smoothing · the face must "
        "read as photographed-not-AI-generated. The rubric is the anti-AI defense at the retouch layer."
    ),
    usable_principle=(
        "Run the 4-rule rubric on every Hero. Frequency separation only · never blur or skin-soften. "
        "Pore detail preserved = anti-AI signal."
    ),
    sniped_relevance=(
        "The retouch-layer anti-AI defense. Pairs with B5 anti-faceless-AI position."
    ),
    direct_quotes=[],
    tags=["retoucher-training", "clinical-retouch", "production-sop", "anti-ai-retouch", "frequency-separation"],
)

# SOP_capture_to_delivery.md · 132L · 2 chunks
add_chunk(
    source_title="SOP Capture-to-Delivery · the end-to-end shoot SOP",
    source_file="production__sop_capture_to_delivery.md",
    domain="production-sop",
    concept="Capture-to-delivery SOP · the end-to-end Reset shoot operating procedure",
    summary=(
        "Capture-to-delivery SOP: 5-hour single-direction shoot -> same-day backup + cull pass 1 -> "
        "next-day cull pass 2-3 + Hero candidate selection -> Day 3 mask stack + Heroes (12-15 min "
        "each) -> Day 4 Selects (color-graded) + Proofs (batch-graded) -> Day 5 Pixieset gallery "
        "live (9 AM PT) + Day 0 delivery email. Total SLA: 5 days from shoot to gallery."
    ),
    usable_principle=(
        "5-day SLA from shoot to gallery. 5-pass cull + mask stack + v3 LUXURY pipeline. Same-day "
        "backup is non-negotiable."
    ),
    sniped_relevance=(
        "The Reset operational backbone. Pairs with B6 sniped-capture-to-delivery skill + "
        "delivery_architecture_v2."
    ),
    direct_quotes=[],
    tags=["sop-capture-to-delivery", "production-sop", "5-day-sla", "end-to-end-shoot"],
)
add_chunk(
    source_title="SOP Capture-to-Delivery · the SLA discipline",
    source_file="production__sop_capture_to_delivery.md",
    domain="production-sop",
    concept="5-day SLA discipline · what to do when the SLA is at risk",
    summary=(
        "5-day SLA from shoot to gallery is locked. If the SLA is at risk (gear failure, family "
        "emergency, mask-stack rebuild needed), notify client within 24 hours of the risk surfacing, "
        "with the new locked delivery date. NEVER let the SLA slip silently. The notification "
        "preserves the locked-experience signal even when the SLA can't hold."
    ),
    usable_principle=(
        "Risk surfaces -> notify within 24 hours -> commit to new locked date. Silent slip = trust "
        "loss."
    ),
    sniped_relevance=(
        "Hospitality discipline. Pairs with B3 Guidara service-as-floor + Lock 9 (Cultural Doc compounding)."
    ),
    direct_quotes=[],
    tags=["sop-capture-to-delivery", "5-day-sla", "production-sop", "risk-notification"],
)

# SOP_reset_shoot_day.md · 114L · 1 chunk
add_chunk(
    source_title="SOP Reset Shoot Day",
    source_file="production__sop_reset_shoot_day.md",
    domain="production-sop",
    concept="Reset shoot day SOP · the locked 5-hour single-direction Reset format",
    summary=(
        "Reset shoot day format (5 hours): 30 min subject arrival + warm-up + Direction Stack reaffirm; "
        "60 min wardrobe set 1 + lighting set 1 (3-4 Hero candidates); 30 min wardrobe set 2 reset; "
        "60 min wardrobe set 2 + lighting set 2 (3-4 Hero candidates); 30 min wardrobe set 3 reset; "
        "60 min wardrobe set 3 + lighting set 3 (3-4 Hero candidates); 30 min BTS + Cultural Doc cluster + "
        "thank-you. Total 5 hours, 9-12 Hero candidates captured."
    ),
    usable_principle=(
        "5 hours, 3 wardrobe sets, 9-12 Hero candidates captured. Anything beyond = Op Kit, not Reset."
    ),
    sniped_relevance=(
        "Reset format lock. Pairs with B6 sniped-shoot-day-reset skill + Reset $1,500 floor."
    ),
    direct_quotes=[],
    tags=["sop-reset-shoot-day", "production-sop", "5-hours", "3-wardrobe-sets"],
)

# SOP_strategic_free.md · 148L · 1 chunk
add_chunk(
    source_title="SOP Strategic Free",
    source_file="production__sop_strategic_free.md",
    domain="production-sop",
    concept="Strategic Free SOP · Community + Access · the compounding-engine free-shoot doctrine",
    summary=(
        "Strategic Free = 2 modes. Community (institutional · church / cultural / HBCU): 5-10 "
        "named-subject Heroes + 30-50 institutional-grade frames + 60-100 raw archive. Trade: $0 to "
        "institution + paid family portraits at event. Access (event / promoter coverage): 10-20 "
        "Hero frames for SNIPED archive + 50-100 event coverage. Trade: $0 + commercial introduction. "
        "Strategic Free is the Reputation Engine input · not a charity model."
    ),
    usable_principle=(
        "Strategic Free is strategic. Always trade for either family-portrait-paid (Community) or "
        "commercial-introduction (Access). Free without a trade = drift."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-shoot-day-strategic-free skill + Reputation Engine."
    ),
    direct_quotes=[],
    tags=["sop-strategic-free", "production-sop", "community-mode", "access-mode", "reputation-engine"],
)

# track_b_frame_walkthrough.md · 305L · 3 chunks
add_chunk(
    source_title="Track B Frame Walkthrough · compositing pipeline",
    source_file="production__track_b_frame_walkthrough.md",
    domain="aesthetics",
    concept="Track B compositing · real subject + AI environment composite pipeline",
    summary=(
        "Track B = compositing pipeline (real subject + AI-generated environment background + "
        "Photoshop assembly). Per the hybrid-operator stance: AI for environment / world-construction "
        "inputs, NEVER for identity. Track B is the IG creative engine without crossing the identity "
        "line. Pipeline: subject capture (v3 LUXURY pipeline) -> background generation (Higgsfield / "
        "Seedream / curated AI tool) -> Photoshop assembly + edge cleanup + color match -> final "
        "v3 LUXURY pass."
    ),
    usable_principle=(
        "Track B = real subject + AI background only. Never AI identity. Photoshop assembly is the "
        "skill bottleneck."
    ),
    sniped_relevance=(
        "Pairs with B5 anti-faceless-AI + B6 sniped-hero-composite-ceiling + sniped-higgsfield-pipeline."
    ),
    direct_quotes=[],
    tags=["track-b", "compositing", "aesthetics", "hybrid-ai-stance", "real-subject-ai-background"],
)
add_chunk(
    source_title="Track B Frame Walkthrough · the edge-cleanup discipline",
    source_file="production__track_b_frame_walkthrough.md",
    domain="aesthetics",
    concept="Edge cleanup · the technical skill that distinguishes operator-grade Track B from amateur",
    summary=(
        "Edge cleanup is the load-bearing technical skill. Hair, fabric edges, transparent objects, "
        "out-of-focus elements all need surgical masking + edge-decontamination + matte refinement. "
        "Amateur Track B reads as composite because edges are wrong. Operator-grade Track B reads "
        "as photographed because edges are clean. Time: 30-60 min per Hero on edge cleanup alone."
    ),
    usable_principle=(
        "Edge cleanup is non-negotiable. Spend the 30-60 min per Hero. Edges are what distinguish "
        "operator-grade from amateur."
    ),
    sniped_relevance=(
        "The Track B skill bottleneck. Pairs with B6 sniped-hero-composite-ceiling."
    ),
    direct_quotes=[],
    tags=["track-b", "edge-cleanup", "aesthetics", "operator-grade", "compositing-discipline"],
)
add_chunk(
    source_title="Track B Frame Walkthrough · color-match + final v3 LUXURY pass",
    source_file="production__track_b_frame_walkthrough.md",
    domain="aesthetics",
    concept="Color match between subject and AI background · final v3 LUXURY pass unifies both",
    summary=(
        "Color match: subject capture and AI background must share light direction, color temperature, "
        "shadow density. Mismatch = composite reads. Match = composite reads as photographed. Final "
        "v3 LUXURY pass unifies the composite into the locked aesthetic register · same Adobe Neutral "
        "base, same restrained-color discipline."
    ),
    usable_principle=(
        "Match light direction + color temperature + shadow density BEFORE Photoshop assembly. "
        "Final v3 LUXURY pass over the assembled composite."
    ),
    sniped_relevance=(
        "Pairs with v3 LUXURY locked aesthetic + Track B pipeline."
    ),
    direct_quotes=[],
    tags=["track-b", "color-match", "aesthetics", "v3-luxury-final-pass"],
)


# ===========================================================================
# P3 · Outreach SOPs · 7 sources · ~16 chunks
# ===========================================================================

# linkedin_comment_doctrine_v1.md · 178L · 2 chunks
add_chunk(
    source_title="LinkedIn Comment Doctrine v1 · LOCKED 2026-05-12",
    source_file="outreach__linkedin_comment_doctrine_v1.md",
    domain="outreach-sop",
    concept="LinkedIn comment doctrine · 5-10/day Tier-0 CRM founders only",
    summary=(
        "LinkedIn comment execution doctrine (MIGRATED 2026-05-12): 5-10 comments/day on Tier-0 CRM "
        "founder posts ONLY. Search filter: 'LA founder' past 24 hours latest sort. Format: "
        "soft-opener (acknowledges the post specifically) + post-language callback (uses one of "
        "the founder's own phrases). Warming surface that feeds the VIB DM conversion."
    ),
    usable_principle=(
        "5-10 comments/day. Tier-0 only. Soft-opener + post-language callback. Never spray comments."
    ),
    sniped_relevance=(
        "Pairs with feedback_linkedin_comment_doctrine auto-memory + VIB outreach pipeline."
    ),
    direct_quotes=[],
    tags=["linkedin-comment-doctrine", "outreach-sop", "5-10-per-day", "tier-0-only", "warming-surface"],
)
add_chunk(
    source_title="LinkedIn Comment Doctrine · the post-language callback technique",
    source_file="outreach__linkedin_comment_doctrine_v1.md",
    domain="outreach-sop",
    concept="Post-language callback · using the founder's own phrases for signal",
    summary=(
        "Post-language callback: every comment uses one phrase the founder used in the post (verbatim "
        "if unique, paraphrased if generic). The callback signals close-reading. Founders see ~50 "
        "generic comments per post; post-language callbacks stand out by demonstrating specificity. "
        "The technique converts to VIB-acceptance at ~10x the generic-comment rate (per CRM data)."
    ),
    usable_principle=(
        "Always include a post-language callback. Verbatim for unique phrases, paraphrased for "
        "generic ones. No generic 'great post' comments."
    ),
    sniped_relevance=(
        "The signal-density technique. Pairs with VIB conversion math."
    ),
    direct_quotes=[],
    tags=["linkedin-comment-doctrine", "post-language-callback", "outreach-sop", "specificity-signal"],
)

# SOP_assistant.md · 440L · 5 chunks (with stale-phase-b-trigger tag on compensation)
add_chunk(
    source_title="SOP SNIPED Assistant v3 · role + scope",
    source_file="outreach__sop_assistant.md",
    domain="outreach-sop",
    concept="Assistant role + scope · what the assistant owns and does NOT own",
    summary=(
        "Role + scope (v3): assistant sources leads + manages CRM. Owns: lead sourcing (30 qualified "
        "leads/week minimum, ~10 Hot tier), CRM hygiene, daily report, Friday roll-up, reply triage "
        "(flag to BJ same-day). Does NOT own: sending any DM or email, replying to leads, pricing "
        "decisions, discovery calls, edit work, contracts, adding leads outside ICP, modifying CRM "
        "columns, improvising scripts."
    ),
    usable_principle=(
        "Assistant sources and tags. BJ owns all outreach + clients + pricing + delivery. The "
        "boundary is the un-delegate-ables ledger."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-assistant-task-routing skill + un-delegate-ables doctrine."
    ),
    direct_quotes=[],
    tags=["sop-assistant", "outreach-sop", "v3-canonical", "role-scope", "un-delegate-ables"],
)
add_chunk(
    source_title="SOP SNIPED Assistant · compensation (Phase 1)",
    source_file="outreach__sop_assistant.md",
    domain="outreach-sop",
    concept="Assistant compensation · $100 base every 2 weeks + per-booked-call commission",
    summary=(
        "Compensation (Phase 1 locked): $100 base every 2 weeks for sourcing + CRM. Per-booked-call "
        "commission (rate confirmed at re-engagement). Re-evaluate at Phase B trigger ($3K MRR "
        "sustained 2 months). Assistant tracks own hours; BJ pays bi-weekly via agreed channel. "
        "Invoice at end of pay period if needed."
    ),
    usable_principle=(
        "Phase 1 compensation: $100/2wk + per-booked-call commission. Re-evaluate at Phase B."
    ),
    sniped_relevance=(
        "Operational pay structure. The Phase B trigger reference is STALE per B4 100Q recalibration "
        "(canonical = $2K x 3 months, not $3K x 2). Source doc not yet swept."
    ),
    direct_quotes=[
        "Re-evaluate at Phase B trigger ($3K MRR sustained 2 months)",
    ],
    tags=["sop-assistant", "outreach-sop", "compensation", "phase-1", "stale-phase-b-trigger-3k-vs-2k"],
)
add_chunk(
    source_title="SOP SNIPED Assistant · the ICP locked at 4 of 4",
    source_file="outreach__sop_assistant.md",
    domain="outreach-sop",
    concept="ICP 4 of 4 (locked) · all four criteria must hit · no exceptions",
    summary=(
        "ICP locked at 4 of 4 (was 3 of 4 in v2 CRM Sheet · conflict resolved to stricter). All "
        "four must hit: (1) LA-based or LA-frequent (verify via LinkedIn location, recent post "
        "locations, or company HQ); (2) Active poster (posted on LinkedIn in last 7 days · skip if "
        ">14 days); (3) Visual gap (current visual presence sits below operational level of "
        "business · this is the load-bearing skill); (4) Has revenue or funding (verify via "
        "LinkedIn signal, press, or website)."
    ),
    usable_principle=(
        "All 4 criteria must hit. No 3-of-4 exceptions. Inactive founders are skipped (don't see DMs)."
    ),
    sniped_relevance=(
        "The lead-quality discipline. Pairs with VIB outreach pipeline + lean-execution-audit overrides."
    ),
    direct_quotes=[
        "ICP locked to 4 of 4 (was 3 of 4 in v2 CRM Sheet · conflict resolved in favor of stricter)",
    ],
    tags=["sop-assistant", "icp-4-of-4", "outreach-sop", "lead-quality"],
)
add_chunk(
    source_title="SOP SNIPED Assistant · the visual gap diagnosis (load-bearing)",
    source_file="outreach__sop_assistant.md",
    domain="outreach-sop",
    concept="Visual gap diagnosis · the load-bearing assistant skill",
    summary=(
        "Visual gap diagnosis: assistant evaluates each candidate's current visual presence (LinkedIn "
        "header, profile photo, posted images) against SNIPED's operational-grade baseline. Gap "
        "categories: (1) commodity headshot (operational mismatch); (2) overly casual (lifestyle "
        "drift); (3) brand-inconsistent (multi-photographer mash-up); (4) operational-grade (skip · "
        "not a lead). 'Looks fine' is not a gap. Calibration examples in source doc."
    ),
    usable_principle=(
        "The load-bearing assistant skill. Never skip the visual gap step. 'Looks fine' is not a gap."
    ),
    sniped_relevance=(
        "The signal-quality gatekeeper. Without good visual gap diagnosis, the outbound pipeline fails."
    ),
    direct_quotes=[
        "Visual gap diagnosis · the load-bearing skill",
        "'Looks fine' is not a gap.",
    ],
    tags=["sop-assistant", "visual-gap-diagnosis", "outreach-sop", "load-bearing-skill"],
)
add_chunk(
    source_title="SOP SNIPED Assistant · v3 changes from v2",
    source_file="outreach__sop_assistant.md",
    domain="outreach-sop",
    concept="v3 changes from v2 · the explicit migration log",
    summary=(
        "7 v3 changes from v2 (April 2026 archived at _archive_v2_2026-05-07/): (1) ICP locked to "
        "4 of 4 (was 3 of 4); (2) Engaged status deprecated · VIB is the engagement (no like-then-"
        "comment 24hr warm-up); (3) Outreach methodology shift · VIBs replace Ambient Audit treatment "
        "mocks + Higgsfield animations; (4) Volume target · BJ targets 3-10 VIBs/week (down from 45 "
        "personalized touches); (5) Tight access list · assistant gets CRM + SOP + research tools only; "
        "(6) Claude usage rules · explicit on what tasks AI helps with; (7) CRM platform · Excel for "
        "now, migrate to Notion when BJ stands it up."
    ),
    usable_principle=(
        "v3 supersedes v2. The archive is reference only. The Engaged status is dead. VIB is the engagement."
    ),
    sniped_relevance=(
        "The v3 supersession audit-trail. Pairs with cold_email_doctrine + VIB pipeline."
    ),
    direct_quotes=[],
    tags=["sop-assistant", "outreach-sop", "v3-changes", "engaged-status-deprecated", "vib-is-engagement"],
)

# SOP_discovery_call.md · 130L · 2 chunks
add_chunk(
    source_title="SOP Discovery Call",
    source_file="outreach__sop_discovery_call.md",
    domain="outreach-sop",
    concept="Discovery call SOP · 30-min subject-context call before any pricing or shoot booking",
    summary=(
        "30-min call structure: (1) 5 min · subject background + business context; (2) 15 min · "
        "Direction Stack 5 questions (the methodology IS the diagnostic); (3) 5 min · scope + "
        "delivery overview; (4) 5 min · pricing + booking. The Direction Stack questions are not "
        "a survey · they are the diagnostic. Operator listens for chapter-fit + lineage-fit signals."
    ),
    usable_principle=(
        "30 min, structured 5/15/5/5. Direction Stack questions are the conversation, not a survey. "
        "Listen for chapter + lineage fit."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-direction-stack + chapter_intake_v1."
    ),
    direct_quotes=[],
    tags=["sop-discovery-call", "outreach-sop", "30-min", "direction-stack-diagnostic"],
)
add_chunk(
    source_title="SOP Discovery Call · the refuse-conditions",
    source_file="outreach__sop_discovery_call.md",
    domain="outreach-sop",
    concept="Discovery call refuse conditions · when to decline cleanly",
    summary=(
        "Refuse conditions surfaced during discovery: (1) off-lineage (subject doesn't fit 5 lineages "
        "AND requires single-visit cultural tourism); (2) over-prescription (client describes the "
        "shoot before BJ runs the diagnostic); (3) price-shopping (client compares to $300 commodity "
        "headshots without engaging on methodology); (4) scope-stretching (asks for 30 Heroes + "
        "Pixieset upgrade pack at Reset price); (5) timeline-impossible (next-day delivery)."
    ),
    usable_principle=(
        "Decline cleanly when any refuse-condition surfaces. Trade scope, never price. Don't apologize."
    ),
    sniped_relevance=(
        "Pairs with refusal-as-positioning + 65+ named refusals catalog."
    ),
    direct_quotes=[],
    tags=["sop-discovery-call", "refuse-conditions", "outreach-sop", "decline-cleanly"],
)

# SOP_discovery_to_close.md · 175L · 2 chunks
add_chunk(
    source_title="SOP Discovery-to-Close",
    source_file="outreach__sop_discovery_to_close.md",
    domain="outreach-sop",
    concept="Discovery-to-close SOP · the 5-step path from VIB-accepted to booked shoot",
    summary=(
        "5-step path: (1) VIB accepted in DM -> discovery call booked within 48 hours; (2) discovery "
        "call (30 min · Direction Stack diagnostic); (3) proposal sent within 24 hours (3-option "
        "structure · anchor high · Reset / Sprint warm / Op Kit); (4) 50% deposit collected within "
        "72 hours; (5) shoot scheduled within 14 days of deposit. Each step has a hard timer."
    ),
    usable_principle=(
        "VIB -> call <48hr -> proposal <24hr -> deposit <72hr -> shoot <14d. Slip = re-engage or drop."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-discovery-to-close skill + B3 Enns 3-option proposal + pricing canon."
    ),
    direct_quotes=[],
    tags=["sop-discovery-to-close", "outreach-sop", "5-step-path", "hard-timers"],
)
add_chunk(
    source_title="SOP Discovery-to-Close · the 3-option proposal anchor",
    source_file="outreach__sop_discovery_to_close.md",
    domain="outreach-sop",
    concept="3-option proposal · anchor high · scope flexes, price holds",
    summary=(
        "Proposal structure (Enns 3-option): Op Kit (~$5-8K · multi-direction + brand-system entry) "
        "anchored at top, Reset ($1,500 · single-direction 5-hour) in the middle, Sprint ($750 · "
        "warm-network only · 2-hour single-direction) at the bottom IF warm referral. Cold leads "
        "see Op Kit + Reset only · Sprint is never cold-pitched. The 3-option anchor preserves the "
        "Reset as the midpoint, not the floor."
    ),
    usable_principle=(
        "3-option proposal. Anchor high. Sprint NEVER cold-pitched. Floor holds at $1,500 for cold."
    ),
    sniped_relevance=(
        "Pairs with B3 Enns + B4 SYNTHESIS Section 6.3 Sprint guardrail + B6 sniped-pricing-decision."
    ),
    direct_quotes=[],
    tags=["sop-discovery-to-close", "3-option-proposal", "anchor-high", "sprint-warm-only"],
)

# SOP_VIB_production.md · 92L · 1 chunk
add_chunk(
    source_title="SOP VIB Production",
    source_file="outreach__sop_vib_production.md",
    domain="outreach-sop",
    concept="VIB production SOP · 2-panel Figma frame · 30-45 min per VIB",
    summary=(
        "VIB production: Figma template (locked spec in VIB_figma_spec.md). Left panel: founder's "
        "current visual presence (LinkedIn header crop or self-shot · annotated with visual-gap "
        "diagnosis). Right panel: SNIPED-grade rebuild (mock from preset library or a comparable "
        "named-photographer reference · annotated with what changes). 30-45 min per VIB. Export as "
        "PNG, send via LinkedIn DM with the locked VIB caption."
    ),
    usable_principle=(
        "30-45 min per VIB. Figma template (don't improvise structure). Annotate both panels. "
        "Export PNG, send via DM."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-vib-outreach skill + VIB_figma_spec + VIB_caption_library."
    ),
    direct_quotes=[],
    tags=["sop-vib-production", "outreach-sop", "30-45-min", "figma-template", "2-panel-comparison"],
)

# VIB_caption_library.md · 186L · 2 chunks
add_chunk(
    source_title="VIB Caption Library · DM caption templates",
    source_file="outreach__vib_caption_library.md",
    domain="outreach-sop",
    concept="VIB DM caption templates · 4 variants per founder profile",
    summary=(
        "Caption library has 4 main variants: (1) operator-to-operator (peer register · default for "
        "Tier-0 founders); (2) cultural-context-anchor (subject is named in a specific LA cultural "
        "circle · use cultural callback); (3) recent-post-callback (built on a specific post the "
        "founder made in last 7 days); (4) referral-warm (sender is a named connection). Each "
        "variant is 60-80 words, ends with the VIB image attached + a single soft question."
    ),
    usable_principle=(
        "60-80 words. Variant by founder context. End with one soft question + VIB image. Never "
        "feature-pitch."
    ),
    sniped_relevance=(
        "The VIB-DM conversion layer. Pairs with B6 sniped-vib-outreach + sniped-caption-writer."
    ),
    direct_quotes=[],
    tags=["vib-caption-library", "outreach-sop", "4-variants", "60-80-words", "soft-question"],
)
add_chunk(
    source_title="VIB Caption Library · the no-feature-pitch rule",
    source_file="outreach__vib_caption_library.md",
    domain="outreach-sop",
    concept="No feature-pitch · captions never list services or pricing",
    summary=(
        "VIB captions NEVER list services (Reset / Op Kit / Brand System), pricing ($1,500), or "
        "deliverables (10-12 Heroes / 14-day window). All commercial detail is gated behind the "
        "discovery call. The VIB itself is the value-demonstration. The caption is the soft open · "
        "ask one question that surfaces the founder's perspective on their visual presence."
    ),
    usable_principle=(
        "Never feature-pitch in captions. VIB demonstrates value. Caption opens conversation. "
        "Pricing is gated behind discovery."
    ),
    sniped_relevance=(
        "Anti-feature-pitch discipline. Pairs with intel_positioning_phrases + refusal-as-positioning."
    ),
    direct_quotes=[],
    tags=["vib-caption-library", "outreach-sop", "no-feature-pitch", "soft-open", "value-demonstration"],
)

# VIB_figma_spec.md · 154L · 2 chunks
add_chunk(
    source_title="VIB Figma Spec · the locked template",
    source_file="outreach__vib_figma_spec.md",
    domain="outreach-sop",
    concept="VIB Figma template spec · the locked layout for the 2-panel comparison",
    summary=(
        "Figma template: 1080x1350 (Instagram portrait ratio), 2-panel split, left panel = current "
        "presence, right panel = SNIPED-grade rebuild. Padding, type stack, annotation arrows, "
        "watermark position all locked. Color palette: SNIPED brand grays + single accent color (no "
        "teal/orange · per v3 LUXURY discipline). Template instance per founder · save as PNG, never "
        "share Figma link."
    ),
    usable_principle=(
        "Use the locked template. Never improvise layout, type stack, or palette. Export PNG, never "
        "share editable Figma."
    ),
    sniped_relevance=(
        "Pairs with sniped-vib-outreach + SOP_VIB_production + v3 LUXURY discipline."
    ),
    direct_quotes=[],
    tags=["vib-figma-spec", "outreach-sop", "1080x1350", "locked-template", "v3-luxury-palette"],
)
add_chunk(
    source_title="VIB Figma Spec · the annotation discipline",
    source_file="outreach__vib_figma_spec.md",
    domain="outreach-sop",
    concept="Annotation discipline · specific named issues, not generic 'looks dated'",
    summary=(
        "Annotations on each panel name specific issues + specific upgrades. Left panel: 2-3 named "
        "issues (lighting flat, casual register, no chapter context). Right panel: 2-3 named upgrades "
        "(operational lighting, editorial register, environment + apparatus). Generic annotations "
        "('looks dated', 'needs work') are forbidden. Specificity is the credibility signal."
    ),
    usable_principle=(
        "Specific named issues + specific named upgrades. 2-3 each. No generic annotations. "
        "Specificity = credibility."
    ),
    sniped_relevance=(
        "The credibility layer of the VIB. Pairs with visual-gap-diagnosis discipline."
    ),
    direct_quotes=[],
    tags=["vib-figma-spec", "annotation-discipline", "outreach-sop", "specificity-signal"],
)


# ===========================================================================
# P4 · Delivery docs · 11 sources · ~13 chunks (delivery-sop NEW domain)
# ===========================================================================

# SOP_post_delivery.md · 181L · 2 chunks
add_chunk(
    source_title="SOP Post-Delivery",
    source_file="delivery__sop_post_delivery.md",
    domain="delivery-sop",
    concept="Post-delivery SOP · the 14-day post-shoot client experience layer",
    summary=(
        "Post-delivery operating SOP: Day 0 gallery delivery + 9 AM email (locked subject 'Sniped · "
        "your gallery is live'). Day 2 social trigger (Story tag if subject opts in). Day 3 voice-note "
        "referral ask. Day 7 testimonial request. Day 14 window-closing reminder (Proofs hidden, "
        "Hero/Select stay accessible). Day 19 final-window note. Day 30 Op Kit pitch (if testimonial "
        "received). Day 90 reengagement check-in. Each touchpoint has a locked template + locked "
        "trigger condition."
    ),
    usable_principle=(
        "Follow the locked 14-day sequence. Each touchpoint has a template + trigger. Never improvise "
        "outside the sequence."
    ),
    sniped_relevance=(
        "Pairs with B4 chat-thread 14-day sequence + B6 sniped-post-delivery skill."
    ),
    direct_quotes=[],
    tags=["sop-post-delivery", "delivery-sop", "14-day-sequence", "client-experience"],
)
add_chunk(
    source_title="SOP Post-Delivery · the testimonial-request gate for Op Kit pitch",
    source_file="delivery__sop_post_delivery.md",
    domain="delivery-sop",
    concept="Op Kit pitch gates · testimonial received + 30-day deployment evidence",
    summary=(
        "Op Kit upsell pitch (Day 30) is gated by two conditions: (1) testimonial received by Day 7-14; "
        "(2) deployment evidence visible (client posted Hero as LinkedIn header / press cover / deck "
        "portrait). If either fails, the Day 30 pitch is held to Day 60 or skipped. The gate prevents "
        "pitch-fatigue and preserves the trust signal."
    ),
    usable_principle=(
        "No testimonial = no Op Kit pitch at Day 30. No deployment evidence = no pitch. The gate "
        "is non-negotiable."
    ),
    sniped_relevance=(
        "Pairs with B4 SYNTHESIS Section 6.4 three upsell paths + Lock 9 (Cultural Doc compounding)."
    ),
    direct_quotes=[],
    tags=["sop-post-delivery", "op-kit-gate", "delivery-sop", "testimonial-required"],
)

# pixieset_config.md · 133L · 2 chunks
add_chunk(
    source_title="Pixieset Config",
    source_file="delivery__pixieset_config.md",
    domain="delivery-sop",
    concept="Pixieset gallery setup spec · 3-tier collection structure",
    summary=(
        "Pixieset gallery structure: 3 sub-collections per gallery. Heroes (10-12 fully retouched, "
        "editorial-grade, all download-enabled). Selects (30-40 color-graded, production-quality, "
        "download-enabled). Proofs (60-100 batch-graded, download disabled, upgrade-only via "
        "Pixieset shop). Gallery window: 14 days. Proofs hidden after 14 days; Heroes + Selects "
        "stay accessible. Password: locked per gallery."
    ),
    usable_principle=(
        "3 sub-collections (Hero/Select/Proof). 14-day window. Proofs hidden after Day 14. Heroes "
        "+ Selects stay accessible."
    ),
    sniped_relevance=(
        "The gallery mechanic. Pairs with B6 sniped-pixieset-gallery + delivery_architecture_v2."
    ),
    direct_quotes=[],
    tags=["pixieset-config", "delivery-sop", "3-tier-gallery", "14-day-window"],
)
add_chunk(
    source_title="Pixieset Config · the upgrade pricing + shop setup",
    source_file="delivery__pixieset_config.md",
    domain="delivery-sop",
    concept="Pixieset shop · upgrade pricing for Select-to-Hero and Proof-to-Select",
    summary=(
        "Pixieset shop pricing (14-day window): Select-to-Hero upgrade = $60 each (5-pack discount). "
        "Proof-to-Select upgrade = $30 each. Single Hero from outside the 10-12 = $250. Shop active "
        "for 14 days only. Stripe payment, auto-trigger retouch for upgraded Heroes (BJ delivers "
        "within 5 business days of payment)."
    ),
    usable_principle=(
        "Upgrade pricing locked. $60 Select-to-Hero, $30 Proof-to-Select, $250 outside-the-12 Hero. "
        "Stripe payment auto-triggers retouch."
    ),
    sniped_relevance=(
        "The Pixieset upsell mechanic. Pairs with Revenue Engine + Path A upsell."
    ),
    direct_quotes=[],
    tags=["pixieset-config", "shop-upgrades", "delivery-sop", "60-30-250-pricing"],
)

# 9 email templates · 1 chunk each
add_chunk(
    source_title="Email · Pre-shoot brief",
    source_file="delivery__email_01_pre_shoot_brief.md",
    domain="delivery-sop",
    concept="Pre-shoot brief email · subject prep 48 hours before shoot day",
    summary=(
        "Pre-shoot brief email sent 48 hours before shoot day. Contents: locked arrival time, "
        "studio address (2715 S Main St, DTLA), wardrobe reminder (photos already submitted), "
        "parking info, what to bring (no makeup if MUA present), what to NOT bring (entourage · "
        "subject only). Trigger: T-48 hours, automated calendar trigger."
    ),
    usable_principle=(
        "Send at T-48. Locked template. No subject-day surprises."
    ),
    sniped_relevance=(
        "Reduces shoot-day friction. Pairs with sniped-pre-shoot-prep skill."
    ),
    direct_quotes=[],
    tags=["email-template", "delivery-sop", "pre-shoot-brief", "t-minus-48-hours"],
)
add_chunk(
    source_title="Email · Day 0 delivery",
    source_file="delivery__email_02_day0_delivery.md",
    domain="delivery-sop",
    concept="Day 0 delivery email · gallery-live notification with 3 suggested deployments",
    summary=(
        "Sent 9 AM PT, Day 5 of SLA. Subject: 'Sniped · your gallery is live'. Body: gallery link + "
        "password, what's inside (Hero/Select/Proof breakdown + upgrade pricing), 3 suggested "
        "deployments by Hero filename (LinkedIn header, press/podcast cover, deck portrait). "
        "Gallery window: 14 days. Trigger: Pixieset gallery is live + tested in incognito."
    ),
    usable_principle=(
        "9 AM PT, locked subject line, 3 suggested deployments. Test gallery in incognito first."
    ),
    sniped_relevance=(
        "Pairs with delivery_architecture_v2 + Pixieset shop."
    ),
    direct_quotes=[
        "Your gallery: [PIXIESET LINK] · password: [PWD]",
    ],
    tags=["email-template", "delivery-sop", "day-0-delivery", "3-suggested-deployments"],
)
add_chunk(
    source_title="Email · Day 7 testimonial",
    source_file="delivery__email_03_day7_testimonial.md",
    domain="delivery-sop",
    concept="Day 7 testimonial request · the trust-signal pull",
    summary=(
        "Sent Day 7 after delivery. Asks for a short (2-3 sentence) testimonial focused on a "
        "specific deployment (which Hero used where + what changed). Includes 3 example formats. "
        "The testimonial gates the Day 30 Op Kit pitch · no testimonial = no upsell ask."
    ),
    usable_principle=(
        "Day 7 timing. Specific-deployment framing (not generic 'great work'). 3 example formats "
        "to lower friction."
    ),
    sniped_relevance=(
        "The trust-signal collection mechanism. Pairs with SOP_post_delivery gate."
    ),
    direct_quotes=[],
    tags=["email-template", "delivery-sop", "day-7-testimonial", "trust-signal"],
)
add_chunk(
    source_title="Email · Day 19 window closing",
    source_file="delivery__email_04_day19_window_closing.md",
    domain="delivery-sop",
    concept="Day 19 window-closing reminder · Pixieset shop closes Day 14, this is the final ask",
    summary=(
        "Sent Day 19 (5 days after Pixieset shop closes). Reminds client of any unfinished upgrades "
        "(Select-to-Hero requests, Proof-to-Select). Light-touch · acknowledges the gallery is now "
        "Hero+Select view-only. No hard sell. Trigger: Day 19 calendar."
    ),
    usable_principle=(
        "Day 19, light-touch. Acknowledge the closed window. No hard sell."
    ),
    sniped_relevance=(
        "Hospitality discipline. Pairs with B3 Guidara service-as-floor."
    ),
    direct_quotes=[],
    tags=["email-template", "delivery-sop", "day-19-window-closing", "light-touch"],
)
add_chunk(
    source_title="Email · Day 30 Op Kit pitch",
    source_file="delivery__email_05_day30_opkit_pitch.md",
    domain="delivery-sop",
    concept="Day 30 Op Kit upsell pitch · gated by testimonial + deployment evidence",
    summary=(
        "Sent Day 30 (gated). Pitches Op Kit ($3-8K multi-direction expansion) referencing the "
        "specific deployment from the Day 0 email + the testimonial received Day 7-14. Frames Op Kit "
        "as the next chapter, not a separate transaction. Includes 1 specific scope idea tailored "
        "to the client's business context."
    ),
    usable_principle=(
        "Day 30 gated by testimonial. Reference specific deployment. 1 tailored scope idea. Frame "
        "as next chapter, not separate transaction."
    ),
    sniped_relevance=(
        "Pairs with B4 SYNTHESIS Section 6.4 three upsell paths + Path A pursuit."
    ),
    direct_quotes=[],
    tags=["email-template", "delivery-sop", "day-30-op-kit-pitch", "next-chapter-framing"],
)
add_chunk(
    source_title="Email · Day 90 reengagement",
    source_file="delivery__email_06_day90_reengagement.md",
    domain="delivery-sop",
    concept="Day 90 reengagement check-in · low-touch relationship maintenance",
    summary=(
        "Sent Day 90 (3 months after delivery). Light check-in: how has the deployment performed? "
        "Any new chapter (round, launch, hire, press) that warrants a refresh shoot? Includes 1 "
        "named-trigger ask (the specific event in their business that would warrant a follow-up "
        "shoot). Low-touch · no Op Kit pitch unless triggered."
    ),
    usable_principle=(
        "Day 90 low-touch. 1 named-trigger ask. No Op Kit pitch unless the client surfaces a trigger."
    ),
    sniped_relevance=(
        "Reputation Engine maintenance. Pairs with sniped-post-delivery skill + B3 Holiday perennial-seller."
    ),
    direct_quotes=[],
    tags=["email-template", "delivery-sop", "day-90-reengagement", "named-trigger-ask"],
)
add_chunk(
    source_title="Email · Referral ask (Day 30-45)",
    source_file="delivery__email_07_referral_ask.md",
    domain="delivery-sop",
    concept="Referral ask email · narrowly-framed two-founder ask",
    summary=(
        "Sent Day 30-45. Asks for TWO specific founder introductions (named criteria · LA founder, "
        "visual gap, would feel good introducing). Not a 'blast my newsletter' ask. Includes offer "
        "to draft the intro language so it's zero-friction for the client. Trigger: testimonial "
        "received + deployment evidence visible."
    ),
    usable_principle=(
        "Two named introductions. Specific criteria. Zero-friction (operator drafts the intro). "
        "Gated by trust signals."
    ),
    sniped_relevance=(
        "Pairs with B4 SYNTHESIS chat-thread Day-3 voice-note + Pearl-network referral discipline."
    ),
    direct_quotes=[
        "Are there two founders or operators in your network who would benefit from the same Direction Stack diagnostic?",
    ],
    tags=["email-template", "delivery-sop", "referral-ask", "two-named-introductions"],
)
add_chunk(
    source_title="Email · Booking confirmation",
    source_file="delivery__email_08_booking_confirmation.md",
    domain="delivery-sop",
    concept="Booking confirmation email · after 50% deposit + shoot scheduled",
    summary=(
        "Sent within 24 hours of 50% deposit + shoot date scheduled. Confirms: shoot date, arrival "
        "time, studio address, 5-hour single-direction format, what to bring + not bring, MUA "
        "schedule (if applicable), pre-shoot brief auto-trigger (T-48 hours). Includes calendar "
        "invite attachment."
    ),
    usable_principle=(
        "Within 24 hours of deposit. Locked template. Calendar invite attached. Pre-shoot brief auto-triggers."
    ),
    sniped_relevance=(
        "Reduces post-booking anxiety. Pairs with sop_discovery_to_close."
    ),
    direct_quotes=[],
    tags=["email-template", "delivery-sop", "booking-confirmation", "calendar-invite"],
)
add_chunk(
    source_title="Email · No-show or late followup",
    source_file="delivery__email_09_no_show_or_late_followup.md",
    domain="delivery-sop",
    concept="No-show / late followup · the two-strike-rule application",
    summary=(
        "Sent same-day after a no-show or significant late arrival. Tone: firm but not punitive. "
        "Notes the strike (first or second per two-strike rule). For first strike: offers reschedule "
        "with $200 reschedule fee. For second strike: cancellation + 50% deposit retained per "
        "contract. Includes calendar link for reschedule (if applicable)."
    ),
    usable_principle=(
        "Send same-day. Firm but not punitive. Two-strike rule applies. Reschedule fee $200 first "
        "strike."
    ),
    sniped_relevance=(
        "Pairs with casting_call_doctrine two-strike rule + contracts."
    ),
    direct_quotes=[],
    tags=["email-template", "delivery-sop", "no-show-followup", "two-strike-rule"],
)


# ===========================================================================
# P5 · Content docs · 7 sources · ~26 chunks
# ===========================================================================

# audience_engine.md · 375L · 4 chunks
add_chunk(
    source_title="Audience Engine · operating doctrine",
    source_file="content__audience_engine.md",
    domain="content-strategy",
    concept="The Audience Engine · cultural gravity layer · IG + LinkedIn as different jobs",
    summary=(
        "Audience Engine = cultural gravity + discovery layer. NOT subordinate to Revenue. NOT a "
        "marketing afterthought. The engine produces taste-archive output (IG) + thought-position "
        "output (LinkedIn). IG and LinkedIn have different jobs: IG = mythology + aesthetic gravity; "
        "LinkedIn = trust + credibility + B2B conversion. Both are co-equal primary surfaces."
    ),
    usable_principle=(
        "IG = mythology. LinkedIn = trust. Different jobs. Both co-equal. The Audience Engine is "
        "load-bearing, not a marketing afterthought."
    ),
    sniped_relevance=(
        "Pairs with feedback_platform_split + 3-engine architecture + intel_distribution_mechanics."
    ),
    direct_quotes=[],
    tags=["audience-engine", "content-strategy", "ig-vs-linkedin", "co-equal-primary"],
)
add_chunk(
    source_title="Audience Engine · the Museum Room Theory",
    source_file="content__audience_engine.md",
    domain="content-strategy",
    concept="Museum Room Theory · the SNIPED Card system as the curatorial spine",
    summary=(
        "Museum Room Theory: every IG grid is a curated museum room. Each chapter card (B&W "
        "dual-register per Lock 2) anchors a 'room' of 6-12 HERO posts (color). Visitors browse "
        "rooms; the curator decides what hangs where. Card system pre-positions the grid for "
        "Year 2-3 fan-page distribution architecture · cards become the surface where new visitors "
        "land first."
    ),
    usable_principle=(
        "Every chapter = one museum room (card + 6-12 HERO). Card = B&W spine. HERO = color content. "
        "Visitors browse rooms, not individual posts."
    ),
    sniped_relevance=(
        "Pairs with intel_distribution_mechanics Museum Room validation + feedback_bw_card_dual_register."
    ),
    direct_quotes=[],
    tags=["audience-engine", "museum-room-theory", "content-strategy", "card-system"],
)
add_chunk(
    source_title="Audience Engine · the HERO + Card dual-register",
    source_file="content__audience_engine.md",
    domain="content-strategy",
    concept="HERO post + Chapter Card dual-register · color for moment, B&W for document",
    summary=(
        "HERO posts render in full v3 LUXURY color · the moment, the live frame, the cultural "
        "gravity output. Chapter Cards render in B&W · the document, the spine, the apparatus-layer "
        "framing. Dual-register doctrine LOCKED 2026-05-13 per Aperture/LIFE/Magnum tradition. "
        "Apparatus stays color. Card = document. HERO = moment."
    ),
    usable_principle=(
        "HERO = color. Card = B&W. Apparatus = color. The dual-register is locked · do not mix."
    ),
    sniped_relevance=(
        "Pairs with feedback_bw_card_dual_register + Lock 2."
    ),
    direct_quotes=[],
    tags=["audience-engine", "hero-card-dual-register", "content-strategy", "bw-card", "color-hero"],
)
add_chunk(
    source_title="Audience Engine · the LinkedIn POV bank",
    source_file="content__audience_engine.md",
    domain="content-strategy",
    concept="LinkedIn POV bank · thought-position posts that feed the trust + conversion layer",
    summary=(
        "LinkedIn POV bank: pre-drafted thought-positions on SNIPED operating themes (premium "
        "pricing, refusal as positioning, the Direction Stack methodology, anti-AI hybrid stance, "
        "lineage doctrine, scene-density thinking, the 4-7 person Year-10, perennial-seller logic, "
        "Cultural Doc as compounding asset). Used to feed 1-2 LinkedIn posts/week + comment-doctrine "
        "ammo. Maintain ~20 ready-to-ship POVs at any time."
    ),
    usable_principle=(
        "Maintain 20+ ready POVs. Ship 1-2/week. POVs feed both posts and comments. Never run out."
    ),
    sniped_relevance=(
        "Pairs with linkedin_pov_bank source + sniped-positioning-phrases skill."
    ),
    direct_quotes=[],
    tags=["audience-engine", "linkedin-pov-bank", "content-strategy", "thought-position"],
)

# caption_templates.md · 219L · 2 chunks
add_chunk(
    source_title="Caption Templates",
    source_file="content__caption_templates.md",
    domain="content-strategy",
    concept="Caption template library · 6 named formats for IG + LinkedIn",
    summary=(
        "6 caption template formats: (1) HERO-with-context (1-2 sentences naming the subject's "
        "chapter); (2) chapter-card-anchor (3-4 sentences introducing the chapter room); (3) "
        "BTS-process (apparatus-layer, behind the work); (4) Cultural-Doc-cluster (subject + "
        "lineage + scene-density); (5) LinkedIn-POV (thought-position with hook + body + close); "
        "(6) refusal-framing (named-no anchored to a specific principle)."
    ),
    usable_principle=(
        "6 formats. Match format to post type. Never improvise. Templates are the speed unlock."
    ),
    sniped_relevance=(
        "Pairs with B6 sniped-caption-writer skill + hook_library."
    ),
    direct_quotes=[],
    tags=["caption-templates", "content-strategy", "6-formats", "speed-unlock"],
)
add_chunk(
    source_title="Caption Templates · the no-em-dash rule + voice constraints",
    source_file="content__caption_templates.md",
    domain="content-strategy",
    concept="Caption voice constraints · em-dash ban, no AI-fluff, severity over warmth",
    summary=(
        "Voice constraints applied to every caption: NO em-dashes (lifetime rule). NO AI-fluff "
        "phrases (unlock potential / supercharge / dive deep / level up / journey). Severity over "
        "warmth as default register. Refusal language preferred over feature language. Caption "
        "ends with a specific question or specific named-refusal · never a generic CTA."
    ),
    usable_principle=(
        "No em-dashes. No AI-fluff. Severity > warmth. End with specificity, not generic CTA."
    ),
    sniped_relevance=(
        "Lifetime voice discipline. Pairs with THE SPINE Section 12 voice rules + global CLAUDE.md em-dash ban."
    ),
    direct_quotes=[],
    tags=["caption-templates", "no-em-dashes", "content-strategy", "no-ai-fluff", "severity-default"],
)

# cultural_documentation_thesis.md · 153L · 2 chunks
add_chunk(
    source_title="Cultural Documentation Thesis",
    source_file="content__cultural_documentation_thesis.md",
    domain="content-strategy",
    concept="Cultural Doc thesis · the compounding-engine output spec",
    summary=(
        "Cultural Doc thesis: photograph the operator-class of modern Black LA founder + artist + "
        "athletic + intellectual culture from INSIDE the 5 lineages. Not journalism (no external "
        "gaze). Not portraiture-as-commodity (no agency commission). Not influencer (no algorithm "
        "optimization). The output is a multi-decade authored body of work that the AI commodity "
        "cannot replace. The thesis grounds the Reputation Engine."
    ),
    usable_principle=(
        "Cultural Doc = from inside the lineage, multi-decade, named-figures-as-individuals, no "
        "external gaze. The output is the compounding asset."
    ),
    sniped_relevance=(
        "The compounding-engine output. Pairs with Lineage Doctrine + Reputation Engine + B5 Day "
        "on personal documentary lineage."
    ),
    direct_quotes=[],
    tags=["cultural-doc-thesis", "content-strategy", "compounding-engine", "5-lineages"],
)
add_chunk(
    source_title="Cultural Documentation Thesis · the 10-year subject-honor test",
    source_file="content__cultural_documentation_thesis.md",
    domain="content-strategy",
    concept="10-year subject-honor test · the publish gate",
    summary=(
        "Before publishing any Cultural Doc frame, run the 10-year subject-honor test: would the "
        "subject, 10 years from now, looking back at this frame + this caption, feel honored? If "
        "no, don't publish. The test prevents categorical-trap flattening (Black-joy as marketing "
        "category, Black-trauma as editorial extraction, Black-culture as brand generalization)."
    ),
    usable_principle=(
        "10-year subject-honor test is the publish gate. If no, don't publish."
    ),
    sniped_relevance=(
        "The ethical discipline. Pairs with Lineage Doctrine + B5 ethics domain."
    ),
    direct_quotes=[
        "Would the subject, 10 years from now, looking back at this frame and this caption, feel honored? If no, don't publish.",
    ],
    tags=["cultural-doc-thesis", "10-year-test", "content-strategy", "publish-gate"],
)

# hook_library.md · 170L · 2 chunks
add_chunk(
    source_title="Hook Library",
    source_file="content__hook_library.md",
    domain="content-strategy",
    concept="Hook library · 8 named hook formats for IG + LinkedIn",
    summary=(
        "8 hook formats: (1) named-refusal opener; (2) specific-number opener (12 Heroes, 5 lineages, "
        "$1,500 floor); (3) chapter-anchor (introduces a specific named subject); (4) lineage-callback "
        "(specific cultural-circle reference); (5) doctrine-quote (anchored to a canonical truth); "
        "(6) before-and-after (operational mismatch -> SNIPED-grade); (7) misconception-correction "
        "(industry-wide false belief -> SNIPED-locked rule); (8) named-figure quote attribution."
    ),
    usable_principle=(
        "8 hook formats. Choose by post type. Hooks ship without writer's block. Library is the "
        "speed unlock."
    ),
    sniped_relevance=(
        "Pairs with caption_templates + B2 Hit Makers MAYA principle (familiar + surprising)."
    ),
    direct_quotes=[],
    tags=["hook-library", "content-strategy", "8-hook-formats", "speed-unlock"],
)
add_chunk(
    source_title="Hook Library · the specificity-signal rule",
    source_file="content__hook_library.md",
    domain="content-strategy",
    concept="Specificity-signal rule · every hook names a specific number, name, or rule",
    summary=(
        "Every hook names something specific · a number, a name, a locked rule, a named-figure, a "
        "specific location. Generic hooks ('photography is changing', 'AI is here') are forbidden. "
        "Specificity = signal. The reader knows within the first 8 words whether the post is for "
        "them. The specificity-signal rule applies to both IG captions and LinkedIn POV openers."
    ),
    usable_principle=(
        "Specific number / name / rule in the first 8 words. Never generic. Specificity = signal."
    ),
    sniped_relevance=(
        "The signal-density technique. Pairs with intel_positioning_phrases + caption_templates."
    ),
    direct_quotes=[],
    tags=["hook-library", "specificity-signal", "content-strategy", "first-8-words"],
)

# linkedin_pov_bank.md · 365L · 4 chunks
add_chunk(
    source_title="LinkedIn POV Bank · structure",
    source_file="content__linkedin_pov_bank.md",
    domain="content-strategy",
    concept="LinkedIn POV bank · pre-drafted thought-positions for the trust + conversion layer",
    summary=(
        "POV bank structure: each POV has a hook (8 words max), body (3-5 paragraphs of stated "
        "operating position), close (1-2 sentence specific question or named-refusal). Maintains "
        "20+ ready-to-ship POVs at any time. Topics rotate across the 12 canonical truths, the "
        "10 operating locks, the lineage doctrine, anti-AI hybrid stance, perennial-seller logic, "
        "Cultural Doc as compounding asset, the 4-7 person Year-10 destination."
    ),
    usable_principle=(
        "POV = hook + body + close. 20+ ready-to-ship. Topics rotate across canon. 1-2 ship per week."
    ),
    sniped_relevance=(
        "The LinkedIn thought-position layer. Pairs with audience_engine + sniped-positioning-phrases."
    ),
    direct_quotes=[],
    tags=["linkedin-pov-bank", "content-strategy", "hook-body-close", "20-ready-povs"],
)
add_chunk(
    source_title="LinkedIn POV Bank · the refusal-as-positioning POV cluster",
    source_file="content__linkedin_pov_bank.md",
    domain="content-strategy",
    concept="Refusal-as-positioning POVs · the named-no catalog ported to thought-position format",
    summary=(
        "Refusal POV cluster: each POV stakes a specific named-refusal as the central claim. Examples: "
        "'I refuse $300 commodity headshots and here's why', 'SNIPED is not influencer photography', "
        "'Sprint $750 is never cold-pitched', 'I do not do single-visit cultural tourism'. The "
        "cluster is the highest-converting POV category · refusal generates stronger reader signal "
        "than feature-listing."
    ),
    usable_principle=(
        "Refusal POVs convert best. Stake a specific named-no as the central claim. Explain the "
        "operating logic behind the no."
    ),
    sniped_relevance=(
        "Pairs with named-refusals catalog + intel_positioning_phrases refusal-positioning lever."
    ),
    direct_quotes=[],
    tags=["linkedin-pov-bank", "refusal-as-positioning", "content-strategy", "named-no"],
)
add_chunk(
    source_title="LinkedIn POV Bank · the doctrine-explainer POV cluster",
    source_file="content__linkedin_pov_bank.md",
    domain="content-strategy",
    concept="Doctrine-explainer POVs · making the operating system teachable on LinkedIn",
    summary=(
        "Doctrine-explainer cluster: each POV explains one element of the SNIPED operating system "
        "(Direction Stack 5 questions, controlled-abundance delivery, 3-engine architecture, "
        "5 lineages, 10-year test, scene-density thinking, methodology-as-IP). Teaches the doctrine "
        "in 3-5 paragraphs. The cluster grounds SNIPED as a teaching authority, not just a "
        "service provider."
    ),
    usable_principle=(
        "Doctrine-explainer = one element per POV, 3-5 paragraphs, teachable form. Builds authority."
    ),
    sniped_relevance=(
        "Pairs with B3 Holiday platform-before-launch + Naval productize-yourself."
    ),
    direct_quotes=[],
    tags=["linkedin-pov-bank", "doctrine-explainer", "content-strategy", "teaching-authority"],
)
add_chunk(
    source_title="LinkedIn POV Bank · the named-figure callback POV cluster",
    source_file="content__linkedin_pov_bank.md",
    domain="content-strategy",
    concept="Named-figure callback POVs · referencing specific operators + photographers as proof",
    summary=(
        "Named-figure callback cluster: each POV references a specific operator, photographer, or "
        "named figure as proof or counter-example. Avedon's apparatus, Sontag's noeme, Barthes's "
        "that-has-been, Stoute's cultural capital, Naval's leverage trilogy, Enns's refusal-positioning, "
        "Guidara's hospitality-as-ceiling. Specific names > generic 'experts say'. Pairs with the "
        "BATCH_005 photography canon for retrieval."
    ),
    usable_principle=(
        "Named figures, not 'experts'. Specific photographers, operators, thinkers. Pull from the "
        "canon · don't invent."
    ),
    sniped_relevance=(
        "Pairs with B5 photography canon + B6 SNIPED skills that wrap intel-memory canon."
    ),
    direct_quotes=[],
    tags=["linkedin-pov-bank", "named-figure-callback", "content-strategy", "specific-names"],
)

# sniped_content_philosophy.md · 673L · 7 chunks (with legacy-language-sweep-pending on AI-cluster)
add_chunk(
    source_title="SNIPED Content Philosophy · what SNIPED IS NOT",
    source_file="content__sniped_content_philosophy.md",
    domain="content-strategy",
    concept="SNIPED is not · the 3 named-refusal categories",
    summary=(
        "SNIPED is NOT influencer photography (no trendy color grades, no teal/orange, no fake film "
        "grain, no Sedona dust, no 'best Instagram presets 2024' edits). SNIPED is NOT creator slop "
        "(no 7-platform 15-posts/day, no reactive trend-chasing, no first-comment-for-link bait). "
        "SNIPED is NOT a personal/Eagle Rock home-studio narrative (Eagle Rock is where BJ lives; "
        "the studio is DTLA at 2715 S Main St). Public-facing materials use 'DTLA studio' only."
    ),
    usable_principle=(
        "Three locked refusal categories. Never drift into any of the three."
    ),
    sniped_relevance=(
        "The named-refusal foundation. Pairs with 65+ refusals catalog + intel_positioning_phrases failure modes."
    ),
    direct_quotes=[
        "SNIPED is not influencer photography.",
        "SNIPED is not creator slop.",
        "Public-facing materials use 'DTLA studio' or 'Downtown LA studio.' Period.",
    ],
    tags=["content-philosophy", "content-strategy", "named-refusals", "dtla-studio-only"],
)
add_chunk(
    source_title="SNIPED Content Philosophy · the identity claim",
    source_file="content__sniped_content_philosophy.md",
    domain="content-strategy",
    concept="The SNIPED identity claim · the load-bearing one-paragraph definition",
    summary=(
        "SNIPED Media is the visual operating system + cultural infrastructure for LA's emerging "
        "founder, artist, and operator culture. Operator-coded. DTLA-anchored. Florida-raised. "
        "Engineering-trained. Methodology-first. Body-of-work-driven. Two engines run simultaneously: "
        "transactional (LinkedIn / VIB -> Reset -> Op Kit -> Brand System) + compounding (Access, "
        "Community, Cultural Documentation). Photography is the entry point; the actual product is "
        "methodology, taste, direction, access, infrastructure, authority, IP, network, media leverage."
    ),
    usable_principle=(
        "This paragraph is the load-bearing identity claim. Reference verbatim in positioning copy. "
        "The compounding engine builds the asset that AI cannot commodify in 5 years."
    ),
    sniped_relevance=(
        "The most cited paragraph in the corpus. Pairs with B4 STRATEGIC_PRINCIPLES 15-source paragraph."
    ),
    direct_quotes=[
        "Photography is the entry point; the actual product is methodology, taste, direction, access, infrastructure, authority, IP, network, and media leverage.",
        "The compounding engine builds the asset that AI cannot commodify in 5 years.",
    ],
    tags=["content-philosophy", "content-strategy", "identity-claim", "two-engines", "ai-cannot-commodify", "legacy-language-sweep-pending"],
)
add_chunk(
    source_title="SNIPED Content Philosophy · the 7-signature SNIPED frame test",
    source_file="content__sniped_content_philosophy.md",
    domain="content-strategy",
    concept="7-signature frame test · the thumbnail-readable SNIPED signal",
    summary=(
        "A SNIPED image, at thumbnail size, reads as SNIPED if all 7 signatures are true: (1) "
        "restraint as dominant register; (2) [signature 2]; (3) [signature 3]; (4) clinical retouch "
        "(skin unified, color casts equalized, pore detail preserved, no plastic smoothing); (5) "
        "[signature 5]; (6) [signature 6]; (7) severity, not warmth, as default register. If a "
        "frame fails 4 of 7, it's not SNIPED · don't post."
    ),
    usable_principle=(
        "Run the 7-signature test before posting. 4+ fails = don't post. Test applies to HERO, "
        "Card, IG, LinkedIn equally."
    ),
    sniped_relevance=(
        "The publish-gate at the frame level. Pairs with B4 Aesthetic Statement 5-descriptors filter."
    ),
    direct_quotes=[
        "If a frame fails 4 of 7, it's not SNIPED. Don't post.",
    ],
    tags=["content-philosophy", "7-signature-test", "content-strategy", "publish-gate", "severity-default"],
)
add_chunk(
    source_title="SNIPED Content Philosophy · the single intentional element rule",
    source_file="content__sniped_content_philosophy.md",
    domain="content-strategy",
    concept="Single intentional element · one detail set deliberately apart from baseline",
    summary=(
        "The Production Stack's 'one thing' rule: one detail set deliberately apart from the "
        "baseline. One impossible color. One prop. One gesture. The other 99% of the frame is "
        "competent; the 1% carries it. The rule prevents over-design and protects restraint as "
        "the dominant register."
    ),
    usable_principle=(
        "One intentional element per frame. 99% competence + 1% deliberate departure. Anything "
        "more = over-design."
    ),
    sniped_relevance=(
        "Frame-design discipline. Pairs with restraint-as-default register."
    ),
    direct_quotes=[
        "One detail set deliberately apart from the baseline.",
    ],
    tags=["content-philosophy", "single-intentional-element", "content-strategy", "one-thing-rule"],
)
add_chunk(
    source_title="SNIPED Content Philosophy · the operator-engineering principles",
    source_file="content__sniped_content_philosophy.md",
    domain="content-strategy",
    concept="Operator-engineering principles · systems > inspiration, methodology > improvisation",
    summary=(
        "Operator-engineering principles: (1) Locked-frame methodology (Shore's locked-geometry-"
        "before-subject is the engineering analog · build the frame, then subject enters · refuse "
        "to chase the moment); (2) System over inspiration (Direction Stack is reliable, inspiration "
        "is not · engineers ship working systems on schedule); (3) Pricing is the price (operators "
        "don't justify, they state · Reset is $1,500, the conversation is scope not price)."
    ),
    usable_principle=(
        "Build the frame first, then the subject enters. System > inspiration. State pricing, "
        "never justify."
    ),
    sniped_relevance=(
        "The operator-engineering identity claim. Pairs with engineering-trained lineage + Stephen Shore lineage."
    ),
    direct_quotes=[
        "Stephen Shore's locked-geometry-before-subject is the engineering analog.",
    ],
    tags=["content-philosophy", "operator-engineering", "content-strategy", "system-over-inspiration", "locked-frame"],
)
add_chunk(
    source_title="SNIPED Content Philosophy · the 10-year test",
    source_file="content__sniped_content_philosophy.md",
    domain="content-strategy",
    concept="The 10-year test · does this image still hold in 5 years, still represent SNIPED in 10?",
    summary=(
        "The 10-year test: does this image still hold in 5 years? Will it still represent SNIPED "
        "in 10? If no, don't post. The test is the perennial-seller filter applied at the frame "
        "level. Pairs with the 10-year subject-honor test (cultural documentation) and the "
        "perennial-creator principle from B3 Holiday."
    ),
    usable_principle=(
        "10-year test before every post. If the frame doesn't still represent SNIPED in 10 years, "
        "don't post."
    ),
    sniped_relevance=(
        "Pairs with B3 Holiday perennial-seller + 10-year subject-honor test + Lock 10."
    ),
    direct_quotes=[
        "The 10-year test: does this image still hold in 5 years? Will it still represent SNIPED in 10? If no, don't post.",
    ],
    tags=["content-philosophy", "10-year-test", "content-strategy", "perennial-seller", "publish-gate"],
)
add_chunk(
    source_title="SNIPED Content Philosophy · the editorial-fashion vs SNIPED distinction",
    source_file="content__sniped_content_philosophy.md",
    domain="content-strategy",
    concept="Editorial fashion vs SNIPED · subject-interchangeable vs subject-specific",
    summary=(
        "Editorial fashion: model + stylist + agency + magazine. Subject is interchangeable; the "
        "styling is the point. Optimizes for magazine cover, brand campaign, lookbook. SNIPED is "
        "the opposite. Subject is non-interchangeable (this specific operator, this specific "
        "chapter, this specific moment). Styling serves the subject, not vice versa. The distinction "
        "is what makes SNIPED a Cultural Doc lane and not an editorial-fashion lane."
    ),
    usable_principle=(
        "Subject is non-interchangeable. Styling serves the subject. Refuse styling-as-the-point."
    ),
    sniped_relevance=(
        "The lane-clarity distinction. Pairs with Cultural Doc thesis + Lineage Doctrine."
    ),
    direct_quotes=[
        "Subject is interchangeable; the styling is the point. SNIPED does the opposite.",
    ],
    tags=["content-philosophy", "editorial-vs-sniped", "content-strategy", "subject-non-interchangeable"],
)

# sniped_video_philosophy.md · 480L · 5 chunks
add_chunk(
    source_title="SNIPED Video Philosophy · what it IS NOT",
    source_file="content__sniped_video_philosophy.md",
    domain="content-strategy",
    concept="SNIPED video is not · the named-refusal video categories",
    summary=(
        "SNIPED video is NOT a tutorial (no 'watch how I edit this in Lightroom', no '5 lighting "
        "setups every photographer needs'). Methodology is taught in the book + Substack essays + "
        "LinkedIn POVs, not in algorithm-bait video. SNIPED video is NOT a cinematic reel set to "
        "lo-fi beats (no fake film grain, no teal/orange grade, no drone establishing shots that "
        "exist for their own sake)."
    ),
    usable_principle=(
        "No tutorial video. No cinematic reels. Methodology = book + Substack + LinkedIn, not "
        "video bait."
    ),
    sniped_relevance=(
        "Pairs with content_philosophy named-refusal cluster + Lock 7 visual direction."
    ),
    direct_quotes=[
        "Not a tutorial.",
        "Not a cinematic reel set to lo-fi beats.",
    ],
    tags=["video-philosophy", "content-strategy", "named-refusals", "no-tutorial-video"],
)
add_chunk(
    source_title="SNIPED Video Philosophy · the cinematographer lineage",
    source_file="content__sniped_video_philosophy.md",
    domain="content-strategy",
    concept="Cinematographer lineage · Bradford Young / Khalil Joseph / Barry Jenkins / Hiro Murai / Wong Kar-wai",
    summary=(
        "Cinematographer lineage for SNIPED video: Bradford Young (color restraint, the held shot), "
        "Khalil Joseph (pacing weight, music as structure not decoration), Barry Jenkins / James "
        "Laxton (Moonlight + Beale Street · tonal restraint, refusal of overexposure), Hiro Murai "
        "(Atlanta · atmospheric Black urban contemporary, the held mood), Wong Kar-wai / Christopher "
        "Doyle (saturated urban color, used selectively for studio shots, never for documentary)."
    ),
    usable_principle=(
        "Reference cinematographer lineage explicitly. The 'cinematic' register is named, not loose. "
        "Bradford Young / Khalil Joseph / Jenkins / Murai / Wong Kar-wai are the locked references."
    ),
    sniped_relevance=(
        "Pairs with B4 SYNTHESIS Contradiction 3 ('cinematic' disambiguation: loose = drift, "
        "specific named-reference = signature)."
    ),
    direct_quotes=[
        "Khalil Joseph · Pacing weight · the refusal to explain · music as structure not decoration",
        "Barry Jenkins / Laxton · Held shots of stillness · tonal restraint · the long look",
    ],
    tags=["video-philosophy", "cinematographer-lineage", "content-strategy", "bradford-young", "khalil-joseph", "barry-jenkins"],
)
add_chunk(
    source_title="SNIPED Video Philosophy · pacing + restraint discipline",
    source_file="content__sniped_video_philosophy.md",
    domain="content-strategy",
    concept="Pacing + restraint · the held shot, the refusal-to-explain edit",
    summary=(
        "SNIPED video pacing: held shots, restrained cuts, refusal to over-explain. The Khalil "
        "Joseph reference is most load-bearing · pacing weight, music doing structural work, the "
        "refusal-to-narrate. Documentary cuts hold longer than commercial cuts. Music selection "
        "names a specific cultural register, never generic 'cinematic score' library tracks."
    ),
    usable_principle=(
        "Hold the shot longer than feels comfortable. Music does structural work, not decoration. "
        "Never narrate what the frame already shows."
    ),
    sniped_relevance=(
        "Editor instruction. Pairs with retoucher_training_notes operator-handoff discipline."
    ),
    direct_quotes=[],
    tags=["video-philosophy", "pacing-restraint", "content-strategy", "held-shot", "khalil-joseph"],
)
add_chunk(
    source_title="SNIPED Video Philosophy · format + length spec",
    source_file="content__sniped_video_philosophy.md",
    domain="content-strategy",
    concept="Video format + length spec · 7x7 cutdown architecture",
    summary=(
        "Format spec: short (15-30 sec) for IG Reels + LinkedIn quick; medium (60-90 sec) for "
        "chapter-card BTS; long (3-5 min) for Cultural Doc cluster + Direction Stack book promo. "
        "The 7x7 cutdown architecture: one shoot session produces 7 different-length cuts across "
        "7 different surface-purpose combinations. The cutdown is the leverage."
    ),
    usable_principle=(
        "One shoot = 7 cuts across 7 surface-purposes. 15-30 / 60-90 / 3-5 min are the locked "
        "length brackets."
    ),
    sniped_relevance=(
        "Pairs with B1 Attention Stack 7x7 cutdown workflow + Remotion automation (B6)."
    ),
    direct_quotes=[],
    tags=["video-philosophy", "7x7-cutdown", "content-strategy", "length-spec", "leverage"],
)
add_chunk(
    source_title="SNIPED Video Philosophy · the apparatus-layer documentation",
    source_file="content__sniped_video_philosophy.md",
    domain="content-strategy",
    concept="Apparatus-layer video · BTS that documents the operator-engine, not the operator",
    summary=(
        "Apparatus-layer video documents the operator-engine in motion: the studio setup, the "
        "lighting build, the cull pass, the retoucher workflow, the VIB Figma build. Audience: "
        "future operators (who recognize the apparatus) + future clients (who understand the "
        "engineering effort behind their shoot). The apparatus stays color · per Lock 2 the Card "
        "is B&W, but apparatus BTS is full color (it documents process, not moment)."
    ),
    usable_principle=(
        "Apparatus BTS = color. Documents process, not moment. Audience = future operators + "
        "future clients."
    ),
    sniped_relevance=(
        "Pairs with feedback_bw_card_dual_register apparatus-layer framing + B5 Stevens-Avedon "
        "studio-as-apparatus."
    ),
    direct_quotes=[],
    tags=["video-philosophy", "apparatus-layer", "content-strategy", "bts-color", "studio-as-apparatus"],
)


# ===========================================================================
# P6 · Commercial / network singletons · 3 sources · ~7 chunks
# ===========================================================================

# delivery_architecture_v2.md · 288L · 3 chunks (with stale-hero-count tag)
add_chunk(
    source_title="Delivery Architecture v2 · LOCKED",
    source_file="offers__delivery_architecture_v2.md",
    domain="commercial-architecture",
    concept="Delivery Architecture v2 · the locked HERO / SELECT / PROOF 3-tier delivery model",
    summary=(
        "v2 delivery architecture: HERO tier (Lightroom base + Evoto clinical retouch + Photoshop "
        "final pass · 10-15 min · editorial deployment · LinkedIn header / press / deck / paid "
        "licensing). SELECT tier (color-graded only · 3-4 min · social + secondary deployment). "
        "PROOF tier (batch-graded · 30 sec/frame · upgrade-only via Pixieset shop). Each Reset "
        "ships 10-12 Heroes + 30-40 Selects + 60-100 Proofs. v2 supersedes the v1 hero-count "
        "range of 8 (canonical floor is now 10, not 8 · per B4 SYNTHESIS Contradiction 4)."
    ),
    usable_principle=(
        "10-12 Heroes (canonical · not 8). 30-40 Selects. 60-100 Proofs. Per-tier time budgets locked."
    ),
    sniped_relevance=(
        "The commercial delivery backbone. Pairs with Pixieset config + delivery emails + Reset "
        "$1,500 floor."
    ),
    direct_quotes=[
        "Promote 8-12 to HERO tier (10-15 min each)",
        "The Hero count is the load-bearing number. Everything else flexes.",
    ],
    tags=["delivery-architecture-v2", "commercial-architecture", "hero-select-proof", "10-12-heroes", "stale-hero-count-8-vs-10-12"],
)
add_chunk(
    source_title="Delivery Architecture v2 · Strategic Free Community + Access modes",
    source_file="offers__delivery_architecture_v2.md",
    domain="commercial-architecture",
    concept="Strategic Free Community + Access · two named-trade modes for free shoots",
    summary=(
        "Strategic Free has 2 named modes. Community (institutional · church / cultural / HBCU): "
        "5-10 named-subject Heroes + 30-50 institutional-grade + 60-100 raw archive · 2-3 hr · "
        "$0 to institution + paid family portraits at event. Access (event / promoter coverage): "
        "10-20 Hero frames for SNIPED archive + 50-100 event coverage + 150-300 raw event archive · "
        "2-3 hr · $0 + commercial introduction as the trade. Strategic Free feeds the Reputation Engine."
    ),
    usable_principle=(
        "Strategic Free is strategic. Always trade · family-portrait-paid (Community) or "
        "commercial-introduction (Access). Free without trade = drift."
    ),
    sniped_relevance=(
        "Pairs with SOP_strategic_free + Reputation Engine."
    ),
    direct_quotes=[],
    tags=["delivery-architecture-v2", "strategic-free", "commercial-architecture", "community-mode", "access-mode"],
)
add_chunk(
    source_title="Delivery Architecture v2 · the 14-day window mechanic",
    source_file="offers__delivery_architecture_v2.md",
    domain="commercial-architecture",
    concept="14-day gallery window · Proofs hidden after Day 14, Hero/Select stay",
    summary=(
        "Window mechanic: all three sub-collections live for 14 days. The Proofs sub-collection "
        "becomes hidden after Day 14; Heroes + Selects stay accessible for the full gallery window. "
        "The 48-hour artificial scarcity (legacy v1) is GONE; the natural gallery expiry is the "
        "only time pressure. Upgrade pricing: $60 Select-to-Hero, $30 Proof-to-Select, $250 "
        "outside-the-12 Hero, 5-pack discounts."
    ),
    usable_principle=(
        "14 days for all 3 collections. Day 14+: Proofs hidden, Hero/Select stay. No artificial "
        "48-hr scarcity. Natural gallery expiry only."
    ),
    sniped_relevance=(
        "Pairs with Pixieset config + delivery emails + Day 19 window-closing reminder."
    ),
    direct_quotes=[
        "The 48-hour artificial scarcity is GONE; the natural gallery expiry is the only time pressure.",
    ],
    tags=["delivery-architecture-v2", "14-day-window", "commercial-architecture", "no-artificial-scarcity"],
)

# notion_crm_schemas.md · 218L · 2 chunks
add_chunk(
    source_title="Notion CRM Schemas",
    source_file="crm__notion_crm_schemas.md",
    domain="commercial-architecture",
    concept="Notion CRM schema · the migration target from Excel · per-table field spec",
    summary=(
        "Notion CRM schema spec. 4 main databases: Leads (ICP 4-of-4 + visual gap + tier + status + "
        "VIB sent date + reply date + booking status), Clients (Reset / Sprint / Op Kit / Brand "
        "System bookings + deposit / final payment / deployment notes), Strategic Free (Community + "
        "Access events + named-subject trades + introduction trail), Cultural Doc (named-figure "
        "relationships + chapter / lineage tags + last-contact + next-contact). Excel-to-Notion "
        "field mapping included."
    ),
    usable_principle=(
        "4 databases. Field-mapping from Excel preserves all current data. Migrate when BJ stands "
        "up the Notion workspace."
    ),
    sniped_relevance=(
        "The CRM migration target. Pairs with B6 sniped-notion-crm-update + SOP_assistant CRM "
        "ownership."
    ),
    direct_quotes=[],
    tags=["notion-crm-schemas", "commercial-architecture", "4-databases", "excel-to-notion-migration"],
)
add_chunk(
    source_title="Notion CRM Schemas · the warm-network gate for Sprint",
    source_file="crm__notion_crm_schemas.md",
    domain="commercial-architecture",
    concept="Warm-network gate · Sprint bookings require a Notion-documented warm-network path",
    summary=(
        "Sprint ($750) bookings require a documented warm-network path in the Notion CRM · referrer "
        "name + relationship + when-warmed timestamp. No Sprint booking can be opened without the "
        "warm-network field populated. This is the Sprint-never-cold-pitched guardrail enforced at "
        "the CRM layer (per B4 SYNTHESIS Section 6.3)."
    ),
    usable_principle=(
        "Sprint requires Notion warm-network field. Cold lead = no Sprint, ever."
    ),
    sniped_relevance=(
        "CRM-layer guardrail for the Sprint pricing discipline. Pairs with operating-locks Lock 8."
    ),
    direct_quotes=[],
    tags=["notion-crm-schemas", "warm-network-gate", "commercial-architecture", "sprint-never-cold"],
)

# access_and_community_architecture.md · 171L · 2 chunks
add_chunk(
    source_title="Access + Community Architecture",
    source_file="network__access_and_community_architecture.md",
    domain="commercial-architecture",
    concept="Access + Community architecture · the network-as-inheritance map",
    summary=(
        "Access + Community architecture: 4 named-circle clusters anchored in LA Black founder + "
        "artist + intellectual + athletic culture. Each cluster names the gatekeeper relationships, "
        "the institutional anchors, the trade-pattern (what SNIPED gives, what the cluster gives "
        "back). The architecture is the network-as-inheritance moat (B4 SYNTHESIS Moat 8). Network "
        "depth compounds over the decade arc."
    ),
    usable_principle=(
        "4 cluster map. Trade-pattern is named per cluster. Network is inherited from operator + "
        "cultural lineage, not built from cold outreach."
    ),
    sniped_relevance=(
        "Pairs with B4 moat-surfaces Moat 8 + Lineage Doctrine + Reputation Engine."
    ),
    direct_quotes=[],
    tags=["access-community-architecture", "commercial-architecture", "4-cluster-map", "network-as-inheritance"],
)
add_chunk(
    source_title="Access + Community Architecture · the gatekeeper-respect protocol",
    source_file="network__access_and_community_architecture.md",
    domain="commercial-architecture",
    concept="Gatekeeper protocol · how to enter a cluster without breaking its trust spine",
    summary=(
        "Gatekeeper protocol: identify the cluster's named gatekeeper(s), enter through a warm "
        "introduction (Pearl-network or documented relationship), demonstrate value before asking "
        "for access (Strategic Free Community shoot for the institution), maintain a long-arc "
        "follow-up cadence (annual check-in minimum). NEVER cold-pitch a cluster gatekeeper. NEVER "
        "use a gatekeeper introduction transactionally."
    ),
    usable_principle=(
        "Warm intro only. Demonstrate value first. Annual cadence. Never cold-pitch a gatekeeper. "
        "Never use introduction transactionally."
    ),
    sniped_relevance=(
        "Pairs with Lineage Doctrine 5 lineages + partnership_protocol + scene-density thinking."
    ),
    direct_quotes=[],
    tags=["access-community-architecture", "gatekeeper-protocol", "commercial-architecture", "warm-intro-only"],
)


# ===========================================================================
# Write JSONL + em-dash sweep
# ===========================================================================

def main():
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")

    print(f"Wrote {len(chunks)} chunks to {OUT_JSONL}")

    # Em-dash sweep on output (Unicode U+2014, replaced with middle dot)
    em_char = chr(0x2014)
    text = OUT_JSONL.read_text(encoding="utf-8")
    em_count = text.count(em_char)
    if em_count:
        print(f"WARNING: {em_count} em-dashes in output. Sweeping.")
        text = text.replace(em_char, " · ")
        OUT_JSONL.write_text(text, encoding="utf-8")
    else:
        print("No em-dashes in output.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
