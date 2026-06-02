#!/usr/bin/env python3
"""Write STORYTELLING_NARRATIVE_CHUNKS.jsonl · 15 curated chunks · 4 sources.

batch_id: STORYTELLING_NARRATIVE · chunk_id: STORYTELLING_NARRATIVE_NNN
Existing domains only (aesthetics anchor). No new domain. No em-dashes.
Curated story-craft + visual-narrative pattern extraction (NOT chapter summary).
Identity optionality + Campbell-cultural-not-faith + Block-visual-operator guardrails in every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/STORYTELLING_NARRATIVE_CHUNKS.jsonl")

TRUBY = ("The Anatomy of Story", "anatomy_of_story_truby.txt", "John Truby")
CAMPBELL = ("The Hero with a Thousand Faces",
            "hero_with_a_thousand_faces_campbell.txt", "Joseph Campbell")
SNYDER = ("Save the Cat!", "save_the_cat_snyder.txt", "Blake Snyder")
BLOCK = ("The Visual Story", "visual_story_block.txt", "Bruce Block")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive "
         "that BJ become a screenwriter, myth-brand guru, novelist, film critic, "
         "narrative consultant, or self-help storyteller. No final SNIPED, SNIPED "
         "Media, or BASEPLATE direction; photography remains one option among several.")
CAMPBELL_CLAUSE = (" Campbell's myth and religion material is held strictly as "
                   "cultural and narrative pattern study, not a faith or spirituality lane.")
BLOCK_CLAUSE = (" Translated into practical visual-structure patterns for BJ's "
                "visual and operator work, not film-school theory.")

# Each tuple: (source, domain, concept, summary, usable_principle, relevance_lead, direct_quotes, tags)
ROWS = [
    # ---- TRUBY (4) ----
    (TRUBY, "aesthetics",
     "The story as an organic body and the designing principle",
     "Truby treats a story as a living body of interconnected subsystems (characters, plot, "
     "revelations, moral argument, story world) rather than a formula, with theme as the brain, "
     "character as the heart, and structure as the skeleton. Above the surface premise sits the "
     "designing principle: the single abstract idea (story process plus original execution) that "
     "organizes the whole and makes it greater than the sum of its parts.",
     "Build any communication as one organic system with a single organizing principle, not a pile "
     "of parts; find the one idea that makes the parts cohere and never lose sight of it.",
     "For BJ a shoot, a feed, or an offer reads as one organic body: define the single designing "
     "principle first, then let every frame and line serve it.",
     ["the seed of the story", "greater than the sum"],
     ["story-structure", "designing-principle", "organic-form", "composition", "coherence"]),

    (TRUBY, "operator-doctrine",
     "Desire versus need versus weakness: the engine beneath the surface",
     "Truby separates desire (the external goal the audience tracks on the surface) from need (the "
     "internal change required to overcome a weakness, hidden under the surface). Weakness and need "
     "are the foundation that makes change and payoff possible; opening on desire alone gives a fast "
     "start but kills the ending.",
     "Distinguish what an audience visibly wants from what they actually need to change; build from "
     "the hidden need, not just the surface want, or the payoff collapses.",
     "BJ can read a client or a market the same way: the stated desire is the visible goal, the real "
     "need is the deeper change, and durable work serves the need beneath the want.",
     ["Don't skip that first step"],
     ["desire-vs-need", "character-weakness", "payoff", "audience-psychology", "change"]),

    (TRUBY, "strategy",
     "The opponent defined structurally: competing for the same goal",
     "Truby argues the true opponent is not whoever looks evil but whoever competes with the hero for "
     "the very same goal, which forces direct, repeated conflict. Two characters chasing separate "
     "goals never truly collide, so there is no story; the real fight is often over which version of "
     "reality everyone will accept.",
     "Define a rivalry by the shared contested goal, not by surface villainy; competition over the "
     "same prize is what creates real stakes and tension.",
     "For BJ this is competitive positioning: the meaningful rival is whoever contests the same buyer, "
     "attention, or definition of value, not whoever merely looks like an enemy.",
     ["competing for the same goal"],
     ["opponent", "conflict", "competitive-positioning", "stakes", "structure"]),

    (TRUBY, "ethics",
     "Theme as moral argument expressed through the character web",
     "For Truby theme is not subject matter but the author's moral vision of how to live well or "
     "badly, expressed through characters acting in the plot rather than stated outright. Each "
     "opponent and ally is a variation on the same moral problem, so the character web argues the "
     "theme structurally instead of preaching it.",
     "Argue a value through structure and contrasting actors, not through statement; let the "
     "arrangement of choices carry the moral vision so it is felt rather than lectured.",
     "BJ can let a body of work make its point through the pattern of choices it shows, not through "
     "slogans; the moral vision lands when it is built into the structure.",
     ["theme is your moral vision"],
     ["theme", "moral-argument", "character-web", "values", "show-not-tell"]),

    # ---- CAMPBELL (4) ----
    (CAMPBELL, "culture",
     "The monomyth: departure, initiation, return as a cross-cultural pattern",
     "Campbell observes one shape-shifting but constant story recurring across cultures and eras: a "
     "hero ventures from the ordinary world into a region of wonder, wins a decisive victory against "
     "fabulous forces, and returns able to benefit others. He frames this departure-initiation-return "
     "arc as a recurring human narrative structure, illustrated through many traditions.",
     "A small set of deep narrative patterns recurs everywhere; recognizing the shared structure lets "
     "you build on what audiences already carry rather than inventing from zero.",
     "BJ can shape a sequence, a project arc, or a portfolio on the familiar departure-and-return "
     "spine audiences already recognize, gaining resonance without copying any single source.",
     ["A hero ventures forth", "boons on his fellow man"],
     ["monomyth", "departure-initiation-return", "cross-cultural-pattern", "structure", "resonance"]),

    (CAMPBELL, "culture",
     "The call to adventure and the refusal of the call",
     "The pattern opens with a call: a herald, often arriving by apparent chance, summons the hero "
     "and shifts the center of gravity from the known world to an unknown zone of treasure and danger. "
     "A common next beat is refusal, the folly of clinging to the old horizon even as it empties of "
     "value and the threshold approaches.",
     "Meaningful change starts with a disruptive call and is usually met first by avoidance; name the "
     "threshold honestly instead of retreating to a familiar comfort that has stopped paying.",
     "For BJ the call-and-refusal pattern is a lens on his own build-mode transitions: a summons to a "
     "new stage, the pull to refuse it, and the cost of staying in an outgrown frame.",
     ["the call to adventure"],
     ["call-to-adventure", "refusal", "threshold", "transition", "narrative-stage"]),

    (CAMPBELL, "aesthetics",
     "The road of trials and the ultimate boon",
     "In the initiation phase the hero passes through a road of trials and ordeals, often aided by a "
     "guide, and ultimately wins a boon or elixir: the hard-won prize at the center of the journey. "
     "The boon is earned through the ordeal rather than seized cheaply, which is what gives it weight "
     "in the structure.",
     "Value that is visibly earned through trial reads as weightier than value handed over easily; "
     "structure the arc so the reward sits at the end of real difficulty.",
     "BJ can sequence work so the payoff frame, result, or reveal lands after visible effort, letting "
     "the difficulty of the road give the boon its meaning.",
     ["the ultimate boon"],
     ["road-of-trials", "ordeal", "boon", "earned-reward", "arc"]),

    (CAMPBELL, "operator-doctrine",
     "The return: master of the two worlds, freedom to live",
     "Campbell calls the return, bringing the boon back into ordinary life, often the hardest stage: "
     "the hero must re-enter common day and face misunderstanding while carrying something "
     "transformative. Mastery is the freedom to move between both worlds without confusing the "
     "principles of one with the other.",
     "Producing insight matters less than translating it back for people who did not take the journey; "
     "the discipline is moving between the new world and the ordinary one without losing either.",
     "BJ, loading a backend before going public, is in the return problem: the work only counts when "
     "its value is carried back and made legible to those who were not inside the build.",
     ["master of the two worlds", "freedom to live"],
     ["the-return", "master-of-two-worlds", "translation", "reintegration", "delivery"]),

    # ---- SNYDER (3) ----
    (SNYDER, "brand",
     "The logline: premise clarity before anything is built",
     "Snyder insists on nailing the logline or one-line first: a single sentence with built-in irony, "
     "a compelling mental picture of the whole movie, a sense of audience and cost, and a title that "
     "lands as a one-two punch. If you cannot say what it is, you are not ready to build it.",
     "Forge one ironic, vivid sentence that makes the whole thing visible before producing anything; "
     "clarity of premise beats cleverness of execution.",
     "BJ should be able to say what a project, offer, or shoot is in one sharp line; if the one-liner "
     "does not blossom in a listener's mind, the concept is not ready.",
     ["what is it?"],
     ["logline", "premise", "clarity", "message", "pitch"]),

    (SNYDER, "media-business",
     "The genres and give me the same thing, only different",
     "Snyder argues every film fits one of about ten primal genres (Monster in the House, Golden "
     "Fleece, Out of the Bottle, Rites of Passage, Buddy Love, Whydunit, and so on), each with its own "
     "rules. The market rewards the familiar primal type delivered with a genuinely fresh twist: the "
     "same thing, only different.",
     "Locate your work in a primal, already-understood category, then differentiate inside it; pure "
     "novelty confuses and pure copying bores.",
     "For BJ this is product and content framing: anchor an offer or series in a category buyers "
     "instantly grasp, then earn attention with one fresh, ownable difference.",
     ["the same thing, only different"],
     ["genre", "familiarity", "differentiation", "market-fit", "positioning"]),

    (SNYDER, "operator-process",
     "The beat sheet and the save-the-cat likability beat",
     "Snyder's fifteen-beat sheet (opening image, theme stated, catalyst, midpoint, all is lost, "
     "finale, final image, and the rest) is a repeatable structural map whose beats hit consistent "
     "marks regardless of length. The namesake save-the-cat beat is an early moment that makes the "
     "audience root for the protagonist before asking them to follow.",
     "Use a repeatable beat map to control pacing and earn buy-in early; give the audience a reason to "
     "root for the subject before you ask for their attention.",
     "BJ can run a consistent structural template across shoots or posts and front-load a likability "
     "or trust beat so attention is earned before the ask.",
     ["save the cat"],
     ["beat-sheet", "pacing", "structure-template", "likability", "audience-buy-in"]),

    # ---- BLOCK (3) ----
    (BLOCK, "aesthetics",
     "The seven basic visual components",
     "Block identifies seven basic visual components present in every still or moving picture: space, "
     "line, shape, tone, color, movement, and rhythm. Actors, locations, props, and scenery are all "
     "made of these components, and each one communicates mood and gives a picture its visual "
     "structure.",
     "Every image is built from a small, controllable vocabulary of visual components; structure them "
     "deliberately rather than leaving them to accident.",
     "BJ already manipulates space, line, shape, tone, color, movement, and rhythm in photographs; "
     "naming them as a fixed set turns instinct into a deliberate control panel.",
     ["the basic visual components"],
     ["visual-components", "space-line-shape", "tone-color", "composition", "control"]),

    (BLOCK, "aesthetics",
     "Contrast and affinity: the key to visual intensity",
     "Block's master principle is contrast and affinity: contrast means difference, affinity means "
     "similarity, and every visual component can be described in those terms. The greater the contrast "
     "in a component the more the visual intensity rises; the greater the affinity the more it falls, "
     "which drives the audience's emotional and physical reaction.",
     "Control intensity by dialing contrast up and affinity down (or the reverse) across any visual "
     "component; difference excites, similarity calms.",
     "BJ can set the energy of a frame or a feed on purpose by raising contrast where he wants "
     "intensity and increasing affinity where he wants calm.",
     ["contrast means difference", "affinity means similarity"],
     ["contrast-and-affinity", "visual-intensity", "tone", "color", "emotional-impact"]),

    (BLOCK, "aesthetics",
     "Visual progressions matched to story structure",
     "Block stresses that the screen is never empty, so visual structure should be controlled like a "
     "writer controls sentences. A visual progression begins as one thing and intensifies (the birds "
     "gathering, a fight sequence escalating, the Godfather climax), and the strongest work aligns "
     "rising visual intensity with the rising structure of the story.",
     "Plan visual intensity as a progression that tracks the story's build, escalating contrast as "
     "stakes rise instead of letting the frame drift uncontrolled.",
     "BJ can structure a sequence or a series so visual intensity climbs with the narrative arc, "
     "matching the strongest images to the highest-stakes moments.",
     ["the screen is never empty"],
     ["visual-progression", "intensity-curve", "story-visual-alignment", "sequencing", "build"]),

    # ---- SYNTHESIS (1) ----
    (TRUBY, "operator-doctrine",
     "Synthesis: the story and visual-narrative toolkit for an operator",
     "Across the four sources a single toolkit emerges: build one organic structure around a designing "
     "principle (Truby), use the deep departure-and-return pattern audiences already carry (Campbell), "
     "say clearly what it is and place it in a familiar category with a fresh twist (Snyder), and "
     "control visual intensity through contrast and affinity matched to the story's build (Block). It "
     "is a pattern-library for shaping attention, meaning, sequence, contrast, and emotional "
     "comprehension.",
     "Combine structural coherence, a recognizable arc, premise clarity, and deliberate visual "
     "intensity to shape attention and meaning, treating all of it as transferable craft.",
     "BJ holds this as a craft toolkit for his visual and operator work: shape sequence, contrast, "
     "and comprehension on purpose, without becoming a screenwriter or myth brand.",
     [],
     ["synthesis", "story-craft", "visual-structure", "attention", "operator-toolkit"]),
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
    for i, (src, domain, concept, summary, principle, rel_lead, quotes, tags) in enumerate(ROWS, 1):
        title, sfile, author = src
        relevance = rel_lead + GUARD
        if src is CAMPBELL:
            relevance += CAMPBELL_CLAUSE
        if src is BLOCK:
            relevance += BLOCK_CLAUSE
        r = {
            "chunk_id": f"STORYTELLING_NARRATIVE_{i:03d}",
            "batch_id": "STORYTELLING_NARRATIVE",
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
        }
        rows.append(r)

    # quote discipline: <= 6 words each
    for r in rows:
        for q in r["direct_quotes"]:
            assert len(q.split()) <= 6, f"quote too long in {r['chunk_id']}: {q}"

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
