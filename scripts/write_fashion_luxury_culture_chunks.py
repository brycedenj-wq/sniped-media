#!/usr/bin/env python3
"""Write FASHION_LUXURY_CULTURE_CHUNKS.jsonl · 13 curated chunks · 4 sources.

batch_id: FASHION_LUXURY_CULTURE · chunk_id: FASHION_LUXURY_CULTURE_NNN
The fashion-history / memoir / taste / craft register (the SECOND split lane).
Existing domains only (aesthetics anchor). No new domain. `taste` reused
(warranted, not created). No em-dashes. Curated fashion/luxury CULTURE and
taste-systems extraction (NOT fashion-history/memoir/gossip/lifestyle summary).
Decision-neutral: NOT a directive and NOT a finalized SNIPED brand. Guardrail in
every chunk.
"""
import json
import os

OUT = os.path.expanduser(
    "~/AI-Brain-Refinery/01_KNOWLEDGE_BASE/batches/FASHION_LUXURY_CULTURE_CHUNKS.jsonl")

DRAKE = ("The Beautiful Fall", "the_beautiful_fall_drake.txt", "Alicia Drake")
TALLEY = ("The Chiffon Trenches", "the_chiffon_trenches_talley.txt", "Andre Leon Talley")
DIOR_AUTO = ("Dior by Dior", "dior_by_dior_dior.txt", "Christian Dior")
DIOR_DICT = ("The Little Dictionary of Fashion", "the_little_dictionary_of_fashion_dior.txt", "Christian Dior")

GUARD = (" Read against CURRENT_OPERATOR_REALITY_BRIEF as decision-support and "
         "pattern-library only, not doctrine and not a directive: not a directive that "
         "BJ become a fashion brand, luxury influencer, streetwear founder, lifestyle "
         "creator, designer persona, clout account, or aesthetics-only operator. Fashion "
         "and luxury culture are held as symbolic value, taste systems, status architecture, "
         "cultural signaling, craft, creative discipline, and visual-cultural perception. No "
         "final SNIPED, SNIPED Media, or BASEPLATE direction; photography remains one option "
         "among several.")

# (source, domain, concept, summary, usable_principle, relevance_lead, quotes, tags)
ROWS = [
    # ---- THE BEAUTIFUL FALL (Drake) · 4 ----
    (DRAKE, "aesthetics",
     "Aesthetic authority: the implicit standard that disciplines a scene",
     "Drake shows how by the early 1970s image became the governing idea of Paris fashion, and how a "
     "single figure's taste could set an unspoken aesthetic standard for everyone around him. Around "
     "Saint Laurent there was an implicit aesthetic responsibility: no one was told the rules, yet no "
     "woman entered his studio less than impeccable, because the standard was understood and self-"
     "enforced.",
     "A strong, consistent aesthetic standard can discipline a whole circle without being announced; "
     "people calibrate to the implicit bar once it is unmistakably set.",
     "BJ can see that a clear, exacting aesthetic standard becomes self-enforcing in the people around "
     "it, a lesson about setting an implicit bar rather than policing rules, held as analysis.",
     ["image was both the word"],
     ["aesthetic-authority", "implicit-standard", "presentation", "image", "visual-perception"]),

    (DRAKE, "status",
     "The designer-as-star: from dressmaker to symbolic figure",
     "Drake charts the shift in which Paris designers stopped being purveyors of grand wardrobes and "
     "emerged as stars in their own right, puissant style arbiters and creators of glamour, drawing on "
     "the myth and mystery of Paris couture. The person and the persona, not just the product, became "
     "the locus of status and desire.",
     "In a symbolic-value field the maker can become the symbol; personal authority and persona can "
     "carry status that the artifact alone cannot.",
     "BJ can read how a maker becomes a symbolic figure (status migrating from product to person), a "
     "dynamic to understand rather than a directive to build a persona or chase fame.",
     ["stars in their own right", "puissant style arbiters"],
     ["designer-as-star", "persona", "symbolic-capital", "personal-authority", "status"]),

    (DRAKE, "founder-psychology",
     "Rivalry and two temperaments: discipline versus torment",
     "At the center of Drake's account are two rivals with opposite temperaments: Lagerfeld, armored, "
     "prolific, and relentlessly productive, and Saint Laurent, the tormented, anguished genius whose "
     "work cost him dearly. The lifelong rivalry between them functioned as an engine, each measuring "
     "himself against the other across decades.",
     "A worthy rival can be a productivity engine, and there is more than one viable temperament for a "
     "creative life (steady armored output or volatile intense genius); know which is yours.",
     "BJ can recognize rivalry as a possible engine and the two temperaments as a mirror for his own "
     "working style (sustainable output versus intense bursts), held as self-knowledge, not a script.",
     ["the two rivals"],
     ["rivalry", "temperament", "discipline-vs-torment", "creative-engine", "founder-psychology"]),

    (DRAKE, "culture",
     "The scene as a creative resource: density, milieu, and fascination",
     "Drake renders 1970s Paris fashion as a dense social scene (the Cafe de Flore, the nightclub Le "
     "Sept, the muses and hangers-on) that was not background but raw material. Designers do not create "
     "in a vacuum; they need relentless stimulation, innovation, and objects of fascination, and the "
     "concentrated milieu supplied exactly that.",
     "Creative output depends on the density and quality of the scene around the work; cultivating a "
     "rich milieu is part of the production, not a distraction from it.",
     "BJ can read scene density as a creative input (proximity to a rich, specific cultural circle "
     "feeds the work), a pattern to weigh decision-neutrally, not a mandate to chase nightlife or "
     "glamour.",
     ["do not create in a vacuum", "myth and mystery"],
     ["scene", "milieu", "cluster", "cultural-density", "stimulation"]),

    # ---- THE CHIFFON TRENCHES (Talley) · 3 ----
    (TALLEY, "taste",
     "Taste formation: built from outside through obsessive study",
     "Talley describes building world-class taste from the segregated American South, far outside the "
     "inner circle, through obsessive study: the city library, classical music, and a hefty diet of "
     "fashion glossies, where his world became the glossy pages of Vogue. Taste here is cultivated and "
     "learned, an act of deliberate self-education, not an inheritance of birth or money.",
     "Taste can be built deliberately from the outside by immersing in the best examples until the eye "
     "is trained; it is learnable, not merely inherited.",
     "BJ can treat taste as trainable through deep immersion in excellent work rather than as a fixed "
     "endowment, an encouraging and transferable pattern for any visual operator.",
     ["hefty diet of fashion glossies", "glossy pages of Vogue"],
     ["taste-formation", "self-education", "immersion", "outsider", "the-eye"]),

    (TALLEY, "status",
     "Editorial status and access: apprenticing into a closed world",
     "Talley's entry to fashion ran through proximity to power: an unpaid, highly selective "
     "apprenticeship under Diana Vreeland, the fashion empress, and later the orbit of Vogue and Anna "
     "Wintour. Access and editorial status were gained by attaching himself to the gatekeepers and "
     "learning at close range, then becoming a gatekeeper of taste himself.",
     "In a closed status field, access is often earned by proximity to the gatekeepers and by serving "
     "to learn, then converting that nearness into one's own authority.",
     "BJ can read how access and authority are earned in a closed world (proximity, apprenticeship, "
     "then earned standing), useful as social-architecture literacy, not a directive to chase a scene.",
     ["my own dream apprenticeship", "fashion empress"],
     ["editorial-status", "access", "apprenticeship", "gatekeepers", "proximity"]),

    (TALLEY, "ethics",
     "Loyalty, dignity, and the human cost beneath the glamour",
     "The memoir's title names the brutality under the beauty: the chiffon trenches, a glamorous world "
     "that can be cold, transactional, and cruel. Talley holds loyalty as a noble human endeavor and "
     "insists on personal dignity even after being discarded by people he served, refusing to let a "
     "status world define his worth.",
     "Glamour and status fields can be ruthless; guard loyalty and personal dignity deliberately, "
     "because the field will not supply them and can withdraw belonging without warning.",
     "BJ can hold loyalty and self-respect as deliberate commitments independent of any status field's "
     "approval, a values anchor that matters more as visibility grows, held as principle.",
     ["a noble human endeavor"],
     ["loyalty", "dignity", "human-cost", "integrity", "belonging"]),

    # ---- DIOR BY DIOR (Christian Dior) · 3 ----
    (DIOR_AUTO, "aesthetics",
     "Craft justifies the effect: workmanship beneath the beauty",
     "Dior insists that the apparently effortless beauty of his clothes rested on real, demanding "
     "craft: an ethereal appearance is only achieved by elaborate workmanship, and he wanted dresses "
     "constructed like buildings, moulded and structured with old, nearly forgotten techniques. The "
     "visible grace is the surface of substantial, invisible labor.",
     "Apparent effortlessness is manufactured by hidden, rigorous craft; the lightness clients see is "
     "paid for by structural work they never see.",
     "BJ can hold that a polished, effortless-looking result is backed by exacting unseen work, "
     "reinforcing that the visible ease of good output is earned by craft, not faked.",
     ["constructed like buildings", "elaborate workmanship"],
     ["craft", "workmanship", "structure", "effortlessness", "the-unseen-work"]),

    (DIOR_AUTO, "operator-doctrine",
     "Reconciling personality and discipline; the editing that destroys",
     "Dior describes the making of a collection as the reconciliation of two apparently irreconcilable "
     "forces, personality and discipline, and as an act of ruthless editing: first enthusiasm puts far "
     "too many toiles into execution, and later a great number must be destroyed so that the collection "
     "has variety yet never contradicts itself.",
     "Sustained creative work means holding personal vision and hard discipline together, and editing "
     "ruthlessly, overproducing then cutting most of it, so the final body of work coheres.",
     "BJ can apply the overproduce-then-cut discipline and the personality-plus-discipline pairing to "
     "his own creative output, a directly transferable operating pattern.",
     ["personality and discipline"],
     ["editing", "selection", "discipline", "coherence", "creative-process"]),

    (DIOR_AUTO, "strategy",
     "Reading the moment: conviction over the dictates of commerce",
     "Dior frames the New Look as a deliberate reaction to a poverty-stricken, ration-book era, "
     "answering a starved appetite for abundance and femininity rather than obeying commercial "
     "pressure. He rejects the idea that fashion varies according to the dictates of commerce, swearing "
     "that anything inspired by that consideration would have no chance of surviving; conviction and "
     "timing, not the market's instruction, drove the move.",
     "Read what the cultural moment is starved for and answer it from conviction; work driven only by "
     "commercial dictate tends not to last.",
     "BJ can weigh reading-the-moment plus conviction against pure market-chasing, a positioning lesson "
     "(answer a real cultural hunger) held as analysis, not a directive about any specific venture.",
     ["dictates of commerce", "no chance of surviving"],
     ["reading-the-moment", "conviction", "counter-positioning", "timing", "anti-commercial"]),

    # ---- THE LITTLE DICTIONARY OF FASHION (Christian Dior) · 2 ----
    (DIOR_DICT, "taste",
     "Elegance is not money: simplicity, care, and good taste",
     "In his aphoristic dictionary Dior reduces good dressing to fundamentals that cost nothing: "
     "simplicity, good taste and grooming, with elegance defined as the right combination of "
     "distinction, naturalness, care, and simplicity. Elegance is not dependent on money, he insists, "
     "and of all its parts the most important is care.",
     "Taste and elegance are mostly discipline, not budget; simplicity, care, and restraint produce "
     "more elegance than spending does.",
     "BJ can hold that taste and a refined result come from restraint and care rather than spend, a "
     "low-cost, high-leverage principle for any visual or presentation work.",
     ["Elegance is not dependent on money", "good taste and grooming"],
     ["elegance", "simplicity", "care", "restraint", "taste-not-money"]),

    (DIOR_DICT, "aesthetics",
     "Quality over quantity and individuality over slavish fashion",
     "Dior's standing rules are to put quality before quantity (one frock of good material rather than "
     "two of cheap fabric, buy little but make sure it is good) and to prize individuality over trend, "
     "since no elegant woman follows fashion slavishly and should ignore any new line that does not "
     "suit her. Curated quality and a true personal signature beat volume and conformity.",
     "Choose fewer, better things and edit toward a personal signature; quality and individuality "
     "outlast quantity and slavish trend-following.",
     "BJ can apply buy-little-buy-good and individuality-over-trend to building a body of work and a "
     "personal signature, a curation discipline held as transferable principle.",
     ["quality before quantity", "follows fashion slavishly"],
     ["quality-over-quantity", "individuality", "curation", "signature", "anti-trend"]),

    # ---- SYNTHESIS · 1 ----
    (DIOR_AUTO, "operator-doctrine",
     "Synthesis: the fashion/luxury culture and taste-systems toolkit",
     "Across the four sources a culture-side toolkit emerges to sit beside the strategy lane: taste is "
     "formed by immersion and trainable from outside (Talley); a maker can become a symbolic figure and "
     "a dense scene is a creative input (Drake); a strong aesthetic standard disciplines a circle and "
     "rivalry can drive output (Drake); craft justifies the visible effect, creative work means "
     "reconciling personality and discipline and editing ruthlessly, and conviction beats the dictates "
     "of commerce (Dior); and elegance is care and restraint, quality over quantity, individuality over "
     "slavish trend (Dior). It is a pattern-library for taste formation, cultural signaling, craft "
     "codes, presentation discipline, and personal authority.",
     "Combine taste-as-trainable, scene-as-input, aesthetic-standard-as-discipline, craft-beneath-the-"
     "effect, overproduce-then-edit, and quality-and-individuality into a culture-side perception and "
     "discipline toolkit, held as analysis rather than a brand to launch.",
     "BJ holds this as taste-formation, craft-discipline, and cultural-perception literacy for his "
     "build-mode stage, NOT a directive to become a fashion or luxury brand, a designer persona, or an "
     "aesthetics-only operator.",
     [],
     ["synthesis", "taste-systems", "craft-codes", "cultural-signaling", "operator-toolkit"]),
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
            "chunk_id": f"FASHION_LUXURY_CULTURE_{i:03d}",
            "batch_id": "FASHION_LUXURY_CULTURE",
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

    forbidden = {"luxury", "fashion", "style", "designer", "apparel", "streetwear",
                 "hype", "clout", "lifestyle", "influencer"}
    used = {r["domain"] for r in rows}
    assert not (used & forbidden), used & forbidden

    rows = [sweep(r) for r in rows]
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    assert chr(0x2014) not in blob, "em-dash found in output"

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"wrote {len(rows)} chunks to {OUT}")


if __name__ == "__main__":
    main()
