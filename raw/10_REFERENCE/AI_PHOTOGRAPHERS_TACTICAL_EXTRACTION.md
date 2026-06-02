# AI Photographers · Tactical Extraction Map

Source: `/Users/sniper/Downloads/AI PHOTOGRAPHERS.docx` (12,372 lines, 62,847 words · multi-creator video transcript collection covering AI image generation, AI compositing workflows, and AI vs analog photography market positioning).

Treatment: tactical workflow + market intelligence. NOT new strategy. The doc resolves one specific load-bearing question SNIPED has been wrestling with: **how to push studio captures into editorial / cinematic / compositing territory without breaking the anti-AI client moat.**

The answer is documented as a working professional pipeline. It validates and refines the Track B creative push lane already established in the prior post-process recommendation.

Classification rule: keep what extends the existing maker-led methodology. Refuse anything that generates the subject or replaces the photographer's eye.

---

## USE NOW · 4 items

### 1. The John Gress NFL Trading Card Compositing Playbook

**Source:** AI PHOTOGRAPHERS.docx lines ~4880-5500.
**Pattern:** John Gress (working pro · 8 years shooting NFL/NBA rookie cards) documents the exact compositing workflow for taking a real-subject studio shot and placing it into a generated cinematic environment. This IS the Track B creative push playbook articulated by a working professional.

**The 5-step workflow:**

1. **Capture** · real subject in studio, multi-light setup (clamshell + back rim + hair light for the John Gress recipe). Shoot RAW. The subject is real. The photographer is present. Methodology runs first.
2. **Lightroom develop** (or Capture One in Gress's case) · base process at high contrast, modest crop, no heavy color grading yet. TIFF export.
3. **Evoto skin retouch** · light pass · blemish removal, dark circles, gentle wrinkle reduction. NOT beauty-tier retouch. 1-3 seconds per image with locked preset.
4. **AI background plate generation** · Firefly for soft-focus cityscapes, Malibu beaches, atmospheric backdrops. Midjourney (or Nano Banana Pro · see item 2) for stadium scenes, tunnels, structured environments. Generate at the highest available res. Be aware they output ~1000-1500 px and need upscale.
5. **Photoshop assembly** · the load-bearing layer:
   - Open retouched subject as Smart Object linked file
   - Crop to 16:9 or composition target
   - Drop background plate, transform/upscale to fit
   - Remove background on subject (Select Subject → Mask)
   - Refine hair selection (Select and Mask · Refine Edge brush · then Overlay-mode brush along hair edges to firm translucent areas)
   - Run Neural Filter Harmonize (sample from background, scale to 50-75% strength)
   - Add colored edge-light layer (cyan/blue/whatever color matches background highlights, painted on duplicated subject mask, blend mode Overlay, blend-if to mid-tones and highlights)
   - Add unifying grain layer (gray fill at L=50, blend Overlay, Filter > Noise > Add Noise)
   - Add color-wash layer (cyan tone painted full layer, blend mode Color, opacity ~5%)
   - Add darkening exposure adjustment with face masked out (draws eye to face)
   - Enhance catchlights (small white brush on eye highlights, Overlay blend)

**Maps to:**
- `/00_BRIEF/PRODUCTION_OS.md` Section 4.1 (AI routing) · add background-plate workflow
- The 36-finals batch from last weekend (the Track B creative push set · 6-12 frames)
- Future Brand System tier deliverables where the client wants editorial register
- Op Kit tier when the founder requests location context they were not actually shot in

**Improves:** quality (Brand System tier register on a studio capture) + portfolio strength + visual signature ceiling lifted

**Critical guardrails (Berger / Sax line absolute):**
- Subject is always real. Always shot in studio. Always run through Direction Stack methodology. Never AI-generated.
- Background plate is utility · the maker chose what to show, what to integrate, what to harmonize. The plate alone is not the work.
- Disclosure norm for client work: if the composite places the subject in a location they were not actually in, the client must explicitly approve the editorial register before delivery. Reset clients get studio register only · no surprise composites.
- For SNIPED's own portfolio / case studies / VIB assets / LinkedIn POV: composites are clearly framed as "Brand System tier composite work · subject shot in DTLA studio, environment composited."
- For Cultural Documentation: NEVER. Cultural Doc is taken-image documentary. Composites would falsify the archive.

**Action this week (with last weekend's 36 finals):**
- Pick 6-12 Track B creative push candidates per the prior recommendation
- Run through the 5-step Gress workflow on those frames only
- Output becomes portfolio update + LinkedIn POV case study + IG carousel + VIB asset proof

### 2. Google Nano Banana Pro for background plates (replaces or supplements Midjourney)

**Source:** AI PHOTOGRAPHERS.docx lines ~5860-6700.
**Pattern:** Nano Banana Pro (accessible via Gemini, Freepik, or direct API) is currently the highest-realism AI background generator with structured prompting support. Better than Firefly for narrative scenes. Better than Midjourney for photographic plausibility.

**Two prompt techniques worth using:**
- **Structured prompt:** define camera, lens, f-stop (use `$f/2$` syntax · the dollar signs improve realism), ISO, lighting (window soft, golden hour, etc.), subject placement, environment specificity. The more specific the camera-and-light spec, the more photographic the output reads.
- **Reprompting:** drop a real reference photo into Gemini, ask it to write the prompt that would generate that image, then edit the prompt for the new scene. Generates internally consistent "shot on" context.

**Maps to:** PRODUCTION_OS Section 4.1 AI routing · alternative to Firefly/Midjourney for narrative background plates

**Improves:** quality of generated backgrounds (more photographically plausible) + speed (no fighting Midjourney's stylization)

**Action:** swap or supplement Firefly with Nano Banana for background generation when the scene needs cinematic narrative weight (stadium, hotel suite, rooftop, urban tunnel). Keep Firefly for the fast-and-cheap atmospheric backgrounds (cityscape bokeh, beach, color wash). Document the prompt convention in the Photoshop comp workflow.

### 3. Tony Northrup's pre-visualization workflow (upgrades the Leonardo moodboard recommendation)

**Source:** AI PHOTOGRAPHERS.docx lines ~9200+.
**Pattern:** before a shoot, drop the founder's existing photos into Gemini, prompt different visual treatments (location, lighting, lens, register), get a preview deck of how the founder would look in different scenarios. Use this for the Direction Stack pre-shoot alignment call.

**Maps to:**
- Direction Stack pre-shoot Protocol 2-3 (the alignment phase before shoot day)
- Replaces or supplements the prior Leonardo AI moodboard recommendation
- Op Kit / Brand System scoping calls (founder sees frames before the shoot)
- VIB DM 4 (the "here's what we'd actually make" tease)

**Improves:** quality of pre-shoot communication. Founders understand frames they've previewed, not frames described in words.

**Critical guardrail:** SAME absolute rule as before. Pre-visualization is INTERNAL alignment / scoping only. Never delivered. Never published. Never represented to the founder as "this is the shoot output." It is "this is what we are aligning to · you'll see the actual frames after the shoot."

**Action:** test Gemini reprompting against 2-3 prior shoots BJ has done. Compare to Leonardo Blueprints. Keep whichever produces more useful direction-confirmation frames. Document in PRODUCTION_OS Section 4 AI routing.

### 4. Photoshop Neural Filter Harmonize (the silent compositing unlock)

**Source:** AI PHOTOGRAPHERS.docx Gress workflow + multiple supporting examples.
**Pattern:** Photoshop's Neural Filter Harmonize is the "make this composite not look fake" button. It samples a target layer (background) and adjusts the source layer (subject) to match contrast, color temperature, and tone. 75% strength default, scale per-image. This is what separates "Photoshop comp that looks like a comp" from "Photoshop comp that reads as a real photo."

**Maps to:**
- The Photoshop step in the Gress workflow (item 1)
- Any prior Photoshop comp work being done · this filter alone elevates output

**Improves:** quality (composites stop reading as composites) + time (replaces 5-15 min of manual color matching)

**Action:** use it as the standard step in the Track B creative push workflow. Before manual color matching, run Harmonize. Then refine.

---

## DELAY · 2 items (revisit at Brand System tier trigger)

### 1. Enhancor.ai for fixing AI skin texture
Only relevant if SNIPED ever generated AI portraits. SNIPED does not. The skin moat is real subjects, real shoots, real Evoto. Hold for the day this becomes false (it won't).
**Trigger:** never · revisit only if SNIPED's anti-AI moat is intentionally retired (and it should not be).

### 2. AI image generation upscaling workflows (Magnific, Topaz Gigapixel, Photoshop neural super-zoom)
Useful only for upscaling AI-generated background plates. Right now the use volume does not justify subscriptions beyond Topaz Photo AI (already in the stack). Revisit if Track B creative push volume hits 20+ composites/month.
**Trigger:** Track B compositing workflow becomes a regular pipeline (not just collab portfolio one-offs).

---

## IGNORE · the off-positioning bulk

These would actively collapse the SNIPED moat. Refuse despite curiosity.

- **Astria.ai (training AI on your own face from 11 reference photos).** Generates fake portraits of yourself in any setting. Direct collapse of the maker-led methodology. Off-positioning entirely. Never for SNIPED, never for clients.
- **Curious Refuge "How to generate the most realistic AI portraits."** Generating subjects from scratch. Anti-Berger. Anti-Sax. Anti-SNIPED.
- **AI face / body / subject generation in any tool (Midjourney, Imagen, Reve, Flux, Sora for subjects, etc.).** Same.
- **AI auto-headshot services as a deliverable.** The 4-camp memo predicts the cheap tier collapses first. SNIPED is the premium tier, defined by refusal of that path.
- **Reverse-prompt-from-real-photo for subject generation.** Reprompting is fine for backgrounds (item 2). For subjects it is identity theft of the photographic relationship.
- **AI replacing Photoshop wholesale.** Photoshop is the assembly layer. AI generates inputs. The "Photoshop tutorials are 3 years old" observation in BJ's voice notes reflects that Photoshop's CORE didn't change · only the input sources did. Photoshop assembly skill is more valuable now, not less.
- **Faceless AI YouTube channels, AI influencer accounts, AI model agencies.** Off-positioning entirely. Wrong ICP, wrong register.
- **Generic AI prompt-engineering hype content.** Already covered in the Udemy AI extraction. Refused once, refuse again.
- **AI lead-gen videos using AI talking-head avatars.** Erodes BJ's reputation if associated. Refuse.

---

## MARKET INTELLIGENCE · 1 high-signal validation

### Sarah Petty's positioning thesis (validates the SNIPED moat)

**Source:** AI PHOTOGRAPHERS.docx lines ~8500+.
**Quote (paraphrased):** "AI will not replace boutique photographers. It will replace photographers who act like vending machines. If your client experience can be done by AI, you don't have a moat. Educate clients that they don't know what to ask when they call you."

**Why this matters for SNIPED:**

This is a working photographer (Sarah Petty · pricing coach + portrait photographer) articulating, in plain language, the exact positioning SNIPED has built from Berger / Sax / Win Without Pitching. It is independent confirmation that the moat is real, that the language ("vending machine" vs "boutique") tracks, and that the strategy of education-of-buyer is correct.

**For SNIPED operationally:**
- Validates the Direction Stack methodology as the moat (not just craft)
- Validates the 90-second on-set opener as the experience moat
- Validates the DTLA studio anchor as the analog premium
- Validates the refusal of generic / commodity work
- Validates the educate-don't-justify pricing posture

**Where to use the language:**
- Carrd "what is SNIPED" copy: "We are not a vending machine."
- LinkedIn POV when the AI conversation surfaces: the vending-machine line is a clean rhetorical handle
- Op Kit MSA preamble: implicit framing of SNIPED as boutique, methodology-led
- Founder-buyer conversation: "If your headshot can be done by AI, you don't need us. If you want a methodology that compounds, you do."

This is being saved as an intel memory (`intel_ai_photographer_market.md`) for future strategic recall.

---

## BJ's voice question · direct answer

> "Should I just go full AI for backgrounds and skip Photoshop? The Photoshop tutorials are 3 years old and there's nothing new."

**Answer:** No. Photoshop is not dying. It is the assembly layer. AI generates inputs · backgrounds, atmosphere, plates · and Photoshop blends them into the real-subject capture. The Photoshop skill being asked of you in 2026 is not "build the entire image from scratch in Photoshop" (which is the 2010 skill that hasn't changed). The 2026 skill is: blend an AI-generated background into a real-subject capture so the seam reads as photographed reality. Harmonize, edge-light, grain, color-wash, exposure-mask. That is what John Gress is doing for trading cards. That is what the Brand System tier is for SNIPED.

**For the 36 finals from last weekend:**
- 24-30 frames: Track A floor · standard SNIPED studio register, clean Lightroom + Evoto, deliver to models.
- 6-12 frames: Track B ceiling · Gress 5-step playbook. AI background plate (Firefly or Nano Banana). Composite in Photoshop. Output is portfolio + LinkedIn POV + VIB asset.

**On Jermaine's bottom-line framing:** "best pictures ever" as the rubric is the right judgment frame. Compare blind against the all-time greats (Avedon, Leibovitz, Eggleston, the Art Series references already in `/09_ART_SERIES/`). The floor goes up. Then add ownership · the methodology, the studio, the LA founder cluster · so the work is comparable AND yours. This is consistent with the Blockbuster strategy memory (bet big, distribution dominates) and the analog premium memory (real maker, real tools, premium tier).

The compositing question was never about Photoshop dying. It was about whether SNIPED has permission to push the editorial ceiling. The answer is yes, on the Track B set, with the Gress playbook, with the moat preserved.

---

## Single integrated instruction

**Real subject + AI background plate + Photoshop assembly = the Track B creative push playbook.** The methodology runs first. The capture is real. The compositing is maker-led. The AI tools (Firefly, Nano Banana, Leonardo) are utility behind the methodology, not in front of it. Sarah Petty's "vending machine vs boutique" line is the buyer-education handle. The 36 finals from last weekend become 24-30 Track A floor + 6-12 Track B ceiling. Photoshop is not dying · it is the assembly layer that makes the AI inputs cohere into a photograph. Refuse AI-generated subjects absolutely. Apply AI backgrounds with Gress's 5-step discipline. Ship the Track B set as portfolio, not as client surprise.
