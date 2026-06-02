#!/usr/bin/env python3
"""
B2B_POSITIONING_CLAUDE_OPERATOR chunker · Claude for Small Business research (SNIPED OS)

Reads 01_KNOWLEDGE_BASE/batches/b2b_positioning_claude_operator_extracted/claude_for_small_business_organized.txt
and emits B2B_POSITIONING_CLAUDE_OPERATOR_CHUNKS.jsonl with the canonical 12-field schema.

Target: 8 chunks (range 6-9 per plan section 3 · target 7-8).
Domains per plan section 4 (all 5 pre-existing · no NEW domain):
  strategy (001, 002, 004, 007) · client-application (003) ·
  operator-process (005) · commercial-architecture (006, 008).
  ai-tooling appears as a secondary tag only.

Source rule per plan section 2: chunk the CANONICAL organized doc only.
The legacy was extracted for quote recovery, but the full organized extraction
proved to carry the cognitive-vs-responsiveness reply and the contractor
missed-call example in full (the planning-time truncation was a peek-windowing
artifact). So ALL chunks source to claude_for_small_business_organized.txt and
the legacy contributes 0 chunks and 0 unique quotes. See COMPLETE marker deviations.

EXCLUDED per operator brief: MJ interview fragment (Part 1), install/setup
walkthrough (Part 3), use-case how-to tutorials (Part 4), Higgsfield tutorial
(Part 5), Android/phone notes (Part 8), raw legacy transcript bulk, hype.

Em-dash sweep (Unicode U+2014) applied to output.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "B2B_POSITIONING_CLAUDE_OPERATOR_CHUNKS.jsonl"

BATCH_ID = "B2B_POSITIONING_CLAUDE_OPERATOR"
AUTHOR = "SNIPED Media (research compilation)"
SOURCE_TITLE = "Claude for Small Business · Sniped OS Research"
SOURCE_FILE = "claude_for_small_business_organized.txt"

BASE_TAGS = ["claude-for-small-business", "b2b-positioning", "2026-05-19", "ai-tooling-aging-risk"]

chunks = []


def add_chunk(num, domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags):
    chunks.append({
        "chunk_id": f"{BATCH_ID}_{num:03d}",
        "batch_id": BATCH_ID,
        "source_title": SOURCE_TITLE,
        "source_file": SOURCE_FILE,
        "author": AUTHOR,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": usable_principle,
        "sniped_relevance": sniped_relevance,
        "direct_quotes": direct_quotes,
        "tags": BASE_TAGS + tags,
    })


# ---------------------------------------------------------------------------
# Chunk 1 · Chatbot to operator (Parts 2 + 7) · strategy
# ---------------------------------------------------------------------------
add_chunk(
    num=1,
    domain="strategy",
    concept="Chatbot to operator · AI moves from a tool you visit to an operator inside the business stack",
    summary=(
        "The durable frame in the Claude for Small Business launch (May 13, 2025) is not the feature "
        "bundle, it is the category shift. Pre-launch, Claude was a chatbot: you went to it, asked it "
        "things, and copy-pasted answers back into your real tools. Post-launch, Claude sits inside the "
        "stack (QuickBooks, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365) and acts directly. "
        "The product specifics (the Cowork desktop bundle, the connector list, the 10-city tour) age fast; "
        "the chatbot-to-operator shift does not. It is the same move that cloud made (from a server you "
        "visit to a platform you operate inside) but compressed."
    ),
    usable_principle=(
        "Position AI as operator infrastructure, not as a chat tool. The defensible value is being "
        "inside the stack and acting on it, not answering questions beside it. When evaluating any AI "
        "surface, ask whether it visits the work or operates the work · the second is where the moat is."
    ),
    sniped_relevance=(
        "Direct market validation of the SNIPED hybrid-operator stance (intel_ai_sentiment · AI for "
        "world-construction and stack-operation, not identity). Pairs with the BATCH_006 automation "
        "blueprints (AI Content Strategy Generator, ElevenLabs voice agent): B6 shows the operator "
        "BUILDING agentic workflows; this chunk frames WHY the market is moving there. The operator-coded "
        "identity (B7) is the human layer that stays un-delegate-able while the stack-operation layer "
        "gets handed to AI."
    ),
    direct_quotes=[
        "The important part is not that Claude got another feature. The important part is that Claude is moving directly into the tools that businesses already run on. This is the shift from chatbot to operator.",
        "AI is going from 'tool you visit' to 'operator inside your business.'",
    ],
    tags=[
        "chatbot-to-operator", "ai-inside-the-stack", "operator-infrastructure",
        "category-shift", "ai-tooling", "claude-cowork",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 2 · Owner-as-integration-layer (Part 7) · strategy
# ---------------------------------------------------------------------------
add_chunk(
    num=2,
    domain="strategy",
    concept="Owner-as-integration-layer · the drowning-in-software problem and the owner-becomes-architect promise",
    summary=(
        "The B2B positioning argument underneath the launch: small businesses are not short on software, "
        "they are drowning in it. The owner becomes the integration layer between QuickBooks, PayPal, "
        "HubSpot, Canva, DocuSign and the rest, stitching them together by hand. Large companies have "
        "always used software to build their own software (internal tools, custom workflows), so their "
        "owners became architects; small businesses never had that luxury. The strategic claim is that "
        "AI-inside-the-stack is the first attempt to give SMB owners the build-your-own-operations "
        "leverage at scale, so the owner stops being the glue."
    ),
    usable_principle=(
        "The sharpest B2B pain to sell against is not 'you need more software,' it is 'you are the glue "
        "holding your software together.' Frame the offer as removing the owner from the integration "
        "layer so they can return to architect-level work. Drowning-in-software, not lack-of-software, "
        "is the buyer's real condition."
    ),
    sniped_relevance=(
        "The inverse of the B7 operator-coded definition + un-delegate-ables ledger: keep the "
        "un-delegate-ables (methodology, final review, pricing, named-subject relationships) and delegate "
        "the glue work to the stack. This is the commercial-architecture frame for any SNIPED productized "
        "offer aimed at busy operators · the value is freeing the architect from manual integration, "
        "which maps to the leverage logic (intel_leverage_logic · code+media leverage over labor)."
    ),
    direct_quotes=[
        "Small businesses aren't short on software, they're drowning in it.",
        "Owner becomes the integration layer between all of these by hand.",
        "Large companies have always used software to create their software ... The owner becomes the architect. Small businesses never had that luxury.",
    ],
    tags=[
        "owner-as-integration-layer", "drowning-in-software", "owner-becomes-architect",
        "commercial-architecture", "smb-leverage", "stop-being-the-glue",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 3 · AI amplifies the system you already have (Part 10 · PhilosopherHot6767) · client-application
# ---------------------------------------------------------------------------
add_chunk(
    num=3,
    domain="client-application",
    concept="AI amplifies the system you already have · amplifier not fixer · fix the basics before layering AI on chaos",
    summary=(
        "The cleanest principle to come out of the launch discourse: AI tools are strongest when the "
        "business already has structure, and they amplify whatever system is already running. If the real "
        "problem is missed calls, no follow-up process, weak local visibility, bad website conversion or "
        "no CRM discipline, AI will not magically fix that · it just adds another shiny layer on top of "
        "chaos. For service businesses especially, the sequence is fix the basics first (answer leads "
        "fast, track every inquiry, follow up consistently, collect reviews, keep data clean), THEN AI "
        "becomes useful. AI is an amplifier, not a fixer."
    ),
    usable_principle=(
        "Diagnose the underlying system before recommending AI. If the operating system is broken, AI "
        "amplifies the brokenness. Sell and deploy AI only on top of a working basics layer · answer "
        "fast, track inquiries, follow up, collect reviews, keep data clean. Amplifier, never fixer."
    ),
    sniped_relevance=(
        "The deepest bridge to the operator-doctrine cluster. 'AI amplifies the system you already have' "
        "is PERSONAL_OPERATING_CODE chunk 009 (mindset-as-software) stated in market language · the "
        "AI-Brain-Refinery corpus IS the system being amplified. It also validates the SNIPED build-order "
        "discipline: the locked architecture (CANONICAL_TRUTHS, SOPs, the spine) is the system; AI is the "
        "amplifier on top, never the substitute for it. Pairs with POC chunk 001 (ownership) and chunk "
        "006 (compound-arc)."
    ),
    direct_quotes=[
        "It amplifies the system you already have.",
        "if the real problem is missed calls, no follow-up process, weak local visibility, bad website conversion or no CRM discipline, AI won't magically fix that.",
        "Otherwise it just adds another shiny layer on top of chaos.",
    ],
    tags=[
        "amplifier-not-fixer", "amplifies-the-system-you-already-have", "fix-the-basics-first",
        "strategy", "service-business-fit", "system-before-ai",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 4 · Cognitive AI vs responsiveness AI (Part 10 · Virtual_Silver5941) · strategy
# ---------------------------------------------------------------------------
add_chunk(
    num=4,
    domain="strategy",
    concept="Cognitive AI vs responsiveness AI · the wrong-amplifier trap · not all AI amplifies the same bottleneck",
    summary=(
        "The most strategically dense distinction in the source: not all AI is the same amplifier. "
        "Claude, ChatGPT and Gemini amplify COGNITIVE work · drafting, summarizing, analyzing, routing. "
        "They make the desk faster, and that is what the Anthropic announcement is about. A different "
        "category · missed-call text-back, AI voice receptionists, schema-tuned web presence that gets a "
        "business cited in AI search · amplifies RESPONSIVENESS and DISCOVERABILITY. Same principle "
        "(amplifier not fixer), totally different tool category. The trap is that the bottleneck in most "
        "service businesses is responsiveness and discoverability, not cognition, so reaching for desk AI "
        "amplifies the wrong 10 percent of the leak."
    ),
    usable_principle=(
        "Before deploying AI, identify which bottleneck the business actually has · cognition, "
        "responsiveness, or discoverability · and match the AI category to it. Desk AI (Claude/GPT) "
        "amplifies cognition; missed-call text-back, AI receptionists and schema work amplify "
        "responsiveness and discoverability. Reaching for the wrong amplifier wastes the spend on a "
        "non-bottleneck."
    ),
    sniped_relevance=(
        "Sharpens the SNIPED hybrid-operator stance (intel_ai_sentiment) into a buyer-side diagnostic: "
        "the same 'use the right AI for the right job' discipline that keeps identity-AI off client "
        "deliverables, applied to where a B2B buyer should spend. This is the conceptual backbone for the "
        "future N8N_AUTOMATION_SYSTEMS mini-batch · the responsiveness-AI category named here (voice "
        "receptionist, missed-call text-back) is exactly what the staged AI Phone Call Assistant and "
        "n8n+RetellAI workflows implement. Demand-side framing for a supply-side mini-batch."
    ),
    direct_quotes=[
        "Claude / ChatGPT / Gemini amplify cognitive work, drafting, summarizing, analyzing, routing. They make the desk faster.",
        "Missed-call text-back, AI voice receptionists, schema-tuned web presence that gets you cited in AI search, those amplify responsiveness and discoverability. Same principle (amplifier not fixer), totally different tool category.",
        "Bottleneck in most service businesses: responsiveness + discoverability, not cognition.",
    ],
    tags=[
        "cognitive-vs-responsiveness-ai", "responsiveness-discoverability", "wrong-amplifier-trap",
        "client-application", "ai-category-matching", "service-business-bottleneck",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 5 · The missed-call gap (Part 10 · contractor example) · operator-process
# ---------------------------------------------------------------------------
add_chunk(
    num=5,
    domain="operator-process",
    concept="The missed-call gap · responsiveness is the real revenue leak · some AI IS the basics now, not Phase 2",
    summary=(
        "The concrete worked example that makes the responsiveness frame operational: a contractor was "
        "excited to use Claude for their business, but when the actual revenue leak was traced it was a "
        "30 percent-plus missed-call rate during job hours. Desk AI would have amplified roughly 10 "
        "percent of the real leak; they needed something answering the phone first. The sequencing "
        "correction matters: 'fix the basics first, then add AI' can mislead operators into treating AI "
        "as a Phase 2 luxury. Some AI IS the basics now · the missed-call autoresponder, the AI "
        "receptionist, the schema work for AI-search citation are the modern form of 'answer leads fast' "
        "and 'be visible.' Desk AI for admin is the part that comes after."
    ),
    usable_principle=(
        "Trace where revenue actually leaks before prescribing a tool. For service businesses the leak is "
        "usually missed calls and weak follow-up, not slow drafting. Treat responsiveness AI (missed-call "
        "text-back, AI receptionist, schema for AI search) as a basics-layer workflow to deploy first, "
        "not a Phase 2 add-on, and reserve desk AI for the admin layer that follows."
    ),
    sniped_relevance=(
        "Operator-process backing for the SNIPED responsiveness discipline (B7 SOP_capture_to_delivery "
        "5-day SLA + SLA-risk notification): responsiveness as a deliverable is already doctrine, and "
        "this gives it B2B market validation. It is also the demand statement for the future "
        "N8N_AUTOMATION_SYSTEMS mini-batch · the missed-call autoresponder and AI receptionist are the "
        "exact workflows in the staged AI Phone Call Assistant and n8n+RetellAI JSON. Cross-reference at "
        "that mini-batch's consolidation."
    ),
    direct_quotes=[
        "A contractor was excited to 'use Claude for their business.' When we walked through where revenue was actually leaking, it was a 30%+ missed-call rate during job hours. Claude on the desk wouldn't have moved the needle, they needed something answering the phone first. Desk AI would have been amplifying ~10% of the actual leak.",
        "Some AI IS the basics now, the missed-call autoresponder, the AI receptionist, the schema work for AI search citation.",
    ],
    tags=[
        "missed-call-gap", "responsiveness-workflow", "ai-receptionist",
        "client-application", "revenue-leak-diagnosis", "n8n-demand-signal", "baseplate-positioning",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 6 · Lukewarm launch reception + pricing-tier gap + objections (Part 9 + Part 11) · commercial-architecture
# ---------------------------------------------------------------------------
add_chunk(
    num=6,
    domain="commercial-architecture",
    concept="Lukewarm launch reception · the missing small-team tier and the real buyer objections",
    summary=(
        "The r/ClaudeAI read of the launch was lukewarm to skeptical · the consensus was that this was a "
        "marketing push, not a new product. What it was: a Cowork plugin with about 15 pre-made skills "
        "(invoice chasing, prospect outreach, campaign planning) plus integrations. What it was not: a "
        "new pricing tier. The biggest complaint by a wide margin was the continued lack of a Team plan "
        "for fewer than 5 users, a structural gap for anything branded 'small business.' Other recurring "
        "objections: caution about letting AI near finances given thin vendor support, and the risk of "
        "becoming dangerously dependent on a single LLM. A related signal · the ClaudeBusiness GitHub "
        "repo distilling 35-plus founder stories · was dismissed because the stories were likely "
        "AI-fabricated, a caution about trusting AI-generated authority."
    ),
    usable_principle=(
        "Read the gap in a competitor's launch as a positioning opening. The unserved 2-to-4-person team "
        "segment, the finance-trust objection, and single-vendor-dependency fear are all live buyer "
        "concerns to address head-on. Treat AI-fabricated 'authority' content as a credibility liability, "
        "not an asset · cite real sources or do not claim them."
    ),
    sniped_relevance=(
        "Commercial-architecture intelligence: the missing small-team tier is a pricing/packaging gap "
        "SNIPED can position against (intel_pricing_logic + intel_new_luxury). The single-LLM-dependency "
        "and finance-trust objections are the trust-mechanics counterweight (intel_trust_mechanics · "
        "self-orientation as divisor). The AI-fabricated-founder-stories skepticism reinforces the SNIPED "
        "anti-faceless-AI position and the carousel-attribution discipline · authority must be real and "
        "sourced, never synthesized."
    ),
    direct_quotes=[
        "The overwhelming consensus is that this is a marketing push, not a new product ... What it isn't: a new pricing tier. The biggest complaint by a long shot is the continued lack of a Team plan for fewer than 5 users, which feels like a huge miss for a 'small business' launch.",
        "It's now easy to become dangerously dependent on one LLM, or LLMs in general.",
        "No, because they are stories made by Claude!",
    ],
    tags=[
        "launch-reception", "pricing-tier-gap", "no-team-plan", "buyer-objections",
        "strategy", "single-llm-dependency", "ai-fabricated-authority", "anti-faceless-ai",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 7 · The small-business implementation gap (Part 9 · More_Ferret5914 + Parzival_3110) · strategy
# ---------------------------------------------------------------------------
add_chunk(
    num=7,
    domain="strategy",
    concept="The small-business implementation gap · category name vs integration coverage · the messy middle",
    summary=(
        "A field-ops critique cuts the launch hype: the category name 'Small Business' sounds broader "
        "than the actual integration coverage. Many SMBs do not operate around documents and meetings · "
        "they operate around scheduling, field ops, POS systems, inventory, storefronts, customer "
        "pipelines and vertical SaaS. Once the core operational tool is not connected, the AI becomes "
        "'assistant beside the business' rather than 'agent inside the business,' which is why glue layers "
        "(MCP, Zapier, custom connectors) keep emerging · no vendor can build native integrations for the "
        "whole SaaS universe fast enough. The browser-agent counter-take names where the value actually "
        "lands: the messy middle of logged-in web apps, half-finished forms, modals, exports and approval "
        "flows · not full autopilot, but a scoped browser session with readable page state, action logs, "
        "and hard pauses before send/pay/save."
    ),
    usable_principle=(
        "Judge any 'inside the business' AI claim by whether it connects the core operational tool, not "
        "the generic document/meeting layer. Where native integrations do not exist, the durable value is "
        "in the messy middle · scoped browser sessions and glue layers with action logs and human "
        "approval gates before irreversible actions. Sell agent-inside-the-business, not assistant-beside-it."
    ),
    sniped_relevance=(
        "Refines the chatbot-to-operator frame (chunk 001) with its hard limit: operator-grade value "
        "requires connecting the core operational tool, otherwise it is still an assistant beside the "
        "work. The hard-pause-before-send/pay/save pattern maps to the SNIPED final-review un-delegate-able "
        "(B7) and to the executing-with-care discipline · automate the glue, gate the irreversible. "
        "Useful framing for any SNIPED systems-as-leverage offer that promises 'inside the business' depth."
    ),
    direct_quotes=[
        "The category name 'Small Business' sounds broader than the actual integration coverage.",
        "Once your core operational tool isn't connected, the AI becomes more 'assistant beside the business' than 'agent inside the business.'",
        "The messy middle is logged-in web apps, half-finished forms, modals, exports, approval flows. The useful layer isn't full autopilot, it's a real browser session with scoped tabs, readable page state, action logs, and hard pauses before send/pay/save.",
    ],
    tags=[
        "small-business-implementation-gap", "category-vs-coverage", "messy-middle",
        "client-application", "glue-layers", "agent-inside-vs-assistant-beside", "human-approval-gate",
    ],
)

# ---------------------------------------------------------------------------
# Chunk 8 · Skill-as-moat productization (Part 6 · Ryan Dozer) · commercial-architecture
# ---------------------------------------------------------------------------
add_chunk(
    num=8,
    domain="commercial-architecture",
    concept="Skill-as-moat productization · the skill is the moat AND the production tool · the Ryan Dozer Skill Stack model",
    summary=(
        "A business-model signal worth keeping from the launch material: Ryan Dozer packaged Claude Code "
        "skills into a $99 product (the Claude Code Skill Stack). A skill here is a portable markdown file "
        "(CLAUDE.md-style) holding the operating logic for a task · branding, tone, workflow, references · "
        "that drops into any Claude setup and works in ChatGPT, Grok or Gemini too. The build sequence: "
        "build a personal skill (a Web Designer skill loaded with his own branding), feed it to Claude "
        "Code along with the product, let it vibecode the landing page in 15-20 minutes (social proof, "
        "FAQs, payment integration), wire a Stripe link, and distribute from owned channels (floating "
        "popup, blog CTAs, email) rather than any Claude-native library. The pattern compounds because "
        "the skill is both the moat AND the production tool, and discovery now comes from Google search "
        "AND LLM-based discovery (the new SEO frontier)."
    ),
    usable_principle=(
        "Productize the operating logic itself: build a portable skill that encodes your method, use that "
        "skill to manufacture the product surface (page, assets), wire payments, and distribute through "
        "owned channels rather than a platform's marketplace. The skill is simultaneously the defensible "
        "asset and the production tool. Optimize for LLM-based discovery alongside search."
    ),
    sniped_relevance=(
        "Direct structural mirror of the AI-Brain-Refinery skill layer itself · the .claude/skills/ files "
        "(source-inventory, staging-plan, batch-extraction, etc.) ARE skills-as-operating-logic, and the "
        "corpus is the moat. Validates the BATCH_006 prompt-engineering packs as productizable IP and the "
        "owned-channel distribution discipline (intel_leverage_logic · code+media leverage; "
        "intel_hit_mechanics · distribution). Commercial-architecture template for any future SNIPED "
        "skill/method product · build the skill, let it build the surface, sell from owned ground."
    ),
    direct_quotes=[
        "build a personal skill → use that skill to build the product page → wire payments → distribute via owned channels. The skill is the moat AND the production tool.",
        "Gaining significant traffic across Google search AND LLM-based discovery (this is the new SEO frontier).",
        "Portable: take the .md file, upload to ChatGPT / Grok / Gemini / whatever, same skill works there too.",
    ],
    tags=[
        "skill-as-moat", "productization-model", "owned-channel-distribution",
        "llm-discovery-seo", "ai-tooling", "ryan-dozer-skill-stack", "skill-as-production-tool",
    ],
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
