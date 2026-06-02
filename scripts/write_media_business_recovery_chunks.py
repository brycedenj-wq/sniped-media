#!/usr/bin/env python3
"""Author MEDIA_BUSINESS_RECOVERY chunks (2 recovered media-institution books).

12-field schema. batch_id MEDIA_BUSINESS_RECOVERY. chunk_id MEDIA_BUSINESS_RECOVERY_NNN.
Existing domains only (media-business anchors): media-business, ethics, commercial-architecture,
culture, operator-doctrine, operator-process, strategy, founder-psychology, capital. NO
music-business/film-business/entertainment/Hollywood/agency or any new domain. Per-source
attribution. Short illustrative quotes only. Em-dash swept to ' · '. Every chunk references
CURRENT_OPERATOR_REALITY_BRIEF; closing chunk makes the optionality guardrail explicit
(pattern-library / decision-support, NOT a directive that BJ become a music/film/media executive).
"""
import json
import os

REPO = os.path.expanduser("~/AI-Brain-Refinery")
OUT = os.path.join(REPO, "01_KNOWLEDGE_BASE/batches/MEDIA_BUSINESS_RECOVERY_CHUNKS.jsonl")
BID = "MEDIA_BUSINESS_RECOVERY"

HITMEN = ("Hit Men: Power Brokers and Fast Money Inside the Music Business", "hit_men_dannen.txt", "Fredric Dannen")
MAIL = ("The Mailroom: Hollywood History from the Bottom Up", "the_mailroom_rensin.txt", "David Rensin")
SYN_H = ("MEDIA_BUSINESS_RECOVERY: cross-source synthesis", "hit_men_dannen.txt", "Dannen / Rensin (SNIPED synthesis)")
SYN_M = ("MEDIA_BUSINESS_RECOVERY: cross-source synthesis", "the_mailroom_rensin.txt", "Dannen / Rensin (SNIPED synthesis)")

GUARD = (
    " Held as a pattern-library / decision-support lens read against "
    "CURRENT_OPERATOR_REALITY_BRIEF: a model of how media institutions convert access into "
    "power, NOT a directive that BJ become a music, film, or media executive. The dark-side "
    "material keeps the patterns honest, not aspirational. Does not finalize SNIPED, SNIPED "
    "Media, or BASEPLATE direction; photography remains one option among several."
)

C = [
    # HIT MEN (7)
    (HITMEN, "media-business", "Airplay was the chokepoint that made superstars",
     "Dannen frames Top 40 radio as the fount of rock superstardom: a station played roughly forty songs, so getting a record 'added' to those playlists was the gate to mass success. Control of that narrow chokepoint, not the music alone, determined who broke through.",
     "Find the narrow chokepoint a market routes through (the few slots everyone competes for); whoever influences the gate holds disproportionate power over outcomes.",
     "Identify the real chokepoint/gate in any market (the platform, the feed, the buyer's shortlist) rather than assuming the best product wins. A lens for where leverage actually sits.",
     ["\"the most listeners nationwide\""], ["chokepoint", "distribution", "gatekeeping", "radio", "media-business"]),
    (HITMEN, "ethics", "The Network: payola's successor as a hidden tollbooth",
     "Dannen exposes the Network, a small group of independent promoters with mysterious influence over radio adds, the modern descendant of payola. Labels paid them rather than risk records not getting played, and parts of it ran on intimidation and organized-crime ties.",
     "When a gate is opaque and essential, a rent-extracting middle layer forms around it; payments to clear the gate can shade from service into a coercive tollbooth.",
     "An ethics lens on gatekeepers: watch for opaque intermediaries who extract rent at a chokepoint, and recognize when 'paying to play' has crossed into something coercive. Not a model to emulate.",
     ["\"the Network\""], ["payola", "ethics", "gatekeeping", "intermediaries", "corruption"]),
    (HITMEN, "ethics", "Fast money and the exploitation beneath the hits",
     "The book's subtitle (fast money) names the culture: a business where huge sums moved fast, artists were often exploited, and the people who controlled access profited more reliably than the talent. The glamour masked a harsh, sometimes predatory machine.",
     "In access-controlled industries the gatekeepers often capture more value than the creators; glamour can mask exploitation, so read who actually keeps the money.",
     "A clear-eyed lens for any creative industry BJ studies: ask who captures the value versus who makes the work, and stay alert to exploitation behind the glamour.",
     ["\"fast money\""], ["ethics", "exploitation", "value-capture", "creators", "music-industry"]),
    (HITMEN, "commercial-architecture", "Indie promotion: the cost that went straight to the bottom line",
     "Independent promotion grew from a tiny line item to the labels' biggest expense after salaries, tens of millions a year, money that (as CBS's Dick Asher saw) went 'right to the bottom line', cutting directly into profit yet seemingly impossible to stop.",
     "A cost that buys access can metastasize into the largest line item precisely because no single player dares stop paying it first; structural costs outlive the logic that created them.",
     "A cost-structure lens: watch for 'everyone pays it because no one can stop first' expenses, and notice how access costs quietly become the dominant line item. Relevant to evaluating any platform tax.",
     ["\"right to the bottom line\""], ["commercial-architecture", "cost-structure", "economics", "access-cost", "labels"]),
    (HITMEN, "founder-psychology", "Concentrated personal power ran the business",
     "Dannen profiles the era's power brokers (Walter Yetnikoff at CBS, David Geffen, Irving Azoff at MCA): forceful, combative personalities whose personal will, relationships, and fear they inspired ran the industry as much as any org chart.",
     "In relationship-driven industries, concentrated personal power and force of personality can outweigh formal structure; who you are and who fears or trusts you is the real org chart.",
     "A lens on how power actually flows in relationship businesses (personality and trust over title), held as observation, not a personality to imitate.",
     ["\"the most powerful man\""], ["founder-psychology", "power", "personality", "relationships", "media-business"]),
    (HITMEN, "strategy", "Control the institution to amplify your power",
     "Geffen and Azoff both followed the same arc: from artist manager to label boss. Representing talent gave them leverage; owning the institution that distributes it multiplied that leverage into industry-shaping power.",
     "Move from representing or serving the talent to controlling the institution that distributes it; owning the chokepoint compounds individual leverage into structural power.",
     "A strategic lens on moving up the value chain: control of the distributing institution beats being one more service provider to it. Connects to the avoid-permanent-service-provider thread.",
     ["\"former artist manager\""], ["strategy", "value-chain", "ownership", "leverage", "institutions"]),
    (HITMEN, "capital", "The 1979 crash punctured the recession-proof myth",
     "Dannen recounts the 1979 industry collapse: sales fell for the first time since WWII as the disco-fueled hype machine force-fed unsold records to retailers that thundered back as returns. The business learned it was not recession-proof and that growth had been hiding bad decisions.",
     "Growth hides mistakes; when it stops, the hype-and-returns dynamics surface at once. Treat 'recession-proof' and force-fed demand as warning signs, not durable conditions.",
     "A capital/cycle lens: durable growth is not a constant, hype inflates apparent demand, and a downturn exposes what easy money was covering. Echoes the DEEP_FINANCE cycle material.",
     ["\"the first decline since World War II\""], ["capital", "cycles", "hype", "returns", "music-industry"]),
    # THE MAILROOM (6)
    (MAIL, "operator-doctrine", "Learn it from the absolute bottom up",
     "The Mailroom's premise: future agents and executives all started in the literal mailroom, delivering packages, and learned the business by full immersion from the bottom. As one alum put it, it was a crucible by accident, but the immersion was the benefit.",
     "Start at the bottom of the actual system to learn it by immersion; the menial entry is where you absorb how the whole machine really works.",
     "A learning-by-immersion lens: real understanding of a domain often comes from working its lowest, most concrete layer, not from the top. Relevant to BJ's hands-on field-operator instinct.",
     ["\"from the absolute bottom up\""], ["operator-doctrine", "apprenticeship", "immersion", "learning", "bottom-up"]),
    (MAIL, "operator-process", "Information is king",
     "Trainees read everything they touched, booking sheets, memos, contracts, even steaming open mail, and memorized names, numbers, and what clients earned. Knowing the information was the stepping-stone to promotion; 'information is king' was the operating creed.",
     "Systematically absorb all the information that passes through your hands; in a relationship/representation business, knowing who, what, and how much is the lever to advance.",
     "An information-discipline lens: the operator who absorbs and retains the flow of information around them gains leverage. A lens for how BJ would learn any system from the inside.",
     ["\"information is king\""], ["operator-process", "information", "learning", "leverage", "apprenticeship"]),
    (MAIL, "media-business", "The agency's asset is relationships and access to talent",
     "The agency business runs on relationships: an agent's value is the roster of clients and the web of people who will and will not take their call. The institution monetizes access to talent and the trust that lets deals happen.",
     "In representation businesses the durable asset is relationships and access, not a product; the network of who trusts you is the inventory.",
     "A lens on relationship/access businesses: the asset is the trusted network, not a deliverable. Frames how representation and gatekeeping institutions actually create value.",
     ["\"form relationships\""], ["media-business", "relationships", "talent", "access", "representation"]),
    (MAIL, "operator-doctrine", "The trainee ethos: take care of it, and find a mentor",
     "What the system rewarded: the person who says 'I can take care of it' and then does, who gives the credit and takes the blame, asks a million questions, and finds a mentor. Reliability plus initiative plus mentorship was the path off the bottom.",
     "Become the reliable person who owns problems end to end, deflects credit, absorbs blame, and attaches to a mentor; that bundle, not talent alone, earns advancement.",
     "An operator-character lens: reliability, ownership, humility about credit, and seeking mentorship compound into trust and opportunity. Directly portable to how BJ operates.",
     ["\"I can take care of it\""], ["operator-doctrine", "reliability", "mentorship", "ownership", "initiative"]),
    (MAIL, "culture", "The say-yes, glad-handing service culture",
     "CAA's creed was literally 'our job is to say yes'; the agency world ran on glad-handing, hyperbole, and a relentless service posture toward clients. The culture was a full-body immersion in pleasing, selling, and never being the one who says no.",
     "Service-and-access cultures reward a relentless yes-posture and social fluency; understand that ethos to read (or operate inside) such an institution, and its costs.",
     "A culture lens: some institutions run on a yes/service/social ethos. Useful for reading how such places work, held as observation, not a prescription for BJ's voice or values.",
     ["\"our job is to say yes\""], ["culture", "service-ethos", "relationships", "selling", "agency-culture"]),
    (MAIL, "strategy", "Earn the desk: make yourself indispensable to climb",
     "The ladder ran mailroom to a desk (an agent's assistant) to agent. Trainees forced promotion by becoming indispensable, knowing more than their role required ('you can fire me or promote me'), and proving they could run an agent's whole life.",
     "Advance by becoming indispensable one level up before you are promoted: do the next role's work, hold more context than required, and make keeping you the obvious choice.",
     "A career-leverage lens: earn the next rung by already operating at it. A lens for how BJ would compound from any starting position by over-delivering on context and reliability.",
     ["\"fire me or promote me\""], ["strategy", "indispensability", "advancement", "leverage", "career"]),
    # SYNTHESIS (2)
    (SYN_H, "media-business", "Synthesis: how media institutions convert access into durable power",
     "Across Hit Men and The Mailroom one pattern recurs: media institutions are built on controlling a chokepoint (radio adds, talent access), monetizing that gate, running on relationships and concentrated personal power, climbed via bottom-up apprenticeship and information, and shadowed by a dark side when access turns coercive. Power flows to whoever controls and distributes access, not only to the talent. This is a closing synthesis chunk.",
     "Media-institution power = control of a chokepoint + monetized access + relationship capital + bottom-up mastery, with a recurring dark side when gatekeeping turns coercive.",
     "An integrated decision-support lens on media/talent/distribution power: see where the gate is, who controls it, and how access becomes leverage, read against current reality.",
     ["\"power brokers\""], ["synthesis", "gatekeeping", "access", "power", "media-business"]),
    (SYN_M, "operator-doctrine", "Synthesis: the optionality guardrail",
     "These two institution histories are a pattern library for how access-controlled media businesses work, NOT a directive that BJ become a music, film, or media executive, and not an endorsement of the dark-side tactics. They sharpen how he reads gatekeeping, relationships, and apprenticeship while identity and direction stay open. This is the closing optionality chunk.",
     "Absorb the media-institution patterns (chokepoints, access, relationships, bottom-up mastery) as observation and judgment, while keeping identity and direction fully open and the ethics honest.",
     "Media-business patterns as portable judgment, not a new identity; explicitly preserves optionality and keeps photography one option among several.",
     ["\"from the bottom up\""], ["optionality", "decision-support", "guardrail", "media-business", "doctrine"]),
]


def sweep(s):
    return s.replace(chr(0x2014), " · ").replace(chr(0x2013), "-")


def main():
    if os.path.exists(OUT):
        raise SystemExit(f"REFUSE: {OUT} exists")
    lines = []
    for i, (src, domain, concept, summary, principle, relevance, quotes, tags) in enumerate(C, start=1):
        title, sfile, author = src
        sr = relevance + GUARD
        rec = {
            "chunk_id": f"{BID}_{i:03d}",
            "batch_id": BID,
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": sr,
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
