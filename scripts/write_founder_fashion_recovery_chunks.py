#!/usr/bin/env python3
"""Write FOUNDER_FASHION_RECOVERY_CHUNKS.jsonl from the 2 recovered memoirs.

Grace: A Memoir (Coddington) + Total Recall (Schwarzenegger). 12-field canonical
schema. Existing domains only. NO new domain (fashion/fashion-luxury/celebrity-brand/
memoir NOT created). Per-source attribution. Total Recall weighted heavier.
Grace anchored on the creative-director's eye (distinct from Vreeland's editor authority);
Total Recall on the personal operator-arc (distinct from company-founder histories).
Every chunk carries the CURRENT_OPERATOR_REALITY_BRIEF reference + identity-optionality
guardrail (GUARD). Em-dash swept. No master-file writes.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "01_KNOWLEDGE_BASE" / "batches" / "FOUNDER_FASHION_RECOVERY_CHUNKS.jsonl"
BATCH = "FOUNDER_FASHION_RECOVERY"

GRACE_TITLE = "Grace: A Memoir"
GRACE_AUTHOR = "Grace Coddington"
GRACE_SRC = "grace_a_memoir_coddington.txt"
TR_TITLE = "Total Recall: My Unbelievably True Life Story"
TR_AUTHOR = "Arnold Schwarzenegger"
TR_SRC = "total_recall_schwarzenegger.txt"

GUARD = (" Held as a pattern-library / decision-support lens, read against "
         "CURRENT_OPERATOR_REALITY_BRIEF: a model of how a singular operator builds taste, "
         "method, and a body of work, NOT a directive that BJ become a fashion operator, "
         "memoirist, or celebrity/personal brand. No final SNIPED, SNIPED Media, or BASEPLATE "
         "direction is set here; photography remains one option among several.")

# (source_tuple, concept, domain, summary, usable_principle, sniped_relevance_core, [quotes], [tags])
GR = (GRACE_TITLE, GRACE_AUTHOR, GRACE_SRC)
TR = (TR_TITLE, TR_AUTHOR, TR_SRC)

CHUNKS = [
    # ---------- Grace (Coddington) · 6 ----------
    (GR,
     "Cast the face to play a role: the creative director's eye",
     "aesthetics",
     "Coddington selects models the way a director casts a film: not the conventionally "
     "pretty face but the one who can play the role the story needs. She prizes the quirky, "
     "individual, 'character' face (freckles, pallor, oddness) over generic beauty, because "
     "the image is a performance, not a product shot.",
     "Cast for the role the work needs, not for generic appeal; the distinctive, slightly "
     "off face carries a story that a perfect one cannot.",
     "When BJ casts or directs any image, the brief is the role the frame must play; choose "
     "the subject and look that serve the story, not the safest or prettiest option.",
     ["pick my models as if casting", "a character rather than pretty"],
     ["casting", "the-eye", "creative-direction", "aesthetics", "coddington", "image-making"]),
    (GR,
     "The shoot as visual narrative: tell a story, do not just show the clothes",
     "aesthetics",
     "Coddington's signature is the narrative fashion shoot: she builds a romance, a fairy "
     "tale, a scene (Alice in Wonderland, The Red Shoes) so the picture reads as a story told "
     "visually rather than a catalogue of garments. The clothes serve the narrative, not the "
     "reverse.",
     "Build images around a story the viewer can feel; narrative and atmosphere make a frame "
     "memorable where a product display is forgettable.",
     "For any visual work BJ makes, leading with a narrative or world (not just the subject "
     "or the object) is the lever that turns a competent frame into a memorable one.",
     ["seeing a story visually", "the romance of the picture"],
     ["narrative", "storytelling", "world-building", "aesthetics", "coddington", "editorial"]),
    (GR,
     "The shoot is an orchestrated production, not a click",
     "operator-process",
     "As creative director Coddington describes the photo session as a complex build: "
     "location, model, photographer, light, styling, logistics, and a thousand decisions "
     "coordinated under pressure (vividly captured in The September Issue). The glamour rests "
     "on heavy, unglamorous orchestration.",
     "Treat a shoot as a production to be project-managed, not a moment to be captured; the "
     "output quality is set by the preparation and coordination behind it.",
     "BJ's field/operator instinct transfers directly: a strong image session is an "
     "orchestrated operation (pre-production, logistics, contingencies), and the craft is in "
     "the preparation as much as the capture.",
     ["a complicated photo session", "a thousand things to deal with"],
     ["production", "orchestration", "pre-production", "operator-process", "coddington", "craft"]),
    (GR,
     "Taste is a trained, opinionated faculty, not a vague gift",
     "taste",
     "Coddington's eye is decisive and specific: she knows instantly what she likes and "
     "rejects (no sappy blondes, no over-tanned athletic girls; yes to freckles and oddness). "
     "Taste here is a sharpened, repeatedly-exercised judgment built over decades of looking, "
     "not an ineffable talent.",
     "Develop taste as a discipline: form strong, specific preferences and exercise them "
     "constantly; decisive selection is a trainable skill that compounds.",
     "BJ can build taste deliberately by looking hard and committing to strong, specific "
     "preferences rather than hedging; a sharpened eye is an operator asset across any visual "
     "or product domain.",
     ["I can't stand all the sappy blondes", "I like freckles"],
     ["taste", "judgment", "curation", "discipline", "coddington", "selection"]),
    (GR,
     "Turn damage into a signature: reinvention after the accident",
     "operator-doctrine",
     "After a car crash sliced off her eyelid and ended her front-line modeling, Coddington "
     "developed a heavy black-shadow eye look that became her trademark, a deliberate "
     "camouflage turned signature, and pivoted from model to editor to creative director. "
     "The setback was reworked into identity and a longer career.",
     "Convert a forced setback into a distinctive signature and a role change; constraint can "
     "be metabolized into a recognizable style and a more durable position.",
     "For BJ, a constraint or pivot can become a signature rather than a loss; reinvention "
     "into the next role (built on what the setback forced) is an operator move, not a "
     "consolation.",
     ["a form of camouflage", "I developed a new look"],
     ["reinvention", "constraint", "signature", "operator-doctrine", "coddington", "career-pivot"]),
    (GR,
     "Coming up inside the editorial institution (distinct from the editor-in-chief)",
     "media-business",
     "Coddington's authority is the creative director's hands-on image-making inside the "
     "Vogue machine, distinct from the editor-in-chief's institutional command (Vreeland, "
     "Wintour). The magazine is a media institution with its own hierarchy, rituals, and "
     "production engine; her power is craft-based, exercised shot by shot.",
     "Inside a media institution there are two different powers: the editor-in-chief's "
     "command and the maker's craft authority; the maker's leverage is the irreplaceable eye, "
     "exercised in the work itself.",
     "If BJ ever operates inside or alongside a media institution, craft authority (the "
     "irreplaceable eye, earned shot by shot) is a different and durable kind of power from "
     "positional command; this is the maker's path.",
     ["as creative director of the magazine", "the most important issue of the year"],
     ["media-institution", "craft-authority", "editorial", "media-business", "coddington", "vogue"]),
    # ---------- Total Recall (Schwarzenegger) · 8 ----------
    (TR,
     "A specific, vivid vision made to feel inevitable",
     "founder-psychology",
     "Schwarzenegger describes refining a dream until it was concrete: not 'be successful' "
     "but Mr. Universe, then Hollywood, then wealth, modeled exactly on Reg Park's path. The "
     "vision became so detailed and certain that it felt like it had to happen, which "
     "organized every daily choice toward it.",
     "Make the goal vivid and specific enough that it feels inevitable; a concrete picture of "
     "the end state recruits daily behavior far better than a vague aspiration.",
     "For BJ, a concrete picture of the end state (not a vague 'build something') is what "
     "aligns daily reps; the brief's posture is to keep options open, but each chosen bet "
     "should be made vivid enough to drive action.",
     ["refined this vision until it was specific", "it had to happen"],
     ["vision", "specificity", "goal-setting", "founder-psychology", "schwarzenegger", "ambition"]),
    (TR,
     "Reps, progressive overload, and shocking the muscle",
     "operator-doctrine",
     "Schwarzenegger's training method is a model for compounding work: relentless reps, "
     "progressive overload, and 'shocking the muscle' (varying the stimulus, stripping sets) "
     "so the body never adapts to a comfortable routine. Growth comes from deliberately "
     "unexpected, escalating stress, then recovery.",
     "Compounding output comes from high-volume reps plus deliberate variation that prevents "
     "adaptation; comfort is the enemy of growth, so keep changing and escalating the "
     "stimulus.",
     "BJ's build benefits from the same logic: volume of reps plus deliberate variation "
     "(new challenges, escalating difficulty) rather than a comfortable fixed routine; "
     "growth is forced by changing the stimulus.",
     ["shocking the muscle", "show them who is boss"],
     ["reps", "progressive-overload", "compounding", "operator-doctrine", "schwarzenegger", "practice"]),
    (TR,
     "The aggressive move: take the toughest arena early",
     "strategy",
     "Rather than climb the ladder (Mr. Austria, then Mr. Europe, then Mr. Universe), the "
     "teenage Schwarzenegger entered Mr. Universe in London directly, the most aggressive "
     "career move available, to find out where he stood against the best. He was impatient "
     "with the queue and willing to lose to learn fast.",
     "Enter the toughest arena earlier than convention says you are ready; testing against "
     "the best accelerates learning and standing far faster than climbing every rung.",
     "BJ can compress a learning curve by entering harder arenas sooner (real problems, "
     "stronger competition) rather than waiting to be 'ready'; an early loss against the best "
     "teaches more than a safe win.",
     ["the most aggressive career move", "where I stood"],
     ["aggression", "arena-selection", "speed", "strategy", "schwarzenegger", "ambition"]),
    (TR,
     "Selling is the master skill: never let them leave without a yes",
     "operator-process",
     "From the hardware store Schwarzenegger took a cardinal rule (never let a customer leave "
     "without a purchase, work every angle) and applied selling everywhere: selling "
     "stewardesses on the gym, selling himself on Munich, ultimately selling himself as a "
     "product. Selling, not just the product, is the operating skill.",
     "Treat selling as a trainable master skill applied to everything (ideas, yourself, the "
     "next yes), not a separate sales function; close every interaction toward a commitment.",
     "BJ's leverage in any path runs through selling (the offer, the vision, himself into "
     "rooms); it is a learnable operating skill, not a personality trait, and worth "
     "practicing as deliberately as the craft.",
     ["never let a customer walk out", "the most important skill was selling"],
     ["selling", "persuasion", "closing", "operator-process", "schwarzenegger", "skill"]),
    (TR,
     "Immigrant hunger and the early entrepreneurial instinct",
     "founder-psychology",
     "A conviction that he was 'meant for bigger things' and bound for America fueled "
     "Schwarzenegger from childhood, alongside an early entrepreneurial instinct (buying "
     "ice-cream cones for a schilling and reselling them at the hot end of the lake for "
     "triple). Hunger plus a bias to make his own money drove the arc.",
     "Outsized ambition plus a bias toward making your own money early is a durable engine; "
     "spotting a simple arbitrage and acting on it is the same instinct that scales later.",
     "BJ's bias to build and to spot real-world opportunity is the same engine; the memoir is "
     "a reminder that hunger and a make-your-own-money instinct compound, while the specific "
     "vehicle stays open.",
     ["meant for bigger things", "a business opportunity"],
     ["ambition", "hunger", "entrepreneurship", "founder-psychology", "schwarzenegger", "drive"]),
    (TR,
     "Serial reinvention: platform-jumping across careers",
     "strategy",
     "Schwarzenegger's arc is deliberate platform-jumping: bodybuilding to film to politics "
     "to business and back to film after the governorship, each stage a stepping-stone whose "
     "audience and credibility he carried into the next. He treated each title as a launchpad "
     "rather than a destination.",
     "Treat each domain you win as a platform into the next, carrying audience and "
     "credibility forward; serial reinvention beats settling, when each move builds on the "
     "last's equity.",
     "For BJ, skills and audience built in one domain (engineering, photography, AI systems) "
     "are platforms into the next; the pattern is to compound credibility across moves rather "
     "than treat any one as the final identity.",
     ["this or nothing", "stepping-stone"],
     ["reinvention", "platform-jumping", "career-arc", "strategy", "schwarzenegger", "compounding"]),
    (TR,
     "Building 'Arnold': the self-constructed public figure as the asset",
     "brand",
     "Schwarzenegger consciously built a recognizable name and persona (the accent, the body, "
     "the one-liners) into a durable asset that carried across bodybuilding, film, and "
     "politics. The brand was a deliberate construction, marketed relentlessly, and became "
     "more valuable than any single role.",
     "A consistent, distinctive personal brand, deliberately built and marketed, becomes a "
     "transferable asset that outlasts any one product or role; identity is constructable.",
     "Useful as a pattern, not a prescription: a coherent public identity can be a "
     "transferable asset, but the brief keeps BJ's identity open; this is a lens on how "
     "brands are built, not a mandate to build a personal one now.",
     ["everyone in the world would know me", "market myself"],
     ["personal-brand", "identity-construction", "name-recognition", "brand", "schwarzenegger", "marketing"]),
    (TR,
     "The honest cost: the price of relentless self-focus",
     "ethics",
     "Total Recall is candid about cost: the heart surgery, and above all the personal "
     "failings and damage to his family that accompanied decades of single-minded ambition. "
     "The drive that built the career also exacted a real, acknowledged human price.",
     "Single-minded ambition has a real cost in health and relationships; an honest operator "
     "accounts for the price rather than mythologizing the drive as cost-free.",
     "A counterweight for BJ: relentless ambition has a documented human cost; the lesson is "
     "to build with eyes open to the trade-offs, not to romanticize all-consuming drive as "
     "the only model.",
     ["the price", "what doesn't kill us"],
     ["cost-of-ambition", "trade-offs", "honesty", "ethics", "schwarzenegger", "family"]),
    # ---------- Synthesis · 2 ----------
    (GR,
     "Synthesis: taste and vision are built faculties, not gifts",
     "taste",
     "Across both memoirs the headline faculty is built, not bestowed: Coddington's eye was "
     "sharpened over decades of decisive looking, and Schwarzenegger's vision was refined "
     "until it was concrete and inevitable. Taste (what to choose) and vision (what to aim "
     "at) are the same kind of trainable, exercised judgment, the upstream skill behind the "
     "craft and the career.",
     "Treat taste and vision as disciplines to be trained through repeated, decisive "
     "practice, not as innate gifts; the judgment of what to choose and where to aim is the "
     "upstream operator skill.",
     "For BJ, both the eye (taste) and the aim (vision) are buildable through deliberate "
     "practice; investing in that upstream judgment pays across whichever path he chooses, "
     "while the path itself stays open.",
     ["a trained eye", "a very specific vision"],
     ["taste", "vision", "judgment", "synthesis", "coddington", "schwarzenegger"]),
    (TR,
     "Synthesis: the singular-operator pattern and the optionality guardrail",
     "operator-doctrine",
     "FOUNDER_FASHION_RECOVERY distills a singular-operator pattern: a specific vision, "
     "relentless reps, trained taste, selling as a master skill, serial reinvention across "
     "platforms, and a deliberately built identity, balanced by the honest cost of "
     "single-minded drive. For SNIPED this is a decision-support pattern library (how "
     "operators build taste, method, and a body of work), explicitly NOT a directive that BJ "
     "adopt fashion editorial, memoir-making, or celebrity branding as his path.",
     "Extract the transferable operator mechanics (vision, reps, taste, selling, reinvention, "
     "honest cost) as a pattern library, decoupled from the specific careers that produced "
     "them, and apply them to whatever BJ actually builds.",
     "This synthesizes the lane for BJ: a toolkit of how singular operators build a body of "
     "work, held as decision-support against CURRENT_OPERATOR_REALITY_BRIEF, with photography "
     "one option among several and no final SNIPED / SNIPED Media / BASEPLATE direction set.",
     ["a body of work", "one option among several"],
     ["synthesis", "operator-pattern", "optionality", "operator-doctrine", "decision-support", "founder-fashion"]),
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
    forb = [d for d in ("fashion", "fashion-luxury", "celebrity-brand", "memoir") if d in doms]
    print("forbidden domains present:", forb or "NONE")


if __name__ == "__main__":
    main()
