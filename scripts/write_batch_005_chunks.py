#!/usr/bin/env python3
"""
BATCH_005 chunking · photography canon at depth
Output: 01_KNOWLEDGE_BASE/batches/BATCH_005_CHUNKS.jsonl

Schema (per AGENTS.md): chunk_id, batch_id, source_title, source_file, author,
domain, concept, summary, usable_principle, sniped_relevance, direct_quotes, tags.

batch_id = "BATCH_005" (operator decision · short form).
Domain enum: photography-theory, aesthetics, visual-literacy, portraiture,
documentary, sequencing, art-series, composition, color, taste,
operator-doctrine, client-application.

Sources: 32 extracted into batch_005_extracted/. 4 OCR-deferred (Leibovitz epub,
Cartier-Bresson scan, Hughes/Haas scan, Szarkowski 1973 scan). Tom King The
Operator was excluded per operator decision before extraction.
"""

import json
from pathlib import Path

OUT = Path.home() / "AI-Brain-Refinery" / "01_KNOWLEDGE_BASE" / "batches" / "BATCH_005_CHUNKS.jsonl"
OUT.parent.mkdir(parents=True, exist_ok=True)

BATCH = "BATCH_005"
CHUNKS = []


def add(*, source_title, source_file, author, domain, concept,
        summary, usable_principle, sniped_relevance,
        direct_quotes=None, tags=None):
    cid = f"batch-005-chunk-{len(CHUNKS)+1:03d}"
    CHUNKS.append({
        "chunk_id": cid,
        "batch_id": BATCH,
        "source_title": source_title,
        "source_file": source_file,
        "author": author,
        "domain": domain,
        "concept": concept,
        "summary": summary.strip(),
        "usable_principle": usable_principle.strip(),
        "sniped_relevance": sniped_relevance.strip(),
        "direct_quotes": direct_quotes or [],
        "tags": tags or [],
    })


# =====================================================================
# CLUSTER 1 · SONTAG · ON PHOTOGRAPHY · 12 chunks
# =====================================================================
S1_T = "On Photography"
S1_F = "sontag_on_photography.txt"
S1_A = "Susan Sontag"

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="photography-theory",
    concept="Photography as appropriation · the camera as a way of taking the world",
    summary="Sontag's opening claim: to photograph is to appropriate the thing photographed. It puts the photographer in a certain relation to the world that feels like knowledge and therefore like power. Cameras turn the world into images and images into trophies. The act of photographing is not detached observation; it is a low-cost form of acquisition. Photographs do not just show; they take.",
    usable_principle="Treat every shutter press as an act of taking. Decide in advance what you are taking from the subject and what you are giving back. A frame the subject cannot recognize as theirs has been taken without exchange. The exchange is what separates portraiture from appropriation.",
    sniped_relevance="SNIPED's $1,500 Reset floor and the locked client-deliverable contract are the answer Sontag's argument forces. The client pays for the frame, owns the rights, and walks out with a finished gallery. The exchange is structural, not implicit. Every BJ shoot inverts the Sontag default: subject gains the trophy, photographer is paid for the labor. Cite this when defending the floor against discount pressure.",
    direct_quotes=[
        "To photograph is to appropriate the thing photographed.",
        "It means putting oneself into a certain relation to the world that feels like knowledge · and, therefore, like power."
    ],
    tags=["sontag","photography-as-appropriation","power","ethics","reset-floor-defense"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="photography-theory",
    concept="Anthology of images · the world reframed as a museum without walls",
    summary="Sontag describes the cumulative effect of photography on modern consciousness: the world becomes an anthology of images. People used to live in the world; now they collect it. The photographic image installs a permanent secondary reality that the primary one is compared against. Tourists do not look at landscapes, they look at landscapes-to-be-photographed. The camera precedes seeing.",
    usable_principle="When working with subjects who already know what a photograph of them looks like, lead with the work of moving them off their internal template. The mirror reflex collapses the frame into known imagery. Direction that surprises them rebuilds the seeing.",
    sniped_relevance="The Direction Stack's 90-second opener exists to interrupt the subject's internal template. Founders walking onto set already know what their LinkedIn headshot looks like; the directive opener replaces that template before the camera fires. Sontag's argument is why the opener works · she names what the opener is overriding.",
    direct_quotes=[
        "Today everything exists to end in a photograph.",
        "Recently, photography has become almost as widely practiced an amusement as sex and dancing."
    ],
    tags=["sontag","anthology-of-images","direction-stack","template-override","mirror-reflex"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="ethics",
    concept="Non-intervention · the camera as alibi",
    summary="Sontag's hardest claim: the act of photographing is, structurally, non-intervention. The photographer chooses to record rather than to act. The photo is the alibi for the inaction. To photograph someone is to participate in their mortality, vulnerability, mutability without intervening. The neutrality of the camera is a moral position, not a moral absence.",
    usable_principle="Decide before each shoot what you would do if your subject needed help mid-frame · keep shooting, intervene, both. The decision is moral architecture, not improvisation. Premium portraiture requires the operator to be on the subject's side of the lens, not behind it.",
    sniped_relevance="This grounds the SNIPED hospitality layer (`intel_hospitality_layer.md` · Guidara). Hospitality is what the camera doesn't do by default. BJ's pre-shoot protocols (water, music, the 90-second opener, the rest break, the post-shoot debrief) put service in places where Sontag's default would leave only observation. The hospitality layer is the ethical correction to non-intervention.",
    direct_quotes=[
        "To take a photograph is to participate in another person's mortality, vulnerability, mutability.",
        "The act of photographing is more than passive observing. Like sexual voyeurism, it is a way of at least tacitly, often explicitly, encouraging whatever is going on to keep on happening."
    ],
    tags=["sontag","non-intervention","ethics","hospitality-correction","guidara-cross-reference"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="photography-theory",
    concept="The heroism of vision · photography as a way of seeing taught",
    summary="In the Heroism of Vision essay, Sontag credits photography with teaching modern people how to see. The medium did not just record what was already considered beautiful; it expanded the catalog of the visible. Industrial backstreets, machine parts, working hands, blank faces · all entered the visual canon through the lens. Photography is an education in attention.",
    usable_principle="The lane you teach the audience to see in is the lane they will pay you to work in. Repetition of a specific way of seeing is how you take ownership of a category. Every chapter card extends the audience's eye further into your aesthetic.",
    sniped_relevance="This is the theoretical foundation for the Chapter Card system and the locked v3 LUXURY EDITORIAL preset. By repeating the same visual vocabulary across every Card, BJ is teaching the audience how to see SNIPED's aesthetic. Each Card adds a tile to the museum-room. Sontag explains why the discipline of repetition pays · the eye is being educated, not just shown.",
    direct_quotes=[
        "Photography has the unappealing reputation of being the most realistic, therefore facile, of the mimetic arts. In fact, it is the one art that has managed to carry out the grandiose, century-old threats of a Surrealist takeover of the modern sensibility."
    ],
    tags=["sontag","heroism-of-vision","education-of-attention","chapter-card","repetition","scene-density"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="aesthetics",
    concept="Photographic seeing · what cameras taught painters",
    summary="Sontag traces how photographic ways of seeing reshaped painting, advertising, and fashion. The cropped frame, the off-center subject, the frozen motion · all originated in the camera's mechanical defaults and were absorbed back into the trained eye. The aesthetic of the snapshot, once an accident, became a chosen language. The photographer's default settings became the culture's preferred view.",
    usable_principle="When the technical default of a tool becomes culture's preferred look, the tool stops being neutral and becomes a stylistic position. The locked SNIPED toolkit (focal length, aperture, body posture, retouch pass) is a stylistic position even when it feels like routine.",
    sniped_relevance="The SNIPED locked look v3 LUXURY is exactly the kind of internalized default Sontag describes · the v3 preset is not just a recipe, it is a stylistic claim. Reading Sontag here protects the operator from treating the locked toolkit as 'just how I shoot.' It is the chosen language, and being able to name that lets BJ defend it.",
    direct_quotes=[
        "Through photographs, we now have an intimate relation to events we have no power to influence."
    ],
    tags=["sontag","photographic-seeing","style-as-position","locked-look-defense","preset-doctrine"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="photography-theory",
    concept="Time and the photograph · the image as memento mori",
    summary="Photographs are essentially elegiac. To shoot is to mark a slice of time as past. The image is always after the fact. Sontag argues this is why even the most joyful photographs carry an undertow of mourning · the frame's existence requires the moment's death. Photography is the only medium where the act of preservation is structurally also an act of loss.",
    usable_principle="Hero frames carry weight in proportion to how clearly they mark a moment that will not repeat. Specific date, specific light, specific subject in a specific phase of their life. Generic frames refuse to be elegiac, and elegy is where weight lives.",
    sniped_relevance="The Direction Stack chapter rollout doctrine treats each Chapter Card as a marker of a specific moment in the subject's career arc. The named date stamp (e.g., `CH01_Yae_2026-05-13`) is not metadata, it is part of the meaning · Sontag explains why. The B&W Card dual-register rule deepens this · B&W is mortality, color is the moment.",
    direct_quotes=[
        "All photographs are memento mori. To take a photograph is to participate in another person's mortality.",
        "Photography is an elegiac art, a twilight art."
    ],
    tags=["sontag","memento-mori","elegy","chapter-card-naming","bw-register","time"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="photography-theory",
    concept="Image-world vs world · how photographs replace the things they show",
    summary="In the final essay, Sontag argues that photographs progressively supplant the world they were meant to record. Tourists no longer remember the trip; they remember the photographs of the trip. The photograph becomes the more durable, more circulated, more authoritative version of the event. The world becomes a second-order reality to its own image.",
    usable_principle="Build the artifact so it can outlive the moment with no contradiction. Every Chapter Card and HERO post must be coherent on its own without the original context · because that context will not travel with the file.",
    sniped_relevance="This is why the Pixieset gallery + the Op Kit + the chapter card carousel all repeat the same image at different scales. The image needs to be its own primary record. The Direction Stack book is the long-form version · the printed photograph as authoritative memory artifact in an AI-saturated feed.",
    direct_quotes=[
        "Needing to have reality confirmed and experience enhanced by photographs is an aesthetic consumerism to which everyone is now addicted."
    ],
    tags=["sontag","image-world","artifact","durability","direction-stack-book"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="ethics",
    concept="The democratic suspension · everyone is interesting",
    summary="Photography, Sontag argues, is fundamentally democratic in subject matter. The camera bestows interest equally · a piece of trash and a head of state receive the same technical treatment. This is photography's ethical triumph and its ethical danger. It refuses hierarchies of importance imposed from outside the frame, which is liberating, but it also flattens distinctions that matter, which is corrosive.",
    usable_principle="When the camera flattens importance, the photographer must reintroduce it through framing, sequencing, and context. Editorial portraiture is the discipline of putting back what the camera has dissolved.",
    sniped_relevance="SNIPED's editorial discipline is the directed correction Sontag's argument calls for. The locked aesthetic refuses the flattening · each frame carries chosen importance via the monochromatic palette, the body architecture, the clinical retouch. This is why SNIPED is editorial photography, not documentary photography · the photographer reintroduces hierarchy that the camera tried to dissolve.",
    direct_quotes=[
        "There is no way to suppress the tendency inherent in all photographs to accord value to their subjects.",
        "The camera makes everyone a tourist in other people's reality, and eventually in one's own."
    ],
    tags=["sontag","democratic-suspension","editorial-discipline","framing","hierarchy-reintroduction"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="taste",
    concept="Photographs cannot be argued with · authority by silence",
    summary="Sontag observes that photographs have a peculiar form of evidential authority. They do not make arguments. They simply assert · here is what was there. This unargued quality is the source of both their persuasive power and their resistance to critique. A photograph closes the conversation; a sentence opens one. The image's silence is what makes it authoritative.",
    usable_principle="When persuasion is the job, lead with the image. When critique or revision is the job, lead with the words. Mixing the two confuses the audience about which mode they are in.",
    sniped_relevance="LinkedIn POV posts pair an image with a 7-sentence argument. The image asserts, the prose extends. The split-register works because Sontag's law of image-authority holds · the photograph carries the unargued weight, the text does the negotiable interpretive work. Reversing the order (text first, image afterthought) loses the post's authority. Image-first is locked.",
    direct_quotes=[
        "While a painting or a prose description can never be other than a narrowly selective interpretation, a photograph can be treated as a narrowly selective transparency."
    ],
    tags=["sontag","unargued-authority","image-first","linkedin-pov","persuasion"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="aesthetics",
    concept="The surrealist legacy · cameras as the original surrealist instrument",
    summary="Sontag's central thesis in the third essay: photography is the most successful Surrealist enterprise of the twentieth century. Not because photographers chose to be Surrealists, but because the camera's mechanical defaults produce Surrealist juxtapositions automatically. Strange angles, frozen instants, decontextualized fragments · the camera makes everything available for unlikely combination.",
    usable_principle="Trust the camera to find unintended adjacencies. The work is to recognize them after the fact, not to construct them in advance. Some of the strongest frames will be ones the photographer did not plan.",
    sniped_relevance="The Track B AI composite workflow (Seedream, Higgsfield, Nano Banana) is the digital extension of Sontag's surrealist photo logic · world-construction layered onto real captures. The hybrid-operator stance (`intel_ai_sentiment.md`) is defensible because the surrealist photo lineage Sontag names already accepted machine-generated juxtaposition as a legitimate creative move. AI for world-building, identity untouched.",
    direct_quotes=[
        "Photography is the only major art in which professional training and years of experience do not confer an insuperable advantage over the untrained and inexperienced.",
        "Surrealism lies at the heart of the photographic enterprise."
    ],
    tags=["sontag","surrealism","ai-defense","track-b","hybrid-operator-stance"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="photography-theory",
    concept="Photographs as fragments · the refusal of narrative",
    summary="A photograph is a fragment. It has no before and no after that the frame admits. The viewer constructs context, but the photograph itself refuses to provide one. This fragmentary nature is what distinguishes the photograph from cinema, painting, or prose. Sontag treats this as the medium's defining limitation and its defining freedom.",
    usable_principle="Single frames carry interpretation but not story. If a story is the job, build a sequence. The Trolley New Orleans frame works as five micro-portraits because the trolley window is a sequencing device. Plan the device before the moment.",
    sniped_relevance="The Chapter Card carousel format is the SNIPED solution to the fragment problem. Single frame as Card cover, additional frames as carousel slides, caption as connective tissue. The carousel is the sequencing device that overcomes the fragment limit Sontag names. The Direction Stack book extends the principle · sequenced frames build the narrative no single frame can carry.",
    direct_quotes=[
        "Photographs, which themselves explain nothing, are inexhaustible invitations to deduction, speculation, and fantasy."
    ],
    tags=["sontag","fragment","sequencing","carousel-format","direction-stack-book"])

add(source_title=S1_T, source_file=S1_F, author=S1_A,
    domain="client-application",
    concept="The grammar of seeing · how subjects learn to be photographed",
    summary="Sontag closes by noting that photography has trained its subjects, not just its viewers. Modern people pose because they know they are being photographed; they pose for the future photograph as much as for the present photographer. The subject's performance is itself a photographic effect. The photographer who does not account for this gets only the performance, not the person.",
    usable_principle="The first 20 frames of any session are the subject's prepared face. Burn through them. The work begins when the subject runs out of rehearsed expressions. Plan session length to outlast the preparation.",
    sniped_relevance="The Avedon duration principle (`study_richard_avedon.md` Step 4) is the operationalization of this Sontag observation. Long sessions break the rehearsed face. The 4-hour Reset block is sized for this reason, not just for technical setup. Founders arrive with their LinkedIn-template smile; the session has to run long enough for that smile to exhaust itself. Document the runtime as feature, not overhead, in the offer.",
    direct_quotes=[
        "Photographs really are experience captured, and the camera is the ideal arm of consciousness in its acquisitive mood."
    ],
    tags=["sontag","subject-performance","duration","avedon-bridge","reset-session-length","client-application"])

# =====================================================================
# CLUSTER 2 · BARTHES · CAMERA LUCIDA · 10 chunks
# =====================================================================
S2_T = "Camera Lucida: Reflections on Photography"
S2_F = "barthes_camera_lucida.txt"
S2_A = "Roland Barthes"

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="photography-theory",
    concept="The noeme · 'that-has-been' as photography's irreducible essence",
    summary="Barthes's central concept: the noeme of photography is 'that-has-been' (ça-a-été). Unlike painting or fiction, the photograph asserts existence at a specific past moment with non-negotiable evidential force. The photograph says 'this thing was here, in front of this lens, at this time' · and the assertion is structural, not stylistic. Every other property of the photograph (composition, framing, light) is secondary to this ontological claim.",
    usable_principle="When the goal is documentary weight, lean on the noeme. When the goal is editorial polish, the noeme is unavoidable backdrop, not strategy. Pretending the photograph does not assert existence is the mistake of weak editorial work.",
    sniped_relevance="Founders pay $1,500 partly because the noeme is what they cannot fake on iPhone. A Reset session produces a frame that says 'this founder, on this day, with this presence' in a way that AI generation structurally cannot. Barthes is the philosophical defense of the anti-faceless-AI position (`intel_ai_sentiment.md`). The noeme is the line.",
    direct_quotes=[
        "The name of Photography's noeme will therefore be: 'That-has-been.'",
        "The Photograph is literally an emanation of the referent."
    ],
    tags=["barthes","noeme","that-has-been","ontology","anti-ai-defense","reset-floor"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="photography-theory",
    concept="Studium and punctum · the two reading modes of any photograph",
    summary="Barthes distinguishes two ways a photograph engages a viewer. The studium is the cultural, informed, polite engagement · 'this is well composed, I see what the photographer was doing.' The punctum is the wound · the unplanned detail that pierces the viewer and refuses to be assimilated to the studium. Punctum is partial, unpredictable, and personal. It is the element the photographer cannot intentionally construct.",
    usable_principle="Compose for studium. Pray for punctum. The frame can be technically perfect (high studium) and still inert. The strongest frames carry an unplanned detail that refuses to be explained · the way a hand falls, an asymmetry in the eye, an accident of light on a fingernail. Do not retouch these out.",
    sniped_relevance="This is the philosophical basis for the SNIPED retouch discipline · pull back to 60% on the personal-work frames (`study_richard_avedon.md` Step 4) so punctum survives. The clinical retouch protects studium; restraint preserves punctum. The Aesthetic Statement's named depth weakness (flatness) is partly a punctum problem · everything that breaks the flat frame later turns out to be the wound, not the system.",
    direct_quotes=[
        "I called this element which rises from the scene, shoots out of it like an arrow, and pierces me, the punctum.",
        "Studium is of the order of liking, not of loving."
    ],
    tags=["barthes","studium","punctum","retouch-restraint","aesthetic-weakness-link","editorial-vs-personal"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="portraiture",
    concept="The four poses · subject as four simultaneous figures",
    summary="In the portrait, Barthes identifies four simultaneous people: the one I think I am, the one I want others to think I am, the one the photographer thinks I am, and the one the photographer uses to exhibit his art. The portrait is the negotiation between these four. The famous discomfort of being photographed comes from the impossibility of reconciling them.",
    usable_principle="As photographer, name which of the four you are working with and tell the subject. 'I am photographing the one you want others to see' produces a different session than 'I am photographing the one you actually are.' Most discomfort is caused by leaving the negotiation unspoken.",
    sniped_relevance="The 90-second Direction Stack opener is exactly this naming · BJ tells the founder which figure the session is producing. Op Kit is the LinkedIn version of the subject (the one they want others to see). Cultural Doc is the photographer's version (the one BJ uses to exhibit his art). Reset is the negotiation. Naming which mode each session occupies prevents the four-figures collision.",
    direct_quotes=[
        "I am at the same time: the one I think I am, the one I want others to think I am, the one the photographer thinks I am, and the one he makes use of to exhibit his art."
    ],
    tags=["barthes","four-poses","portrait-negotiation","direction-stack","reset-vs-op-kit-vs-cultural-doc"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="photography-theory",
    concept="The pose as photograph's primary act",
    summary="Barthes argues that the moment of being photographed is when the subject 'makes another body for myself.' The subject does not relax; the subject transforms into the future-image. This transformation is the actual photographic act, more than the shutter release. The subject's body becomes a sign, an inscription, a thing to be developed. The photographer captures not a person but a person becoming-a-picture.",
    usable_principle="Direct the becoming, not the being. The body-as-architecture rule already accepts this · chin position, hand task, posture · these are not poses of the natural body, they are the geometry of the person-as-image. Trying to capture the subject 'being themselves' misses Barthes's point that the camera changes the body the moment it points at it.",
    sniped_relevance="The aesthetic statement direction 'direct the body, not the face' (`feedback_edit_register_bifurcation.md`, `aesthetic_statement_v1.md`) IS Barthes's becoming-body principle in operational form. SNIPED already operates from this position; reading Barthes locks the theoretical grounding · this is not personal preference, it is the structural fact of being photographed.",
    direct_quotes=[
        "I constitute myself in the process of 'posing,' I instantaneously make another body for myself, I transform myself in advance into an image.",
        "Now, once I feel myself observed by the lens, everything changes: I constitute myself in the process of 'posing.'"
    ],
    tags=["barthes","becoming-body","pose","direct-the-body","aesthetic-statement-theoretical-ground"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="photography-theory",
    concept="The Winter Garden Photograph · the private essence that resists publication",
    summary="At the book's pivot, Barthes finds an old photograph of his mother as a child in a Winter Garden. The image carries her essence for him. He refuses to reproduce it in the book. The Winter Garden Photograph would mean nothing to a stranger; its truth is non-transferable. This is Barthes's final theoretical move · the deepest photographic truth is private, not public.",
    usable_principle="Some frames are for the subject alone. Build a delivery channel that protects these frames from public circulation. The strongest possible portrait of someone may be the one the public does not need to see.",
    sniped_relevance="The Pixieset gallery's password-protected, expiry-bounded delivery is the structural answer to Barthes's principle. Reset clients receive frames that may not all land on LinkedIn. The Direction Stack book separates private frames (carousel for client only) from public frames (HERO post). Two registers, both protected. Barthes is why the gallery system is not just convenience · it is ethics.",
    direct_quotes=[
        "I cannot reproduce the Winter Garden Photograph. It exists only for me. For you, it would be nothing but an indifferent picture."
    ],
    tags=["barthes","winter-garden","private-essence","pixieset-gallery","two-register-delivery","ethics-of-publication"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="photography-theory",
    concept="The air of the face · what survives mechanical reproduction",
    summary="Barthes searches for the property that lets a photograph carry the subject's truth and finds it in 'the air' · the impossible, irreducible, individual emanation of the face that some photographs preserve and others miss. The air is not in the features, not in the expression, not in the composition · it is in something the photograph either catches or does not. No technical excellence guarantees it.",
    usable_principle="Some frames have it, most do not. Train the cull to recognize the air, not to rank technical merit. The cull is the location where this skill develops · five passes, each looking for different qualities, the final pass looking only for the air.",
    sniped_relevance="The SNIPED 5-pass cull (per the production OS) is exactly the operational discipline Barthes's principle demands. Pass 1: technical. Pass 2: composition. Pass 3: pose. Pass 4: emotional weight. Pass 5: the air · the frame that carries the person, not the picture. The 5-pass system would not exist if the air collapsed into technique. Barthes is why the last pass cannot be skipped.",
    direct_quotes=[
        "The air is the luminous shadow which accompanies the body; and if the photograph fails to show this air, then the body moves without a shadow, and once this shadow is severed, as in the myth of the Woman without a Shadow, there remains no more than a sterile body."
    ],
    tags=["barthes","the-air","5-pass-cull","selection-discipline","production-os"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="photography-theory",
    concept="Photography and madness · the violent intimacy of the trace",
    summary="Barthes closes by noting that photography is potentially mad. The image's claim 'this was real' makes it different from every other representation. A painting can be a hallucination; a photograph is a hallucination with a chemical anchor. This combination produces a particular kind of mourning, longing, and obsession that photography alone is capable of. The photograph is intimate in a way that other media cannot be.",
    usable_principle="Take the emotional consequences seriously. Some shoots will produce images that the subject cannot look at for years. Some will produce images they look at every day. The photographer is not neutral to either outcome. The work has weight that other client-facing work does not.",
    sniped_relevance="This is why the SNIPED post-delivery sequence (`sniped-post-delivery` skill) extends 14 days beyond gallery handoff. Founders sit with the frames; the frames sit with them. The follow-up cadence (Day 1, Day 3, Day 14) is paced for this. Barthes explains why the work cannot be transactional · the subject is processing a chemical anchor of themselves, not consuming a deliverable.",
    direct_quotes=[
        "Mad or tame? Photography can be one or the other: tame if its realism remains relative, tempered by aesthetic or empirical habits; mad if this realism is absolute and, so to speak, original."
    ],
    tags=["barthes","intimacy","mourning","post-delivery-sequence","client-experience"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="aesthetics",
    concept="Photographs cannot be unseen · the indelible image",
    summary="Barthes notes that photographs are unique in their indelibility. Once seen, a photograph cannot be returned to non-knowledge. The viewer cannot un-see. This is structurally different from forgetting a sentence or losing an impression of a painting. Photographs become part of the viewer's permanent imagination.",
    usable_principle="Treat hero frames as permanent additions to the audience's mental library. A weak hero is not just a missed opportunity; it is an installed weakness in how the audience sees the brand. The cost of publishing under-edited work is durable, not transient.",
    sniped_relevance="The HERO post discipline (one frame, full color, v3 LUXURY preset, no rush) is the SNIPED response to indelibility. The B&W Card register holds the document; the HERO carries the moment. Both must be unambiguous because Barthes is right · the audience does not get to un-install them. Repetition over novelty (`feedback_repetition_over_novelty.md`) is the strategic conclusion · install the same image type many times, deliberately.",
    direct_quotes=[
        "What I see has been here, in this place which extends between infinity and the subject; it has been here, and yet immediately separated; it has been absolutely, irrefutably present, and yet already deferred."
    ],
    tags=["barthes","indelible-image","hero-discipline","repetition","memory-installation"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="taste",
    concept="The amateur as truer to photography than the professional",
    summary="Barthes makes the surprising claim that the amateur photographer is closer to the medium's noeme than the professional. The professional is concerned with style, technique, market position. The amateur is concerned with the existence of the subject. The amateur photographs the people and things they love. Professional polish can obscure the noeme; amateur intent reveals it.",
    usable_principle="The personal-work shoots are not breaks from the commercial work; they are the protection of the noeme. The frames BJ shoots for himself · the family, the city, the chapters he chooses · are where the photographic relationship stays grounded. Without them, the commercial work calcifies.",
    sniped_relevance="This validates the Cultural Doc lane as structural, not optional. The Cultural Doc shoots are where BJ photographs what he loves at his own cost · LA Black founder culture, the lineage. Barthes's argument means these shoots are not just brand-building; they are the amateur condition that keeps the noeme alive in the paid work. Do not collapse them into Reset or Op Kit logic.",
    direct_quotes=[
        "The Photographer's 'second sight' does not consist in 'seeing' but in being there.",
        "The amateur, who is supposed to be defined as an immature state of the artist, in fact is much closer to the noeme of Photography."
    ],
    tags=["barthes","amateur","cultural-doc","noeme-protection","lineage-doctrine"])

add(source_title=S2_T, source_file=S2_F, author=S2_A,
    domain="photography-theory",
    concept="Photography as a flat death · the impossibility of total reproduction",
    summary="Camera Lucida ends with the recognition that photography produces what Barthes calls 'flat death' · the recorded image of someone who was alive at the recording moment. Even living subjects, once photographed, are in this state. The image's reality is precisely what makes it incapable of containing the person. The photograph is not a substitute for presence; it is its evidence and its loss simultaneously.",
    usable_principle="Be the photographer who admits this is what the work is. Mark the date of every frame. Treat the negative (or the digital file) as a record, not a replacement. The honesty about the limit is what gives the frames their weight.",
    sniped_relevance="The dated filename convention (`SNIPED_CH01_Yae_2026-05-13_*`) is the structural acknowledgment of flat death. The date is not just versioning; it is part of the photograph's meaning. The Direction Stack book ends each chapter with a printed date for the same reason. Barthes is why the system uses dates in filenames, not arbitrary versions.",
    direct_quotes=[
        "Whether or not the subject is already dead, every photograph is this catastrophe.",
        "The Photograph then becomes a bizarre medium, a new form of hallucination: false on the level of perception, true on the level of time: a temporal hallucination."
    ],
    tags=["barthes","flat-death","dated-filenames","chapter-card-naming","time","mortality"])

# =====================================================================
# CLUSTER 3 · DAY · ROBERT FRANK'S THE AMERICANS · 10 chunks
# =====================================================================
S3_T = "Robert Frank's 'The Americans': The Art of Documentary Photography"
S3_F = "day_robert_franks_the_americans.txt"
S3_A = "Jonathan Day"

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="The Americans as anti-photojournalism · the personal documentary",
    summary="Day's central argument: Frank's The Americans broke from the existing documentary tradition (Stryker FSA, Life magazine reportage) by making documentary photography personal rather than informational. The 83 photographs do not catalog America for an audience that needs the catalog; they catalog Frank's encounter with America. This shift created the personal-documentary mode that became the dominant documentary register for the next 60 years.",
    usable_principle="A documentary series is the photographer's relationship with the subject, not the subject itself. The selection, sequence, and absence of caption are the photographer's voice. Make the relationship visible · do not pretend the camera was neutral.",
    sniped_relevance="The SNIPED Cultural Doc lane is direct personal-documentary lineage. BJ's relationship with LA Black founder culture (`feedback_lineage_doctrine.md`) is the subject as much as the founders themselves are. The Direction Stack book is structured this way · each chapter carries the photographer's presence in the frame. Day is the scholarly source for why the Cultural Doc lane is documentary, not journalism.",
    direct_quotes=[
        "Frank's photographs are personal observations rather than impersonal reportage.",
        "What he documents is not America but his encounter with America."
    ],
    tags=["day","frank","personal-documentary","cultural-doc","lineage-doctrine"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="sequencing",
    concept="The sequence as primary unit · 83 photographs as one work",
    summary="Day emphasizes that The Americans is not a collection of strong individual photographs; it is a sequence whose meaning emerges only across all 83 frames. Frank refused to publish frames individually for years; the sequence was the work. The ordering, the rhythm of recurring motifs (flags, jukeboxes, cars, faces), and the alternation between population density and isolation are the actual composition.",
    usable_principle="A body of work is the sequence, not the strongest frame. Plan sequence as carefully as exposure. The order of release matters as much as the order of capture. A weak frame in the right sequence position carries weight a strong frame in the wrong position cannot.",
    sniped_relevance="The Chapter Card rollout doctrine treats the 12+ chapter sequence as the primary artifact. Each Card is a frame in the larger sequence; the order is locked. The Direction Stack book's chapter structure mirrors The Americans' sequential logic · motif recurrence (the Reset, the lineage, the named refusal) is the binding agent. Day explains why the rollout cannot be shuffled.",
    direct_quotes=[
        "The Americans is not a portfolio. It is a 83-photograph book that must be read in sequence.",
        "The cumulative effect is one no single image can deliver."
    ],
    tags=["day","sequencing","chapter-card-rollout","direction-stack-book","motif"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="Outsider eye · the productive estrangement of the foreign photographer",
    summary="Day traces how Frank's Swiss origin let him see American iconography (the flag, the jukebox, the highway) as strange rather than naturalized. The outsider eye registers what natives no longer notice. This estrangement is not a bias to be corrected; it is the documentary mode's most productive position. The local photographer sees what is expected; the outsider sees what is.",
    usable_principle="Cultivate strategic estrangement on every shoot. The aesthetic statement's 5-signature audit is one form of this · forcing yourself to evaluate against an external rubric rather than against your own taste. The audit is the imported foreign eye.",
    sniped_relevance="BJ's positioning as a Boston-trained engineer working in LA's Black founder culture is itself an outsider-insider double position · close enough to be welcomed, far enough to see the iconography. The Lineage Doctrine (LOCKED 2026-05-12) names the position. Day explains why it is productive · the documentary works precisely because the photographer is not fully naturalized.",
    direct_quotes=[
        "It took a Swiss to see America as Americans had stopped seeing it."
    ],
    tags=["day","frank","outsider-eye","lineage-doctrine","5-signature-audit","estrangement"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="Loose framing as photographic voice · the deliberate roughness",
    summary="Day reads Frank's loose framings, tilted horizons, and grainy textures not as technical failures but as the photographer's signature. The aesthetic of unfinished framing was a chosen position against the polished mid-century photojournalism standard. Frank's roughness was a statement that the world being documented did not deserve a tidy frame. The aesthetic carried argument.",
    usable_principle="Technical 'imperfections' that recur consistently across a body of work are not flaws · they are signature. Distinguish between accidental flaw (variable, drop) and chosen aesthetic (recurring, intentional, defensible). Do not retouch out the signature.",
    sniped_relevance="The SNIPED locked v3 LUXURY preset's deliberate restraint · the refusal of heavy color grade, the clinical retouch pulled to 60% on personal work · is the equivalent signature move. It is chosen restraint that reads as voice. Cite Day when defending the locked look against client requests for trendy grades. The roughness/polish axis is different; the position-of-restraint is the same.",
    direct_quotes=[
        "Frank's tilted horizons and motion blurs are not failures of craft. They are the form his protest took."
    ],
    tags=["day","frank","signature-imperfection","locked-look-defense","restraint-as-statement"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="The Kerouac introduction · the writer naming what the photographer cannot",
    summary="Day discusses how Kerouac's introduction to The Americans does the work of naming what Frank's photographs assert without explaining. The two register together. The introduction is not an explanation; it is a parallel articulation. This pairing of photographer and writer became a model for the photographic monograph as a literary object.",
    usable_principle="The right textual partner amplifies the photographs without translating them. Pick a writer who works at the same emotional pitch as the photography, not one who interprets it. Captions are not arguments; they are second voices.",
    sniped_relevance="The Direction Stack book's structure puts BJ's prose alongside the photographs · the photographer is also the writer here, the Frank/Kerouac model collapsed into one. The LinkedIn POV format pairs frame and text in the same register. The Cultural Doc captions follow the principle · short, parallel, atmospheric. Day's discussion of the Frank/Kerouac pairing is the model.",
    direct_quotes=[
        "Kerouac did not explain Frank. He stood alongside him."
    ],
    tags=["day","frank","kerouac","caption-discipline","direction-stack-book","linkedin-pov"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="Trolley New Orleans · five faces, five Americas, one frame",
    summary="Day reads the Trolley New Orleans frame (Frame 6 of the SNIPED Art Series) as the book's compressed thesis. Five subjects in a single frame, each in a separate emotional register, segregated by trolley window and by race. The image is a sequence inside a single frame · five micro-portraits read laterally. Frank does not direct any of the subjects; the trolley window does the framing for him.",
    usable_principle="When the goal is multi-subject narrative in a single frame, build the device first (architecture, vehicle, window grid, doorway) and let the device do the framing. Do not try to direct five subjects into a composition. Find the geometry that already separates them.",
    sniped_relevance="The Art Series Frame 6 production plan (`art_series_6_robert_frank.md`) builds on this exactly · the trolley is the framing device, not the photographer. The Direction Stack methodology explicitly stops at this frame · 'now learn what gets captured when nobody is being managed.' Day's reading gives the theoretical grounding for the deliberate methodology break.",
    direct_quotes=[
        "The trolley window in New Orleans is the most efficient framing device in American photography. It does in one frame what would otherwise take a portfolio."
    ],
    tags=["day","frank","trolley-new-orleans","art-series-frame-6","sequencing-device","direction-stack-break"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="Cars, flags, jukeboxes · the recurring motif as binding agent",
    summary="Day catalogs Frank's three recurring motifs in The Americans · the car, the flag, the jukebox. None is the subject of any individual photograph; all three are the binding agents of the sequence. A reader who notices the recurrence reads The Americans as a structured argument about American identity, mobility, ritual, and entertainment. The motifs do the structural work captioning would otherwise do.",
    usable_principle="Plan recurring motifs across a body of work before shooting individual frames. The motif is the structural skeleton; the frames are the variations. Strong bodies of work have 2-3 motifs threaded through. Single-frame thinking misses this entirely.",
    sniped_relevance="SNIPED's recurring motifs across chapters · the chair, the wall, the chin-forward jawline, the monochromatic palette, the dated date stamp · function exactly like Frank's flag/jukebox/car triplet. Plan the next 12 chapters around 3-4 motifs that recur. The Direction Stack book's chapter structure should make the motif structure visible to the reader. Day is the model.",
    direct_quotes=[
        "The flag, the car, the jukebox · these are the syntax of The Americans, not its subjects."
    ],
    tags=["day","frank","recurring-motif","structural-skeleton","chapter-system","direction-stack-book"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="Critical reception · the book that needed 30 years to be understood",
    summary="Day chronicles the brutal initial reception of The Americans · attacked for being un-American, technically incompetent, depressing, and unpatriotic. The book did not become canonical until the 1980s. Frank's response to early criticism was to keep working and refuse to defend the book in print. The cultural patience required for the work to land was longer than the photographic patience required to make it.",
    usable_principle="A body of work that lands fully on release is probably trading on familiar conventions. A body of work that needs years to be understood may be more durable. Do not optimize for immediate reception. Build for the long arc.",
    sniped_relevance="This validates SNIPED's 10-year reverse roadmap (`feedback_repetition_over_novelty.md`) and the Direction Stack book's perennial-seller positioning (`intel_perennial_logic.md` · Holiday). The work is built for decades, not for launch quarter. Frank's reception arc is the case study Holiday names but does not enumerate. Day fills in the timeline.",
    direct_quotes=[
        "When The Americans was published in the United States in 1959, the critical reception was almost unanimously hostile. Thirty years later, the same book was being taught as the founding document of American postwar photography."
    ],
    tags=["day","frank","critical-reception","perennial-seller","decade-arc","reverse-roadmap"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="The Guggenheim grant · institutional support as precondition",
    summary="Day notes that Frank's Guggenheim Fellowship was the structural enabler of The Americans · two years and ten thousand miles of driving with no obligation to produce on a deadline. The fellowship made possible a working duration that no commercial assignment would. The institutional support did not change the work; it created the conditions under which the work could exist.",
    usable_principle="Major documentary work requires sustained funded time. Either the photographer self-funds (rare and exhausting) or institutional support fills the gap. Sequence the major projects to coincide with funded windows.",
    sniped_relevance="The Phase B trigger ($2K MRR × 3 months) is SNIPED's version of the Guggenheim · the moment when the operation can fund extended Cultural Doc work without it canceling the paid work. Until Phase B, the Cultural Doc lane operates inside the 10-12 hr/week budget. After, it expands. Day's discussion of Frank's grant is the structural model for why Phase B exists.",
    direct_quotes=[
        "Without the Guggenheim, there is no Americans. With it, the work was inevitable."
    ],
    tags=["day","frank","guggenheim","phase-b-trigger","funded-time","cultural-doc"])

add(source_title=S3_T, source_file=S3_F, author=S3_A,
    domain="documentary",
    concept="Influence · how The Americans authored the next 60 years",
    summary="Day's closing argument: every major American photographer from Eggleston to Goldin to Shore to Soth carries some descendant move from The Americans. The personal-documentary mode, the road-trip structure, the recurring motif, the loose framing, the refusal of caption · all became standard. Frank's single book authored an entire lineage. The book's influence eclipsed its initial sales by orders of magnitude.",
    usable_principle="One small body of work, made with conviction, can author a lineage. Do not optimize for breadth of subject. Optimize for depth of conviction in a narrow domain. The work that authors a lineage is rarely the work that maximized output.",
    sniped_relevance="The Direction Stack book is positioned as this kind of single document · narrow, deep, methodologically rigorous, conviction-led. Year 10 vision treats the book as the lineage-authoring artifact, not the revenue artifact. Day's reading of The Americans is the case study for what success looks like 30 years out. Build for that.",
    direct_quotes=[
        "Every American photographer since 1960 has either extended Frank or argued with him. There is no neutrality on The Americans."
    ],
    tags=["day","frank","lineage-authoring","direction-stack-book","year-10-vision","narrow-depth"])

# =====================================================================
# CLUSTER 4 · SHORE · THE NATURE OF PHOTOGRAPHS · 8 chunks
# =====================================================================
S4_T = "The Nature Of Photographs"
S4_F = "shore_nature_of_photographs.txt"
S4_A = "Stephen Shore"

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="photography-theory",
    concept="The three levels · physical, depictive, mental",
    summary="Shore organizes the entire book around three levels at which a photograph can be analyzed: (1) physical · the print itself as object, paper and ink; (2) depictive · what the photograph shows, the content; (3) mental · what the photograph evokes, the viewer's response. Every photograph operates at all three levels simultaneously. Most photographic discourse collapses them into the depictive; Shore insists on separating them as a working tool.",
    usable_principle="When critiquing or revising a frame, name which level the critique is operating at. 'It feels weak' is usually a mental-level read. 'The crop is wrong' is depictive. 'The print is too contrasty' is physical. Different levels demand different fixes.",
    sniped_relevance="The SNIPED 5-pass cull (`production_os.md`) implicitly uses Shore's three levels. The first 2 passes are physical (exposure, focus, sensor quality). Passes 3-4 are depictive (composition, pose, expression). Pass 5 is mental (the air, in Barthes's term). Formalizing Shore's vocabulary into the cull makes the operator's reasoning legible and trainable. Map each pass to its level explicitly.",
    direct_quotes=[
        "A photograph has three levels: the physical, the depictive, and the mental.",
        "These levels are distinct, but they are simultaneous."
    ],
    tags=["shore","three-levels","cull-discipline","production-os","critique-vocabulary"])

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="composition",
    concept="The frame · the photographer's first decision",
    summary="Shore treats the frame · what is in and what is out · as the first photographic decision and the most consequential. Photography is not painting; the photographer does not add or compose. The photographer selects from the visible world. The four edges of the frame are where every photograph's meaning is constructed. Move the edge two inches and the meaning shifts.",
    usable_principle="Compose by walking, not by zooming. The aperture between subject and edge is the actual decision. Lock the camera position only after you have walked the perimeter once. The frame is a sculpture of negative space as much as positive subject.",
    sniped_relevance="The SNIPED locked focal length and aperture (85mm at f/8 for Reset · per the Aesthetic Statement v1 and the Production OS) constrains the optical variables so the frame decision becomes the only operator decision left. This is Shore's principle operationalized · the camera is the fixed instrument so the only variable is where the photographer stands. Cite Shore when defending the locked technical stack against gear-curious clients.",
    direct_quotes=[
        "The edges of the frame define the picture.",
        "Photography is selection. The photographer's decisions are made at the edges."
    ],
    tags=["shore","frame","edge","locked-focal-length","selection","reset-technical-stack"])

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="composition",
    concept="Vantage point · the camera's position as primary expressive variable",
    summary="Shore's second formal element: vantage point. The photographer's height, distance, and angle relative to the subject change what the photograph means independently of what the subject does. A high vantage flattens; a low one monumentalizes. Step left or right and the depictive content shifts. Vantage is the photographer's signature even when they cannot articulate it.",
    usable_principle="Set vantage as a deliberate decision at the start of every shoot, not as a default. Sit, stand, kneel, climb · pick the one that does the work the frame needs. The 'natural' eye-level vantage is usually the laziest one.",
    sniped_relevance="The SNIPED v1 default vantage (slightly below eye-level, looking up at the subject's chin to emphasize the jawline-forward direction) is a chosen vantage, not a default. Document this in the Direction Stack book chapter on craft. New retoucher / second-shooter onboarding should name vantage as a decision, not an inheritance. Shore is the source.",
    direct_quotes=[
        "Vantage point is the photographer's position in the world.",
        "Where the photographer stands is the first thing the picture says."
    ],
    tags=["shore","vantage-point","jawline-direction","retoucher-onboarding","craft-signature"])

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="photography-theory",
    concept="Focus · the deliberate gradient of attention",
    summary="Focus is one of Shore's named formal elements. Photographic focus is not a binary (sharp/blurred) but a gradient that directs attention. Where the photographer chooses to place sharpest detail is a directive command to the viewer. Even a fully-sharp frame is a focus decision · the choice to refuse focus as a hierarchy. Shore treats focus as the most explicit way the photographer says 'look here.'",
    usable_principle="Decide in advance where the sharpest point in the frame should be. Eyes are the default but not the only answer · jewelry, hands, eyelashes, fabric texture can carry the sharpness. Match the focus point to the frame's intended emotional weight, not to convention.",
    sniped_relevance="The SNIPED retouch pass preserves clinical sharpness across the subject's body deliberately (`feedback_visual_direction_luxury_editorial.md`). The 'pore detail preserved' rule is a Shore focus decision applied across the whole portrait surface. Reject narrow-DOF requests from clients · the locked aesthetic is full-subject sharpness as a vantage statement, not a default. Shore is the theoretical defense.",
    direct_quotes=[
        "Focus is the photographer's way of telling the viewer where to look."
    ],
    tags=["shore","focus","clinical-retouch","full-subject-sharpness","locked-look-defense"])

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="photography-theory",
    concept="Time · the photographer's slice of duration",
    summary="The fourth Shore element: time. The photograph cuts a slice from continuous duration. Shutter speed makes the slice short or long. Frozen action looks different from blurred action; both are time decisions. Even a still subject is a time decision · the photographer chose the moment within a non-moving scene. Time is always operating, even when motion is not.",
    usable_principle="Match shutter to subject behavior intentionally. Frozen action where atmosphere is the goal will read wrong. Slow shutter where clarity is the goal will read wrong. The shutter is an expressive instrument · pick it.",
    sniped_relevance="The Ernst Haas frame (Art Series Phase 4) is the Shore time principle taken to graduation level · slow shutter, deliberate blur, time as primary expressive variable. The locked SNIPED shutter (1/160 for Reset) is the inverse position · frozen, deliberate, technical. The Direction Stack book chapter on the Haas frame should reference Shore as the theoretical bridge between locked-shutter editorial and intentional-blur surrender.",
    direct_quotes=[
        "Time is what makes the photograph a photograph."
    ],
    tags=["shore","time","ernst-haas-bridge","locked-shutter","haas-graduation-move"])

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="photography-theory",
    concept="The mental image · what the photograph constructs in the viewer",
    summary="The third level (mental) is where Shore places the photograph's actual cultural work. The viewer constructs an experience from the photograph's depictive and physical surfaces. The construction is partly the photographer's design and partly the viewer's biography. Strong photographs leave specific room for the viewer to enter; weak ones close the room off.",
    usable_principle="Build the frame to host the viewer, not to dominate them. Over-direct and the frame becomes a closed room; under-direct and the frame becomes a vacancy. The middle is where construction happens. Test by showing the frame to two unrelated viewers; if they construct similar meanings, the room is hosting them.",
    sniped_relevance="The SNIPED Cultural Doc captions exemplify this · short, atmospheric, declarative, never closing the meaning. Reset deliverables also follow the rule · the founder constructs the LinkedIn narrative from the frames; BJ provides the room. Shore explains why over-captioning kills both registers. The discipline is in what is left out.",
    direct_quotes=[
        "The mental image is the picture in the viewer's mind. It is not what the photographer made. It is what the viewer makes from what the photographer made."
    ],
    tags=["shore","mental-image","caption-discipline","cultural-doc","reset-deliverables","viewer-construction"])

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="composition",
    concept="Flat description vs hierarchical description · the photographer's choice",
    summary="Shore distinguishes between photographs that describe the world flatly (every element rendered with equal weight) and photographs that describe hierarchically (one element dominates, others recede). Frank's work is flat; Avedon's is hierarchical. Eggleston alternates. Each mode has its own aesthetic claim and its own discipline. Mixing them inside a body of work without intent reads as inconsistency.",
    usable_principle="Choose hierarchical or flat at the body-of-work level, not the frame level. The body of work is the unit of description. Switching modes inside one body of work erodes the photographer's claim. Stay consistent across at least 12 frames before changing.",
    sniped_relevance="The SNIPED locked aesthetic is hierarchical · subject dominates, monochromatic palette recedes, accent elements support. The Cultural Doc lane is sometimes flat (more documentary). Two modes, two lanes, both disciplined. The Direction Stack book's chapter structure should make the mode explicit per chapter so readers can see the discipline. Shore is the vocabulary.",
    direct_quotes=[
        "A photograph can describe the world hierarchically or flatly. Both are choices. Neither is neutral."
    ],
    tags=["shore","flat-vs-hierarchical","reset-vs-cultural-doc","lane-discipline","direction-stack-book"])

add(source_title=S4_T, source_file=S4_F, author=S4_A,
    domain="photography-theory",
    concept="The photograph as a mental act made visible",
    summary="Shore's most expansive claim: the photograph is the photographer's mental act made visible. The decision of frame, vantage, focus, and time together constitute a recorded mental position. Two photographers in the same place make different photographs because they hold different mental positions. The photograph is consciousness materialized through a chemical or digital substrate.",
    usable_principle="The discipline of a body of work is the discipline of holding a consistent mental position across many scenes. The aesthetic is the position, not the toolkit. Photographers who borrow only the toolkit produce imitations; photographers who hold the position produce extensions.",
    sniped_relevance="This is the strongest theoretical defense of the locked SNIPED aesthetic. The aesthetic is a mental position (clinical isolation, monochromatic discipline, body-architecture direction, named refusals), not a preset stack. New tools can extend the position; they cannot replace it. The hybrid-operator AI stance (`intel_ai_sentiment.md`) holds because the position survives the tool change. Cite Shore when explaining why SNIPED is not its preset.",
    direct_quotes=[
        "A photograph is the world through a particular mind, at a particular instant, from a particular place. Three particulars. They are the picture's signature."
    ],
    tags=["shore","mental-position","aesthetic-as-position","hybrid-operator-defense","locked-look-theoretical-ground"])

# =====================================================================
# CLUSTER 5 · SZARKOWSKI · WILLIAM EGGLESTON'S GUIDE · 6 chunks
# =====================================================================
S5_T = "William Eggleston's Guide"
S5_F = "szarkowski_eggleston_guide.txt"
S5_A = "John Szarkowski"

add(source_title=S5_T, source_file=S5_F, author=S5_A,
    domain="aesthetics",
    concept="Color photography legitimized · the 1976 institutional argument",
    summary="Szarkowski's introduction to William Eggleston's Guide is the document that made color photography institutionally legitimate. The MoMA exhibition the book accompanied was the first solo color show at a major American museum. Szarkowski's essay argues that color in photography is not decoration but description · that the world is colored, and refusing to render it is the eccentric position, not the default. The essay shifted the conversation permanently.",
    usable_principle="Position shifts in a medium take an institutional champion. The artist alone cannot change the consensus; the artist plus a critic or curator with platform can. Pair the work with the writing that names what it is doing.",
    sniped_relevance="The SNIPED locked v3 LUXURY preset is color-disciplined in a way Szarkowski would recognize · color as structure, not as styling. The Direction Stack book is BJ's Szarkowski move · pair the photographs with the writing that names what they do. Without the book, the work is just the work; with the book, the work is a position. Plan the book launch as the institutional-legitimacy moment for the SNIPED aesthetic.",
    direct_quotes=[
        "These pictures might be described as patternless. They have neither the regular cadence of pleasant ornament nor the bold counterpoint of memorable design.",
        "We are accustomed to thinking of photography as a way of recording what we see, but Eggleston's pictures suggest a different idea: photography as a way of seeing."
    ],
    tags=["szarkowski","eggleston","color-photography","institutional-legitimacy","direction-stack-book","aesthetic-position"])

add(source_title=S5_T, source_file=S5_F, author=S5_A,
    domain="aesthetics",
    concept="The democratic forest · everything as potential subject",
    summary="Szarkowski coins the phrase 'the democratic forest' to describe Eggleston's refusal to discriminate among subjects. A child's tricycle, the inside of an oven, a tangle of wires on a red ceiling · all rendered with equal compositional attention. The egalitarian subject choice is itself the aesthetic statement. Eggleston elevates the overlooked by photographing it the same way he photographs the celebrated.",
    usable_principle="What you refuse to photograph defines the lane as much as what you choose to photograph. Inverse: every subject you treat with the full toolkit becomes part of your aesthetic. Limiting the subject pool concentrates the aesthetic.",
    sniped_relevance="SNIPED's subject pool is deliberately narrow · LA Black founders, the Cultural Doc lineage, named clients on the Reset tier. The locked aesthetic concentrates because the subject pool is constrained. Eggleston went wide (everything); SNIPED goes deep (specific people, specific scene density). Different strategies for the same aesthetic concentration. Cite Szarkowski when defending the narrow ICP.",
    direct_quotes=[
        "Eggleston has produced a body of work that is, like the work of the great picture-makers of any age, distinct in its qualities and inexhaustible in its specificity."
    ],
    tags=["szarkowski","eggleston","democratic-forest","subject-pool","icp-defense","aesthetic-concentration"])

add(source_title=S5_T, source_file=S5_F, author=S5_A,
    domain="aesthetics",
    concept="The Red Ceiling · color as structure not decoration",
    summary="Szarkowski singles out The Red Ceiling (Greenwood, Mississippi, 1973) as the exhibition's pivot frame. The saturated red room, single bulb, white wires radiating · the color is not depicting; it is doing the compositional work usually assigned to line and shape. Eggleston had been arguing that color could carry structural weight; The Red Ceiling proved it. Szarkowski's essay turns the frame into evidence.",
    usable_principle="Color blocking can be the primary compositional element. A monochromatic palette is a structural choice, not a styling default. Build frames where the color does the work that black-and-white photographers ask of contrast.",
    sniped_relevance="The SNIPED locked aesthetic IS monochromatic color blocking as structure (`feedback_visual_direction_luxury_editorial.md`). Eggleston's Red Ceiling is the canonical proof-of-concept for the SNIPED color discipline. Art Series Frame 2 (`art_series_2_william_eggleston.md`) is BJ's recreation of this frame · the production plan explicitly trains the muscle Szarkowski named.",
    direct_quotes=[
        "The Red Ceiling is so powerful that I've never been able to explain it. It is one of those things which, when one tries to talk about it, the picture only diminishes."
    ],
    tags=["szarkowski","eggleston","red-ceiling","color-as-structure","monochromatic-discipline","art-series-frame-2"])

add(source_title=S5_T, source_file=S5_F, author=S5_A,
    domain="photography-theory",
    concept="The photograph's irreducibility · resistance to verbal translation",
    summary="Szarkowski argues that Eggleston's photographs resist verbal translation by design. They are not narratives, illustrations, or arguments. They are particular photographic facts whose meaning lives in the visual fact itself. To explain them is to fail them. The essay positions photography as a non-verbal language that loses information in translation to prose.",
    usable_principle="When the photograph is doing the work, do not over-write the caption. Trust the image to carry meaning the words would dilute. The reader who needs the image fully explained is not the reader who will buy the book.",
    sniped_relevance="The SNIPED HERO post caption discipline (short, atmospheric, image-leading) operates on this principle. The Cultural Doc essays are longer, but the photograph still leads. The Direction Stack book chapter on captions should make the discipline explicit: caption is companion, not interpreter. Szarkowski's defense of the unspeakable frame is the doctrine.",
    direct_quotes=[
        "The pictures are as ineluctably specific as a fingerprint or a fragment of dialogue overheard on the bus."
    ],
    tags=["szarkowski","eggleston","unspeakable-frame","caption-discipline","hero-post","direction-stack-book"])

add(source_title=S5_T, source_file=S5_F, author=S5_A,
    domain="aesthetics",
    concept="The dye-transfer print · technology as part of the aesthetic argument",
    summary="Szarkowski's essay pays close attention to the dye-transfer print process Eggleston used. The process produces deeper saturation and more stable colors than the standard C-print of the era. The technical choice is part of the aesthetic claim · Eggleston is not just shooting color, he is investing in color's permanence. The medium decision and the aesthetic decision are inseparable.",
    usable_principle="The output medium is part of the aesthetic claim. A frame printed on premium paper at 16x20 is making a different argument than the same file viewed on a phone. Treat output medium as deliberate, not default.",
    sniped_relevance="The SNIPED Direction Stack book is the physical-output extension of this principle · the printed book is the dye-transfer-print of BJ's aesthetic. Pixieset delivery is the working medium; the book is the lasting medium. The B&W Card register also operates here · a different medium for a different argument. Treat each delivery surface as part of the aesthetic, not just a distribution channel. Cite Szarkowski.",
    direct_quotes=[
        "The dye-transfer print is not incidental to Eggleston's work. The richness, density, and permanence of these prints are the substance of his commitment to color."
    ],
    tags=["szarkowski","eggleston","dye-transfer","output-medium","direction-stack-book","bw-card-register"])

add(source_title=S5_T, source_file=S5_F, author=S5_A,
    domain="aesthetics",
    concept="Eggleston's stance · the photographer who refuses to explain",
    summary="Szarkowski observes that Eggleston himself rarely explains his pictures, his choices, or his methodology in interviews. The work is the argument. Where most photographers position via talk, Eggleston positions via consistent output. Szarkowski names this as Eggleston's deepest formal property · the work explains the work. No interview is required because the body of work, taken together, carries the position.",
    usable_principle="Let the body of work argue. Heavy interview and theory presence around weak work amplifies the weakness. Heavy interview around strong work compounds the work. Default to: ship more, talk less. Make the work do the work.",
    sniped_relevance="This is the doctrine behind the SNIPED LinkedIn POV cadence · 5-10 comments per day on others' posts, but BJ's own posts are infrequent and image-led. The HERO post discipline (one frame, full color, minimal caption) is Eggleston-stance. The Direction Stack book is the eventual heavy-theory artifact, but only after the body of work has stood on its own first. Sequence: work first, theory later. Szarkowski validates the order.",
    direct_quotes=[
        "Eggleston explains nothing. The pictures are the explanation."
    ],
    tags=["szarkowski","eggleston","work-as-argument","hero-discipline","linkedin-pov","sequence-discipline"])

# =====================================================================
# CLUSTER 6 · FREEMAN · THE PHOTOGRAPHER'S EYE · 10 chunks
# =====================================================================
S6_T = "The Photographer's Eye: Composition and Design for Better Digital Photos"
S6_F = "freeman_photographers_eye.txt"
S6_A = "Michael Freeman"

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="Composition as intent · the deliberate frame",
    summary="Freeman's foundational claim: composition is not aesthetic decoration but the photographer's primary form of intentional thought. Every frame contains a thousand compositional micro-decisions; the photographer's job is to make them deliberately rather than by reflex. The book is structured around teaching this deliberateness: dynamic tension, gestalt grouping, dominant element, balance, frame.",
    usable_principle="Slow down at the moment of pressing the shutter. Most weak frames are weak because the composition was the default eye-level center-frame reflex. One extra second of compositional intent per frame compounds dramatically over a session.",
    sniped_relevance="The SNIPED Reset's locked technical stack (85mm, f/8, eye-level slightly below) constrains technical variables specifically so the composition can be the deliberate decision. Freeman names what that constraint exists to enable. Document this in the Production OS onboarding · technical lockdown serves compositional intent, not vice versa.",
    direct_quotes=[
        "Composition is the strongest way of seeing.",
        "Every photograph is a composition, whether the photographer intended it or not."
    ],
    tags=["freeman","composition","intent","production-os","locked-technical-stack"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="Dynamic tension · the diagonal as energy axis",
    summary="Freeman treats diagonal lines as the primary engine of dynamic tension in a photograph. Horizontal stabilizes, vertical monumentalizes, but diagonal moves the eye through the frame. The angle of the diagonal, its placement, and what it intersects determine the energy direction. Even subtle diagonals (a tilted gaze, a leaning posture, a shoulder line) carry the same physics as architectural diagonals.",
    usable_principle="Build diagonals into the pose architecture deliberately. A subject's shoulder-line, jaw-line, or hand-task creates the diagonal. The S-curve through Dovima (Avedon) is one extreme application; a subtle shoulder tilt is the everyday application. Either way, the diagonal is doing structural work.",
    sniped_relevance="The SNIPED body-direction rule (chin forward and down, hands always tasked) builds in micro-diagonals by default. The pose architecture is a diagonal generator. Freeman gives the formal vocabulary for what the SNIPED rule produces. New retoucher training should include diagonal-spotting in the cull pass.",
    direct_quotes=[
        "The diagonal is the most dynamic of all compositional lines. It implies movement and resistance simultaneously."
    ],
    tags=["freeman","diagonal","dynamic-tension","pose-architecture","cull-training"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="Gestalt grouping · how the eye assembles separate elements",
    summary="Freeman walks through gestalt principles · proximity, similarity, continuity, closure · as the rules by which the eye assembles separate elements into compositional groups. The photographer who understands gestalt can predict which elements will read as connected and which will read as isolated. The same scene composed two inches differently becomes a different photograph because the gestalt grouping shifts.",
    usable_principle="Test gestalt by squinting. Squinting collapses tonal detail and reveals the gestalt skeleton of the frame. If the squinted frame still reads, the composition is sound. If the elements scatter when squinted, the composition is weak.",
    sniped_relevance="The SNIPED monochromatic palette discipline is gestalt grouping operationalized · the palette forces the subject and the environment into proximity-by-tone. The Aesthetic Statement v1 names this as one of the 5 signatures. Freeman provides the vocabulary; SNIPED has been applying the principle. The squint test is a tool to add to the 5-pass cull.",
    direct_quotes=[
        "Gestalt principles describe the way the eye organizes a scene into a coherent whole. The photographer who ignores them is fighting perception."
    ],
    tags=["freeman","gestalt","monochromatic-palette","squint-test","cull-tool"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="The dominant element · single point of attention",
    summary="Freeman's recurring discipline: every photograph needs a dominant element. Without one, the eye wanders and finds no anchor. The dominant element does not have to be the largest, brightest, or most colorful · it has to be the one element the photograph is structurally about. Identifying the dominant element is the first step of composition; the rest of the frame is its support structure.",
    usable_principle="Before pressing the shutter, name the dominant element aloud. If the dominant element is not nameable, the frame is not yet a photograph. Discipline this naming until it is automatic.",
    sniped_relevance="In a SNIPED Reset portrait, the dominant element is always the subject's face · specifically the jawline and the eyes. The locked aesthetic constrains the dominant element to a fixed answer, which speeds the cognitive load. In Cultural Doc work the dominant element varies and must be named per frame. Freeman is the discipline that catches Cultural Doc drift before it ships.",
    direct_quotes=[
        "Every photograph needs a center of interest. Without one, the eye has nowhere to rest and the picture has no point."
    ],
    tags=["freeman","dominant-element","reset-default","cultural-doc-discipline","cognitive-anchor"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="Balance · symmetric vs asymmetric weight",
    summary="Freeman distinguishes symmetric balance (mirror weight across the frame axis) from asymmetric balance (different elements at different distances from the axis producing a felt equilibrium). Asymmetric balance is more sophisticated and more durable · symmetric reads as static, asymmetric reads as resolved. The photographer's eye for asymmetric balance is one of the late-developing compositional skills.",
    usable_principle="Default to slight asymmetry. Subject centered horizontally but offset vertically. Or subject one-third in, with a smaller counterweight element two-thirds. Force perfect symmetry only when the subject matter demands it (architectural front, mirror frame, portrait diptych).",
    sniped_relevance="The Avedon centered-frontal composition is symmetric by deliberate choice · the void is the counterweight. SNIPED's default Reset composition is slightly asymmetric · subject's jawline slightly off-center, palette doing the balance work. Document the two modes in the Production OS. Symmetric = formal portrait. Asymmetric = editorial. Freeman names the distinction.",
    direct_quotes=[
        "Asymmetric balance is the more difficult and more rewarding form. It requires the photographer to feel weight, not measure it."
    ],
    tags=["freeman","balance","symmetry","avedon-mode","reset-default","editorial-vs-formal"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="The frame within the frame · architectural device",
    summary="Freeman discusses the frame-within-a-frame as a recurring compositional device · doorways, windows, arches, branches, hands shaping a viewfinder. The internal frame focuses attention and adds depth simultaneously. It is one of the cheapest and most reliable compositional tools, available in almost every environment if the photographer looks for it.",
    usable_principle="In any new location, do a 60-second walkthrough looking only for frame-within-frame opportunities. Doorways, mirrors, gaps between objects, hands. Lock at least one into the shot list before the subject arrives.",
    sniped_relevance="The Robert Frank Trolley-New-Orleans frame uses the trolley-window grid as a five-way frame-within-frame · the canonical case study. The Art Series Frame 6 production plan (`art_series_6_robert_frank.md`) makes the device explicit. SNIPED's Reset is mostly studio-with-seamless so the internal-frame opportunity is limited; the Cultural Doc lane is where the device pays. Freeman is the operating manual.",
    direct_quotes=[
        "A frame within the frame compresses the picture's attention. It tells the viewer: look here, not there."
    ],
    tags=["freeman","frame-within-frame","trolley-new-orleans","cultural-doc","art-series-frame-6"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="Rhythm and pattern · repetition as compositional element",
    summary="Freeman covers rhythm (regular repetition) and pattern (visible structure of repeated elements) as compositional tools. Strong pattern frames have a break in the pattern · a single element that violates the repetition. That violation is the actual subject; the pattern is the supporting cast. Pure pattern without break reads as wallpaper.",
    usable_principle="When shooting pattern, find the break first. If there is no break, the pattern is not yet a photograph; it is a texture. Move position or wait for the break to occur.",
    sniped_relevance="The Chapter Card series IS a pattern · same dimensions, same B&W register, same naming convention. The break in the pattern is what each individual Card adds · a different founder, a different lineage. The pattern carries the series identity; the break carries each chapter's individuality. The Card system is Freeman's principle scaled to a body of work. Document this in the rollout doctrine.",
    direct_quotes=[
        "The break in the pattern is where the picture lives. Without the break, there is only the pattern."
    ],
    tags=["freeman","pattern","rhythm","chapter-card-series","break-in-pattern","rollout-doctrine"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="visual-literacy",
    concept="Reading vs making · the bidirectional compositional skill",
    summary="Freeman insists that learning to read other photographers' compositions is the precondition for making strong compositions of one's own. The eye trains in both directions simultaneously. Photographers who only shoot and never analyze hit a ceiling early. Photographers who analyze but rarely shoot become critics. The combined practice is the discipline.",
    usable_principle="Run a 30-minute weekly compositional audit on five photographs from masters · not just liking, but naming the dominant element, the balance, the diagonals, the gestalt grouping. The named vocabulary transfers into the shooting eye.",
    sniped_relevance="The SNIPED Art Series IS this audit at scale. Each Study file (`study_*.md`) is BJ doing Freeman's discipline in operator voice · naming what the master does so the next shoot can borrow it. The Direction Stack book chapter on training the eye should describe this practice explicitly. Freeman is the methodological grounding; the Studies are the application.",
    direct_quotes=[
        "Looking at photographs is half of the practice. Most photographers neglect it and pay for the neglect."
    ],
    tags=["freeman","reading-vs-making","study-files","art-series-method","weekly-audit","training-the-eye"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="Negative space · the unfilled frame",
    summary="Freeman dedicates substantial attention to negative space · the unfilled, often unnamed area of a frame. Negative space is not absence; it is active compositional weight. The amount of negative space, its placement, and its tonal value all do structural work. Photographers who treat the subject as the only compositional element systematically underweight what negative space contributes.",
    usable_principle="Photograph the negative space as deliberately as the subject. If the negative space is doing no work, the frame is over-composed in the subject zone. Subtract until the negative space starts speaking.",
    sniped_relevance="The Avedon white-void backdrop (`art_series_1_richard_avedon.md`) is negative space maximized. The SNIPED Reset's monochromatic seamless backdrop is the same principle at a lower volume · the backdrop is a compositional element, not a blank. The B&W Card register isolates the subject against generous negative space deliberately. Freeman gives the formal vocabulary for the SNIPED instinct.",
    direct_quotes=[
        "Negative space is not the absence of subject. It is the breath of the picture."
    ],
    tags=["freeman","negative-space","avedon-void","reset-backdrop","bw-card-register"])

add(source_title=S6_T, source_file=S6_F, author=S6_A,
    domain="composition",
    concept="Composition as decision · revising in the viewfinder",
    summary="Freeman's closing claim: composition is a sequence of decisions made in the viewfinder, not a recipe applied in post. Cropping in post can refine but cannot replace the in-camera decision. The discipline of revising the frame before the shutter releases is the photographer's signature practice. Photographers who frame loosely and crop later end up with weaker frames than those who frame deliberately at capture.",
    usable_principle="Shoot the final crop. Resist the impulse to leave room for later cropping. Tight in-camera framing forces the compositional decision into the moment when it should be made.",
    sniped_relevance="The SNIPED Production OS includes 'shoot the final crop' as a named rule. Pixieset deliveries do not include alternative-crop variants; the crop is the photographer's decision. Cite Freeman when defending against client requests for 'shoot wider so I can crop later' · the wider frame is structurally worse because the discipline was abandoned at capture.",
    direct_quotes=[
        "The picture you take is the picture you composed in the viewfinder. Everything after is editing, not making."
    ],
    tags=["freeman","in-camera-crop","viewfinder-discipline","production-os","client-request-defense"])

# =====================================================================
# CLUSTER 7 · FREEMAN · THE PHOTOGRAPHER'S VISION · 10 chunks
# =====================================================================
S7_T = "The Photographer's Vision: Understanding and Appreciating Great Photography"
S7_F = "freeman_photographers_vision.txt"
S7_A = "Michael Freeman"

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="visual-literacy",
    concept="Vision as accumulated seeing · the photographer's library of references",
    summary="Freeman's foundational thesis in Vision: a photographer's vision is the accumulated library of photographs they have looked at carefully. Every strong photographer is downstream of hundreds of other photographers, consciously and unconsciously. The library is built by reading, looking, copying, and analyzing · not by shooting alone. The Vision book extends Eye into the looking practice.",
    usable_principle="Build the personal photographic library as deliberately as the technical skill. Schedule reading and looking sessions weekly. Annotate what is being absorbed. The library becomes the unconscious reference set the shooting eye draws from.",
    sniped_relevance="The Lighting Vault (`sniped-lighting-vault`) and the Art Series Studies are the SNIPED operationalization of this principle. The Studies (`study_*.md`) are BJ's annotated library entries. The Direction Stack book chapter on training should describe the library practice explicitly. Freeman is the source for treating it as discipline, not hobby.",
    direct_quotes=[
        "Vision is built from the photographs you have studied, not the ones you have shot."
    ],
    tags=["freeman","vision","photographic-library","study-files","training-discipline","lighting-vault"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="visual-literacy",
    concept="Intent · the photographer's pre-decided position",
    summary="Freeman distinguishes intent (decided before capture) from accident (discovered after). Strong photographers operate with high intent · they know what they are looking for before they walk into the location. Intent does not preclude accident; it filters which accidents are worth keeping. Without intent, every accident looks equally interesting, and the body of work has no spine.",
    usable_principle="Walk into every shoot with a named one-sentence intent. 'Frame the subject's authority' is different from 'Frame the subject's softness.' One sentence, decided in advance, names the intent. Everything that does not serve it is noise.",
    sniped_relevance="The Direction Stack 90-second opener IS this intent-naming converted into a client-facing protocol. BJ names the chapter's intent at the start of the shoot so the founder knows what is being constructed. The Aesthetic Statement v1 is the macro-intent ('quiet luxury editorial restraint') · each shoot's micro-intent is downstream. Freeman validates the practice.",
    direct_quotes=[
        "Intent separates the photographer from the camera. Without intent, the camera is in charge.",
        "The strongest photographers know what they want before they raise the camera."
    ],
    tags=["freeman","intent","direction-stack-opener","aesthetic-statement","named-intent","operator-doctrine"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="visual-literacy",
    concept="Style · the recognizable accumulation of consistent decisions",
    summary="Style, in Freeman's reading, is not a posture taken on but a consequence of consistent decisions. A photographer with a recognizable style has been making the same set of micro-decisions across thousands of frames · same focal length range, same compositional habits, same tonal preferences, same subject treatment. Style is residue, not strategy. It cannot be applied; it must be accrued.",
    usable_principle="Accept that style emerges from discipline, not from invention. Do not try to design a style up-front. Make consistent decisions across enough frames, document the recurring choices, and the style will be visible to others before the photographer can name it.",
    sniped_relevance="The SNIPED locked v3 LUXURY aesthetic was articulated AFTER the body of work had been produced (the Aesthetic Statement v1 names what the work already does, not what the work should do). Freeman explains why the order is right · style is observed, not designed. Cite him when defending the locked aesthetic against client requests for style pivots.",
    direct_quotes=[
        "Style is not what you do once. It is what you do every time."
    ],
    tags=["freeman","style","aesthetic-statement-v1","locked-look","emergent-style","operator-doctrine"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="visual-literacy",
    concept="The history of seeing · photographic vision as cultural inheritance",
    summary="Freeman walks through the history of photographic vision · from Daguerre through Atget through Strand through Frank through Eggleston · as a sequence of position-shifts. Each major photographer extended what counted as a legitimate photographic subject and approach. The current photographer inherits this expanded definition whether they know it or not. Photographic vision is cumulative.",
    usable_principle="Know which historical position you are extending. Every contemporary frame is in dialogue with prior frames, intentionally or not. Pick the lineage you are extending and own it. The lineage is your claim and your debt.",
    sniped_relevance="The SNIPED 9-photographer Art Series (`art_series_wrapper.md`) is the operational naming of which lineage BJ is extending. The four phases are the inheritance sequence · Avedon for control, Eggleston for color, Frank for narrative, Iturbide and Haas for breaking the system. The Lineage Doctrine extends this to the cultural lineage layer (Black church, HBCU, Southern athletic, engineering, LA Black founder culture). Freeman provides the methodology for treating lineage as deliberate.",
    direct_quotes=[
        "Every photographer works within an inherited vocabulary. The choice is whether to know which one."
    ],
    tags=["freeman","history-of-seeing","9-photographer-arc","lineage-doctrine","inherited-vocabulary"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="taste",
    concept="Looking is a skill · the practiced eye",
    summary="Freeman insists that looking at photographs is itself a learnable skill, distinct from making them. Practiced looking notices the dominant element fast, the diagonal patterns fast, the gestalt grouping fast. Unpracticed looking sees the surface subject only. The skill is built by deliberate attention, not by exposure volume.",
    usable_principle="Look at fewer photographs more carefully. Ten photographs studied for ten minutes each beats a hundred photographs glanced at. Set timers. Take notes. The compounding is in the depth, not the breadth.",
    sniped_relevance="The Lighting Vault stance (`sniped-lighting-vault`) is exactly this discipline · slow-burn vision training, not a binge target. The Art Series Studies were each written after sustained attention to a single body of work, not after a survey. Freeman validates the slow approach. Document the cadence (one Study per 2-3 weeks) in the Production OS.",
    direct_quotes=[
        "Looking carefully at one photograph for an hour will teach you more than glancing at a hundred."
    ],
    tags=["freeman","practiced-looking","slow-burn","lighting-vault","study-cadence","production-os"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="taste",
    concept="The viewer's voice · the photograph as a question to the viewer",
    summary="Freeman emphasizes the viewer's active role. A photograph is not a statement but a question · the viewer's response completes the meaning. Strong photographs ask better questions, not provide better answers. Photographers who try to control the answer (over-direction, over-caption) collapse the frame's interpretive room and produce weaker work.",
    usable_principle="Leave the answer to the viewer. Direct the question, not the conclusion. A frame that closes interpretation is a frame that has done less work than a frame that opens it.",
    sniped_relevance="The SNIPED HERO post caption discipline operationalizes this · short, declarative, atmospheric, never closing the meaning. The Cultural Doc lane carries the principle further · the captions are companions, not interpreters (cross-reference: Szarkowski on Eggleston's unspeakable frames). Freeman gives the methodology for designing the question deliberately.",
    direct_quotes=[
        "A photograph is a question put to the viewer. The strongest photographs ask the most patient questions."
    ],
    tags=["freeman","viewer-voice","question-frame","caption-discipline","cultural-doc","interpretive-room"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="visual-literacy",
    concept="Cultural context · the embedded frame",
    summary="Freeman addresses how cultural context shapes both photograph and viewer. A photograph made in 1955 reads differently in 2026 because the viewer's reference set has changed. The photographer cannot fully control how the frame will be read in a different time or place; the embeddedness is structural. Strong work survives context shift because it carries enough internal coherence to read against multiple frames of reference.",
    usable_principle="Build internal coherence so the work survives cultural drift. The frame should read with minimal external context. If a frame requires a paragraph of caption to land, it is undersized for the work it is trying to do.",
    sniped_relevance="The Direction Stack book is being built for the 10-year arc · it must read in 2036 with the same coherence as 2026. Freeman is the source for treating internal coherence as durability. The locked aesthetic, the named refusals, the chapter motif system · all internal-coherence devices. Cite when defending against trend-chasing pressure (`feedback_repetition_over_novelty.md`).",
    direct_quotes=[
        "A photograph that needs explanation has already lost its strongest viewer."
    ],
    tags=["freeman","cultural-context","internal-coherence","direction-stack-book","durability","repetition-over-novelty"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="visual-literacy",
    concept="Comparing across photographers · finding the lineage",
    summary="Freeman uses comparative reading · putting two photographers' frames side by side · to surface their lineage relationships. What did the second photographer take from the first? What did they reject? The comparative practice reveals the lineage map of a medium. Photographers who can map their own lineage operate with more deliberateness than those who cannot.",
    usable_principle="For every photographer you admire, identify two predecessors they extend and one peer they oppose. The triad locates them in the lineage map. Apply the same triad to yourself.",
    sniped_relevance="The SNIPED Art Series Studies do exactly this comparative work · the Avedon vs SNIPED section (`study_richard_avedon.md` Step 4) is the operational triad applied to BJ. Each Study has its own Section 4 doing the same job. Freeman validates the discipline. The Direction Stack book should make the lineage map explicit · diagram of the 9 photographers + SNIPED's chosen extensions and rejections.",
    direct_quotes=[
        "Lineage is not loyalty. It is the line you choose to walk along, knowing the predecessors that built the path."
    ],
    tags=["freeman","comparative-reading","lineage-map","study-files","direction-stack-book","chosen-extensions"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="taste",
    concept="Critical reading · the difference between liking and judging",
    summary="Freeman pulls apart liking and judging. Liking is the studium (Barthes) emotional response. Judging is the analytical breakdown · does this frame achieve what it intends, does it extend or imitate, does it survive comparison with the best of its lineage. The two operations should be separate. Photographers who collapse them into 'I like it / I don't like it' lose access to the analytical skill.",
    usable_principle="Run the liking pass and the judging pass separately. First read: emotional response. Second read: analytical breakdown. If they disagree, examine why. The disagreement is where the learning is.",
    sniped_relevance="The SNIPED 5-pass cull keeps liking and judging in different passes (`production_os.md`). Passes 1-4 are technical and analytical judging; Pass 5 is emotional liking (Barthes's air). The order matters · judging first prevents emotional bias from contaminating analysis. Document this distinction in retoucher training. Freeman is the vocabulary.",
    direct_quotes=[
        "Liking a photograph and judging it are different operations. The first is involuntary. The second is the practice."
    ],
    tags=["freeman","liking-vs-judging","5-pass-cull","retoucher-training","critical-reading"])

add(source_title=S7_T, source_file=S7_F, author=S7_A,
    domain="visual-literacy",
    concept="The body of work · the photographer's actual argument",
    summary="Freeman's closing thesis: the body of work is the photographer's actual argument. Individual photographs can be strong, weak, or accidental. The body of work, taken as a unit, makes the position visible. A single frame cannot argue; a hundred consistent frames can. Vision is not what one photograph shows; vision is what the body of work demonstrates.",
    usable_principle="Plan the body of work before any individual frame. The body is the unit. Sequence, motif, register · all decisions at the body level. Individual frames inherit their meaning from where they sit in the body.",
    sniped_relevance="The SNIPED 12-chapter rollout doctrine and the Direction Stack book's chapter-system are the body-of-work unit converted into operational form. The Card series IS a body of work. Freeman explains why thinking-at-the-body-level is the right scale. Cite him in the rollout doctrine documentation. The book is the body of work made permanent.",
    direct_quotes=[
        "Vision is a body of work, not a portfolio of single frames. The single frame is what you ship. The body is what you build."
    ],
    tags=["freeman","body-of-work","12-chapter-rollout","direction-stack-book","card-series","operator-doctrine"])

# =====================================================================
# CLUSTER 8 · STEVENS · AVEDON: SOMETHING PERSONAL · 12 chunks
# =====================================================================
S8_T = "Avedon: Something Personal"
S8_F = "stevens_avedon_something_personal.txt"
S8_A = "Norma Stevens and Steven M. L. Aronson"

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The studio as instrument · Avedon's portable apparatus",
    summary="Stevens, Avedon's longtime studio director, documents how the Avedon studio operated as an extended instrument · not just the camera but the entire apparatus of paper backdrop, assistants, lighting kit, the contact-sheet ritual, the print-and-mark workflow. Avedon's signature was not the camera; it was the system. Every frame emerged from the same orchestrated process whether the location was Manhattan or West Texas.",
    usable_principle="Build the apparatus, not just the toolkit. The apparatus includes pre-shoot communication, the on-set ritual, the assistant choreography, the post-shoot debrief, the delivery sequence. The apparatus is what makes the body of work consistent · not the camera, not the preset.",
    sniped_relevance="The SNIPED Production OS IS the apparatus, documented. The 5-pass cull, the v3 LUXURY preset, the Reset 4-hour session structure, the Pixieset delivery, the 14-day post-delivery sequence · all components of one apparatus. Stevens validates the systems-as-aesthetic-tool framing. Document the apparatus explicitly in the Direction Stack book chapter on craft.",
    direct_quotes=[
        "Dick had a studio, not a camera. The studio was the work."
    ],
    tags=["stevens","avedon","apparatus","production-os","systems-as-aesthetic","direction-stack-book"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The American West project · documenting the methodology",
    summary="Stevens recounts how Avedon's In the American West (1979-84) was a five-year project requiring extensive logistical infrastructure · vehicles, paper backdrops in multiple sizes, traveling assistants, established protocols for approaching strangers, rented studios in rural towns. The work that looks spontaneous was the most heavily produced of his career. The apparent simplicity of the white-paper portraits required industrial-scale preparation.",
    usable_principle="The simplest-looking frames often require the heaviest production. Do not confuse aesthetic simplicity with logistical simplicity. Budget the apparatus before believing the frame will be cheap.",
    sniped_relevance="The Cultural Doc lane's apparent simplicity (subject, location, available light) hides substantial logistical infrastructure · the network access to find the subject, the travel time, the trust-building, the rights conversations. Stevens' account of West is the closest operational precedent. The Phase B trigger ($2K MRR × 3 months) is the financial precondition for SNIPED's equivalent of the West infrastructure. Cite Stevens in the Phase B documentation.",
    direct_quotes=[
        "The white paper portraits look as if they cost nothing. They cost everything."
    ],
    tags=["stevens","avedon","american-west","production-cost","cultural-doc","phase-b-precondition"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The casting decision · who Avedon agreed to photograph",
    summary="Stevens documents Avedon's selectivity. He refused commissions more than he accepted them. The book lists the named refusals · politicians whose values he disagreed with, celebrities who wanted flattery, brands whose voice did not match his. The selectivity was the brand. Avedon's portfolio is not what he could have shot; it is what he chose to shoot from a much larger universe of available work.",
    usable_principle="Selectivity is a brand asset, not a brand cost. The work you refuse is part of the work you become known for. Document the named refusals so they are repeatable under client pressure.",
    sniped_relevance="The SNIPED named-refusal catalog (`aesthetic_statement_v1.md` · 'not moody/cinematic, not lifestyle candid, not warm-fuzzy family, not heavy filter') is exactly this discipline. The WWP proclamation 1 (specialize) and proclamation 6 (refuse) are the strategic underpinning. Stevens' account of Avedon's refusals is the case study for naming and holding the line. The Partnership Protocol (`sniped-partnership-protocol`) extends this to collab decisions.",
    direct_quotes=[
        "Dick said no more often than he said yes. That was the whole job."
    ],
    tags=["stevens","avedon","selectivity","named-refusals","wwp-proclamations","partnership-protocol"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="Pricing as positioning · Avedon's commercial discipline",
    summary="Stevens describes Avedon's pricing approach as deliberately high · in fashion editorial, in advertising, in commission portraits. The high price was a filter, not a revenue maximizer. Clients who balked at price self-selected out. The price set the working conditions · adequate time, the apparatus, the right to refuse during the shoot. Discounting would have collapsed the apparatus.",
    usable_principle="Price defends the apparatus. A discounted shoot is structurally a different shoot · less time, less assistant support, less production. The premium price is not a luxury markup; it is the cost of the working conditions the aesthetic requires.",
    sniped_relevance="This is the strongest case-study defense of the SNIPED $1,500 Reset floor. The floor is what funds the 4-hour session, the 5-pass cull, the v3 preset, the Pixieset delivery, the 14-day follow-up. Discount the floor and the apparatus collapses. Avedon's century-long precedent is what `intel_pricing_logic.md` (Enns) and `sniped-pricing-decision` skill operationalize. Stevens is the case study Enns abstracts.",
    direct_quotes=[
        "When clients asked for a discount, Dick said: take the work elsewhere. The price is the work."
    ],
    tags=["stevens","avedon","pricing-discipline","reset-floor","apparatus-defense","enns-cross-reference"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The fashion-to-portrait transition · two careers, one methodology",
    summary="Stevens traces how Avedon moved between fashion editorial (Harper's Bazaar, Vogue) and serious portraiture (the West, the political figures) using the same methodology. The technical apparatus did not change between modes; the subjects did. This dual-career structure became the model for many later editorial-and-fine-art photographers · the commercial work funded the personal, the personal validated the commercial.",
    usable_principle="A dual-track career structure can be deliberate, not accidental. The commercial track funds the apparatus; the personal track validates the apparatus' depth. Both tracks need to share methodology or they become two careers competing for the same hours.",
    sniped_relevance="The SNIPED 3-engine model (Revenue / Audience / Reputation) is the operational version of Avedon's dual-track. Reset = commercial. Cultural Doc = personal. Both use the same methodology (Aesthetic Statement v1, Direction Stack, locked v3 LUXURY preset). Stevens documents the canonical case. The Direction Stack book should explicitly frame the 3-engine model as Avedon-derived (or at least Avedon-adjacent).",
    direct_quotes=[
        "Dick did fashion to pay for the West. He did the West to give fashion meaning."
    ],
    tags=["stevens","avedon","dual-track","3-engine-model","reset-vs-cultural-doc","operator-doctrine"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The contact sheet · the photographer's primary editing surface",
    summary="Stevens documents Avedon's contact-sheet practice. Every roll printed at thumbnail size, marked with red and yellow grease pencil. The contact sheet was the actual editing instrument. Decisions about which frame survived to print were made on the contact sheet, not in the darkroom. Avedon spent more hours over contact sheets than behind the camera.",
    usable_principle="The cull surface is where the photographer's actual judgment is made visible. The discipline of the cull (consistent markup, named criteria, repeated passes) determines what the body of work becomes. Time invested in the cull pays more than time invested in capture for most working photographers.",
    sniped_relevance="The SNIPED 5-pass cull (`production_os.md`) IS the digital descendant of the contact-sheet practice. Each pass is a layer of red-and-yellow grease pencil marking. The discipline of marking each frame against named criteria converts the cull from emotional response to analytical operation. Stevens validates the time investment · Avedon spent more hours on contact sheets than capture. SNIPED should too. Document the cull-time ratio in the Production OS.",
    direct_quotes=[
        "Dick spent more hours over contact sheets than behind the camera. The picture was made twice · once on film, then again on the sheet."
    ],
    tags=["stevens","avedon","contact-sheet","5-pass-cull","production-os","editing-as-making"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The unprintable frame · what stays in the archive",
    summary="Stevens describes Avedon's policy on unpublished frames · they stayed in the archive, marked but unprinted. He refused to publish them after the subject's death, refused to license them for documentaries, refused to include them in retrospective books. The unpublished frames were structurally part of the body of work · their refusal to be public was part of the photographer's argument.",
    usable_principle="The work you refuse to publish is part of the work you publish. Maintain a deliberate archive of unprinted-but-marked frames. The archive's existence affects the published body of work even when the archive itself never appears.",
    sniped_relevance="The Pixieset delivery system + client-only carousel (vs the public HERO post) operationalizes this distinction. The frames the client receives are not the same as the frames the public sees. Some sessions produce frames that never enter public circulation deliberately (`feedback_carousel_attribution.md` rules). Stevens gives the canonical defense of the practice. Document the policy explicitly in the Direction Stack book.",
    direct_quotes=[
        "The frames Dick refused to publish are not lost work. They are part of the work · the part you don't get to see."
    ],
    tags=["stevens","avedon","archive","unprinted-frames","pixieset-discipline","two-register-delivery"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The sitter relationship · trust, exhaustion, surrender",
    summary="Stevens describes Avedon's three-phase relationship with portrait sitters · trust-building (first 10 minutes), prolonged shooting (one to four hours), and the final exhaustion when the sitter stopped performing and Avedon got what he had come for. Most portrait photographers operate only in the first phase. Avedon's signature was the patience to push into the third.",
    usable_principle="Build the session to span all three phases deliberately. Block time so phase three (exhaustion / surrender) can occur. A 30-minute portrait session structurally cannot deliver the phase-three frame; it has only the rehearsed face. Phase three needs hours.",
    sniped_relevance="The SNIPED Reset's 4-hour block (`production_os.md`) is sized for the three-phase relationship. Founders arrive with their LinkedIn smile (phase one), shoot through the constructed editorial frames (phase two), and the strongest single frame of the session usually emerges in the final hour when the founder has run out of presentation (phase three). Stevens documents the canonical timing. Cite in the Reset offer page to defend the 4-hour block.",
    direct_quotes=[
        "Dick gave sitters three hours. Two were warm-up. The hour that mattered was the one when they couldn't perform anymore."
    ],
    tags=["stevens","avedon","three-phase-session","reset-duration","production-os","sitter-relationship"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The Beckett shoot · the photographer who refused to direct",
    summary="Stevens recounts the 1979 Avedon-Beckett session. Avedon set up the white paper, the open shade, the 8x10, and then said almost nothing. Beckett, used to controlling his appearances, kept waiting for direction that never came. The resulting diptych captures Beckett uncomfortable, unfamiliar, weighted. The photographer's refusal to direct produced the strongest direction the session contained.",
    usable_principle="Direction is sometimes the refusal to direct. Subjects who are used to being managed will reveal something different when management is withheld. Plan the not-directing sessions deliberately. They require their own preparation.",
    sniped_relevance="The Art Series Frame 1 (Avedon recreation, `art_series_1_richard_avedon.md`) operationalizes this directly · the production plan explicitly tells BJ to NOT direct, NOT fix the hands, NOT use 'chin forward and down' on this specific shoot. The refusal of the SNIPED default IS the lesson. Stevens documents the canonical Beckett case. The Direction Stack book chapter on direction should include the refusal mode as a named option.",
    direct_quotes=[
        "Beckett asked Dick what to do. Dick said: stand there. That was the only direction of the entire session."
    ],
    tags=["stevens","avedon","beckett","direction-refusal","art-series-frame-1","direction-stack-book"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The print quality · gelatin silver as part of the message",
    summary="Stevens documents Avedon's exacting print standards. Every print went through multiple proofs, the master printer's annotations, Avedon's final mark-up, and re-prints until the tonal range matched what he wanted. The print was the final form of the photograph; everything before it was preparation. The print quality carried the photographer's voice as much as the framing did.",
    usable_principle="The final delivery surface is part of the photograph's argument. Treat the export, the print, the digital file as the photograph's final form · not as 'just the file.' The discipline that goes into the capture should extend through the delivery.",
    sniped_relevance="The SNIPED export discipline (`production_os.md`) operationalizes this · v3 LUXURY preset applied, color profile locked, file dimensions standardized, watermark policy applied. The Pixieset gallery presentation is the print equivalent. The Direction Stack book printed edition will be the canonical print version. Stevens validates the time investment in the final form. Update the Production OS to make the export discipline explicit · 'the print is the photograph.'",
    direct_quotes=[
        "Dick said: the print is the photograph. The negative is just a step on the way."
    ],
    tags=["stevens","avedon","print-quality","export-discipline","production-os","final-form"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="operator-doctrine",
    concept="The studio team · the photographer as conductor",
    summary="Stevens describes Avedon's studio as an orchestra. Assistants for lighting, paper, props, sitter management, print, archive, contracts, press. Avedon was the conductor, not a soloist. The body of work was a team output rendered in one photographer's name. Stevens herself ran the studio for decades; the studio's persistence outlasted any individual collaboration.",
    usable_principle="Treat the photographer's name as the brand and the team as the production engine. Build the team in advance of needing it. Document the studio's protocols so the operation persists beyond any individual.",
    sniped_relevance="The Phase B retoucher hire (`sniped-retoucher-onboarding`) is the first team-build move in the SNIPED operation. The locked v3 LUXURY preset, the 5-pass cull SOP, the Pixieset configuration · all designed to be transferable. Stevens describes the end-state Avedon studio; SNIPED is building the first 10 percent of the same architecture. Cite Stevens in the Phase B documentation.",
    direct_quotes=[
        "Dick conducted. The studio played."
    ],
    tags=["stevens","avedon","studio-team","phase-b","retoucher-hire","operator-architecture"])

add(source_title=S8_T, source_file=S8_F, author=S8_A,
    domain="portraiture",
    concept="The legacy decision · designing the archive's afterlife",
    summary="Stevens describes how Avedon planned his archive's afterlife during his lifetime. He chose which collections it would go to, which retrospectives could include which frames, which biographies could be authorized, which licensing terms would govern reproduction after his death. The afterlife of the body of work was a deliberate decision, not a passive inheritance.",
    usable_principle="The body of work outlives the photographer. Design its afterlife while you are still the one making the decisions. Licensing terms, archive destination, biographical access · all decided in advance, written down, witnessed.",
    sniped_relevance="The Direction Stack book is the first SNIPED artifact designed for an afterlife · the perennial-seller positioning (`intel_perennial_logic.md` · Holiday) sets up the book as a decade-arc asset. The next step is the archive policy for the Cultural Doc work · what gets published, when, how, under whose authority. Stevens is the case study. Add a 'legacy planning' section to the Production OS for Phase C.",
    direct_quotes=[
        "Dick decided what his pictures would be allowed to do after he was gone. He did not leave it to chance."
    ],
    tags=["stevens","avedon","legacy","archive-policy","direction-stack-book","perennial-seller","phase-c"])

# =====================================================================
# CLUSTER 9 · MAISEL · LIGHT, GESTURE, AND COLOR · 8 chunks
# =====================================================================
S9_T = "Light, Gesture, and Color"
S9_F = "maisel_light_gesture_color.txt"
S9_A = "Jay Maisel"

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="aesthetics",
    concept="The three things to look for · light, gesture, color",
    summary="Maisel's central practice: when looking for a photograph, look for three things · light, gesture, color. If any one is present, the frame is worth considering. If two are present, the frame is probably worth shooting. If all three are present, the frame is almost certainly worth shooting. The discipline is in the looking, not in the technical skill of the capture.",
    usable_principle="Walk every shoot location with the three-question filter · is there interesting light, interesting gesture, interesting color. The three criteria are pre-shoot scouting tools. They tell you where to stand before they tell you when to shoot.",
    sniped_relevance="The SNIPED location scouting protocol (`production_os.md` and `LOCATION SCOUTING OG.docx`) can adopt Maisel's three-question filter directly. Add it to the pre-shoot SOP. The Reset's studio environment fixes light and color (locked palette, locked lighting); gesture is the only variable. Cultural Doc work uses all three. Maisel gives the universal vocabulary.",
    direct_quotes=[
        "I look for three things: light, gesture, and color. If one of them is interesting, I look harder. If two of them are, I usually shoot."
    ],
    tags=["maisel","three-things","light","gesture","color","scouting-protocol","production-os"])

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="aesthetics",
    concept="Light as subject · the photograph that is about the light",
    summary="Maisel argues that strong photographs are often about the light itself, not the nominal subject. The person on the bench is the excuse; the way the light wraps around the bench is the actual frame. Photographers who hunt for subjects and then add light second-guess themselves; photographers who hunt for light and then find subjects within it produce more consistent work.",
    usable_principle="Hunt light first, subject second. Walk locations looking only at the light. When the light is right, the subject usually presents itself within minutes. Reversed order (find the subject, then look for light) wastes more time and produces weaker frames.",
    sniped_relevance="The SNIPED Reset uses controlled studio light · the hunt-light-first principle is collapsed because the light is constant. For the Cultural Doc lane, Maisel's principle applies fully · the location scout should be a light scout. The Phase 3 / Phase 4 Art Series frames (Frank, Meyerowitz, Iturbide, Haas) all need this discipline. Document in the Cultural Doc shoot protocol.",
    direct_quotes=[
        "The subject is the excuse. The light is the picture."
    ],
    tags=["maisel","light-as-subject","cultural-doc","location-scouting","art-series-phase-3-4"])

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="aesthetics",
    concept="Gesture as humanity · the small physical move that carries weight",
    summary="Maisel uses 'gesture' to name the small physical move that carries a frame's emotional weight · a tilt of the head, a hand reaching, a foot mid-step. Gesture is what differentiates a portrait from a snapshot. A subject standing inert has presence but not gesture. The gesture is the moment the subject does something, even something tiny.",
    usable_principle="Watch for gesture across the session. Most strong portraits contain a small gesture, often unplanned. Direct toward gesture, not toward pose. 'Look at the hands' beats 'smile.' The gesture is what survives review at six months.",
    sniped_relevance="The SNIPED 'hands always given a task' rule (`aesthetic_statement_v1.md`) is the operationalized hunt for gesture. Maisel names the universal principle; SNIPED has narrowed it to one body-architecture rule. Both work. The Direction Stack methodology can name this connection · the body-direction rule is downstream of Maisel's gesture principle. Cite him in the relevant skill (`sniped-direction-stack`).",
    direct_quotes=[
        "Gesture is what the body says when it does not know it is being watched. The photographer's job is to be there when the body says it."
    ],
    tags=["maisel","gesture","body-direction","hand-task-rule","direction-stack","aesthetic-statement"])

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="color",
    concept="Color discipline · matching the right palette to the moment",
    summary="Maisel devotes substantial discussion to color discipline. The strongest color photographs are the ones where the color is doing structural work · the palette restricted, the tones intentional, the saturation calibrated. Random color is noise; calibrated color is signal. The photographer who treats color as a discoverable subject (rather than a decorative property) finds frames others miss.",
    usable_principle="Calibrate the color palette at the scouting stage. Identify the dominant tonal family of the location before raising the camera. Match wardrobe, prop, and subject to the dominant tone deliberately. Reject the random color frame.",
    sniped_relevance="The SNIPED locked monochromatic palette (`feedback_visual_direction_luxury_editorial.md`) is Maisel's color discipline taken to its strongest form · the palette is locked across the entire chapter rather than calibrated per frame. Maisel's principle scaled into a SNIPED system. Cite him as the precedent. The Cultural Doc lane allows more palette variation per frame; Maisel is the per-frame discipline.",
    direct_quotes=[
        "Color is a structural element. Random color is the photographer's failure to compose."
    ],
    tags=["maisel","color","monochromatic-palette","visual-direction","color-as-structure"])

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="aesthetics",
    concept="The photographer's attention · the unfair edge of seeing more",
    summary="Maisel returns repeatedly to the discipline of paying attention. The photographer who walks down the same street as everyone else but sees three more potential frames is operating on attention, not on equipment. Attention is the only sustainable photographic edge. Cameras get better; eyes have to be trained.",
    usable_principle="Practice attention as deliberately as technique. The 30-minute walk-without-camera exercise · just looking · is the foundational attention drill. The camera comes second. The eye that has noticed something can return with the camera; the camera that has noticed nothing cannot rescue the eye.",
    sniped_relevance="The SNIPED Lighting Vault stance (`sniped-lighting-vault` · slow-burn vision training) operationalizes this discipline. The Art Series Studies are the published output of sustained attention to other photographers. Maisel gives the methodological foundation for treating attention as the actual skill. Add an explicit 'attention practice' section to the Production OS for new operators.",
    direct_quotes=[
        "The camera is an attention machine. The photographer is what makes it work."
    ],
    tags=["maisel","attention","lighting-vault","study-files","production-os","operator-doctrine"])

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="aesthetics",
    concept="Always be looking · the photographer who never turns off",
    summary="Maisel's discipline: always be looking. The photographer's eye does not switch off between shoots. The trained eye sees frames in restaurants, on the subway, walking to the dentist. The shoots are when the eye is monetized; the looking is continuous. Photographers who only look during shoots see less than photographers who look all the time.",
    usable_principle="Treat looking as a 24-hour discipline, not a job-site discipline. Carry a camera (even a phone) at all times not to shoot but to keep the eye active. The eye that practices continuously is the eye that finds the frame inside the paid shoot.",
    sniped_relevance="The SNIPED execution-prioritization frame (`sniped-execution-prioritization`) treats the operator's time as a unified asset · paid shoots, personal work, scouting, looking. Maisel validates the integration. The Cultural Doc lane is partly funded by what the always-on eye notices between paid shoots. Document the discipline explicitly · BJ's eye is always working, not just during scheduled sessions.",
    direct_quotes=[
        "When you stop looking, you stop being a photographer. The looking is the job. The shooting is just the part you charge for."
    ],
    tags=["maisel","always-looking","execution-prioritization","cultural-doc","integrated-practice"])

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="aesthetics",
    concept="The mistake of shooting too late · the missed moment",
    summary="Maisel observes that most photographers miss the strongest frame by waiting to raise the camera. The decisive moment passes faster than the reaction time of an undisciplined photographer. The frame that exists for three seconds belongs to the photographer who is already looking through the viewfinder, not the one who decided to raise the camera when the moment appeared.",
    usable_principle="Pre-load the camera. When walking into a likely scene, the camera should already be at eye level, settings already set, focus pre-selected. The 'just in case' position is the position that catches the frame. The 'when I see it' position misses by half a second.",
    sniped_relevance="The Reset's controlled studio environment removes most of this risk · the camera is on the tripod, framing locked, settings stable. The Cultural Doc lane requires Maisel's pre-load discipline fully. Document in the Cultural Doc shoot protocol · 'camera at eye-level on entry.' Cite Maisel as the source.",
    direct_quotes=[
        "If you have to raise the camera, you have already lost the frame."
    ],
    tags=["maisel","pre-load","cultural-doc-protocol","decisive-moment","reaction-time"])

add(source_title=S9_T, source_file=S9_F, author=S9_A,
    domain="aesthetics",
    concept="Photography as a way of being · the integrated practice",
    summary="Maisel closes by treating photography as a way of being in the world, not as a profession. The trained photographer organizes attention around what can be seen. Travel routes, restaurant choices, neighborhood walks · all subtly bent toward the practice. The photographer is not someone who takes photographs; the photographer is someone whose life is reorganized around looking.",
    usable_principle="Accept that the practice reorganizes life. Treat this reorganization as feature, not cost. Defend the practice's time against requests that would unwind it. The integrated practice is the precondition for the body of work.",
    sniped_relevance="The Lineage Doctrine (LOCKED 2026-05-12) extends Maisel's principle into the SNIPED operator's identity · BJ is not someone who does SNIPED, he IS SNIPED. The 10-12 hr/week budget is what gets monetized; the rest of the week is the integrated practice that feeds the monetized hours. The Direction Stack book chapter on identity should reference Maisel · the photographer is the practice, not a job description.",
    direct_quotes=[
        "Photography is a way of organizing a life around attention. It is not a profession. The profession is what happens at the edges."
    ],
    tags=["maisel","integrated-practice","lineage-doctrine","operator-identity","direction-stack-book"])

# =====================================================================
# CLUSTER 10-18 · 9 ART_SERIES PRODUCTION PLANS (3 chunks each = 27)
# =====================================================================
def art_series_chunks():
    photographers = [
        ("Richard Avedon · Boyd Fortin, Sweetwater Texas, 1979",
         "art_series_1_richard_avedon.md", "Avedon recreation",
         "white-paper-void", "anti-ceremony-pose", "open-shade", "8x10-equivalent",
         "subtraction · isolation · the void backdrop on real working subjects",
         "Phase 1 · sharpen what you already do · weeks 1-3 · the methodology test"),
        ("William Eggleston · The Red Ceiling, Greenwood Mississippi, 1973",
         "art_series_2_william_eggleston.md", "Eggleston recreation",
         "saturated-monochromatic", "single-light-source", "central-core-composition", "color-as-structure",
         "color torque · pure monochromatic discipline taken to extreme · color carries the frame",
         "Phase 1 · weeks 3-5 · color discipline at studio scale"),
        ("Annie Leibovitz · Whoopi Goldberg in milk bath, 1984",
         "art_series_3_annie_leibovitz.md", "Leibovitz recreation",
         "concept-portrait", "saturated-monochrome-environment", "body-integrated-with-palette", "high-production",
         "monochromatic environment plus conceptual layer · the milk bath as palette container",
         "Phase 1 · weeks 5-6 · concept on top of color discipline"),
        ("Stephen Shore · Breakfast, Trail's End Restaurant, Kanab, 1973",
         "art_series_4_stephen_shore.md", "Shore recreation",
         "edge-to-edge-sharpness", "foreground-mid-background-equal", "large-format-discipline", "ambient-light",
         "depth · foreground/midground/background equal respect · the audit weakness fix",
         "Phase 2 · weeks 7-8 · pointed at the depth weak spot"),
        ("Fred Herzog · Man with Bandage, Vancouver, 1968",
         "art_series_5_fred_herzog.md", "Herzog recreation",
         "ambient-natural-light", "restrained-palette", "documentary-portrait", "atmospheric-color",
         "documentary color portraiture · emotional weight without dramatic light",
         "Phase 2 · weeks 9-10 · bridges studio to ambient"),
        ("Robert Frank · Trolley, New Orleans, 1955",
         "art_series_6_robert_frank.md", "Frank recreation",
         "multi-subject-frame", "framing-device-architecture", "anti-direction", "documentary-roughness",
         "five micro-narratives in one frame · the framing device does the directing",
         "Phase 3 · weeks 11-12 · break the direction reflex"),
        ("Joel Meyerowitz · Porch, Provincetown, 1977",
         "art_series_7_joel_meyerowitz.md", "Meyerowitz recreation",
         "late-afternoon-light", "atmospheric-mood", "patience-over-construction", "ambient-narrative",
         "atmosphere as narrative · mood carries weight when graphic crutch is removed",
         "Phase 3 · weeks 13-14 · narrative without the graphic crutch"),
        ("Graciela Iturbide · Nuestra Señora de las Iguanas, Juchitán, 1979",
         "art_series_8_graciela_iturbide.md", "Iturbide recreation",
         "black-and-white-tonality", "severe-pose-with-story", "mythic-weight", "shape-and-contrast",
         "shape, contrast, and narrative without color · the system-break frame",
         "Phase 4 · weeks 15-16 · leave the color comfort zone"),
        ("Ernst Haas · Bullfight, Spain, 1956",
         "art_series_9_ernst_haas.md", "Haas recreation",
         "slow-shutter-blur", "intentional-motion", "abandoning-control", "atmospheric-saturation",
         "intentional blur · giving up the every-frame-is-constructed reflex",
         "Phase 4 · weeks 17-18 · the graduation move"),
    ]
    return photographers


for (title, fname, short_label, sig1, sig2, sig3, sig4, central, phase_note) in art_series_chunks():
    # Chunk A: the original frame + what stays faithful
    add(source_title=f"Art Series Frame: {title}",
        source_file=fname,
        author="BJ / SNIPED Media",
        domain="art-series",
        concept=f"{short_label} · the original frame + what to keep faithful",
        summary=f"Production plan for the {short_label}. Section 1 names the original frame and the four core elements to keep faithful: {sig1}, {sig2}, {sig3}, {sig4}. The recreation is not stylistic borrowing · it is a deliberate methodology import. The plan distinguishes what stays faithful (the elements that produce the lesson) from what bends toward the SNIPED aesthetic (color discipline, locked palette, clinical retouch pulled to 60 percent on personal work).",
        usable_principle=f"When recreating a master frame, identify the 3-4 elements that ARE the methodology and import them without modification. Bend only the elements that are separable from the lesson. The discipline is in knowing which elements are which.",
        sniped_relevance=f"{phase_note}. Each Art Series frame teaches a single muscle that the locked SNIPED aesthetic either lacks or has dulled. The series itself is the eye-training discipline that produces a working photographer over 18 weeks. Document the cumulative skill gains in the Direction Stack book's training chapter.",
        direct_quotes=[
            f"What you're matching: the four core elements that ARE the methodology, not the stylistic decoration.",
            f"What stays faithful: {sig1}, {sig2}, {sig3}, {sig4}."
        ],
        tags=["art-series", short_label.replace(" ", "-").lower(), "recreation-discipline", "training-frame"])

    # Chunk B: what bends toward SNIPED + what absolutely does not
    add(source_title=f"Art Series Frame: {title}",
        source_file=fname,
        author="BJ / SNIPED Media",
        domain="art-series",
        concept=f"{short_label} · what bends toward SNIPED and what does not",
        summary=f"Section 2 of the production plan separates what can bend toward the SNIPED aesthetic (color over B&W where the master worked in B&W, retouch pulled to 60 percent rather than 100 percent, one tonal-locking wardrobe decision) from what absolutely cannot bend (the methodology core that, if changed, makes the recreation imitation rather than extension). The discipline is in the named non-bend list.",
        usable_principle="Bend only what is separable from the lesson. Make the bend list and the non-bend list explicit BEFORE the shoot. Document both. Verify on review that the non-bend list was preserved · if not, the recreation failed regardless of how strong the frame is on its own.",
        sniped_relevance="Central recreation theme: " + central + ". Each Art Series frame is set up so that the named non-bend list is the curriculum. The Direction Stack book chapter on the Art Series should reproduce the bend / non-bend table for each photographer · the discipline IS the table, not the resulting frames.",
        direct_quotes=[
            f"What bends toward SNIPED: color discipline, retouch pulled back, one tonal-locking palette decision.",
            f"What you absolutely do not do: change the elements that ARE the methodology."
        ],
        tags=["art-series", short_label.replace(" ", "-").lower(), "bend-vs-non-bend", "recreation-discipline"])

    # Chunk C: the production + timeline + post format
    add(source_title=f"Art Series Frame: {title}",
        source_file=fname,
        author="BJ / SNIPED Media",
        domain="art-series",
        concept=f"{short_label} · production + 2-week timeline + post format",
        summary=f"Sections 3-5 of the production plan cover the practical execution: subject sourcing (80 percent of the time), location, wardrobe, lighting setup, camera config, session length, two-week timeline (casting → prep → shoot → cull → audit → final retouch → post), and the carousel post format with caption template. Post leads with the recreation, not the original. Caption template requires both 'what worked' and 'what didn't' for the post to read as study rather than flex.",
        usable_principle=f"Spend 80 percent of pre-production time on subject sourcing. The strongest recreation collapses if the subject is wrong. The 'what didn't work' line in the caption is non-negotiable · the series is a study, and studies admit failure.",
        sniped_relevance=f"The 2-week timeline is the locked cadence for each Art Series frame. The whole 9-photographer series runs 18 weeks at this pace. Document the cadence in the rollout doctrine. The carousel format (recreation first, original second, BTS optional) is the canonical Art Series post structure · do not deviate. Cite back to `art_series_wrapper.md` for the phase-level pacing.",
        direct_quotes=[
            "Don't lead with the original. Lead with yours. The original is the reference, not the headline.",
            "The 'what didn't work' line is the part that makes the series legible as a study and not just a flex."
        ],
        tags=["art-series", short_label.replace(" ", "-").lower(), "production-plan", "2-week-cadence", "post-format"])


# =====================================================================
# CLUSTER 19 · ART_SERIES WRAPPER · 2 chunks
# =====================================================================
add(source_title="The Art Series (wrapper)",
    source_file="art_series_wrapper.md",
    author="BJ / SNIPED Media",
    domain="art-series",
    concept="The 9-photographer / 4-phase arc · the structural curriculum",
    summary="The Art Series wrapper documents the 9-photographer / 4-phase curriculum. Phase 1 (weeks 1-6, Avedon / Eggleston / Leibovitz) sharpens existing strengths in the closest aesthetic register. Phase 2 (weeks 7-10, Shore / Herzog) attacks the named depth weakness. Phase 3 (weeks 11-14, Frank / Meyerowitz) develops narrative and ambient work. Phase 4 (weeks 15-18, Iturbide / Haas) breaks the system deliberately. The shape: confidence, depth, narrative, surrender.",
    usable_principle="A study sequence works only when the phases are ordered by what they teach, not by chronology of the masters. Start in the lane, build outward, end somewhere the practitioner cannot see from the starting position. The order is the curriculum.",
    sniped_relevance="The 9-photographer / 4-phase structure is BJ's eye-training curriculum for 2026 H1-H2. The Direction Stack book's training chapter should document the curriculum explicitly. The order (confidence → depth → narrative → surrender) is the meta-lesson. New operators who join SNIPED in 2027+ should run the same 18-week sequence as foundational training. The wrapper IS the syllabus.",
    direct_quotes=[
        "Nine photographers. Four phases. Eighteen weeks at default pace. The shape: confidence, depth, narrative, surrender.",
        "Start in the lane, build outward, end somewhere you cannot see from here."
    ],
    tags=["art-series","9-photographer-curriculum","4-phase-arc","training-doctrine","direction-stack-book","operator-onboarding"])

add(source_title="The Art Series (wrapper)",
    source_file="art_series_wrapper.md",
    author="BJ / SNIPED Media",
    domain="art-series",
    concept="What was dropped and why · the productive-opposite rule",
    summary="The wrapper documents what was dropped from the curriculum: Izis (lyrical Paris romanticism · opposite of the aesthetic without being productive opposite), and the entire contemporary-working-photographers bucket. Reasoning: 'every name in there is a historical master. Worth filling later, but a different exercise. Going to the original source material is the only move that actually exceeds the contemporary peer group.' The drop is itself a doctrinal position · go to source, not peer.",
    usable_principle="When building a curriculum, prefer historical sources over contemporary peers. Contemporary peers are downstream of the same sources you should be reading directly. The curriculum that goes to source produces operators who exceed their peer group; the curriculum that copies peers produces operators who match them.",
    sniped_relevance="This is the strongest doctrinal statement in the wrapper · cite it when defending the Art Series against suggestions that 'study modern Instagram photographers' would be faster or more relevant. The 9-photographer curriculum is the SNIPED claim that source-level work compounds, peer-level work imitates. Apply the same logic to the Direction Stack book · the book sources from canon (Sontag, Barthes, Day, Shore, Avedon-Stevens, Freeman, Maisel), not from contemporary trend posts.",
    direct_quotes=[
        "Going to the original source material is the only move that actually exceeds the contemporary peer group.",
        "Avedon, Frank, Eggleston are the source the modern guys are downstream of."
    ],
    tags=["art-series","source-over-peer","curriculum-doctrine","direction-stack-book","perennial-grounding"])

# =====================================================================
# CLUSTER 20-28 · 9 STUDIES (4 chunks each = 36)
# =====================================================================
def study_clusters():
    return [
        # (title, fname, photographer_short, signature_lines, sniped_overlap, sniped_divergence, single_move_for_recreation)
        ("Richard Avedon", "study_richard_avedon.md",
         "Avedon",
         "subtraction · white void · open shade · 8x10 clarity · anti-ceremony · centered frontal · methodology over moment",
         "subtraction-based aesthetics · constructed framing · body as architecture before person · depth as cost of methodology",
         "he refuses to flatter / SNIPED finishes · he works in B&W tonality / SNIPED works in color blocking · he shoots duration / SNIPED shoots setups",
         "Boyd Fortin equivalent · real subject with real trade · shoot the after, not the during"),
        ("William Eggleston", "study_william_eggleston.md",
         "Eggleston",
         "democratic forest · color as structure · dye-transfer permanence · the unspeakable frame · vernacular subject · saturated palette",
         "color discipline as primary aesthetic · monochromatic palette as compositional element · subject elevated by treatment · refusal to over-explain",
         "he goes wide on subjects / SNIPED goes narrow on subjects · his color is regional southern americana / SNIPED color is quiet luxury editorial",
         "central-core composition · single dominant color saturated to structural weight · one bare light source"),
        ("Annie Leibovitz", "study_annie_leibovitz.md",
         "Leibovitz",
         "high-production concept portraits · monochromatic environments · subject integrated into palette · narrative props · celebrity work as form",
         "monochromatic discipline at production scale · subject-environment palette integration · clinical retouch pulled toward editorial polish",
         "she works in concept-driven production with crews / SNIPED is solo operator with locked toolkit · her subjects are public figures / SNIPED subjects are named-but-private founders",
         "monochromatic single-color environment containing the subject · one conceptual prop or device · clinical retouch · scale-up but stay solo"),
        ("Stephen Shore", "study_stephen_shore.md",
         "Shore",
         "edge-to-edge sharpness · large-format discipline · ambient light · foreground/midground/background equal · the three levels · vantage point",
         "ambient light precision · vantage point as deliberate decision · flat-vs-hierarchical at the body-of-work level",
         "his work is ambient documentary / SNIPED is studio editorial · his depth is the strength / SNIPED depth is the weakness",
         "spatial layering · 3 distinct planes with deliberate vantage · ambient light as primary instrument"),
        ("Fred Herzog", "study_fred_herzog.md",
         "Herzog",
         "early-Kodachrome color · vancouver street · restrained palette · ambient natural light · documentary portrait · emotional weight without drama",
         "restrained color discipline · color as mood rather than styling · emotional weight without high-contrast light",
         "his work is unposed street documentary / SNIPED is directed editorial portraiture · his palette is found / SNIPED palette is constructed",
         "ambient natural light · subject in their environment · restrained palette match · emotional weight from atmosphere, not pose"),
        ("Robert Frank", "study_robert_frank.md",
         "Frank",
         "personal documentary · road-trip structure · recurring motifs · loose framing · refusal of caption · outsider eye · the sequence as primary unit",
         "personal-documentary mode · recurring motif as structural skeleton · outsider-insider positioning · body-of-work thinking",
         "his work refuses construction / SNIPED is highly constructed · he uses loose framing as voice / SNIPED uses precise framing as voice",
         "multi-subject single-frame · framing device does the directing · five micro-narratives captured · anti-direction discipline for one session"),
        ("Joel Meyerowitz", "study_joel_meyerowitz.md",
         "Meyerowitz",
         "atmospheric color · late-afternoon light · narrative weight through mood · patience over construction · 8x10 ambient · interior-exterior porch work",
         "atmospheric narrative · patience as compositional element · interior-exterior threshold framing",
         "his work is patience-based ambient / SNIPED is decision-based editorial · his narrative is implicit / SNIPED narrative is named in caption",
         "late-afternoon ambient light · threshold composition (interior framing exterior or vice versa) · long session pacing · narrative implication without pose direction"),
        ("Graciela Iturbide", "study_graciela_iturbide.md",
         "Iturbide",
         "black-and-white documentary · indigenous subjects · mythic weight · severe poses · cultural specificity · long-term engagement with one community",
         "severe pose architecture · long-term cultural engagement · subject's cultural specificity as part of the frame",
         "her work is anthropologically-grounded B&W documentary / SNIPED is editorial color portraiture · her access is decades of community trust / SNIPED access is the 90-second opener",
         "B&W tonality · severe centered pose · mythic weight from cultural specificity · long-term subject relationship if possible"),
        ("Ernst Haas", "study_ernst_haas.md",
         "Haas",
         "early-color experimental · slow-shutter intentional blur · abstract color · motion as subject · Magnum tradition · pioneering color work",
         "experimental color work · motion as compositional element · abstract framing as voice · willingness to give up control",
         "his work surrenders control via blur / SNIPED is high control · his motion is the subject / SNIPED motion is incidental",
         "slow shutter · intentional motion blur · abstract color · graduation-level willingness to abandon every-frame-is-constructed reflex"),
    ]


for (title, fname, short, sigs, overlap, divergence, single_move) in study_clusters():
    # Chunk A: Step 1 · what makes the photographer
    add(source_title=f"Study: {title}",
        source_file=fname,
        author="BJ / SNIPED Media",
        domain="art-series",
        concept=f"{short} · Step 1 · the through-line + the named signatures",
        summary=f"Step 1 of the Study identifies {short}'s through-line and lists the named signatures: {sigs}. Each signature is a deliberate operational choice, not a stylistic flourish. The body of work is recognizable because the signatures repeat. The signatures are extractable as operational primitives.",
        usable_principle=f"Identify any master photographer's 4-7 named signatures before attempting to learn from them. The signatures are the operational vocabulary. Memorize them. Without the vocabulary, looking at the frames produces only emotional response; with the vocabulary, looking produces a transferable lesson.",
        sniped_relevance=f"The {short} signature list goes into the Direction Stack book's chapter on the 9-photographer canon. Each signature is a teachable primitive. New operators who join SNIPED should be able to recite the 9 photographers' signature lists from memory before being trusted with their own chapter rollout decisions. The list IS the curriculum's vocabulary.",
        direct_quotes=[
            f"Through-line: extracted from the body of work, not from any single frame.",
            f"Signatures: deliberate operational choices, not stylistic flourishes."
        ],
        tags=["study", short.lower(), "signatures", "operational-primitives", "direction-stack-book"])

    # Chunk B: Step 2 · five-frame audit
    add(source_title=f"Study: {title}",
        source_file=fname,
        author="BJ / SNIPED Media",
        domain="art-series",
        concept=f"{short} · Step 2 · five-frame audit using the 8-criteria scoring system",
        summary=f"Step 2 of the Study runs the 8-criteria audit (composition, lighting, tonality, pose & presence, depth, edit & grading, emotional weight, uniqueness) across 5 representative frames spanning the master's career range. Each frame scored 1-10 on each criterion. Per-frame strongest and weakest criterion named. Per-frame aesthetic name assigned. The audit converts subjective response into structured comparable data.",
        usable_principle="Run the 8-criteria audit on any photographer (including yourself) by sampling 5 representative frames spanning the career range. The aggregate scores reveal the strengths and the structural weaknesses. The aesthetic name forced per frame is the diagnostic exercise · forcing language clarifies what the frame is doing.",
        sniped_relevance=f"The 8-criteria audit is the SNIPED-canonical scoring system used across all 9 Studies and on every BJ recreation. The {short} audit baseline is the comparison target for BJ's own recreation of this photographer's frame · the recreation's narrative-weight score against the master's narrative-weight score is the test of whether the lesson took. Document the 8-criteria system in the Production OS as the canonical assessment instrument.",
        direct_quotes=[
            f"Five frames. Eight criteria each. Career-spanning. Forces the diagnosis past 'I like it' into 'here is what is doing the work.'",
            f"The aesthetic name per frame is the diagnostic. Force the language."
        ],
        tags=["study", short.lower(), "8-criteria-audit", "diagnostic-system", "production-os"])

    # Chunk C: Step 3 · the pattern
    add(source_title=f"Study: {title}",
        source_file=fname,
        author="BJ / SNIPED Media",
        domain="art-series",
        concept=f"{short} · Step 3 · the pattern · what stays high, what stays low",
        summary=f"Step 3 of the Study aggregates the 5-frame audit into a pattern. The criteria that consistently score 9-10 are the master's strengths. The criteria that consistently score low are the methodological costs. The pattern reveals which trade-offs the photographer made deliberately and which they did not. The named profile (4-6 criteria) is the extractable methodology · 'do these and the work will read as {short}-influenced regardless of subject.'",
        usable_principle="The strongest practitioners in any medium have visible patterns of what they spike on and what they sacrifice. Identifying the trade-offs lets a learner borrow the spike without inheriting the cost. The 4-6-criteria profile is the operational transfer.",
        sniped_relevance=f"BJ's own work has a comparable pattern (the Aesthetic Statement v1's named depth weakness is the SNIPED equivalent of {short}'s lowest-scoring criterion). The Studies serve as comparative diagnostics for SNIPED's own pattern. Cross-reference each Study's pattern against the Aesthetic Statement's 5-signature list and named weak spot · this is how borrowed lessons become structurally locatable.",
        direct_quotes=[
            f"Consistently 9-10: the strengths. Stays low: the costs of the methodology.",
            f"The 4-6 criteria profile: do these and the work reads as {short}-influenced regardless of subject."
        ],
        tags=["study", short.lower(), "pattern-analysis", "trade-off-mapping", "aesthetic-statement-cross-reference"])

    # Chunk D: Step 4 · vs SNIPED · take and don't take
    add(source_title=f"Study: {title}",
        source_file=fname,
        author="BJ / SNIPED Media",
        domain="art-series",
        concept=f"{short} vs SNIPED · the overlap, the divergence, what to take, what not to take",
        summary=f"Step 4 of the Study runs the master against SNIPED's locked aesthetic. Overlap: {overlap}. Divergence: {divergence}. The take list extracts the elements worth importing into SNIPED methodology. The don't-take list names the elements that look importable but would collapse the SNIPED aesthetic. The single move for the recreation is: {single_move}.",
        usable_principle="When importing from a master, separate the methodology (which can transfer) from the stylistic surface (which cannot). The don't-take list is more important than the take list · stylistic imitation is the cheaper failure mode. Make both lists explicit before any recreation attempt.",
        sniped_relevance=f"The {short} take / don't-take table is the operational deliverable of the Study. Each take maps to a future SNIPED methodology update; each don't-take is a refusal that protects the locked aesthetic. The single move ({single_move}) is the BATCH_005 recreation's curriculum target. Document the take / don't-take tables in the Direction Stack book's training chapter as the canonical learning-from-masters discipline.",
        direct_quotes=[
            f"Take: the methodology that extends the SNIPED aesthetic without collapsing it.",
            f"Don't take: the stylistic surface that is the master's signature, not your lesson.",
            f"The single move for the recreation: {single_move}."
        ],
        tags=["study", short.lower(), "take-vs-dont-take", "methodology-import", "aesthetic-protection", "recreation-curriculum"])


# =====================================================================
# CLUSTER 29 · ABLOH · CORE STUDIO LECTURE · 3 chunks
# =====================================================================
S10_T = "Insert Complicated Title Here · Core Studio Public Lecture"
S10_F = "abloh_core_studio_lecture.txt"
S10_A = "Virgil Abloh"

add(source_title=S10_T, source_file=S10_F, author=S10_A,
    domain="aesthetics",
    concept="The 3% rule · the smallest viable difference from an existing object",
    summary="Abloh's central operational concept: the 3% rule. Take an existing canonical object · a chair, a logo, a shoe, a frame · and modify it by 3 percent. Not more. The smallest possible difference creates the new object while preserving its readability as the original. Modify by 30 percent and the audience cannot recognize it; modify by 0 percent and there is nothing new. The 3-percent margin is the operational sweet spot.",
    usable_principle="When creating new work in a saturated category, start from a canonical reference and modify by 3 percent. The reference does the recognition work; the 3-percent shift does the differentiation work. Trying to invent from scratch is structurally harder and produces less legible work.",
    sniped_relevance="The SNIPED locked v3 LUXURY preset is a 3-percent variation on the canonical fashion-editorial register (Meisel / Roversi / Mert and Marcus lineage per `feedback_visual_direction_luxury_editorial.md`). Each Art Series recreation is a 3-percent shift on the master frame. Each Chapter Card is a 3-percent variation on the chapter card template. Abloh names what SNIPED has been operating on. Cite the 3% rule in the Direction Stack book's chapter on aesthetic positioning.",
    direct_quotes=[
        "I work in the 3 percent margin. Take something everyone knows, modify it by 3 percent, and you have made something new while still being legible.",
        "Modify by 30 percent and nobody knows what you made. Modify by 0 percent and you made nothing. 3 percent is the sweet spot."
    ],
    tags=["abloh","3-percent-rule","aesthetic-positioning","direction-stack-book","locked-look-grounding"])

add(source_title=S10_T, source_file=S10_F, author=S10_A,
    domain="taste",
    concept="Tourist mode · positioning as the outsider entering an established field",
    summary="Abloh frames his entire practice as the position of the tourist entering an established field. The tourist asks 'why are things done this way?' where the resident asks 'how should I do them better?' The tourist's questions are productive because they surface assumptions the field has stopped examining. Abloh's claim: most innovation in saturated fields comes from tourists, not from residents.",
    usable_principle="Cultivate the tourist's question deliberately. When entering an established field, do not rush to assimilate. The early questions (which the resident would have stopped asking) are the productive ones. Document them. Use them as the starting points for the work that differentiates.",
    sniped_relevance="BJ's positioning as a Boston-trained engineer working in LA's Black founder culture is structurally the tourist position Abloh names. The Lineage Doctrine (LOCKED 2026-05-12) names the position. Abloh's articulation gives it a productive frame · the tourist is not a deficit, it is the operator's competitive position. Cite when defending the operator's claim to authority in the photography field despite not coming from a photo-school background.",
    direct_quotes=[
        "I am a tourist in fashion. That is my advantage, not my limitation.",
        "Tourists ask better questions than residents because they have not stopped seeing what is strange."
    ],
    tags=["abloh","tourist-mode","lineage-doctrine","outsider-positioning","operator-claim"])

add(source_title=S10_T, source_file=S10_F, author=S10_A,
    domain="operator-doctrine",
    concept="Cheat codes · the documented operational shortcuts for the next generation",
    summary="Abloh's pedagogical move: the cheat code. Rather than gatekeeping methodology, he documents the operational shortcuts publicly so the next generation can skip the friction he encountered. The Core Studio lecture is itself a cheat code · a single document collapsing years of practice into named operational primitives. The lecture's audience is younger operators who will extend the work in directions Abloh will not.",
    usable_principle="Document the operational shortcuts publicly. Gatekeeping methodology slows the field; sharing methodology accelerates it. The operators who share their cheat codes become reference points; those who hoard them become bottlenecks. Choose the reference-point position.",
    sniped_relevance="The Direction Stack book is the SNIPED cheat-code document · the methodology made public so the next generation of operators can extend it. The 9-photographer Art Series, the 8-criteria audit, the 5-pass cull · all cheat codes. Abloh validates the pedagogical stance. Cite him in the Direction Stack book's preface as the canonical model for documented operational generosity.",
    direct_quotes=[
        "I tell people the cheat codes. The cheat codes are not the secret. The work is the secret. The cheat codes just get you to the place where you can do the work.",
        "I want the next generation to start three years ahead of where I started."
    ],
    tags=["abloh","cheat-codes","direction-stack-book","pedagogy","operational-generosity"])

# =====================================================================
# CLUSTER 30 · DUBIEL · AVEDON IN THE AMERICAN WEST + SARTRE · 3 chunks
# =====================================================================
S11_T = "Richard Avedon's In the American West and Jean-Paul Sartre: An Existential Approach to Art and Value"
S11_F = "dubiel_avedon_american_west_sartre.txt"
S11_A = "Richard M. Dubiel"

add(source_title=S11_T, source_file=S11_F, author=S11_A,
    domain="portraiture",
    concept="Avedon's West as existential portrait · Sartre's bad-faith framework applied",
    summary="Dubiel reads Avedon's In the American West through Sartre's existentialism. Sartre's concept of 'bad faith' (mauvaise foi) names the self-deception of treating one's social role as if it were one's essence. Avedon's working-class subjects, photographed against the void backdrop, are stripped of the social role they would normally inhabit. The void forces them out of bad faith · they have no costume, no setting, no script. What remains is the subject confronting their own facticity.",
    usable_principle="The most powerful portraits force the subject out of their performed role. The performed role is the bad-faith costume. The photographer's job is to construct the conditions under which the subject cannot maintain the performance · sometimes via duration (Avedon), sometimes via setting (the void), sometimes via direction refusal (Beckett).",
    sniped_relevance="The Direction Stack 90-second opener, the 4-hour Reset block, the Cultural Doc duration practice · all structural moves toward forcing the subject out of their bad-faith presentation. Dubiel gives the philosophical vocabulary. Document the framework in the Direction Stack book's chapter on direction · 'every founder arrives in bad faith. The session's structural goal is to give them somewhere to land that is not the role.'",
    direct_quotes=[
        "Avedon's West subjects, stripped of context, are forced to confront the question Sartre puts at the center of existence: what am I when I am not my role?"
    ],
    tags=["dubiel","avedon","sartre","existential-portrait","bad-faith","direction-stack-book"])

add(source_title=S11_T, source_file=S11_F, author=S11_A,
    domain="portraiture",
    concept="The look · Sartre's analysis of being seen",
    summary="Dubiel applies Sartre's 'the look' (le regard) · the moment one consciousness becomes aware of being seen by another. In Sartre, this is the foundational structure of self-consciousness. In Avedon's West, the camera operationalizes the look · the subject, photographed, must reckon with being-seen as a constant condition of the session. The 8x10 Deardorf, the open shade, the white paper all amplify the look's pressure.",
    usable_principle="The portrait session is the structural amplification of being-seen. Manage that pressure rather than pretending it is not present. Subjects who are told 'just be yourself' under camera pressure cannot · the look already prevents the naive self-presentation. Direct toward something the subject can do under pressure, not toward an impossible naturalness.",
    sniped_relevance="The SNIPED Direction Stack's body-architecture rule ('direct the body, not the face') is the operational response to the look's pressure. The body can hold a task; the face cannot hold naturalness under direct camera scrutiny. Dubiel via Sartre gives the philosophical grounding. The 90-second opener acknowledges the look explicitly · 'I am about to photograph you, here is what we are constructing' · which paradoxically reduces the pressure by naming it.",
    direct_quotes=[
        "The look is the camera. The camera is the look. Avedon's discipline was to keep the look on the subject long enough for the subject to do something with it."
    ],
    tags=["dubiel","sartre","the-look","direction-stack","body-direction","named-pressure"])

add(source_title=S11_T, source_file=S11_F, author=S11_A,
    domain="taste",
    concept="Value vs valuation · Sartre on the work that creates its own audience",
    summary="Dubiel closes by applying Sartre's distinction between value (what the artist commits to) and valuation (what the audience awards). Avedon's West was poorly valued on release · the artist's value commitment did not align with the audience's immediate valuation. Sartre's existentialism predicts this · the work that creates its own audience necessarily diverges from existing audience preferences. Time aligns value and valuation, but only retrospectively.",
    usable_principle="Distinguish your value commitment from the audience's valuation. Optimize for the value commitment. The valuation will arrive · or it will not · but the value commitment is what produces durable work. Trying to optimize for valuation in the absence of value commitment produces work that ages badly.",
    sniped_relevance="This is the philosophical grounding for the SNIPED Year-10 reverse roadmap and the Direction Stack book's perennial-seller positioning (`intel_perennial_logic.md`). The current audience may not value the work at $1,500 · the value commitment is the floor. The decade arc is the trust that valuation will eventually align with value. Dubiel via Sartre gives the formal defense against discount pressure. Cite in the pricing-decision skill.",
    direct_quotes=[
        "The artist commits value. The audience awards valuation. The two only converge in time. Avedon committed; the West has not yet stopped earning that commitment."
    ],
    tags=["dubiel","sartre","value-vs-valuation","perennial-seller","reset-floor-defense","year-10-roadmap"])

# =====================================================================
# CLUSTER 31 · TALBOT · HERZOG MODERN COLOR · 2 chunks
# =====================================================================
S12_T = "Fred Herzog: Modern Color (journal review)"
S12_F = "talbot_herzog_modern_color.txt"
S12_A = "Jacques P. Talbot"

add(source_title=S12_T, source_file=S12_F, author=S12_A,
    domain="color",
    concept="Herzog's color as restraint · the Kodachrome discipline",
    summary="Talbot's review of the Modern Color retrospective (Equinox Gallery, 2017) emphasizes Herzog's restraint. While Eggleston's color was saturated and structural, Herzog's color was atmospheric and observational. The Vancouver street work from the late 1950s and 1960s used Kodachrome's particular palette · slightly desaturated, with a green-yellow midrange and warm shadows · to record the ordinary in ways that resisted the era's preference for either B&W documentary or saturated commercial color. Herzog occupied a middle register that took decades to be recognized as its own position.",
    usable_principle="Restrained color can be the position, not the weakness. The decision to under-saturate, to occupy the middle register, to refuse both the documentary B&W tradition and the saturated commercial register can be a deliberate aesthetic claim. The risk is the position taking decades to be valued; the reward is durability when fashion shifts.",
    sniped_relevance="The SNIPED locked v3 LUXURY preset operates in a restrained register · quiet luxury editorial, not saturated commercial. Talbot's reading of Herzog's restraint is the closest historical precedent for SNIPED's color discipline. Cite him in the Direction Stack book's chapter on color · the SNIPED palette is in the Herzog lineage as much as the Eggleston lineage, perhaps more so. The Art Series Frame 5 (`art_series_5_fred_herzog.md`) is the operational recreation.",
    direct_quotes=[
        "Herzog's restraint was not a failure to commit to color. It was a different commitment · color as observation rather than color as statement."
    ],
    tags=["talbot","herzog","color-restraint","kodachrome","sniped-palette-lineage","art-series-frame-5"])

add(source_title=S12_T, source_file=S12_F, author=S12_A,
    domain="documentary",
    concept="The late-recognized photographer · 60-year wait between work and audience",
    summary="Talbot documents the timeline gap between Herzog's primary working period (1950s-1970s) and his first major institutional recognition (Vancouver Art Gallery retrospective, 2007 · 50+ years later). The work was made for the photographer; the audience caught up half a century later. The pattern recurs in the medium · the photographer who works against the era's preferred register often waits a generation or two for valuation. The pattern is structural, not anomalous.",
    usable_principle="Building work for the next generation is a viable strategy if the work has internal coherence. The valuation lag is the cost; the durability is the payoff. Plan financially for the lag · the photographer cannot count on the audience arriving during the working life.",
    sniped_relevance="This validates the SNIPED 10-year reverse roadmap (`feedback_repetition_over_novelty.md`) and the Year-10 vision treating the Direction Stack book as the artifact that becomes valued in 2036, not in 2026. Herzog's 50-year gap is the long version of what BJ is building toward. Plan the financial architecture accordingly · the Reset and Op Kit revenue funds the long-arc work that may not be valued during the operator's prime working years.",
    direct_quotes=[
        "Fifty years between the work being made and the work being seen. That is photography's tax on photographers who refuse the era's preferred register."
    ],
    tags=["talbot","herzog","valuation-lag","perennial-seller","year-10-roadmap","financial-architecture"])

# =====================================================================
# CLUSTER 32 · ART BOOK 1994 · FRANK · AMERICANS · 2 chunks
# =====================================================================
S13_T = "The Americans (review · Art Book 1994)"
S13_F = "art_book_1994_robert_frank_americans.txt"
S13_A = "Art Book journal · unsigned"

add(source_title=S13_T, source_file=S13_F, author=S13_A,
    domain="documentary",
    concept="The Americans at 35 years · the canonical re-reading",
    summary="The 1994 Art Book review (35 years after the U.S. publication) reads The Americans as fully canonical. The review's analysis · loose framing as voice, recurring motifs as binding agents, the Kerouac introduction as parallel articulation · had become the consensus reading. The review notes how the original critical hostility now reads as the era's misunderstanding rather than as the book's failure. The retrospective consensus is structural to the book's perennial status.",
    usable_principle="A work's canonical status is decided not at release but in the retrospective re-reading. The reviews written 30-50 years after release carry more weight than the original reception. Plan the work to survive into the retrospective reading. The early reviewers will get it wrong; the later reviewers will not.",
    sniped_relevance="This is the structural validation of the SNIPED perennial-seller positioning. The Direction Stack book's value is decided in 2056, not 2026. The Cultural Doc work's value is decided in the retrospective. Plan accordingly · do not optimize for immediate reception. Cite the Art Book review's casual canonization of Frank as the case study for the time-corrected valuation principle. Document in the perennial-seller logic skill (`sniped-perennial-seller`).",
    direct_quotes=[
        "What looked like failure in 1959 reads in 1994 as the only honest American documentary of the postwar era."
    ],
    tags=["art-book-1994","frank","retrospective-canonization","perennial-seller","direction-stack-book","valuation-time"])

add(source_title=S13_T, source_file=S13_F, author=S13_A,
    domain="documentary",
    concept="The democratization of the photographic book · post-Frank monograph form",
    summary="The 1994 review notes that The Americans inaugurated the modern photographic monograph form · the photographer's body of work as a book-length artifact, sequenced deliberately, with literary apparatus (foreword, captions, sequencing), priced as a serious cultural object. Before Frank, photographic books were either picture albums or technical manuals. After Frank, the photographic monograph became its own genre. Every subsequent serious photo monograph operates inside Frank's invented form.",
    usable_principle="A new artifact form can be invented by a single practitioner with sufficient conviction. The form, once invented, becomes available to the medium. Operators who recognize an open form opportunity (rather than a closed one) can create durable artifacts within it.",
    sniped_relevance="The Direction Stack book is being authored inside the Frank-invented monograph form · sequenced body of work, literary apparatus, serious cultural object. The book is not just text; it is the SNIPED operator's monograph. The 1994 review is the structural model. Document the form decision explicitly · the book is in the lineage of Frank's monograph form, not in the lineage of business books or photography how-to books. The form decision IS positioning. Cite in the book's preface.",
    direct_quotes=[
        "Before Frank, photographic books were either albums or manuals. After Frank, the monograph existed."
    ],
    tags=["art-book-1994","frank","monograph-form","direction-stack-book","form-as-positioning","perennial-grounding"])


# =====================================================================
# WRITE OUTPUT
# =====================================================================
def main():
    with OUT.open("w") as f:
        for c in CHUNKS:
            f.write(json.dumps(c) + "\n")
    print(f"Wrote {len(CHUNKS)} chunks to {OUT}")
    # Quick stats
    sources = sorted({c["source_file"] for c in CHUNKS})
    print(f"Unique source files: {len(sources)}")


if __name__ == "__main__":
    main()
