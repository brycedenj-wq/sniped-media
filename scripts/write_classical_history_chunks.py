#!/usr/bin/env python3
"""Write CLASSICAL_HISTORY_CHUNKS.jsonl from the 4 curated ancient Greek/Macedonian histories.

The Landmark Herodotus + The Landmark Thucydides + Arrian (Campaigns of Alexander) +
Engels (Alexander logistics). 12-field canonical schema. Existing domains only
(strategy / power / leadership / operator-process / culture / ethics / operator-doctrine /
systems-thinking / mental-models). NO new domain (history / empire / war / politics /
statecraft / military / civilization / antiquity NOT created). Per-source attribution.
CURATED representative strategy/power/culture/logistics extraction, NOT exhaustive history.
Held as a decision-support / pattern-library lens, NOT a directive that BJ build an empire,
seek political power, or copy ancient rulers; overreach material is cautionary, not
aspirational. Bible held separately and untouched. Every chunk carries the
CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality guardrail (GUARD).
Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "CLASSICAL_HISTORY_CHUNKS.jsonl"
BATCH = "CLASSICAL_HISTORY"

HDT = ("The Landmark Herodotus: The Histories", "Herodotus (Robert B. Strassler, ed.)",
       "herodotus_histories.txt")
THU = ("The Landmark Thucydides: The Peloponnesian War", "Thucydides (Robert B. Strassler, ed.)",
       "thucydides_peloponnesian_war.txt")
ARR = ("The Campaigns of Alexander", "Arrian", "arrian_campaigns_of_alexander.txt")
ENG = ("Alexander the Great and the Logistics of the Macedonian Army", "Donald W. Engels",
       "engels_macedonian_logistics.txt")

GUARD = (" Held as a strategy / power / culture / operator pattern-library lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: a transferable model of strategy, leadership, overreach, "
         "and logistics, NOT a directive that BJ build an empire, seek political power, or copy "
         "ancient rulers, and not an endorsement of conquest (the overreach material is cautionary, "
         "not aspirational). The Bible remains held separately and untouched. No final SNIPED, SNIPED "
         "Media, or BASEPLATE direction is set here; photography remains one option among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
CHUNKS = [
    # ---------- Herodotus · 4 source ----------
    (HDT,
     "Custom is king of all: reading a culture from the inside",
     "culture",
     "Herodotus, citing Pindar, concludes that 'custom is king of all': Darius's experiment showed "
     "Greeks and Indian Kallatiai equally horrified by each other's funeral customs, because every "
     "people believes its own norms are best. Herodotus, the first cultural anthropologist, treats "
     "custom (nomos), not nature, as the governing force in how a society behaves.",
     "Read the unstated norms of any culture or scene you enter on their own terms rather than "
     "assuming your own defaults are universal; what looks self-evident is usually just local custom.",
     "A culture-reading lens for BJ entering specific LA cultural circles and client worlds: learn "
     "the scene's actual norms from inside rather than importing assumptions; nomos is local. Held "
     "interpretively.",
     ["custom is king of all"],
     ["nomos", "custom", "cultural-relativism", "culture", "herodotus", "landmark-herodotus"]),
    (HDT,
     "Call no man fortunate until he is dead: the impermanence of fortune",
     "operator-doctrine",
     "In the Solon and Croesus story Herodotus sets his central theme: 'human happiness never "
     "continues long in one place,' the cities once great have become small and the weak have grown "
     "powerful. Solon warns the rich king to call no man happy until he is dead, because fortune "
     "reverses suddenly and the present high is no guarantee.",
     "Hold present success and present failure as provisional; fortune reverses, so do not "
     "over-extrapolate from a current peak or trough, and keep humility and a margin against reversal.",
     "A proportion lens for BJ: treat any current high or low as provisional, keep humility and "
     "reserves against reversal, and do not build as if today's fortune is permanent. Held "
     "interpretively.",
     ["never continues long in one place", "until you are dead"],
     ["impermanence", "fortune", "humility", "operator-doctrine", "herodotus", "landmark-herodotus"]),
    (HDT,
     "Croesus and the ambiguous oracle: hearing what you want to hear",
     "operator-process",
     "Croesus asked the Delphic oracle whether to attack Persia and was told he would 'destroy a "
     "great empire'; he read it as victory and attacked, destroying his own empire instead. "
     "Herodotus's point is that the signal did not lie; Croesus interpreted an ambiguous message "
     "through his own arrogance and desire.",
     "Ambiguous feedback and data get read through hope and ego; before acting on a favorable "
     "reading, ask what the same signal would mean if it pointed the other way, and what would "
     "falsify it.",
     "A decision-hygiene lens for BJ: when a market signal, a client cue, or a metric is ambiguous, "
     "guard against reading it the way you want; pre-state what would prove you wrong. Held "
     "interpretively.",
     ["destroy a great empire"],
     ["ambiguity", "wishful-interpretation", "decision-hygiene", "operator-process", "herodotus", "landmark-herodotus"]),
    (HDT,
     "Free men outfight subjects: ownership as a force multiplier",
     "leadership",
     "A recurring Herodotean theme of the Persian Wars is that Greeks fighting for their own freedom "
     "and laws outperformed the larger conscript forces of the Persian king; even the Persians "
     "themselves had fought fiercest when becoming 'free men instead of slaves.' Stake and self-rule, "
     "not numbers alone, drove the fighting power.",
     "People defending their own stake and choices outperform conscripts and hired hands; genuine "
     "ownership is a force multiplier that raw scale cannot match.",
     "A team/relationship lens for BJ: a small group with real ownership and stake outperforms larger "
     "hired-gun labor; build genuine stake into collaborators rather than relying on scale. Held "
     "interpretively.",
     ["free men instead of slaves"],
     ["ownership", "stake", "motivation", "leadership", "herodotus", "landmark-herodotus"]),
    # ---------- Thucydides · 5 source ----------
    (THU,
     "The real cause: a rising power and the fear it inspires (the Thucydides Trap)",
     "mental-models",
     "Thucydides distinguishes the surface grievances of the Peloponnesian War from its real cause: "
     "'the growth of the power of Athens, and the alarm which this inspired in Sparta, made war "
     "inevitable.' The structural dynamic, a rising power and the fear it provokes in the established "
     "one, is the model later called the Thucydides Trap.",
     "Watch the structural dynamic, not just the stated grievances: a fast-rising player and the "
     "alarm it creates in incumbents drives conflict independent of anyone's intentions.",
     "A model for BJ reading competitive dynamics: rapid rise provokes incumbent alarm and reaction "
     "regardless of stated reasons; anticipate the structural response, not just the surface "
     "complaints. Held interpretively.",
     ["growth of the power of Athens", "made war inevitable"],
     ["thucydides-trap", "rising-power", "structural-dynamics", "mental-models", "thucydides", "landmark-thucydides"]),
    (THU,
     "The Melian dialogue: power realism read honestly, with its moral cost",
     "power",
     "In the Melian dialogue the Athenians strip away pretense: 'the strong do what they can and the "
     "weak suffer what they must,' right being a question only between equals in power. Thucydides "
     "records this as cold realism about how power behaves, while the slaughter of Melos that follows "
     "stands as a moral indictment, not an endorsement.",
     "See clearly that raw power often overrides appeals to justice between unequals, so you are not "
     "naive; this is analysis of how power behaves, not a license to behave that way.",
     "An honest-realism lens for BJ: understand that leverage and power, not fairness, often decide "
     "outcomes between unequal parties, so negotiate from a position of strength, while the Melian "
     "atrocity keeps it cautionary, not a model to imitate. Held interpretively.",
     ["the strong do what they can", "the weak suffer what they must"],
     ["power-realism", "leverage", "melian-dialogue", "power", "thucydides", "landmark-thucydides"]),
    (THU,
     "Pericles' strategy: the discipline of not over-reaching",
     "strategy",
     "Pericles' war strategy was deliberately bounded: rely on the command of the sea and Athens's "
     "capital, 'attempt no new conquests, and expose the city to no hazards during the war.' "
     "Thucydides judges that Athens fell not because the strategy was wrong but because Pericles's "
     "successors abandoned its discipline for private ambition.",
     "Define the bounded strategy that wins and hold the line on it; most failures come not from a "
     "flawed plan but from abandoning its discipline for opportunistic side-bets.",
     "A strategic-discipline lens for BJ: pick the bounded plan that wins (own the core, avoid "
     "unforced risks) and resist scope creep and shiny side-bets; discipline beats opportunism. Held "
     "interpretively.",
     ["attempt no new conquests", "expose the city to no hazards"],
     ["strategic-discipline", "focus", "scope-control", "strategy", "thucydides", "landmark-thucydides"]),
    (THU,
     "The Sicilian expedition: catastrophic over-extension far from base",
     "strategy",
     "Against Pericles's caution, Athens launched the vast Sicilian expedition, a struggle 'with a "
     "people who live in a distant land,' far from home and supply. Thucydides treats it as a host of "
     "blunders ending in total destruction of fleet and army, the textbook case of ambition "
     "over-reaching its base and reach.",
     "Ambition has a culminating point: projecting force far beyond your base and support invites "
     "catastrophe; weigh distance, supply, and reinforcement before committing to a distant bet.",
     "An overreach-warning lens for BJ: a glamorous distant expansion that outruns your base, cash, "
     "and ability to reinforce can sink the whole enterprise; size the bet to your reach. Read as "
     "cautionary, not aspirational. Held interpretively.",
     ["a host of blunders", "the Sicilian expedition"],
     ["overreach", "culminating-point", "over-extension", "strategy", "thucydides", "landmark-thucydides"]),
    (THU,
     "Stasis at Corcyra: how conflict corrupts language and judgment",
     "ethics",
     "In the Corcyrean revolution Thucydides shows civil conflict inverting values: 'words had to "
     "change their ordinary meaning,' reckless audacity was praised as courage and prudent hesitation "
     "scorned as cowardice. War, 'a rough master,' brought most men's characters down to the level of "
     "their circumstances, and the lust for power drove the violence.",
     "Under factional conflict and stress, language and values invert and moderation gets punished; "
     "guard your own definitions and integrity rather than letting the climate redefine them for you.",
     "A clarity-under-pressure lens for BJ: in heated, factional, or hype-driven environments, words "
     "and norms get corrupted; hold your own standards and plain meanings instead of being pulled into "
     "the distortion. Held interpretively.",
     ["change their ordinary meaning", "a rough master"],
     ["stasis", "corruption-of-language", "integrity", "ethics", "thucydides", "landmark-thucydides"]),
    # ---------- Arrian · 4 source ----------
    (ARR,
     "Rapidity was all in all: speed and tempo as a weapon",
     "strategy",
     "At the river crossing against Darius, Arrian writes that 'rapidity was now all in all': a swift "
     "attack would shake the enemy and minimize the damage they could do. Across the campaigns "
     "Alexander repeatedly won by moving faster than opponents expected, seizing the decisive moment "
     "before they could organize.",
     "Speed and tempo are themselves a weapon: acting decisively before opponents can react can be "
     "worth more than superior resources, provided the timing rests on real judgment.",
     "A tempo lens for BJ: moving fast and decisively at the right moment can win position that "
     "hesitation forfeits; speed compounds advantage when it rests on judgment, not haste. Held "
     "interpretively.",
     ["Rapidity was now all in all"],
     ["speed", "tempo", "initiative", "strategy", "arrian", "campaigns-of-alexander"]),
    (ARR,
     "Leading from the front: the bond between commander and troops",
     "leadership",
     "Arrian shows Alexander leading from the front, at the head of his own troops, riding 'at a "
     "gallop into the stream' ahead of his men and sharing their hardship and risk. That visible "
     "shared exposure, not rank alone, bound the army's fierce loyalty to him through years of "
     "campaigning far from home.",
     "Loyalty and morale are earned by visibly sharing the risk and hardship you ask of others; "
     "leading from the front binds people in a way that command from safety cannot.",
     "A leadership lens for BJ: visibly carrying the same risk and work you ask of collaborators "
     "earns durable loyalty; presence and shared stake beat distant directives. Held interpretively.",
     ["rode at a gallop", "head of his own troops"],
     ["leading-from-front", "shared-risk", "loyalty", "leadership", "arrian", "campaigns-of-alexander"]),
    (ARR,
     "Cutting the Gordian knot: refusing the inherited framing of a problem",
     "mental-models",
     "Confronted with the Gordian knot, which no one could untie and whose solver was destined to "
     "rule Asia, Alexander (in the popular account) cut it with his sword and declared 'I have undone "
     "it.' The story endures as the model of refusing a problem's assumed rules and reframing it so a "
     "decisive move becomes possible.",
     "When a problem is framed as an intractable puzzle, question whether you must accept that framing; "
     "a decisive reframing can dissolve a constraint others treat as fixed.",
     "A problem-solving lens for BJ: when stuck inside someone else's framing of a constraint, look "
     "for the move that changes the rules rather than grinding at the knot as given. Held "
     "interpretively.",
     ["I have undone it", "cut the knot"],
     ["reframing", "gordian-knot", "constraint-breaking", "mental-models", "arrian", "campaigns-of-alexander"]),
    (ARR,
     "Hubris and the failure of self-mastery: the limit Alexander could not feel",
     "power",
     "Arrian, admiring but candid, censures Alexander's 'insatiable appetite for fame' and his "
     "deteriorating self-mastery, the Persian dress and attempted prostration that alienated his own "
     "men, the murder of Cleitus, the refusal to stop. At the Hyphasis his exhausted army finally "
     "refused to march further; Coenus reminded him that 'self-restraint is a noble thing.'",
     "Unchecked success erodes self-mastery and the ability to sense your own limit; the discipline "
     "to stop and consolidate at the peak is rarer and more valuable than the drive that got you "
     "there.",
     "A self-mastery lens for BJ: the danger at a peak is losing the ability to feel your own limit; "
     "build in the restraint to consolidate rather than chase endless expansion. Read as cautionary, "
     "not a directive to accumulate power. Held interpretively.",
     ["insatiable appetite for fame", "self-restraint is a noble thing"],
     ["hubris", "self-mastery", "restraint", "power", "arrian", "campaigns-of-alexander"]),
    # ---------- Engels · 3 source ----------
    (ENG,
     "Supply is the basis of strategy: logistics underwrites everything",
     "operator-process",
     "Engels's systematic study argues that 'supply is the basis of strategy and tactics': Alexander's "
     "famous rapid marches and desert crossings were possible only because of a highly efficient "
     "logistic organization, not despite the absence of one. The unglamorous machinery of provisioning "
     "set what the campaigns could attempt.",
     "Logistics determines what strategy is even possible; the unglamorous supply and operations layer "
     "is the foundation, not an afterthought to the bold plan.",
     "A foundations lens for BJ: the boring backend (systems, cash flow, supply, operations) sets the "
     "ceiling on what the visible work can attempt; load the backend before the bold move. Held "
     "interpretively.",
     ["supply is the basis of strategy"],
     ["logistics", "supply", "operations-foundation", "operator-process", "engels", "macedonian-logistics"]),
    (ENG,
     "The transport eats its own load: the carrying-capacity limit on reach",
     "systems-thinking",
     "Engels shows that pack animals over long distances 'consumed all the supplies they were carrying' "
     "before they could deliver them, so beyond a certain range land transport becomes self-defeating "
     "and supply has to 'import food and water by sea.' Reach is bounded by a systemic constraint, not "
     "by will or ambition.",
     "Every delivery system has a range past which it consumes more than it carries; model the "
     "carrying-capacity limit before assuming you can extend reach indefinitely.",
     "A constraints lens for BJ: any system (time, cash, attention, a small team) has a range past "
     "which extending it consumes more than it returns; find that limit instead of assuming reach is "
     "free. Held interpretively.",
     ["consumed all the supplies", "import food and water by sea"],
     ["carrying-capacity", "constraints", "diminishing-returns", "systems-thinking", "engels", "macedonian-logistics"]),
    (ENG,
     "Provisions arranged in advance: intelligence and preparation before the march",
     "operator-process",
     "Far from securing food in some automatic sequence, Alexander 'arranged the collection of "
     "provisions in advance' with local officials before marching into territory, and was 'deeply "
     "aware of the importance of military intelligence.' The reach came from preparation and "
     "information, secured before the army ever moved.",
     "Secure your supply and intelligence before you commit, not during; the apparently effortless "
     "advance is bought by preparation and information gathered in advance.",
     "A preparation lens for BJ: line up the supply, the intelligence, and the groundwork before "
     "committing to a move, so the execution looks effortless because the work was done up front. "
     "Held interpretively.",
     ["collection of provisions in advance", "importance of military intelligence"],
     ["preparation", "intelligence", "groundwork", "operator-process", "engels", "macedonian-logistics"]),
    # ---------- Synthesis · 2 ----------
    (THU,
     "Synthesis: the ancient-history operating pattern",
     "strategy",
     "Across the four histories a single operating pattern emerges: read the scene's real norms from "
     "inside (Herodotus's nomos), see power and incentives honestly without naivety or cruelty "
     "(Thucydides's realism), hold strategic discipline and respect the culminating point rather than "
     "over-reaching (Pericles's caution, the Sicilian and Hyphasis disasters), and remember that "
     "logistics underwrites every bold move (Engels). Clear sight, disciplined ambition, supply "
     "before reach.",
     "Combine reading a culture from inside, honest realism about power, strategic discipline against "
     "over-reach, and logistics-first foundations, the durable spine of how campaigns and societies "
     "succeed or collapse.",
     "For BJ this is a portable judgment toolkit (read the scene, see power clearly, hold discipline "
     "against over-reach, build the supply base first), held as decision-support against the brief, "
     "not a directive about empire or conquest. Held interpretively.",
     ["supply is the basis of strategy", "the strong do what they can"],
     ["synthesis", "ancient-history", "judgment", "strategy", "thucydides", "classical-history"]),
    (HDT,
     "Synthesis: pattern-library discipline and the optionality guardrail",
     "operator-doctrine",
     "CLASSICAL_HISTORY is held as an interpretive strategy / power / culture pattern library, NOT a "
     "directive: Herodotus, Thucydides, Arrian, and Engels are mined for transferable patterns of "
     "strategy, leadership, over-reach, and logistics, explicitly not a mandate that BJ build an "
     "empire, seek political power, or copy ancient rulers. The over-reach and conquest material "
     "(the Melian dialogue, the Sicilian expedition, Alexander's hubris) is read as cautionary "
     "analysis, with Herodotus's 'call no man happy until he is dead' as the humility anchor.",
     "Mine ancient history for transferable judgment while holding it as interpretation, not "
     "doctrine or directive; the value is sharpened judgment and cautionary patterns, decoupled "
     "from the conquest and politics that produced them.",
     "This synthesizes the lane for BJ: a sharpened-judgment toolkit and a set of cautionary "
     "over-reach patterns held as decision-support against CURRENT_OPERATOR_REALITY_BRIEF, not a "
     "directive to build empire, seek power, or copy ancient rulers; the Bible stays held separately; "
     "photography remains one option among several; no final SNIPED / SNIPED Media / BASEPLATE "
     "direction is set.",
     ["never continues long in one place", "one option among several"],
     ["synthesis", "interpretive-lens", "optionality", "operator-doctrine", "herodotus", "classical-history"]),
]


def sweep(o):
    if isinstance(o, str):
        return o.replace(chr(0x2014), " · ")
    if isinstance(o, list):
        return [sweep(x) for x in o]
    if isinstance(o, dict):
        return {k: sweep(v) for k, v in o.items()}
    return o


def main():
    lines = []
    for i, (src, concept, domain, summary, principle, relevance, quotes, tags) in enumerate(CHUNKS, 1):
        title, author, sfile = src
        rec = {
            "chunk_id": f"{BATCH}_{i:03d}",
            "batch_id": BATCH,
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": relevance + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        lines.append(sweep(rec))

    text = "\n".join(json.dumps(r, ensure_ascii=False) for r in lines) + "\n"
    assert chr(0x2014) not in text, "em-dash leaked"
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {len(lines)} chunks -> {OUT}")
    doms, srcs = {}, {}
    for r in lines:
        doms[r["domain"]] = doms.get(r["domain"], 0) + 1
        srcs[r["source_file"]] = srcs.get(r["source_file"], 0) + 1
    print("domains:", json.dumps(doms, ensure_ascii=False))
    print("per-source:", json.dumps(srcs, ensure_ascii=False))
    forb = [d for d in ("history", "empire", "war", "politics", "statecraft",
                        "military", "civilization", "antiquity") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
