# Pixieset · Reset Gallery Configuration

**One-time setup, then duplicate per delivery. Target setup time: 30 minutes for the master template, then 5 minutes per gallery to deploy.**

The Pixieset gallery is the deliverable surface. It also runs the 48-hour upsell mechanic that is one of the documented leverage loops. Configure once correctly; the gallery template earns money on every shoot.

---

## Account-level settings

- [ ] Pixieset plan: **Pro** (required for Store with custom pricing). $30/month. Cheaper plans don't support the upsell pricing structure.
- [ ] Branding: charcoal #1A1A1A primary, white text, no logo on gallery (work-is-asset principle). Custom CSS if available, or use the Pixieset "Dark · Minimal" theme as base.
- [ ] Custom domain: `gallery.snipedmedia.com` (CNAME to Pixieset, set up after Google Workspace email is live)
- [ ] Studio name: `Sniped Media`
- [ ] Studio email: `bj@snipedmedia.com` (Google Workspace)
- [ ] Currency: USD
- [ ] Timezone: PT
- [ ] Default language: English

---

## Reset Gallery · master template

Create one Collection in Pixieset called `[TEMPLATE] Sniped Reset · DUPLICATE PER CLIENT`. Configure once; duplicate per delivery.

### Cover settings
- Cover image: black charcoal placeholder (replace per client with hero frame)
- Cover style: Full-screen · centered title · no overlay text other than client first name + shoot date
- Cover music: off

### Gallery settings
- Gallery title format: `[Client First Name] · The Reset · YYYY-MM-DD`
- Gallery description: `20 contracted final images. Additional 12-15 images available for purchase below for the next 48 hours.`
- Slug: `[firstname-lastname-yyyymmdd]` (e.g., `marcus-chen-20260620`)
- Privacy: **Password protected** (password emailed separately)
- Expiration: 14 days from delivery date
- Watermark: **OFF** (clients receive unwatermarked deliverables)
- Right-click: enabled (clients can save)
- Download: enabled · high-res JPG
- Pin protection: optional (low-friction; password handles auth)
- Layout: Grid · 4 columns desktop · 2 columns mobile · uniform crop

### Collections within the gallery

> **v2 OVERRIDE (2026-05-06):** The two-sub-collection structure (Selections · Additional) is superseded by the three-sub-collection structure per `/01_OFFERS/delivery_architecture_v2.md` Section 4.2. New structure: **Heroes · Selects · Proofs**. The 48-hour upsell window on Additional is retired; all three tiers live for 14 days, with Proofs auto-hiding at expiry. Read v2 Section 4.2 for the new gallery setup.

The v1 two-sub-collection text below is preserved for reference only.

### v1 (deprecated) · for reference only

The master Collection has TWO sub-collections:

**Sub-collection 1 · `Selections`** (the 20 contracted)
- Visibility: visible to client
- Download enabled: yes
- Store enabled: no (these are included in the contract)
- Display order: SNIPED's selected order (the strongest 5-7 frames first)

**Sub-collection 2 · `Additional`** (the 10-15 upsell)
- Visibility: visible to client (with banner: `Available for 48 hours · $80/image`)
- Download enabled: NO (purchase first)
- Store enabled: YES
- Display order: SNIPED's order

### Store / pricing config (the upsell mechanic)
- Store enabled: yes (on Additional sub-collection only)
- Pricing structure:
  - Single image: **$80**
  - 5-image bundle: **$300** (saves $100)
  - All-additional bundle: **$500** flat (only available if 8+ additional images, saves substantially)
- Payment processor: Stripe (connected to SNIPED Stripe account)
- Tax: configure per CA
- Auto-fulfillment: yes · digital download immediately on purchase
- Email receipt: branded, includes thank-you and a link to book a Reset for someone else (referral mechanic)

### Time-window mechanic for upsell
- Sub-collection `Additional` becomes hidden 48 hours after Sub-collection `Selections` was first visible to the client
- Use Pixieset's "Schedule visibility" feature on the Additional sub-collection: visible from delivery time + 0h to delivery time + 48h
- After 48h, only `Selections` remains visible for the remaining 12 days of the gallery window

### Client message
- Welcome email when gallery is delivered: branded, references password sent separately, names the 48-hour upsell window
- Auto-reminder: Pixieset built-in 24-hour-before-expiry reminder · enabled · custom subject `Sniped Reset · 24 hours left on your gallery`
- Custom 48-hour upsell warning: separately scheduled email at 24h post-delivery (use SNIPED's own email tooling, since Pixieset's reminder fires only at gallery-window-end, not at upsell-window-end)

---

## Per-delivery deployment (5 min, after Phase 4 of `SOP_capture_to_delivery.md`)

1. Duplicate the master Collection
2. Rename to `[Client First Name] · The Reset · YYYY-MM-DD`
3. Update slug
4. Upload 20 final images to `Selections` (drag from local · 4000px longest edge JPGs)
5. Upload 10-15 upsell images to `Additional`
6. Set cover to the strongest hero frame
7. Set password (8 characters · combination of letters and digits · use a password generator)
8. Schedule visibility on `Additional` for 48-hour window
9. Confirm gallery URL works in incognito
10. Capture the gallery URL into the Notion Galleries DB

---

## Operator Kit gallery (variant)

For Tier 2 deliveries, configure a separate template `[TEMPLATE] Sniped Operator Kit · DUPLICATE PER CLIENT`:
- 40 contracted images (vs 20)
- Gallery window: 30 days (vs 14)
- Upsell window: 7 days (vs 48 hours) · upsell volume tends to be higher per-shoot, longer window justified
- Upsell pricing: $120/image, $500 for 5, $900 for 10
- Sub-collections: `Look 1 · Studio` / `Look 2 · On-location` / `Look 3 · Detail` (per the agreed scope)
- Plus a `Recommendations` doc embedded as a PDF: SNIPED's recommendations for which image deploys where (LinkedIn header, podcast cover, deck portrait, press lead)

---

## Tracking · Notion Galleries DB integration

Each gallery's data flows into Notion manually for now (no Zapier yet):
- Pixieset URL → Galleries DB
- Delivered date → Galleries DB  
- Expiry date → Galleries DB · auto-calculated
- Upsell window status → Galleries DB · formula
- Upsell sequence sent (3 checkpoints) → Galleries DB
- Upsell revenue → Galleries DB · update at 48h close
- Conversion % → Galleries DB · formula

---

## What NOT to configure

- **Public homepage:** not needed for SNIPED. The Pixieset domain is gallery delivery only, not a portfolio destination. Portfolio lives on the Carrd one-pager (`/14_WEB/`).
- **Email collection lead-magnet:** not on Pixieset. The site Carrd handles inbound capture; Pixieset is for delivered clients only.
- **Mobile app branding:** not needed; clients access via web.
- **Print products:** Phase 1 ignores print fulfillment. The Art Series print workflow goes elsewhere (Year 2 buildout, with a dedicated lab partner like Chromira).
