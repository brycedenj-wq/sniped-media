# SOLE HOUSE · VISUAL IDENTITY SYSTEM

72-Hour AI-Native Campaign House · The Vault Room · The Singular Seal

This is the locked visual system for SOLE HOUSE. It exists to make one claim feel already true and already expensive. The world is the moat. Visual drift is the primary failure mode, so every spec here is a constraint, not a suggestion. Only the claim and the per-client copy vary. Everything else is pre-rigged and held strict.

Working name SOLE (name-availability gate flagged). Backups if the gate kills it: VANTABLE, ONLIQ, MONARCH ROOM. This system is built so the wordmark swaps without breaking the world.

Implementable in Figma (variables, components, auto-layout) and Adobe (Illustrator master, Photoshop emboss, InDesign deck, After Effects strike). All measurements are given as ratios first so they scale to any artboard.

---

## 1. THE FIRST PRINCIPLE

Everything in this system obeys one composition: **a single object under a hard shaft of top-light, on a plinth, in a vast dark room.** The wordmark is that object. The Seal is that object. The deck cover is that object. The film's final frame is that object. When a layout is in doubt, return to the single-object-under-light rule and remove whatever is not it.

The register is engraved, struck, embossed, acquired, archived. Never printed, never flat, never SaaS. Surfaces look machined into metal and stone, not laid onto paper.

---

## 2. WORDMARK SPEC · SOLE

### 2.1 Register

The SOLE wordmark is a high-contrast didone engraved nameplate. It reads as a maker's mark struck into brass, not a startup logotype. Four capitals, no lowercase, no icon lockup required (the Seal is the icon, kept separate).

### 2.2 Typeface

- **Primary cut:** Canela Deck or Canela (Commercial Type) at the Bold or Black weight for the struck nameplate look.
- **Approved alternates (in priority order):** GT Sectra Display, Ogg, or Tiempos Headline. All carry the high-contrast didone-adjacent stress with a slightly humanist terminal that survives engraving and embossing better than a pure modern.
- **Pure-didone option for the most austere lockup:** Didot LT Std or Bodoni* (used only at large display sizes; hairlines collapse below 28px on screen and below 18pt in print, so never set body or small UI in these).

If no license is available at build time, the system-safe fallback chain for mockups only is: `"Canela Deck", "GT Sectra Display", Didot, "Bodoni 72", Georgia, serif`. Final deliverables must use a licensed cut.

### 2.3 Letterforms and lockup

- All four characters set in capitals: **S O L E**.
- Optical alignment, not metric. The S and the E carry slightly past the cap-height baseline to sit visually level with O and L.
- The O is the anchor circle and rhymes with the Seal ring. Do not condense it.
- The L is the single vertical stroke that rhymes with the Seal numeral 1. Keep its stem the same weight as the heaviest vertical in the cut.

### 2.4 Tracking and size

| Context | Tracking | Min size |
|---|---|---|
| Display nameplate (deck cover, film, landing hero) | +120 to +180 (engraved-plate spacing) | 64px / 48pt |
| Standard lockup (deck running head, site nav) | +80 to +120 | 24px / 18pt |
| Caption / footer mark | +40 to +60 | 14px / 11pt |

Never set SOLE below 14px / 11pt. Below that it reads as text, not a mark, and the engraving cue dies.

### 2.5 Clear space

Minimum clear space on all sides = the cap-height of the wordmark (1 x cap-height). Preferred clear space for hero placements = 2 x cap-height. Nothing enters this zone except the Seal when the two are intentionally locked up (see 4.5).

### 2.6 House signature

The full entity is **SOLE HOUSE**. Lockup: SOLE set as the nameplate, HOUSE set in the body grotesque (see section 5) in all caps at roughly 0.4x the SOLE cap-height, tracked +200, sitting on the SOLE baseline to the right with one cap-height of space between them, or centered directly beneath on a second line. The strategic act **The Sole Claim** is always set in the body grotesque, italic optional, never in the didone (it is language, not a mark).

---

## 3. COLOR TOKENS

Five locked tokens. No sixth color enters the system without breaking the world. No teal, no orange, no SaaS gradient, no modern-minimal startup white.

| Token | Name | Role | Hex | RGB | Notes |
|---|---|---|---|---|---|
| `--sole-ink` | Ink black | Primary ground | `#0A0A0B` | 10, 10, 11 | The dark room. Default background everywhere. |
| `--sole-bone` | Bone white | Primary light / type on ink | `#EDE8DD` | 237, 232, 221 | Warm off-white. The shaft of light. Never pure #FFFFFF. |
| `--sole-brass` | SOLE brass | The one struck metal | `#A8843C` | 168, 132, 60 | The single accent. The Seal, the strike, the rule lines. Used sparingly, like real gold. |
| `--sole-concrete` | Concrete grey | Connective neutral | `#6B6B6E` | 107, 107, 110 | Cool stone. Secondary type, captions, dividers, metadata. |
| `--sole-shadow` | Vault shadow | Depth / panels | `#1C1C1E` | 28, 28, 30 | Charcoal. Raised panels, cards, redaction-bar fill, the step above ink. |

### 3.1 Usage law

- **Ink is the default ground. Always.** Light is the exception, earned by the shaft.
- **Brass is precious.** Treat it as struck metal. One brass element should dominate any given view: the Seal, or a single rule line, or the wordmark strike, not all at once. If two brass elements compete, demote one to concrete.
- **Bone carries all primary reading.** Body copy is bone on ink, or ink on bone for inverted plates.
- **Concrete is the in-between voice.** Metadata, captions, secondary labels, dividers. Never primary headlines.
- **Shadow builds depth, not contrast.** It is the panel that sits one step off the ink ground so a card reads as raised, like a drawer pulled from the archive wall.

### 3.2 Contrast and accessibility

- Bone `#EDE8DD` on ink `#0A0A0B`: contrast ratio ~17:1. Passes AA and AAA for all text.
- Concrete `#6B6B6E` on ink `#0A0A0B`: ratio ~4.0:1. Use for large text (24px+) and metadata only, not body paragraphs.
- Brass `#A8843C` on ink `#0A0A0B`: ratio ~5.6:1. Passes AA for normal text but reserve for emphasis and marks, not running copy.
- Ink on bone for inverted plates: ratio ~17:1, full pass.

### 3.3 Brass as gradient (the one permitted gradient)

The only sanctioned gradient is a brass-on-brass metallic sheen used exclusively on the Seal and on struck type, never on backgrounds or buttons. Build it as a linear or angular gradient across three stops to fake a struck-metal highlight:

- Stop 0%: `#7A5E27` (deep brass, the shadowed edge)
- Stop 50%: `#C9A65A` (lit face)
- Stop 100%: `#8A6B30` (return to shadow)

Angle the gradient to match the world's top-light (light from above, roughly 75 to 90 degrees). This is metal catching the shaft, not a UI gradient.

---

## 4. THE SINGULAR SEAL · CONSTRUCTION

The Seal is the hero artifact: a struck brass medallion engraved with the numeral **1** rendered as a single unbroken vertical stroke, set inside a circular vault-door ring. The category of one, made physical and sealed. It is the icon of the system; the wordmark is the nameplate. They are separate assets that may lock up but are designed independently.

### 4.1 Anatomy

```
        outer ring (vault-door collar)
       ┌───────────────────────┐
       │   ●  ●  ●  ●  ●  ●     │   bolt-stud dots on the ring
       │  ┌─────────────────┐   │
       │  │                 │   │   inner field (ink or struck-brass)
       │  │        │        │   │
       │  │        │        │   │   the numeral 1 = one unbroken vertical stroke
       │  │        │        │   │
       │  │                 │   │
       │  └─────────────────┘   │
       │   ●  ●  ●  ●  ●  ●     │
       └───────────────────────┘
```

### 4.2 Proportions (master on a 100-unit grid; scales to any size)

Define the full medallion diameter as **D = 100 units**.

| Element | Spec |
|---|---|
| Outer ring diameter | 100 units (D) |
| Outer ring stroke width | 6 units (the collar of the vault door) |
| Inner field diameter | 76 units (centered) |
| Ring band (gap between outer edge and inner field) | 12 units on each side |
| Bolt-stud dots | 12 dots, each 2.5 units diameter, evenly spaced at 30-degree intervals around the ring band centerline (radius 44 units from center) |
| Numeral 1 stroke height | 48 units (centered vertically in the inner field) |
| Numeral 1 stroke width | 6 units (matches the ring stroke, so the mark reads as one struck weight) |
| Numeral 1 position | Dead center. No serif, no flag, no base. A single unbroken vertical bar. This is the whole point: the 1 is not a typographic glyph, it is a stroke. |
| Optional engraved hairline | A 0.75-unit concentric hairline ring at 84 units diameter, separating the inner field from the ring band, for the engraved-vitrine cue. Use only at large sizes (Seal rendered above 240px). |

The numeral stroke and the ring stroke share the same 6-unit weight on purpose: the eye reads the entire Seal as one continuous act of striking, ring and numeral struck in the same pass.

### 4.3 Color builds

- **Embossed / printed-deck build:** brass `#A8843C` mark and ring on ink `#0A0A0B` field, with the struck-metal gradient (3.3) on the ring and numeral for the lit-from-above effect.
- **Watermark build (on world stills):** brass at 12 to 20 percent opacity, or bone at 8 to 14 percent opacity, struck into a lower corner. Must be felt, not read. Never competes with the single object under the light.
- **Reverse build:** ink mark on bone field, for the rare inverted plate.
- **Live-strike build (landing):** see 4.4.

### 4.4 The strike (locked-to-live mechanic)

On the live landing the Seal sits **locked and embossed during the pre-launch window**, then **visibly strikes from locked to live at go-live**. Two states:

- **Locked state:** Seal rendered in concrete `#6B6B6E` and shadow `#1C1C1E` only. Desaturated, recessed, embossed into the surface as if not yet struck. The numeral is present but reads as a debossed groove, no brass.
- **Live state:** the brass strikes in. The numeral and ring fill with brass `#A8843C` and the struck-metal gradient, a single hard top-light glint passes across the face left to right, and the Seal settles raised and lit. This is the go-live signal and the reason the launch date is real.

Build the transition in After Effects (section 8). On the web it can be a pre-rendered transparent-background video or a Lottie/SVG sequence triggered by the n8n countdown.

### 4.5 Wordmark + Seal lockup

When SOLE and the Seal appear together:

- **Vertical lockup (preferred, hero):** Seal centered above, SOLE wordmark centered beneath, separated by 1 Seal-radius of space. Seal diameter roughly equal to 1.5x the SOLE cap-height.
- **Horizontal lockup (nav, footer):** Seal to the left, SOLE to the right, vertically centered on the Seal, separated by 0.5 Seal-diameter. Seal diameter roughly equal to 1.4x the SOLE cap-height.
- Never overlap the two. Never tint the Seal to match a non-token color. Never rotate the numeral; the stroke is always perfectly vertical.

---

## 5. TYPE SYSTEM

A two-voice system: a high-contrast didone display (the engraved nameplate register) paired with a quiet grotesque for body and UI. The contrast between the two voices is the typographic tension of the whole house: struck heritage against clean modern silence.

### 5.1 Display (the engraved voice)

- **Cut:** Canela Deck (Commercial Type), Bold / Black. Alternates: GT Sectra Display, Ogg, Tiempos Headline. Pure-didone-only-at-large: Didot, Bodoni.
- **Use for:** the SOLE wordmark, deck cover titles, film titles, landing hero headline, section openers, the Sole Claim sentence when set as a hero statement.
- **Setting:** generous tracking on caps (+80 to +180), tight leading (0.95 to 1.05x), never justified. Headlines are short, declarative, struck.

### 5.2 Body / UI (the quiet voice)

- **Cut:** Söhne (Klim) or Neue Haas Grotesk. Approved alternates: Suisse Int'l, Founders Grotesk, GT America. System-safe fallback for mockups only: `Inter, "Helvetica Neue", Arial, sans-serif`.
- **Use for:** all body copy, the doctrine one-pager, deck running text, captions, metadata, UI labels, buttons, booking flow, HOUSE in the signature, the Sole Claim when set as body.
- **Setting:** normal tracking (0 to +10 for caps labels, +200 for the HOUSE signature and metadata micro-labels), leading 1.4 to 1.6x for paragraphs, ragged-right.

### 5.3 Type scale (modular, ratio 1.25 major-third on web; print in parallel)

| Token | Voice | Web size / line-height | Print equivalent | Use |
|---|---|---|---|---|
| `display-hero` | Didone | 72px / 1.0 | 56pt / 60pt | Landing hero, deck cover, claim-as-hero |
| `display-1` | Didone | 48px / 1.05 | 36pt / 40pt | Section openers |
| `display-2` | Didone | 32px / 1.1 | 24pt / 28pt | Sub-openers, pull statements |
| `body-lead` | Grotesque | 21px / 1.5 | 13pt / 19pt | Lead paragraph, doctrine summary |
| `body` | Grotesque | 17px / 1.55 | 10.5pt / 16pt | Default body |
| `caption` | Grotesque | 14px / 1.45 | 9pt / 13pt | Captions, metadata, footer |
| `micro-label` | Grotesque caps | 11px / 1.3, tracked +200 | 7pt / 11pt, tracked +200 | Drawer labels, redaction tags, system metadata |

The `micro-label` token is the connective tissue of the archive look: small, wide-tracked, concrete-grey caps that label the world like a vitrine plaque or an archive drawer.

---

## 6. LAYOUT GRID

### 6.1 Print / deck grid

- **Format:** the Category Brief deck and one-pager build on a 12-column grid with a wide outer margin (the vault is vast; give the object room).
- **Margins:** outer margin = 10 percent of the page width on all sides minimum. The dark ground bleeds full; the type column sits inside the generous margin so the object floats in space.
- **Columns:** 12 columns, gutter = 2 percent of page width. Most content occupies the center 6 to 8 columns. Single-object hero pages use a single centered column.
- **Baseline grid:** 8pt baseline, all body type snaps to it.
- **Vertical rhythm:** content sits low and centered or low-and-left, not top-aligned. The plinth is near the lower third; weight rests at the bottom like an object on a base.

### 6.2 Screen grid (landing, Figma)

- **Container:** max-width 1280px, centered, on a full-bleed ink ground.
- **Columns:** 12-column auto-layout, 80px outer padding desktop, 24px mobile, 24px gutter.
- **Spacing scale (Figma variables):** 4, 8, 16, 24, 40, 64, 104, 168 (an 8-base scale with a near-golden jump at the top for the dramatic empty space the world needs).
- **Vertical sections:** each landing section is a full-viewport dark stage with one object/idea under light. Scroll moves the visitor through a sequence of lit objects, not a wall of content.

### 6.3 The single-object rule applied to grid

On any hero or section-opener, one element is the lit object. Everything else recedes into the ink. Resist the instinct to fill columns. Empty dark space is the product looking expensive.

---

## 7. THE REDACTION-BAR DEVICE

A graphic device borrowed from the archive/heist/private-bank world: a solid bar that conceals, classifies, and signals that information is held and earned, not given. It is how SOLE shows that the claim is sealed before it is revealed, and how the faceless constraint becomes a deliberate aesthetic instead of an absence.

### 7.1 Construction

- **Fill:** vault shadow `#1C1C1E` for a recessed redaction, or ink `#0A0A0B` for a flush one, or brass `#A8843C` for a struck/declassified redaction (rare, high-impact).
- **Shape:** hard rectangle, zero corner radius. The redaction bar is never rounded. Sharp edges only.
- **Proportion:** height = the cap-height or x-height of the text it covers, plus 0.25x padding top and bottom. Length = exactly the run of text or object it conceals, plus 0.5x cap-height bleed on each end.
- **Optional tag:** a `micro-label` in concrete grey may sit just above or below the bar (e.g., `CLAIM · SEALED`, `HOUSE 001`, `CLASSIFIED UNTIL GO-LIVE`).

### 7.2 Usage

- **Conceal the claim pre-reveal:** on the deck cover, the landing pre-launch state, or teaser assets, the Sole Claim sentence sits under a redaction bar. The reveal (deck turn, scroll, go-live) lifts or dissolves the bar. This dramatizes that the claim is the held thing.
- **Faceless framing:** where a real face would conventionally appear, a redaction bar stands in deliberately. This converts the faceless-safe constraint into a signature, not an apology. Never use a redaction bar to hide a real face you actually have; the system has no real faces by construction. The bar marks where a lesser brand would have put a stock face and SOLE refused.
- **Metadata and classification:** redaction-style `micro-label` tags throughout the deck and site label assets like archive entries (`WORLD · LOCKED`, `RECUT · 01 / 01`).

### 7.3 Restraint

Maximum one redaction bar as a focal device per view. Used everywhere it becomes a gimmick and the world cheapens. It is a held secret, not a texture.

---

## 8. EMBOSSING RULES

Surfaces are embossed, not printed. This is the single most important material cue separating SOLE from every templated competitor. Type, the Seal, and rule lines should feel struck into metal or pressed into stone.

### 8.1 The light model (locked)

All emboss and deboss in the system obeys one light source: **hard light from directly above, roughly 75 to 90 degrees**, matching the Vault Room's top-light shaft. Highlights fall on the top edge of a raised form; shadows fall on the bottom edge. Never light from the lower-left default. If the whole system lights from above, the world stays coherent.

### 8.2 Emboss (raised) recipe

For a raised brass or bone element on ink:

- Top edge highlight: 1 to 2px (or 0.5pt) inner bevel highlight at the lit color (bone, or brass gradient stop `#C9A65A`).
- Bottom edge shadow: 1 to 2px inner shadow toward `#000000` at 60 to 80 percent.
- Subtle drop shadow beneath the element: blur 4 to 12px, distance 2 to 4px straight down, color `#000000` at 40 to 60 percent, to lift it off the ground.

### 8.3 Deboss (pressed-in) recipe

For a pressed-in / locked / not-yet-struck element (the locked Seal state, redaction grooves):

- Top edge shadow: pressed forms catch shadow on the top inner edge.
- Bottom edge highlight: a thin highlight on the bottom inner edge.
- This is the inverse of emboss and reads as carved into the surface. Use it for the pre-strike locked state so the live strike (raising it into brass) reads as a real change.

### 8.4 Tooling

- **Adobe Photoshop:** Layer Styles → Bevel & Emboss (Style: Inner Bevel for raised type/Seal; Style: Pillow Emboss or Emboss for pressed), with Global Light angle set to 90 degrees, plus a tight Inner Shadow and Drop Shadow per the recipe. Save as a layer style preset named `SOLE_EMBOSS_RAISED` and `SOLE_DEBOSS_PRESSED`.
- **Adobe Illustrator:** use the Appearance panel with two offset fills (a lit-color fill offset up 1px, a shadow-color fill offset down 1px) for crisp vector emboss that survives scaling. Group as a graphic style `SOLE Emboss`.
- **Figma:** Inner Shadow (bottom, dark) + Inner Shadow (top, light) + Drop Shadow (straight down). Save as an effect style `Emboss / Raised` and `Emboss / Pressed`. Bind shadow colors to the color variables so a token change ripples through.
- **After Effects (the strike):** animate the deboss-to-emboss transition by keyframing inner-shadow direction and a brass fill-in, plus a single hard highlight sweep (a thin bright bar masked across the Seal face) timed to the strike beat. Add a low, dense impact sound on the strike frame.

### 8.5 Print production note

For physical deliverables (the Category Brief cover, the Sovereign-tier machined brass object), specify true blind deboss or brass foil emboss with the printer/machinist. The on-screen emboss is the proxy; the physical artifact is the real strike. The Sovereign brass Seal is machined to the section 4.2 proportions in solid brass.

---

## 9. MOTIF KIT

Locked recurring elements. Compose with these; do not invent new ones.

- **The shaft:** a single hard column of top-light striking one object on a plinth. The defining composition. Recurs in every world still and the film.
- **The plinth:** a low stone or brass base the object rests on. Weight sits low.
- **Vault-door circular geometry:** the ring of the Seal, echoed in arches, lenses, drawer pulls, and round vitrines throughout the world.
- **Archive drawers:** flat-file / safe-deposit drawer fronts with `micro-label` plaques. The connective texture of the world and the home of the redaction tags.
- **Polished stone floor + long shadows:** reflective dark floor, one long shadow cast by the single object.
- **Hairline rules in brass:** a single thin brass rule as a divider or underline. One per view, precious.
- **Embossed surfaces:** everything material is struck or pressed, never flat-printed.

---

## 10. THE WORLD STILLS (BRAND WORLD BIBLE LINK)

12 to 16 world-built stills, all in The Vault Room, all faceless, all the single-object-under-light composition. Generated on the operator's stack (Higgsfield plates, Blender hero-object renders), graded to the five-token palette in the Adobe stack. Every still carries the Seal watermark (4.3). Identity rule: zero exposed real faces, ever; where a subject would be, use the lit object, a silhouette in deep shadow, or a redaction bar. The stills are configuration of the pre-rigged world, not new creation per client. Hold the world strict; let only the claim and copy vary.

---

## 11. FIGMA AND ADOBE IMPLEMENTATION CHECKLIST

### 11.1 Figma file setup

1. **Variables (Color):** create the five tokens as variables: `sole/ink`, `sole/bone`, `sole/brass`, `sole/concrete`, `sole/shadow`, plus the three brass-gradient stops. One collection, one mode for now; a `Locked` and `Live` mode pair can drive the strike states.
2. **Variables (Number):** the spacing scale (4 → 168) and the type scale as number variables.
3. **Text styles:** build all seven type tokens (section 5.3) as Figma text styles, mapped to the licensed cuts (or fallback chain in mockups).
4. **Effect styles:** `Emboss / Raised`, `Emboss / Pressed`, `Strike Glint` per section 8.4, colors bound to variables.
5. **Components:** Seal (variant: Locked / Live), Wordmark (variant: standalone / SOLE HOUSE / Seal lockup vertical / Seal lockup horizontal), Redaction Bar (variant: shadow / ink / brass-struck, with optional micro-label slot), Section Stage (full-bleed ink frame with single-object slot and generous margin), Drawer Label, Brass Rule.
6. **Grid:** 12-column layout grid style, 1280 max-width, 80/24 padding, 24 gutter; mobile variant.
7. **Landing:** assemble the single-page site from Section Stage components; export to Vercel build. Keep the pre-launch (Locked) and go-live (Live) frames as the two modes.

### 11.2 Adobe file setup

1. **Illustrator:** master the Seal on the 100-unit grid (section 4.2) as a single artboard, with the `SOLE Emboss` graphic style and the brass gradient swatch group. Master the wordmark and all lockups here. Export EPS/SVG for the web and PDF/X for print. This is the source of truth for the marks.
2. **Photoshop:** the `SOLE_EMBOSS_RAISED` and `SOLE_DEBOSS_PRESSED` layer-style presets, Global Light at 90 degrees. Used for compositing the Seal and struck type onto world stills and the deck cover, and for the watermark passes on the 12 to 16 stills.
3. **InDesign:** the Category Brief deck on the 12-column grid (6.1), 8pt baseline, paragraph and character styles mapped to the type tokens, color swatches = the five tokens as spot-named swatches (`SOLE Ink`, `SOLE Bone`, `SOLE Brass`, `SOLE Concrete`, `SOLE Shadow`). Seal embossed on the cover (foil/deboss spec in the print note, 8.5).
4. **After Effects:** the strike composition (deboss-to-emboss + brass fill + highlight sweep + impact) for the manifesto film's final frame and the landing's locked-to-live transition. Premiere for the film grade and assembly. ElevenLabs voice, scored.
5. **Token parity:** the five hex values are identical across Figma variables, Illustrator swatches, Photoshop, and InDesign. One source list (section 3). Never eyeball a brass.

---

## 12. DO / DON'T

### Do

- Default every surface to the ink ground and earn the light.
- Treat brass as real struck metal: one dominant brass element per view, used like gold.
- Keep the numeral 1 a single unbroken vertical stroke, always perfectly vertical, ring and stroke at the same struck weight.
- Light everything from directly above (75 to 90 degrees). One light model, whole system.
- Emboss and deboss; make type and marks feel struck into metal or pressed into stone.
- Hold the single-object-under-light composition. Leave dark space empty.
- Use the redaction bar to dramatize a held claim and to turn the faceless constraint into a signature.
- Keep the Vault Room strict. Vary only the claim and the per-client copy.
- Set headlines short, declarative, struck, in the didone with wide tracking.
- Keep the wordmark and the Seal as separate, independently designed assets that lock up cleanly.

### Don't

- Don't introduce a sixth color. No teal, no orange, no SaaS gradient, no startup white (`#FFFFFF`), no neon, no reactor-cyan dev-tool look.
- Don't use pure white anywhere; bone `#EDE8DD` is the lightest value.
- Don't round the redaction bar, the Seal ring, or any corner that should read as struck. Sharp edges.
- Don't let two brass elements compete in one view.
- Don't give the numeral 1 a serif, a flag, a base, or any glyph styling. It is a stroke, not a font character.
- Don't light from the lower-left default; it breaks the world instantly.
- Don't set the didone below 28px / 18pt or in body copy; hairlines collapse.
- Don't set SOLE below 14px / 11pt or it stops reading as a mark.
- Don't fill columns to look busy; empty dark space is the product looking expensive.
- Don't use a redaction bar as wallpaper or to hide a real face you actually have. The house has no real faces by construction.
- Don't expose any real face, operator or client, anywhere, ever.
- Don't render the strike before go-live; the locked-to-live transition is the launch signal and only fires once.
- Don't drift the world for variety. Drift is the primary failure mode. The sameness is the moat.

---

## 13. ONE-LINE GOVERNANCE

If a design decision is unclear, ask one question: does this make the client feel like the single object under the light, already struck, already archived, already the only one? If not, cut it.
