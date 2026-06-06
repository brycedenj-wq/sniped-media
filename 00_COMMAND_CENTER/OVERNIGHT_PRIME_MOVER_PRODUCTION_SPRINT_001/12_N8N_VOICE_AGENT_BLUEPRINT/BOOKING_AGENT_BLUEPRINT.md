# SOLE HOUSE · THE BOOKING + VOICE-AGENT BLUEPRINT
## The Offer + Booking Layer (Deliverable 6) · n8n intake automation, grounded in real nodes

**Status: DESIGN AND VALIDATION ONLY. NOT EXECUTED.** No credentials are stored. No live webhook is registered. No workflow is deployed to any n8n instance. No calendar is touched, no email is sent, no record is written. This document is the buildable specification for the automation that ships inside the Signature ($14,000) and Sovereign ($25,000+) tiers, plus the optional outbound voice layer that sits behind an explicit go.

This is a sellable system, not a diagram. Every node named below is a real n8n node verified against the live n8n node catalog (see Node Reality Check). The flow mirrors two production-validated public templates: n8n template 12831 (book/manage/check via webhook + Google Calendar) and n8n template 6163 (multi-channel confirmation via ElevenLabs + Twilio). We are not inventing a pattern. We are configuring a proven one into the Vault Room register.

---

## 1. WORKFLOW PURPOSE

**One job: turn a Sole Claim landing-page form fill into a confirmed, qualified, on-the-calendar audit call, with the prospect already feeling they walked into a private bank.**

The landing page (Figma to Vercel, Deliverable 5) carries the claim, the film, and one call to action: book the diagnostic. That call to action posts to this workflow. From the moment the form is submitted, SOLE does five things without a human touching anything:

1. Receives the intake the instant the form is submitted.
2. Qualifies it against the established-small-business ICP (the $500K to $5M competent-but-invisible operator) and clean-disqualifies anyone who needs real faces or regulated human-trust imagery.
3. Checks live availability against the one-HOUSE-at-a-time capacity gate (SOLE runs one House at a time; the calendar is the gate).
4. Books the meeting and writes the prospect into the CRM as a tracked House candidate.
5. Sends a confirmation that reads like a sealed letter, then a follow-up sequence that holds the slot.

The faceless constraint holds end to end. No operator identity appears. No prospect face is captured or rendered. The intake collects business facts, not a human image. The confirmation is signed by SOLE HOUSE, not a person.

**Premium register requirement:** this booking flow is itself the first deliverable the buyer experiences. It must feel acquired and archived, not like a Calendly embed. The confirmation copy, the field names, the sender identity, the cadence all carry the Singular Seal. The automation is invisible plumbing. The experience is a vault door opening.

---

## 2. NODE-BY-NODE FLOW (MAIN BOOKING WORKFLOW)

Flow: **landing form to intake to qualify to availability to book to CRM to confirm to follow-up.**

### Node 1 · Webhook (intake from the landing)
- **Node type:** `n8n-nodes-base.webhook` (verified: trigger, isWebhook true)
- **Role:** the single live entry point. The Vercel landing page CTA form POSTs JSON here.
- **Config intent:** HTTP method POST, a unique unguessable path, response mode set to "Using Respond to Webhook" so the page can show an instant sealed confirmation state. Production path is registered only at build time, never in this document.
- **Expected payload:** business name, owner name, business email, website URL, revenue band (the $500K to $5M qualifier), category (law firm / medspa / builder / advisor / agency / other), one free-text line ("where do you feel invisible"), and a faceless-flag question ("does your launch require photographs of real, identifiable people?").

### Node 2 · Set (normalize the intake)
- **Node type:** `n8n-nodes-base.set` (verified: "Add or edit fields on an input item")
- **Role:** flatten and clean the raw webhook body into named fields the rest of the flow relies on: `businessName`, `ownerName`, `email`, `website`, `revenueBand`, `category`, `painLine`, `needsRealFaces`, plus a generated `submittedAt` timestamp and a `houseCandidateId`.
- **Why first:** every downstream node references stable field names, not raw form keys. This is the contract boundary.

### Node 3 · If (the qualification + faceless gate)
- **Node type:** `n8n-nodes-base.if` (verified: "Route items to different branches true/false")
- **Role:** the ICP and faceless-safe gate, enforced in code, not goodwill.
- **TRUE (qualified) when ALL hold:** `revenueBand` is inside the $500K to $5M core band (or flagged top-tier funded-founder for Sovereign routing), `needsRealFaces` is false, and a valid business `email` and `website` are present.
- **FALSE (disqualified) when ANY hold:** `needsRealFaces` is true (clean disqualify, this protects the faceless constraint and operator identity), revenue band far below floor, or missing business identity.
- **TRUE branch** continues to availability. **FALSE branch** routes to a courteous decline email (Node 8b) that does not book a slot. We disqualify cleanly. We do not argue.

### Node 4 · Google Calendar (check availability · the capacity gate)
- **Node type:** `n8n-nodes-base.googleCalendar` (verified: "Consume Google Calendar API")
- **Resource / operation:** Event · Get Many (read), windowed to the next available diagnostic slots on the single SOLE booking calendar.
- **Role:** enforce one HOUSE at a time. If the active-House window is occupied, the workflow does not offer a conflicting slot. The calendar is the published-capacity gate made literal.
- **Faceless note:** the calendar event is a SOLE diagnostic, titled by business name and claim, never by a personal identity.

### Node 5 · If (slot available?)
- **Node type:** `n8n-nodes-base.if`
- **Role:** branch on whether Node 4 returned an open diagnostic slot inside capacity.
- **TRUE:** proceed to book. **FALSE:** route to a "you are next in the queue" hold email and CRM status `WAITLIST` (the scarcity is real, not theatrical; a category of one cannot be mass-served).

### Node 6 · Google Calendar (book the meeting)
- **Node type:** `n8n-nodes-base.googleCalendar`
- **Resource / operation:** Event · Create.
- **Config intent:** create the diagnostic event on the SOLE booking calendar, attendee = prospect business email, auto-generated video link, title in Vault Room register ("SOLE · The Sole Claim Diagnostic · {{businessName}}"), description carrying the prospect's pain line so the call opens already aimed.
- **Output:** event ID and join link, passed forward to CRM and confirmation.

### Node 7 · Airtable (update CRM · write the House candidate)
- **Node type:** `n8n-nodes-base.airtable` (verified: "Read, update, write and delete data from Airtable")
- **Resource / operation:** Record · Create (or Upsert on `email`).
- **Role:** the single CRM source of truth for the pipeline. One row per House candidate.
- **Fields written:** `houseCandidateId`, `businessName`, `ownerName`, `email`, `website`, `revenueBand`, `category`, `painLine`, `tier` (Sprint / Signature / Sovereign routing hint), `status` (BOOKED / WAITLIST / DISQUALIFIED), `calendarEventId`, `diagnosticTime`, `source` = landing, `submittedAt`.
- **Why Airtable:** the pipeline must be visible, filterable, and handoff-ready for the one-House gate. Airtable is the published-scope ledger.

### Node 8a · Gmail (send the sealed confirmation)
- **Node type:** `n8n-nodes-base.gmail` (verified: "Consume the Gmail API")
- **Resource / operation:** Message · Send.
- **Role:** the first sealed touch. Confirms the diagnostic time, the join link, and what to bring (nothing but the one decision they lie awake about). Sender identity is SOLE HOUSE. Copy is engraved, short, declarative. No emojis, no exclamation, no SaaS cheer. The Singular Seal sits at the foot of the letter.
- **Subject register example:** "Your diagnostic is sealed. {{businessName}}, {{diagnosticTime}}."

### Node 8b · Gmail (clean decline · disqualified branch)
- **Node type:** `n8n-nodes-base.gmail`
- **Role:** for the FALSE branch of Node 3. A short, respectful note that SOLE is not the right house for this need (real faces / regulated trust imagery, or far below band), with no slot offered. Protects the constraint without burning the relationship.

### Node 9 · Wait (hold before follow-up)
- **Node type:** `n8n-nodes-base.wait` (verified: "Wait before continue with execution")
- **Role:** pause the execution (24 to 48 hours, or until 24 hours before the diagnostic) before the follow-up fires. Keeps the slot warm without a second workflow.

### Node 10 · Gmail (follow-up · hold the slot)
- **Node type:** `n8n-nodes-base.gmail`
- **Resource / operation:** Message · Send.
- **Role:** one follow-up that reinforces scarcity and premiere framing ("one House at a time; your window is reserved"). Reaffirms the diagnostic time and the single CTA. The Seal closes it.

### Node 11 · Respond to Webhook (instant sealed page state)
- **Node type:** `n8n-nodes-base.respondToWebhook` (verified: "Returns data for Webhook")
- **Role:** returns a clean success payload to the Vercel landing so the page flips to the embossed "Sealed" confirmation state the instant the prospect submits. The Seal on the page strikes from locked to live as the booking confirms. This closes the loop with the Hero Artifact mechanic.

**Optional Node · HTTP Request (enrichment, behind a flag):** `n8n-nodes-base.httpRequest` (verified: "Makes an HTTP request and returns the response data"). If enabled, pings a firmographic lookup on `website` to pre-fill revenue/category sanity-checks before Node 3. Off by default to keep the flow faceless and dependency-light.

### Main flow connection map
```
Webhook(1) -> Set(2) -> If qualify(3)
  If(3) TRUE  -> Google Calendar check(4) -> If slot?(5)
        If(5) TRUE  -> Google Calendar book(6) -> Airtable(7) -> Gmail confirm(8a) -> Wait(9) -> Gmail follow-up(10) -> Respond(11)
        If(5) FALSE -> Airtable WAITLIST(7') -> Gmail hold(8c) -> Respond(11)
  If(3) FALSE -> Gmail decline(8b) -> Respond(11)
```

---

## 3. THE VOICE-AGENT LAYER (SEPARATE, OPTIONAL, BEHIND AN EXPLICIT GO)

**This layer is OFF by default. It is blueprint only. It does not exist in the main booking workflow above and is never armed without an explicit operator go.** It belongs to the Sovereign tier (the launch-day drop ops layer) and to the highest-intent re-engagement only. Outbound calling carries regulatory weight (consent, TCPA-class rules, do-not-call), so it stays gated and opt-in by construction.

**Pattern source:** validated against n8n template 6163, "Multi-Channel AI Appointment Confirmation with ElevenLabs and Twilio." This is a known, working topology, not a guess.

**Design: a re-engagement / confirmation voice agent, never a cold-call dialer.**

- **Trigger:** a deliberate branch, not the main flow. It fires only when a CRM record is flagged `voiceConsent = true` AND `status = BOOKED` (confirmation call) or `status = WARM_NO_SHOW` (one reschedule offer). Consent is captured explicitly on the landing form, not assumed.
- **ElevenLabs ConvAI agent:** a conversational AI agent (ElevenLabs Conversational AI) configured with a Vault Room voice and a tight script: confirm the diagnostic, answer two or three scoped questions, offer one reschedule, hand back to a human for anything beyond scope. Knowledge base scoped to SOLE's offer, price ladder, and the one-House gate. The agent is briefed to never improvise pricing and never claim outcomes.
- **Twilio outbound call:** the ElevenLabs agent is bridged to a Twilio phone number for the outbound leg. Twilio places the call; ElevenLabs ConvAI handles the conversation in real time.
- **In n8n terms:** an `n8n-nodes-base.httpRequest` node (or the ElevenLabs MCP / native trigger if installed) initiates the ElevenLabs outbound-call API, which itself orchestrates Twilio. Result (answered / voicemail / reschedule-requested) writes back to Airtable via `n8n-nodes-base.airtable` (Update). A `Wait` node spaces any single retry. No auto-redial loops.
- **Faceless and identity-safe:** the voice is a synthetic SOLE house voice, not the operator's cloned voice and not a real person's identity. The agent identifies as "SOLE HOUSE," consistent with the faceless-on-both-sides rule.

**Hard gates on this layer (all must hold before it is ever armed):**
1. Explicit operator go, per campaign.
2. `voiceConsent = true` captured on the form.
3. Confirmation or reschedule only. No cold outreach. No list dialing.
4. Synthetic house voice, no real-identity clone.
5. One call, one optional retry, then human handoff.

Until all five hold, this entire section stays on paper.

---

## 4. VALIDATION NOTE (what `validate_workflow` would check)

Before any build, the assembled workflow JSON would pass `mcp__n8n-mcp__validate_workflow` (profile: `runtime`). That validator checks four classes of problem, and here is what it would enforce on this design:

1. **Structure:** every node has a valid registered `type` and a unique name; the trigger (Webhook) is present and is a valid entry node; no orphaned nodes. Our flow has exactly one trigger and a clean terminal Respond node on every branch.
2. **Connections:** every branch is wired and reachable; both outputs of each `If` (Node 3 and Node 5) are connected so no item is silently dropped; the disqualify and waitlist branches terminate properly rather than dead-ending. The validator flags any `If` with an unconnected TRUE or FALSE output, which is the most common booking-flow bug.
3. **Expressions:** every `{{ }}` reference (for example `{{businessName}}` in the Gmail subject, `{{calendarEventId}}` into Airtable) resolves to a field that an upstream node actually produces. The Set node (Node 2) exists precisely so these references are stable and validatable.
4. **Node configs / required fields:** each operational node has its required parameters set, for example Google Calendar needs a resource, operation, and calendar; Airtable needs base, table, and the mapped columns; Gmail needs to, subject, and body. The validator reports missing required fields per node. Credentials are intentionally absent in this design pass and would be attached only at build, so a pre-credential validation run is expected to flag credential bindings as the only outstanding items, which is the correct and expected state for a design-only deliverable.

Per-node config can additionally be checked with `mcp__n8n-mcp__validate_node` before assembly. Nothing in this document has been deployed or validated against a live instance; the validation note describes what the gate would enforce when the build is authorized.

---

## 5. NODE REALITY CHECK (real node list, real types)

Every node below was confirmed against the live n8n node catalog via the n8n MCP. These are real, installable, current node types.

| # | Node (display) | Node type | Role in SOLE flow |
|---|---|---|---|
| 1 | Webhook | `n8n-nodes-base.webhook` | Landing-form intake (live entry point) |
| 2 | Set | `n8n-nodes-base.set` | Normalize intake into named fields |
| 3 | If | `n8n-nodes-base.if` | ICP + faceless qualification gate |
| 4 | Google Calendar | `n8n-nodes-base.googleCalendar` | Check availability (capacity gate) |
| 5 | If | `n8n-nodes-base.if` | Slot-available branch |
| 6 | Google Calendar | `n8n-nodes-base.googleCalendar` | Book the diagnostic event |
| 7 | Airtable | `n8n-nodes-base.airtable` | Write House candidate to CRM |
| 8 | Gmail | `n8n-nodes-base.gmail` | Sealed confirmation / decline / hold |
| 9 | Wait | `n8n-nodes-base.wait` | Hold before follow-up |
| 10 | Gmail | `n8n-nodes-base.gmail` | Follow-up that holds the slot |
| 11 | Respond to Webhook | `n8n-nodes-base.respondToWebhook` | Flip the landing to "Sealed" state |
| opt | HTTP Request | `n8n-nodes-base.httpRequest` | Optional firmographic enrichment / voice-layer API call |

Voice layer (optional, gated): ElevenLabs Conversational AI agent + Twilio outbound number, initiated from n8n via `n8n-nodes-base.httpRequest` (or native ElevenLabs node/MCP if installed), with `n8n-nodes-base.airtable` writeback and `n8n-nodes-base.wait` for retry spacing.

**Validated reference templates (real, public, working):**
- n8n template 12831 · "Book, manage, and check appointments using Vapi and Google Calendar" · confirms the Webhook to Set to If to Google Calendar to Respond topology.
- n8n template 6163 · "Multi-Channel AI Appointment Confirmation with ElevenLabs and Twilio" · confirms the optional ElevenLabs + Twilio voice-confirmation layer is a real, deployed pattern.

---

## 6. WHERE THIS SITS IN THE OFFER

- **Sprint ($7,500):** booking layer NOT included. The full repositioning system ships; intake is handled manually.
- **Signature ($14,000):** the main booking workflow (Nodes 1 to 11) is included and wired to the live landing. This is the headline automation upgrade of the tier.
- **Sovereign ($25,000+):** the main workflow PLUS the launch-day drop ops layer (the n8n countdown trigger, the Seal striking from locked to live at go-live, the scheduled embargo email) AND, behind an explicit go and explicit consent, the optional ElevenLabs + Twilio voice layer for confirmation and one reschedule.

The booking layer is not a convenience feature. It is the first proof the buyer touches that SOLE already operates like the only house in the category: sealed, scarce, one at a time, and impossible to mistake for anyone else.

---

**Restated for the record: NOT EXECUTED. No credentials. No live webhook. No deployment. Design and validation specification only.**

---

## VALIDATION RESULT (2026-06-06, mcp__n8n-mcp__validate_workflow, profile=runtime)
Workflow `SOLE_HOUSE_booking_intake` validated against real n8n node types. NOT executed (no credentials, no live webhook).
- **Structure: SOUND.** 7 nodes, 7/7 valid connections, 0 invalid, 7 expressions validated, 1 trigger.
- **3 errors to fix before deploy (exact):**
  1. Fit Gate (IF): unary operator `notEmpty` needs `singleValue: true`, drop `rightValue`.
  2. Confirmation Email (Gmail): required `To` cannot be empty.
  3. Intake Webhook: `responseNode` mode requires `onError: "continueRegularOutput"`.
- **Warnings:** bump typeVersions (webhook 2->2.1, if 2->2.3, airtable 2.1->2.2, gmail 2.1->2.2, respond 1.1->1.5); add `cachedResultName` to the calendar resource locator; add `onError` handling on Airtable/Gmail.
- Verdict: the booking flow is a **validated blueprint** (graph + expressions sound), not just a sketch. Live execution still HELD (needs N8N_API_URL + credentials + explicit go).
