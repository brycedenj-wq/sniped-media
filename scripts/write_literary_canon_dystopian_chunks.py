#!/usr/bin/env python3
"""
LITERARY_CANON_DYSTOPIAN chunker · Orwell · Atwood · Huxley

Reads the 3 normalized extracted txt files and emits LITERARY_CANON_DYSTOPIAN_CHUNKS.jsonl
with the canonical 12-field schema.

Target: 17 chunks (range 12-19 per plan section 3).
Domains (systems-thinking is a NEW domain · operator-approved · introduced here, registered at consolidation):
  systems-thinking NEW (8) + culture (3) + operator-doctrine (4) + ethics (2). strategy not used.

Brave New World Revisited = Huxley 1958 NONFICTION essays (not the novel).
Study guides absent · 0 chunks. In-copyright · direct_quotes are SHORT illustrative lines only.
Em-dash sweep (Unicode U+2014) applied · authored quotes already use em-dash-free punctuation.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "LITERARY_CANON_DYSTOPIAN_CHUNKS.jsonl"

BATCH_ID = "LITERARY_CANON_DYSTOPIAN"
F_AF = "animal_farm_orwell.txt"
F_HT = "handmaids_tale_atwood.txt"
F_BNW = "brave_new_world_revisited_huxley.txt"
BASE_TAGS = ["dystopian-canon", "systems-warning", "2026-05-19-intake"]

chunks = []


def add(num, source_title, source_file, author, domain, concept, summary, principle, relevance, quotes, tags):
    chunks.append({
        "chunk_id": f"{BATCH_ID}_{num:03d}", "batch_id": BATCH_ID,
        "source_title": source_title, "source_file": source_file, "author": author,
        "domain": domain, "concept": concept, "summary": summary,
        "usable_principle": principle, "sniped_relevance": relevance,
        "direct_quotes": quotes, "tags": BASE_TAGS + tags,
    })


AF = "Animal Farm · George Orwell"
HT = "The Handmaid's Tale · Margaret Atwood"
BNW = "Brave New World Revisited · Aldous Huxley (nonfiction essays)"
SYN = "Dystopian Canon · cross-text synthesis"
A_O, A_A, A_H = "George Orwell", "Margaret Atwood", "Aldous Huxley"
SNIPED = "SNIPED (cross-text synthesis)"

# ===========================================================================
# ANIMAL FARM (Orwell · 5)
# ===========================================================================
add(1, AF, F_AF, A_O, "systems-thinking",
    "The revolution betrayed · the new elite becomes indistinguishable from the old",
    ("Orwell's allegory tracks how a liberation (the animals overthrow the farmer) curdles into a new "
     "tyranny: the pigs accrue privileges, rewrite the rules, and by the end are eating at the table with "
     "the humans they replaced. The closing image · the other animals look from pig to man and cannot tell "
     "which is which · is the warning that a system's stated ideals do not protect against its leaders "
     "recreating the very power they overthrew."),
    ("Watch what a system DOES to its own stated ideals over time, not what it claims at founding. Power "
     "structures tend to reconstitute the hierarchy they replaced unless the structure itself prevents it. "
     "Judge by the drift, not the founding slogan."),
    ("The structural warning behind the SNIPED operating-locks discipline (B7): stated values do not "
     "self-enforce · the system's design must prevent drift. A caution for any operator building "
     "structures (or AI agents) that concentrate power · the founding intent is not a safeguard."),
    ["from pig to man, and from man to pig, and from pig to man again; but already it was impossible to say which was which"],
    ["animal-farm", "orwell", "revolution-betrayed", "institutional-design", "power", "drift"])

add(2, AF, F_AF, A_O, "systems-thinking",
    "Propaganda + the rewritten rules · changing the record to change the present",
    ("The Seven Commandments are quietly edited as the pigs need them · 'No animal shall drink alcohol' "
     "becomes 'No animal shall drink alcohol to excess', and all seven collapse into 'ALL ANIMALS ARE "
     "EQUAL BUT SOME ANIMALS ARE MORE EQUAL THAN OTHERS'. Control of the written record is control of "
     "reality: if you can edit the rules retroactively, the population cannot prove the betrayal."),
    ("Whoever can edit the record controls what is true. Protect the immutable record (what was actually "
     "said, written, promised) because retroactive editing is how a system makes betrayal unprovable. "
     "Version history is a safeguard against gaslighting at scale."),
    ("Directly applicable to AI / automation systems an operator builds: logs, audit trails, and "
     "immutable records are the defense against this exact failure (cf. N8N branching + the SNIPED "
     "STALE-FLAG audit trail · preserve what was true rather than silently overwriting it)."),
    ["No animal shall drink alcohol to excess",
     "ALL ANIMALS ARE EQUAL BUT SOME ANIMALS ARE MORE EQUAL THAN OTHERS"],
    ["animal-farm", "orwell", "propaganda", "truth-decay", "language-control", "audit-trail"])

add(3, AF, F_AF, A_O, "culture",
    "Squealer · the spin apparatus that makes a population doubt its own memory",
    ("Squealer, the pig who 'could turn black into white', is the regime's communications arm: every "
     "reversal is re-explained until the animals doubt their own recollection of what was promised. The "
     "warning is about the dedicated persuasion function whose job is not to inform but to manage "
     "perception until dissent feels like confusion."),
    ("Distrust any apparatus whose job is to manage perception rather than inform. When an institution "
     "spends more energy explaining away contradictions than resolving them, the explaining IS the "
     "control. Trust your own record over the official re-explanation."),
    ("The anti-pattern to the SNIPED hospitality + honesty stance (B3/B7): SNIPED's communications exist "
     "to inform and dignify, never to manage a subject into doubting reality. The cautionary mirror for "
     "anyone writing copy or designing AI outputs · persuasion that erodes the audience's grip on truth "
     "is the line not to cross."),
    ["Squealer could turn black into white (the spin function that makes the population doubt its own memory)"],
    ["animal-farm", "orwell", "spin", "truth-decay", "perception-management", "honesty"])

add(4, AF, F_AF, A_O, "culture",
    "Boxer · the exploited loyalty of the believing worker",
    ("Boxer the carthorse answers every crisis with 'I will work harder' and 'Napoleon is always right', "
     "and is worked to collapse · then sold to the knacker the moment he is no longer useful, his "
     "loyalty repaid with betrayal. Orwell's warning: systems extract maximum devotion from their most "
     "earnest members and discard them without sentiment."),
    ("Earnest loyalty to a system is not protection · the most devoted are the most exploitable. Direct "
     "loyalty to your own standards and people, not to an institution that will discard you when you stop "
     "producing. 'Work harder' is not a strategy when the system is rigged against you."),
    ("Reinforces the PERSONAL_OPERATING_CODE ownership axiom (internal locus · loyalty to your own code "
     "over an external master) and the SNIPED Company-of-One independence: the operator does not pour "
     "devotion into a structure that will not reciprocate. A caution against being the Boxer of someone "
     "else's platform."),
    ["I will work harder", "Napoleon is always right"],
    ["animal-farm", "orwell", "exploited-loyalty", "ownership", "independence"])

add(5, AF, F_AF, A_O, "systems-thinking",
    "The dogs · violence as the enforcement that stands behind the propaganda",
    ("Napoleon raises a litter of puppies in secret into a private army of attack dogs, then uses them to "
     "expel Snowball and to terrorize any dissent. The propaganda (Squealer) and the comfort of slogans "
     "work because raw force stands silently behind them. The warning: persuasion is enforced by the "
     "threat of violence, even when the violence is rarely shown."),
    ("Read the enforcement mechanism behind any persuasive system, not just its messaging. Soft control "
     "(slogans, comfort) usually rests on a hard backstop (force, exclusion, deplatforming). Knowing "
     "where the backstop is tells you how free the system actually is."),
    ("The systems-design caution for institutional power: the velvet glove has an iron hand. For an "
     "operator, the inverse discipline · build influence on genuine trust and value (B3 hospitality), not "
     "on a coercive backstop · is what keeps a SNIPED-style practice ethical and durable."),
    ["Napoleon's private army of dogs (the force standing silently behind the slogans)"],
    ["animal-farm", "orwell", "fear-as-governance", "enforcement", "state-power"])

# ===========================================================================
# THE HANDMAID'S TALE (Atwood · 5)
# ===========================================================================
add(6, HT, F_HT, A_A, "systems-thinking",
    "Theocratic control of bodies · the system that reduces a person to a function",
    ("In the Republic of Gilead, fertile women are conscripted as Handmaids, assigned to households "
     "purely to bear children, stripped of names, money, reading, and movement. Atwood's warning is "
     "about institutional design that reduces a human to a single function and builds an entire "
     "apparatus (Wives, Marthas, Aunts, Eyes) to enforce that reduction."),
    ("The deepest harm a system can do is reduce a person to one function and then optimize around it. "
     "When evaluating any institutional or automated design, ask what whole humans it is flattening into "
     "roles · and refuse designs whose efficiency depends on that flattening."),
    ("The literary counter-image to the SNIPED whole-human / dignity ethic (B5 portraiture · "
     "LITERARY_CANON_BLACK the-gaze chunks). Gilead is what it looks like when a system sees only "
     "function, not person · the exact opposite of the dignifying gaze SNIPED is built on."),
    ["the Republic of Gilead (women reduced to function · names, money, and reading stripped away)"],
    ["handmaids-tale", "atwood", "institutional-design", "dignity-under-pressure", "state-power"])

add(7, HT, F_HT, A_A, "culture",
    "Language control · renaming, ritual greetings, and banned reading",
    ("Gilead governs through language: Handmaids are renamed by their Commander (Offred = Of-Fred), "
     "speech is reduced to mandated ritual greetings ('Blessed be the fruit' / 'Under His Eye'), and "
     "women are forbidden to read. Controlling what can be said, and who may read, is how the regime "
     "controls what can be thought."),
    ("Control of language is control of thought · who may name, who may read, and which words are "
     "permitted shape what a population can even conceive. Guard the freedom to name accurately and to "
     "read widely; mandated euphemism is a control mechanism, not politeness."),
    ("The dark mirror of PROMPT_TEMPLATES_DEEP (language-as-leverage) and the SNIPED voice discipline: "
     "shaping language is power, which is exactly why the operator who writes copy and designs prompts "
     "must wield it to dignify and inform, never to constrain thought. Naming accurately is the ethical "
     "baseline (cf. LITERARY_CANON_BLACK reclaiming-the-frame)."),
    ["Offred (the Handmaid renamed as the possession of her Commander, Of-Fred)",
     "Blessed be the fruit", "Under His Eye"],
    ["handmaids-tale", "atwood", "language-control", "truth-decay", "naming"])

add(8, HT, F_HT, A_A, "systems-thinking",
    "Surveillance + informants · the Eyes, and everyone policing everyone",
    ("Gilead runs on surveillance: the secret police are the Eyes, the farewell greeting itself ('Under "
     "His Eye') is a reminder of constant watching, and Handmaids are paired partly so each can inform on "
     "the other. The most efficient surveillance is the kind the watched perform on themselves and each "
     "other, cheaply and continuously."),
    ("The cheapest, most total surveillance is peer-to-peer and self-imposed · a system that makes "
     "everyone a potential informant needs few cameras. When designing or adopting any monitoring "
     "system, ask whether it is turning people into watchers of each other; that is where freedom dies "
     "quietly."),
    ("The direct warning for AI / automation systems that log, track, and score (cf. N8N "
     "Airtable-as-memory + data tables): surveillance capacity is a design choice with a cost. The "
     "operator builds with restraint and human-approval gates (N8N 012/013), not maximal monitoring."),
    ["the Eyes (Gilead's secret police · everyone a potential informant on everyone)"],
    ["handmaids-tale", "atwood", "surveillance", "attention-discipline", "state-power"])

add(9, HT, F_HT, A_A, "operator-doctrine",
    "Gradual normalization · how a free society slides without a single decisive break",
    ("Atwood is precise that Gilead did not arrive overnight: rights were suspended 'temporarily', "
     "accounts were frozen, jobs were lost, and each step felt survivable, so people adjusted. The "
     "narrator recalls that you get used to anything, and that nothing changes instantaneously · the "
     "slide happens through a thousand tolerated small steps."),
    ("Watch the slope, not the cliff · dangerous change arrives as a series of individually-tolerable "
     "small steps, each rationalized as temporary. Set bright lines in advance, because in the moment "
     "every single step will feel survivable. Normalization is the mechanism, not the exception."),
    ("Sharpens the SNIPED operating-locks + bright-line discipline (B7): decide the non-negotiables in "
     "advance because in-the-moment judgment normalizes drift (cf. Animal Farm chunk 001). For an "
     "operator adopting AI tools, the warning is to set the lines (what you will never automate, never "
     "fake) before the convenient small steps arrive."),
    ["you get used to anything (nothing changes instantaneously · the slide is a thousand tolerated small steps)"],
    ["handmaids-tale", "atwood", "normalization", "bright-lines", "operator-guardrail"])

add(10, HT, F_HT, A_A, "ethics",
    "The Aunts + private resistance · the system runs on the complicity of the controlled, and dignity survives in secret",
    ("Gilead is enforced largely by the Aunts · women who indoctrinate and discipline other women · so "
     "the oppression is administered by the oppressed. Against this, Offred finds a scratched Latin "
     "phrase left by her predecessor, 'Nolite te bastardes carborundorum' (do not let the bastards grind "
     "you down): a private act of memory and defiance that keeps a self alive under total control."),
    ("Systems of control recruit the controlled as enforcers · refusing to administer harm to your peers "
     "is itself resistance. And dignity survives in small, private acts of memory and refusal even when "
     "open resistance is impossible. Guard the inner self the system cannot see."),
    ("The ethical hinge: complicity is a choice even under pressure (pairs with PERSONAL_OPERATING_CODE "
     "ownership) and interior dignity persists (LITERARY_CANON_BLACK self-possession chunks). For the "
     "operator, the refusal to become the system's enforcer · against your peers, your subjects, your "
     "audience · is the line that keeps the work human."),
    ["Nolite te bastardes carborundorum (the predecessor's scratched defiance · do not let the bastards grind you down)"],
    ["handmaids-tale", "atwood", "complicity", "dignity-under-pressure", "resistance", "ethics"])

# ===========================================================================
# BRAVE NEW WORLD REVISITED (Huxley · nonfiction essays · 5)
# ===========================================================================
add(11, BNW, F_BNW, A_H, "systems-thinking",
    "Over-organization · the person subordinated to the efficiency of the system",
    ("In the opening essay 'Over-Organization', Huxley argues that modern technological society tends to "
     "subordinate the individual to large, efficient organizations · that the drive toward order and "
     "scale steadily erodes the freedom and variety of persons. The dystopian threat, he says, is less a "
     "jackbooted tyranny than a smoothly over-managed order that treats people as interchangeable units."),
    ("Efficiency and scale are not free · past a point they subordinate persons to the system. When "
     "designing organizations or automations, weigh the cost to human freedom and variety, not only "
     "throughput. The over-organized system is a soft dystopia precisely because it feels reasonable."),
    ("The systems-design caution behind SNIPED's deliberate smallness (intel_company_of_one · "
     "right-size-not-scale) and restraint-over-volume lane. Huxley names why SNIPED resists the "
     "over-organized, scale-maximizing default · it costs the person and the variety that are the whole "
     "point."),
    ["Over-Organization (Huxley's thesis: technological society subordinates the individual to the efficient organization)"],
    ["brave-new-world-revisited", "huxley", "over-organization", "institutional-design", "comfort-as-control"])

add(12, BNW, F_BNW, A_H, "systems-thinking",
    "Propaganda in a democratic society · manufacturing consent vs informing",
    ("Huxley distinguishes propaganda that appeals to reason and serves the public from propaganda that "
     "exploits irrational drives to manufacture consent. His warning for democracies: the danger is not "
     "only the dictator's lie but the commercial and political persuasion that bypasses the rational mind "
     "while wearing the costume of free choice."),
    ("Distinguish persuasion that informs (gives the audience more capacity to choose) from persuasion "
     "that manufactures consent (bypasses their reason). The test is whether the technique would still "
     "work if the audience fully understood it · if not, it is manipulation wearing the costume of "
     "choice."),
    ("The ethical line for the SNIPED operator who writes copy, designs offers, and builds AI outputs "
     "(B2/B3 + PROMPT_TEMPLATES_DEEP): inform and earn the yes, never engineer it past the buyer's "
     "reason. Huxley is the canonical statement of why refusal-positioning + honest persuasion is the "
     "durable lane."),
    ["Huxley's split: propaganda that appeals to reason and serves the public vs propaganda that exploits irrational drives to manufacture consent"],
    ["brave-new-world-revisited", "huxley", "propaganda", "manufacturing-consent", "honesty"])

add(13, BNW, F_BNW, A_H, "operator-doctrine",
    "The arts of selling + chemical / subconscious persuasion · comfort and pleasure as control",
    ("Across 'The Arts of Selling', 'Subconscious Persuasion', and 'Chemical Persuasion', Huxley argues "
     "the modern controller need not use force · distraction, manufactured desire, and pleasant "
     "sedation (the real-world analogs of soma) keep a population content and compliant. People can be "
     "made to love a servitude that is comfortable. Comfort, not terror, is the efficient control."),
    ("The most effective control is the kind that feels good · distraction, manufactured wants, and "
     "frictionless comfort. Audit what a product or platform optimizes you toward: if it maximizes "
     "comfortable engagement over your actual interest, the comfort IS the leash. Build, and consume, "
     "against that grain."),
    ("The most pointed warning for AI / attention-economy systems an operator builds or uses: "
     "engagement-optimization and frictionless comfort are Huxley's soma. SNIPED's anti-faceless-AI, "
     "depth-over-dopamine, restraint stance (distribution_mechanics + max_default) is the deliberate "
     "refusal to build the comfortable leash."),
    ["the arts of selling and chemical persuasion (comfort, distraction, and manufactured desire as control · people made to love their servitude)"],
    ["brave-new-world-revisited", "huxley", "comfort-as-control", "attention-discipline", "soma-principle", "operator-guardrail"])

add(14, BNW, F_BNW, A_H, "ethics",
    "Brainwashing + conditioning · the engineering of belief",
    ("In 'Brainwashing', Huxley surveys how stress, repetition, and managed environments can be used to "
     "break and remake belief · and warns that the same techniques, applied gently and at scale through "
     "media and education, can condition a population without their awareness. Conditioning is most "
     "dangerous when it is invisible and pleasant."),
    ("Belief can be engineered · by stress, repetition, and a managed information environment · and the "
     "most effective conditioning is the kind the subject never notices. Protect the conditions for "
     "independent thought (varied inputs, time, dissent) as a deliberate practice, because the default "
     "drift is toward managed belief."),
    ("The ethical boundary for any operator with influence over an audience or a model's outputs: the "
     "capacity to condition belief carries the duty not to. Pairs with the SNIPED honesty + "
     "anti-manipulation stance and the dystopian guardrail · powerful persuasion tools demand restraint, "
     "not maximal use."),
    ["Huxley on brainwashing: stress, repetition, and a managed environment can remake belief · most dangerous when gentle and unnoticed"],
    ["brave-new-world-revisited", "huxley", "conditioning", "social-conditioning", "ethics", "truth-decay"])

add(15, BNW, F_BNW, A_H, "operator-doctrine",
    "Education for freedom · the antidote · teaching people to resist manipulation",
    ("Huxley closes with the remedy: 'Education for Freedom' · teaching people the facts about "
     "propaganda, the analysis of persuasion, and the value of liberty, so they can recognize and resist "
     "manipulation. Freedom is not the default; it must be actively taught, defended, and chosen against "
     "the easier pull of managed comfort."),
    ("Freedom is a practiced skill, not a default state · the antidote to manipulation is to teach "
     "(and learn) how manipulation works. Build the analytic literacy that lets you and your audience "
     "see the technique. An informed audience is the only durable defense against the arts of selling."),
    ("The constructive operator stance: SNIPED's intel-corpus practice (this whole brain) IS education "
     "for freedom · understanding the mechanics of persuasion, distribution, and AI so they are used "
     "consciously rather than fallen for. The mirror of chunk 013 · know the soma to refuse the soma."),
    ["Education for Freedom (Huxley's antidote: teach the facts about propaganda and persuasion so people can resist it)"],
    ["brave-new-world-revisited", "huxley", "education-for-freedom", "operator-guardrail", "analytic-literacy"])

# ===========================================================================
# CROSS-TEXT SYNTHESIS (2)
# ===========================================================================
add(16, SYN, F_BNW, SNIPED, "operator-doctrine",
    "The dystopian warnings as the operator's guardrail · what NOT to build when building AI / automation",
    ("Read together, the three texts are a checklist of what an operator building powerful systems must "
     "refuse to become: the rewriter of records (Animal Farm), the surveiller and language-controller "
     "(Handmaid's Tale), and the comfort-and-conditioning machine (Brave New World Revisited). The corpus "
     "spends most of its weight on how to BUILD AI and automation; this lane is the deliberate "
     "counterweight on what those systems must never do."),
    ("Hold a fixed do-not-build list alongside the build skill: no silent record-rewriting, no maximal "
     "surveillance, no language/thought constraint, no engagement-as-leash, no manufactured consent. "
     "Power to build is matched by a discipline of refusal · the guardrail is part of the competence, "
     "not separate from it."),
    ("The explicit ethical guardrail over the corpus's automation layers (N8N, PROMPT_TEMPLATES_DEEP, "
     "future BATCH_008): the SNIPED operator builds with brakes · audit trails, human-approval gates, "
     "honest persuasion, restraint over scale (intel_company_of_one). This lane is the conscience the "
     "build-canon is read against."),
    ["the three texts as a do-not-build checklist: record-rewriting (Orwell), surveillance + language control (Atwood), comfort + conditioning (Huxley)"],
    ["dystopian-canon", "operator-guardrail", "ethics", "ai-systems-warning", "do-not-build"])

add(17, SYN, F_BNW, SNIPED, "systems-thinking",
    "Orwell's boot vs Huxley's soma · two faces of control, and which one AI tends toward",
    ("The lane stages the classic distinction (sharpened by Neil Postman): Orwell feared control by pain "
     "· the boot, surveillance, censorship, the inflicted lie. Huxley feared control by pleasure · soma, "
     "distraction, manufactured desire, a populace that loves its servitude. Atwood's Gilead uses both. "
     "The open question for the present: modern AI / attention systems tend toward the HUXLEYAN failure "
     "(comfort, distraction, frictionless engagement) far more than the Orwellian one."),
    ("Diagnose which kind of control a system exerts · pain (coercion, censorship) or pleasure (comfort, "
     "distraction). Attention-economy and AI systems usually fail the Huxleyan way, so the relevant "
     "vigilance is against seductive comfort, not just overt coercion. The leash you have to watch for is "
     "the pleasant one."),
    ("The framing that tells the SNIPED operator where the real risk lies: not jackbooted censorship but "
     "Huxleyan comfort-capture · which is exactly why SNIPED's depth-over-dopamine, anti-faceless-AI, "
     "restraint posture (distribution_mechanics) is the on-point defense. Know which dystopia you are "
     "actually near."),
    ["Orwell feared those who would deprive us of information; Huxley feared those who would give us so much that we would be reduced to passivity (Postman's distinction)"],
    ["dystopian-canon", "orwell-vs-huxley", "comfort-as-control", "attention-discipline", "systems-warning"])


# ===========================================================================
# Write JSONL + em-dash sweep
# ===========================================================================

def main():
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"Wrote {len(chunks)} chunks to {OUT_JSONL}")

    em = chr(0x2014)
    text = OUT_JSONL.read_text(encoding="utf-8")
    n = text.count(em)
    if n:
        print(f"WARNING: {n} em-dashes. Sweeping.")
        OUT_JSONL.write_text(text.replace(em, " · "), encoding="utf-8")
    else:
        print("No em-dashes in output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
