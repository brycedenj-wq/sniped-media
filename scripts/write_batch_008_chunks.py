#!/usr/bin/env python3
"""
BATCH_008 chunk writer · AI / tech / automation / agency / operating-edge canon.
Schema: chunk_id, batch_id, source_title, source_file, author, domain, concept, summary,
        usable_principle, sniped_relevance, direct_quotes, tags. ID pattern BATCH_008_NNN.
Domains reused (all pre-existing): ai-tooling, prompt-engineering, automation-blueprint,
operator-process, strategy, systems-thinking, ethics, client-application, commercial-architecture,
meta-doctrine. NO new domain. Copyright-safe SHORT illustrative quotes only. Em-dash swept.
Parts 1-5 of sniped_os_knowledge_dump (n8n/prompt) are cross-referenced, NOT re-chunked
(already in N8N_AUTOMATION_SYSTEMS + PROMPT_TEMPLATES_DEEP).
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_008_CHUNKS.jsonl"

C = []  # list of dicts; chunk_id assigned sequentially


def add(src, title, author, domain, concept, summary, usable, relevance, quotes, tags):
    C.append({
        "source_title": title, "source_file": src, "author": author, "domain": domain,
        "concept": concept, "summary": summary, "usable_principle": usable,
        "sniped_relevance": relevance, "direct_quotes": quotes, "tags": tags,
    })


# ============================ CLUSTER A · 12 ai_tech books ============================

# --- 1 · Automate This · Christopher Steiner (2012) · 7 ---
S = "automate_this_steiner.txt"; T = "Automate This (2012)"; A = "Christopher Steiner"
add(S, T, A, "systems-thinking", "Algorithms colonize human work, starting at the top",
    "Steiner traces how algorithms first conquered Wall Street, then spread to medicine, music, law, and customer service. The pattern is consistent: wherever a task can be reduced to rules and data, code eventually outperforms and replaces the human doing it.",
    "Assume any rules-based, data-rich task in a client's business is on an automation timeline. The question is not whether it gets automated but when, and whether you build the system that does it.",
    "Validates SNIPED's AI-build thesis: the agency captures value by being the one who automates a client's rules-based bottlenecks before a generic tool does.",
    "Algorithms came to rule our world, starting with the places that paid the most.",
    ["automate-this", "algorithms", "automation-history", "wall-street", "ai-canon"])
add(S, T, A, "strategy", "The quants left finance and seeded every other industry",
    "The book documents how mathematicians and physicists who built trading algorithms dispersed into other sectors, carrying the automation playbook with them. Talent migration, not just technology, drove the spread.",
    "Follow where automation talent and tooling migrate next; those industries are about to be reshaped and are the richest agency markets.",
    "Tells SNIPED where to point its AI-agency lane: industries just now receiving the automation wave that finance got two decades ago.",
    "",
    ["talent-migration", "automation-spread", "market-timing", "strategy"])
add(S, T, A, "ethics", "Automation displaces the middle, rewards the builders",
    "Steiner is candid that algorithmic automation hollows out routine cognitive jobs while concentrating gains among those who design the systems. The bots do not get tired, do not need salaries, and do not quit.",
    "Position yourself on the builder side of the line, and frame client offers as protecting the owner's margin rather than as cutting their staff.",
    "Sharpens SNIPED's outcome framing: sell the owner more capacity and resilience, not layoffs, while privately knowing the builder captures the durable value.",
    "",
    ["displacement", "builder-vs-built", "ethics", "labor"])
add(S, T, A, "commercial-architecture", "Speed is the original algorithmic edge",
    "In trading, the entire early advantage was latency: being milliseconds faster than the next participant. The lesson generalizes: when a process is automated, whoever runs it fastest and most reliably wins the spread.",
    "Design client automations for speed and reliability of response, because in a commoditizing market, response time becomes the differentiator.",
    "Backs the SNIPED responsiveness-AI lane (missed-call / 24-7 booking): the speed of the automated reply is itself the competitive moat for a small business.",
    "",
    ["latency", "speed-as-edge", "responsiveness", "commercial-architecture"])
add(S, T, A, "systems-thinking", "Every automatable process is first mapped, then encoded",
    "Before an algorithm can run a process it must be made explicit: the implicit judgment of an expert is decomposed into observable inputs, rules, and outputs. The mapping work is the hard part; the code is downstream.",
    "Treat process-mapping as the billable, defensible core of an AI build; the model is a commodity, the mapped process is the IP.",
    "Frames SNIPED's discovery phase as the real product: the documented process map is what the client cannot easily get elsewhere and what the workflow is built on.",
    "",
    ["process-mapping", "tacit-to-explicit", "systems-thinking", "ip"])
add(S, T, A, "strategy", "First movers in a vertical compound their data advantage",
    "Early algorithmic adopters in a sector accumulated proprietary data and refinement cycles that latecomers could not match. The advantage compounded because better predictions attracted more activity, which produced more data.",
    "Get a client live early in their vertical so their accumulating operational data becomes a moat you maintain.",
    "Supports SNIPED's scene-density logic applied commercially: depth in one vertical compounds, breadth across many does not.",
    "",
    ["first-mover", "data-advantage", "compounding", "strategy"])
add(S, T, A, "ai-tooling", "Bots are tireless, consistent, and scale without headcount",
    "Steiner's recurring contrast is structural: software does not sleep, does not vary, and its marginal cost approaches zero. A single well-built automation replaces a function that previously required hiring.",
    "Price automations against the fully loaded cost of the headcount or hours they replace, not against software-license benchmarks.",
    "Anchors SNIPED's ROI-based pricing: the business case is labor-hours and lost-opportunity recovered, which the AI Edge opportunity templates already structure.",
    "",
    ["zero-marginal-cost", "scale", "roi-pricing", "ai-tooling"])

# --- 2 · Only Humans Need Apply · Davenport & Kirby (2016) · 8 ---
S = "only_humans_need_apply_davenport.txt"; T = "Only Humans Need Apply (2016)"; A = "Thomas H. Davenport, Julia Kirby"
add(S, T, A, "strategy", "Augmentation beats automation as a career and business strategy",
    "Davenport and Kirby reframe the automation debate away from human-versus-machine toward augmentation: people working alongside smart machines. They reject the zero-sum 'race against the machine' framing in favor of a deliberate division of labor.",
    "Sell augmentation, not replacement: the offer is a human operator made more capable by AI, which is both more accurate and more sellable.",
    "This is the intellectual backbone of SNIPED's hybrid-operator stance: AI as leverage on a human judgment layer, never a faceless replacement.",
    "We like to say that, as they work with machines, people can step up, step aside, step in, step narrowly, or step forward.",
    ["augmentation", "human-plus-machine", "hybrid-operator", "strategy"])
add(S, T, A, "operator-process", "Step up: move to higher-level judgment the machine cannot reach",
    "The first augmentation strategy is to rise above automated decisions to the big-picture judgment, synthesis, and framing that machines do not do. You let the system handle the computable layer and you own the meaning layer.",
    "Keep yourself on the framing and judgment layer of any client engagement; delegate the computable layer to the build.",
    "Defines where the SNIPED operator sits in every engagement: above the automation, owning direction and interpretation.",
    "",
    ["step-up", "judgment", "operator-process", "augmentation"])
add(S, T, A, "operator-process", "Step narrowly: own a specialty too small to automate",
    "Stepping narrowly means finding a specialty so specific that no one will build a system for it. Deep, defensible niche knowledge is a hedge against general-purpose automation.",
    "Choose a vertical narrow enough that a generic AI tool will never target it, then become the operator who automates it.",
    "Directly reinforces the find-your-edge backwards approach and SNIPED's narrow-niche ICP doctrine: defensibility comes from specificity.",
    "",
    ["step-narrowly", "niche", "defensibility", "operator-process"])
add(S, T, A, "client-application", "Step in: become the human who governs the machine",
    "Stepping in means monitoring, interpreting, and improving the automated system, standing between the model and the business outcome. The value is in oversight, exception handling, and trust.",
    "Build a human-in-the-loop checkpoint into every client automation and bill for the governance, not just the build.",
    "Maps to SNIPED's human-approval gate in the N8N workflows: the operator who governs the automation is the trusted, recurring relationship.",
    "",
    ["step-in", "human-in-the-loop", "governance", "client-application"])
add(S, T, A, "ethics", "Step aside: lean into the human-only work machines cannot touch",
    "Stepping aside means moving toward interpersonal, creative, and physical work where humans hold durable advantage. Empathy, persuasion, and taste are not on the near-term automation frontier.",
    "Reserve the relationship, creative-direction, and taste work for the human operator; let AI carry the rote production.",
    "Confirms SNIPED's edit-register and direction-stack work as the human-held, premium layer that AI production cannot replace.",
    "",
    ["step-aside", "human-advantage", "taste", "ethics"])
add(S, T, A, "strategy", "Step forward: build the machines themselves",
    "The fifth strategy is to become a builder of the automating systems. This is the highest-leverage position because the builder captures value across every business that adopts the tool.",
    "The agency itself is the step-forward play: SNIPED builds the machines that its clients then operate.",
    "Names SNIPED's structural position in the AI economy: the builder layer, which is why the AI-agency lane is the leverage move.",
    "",
    ["step-forward", "builder", "leverage", "strategy"])
add(S, T, A, "ethics", "The John Henry track is a losing strategy",
    "Trying to out-compute the machine, like John Henry racing the steam drill, is a guaranteed long-run loss. Whatever performance level a human achieves, the machine will match it next year, demanding ever more.",
    "Never compete with AI on the axis it is good at; compete on the axis it is structurally bad at.",
    "Validates SNIPED's refusal to compete on volume or speed of generic output, choosing instead judgment, taste, and relationship.",
    "If you believe your value depends on out-thinking the computers, you are on the John Henry track.",
    ["john-henry", "anti-pattern", "human-advantage", "ethics"])
add(S, T, A, "systems-thinking", "Machines have depth, humans have breadth",
    "The book's enduring distinction is that AI systems are specialized: superb at one narrow task, unable to transfer. Humans retain breadth, the ability to do many things adequately and connect across them.",
    "Compose narrow AI tools under a human generalist who connects them into an outcome; the connective layer is the human edge.",
    "Describes the SNIPED operator exactly: the generalist who orchestrates many narrow tools into a single client outcome.",
    "We have machines that are very good at playing chess, but they cannot play dominoes too.",
    ["depth-vs-breadth", "generalist", "orchestration", "systems-thinking"])

# --- 3 · Power and Prediction · Agrawal, Gans, Goldfarb (2022) · 7 ---
S = "power_and_prediction_agrawal.txt"; T = "Power and Prediction (2022)"; A = "Ajay Agrawal, Joshua Gans, Avi Goldfarb"
add(S, T, A, "strategy", "Point solutions versus system solutions",
    "The central thesis: AI value arrives in two waves. Point solutions drop AI into an existing process for a quick win; system solutions redesign the product and the organization around the new low cost of prediction, unlocking far larger gains.",
    "Diagnose whether a client opportunity is a point solution (fast, modest) or a system solution (slow, transformative) and price and sequence accordingly.",
    "Gives SNIPED a two-tier opportunity taxonomy: quick point-solution wins build trust, system solutions are the high-value follow-on engagements.",
    "Some implementations are what we call point solutions. They are straightforward. Other implementations require redesigning the product and the organization.",
    ["point-solution", "system-solution", "ai-economics", "strategy"])
add(S, T, A, "strategy", "We live in the Between Times",
    "The authors name the present a unique interval: after the power of the technology is proven but before its widespread system-level adoption. The gap exists because system change is hard, not because the technology is unready.",
    "Frame the current moment to clients as a closing window: the businesses that redesign now will entrench, the ones that wait will be disrupted.",
    "Arms SNIPED's sales narrative with a credible, non-hype urgency: the Between Times is the operator's opening.",
    "We have entered a unique moment in history, The Between Times, after witnessing the power of this technology and before its widespread adoption.",
    ["between-times", "adoption-gap", "urgency", "strategy"])
add(S, T, A, "systems-thinking", "Cheap prediction changes the value of everything around it",
    "When prediction gets cheap, the things that complement it (judgment, data, action) rise in value, and substitutes fall. Redesigning a system means rebuilding it around what is now cheap and what is now precious.",
    "When you automate the prediction in a client's process, deliberately upgrade the human judgment and data inputs that now matter more.",
    "Tells SNIPED where to invest in a build: not just the model, but the judgment layer and data quality that become the new bottleneck.",
    "",
    ["complements", "value-shift", "system-redesign", "systems-thinking"])
add(S, T, A, "commercial-architecture", "System solutions entrench some incumbents and disrupt others",
    "Whether AI helps or hurts a firm depends on whether it can redesign its system. Incumbents with the will to rebuild capture the gains; those who only bolt on point solutions get disrupted by those who rebuild.",
    "Target clients who can be repositioned as the disruptor in their vertical via a system redesign, not just patched.",
    "Helps SNIPED pick clients: the owner willing to redesign is the one who becomes a flagship case study.",
    "",
    ["incumbent-disruption", "redesign", "case-study", "commercial-architecture"])
add(S, T, A, "strategy", "AI is a prediction technology, not a magic technology",
    "Building on Prediction Machines, the authors insist the economic lens, not the engineering hype, predicts adoption. Economics changes slowly even as the technology races, so the framework outlasts the model of the month.",
    "Reason about AI opportunities from the economics (what got cheap, what got precious), which stays stable, rather than from the latest model release.",
    "Keeps SNIPED's strategy durable against model churn: the economic framing does not expire when a new model ships.",
    "Technologies change, but economics doesn't.",
    ["economics-lens", "durability", "anti-hype", "strategy"])
add(S, T, A, "client-application", "Friction and rules block adoption more than capability",
    "The authors show adoption stalls on regulation, coordination, and trust, not on model accuracy. The hard part of a system solution is the human and institutional rewiring around it.",
    "Scope client builds to include the rule changes, approvals, and trust-building required, because those, not the model, are where projects die.",
    "Explains why SNIPED's implementation-readiness gate (from the opportunity templates) exists: capability is rarely the blocker, readiness is.",
    "",
    ["adoption-friction", "readiness", "trust", "client-application"])
add(S, T, A, "operator-process", "Find the bottleneck the cheap prediction unlocks",
    "A system solution works by locating the constraint that cheap prediction now relieves, then rebuilding the workflow so that relief flows through. The skill is constraint-spotting, not model-tuning.",
    "Lead discovery by hunting the single constraint AI can relieve, then design the whole workflow to exploit that relief.",
    "Operationalizes SNIPED discovery: one well-chosen bottleneck per engagement beats a scattershot list of AI features.",
    "",
    ["bottleneck", "constraint", "discovery", "operator-process"])

# --- 4 · Prediction Machines · Agrawal, Gans, Goldfarb (2018) · 8 ---
S = "prediction_machines_agrawal.txt"; T = "Prediction Machines (2018)"; A = "Ajay Agrawal, Joshua Gans, Avi Goldfarb"
add(S, T, A, "strategy", "AI is a drop in the cost of prediction",
    "The foundational reframe: machine learning is not intelligence in the abstract, it is cheap prediction. When the price of anything falls, you use more of it and you use it in new places, which is exactly what is happening with prediction.",
    "Translate every AI opportunity into the question: what prediction just got cheap here, and where else can we now afford to predict?",
    "The single most useful lens SNIPED can give a client: AI as cheap prediction makes the value obvious and the hype evaporate.",
    "The drop in the cost of prediction is transforming many human activities.",
    ["cheap-prediction", "economics", "reframe", "strategy"])
add(S, T, A, "strategy", "Prediction is not decision; judgment is the complement",
    "A prediction is only an input. The decision still requires judgment about payoffs and what to do with the prediction. As prediction gets cheap, judgment becomes the scarce, valuable complement.",
    "Keep the judgment layer human and explicit; that is what the client is really paying the operator to provide.",
    "Defines the durable human role in SNIPED's deliverables: the operator supplies the judgment that the cheap prediction cannot.",
    "Prediction is not the same as decision. Making a decision requires applying judgment to a prediction.",
    ["judgment", "decision", "human-complement", "strategy"])
add(S, T, A, "systems-thinking", "When prediction is cheap, more problems become prediction problems",
    "Tasks not previously thought of as prediction (driving, translation, diagnosis) get reframed as prediction once it is cheap enough. The reframing is where the new applications come from.",
    "Audit a client's manual decisions and ask which could be recast as prediction problems now that prediction is cheap.",
    "A discovery technique for SNIPED: re-read a client's workflow looking for hidden prediction problems to automate.",
    "",
    ["reframing", "prediction-problems", "discovery", "systems-thinking"])
add(S, T, A, "operator-process", "The AI canvas: decompose a task into prediction, judgment, action, outcome",
    "The authors give a worksheet that breaks any task into its prediction, judgment, action, outcome, input, training, and feedback components. It turns a vague AI ambition into a buildable spec.",
    "Run client tasks through a prediction-judgment-action decomposition before quoting, to surface what is actually buildable.",
    "A ready-made discovery instrument that complements SNIPED's opportunity-card and business-case templates.",
    "",
    ["ai-canvas", "decomposition", "spec", "operator-process"])
add(S, T, A, "commercial-architecture", "Cheap prediction shifts where the profit sits",
    "As prediction commoditizes, profit migrates to the complements: proprietary data, the judgment layer, and control of the action. Owning a complement, not the model, is the durable business.",
    "Build the agency's durable assets around data, judgment, and workflow ownership, not around any model that will commoditize.",
    "Warns SNIPED away from model-dependency and toward owning the process, data, and relationship that retain value.",
    "",
    ["complements", "profit-migration", "moat", "commercial-architecture"])
add(S, T, A, "strategy", "More data, more prediction, more activity: the AI flywheel",
    "Better predictions attract more usage, which generates more data, which improves predictions. The loop is why early and deep beats late and broad in any single domain.",
    "Engineer a data flywheel into client builds so usage compounds into a defensible advantage over time.",
    "Commercial version of SNIPED's scene-density principle: depth compounds through a feedback loop, breadth does not.",
    "",
    ["flywheel", "data-loop", "compounding", "strategy"])
add(S, T, A, "ethics", "Prediction machines surface uncomfortable trade-offs",
    "Cheap prediction forces explicit choices about false positives versus false negatives, fairness, and who bears the cost of errors. What was hidden in human discretion becomes an explicit, auditable parameter.",
    "Make the error trade-offs explicit and let the client own them; do not bury them in the model.",
    "Aligns with SNIPED's trust posture: surfacing trade-offs honestly is itself a trust signal in the build.",
    "",
    ["trade-offs", "fairness", "error-costs", "ethics"])
add(S, T, A, "client-application", "Start where prediction is valuable and tolerance for error is high",
    "The best first AI projects are where a good-enough prediction creates clear value and mistakes are cheap. Picking the right first use case determines whether the relationship survives to a second project.",
    "Choose the client's first automation for high value and high error-tolerance, to bank an early win before harder builds.",
    "Sequencing rule for SNIPED engagements: land a safe, valuable first win, then earn the right to the system solution.",
    "",
    ["first-use-case", "sequencing", "error-tolerance", "client-application"])

# --- 5 · The Network State · Balaji Srinivasan · 7 ---
S = "the_network_state_srinivasan.txt"; T = "The Network State"; A = "Balaji Srinivasan"
add(S, T, A, "systems-thinking", "Start with a community, then crowdfund territory",
    "Srinivasan's thesis: a network state begins as a highly aligned online community with a shared moral purpose, builds an economy and internal trust, then crowdfunds physical territory and seeks recognition. Software-first, land-later.",
    "Build the aligned audience and shared belief first; physical and commercial assets follow a committed community, not the reverse.",
    "Mirrors SNIPED's build-the-scene-first logic: assemble the aligned community and mythology before scaling physical or commercial surface.",
    "A network state is a highly aligned online community with a capacity for collective action.",
    ["network-state", "community-first", "alignment", "systems-thinking"])
add(S, T, A, "strategy", "A moral innovation is the founding asset",
    "What distinguishes a network state from a mere social network is a 'one commandment', a moral innovation the broader society gets wrong and the community gets right. Shared conviction, not features, creates cohesion.",
    "Found a community on a single sharp conviction the mainstream gets wrong; conviction recruits and retains better than benefits.",
    "Underwrites SNIPED's positioning via refusal: a clear conviction about what others get wrong is the recruiting magnet.",
    "A network state is a social network with a moral innovation, a sense of national consciousness, and a recognized founder.",
    ["moral-innovation", "conviction", "positioning", "strategy"])
add(S, T, A, "systems-thinking", "The recognized founder is a feature, not a bug",
    "Srinivasan argues legitimate founder-led communities outperform leaderless ones; a recognized founder provides direction, accountability, and narrative coherence. Decentralization is a tool, not a virtue in itself.",
    "Lead from the front with a named, accountable founder voice rather than hiding behind a faceless brand.",
    "Validates SNIPED's founder-forward identity: the named operator, not an anonymous agency, carries trust and direction.",
    "",
    ["founder-led", "accountability", "narrative", "systems-thinking"])
add(S, T, A, "commercial-architecture", "Build a parallel economy on trust and aligned incentives",
    "A network state runs its own internal economy: members transact, build, and reinforce shared incentives. Economic activity inside the aligned group compounds the community's capacity for collective action.",
    "Create internal economic loops among an aligned audience (referrals, collaborations, shared tooling) rather than chasing external transactions only.",
    "Maps to SNIPED's scene-density commercial logic: a tight aligned cluster transacts internally and compounds.",
    "",
    ["parallel-economy", "aligned-incentives", "scene-density", "commercial-architecture"])
add(S, T, A, "strategy", "Sovereignty is built incrementally, not declared",
    "The path runs from community to economy to territory to recognition, each step earned. Legitimacy accrues through demonstrated capacity for collective action, not through proclamation.",
    "Earn standing through demonstrated collective wins in sequence; do not claim authority you have not built.",
    "Reinforces SNIPED's repetition-over-novelty doctrine: standing is accrued through reps, not announced.",
    "",
    ["incremental", "legitimacy", "sequencing", "strategy"])
add(S, T, A, "systems-thinking", "Technology lets small aligned groups punch far above their size",
    "The network-state argument rests on leverage: code, media, and crypto rails let a small, aligned group coordinate at a scale once reserved for nation-states. Alignment plus tooling beats headcount.",
    "Use code-and-media leverage so a small aligned team operates at a scale that headcount alone could never reach.",
    "Direct expression of SNIPED's leverage doctrine: a small operator with code and media leverage outperforms larger, unaligned teams.",
    "",
    ["leverage", "small-aligned-group", "code-and-media", "systems-thinking"])
add(S, T, A, "ethics", "Exit and build over voice and complain",
    "Srinivasan favors building parallel alternatives (exit) over fighting within failing systems (voice). The constructive response to a broken institution is to build a better one beside it.",
    "When an existing system is broken, build the alternative rather than spending energy fighting the old one.",
    "Matches SNIPED's high-agency stance: build the better system rather than litigate the broken one.",
    "",
    ["exit-vs-voice", "build-alternative", "high-agency", "ethics"])

# --- 6 · Read Write Own · Chris Dixon (2024) · 7 ---
S = "read_write_own_dixon.txt"; T = "Read Write Own (2024)"; A = "Chris Dixon"
add(S, T, A, "systems-thinking", "Three eras of the internet: read, write, own",
    "Dixon frames internet history in three eras: read (static pages), write (user-generated content on platforms), and own (networks where users hold a stake). The 'own' era is about returning value to the people who create it.",
    "Architect creator surfaces so the people producing value retain a stake, rather than renting attention from a platform.",
    "Frames SNIPED's owned-audience priority: build on surfaces you control, not ones that can revoke your reach.",
    "",
    ["read-write-own", "internet-eras", "ownership", "systems-thinking"])
add(S, T, A, "commercial-architecture", "Protocol networks versus corporate networks",
    "Dixon contrasts open protocol networks (value accrues to participants) with corporate networks (value accrues to the platform owner). Corporate networks inevitably extract from the creators who built them.",
    "Reduce dependence on extractive corporate platforms; own the protocol-like layer (your list, your site, your relationships).",
    "Underpins SNIPED's two-system platform split: rented platforms for reach, owned surfaces for durable value.",
    "",
    ["protocol-networks", "platform-risk", "ownership", "commercial-architecture"])
add(S, T, A, "strategy", "The attract-extract cycle of platforms",
    "Platforms first attract creators with generous terms, then extract once lock-in is achieved by changing the rules in their own favor. The creator who saw it coming kept an owned escape hatch.",
    "Assume any platform you build on will turn extractive; maintain an owned channel as insurance from day one.",
    "Justifies SNIPED's investment in owned surfaces even while using rented platforms for distribution.",
    "",
    ["attract-extract", "lock-in", "platform-risk", "strategy"])
add(S, T, A, "systems-thinking", "Tokens align incentives between builders and users",
    "Dixon argues ownership stakes (tokens) can align the incentives of a network's builders, users, and investors, so growth benefits participants rather than only the platform. Incentive design is the core innovation.",
    "Design incentives so that the people who grow your network share in its upside, increasing their commitment.",
    "Abstracts to SNIPED's referral and collaboration design: align incentives so participants are motivated to grow the scene.",
    "",
    ["incentive-alignment", "ownership-stake", "network-design", "systems-thinking"])
add(S, T, A, "ethics", "Centralized control of networks is a long-run risk",
    "Concentrated platform control over distribution, identity, and payments is a structural risk to anyone who builds on top. History shows the platform's interests eventually diverge from the creator's.",
    "Never let a single platform own your distribution, identity, and payments simultaneously; diversify the dependency.",
    "Reinforces SNIPED's platform-risk discipline and the case for owned identity and direct client relationships.",
    "",
    ["centralization-risk", "distribution", "diversification", "ethics"])
add(S, T, A, "strategy", "Build for the era you believe is coming",
    "Dixon's investing thesis is to back the next era before it is obvious, tolerating ridicule in the gap between vision and consensus. The asymmetric returns sit in the period of disbelief.",
    "Position the agency for where AI and ownership are going, accepting that the bet looks early before it looks obvious.",
    "Echoes SNIPED's perennial-seller and prophecy logic: build for the era arriving, not the one departing.",
    "",
    ["future-positioning", "asymmetric-bets", "prophecy", "strategy"])
add(S, T, A, "ai-tooling", "Composability: open building blocks compound innovation",
    "Open, composable software primitives let builders stack each other's work, accelerating innovation far beyond closed silos. The composable ecosystem out-innovates the walled garden.",
    "Compose client builds from interoperable primitives so each engagement reuses and extends prior work.",
    "Validates SNIPED's reusable-system approach: composable workflow primitives compound across clients.",
    "",
    ["composability", "primitives", "reuse", "ai-tooling"])

# --- 7 · Human + Machine · Daugherty & Wilson (2018) · 7 ---
S = "human_plus_machine_daugherty.txt"; T = "Human + Machine (2018)"; A = "Paul R. Daugherty, H. James Wilson"
add(S, T, A, "strategy", "The missing middle: humans and machines collaborate",
    "Daugherty and Wilson identify a 'missing middle' overlooked by the replace-or-be-replaced debate: hybrid activities where humans help machines and machines augment humans. The biggest gains live in that collaborative zone.",
    "Design for the collaborative middle: humans training, explaining, and sustaining AI while AI amplifies human reach and decision-making.",
    "This is the precise architecture of SNIPED's hybrid-operator offer: the value is in the human-machine middle, not at either pole.",
    "Human + Machine addresses the missing middle: how humans and machines can collaborate to augment, not replace, human skills.",
    ["missing-middle", "collaboration", "hybrid-operator", "strategy"])
add(S, T, A, "operator-process", "Humans train, explain, and sustain machines",
    "On the human-helps-machine side, people perform three roles: training models, explaining their outputs to stakeholders, and sustaining responsible operation. These roles are durable jobs created by AI.",
    "Bundle training, explainability, and ongoing stewardship into the client offer as recurring, human-delivered services.",
    "Defines recurring revenue for SNIPED beyond the build: the train-explain-sustain layer is an ongoing retainer.",
    "",
    ["train-explain-sustain", "recurring", "stewardship", "operator-process"])
add(S, T, A, "client-application", "Machines amplify, interact, and embody human work",
    "On the machine-helps-human side, AI amplifies cognition, enables natural interaction, and embodies capability in physical or digital agents. The human gets superhuman reach without losing the human role.",
    "Frame deliverables as amplifying the owner's existing strengths, so the client experiences AI as more of themselves, not a replacement.",
    "Shapes SNIPED's client experience: the automation makes the owner feel more capable, which is the emotional sale.",
    "",
    ["amplify", "interact", "client-experience", "client-application"])
add(S, T, A, "operator-process", "MELDS: reimagine processes, do not pave the cow path",
    "Their MELDS framework (Mindset, Experimentation, Leadership, Data, Skills) insists you reimagine a process around AI rather than bolt AI onto the old workflow. Automating a broken process just makes it fail faster.",
    "Reimagine the client's process before automating it; never automate the existing broken steps as-is.",
    "Echoes SNIPED's system-solution discipline and the youtube-skool process-mapping caution: fix the process, then automate.",
    "",
    ["melds", "reimagine-process", "anti-cow-path", "operator-process"])
add(S, T, A, "commercial-architecture", "Process reinvention captures exponential gains",
    "Incremental AI bolt-ons yield incremental returns; reinventing the process around AI yields step-change improvements. The companies that rethink, not retrofit, capture the outsized gains.",
    "Pitch the high-value engagement as process reinvention with step-change ROI, not as a tool installation.",
    "Distinguishes SNIPED's premium system engagements from commodity point-solution work in commercial terms.",
    "",
    ["process-reinvention", "step-change", "premium", "commercial-architecture"])
add(S, T, A, "ethics", "Responsible AI is a design requirement, not an afterthought",
    "The sustain role includes building fairness, transparency, and safety into systems from the start. Trust is engineered in, and it is what lets an organization scale AI without backlash.",
    "Build trust signals (transparency, human oversight, clear limits) into the deliverable as a core feature.",
    "Aligns with SNIPED's trust-equation discipline: low self-orientation and visible reliability are designed in, not added later.",
    "",
    ["responsible-ai", "trust", "transparency", "ethics"])
add(S, T, A, "ai-tooling", "Fusion skills: working in the human-machine middle is learnable",
    "The authors define new 'fusion skills' (such as intelligent interrogation and bot-based empowerment) for working effectively with AI. These are teachable competencies, not innate talents.",
    "Develop and teach concrete AI-collaboration skills as part of the operator's craft and the client handoff.",
    "Supports SNIPED's skill-stack and prompt-craft lanes: fusion skills are the trainable core of operator value.",
    "",
    ["fusion-skills", "human-machine", "skill-stack", "ai-tooling"])

# --- 8 · The Second Machine Age · Brynjolfsson & McAfee (2014) · 7 ---
S = "the_second_machine_age_brynjolfsson.txt"; T = "The Second Machine Age (2014)"; A = "Erik Brynjolfsson, Andrew McAfee"
add(S, T, A, "systems-thinking", "The second machine age automates cognition",
    "Where the first machine age (steam) augmented muscle, the second augments mind. Digital technologies now do cognitive work, and they improve exponentially, which is why progress feels sudden.",
    "Treat cognitive automation as the defining shift; the work being automated now is thinking work, which is most office work.",
    "Frames the macro backdrop for SNIPED's AI-agency thesis: cognitive automation is the wave the agency rides.",
    "",
    ["second-machine-age", "cognitive-automation", "exponential", "systems-thinking"])
add(S, T, A, "strategy", "Exponential, digital, and recombinant growth",
    "Three forces drive the era: exponential improvement (Moore's law), digitization (zero-cost copies), and recombinant innovation (new ideas as combinations of existing ones). Together they compound.",
    "Build by recombining existing tools and prior work into new offers, since recombination is the cheapest path to novelty.",
    "Validates SNIPED's reuse-and-recombine method: new client offers assembled from existing workflow primitives.",
    "",
    ["recombinant-innovation", "digitization", "exponential", "strategy"])
add(S, T, A, "ai-tooling", "Digital goods are free, perfect, and instant to copy",
    "Once something is digitized, copying it costs nothing, loses no quality, and happens instantly. This economics is why software businesses scale unlike physical ones.",
    "Productize the agency's repeatable work into digital assets that copy at zero marginal cost across clients.",
    "Points SNIPED toward productized, reusable digital deliverables rather than purely bespoke one-off labor.",
    "",
    ["zero-marginal-cost", "digital-goods", "productization", "ai-tooling"])
add(S, T, A, "ethics", "The bounty and the spread",
    "The era produces a bounty (more abundance and value) but also a spread (rising inequality between those who own and build technology and those displaced by it). Both happen at once.",
    "Position to capture the bounty by being on the builder side, while framing client value as broadly shared capacity gains.",
    "Names the stakes of SNIPED's builder positioning and informs how the work is framed to clients and audience.",
    "",
    ["bounty-and-spread", "inequality", "builder", "ethics"])
add(S, T, A, "strategy", "Race with the machines, not against them",
    "The prescription is to compete alongside machines, finding the tasks where human plus machine beats either alone. The freestyle-chess example shows good process plus machine beating a grandmaster or a supercomputer.",
    "Pair human judgment with machine output in a deliberate process; the human-plus-machine team is the winning unit.",
    "Reinforces SNIPED's hybrid-operator architecture with the canonical freestyle-chess evidence.",
    "",
    ["race-with-machines", "freestyle-chess", "hybrid-operator", "strategy"])
add(S, T, A, "commercial-architecture", "Winner-take-most markets reward the best, not the average",
    "Digital economics produce superstar, winner-take-most markets where small quality differences yield enormous reward differences. Being clearly the best in a niche pays disproportionately.",
    "Aim to be unambiguously the best in a narrow niche, where digital economics concentrate the reward.",
    "Commercial case for SNIPED's depth-and-excellence posture: in winner-take-most niches, being the best operator captures the market.",
    "",
    ["winner-take-most", "superstar-economics", "excellence", "commercial-architecture"])
add(S, T, A, "operator-process", "Ideation, big-picture, and complex communication remain human",
    "The authors identify the durable human strengths: novel idea generation, broad pattern synthesis, and complex interpersonal communication. These are where humans should concentrate.",
    "Concentrate the operator's hours on ideation, synthesis, and communication; automate the rest.",
    "A staffing rule for SNIPED: the human spends time only where humans still win, and the build covers everything else.",
    "",
    ["human-strengths", "ideation", "communication", "operator-process"])

# --- 9 · Co-Intelligence · Ethan Mollick (2024) · 9 ---
S = "co_intelligence_mollick.txt"; T = "Co-Intelligence (2024)"; A = "Ethan Mollick"
add(S, T, A, "ai-tooling", "Principle 1: always invite AI to the table",
    "Mollick's first rule is to use AI for everything you legally and ethically can, because you only learn its shape by using it constantly. Treat it as a default collaborator on every task.",
    "Default to bringing AI into every workflow step; the habit of constant use is how the operator finds the leverage.",
    "Sets SNIPED's working posture and the case studies' raw material: relentless hands-on use produces the operator's edge.",
    "Principle 1: Always invite AI to the table.",
    ["invite-ai", "default-collaborator", "habit", "ai-tooling"])
add(S, T, A, "ai-tooling", "The Jagged Frontier of AI capability",
    "AI capability is a jagged, invisible wall: some surprisingly hard tasks are easy for it and some easy-seeming tasks are hard. You cannot predict the shape from the outside; you map it by experimenting.",
    "Map each tool's jagged frontier empirically before trusting it on client work; never assume capability from task difficulty.",
    "Disciplines SNIPED's tool selection: test where each model is strong and weak rather than assuming, protecting deliverable quality.",
    "We call the Jagged Frontier of AI. Everything inside the wall can be done by the AI; everything outside is hard for the AI to do.",
    ["jagged-frontier", "capability-mapping", "experimentation", "ai-tooling"])
add(S, T, A, "operator-process", "Principle: be the human in the loop",
    "Because AI is unreliable at the edges and confidently wrong, a human must stay in the loop to catch errors and own the outcome. The human provides the accountability the model cannot.",
    "Keep a human checkpoint on every AI output that reaches a client; the operator owns correctness, not the model.",
    "Codifies SNIPED's human-approval gate as a quality and trust mechanism, not just a safety formality.",
    "",
    ["human-in-the-loop", "accountability", "quality-gate", "operator-process"])
add(S, T, A, "prompt-engineering", "Treat AI like a person (but tell it what kind of person)",
    "Mollick's heuristic is to interact with AI as if it were a capable but context-free collaborator: give it a persona, context, and clear intent. The persona framing reliably improves output.",
    "Open client-facing prompts by assigning a clear role and context, the cheapest reliable quality lever.",
    "Reinforces PROMPT_TEMPLATES_DEEP's role-and-context craft with a memorable working heuristic for the team.",
    "Treat AI like a person, but tell it what kind of person it is.",
    ["persona", "context", "prompt-heuristic", "prompt-engineering"])
add(S, T, A, "operator-process", "Assume this is the worst AI you will ever use",
    "Mollick's framing is to treat today's model as the floor, not the ceiling: it will only get better, so build habits and systems for where it is going. Plan around improvement, not the current limitation.",
    "Design workflows for the trajectory of capability, not today's snapshot, so the system improves as models do.",
    "Future-proofs SNIPED's builds: architect for the rising tide so deliverables get better as models improve.",
    "Today's AI is the worst you will ever use.",
    ["trajectory", "future-proofing", "improvement", "operator-process"])
add(S, T, A, "strategy", "The centaur and cyborg ways of working",
    "Mollick distinguishes centaur work (a clean division of labor between human and AI) from cyborg work (tightly interwoven turns). Both are deliberate collaboration patterns superior to either ignoring or fully delegating to AI.",
    "Choose centaur or cyborg working modes deliberately per task, rather than defaulting to all-human or all-AI.",
    "Gives SNIPED a vocabulary for designing how operators and AI interleave on each deliverable.",
    "",
    ["centaur", "cyborg", "collaboration-modes", "strategy"])
add(S, T, A, "ethics", "AI is unreliable, biased, and confidently wrong",
    "Mollick is clear-eyed about hallucination, bias, and the persuasive confidence of wrong answers. The risks are real and require verification habits, not blind trust.",
    "Institutionalize verification of AI claims before they reach a client; confident output is not correct output.",
    "Anchors SNIPED's quality discipline and protects the trust relationship from a confident-but-wrong failure.",
    "",
    ["hallucination", "bias", "verification", "ethics"])
add(S, T, A, "ai-tooling", "AI as a co-worker, tutor, coach, and creative partner",
    "Mollick catalogs AI's practical roles: drafting, tutoring, coaching, brainstorming, and acting as an always-available expert. The value compounds when it fills several roles at once for a small operator.",
    "Deploy AI across multiple operator roles (draft, critique, tutor, brainstorm) to multiply a small team's output.",
    "Directly serves SNIPED's lean-team leverage: one operator plus AI covers roles that once needed several people.",
    "",
    ["co-worker", "multi-role", "leverage", "ai-tooling"])
add(S, T, A, "operator-process", "Expertise still matters most for judging AI output",
    "The people who get the most from AI are domain experts who can judge, correct, and direct it. AI raises the floor for novices but raises the ceiling most for experts.",
    "Pair AI with genuine domain expertise; the operator's expertise is what converts raw AI output into trusted work.",
    "Explains why SNIPED's craft and judgment investment is not made obsolete by AI but made more valuable by it.",
    "",
    ["expertise", "judgment", "ceiling-raiser", "operator-process"])

# --- 10 · Competing in the Age of AI · Lakhani & Iansiti (2020) · 8 ---
S = "competing_in_the_age_of_ai_iansiti.txt"; T = "Competing in the Age of AI (2020)"; A = "Karim R. Lakhani, Marco Iansiti"
add(S, T, A, "commercial-architecture", "The AI factory turns data into decisions at scale",
    "The authors describe the 'AI factory': a systematic pipeline that turns data into predictions and decisions, run as core infrastructure. Digital firms scale because their decision-making is software, not headcount.",
    "Build the client a small AI factory (data in, decisions out) rather than a one-off automation, so decisions scale without staff.",
    "Elevates SNIPED's builds from point automations to decision infrastructure, the higher-value commercial frame.",
    "",
    ["ai-factory", "decision-pipeline", "infrastructure", "commercial-architecture"])
add(S, T, A, "strategy", "Digital operating models scale without diminishing returns",
    "Traditional firms hit bottlenecks as they grow because value is delivered by people; digital operating models deliver value through software, so they scale, scope, and learn without the usual constraints.",
    "Move the client's value delivery from human-bound to software-bound wherever possible, removing the growth ceiling.",
    "Defines the transformation SNIPED sells: shifting delivery from headcount-bound to software-bound.",
    "",
    ["digital-operating-model", "scalability", "no-diminishing-returns", "strategy"])
add(S, T, A, "systems-thinking", "Software-driven firms scale, scope, and learn differently",
    "The three classic constraints (scale, scope, learning) bind people-based firms but release for software-based ones: one platform can serve more, span more domains, and improve from every interaction.",
    "Architect for scale, scope, and learning simultaneously, since a software core lets all three compound together.",
    "Gives SNIPED the diagnostic for which client functions to convert to software first: those choking on scale, scope, or learning.",
    "",
    ["scale-scope-learning", "constraints", "software-core", "systems-thinking"])
add(S, T, A, "commercial-architecture", "The collision of operating models",
    "When digital operating models collide with traditional ones, the digital model usually wins because its economics are structurally superior. Incumbents must rebuild their operating model, not just digitize the edges.",
    "Help an incumbent client rebuild its operating model before a digital-native competitor collides with it.",
    "Frames SNIPED's urgency narrative for incumbent clients in the same terms as Power and Prediction's system solutions.",
    "",
    ["operating-model-collision", "incumbent-risk", "rebuild", "commercial-architecture"])
add(S, T, A, "ethics", "Concentrated AI power demands new responsibility",
    "The authors warn that AI-driven firms concentrate economic power and create ethical hazards (bias, privacy, systemic risk) that leaders must govern deliberately. Capability without governance is dangerous at scale.",
    "Build governance and ethical guardrails into scaled client systems as a leadership requirement, not a compliance afterthought.",
    "Aligns SNIPED's trust posture with the governance expectations of larger, scaled engagements.",
    "",
    ["concentration", "governance", "responsibility", "ethics"])
add(S, T, A, "strategy", "Strategy becomes about networks, data, and learning loops",
    "Competitive advantage shifts from traditional positioning to controlling network connections, data flows, and learning loops. The firm with the best loops, not the best products alone, wins.",
    "Compete for the client on the strength of their data and learning loops, not just the features you ship.",
    "Connects to Prediction Machines' flywheel and SNIPED's compounding-depth logic at the firm-strategy level.",
    "",
    ["network-effects", "learning-loops", "data-strategy", "strategy"])
add(S, T, A, "operator-process", "Agile, data-driven leadership beats hierarchical control",
    "Running an AI-centric firm requires leaders who experiment, decide from data, and remove organizational friction rather than command through hierarchy. The operating culture is as important as the technology.",
    "Coach client leadership toward experiment-and-measure habits; the culture change is part of the deliverable.",
    "Extends SNIPED's role beyond the build into operating-discipline coaching, a stickier relationship.",
    "",
    ["agile-leadership", "data-driven", "culture", "operator-process"])
add(S, T, A, "client-application", "Start the AI factory small and let it compound",
    "The authors advise beginning with a focused data-to-decision loop and expanding as it proves value, rather than attempting an enterprise-wide overhaul at once. The factory grows from a working seed.",
    "Deliver a single working data-to-decision loop first, then expand its scope as trust and results accumulate.",
    "Sequencing guidance for SNIPED's larger engagements: seed one loop, prove it, then widen.",
    "",
    ["seed-and-expand", "data-to-decision", "sequencing", "client-application"])

# --- 11 · Life 3.0 · Max Tegmark (2017) · 8 ---
S = "life_3_0_tegmark.txt"; T = "Life 3.0 (2017)"; A = "Max Tegmark"
add(S, T, A, "systems-thinking", "Life 1.0, 2.0, 3.0: hardware and software you can redesign",
    "Tegmark classifies life by what it can redesign: 1.0 (biology, fixed hardware and software), 2.0 (humans, fixed hardware but learned software, like culture and skills), 3.0 (a hypothetical future life that redesigns both).",
    "Locate yourself as Life 2.0: you cannot change your hardware but you can continuously rewrite your software (skills, mental models, systems).",
    "Reframes SNIPED's self-upgrade and mindset-as-software thread (PERSONAL_OPERATING_CODE) in Tegmark's vocabulary.",
    "Life 1.0 cannot redesign its hardware or software; Life 2.0 can redesign its software.",
    ["life-1-2-3", "self-redesign", "software-of-the-self", "systems-thinking"])
add(S, T, A, "ethics", "Intelligence is substrate-independent",
    "Tegmark argues intelligence is about information processing, not the matter doing it, so it can run on biological or digital substrates. This is why machine intelligence is possible in principle.",
    "Reason about capability in terms of information processing, not the medium, when judging what AI can take on.",
    "Grounds SNIPED's clear-eyed view of AI capability without mysticism, useful for honest client conversations.",
    "",
    ["substrate-independence", "intelligence", "information", "ethics"])
add(S, T, A, "ethics", "Align powerful systems with human goals before scaling them",
    "The book's central safety concern is alignment: ensuring advanced AI pursues goals compatible with human values. Misalignment, not malice, is the danger as capability grows.",
    "Define the intended goal and guardrails of any automation explicitly, so the system optimizes what the client actually wants.",
    "Maps the alignment idea down to SNIPED scale: a misaligned automation optimizes the wrong metric and erodes trust.",
    "",
    ["alignment", "goal-specification", "safety", "ethics"])
add(S, T, A, "strategy", "Think in scenarios, not single predictions, about the future",
    "Tegmark lays out a wide range of AI futures rather than one forecast, arguing the responsible move is to consider the space of outcomes and steer. Certainty about the future is the mistake.",
    "Plan the agency and client bets across a range of AI scenarios rather than betting everything on one forecast.",
    "Supports SNIPED's constraint-audit and scenario thinking over single-point prediction.",
    "",
    ["scenario-thinking", "futures", "steering", "strategy"])
add(S, T, A, "ethics", "Keep humans meaningfully in control",
    "A recurring theme is preserving meaningful human control and agency as systems get more capable. The goal is technology that empowers human choice rather than removing it.",
    "Design automations that expand the owner's control and choices, never ones that quietly remove their agency.",
    "Reinforces the SNIPED client-experience principle: the owner should feel more in command, not displaced.",
    "",
    ["human-control", "agency", "empowerment", "ethics"])
add(S, T, A, "systems-thinking", "Goals, not capabilities, determine outcomes",
    "Tegmark stresses that a system's objective function drives its behavior; a highly capable system with a poorly specified goal produces bad outcomes efficiently. What you measure is what you get, at scale.",
    "Spend disproportionate care specifying the objective of an automation, because capability amplifies whatever goal you set.",
    "Sharpens SNIPED's metric discipline: define the right success metric before building, since the system will maximize it literally.",
    "",
    ["objective-function", "goals", "metric-discipline", "systems-thinking"])
add(S, T, A, "strategy", "The window to set norms is before, not after, capability arrives",
    "Tegmark argues the time to establish safety norms and governance is in advance of the capability, because retrofitting control onto a deployed system is far harder. Proactive beats reactive.",
    "Establish a client's usage norms and guardrails before deploying an automation, not after an incident.",
    "Connects to SNIPED's operating-locks discipline: set the bright lines before the capability is live.",
    "",
    ["proactive-norms", "governance", "operating-locks", "strategy"])
add(S, T, A, "meta-doctrine", "Curiosity plus responsibility is the mature stance on AI",
    "Tegmark models a posture that is neither doom nor hype: deep engagement with the technology paired with serious responsibility for its direction. The point is to participate in steering, not to spectate.",
    "Hold the curious-but-responsible stance publicly: neither AI-doomer nor AI-hype, which is itself a trust signal.",
    "Defines SNIPED's public AI voice: hybrid-operator realism that is credible precisely because it is neither camp.",
    "",
    ["curiosity-and-responsibility", "stance", "credibility", "meta-doctrine"])

# --- 12 · The Coming Wave · Suleyman & Bhaskar (2023) · 8 ---
S = "the_coming_wave_suleyman.txt"; T = "The Coming Wave (2023)"; A = "Mustafa Suleyman, Michael Bhaskar"
add(S, T, A, "systems-thinking", "The coming wave: AI and synthetic biology arriving together",
    "Suleyman argues a wave of general-purpose technologies (AI foremost) is arriving with unprecedented speed, asymmetry, and autonomy. These technologies diffuse faster and more widely than any before.",
    "Plan for fast, broad diffusion: assume the capabilities you use today are about to be everywhere, so durable advantage is elsewhere.",
    "Sets realistic expectations for SNIPED: tool access commoditizes quickly, so the moat is judgment, taste, and relationship.",
    "",
    ["coming-wave", "diffusion", "general-purpose-tech", "systems-thinking"])
add(S, T, A, "ethics", "The containment problem",
    "The book's central problem is containment: how to keep powerful, proliferating technologies under meaningful control. Suleyman argues containment is extremely hard but abandoning it is not an option.",
    "Treat control and guardrails as a first-class design constraint, since uncontained capability is a liability not an asset.",
    "Frames the responsible-builder posture SNIPED takes toward the automations it deploys.",
    "It explores the existential dangers that AI and biotechnology pose, and offers practical solutions for how we can contain the threat.",
    ["containment", "control", "responsible-builder", "ethics"])
add(S, T, A, "strategy", "Asymmetry: small actors wield outsized power",
    "A defining feature of the wave is asymmetry: small groups and individuals gain capabilities once reserved for states and large corporations. Leverage flows to the few who master the tools.",
    "Exploit the asymmetry deliberately: a small expert operator can now deliver what once required a large firm.",
    "Direct validation of SNIPED's company-of-one leverage thesis: the wave hands disproportionate power to the small and skilled.",
    "",
    ["asymmetry", "small-actor-leverage", "company-of-one", "strategy"])
add(S, T, A, "systems-thinking", "Hyper-evolution: capability compounds faster than institutions adapt",
    "Suleyman describes technologies improving and combining at a pace that outstrips regulation, organizations, and norms. The adaptation gap is itself the source of both opportunity and risk.",
    "Position in the gap between capability and institutional adaptation, where the agency's speed is an advantage.",
    "Explains where SNIPED's nimbleness pays: between what is now possible and what institutions have caught up to.",
    "",
    ["hyper-evolution", "adaptation-gap", "speed", "systems-thinking"])
add(S, T, A, "ethics", "Pessimism aversion blinds people to real risks",
    "Suleyman names 'pessimism aversion': the tendency of smart people to dismiss dire possibilities because they are unpleasant to consider. Honest risk assessment requires resisting that reflex.",
    "Assess automation risks honestly even when inconvenient; naming the downside is part of trustworthy advising.",
    "Reinforces SNIPED's honest-broker trust posture: surfacing real risks builds more trust than reflexive optimism.",
    "",
    ["pessimism-aversion", "honest-risk", "trust", "ethics"])
add(S, T, A, "commercial-architecture", "General-purpose technologies reshape every industry",
    "Like electricity and the internet, the wave's technologies are general-purpose: they touch every sector rather than one. The implication is that no industry is outside the agency's potential market.",
    "Treat every vertical as an addressable market, then choose by edge and density rather than by whether AI applies.",
    "Confirms SNIPED's market is bounded by chosen focus, not by where AI is relevant, since AI is relevant everywhere.",
    "",
    ["general-purpose", "every-industry", "market-scope", "commercial-architecture"])
add(S, T, A, "strategy", "Narrow paths between catastrophe and stagnation",
    "Suleyman frames the goal as steering a narrow path between uncontained catastrophe and overcautious stagnation. Both extremes fail; deliberate, balanced steering is the only viable route.",
    "Advise clients toward deliberate adoption that is neither reckless nor frozen, the same narrow path at business scale.",
    "Mirrors SNIPED's restraint-with-momentum operating style: move decisively but within deliberate guardrails.",
    "",
    ["narrow-path", "balance", "steering", "strategy"])
add(S, T, A, "meta-doctrine", "The builder has a duty to think about consequences",
    "As a leading AI builder, Suleyman insists practitioners cannot outsource responsibility for what they build. The person closest to the capability carries the obligation to consider its effects.",
    "Own responsibility for the downstream effects of what you build for clients; do not hide behind the tool.",
    "Defines the ethical spine of SNIPED's builder identity, consistent with its trust and lineage doctrines.",
    "",
    ["builder-responsibility", "consequences", "ethics-of-building", "meta-doctrine"])

# ============================ CLUSTER B · AI Edge course + operator/agency docs ============================

# --- 13 · Finding Your Edge.pdf · The AI Edge · 4 ---
S = "finding_your_edge.txt"; T = "Finding Your Edge"; A = "The AI Edge"
add(S, T, A, "operator-process", "Find your edge by inventorying what you already have",
    "The assessment forces an honest inventory of real advantages (business access, experience, network, skills, interests) rather than chasing a market that sounds good. The edge is found, not invented.",
    "Before choosing a niche, inventory genuine existing advantages; build the venture on real edges, not aspirational ones.",
    "Operationalizes the find-your-edge backwards approach for SNIPED's own ICP selection and for client positioning work.",
    "The goal isn't to create advantages that don't exist, but to find the genuine ones you already have.",
    ["find-your-edge", "advantage-inventory", "niche-selection", "operator-process"])
add(S, T, A, "strategy", "Rank advantages: ownership beats experience beats network beats interest",
    "The worksheet ranks advantage types from strongest to weakest: owning or controlling a business, deep experience plus network, experience alone, network alone, and finally raw interest. Test-and-implement access is the top advantage.",
    "Weight niche decisions toward the strongest advantage class you actually hold, and discount mere interest.",
    "Gives SNIPED a ranked framework for evaluating which verticals it (and clients) can credibly win.",
    "",
    ["advantage-hierarchy", "ownership", "prioritization", "strategy"])
add(S, T, A, "operator-process", "Reality-check every advantage against a paying market",
    "Each claimed advantage is tested against four questions: a specific expensive problem, people already paying for solutions, reachable decision makers, and a growing market. An advantage that fails these is not a business.",
    "Validate any niche against expensive-problem, paying-customers, reachable-buyers, and growing-market before committing.",
    "A four-gate qualification that complements SNIPED's opportunity-readiness templates at the market-selection stage.",
    "",
    ["reality-check", "market-validation", "qualification", "operator-process"])
add(S, T, A, "meta-doctrine", "It is fine to stay general until a real edge appears",
    "The worksheet ends by legitimizing patience: forcing a niche that does not really exist is worse than honestly staying broad while you find your real opportunity. Honesty about the absence of an edge is itself the discipline.",
    "Do not manufacture a false edge; stay broad and keep searching until a genuine advantage is identifiable.",
    "Reinforces SNIPED's repetition-over-novelty and honesty discipline: do not force a position you have not earned.",
    "There's nothing wrong with not having a clear niche yet. It's better to be honest than to force something that isn't there.",
    ["patience", "honesty", "anti-forcing", "meta-doctrine"])

# --- 14 · COURSE WORK 1 thru 2.docx · The AI Edge · 5 ---
S = "course_work_1_thru_2.txt"; T = "AI Edge Course Work 1-2"; A = "The AI Edge"
add(S, T, A, "strategy", "The implementation gap is the billion-dollar opportunity",
    "The masterclass argues that AI capability is now near-universal but implementation is not, creating a large gap between businesses that could use AI and those that actually have. That gap is the agency's market.",
    "Sell implementation, not access: clients can already reach the models, what they lack is the working build.",
    "States SNIPED's core commercial thesis plainly: the money is in closing the implementation gap, not in AI access.",
    "",
    ["implementation-gap", "opportunity", "agency-thesis", "strategy"])
add(S, T, A, "commercial-architecture", "Democratized AI lets small operators serve enterprise-grade work",
    "The course frames AI as democratizing capabilities once reserved for large consultancies, letting solo operators and small agencies deliver work that previously required a Deloitte-scale firm.",
    "Position the small agency as delivering enterprise-grade outcomes at small-business speed and price.",
    "Backs SNIPED's company-of-one positioning: one operator plus AI competes with far larger firms.",
    "",
    ["democratization", "small-vs-enterprise", "positioning", "commercial-architecture"])
add(S, T, A, "strategy", "The next 12 to 24 months are the critical adoption window",
    "The masterclass stresses urgency: the current window, before AI implementation becomes table stakes, is when an operator can establish a position. The window parallels websites going from novel to mandatory.",
    "Move now to establish position; the window where being early matters is measured in months, not years.",
    "Gives SNIPED's outreach a credible, non-hype urgency line grounded in the historical adoption-curve parallel.",
    "",
    ["adoption-window", "urgency", "timing", "strategy"])
add(S, T, A, "operator-process", "Be data-driven, not hype-driven, about the market",
    "The course repeatedly insists on grounding claims in real data (market sizes, saturation rates) rather than the inflated promises common in the AI space. Credibility comes from honest numbers.",
    "Quote real market data in client conversations and avoid the inflated income claims common in the space.",
    "Distinguishes SNIPED's credible, data-grounded sales voice from the hype-merchant pattern it explicitly rejects.",
    "",
    ["data-driven", "anti-hype", "credibility", "operator-process"])
add(S, T, A, "client-application", "Run a reality check before committing to the path",
    "Module 1 ends with an honest reality check on time, money, and effort required, so the would-be operator decides with eyes open. The course front-loads the difficulty rather than hiding it.",
    "Front-load the honest cost and effort of an engagement so the client commits with realistic expectations.",
    "Matches SNIPED's expectation-setting and readiness discipline: an honest reality check protects the relationship.",
    "",
    ["reality-check", "expectation-setting", "readiness", "client-application"])

# --- 15 · AI CHANGED EVERYTHING.docx · AlphaGo case study · 4 ---
S = "ai_changed_everything.txt"; T = "AI Changed Everything"; A = "SNIPED (operator-authored)"
add(S, T, A, "ai-tooling", "The AlphaGo milestone: machines reached intuition",
    "The transcript documents the AlphaGo moment, when a system mastered Go, a game long thought to require human intuition, by learning from raw experience rather than hand-coded rules. It marked AI crossing into territory assumed to be uniquely human.",
    "Recognize that the capability frontier has already crossed into intuitive, creative-seeming domains; do not underestimate what AI can attempt.",
    "Grounds SNIPED's AI-changed-everything narrative in a concrete, credible milestone rather than vague hype.",
    "It's like putting your hand on the third rail of the universe.",
    ["alphago", "milestone", "intuition", "ai-tooling"])
add(S, T, A, "systems-thinking", "Learning from raw experience beats hand-coded rules",
    "AlphaGo and its successors learned by self-play from minimal priors, surpassing systems built on encoded human expertise. The lesson: systems that learn from data and feedback outgrow systems that encode fixed rules.",
    "Prefer client systems that learn and improve from feedback over brittle, hand-coded rule sets where feasible.",
    "Connects to Prediction Machines and the AI-factory idea: learning loops, not fixed rules, are the durable design.",
    "The agent system has to learn everything for itself, just from the raw pixels.",
    ["self-play", "learning-systems", "feedback", "systems-thinking"])
add(S, T, A, "strategy", "Move 37: machines can produce genuinely creative moves",
    "The famous move-37 moment showed a machine making a move no human would play, later judged brilliant. It demonstrated that AI can expand, not just imitate, the space of good ideas.",
    "Use AI to generate options outside your habitual range, then apply human judgment to select among them.",
    "Reinforces SNIPED's use of AI for world-construction and idea generation while keeping human selection.",
    "",
    ["move-37", "machine-creativity", "idea-generation", "strategy"])
add(S, T, A, "meta-doctrine", "Understanding what understanding is",
    "The transcript frames the deeper stakes: the pursuit of AI is partly a pursuit of understanding intelligence itself. Engaging with AI is engaging with the question of what thinking is.",
    "Hold the long view that working with AI is also a way of sharpening how you yourself think and decide.",
    "Aligns with SNIPED's intellectual-artist frame: the tool is also a mirror for the operator's own thinking.",
    "They want to understand what understanding is. And maybe that is truly what it means to be human.",
    ["understanding", "intelligence", "intellectual-artist", "meta-doctrine"])

# --- 16 · sniped_os_knowledge_dump.docx · Part 6 + meta · 6 ---
S = "sniped_os_knowledge_dump.txt"; T = "SNIPED OS Knowledge Dump"; A = "SNIPED (operator-authored)"
add(S, T, A, "operator-process", "Speak to owners about outcomes, not tools",
    "The agency masterclass insists business owners do not care whether the stack is VAPI or Retell; they care that the phone is answered 24/7 and meetings get booked. Sell the outcome, keep the tooling invisible.",
    "Frame every offer in the owner's outcome (revenue, recovered hours, answered calls), never in the underlying tools.",
    "Codifies SNIPED's sales language: outcome-first framing that the B2B positioning lane already established.",
    "Speak to business owners about outcomes, not tools.",
    ["outcomes-not-tools", "sales-framing", "owner-language", "operator-process"])
add(S, T, A, "commercial-architecture", "Bottom-line automation is where the spend sits",
    "The dump distinguishes top-line (new revenue) from bottom-line (cost reduction via back-office and ops automation), noting most addressable spend is bottom-line. Cost recovery is the easier first sale.",
    "Lead with bottom-line cost-recovery automations, which are easier to justify, then expand to top-line later.",
    "Sequences SNIPED's offer ladder: start with provable cost recovery, earn the right to revenue-growth work.",
    "",
    ["top-line-vs-bottom-line", "cost-recovery", "offer-ladder", "commercial-architecture"])
add(S, T, A, "client-application", "A proper ICP has four components",
    "The masterclass defines a real ICP as firmographics, a specific recurring scenario, a specific expensive problem, and a concrete way to reach them. Broad or size-only ICPs fail.",
    "Define every target ICP across all four components; reject vague or size-only definitions.",
    "Directly upgrades SNIPED's targeting and feeds the opportunity-card and outreach lanes with a sharper ICP.",
    "Proper ICP has FOUR components: firmographics, specific scenario, specific expensive problem, how to reach them.",
    ["icp", "four-components", "targeting", "client-application"])
add(S, T, A, "commercial-architecture", "The one-liner pitch formula",
    "The dump gives a reusable pitch formula: help a specific target who struggles with a specific expensive problem achieve a result. The conversational version is even sharper than the formal one.",
    "Write the one-liner as help-[target]-who-struggle-with-[expensive-problem]-[result], then test it on three strangers.",
    "A ready copy template for SNIPED's hero lines, LinkedIn headlines, and outreach openers.",
    "We help insurance agencies who get slammed during renewal season.",
    ["one-liner", "pitch-formula", "copy-template", "commercial-architecture"])
add(S, T, A, "operator-process", "SMART goals cascade from 12-month vision to weekly actions",
    "The masterclass uses SMART goals plus a hierarchy: a vivid 12-month vision, quarterly milestones, monthly objectives, and weekly actions, with a traceable line from this week's tasks up to the vision.",
    "Maintain a traceable line from weekly tasks to the 12-month vision; if a task does not ladder up, cut it.",
    "Mirrors SNIPED's Direction Stack and MVMM cadence: vision cascaded into checkable weekly reps.",
    "A goal is a dream with a deadline.",
    ["smart-goals", "goal-hierarchy", "cadence", "operator-process"])
add(S, T, A, "strategy", "Start lean and develop critical thinking, sales, and resilience",
    "The dump argues the agency can start under $100 a month and that the decisive skills are critical thinking, problem solving, communication, sales, and resilience, not capital. Discipline beats motivation; expect heavy rejection.",
    "Start lean and invest in the durable skills (critical thinking, sales, resilience) rather than tools or spend.",
    "Reinforces SNIPED's lean-leverage operating constraint and the high-agency, rejection-tolerant founder posture.",
    "Discipline beats motivation. Can you keep going without immediate results?",
    ["lean-start", "durable-skills", "resilience", "strategy"])

# --- 17 · youtube skool doc.docx · transcript collection · 6 ---
S = "youtube_skool_doc.txt"; T = "YouTube / Skool Doc"; A = "SNIPED (operator-authored)"
add(S, T, A, "ai-tooling", "Vibe-coding apps from an idea with free AI studios",
    "One transcript walks through building and deploying a working web app from a plain-language idea using a free AI studio, in three steps: idea, build, deploy to a public URL. The barrier to shipping software has collapsed.",
    "Prototype client-facing apps directly from a described idea using free or cheap AI build tools before committing real spend.",
    "Lowers SNIPED's cost to demo a custom build, turning a sales conversation into a working prototype quickly.",
    "Start free, ship faster, and then upgrade as you need.",
    ["vibe-coding", "ai-studio", "rapid-prototype", "ai-tooling"])
add(S, T, A, "strategy", "Why 95% of AI projects fail: the off-the-shelf trap",
    "A transcript summarizing an MIT-style finding argues most AI projects fail because generic off-the-shelf tools do not fit the specific process. Custom-fit builds, matched to a real workflow, are what succeed.",
    "Win by custom-fitting automations to a specific process rather than dropping in a generic tool and hoping.",
    "Justifies SNIPED's bespoke-build positioning against commodity tools and explains the failure clients fear.",
    "",
    ["95-percent-fail", "off-the-shelf-trap", "custom-fit", "strategy"])
add(S, T, A, "operator-process", "Back office before front office",
    "The transcript advises starting AI automation in back-office functions (finance, IT, admin) where rules are clear and errors are contained, before touching customer-facing front-office work.",
    "Sequence client automation back-office first, where the process is rules-based and mistakes are low-stakes.",
    "A concrete sequencing rule that complements Prediction Machines' high-value, high-error-tolerance first-use-case guidance.",
    "",
    ["back-office-first", "sequencing", "low-stakes", "operator-process"])
add(S, T, A, "operator-process", "Identify opportunities by volume and rules",
    "The process-analysis framework scores a task by how high its volume is and how rules-based it is; high-volume, high-rules tasks are the prime automation candidates. Exceptions are handled by humans.",
    "Screen client tasks on the volume-times-rules axis to pick automation targets, and route exceptions to a human.",
    "A reusable discovery filter for SNIPED, consistent with the opportunity-hopper scoring it already uses.",
    "",
    ["volume-and-rules", "opportunity-scoring", "exception-handling", "operator-process"])
add(S, T, A, "systems-thinking", "Apply Lean Six Sigma (DMAIC) to AI implementation",
    "The transcript brings Define-Measure-Analyze-Improve-Control to AI: map the current process, measure waste and time, analyze the root problem, then automate and monitor. Discipline from process engineering raises the hit rate.",
    "Run AI builds through a define-measure-analyze-improve-control loop so the automation targets measured waste, not guesses.",
    "Gives SNIPED a rigorous, sellable methodology wrapper that elevates the build above ad-hoc tool installation.",
    "",
    ["dmaic", "lean-six-sigma", "process-engineering", "systems-thinking"])
add(S, T, A, "commercial-architecture", "Prove ROI and engineer adoption for long-term success",
    "The closing chapters stress calculating ROI explicitly and then driving adoption and continuous improvement, because an unused automation delivers zero return regardless of how good the build is.",
    "Quantify ROI up front and build an adoption plan into the engagement; track usage as the real success metric.",
    "Connects SNIPED's business-case templates to a post-delivery adoption discipline that protects the retainer.",
    "",
    ["roi", "adoption", "continuous-improvement", "commercial-architecture"])

# ============================ SYNTHESIS · 4 (cite a representative real source_file) ============================
add("prediction_machines_agrawal.txt", "BATCH_008 cross-source synthesis", "SNIPED synthesis", "strategy",
    "The canon converges on cheap prediction plus expensive judgment",
    "Across Prediction Machines, Power and Prediction, and The Second Machine Age, the unifying economic claim is that AI makes prediction cheap, which raises the value of the human judgment, data, and action around it. The canon agrees the durable value migrates to the complements.",
    "Build and price around the complements (judgment, data, workflow, relationship), since the prediction itself is commoditizing.",
    "The single strategic conclusion BATCH_008 hands SNIPED: own the judgment and relationship layer, rent the model.",
    "",
    ["synthesis", "cheap-prediction", "complements", "strategy"])
add("only_humans_need_apply_davenport.txt", "BATCH_008 cross-source synthesis", "SNIPED synthesis", "operator-process",
    "Augmentation, not replacement, is the canon's consensus",
    "Davenport and Kirby, Daugherty and Wilson, Mollick, and Brynjolfsson and McAfee independently arrive at the same prescription: the winning unit is human plus machine, working in a deliberate middle, not the machine alone. The hybrid operator is the durable role.",
    "Architect every deliverable as a human-plus-machine system with the human owning judgment, taste, and accountability.",
    "Confirms SNIPED's hybrid-operator identity is not a stylistic choice but the conclusion of the entire AI-tech canon.",
    "",
    ["synthesis", "augmentation", "hybrid-operator", "operator-process"])
add("course_work_1_thru_2.txt", "BATCH_008 cross-source synthesis", "SNIPED synthesis", "commercial-architecture",
    "The implementation gap is the agency's whole business",
    "The course and operator docs (AI Edge, sniped_os, youtube skool) and the strategy books agree that capability is widely available but implementation is not, and that most projects fail by using generic tools on un-mapped processes. The agency exists to close that gap with custom-fit, process-mapped builds.",
    "Center the agency's offer on closing the implementation gap with process-mapped, custom-fit builds, not tool access.",
    "Unifies BATCH_008's practical and theoretical halves into SNIPED's commercial thesis and demand-to-delivery spine.",
    "",
    ["synthesis", "implementation-gap", "custom-fit", "commercial-architecture"])
add("the_coming_wave_suleyman.txt", "BATCH_008 cross-source synthesis", "SNIPED synthesis", "meta-doctrine",
    "Tool access commoditizes; edge, density, and trust do not",
    "The Coming Wave, Read Write Own, and The Network State together argue that capability diffuses fast and asymmetrically, so durable advantage comes from a found edge, a dense aligned community, and earned trust, not from access to tools everyone will have. The builder's responsibility is the moral spine of the position.",
    "Compound the assets the wave cannot commoditize: your specific edge, a dense aligned audience, and earned trust.",
    "Ties BATCH_008 back to SNIPED's locked doctrines (find-your-edge, scene-density, lineage, trust) as the AI-proof moat.",
    "",
    ["synthesis", "moat", "edge-density-trust", "meta-doctrine"])

# ---- emit ----
em = chr(0x2014)
lines = []
for i, ch in enumerate(C, start=1):
    rec = {
        "chunk_id": f"BATCH_008_{i:03d}",
        "batch_id": "BATCH_008",
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
    }
    lines.append(rec)

# em-dash sweep across all string fields (lifetime rule · SNIPED-authored output)
swept = 0
for rec in lines:
    for k, v in rec.items():
        if isinstance(v, str) and em in v:
            rec[k] = v.replace(em, " · "); swept += 1
        if isinstance(v, list):
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
dist = Counter(r["domain"] for r in lines)
print("Domain distribution:", dict(sorted(dist.items())))
srcdist = Counter(r["source_file"] for r in lines)
print("Source distribution:")
for k, v in sorted(srcdist.items()):
    print(f"  {v:3d}  {k}")
