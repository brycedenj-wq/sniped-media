# Seedream 5.0 · Tactical Extraction for SNIPED

Source: `/99_VAULT/_intake_archive_2026-05-12/Seedream 5.0.docx`
Distilled: 2026-05-12

ByteDance image gen model with real-time web search + multi-step reasoning + HEX color control. Released February 2026 (Lite version). Available via fal.ai API and direct ByteDance.

---

## When to use Seedream vs alternatives

| Use case | Best tool | Why |
|---|---|---|
| Background plate generation (luxury editorial) | **Seedream 5.0 Lite** | HEX palette control + camera-name cheat codes + less filtered than Nano Banana |
| Subject-preserving composite (identity must hold) | **Seedream 4.5** | Better face preservation than 5.0; 5.0 has "three hands" artifact issue |
| Style transfer between SNIPED frames | Seedream 5.0 edit model | Color/lens transfer with reduced hallucination |
| Brand color exact match | Seedream 5.0 with HEX in prompt | Drop `#2A2A2E` and it actually uses it |
| Identity-required portrait composite | Nano Banana Pro (NOT Seedream 5.0) | See [[ai-image-tools-tactical-extraction]] |

---

## The 6 prompting tricks (the load-bearing techniques)

### 1. HEX color codes work directly

Drop hex values in the prompt, the model uses the exact color. For SNIPED v3 luxury direction use this locked palette:

| Role | HEX | Use in prompt |
|---|---|---|
| Deep shadow | `#2A2A2E` | "shadow palette #2A2A2E" |
| Cool shadow accent | `#3D4B5C` | "cool shadow accent #3D4B5C" |
| Mid skin tone | `#B8956E` | "skin retention #B8956E" |
| Mid environment | `#C9B7A3` | "muted mid palette #C9B7A3" |
| Cream highlight | `#F5EFE6` | "cream highlight #F5EFE6" |

### 2. JSON structured prompting

Pass entire prompt as JSON for multi-subject placement, per-element color, exact positioning. Useful for layered scenes with precise control.

### 3. Language affects visual style

Write prompt in French → output looks more French (architecture, light, vibe). Tested across 12 languages. **SNIPED USE:** for European luxury editorial register, write prompts in French. Italian for Mediterranean editorial. Japanese for minimalist luxury.

### 4. Quotation marks for text rendering

Any text in the image goes in quotes. Without quotes, words read as descriptive keywords.

### 5. Camera names as cheat codes · the most important trick

The model knows what these look like:

| Cheat code | Effect | When to use |
|---|---|---|
| "Mamiya 7" | Medium format depth of field | SNIPED default for luxury editorial |
| "Hasselblad H6D" | Digital medium format clinical | High-end fashion campaign register |
| "Kodak Portra 400" | Warm film tones + grain | SNIPED locked grain register |
| "Fuji 400H" | Cooler editorial cleanness | Alternative grain register |
| "Sergio Leone composition" | Wide composition with negative space | Architectural / environmental plates |
| "ARRI Alexa" | Cinematic | AVOID for SNIPED · reads cinematic cliche |

**SNIPED default combo:** "Mamiya 7 medium format, Kodak Portra 400 grain"

### 6. Real-time web search toggle

ON for current events, public figures, news content. OFF for stable output. **SNIPED usage:** OFF · we're not making news graphics.

---

## SNIPED prompt templates (locked to v3 luxury direction)

### Template A · Studio extension atmosphere
Use when you want to keep yae in the studio but add atmospheric depth.

```
Editorial fashion background plate, dark luxury studio environment,
deep restrained shadows palette #2A2A2E #3D4B5C,
warm spill from upper-right palette #B8956E,
dust motes in air, atmospheric haze,
16:9 horizontal, no people, no subjects, photographic realism,
shot on Mamiya 7, Kodak Portra 400 grain,
Loewe campaign aesthetic, Paolo Roversi reference,
quiet luxury restraint, no cinematic theatrics
```

### Template B · Urban quiet luxury

For when scene needs to leave studio.

```
Background plate, downtown Los Angeles street at dusk,
muted luxury palette #2A2A2E #C9B7A3 #F5EFE6,
no neon, no motion blur, no theatrics,
soft diffused light from upper left, deep contemplative tone,
16:9 horizontal, no people, no subjects,
shot on Mamiya 7 medium format, Kodak Portra 400,
"The Row" campaign aesthetic, editorial restraint
```

### Template C · Identity-preserving subject placement

Use Seedream 4.5 (NOT 5.0) for face preservation. Upload Evoto TIFF as reference.

```
Preserve subject identity exactly. Maintain face, hair texture,
body proportions, skin tone palette #B8956E.
Compose subject into [scene description],
shadow palette #2A2A2E, Mamiya 7 depth of field,
Kodak Portra 400 grain unification.
Do not modify face, hair texture, or body proportions.
Luxury editorial register, Mert and Marcus reference.
```

### Template D · Style transfer between two SNIPED frames

Seedream 5.0 edit model. Transfer the color/lens feel of a finished SNIPED Hero onto a new Hero candidate.

```
Transfer color tone, lens character, and grain from reference image A
onto subject image B. Preserve subject identity in image B exactly.
Match palette #2A2A2E #B8956E #F5EFE6.
Mamiya 7 lens character, Kodak Portra 400 grain.
Do not modify subject pose, expression, or composition.
```

---

## Failure modes (from fal.ai community reports)

| Failure | Cause | Fix |
|---|---|---|
| "Three hands" artifact | Seedream 5.0 known issue | Use 4.5 OR regenerate OR crop hands out |
| Faces shift in 5.0 | Identity preservation weaker | Switch to 4.5 for portraits |
| Smooth CGI feel | Default style too synthetic | Add "Kodak Portra 400" + "subtle film grain" + "photographic realism" |
| Over-stylization | Long prompts dilute | Keep under 250 words |
| Wrong color despite HEX | Conflicting style words in prompt | Remove style descriptors, let HEX carry |

---

## Access + integration

- **fal.ai** · API + web UI (recommended for SNIPED workflow integration)
- Direct ByteDance access (less stable for non-Chinese users)
- Pricing: per-image · check fal.ai for current rates

---

## When NOT to use Seedream

- **Generating the subject** · violates `feedback_edit_register_bifurcation` (identity holds, subject must be real photographed person)
- **Anti-AI client deliverables** · per `intel_ai_sentiment` memory. Seedream output is for IG creative engine only, never client work.
- **Direction Stack book frames** · those get the full Track B Photoshop assembly for portfolio-anchor ceiling. Seedream is the lite-comp lane.

---

## Cross-references

- `/05_PRODUCTION/track_b_frame_walkthrough.md` Step 3 · plate generation (Seedream is now a primary option)
- `/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md` · the broader AI image tool landscape
- Memory: `[[sniped-visual-direction-luxury-editorial]]` governs all Seedream prompts
- Memory: `[[feedback-edit-register-bifurcation]]` defines identity preservation rules
