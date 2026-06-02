#!/usr/bin/env python3
"""Write LITERARY_RECOVERY_CHUNKS.jsonl from the 2 recovered literary works.

Beloved (Morrison) + Jonathan Livingston Seagull (Bach). 12-field canonical schema.
Existing domains only (culture / lineage / aesthetics / ethics / operator-doctrine).
NO new domain (literary/identity/memory/trauma/freedom/myth/faith/self-help NOT created).
Per-source attribution. Beloved weighted heavier. Beloved distinguished from The Bluest Eye;
Seagull read at the cultural/craft level, NOT as a belief system. Every chunk carries the
CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality guardrail (GUARD).
Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "LITERARY_RECOVERY_CHUNKS.jsonl"
BATCH = "LITERARY_RECOVERY"

BEL = ("Beloved", "Toni Morrison", "beloved_morrison.txt")
SEA = ("Jonathan Livingston Seagull", "Richard Bach", "jonathan_livingston_seagull_bach.txt")

GUARD = (" Held as an interpretive / cultural pattern-library lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: the humanistic-formation and cultural-lineage layer "
         "the operator/AI-build canon is read against, NOT a directive that BJ turn the OS into "
         "literary criticism or toward faith/self-help, and not doctrine. No final SNIPED, SNIPED "
         "Media, or BASEPLATE direction is set here; photography remains one option among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
CHUNKS = [
    # ---------- Beloved (Morrison) · 8 ----------
    (BEL,
     "Sixty million: the ancestral inheritance of the uncounted dead",
     "lineage",
     "Beloved opens with the dedication 'Sixty million and more' and renders slavery as a "
     "lineage wound carried across generations: Baby Suggs' eight children scattered ('stored "
     "up, mortgaged, won, stolen or seized'), kin unmade as property. The novel insists the "
     "past is inherited, not escaped.",
     "Cultural and family lineage carries inherited weight that outlives the original event; "
     "a people's history lives in its descendants, not only in records.",
     "A lineage lens for BJ's cultural-formation layer: history is inherited and load-bearing, "
     "a reminder that the work sits inside lineages (per the Lineage Doctrine), held "
     "interpretively, not as a directive.",
     ["Sixty million", "stored up, mortgaged, won, stolen"],
     ["lineage", "ancestry", "slavery", "inheritance", "morrison", "beloved"]),
    (BEL,
     "Rememory: the past persists in places, collective and inescapable",
     "culture",
     "Morrison's coined 'rememory' holds that memory is not just private recall but a thing "
     "out in the world: 'the picture of it stays,' and you can bump into a rememory that "
     "belongs to someone else. The past is a shared, place-bound presence, not a closed file.",
     "Collective memory persists in places and is shared across people; the past is an active "
     "presence a culture keeps encountering, not a sealed record.",
     "For BJ's cultural reading, memory is treated as collective and environmental, not merely "
     "individual; a lens on how shared history stays present, held interpretively.",
     ["bump into a rememory", "the picture of it stays"],
     ["rememory", "collective-memory", "place", "culture", "morrison", "beloved"]),
    (BEL,
     "The haunting: the unprocessed past returns until it is faced",
     "culture",
     "124 is 'spiteful,' literally haunted by the murdered baby; the family organizes its "
     "whole life around keeping the past at bay until the haunting forces a reckoning. The "
     "ghost is the past that refuses to stay buried until it is confronted.",
     "What is suppressed does not disappear; an unprocessed past returns and distorts the "
     "present until it is faced directly.",
     "An interpretive lens on avoidance: suppressed history (personal or collective) keeps "
     "returning until confronted, useful as a pattern, not a directive about BJ's path.",
     ["124 was spiteful", "keeping the past at bay"],
     ["haunting", "the-past", "reckoning", "culture", "morrison", "beloved"]),
    (BEL,
     "The deepest theft of slavery is the theft of self",
     "ethics",
     "Beloved's moral core is that slavery's worst violence is not only labor, killing, or "
     "maiming but the power to 'dirty you so bad you forgot who you were and couldn't think it "
     "up.' The novel bears witness to dehumanization as the unforgivable harm.",
     "The gravest harm a system can do is to corrupt a person's relationship to their own "
     "worth; bearing honest witness to that harm matters.",
     "Read as ethical witness, not prescription: a lens on how systems can attack selfhood "
     "itself, held interpretively within BJ's humanistic-formation layer.",
     ["dirty you so bad you forgot", "your best thing"],
     ["dehumanization", "witness", "selfhood", "ethics", "morrison", "beloved"]),
    (BEL,
     "Mother-love and the impossible choice under bondage",
     "ethics",
     "Sethe's killing of her daughter to keep her from being taken back into slavery is the "
     "novel's unbearable center: 'the best thing she was, was her children,' and she will not "
     "let slavery claim her best thing. Morrison renders it as anguished witness, refusing easy "
     "judgment.",
     "Some moral situations are genuinely irreducible; literature can hold an impossible choice "
     "as witness without flattening it into a verdict.",
     "An interpretive lens on moral complexity, NOT an endorsement of any act: a reminder that "
     "honest witness can hold irreducible hardship, held within the cultural-formation layer.",
     ["her best thing", "she flies"],
     ["moral-complexity", "witness", "sacrifice", "ethics", "morrison", "beloved"]),
    (BEL,
     "The Clearing: communal self-love as lineage-rooted resistance",
     "lineage",
     "Baby Suggs' sermon in the Clearing commands a despised people to love their own flesh, "
     "hands, mouths, and hearts: 'love your heart, for this is the prize.' Self-love becomes a "
     "communal, ritual act of resistance against a world that despises the body, rooted in the "
     "Black-church tradition.",
     "Reclaiming worth can be a collective, ritual practice rooted in cultural tradition, not "
     "only an individual effort; community affirms the self the world denies.",
     "A lineage/cultural lens (the Black-church Clearing tradition): self-worth affirmed "
     "communally, held interpretively within BJ's cultural-formation layer, not as a program.",
     ["love your heart", "flesh that needs to be loved"],
     ["self-love", "black-church", "ritual", "lineage", "morrison", "beloved"]),
    (BEL,
     "Claiming ownership of the freed self",
     "operator-doctrine",
     "Baby Suggs' hard-won insight: 'Freeing yourself was one thing; claiming ownership of "
     "that freed self was another.' Legal or physical freedom is only the start; the harder, "
     "ongoing work is taking full possession of one's own life and worth.",
     "Liberation is not the finish line; the real work is claiming ownership of the freed self "
     "(your time, judgment, and worth) after the external constraint is gone.",
     "A resonant lens for BJ's current build-mode: securing freedom (optionality) is one "
     "thing; actively owning and directing that freed self is the harder, continuing work, "
     "held interpretively against the brief.",
     ["claiming ownership of that freed self", "freeing yourself was one thing"],
     ["self-ownership", "freedom", "agency", "operator-doctrine", "morrison", "beloved"]),
    (BEL,
     "Form as witness: the fractured structure and 'not a story to pass on'",
     "aesthetics",
     "Morrison's non-linear, fragmented, circling structure enacts how trauma resists tidy "
     "narrative, and the closing refrain 'It was not a story to pass on' holds the paradox of "
     "bearing witness to what is almost unspeakable. Form and meaning are inseparable; the "
     "telling embodies the difficulty of the told.",
     "Form can carry meaning that content alone cannot; how a thing is structured and told is "
     "part of what it means.",
     "A craft lens for BJ's image/work-making: structure and form are not decoration but "
     "carry meaning, held interpretively within the aesthetics layer.",
     ["not a story to pass on", "disremembered and unaccounted for"],
     ["form", "narrative-structure", "witness", "aesthetics", "morrison", "beloved"]),
    # ---------- Jonathan Livingston Seagull (Bach) · 4 ----------
    (SEA,
     "Mastery through relentless, joyful practice",
     "operator-doctrine",
     "Jonathan refuses the Flock's bare-survival flying and obsessively practices speed and "
     "control, learning 'more about speed in a week than the fastest gull alive.' Mastery comes "
     "from relentless, self-directed, joyful repetition far beyond what the group requires.",
     "Excellence is built by relentless self-directed practice past the point others stop; the "
     "drive to master a craft for its own sake compounds into rare skill.",
     "A practice/mastery lens for BJ: deep skill comes from reps pursued well past the "
     "good-enough line, held interpretively (a pattern about craft, not a directive about "
     "which craft).",
     ["learning to fly", "the speed was joy"],
     ["mastery", "practice", "craft", "operator-doctrine", "bach", "seagull"]),
    (SEA,
     "The cost of pursuing excellence beyond the flock",
     "culture",
     "The Breakfast Flock casts Jonathan out for caring about flight rather than food; pursuing "
     "excellence beyond the group's norms is treated as deviance. The fable reads the social "
     "cost of nonconformity and the loneliness of the one who reaches past consensus.",
     "Pursuing excellence beyond a group's norms often incurs social cost; the outlier who "
     "cares about the craft itself is frequently misunderstood by the consensus.",
     "An interpretive lens on the social cost of going past consensus, useful as a pattern for "
     "any operator who pursues a higher standard, held against the brief, not as a directive.",
     ["why is it so hard", "the Flock"],
     ["nonconformity", "outlier", "social-cost", "culture", "bach", "seagull"]),
    (SEA,
     "Craft as its own reward: the pursuit of perfection",
     "aesthetics",
     "Jonathan flies not for utility but because 'the speed was power, and the speed was joy, "
     "and the speed was pure beauty.' The fable frames the disciplined pursuit of perfection in "
     "a craft as intrinsically worthwhile, beyond any external payoff.",
     "Craft pursued for its own beauty and excellence, not only for utility, is a legitimate "
     "and durable motivation; perfection of the work can be its own reward.",
     "A craft-level lens for BJ: pursuit of excellence for its own sake (not only ROI) is a "
     "real motivation, held interpretively within the aesthetics layer.",
     ["the speed was pure beauty", "touched excellence in his learning"],
     ["perfection", "craft", "intrinsic-motivation", "aesthetics", "bach", "seagull"]),
    (SEA,
     "Read the parable at the craft level, not as a belief system",
     "culture",
     "Part Three turns Jonathan into a messiah figure with disciples, and the book was widely "
     "received as quasi-spiritual self-help. The disciplined reading takes the craft/aspiration "
     "metaphor (practice, excellence, nonconformity) and explicitly declines to literalize it "
     "into a belief system or a self-help doctrine.",
     "Take the transferable craft/aspiration metaphor from a parable while refusing to "
     "literalize it into doctrine; distinguish a useful figure from a belief system.",
     "Explicit guardrail for this lane: Seagull is read at the cultural/craft level (mastery, "
     "nonconformity, excellence), NOT adopted as faith or self-help doctrine for BJ or the OS; "
     "the metaphor is a lens, not a creed.",
     ["touched excellence in his learning", "we can be free"],
     ["metaphor", "reading-discipline", "anti-doctrine", "culture", "bach", "seagull"]),
    # ---------- Synthesis · 2 ----------
    (BEL,
     "Synthesis: literature as the humanistic-formation counterweight",
     "culture",
     "LITERARY_RECOVERY pairs two opposite registers, Beloved's witness to historical trauma "
     "and lineage and Seagull's aspiration to mastery and excellence, as the humanistic-"
     "formation and cultural-lineage layer the operator/AI-build canon is read against (the "
     "cultural spine and conscience the literary lanes established). The works supply meaning, "
     "memory, and moral weight that the operating canon alone does not.",
     "Keep a humanistic-formation layer (memory, lineage, moral witness, the pursuit of "
     "excellence) alongside the operating canon, as the cultural counterweight that keeps the "
     "work grounded in meaning.",
     "For BJ, these works are the cultural-formation counterweight to the operator/AI canon, "
     "held interpretively against CURRENT_OPERATOR_REALITY_BRIEF, not a turn toward literary "
     "criticism as a business.",
     ["the cultural spine", "not a story to pass on"],
     ["synthesis", "humanistic-formation", "cultural-spine", "culture", "morrison", "literary-recovery"]),
    (SEA,
     "Synthesis: the interpretive lens and the optionality guardrail",
     "operator-doctrine",
     "The lane's discipline: extract the transferable patterns (lineage and inherited weight, "
     "collective memory, ethical witness, self-ownership after liberation, mastery through "
     "practice, the cost of nonconformity, craft as its own reward) as an interpretive / "
     "cultural pattern library, while refusing to turn the OS into literary criticism, to "
     "literalize Seagull into a belief system, or to set any brand direction. The works are a "
     "lens, not a creed and not a plan.",
     "Mine literature for transferable human patterns while holding it as interpretation, not "
     "doctrine; the value is the lens, not a conversion into criticism, faith, or self-help.",
     "This synthesizes the lane for BJ: an interpretive cultural toolkit (memory, lineage, "
     "witness, self-ownership, mastery) held against CURRENT_OPERATOR_REALITY_BRIEF, with "
     "photography one option among several and no final SNIPED / SNIPED Media / BASEPLATE "
     "direction set.",
     ["a lens, not a creed", "one option among several"],
     ["synthesis", "interpretive-lens", "optionality", "operator-doctrine", "bach", "literary-recovery"]),
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
    forb = [d for d in ("literary", "identity", "memory", "trauma", "freedom", "myth",
                        "faith", "self-help") if d in doms]
    print("forbidden domains present:", forb or "NONE")
    mx = max(len(q.split()) for r in lines for q in r["direct_quotes"])
    print("longest quote words:", mx)


if __name__ == "__main__":
    main()
