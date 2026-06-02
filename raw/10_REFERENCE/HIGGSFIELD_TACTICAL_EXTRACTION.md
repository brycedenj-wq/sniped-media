# Higgsfield · Tactical Extraction for SNIPED

Source: `/99_VAULT/_intake_archive_2026-05-12/higgsfield never forget.docx`
Distilled: 2026-05-12

Higgsfield is NOT just a motion/animation tool (as currently slotted in `PRODUCTION_OS.md` Section 4.4). It's a **Claude-integrated content factory** via MCP connector. This extraction repositions Higgsfield's role in the SNIPED stack.

---

## What changed

Old SNIPED slotting (PRODUCTION_OS.md Section 4.4):
> Higgsfield · Same as Kling · Post-conversion delivery moments

Updated reality:
> Higgsfield · Full content factory via MCP. Image gen (GPT Image 2.0 + Seedance 2 routing), video gen (Higgsfield Marketing Studio), avatars, plus 4-stage pipeline (research → content plan → generation → schedule to Meta Ads). Per-batch permission gates so credits don't disappear silently.

This means Claude (this assistant) can talk DIRECTLY to Higgsfield once MCP is configured. No copy-paste workflow. No re-uploading subject images between sessions.

---

## Setup · the one-time install

### Step 1 · Add MCP connector
1. Go to Higgsfield website → MCP and CLI tab
2. Copy the connector link
3. In Claude (desktop or web): Settings → Connectors → Add custom connector
4. Paste link, name it "Higgsfield," hit add
5. Sign into Higgsfield account when prompted
6. ~30 seconds total

After this, Claude can: generate images, videos, choose avatars, pull from generation history · all without leaving chat.

### Step 2 · Upload Higgsfield Content Factory skill
1. Download the skill file (link in source video description)
2. In Claude: Customize Skills → plus button → Create Skill → Upload Skill
3. Drag and drop the file

### Step 3 · Invoke
Type `/higgsfield content factory` to trigger the 4-stage pipeline.

---

## The 4-stage Content Factory pipeline

### Stage 1 · Research & trend analysis
- Pulls live data from TikTok, Instagram, YouTube
- Identifies what's viral in your niche
- Synthesizes into a viral content brief with:
  - Trends table
  - Competitor brands killing it
  - Hook patterns that are working
  - 20 idea cards (each with preset name, setting, system hook, duration, scene description, caption)

### Stage 2 · Content plan
- 60-day production calendar (default)
- Campaign name auto-derived
- Date range, formats, hook breakdown auto-calculated
- For 100 UGC videos: groups by 5 formats, 100 rows
- "More thorough than a human producer" per source

### Stage 3 · Generation
- Videos via Higgsfield Marketing Studio
- Images via GPT Image 2.0 (or Seedance 2 for video pipelines)
- **Per-batch permission gates** · approve before credits burn. Critical discipline.

### Stage 4 · Schedule to Meta Ads
- Connects to Meta Ads
- Schedules content directly into campaigns
- Can analyze performance and adjust content

### Stage 5 · Cost breakdown (the comparison)
Per source: 100 UGC videos + image pack via Higgsfield ≈ a few hundred dollars. Equivalent via hired UGC creators ≈ $28,000 + 6-8 weeks managing 20 different creators.

---

## Image Pack workflow (Chapter 13) · the SNIPED hero relevant part

After videos are generated, switch Claude to GPT Image 2.0 to generate the still image pack:
- Product shots
- Hero banners
- Ad creatives
- The full visual system underneath the videos

Key benefit: **no re-uploading, no re-explaining the brand.** Claude pulls from the same plan and same product image already uploaded.

For SNIPED: this is the lite-hero-composite path. Upload yae 04 Evoto TIFF once. Higgsfield generates the IG hero variations + IG carousel frames + LinkedIn POV asset · all in the same chat, all using the same subject reference.

---

## Image Prompt Helper Skill + Seedance 2 workflow

Second tutorial section. Different pipeline:

1. Set up a local folder with project files
2. Drop a product/subject image into the folder
3. Run the Image Prompt Helper skill in Claude
4. Skill analyzes the image and style references, asks questions about:
   - Style of commercial / shot
   - Environment
   - Lighting
   - Use case + platform
5. Pre-built suggestions surface based on the image
6. Choose image model, frame count, style reference handling
7. Iterate prompts with Claude back-and-forth
8. When satisfied with images → trigger Seedance 2 for video generation based on the chosen stills

For SNIPED: this is closer to the locked Track B workflow but with Claude orchestrating the prompts instead of you manually prompting Firefly/Nano Banana.

---

## SNIPED-specific usage

### Use NOW for

| Task | How |
|---|---|
| IG hero composite (lite lane) | Image Pack via GPT Image 2.0 · upload yae Evoto TIFF, generate 4-6 variations of hero scenes |
| IG carousel for one shoot | 4-stage pipeline OR Image Pack · multi-frame consistency baked in |
| Behind-the-scenes UGC content | Stage 3 of pipeline · generate UGC-style frames from shoot reference |
| Product/Op Kit / Brand System hero shots (for LinkedIn carousel) | Image Pack · multiple angles from one capture |
| Pre-vis for a planned shoot | Stage 1 research + Stage 2 plan · use to brief models before show day |

### Use NEVER for

- **Generating the subject** · violates identity rule per `feedback_edit_register_bifurcation`. Subject must always be real photographed person. Higgsfield generates plates, backgrounds, atmospheric extensions · NOT yae's face.
- **Anti-AI client deliverables** · per `intel_ai_sentiment`. Higgsfield is for IG creative engine + internal pipeline, never client work.
- **Direction Stack book frames** · those get full Track B Photoshop assembly for portfolio-anchor ceiling.

---

## Permission gate discipline (the load-bearing rule)

Higgsfield burns credits. The MCP defaults to "ask before generating" but you can set "always allow." 

**SNIPED rule:** keep permission gates ON for first 30 days of usage. After you understand the credit economics per output, allow specific batch types to auto-run (e.g., 4-variation plate gen for IG hero). Never set "always allow" globally.

---

## Cost framing (for the Phase 1 ledger)

Higgsfield credits + GPT Image 2.0 credits + Seedance 2 credits add up. The source frames it as "vs. hired UGC creators" which is fine for content factory but misleading for SNIPED's primary lane (premium portraits, not content volume).

**SNIPED's real comparison:** Higgsfield IG hero composite = 20-40 minutes + ~$X credits vs. Track B Photoshop = 60-80 minutes + $0 credits + your full attention.

Lite lane (Higgsfield) when the frame is for IG/content velocity. Ceiling lane (Track B) when the frame is portfolio anchor.

---

## How this changes existing locked docs

The following SHOULD be updated (track in ACTIVE_THREADS.md as a deferred maintenance task):

| Doc | Update |
|---|---|
| `/00_BRIEF/PRODUCTION_OS.md` Section 4.4 | Reposition Higgsfield from motion-only to full content factory + Claude MCP integration |
| `/00_BRIEF/PRODUCTION_OS.md` Section 4.6 | Add Higgsfield Image Pack as "AI free leverage" candidate |
| `/05_PRODUCTION/track_b_frame_walkthrough.md` Step 3 | Add Higgsfield Image Pack as primary plate / lite-composite option alongside Seedream + Nano Banana |
| `/07_CONTENT/audience_engine.md` | Reference Stage 1 research output as input for content calendar |

Pending until Higgsfield MCP is actually installed and stress-tested on one full pipeline (one yae frame).

---

## Cross-references

- `/10_REFERENCE/SEEDREAM_TACTICAL_EXTRACTION.md` · Seedream 5.0 prompting tricks
- `/10_REFERENCE/AI_IMAGE_TOOLS_TACTICAL_EXTRACTION.md` · the broader image tool matrix
- `/05_PRODUCTION/track_b_frame_walkthrough.md` · the Photoshop ceiling lane (compare against Higgsfield lite lane)
- Memory: `[[sniped-visual-direction-luxury-editorial]]` · governs all Higgsfield prompts
- Memory: `[[ai-sentiment-photography-market]]` · why Higgsfield output never reaches client deliverables
