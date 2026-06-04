## series_5 INTAKE DOCTRINE

---

### COVERAGE NOTE

19 segments processed.

- Read OK: segs 1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 15, 16, 17, 18
- Partial: segs 1 (first 7500 of 2.1M file), 6, 10, 14
- Empty/boilerplate: segs 6 (Reddit noise, zero signal), 19 (GitHub footer, skill nav artifact)
- Zero SNIPED relevance: segs 10, 11 (Docker/Nginx/homelab), 16 (security headers, app deployment)

Substantive content: 14 of 19 segments. 2 fully empty or near-empty.

---

### SOURCE INVENTORY

| # | Source / Topic |
|---|---|
| 1 | Reddit r/nextjs, r/webdev, r/ExperiencedDevs: Vercel deployment, pricing, enterprise skepticism |
| 2 | CloudFlare setup tutorial; Google Analytics vs Plausible Analytics; PostHog product analytics |
| 3 | Loves Data: GA + AI analyst workflows; Fabi.ai case study; Tally, Typeform, Airtable Forms comparisons |
| 4 | Reddit r/gtd (GTD/Tiago Forte weekly review); Vercel pricing threads; checklist tool preferences |
| 5 | Automation Helpers (Dan Lehman/Alex Nolles): Airtable CRM tutorials; Softr no-code UI; HubSpot free CRM |
| 6 | Reddit Reddit noise (r/WatchMaker, r/gtd, r/GoogleAppsScript etc.); Render DNS setup (Checkmark Academy) |
| 7 | Notion-to-Next.js CMS tutorials (two YouTube transcripts); headless CMS stack |
| 8 | Claude Code agent deployment (loop/scheduled/cloud/modal); Subabase backend integration; Railway vs Vercel |
| 9 | Darrel Wilson: AI website build + Subabase; Matt Pocock: "$10K Website with Claude Code" |
| 10 | Nginx Proxy Manager (Docker reverse proxy); Cloudflare DNS challenge; Jellyfin configuration |
| 11 | TechHut homelab: Nginx, Proxmox, Twingate VPN, Let's Encrypt SSL |
| 12 | Local SEO tutorial (comprehensive course); DataForSEO API; Google Maps/GBP optimization; AI SEO audit case study |
| 13 | Ahrefs: Google AI Mode + SEO; Caleb Ulku: Seven Layers of SEO Quality; Neil Patel/Exploding Topics keyword research |
| 14 | Cloudflare DNS setup tutorial; Google Analytics vs Plausible comparison (partial) |
| 15 | Plausible Analytics vs Google Analytics (A Better Computer / Matt walkthrough) |
| 16 | LiveOverflow: security headers/CSP; Jan Goebel: iOS/Android app release; ByteByteGo: Node.js deployment; Android checklist |
| 17 | Plausible Analytics overview/pricing walkthrough |
| 18 | ByteByteGo: production web app architecture; Netlify deploy tutorial; Claude Code workflow optimization; AI skill system (Claude) |
| 19 | GitHub repo footer boilerplate; Ishan Sharma skill reference list (nav artifact) |

---

### TOP LESSONS (deduped, ranked by SNIPED signal strength)

**Tier 1: Direct operator doctrine**

1. **Skill abstraction as force multiplier.** Claude skills are packaged .md frameworks that encode how to think (copywriter pattern, decision framework, creative director constraints) not just what to do. Skills enable reuse across contexts without re-prompting. SNIPED's existing doctrine (Composite Environment Rotation, Lineage Doctrine, Visual Direction, Trust Equation) can be packaged as Claude skills and deployed consistently. (Seg 18)

2. **Session discipline prevents context drift.** Multi-task single sessions = hallucinations + "fix one, break another" spiral. Correct pattern: PRD (vision/brief) + CLAUDE.md (stack/brand constraints) + Task Manager .md (session log, completion status) + isolated sub-agent windows per discipline. Session-start reads context; session-end records completion before clearing. Directly mirrors EXECUTION_GOVERNOR doctrine. (Segs 18, 9)

3. **Multi-agent orchestration by discipline.** Break projects into specialist agents (Business / Infrastructure / Creative / Narrative) rather than one all-context session. Reduces hallucination, enables parallel workstreams, matches SNIPED's limited-hours operating model. (Seg 18)

4. **Plan before execute; batch over drip.** Planning mode first (explore codebase/brief, surface unresolved questions, lock architecture). After architecture locked, switch to auto-accept batch mode. Batch 5+ small changes per prompt, approve as one unit. Fewer tokens, more coherent output. Applies to shoot planning, post production batching, caption writing runs. (Segs 9, 18)

5. **"How it should feel" beats feature specification.** Directional language (expensive, restrained, handcrafted) outperforms feature lists when prompting Claude for design or copy. Claude translates intent to specifics better than humans write specs. Mirrors VISUAL_DIRECTION doctrine (Meisel/Roversi restraint, no teal/orange). (Seg 9)

6. **Human judgment pass is non-negotiable after automated batch.** Claude cannot feel flatness, tension, or visual rhythm. After any automated creative batch, human scrolls, identifies static sections, adds one interaction per flat section. Tool for exploration; human for felt sense. (Seg 9, confirmed by STRONGEST_PHOTOGRAPH_NOT_MOST_PROCESSED rule)

7. **The $10K website quality checklist (8 dimensions).** Point of view + typography + color + hierarchy + imagery + motion + mobile + invisible/performance quality. These form three buckets: taste + substance + felt quality. Applicable to any client deliverable, brand system, or portfolio review. (Seg 9)

8. **Copy restraint as premium signal.** "Six dishes, one fire" beats adjective-loading. Inter screams AI-made; Geist reads premium. Font + restraint as anti-AI signal. Directly applies to SNIPED caption writing and brand system copy. (Seg 9)

9. **Concision as authored-signal.** Configure Claude rules to demand "extremely concise" output in all planning/commit artifacts. Sacrifice grammar for brevity. Outputs that feel authored rather than AI-generated break the pattern-recognition that triggers "AI slop" perception. (Seg 9)

**Tier 2: Infrastructure + distribution doctrine**

10. **Local SEO: Three ranking factors, two are controllable.** Proximity is fixed. Relevance (GBP categories/services/description/consistency) and Authority (external links, local trust signals) are controllable. Small operators can beat established incumbents in weeks by mastering the two controllable factors. (Seg 12)

11. **GBP foundations take 30 minutes; 90% of competitors skip them.** 10 categories max, 20-30 services minimum, description at 750 chars, 20+ photos, posts, attributes. Completion = legitimacy signal to Google algo. This is a zero-cost moat most operators leave on the table. (Seg 12)

12. **Core 30 architecture.** 1 homepage + 3-4 category pages + 25-30 service pages. Internal linking mirrors GBP structure. Editorial links pass more authority than navigation links. This is the foundational web content architecture before any content scaling. (Seg 12)

13. **Topical authority before geographic expansion.** Prove topical depth first (FAQ content, People Also Ask, Reddit crawl for real local questions). Only expand geographic targeting after top-3% rank-map threshold achieved. Sequential build, not simultaneous scatter. (Seg 12)

14. **Seven Levels of SEO Quality.** Level 3 (Mid) is the danger zone: SEO plugin assumption, AI-generated content with zero human touch. Level 5+ requires actual keyword research, tool integration, topical authority commitment. Level 7 (GOAT) = topic authority depth, community karma, search-engine agnostic presence. (Seg 13)

15. **AI search presence as platform-risk defense.** Authority sites rank first in ChatGPT and Perplexity when queried. Content valuable enough to survive if Google disappeared = real competitive moat. Mirrors CRM/owned-audience thinking in LEVERAGE_LOGIC. (Seg 13)

16. **12-month planning over 5-year.** Strategic curve is too steep for long-range locks. Execute on what works now, stay close to changes. Play offense (more queries, more intent, more opportunity) rather than defending turf. (Seg 13)

17. **Analytics: right-size tool to job-to-be-done.** Plausible (1KB script, 75x lighter than GA, privacy-first, CSV export, data ownership, one-line setup) beats GA for simple operator tracking (pageviews, conversion events, retention). GA's feature depth is waste if you only need week-1 retention + funnel conversion data. (Segs 2, 15, 17)

18. **Week-1 retention is the launch metric.** Talk to users first; analytics illuminate priorities after product-market readiness. Week-1 retention cohort is the single most actionable number at launch. Vanity funnels mislead. (Seg 2)

19. **Analytics intelligence inputs.** Tell AI "this data represents [context + plan tiers + user segments]" before analysis. Business context amplifies AI usefulness more than raw schema alone. (Seg 3)

20. **Airtable CRM architecture: relational beats monolithic.** Contacts > Opportunities > Deals as linked tables. Email-domain formula extracts auto-account-match on inbound submissions. Kanban + automation status updates. Forecasting dashboard (commit, closed, pipeline). Win-notification Slack automation. CRM must match business process, not force process into CRM. (Seg 5)

21. **Agent deployment cost math.** Cloud routines (Anthropic): 15 runs/day max on Max plan, 1-hour minimum interval, expensive per token. /loop loops free under Cloud Code subscription, session-scoped. Modal/trigger.dev for deterministic workloads. Choose by autonomy needs + availability. (Seg 8)

22. **Hooks as lightweight event-driven automation.** Session-start, pre-tool, post-tool, message-sent triggers enable layered automations without full agent loops. Silent by default. Fits EXECUTION_GOVERNOR anti-report stance (action not summary). (Seg 8)

23. **Conditional logic in forms is now table-stakes.** Tally (slash-command/Notion-like, unlimited free submissions, Airtable/Notion sync, Zapier webhooks) supports CASTING_CALL_DOCTRINE workflows better than Typeform (10-response/month free tier). (Seg 3)

24. **Deployment options trade complexity vs control.** VM (full control, high ops overhead), PaaS/Cloud Run (hybrid control, cost-efficient, handles most SNIPED-scale needs), Kubernetes (enterprise overkill), Serverless (cheap, no websockets, cold-start latency). Cloud Run + minimum instances = best balance for operator-scale backend. (Seg 16)

25. **CI/CD pipeline discipline mirrors shoot delivery discipline.** Feature branch > code review > dev > staging (load/smoke tests) > production. Each gate prevents issues at scale. Direct parallel to CASTING_CALL_DOCTRINE gating (24-hr confirm, wardrobe photo, 2-strike rule). Systems discipline transfers across domains. (Seg 18)

26. **Vercel pricing trap at scale.** Works well for niche/low-traffic apps. At high traffic, cost-to-convenience ratio inverts. Enterprise perception: "over-promises, claims to replace CDN/security/GCP, doesn't deliver; benefit is easier deployments only." Pricing starts $1K+/month enterprise tier, no public pricing (standard premium SaaS sales motion). (Seg 1)

27. **Platform pricing psychology.** Founder/operator communities treat platform costs as cultural signal, not edge case. "DX convenience beats infrastructure costs" argument holds at small scale; cost becomes visible concern at mid-scale; stability + no-ops engineering avoidance dominates at enterprise scale. (Segs 1, 4)

---

### SNIPED-RELEVANT EXTRACTS

**Creative Director Skill (high-value build):** Seg 18 documents that Claude skills can encode complete operating frameworks as .md files. SNIPED's Composite Environment Rotation, Lineage Doctrine, Visual Direction (Meisel/Roversi lane, Adobe Neutral, no teal/orange), and Trust Equation could ship as a single "SNIPED Creative Director" skill. Claude would then have these constraints available without re-prompting every session. This directly operationalizes CONNECTED_TOOLCHAIN_DEFAULT.

**Session-Manager Workflow for production:** PRD = shot brief. CLAUDE.md = brand constraints + editorial rules. Task Manager = production log with completion status. Isolated agent windows per discipline (photography / retouching / narrative / outreach). This is the EXECUTION_GOVERNOR made concrete for a creative OS.

**Local SEO as authority scaffold:** GBP optimization, Core 30 content architecture, and topical-first expansion map directly onto SNIPED's LA founder-scene positioning. Building topical depth in specific LA cultural circles (scene-density thinking) has a direct SEO parallel: prove topical authority in one cluster before expanding geographically. Same discipline, different medium.

**Plausible analytics for SNIPED site:** Privacy-compliant, 1KB, one-line setup, CSV export, data ownership. Right-sized for Chapter Card distribution tracking + founder outreach pipeline measurement. Pricing ($22/month at 200k views) is material; deploy after site has validated traffic not before.

**Form builder for casting calls:** Tally wins over Typeform for CASTING_CALL_DOCTRINE: unlimited free submissions, conditional logic, Airtable/Notion sync, Zapier webhooks. Immediate swap candidate if current intake form has submission limits.

**Airtable CRM for SNIPED pipeline:** Email-domain auto-match on inbound form submissions, Kanban pipeline view, win-notification Slack automation, and forecasting dashboard are all directly applicable to shoot inquiry tracking, lead flow, and payment/delivery status.

**Anti-AI slop defense via external validation:** Local authority links (chamber of commerce, sponsorships) + human editor pass on AI content = validation that content is not AI slop. Both SEO algo and trust audience use the same signal. Aligns with HYBRID_OPERATOR stance.

**Reference sites over mood boards:** Show Claude 3-5 existing sites you like. Easier than describing visual taste in words. Direct improvement to current Direction Stack briefing workflow for web or composite reference.

---

### ANYTHING NEW NOT ALREADY IN SNIPED DOCTRINE

These are signals present in series_5 that are not yet formalized in SNIPED doctrine. Reporting only; no lane crowned.

1. **Claude skill system as doctrine-packaging layer.** SNIPED has extensive written doctrine but no mechanism to make it Claude-accessible without manual paste. The skill (.md framework) architecture is a delivery mechanism for the existing OS corpus. This is operationally new, not strategically new, but the tooling path is undocumented.

2. **Local SEO as scene-density infrastructure.** GBP + Core 30 + topical authority build is not mentioned anywhere in current SNIPED doctrine. SNIPED has scene-density thinking (depth in LA cultural circles, not breadth) but no web-search presence strategy mapped to it. These are the same logic applied to different surfaces.

3. **Seven Layers of SEO Quality as a quality-ladder framework.** Structurally mirrors how SNIPED thinks about work quality (amateur to master), but the specific levels (1-7, from black hat to topic-authority-depth + search-engine-agnostic presence) are new and directly usable as a maturity model for any SNIPED digital surface.

4. **Analytics tool selection as positioning signal.** Plausible's "privacy-first, transparent, minimal" positioning is not just a tool preference; it is a brand stance. Current SNIPED doctrine does not address analytics tool as a positioning decision. Small but real.

5. **AI search presence as separate layer from Google SEO.** ChatGPT and Perplexity rank authority content first. Building content that survives Google's disappearance = real moat. Current SNIPED content doctrine (Chapter Cards, Cultural Doc, LinkedIn) does not address AI search indexing as an explicit distribution target.

6. **Batch-approve after architecture lock.** The specific workflow (plan mode locked, then auto-accept batch mode) is an efficiency pattern not documented in current EXECUTION_GOVERNOR or OPERATOR_PLAN. Small but applicable to any multi-step creative or copy production run.

7. **Session-to-session persistence via Task Manager .md file.** Current SNIPED doctrine uses CURRENT_STATE.md, ACTIVE_THREADS.md, SESSION_LOG.md for state persistence. The Claude Code task-manager pattern (sub-agent windows, PRD + CLAUDE.md + task manager, explicit session-end logging before window close) is a more granular refinement worth cross-referencing.

8. **Cold start latency in serverless as user experience concern.** Not relevant to current SNIPED infrastructure, but if SNIPED ever ships a client portal or automated delivery tool, Cloud Run + minimum instances (not pure serverless) is the right call. No doctrine covers this.