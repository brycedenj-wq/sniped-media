# PHOTOSHOP_EDUCATION_GAP_AUDIT

**Date:** 2026-05-29
**Status:** Anchor-class. Markdown-only, not chunked, not a chunk source, not in master files. Companion to `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/photoshop_ceiling_v1/CURRICULUM.md`.
**Frame:** Decide what Photoshop / retouch / compositing education should be added to the OS to unlock the highest SNIPED image ceiling. Treat as targeted post-production doctrine, not generic Photoshop learning.

---

## Locked context (what we already know from the recent image arc)

- Local RAW pipeline works (rawpy decode + numpy float ops + 16-bit TIFF master + 8-bit JPG export).
- Greats-informed edit lanes work (Eggleston + Haas + Herzog + Avedon-light applied as parameters).
- Overprocessing is a real danger; the locked memory `feedback-strongest-photograph-not-most-processed` codifies the reject gate.
- Bad cleanup artifacts are worse than honest studio context (proven in the Untitled-1.CR3 v4 PS Content-Aware result).
- Higgsfield is the wrong tool for preserving stills (defishes, drifts, reduces resolution to 1 MP); useful for world building and motion derivatives.
- Adobe Firefly web (firefly.adobe.com) is the correct route for surgical cleanup like the black cap, included in Creative Cloud subscription.
- Photoshop remains the ceiling tool for composites, skin, masks, type-adjacent polish, and print masters.

---

## 1. What Photoshop knowledge is actually missing

Honest gap analysis against the 6 SNIPED lanes (Clean Editorial, Founder/Operator, Cultural Doc, High-Concept Fashion/Surreal, Campaign/Set Piece, Live Access). Where the local pipeline + Adobe MCP + Firefly web + Higgsfield combination cannot reach the ceiling.

| Category | Current gap | Lane it would unlock |
|---|---|---|
| Masking / selections | Adobe MCP AI Subject is fine for batch but not composite-grade. Hair, transparent edges, channel-based luminosity masks need hand refinement. | 1, 2, 3, 4, 5 |
| Skin texture / dodge and burn | Local engine + Evoto handle volume; D&B for editorial light sculpting (light SHAPING not brightness correction) and selective curves on luminosity masks is the gap. | 1, 2, 4, 5 |
| Frequency separation | High-risk technique. SNIPED-appropriate version: low-frequency smoothing only, high-frequency texture layer never touched. | 1, 2 (selectively), 4, 5 |
| Color grading (advanced) | Camera Raw Filter as Smart Filter for non-destructive grading; 3D LUT creation; print color management. | All lanes |
| Compositing | Layer blend mode mastery, subject + AI-world masking, light/color matching across layers, edge blending. | 4, 5 |
| Generative Fill / Firefly in PS | When to use Gen Fill vs Remove tool vs Content-Aware; prompt construction; selective editing that respects the photograph. | 1, 3, 4, 5 |
| Product / campaign polish | Edge sheen, sculpted shadow, color block backdrops, gradient discipline. | 5 |
| Print prep | 16-bit lock, soft-proofing, CMYK with ink limits, output sharpening math, print sizing, master file structure. | All lanes (print edition tier) |
| Batch actions / automation | Action recording, batch processing, Image Processor, droplets, ScriptListener. | 1 (tier-B), 6 (same-day) |
| Smart objects / non-destructive workflow | SO foundation, Smart Filters, CRF as SF, one master PSD multi-deliverable export. | All lanes |

---

## 2. Tutorial categories to add

Per category, with priority gate (ESSENTIAL / USEFUL / OPTIONAL).

### A. Masking / selections · ESSENTIAL
- **Why it matters:** Adobe MCP gives selection; PS gives the refinement that turns selection into composite-grade alpha.
- **Lane it unlocks:** All 6; ceiling-grade in 4 + 5.
- **Without this:** Lanes 4 and 5 have no ceiling.

### B. Skin texture-preserving retouch + dodge and burn · ESSENTIAL
- **Why it matters:** PS reaches the Pratik Naik / Solstice Retouch / pulled-back-Avedon ceiling. Evoto handles volume; PS handles tier-A.
- **Lane it unlocks:** 1, 2, 4, 5 ceiling.
- **Ignore:** "perfect skin", "porcelain skin", "magazine skin secrets", "beauty retouching" titles. Anti-patterns.

### C. Frequency separation · USEFUL (gated)
- **Why it matters:** Works when constrained correctly. Most tutorials destroy texture.
- **Verdict:** Include with explicit reject gates against the destructive version.
- **Ignore:** Anything smoothing the high-freq layer; any "1-click frequency separation" preset packs.

### D. Color grading via Camera Raw Filter as Smart Filter · ESSENTIAL
- **Why it matters:** Non-destructive register application. Greats moves applied as Smart Filter are reversible / reapplicable.
- **Lane it unlocks:** All 6.

### E. Compositing · ESSENTIAL for lanes 4 + 5
- **Why it matters:** The timtadder + jpwphoto + kykapture register is fundamentally composited. Real subject + crafted world.
- **Verdict:** Highest-leverage education gap.

### F. Generative Fill + Remove tool discipline · ESSENTIAL
- **Why it matters:** Addresses the specific failure mode from the prior arc (the black cap left unfixed).
- **Lane it unlocks:** 1, 3, 4, 5.
- **Ignore:** "10 AMAZING Generative Fill tricks" content. Magic-button framing.

### G. Product / campaign polish · USEFUL (lane 5)
- **Why it matters:** Album cover / kykapturedit / jpwphoto product + set work depends on this.
- **Lane it unlocks:** 5.

### H. Print prep · USEFUL now, ESSENTIAL when print editions launch
- **Why it matters:** Print editions ($300 to $1,500 per piece) require print-master discipline.

### I. Batch actions / automation · USEFUL
- **Why it matters:** Lane 1 tier-B volume + Lane 6 same-day work.

### J. Smart objects / non-destructive workflow · ESSENTIAL
- **Why it matters:** Iteration speed + multiple deliverable export from one master PSD.
- **Lane it unlocks:** All 6.

---

## 3. Reject list (what does NOT go in the curriculum)

| Category | Why reject |
|---|---|
| Beginner Photoshop basics | BJ has 7 years of shooting; gap is ceiling, not entry. |
| Generic beauty retouching | Anti-pattern. |
| Plastic skin workflows | Identity violation. |
| Preset pack culture | Preset worship is locked-against. |
| "10 amazing Photoshop tricks" YouTube content | Surface-level, often anti-pattern. |
| Trendy AI effects (cartoonize, anime-fy, restyle to Pixar) | Identity violation. |
| "Look younger / remove wrinkles / smooth skin" tutorials | Anti-pattern. |
| HDR-style tone mapping | Produces unreal looks. |
| Dragan-style processing | Anti-Avedon. |
| Surface Blur skin smoothing | Destroys texture. |
| Liquify body / face reshaping | Identity violation. |
| Eye-enlargement / teeth-whitening | Identity violation. |
| "Complete Photoshop master class" courses | Too broad. |
| Warm-teal cinematic color grade tutorials | Anti-pattern. |
| Newborn / wedding / family retouching | Different register. |

---

## 4. SNIPED Photoshop ceiling curriculum (the 10 core techniques)

Each technique maps to a specific SNIPED output. Folders established in `05_PRODUCTION/photoshop_ceiling_v1/`.

| # | Technique | Maps to SNIPED output | Priority |
|---|---|---|---|
| 1 | Advanced subject masking + hair / edge refinement | Tier-A frames across all 6 lanes; lane 4 + 5 ceiling impossible without this | ESSENTIAL |
| 2 | Skin texture-preserving retouch (low-freq only) + D&B for light sculpting | Lane 1 + 2 + 4 + 5 ceiling; Pratik Naik / Solstice register | ESSENTIAL |
| 3 | Camera Raw Filter as Smart Filter (non-destructive Greats-grade) | All lanes; non-destructive register application | ESSENTIAL |
| 4 | Compositing · subject + AI-generated world | Lane 4 + 5 entirely (timtadder + kykapturedit register) | ESSENTIAL for 4 + 5 |
| 5 | Generative Fill / Remove tool discipline | Lane 1 + 3 + 4 + 5 cleanup (the black cap fix) | ESSENTIAL |
| 6 | Color matching across composited layers | Lane 4 + 5 (subject + AI world believability) | ESSENTIAL for 4 + 5 |
| 7 | Print master preparation | Print edition deliverables | USEFUL, becomes ESSENTIAL when print launches |
| 8 | Action recording + batch processing | Lane 1 tier-B + Lane 6 same-day | USEFUL |
| 9 | Smart object workflow + master PSD multi-deliverable export | All lanes (efficiency multiplier) | ESSENTIAL |
| 10 | Specific Generative Fill prompt language | Lane 3 + 4 + 5 cleanup beyond simple object removal | USEFUL |

---

## 5. Where these resources live in the OS

**Path locked:** `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/photoshop_ceiling_v1/`

**Rationale:** Adjacent to `_preset_backups/` (the locked Lightroom presets). Production-grade resources clustered together. Distinct from `00_COMMAND_CENTER/sniped_retouch_engine_v1/` which is the LOCAL engine spec; the PS ceiling is the manual-ceiling layer above the local engine.

---

## 6. How tutorials convert into OS value

Every tutorial consumed must produce at least ONE persistent asset. Anything that does not produce a persistent asset was not actually consumed for OS leverage.

| Asset | Purpose |
|---|---|
| Checklist | Step-by-step operator follows; replaces re-watching. |
| Reject gate | Discipline rule that disqualifies a result. |
| Before/after standard | Visual reference frame for acceptable outcome. |
| Photoshop action (.atn) | Recorded sequence runnable with one click. |
| Figma / cover output standard | Export spec when technique feeds into Figma layout. |
| Retouch decision rule | When to apply this vs alternatives. |
| Compositing recipe (PSD template) | Starting PSD with layer structure. |
| Print-master standard | Specific export spec for print. |
| Prompt language reference | Generative Fill prompts that produce clean context. |

The tutorial is consumed once. The OS asset is the recurring leverage.

---

## 7. Top 5 tutorial sources to look for first

| # | Source | Why | Unlocks |
|---|---|---|---|
| 1 | Pratik Naik (Solstice Retouch) · Conscious Retouching | Closest match to locked SNIPED restraint doctrine. Editorial skin work at the Naik / Avedon / Herzog ceiling. | Technique 2 |
| 2 | Aaron Nace (PHLEARN Pro) · advanced compositing series | Gold standard for PS technical training. Compositing curriculum aligned to lanes 4 + 5. | Techniques 1 + 4 |
| 3 | Glyn Dewis · 21 Days of Photoshop + Photographer's Workflow | Editorial light sculpting in post. Leibovitz / Frank lineage applied digitally. | Technique 2 (D&B) + parts of 5 |
| 4 | Adobe Helpx official · Generative Fill + Remove tool + Smart Object docs | Authoritative PS 2024+ Firefly workflows. Free, no preset culture. | Techniques 5 + 9 + 10 |
| 5 | Bret Malley · surreal compositing | Subject + crafted world compositing for the timtadder lane. | Technique 4 |

If only ONE budget item: Pratik Naik's Conscious Retouching (closes largest gap, aligns with locked doctrine). If TWO: add PHLEARN Pro advanced compositing.

---

## 8. Honest verdict on the gap

**Largest single gap:** Technique 4 (compositing). Lane 4 (timtadder) and lane 5 (jpwphoto, kykapturedit, album cover) are entirely composite-driven. Without ceiling compositing, SNIPED cannot reach those lanes.

**Second-largest gap:** Technique 2 (skin texture-preserving retouch + D&B). Closes the Evoto bridge. Once SNIPED matches Pratik Naik's register, Evoto becomes redundant.

**Third gap:** Technique 5 (Generative Fill discipline). The specific failure mode from the prior arc (black cap). Closing this gap fixes a recurring miss.

---

## 9. Standing rule (carried into the OS)

Only add tutorials and classes that map to a specific missing SNIPED ceiling technique. Anything else is education noise. Every new resource must produce a persistent OS asset within the same week it is consumed, or it gets deleted.

Companion locked memory: `feedback-strongest-photograph-not-most-processed`. The reject-gate discipline applies to every technique in this curriculum.

---

## 10. Pickup pointer

For any future Photoshop / retouch / compositing decision, read in this order:

1. `CURRENT_STATE.md` for locked thesis and architecture.
2. `SNIPED_2026_PRODUCTION_SYSTEM.md` for the production system + retouch posture.
3. `EMPIRE_OS_MONEY_MACHINE_THESIS.md` for the 17-step revenue path the technique serves.
4. **This audit** for the gap map.
5. `/Users/sniper/Downloads/    SNIPED_OS/05_PRODUCTION/photoshop_ceiling_v1/CURRICULUM.md` for the operating curriculum.
6. Topic-specific `checklist.md` / `reject_gates.md` / `references.md` for the technique itself.

---

## Guardrails (still locked)

- Anchor-class: not chunked, not in master files, total_chunks unchanged at 1,837.
- No fake proof, no fake identity, no plastic skin, no race-to-bottom, no SNIPED / BASEPLATE merge.
- No tool spiral; each tutorial earns its slot via mapped technique gap.
- Per-batch approval gates on every credit-spending generation.
- Reject gate discipline applies to every output, including manual PS ceiling work.
