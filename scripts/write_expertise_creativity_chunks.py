#!/usr/bin/env python3
"""Write EXPERTISE_CREATIVITY_CHUNKS.jsonl · 11 curated chunks · 4 sources.

batch_id: EXPERTISE_CREATIVITY · chunk_id: EXPERTISE_CREATIVITY_NNN
The deliberate-practice / mastery / creative-craft / visual-perception register · the
FOURTH and FINAL of the four ADJACENT_TIER_2_CLUSTERS sub-lanes. Existing domains
only (operator-doctrine anchor). No new domain. `creativity` does NOT exist and is
NOT created (creative/craft material routes to aesthetics + operator-doctrine);
`systems` (6) NOT used/grown. No em-dashes. Curated expertise/creative-skill
extraction (NOT a creativity-book chapter summary, art-theory summary, or self-help
manifesto). Decision-neutral: NOT a directive and NOT a SNIPED brand. Guardrail in
every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/EXPERTISE_CREATIVITY_CHUNKS.jsonl")

WOS = ("Ways of Seeing", "ways_of_seeing_berger.txt", "John Berger")
TCA = ("The Creative Act", "the_creative_act_rubin.txt", "Rick Rubin")
PEAK = ("Peak", "peak_ericsson_pool.txt", "Anders Ericsson and Robert Pool")
TIO = ("Talent Is Overrated", "talent_is_overrated_colvin.txt", "Geoff Colvin")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that BJ "
         "become a creativity coach, expert-brand persona, productivity influencer, "
         "artist-guru, art-theory account, self-help creator, or mastery influencer. "
         "Expertise and creative-skill material is held as trained perception, craft "
         "standards, practice design, feedback loops, skill acquisition, and visual-cultural "
         "literacy. No final SNIPED, SNIPED Media, or BASEPLATE direction; photography "
         "remains one option among several.")

# (source, domain, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- WAYS OF SEEING (Berger) · 2 ----
    (WOS, "aesthetics",
     "Seeing is active and trained, not neutral",
     "Berger opens with the claim that seeing comes before words and is never a neutral recording: what "
     "we see is shaped by what we know and believe, and we never look at just one thing but always at "
     "the relation between things and ourselves. Perception is an active, learned, situated act, so the "
     "eye can be trained and is always already interpreting.",
     "Treat seeing as a trainable, interpretive act shaped by knowledge and assumption, not a neutral "
     "recording; what you notice is a skill, and it is always relational.",
     "For BJ, a visual operator, this frames perception itself as a trainable craft (the eye is made, "
     "not given), held as analysis of how seeing works, not an art-theory identity.",
     ["Seeing comes before words"],
     ["trained-perception", "seeing", "active-vision", "interpretation", "aesthetics"]),

    (WOS, "culture",
     "Images carry ideology; publicity manufactures glamour",
     "Berger argues images are never innocent: conventions of depiction encode social power (men act and "
     "women appear), and mechanical reproduction strips an image of its original context and meaning. "
     "Publicity is the engineered descendant of oil painting, and its job is manufacturing glamour, "
     "selling the viewer an enviable transformed self rather than the product itself.",
     "Read any image for the ideology and the desire it encodes; publicity sells an envied future self, "
     "and reproduction detaches an image from its original meaning.",
     "BJ can read images (his own and others') for the social desire and ideology they carry, a "
     "visual-culture literacy lens held as analysis, not a directive to make advertising or chase "
     "glamour.",
     ["men act and women appear", "manufacturing glamour"],
     ["image-literacy", "ideology", "publicity", "glamour", "visual-culture"]),

    # ---- THE CREATIVE ACT (Rubin) · 3 ----
    (TCA, "aesthetics",
     "Creative receptivity: everyone is a creator tuning to what is available",
     "Rubin frames creativity as receptivity rather than generation: everyone is a creator, and the "
     "artist's job is to develop sensitive antennae that tune in to the ideas and energy already present "
     "in the world. The work is less about inventing from nothing than about perceiving and selecting "
     "what is resonating and letting it through.",
     "Treat creative work as receiving and selecting (tuning sensitive antennae to what resonates) more "
     "than forcing output; cultivate perception as the primary creative faculty.",
     "BJ can hold creativity as trained receptivity and perception rather than pressure-to-produce, a "
     "craft-orientation held as analysis, not a directive to become an artist-guru.",
     ["Everyone Is a Creator", "antennae"],
     ["receptivity", "antennae", "tuning-in", "perception", "aesthetics"]),

    (TCA, "operator-doctrine",
     "Make for yourself; awareness is the practice",
     "Rubin's discipline is to make the work for yourself, by your own standard, rather than for an "
     "imagined audience (the moment you make it for someone else you are in commerce, not art), and to "
     "treat creative life as an ongoing practice of paying attention. The standard is internal and the "
     "method is sustained awareness, not technique alone.",
     "Make to your own taste and standard rather than a guessed audience, and treat sustained attention "
     "as the core practice; the bar is internal.",
     "BJ can hold make-for-yourself and awareness-as-practice as a craft discipline for any creative "
     "output, a transferable operating stance, not a directive.",
     ["for yourself", "paying attention"],
     ["self-standard", "awareness", "practice", "taste", "operator-doctrine"]),

    (TCA, "founder-psychology",
     "Working with self-doubt: lower the stakes to free the work",
     "Rubin treats self-doubt as a permanent companion rather than a problem to eliminate, and offers "
     "lowering the stakes as a key strategy: when we stop treating a piece as the most important thing "
     "in our life, the pressure that blocks the work eases and play returns. The inner state, not just "
     "skill, governs whether the work can happen.",
     "Expect self-doubt as constant and lower the stakes deliberately (this is not the most important "
     "thing) to unblock the work; manage the inner state, not just the technique.",
     "BJ can use lower-the-stakes and accept-the-doubt as a self-management pattern for his own creative "
     "work, a psychological lens held as analysis, not a directive.",
     ["Self-Doubt", "lower the stakes"],
     ["self-doubt", "lower-the-stakes", "inner-state", "play", "founder-psychology"]),

    # ---- PEAK (Ericsson & Pool) · 3 + synthesis ----
    (PEAK, "operator-process",
     "Purposeful and deliberate practice: out of the comfort zone with feedback",
     "Ericsson distinguishes mere repetition from purposeful practice: well-defined specific goals, full "
     "focus, immediate feedback, and constantly pushing just beyond the comfort zone. Deliberate "
     "practice adds a field with known best practices and a teacher who can guide it; it is the design "
     "of practice, not the hours alone, that builds skill.",
     "Design practice to be purposeful: specific goals, full attention, immediate feedback, and "
     "repeated reaching just past the comfort zone; structure beats raw hours.",
     "BJ can structure his own skill-building as purposeful practice (targeted reps, feedback, edge of "
     "ability) rather than passive repetition, a directly usable method.",
     ["purposeful practice", "comfort zone"],
     ["deliberate-practice", "purposeful-practice", "feedback", "comfort-zone", "operator-process"]),

    (PEAK, "mental-models",
     "Mental representations: what expertise actually is",
     "Ericsson argues the core of expertise is rich mental representations: highly developed, "
     "domain-specific internal patterns that let experts perceive meaning, anticipate, and act where "
     "novices see noise. Deliberate practice works largely by building better and better "
     "representations, which then guide still more effective practice.",
     "Build richer mental representations of your domain (the patterns experts see); expertise is "
     "largely better internal models, and they compound with practice.",
     "BJ can treat building rich domain representations (seeing the patterns) as the real target of "
     "practice, a model of how skill works, held as analysis.",
     ["mental representations"],
     ["mental-representations", "expertise", "pattern-recognition", "domain-models", "mental-models"]),

    (PEAK, "operator-doctrine",
     "Skill is built, not born: the gift is the practice",
     "Ericsson's central claim challenges the idea of fixed innate talent: with rare exceptions, "
     "world-class ability is built through years of deliberate practice exploiting the brain and body's "
     "adaptability, not bestowed by a gift at birth. Believing ability is innate becomes a "
     "self-limiting prophecy; treating it as buildable opens the path.",
     "Treat high ability as buildable through deliberate practice rather than fixed by innate talent; "
     "the belief itself shapes how far you go.",
     "BJ can hold ability-is-built as an operating belief for his own skill development, an empowering "
     "frame held as analysis, not a mastery-influencer directive.",
     ["deliberate practice", "innate talent"],
     ["skill-is-built", "adaptability", "growth", "anti-talent-myth", "operator-doctrine"]),

    # ---- TALENT IS OVERRATED (Colvin) · 2 ----
    (TIO, "operator-doctrine",
     "Talent is overrated: practice is what really separates",
     "Colvin's thesis is that talent is overrated as an explanation of great performance: what really "
     "separates world-class performers is sustained deliberate practice plus deep domain knowledge, not "
     "an inborn gift. He shows that famous prodigies usually had enormous structured practice behind "
     "them, and that the talent story mostly excuses us from the work.",
     "Discount the talent explanation and look for the deliberate practice behind great performance; the "
     "talent story usually hides years of structured work.",
     "BJ can read top performance as accumulated practice rather than gift (and discount his own 'not "
     "talented enough' excuses), a decision-neutral lens, not a directive.",
     ["Talent Is Overrated", "really separates"],
     ["talent-myth", "deliberate-practice", "performance", "domain-knowledge", "operator-doctrine"]),

    (TIO, "founder-psychology",
     "The multiplier: intrinsic drive sustains the practice",
     "Colvin asks what sustains people through years of hard, un-fun deliberate practice and finds it in "
     "what he calls the multiplier effect: an early bit of encouragement or success feeds intrinsic "
     "motivation, which fuels more practice, which produces more success, compounding into a "
     "self-reinforcing drive. The passion is largely built by the loop, not purely born.",
     "Recognize that intrinsic drive is grown by a multiplier loop (small success feeds motivation feeds "
     "practice); engineer early wins to compound the motivation that sustains hard practice.",
     "BJ can use the multiplier loop to sustain his own long practice (stack early wins to feed intrinsic "
     "drive), a motivation pattern held as analysis, not a directive.",
     ["The Multiplier Effect", "intrinsic"],
     ["multiplier-effect", "intrinsic-motivation", "drive", "compounding", "founder-psychology"]),

    # ---- SYNTHESIS · 1 (attributed to Peak) ----
    (PEAK, "operator-doctrine",
     "Synthesis: the expertise / creative-skill operator toolkit",
     "Across the four sources a skill-building toolkit emerges: seeing is a trainable, ideology-laden act "
     "and images can be read for the desire they encode (Berger); creativity is trained receptivity made "
     "for your own standard, with self-doubt managed by lowering the stakes (Rubin); and world-class "
     "ability is built, not born, through purposeful deliberate practice that grows rich mental "
     "representations, sustained by an intrinsic-motivation multiplier (Ericsson, Colvin). It is a "
     "pattern-library for trained perception, craft standards, practice design, and skill acquisition.",
     "Combine trained perception, image literacy, creative receptivity, self-doubt management, "
     "deliberate practice, mental representations, and the motivation multiplier into a skill-building "
     "toolkit, held as analysis rather than a creative-coach identity.",
     "BJ holds this as trained-perception and skill-acquisition literacy for his build-mode stage, NOT a "
     "directive to become a creativity coach, an artist-guru, or a mastery influencer.",
     [],
     ["synthesis", "trained-perception", "deliberate-practice", "craft-standards", "operator-toolkit"]),
]


def sweep(obj):
    em = chr(0x2014)
    if isinstance(obj, str):
        return obj.replace(em, " · ")
    if isinstance(obj, list):
        return [sweep(x) for x in obj]
    if isinstance(obj, dict):
        return {k: sweep(v) for k, v in obj.items()}
    return obj


def main():
    rows = []
    for i, (src, domain, concept, summary, principle, rel, quotes, tags) in enumerate(ROWS, 1):
        title, sfile, author = src
        r = {
            "chunk_id": f"EXPERTISE_CREATIVITY_{i:03d}",
            "batch_id": "EXPERTISE_CREATIVITY",
            "source_title": title,
            "source_file": sfile,
            "author": author,
            "domain": domain,
            "concept": concept,
            "summary": summary,
            "usable_principle": principle,
            "sniped_relevance": rel + GUARD,
            "direct_quotes": quotes,
            "tags": tags,
        }
        rows.append(r)

    for r in rows:
        for q in r["direct_quotes"]:
            assert len(q.split()) <= 6, f"quote too long in {r['chunk_id']}: {q}"

    forbidden = {"creativity", "expertise", "innovation", "productivity", "self-help",
                 "systems", "management", "consulting", "service", "business"}
    used = {r["domain"] for r in rows}
    assert not (used & forbidden), used & forbidden
    assert "creativity" not in used and "systems" not in used

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
