# BASEPLATE_CARRD_BUILD_CHECKLIST

**Date:** 2026-05-26
**Status:** Build checklist. NOT a canon chunk. NOT a strategy change. Converts `CARRD_COPY_V1_CAPABILITY_DOSSIER.md` into exact build steps under the `PUBLIC_WRAPPER_DECISION.md` wrapper (BASEPLATE, founder-led, The Capability Dossier). Anchor-class: markdown-only, not chunked, not in the master files.
**Build target:** a live BASEPLATE Carrd one-pager that converts a critical-facilities staffing-firm owner into a booked 15-minute capability call in under 60 seconds. Target build time: 2 to 3 hours once images are picked. Tools: Carrd Pro ($19/yr) + Calendly + the already-claimed BASEPLATE domain.

---

## 0. Pre-build inputs (have these ready first)

- [ ] Confirm the exact already-claimed BASEPLATE domain string (from the BASEPLATE properties named in the brand bible). Write it here once confirmed: `__________` .
- [ ] Pick 1 approved, non-secure hero image (people/work, security-safe per section 06 rules). No secure floors, no equipment layouts, no client logos.
- [ ] Grab the BASEPLATE brand kit from `~/Downloads/BASEPLATE/`: the on-dark full-lockup PNG (`Logo Files/Transparent PNG/Verson 1-4.png`), the icon PNG (`Logo Files/Transparent PNG/Icon/Verson 1-4.png`), and a Profile crop (`Logo Files/Profile/Verson 1-5.jpg`). Keep `BASEPLATE.ai` / `BASEPLATE.eps` as masters; export an SVG from the .ai only if Carrd needs vector. Reference: `Downloads/BASEPLATE/Brand Bible.pdf`.
- [ ] Confirm Google Workspace from-address is live (bj@ the BASEPLATE domain) for the Calendly confirmations.
- [ ] Have the final Carrd copy open (`CARRD_COPY_V1_CAPABILITY_DOSSIER.md`).

## 1. Page URL / domain decision

- [ ] Carrd Pro plan ($19/yr) so a custom domain and SEO controls are available.
- [ ] Connect the **already-claimed BASEPLATE custom domain** (do not invent a new one, do not use a SNIPED domain). If a subdomain is cleaner for the test, use the root or a clean path on the BASEPLATE domain.
- [ ] Set the Carrd internal site name to `BASEPLATE`.
- [ ] Enable HTTPS/SSL (Carrd handles automatically once the domain is verified).
- [ ] Do not point any SNIPED/SNIPED Media domain at this page.

## 2. Carrd sections (build in this order, one scroll, no nav)

Build each as a Carrd "Section." Map 1:1 to the copy doc.

- [ ] **01 Hero:** BASEPLATE logo lockup (the on-dark Transparent PNG, small, top-left) · headline "The critical-facilities techs you want have other offers. This is how they choose you." · operator line (gray `#8C8C8C`) "BASEPLATE · capability proof for critical-facilities firms, built by an operator who has stood on the floor." · CTA button "Book a 15-minute capability call" · one approved non-secure hero image.
- [ ] **02 The problem:** the "you look like one more logo in the feed" paragraph.
- [ ] **03 The offer:** The Capability Dossier paragraph (premium proof asset, insider-to-insider, you own it).
- [ ] **04 Who it is for:** 3 bullets (staffing firms, specialty subs, owner-led firms) + the "not for cheap content/headshots/social management" line.
- [ ] **05 What is included:** the 6 deliverable bullets + the "larger engagements add" line.
- [ ] **06 Security-safe approach:** the "nothing sensitive is ever shown / you approve every image and line" paragraph.
- [ ] **07 Proof:** placeholder text "Sample dossier shown on the call. Built to your firm, never templated." (see section 7 below). No fake testimonials.
- [ ] **08 Process:** the 5 numbered steps (call, approve scope, produce, approve assets, delivery in 1 to 2 weeks).
- [ ] **09 CTA:** repeat the "Book a 15-minute capability call" button + the gray sub-text "Fifteen minutes. I will show you one sample and tell you honestly if it is a fit. Pilot from $2,500, scoped to one hard role."
- [ ] **10 FAQ:** the 6 Q&A pairs (is this photography / security+NDAs / how fast / cost / ownership / we already have marketing).
- [ ] **11 About / footer:** about line, footer line, legal fine print (see section 8 below).

## 3. Visual direction (locked to the BASEPLATE Brand Bible · `Downloads/BASEPLATE/Brand Bible.pdf`)

- [ ] Background: `#0F0F0F` near-black full-bleed (Brand Bible value, replaces the earlier #1A1A1A placeholder).
- [ ] Body text: `#FFFFFF` white; sub-text/operator line/FAQ answers: `#8C8C8C` gray.
- [ ] Accent: `#0055FF` electric blue, used sparingly only (the chevron in the mark, text links, one CTA hover state). Never a background wash. Restraint keeps it premium.
- [ ] Base theme: Carrd "Dark / Minimal" as the starting point; strip ornamentation; tune the palette to the four values above.
- [ ] Typography: Helvena (Brand Bible). Web fallback Helvetica / Arial / Inter. Large heavy/clean headline, restrained body. No gradients, no shadows, no emoji, no stock-marketing look. Aesthetic: Industrial Precision / Architectural Brutalism, the feel of high-end data center schematics or a luxury technical manual.
- [ ] BASEPLATE wordmark: small, top-left, the **Transparent PNG full lockup (on-dark version)** from `Logo Files/Transparent PNG/Verson 1-4.png`, not retyped text. No logo wall, no social icons.
- [ ] Hero image: single approved non-secure frame, low-opacity dark overlay so the headline reads. Optional subtle Ken Burns if Carrd supports it cleanly; otherwise static.
- [ ] CTA button: `#0F0F0F` fill, thin white border, white text; hover inverts (white or `#0055FF` fill, near-black text).
- [ ] One scroll, generous spacing, no nav bar. The whole page is a single vertical scroll.

## 4. Button links needed

All CTAs point to the same Calendly event. Three button instances:

- [ ] Hero CTA (01) link: `[CALENDLY_15MIN_CAPABILITY_CALL_URL]`
- [ ] Mid CTA (09) link: `[CALENDLY_15MIN_CAPABILITY_CALL_URL]`
- [ ] Footer CTA (11) link: `[CALENDLY_15MIN_CAPABILITY_CALL_URL]`
- [ ] No other outbound links on the page (no IG, no LinkedIn, no portfolio link). One action only.

## 5. Calendly setup

- [ ] Create event type: **"BASEPLATE Capability Call"**, 15 minutes.
- [ ] Location: phone or Google Meet (operator preference; phone is lower-friction for this buyer).
- [ ] Availability: off-hours blocks compatible with the day job (evenings/early mornings); buffer 10 min between calls.
- [ ] Intake questions on booking: (1) Company name, (2) Are you a staffing firm or a specialty subcontractor, (3) One hard role open or one bid coming up, (4) Best number.
- [ ] Confirmation email: from the BASEPLATE Google Workspace address; short, on-brand, restates the 15-min purpose.
- [ ] Reminders: 24-hour and 1-hour.
- [ ] Copy the public Calendly link into the three CTA buttons (section 4).

## 6. Pixieset link placeholders (NOT on the public page)

Pixieset is the private CRM/contract/delivery layer, not part of the public Carrd. Track these placeholders for the post-call flow:

- [ ] `[PIXIESET_SAMPLE_DOSSIER_GALLERY_URL]` · the private sample-dossier gallery shown/sent on the call (see section 7). Not linked publicly.
- [ ] `[PIXIESET_PILOT_CONTRACT_URL]` · Studio Manager contract template link, sent after a qualified call.
- [ ] `[PIXIESET_PILOT_INVOICE_URL]` · deposit/invoice link ($2,500 to $4,000), sent with the proposal.
- [ ] `[PIXIESET_DELIVERY_GALLERY_TEMPLATE]` · the branded private delivery gallery template, duplicated per client.
- [ ] These live in Google Workspace emails and the call, never on the Carrd.

## 7. Sample dossier placeholder

- [ ] Section 07 of the page shows text only: "Sample dossier shown on the call. Built to your firm, never templated." Do NOT embed a sample publicly and do NOT fabricate testimonials.
- [ ] Build one clearly-labeled illustrative sample dossier (composite example firm, no real client, watermark "SAMPLE · ILLUSTRATIVE FORMAT · NOT A REAL CLIENT", security-safe) and host it as a private Pixieset gallery: `[PIXIESET_SAMPLE_DOSSIER_GALLERY_URL]`.
- [ ] The sample is screen-shared or sent during the 15-minute call, not linked from the public page.

## 8. Footer / legal line

- [ ] About line: "BASEPLATE is the operator practice of Bryceden Jones. Capability proof and presence assets for the firms building and staffing critical infrastructure. Built insider-to-insider, security-safe, outcome-first."
- [ ] Footer line: "BASEPLATE · built by Bryceden Jones · [Book a 15-minute capability call]" (the call text links to Calendly).
- [ ] Footer logo: the same on-dark BASEPLATE Transparent PNG lockup as the hero, small.
- [ ] Legal fine print (smallest text): "BASEPLATE Media, LLC".
- [ ] No "SNIPED" or "SNIPED Media" anywhere on the page.

## 9. Mobile check

- [ ] Headline readable above the fold on a phone (no awkward wrap; reduce font size on the mobile breakpoint if needed).
- [ ] Hero image crops cleanly on portrait; subject/overlay still works.
- [ ] All three CTA buttons are full-width or clearly tappable on mobile (min ~44px tap height).
- [ ] Single-column stack; no horizontal scroll.
- [ ] FAQ readable; no text clipped.
- [ ] Test on at least one real phone, not just the Carrd preview.

## 10. Publish checklist

- [ ] Custom BASEPLATE domain connected and resolving with HTTPS.
- [ ] All three CTA buttons open the live Calendly event (click each).
- [ ] Calendly event live, availability set, intake questions in, confirmation + reminders firing (book a test slot, then cancel it).
- [ ] No placeholder tokens left visible on the public page (the `[PIXIESET_...]` and `[CALENDLY_...]` tokens are internal; confirm none render on the page).
- [ ] No "SNIPED"/"SNIPED Media" text or domain anywhere.
- [ ] SEO title: "BASEPLATE · Capability Proof for Critical-Facilities Firms". Meta description: one line from the operator line. Favicon: the BASEPLATE icon PNG (`Logo Files/Transparent PNG/Icon/Verson 1.png`, or whichever icon version reads cleanest at 32px).
- [ ] Social/share preview (OG image): a `Logo Files/Profile/Verson 1-5.jpg` crop or the approved non-secure hero frame. No sensitive content.
- [ ] Mobile checked on a real device (section 9).
- [ ] Spelling/grammar pass; confirm price reads "Pilot from $2,500".
- [ ] Publish. Then paste the live URL into the outreach scripts and the Calendly is the only next step a visitor can take.

---

## Guardrails (unchanged)

This is a build translation, not a strategy change. Wrapper: BASEPLATE, founder-led (Bryceden Jones), The Capability Dossier as the offer; a 30-day test deployment, not a permanent identity lock. No SNIPED/SNIPED Media on the page. No photography / content / headshot framing (the deliverable is a capability dossier; media is the instrument). No platform / registry / network claim. Security-safe by design: no secure floors, no equipment layouts, no client names, nothing under NDA, non-secure imagery only, buyer approves every asset. No fake proof or testimonials. Old SNIPED/BASEPLATE brand material is historical evidence, not law. Bible held until a deliberate SPIRITUAL_FOUNDATION decision. Not chunked, no master/raw changes, no new domain; total_chunks unchanged at 1,837. Feeds the 30-day run in `EXECUTION_RUN_30DAY_CAPABILITY_DOSSIER.md`; results log to `PROOF_LOOPS_30_60_90.md`.
