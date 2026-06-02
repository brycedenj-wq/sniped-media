# AI Image Tools · Tactical Extraction for SNIPED

Source: `/99_VAULT/_intake_archive_2026-05-12/chat images .docx`
Distilled: 2026-05-12

Coverage: background removal landscape · Nano Banana Pro deep dive · ChatGPT image gen 12 tips · tool-to-task matrix.

---

## Tool-to-task matrix · USE NOW

| Task | Tool | Why |
|---|---|---|
| Background removal (utility) | Remove.bg | Best hair edge preservation, 5-sec turn |
| Background removal in design context | Canva | Skip round-trip if mocking up in Canva |
| Object removal / cleanup (quick) | Cleanup.pictures (free) | Faster than Photoshop Spot Heal for one-off |
| Subject extraction (fashion-tier) | Photoshop Select Subject + Refine Edge | Still the ceiling for hair. Do not replace. |
| Background plate (atmospheric/studio extension) | **Seedream 5.0 Lite** | See [[SEEDREAM_TACTICAL_EXTRACTION]] |
| Background plate (narrative urban) | Nano Banana Pro (via Gemini) | Detailed scene reasoning, `$f/2.0$` syntax for realism |
| Identity-preserving subject placement | **Nano Banana Pro** | Best likeness preservation per testing |
| Brand board / persistent style sheet | ChatGPT (Memory feature) | Style consistency across sessions |
| Multi-perspective from one image | ChatGPT Tip #7 | 3/4 view, profile, back generation |
| Style transfer between SNIPED frames | Seedream 5.0 edit model | Color/lens transfer with reduced hallucination |
| Iterative refinement of a comp | ChatGPT Tip #10 (art director mode) | Conversational refinement, no prompt rewriting |
| Reverse-engineer a reference image's prompt | ChatGPT Tip #3 | Drop reference in, get prompt out |

---

## ChatGPT image gen · the 6 tips that matter for SNIPED

The doc covers 12 tips total. The 6 that apply directly to SNIPED hero composite work:

### Tip #1 · The 8-Element Prompting Framework
Order every prompt: subject → context → composition → lighting → style → camera → mood → constraints.

### Tip #3 · Image-to-prompt reverse engineering
Drop a reference image into ChatGPT, ask for the prompt that would generate it. Steal what works, run it through Seedream or Nano Banana with SNIPED tweaks.

### Tip #6 · Adding elements to existing images
Upload current image, prompt the addition (atmosphere, props, depth). Watch for identity shift on subject · decline if face changes.

### Tip #7 · Multi-perspective image generation
Generate the same scene from 3/4 view, profile, back. Useful for IG carousel where one frame becomes 3-5 angled variations of the same world.

### Tip #10 · Iterative chat loop editing (art director mode) · LOAD-BEARING
Treat ChatGPT as an art director: "make the light warmer," "pull back left shadow," "increase grain." Avoids prompt rewriting. Best for plate refinement before download.

### Tip #12 · Multi-scene storytelling
Multiple images at once with consistent character/style. For IG carousels where 3-5 frames share a visual world.

The other 6 tips (brand boards, logos, brand avatars, style transfers, image expansion, Meta ad creative) are situational · skip until needed.

---

## Nano Banana Pro · the 3 chapters that matter

### Likeness Preservation
Best-in-class for identity-preserving composites per source's testing. Beats Seedream 5.0 (which has three-hands issue) and ChatGPT image gen.

**SNIPED USE:** when yae's identity MUST hold and atmospheric scene placement is needed. Upload Evoto TIFF, prompt scene addition with explicit identity-hold language.

Prompt template (luxury direction):
```
Preserve subject identity exactly: face, hair texture, skin tone palette #B8956E, body proportions.
Place subject in [scene with palette #2A2A2E #C9B7A3 #F5EFE6].
Mamiya 7 depth of field, Kodak Portra 400 grain, $f/2.8$ photographic realism.
Loewe campaign aesthetic. Do not modify identity.
```

### Photo Blending & Design Mixing
Two images → one. Layer SNIPED subject into a generated plate without Photoshop. Output quality depends on prompt clarity about what to keep from each source.

### Multi-Turn Editing
Iterative refinement like ChatGPT Tip #10. Edit, see result, edit again. No prompt rewriting between turns.

### Nano Banana failure modes
- Three-hand artifacts (less frequent than Seedream 5.0)
- Smooth CGI on portraits (combat with film camera cheat codes)
- Background plate prompts: use `$f/2.0$` dollar-sign syntax for photographic realism

---

## Background removal · the actual ranking

For your subject extraction needs in Track B Step 5.3 you have Photoshop Select Subject. The ranking below is for utility one-offs:

1. **Remove.bg** · best quality, hair edge preservation
2. **Canva** · best workflow integration if already designing in Canva
3. **Photo Leap** · mobile-first, fine for IG Stories
4. **Adobe Express** · free, surprisingly good

Photoshop Select Subject + Refine Edge brush remains the ceiling for fashion-tier hair. Don't replace.

---

## What's NOT in SNIPED's stack from this source

Tools mentioned but skip for now:
- **Blueberry AI** (asset management) · Notion DB covers this for SNIPED at current scale
- **Waifu 2x** (upscaling) · Topaz Photo AI is locked already

---

## Lite hero composite workflow · using these tools

Bypasses ~80% of the Photoshop assembly in `track_b_frame_walkthrough.md` Step 5.

| Step | Tool | Time |
|---|---|---|
| 1. LR develop + AI mask stack + Generative Remove | Lightroom Classic | 10 min |
| 2. Evoto skin pass | Evoto | 5 min |
| 3. Generate plate OR composite directly | Seedream 5.0 Lite (plate) OR Nano Banana Pro (full composite) | 10-15 min |
| 4. Identity check on output | Manual eye | 2 min |
| 5. Light Photoshop pass (edge cleanup, hair flyaways only · no Harmonize ceremony) | Photoshop | 10 min |
| 6. Re-import LR, apply v3 LUXURY, export | Lightroom | 5 min |
| **Total** | | **~45 min** |

vs. Track B walkthrough's 60-80 min for first frame, 40 min for subsequent. The lite lane trades Photoshop control for AI assembly speed. Use for IG hero composites where ceiling is "Loewe campaign IG" not "Direction Stack book frame."

---

## Cross-references

- `/05_PRODUCTION/track_b_frame_walkthrough.md` · the full Photoshop assembly (ceiling lane)
- `/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md` · Seedream-specific deep dive
- `/00_BRIEF/PRODUCTION_OS.md` Section 4.4 · existing AI tool stack (pending update to incorporate these)
- Memory: `[[sniped-visual-direction-luxury-editorial]]` governs all prompts
- Memory: `[[feedback-edit-register-bifurcation]]` defines identity rules (face/body/skin untouched)
