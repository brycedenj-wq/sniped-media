## series_3 INTAKE DOCTRINE

---

### TOP LESSONS (deduped, ranked by SNIPED signal strength)

**TIER 1: Core Composite Methodology (highest recurrence, highest relevance)**

1. **Non-destructive layer architecture is the professional standard.** Smart objects, adjustment layers, layer masks, and smart filters are the mandatory stack. Destructive edits (rasterizing, merging too early, baking filters) eliminate future client-change flexibility. This is not optional discipline; it is the production baseline.

2. **Lightness/tone matching before color.** Desaturate composited elements to B&W first. If the B&W version holds together, the color version will. Mismatched luminosity is the most visible failure tell in composites.

3. **6-part modular composite workflow (Andre).** Composition assembly > detail populate > ambient/particles/depth > integration via adjustment layers > light effects > color/tone finishing. Nearly every expert-level composite follows this or an equivalent sequence. The order is load-bearing; jumping to effects before integration produces visible failure.

4. **Selection precision matters more than prompt sophistication.** In AI generative workflows, tight, deliberate selections produce better outputs than highly crafted text prompts. Spatial constraints beat word choice every time.

5. **Identity untouched; world variable.** The real subject (face, skin texture, body) is preserved across all composite versions. Hair styling and environment are the variable layers. AI generates the world; the photographer locks the identity.

6. **Color unification via gradient maps and Blend If.** Gradient maps (not curves alone) applied with Color blend mode at reduced opacity are the fastest tonal unification tool. Blend If sliders allow selective blending by tonal zone without destructive masks.

7. **Atmospheric perspective as credibility marker.** Background elements must be more faded, less saturated, and lower contrast than foreground. Haze mimicry distinguishes "integrated" from "pasted." Separate foreground blur / subject sharp / background blur layers are the operational pattern.

8. **Shadow anatomy is non-negotiable.** Umbra (hard core) + penumbra (soft edge) + occlusion contact shadow. All shadows converge toward the horizon line. Shadow size correlates with light source distance. Composites without correct shadows read as fake immediately.

9. **Lighting direction must be locked before assembly.** Flip/rotate elements so shadow direction matches the scene's key light. Harsh studio light with AI outdoor background creates an unresolvable conflict. This constraint informs environment selection upstream, not downstream.

10. **Camera Raw Filter as the unified final grading pass.** Applied as a smart filter on a merged-group smart object, Camera Raw handles vignette, lens blur, color grading, grain, and saturation in one editable, reversible pass. This replaces scattered adjustment layers and is operationally cleaner.

**TIER 2: Technical Tools (high practical value, medium strategic weight)**

11. **Blend modes decoded.** Multiply hides light pixels, shows darks. Screen hides dark pixels, shows lights. Overlay/Soft Light hide 50% gray (used for texture layers). Pass-through vs Normal on groups: pass-through lets adjustments leak outside; normal confines them. Keyboard Shift+Plus/Minus cycles through blend modes for rapid preview.

12. **Curves vs Levels.** Functionally equivalent for basic tonal control. Curves advantage: infinite point placement for granular sculpting beyond Levels' three fixed anchors. Per-channel work (Red/Green/Blue independently) enables color temperature shifts and creative toning without global hue contamination.

13. **Median Stack Mode removes transient elements.** File > Scripts > Statistics > Median with 14+ tripod-stabilized frames removes moving people and non-constant pixels. Stationary subjects persist; shoot 20-30 seconds apart and monitor for standing groups. Post-stack: spot heal residual artifacts plus rebuild cloud/sky layers if ambient elements drifted.

14. **Generative Fill reliable use cases vs unreliable.** Sky replacement, background extension, object removal, and reflections are reliable. Hair, jewelry, hands, and facial features require 3-5 trials and are often unusable without manual cleanup. Blank prompt triggers context-aware removal; descriptive prompt triggers generative insertion.

15. **AI object insertion is expensive and inconsistent.** Partner models (Flux 2 Pro, Gemini 3 Nano Banana Pro) cost 20-40 credits per variation and often produce unusable results. The honest operator reality: generative fill for world-extension is practical; generative fill for adding complex objects is a coin flip.

16. **Frequency separation retouching** separates texture layer from color layer; enables skin smoothing while preserving 100% texture detail. Not dependent on AI; stable professional technique.

17. **Halo removal via layer math.** Command-click mask > Filter > Other > Minimum (1px to shrink) > invert selection > paint black on mask edges. Removes fringe artifacts without rebuilding the mask from scratch.

18. **Gray card + eyedropper white balance.** Capture 18% gray card on set. Use eyedropper in Camera Raw for consistent white balance across an entire shoot batch. The most precise white balance tool available.

19. **Dodge and burn via adjustment layers + masks (not dodge/burn tools).** Group subject-selection mask over dodge/burn adjustment layer stack. Avoids brush artifacts. Non-destructive, fully reversible, and scalable to retoucher onboarding.

20. **PSDT template format for shared workflows.** Renaming PSD to PSDT prevents direct edits to master; opening PSDT creates untitled copy. Applicable to scale operations and retoucher handoffs.

**TIER 3: Content Strategy and Distribution (2 segments, distinct from the Photoshop corpus)**

21. **Script pacing: 2-1-3-4 method (Callaway).** Best point is second (not first), second-best is first. Escalating value trains viewers to stay. Diminishing value trains them to leave. Music album structure precedent: best songs in slots 3-4.

22. **Expectations vs Reality is the retention engine.** First lines must confirm AND exceed the title's implied promise. Click confirmation (beat what you promised to deliver) is the opening job.

23. **Value Loop per body point.** Each content point needs: (1) context/explanation, (2) application/examples, (3) framing for why it matters to the larger argument. Missing step 3 produces unmemorable content.

24. **Common belief + contrarian take as intro structure.** (1) immediate context, (2) establish common belief, (3) state contrarian approach to create contrast, (4) proof, (5) plan. This structure is load-bearing for authority-building content (Direction Stack, LinkedIn POV).

25. **Native CTA embedding.** Integrate calls-to-action as natural extensions of a solved pain point. Standalone CTAs feel promotional; embedded ones feel helpful.

**TIER 4: Audio Production (1 segment, lower weight)**

26. **Two-compressor audio chain: Expander + Peak Limiter separately.** Single dynamics processor cannot handle breath/room noise AND peak ceiling simultaneously without artifacts. Expander (slow attack) reduces floor; Limiter (fast attack, hard ceiling) protects peaks.

27. **Platform-specific loudness targets.** YouTube: -14 LUFS, true peak -1 dBTP. Manual processing produces smoother dynamics than Premiere's export auto-normalization (which peaks music intro and tapers dialog end).

---

### SOURCE INVENTORY

**Primary corpus: Photoshop compositing tutorials (32 of 37 substantive segments)**

- PHLEARN / Aaron Nace: "30 Days of Photoshop" multi-day series (Days 1-21+ documented); "Advanced Compositing for Brands Photography and Type"
- Photoshop Training Channel / Jesus (JR) Ramirez: compositing livestreams, bootcamp, course promo
- Adobe Live: compositing bootcamp, Firefly integration streams (hosts: Jack, Emily, Ted, Ellie)
- Andre (instructor since 2009): "Advanced Fantasy Artwork" 6-part composite workflow
- Nor Arts channel ("N"): "Stranger Things inspired poster" compositing, "Create a Design Step by Step," product mockup tutorials
- PiXimperfect: "7 Signs of a Photoshop Pro," vibrance vs saturation tutorial
- John Whitehead Images: MSI Competition composite + portrait retouching tutorial
- Nathaniel Dodson / TutVid.com: full Photoshop compositing tutorial
- JRfromPTC: compositing course promo (Stack Mode / Median workflow highlight)
- Dansky (Daniel White): "Advanced Photoshop Techniques for Album Artwork"
- Terry White: Adobe Photoshop 27.6 release features walkthrough (April 2026)
- Julieanne Kost (Adobe Digital Imaging Evangelist): Adobe Creative Cloud compositing philosophy segment
- Russell Preston Brown: Firefly generative fill use cases tutorial

**Secondary corpus: content strategy (1 segment)**

- Callaway (YouTube): "How to Write Killer Scripts That Keep Viewers Hooked"

**Tertiary corpus: non-photography (3 segments)**

- "How to Sell Your Screenplay" (screenwriting career pathway)
- AlphaGo documentary (DeepMind, Go AI training)
- Premiere Pro plugins review (Gavin Herman): Smoothify, Excalibur, Neat Video, Boris Sapphire, 20+ plugins

**Audio production (1 segment)**

- "Why God Why Podcast" production workflow; Premiere Pro audio mixing, compressor techniques, loudness normalization (ITU-1770-3)

**Premiere Pro video editing basics (1 segment, empty of strategic value)**

- Hallease (filmmaker, Atlanta): Premiere Pro workspace orientation, panel definitions

---

### SNIPED-RELEVANT EXTRACTS

**Composite Environment Rotation operations:**
- The 6-part modular workflow (seg 4) is a lockable SOP for Chapter Card and HERO post production
- Gradient map tonal unification + clipping adjustments (segs 7, 27, 35, 36) are the color-unification engine specifically named for making synthetic elements read as one photograph
- Sky Replacement and Generative Expand validated as AI accelerants for environment construction, not identity risk (segs 32, 30)
- Median Stack Mode (seg 20) is a directly applicable tool for removing location crowds from SNIPED composite environment backgrounds

**Edit Register Bifurcation (identity untouched, world variable):**
- Segs 25, 31 explicitly confirm: restored identity from original photograph beats pristine AI generation. Masking discipline returns subject features even after AI modification.
- Harsh lighting is AI's documented failure mode (seg 25): shadow direction cannot transfer naturally when changing environments. This constrains SNIPED's environment rotation: fixed lighting per environment, subject light direction must match or be artfully motivated.
- Frequency separation keeps texture (identity) separate from color layer (variable); applies to both portrait retouching and composite finishing.

**Strongest photograph != most processed (gate validation):**
- Segs 31, 7 confirm selection discipline and color-matching fundamentals (curves, dodge-burn, clone) are the actual moat, not AI model capability. AI fill is a 2-hour shortcut; manual retouching foundation is non-negotiable.
- Halo removal and mask quality checks (segs 36, 25) are the QA layer that distinguishes SNIPED output from vending-machine output.

**Luxury Editorial visual direction:**
- Texture down (softer clarity) + small opacity values + Camera Raw restraint = the editorial finish, not volume (segs 6, 8, 20)
- Atmospheric perspective + haze mimicry specifically mentioned as "the difference between pasted and integrated" (seg 5)
- Channel-specific color grading (per tonal zone, not global hue push) repeatedly validated as the correct method for SNIPED's Meisel/Roversi lane (segs 6, 7, 14, 16, 17)

**Production efficiency wins:**
- AI depth masking, Distraction Removal, Rotate Object, Harmonize, and automated layer naming (Photoshop 27.6, seg 30) reduce composite production time meaningfully
- Smart object linked instances: edit source once, all instances update (segs 2, 25)
- PSDT template format distributes master files without risk of source mutation (seg 26)
- LUT/preset export as a distribution model for grading consistency across library; potential teachable product (seg 19)
- Actions panel batch processing (seg 30) enables gallery-level consistency across shoot outputs

**Content strategy (Direction Stack, LinkedIn):**
- 2-1-3-4 body pacing and value loop structure (seg 24) are directly applicable to SNIPED Card caption sequencing and short-form motion IG
- Common belief + contrarian take intro structure (seg 24) maps onto Direction Stack positioning and LinkedIn authority posts
- "Saying things nobody else says is the moat" (seg 24) reinforces lineage-specific POV as competitive differentiator

**Easter egg / authorial signature:**
- Seg 13: hidden signature element in every composition adds authorial voice and encourages audience replay. Mirrors SNIPED's Lineage Doctrine (work documents from inside the lineage). Operationalizable as a recurring visual or contextual marker embedded in Chapter Cards.

---

### ANYTHING NEW NOT ALREADY IN SNIPED DOCTRINE

The following items have meaningful signal and are not yet codified in the OS:

**1. Two-compressor audio chain as doctrine for Cultural Doc / podcast audio.** Expander + Limiter separately, with platform-specific LUFS targets. If Direction Stack Cultural Doc includes any spoken-word or voiceover component, this is the production standard. Not currently in SNIPED audio doctrine.

**2. Median Stack Mode as a crowd-removal tool for composite backgrounds.** Tripod + 14+ frames + File > Scripts > Statistics > Median. Removes location-crowd noise from architectural or urban environments. This is a specific, repeatable technique for SNIPED's Composite Environment Rotation that currently has no named method in the OS.

**3. Rotate Object feature (Photoshop 27.6) as a perspective correction tool.** Studio subjects shot at different angles can be re-oriented to match scene perspective without quality loss. New as of April 2026 release. Reduces the manual transform-and-blend workaround.

**4. Harmonize feature (one-click, Photoshop 27.6)** auto-corrects skin tones, lighting, shadows, and reflections in composites to match environment context. Saves manual retouching time on subject-environment integration. Not yet in SNIPED composite SOP.

**5. AI layer naming and cleanup (Photoshop 27.6).** Auto-detects content and renames Layer 1/2/3 to semantic names, removes empty layers. Small but operationally meaningful for a multi-layer composite workflow under time pressure.

**6. LUT export / branded preset creation as a future product or cohort tool.** Seg 19 documents generating 3D LUTs from Camera Raw workflows, exporting for library-wide consistency. Potential revenue surface (sellable presets, grading cohort) not currently addressed in SNIPED's product architecture.

**7. Callaway 2-1-3-4 pacing method.** Not referenced elsewhere in SNIPED OS content strategy doctrine. The escalating value body structure (second-best first, best second) is a specific, actionable content architecture that the OS does not currently have.

**8. "Astronaut as universal subject" design principle (seg 9).** Gender/race/sexuality-neutral subject allows viewers to project into the narrative. Applicable to Direction Stack visual abstraction when SNIPED works with brand/product clients rather than individual portrait subjects.

**9. PSDT template format for retoucher or client handoffs.** Operational gap: SNIPED has composite methodology but no documented file-format protocol for distributing masters without source mutation risk.

**10. Distraction Removal expanded scope (Photoshop 27.6).** Now covers poles, barriers, potholes, urban elements, dust/spots beyond people/wires. Directly speeds up location shoot cleanup on SNIPED's urban environments.

---

### COVERAGE NOTE

- Segments read OK: 35 of 38 (segs 1-22, 24-37)
- Segments partial: 2 (seg 16: transcript end reached mid-segment; seg 19: file output truncated at end; seg 32: source header not visible in extracted window)
- Segments EMPTY: 1 (seg 38: Premiere Pro UI boilerplate only, no extractable lessons)

Total: 35 OK / 2 partial / 1 EMPTY across 38 segments.

---

*This is a research intake distillation. No lane crowned. No strategic direction locked. Findings are evidence, not authority.*