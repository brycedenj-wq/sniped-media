# 08 · VISUAL IDENTITY BRIEF · BASEPLATE STUDIO

**Locked:** 2026-05-13 (evening · v2 · rewritten from actual brand bible)
**Source:** `/Users/sniper/Downloads/BASEPLATE/Brand Bible.pdf` + logo files (received 2026-04-11)

This file documents the EXISTING BASEPLATE brand bible and translates it into surface-specific application briefs for the photography work. The visual identity is already built. This file does not redesign it · it deploys it.

---

## The brand bible stance (verbatim from existing bible)

> Industrial Precision / Architectural Brutalism. Dark, highly structured, calculated. Think high-end data center schematics or a luxury technical manual.

This is the entire visual mood in one sentence. Every Card, every IG post, every founder bio, every Reset deck flows from this stance. When in doubt, the question is "does it feel like a data center schematic or a luxury technical manual?"

---

## The mark

The BASEPLATE mark is a stacked B-form composed of two arrow / bracket shapes:
- Upper bracket: blue or white (depending on background)
- Lower bracket: black or white (depending on background)
- Together they form a "B" that also reads as two stacked plates / shelves / foundation layers
- Industrial-geometric · constructed on triangular grid (per page 02 of bible)

**Mark behavior:**
- On dark backgrounds (default): B-mark in white + electric blue accent + white wordmark
- On white backgrounds: B-mark in blue + black + black wordmark
- On electric-blue backgrounds: B-mark in white only · white wordmark

**Mark + wordmark spacing:** B-mark sits left of wordmark · vertical alignment matches cap-height of "BASEPLATE" · breathing room between mark and wordmark ≈ 1× the width of the mark.

Files available at `/Users/sniper/Downloads/BASEPLATE/Logo Files/`:
- BASEPLATE.ai · Illustrator source
- BASEPLATE.eps · vector
- JPG 1 + JPG 2 · raster references
- Profile/ · 5 variants for social profile use
- Transparent PNG/ · 4 wordmark variants + Icon/ folder (B-mark alone)

---

## Typography

The bible names **Helvena** as the typeface. In practice this functions as a geometric industrial sans-serif. If the actual Helvena license isn't on hand, the practical equivalent is **Helvetica Neue** or **Inter** at the corresponding weights · same visual register.

| Use | Typeface | Weight | Tracking |
|---|---|---|---|
| Wordmark BASEPLATE | Helvena (Helvetica Neue Bold) | Bold | +20 |
| Display headlines | Helvena | Bold / Black | normal |
| Body / editorial text | Helvena | Regular | normal |
| Sub-marks / labels (e.g. STUDIO · VOL · CHAPTER) | Helvena | Medium · all-caps | +120 to +160 |
| Technical specs / colophons | Helvena Mono OR Helvetica Regular small-caps | Regular | +80 |

**Editorial-archival fonts removed.** Playfair Display Black (which was on the SNIPED Card master) is NOT BASEPLATE STUDIO typography. It comes off. The replacement is Helvena across the entire system.

---

## Color palette (locked from bible)

| Use | Hex | RGB | Notes |
|---|---|---|---|
| Brand accent | `#0055FF` | rgb(0, 85, 255) | Electric blue · use SPARINGLY · 1 accent element per surface max |
| Light / paper | `#FFFFFF` | rgb(255, 255, 255) | Pure white · NOT the warm paper `#F5EFE6` from SNIPED · that comes off |
| Mid gray | `#8C8C8C` | rgb(140, 140, 140) | Colophon body · technical labels · hairline rules |
| Dark / near-black | `#0F0F0F` | rgb(15, 15, 15) | Default dark mode background · NOT the charcoal `#2A2A2E` from SNIPED |

**Removed colors:** warm paper `#F5EFE6`, brass `#8B6E50`, charcoal `#2A2A2E`. These were SNIPED-era warm-archival palette. BASEPLATE STUDIO is industrial-precision · the palette above replaces them entirely.

---

## Mode system

Three modes for any surface · one chosen per artifact.

### Dark mode (default · most surfaces)
- Background: `#0F0F0F` near-black
- Wordmark: white + B-mark in white with blue accent
- Body text: white or `#8C8C8C` mid gray
- Reference register: data center documentation · MIT Press technical books · Wired night spreads

### Light mode (alternate)
- Background: `#FFFFFF` pure white
- Wordmark: black with B-mark in blue + black
- Body text: black or `#8C8C8C`
- Reference register: Vercel docs · Linear app · Criterion Collection back covers

### Brand mode (rare · special editions only)
- Background: `#0055FF` electric blue (whole surface)
- Wordmark: white
- Body text: white
- Use case: announcement-only · special edition Cards · launch frames
- Frequency: < 5% of all surfaces

---

## Card system · rebuilt for BASEPLATE STUDIO

The Chapter Card master needs a full redesign in Figma. The SNIPED-era warm-paper/Playfair Card was beautiful for SNIPED · it doesn't fit BASEPLATE. The new Card system uses the brand bible directly.

### Card structure (locked elements · transferred from SNIPED Card)

These stay:
- VOL · CHAPTER · SUBJECT · LOCATION · MONTH masthead structure
- Image area (B&W per dual-register rule)
- Cover line (optional · one short sentence)
- Colophon at bottom (credits + edition + serial)
- 4:5 / 1:1 / 9:16 ratio variants

### Card design · industrial register

**Default Card · DARK MODE STANDARD:**

```
┌───────────────────────────────────────┐
│                                       │
│  [B-mark]  BASEPLATE STUDIO           │ ← masthead · white on near-black
│                                       │
│  VOL · II · CHAPTER 02                │ ← Helvena Medium · gray
│  MIMI · LOS ANGELES · MAY 2026        │ ← Helvena Medium · gray
│                                       │
│  ┌─────────────────────────────────┐  │
│  │                                 │  │
│  │                                 │  │
│  │     [B&W photograph · v3        │  │
│  │      LUXURY edit · centered]    │  │
│  │                                 │  │
│  │                                 │  │
│  └─────────────────────────────────┘  │
│                                       │
│  "Texture as power."                  │ ← Helvena Italic · centered · cover line (optional)
│                                       │
│  ─────────────────────────────────    │ ← hairline rule · gray
│                                       │
│  EDITION I · MMXXVI · CHAPTER 02      │ ← Helvena Mono · gray · small
│  SERIAL 01 / 01                       │
│                                       │
│  DIRECTION & PHOTOGRAPHY · BRYCE DENJ │
│  COMPOSITE · @[rejuar handle]         │
│  LINEAGE · [designation]              │
│                                       │
└───────────────────────────────────────┘
```

**Variants needed (rebuild in Figma · Sat session):**
- DARK STANDARD · default for most chapters
- LIGHT STANDARD · alternate · clean white background
- DARK + BLUE ACCENT · special edition · single blue element (typically the hairline rule)
- 1:1 SQUARE · for grid posts
- 9:16 STORY · for IG Stories

**What dies:**
- Warm paper background (was `#F5EFE6` · now `#0F0F0F` or `#FFFFFF`)
- Playfair Black masthead (was the SNIPED wordmark style · now Helvena Bold)
- Brass colophon text (was `#8B6E50` · now `#8C8C8C` gray)
- "Aperture / LIFE / Magnum" reference register · replaced by "Wired / MIT Press / Criterion Collection"
- The 6 archival variants on Page 2 of the SNIPED Card master (LIGHT FOIL · DARK FOIL · etc.) · those were the SNIPED system · BASEPLATE STUDIO is simpler · 5 variants max

**What survives:**
- The VOL · CHAPTER · SUBJECT · LOCATION · MONTH structure
- The B&W photograph rule
- The serial-numbered edition discipline
- The hairline rule separating image from colophon
- The credits-in-colophon discipline

---

## Reference register (use these to test new design decisions)

When designing a BASEPLATE STUDIO surface, ask "does this feel like one of these references?"

**Tier A · core references:**
- Wired magazine technical spreads (2010-2020 era · pre-redesign)
- MIT Press technical books (Helvetica · dark mode · negative space)
- Criterion Collection film covers + booklets (single-image discipline · Helvetica colophons)
- Vercel + Linear + Stripe documentation (industrial-clean SaaS · sparse blue accents)

**Tier B · secondary references:**
- Bauhaus archival posters (geometric · constructed · industrial-typographic)
- NASA technical documentation (mission reports · technical-archival)
- IDEO design documentation (sparse industrial · sans-serif · clean grids)
- Pentagram-designed corporate identities (industrial-precision · negative space · single accent)

**Tier C · what to AVOID:**
- Aperture / Magnum / LIFE monograph design (warm-archival · was the SNIPED reference register · doesn't apply)
- Wedding photographer / lifestyle creator brand aesthetics
- Tech-bro casual / "founder lifestyle" energy (Substack creator-economy register)
- Any brand using Playfair, Garamond, Caslon, or other editorial serifs for primary wordmarks

---

## Logo file usage reference

| File | Use when |
|---|---|
| `Profile/Verson 1.jpg` through `Verson 5.jpg` | Profile picture · use whichever scales best at 1:1 IG round crop · likely Verson 3 or 4 |
| `Transparent PNG/Verson 1.png` through `Verson 4.png` | Wordmark + B-mark composite · for headers, masthead use, deck covers |
| `Transparent PNG/Icon/` (B-mark alone) | Icon use · favicon · small Card footer mark · social profile pic (if wordmark is too long) |
| `BASEPLATE.ai` | Source file · open in Illustrator for any custom adaptation |
| `BASEPLATE.eps` | Vector export · use when scaling to print |

For the Card master in Figma, import the appropriate Transparent PNG variant directly into the Figma file. Place B-mark + wordmark at the top-left of every Card variant.

---

## Mark behavior across surfaces (updated for BASEPLATE STUDIO)

| Surface | Mark version | Background | Notes |
|---|---|---|---|
| Chapter Card (default) | BASEPLATE STUDIO wordmark + B-mark | Dark `#0F0F0F` | Card colophon at bottom |
| Chapter Card (alt) | Same | Light `#FFFFFF` | Special chapters or contrast moves |
| IG profile picture | B-mark icon alone (square crop) | Brand blue `#0055FF` or near-black | Profile/Verson 3 or 4 |
| IG bio | Plain text "BASEPLATE STUDIO" in display name | n/a | Per file 07 |
| IG post (image) | No mark on image | n/a | The image carries · mark in profile only |
| LinkedIn header banner | BASEPLATE STUDIO wordmark + tagline | Dark mode or brand blue | Use the wordmark + tagline combo |
| Email signature | Wordmark text inline | n/a | "Bryce Denj · BASEPLATE STUDIO" |
| baseplate.studio website root | Wordmark + tagline · centered | Dark mode default | Below wordmark: imprint description |
| Reset deck cover | Wordmark + service name · single page | Dark mode | "BASEPLATE STUDIO · THE RESET" |
| Direction Stack book cover | Wordmark + book title | TBD per book design | Helvena throughout |
| Cold DM signature | Plain "Bryce · BASEPLATE STUDIO" | n/a | Per file 07 DM voice |

---

## The Saturday Figma session (rebuilt scope)

The Card master rebuild on Sat 5/16 needs to be more substantial than the original migration plan estimated. Real session brief:

1. Open existing Chapter Card master Figma (`AiMtRfT8W33yZRf4khjnds`)
2. Archive the existing Page 1 + Page 2 (SNIPED-era warm-archival Cards) · rename to `LEGACY · SNIPED v1` for historical reference · don't delete
3. Create new Page 3 · `BASEPLATE STUDIO · MASTER v1`
4. Build the 5 Card variants per the section above (DARK STANDARD · LIGHT STANDARD · DARK + BLUE ACCENT · 1:1 · 9:16)
5. Import BASEPLATE wordmark + B-mark PNG/SVG into the Figma file
6. Set up Helvena (or Helvetica Neue fallback) as the file's primary typeface
7. Build text styles · Wordmark · Display · Body · Mono · Colophon · Cover Line
8. Build color styles using the locked palette
9. Test against the CH02 Mimi leather coat standing front frame (already selected per Mimi brief) · apply Card · verify register reads correctly
10. Export each variant as PNG · file in `/04_DELIVERABLES/CH02_mimi/cards/baseplate_studio_v1/`

Time estimate: 2-3 hours · do on Sat afternoon. CH02 Mimi Card production happens AFTER the master is rebuilt (Sun 5/17).

---

## What the new register signals (vs old warm-archival)

| Signal | SNIPED warm-archival Card | BASEPLATE STUDIO industrial Card |
|---|---|---|
| What audience reads | "This is editorial photography in the Aperture tradition" | "This is editorial photography produced by an infrastructure operator" |
| Founder credibility | Reads creator | Reads founder · Forbes-credible |
| Cultural-memory positioning | Archival warmth · accessible | Archival precision · technical · gallery-credible (the gallery wants the precision register · not the warmth) |
| Differentiation from other photographers | Modest (warm-archival is a known register) | High (industrial-tech photography brand is rare · operator-coded refusal) |
| The dual-register effect on photography | Photo + frame both warm · congruent · "expected" | Warm photo INSIDE cold industrial frame · tension · signature move |

The new register is harder to do well · the warmth must come ENTIRELY from the photograph since the frame won't carry it. v3 LUXURY edit register has to deliver the emotional warmth · the industrial Card frame creates the contrast.

This pressure-tests the v3 LUXURY edit · which is the right pressure-test.

---

## Tagline integration with industrial register

Tagline candidates from file 06 · revisited under industrial register:

1. **`The operating layer for editorial photography.`** · ✓ matches industrial register · use on LinkedIn + website
2. **`A named archive.`** · ✓ matches · use on IG bio
3. **`Editorial photography. Compounded.`** · ~ works · slightly warm
4. **`Published in the lineage.`** · ✓ matches · use on Card colophons sparingly
5. **`Documented work, sealed in editions.`** · ✓ matches · use on PRESS surfaces

The taglines from file 06 hold · they were industrial-credible already. The visual treatment under the tagline shifts to Helvena.

---

## Open question for BJ

The bible names **Helvena** as the typeface. Two possibilities:

1. Helvena is the actual font name your brand bible designer specified (some custom or licensed font) · in which case you have the source license and can use it
2. Helvena is shorthand for Helvetica · or a typo · or a placeholder · in which case Helvetica Neue or Inter is the practical substitute

If you have the actual Helvena font file, use it. If not, default to Helvetica Neue (paid · Apple-system-shipped) or Inter (free · Google Fonts) for the Figma rebuild. Either substitute is visually within 5% of any "Helvena" interpretation.

Note in the Card master Figma · whichever font is used · for future continuity.
