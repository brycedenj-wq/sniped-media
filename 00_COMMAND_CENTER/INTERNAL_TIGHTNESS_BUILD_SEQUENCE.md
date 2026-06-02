# INTERNAL_TIGHTNESS_BUILD_SEQUENCE

**Date:** 2026-05-27
**Status:** The finish-line definition for "internally tight" before BASEPLATE takes market action. Anchor-class: markdown-only, not chunked, not a chunk source, not in the master files. This converts the docs into connected runnable systems. No outreach is attached to this build, BJ sets the launch timing.
**Operating principle:** each system pulls the best method from the best source on its topic (the docs are best-in-class on their subjects), so the activated system encodes the best available craft. Build it to help BJ first; the same systems become deployable to others later via /operator-review.

---

## 1. Definition of internally tight
Internally tight means the system can **explain and run the full path** without improvisation:
**stranger to lead to reply to call to proposal to paid pilot to delivery to proof log.**
At every handoff in that chain, a runnable artifact answers "what happens now, who does it, and why," and the artifacts connect (the output of one is the input of the next). When BJ can trace that entire path on paper and each step has a system behind it, the internal build is tight and market action becomes a decision, not a leap.

## 2. What does NOT count as tight
- More generic strategy or another thesis pass.
- More name/domain loops (decided: BASEPLATE, baseplatehq.com).
- "Go do outreach" pressure (BJ sets timing, internal-first).
- Raw coverage without activation (chunked is not runnable).
- Reading more docs/books for their own sake.
- Overbuilt automation (n8n, agents, callers) before proof.
- Fake certainty, fake proof, or polished decks with no runnable steps behind them.

## 3. Required operating systems

| # | Artifact | Purpose | Source docs | Decision it enables | What must be runnable | Before first outreach? |
|---|---|---|---|---|---|---|
| 1 | **Outbound Activation Playbook** | The engine that finds and contacts leads | WEDGE_OFFER_SPEC §9, OPERATOR_CONTROL_ROOM §5-7, The_Outbound_Stack, Instantly gold doc, IMPLEMENTATION_STACK | who to contact, how, with what message | ICP filters, lead schema, 3-email sequence, LinkedIn pairing, cadence | YES |
| 2 | **Admin Lead Research SOP** | Exactly what admin does (build/enrich list, never contact) | OPERATOR_CONTROL_ROOM §5, WEDGE_OFFER_SPEC §3 | delegation: admin fills the funnel | paste-ready assignment, fields, urgency tags, QC standard, do-not list | YES |
| 3 | **Discovery + Qualification Playbook** | How a booked call becomes a qualified yes | WEDGE_OFFER_SPEC §10 (script) + §11 (qual/disqual) | run the call, score the buyer, green/yellow/red | 20-min script, qualifying questions, disqualifiers, minimum viable buyer | YES |
| 4 | **Proposal + Invoice Playbook** | Turn a yes into money committed | WEDGE_OFFER_SPEC §6 (tiers/price), IMPLEMENTATION_STACK (Pixieset Studio Manager) | which tier, what price, how they pay | Pilot proposal template, deposit invoice, scope, terms | YES |
| 5 | **Sample Dossier Build Playbook** | The artifact shown on the call that earns trust | WEDGE_OFFER_SPEC §4 (deliverable) + §5 (security rules) | what to build, what to never show | a labeled SAMPLE dossier spec/mock, security-safe rules | YES |
| 6 | **Delivery + Approval Playbook** | Produce and deliver the paid dossier, client approves every asset | WEDGE_OFFER_SPEC §4-5, IMPLEMENTATION_STACK (Pixieset gallery) | how delivery happens, approval gates | brief to approve to produce to approve to deliver workflow | CAN WAIT (needed at first delivery, not first contact) |
| 7 | **Proof Log Operating SOP** | Record every real interaction as evidence | PROOF_LOOPS_30_60_90 §6, WEDGE_OFFER_SPEC §12 | what counts as real proof vs noise | the proof-entry template, what to log, R/Y/G rules | YES |
| 8 | **Content / Named-Author Media Seed Playbook** | The distribution amplifier (BJ byline) | distribution-mechanics memory, TRUE_BILLION_DOLLAR_THESIS media layer | when/what to post, BJ as author | post cadence, angle rules, what not to post | CAN WAIT (amplifier, post-proof, BJ-timed) |
| 9 | **/operator-review Client Delivery Playbook** | Deliver the OS to a paying outside client | /operator-review skill, COMMAND_CENTER_RESPONSE_PROTOCOL | how the productized service is run | scoping, the operator-review output, boundaries | CAN WAIT (the service layer, post-proof) |
| 10 | **Legal / Employment / IP Guardrail Checklist** | The boundary that governs every action | BASEPLATE_DOMAIN_AND_EMPIRE_ARCHITECTURE (employment gate), WEDGE_OFFER_SPEC §5 hard rules | what is safe to do/say/show | the do/do-not boundary, employer-clean rules | YES (cheap, governs outreach + first client) |

## 4. Dependency map
```
domain (baseplatehq.com) + site + Calendly
        |
        v
Sample Dossier (the thing shown)  <----+
        |                               |
        v                               |
Lead list (admin) --> Outbound --> Reply --> Discovery call
        |                                         |
        v                                         v
   Proof Log  <----------------------------  Proposal + Invoice
        ^                                         |
        |                                         v
   (iterate)  <---- Delivery + Approval  <---  Paid Pilot
```
Every box has an artifact behind it (section 3). The Legal/IP checklist sits underneath the whole chain as the boundary. Content and /operator-review attach after the chain is proven.

## 5. Minimum viable internal system before outreach
The smallest set that must exist before any contact with a buyer:
- **Surface:** site live on baseplatehq.com, canonical + Calendly wired (pending domain registration, a real-world step, not a strategy blocker).
- **Sample Dossier:** defined or built (the call needs something to show).
- **Outbound Activation Playbook** (artifact 1).
- **Admin Lead Research SOP** (artifact 2).
- **Discovery + Qualification Playbook** (artifact 3).
- **Proposal + Invoice template** (artifact 4).
- **Proof Log Operating SOP** (artifact 7).
- **Legal / IP Guardrail Checklist** (artifact 10).
Delivery, content, and /operator-review are NOT required for first contact and do not gate it.

## 6. Full internal system before scale (Instantly volume / larger campaigns)
Required before moving from warm/manual to cold volume:
- **Cold domain + inbox architecture** (separate cold domains, never baseplatehq.com; 5 inboxes/domain; SPF/DKIM/DMARC; 2-3 week warmup to 30/inbox/day).
- **Reply classification** (positive / objection / neutral / negative to action).
- **Deliverability monitoring** (open 40-60%, reply 3-5%, positive >1%, bounce <3%, spam <0.1%).
- **Admin QC** (verified emails, dedupe, decision-makers only, urgency tags).
- **Follow-up rules** (spacing, max touches, break-up).
- **Objection handling** (the WEDGE_OFFER_SPEC §7 lines).
- **Proof-loop review cadence** (weekly pass, R/Y/G at the 30/60/90 marks).
These live inside the Outbound Playbook plus a dedicated Instantly Scale SOP (artifact built last).

## 7. Build order (exact)
1. Outbound Activation Playbook
2. Admin Lead Research SOP
3. Discovery + Qualification Playbook
4. Proposal + Invoice Playbook
5. Sample Dossier Build Playbook
6. Proof Log Operating SOP
7. Content / Named-Author Media Seed Playbook
8. /operator-review Client Delivery Playbook
9. Legal / Employment / IP Guardrail Checklist
10. Instantly Scale SOP

Note: the **Delivery + Approval Playbook** (artifact 6 in section 3) builds alongside the Sample Dossier work and must exist before the first paid delivery; it is a can-wait relative to first outreach, so it is not in the pre-outreach critical path but should not be skipped before delivering. Items 1 through 6 (plus 9) form the minimum viable internal system; 7, 8, and 10 are post-proof or scale layers.

## 8. Stop conditions (when building stops and proof starts)
Internal building stops, and the decision to run the proof loop becomes BJ's to make, when ALL of these exist:
- Minimum viable internal system complete (section 5).
- Site deployed on baseplatehq.com (canonical + Calendly live).
- Sample dossier ready (defined or built).
- A 25-target lead list ready (admin).
- The discovery to proposal flow ready (scripts + templates).
At that point the system is tight: do not keep building. BJ decides when to move.

## 9. What remains parked (do not build now)
- Platform / registry / verified-operator graph / network (earned endgame only).
- App / product build (post-proof, earned layer).
- n8n / Twilio / RetellAI automation (automation-before-proof).
- Higgsfield / Kling content engine (later amplifier; concept-film is internal only).
- Clothing / status artifacts.
- Full ingestion of every book (curate; deep-extract only a named book on request, e.g. Batch A).
- Cold-email volume before the warm/manual proof works.

## 10. Final recommendation
- **HOLD OUTREACH UNTIL THE MINIMUM INTERNAL SYSTEM EXISTS** (section 5). This honors the internal-first operating mode.
- **DO NOT HOLD FOR FULL 426-DOC ACTIVATION.** Tightness is the connected set of runnable systems, not every doc reviewed.
- **BUILD THE REQUIRED ARTIFACTS IN ORDER** (section 7), each pulling the best source on its topic.
- **THEN RUN THE PROOF LOOP**, on BJ's timing, once the stop conditions (section 8) are met.

---

## Guardrails (unchanged)
Internal-first build, no outreach attached, BJ sets launch timing. No platform/registry/network public claim. No photography-only reduction (media is the instrument; the operator layer is the company). No automation before proof. No fake proof. Employer-clean (own devices/accounts/time, no employer data, no targeting employer clients/vendors/employees). Old SNIPED/BASEPLATE material is historical evidence, not law. Bible held until a deliberate SPIRITUAL_FOUNDATION decision. Anchor-class: not chunked, not in the master files, total_chunks unchanged at 1,837. This artifact defines the build sequence; it builds nothing by itself and changes no site, master, or raw file.
