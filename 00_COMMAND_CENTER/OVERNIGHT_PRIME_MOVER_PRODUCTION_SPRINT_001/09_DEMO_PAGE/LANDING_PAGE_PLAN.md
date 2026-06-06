# SOLE HOUSE · LANDING PAGE PLAN
## Single-page private demo site · The Vault Room · Internal build only

---

### 0. SHIP NOTE (read first)

This is a **static, local-only demo**. It is built in Figma and exported to a single static HTML/CSS bundle that runs from `file://` or a local preview server. For this internal demo:

- **No hosting.** No Vercel deploy, no Netlify, no public URL. The production brief calls for Vercel; the demo deliberately does not ship there.
- **No real domain.** Placeholder wordmark only (`SOLE HOUSE`). No DNS, no `sole.com`, no purchase. The name still sits behind the open availability gate (backups VANTABLE / ONLIQ / MONARCH ROOM).
- **No live booking endpoint.** The single CTA is wired to a **mock booking modal** that captures intent locally and shows a confirmation state. The real n8n intake flow is documented in section 9 as the handoff spec, not built here.
- **Faceless-safe.** Zero real client face, zero operator identity, zero shoot footage. Every visual is a world-built Vault Room asset or the Singular Seal. The manifesto film slot plays an AI-voiced, world-plate film with no human face on either side.
- **Nothing is posted or sent.** This page exists to be walked through in a private demo, on one screen, by one person.

One page. One scroll. One claim. One call to action.

---

### 1. PAGE ARCHITECTURE (top to bottom)

| # | Section | Job | CTA present |
|---|---|---|---|
| 1 | Hero | State the Sole Claim. Strike the Seal. | Primary CTA (anchors to booking) |
| 2 | Manifesto Film | Make the claim feel already true and already expensive | Inline, secondary (play) |
| 3 | The Problem | Name the buyer's private fear (commoditization in the AI flood) | None |
| 4 | The 72-Hour System | Show the three-day machine and the six sealed deliverables | None |
| 5 | The Three Tiers | Publish the price and the closed scope | Per-tier CTA (anchors to booking) |
| 6 | Anti-Agency Comparison | Convert the skeptic against the slow, expensive agency | None |
| 7 | The Seal | Hero artifact close. The category of one, made physical | None |
| 8 | FAQ / Objections | Clear the standing objections before the CTA | None |
| 9 | Booking CTA | The one conversion. Book the call | Primary CTA (opens booking flow) |
| 10 | Footer | Wordmark, capacity gate line, faceless-safe legal line | None |

The page has exactly **one conversion goal**: book the qualification call. Every CTA on the page points to the same destination (section 9). There is no secondary funnel, no newsletter, no chat widget.

---

### 2. EXACT COPY · SECTION BY SECTION

> Voice rules for all copy below: premium register, declarative, short. No em-dashes. No exclamation points. No SaaS filler ("supercharge," "unlock," "revolutionary"). The page should read like the lobby plaque of a private bank, not a startup landing page.

---

#### SECTION 1 · HERO

**Eyebrow (small caps, brass):**
SOLE HOUSE · THE 72-HOUR REPOSITIONING HOUSE

**Headline (didone display, full bleed):**
We do not make you better.
We make you the only one.

**Subhead (grotesque, bone white):**
In three days, SOLE rebuilds an established business as a category of one. One claim. One world. One name the market cannot copy.

**Primary CTA button (brass fill, ink text):**
Claim your category

**Supporting line under CTA (concrete grey, small):**
One HOUSE at a time. Price and scope published below.

**Seal behavior:**
The Singular Seal sits top-right of the hero frame, embossed and **locked** in the pre-launch state (engraved into stone, low brass glow). On a defined scroll or load trigger it performs the strike: locked to live, the brass igniting to full saturation for ~1.2s, then settling. This is the page's one motion moment and the proof that the launch date is real.

---

#### SECTION 2 · MANIFESTO FILM

**Section eyebrow:**
THE PREMIERE

**Headline:**
This is not a press release. It is a premiere.

**Film embed slot:**
- A single 16:9 frame, full content width, centered, set on ink black with a thin brass hairline border.
- Poster state: the final frame of the film, the Seal struck, with a centered play control (brass ring, single triangle).
- The 60 to 90 second manifesto film: AI-voiced (ElevenLabs), scored, graded, assembled from Higgsfield Vault Room plates and Blender hero-object renders. No human face. The Seal strikes on the final frame as the sign-off.
- **Demo wiring:** local `<video>` element pointing at the rendered film file in the demo bundle (`/assets/manifesto_film.mp4`). No external player, no embed script, no tracking. Plays muted-to-sound on click; never autoplays with sound.

**Caption under film (concrete grey, small):**
60 to 90 seconds. Scored, graded, sealed. The world is built, not filmed. No faces, on either side of the camera.

---

#### SECTION 3 · THE PROBLEM

**Eyebrow:**
THE PROBLEM

**Headline:**
You are competent, profitable, and indistinguishable.

**Body (two short stacked paragraphs):**
You do good work. So does every competitor on the same template, with the same stock photography, the same three adjectives, and a slightly different logo. The market cannot tell you apart, so it decides on price.

AI just made "good enough" infinite and free. The cheaper option now looks identical to yours on the surface. The only position left that cannot be copied is being the only one. Not better. The only.

**Pull line (brass, set apart):**
A single quarter of "they picked the cheaper option" makes this fee look trivial.

---

#### SECTION 4 · THE 72-HOUR SYSTEM

**Eyebrow:**
THE SYSTEM

**Headline:**
One strategic act. Six sealed deliverables. Three days.

**Lead line:**
SOLE performs one act: The Sole Claim. A single sentence that renames your market so you become its only legitimate occupant. Everything else exists to make that claim feel already true and already expensive.

**The three-day timeline (3 columns or 3 stacked blocks):**

**DAY 1 · THE VERDICT**
The Sole Claim and Positioning Doctrine. A one-sentence renaming of your business plus a one-page doctrine: who you are the only one for, the enemy you reject, the new category you now own. Delivered as a strategic verdict, not a mood board. It clears a hard positioning gate before a single frame is rendered. No claim, no build.

**DAY 2 · THE WORLD**
The Brand World Bible and the Manifesto Film. 12 to 16 world-built stills in a single signature world, the Vault Room, plus color, type, and motif systems. A 60 to 90 second scored manifesto film. All synthetic, all world-built, zero exposed faces.

**DAY 3 · THE SEAL**
The Category Brief, the Live Landing, and the Offer and Booking Layer. A deck you can hand to a board, a banker, or an acquirer. A single-page site carrying the claim and the film. Premium offer copy with an intake flow. The Seal strikes on the final frame. One timestamped handoff with a change-log.

**The six deliverables (compact sealed list, Seal bullet on each):**
1. The Sole Claim + Positioning Doctrine
2. The Brand World Bible (12 to 16 Vault Room stills, color, type, motif)
3. The Manifesto Film (60 to 90 seconds, AI-voiced, scored, sealed)
4. The Category Brief (board-ready repositioning deck)
5. The Live Landing (single page, claim, film, one call to action)
6. The Offer + Booking Layer (premium offer copy, intake flow)

**Discipline line (concrete grey, small):**
Price published. Scope published and closed. One recut only, no revisions inside the 72-hour window. Every deliverable clears the readiness gate before handoff.

---

#### SECTION 5 · THE THREE TIERS

**Eyebrow:**
THE LADDER

**Headline:**
A category of one cannot credibly be cheap.

**Three pricing cards (ink black, brass hairline, Seal at top of each):**

**SPRINT · $7,500**
The full repositioning system.
- The Sole Claim + Positioning Doctrine
- Brand World Bible (12 to 16 stills)
- The Manifesto Film
- The Category Brief deck
- The Live Landing
CTA: Book the Sprint

**SIGNATURE · $14,000**
Everything in Sprint, plus the launch machine.
- Extended film cut
- Full premium offer rewrite
- Booking and intake automation
- 90-day world-asset pack for ongoing content
CTA: Book the Signature

**SOVEREIGN · $25,000+**
Everything in Signature, plus the category locked to you.
- Named category audit of the whole market
- Exclusivity in category this quarter (your direct rival cannot buy this from us)
- Quarterly world-refresh retainer
- Launch-day drop ops layer (scheduled go-live, embargo email, countdown trigger, the Seal that strikes from locked to live at go-live)
- A machined brass Singular Seal shipped to your desk
CTA: Request Sovereign

**Footnote under cards (concrete grey, small):**
Premium price is the proof. One HOUSE at a time protects the promise. If your category needs real faces or regulated human-trust imagery, SOLE is not your house, and we will say so on the call.

---

#### SECTION 6 · THE ANTI-AGENCY COMPARISON

**Eyebrow:**
WHY NOT AN AGENCY

**Headline:**
One fraction of the price. One fraction of the time. Bookable on day four.

**Comparison table (two columns: THE AGENCY vs SOLE HOUSE):**

| | The agency | SOLE HOUSE |
|---|---|---|
| Timeline | 8 to 16 weeks, then it slips | 72 hours, fixed |
| Price | A moving five-figure-plus number | Published. $7,500 to $25,000+ |
| Scope | Creeps. Every change is a new invoice | Published and closed. One recut |
| Output | A logo refresh and a "fresh look" | A claim that renames your market |
| Faces | Stock photos and a costly shoot | World-built. Zero faces, zero shoot |
| The end | A deck and an open retainer | A sealed system, live, on day four |

**Closing line under table (brass):**
The agency sells you motion. SOLE sells you a verdict you repeat for years.

---

#### SECTION 7 · THE SEAL (HERO ARTIFACT)

**Eyebrow:**
THE SINGULAR SEAL

**Headline:**
One symbol. One numeral. One client.

**Body:**
A struck brass medallion engraved with the numeral 1 as a single unbroken vertical stroke, set inside a circular vault-door ring. The category of one, made physical. It is embossed on your deck cover, watermarked into every world still, and struck into the final frame of your film. In the Sovereign tier it ships as an actual machined brass object that sits on your desk.

**Visual:**
Large centered render of the Seal under a hard top-light shaft, on a plinth, in the Vault Room. Long shadow, polished stone floor. The single object under the light. This is the recurring composition of the entire brand, shown here at full scale.

---

#### SECTION 8 · FAQ / OBJECTIONS

**Eyebrow:**
BEFORE YOU BOOK

**Q. Three days is not enough to rebrand a business.**
Correct, and SOLE does not rebrand. It performs one strategic act and builds a pre-rigged world around it. The only bespoke unit of work is your claim. Everything downstream is configuration of a world that already exists. That is how the three days is real.

**Q. Is this just AI output?**
The production stack is invisible plumbing. The product is a strategic outcome: a single sentence that makes you uncopyable, proven out in a world that looks acquired and archived. You are buying the verdict and the world, not the tool that rendered it.

**Q. Why no photos of me, my team, or my clients?**
SOLE is faceless by construction. The Vault Room never needs a face. That keeps the world consistent, the timeline fixed, and your launch independent of a shoot. If your category legally requires real human-trust imagery, this is not your house.

**Q. What exactly do I get, and when?**
Six sealed deliverables in one timestamped handoff with a change-log, on day four. The Sole Claim and doctrine, the Brand World Bible, the manifesto film, the Category Brief deck, the live landing, and the offer and booking layer.

**Q. What if I want revisions?**
One recut only, inside the window. Scope is published and closed before you book. The fixed scope is what protects the fixed timeline and the fixed price.

**Q. Why is only one client served at a time?**
The capacity gate protects the promise. One HOUSE at a time means your 72 hours are yours. It is also why the Sovereign tier can guarantee your direct rival cannot buy this from us this quarter.

**Q. Why does it cost this much?**
Because a category of one cannot credibly be cheap. The premium is the proof. The pain you are solving is status, not cash, and the fee looks trivial against a single lost quarter to a cheaper competitor.

---

#### SECTION 9 · BOOKING CTA (the one conversion)

**Eyebrow:**
ONE CALL

**Headline:**
Claim your category.

**Subhead:**
One HOUSE at a time. Tell us about the business you are tired of being mistaken for. If SOLE is right for you, we book the 72 hours. If it is not, we will tell you on the call.

**Primary CTA button (brass fill, ink text, largest on page):**
Book the qualification call

**Microcopy under button (concrete grey, small):**
No deck pitch. No proposal theater. A short call to confirm fit, claim the slot, and set the start date.

**CTA wiring · see section 9 (CTA WIRING) below for the exact behavior.**

---

#### SECTION 10 · FOOTER

**Wordmark (didone, brass):** SOLE HOUSE

**Tagline line:** One claim. One world. One name the market cannot copy.

**Capacity line (concrete grey, small):** One HOUSE at a time. Price and scope published. Faceless by construction.

**Legal/demo line (smallest, concrete grey):** Internal demo. Static build, no hosting, no live booking. Name pending availability gate.

---

### 3. FIGMA HANDOFF SPEC

#### 3.1 File and page structure

- **File name:** `SOLE_HOUSE_Landing_Demo`
- **Pages:**
  1. `01 · Tokens` (color, type, effect styles, the Seal component)
  2. `02 · Components` (buttons, pricing card, FAQ row, comparison table, film frame)
  3. `03 · Landing / Desktop` (the single page, 1440 frame)
  4. `04 · Landing / Mobile` (390 frame)
  5. `05 · Booking Modal` (the mock booking flow states)
  6. `06 · Export` (flattened static export notes)

#### 3.2 Frames

| Frame | Width | Notes |
|---|---|---|
| `Landing / Desktop` | 1440 | Auto-layout vertical, section blocks stacked, 0 gap, full-bleed sections |
| `Landing / Mobile` | 390 | Same sections, single column, cards stack |
| `Booking Modal / Default` | 1440 overlay | Centered card, ink scrim at 80% |
| `Booking Modal / Confirmed` | 1440 overlay | Confirmation state, Seal struck |

Section blocks inside the desktop frame, each its own auto-layout container:
`sec-hero`, `sec-film`, `sec-problem`, `sec-system`, `sec-tiers`, `sec-compare`, `sec-seal`, `sec-faq`, `sec-booking`, `sec-footer`.

Vertical rhythm: section padding 160 top / 160 bottom on desktop, 88 / 88 on mobile. Content max-width 1120, centered, 32 side gutters desktop / 20 mobile.

#### 3.3 Color tokens (Figma variables · collection `sole/color`)

| Token | Hex | Role |
|---|---|---|
| `color/ink` | `#0A0A0B` | Ground. Page background, button text on brass |
| `color/bone` | `#EDE8DD` | Primary text on dark, light surfaces |
| `color/brass` | `#A8843C` | The one struck metal. CTAs, Seal, accents, hairlines |
| `color/concrete` | `#6B6B6E` | Connective neutral. Captions, microcopy, secondary text |
| `color/shadow` | `#1C1C1E` | Depth. Card fills, raised surfaces, vault shadow |

Discipline: no teal/orange, no gradients, no pure white. Brass is used sparingly and never as a large fill except the primary CTA and the Seal.

#### 3.4 Type styles (Figma text styles · `sole/type`)

Display family: a high-contrast **didone** (engraved nameplate register). Body family: a quiet **grotesque**.

| Style | Family | Size / line | Weight | Use |
|---|---|---|---|---|
| `type/display-xl` | Didone | 72 / 76 | Regular | Hero headline |
| `type/display-l` | Didone | 48 / 54 | Regular | Section headlines |
| `type/display-m` | Didone | 32 / 38 | Regular | Tier names, wordmark |
| `type/eyebrow` | Grotesque | 13 / 16, tracking +12% | Medium, all caps | Section eyebrows |
| `type/body` | Grotesque | 18 / 28 | Regular | Body copy |
| `type/body-s` | Grotesque | 14 / 22 | Regular | Captions, microcopy |
| `type/button` | Grotesque | 16 / 16, tracking +4% | Medium | CTA labels |

Demo font fallback: if the licensed didone is unavailable in the static export, substitute a free didone-adjacent face for the demo only and flag it. Body falls back to a system grotesque. Note the substitution in the Export page.

#### 3.5 Effect styles

- `effect/emboss-locked`: inner shadow + low brass glow for the locked Seal state.
- `effect/strike-live`: full brass fill, soft outer glow, used in the struck Seal state.
- `effect/hairline`: 1px brass stroke at 60% opacity for card and film borders.
- `effect/scrim`: ink black at 80% for the booking modal overlay.

#### 3.6 Components

| Component | Variants / props | Notes |
|---|---|---|
| `Seal` | `state = locked / struck`, `size = inline / hero / footer` | The Singular Seal. Numeral 1 as one vertical stroke inside vault ring |
| `Button / Primary` | `state = default / hover / pressed` | Brass fill, ink text, `type/button` |
| `Button / Tier` | `tier = sprint / signature / sovereign` | Outlined brass, fills on hover |
| `PricingCard` | `tier`, swaps label list + CTA | Ink shadow fill, brass hairline, Seal top |
| `FAQRow` | `state = collapsed / expanded` | Brass divider, didone question, grotesque answer |
| `CompareTable` | static | Two columns, agency vs SOLE, brass row dividers |
| `FilmFrame` | `state = poster / playing` | 16:9, hairline border, brass play ring |
| `BookingModal` | `state = default / confirmed` | Form fields + confirmation, scrim background |

#### 3.7 Imagery slots (all Vault Room, faceless)

- Hero background: Vault Room wide, one object under the top-light shaft, low key.
- Film poster: final frame, Seal struck.
- Seal section: Seal on plinth, hard top-light, long shadow.
- Tier cards: subtle Vault Room texture or flat ink, no photography of people.

Every image is a world-built asset. No stock, no faces, no operator identity. Source: Higgsfield Vault Room plates and Blender Seal renders, dropped into named Figma image fills.

---

### 4. STATIC / LOCAL EXPORT

- Export the desktop and mobile frames to a single static HTML/CSS bundle (Figma to code via the chosen export path, or hand-built static markup from this spec).
- Bundle layout:
  - `index.html`
  - `/styles.css` (tokens as CSS custom properties mirroring section 3.3 and 3.4)
  - `/assets/` (Vault Room stills, Seal renders, `manifesto_film.mp4`)
  - `/script.js` (Seal strike trigger, smooth-scroll anchors, mock booking modal only)
- Runs from `file://` or a local static preview. No build server required, no environment variables, no network calls.
- **No analytics, no fonts CDN at demo time** (fonts embedded or substituted locally), no third-party scripts. Fully self-contained so the demo runs offline.

---

### 5. CTA WIRING (the one call to action)

There is exactly one conversion: **Book the qualification call.** Every CTA on the page (hero, each tier card, booking section) points to the same flow.

**Demo behavior (what actually ships in this static build):**
1. All CTA buttons share the action `openBooking(tier)`.
2. Hero and booking-section CTAs pass `tier = "unspecified"`. Tier-card CTAs pass `tier = "sprint" | "signature" | "sovereign"`, pre-selecting the tier in the modal.
3. The action opens the `BookingModal / Default` overlay (ink scrim at 80%). The modal is a **mock**: fields for name, business, category they are tired of being mistaken for, revenue band, and tier interest.
4. On submit, the modal captures the payload to local state only (in-memory or `localStorage`, no network), then swaps to `BookingModal / Confirmed`: the Seal strikes from locked to live and the confirmation copy reads:

   > Your slot request is in. SOLE serves one HOUSE at a time. If the fit is right, we confirm your 72 hours and set the start date.

5. No email is sent. No calendar is booked. No endpoint is hit. This is a demo of the flow, not the live flow.

**Production handoff (documented here, not built in the demo):**
- The live build replaces `openBooking()` with an **n8n booking and intake flow** wired to the landing, per the brief's Offer + Booking Layer.
- n8n webhook receives the intake payload, runs the clean-disqualify check (real-faces / regulated-imagery buyers routed to a polite decline), books the qualification call against the operator's calendar, and confirms by email.
- Sovereign-tier requests additionally tag the lead for the launch-day drop ops layer (scheduled go-live, embargo email, countdown trigger).
- This wiring is specified for the production build only. The demo stops at the mock confirmation.

---

### 6. MOTION (kept to one moment)

The page has a single intentional motion: the **Seal strike** in the hero (and again on booking confirmation). Everything else is static, in keeping with the Vault Room's stillness. No parallax, no scroll-jacking, no animated gradients. The restraint is the brand.
