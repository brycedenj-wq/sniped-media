#!/usr/bin/env python3
"""
LITERARY_CANON_BLACK chunker · Morrison · Hurston · Walker

Reads the 3 normalized extracted txt files and emits LITERARY_CANON_BLACK_CHUNKS.jsonl
with the canonical 12-field schema.

Target: 28 chunks (range 22-32 per plan section 4).
Domains (lineage is a NEW domain · approved by operator brief · introduced here, registered at consolidation):
  culture (13) + lineage NEW (8) + aesthetics (5) + operator-doctrine (2 · only where directly SNIPED-tied).
  strategy not used.

Beloved DEFERRED (publisher-blurb / SEO-spam stub · 0 chunks). To Kill a Mockingbird NOT in lane (0 chunks).
In-copyright novels · direct_quotes are SHORT illustrative lines only (a sentence or two · fair-use scale).
Em-dash sweep (Unicode U+2014) applied to output · authored quotes already use em-dash-free punctuation.
"""

import json
from pathlib import Path

ROOT = Path.home() / "AI-Brain-Refinery"
OUT_JSONL = ROOT / "01_KNOWLEDGE_BASE" / "batches" / "LITERARY_CANON_BLACK_CHUNKS.jsonl"

BATCH_ID = "LITERARY_CANON_BLACK"
F_BE = "bluest_eye_morrison.txt"
F_TE = "their_eyes_hurston.txt"
F_CP = "color_purple_collection_walker.txt"

BASE_TAGS = ["literary-canon", "black-literary-canon", "lineage-doctrine", "2026-05-19-intake"]

chunks = []


def add(num, source_title, source_file, author, domain, concept, summary, principle, relevance, quotes, tags):
    chunks.append({
        "chunk_id": f"{BATCH_ID}_{num:03d}",
        "batch_id": BATCH_ID,
        "source_title": source_title,
        "source_file": source_file,
        "author": author,
        "domain": domain,
        "concept": concept,
        "summary": summary,
        "usable_principle": principle,
        "sniped_relevance": relevance,
        "direct_quotes": quotes,
        "tags": BASE_TAGS + tags,
    })


BE = "The Bluest Eye · Toni Morrison"
TE = "Their Eyes Were Watching God · Zora Neale Hurston"
CP = "The Color Purple · Alice Walker"
TMF = "The Temple of My Familiar · Alice Walker"
PSJ = "Possessing the Secret of Joy · Alice Walker"
SYN = "Black Literary Canon · cross-author synthesis"
AUTH_M, AUTH_H, AUTH_W = "Toni Morrison", "Zora Neale Hurston", "Alice Walker"
SNIPED = "SNIPED (cross-author synthesis)"

# ===========================================================================
# THE BLUEST EYE (Morrison) · 6
# ===========================================================================
add(1, BE, F_BE, AUTH_M, "culture",
    "The Dick-and-Jane primer as imposed ideal · the white-family template against Black reality",
    ("The Bluest Eye opens with the Dick-and-Jane reading primer (green-and-white house, happy Mother and "
     "Father, a red dress) and then runs it again with the spacing collapsed into nonsense. The pristine "
     "white-American family is set up as the cultural template every character is measured against and "
     "none can occupy. The imposed ideal, not any inherent lack, is the wound."),
    ("Name the imposed ideal explicitly before you critique its effects. A culture that holds up a single "
     "template of the good life (or the beautiful face) does harm not by what people lack but by what the "
     "template declares illegitimate. Surface the template; do not absorb it."),
    ("Backs the SNIPED counter-position on whose life and whose beauty get treated as the default. The "
     "primer is the literary form of a beauty/lifestyle standard imposed from outside · exactly what "
     "SNIPED's Lineage Doctrine refuses to shoot from the outside of."),
    ["Here is the house. It is green and white. It has a red door. It is very pretty.",
     "Mother, Father, Dick, and Jane live in the green-and-white house. They are very happy."],
    ["bluest-eye", "morrison", "imposed-ideal", "whose-story-gets-told", "beauty-standard"])

add(2, BE, F_BE, AUTH_M, "culture",
    "The beauty-standard wound · internalized racism and Pecola's prayer for blue eyes",
    ("Pecola Breedlove prays for blue eyes, believing that if she were beautiful by the white standard she "
     "would be loved and seen. Morrison renders the slow internalization of a beauty hierarchy as a "
     "literal, disfiguring desire. The wound is not ugliness; it is a child accepting a verdict the world "
     "handed her about her own face."),
    ("The most dangerous standard is the one a person turns on themselves. When a beauty hierarchy is "
     "internalized, the harm is self-administered and invisible. Any image-making practice either "
     "reinforces that verdict or refuses it; there is no neutral."),
    ("Directly grounds the SNIPED stance that portraiture confers dignity or withholds it. Pecola's prayer "
     "is the negative space of the SNIPED portrait that renders its subject fully, beautifully seen on "
     "their own terms (B5 photography canon · portraiture-as-dignity)."),
    ["the bluest eye (the white beauty standard Pecola believes will make her loved and visible)"],
    ["bluest-eye", "morrison", "internalized-racism", "the-gaze", "dignity", "aesthetics-adjacent"])

add(3, BE, F_BE, AUTH_M, "culture",
    "Accepting rejection as legitimate · the death of self-esteem (Morrison's own frame)",
    ("In her afterword Morrison names her real subject: not resistance to contempt but the tragic "
     "consequence of accepting rejection as legitimate, as self-evident. The death of self-esteem can "
     "occur quickly in children, before the ego has legs, when language, laws, and images all reinforce "
     "despair. Some collapse silently, with no voice to express it."),
    ("The decisive battle is whether a person treats an external verdict as legitimate. Build work and "
     "environments that refuse to ratify despair · because language, laws, and images either re-enforce "
     "it or interrupt it. Voice is the antidote to silent collapse."),
    ("The deepest tie to the SNIPED operator identity: the refusal to accept an externally imposed verdict "
     "as legitimate is the same internal-locus posture as PERSONAL_OPERATING_CODE ownership. Images that "
     "interrupt despair rather than re-enforce it is the SNIPED brief in literary form."),
    ["the far more tragic and disabling consequences of accepting rejection as legitimate, as self-evident",
     "Most others, however, grow beyond it. But there are some who collapse, silently, anonymously, with no voice to express or acknowledge it."],
    ["bluest-eye", "morrison", "self-esteem", "voice", "identity-formation", "anti-shallow-content"])

add(4, BE, F_BE, AUTH_M, "lineage",
    "Quiet as it's kept · the marigolds, communal witness, and the seasons as structure",
    ("The novel is narrated by Claudia as a communal we, organized by the seasons, framed by the marigolds "
     "that would not bloom the year Pecola carried her father's child. The community both witnesses and is "
     "complicit · everyone's seeds failed, not just theirs. Cultural memory is held collectively and "
     "confessed, not assigned to a single guilty party."),
    ("Hold memory collectively and honestly · the witness who says quiet as it's kept is also implicated. "
     "Inherited story is told by a we that includes its own failure. Structure long memory by natural "
     "cycle (the seasons) so the telling has shape and return."),
    ("Models the Lineage Doctrine's from-inside stance: the narrator is inside the community she indicts, "
     "never a tourist. The collective we and the seasonal structure are how a lineage holds and transmits "
     "a hard memory · the posture SNIPED's cultural documentation aims for."),
    ["Quiet as it's kept, there were no marigolds in the fall of 1941.",
     "our seeds were not the only ones that did not sprout; nobody's did."],
    ["bluest-eye", "morrison", "cultural-memory", "witness", "communal-narration", "inherited-story"])

add(5, BE, F_BE, AUTH_M, "aesthetics",
    "The fractured primer as form · whose order, whose legibility",
    ("Morrison breaks the Dick-and-Jane lines into section epigraphs that grow more illegible (spacing then "
     "punctuation stripped away), the orderly white-family sentence dissolving into a run-on as it is "
     "forced onto lives it does not fit. Form enacts content: an imposed order made unreadable when "
     "applied to the wrong reality."),
    ("Let form carry argument. When an imposed template does not fit a subject, the honest rendering shows "
     "the strain rather than smoothing it into the template. Legibility on whose terms is itself an "
     "aesthetic and political choice."),
    ("Aesthetic backing for the SNIPED restraint-and-seriousness lane (B4 aesthetic doctrine): form is not "
     "decoration but argument. The refusal to force a subject into an alien template is the editorial "
     "discipline behind quiet-luxury portraiture."),
    ["the primer sentence repeated three times · spaced, then unspaced, then stripped of punctuation as it is forced onto lives it does not fit"],
    ["bluest-eye", "morrison", "form-as-argument", "legibility", "restraint"])

add(6, BE, F_BE, AUTH_M, "culture",
    "Pecola as the unloved · the gaze that erases vs the gaze that confers worth",
    ("Pecola is rendered invisible and worthless by every gaze around her · shopkeepers, schoolmates, even "
     "her mother, who lavishes care on a white child instead. Morrison shows worth as something conferred "
     "or withheld by how others look. To be unseen is the injury; to be truly seen would have been the "
     "rescue."),
    ("Being seen accurately and with care is not a courtesy · it is how worth is conferred. Any practice "
     "built on looking at people carries the power to erase or to dignify. Choose the gaze that confers."),
    ("The literary statement of the SNIPED portrait thesis: the camera, like the gaze in the novel, either "
     "erases or dignifies. Pecola is the case for why SNIPED's whole-human, dignity-first portraiture "
     "matters (B5 photography canon · the gaze)."),
    ["the unloved child rendered invisible by every gaze · worth conferred or withheld by how others look"],
    ["bluest-eye", "morrison", "the-gaze", "dignity", "to-be-seen"])

# ===========================================================================
# THEIR EYES WERE WATCHING GOD (Hurston) · 7
# ===========================================================================
add(7, TE, F_TE, AUTH_H, "culture",
    "Ships and the horizon · men's wishes vs women's remembering and acting",
    ("The famous opening splits the relation to dreams by gender: for men, ships of wish stay forever on "
     "the horizon, mocked by time; women, by contrast, forget what they do not want to remember, remember "
     "what they must not forget, and the dream is the truth, so they act and do things accordingly. Janie's "
     "whole arc is a woman acting on her own remembered truth."),
    ("Distinguish wishing from acting on a remembered truth. The dream that organizes a life is the one you "
     "treat as truth and then act on, not the one you watch recede on the horizon. Agency is acting "
     "accordingly."),
    ("Pairs with PERSONAL_OPERATING_CODE execution (ship over plan): the dream becomes real only when acted "
     "on. Janie's self-directed agency is the literary form of the SNIPED operator who acts on a held truth "
     "rather than waiting for the horizon."),
    ["Ships at a distance have every man's wish on board.",
     "Now, women forget all those things they don't want to remember ... The dream is the truth. Then they act and do things accordingly."],
    ["their-eyes", "hurston", "agency", "self-direction", "voice"])

add(8, TE, F_TE, AUTH_H, "aesthetics",
    "The pear tree · awakening, organic union, and the personal ideal",
    ("Under the blossoming pear tree the young Janie sees the bee sink into the bloom and takes it as a "
     "vision of harmonious, ecstatic union · her measure for love and a life. The image becomes the "
     "standard she tests every relationship against, including her recognition of Tea Cake as a glance "
     "from God, a bee to a blossom."),
    ("Define your own ideal from a true felt image, not an inherited prescription, and measure choices "
     "against it. A vivid personal standard, held precisely, is what lets you recognize the real thing and "
     "refuse the counterfeit."),
    ("Aesthetic backing for the SNIPED locked visual direction: a precise personal ideal (the pear tree) is "
     "what gives taste its spine. SNIPED measures every frame against a held standard rather than a "
     "borrowed one (B4 aesthetic doctrine · taste as a discipline)."),
    ["He could be a bee to a blossom, a pear tree blossom in the spring.",
     "He was a glance from God."],
    ["their-eyes", "hurston", "personal-ideal", "taste", "awakening", "voice-of-form"])

add(9, TE, F_TE, AUTH_H, "aesthetics",
    "Vernacular as serious craft · free indirect voice and the dignity of dialect",
    ("Hurston renders her characters' Black Southern vernacular in full, and moves between a lyrical "
     "narrating voice and the characters' speech without condescension. The dialect is not local color; it "
     "is treated as a complete, capable literary instrument. Voice itself is the novel's argument for "
     "dignity."),
    ("Render a voice in its own register rather than translating it into a prestige dialect. Treating a "
     "vernacular as fully capable, not as decoration, is itself a statement of respect. The medium carries "
     "the dignity."),
    ("The literary anchor for SNIPED voice discipline: speak in the subject's own register, never flatten "
     "it to a prestige default. The same respect Hurston pays dialect, SNIPED pays a subject's actual "
     "self-presentation (B4 + the Lineage Doctrine)."),
    ["Hurston's narration moves between lyric and vernacular without condescension · the dialect treated as a complete literary instrument"],
    ["their-eyes", "hurston", "vernacular", "voice", "craft", "dignity"])

add(10, TE, F_TE, AUTH_H, "lineage",
    "The porch · communal storytelling and dignity reclaimed after labor",
    ("At sundown the porch sitters, who had been tongueless, earless, eyeless conveniences during the "
     "workday, become lords of sounds: they pass nations through their mouths and sit in judgment. "
     "Storytelling on the porch is where a community reclaims its humanity from the day's labor and holds "
     "its collective memory and verdicts."),
    ("Protect the gathering where a community tells its own story · that is where dignity is reclaimed and "
     "memory is kept. The right to narrate and to judge your own world is not a leisure activity; it is how "
     "a people stays human."),
    ("The Lineage Doctrine in a single image: the porch is the from-inside gathering where a culture "
     "narrates itself. SNIPED's cultural documentation aims to sit on the porch, not photograph it from "
     "the road · the scene-density / from-inside stance."),
    ["These sitters had been tongueless, earless, eyeless conveniences all day long ... But now ... They became lords of sounds and lesser things. They passed nations through their mouths. They sat in judgment."],
    ["their-eyes", "hurston", "oral-tradition", "communal-storytelling", "cultural-memory", "from-inside"])

add(11, TE, F_TE, AUTH_H, "culture",
    "Finding her voice · Janie's silencing under Joe and her reclamation of speech",
    ("Joe Starks raises Janie to a pedestal and silences her · she is not to speak on the store porch, her "
     "voice belongs to him. Her growth is the slow, then decisive, reclamation of her own speech, "
     "culminating in her refusal to stay tongueless. Selfhood in the novel is inseparable from the right "
     "to speak."),
    ("Watch for the gilded silencing · being put on a pedestal can be the same as being denied a voice. "
     "Self-possession is measured by whether you still get to speak in your own house. Reclaim the voice "
     "before anything else."),
    ("Directly tied to the SNIPED refusal to let a polished surface replace a real voice. Janie on Joe's "
     "pedestal is the warning against image without agency · SNIPED's whole method keeps the subject's "
     "voice intact under the polish."),
    ["Joe Starks puts Janie on a pedestal and forbids her the porch · selfhood returns only when she reclaims her own speech"],
    ["their-eyes", "hurston", "voice", "self-possession", "identity-formation"])

add(12, TE, F_TE, AUTH_H, "culture",
    "The horizon pulled in · living fully and the return home",
    ("Janie returns from burying Tea Cake having lived fully, and the novel closes with her pulling in her "
     "horizon like a great fish-net, draping it over her shoulder · so much of life in its meshes. Having "
     "gone to the horizon and back, she possesses her own life and can tell it. The journey was the point, "
     "and the telling completes it."),
    ("A life fully lived is one you can pull in and possess, then tell. Go to the horizon and come back "
     "with the experience in your net · the round trip, lived and then narrated, is what makes a life "
     "yours."),
    ("Pairs with the Perennial-Seller / long-arc patience in the corpus and the SNIPED documentary "
     "instinct: live the thing fully, then tell it. The framed narration (Janie telling Pheoby) is the "
     "documentation impulse SNIPED runs on."),
    ["She pulled in her horizon like a great fish-net. Pulled it from around the waist of the world and draped it over her shoulder. So much of life in its meshes!"],
    ["their-eyes", "hurston", "the-horizon", "lived-fully", "narration"])

add(13, TE, F_TE, AUTH_H, "lineage",
    "Folklore, judgment, and the right to narrate one's own world",
    ("Hurston, a trained folklorist, threads the novel with proverb, signifying, courtroom and porch "
     "judgment, and the rhythms of oral culture. The community claims the authority to narrate and to "
     "judge · who tells the story and who renders the verdict is itself contested and reclaimed throughout."),
    ("The authority to narrate and to judge your own world is a thing to be claimed, not granted. Folklore "
     "and proverb are not quaint · they are a culture's accumulated judgment, its working memory."),
    ("Foundational for the Lineage Doctrine and BATCH_010 (culture / Black culture): the canon documents "
     "from inside the oral tradition. SNIPED's documentation should carry the community's own forms of "
     "judgment and memory, not impose an outside frame."),
    ["the porch sitters passed nations through their mouths · they sat in judgment (the community claiming the authority to narrate and judge its own world)"],
    ["their-eyes", "hurston", "folklore", "oral-tradition", "authority-to-narrate", "inherited-story"])

# ===========================================================================
# THE COLOR PURPLE (Walker) · 6
# ===========================================================================
add(14, CP, F_CP, AUTH_W, "aesthetics",
    "Epistolary voice · letters to God and survival narrated in the subject's own vernacular",
    ("The Color Purple is told entirely in Celie's letters · first to God, then to her sister Nettie · in "
     "her own unschooled, exact vernacular. The form refuses any mediating literary narrator: the reader "
     "hears Celie directly, survival recorded in the first person as it happens. The plainness is the "
     "power."),
    ("Let the subject narrate in the first person and in their own words · the unmediated voice carries a "
     "truth no polished third-person summary can. Plain, exact language from inside an experience beats "
     "elegant language about it."),
    ("The strongest argument in the corpus for first-person, unmediated voice · the SNIPED principle that "
     "the subject's own register is the deliverable, not a prettified version of it. Pairs with B2 "
     "first-person founder voice and the Lineage Doctrine."),
    ["Dear God, I am fourteen years old. I have always been a good girl. Maybe you can give me a sign letting me know what is happening to me."],
    ["color-purple", "walker", "epistolary-voice", "first-person", "vernacular", "voice"])

add(15, CP, F_CP, AUTH_W, "culture",
    "The unspeakable made speakable · writing as survival and endurance",
    ("Celie writes because she has been told to tell nobody but God · so the letters are how she survives "
     "abuse that cannot be spoken aloud. Putting the unspeakable into written words is itself the act of "
     "endurance and, eventually, of becoming a self who can be addressed and answered."),
    ("Naming the unspeakable, even privately and imperfectly, is an act of survival. The record kept under "
     "pressure is not just documentation · it is how a self stays intact and eventually claims standing."),
    ("Reinforces the SNIPED conviction that the work documents from inside hardship, not from a comfortable "
     "remove. Celie's letters are the from-inside record · the Lineage Doctrine's refusal of single-visit "
     "tourism, lived at the level of one voice."),
    ["the letters are written because Celie was told to tell nobody but God · the unspeakable put into words is the act of survival"],
    ["color-purple", "walker", "survival", "writing-as-endurance", "cultural-memory"])

add(16, CP, F_CP, AUTH_W, "culture",
    "Sisterhood and solidarity · liberation through Celie, Nettie, and Shug",
    ("Celie's liberation is not solitary · it comes through bonds with women: Nettie's surviving letters, "
     "and above all Shug Avery, who teaches Celie to value herself, her body, and her own perception. "
     "Freedom in the novel is relational · it is conferred and sustained in solidarity, not seized alone."),
    ("Liberation is usually relational · someone has to model self-worth before you can claim it. Build and "
     "protect the bonds that confer dignity; they are the mechanism of becoming, not a soft extra."),
    ("Tempers the lone-operator frame: PERSONAL_OPERATING_CODE ownership is internal, but Celie shows that "
     "self-worth is often first conferred by a relationship. Backs the SNIPED scene-density / lineage "
     "thinking · you become inside a community, not apart from it."),
    ["Shug Avery teaches Celie to value herself · liberation conferred and sustained in solidarity, not seized alone"],
    ["color-purple", "walker", "sisterhood", "solidarity", "liberation", "scene-density"])

add(17, CP, F_CP, AUTH_W, "culture",
    "From object to subject · Celie's arc of self-authorship",
    ("Across the letters Celie moves from a girl things are done to · silenced, married off, beaten · into "
     "a woman who runs her own business, names her own desire, and addresses her sister and the world as an "
     "equal. The epistolary form lets the reader watch a subject author herself into existence sentence by "
     "sentence."),
    ("Selfhood is authored over time, in the first person, through the accumulation of small reclaimed "
     "acts. The arc from object to subject is built, not declared · each sentence in your own voice is a "
     "brick."),
    ("The literary form of the SNIPED becoming-the-operator arc: identity is authored incrementally in your "
     "own voice (cf. PERSONAL_OPERATING_CODE consistency / compound-arc). Celie is the case study in "
     "self-authorship as a built thing."),
    ["Celie moves from a girl things are done to into a woman who names her own desire and addresses the world as an equal"],
    ["color-purple", "walker", "self-authorship", "identity-formation", "compound-arc"])

add(18, CP, F_CP, AUTH_W, "lineage",
    "Spirituality reimagined · God from patriarchal master into trees, stars, and the Ultimate Ancestor",
    ("Through Shug, the novel transforms God from a patriarchal white male authority into something diffuse "
     "and immanent · trees, stars, wind, the color purple in a field, everything. Walker frames the book "
     "as a search for the Ultimate Ancestor: the sacred relocated from an imposed hierarchy into inherited, "
     "living nature."),
    ("Relocate the sacred (and the authoritative) from an imposed external hierarchy into what is inherited "
     "and immanent. Reclaiming the frame · who and what gets called God or authority · is itself an act of "
     "liberation."),
    ("Deep Lineage-Doctrine resonance: authority and the sacred are reclaimed from an imposed master-frame "
     "into the inherited and ancestral. The same move SNIPED makes refusing an outside cultural template "
     "in favor of the lineage's own."),
    ["the pagan transformation of God from patriarchal male supremacist into trees, stars, wind, and everything else",
     "a book that begins Dear God ... about the desire to encounter the Ultimate Ancestor"],
    ["color-purple", "walker", "spirituality", "reclaiming-the-frame", "ultimate-ancestor", "inherited-story"])

add(19, CP, F_CP, AUTH_W, "culture",
    "Refusing to be silenced · Celie's curse and the turn against Mr.",
    ("Celie's decisive turn is verbal: she finally speaks against Mr., the man who has owned and beaten "
     "her, declaring that until he does right by her everything he touches will crumble. The reclaimed "
     "voice is the hinge of her freedom · speech is the act that breaks the long submission."),
    ("The hinge of liberation is usually an act of speech · saying the true thing to the face of the power "
     "that silenced you. The reclaimed voice is not the reward of freedom; it is the mechanism of it."),
    ("Echoes Janie's reclamation (chunk 11) and the SNIPED refusal to let polish replace voice · across the "
     "canon, freedom arrives as speech. The operator keeps the subject's voice intact and, when needed, "
     "loud."),
    ["Celie finally speaks against Mr. · the reclaimed voice is the hinge of her freedom"],
    ["color-purple", "walker", "voice", "refusal", "liberation"])

# ===========================================================================
# WALKER COMPANION NOVELS (light coverage) · 2
# ===========================================================================
add(20, TMF, F_CP, AUTH_W, "lineage",
    "The Temple of My Familiar · ancestral memory and inherited story across generations",
    ("In the collection's second novel, Walker spans continents and lifetimes, weaving characters' "
     "remembered and dreamed ancestral pasts into the present. Story is treated as inheritance · identity "
     "is assembled from the memories and myths handed down, recovered, and retold across generations."),
    ("Treat inherited story as a live inheritance to recover and retell, not a closed archive. Identity is "
     "assembled from what is handed down; the work of remembering is ongoing and generational."),
    ("Direct primary-source weight for the Lineage Doctrine's generational dimension · identity built from "
     "inherited and recovered story. Light-coverage companion (per operator decision · main weight stays "
     "on The Color Purple)."),
    ["Walker weaves remembered and dreamed ancestral pasts into the present · identity assembled from inherited story"],
    ["temple-of-my-familiar", "walker", "ancestral-memory", "inherited-story", "generational"])

add(21, PSJ, F_CP, AUTH_W, "culture",
    "Possessing the Secret of Joy · cultural trauma, ritual harm, and the duty of witness",
    ("The collection's third novel follows Tashi through the lasting trauma of a cultural ritual of genital "
     "cutting, insisting that the reader witness harm done in the name of tradition. Walker holds the hard "
     "tension: deep respect for a culture alongside the refusal to look away from a practice that wounds "
     "its women."),
    ("Loving a culture from inside includes the duty to witness its harms honestly, not to launder them. "
     "Reverence and unflinching witness are not opposites · the from-inside stance earns the standing to "
     "name what wounds."),
    ("Sharpens the Lineage Doctrine against sentimentality: documenting from inside a lineage means honest "
     "witness, including of harm · not a tourist's flattering gloss. Light-coverage companion (per operator "
     "decision)."),
    ["Tashi carries the lasting trauma of a cultural ritual · Walker refuses to look away from harm done in tradition's name"],
    ["possessing-the-secret-of-joy", "walker", "cultural-trauma", "witness", "honest-from-inside"])

# ===========================================================================
# CROSS-AUTHOR SYNTHESIS · 7
# ===========================================================================
add(22, SYN, F_TE, SNIPED, "lineage",
    "The Black women's literary canon as Lineage-Doctrine backing · from inside, never tourist",
    ("Morrison, Hurston, and Walker each write from deep inside the Black communities they render · as "
     "members and inheritors, never as visiting observers. Together they are the primary-source literary "
     "grounding for working from inside a lineage: the authority of the telling comes from belonging to "
     "the world told."),
    ("Earn the authority to document a world by belonging to it or committing to it for the long haul. "
     "From-inside telling is not a style choice · it is the source of the work's legitimacy. Single-visit "
     "tourism produces a flattering, false record."),
    ("The literary canon behind the locked Lineage Doctrine (feedback_lineage_doctrine · single-visit "
     "cultural tourism refused). This canon is the bar SNIPED's cultural documentation measures itself "
     "against · and the reason scene-density beats breadth."),
    ["Morrison, Hurston, and Walker each write from inside the communities they render · belonging is the source of the telling's authority"],
    ["lineage-doctrine", "from-inside", "cultural-documentation", "morrison", "hurston", "walker"])

add(23, SYN, F_CP, SNIPED, "lineage",
    "Voice and vernacular as craft and dignity · the anti-shallow-content thesis",
    ("Across the three authors, the deliberate use of vernacular and first-person voice (Celie's letters, "
     "Janie's porch speech, Claudia's we) is not folksy texture · it is rigorous craft that confers "
     "dignity on its speakers. The canon's seriousness lives precisely in how carefully it renders voices "
     "the prestige culture dismissed."),
    ("Seriousness shows in how carefully you render the voices others dismiss. The opposite of shallow "
     "content is not complexity for its own sake · it is the disciplined respect that treats every subject "
     "and register as worth full craft."),
    ("The literary embodiment of SNIPED's refusal to become shallow content (the operator brief's core "
     "value): depth is respect rendered as craft. This canon is the standard against which SNIPED checks "
     "whether its own work is serious or merely pretty."),
    ["the vernacular and first-person voice across the canon is rigorous craft that confers dignity, not folksy texture"],
    ["anti-shallow-content", "voice", "vernacular", "craft", "dignity", "artistic-seriousness"])

add(24, SYN, F_BE, SNIPED, "culture",
    "Black interiority and double-consciousness · who narrates, who is seen",
    ("All three novels insist on full Black interiority · rich inner lives rendered from within · and "
     "dramatize the doubled awareness of being seen through others' (often white, often patriarchal) eyes "
     "while holding one's own self-perception. The central contest is who gets to narrate a life and on "
     "whose terms it is seen."),
    ("The question who narrates and on whose terms a subject is seen is the whole game. Render full "
     "interiority from within; never let an external gaze be the only frame on a person's life."),
    ("The literary articulation of the SNIPED portrait ethic: render the full interior person, not the "
     "outside gaze's reduction. Double-consciousness names exactly the trap SNIPED portraiture refuses · "
     "the subject seen on their own terms (B5 photography canon)."),
    ["the canon renders Black interiority from within while dramatizing the doubled awareness of being seen through others' eyes"],
    ["black-interiority", "double-consciousness", "the-gaze", "whose-story-gets-told", "to-be-seen"])

add(25, SYN, F_TE, SNIPED, "lineage",
    "Cultural memory, survival, and inherited story as the through-line",
    ("Beneath their different forms, the three novels share a through-line: cultural memory carried "
     "collectively (the marigolds, the porch, the letters, the ancestral pasts), survival recorded from "
     "inside, and identity assembled from inherited story. Memory is an active, communal, ongoing labor, "
     "not a static archive."),
    ("Cultural memory is maintained labor · it is carried, confessed, and retold by a community, or it is "
     "lost. Build the practices (the gathering, the record) that keep a lineage's memory active and "
     "honest."),
    ("The structural rationale for SNIPED's cultural documentation as ongoing practice, not one-off "
     "capture · and for scene-density (depth in a community over time) over breadth. The canon shows "
     "memory as communal maintained labor."),
    ["cultural memory carried collectively across the canon · the marigolds, the porch, the letters, the ancestral pasts"],
    ["cultural-memory", "survival", "inherited-story", "lineage-doctrine", "scene-density"])

add(26, SYN, F_BE, SNIPED, "operator-doctrine",
    "Artistic seriousness as refusal · the canon SNIPED measures itself against",
    ("Morrison, Hurston, and Walker are Pulitzer- and Nobel-level artists who treated Black life with the "
     "full apparatus of serious literature · structural ambition, formal innovation, moral weight. Their "
     "seriousness is a refusal: of minstrelsy, of simplification, of the demand to be palatable. The "
     "standard they set is depth as a moral and craft commitment."),
    ("Hold your work to the standard of the serious canon in your field, not the standard of the feed. "
     "Artistic seriousness is a refusal · of the shallow, the palatable, the simplified · sustained as a "
     "craft and moral commitment over a career."),
    ("Directly tied to the SNIPED operator identity (operator-doctrine): the refusal to make shallow "
     "content is the same refusal this canon embodies. Pairs with INTELLECTUAL_ARTIST_FRAME (MJ's craft "
     "seriousness) · performance and literature, same bar. This canon is the literary measuring stick."),
    ["Morrison, Hurston, and Walker treated Black life with the full apparatus of serious literature · seriousness as a refusal of the palatable"],
    ["artistic-seriousness", "refusal", "anti-shallow-content", "operator-identity", "intellectual-artist-frame"])

add(27, SYN, F_BE, SNIPED, "aesthetics",
    "Witness, dignity, and the gaze · the literary canon behind SNIPED portraiture",
    ("The canon's preoccupation with how people are seen · Pecola erased by every gaze, Janie put on a "
     "pedestal, Celie made invisible then finally addressed · is a sustained meditation on the ethics of "
     "the gaze. Across all three, to be truly witnessed with dignity is the rescue, and to be looked at "
     "without being seen is the harm."),
    ("The ethics of looking is the ethics of the work: every act of rendering a person either confers "
     "dignity or withholds it. Aim the gaze to witness fully, never to reduce. There is no neutral lens."),
    ("The literary foundation under the SNIPED photography canon (B5) and quiet-luxury portrait doctrine "
     "(B4): the camera is a gaze with the same ethical weight the novels assign it. SNIPED portraiture is "
     "the practice of the dignifying gaze these books argue for."),
    ["across the canon, to be truly witnessed with dignity is the rescue · to be looked at without being seen is the harm"],
    ["the-gaze", "witness", "dignity", "portraiture", "aesthetics", "photography-canon"])

add(28, SYN, F_CP, SNIPED, "operator-doctrine",
    "Reclaiming the frame · authority, naming, and self-definition across the canon",
    ("A shared move runs through the canon: reclaiming the frame that defines you · Celie remaking God and "
     "naming her own worth, Janie reclaiming her speech, Claudia's we narrating its own town. Liberation "
     "is repeatedly the act of seizing the authority to name and define rather than accepting an imposed "
     "definition."),
    ("Reclaim the frame before you optimize within it. The decisive move is seizing the authority to define "
     "and name your own terms · accepting someone else's frame is the deeper defeat than losing inside it."),
    ("The operator-doctrine throughline: SNIPED's whole positioning posture is reclaiming the frame "
     "(refusal-positioning, defining its own lane and standards) rather than competing on imposed terms. "
     "This canon is the cultural-canon backing for definition-on-your-own-terms."),
    ["the canon's shared move is reclaiming the frame that defines you · seizing the authority to name and self-define"],
    ["reclaiming-the-frame", "self-definition", "authority-to-narrate", "operator-identity", "positioning"])


# ===========================================================================
# Write JSONL + em-dash sweep
# ===========================================================================

def main():
    OUT_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSONL.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"Wrote {len(chunks)} chunks to {OUT_JSONL}")

    em_char = chr(0x2014)
    text = OUT_JSONL.read_text(encoding="utf-8")
    n = text.count(em_char)
    if n:
        print(f"WARNING: {n} em-dashes in output. Sweeping.")
        OUT_JSONL.write_text(text.replace(em_char, " · "), encoding="utf-8")
    else:
        print("No em-dashes in output.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
