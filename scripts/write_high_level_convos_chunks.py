#!/usr/bin/env python3
"""Author HIGH_LEVEL_CONVOS chunks (single source: high level convos.docx · curated transcripts).

12-field schema. batch_id HIGH_LEVEL_CONVOS. chunk_id HIGH_LEVEL_CONVOS_NNN.
Single source_file high_level_convos.txt; per-transcript/guest attribution carried in
source_title + author. Existing domains only (NO new domain · NO nightlife/transcript/
interview/conversation). Short illustrative quotes only. Em-dash swept to ' · '. Speaker
claims distinguished from reusable principles. Every chunk references CURRENT_OPERATOR_
REALITY_BRIEF; closing chunk makes the optionality guardrail explicit (decision-support
only, NOT a directive that BJ become a nightlife/hospitality/AI-influencer brand). The
Bible is NOT included; no faith/spiritual lane.
"""
import json
import os

REPO = os.path.expanduser("~/AI-Brain-Refinery")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/HIGH_LEVEL_CONVOS_CHUNKS.jsonl")
SF = "high_level_convos.txt"
BID = "HIGH_LEVEL_CONVOS"

# attribution shorthands (source_title, author)
PINKY = ("High Level Convos: Miss Pinky · investment basics", "Miss Pinky")
BARNES = ("High Level Convos: Earn Your Leisure · club owner (Dream/Park, DC nightlife)", "Mark Barnes (Earn Your Leisure)")
MALKA = ("High Level Convos: Earn Your Leisure · Malka/OWN creator-equity", "Jeff Fromer (Earn Your Leisure)")
MIS = ("High Level Convos: Earn Your Leisure · multiple income streams", "Rashad, Ian, Troy (Earn Your Leisure)")
AIFS = ("High Level Convos: Earn Your Leisure · AI Future Shock", "Earn Your Leisure")
SYN = ("High Level Convos: cross-conversation synthesis", "Earn Your Leisure (collected) / SNIPED synthesis")

GUARD = (
    " Held as decision-support / operator pattern material read against "
    "CURRENT_OPERATOR_REALITY_BRIEF: a speaker claim from a conversation distilled to a "
    "reusable principle, NOT canonical doctrine and NOT a directive that BJ become a "
    "nightlife, hospitality, or AI-influencer brand or copy any speaker. Does not finalize "
    "SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option among several."
)

# (src, domain, concept, summary, usable_principle, sniped_relevance, [quotes], [tags])
C = [
    (PINKY, "capital", "Equity is ownership; giving it away trades control for capital",
     "Miss Pinky's plain-register teaching: an investment is money given for equity, and equity means ownership; the more equity you give away, the less of your business you control.",
     "Equity is ownership traded for capital; every raise is a control-for-cash decision, so give away only what the capital is genuinely worth.",
     "The first lens on any future funding question: raising money means selling ownership and control, not free fuel.",
     ["\"equity means ownership\""], ["equity", "ownership", "dilution", "fundraising-basics", "capital"]),
    (PINKY, "commercial-architecture", "Valuation and the cap table",
     "Miss Pinky's basics: valuation is what the business is worth (a high valuation lets you give away less for the same money), and a cap table is the list of everyone who owns a piece of the company.",
     "Valuation sets the price of ownership and the cap table records who owns what; both govern how much you keep as you raise.",
     "Structural literacy for any venture: know your valuation logic and keep a clean cap table before taking outside money.",
     ["\"a cap table is a list\""], ["valuation", "cap-table", "ownership-structure", "fundraising-basics", "commercial-architecture"]),
    (MALKA, "capital", "Get cash upfront: a headline exit can net nothing",
     "Jeff Fromer's hard lesson from Malka: a deal that sounds like a $450M exit can leave the founder with almost nothing once the structure (debt, preferences, what was actually owned) is accounted for. They had been an LLC and did not understand equity.",
     "Judge a deal by what you actually keep after structure, not the headline number; understand equity, preferences, and terms before celebrating.",
     "A guardrail for any exit/deal BJ ever evaluates: model the net-to-you after structure, not the press-release figure.",
     ["\"get cash upfront\""], ["exit", "deal-structure", "equity", "net-proceeds", "capital"]),
    (MALKA, "operator-doctrine", "Find mentors who have already been through it",
     "Fromer's post-exit reflection: he wished he had had mentors and people who had gone through an exit to lean on, and advises stopping to find and simply ask the people who can answer the questions you cannot answer yourself.",
     "Proactively recruit mentors who have already done the specific thing you are attempting; most will help if you simply ask.",
     "A cheap, high-leverage move for a solo operator: seek out people who have already walked the path BJ is considering and ask directly.",
     ["\"I wish I had mentors\""], ["mentorship", "ask", "learning", "operator-doctrine", "humility"]),
    (MIS, "capital", "Layer income: business, then long-term investment, then speculative bets",
     "The EYL multiple-income-streams panel (Rashad/Ian/Troy): leverage your network and reinvest profits; build a business first, route a chunk into long-term investments for your future number, and only then take measured speculative bets (e.g., futures).",
     "Sequence income-building: an operating business funds long-term investing, which earns the right to small speculative bets; do not invert the order.",
     "A layering model for how BJ could structure income beyond a single service line, sequencing safety before speculation.",
     ["\"multiple income streams\""], ["income-streams", "reinvestment", "sequencing", "diversification", "capital"]),
    (MIS, "operator-doctrine", "Frugality and execution speed compound",
     "The panel's blunt operator notes: it 'costs a lot of money to be outside,' i.e. staying disciplined and indoors building beats lifestyle spend, and speed of execution plus smart early bets outpace waiting.",
     "Protect the runway with frugality and move fast on validated bets; lifestyle spend and hesitation are silent compounders against you.",
     "A discipline lens for a solo operator loading the backend: spend on building, not on appearing, and execute quickly once a bet is validated.",
     ["\"cost a lot of money to be outside\""], ["frugality", "execution-speed", "discipline", "runway", "operator-doctrine"]),
    (BARNES, "capital", "High-cost capital to seize an opportunity (with the risk named)",
     "Mark Barnes borrowed at 32% interest to renovate and launch the Dream nightclub when a prime location opened up. The speaker's claim is that seizing the location was worth it; the reusable principle is narrower and carries a caution.",
     "Expensive capital can be justified only when it buys a genuinely scarce, high-return asset and you have a clear path to service it; 32%-type debt is a last-resort, high-risk lever, not a default.",
     "A risk-weighted lens (not an endorsement): BJ should treat costly financing as a rare, opportunity-specific move with the downside fully priced, not a normal funding path.",
     ["\"borrow that money at 32%\""], ["financing", "high-cost-debt", "risk", "opportunity-cost", "capital"]),
    (BARNES, "operator-process", "Own the ancillary cash lines: parking and coat check",
     "Barnes details that parking and coat check were pure-cash, high-margin ancillary lines on top of the venue (e.g., party parking at a Gilbert Arenas event did $50,000), separate from the door and bar.",
     "Capture the high-margin ancillary revenue around your core offer; the add-on lines often carry better margins than the headline product.",
     "An operator lens for any offer BJ builds: design the profitable ancillary services around the core, not just the core itself.",
     ["\"parking did $50,000\""], ["ancillary-revenue", "margin", "cash-flow", "operations", "operator-process"]),
    (BARNES, "commercial-architecture", "Corporate events: the highest-margin, lowest-hassle segment",
     "Barnes contrasts segments: corporate events are 'the easiest thing in the world' (three to four hours, food and drink included, no damage, crazy margins above a spend threshold) versus thinner restaurant margins and rowdier public nights.",
     "Identify and prioritize the segment with the best margin-to-hassle ratio; not all revenue is equal, and the easiest dollars often hide in B2B/corporate channels.",
     "A segmentation lens: BJ should find the highest-margin, lowest-friction customer segment for any offer rather than chasing volume.",
     ["\"crazy margins\""], ["segmentation", "margin", "corporate-events", "b2b", "commercial-architecture"]),
    (BARNES, "commercial-architecture", "Shift toward membership and recurring revenue",
     "Barnes describes transitioning a venue (Park) toward a membership-only model, moving from one-off door revenue toward predictable recurring membership income.",
     "Convert one-off transactions into recurring membership/subscription revenue where you can; predictability and retained relationships beat episodic sales.",
     "A recurring-revenue lens: BJ should look for the membership/retainer version of any offer rather than only one-off projects.",
     ["\"membership-only model\""], ["recurring-revenue", "membership", "retention", "predictability", "commercial-architecture"]),
    (BARNES, "hospitality", "Unreasonable hospitality and ambiance as the product",
     "Barnes recommends Unreasonable Hospitality and stresses that ambiance and excellence in service are the real product in nightlife; people return for how the place makes them feel, not just the drinks.",
     "In experience businesses the felt experience (ambiance, service excellence, hospitality) is the product; invest in it as the core, not the garnish.",
     "A hospitality lens for any client-facing work BJ does: the experience around the deliverable drives loyalty as much as the deliverable itself.",
     ["\"excellence in service\""], ["hospitality", "service-excellence", "ambiance", "experience", "loyalty"]),
    (BARNES, "hospitality", "Know your crowd economics and segments",
     "Barnes speaks candidly about the venue's crowd economics, distinguishing nights, demographics, and spend patterns, and tuning the operation to who actually shows up and spends.",
     "Read the real economics of who your customers are and when they spend, and tune the offer to the segments that actually sustain it.",
     "A market-reading lens: BJ should design around the customers who genuinely value and fund the work, not an idealized average.",
     ["\"Friday night was my white night\""], ["customer-segments", "demand", "market-reading", "hospitality", "economics"]),
    (BARNES, "culture", "Build to pass on: succession and legacy",
     "Barnes discusses working with his son and passing on the business, framing the venue as a legacy and a vehicle to transfer to the next generation rather than only a personal income source.",
     "Build the operation as a transferable asset and legacy, not just a job for yourself; design for succession from the start.",
     "A legacy lens (held, not prescribed): BJ can weigh whether what he builds is a transferable asset, while keeping his direction open.",
     ["\"working with his son\""], ["succession", "legacy", "ownership", "family-business", "culture"]),
    (AIFS, "ai-tooling", "AI and the future of work and skills",
     "The EYL 'AI Future Shock' episode argues AI is reshaping which skills and jobs hold value, pushing people to move up the value chain toward judgment, taste, and orchestration rather than easily-automated tasks.",
     "Position your skills above what AI commoditizes: judgment, taste, relationships, and orchestration retain value as routine tasks get automated.",
     "Directly relevant to BJ's AI-operator profile: build on the judgment/taste/orchestration layer AI does not commoditize, as the brief's backend loads.",
     ["\"AI Future Shock\""], ["ai-future", "skills", "automation", "value-chain", "ai-tooling"]),
    (MALKA, "ai-tooling", "AI-era trust moats: pre-AI reputation compounds",
     "Fromer's thesis: as AI multiplies faces, clips, and virtual influencers (100x the content), trust earned over time becomes the scarce moat, and IP and reputation built in the pre-AI world rise sharply in value.",
     "In an AI-saturated feed, durable earned trust and a real track record become the differentiator; reputation built now compounds as synthetic content floods in.",
     "A lens for BJ's positioning: a genuine, attributable track record and earned trust are the moat AI cannot fake, worth building deliberately now.",
     ["\"trust is earned over time\""], ["trust", "ai-saturation", "reputation", "moat", "ai-tooling"]),
    (MALKA, "ethics", "Virtual-influencer ethics and the creator trust gap",
     "Fromer raises the ethics of virtual/AI influencers and a widening 'AI creator trust gap': audiences increasingly need to know whether a face is real, and synthetic personas raise disclosure and authenticity questions.",
     "Disclosure and authenticity are ethical obligations as synthetic personas spread; trust depends on audiences knowing what is real.",
     "An ethics lens for any AI-assisted content BJ might make: be transparent about what is synthetic; authenticity is both ethical and a trust asset.",
     ["\"virtual influencers\""], ["ethics", "authenticity", "disclosure", "ai-creators", "trust"]),
    (MALKA, "media-business", "The distribution flywheel",
     "Fromer describes Malka's growth through a distribution flywheel: produce content that builds audience, which attracts partners/brands, which funds more content, compounding reach over time.",
     "Build a flywheel where output grows audience, audience attracts resources, and resources fund more output; compounding distribution beats one-off hits.",
     "A media-engine lens: whatever BJ builds, design the self-reinforcing loop between output, audience, and resources rather than chasing single launches.",
     ["\"distribution flywheel\""], ["distribution", "flywheel", "audience", "compounding", "media-business"]),
    (MALKA, "commercial-architecture", "Share ownership: creator stock and option pools",
     "Fromer built shared ownership at Malka/OWN, including creator equity and a stock-option pool, aligning the people who create the value with the upside of the company.",
     "Align contributors with the upside through real ownership (equity, option pools); shared ownership turns talent into invested partners.",
     "An alignment lens: if BJ ever builds with collaborators, structuring real ownership/upside-sharing aligns incentives better than fees alone.",
     ["\"creator stock option pool\""], ["equity", "option-pool", "alignment", "ownership", "commercial-architecture"]),
    (MALKA, "ethics", "Due diligence: founders hide the truth",
     "Fromer warns that in deals 'founders hide the truth' and stresses real due diligence on exit terms and incentives; what is disclosed in a deal is not always the whole picture.",
     "Assume incomplete disclosure and do independent due diligence on any deal; verify terms and incentives rather than trusting the narrative.",
     "A due-diligence lens for any partnership/deal BJ enters: verify independently, because the counterparty's framing is not the full truth.",
     ["\"founders hide the truth\""], ["due-diligence", "disclosure", "deal-terms", "skepticism", "ethics"]),
    (MALKA, "content-strategy", "A small, trusting audience beats a big passive one",
     "Fromer notes creators with 50,000 to 100,000 engaged followers making two to three million a year by providing value, not selling ads; audience-offer fit and trust matter more than raw size.",
     "Monetize trust and value with an engaged niche audience; depth of relationship and offer-fit outperform raw follower count.",
     "A content lens for BJ: a small, genuinely-engaged audience served with real value can outperform chasing scale, fitting the lean-operator constraint.",
     ["\"provide value\""], ["audience", "niche", "trust", "monetization", "content-strategy"]),
    (MALKA, "media-business", "Creator marketplace, pricing, and audience fit",
     "Fromer describes building a creator marketplace and stresses pricing and audience fit: matching the right creator/offer to the right audience, not maximizing reach for its own sake.",
     "Match offer to audience and price to fit; a marketplace works when relevance and pricing are right, not when reach is maximized blindly.",
     "A matching lens: BJ should prioritize offer-to-audience fit and correct pricing over chasing the largest possible reach.",
     ["\"pricing and audience fit\""], ["marketplace", "pricing", "audience-fit", "relevance", "media-business"]),
    (MALKA, "strategy", "Negotiation and the ownership mindset through hardship",
     "Fromer covers negotiation tactics and a hardship/ownership mindset: treating setbacks as the cost of owning your outcome and negotiating from a clear sense of what you actually own and want.",
     "Negotiate from clarity about what you own and want, and treat hardship as the price of ownership rather than a reason to give it up.",
     "A posture lens: BJ should hold an ownership mindset through difficulty and negotiate from clear self-knowledge, not scarcity.",
     ["\"ownership mindset\""], ["negotiation", "ownership-mindset", "resilience", "strategy", "hardship"]),
    (BARNES, "culture", "Black entrepreneurship and building in your own scene",
     "Barnes recounts the challenges of getting into nightlife as a Black entrepreneur and building Dream within DC's culture, including financing barriers and reclaiming a neighborhood corridor.",
     "Building from inside your own cultural scene is both a barrier (access, financing) and an edge (authentic demand, community trust); know which you are leveraging.",
     "A cultural-context lens (attributed, not generalized): BJ's own community/scene context can be a source of authentic demand and trust, held as context not a directive.",
     ["\"as a Black entrepreneur\""], ["black-entrepreneurship", "scene", "community", "access", "culture"]),
    (SYN, "operator-doctrine", "Synthesis: the operator-conversation pattern",
     "Across these conversations a consistent operator pattern emerges: own real equity and understand deal structure (Fromer, Miss Pinky), control your high-margin and recurring cash lines (Barnes), build earned trust and a track record that compounds (Fromer), layer income from a stable base (the EYL panel), and recruit mentors who have done it. This is a closing synthesis chunk.",
     "The cross-conversation operator pattern: understand and own equity, control high-margin/recurring cash lines, compound earned trust, layer income from safety to speculation, and learn from people who have done it.",
     "An integrated decision-support pattern for how a real operator thinks, distilled from the conversations and read against BJ's current reality.",
     ["\"get cash upfront\""], ["synthesis", "operator-pattern", "ownership", "trust", "decision-support"]),
    (SYN, "operator-doctrine", "Synthesis: the optionality guardrail",
     "These transcripts are operator pattern material, not canonical doctrine and not a directive that BJ become a nightlife operator, a creator-equity founder, or an AI influencer. They sharpen how he evaluates options while identity and direction stay fully open. This is the closing optionality chunk.",
     "Absorb the conversations as a pattern library for operator judgment while keeping identity and direction open; speaker claims are inputs, not instructions.",
     "Operator conversations as portable judgment, not a new identity; explicitly preserves optionality and keeps photography one option among several.",
     ["\"high level convos\""], ["optionality", "decision-support", "guardrail", "operator-pattern", "doctrine"]),
]


def sweep(s):
    return s.replace(chr(0x2014), " · ").replace(chr(0x2013), "-")


def main():
    if os.path.exists(OUT):
        raise SystemExit(f"REFUSE: {OUT} exists")
    lines = []
    for i, (src, domain, concept, summary, principle, relevance, quotes, tags) in enumerate(C, start=1):
        title, author = src
        rec = {
            "chunk_id": f"{BID}_{i:03d}",
            "batch_id": BID,
            "source_title": title,
            "source_file": SF,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": relevance + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        for k, v in rec.items():
            if isinstance(v, str):
                rec[k] = sweep(v)
            elif isinstance(v, list):
                rec[k] = [sweep(x) if isinstance(x, str) else x for x in v]
        lines.append(json.dumps(rec, ensure_ascii=False))
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {len(lines)} chunks -> {OUT}")


if __name__ == "__main__":
    main()
