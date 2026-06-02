#!/usr/bin/env python3
"""
Write BATCH_009_EXPANSION_CHUNKS.jsonl · 22 chunks (20 source + 2 synthesis) across 5 books.
12-field canonical schema. NO new domain (11 approved existing domains only).
Identity-optionality guardrail: sniped_relevance frames everything as decision-support, never
as a finalized SNIPED / SNIPED Media / BASEPLATE direction. Em-dash sweep at the end.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_009_EXPANSION_CHUNKS.jsonl"

VOSS = ("Never Split the Difference", "never_split_the_difference_voss.txt", "Chris Voss & Tahl Raz")
MORGAN = ("Eating the Big Fish", "eating_the_big_fish_morgan.txt", "Adam Morgan")
PB = ("Play Bigger", "play_bigger_ramadan_lochhead.txt", "Al Ramadan, Dave Peterson, Christopher Lochhead & Kevin Maney")
TRIBES = ("Tribes: We Need You to Lead Us", "tribes_godin.txt", "Seth Godin")
CAL = ("Competing Against Luck", "competing_against_luck_christensen.txt", "Clayton M. Christensen, Karen Dillon, Taddy Hall & David S. Duncan")

DG = "Decision-support lens only. This does NOT finalize SNIPED, SNIPED Media, or BASEPLATE direction; direction stays undecided and optionality is preserved."

C = []
def add(src, domain, concept, summary, principle, relevance, quotes, tags):
    n = len(C) + 1
    title, sfile, author = src
    C.append({
        "chunk_id": f"BATCH_009_EXPANSION_{n:03d}",
        "batch_id": "BATCH_009_EXPANSION",
        "source_title": title,
        "source_file": sfile,
        "author": author,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": principle,
        "sniped_relevance": relevance,
        "direct_quotes": quotes,
        "tags": tags,
    })

# ---------------- Never Split the Difference (Voss) · negotiation · 4 ----------------
add(VOSS, "sales-flow",
    "Tactical empathy: name and understand the other side's emotions",
    "Voss reframes negotiation as emotional intelligence, not haggling. Tactical empathy means deliberately recognising the counterpart's perspective and feelings and voicing that understanding, which lowers their defensiveness and surfaces what they actually need. A calm, downward-inflected voice (the late-night FM DJ voice) signals safety and control.",
    "Lead with understanding before influence: demonstrate you grasp the other side's situation and emotions before you make any ask.",
    "A lens for client/Reset conversations: understand the prospect's real situation before pitching. Used as decision-support for how the operator could run discovery conversations. " + DG,
    ["The opposite of that is tactical empathy."],
    ["negotiation", "empathy", "discovery", "sales-flow", "voss"])

add(VOSS, "sales-flow",
    "Mirroring, labeling, and the accusation audit",
    "Three listening tools: mirroring (repeat the last few words to keep them talking), labeling (verbalise their emotion, 'It seems like...'), and the accusation audit (pre-empt every negative they might think before they raise it). Together they defuse hostility and extract information cheaply.",
    "Disarm objections by naming them first and reflecting the counterpart's words back, so they feel heard and reveal more.",
    "A reusable toolkit for objection handling and rapport in any future offer conversation, independent of what the offer ends up being. " + DG,
    [],
    ["mirroring", "labeling", "accusation-audit", "objections", "sales-flow"])

add(VOSS, "brand-psychology",
    "'No' is protection; 'That's right' is the breakthrough",
    "Voss argues 'no' makes people feel safe and in control, so inviting it opens real dialogue, whereas chasing 'yes' creates pressure. The true turning point is 'that's right', when the counterpart confirms you have summarised their worldview correctly, signalling genuine agreement rather than the compliance of 'you're right'.",
    "Aim for 'that's right' (they feel understood), not 'yes' (compliance); let people say 'no' to give them safety.",
    "Informs how the operator might earn trust before any commitment, a psychology lens that applies whatever direction SNIPED takes. " + DG,
    [],
    ["no", "thats-right", "trust", "brand-psychology", "voss"])

add(VOSS, "sales-flow",
    "Calibrated questions, Ackerman bargaining, and Black Swans",
    "Calibrated 'how' and 'what' questions hand the counterpart the illusion of control while making them solve your problem ('How am I supposed to do that?'). The Ackerman system stages offers (65/85/95/100 percent with shrinking increments and a non-round final number). Black Swans are hidden pieces of information that, once uncovered, reshape the whole deal.",
    "Use open 'how/what' questions to shape outcomes without confrontation, anchor and concede systematically, and hunt for the unknown fact that changes everything.",
    "A negotiation-mechanics lens for pricing and scoping conversations; held as option-input, not a directive to set any particular price or offer. " + DG,
    ["No deal is better than a bad deal."],
    ["calibrated-questions", "ackerman", "black-swan", "pricing", "sales-flow"])

# ---------------- Eating the Big Fish (Morgan) · challenger positioning · 4 ----------------
add(MORGAN, "positioning",
    "The Challenger mindset: ideas-led, not budget-led",
    "Morgan defines a Challenger as a brand that is neither the market leader nor a niche player, and that grows by punching above its share of voice through ideas rather than spend. Challengers accept they cannot win on resources, so they must win on intelligent emotional and strategic difference.",
    "Compete on ideas and a sharp point of difference rather than on budget or breadth; behave bigger than your resources.",
    "A framework to evaluate a possible challenger play, presented as one option among several for the upcoming direction decision. " + DG,
    [],
    ["challenger", "positioning", "share-of-voice", "ideas-led", "morgan"])

add(MORGAN, "brand",
    "Lighthouse Identity: project who you are and draw people to you",
    "Strong challengers behave like a lighthouse: intensely self-referential about who they are and what they believe, broadcasting it with clarity and consistency so the right people navigate toward them. They lead with identity and conviction rather than chasing every consumer need.",
    "Build an unmistakable, self-assured identity and broadcast it consistently, so the right audience orients to you rather than you chasing them.",
    "A lens for how a clear identity could attract the right audience; the specific identity SNIPED would project is left undecided. " + DG,
    [],
    ["lighthouse-identity", "brand", "conviction", "identity", "morgan"])

add(MORGAN, "strategy",
    "Sacrifice and Overcommitment: concentrate force",
    "Because challengers lack resources, they must sacrifice (deliberately give up audiences, messages, and channels) to concentrate everything behind a few high-conviction moves, then overcommit to those moves so they land disproportionately. Doing fewer things harder beats doing many things thinly.",
    "Deliberately give up the secondary so you can overcommit to the few moves that matter; concentration creates impact under constraint.",
    "Directly relevant to a solo operator with limited hours: a lens on focusing scarce resources, applied without committing to any one focus yet. " + DG,
    [],
    ["sacrifice", "overcommitment", "focus", "constraint", "strategy"])

add(MORGAN, "brand-psychology",
    "Intelligent Naivety and Thought Leadership of the consumer",
    "Challengers cultivate intelligent naivety (questioning category conventions a veteran would never think to challenge) and practise thought leadership: actively shaping how consumers see the category rather than passively serving stated needs. They change the conversation instead of joining it.",
    "Question the category's unwritten rules and lead the customer's thinking, rather than competing on the incumbents' terms.",
    "A reframing lens for challenging assumptions about the operator's own category, useful precisely while the direction is still open. " + DG,
    [],
    ["intelligent-naivety", "thought-leadership", "reframing", "brand-psychology", "morgan"])

# ---------------- Play Bigger · category design · 5 ----------------
add(PB, "commercial-architecture",
    "Category design and the category king's economics",
    "Play Bigger argues that the biggest winners do not just build better products, they design and dominate a new market category. The category king captures the large majority of the category's economic value, so the strategic prize is creating the category, not winning inside an existing one.",
    "Design the category you can lead instead of competing in someone else's; category creation, not product superiority, is the durable advantage.",
    "A framework to evaluate whether a future direction could create its own category; offered as analysis, not a decision to pursue category creation now. " + DG,
    ["This book is about the strategy that builds category kings."],
    ["category-design", "category-king", "market-creation", "commercial-architecture", "play-bigger"])

add(PB, "positioning",
    "Point of View: frame a problem the world doesn't yet name",
    "A category-defining Point of View articulates a problem people feel but cannot yet name, then positions the new category as the answer. The POV educates the market into seeing the world the founder's way, which is the precondition for owning the resulting category.",
    "Lead with a POV that names a previously unnamed problem; define the question before you sell the answer.",
    "A lens for articulating a distinctive POV when the operator chooses a direction; the POV itself is intentionally left unwritten here. " + DG,
    [],
    ["point-of-view", "framing", "market-education", "positioning", "play-bigger"])

add(PB, "systems-thinking",
    "The Magic Triangle: co-design product, company, and category",
    "Category kings develop their product, their company, and their category in lockstep (the Magic Triangle). The category narrative, the company built to deliver it, and the product that proves it must evolve together; optimising one without the others fails.",
    "Treat product, company, and category as one interdependent system and advance them together, not sequentially.",
    "A systems lens reminding the operator that any future direction couples the offer, the entity, and the market story; held as analysis, not a build order. " + DG,
    [],
    ["magic-triangle", "systems-thinking", "alignment", "category", "play-bigger"])

add(PB, "content-strategy",
    "The Lightning Strike: a concentrated blitz that conditions the market",
    "Rather than steady drip marketing, category designers stage a Lightning Strike: a concentrated, high-energy burst of coordinated activity that forces the market to pay attention and frames the new category on the designer's terms.",
    "Concentrate launch energy into a single coordinated strike to set the category frame, instead of diffusing it across constant low-level output.",
    "A distribution lens for how a future launch could be concentrated rather than diffuse; not a commitment to any launch or timing. " + DG,
    [],
    ["lightning-strike", "launch", "distribution", "content-strategy", "play-bigger"])

add(PB, "strategy",
    "Conditioning the market and becoming the category king",
    "Sustained category leadership comes from continuously conditioning the market (analysts, press, customers, ecosystem) to accept your frame as the default, so that the category and your name become synonymous. The king defends the frame, not just the product.",
    "Win durably by conditioning the whole ecosystem to your frame so the category and your brand become inseparable.",
    "A lens on durable advantage through framing; supplied as decision-support while SNIPED's category remains undecided. " + DG,
    [],
    ["conditioning", "category-king", "ecosystem", "strategy", "play-bigger"])

# ---------------- Tribes (Godin) · tribe building / leadership · 3 ----------------
add(TRIBES, "brand-psychology",
    "A tribe needs a shared interest and a way to communicate",
    "Godin defines a tribe as a group connected to a leader and to one another around a shared idea, requiring only a common interest and a means of communication. People have always sought tribes; they want connection, growth, and something new to belong to.",
    "Give people something to belong to: a shared idea plus the means to connect with each other and a leader.",
    "A belonging lens for whatever audience the operator eventually serves; the specific tribe is left open by design. " + DG,
    ["For millions of years, human beings have been part of one tribe or another."],
    ["tribe", "belonging", "community", "brand-psychology", "godin"])

add(TRIBES, "operator-process",
    "Leadership is not management; heretics challenge the status quo",
    "Godin separates management (optimising the existing, herding people toward a known outcome) from leadership (creating change around a belief). Leaders are heretics who question the status quo and give people a new story; the safest path is often the most dangerous in a changing world.",
    "Lead change rather than manage the status quo; challenging the default is the leadership act, not a risk to be avoided.",
    "An operating-stance lens for an operator deciding how to lead a future effort; applied without fixing what that effort is. " + DG,
    [],
    ["leadership", "heretic", "status-quo", "operator-process", "godin"])

add(TRIBES, "content-strategy",
    "Lead the smallest viable tribe and give them tools to connect",
    "Movements start small: find the few who already care, give them a tighter way to connect and act, and let them pull others in. Tightening the bonds and lowering the barrier to participate matters more than chasing scale early.",
    "Start with the smallest committed group, strengthen their connection, and equip them to spread the idea, rather than chasing mass reach first.",
    "A growth lens favouring depth before breadth; consistent with the corpus's scene-density thinking and held as option-input, not a mandate. " + DG,
    [],
    ["movement", "smallest-viable-tribe", "depth", "content-strategy", "godin"])

# ---------------- Competing Against Luck (Christensen) · JTBD · 4 ----------------
add(CAL, "strategy",
    "Jobs to Be Done: customers hire products to make progress",
    "Christensen argues customers do not buy products, they 'hire' them to make progress in a particular circumstance. The Job to Be Done (not the customer's demographics or the product's attributes) is the right unit of analysis, and understanding it predicts what people will actually buy.",
    "Define what progress the customer is trying to make in their circumstance, then build to that job rather than to product features or demographics.",
    "The core demand-discovery lens for any future direction: find the real job before designing the offer; the job SNIPED would serve is left open. " + DG,
    ["hire a milk shake to resolve a job"],
    ["jobs-to-be-done", "progress", "demand", "strategy", "christensen"])

add(CAL, "brand-psychology",
    "Every job has functional, social, and emotional dimensions",
    "A Job to Be Done is never purely practical: it has functional, social, and emotional dimensions. Customers care how a choice makes them feel and how it makes them appear to others, so the social and emotional layers often decide the purchase as much as the functional one.",
    "Design for the emotional and social dimensions of the job, not only the functional task, because feelings and self-image often drive the choice.",
    "Links demand discovery to status and identity (the corpus's status/culture layer); a lens, not a verdict on what SNIPED's customers feel. " + DG,
    [],
    ["functional-social-emotional", "jtbd", "status", "brand-psychology", "christensen"])

add(CAL, "client-application",
    "Demand-side thinking: circumstance over customer attributes",
    "The milkshake study showed the same product was hired for completely different jobs depending on circumstance (a boring commute versus pleasing a child). Christensen warns against correlation-driven 'customer attribute' thinking; the circumstance, not the customer profile, defines the job.",
    "Investigate the circumstance in which a product gets hired, not the customer's profile; circumstance, not correlation, reveals the real job.",
    "A discovery lens for understanding why someone would hire the operator in a given moment; applied as analysis without fixing the service. " + DG,
    [],
    ["circumstance", "milkshake", "demand-side", "client-application", "christensen"])

add(CAL, "offer-design",
    "Integrate experiences and the organisation around the job",
    "Once the job is understood, winners design the whole set of experiences (purchase and use) around nailing it, and organise the company's processes around the job rather than around functions. The job becomes the organising principle for the offer and the operation.",
    "Architect the offer and the operating processes around the customer's job, so the entire experience is purpose-built to get it done.",
    "An offer-architecture lens for a future offer; supplied as decision-support, with no offer or offer ladder being finalized here. " + DG,
    [],
    ["experience-design", "integration", "offer-design", "jtbd", "christensen"])

# ---------------- Synthesis · 2 ----------------
add(CAL, "strategy",
    "SYNTHESIS: the commercial-strategy stack as a sequence of lenses",
    "Read together, the five books form a sequence: discover the real Job to Be Done (Christensen), frame a Point of View and design the category around it (Play Bigger), compete as an ideas-led Challenger with a lighthouse identity under deliberate sacrifice (Morgan), rally the smallest viable tribe and lead the change (Godin), and negotiate the deal with tactical empathy (Voss). Each is a reusable lens, not a prescription.",
    "Move from demand (the job) to frame (POV/category) to identity (challenger/lighthouse) to people (tribe) to the deal (negotiation); use the stack as a thinking sequence.",
    "A consolidated decision-support stack for the operator's upcoming direction work. It generates and evaluates options; it does NOT pick the direction. " + DG,
    [],
    ["synthesis", "commercial-strategy", "decision-support", "strategy", "expansion"])

add(PB, "systems-thinking",
    "SYNTHESIS: option-generators, not a mandate; preserve optionality",
    "Category design and challenger positioning are powerful but commitment-heavy: each, taken literally, pushes toward locking a single category, identity, or niche. Within the current identity-and-brand-optionality guardrails these are treated strictly as option-generators that widen and pressure-test the choice set, keeping decisions reversible until the operator writes the fresh current brief.",
    "Use commitment-heavy frameworks to expand and stress-test options, not to prematurely lock a category, niche, identity, or offer ladder.",
    "Explicitly preserves optionality: category design and challenger positioning are decision-support only. No final SNIPED, SNIPED Media, or BASEPLATE direction is set; photography remains one option among several. " + DG,
    [],
    ["optionality", "decision-support", "guardrail", "systems-thinking", "expansion"])

# ---------------- write + em-dash sweep ----------------
EM = chr(0x2014)
def sweep(o):
    if isinstance(o, str):
        return o.replace(EM, " · ")
    if isinstance(o, list):
        return [sweep(x) for x in o]
    if isinstance(o, dict):
        return {k: sweep(v) for k, v in o.items()}
    return o

C = [sweep(c) for c in C]
with OUT.open("w", encoding="utf-8") as f:
    for c in C:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

# domain tally
from collections import Counter
dist = Counter(c["domain"] for c in C)
print(f"wrote {len(C)} chunks to {OUT}")
print("domains:", dict(sorted(dist.items(), key=lambda x: -x[1])))
em_hits = sum(json.dumps(c, ensure_ascii=False).count(EM) for c in C)
print("em-dashes in output:", em_hits)
