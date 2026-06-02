#!/usr/bin/env python3
"""
BATCH_009 chunk writer · advertising / copywriting / persuasion / positioning canon (CORE 18 books).
Schema: chunk_id, batch_id, source_title, source_file, author, domain, concept, summary,
        usable_principle, sniped_relevance, direct_quotes, tags. ID pattern BATCH_009_NNN.
Domains reused (all pre-existing · operator-approved · NO new domain): copywriting, meta-advertising,
positioning, brand-psychology, sales-flow, offer-design, content-strategy, brand, commercial-architecture,
strategy, client-application, aesthetics, operator-process. Copyright-safe SHORT quotes only. Em-dash swept.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_009_CHUNKS.jsonl"

C = []


def add(src, title, author, domain, concept, summary, usable, relevance, quotes, tags):
    C.append({"source_title": title, "source_file": src, "author": author, "domain": domain,
              "concept": concept, "summary": summary, "usable_principle": usable,
              "sniped_relevance": relevance, "direct_quotes": quotes, "tags": tags})


# ===================== Scientific Advertising · Hopkins (4) =====================
S = "scientific_advertising_hopkins.txt"; T = "Scientific Advertising (1923)"; A = "Claude C. Hopkins"
add(S, T, A, "copywriting", "Advertising is salesmanship in print",
    "Hopkins' founding axiom: an ad is a salesperson, judged only by the sales it produces, not by applause or aesthetics. Every element exists to sell, and the whole discipline follows from treating the page as a salesman.",
    "Judge every piece of copy by whether it would work as a one-to-one sales pitch; if it would not sell in person, it will not sell on the page.",
    "The bedrock standard for SNIPED's commercial copy: the line earns its place by selling, not by sounding clever.",
    "Advertising is salesmanship.",
    ["salesmanship-in-print", "direct-response", "first-principles", "copywriting"])
add(S, T, A, "strategy", "Test everything; let results, not opinions, decide",
    "Hopkins pioneered measurable advertising: coupons, keyed responses, and split tests so that copy decisions rest on data, not taste. Almost any question can be answered cheaply by a test rather than an argument.",
    "Resolve copy and offer debates with a cheap test, not an opinion; instrument every campaign so results can teach you.",
    "Grounds SNIPED's data-over-hype posture in the original direct-response discipline; mirrors the test-and-measure habit from the AI canon.",
    "Almost any question can be answered, cheaply, quickly and finally, by a test campaign.",
    ["testing", "measurement", "data-driven", "strategy"])
add(S, T, A, "copywriting", "Be specific; concrete claims beat generalities",
    "Hopkins showed that exact figures and concrete claims outpull vague superlatives: 'used by millions' loses to a precise, verifiable number. Specificity reads as truth; generality reads as bluster.",
    "Replace every generality in copy with a concrete, specific, verifiable fact; precise claims are believed, vague ones are discounted.",
    "A direct rule for SNIPED case-study and offer copy: specifics (exact results, named outcomes) outperform adjectives.",
    "Platitudes and generalities roll off the human understanding like water from a duck.",
    ["specificity", "concreteness", "believability", "copywriting"])
add(S, T, A, "meta-advertising", "Give a reason why, and offer service not flattery",
    "Hopkins' copy always supplied a 'reason why' the claim was true and framed the ad as a service to the reader rather than self-praise. The reader cares about their own benefit, never the advertiser's pride.",
    "Lead with the reader's benefit and always justify the claim; write to serve the reader's self-interest, not to boast.",
    "Shapes SNIPED's reader-first, low-self-orientation voice: the copy serves the prospect, which is itself a trust signal.",
    "",
    ["reason-why", "reader-benefit", "service", "meta-advertising"])

# ===================== Cashvertising · Whitman (4) =====================
S = "cashvertising_whitman.txt"; T = "Cashvertising (2009)"; A = "Drew Eric Whitman"
add(S, T, A, "brand-psychology", "The Life-Force 8: the biological desires ads tap",
    "Whitman names eight hardwired human desires (survival, enjoyment, freedom from fear, comfort, superiority, etc.) that drive the strongest response. Selling against a Life-Force 8 desire beats selling a learned want.",
    "Anchor an offer to one of the eight biological desires rather than a surface feature; primal wants convert harder than acquired ones.",
    "Gives SNIPED a desire-level targeting lens for offer and hook design beyond surface benefits.",
    "",
    ["life-force-8", "primal-desire", "consumer-psychology", "brand-psychology"])
add(S, T, A, "copywriting", "Ad-agency psychology techniques are learnable levers",
    "Whitman catalogs concrete psychological techniques (the fear-then-relief, the bandwagon, the means-end chain) as repeatable copy levers rather than innate talent. The craft is a toolkit, not a gift.",
    "Treat persuasion techniques as a checklist of levers to deliberately apply, not as inspiration to wait for.",
    "Supports SNIPED's skill-stack view: persuasion is a trainable toolkit the operator applies on demand.",
    "",
    ["techniques", "levers", "applied-psychology", "copywriting"])
add(S, T, A, "brand-psychology", "People buy on emotion and justify with logic",
    "Whitman stresses the order of operations: the emotional desire drives the decision, and reasons are recruited afterward to justify it. Copy must light the emotion first, then arm the buyer with logic.",
    "Open on the emotional payoff, then supply the rational justification the buyer needs to defend the purchase.",
    "Sequences SNIPED's offer copy: lead emotional (the transformation), close rational (the proof and terms).",
    "",
    ["emotion-first", "post-rationalization", "decision-order", "brand-psychology"])
add(S, T, A, "copywriting", "The headline does most of the work",
    "Whitman echoes the direct-response law that the headline carries the majority of an ad's impact, because most readers decide whether to continue from it alone. A weak headline wastes the entire piece.",
    "Spend disproportionate effort on the headline / hook; if it fails, nothing downstream gets read.",
    "Reinforces SNIPED's hook-first discipline across IG, LinkedIn, and ad creative.",
    "",
    ["headline", "hook", "attention", "copywriting"])

# ===================== Hey, Whipple, Squeeze This · Sullivan (4) =====================
S = "hey_whipple_squeeze_this_sullivan.txt"; T = "Hey, Whipple, Squeeze This (2008)"; A = "Luke Sullivan"
add(S, T, A, "copywriting", "Sell the idea, not the words",
    "Sullivan's central craft lesson: great advertising is built on a single strong idea, and the words and visuals are downstream of it. Polishing language cannot rescue a weak concept.",
    "Find the one idea first; do not write copy until the concept is strong enough to carry the whole piece.",
    "Disciplines SNIPED's content production: lock the idea before the caption, not the reverse.",
    "",
    ["the-idea", "concept-first", "craft", "copywriting"])
add(S, T, A, "aesthetics", "Simplicity and restraint cut through",
    "Sullivan champions reduction: the strongest ads say one thing with ruthless economy, because clutter buries the message. The discipline is removing everything that is not the idea.",
    "Cut a piece down to the single message and remove everything else; restraint reads as confidence.",
    "Directly echoes SNIPED's quiet-luxury / restraint visual direction at the copy level.",
    "",
    ["simplicity", "restraint", "reduction", "aesthetics"])
add(S, T, A, "meta-advertising", "Write to one person, in their language",
    "Sullivan insists good copy speaks to a single reader in plain, human language rather than to a demographic in corporate-speak. The ad should feel like one person talking to another.",
    "Write every piece to one specific person in the language they actually use, never to a faceless audience.",
    "Shapes SNIPED's DM and caption voice: human, singular, plain, never corporate.",
    "",
    ["one-reader", "voice", "plain-language", "meta-advertising"])
add(S, T, A, "copywriting", "Make the product the hero of an interesting story",
    "Sullivan's craft frame: the most memorable ads dramatize the product inside a story or tension rather than listing features. Interest, not information, is what gets remembered.",
    "Dramatize the product inside a tension or story rather than reciting features; interest is the carrier of the message.",
    "Backs SNIPED's narrative-led content (the lineage doc, the chapter cards) over feature-listing.",
    "",
    ["story", "drama", "memorability", "copywriting"])

# ===================== Breakthrough Advertising · Schwartz (4) =====================
S = "breakthrough_advertising_schwartz.txt"; T = "Breakthrough Advertising (1966)"; A = "Eugene M. Schwartz"
add(S, T, A, "meta-advertising", "Channel existing mass desire; you cannot create it",
    "Schwartz's foundational law: copy cannot create desire, only channel the mass desire already present in the market onto a product. The advertiser's job is direction, not generation.",
    "Identify the desire the market already has and channel it onto the offer; never try to manufacture want from scratch.",
    "Reframes SNIPED's positioning work: find the demand already in the LA founder/photography market and aim it, do not invent it.",
    "",
    ["mass-desire", "channeling", "demand", "meta-advertising"])
add(S, T, A, "meta-advertising", "Five stages of market awareness",
    "Schwartz maps how aware the prospect is (unaware, problem-aware, solution-aware, product-aware, most-aware) and shows the headline must meet them at their stage. The same offer needs different copy at each level.",
    "Diagnose the prospect's awareness stage and pitch to it; lead with the claim for the most-aware, with the problem for the unaware.",
    "A precise targeting tool for SNIPED's funnel: cold IG vs warm LinkedIn vs referred prospects need different openers.",
    "",
    ["awareness-stages", "prospect-state", "message-match", "meta-advertising"])
add(S, T, A, "strategy", "Market sophistication: escalate the claim as the market matures",
    "Schwartz's second axis: as a market hears more claims, simple promises stop working and copy must escalate (bigger claim, then mechanism, then identification). Where the market has heard everything, you sell identity.",
    "Gauge how many claims the market has already heard and escalate accordingly; in saturated markets, sell identity and mechanism, not the bare promise.",
    "Tells SNIPED how to pitch in the saturated AI-services and photography markets: lead with mechanism and identity, not generic promises.",
    "",
    ["market-sophistication", "escalation", "saturation", "strategy"])
add(S, T, A, "copywriting", "Intensify and verify the prospect's belief",
    "Schwartz's copy works by intensifying the desire and then verifying the claim with proof tuned to the prospect's existing beliefs. You amplify what they already feel, then make the promise credible to them.",
    "Amplify the desire the prospect already has, then prove the claim in terms they already believe.",
    "Sequences SNIPED's offer copy: intensify the founder's existing ambition, then verify with named proof.",
    "",
    ["intensify", "verify", "belief", "copywriting"])

# ===================== The Copywriter's Handbook · Bly (4) =====================
S = "copywriters_handbook_bly.txt"; T = "The Copywriter's Handbook (2006)"; A = "Robert W. Bly"
add(S, T, A, "copywriting", "The headline's four functions: attract, select, deliver, pull in",
    "Bly defines the headline's job precisely: get attention, select the audience, deliver a complete message, and draw the reader into the body. A headline that fails any of these wastes the ad.",
    "Test each headline against the four functions; rewrite until it attracts, qualifies, communicates, and pulls the reader in.",
    "A concrete QA checklist for every SNIPED hook and subject line.",
    "",
    ["headline-functions", "attention", "qualification", "copywriting"])
add(S, T, A, "copywriting", "The AIDA / motivating sequence structures persuasive copy",
    "Bly lays out the classic flow (attention, interest, desire, action) and the problem-agitate-solve motivating sequence as reliable scaffolds for copy that moves the reader to act.",
    "Structure persuasive copy on a proven sequence (attention to action, or problem-agitate-solve) rather than improvising the order.",
    "Gives SNIPED a repeatable skeleton for DMs, landing copy, and pitch decks.",
    "",
    ["aida", "motivating-sequence", "structure", "copywriting"])
add(S, T, A, "operator-process", "Copy is a craft of revision, not inspiration",
    "Bly frames copywriting as a systematic, revisable process (research, draft, edit, test) rather than a wait-for-inspiration art. Most of the quality is added in the rewrite.",
    "Treat copy as a process: research deeply, draft fast, then earn the quality in revision and testing.",
    "Aligns with SNIPED's operator-process discipline and the PROMPT_TEMPLATES_DEEP self-criticism gate.",
    "",
    ["revision", "process", "craft-not-inspiration", "operator-process"])
add(S, T, A, "copywriting", "Features tell, benefits sell; translate every feature",
    "Bly's enduring rule: customers buy benefits (what the feature does for them), so every feature must be translated into the outcome it produces for the reader.",
    "Translate every feature into the concrete benefit it delivers; never list a feature without its 'so that you...'.",
    "A line-level rule for SNIPED's offer and deliverable copy: sell the outcome, name the benefit.",
    "",
    ["features-vs-benefits", "translation", "outcome", "copywriting"])

# ===================== Influence · Cialdini (5) =====================
S = "influence_cialdini.txt"; T = "Influence (1984)"; A = "Robert B. Cialdini"
add(S, T, A, "brand-psychology", "Six principles of influence",
    "Cialdini identifies six near-universal levers of compliance: reciprocation, commitment/consistency, social proof, liking, authority, and scarcity. Each is a shortcut the mind uses under cognitive load.",
    "Build the six principles into offers and outreach deliberately and ethically; they are how decisions actually get made under load.",
    "The persuasion backbone for SNIPED's outreach, social proof, and offer design; pairs with the trust equation.",
    "",
    ["six-principles", "compliance", "influence", "brand-psychology"])
add(S, T, A, "brand-psychology", "Reciprocation: give first, and give meaningfully",
    "The reciprocity rule means people feel obligated to return a favor; advertisers and operators who give genuine value first earn a disproportionate willingness to reciprocate.",
    "Lead the relationship by giving real value first (insight, a useful asset) before any ask.",
    "Underwrites SNIPED's give-first content + LinkedIn-comment warming strategy before the VIB DM.",
    "",
    ["reciprocation", "give-first", "obligation", "brand-psychology"])
add(S, T, A, "brand-psychology", "Social proof: people follow people like them",
    "Under uncertainty, people copy the behavior of similar others; testimonials, client logos, and 'people like you' framing reduce perceived risk. Proof from a peer outweighs a claim from the seller.",
    "Show evidence that similar people (LA founders, peers) already chose you; peer proof beats self-claims.",
    "Directly shapes SNIPED's case-study and named-client strategy and the scene-density logic.",
    "",
    ["social-proof", "similarity", "risk-reduction", "brand-psychology"])
add(S, T, A, "brand-psychology", "Authority and liking lower resistance",
    "Credible authority signals (expertise, credentials, results) and genuine liking (similarity, rapport, sincere compliments) both reduce a prospect's resistance to a message.",
    "Establish earned authority (demonstrated results) and real rapport before the ask; both lower resistance ethically.",
    "Informs SNIPED's authority-asset building and the relationship-first sales motion.",
    "",
    ["authority", "liking", "resistance", "brand-psychology"])
add(S, T, A, "brand-psychology", "Scarcity: people want what is limited",
    "Cialdini shows that opportunities feel more valuable as they become less available; genuine scarcity and deadlines increase response. The lever is honest limits, not manufactured fakery.",
    "Use genuine scarcity (real capacity limits, real deadlines) to prompt action; never fabricate it, which destroys trust.",
    "Shapes SNIPED's capacity-limited, selective-roster positioning (the Reset floor + limited slots) honestly.",
    "",
    ["scarcity", "limited-availability", "honest-urgency", "brand-psychology"])

# ===================== Pre-Suasion · Cialdini (4) =====================
S = "presuasion_cialdini.txt"; T = "Pre-Suasion (2016)"; A = "Robert B. Cialdini"
add(S, T, A, "brand-psychology", "The privileged moment: prime before you pitch",
    "Cialdini's pre-suasion thesis: what you do in the moment before a message shapes how it lands. Directing attention to the right idea first makes the audience receptive before the ask.",
    "Engineer the moment before the pitch (the framing, the question, the context) so the prospect is already oriented toward yes.",
    "Shapes SNIPED's DM openers and discovery-call framing: set the frame before the offer.",
    "",
    ["pre-suasion", "privileged-moment", "priming", "brand-psychology"])
add(S, T, A, "content-strategy", "Attention channeled is importance implied",
    "Cialdini shows that whatever we focus attention on feels more important and causal. Directing a prospect's attention to one factor makes them weight it more heavily in the decision.",
    "Deliberately direct attention to the one factor you want weighted most; what you make salient becomes what they decide on.",
    "Informs SNIPED's content sequencing and the single-message discipline per post.",
    "",
    ["attention", "salience", "framing", "content-strategy"])
add(S, T, A, "brand-psychology", "Openers that create the right associations",
    "Pre-suasion works by opening with cues that activate the associations favorable to the message (warmth, trust, adventure). The opener primes the network the pitch then lands in.",
    "Choose openers (images, words, questions) that pre-activate the exact associations your offer needs.",
    "Guides SNIPED's hero-image and caption pairing: the visual primes the read.",
    "",
    ["associations", "priming", "openers", "brand-psychology"])
add(S, T, A, "operator-process", "Persuasion is ethical only with genuine merit",
    "Cialdini warns that pre-suasive technique without genuine merit backfires: the moment the audience discovers manipulation, trust and future influence collapse. Technique amplifies a real offer, it cannot replace one.",
    "Use pre-suasion only to spotlight genuine strengths; never to mask a weak offer, which destroys the relationship on discovery.",
    "Anchors SNIPED's low-self-orientation ethic: persuasion technique serves a genuinely strong offer or not at all.",
    "",
    ["ethics", "genuine-merit", "trust", "operator-process"])

# ===================== Contagious · Berger (4) =====================
S = "contagious_berger.txt"; T = "Contagious (2013)"; A = "Jonah Berger"
add(S, T, A, "content-strategy", "STEPPS: why things catch on",
    "Berger's six drivers of word-of-mouth: Social Currency, Triggers, Emotion, Public, Practical Value, and Stories. Content spreads when it makes the sharer look good and is built to travel.",
    "Engineer shareable content against the STEPPS checklist, especially social currency and emotion, rather than hoping it goes viral.",
    "A direct toolkit for SNIPED's organic-distribution and Card-system design.",
    "Six key STEPPS.",
    ["stepps", "word-of-mouth", "virality", "content-strategy"])
add(S, T, A, "content-strategy", "Social currency: people share what makes them look good",
    "The strongest sharing driver is self-presentation: people pass on things that make them appear smart, in-the-know, or high-status. Give sharers something that elevates them.",
    "Design content so sharing it raises the sharer's status; the audience is your distribution only if it flatters them to spread it.",
    "Directly informs SNIPED's Museum-Room / Card distribution: make the work status-conferring to share.",
    "",
    ["social-currency", "self-presentation", "sharing", "content-strategy"])
add(S, T, A, "content-strategy", "Triggers: top of mind is tip of tongue",
    "Berger shows that content linked to frequent environmental triggers gets talked about more, because the trigger keeps cueing it. Stickiness in memory beats a one-time splash.",
    "Tie the brand or message to a recurring everyday trigger so it gets cued repeatedly, not just once.",
    "Shapes SNIPED's recurring-cue content (the chapter cadence, signature visual motifs) for sustained recall.",
    "",
    ["triggers", "top-of-mind", "recall", "content-strategy"])
add(S, T, A, "brand-psychology", "High-arousal emotion drives sharing",
    "Berger's research: content that evokes high-arousal emotions (awe, excitement, even anger) is shared far more than low-arousal content (contentment, sadness). Emotion is the engine of spread.",
    "Build high-arousal emotion (especially awe) into work meant to travel; calm content does not move.",
    "Validates SNIPED's awe-and-aspiration visual register as a distribution lever, not just an aesthetic one.",
    "",
    ["high-arousal", "emotion", "awe", "brand-psychology"])

# ===================== The Choice Factory · Shotton (4) =====================
S = "the_choice_factory_shotton.txt"; T = "The Choice Factory (2018)"; A = "Richard Shotton"
add(S, T, A, "brand-psychology", "Behavioural biases shape what we buy",
    "Shotton catalogs 25 evidence-backed biases (social proof, the pratfall effect, price anchoring, etc.) that quietly govern purchase decisions, each with field experiments showing the lift.",
    "Apply specific, tested biases to offer and copy decisions rather than relying on intuition about what persuades.",
    "Gives SNIPED an evidence base for small, high-leverage copy and pricing tweaks.",
    "",
    ["behavioural-biases", "evidence-based", "purchase", "brand-psychology"])
add(S, T, A, "brand-psychology", "The pratfall effect: a flaw can increase appeal",
    "Shotton shows that admitting a small weakness can make a brand more credible and likable than claiming perfection. A visible flaw makes the strengths believable.",
    "Admit a genuine small limitation in positioning; the honesty makes the strong claims more credible.",
    "Backs SNIPED's refusal-positioning and honest-broker voice: naming what you do not do builds trust.",
    "",
    ["pratfall-effect", "honesty", "credibility", "brand-psychology"])
add(S, T, A, "strategy", "Context and framing move behavior more than persuasion",
    "Shotton's recurring finding: changing the decision context (defaults, ordering, environment) often shifts behavior more than changing the argument. The frame beats the pitch.",
    "Before strengthening the argument, change the context and framing; defaults and ordering often move more than copy.",
    "Connects to Pre-Suasion and tells SNIPED to design the buying context, not just the pitch.",
    "",
    ["context", "framing", "defaults", "strategy"])
add(S, T, A, "brand-psychology", "Distinctiveness beats differentiation for memory",
    "Shotton draws on the evidence that distinctive brand assets (consistent colors, symbols, sounds) drive recall more reliably than rational differentiation claims. Be recognizable first.",
    "Invest in consistent distinctive assets for instant recognition, not only in rational differentiation arguments.",
    "Validates SNIPED's consistent visual-identity discipline (the Card system, signature grading) as a memory asset.",
    "",
    ["distinctiveness", "brand-assets", "recall", "brand-psychology"])

# ===================== Alchemy · Sutherland (4) =====================
S = "alchemy_sutherland.txt"; T = "Alchemy (2019)"; A = "Rory Sutherland"
add(S, T, A, "brand-psychology", "Psycho-logic: value is perceived, not just rational",
    "Sutherland argues that perceived value often defies economic logic: the meaning, context, and story around a thing can matter more than its function. Solving the perception can beat improving the product.",
    "Look for psychological solutions (meaning, framing, ritual) before expensive functional ones; perception is where much value lives.",
    "Frees SNIPED to compete on meaning and experience, not just deliverable specs.",
    "",
    ["psycho-logic", "perceived-value", "meaning", "brand-psychology"])
add(S, T, A, "aesthetics", "Costly signalling makes value credible",
    "Sutherland explains that expensive, hard-to-fake signals (craft, restraint, evident effort) credibly communicate quality precisely because they are costly. The expense is the message.",
    "Invest visibly in costly signals of quality (craft, restraint, production value); the evident effort is itself the proof.",
    "Underwrites SNIPED's quiet-luxury production investment as a credibility signal, not vanity.",
    "",
    ["costly-signalling", "quality-signal", "craft", "aesthetics"])
add(S, T, A, "brand", "The opposite of a good idea can also be a good idea",
    "Sutherland's heuristic against best-practice conformity: when everyone optimizes the same way, the contrarian move can win precisely because it is different. Distinctiveness comes from doing the non-obvious.",
    "Test the deliberately contrarian option; in a market of copycats, the opposite of consensus is often the opportunity.",
    "Backs SNIPED's anti-faceless-AI, against-the-grain positioning as a strategic edge, not just taste.",
    "",
    ["contrarian", "distinctiveness", "non-obvious", "brand"])
add(S, T, A, "strategy", "Test the irrational; do not over-trust the spreadsheet",
    "Sutherland warns that purely rational, measurable optimization misses the psychological wins that cannot be easily quantified. The most valuable moves often look irrational on a spreadsheet.",
    "Reserve room for psychologically-driven bets that resist measurement; do not let the spreadsheet veto every non-rational win.",
    "Balances SNIPED's data discipline with permission for taste-led, hard-to-measure brand bets.",
    "",
    ["anti-spreadsheet", "irrational-value", "judgment", "strategy"])

# ===================== This Is Marketing · Godin (4) =====================
S = "this_is_marketing_godin.txt"; T = "This Is Marketing (2018)"; A = "Seth Godin"
add(S, T, A, "positioning", "Seek the smallest viable market",
    "Godin argues you win by serving the smallest market you can sustainably delight, not the largest you can reach. Specificity to a tight audience produces the remarkability that then spreads.",
    "Define the smallest viable audience and obsess over delighting them; let the breadth come from their word-of-mouth.",
    "The commercial version of SNIPED's scene-density doctrine: depth in a tight LA founder cluster over broad reach.",
    "The Smallest Viable Market.",
    ["smallest-viable-market", "specificity", "scene-density", "positioning"])
add(S, T, A, "brand", "People like us do things like this",
    "Godin frames marketing as identity and belonging: people adopt what fits the story of who they are. The strongest positioning aligns the offer with a tribe's sense of 'people like us'.",
    "Frame the offer as what 'people like us' do; sell belonging and identity, not just function.",
    "Shapes SNIPED's positioning as membership in a specific LA creative-founder identity.",
    "People like us do things like this.",
    ["identity", "belonging", "tribe", "brand"])
add(S, T, A, "meta-advertising", "Marketing is the generous act of helping people become who they want to be",
    "Godin reframes marketing away from hype toward service: helping people make the change they seek and become the version of themselves they aspire to. Good marketing serves a desire the customer already holds.",
    "Position the work as helping the buyer become who they want to be; market the transformation, not the attention grab.",
    "Defines SNIPED's hospitality-grade, service-first commercial voice over interruptive selling.",
    "",
    ["generous-marketing", "transformation", "service", "meta-advertising"])
add(S, T, A, "positioning", "Learn to see: marketing is empathy and tension",
    "Godin's titular lesson: you cannot be seen until you learn to see the customer's worldview, and effective marketing creates a productive tension that the desired change resolves.",
    "Start from the customer's worldview and create the tension your offer resolves; lead with empathy, not features.",
    "Grounds SNIPED's discovery and positioning in the founder's worldview, not the photographer's preferences.",
    "You Can't Be Seen Until You Learn to See.",
    ["empathy", "worldview", "tension", "positioning"])

# ===================== Purple Cow · Godin (3) =====================
S = "purple_cow_godin.txt"; T = "Purple Cow (2003)"; A = "Seth Godin"
add(S, T, A, "brand", "Be remarkable or be invisible",
    "Godin argues that in a crowded market the safe, average product is invisible; only the remarkable (literally worth remarking on) gets noticed and spread. Boring is the biggest risk.",
    "Build remarkability into the product itself, not the ad; if it is not worth talking about, no budget will save it.",
    "Pushes SNIPED to make the work itself remarkable (the lineage doc, the Card system) rather than relying on promotion.",
    "",
    ["remarkable", "purple-cow", "anti-average", "brand"])
add(S, T, A, "strategy", "Market to the sneezers and early adopters, not the mass",
    "Godin says the remarkable spreads through early adopters and 'sneezers' who tell the rest; the mass market is reached through them, not directly. Aim the launch at the people who spread.",
    "Target the early adopters and natural sharers first; they carry the work to the majority.",
    "Aligns with SNIPED's scene-density + Hit-Makers cluster strategy for distribution.",
    "",
    ["early-adopters", "sneezers", "diffusion", "strategy"])
add(S, T, A, "brand", "Safe is risky; the average gets ignored",
    "Godin inverts the intuition that bold is risky: in a saturated attention market, blending in is the genuine risk because it guarantees being ignored. Playing safe is the dangerous bet.",
    "Treat blending in as the real risk; choose the bold, distinctive option over the safe, average one.",
    "Backs SNIPED's restraint-but-distinctive register and refusal to look like every other photographer.",
    "",
    ["safe-is-risky", "boldness", "distinctiveness", "brand"])

# ===================== Differentiate or Die · Trout (4) =====================
S = "differentiate_or_die_trout.txt"; T = "Differentiate or Die (2008)"; A = "Jack Trout, Steve Rivkin"
add(S, T, A, "positioning", "Own a differentiating idea in the prospect's mind",
    "Trout's core: differentiation happens in the prospect's mind, and a brand must own a single distinct idea there. Without a clear differentiating idea, you compete only on price.",
    "Define and own one differentiating idea in the prospect's mind; without it, you have only price to compete on.",
    "The positioning spine for SNIPED's one-liner and the refusal-positioning lever.",
    "",
    ["differentiation", "owning-an-idea", "mind-positioning", "positioning"])
add(S, T, A, "positioning", "Being first or being a specialist are powerful differentiators",
    "Trout catalogs durable differentiators: leadership/heritage, being first, being the specialist, and proprietary attributes. The specialist beats the generalist in the prospect's mind.",
    "Claim a credible differentiator (first, specialist, heritage, or a proprietary attribute) rather than a generic 'better'.",
    "Tells SNIPED to position as the specialist (LA founder photography lineage), not a general photographer.",
    "",
    ["specialist", "first-mover", "heritage", "positioning"])
add(S, T, A, "strategy", "A differentiator needs proof and a reason to believe",
    "Trout stresses that a differentiating claim must be backed by credentials and proof, or it is just an empty slogan. The reason-to-believe is what makes the difference stick.",
    "Pair every differentiating claim with concrete proof and credentials; an unproven claim is ignored.",
    "Connects SNIPED's positioning to its case-study and authority-asset requirements.",
    "",
    ["reason-to-believe", "proof", "credentials", "strategy"])
add(S, T, A, "positioning", "Price is the enemy of differentiation",
    "Trout warns that competing on price is the default for the undifferentiated and a race to the bottom; real differentiation is what lets a brand escape price competition.",
    "Refuse to let the conversation default to price; differentiation is the only durable escape from a price war.",
    "Underwrites SNIPED's price-floor discipline (the Reset floor) backed by a differentiated position.",
    "",
    ["price-competition", "commoditization-escape", "value", "positioning"])

# ===================== Obviously Awesome · Dunford (4) =====================
S = "obviously_awesome_dunford.txt"; T = "Obviously Awesome (2019)"; A = "April Dunford"
add(S, T, A, "positioning", "Positioning is the context you set for your product",
    "Dunford reframes positioning as deliberately choosing the market context (the frame of reference) through which customers perceive the product. The same product is dull or awesome depending on its context.",
    "Choose the market context that makes the offer obviously valuable; positioning is a deliberate choice, not a tagline.",
    "Gives SNIPED a concrete method to set the frame for its premium offer rather than defaulting to 'photographer'.",
    "products can be transformed by changing their context",
    ["positioning-as-context", "frame-of-reference", "deliberate", "positioning"])
add(S, T, A, "positioning", "The five components of effective positioning",
    "Dunford's method: competitive alternatives, unique attributes, the value those enable, the customers who care most, and the market category you frame yourself in. Work them in order to land a position.",
    "Run the five-component process (alternatives, attributes, value, best-fit customers, market category) to build a position deliberately.",
    "A repeatable positioning worksheet for SNIPED offers, complementing Finding Your Edge.",
    "",
    ["five-components", "positioning-process", "method", "positioning"])
add(S, T, A, "commercial-architecture", "Pick the market category you want to be compared in",
    "Dunford shows that the category you claim determines the expectations, competitors, and price anchors you are judged against. Choosing the category is choosing the comparison.",
    "Deliberately choose the market category you compete in so you control the comparison set and price anchor.",
    "Helps SNIPED frame itself in a premium category (creative direction / brand-building), not commodity photography.",
    "",
    ["market-category", "comparison-set", "price-anchor", "commercial-architecture"])
add(S, T, A, "positioning", "Position from genuine strengths, not aspirations",
    "Dunford insists positioning must start from what the product is genuinely best at for a specific customer, not from where the team wishes it competed. Honest strengths beat aspirational claims.",
    "Anchor positioning in demonstrable strengths for a specific best-fit customer, never in aspiration.",
    "Echoes the find-your-edge honesty: position on real advantages, not wished-for ones.",
    "",
    ["genuine-strengths", "best-fit-customer", "honesty", "positioning"])

# ===================== $100M Offers · Hormozi (4) =====================
S = "100m_offers_hormozi.txt"; T = "$100M Offers (2021)"; A = "Alex Hormozi"
add(S, T, A, "offer-design", "The Grand Slam Offer: so good people feel stupid saying no",
    "Hormozi's thesis: a great offer (not better marketing) is the highest leverage point; the goal is an offer so strong, with so much value stacked, that declining feels foolish.",
    "Engineer the offer itself to be overwhelmingly valuable before optimizing the marketing; the offer is the leverage.",
    "Reframes SNIPED's commercial work around offer construction (the Reset, Op Kit, Brand System) as the primary lever.",
    "",
    ["grand-slam-offer", "offer-leverage", "value-stack", "offer-design"])
add(S, T, A, "offer-design", "The Value Equation",
    "Hormozi's value equation: perceived value rises with the dream outcome and likelihood of achievement, and falls with time delay and effort/sacrifice. Improve any of the four to raise value.",
    "Maximize dream outcome and perceived likelihood while minimizing time and effort in every offer.",
    "A precise design tool for SNIPED offers: speed and certainty of the client's result are as sellable as the result itself.",
    "",
    ["value-equation", "dream-outcome", "time-and-effort", "offer-design"])
add(S, T, A, "commercial-architecture", "Sell in a market with demand; do not fight the market",
    "Hormozi insists the offer's market matters first: a great offer to a starving, growing, reachable, painful-problem market beats a perfect offer to a bad one. Pick the market before perfecting the pitch.",
    "Choose a market with real, growing, painful demand before engineering the offer; the market caps the offer's ceiling.",
    "Reinforces SNIPED's ICP discipline: the LA founder market selection precedes offer craft.",
    "",
    ["market-selection", "demand", "starving-crowd", "commercial-architecture"])
add(S, T, A, "offer-design", "Stack value and remove risk with guarantees",
    "Hormozi builds offers by stacking distinct value components (each priced) and removing the buyer's risk through strong guarantees, so the perceived value vastly exceeds the price.",
    "Itemize and stack the offer's value components and add a real risk-reversal guarantee to collapse the buyer's perceived risk.",
    "Directly applicable to SNIPED's premium packages: stack the deliverables and reverse the risk.",
    "",
    ["value-stack", "guarantee", "risk-reversal", "offer-design"])

# ===================== $100M Leads · Hormozi (4) =====================
S = "100m_leads_hormozi.txt"; T = "$100M Leads (2023)"; A = "Alex Hormozi"
add(S, T, A, "sales-flow", "The Core Four ways to get leads",
    "Hormozi reduces lead generation to four channels: warm outreach, posting free content, cold outreach, and paid ads, each a 'one-to-one or one-to-many' to 'people you know or do not know' quadrant.",
    "Pick and systematize from the Core Four (warm/cold outreach, content, ads) rather than improvising lead-gen.",
    "Maps SNIPED's existing surfaces (LinkedIn comments = warm, IG content = posting, VIB DM = cold) onto a complete framework.",
    "",
    ["core-four", "lead-generation", "channels", "sales-flow"])
add(S, T, A, "sales-flow", "The lead magnet: give a complete solution to a narrow problem",
    "Hormozi's lead magnet principle: offer a free thing that fully solves one narrow problem, which both proves value and reveals the next, larger problem you sell the solution to.",
    "Build a lead magnet that completely solves one small problem and naturally surfaces the bigger paid one.",
    "Shapes SNIPED's give-first assets (a free audit, a mini direction guide) as qualified lead generators.",
    "",
    ["lead-magnet", "free-value", "problem-revelation", "sales-flow"])
add(S, T, A, "commercial-architecture", "More leads plus better offers compound",
    "Hormozi frames growth as the product of lead volume, lead quality, and offer strength; improving each multiplies the others rather than adding. The system compounds.",
    "Improve lead volume, lead quality, and offer strength together; they multiply, so do not optimize one in isolation.",
    "Connects SNIPED's outreach (B2B/N8N) and offer (100M Offers) work into one compounding commercial system.",
    "",
    ["compounding", "lead-volume-quality", "system", "commercial-architecture"])
add(S, T, A, "sales-flow", "Engage your audience and turn it into leads with a clear CTA",
    "Hormozi stresses that an audience only becomes leads when you make a clear, repeated offer to engage; attention without a call to action does not convert. Ask, specifically and often.",
    "Make a clear, specific call to action repeatedly; an audience without an explicit ask never becomes leads.",
    "Corrects a common SNIPED-adjacent failure mode: beautiful content with no consistent CTA.",
    "",
    ["call-to-action", "audience-to-leads", "conversion", "sales-flow"])

# ===================== Made to Stick · Heath (4) =====================
S = "made_to_stick_heath.txt"; T = "Made to Stick (2007)"; A = "Chip Heath, Dan Heath"
add(S, T, A, "content-strategy", "SUCCESs: the six traits of sticky ideas",
    "The Heaths' framework for memorable ideas: Simple, Unexpected, Concrete, Credible, Emotional, Stories. Ideas that stick share these traits; you can engineer them in.",
    "Run any message through the SUCCESs checklist; deliberately add simplicity, surprise, concreteness, credibility, emotion, and story.",
    "A direct toolkit for SNIPED's content, captions, and the lineage-doc narrative.",
    "Simple, Unexpected, Concrete, Credible, Emotional, Stories.",
    ["success-framework", "stickiness", "memorability", "content-strategy"])
add(S, T, A, "content-strategy", "Find the core and lead with it",
    "The Heaths' first principle is simplicity-as-core: strip an idea to its single most important element and say that first. A message that says everything says nothing.",
    "Strip every message to its one core idea and lead with it; resist burying the lead under completeness.",
    "Disciplines SNIPED's one-message-per-post and one-idea-per-deliverable habit.",
    "",
    ["core-idea", "simplicity", "lead-with-it", "content-strategy"])
add(S, T, A, "copywriting", "The Curse of Knowledge is the enemy of clarity",
    "The Heaths name the curse of knowledge: once you know something, you cannot imagine not knowing it, so experts communicate in abstractions the audience cannot decode. Concreteness breaks the curse.",
    "Fight the curse of knowledge by translating expertise into concrete, audience-level language and examples.",
    "Explains why SNIPED must translate its craft expertise into founder-legible benefits.",
    "Curse of Knowledge.",
    ["curse-of-knowledge", "concreteness", "clarity", "copywriting"])
add(S, T, A, "content-strategy", "Unexpectedness opens and curiosity gaps hold attention",
    "The Heaths show that surprise grabs attention and a 'curiosity gap' (a hole in the audience's knowledge they want closed) holds it. Break a pattern, then promise to resolve the gap.",
    "Open with a pattern-break and create a curiosity gap the content then closes; surprise earns attention, the gap keeps it.",
    "Backs SNIPED's hook design and the open-loop structure of carousels and threads.",
    "",
    ["unexpectedness", "curiosity-gap", "attention", "content-strategy"])

# ===================== Building a StoryBrand · Miller (4) =====================
S = "building_a_storybrand_miller.txt"; T = "Building a StoryBrand (2017)"; A = "Donald Miller"
add(S, T, A, "brand", "The customer is the hero; the brand is the guide",
    "Miller's central inversion: position the customer as the hero of the story and the brand as the guide who helps them win. Brands that cast themselves as the hero lose the customer's attention.",
    "Frame all messaging with the customer as hero and the brand as the guide; never make the brand the hero.",
    "Reframes SNIPED's client storytelling: the founder is the hero, SNIPED is the guide with a plan.",
    "",
    ["customer-as-hero", "brand-as-guide", "story-role", "brand"])
add(S, T, A, "copywriting", "The SB7 framework structures a clear brand message",
    "Miller's seven-part story spine: a character with a problem meets a guide who gives a plan and calls them to action, ending in success and avoiding failure. It is a repeatable message skeleton.",
    "Structure brand messaging on the SB7 spine (character, problem, guide, plan, call to action, success, failure).",
    "A ready scaffold for SNIPED's site copy, decks, and onboarding narrative.",
    "the StoryBrand 7-Part Framework",
    ["sb7", "story-spine", "message-structure", "copywriting"])
add(S, T, A, "positioning", "Clarify the problem on three levels: external, internal, philosophical",
    "Miller shows that customers buy resolution to an internal feeling, not just the external problem; the strongest messaging names the external problem, the internal frustration, and the philosophical stake.",
    "Name the customer's external problem, the internal frustration it causes, and the philosophical why; sell the internal resolution.",
    "Deepens SNIPED's discovery: the founder's external need (photos) sits over an internal need (to be seen as serious).",
    "",
    ["three-level-problem", "internal-problem", "stakes", "positioning"])
add(S, T, A, "copywriting", "If you confuse, you lose; clarity beats cleverness",
    "Miller's blunt rule: a confused customer does not buy, so clarity always beats cleverness. Cut jargon and make the offer and next step obvious.",
    "Ruthlessly prioritize clarity over cleverness; if the customer has to work to understand, they leave.",
    "A guardrail against over-stylized SNIPED copy: the offer and next step must be instantly clear.",
    "If you confuse, you lose.",
    ["clarity", "anti-jargon", "clear-cta", "copywriting"])

# ===================== synthesis (4 · cite a representative real file) =====================
add("scientific_advertising_hopkins.txt", "BATCH_009 cross-source synthesis", "SNIPED synthesis", "copywriting",
    "The whole canon reduces to: sell the outcome to a specific person, with proof",
    "From Hopkins to Hormozi, the advertising/copywriting canon agrees on a spine: understand a specific prospect's existing desire, promise a concrete outcome, prove it, and make acting easy. Style serves selling, never the reverse.",
    "Hold every SNIPED commercial asset to the canon's spine: specific person, concrete outcome, real proof, easy action.",
    "The unifying standard BATCH_009 hands SNIPED's commercial voice across copy, offers, and content.",
    "",
    ["synthesis", "outcome-proof-action", "commercial-voice", "copywriting"])
add("influence_cialdini.txt", "BATCH_009 cross-source synthesis", "SNIPED synthesis", "operator-process",
    "Persuasion is dual-use; SNIPED applies it with low self-orientation",
    "Cialdini, Shotton, and Pre-Suasion supply powerful compliance levers that can manipulate or serve. The canon and SNIPED's trust doctrine converge: technique is only legitimate atop a genuinely strong, honestly-described offer.",
    "Use the persuasion levers only to spotlight a genuinely strong offer; never to mask a weak one, which destroys trust on discovery.",
    "Ties BATCH_009's persuasion power to SNIPED's trust-equation / low-self-orientation ethic.",
    "",
    ["synthesis", "ethical-persuasion", "trust", "operator-process"])
add("differentiate_or_die_trout.txt", "BATCH_009 cross-source synthesis", "SNIPED synthesis", "positioning",
    "Differentiation plus an irresistible offer is the escape from price",
    "Trout, Dunford, and Godin say own a distinct position in a specific mind; Hormozi says make the offer overwhelmingly valuable. Together they are SNIPED's escape from commodity-photographer price competition: a differentiated position carrying a grand-slam offer.",
    "Pair a sharply differentiated position with an overwhelmingly valuable offer; the combination is what defends the premium price.",
    "Connects BATCH_009 to SNIPED's price-floor discipline and the B2B positioning lane.",
    "",
    ["synthesis", "differentiation-plus-offer", "premium-defense", "positioning"])
add("contagious_berger.txt", "BATCH_009 cross-source synthesis", "SNIPED synthesis", "content-strategy",
    "Make work remarkable and shareable for the smallest viable market",
    "Godin's smallest-viable-market, Berger's STEPPS, and the Heaths' SUCCESs converge: serve a tight audience with work so remarkable and well-built-to-travel that they spread it. Distribution is engineered into the work, not bolted on.",
    "Engineer remarkability and shareability into the work itself for a specific tight audience; let them be the distribution.",
    "Unifies BATCH_009's distribution lessons with SNIPED's scene-density + Card-system + Hit-Makers doctrine.",
    "",
    ["synthesis", "remarkable-shareable", "smallest-viable-market", "content-strategy"])

# ---- emit ----
em = chr(0x2014)
lines = []
for i, ch in enumerate(C, start=1):
    lines.append({
        "chunk_id": f"BATCH_009_{i:03d}",
        "batch_id": "BATCH_009",
        "source_title": ch["source_title"],
        "source_file": ch["source_file"],
        "author": ch["author"],
        "domain": ch["domain"],
        "concept": ch["concept"],
        "summary": ch["summary"],
        "usable_principle": ch["usable_principle"],
        "sniped_relevance": ch["sniped_relevance"],
        "direct_quotes": ch["direct_quotes"],
        "tags": ch["tags"],
    })

swept = 0
for rec in lines:
    for k, v in rec.items():
        if isinstance(v, str) and em in v:
            rec[k] = v.replace(em, " · "); swept += 1
        elif isinstance(v, list):
            nl = []
            for item in v:
                if isinstance(item, str) and em in item:
                    nl.append(item.replace(em, " · ")); swept += 1
                else:
                    nl.append(item)
            rec[k] = nl

OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in lines) + "\n", encoding="utf-8")
print(f"Wrote {len(lines)} chunks to {OUT.name}")
print(f"Em-dashes swept: {swept}")
from collections import Counter
print("Domain distribution:", dict(sorted(Counter(r["domain"] for r in lines).items())))
print("Source distribution:")
for k, v in sorted(Counter(r["source_file"] for r in lines).items()):
    print(f"  {v:3d}  {k}")
