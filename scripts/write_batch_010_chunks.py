#!/usr/bin/env python3
"""
BATCH_010 chunk writer · lineage + Black culture canon (CORE 7 books).
Schema: chunk_id, batch_id, source_title, source_file, author, domain, concept, summary,
        usable_principle, sniped_relevance, direct_quotes, tags. ID pattern BATCH_010_NNN.
Domains reused (all pre-existing · operator-approved · NO new domain): lineage, culture, aesthetics,
brand, operator-doctrine, strategy, systems-thinking, ethics. Copyright-safe SHORT quotes only
(memoirs: a sentence or short phrase, mostly paraphrase). Em-dash swept. Supreme Models = LIGHT (3).
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_010_CHUNKS.jsonl"

C = []


def add(src, title, author, domain, concept, summary, usable, relevance, quotes, tags):
    C.append({"source_title": title, "source_file": src, "author": author, "domain": domain,
              "concept": concept, "summary": summary, "usable_principle": usable,
              "sniped_relevance": relevance, "direct_quotes": quotes, "tags": tags})


# ===================== The Big Payback · Dan Charnas (8) =====================
S = "the_big_payback_charnas.txt"; T = "The Big Payback: The History of the Business of Hip-Hop (2010)"; A = "Dan Charnas"
add(S, T, A, "culture", "Hip-hop became global culture itself, not a niche",
    "Charnas traces hip-hop from a marginal Bronx/Harlem subculture in 1977 to global culture spanning music, language, film, fashion, sport, and politics within three decades. The improbable leap is the book's spine.",
    "Treat a tightly-rooted scene as a potential global culture; depth in a specific place can scale into something far larger.",
    "Validates SNIPED's scene-density bet: a specific LA cultural circle, built deeply, is how cultural reach actually compounds.",
    "Hip-hop has become global culture itself.",
    ["hip-hop", "scene-to-global", "cultural-force", "culture"])
add(S, T, A, "strategy", "The culture was built by entrepreneurs and hustlers, not institutions",
    "The history is carried by executives, artists, entrepreneurs, and hustlers who surmounted opposition out of belief, building an industry the establishment did not hand them. Ownership was seized, not granted.",
    "Build the commercial infrastructure yourself rather than waiting for gatekeepers to admit you; belief plus hustle precedes permission.",
    "Backs SNIPED's high-agency, build-your-own-platform stance over seeking institutional validation.",
    "",
    ["entrepreneurs", "self-built", "hustle", "strategy"])
add(S, T, A, "systems-thinking", "Ownership versus being owned is the recurring battle",
    "A throughline is the fight over who owns the masters, the publishing, the company, and therefore the wealth. Artists who only performed got paid once; those who owned captured the compounding value.",
    "Own the asset, not just the labor; the durable wealth in any creative business sits with whoever owns the rights and the entity.",
    "Reinforces SNIPED's ownership doctrine (own the audience, the IP, the relationship) drawn from the music industry's hardest lesson.",
    "",
    ["ownership", "masters", "value-capture", "systems-thinking"])
add(S, T, A, "systems-thinking", "Independent distribution was the leverage point",
    "Charnas shows how control of distribution (independent labels, street-level networks, then major-label deals on better terms) determined who won. The bottleneck was getting the product to people, and whoever controlled that controlled the economics.",
    "Find and control the distribution bottleneck in your market; the gatekeeper of reach captures the margin.",
    "Maps to SNIPED's owned-distribution priority and the Card-system distribution architecture.",
    "",
    ["distribution", "leverage-point", "independents", "systems-thinking"])
add(S, T, A, "culture", "Cultural credibility is the currency",
    "In hip-hop, authenticity and credibility (the cosign, the respect of the streets and peers) were prerequisites to commercial success; you could not buy your way past them. Credibility converted into commerce, never the reverse.",
    "Earn cultural credibility first; it is the non-purchasable asset that commercial success is built on, not the other way around.",
    "Directly underwrites SNIPED's lineage-credibility-first posture: the work must earn standing inside the culture before it monetizes.",
    "",
    ["credibility", "authenticity", "cosign", "culture"])
add(S, T, A, "strategy", "Crossover without losing the core base",
    "The hardest move Charnas documents is reaching the mainstream without alienating the core audience that conferred credibility. The winners expanded the tent while keeping the base that made them legitimate.",
    "Grow into broader markets without abandoning the core audience that gave you legitimacy; protect the base while expanding.",
    "Informs SNIPED's two-system platform split: expand reach (IG mythology) without diluting the credible core (LinkedIn/trust).",
    "",
    ["crossover", "core-base", "expansion", "strategy"])
add(S, T, A, "ethics", "Exploitation and appropriation shadow the business",
    "Charnas does not romanticize: the history includes artists exploited by bad contracts and a culture's value extracted by outsiders. The cautionary lesson is about who profits from culture they did not create.",
    "Structure deals so the creators of value share in it; be on the right side of the appropriation line, as creator-owner not extractor.",
    "Sharpens SNIPED's ethical stance and the Lineage Doctrine's insistence on documenting from inside the culture, not extracting from outside it.",
    "",
    ["exploitation", "appropriation", "fair-deal", "ethics"])
add(S, T, A, "brand", "The artist-as-brand and the entrepreneur-artist emerge",
    "Charnas charts the shift from artist-as-talent to artist-as-brand-and-mogul (the entrepreneur who owns labels, lines, and ventures). The persona became a platform for enterprises far beyond the music.",
    "Build the personal brand as a platform that can carry multiple ventures, not as decoration on a single product.",
    "Models SNIPED's founder-as-brand architecture: the named operator as the platform the offers hang from.",
    "",
    ["artist-as-brand", "mogul", "platform", "brand"])

# ===================== Dilla Time · Dan Charnas (7) =====================
S = "dilla_time_charnas.txt"; T = "Dilla Time: The Life and Afterlife of J Dilla (2022)"; A = "Dan Charnas"
add(S, T, A, "aesthetics", "Dilla Time: a third path of rhythm",
    "Charnas argues J Dilla created a new time-feel by juxtaposing even (straight) and uneven (swung) rhythm simultaneously, a disorienting, pleasurable friction that changed how musicians perceive time. It was a genuine formal invention.",
    "Look for the third option between two accepted conventions; the breakthrough is often the deliberate juxtaposition no one allowed themselves.",
    "A craft model for SNIPED's aesthetic invention: the signature is born from breaking a binary, not picking a side.",
    "a third path of rhythm",
    ["dilla-time", "rhythmic-invention", "third-path", "aesthetics"])
add(S, T, A, "operator-doctrine", "Mastery through obsessive, private practice",
    "Dilla's innovation came from relentless, largely unseen work on the machine (the MPC), accumulating thousands of hours before the world noticed. The legend was built in private repetition.",
    "Put in the unglamorous reps in private; the visible breakthrough is the surfacing of accumulated, unseen practice.",
    "Reinforces SNIPED's repetition-over-novelty doctrine and the disciplined-artist frame (Moonwalk lineage).",
    "",
    ["obsessive-practice", "reps", "mastery", "operator-doctrine"])
add(S, T, A, "aesthetics", "Constraints (the machine) produced the signature",
    "Dilla's sound was shaped by working deeply within the limits of his sampler rather than around them; the constraints of the MPC became the source of his distinctive feel.",
    "Master one tool's constraints deeply rather than chasing every new tool; the constraint is where the signature forms.",
    "Maps to SNIPED's tool-mastery discipline (one-at-a-time) and the composite/grading signature built within a fixed system.",
    "",
    ["constraints", "tool-mastery", "signature", "aesthetics"])
add(S, T, A, "culture", "Influence without fame; the long afterlife",
    "Dilla was never a household name yet reshaped popular music through the musicians he influenced. Charnas shows cultural impact and celebrity are different currencies, and the deeper one outlasts.",
    "Optimize for durable influence over visible fame; the work that changes how peers work outlasts the work that merely trends.",
    "Validates SNIPED's perennial-seller / influence-over-virality posture.",
    "",
    ["influence-vs-fame", "afterlife", "legacy", "culture"])
add(S, T, A, "lineage", "The Detroit scene and the chain of mentors",
    "Dilla emerged from a specific Detroit musical lineage (church, family musicianship, local mentors and crews) that fed his craft. He was a node in a place-based chain, not a lone genius.",
    "Locate yourself in a specific place-based lineage of mentors and peers; genius is grown inside a scene, not in isolation.",
    "Directly grounds the SNIPED Lineage Doctrine: document from inside the chain (Detroit here, LA for SNIPED).",
    "",
    ["detroit", "mentors", "scene-lineage", "lineage"])
add(S, T, A, "operator-doctrine", "Document from inside, faithful to the people",
    "Charnas built the book from 190+ interviews, telling the story from the perspectives of those who lived it rather than imposing an outside thesis. The method is faithful witness from inside the lineage.",
    "Document a culture from inside it, faithful to the people who lived it, rather than imposing an outsider's frame.",
    "Models the SNIPED Lineage Doctrine's documentary method exactly: inside the lineage, not cultural tourism.",
    "Dilla Time is journalism, not memoir.",
    ["documentary-method", "faithful-witness", "inside-the-lineage", "operator-doctrine"])
add(S, T, A, "aesthetics", "Feel over precision; the human imperfection",
    "Dilla's rhythms deliberately resisted the quantized perfection the machine offered, keeping a human looseness that felt better than metronomic accuracy. The imperfection was the point.",
    "Preserve deliberate human imperfection where it reads as feel; perfect precision can drain the life from the work.",
    "Counterbalances SNIPED's polish with a feel-first principle: the editorial restraint that keeps work human, not sterile.",
    "",
    ["feel", "imperfection", "anti-quantize", "aesthetics"])

# ===================== Decoded · Jay-Z (6) =====================
S = "decoded_jayz.txt"; T = "Decoded (2010)"; A = "Jay-Z"
add(S, T, A, "aesthetics", "Rap is poetry: nuance, layering, double meaning",
    "Jay-Z reframes rap as a serious literary craft, decoding his lyrics to show the layered meaning, metaphor, and double entendre beneath what sounds simple. The surface ease hides deliberate construction.",
    "Build layered meaning beneath an accessible surface; the craft is making the constructed thing feel effortless.",
    "Backs SNIPED's intellectual-artist frame: the work reads as effortless luxury but is densely constructed.",
    "",
    ["rap-as-poetry", "layered-meaning", "craft", "aesthetics"])
add(S, T, A, "lineage", "Self-authorship: re-create yourself and reimagine your world",
    "Hearing his own recorded voice, Jay-Z saw an opening to re-create himself and reimagine his world. The act of recording was an act of self-authorship out of Marcy.",
    "Use the act of making (recording, publishing, building) to author the self you intend to become, not just to document the one you are.",
    "Core to the SNIPED self-authorship thread: the founder builds the work that builds the founder.",
    "a way to re-create myself and reimagine my world",
    ["self-authorship", "reinvention", "voice", "lineage"])
add(S, T, A, "strategy", "The hustler's logic translated to art and enterprise",
    "Jay-Z frames the skills of the corner (reading people, managing risk, supply and demand, relentless drive) as directly transferable to building an artistic and business empire. The street was a business school.",
    "Recognize and transfer the operating skills you already have from one arena to a higher-leverage one; the underlying logic ports.",
    "Echoes the find-your-edge principle: inventory the real skills you already hold and redeploy them upward.",
    "",
    ["transferable-skills", "hustler-logic", "enterprise", "strategy"])
add(S, T, A, "brand", "Multiple selves: the persona, the man, the mask",
    "Jay-Z plays openly with the gap between Shawn Carter and Jay-Z, the man and the persona, treating the public self as a deliberate construction he controls. The mask is chosen, not imposed.",
    "Author the public persona deliberately as a controlled construction distinct from the private self; own the gap rather than denying it.",
    "Directly informs SNIPED's two-register identity (the mythology vs the operator) and deliberate persona design.",
    "",
    ["persona", "public-self", "constructed-identity", "brand"])
add(S, T, A, "lineage", "Marcy as origin: where you come from is the material",
    "Jay-Z roots the entire work in the Marcy projects, treating his origin not as something to escape and hide but as the source material and the legitimacy. The origin is the asset.",
    "Treat your specific origin as load-bearing material and legitimacy, not a past to sand off.",
    "Grounds the SNIPED Lineage Doctrine: the specific origin is the work's material and its credibility.",
    "",
    ["origin", "marcy", "material-as-legitimacy", "lineage"])
add(S, T, A, "aesthetics", "The recording captures and distorts; the made object differs from the self",
    "Jay-Z notes a recording plays back a distortion, a voice different from the one in your head yet recognizably you. The made artifact is never the raw self; it is a deliberate transformation.",
    "Accept that the published artifact is a transformation of the self, and shape that transformation deliberately rather than chasing raw authenticity.",
    "Frames SNIPED's edit-register doctrine: the deliverable is a deliberate transformation, not an unmediated capture.",
    "a recording captures you, but plays back a distortion",
    ["artifact-vs-self", "transformation", "mediation", "aesthetics"])

# ===================== The Autobiography of Gucci Mane (6) =====================
S = "autobiography_of_gucci_mane.txt"; T = "The Autobiography of Gucci Mane (2017)"; A = "Gucci Mane, Neil Martinez-Belkin"
add(S, T, A, "operator-doctrine", "Transformation: the deliberate post-prison reinvention",
    "Gucci Mane recounts using a prison term to get sober, disciplined, and physically and mentally rebuilt, emerging as a deliberately reinvented person. The turnaround was chosen and engineered, not accidental.",
    "A rock-bottom can be converted into a deliberate, total reinvention; the turnaround is engineered through chosen discipline.",
    "Primary-source backing for SNIPED's self-reinvention and composure doctrine: the operator can author a new version of self.",
    "",
    ["transformation", "reinvention", "sobriety", "operator-doctrine"])
add(S, T, A, "operator-doctrine", "Discipline and prolific output as the comeback engine",
    "Post-transformation, Gucci Mane's relentless work ethic and prolific release schedule (mixtape after mixtape) drove the comeback. Volume and consistency, not a single hit, rebuilt the career.",
    "Rebuild through disciplined, prolific output and consistency rather than betting on one breakthrough.",
    "Reinforces SNIPED's repetition-over-novelty doctrine and the run-the-office cadence.",
    "",
    ["discipline", "prolific-output", "consistency", "operator-doctrine"])
add(S, T, A, "ethics", "Honest accounting of the lost years",
    "The memoir is unflinching about the addiction, the violence, and the self-sabotage of the lost years, refusing to glamorize them. The honesty is what makes the transformation credible.",
    "Account honestly for your failures; the credibility of a comeback rests on not glamorizing what went wrong.",
    "Aligns with SNIPED's honest-broker / pratfall-effect trust posture: candor about the low points builds belief.",
    "",
    ["honest-accounting", "anti-glamorize", "credibility", "ethics"])
add(S, T, A, "lineage", "Inheritance: the father's flight and the family line",
    "Gucci Mane traces his story back through his father's troubles with the law and his grandmother Madear holding the family together. The personal arc is rooted in an inherited family context.",
    "Read the present arc through the inherited family line; the origin context shapes the operator's material and motivation.",
    "Grounds the SNIPED Lineage Doctrine in the personal-inheritance register.",
    "",
    ["inheritance", "family-line", "origin", "lineage"])
add(S, T, A, "culture", "Regional scene-building: Atlanta trap as a local movement",
    "Gucci Mane built a regional Atlanta movement (a sound, a roster, a local dominance) before national reach, anchoring his rise in a specific place and crew. The local scene was the foundation.",
    "Dominate a specific local scene and build a roster/crew before chasing national reach; local density precedes breadth.",
    "Mirrors SNIPED's scene-density strategy: own the LA cultural circle first.",
    "",
    ["regional-scene", "atlanta", "local-dominance", "culture"])
add(S, T, A, "brand", "The name and the character as a built asset",
    "Gucci Mane cultivated a recognizable persona and name (the ad-libs, the iconography, the brand) that became an asset independent of any single song. The character was deliberately maintained.",
    "Maintain a consistent, recognizable persona and signature marks; the character becomes an asset that outlives any one release.",
    "Models SNIPED's distinctive-brand-assets discipline (consistent signature, recognizable register).",
    "",
    ["name-as-asset", "persona", "iconography", "brand"])

# ===================== Hurricanes · Rick Ross (5) =====================
S = "hurricanes_rick_ross.txt"; T = "Hurricanes: A Memoir (2019)"; A = "Rick Ross, Neil Martinez-Belkin"
add(S, T, A, "brand", "Persona-construction: the character built around a name",
    "Ross built the larger-than-life boss persona deliberately, constructing a character (the name borrowed, the imagery, the lifestyle) that the music then inhabited. The persona was an authored creation.",
    "Construct the public persona deliberately and let the work inhabit it; the character can precede and exceed the literal facts.",
    "Informs SNIPED's mythology-building (IG register) as a deliberately authored persona.",
    "",
    ["persona-construction", "boss-character", "authored-image", "brand"])
add(S, T, A, "ethics", "The authenticity question: image versus literal biography",
    "Ross addresses the controversy over his past as a correctional officer, forcing the question of how much a built persona must match literal biography. The memoir wrestles with image-vs-fact openly.",
    "Decide deliberately where persona and literal fact can diverge and where they cannot; the gap, once exposed, must be survivable.",
    "A cautionary lens for SNIPED's mythology lane: build aspirational image, but keep the load-bearing claims true.",
    "",
    ["authenticity", "image-vs-fact", "persona-risk", "ethics"])
add(S, T, A, "culture", "Hustlin and the birth of an artist",
    "The memoir frames the breakout song and the early grind as the birth of the artist out of a Miami context, a specific place and moment producing the work. The art was forged in a scene.",
    "Anchor the origin story in a specific place and breakthrough moment; the scene and the grind are part of the work's meaning.",
    "Reinforces SNIPED's place-rooted, scene-anchored origin storytelling.",
    "",
    ["origin-story", "miami", "the-grind", "culture"])
add(S, T, A, "operator-doctrine", "Transcending setbacks: health, arrests, feuds",
    "Ross recounts surviving serious health scares, legal trouble, and public feuds while continuing to build, treating setbacks as obstacles to transcend rather than endpoints. Continuity through adversity is the throughline.",
    "Build through setbacks rather than pausing for them; continuity and resilience compound across the inevitable obstacles.",
    "Aligns with SNIPED's resilience doctrine and the company-of-one resilience-over-scale stance.",
    "",
    ["resilience", "transcending-setbacks", "continuity", "operator-doctrine"])
add(S, T, A, "lineage", "Taking a name and a mythology",
    "Ross took his name and much of his iconography from an existing legend, building a personal mythology by drawing on a lineage of imagery. The self was authored partly by inheriting and reworking a myth.",
    "Author a personal mythology by deliberately drawing on and reworking an existing lineage of imagery, owning the reinterpretation.",
    "Models how SNIPED can build mythology by drawing on its named lineages rather than inventing from nothing.",
    "",
    ["mythology", "naming", "inherited-imagery", "lineage"])

# ===================== Empire State of Mind · Greenburg (5) =====================
S = "empire_state_of_mind_greenburg.txt"; T = "Empire State of Mind: How Jay-Z Went from Street Corner to Corner Office (2011)"; A = "Zack O'Malley Greenburg"
add(S, T, A, "strategy", "Street corner to corner office: the deliberate arc",
    "Greenburg charts Jay-Z's deliberate progression from selling on the corner to running companies, treating each stage as a calculated step up in leverage. The arc was strategy, not luck.",
    "Plan a deliberate progression of increasing leverage rather than staying at one level; each stage should buy access to the next.",
    "Models SNIPED's own staged progression (photography proof now, product later) as a deliberate leverage ladder.",
    "",
    ["arc", "leverage-ladder", "progression", "strategy"])
add(S, T, A, "brand", "Building a notorious brand: the name as the asset",
    "Greenburg shows Jay-Z's name becoming the central asset that ventures attached to (Roc-A-Fella, Rocawear, partnerships), worth more than any single product. The brand was the platform.",
    "Build the name into the primary asset that ventures hang from; a strong personal brand is more durable than any product.",
    "Direct model for SNIPED's founder-as-platform architecture.",
    "",
    ["personal-brand", "name-as-asset", "platform", "brand"])
add(S, T, A, "strategy", "Equity over fees: own, do not just earn",
    "A recurring lesson is Jay-Z's shift from taking fees to taking ownership and equity (masters, companies, stakes), capturing the upside instead of a one-time payment. Ownership compounded his wealth.",
    "Take equity and ownership over one-time fees wherever possible; the durable wealth is in the stake, not the paycheck.",
    "Reinforces SNIPED's ownership doctrine and the case for productized IP over pure service fees.",
    "",
    ["equity-over-fees", "ownership", "upside", "strategy"])
add(S, T, A, "strategy", "Diversification across categories on one brand",
    "Greenburg documents Jay-Z extending one brand across music, fashion, spirits, sports, and tech, using credibility in one domain to enter the next. The brand was the passport between categories.",
    "Use credibility built in one category as the entry pass to adjacent ones; diversify on the strength of a single trusted brand.",
    "Informs SNIPED's potential expansion path: photography credibility as the passport to adjacent creative-direction ventures.",
    "",
    ["diversification", "category-extension", "brand-passport", "strategy"])
add(S, T, A, "lineage", "The come-up grounded in Marcy",
    "Greenburg keeps the empire rooted in its Marcy-projects origin, showing the come-up's credibility and drive traced back to a specific place. The origin grounds the empire's authenticity.",
    "Keep the empire visibly rooted in its specific origin; the come-up story is part of the brand's authenticity and drive.",
    "Reinforces the SNIPED Lineage Doctrine: never sand off the origin; it grounds the whole structure.",
    "",
    ["come-up", "origin-rooted", "marcy", "lineage"])

# ===================== Supreme Models · Reynolds (3 · LIGHT) =====================
S = "supreme_models_reynolds.txt"; T = "Supreme Models: Iconic Black Women Who Revolutionized Fashion (2019)"; A = "Marcellas Reynolds"
add(S, T, A, "culture", "A visual archive of Black women who revolutionized fashion",
    "Reynolds assembles a curated archive of iconic Black women who broke into and reshaped fashion, preserving a lineage that the mainstream record under-documented. The book is an act of cultural memory.",
    "Build the archive that preserves an under-documented lineage; curation itself is a cultural and strategic act.",
    "Models SNIPED's Cultural Doc / archive instinct: documenting a lineage the mainstream record neglects.",
    "Iconic Black Women Who Revolutionized Fashion",
    ["visual-archive", "cultural-memory", "black-women-fashion", "culture"])
add(S, T, A, "lineage", "Being first: breaking the barrier as inheritance",
    "The profiles foreground the firsts (the first to walk certain runways, cover certain magazines), framing each breakthrough as opening a door for those who followed. The lineage is a chain of barrier-breaking.",
    "Frame breakthroughs as inheritance: each first opens the door for the next, and the lineage is the chain of doors opened.",
    "Grounds the SNIPED Lineage Doctrine in the image-making register: representation as an inherited, extended chain.",
    "",
    ["being-first", "barrier-breaking", "inherited-doors", "lineage"])
add(S, T, A, "aesthetics", "Image-making as power and self-definition",
    "Reynolds treats the fashion image as a site of power and self-definition for Black women, where being seen on one's own terms is itself the achievement. The image is not decoration but authorship.",
    "Treat the image as authorship and power, not decoration; being seen on your own terms is the achievement.",
    "Connects to BATCH_005 photography canon + SNIPED's image-as-power thesis (the portrait as self-definition).",
    "",
    ["image-making", "self-definition", "representation", "aesthetics"])

# ===================== synthesis (5 · cite a representative real file) =====================
add("decoded_jayz.txt", "BATCH_010 cross-source synthesis", "SNIPED synthesis", "lineage",
    "Self-authorship is the through-line: make yourself the made object",
    "Across Jay-Z, Gucci Mane, and Rick Ross, the recurring move is authoring the self deliberately, treating the public persona and the work as a chosen construction built out of a specific origin. Identity is made, not just inherited.",
    "Author the self and the persona deliberately out of your real origin; the operator is the made object, built on purpose.",
    "The central SNIPED Lineage Doctrine principle in primary-source form: build the work that builds the founder, from inside the lineage.",
    "",
    ["synthesis", "self-authorship", "made-self", "lineage"])
add("the_big_payback_charnas.txt", "BATCH_010 cross-source synthesis", "SNIPED synthesis", "strategy",
    "Ownership over being owned is the lineage's hard economic lesson",
    "Charnas's history and Greenburg's biography converge: the artists who owned (masters, companies, equity) built durable wealth, while those who only performed were paid once. The economic moral of the culture is ownership.",
    "Own the asset, the IP, the audience, and the entity; the music industry's hardest lesson is that ownership is the only durable position.",
    "Reinforces SNIPED's ownership doctrine end to end, drawn from the culture that learned it the hard way.",
    "",
    ["synthesis", "ownership", "durable-wealth", "strategy"])
add("hurricanes_rick_ross.txt", "BATCH_010 cross-source synthesis", "SNIPED synthesis", "brand",
    "Persona is a built asset; the image is part of the product",
    "Ross, Gucci Mane, and Jay-Z all treat the public persona as a deliberately constructed asset that the work inhabits and that markets the work. The image is engineered, maintained, and load-bearing.",
    "Engineer and maintain the persona as a real asset; the consistent constructed image is part of what the audience buys.",
    "Underwrites SNIPED's deliberate mythology/persona building across its two platform registers, with the authenticity guardrail.",
    "",
    ["synthesis", "persona-as-asset", "image", "brand"])
add("dilla_time_charnas.txt", "BATCH_010 cross-source synthesis", "SNIPED synthesis", "operator-doctrine",
    "Craft discipline plus obsessive reps make the legend",
    "Dilla's invention and Gucci Mane's comeback share an engine: relentless, disciplined, often-private repetition that accumulated into mastery and legacy. The legend is the surfacing of unseen reps.",
    "Trust disciplined private repetition as the real engine of mastery and reputation; the visible legend is accumulated unseen work.",
    "The primary-source version of SNIPED's repetition-over-novelty and disciplined-artist doctrines.",
    "",
    ["synthesis", "discipline-and-reps", "mastery", "operator-doctrine"])
add("the_big_payback_charnas.txt", "BATCH_010 cross-source synthesis", "SNIPED synthesis", "culture",
    "Document from inside the lineage, faithful to the people",
    "Charnas's interview-based method and the memoirists' first-person accounts model the same stance: the culture is rendered from inside it, faithful to those who lived it, never as outside extraction. This is the Lineage Doctrine's method.",
    "Document and build from inside the lineage, faithful to the people who lived it; refuse single-visit cultural tourism.",
    "Names the SNIPED Lineage Doctrine's core method and makes these seven books its primary-source grounding.",
    "",
    ["synthesis", "inside-the-lineage", "documentary-method", "culture"])

# ---- emit ----
em = chr(0x2014)
lines = []
for i, ch in enumerate(C, start=1):
    lines.append({
        "chunk_id": f"BATCH_010_{i:03d}",
        "batch_id": "BATCH_010",
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
