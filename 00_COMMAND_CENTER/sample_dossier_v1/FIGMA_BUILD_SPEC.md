# Figma Build Spec · Sample Capability Dossier (PhaseLine Talent Partners)

**Date:** 2026-05-27 · **For:** building the v1 master kit in Figma to match the rendered PDF in this directory.

Honest scope: this spec gets you (or a designer) from zero to a brand-bible-accurate Figma file in a couple of focused hours. The PDF in this directory is the visual target; the markdown is the editable text source.

---

## 1. Figma file structure

```
File: BASEPLATE · Sample Capability Dossier v1
Pages:
  · COVER
  · CONTENT
  · COMPONENTS (master kit)
  · TYPE + COLOR (styles)
```

Set the file thumbnail to the cover. File-level cover image visibility: private.

---

## 2. Color styles (brand-bible · register as Figma Color Styles)

| Name | Hex | Use |
|---|---|---|
| Onyx | `#0F0F0F` | Primary text, structural lines, key headings. |
| White | `#FFFFFF` | Page background, inverse panels. |
| Concrete | `#8C8C8C` | Secondary text, dividers, eyebrows, slot frames. |
| Concrete Light | `#DCDCDC` | Section dividers, sub-rules. |
| Concrete Faint | `#F2F2F2` | Image slot fills, restrained tint blocks. |
| Blueprint Blue | `#0055FF` | Accent only · proof numbers, CTA labels, key callouts. Use sparingly. |

Do not introduce gradients, drop shadows, glow, or any color outside this set.

---

## 3. Type styles (Figma Text Styles)

| Style name | Family | Weight | Size | Line | Letter-spacing | Use |
|---|---|---|---|---|---|---|
| Display / Firm | Space Grotesk | 600 | 56 | 60 | -0.025em | Cover firm name. |
| Display / Section | Space Grotesk | 500 | 32 | 38 | -0.015em | Section heading (H1) on each page. |
| Display / Sub | Space Grotesk | 500 | 18 | 24 | -0.005em | Proof block titles. |
| Display / Positioning | Space Grotesk | 400 | 20 | 28 | -0.005em | Cover positioning line, profile lead. |
| Body / Regular | Inter | 400 | 14 | 22 | 0 | Body paragraphs. |
| Body / Medium | Inter | 500 | 14 | 22 | 0 | Body emphasis. |
| Body / Profile | Inter | 400 | 14 | 22 | 0 | One-screen profile lists. |
| Mono / Eyebrow | IBM Plex Mono | 500 | 10 | 14 | 0.22em | Eyebrows, page numbers, CTA labels, slot labels. |
| Mono / Field Label | IBM Plex Mono | 500 | 10 | 14 | 0.16em | Role-context field labels. |
| Mono / Tag | IBM Plex Mono | 500 | 9 | 12 | 0.08em | Image-slot tags ("approved non-secure" etc.). |

If you ship as a static file and want offline-safe fonts, swap Space Grotesk for system "SF Pro Display," Inter for "SF Pro Text," and IBM Plex Mono for "SF Mono." The register holds.

---

## 4. Page setup

- **Page size:** US Letter (8.5 x 11 in / 612 x 792 pt).
- **Margins:** top 0.85 in, right 0.9 in, bottom 1 in, left 0.9 in.
- **Grid:** 12-column, 16 pt gutter, 0.9 in side margins. Use for layout, not visible.
- **Page header (every page):** top-right "SAMPLE" in Mono / Eyebrow, color Concrete.
- **Page footer (every page):** bottom-left `PhaseLine Talent Partners  ·  The Capability Dossier  ·  SAMPLE  ·  v1  ·  2026-05-27` in Body / Regular at 7.5 pt, Concrete. Bottom-right page number in Mono at 8 pt, Concrete.

---

## 5. Components (build these as Figma master components in the COMPONENTS page)

### C1 · Cover
- Full page.
- Top: cover header eyebrow ("PhaseLine Talent Partners · the capability dossier · SAMPLE").
- Center: firm name (Display / Firm), two lines if needed.
- 1.2 in onyx rule directly below.
- Positioning (Display / Positioning), max width 5 in.
- Bottom: cover footer in Mono / Eyebrow, two lines (`SAMPLE · v1 · 2026-05-27` / `Invented firm. Anonymized program. No real-client implication.`)
- No image on the cover. Restraint is the cover.

### C2 · Section header
- Eyebrow ("01 · Capability story") in Mono / Eyebrow above.
- H1 in Display / Section.
- Onyx 1 pt rule directly below H1, full content width.
- Spacing: 16 pt after eyebrow, 24 pt below rule before body.

### C3 · Story block
- Body text (Body / Regular), max width 5.6 in.
- Paragraphs spaced 12 pt apart.

### C4 · Proof block (variant component)
- Top 1 pt rule in Concrete Light, full content width.
- Proof number in Mono / Eyebrow, Blueprint Blue.
- Proof title in Display / Sub.
- Body in Body / Regular.
- Optional bulleted list (Body / Regular, indent 1.2 em).
- Variants: with-bullets, without-bullets.
- Top rule is suppressed for the first proof block in a section.

### C5 · Team / operator block
- Story block (C3) on top.
- Image slot (C7) below.

### C6 · Role / bid context row (master + variants for one-line vs multi-line value)
- Grid: 110 pt label column · gap 0.8 em · value column.
- Label in Mono / Field Label, color Concrete, padded 3 pt top.
- Value in Body / Regular.
- Bottom 1 pt rule in Concrete Light. Suppressed on the last row in a stack.

### C7 · Image slot
- Frame: 1 pt dashed Concrete border, fill Concrete Faint.
- Height 2.1 in (single slot), 1.6 in (compact variant for double-stack).
- Center vertical stack:
  - Slot label in Mono / Eyebrow, Concrete.
  - Slot description in Body / Regular at 9 pt, Concrete, max 4 in wide.
  - Tags row at bottom (C8).
- Variants: portrait, work-scene, tools-bench, compact.

### C8 · Tag
- Pill: 1 pt Concrete border, white fill, 2 pt vertical / 6 pt horizontal padding.
- Mono / Tag, Concrete text, uppercase.
- Common tags: `approved non-secure`, `with release`, `controlled setting`, `placeholder`.

### C9 · Decision-path list block
- Plain bulleted list, Body / Regular.
- 4 to 6 items.

### C10 · CTA block
- Top + bottom 1 pt onyx rules, full content width.
- Internal pattern (repeating):
  - CTA label in Mono / Eyebrow, Blueprint Blue.
  - One-line CTA paragraph in Body / Regular.
- Spacing: 12 pt label-to-line, 18 pt between CTA groups.

### C11 · One-screen profile section
- Section name in Mono / Eyebrow at 7.5 pt with 5 pt bottom padding and a 1 pt Concrete Light rule.
- Plain list, no bullets, Body / Profile.
- 4 sections in a 2 x 2 grid: Disciplines · Standards literacy · Coverage · Engagement model.
- Footer CTA block (C10) for Contact.

### C12 · SAMPLE corner stamp
- A reusable text label component for the top-right "SAMPLE" stamp on every page.
- Mono / Eyebrow, Concrete, 0.22 em tracking.
- Used inside the page header.

---

## 6. Page-by-page assembly

| Page | Components used | Notes |
|---|---|---|
| 1 · Cover | C1 + C12 | No section header. No image. |
| 2 · Capability story | C2 + C3 | One block. |
| 3 · Proof | C2 + three C4 (first variant without top rule) | Three proof blocks. |
| 4 · Operator credibility | C2 + C5 (which is C3 + C7) | Portrait slot. |
| 5 · The named decision | C2 + four C6 rows | Role · Program · Scope · Why PhaseLine. |
| 6 · Security-safe visual proof | C2 + C3 (intro paragraph) + two C7 (variant: work-scene + tools-bench) | Slot intro + two slots. |
| 7 · Why this is the obvious yes | C2 + C9 + C10 | Decision-path list and CTA. |
| 8 · Capability profile · one screen | C2 + C11 | The leave-behind page. |

---

## 7. Image-handling discipline

- All image placeholders ship as C7 (dashed frame, no real photo) until BJ stages a non-secure shoot or sources permissioned imagery.
- Real images, once available, replace the slot fills in the master component, propagating to every instance.
- No stock photo, no AI image as evidence, no facility-floor frames, no client-tagged equipment. The §10 "cannot show" list governs every slot.

---

## 8. Export

- **PDF:** File → Export → Letter, "Include bleed: off." One PDF per dossier version, named `Sample_Capability_Dossier_v1.pdf` (rev the suffix on each version: `_v2`, `_v3`).
- **Pixieset:** later, when real images exist. Password-protected gallery, client-owned.

---

## 9. Watermarks and labels

- SAMPLE corner stamp (C12) on every page, no exceptions, for as long as this file is the SAMPLE.
- Cover and footer both carry SAMPLE + v1 + date.
- Never remove the SAMPLE label on this file. The real client dossier is a separate Figma file built from these same components, with a "Confidential" header in place of "SAMPLE."

---

## 10. What this build deliberately does not have
- No marketing tagline beyond the positioning line.
- No "Our values," "Our process," "Why us in six pillars," or anything brochure-shaped.
- No firm logo (yet). The wordmark in Space Grotesk 600 is the identity for v1.
- No client logos, no real-client implication, no fake testimonials, no fabricated metrics.
- No platform/registry framing.
- No "studio," "media," "creative" language anywhere.
- No outcome guarantees ("we'll get you hired"). The dossier moves a decision; it does not promise the result.

---

## 11. Truth-check before exporting v1
- [ ] All 8 pages render in the brand-bible palette only.
- [ ] No type outside the three families (Space Grotesk / Inter / IBM Plex Mono).
- [ ] Every image slot is a clearly-marked placeholder.
- [ ] SAMPLE corner stamp present on every page.
- [ ] Footer carries firm name + SAMPLE + v1 + date on every page.
- [ ] No marketing filler ("passionate / cutting-edge / world-class / seamless") anywhere.
- [ ] Page 5 role context renders all four fields cleanly.
- [ ] Page 8 profile renders the 2 x 2 grid cleanly.
- [ ] No element pulls visual energy away from operator-grade restraint.

---

## 12. Next versions

When v2 lands:
- Replace image-slot placeholders with permissioned non-secure imagery.
- Tighten any sentence that read off on the first share-screen.
- Hold the master components stable so every future client dossier is a fast assembly, not a redesign.
- Keep the SAMPLE label here. New client dossiers branch into a new file from the same components.
