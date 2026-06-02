# TOOLCHAIN_ACTIVATION

**Date:** 2026-05-27
**Status:** Anchor-class. Markdown-only, not chunked, not a chunk source, not in the master files. The single canonical tool-layer reference for the OS. Tracks every MCP, connector, skill, API, and script in BJ's stack with status (active / candidate / queued / deferred), use case, and trigger. The OS consults this at routing time so every task asks "what tool can execute this?" before falling back to manual.

**Operating frame:**
Tools are part of the OS knowledge base. The OS consults what is connected, authed, and runnable, not only what is in books and brand docs. Manual is the last resort, not the default.

---

## 1. The locked operating rule

Before answering any task involving creation, publishing, design, video, content, CRM, payments, outreach, research, file operations, automation, or external systems, the OS asks:

> "What tool, app, MCP, API, script, or skill in BJ's stack can execute this instead of only advising?"

That question runs before any "you could write this yourself" or "a designer would" or "manual" answer ships.

## 2. The four-step routing every response runs through

1. **What does the OS know?** corpus, memory, committed docs, prior sessions.
2. **What tool can execute it?** MCP, API, skill, script, repo tooling.
3. **What artifact should exist after?** file, design, site, log, commit, external output.
4. **What should be committed, logged, or handed off?** so the work survives this conversation.

## 3. Tool layer as a first-class OS lane

Equal peer to thesis, money, brand, proof, legal, distribution, execution. Same recall discipline. When a task lands, the OS retrieves from this lane as readily as it retrieves from the spine or the canon.

---

## 4. Active connectors and MCPs (callable now)

### Figma MCP (Claude Code plugin v2.2.12) · ACTIVE / PROVEN
- **Endpoint:** `https://mcp.figma.com/mcp` (streamable HTTP).
- **Install path:** `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/`.
- **Auth:** OAuth alive. Account `brycedenj@gmail.com`, plan "Bryce's team" (`planKey: team::1304582857318682870`, Pro tier).
- **Tools (representative):** `create_new_file`, `use_figma`, `generate_figma_design`, `upload_assets`, `get_screenshot`, `get_metadata`, `whoami`, `search_design_system`, `get_design_context`, `get_figjam`, `get_libraries`, `get_variable_defs`, `add_code_connect_map`, `get_code_connect_map`, `get_code_connect_suggestions`, `get_context_for_code_connect`, `send_code_connect_mappings`.
- **Bundled skills:** `/figma-use`, `/figma-create-new-file`, `/figma-generate-design`, `/figma-generate-library`, `/figma-generate-diagram`, `/figma-code-connect`, `/figma-use-figjam`, `/figma-use-slides`. The plugin marks specific skills as mandatory before specific tools.
- **Precedent:** `SNIPED · VIB Master` (`figma.com/design/qIu3GAifLsRuWosXdingYZ`). `BASEPLATE · Sample Capability Dossier v1` (`figma.com/design/p7qWs3AhjTHZa6vDZGoKGE`, built 2026-05-27).
- **Trigger:** any design, layout, mockup, brand visual, component build, design system, dossier, slide deck, FigJam board, or code-connect mapping.

### Gmail connector · AVAILABLE / CONNECTED
- **Status:** visible in Claude Directory, connected.
- **Use case:** email drafting, inbox search, message summarization.
- **Trigger:** when an email artifact, search query, or inbox-driven action is the actual task.
- **Guardrail:** approval-gated for sending. No employer email targeting. No SNIPED cold outreach outside the warm-network rule.

### Adobe for Creativity connector (Adobe Creative Cloud) · VISIBLE / ADDED
- **Status:** connector visible and added. Creative-production lane.
- **Use case:** ideation, image editing, retouching, compositing, visual polish, campaign assets, brand visuals, social variants, motion and polish workflows. Possible Adobe pro-tool integrations as they expose APIs.
- **Trigger:** SNIPED campaign edits, Reset delivery assets, BASEPLATE dossier visual treatment, concept art, composites, social and creative variants.
- **Guardrail:** can edit, polish, composite, stylize, build atmosphere. Cannot create fake client proof, fake facilities, fake crews, fake testimonials, fake metrics, or anything presented as real evidence.

### Airtable connector · AVAILABLE / CONNECTED
- **Endpoint:** `https://mcp.airtable.com/mcp`
- **Status:** visible in Claude Directory, connected. Live in `claude mcp list`.
- **Use case:** base + table + record CRUD, schema queries, interface and page reads, record comments. Native multi-base relational store for CRM, content calendar, proof log, lead pipeline, asset inventory, shoot tracker.
- **Trigger:** any task where structured records (leads, shoots, deliveries, content schedule, proof entries) belong in a relational store. Candidate home for SNIPED CRM and BASEPLATE proof log while the Notion MCP path stays queued. The user skill `sniped-notion-crm-update` documents the workflow shape; Airtable is a parallel substrate when Notion is not the active path.
- **Guardrail:** approval-gated for record mutations (create / update / delete). Read-only operations (list, search, schema, comments) safe to default-run when routing requires.

### Higgsfield CLI (`@higgsfield/cli`) · ACTIVE / AUTHED
- **Install path:** `/opt/homebrew/bin/higgsfield` · `@higgsfield/cli@0.1.40` (build `9aa6f1f3`, 2026-05-12).
- **Aliases:** `higgsfield`, `higgs`, `hf`.
- **Auth (verified 2026-05-28 audit):** ✓ `brycedenj@gmail.com`, Plus plan, **1000 credits**. Workspace context: Private (single workspace, ID `18b3ba15-661a-472f-a91f-85d1330b81b4`; no team workspace).
- **Read-only commands (no spend):** `account status`, `account transactions`, `workspace list / status`, `model list [--image|--video|--text]`, `model get <slug>`, `generate cost`, `generate list`, `generate wait`, `version`.
- **Spend commands (per-batch approval, never default):** `generate create <model>`, `marketing-studio`, `marketplace-cards`, `product-photoshoot`, `soul-id train`.
- **Key image model slugs (live, 2026-05-28):** `nano_banana_2` = Nano Banana Pro, `nano_banana_flash` = Nano Banana 2, `nano_banana` = Nano Banana, `seedream_v4_5` = Seedream 4.5, `seedream_v5_lite` = Seedream V5 Lite, `gpt_image_2` = GPT Image 2, `flux_2` = FLUX.2, `flux_kontext` = Flux Kontext, `text2image_soul_v2` = Higgsfield Soul V2, `soul_cinematic`, `soul_location`, `marketing_studio_image`, `image_background_remover`, `image_auto`.
- **Bundled Higgsfield skills (installed via `npx skills add higgsfield-ai/skills`, symlinked from `~/.claude/skills/` to `~/.agents/skills/`):** `higgsfield-generate`, `higgsfield-product-photoshoot`, `higgsfield-marketplace-cards`, `higgsfield-soul-id`, plus `find-skills`.
- **Pre-existing SNIPED wrapper:** `sniped-higgsfield-pipeline` (user skill, since 2026-05-12) wraps the Content Factory + Image Pack workflows.
- **Trigger:** any image / motion / Marketing Studio / Soul / marketplace creative for SNIPED IG creative engine or BASEPLATE concept film. CLI is the execution surface; skills are the wrappers.
- **Guardrail:** every spend command runs only on explicit per-batch approval. Concept and atmosphere only on BASEPLATE; never client evidence. SNIPED may publish AI-forward creative openly as art and mythology, never as fake client proof.

---

## 5. Candidate MCPs and connectors (queued, deferred, not installed/active in this session)

### Higgsfield MCP (claude.ai connector) · ACTIVE / CONNECTED
- **Endpoint:** `https://mcp.higgsfield.ai/mcp`
- **Status:** ✓ Connected (appeared in `claude mcp list` on 2026-05-28 after the Drive / Calendar OAuth round, surfaced by claude.ai's cloud connector layer). Now a parallel surface alongside the CLI + skill layer in §4.
- **Use case:** structured tool-call surface for image / motion / Marketing Studio / Soul / marketplace generation. The CLI + skill path remains active; the MCP adds tighter schemas and native async job state.
- **Routing today:** continue routing through the CLI + skill path (the Higgsfield CLI entry in §4) until a real schema-friction or async-polling reason emerges to switch. Both surfaces work; do not double-route the same generation.
- **Guardrail:** identical to CLI · every spend command runs only on explicit per-batch approval. Concept and atmosphere only on BASEPLATE; never client evidence. SNIPED may publish AI-forward creative openly as art and mythology, never as fake client proof. Soul ID training is DEFERRED per `BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md` §"Soul ID · DELAYED."

### Stripe MCP · QUEUE (gated on EIN legal-name correction + business bank account)
- **Status:** not installed. Gated on two independent prerequisites: (1) IRS legal-name correction or 147C verification letter showing `Baseplate, LLC` as the canonical name (current IRS record shows `BASEPLATE` uppercase brand; correction PENDING as of 2026-05-28, BJ attempted phone call to IRS Business & Specialty Tax Line and did not get through); (2) business bank account opening (Mercury / Relay / Chase Business / similar).
- **Use case:** invoicing, subscriptions, refund automation.
- **Trigger:** after BOTH gates clear. See `feedback-ein-correction-gate` memory for the full gate status and the list of dependent workflows (bank account, W-9 issuance, payment processor enrollment, any entity-name-verifying surface).
- **Do not attempt:** Stripe account creation, W-9 issuance, or any payment processor enrollment using the as-issued (incorrect) EIN name until the correction is confirmed.

### Notion MCP · QUEUE (CRM / proof logging)
- **Status:** not installed in this session. The `sniped-notion-crm-update` user skill wraps the intended workflow.
- **Use case:** CRM, proof log, structured note capture, internal wiki.
- **Trigger:** when discovery calls start producing real logging volume on either lane.

### Adobe Analytics MCP · CANDIDATE (analytics lane, separate from creative)
- **URL:** `https://aa-mcp.adobe.io/mcp`
- **Status:** not installed. No traffic or Adobe Analytics environment yet.
- **Use case:** web traffic analytics, campaign performance.
- **Trigger:** when BASEPLATE or SNIPED has actual web traffic or a configured Adobe Analytics environment to query.

### Customer Journey Analytics MCP · CANDIDATE (analytics lane)
- **URL:** `https://cja-mcp.adobe.io/mcp`
- **Status:** not installed. No journey data yet.
- **Use case:** funnel and journey analysis, cross-touchpoint attribution.
- **Trigger:** when meaningful journey data exists.

### Search / Research MCP (Tavily, Exa, or web search) · DEFER
- **Status:** not installed.
- **Use case:** current-info retrieval beyond corpus and training cutoff.
- **Trigger:** only when a research task genuinely requires post-corpus current data. Corpus covers most current needs in BJ's domain.

### Microsoft 365 connector · AVAILABLE / CANDIDATE
- **Status:** visible in directory. Not added.
- **Use case:** Outlook, Word, Excel, Teams workflows.
- **Trigger:** only if a real Microsoft-365-resident workflow appears.

### Google Drive connector · CONNECTED (temporary bridge)
- **Endpoint:** `https://drivemcp.googleapis.com/mcp/v1`
- **Status:** ✓ Connected (authed 2026-05-28). **Important:** the authed accounts are BJ's personal Google account and `admin@snipedmedia.com` operating as TEMPORARY bridges, NOT the future BASEPLATE Google Workspace. See `feedback-google-account-bridge-temp` memory for the lane mapping and constraints.
- **Use case:** Drive search, doc creation, file management, asset archive.
- **Guardrail:** read-only operations (search, list, read content) are safe. NO cross-account file moves. NO Drive folder structures that anchor the personal account as the BASEPLATE workspace. NO mutations until BJ explicitly authorizes a Drive workflow. When the BASEPLATE Google Workspace is created later, re-auth against the new Workspace and archive the temp-bridge posture.

### Google Calendar connector · CONNECTED (temporary bridge)
- **Endpoint:** `https://calendarmcp.googleapis.com/mcp/v1`
- **Status:** ✓ Connected (authed 2026-05-28). Same temporary-bridge posture as Drive · see `feedback-google-account-bridge-temp` memory.
- **Use case:** scheduling, availability lookup, event creation. Calendly bridge candidate once paid Reset booking automates.
- **Guardrail:** read-only availability checks safe to default-run. Event creation, update, delete approval-gated. NO new calendars that imply BASEPLATE-as-tenant under the personal account. When the BASEPLATE Google Workspace is created later, re-auth against the new Workspace and archive the temp-bridge posture.

### Notion connector (separate from Notion MCP) · AVAILABLE / NOT ADDED
- **Status:** visible in directory. Not added.
- **Trigger:** only when a Notion-resident workflow appears.

### HubSpot connector · AVAILABLE / NOT ADDED
- **Status:** visible in directory. Not added.
- **Use case:** enterprise CRM, marketing automation.
- **Trigger:** only if BASEPLATE outgrows lighter CRM (Notion) at scale. Not now.

### Zoom connector · AVAILABLE / NOT ADDED
- **Status:** visible in directory. Not added.
- **Use case:** meeting recording, transcript retrieval.
- **Trigger:** only when discovery calls actually need recorded or transcribed automation.

### figma-desktop local bridge · REGISTERED / FAILING
- **Endpoint:** `http://127.0.0.1:3845/mcp` (local Figma desktop bridge, separate from the cloud Figma MCP plugin in §4).
- **Status:** registered in `claude mcp list`, failing to connect. The cloud Figma MCP plugin (§4 ACTIVE / PROVEN) covers all current Figma needs; the local bridge would only matter for desktop-only flows the cloud plugin cannot reach.
- **Use case:** desktop-Figma-specific operations (selection inspection, dev-mode local plugin bridge, local file ops not exposed by the cloud plugin).
- **Trigger:** only if a desktop-only Figma workflow becomes the actual bottleneck. Currently not. Leave failing; do not debug until a job appears.

### n8n / broader automation orchestration · DEFER
- **Status:** not installed.
- **Use case:** multi-step workflow orchestration, scheduled jobs.
- **Trigger:** only when a repeatable manual workflow appears and deserves automation. Not now.

---

## 6. Available skills (Claude Directory + plugin + repo + user)

### Claude Directory skills (newly visible)
- **`/canvas-design`** · visual art, PNG / PDF documents, designed outputs. Trigger: when a fast designed artifact is needed and Figma is overkill.
- **`/web-artifacts-builder`** · elaborate HTML artifacts, landing-page prototypes, reports, interactive visuals. Trigger: when an HTML artifact or rich browser-view output beats a markdown doc.
- **`/mcp-builder`** · build custom MCP servers. Trigger: only when a real external service needs a custom MCP integration.
- **`/theme-factory`** · styling artifacts, slides, docs, reports, landing pages with consistent themes. Trigger: when a designed artifact needs a reusable visual theme.
- **`/skill-creator`** · create or improve skills. Trigger: only after a workflow repeats enough to deserve a skill.

### Figma plugin skills (bundled with the Figma plugin)
- `/figma-use`, `/figma-create-new-file`, `/figma-generate-design`, `/figma-generate-library`, `/figma-generate-diagram`, `/figma-code-connect`, `/figma-use-figjam`, `/figma-use-slides`.
- Trigger: per the Figma MCP tool docs; mandatory loads before specific `use_figma`, `create_new_file`, or `generate_diagram` calls.

### Repo skills (`.claude/skills/` in AI-Brain-Refinery)
- `batch-extraction`, `boardroom`, `challenge`, `jsonl-validation`, `master-consolidation`, `operator-review`, `save`, `session-save`, `source-inventory`, `staging-plan`.
- Trigger: corpus build pipeline + Command Center operator tools.

### User skills (`~/.claude/skills/`, SNIPED-specific)
- 30+ `sniped-*` skills. Key examples: `sniped-direction-stack`, `sniped-canonical-truths`, `sniped-notion-crm-update`, `sniped-higgsfield-pipeline`, `sniped-caption-writer`, `sniped-monday-cockpit`, `sniped-luxury-edit`, `sniped-evoto-skin-pass`, `sniped-capture-to-delivery`, `sniped-discovery-to-close`, `sniped-photo-theory`, `sniped-hit-mechanics`, `sniped-hospitality-layer`, `sniped-leverage-logic`, `sniped-execution-prioritization`, `sniped-art-series`, `sniped-ai-image-tool-pick`, `sniped-ai-photographer-market`, `sniped-ai-sentiment`, `sniped-analog-premium`, `sniped-assistant-task-routing`, `sniped-blockbuster-strategy`, `sniped-company-of-one`, `sniped-hero-composite-ceiling`, `sniped-hero-composite-lite`, `sniped-lighting-vault`, `sniped-new-luxury`, `sniped-partnership-protocol`, `sniped-perennial-seller`, `sniped-lean-audit`.
- Trigger: SNIPED operating workflows; consult the relevant skill before improvising.

---

## 7. APIs (direct, non-MCP access available)
- Figma REST API (also exposed via MCP).
- Notion API (active when Notion MCP installed).
- Stripe API (active when Stripe MCP installed and entity gates cleared).
- Porkbun DNS API (manual today; possible automation later).
- Pixieset, HoneyBook (manual today).
- Adobe SDKs (creative + analytics, covered above).

---

## 8. Local scripts and automation
- `scripts/` in AI-Brain-Refinery (corpus build, validation).
- Chrome-headless PDF render pipeline (verified working, used for the v1 dossier PDF render).
- Pandoc 3.9.0.2 installed (no LaTeX engine present; HTML route preferred).
- Off-machine encrypted zip snapshot workflow (`COMMAND_CENTER_SURVIVAL_AND_RECOVERY`).
- sha256 sidecar verification.
- **Vercel CLI 50.42.0** at `/opt/homebrew/bin/vercel`. **Auth state: ✓ AUTHED as `brycedenj-3481` (2026-05-28).** The deploy path for the `baseplate_site/` static build to `baseplateworks.com`. **Trigger to deploy:** once `baseplateworks.com` is registered and the canonical + Calendly URLs are wired (CURRENT_STATE §5 next actions). Deploy is BJ-approval-gated; do not run `vercel deploy` automatically.
- **Vercel plugin (Claude Code) v0.43.0** at `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/`. Enabled in `~/.claude/settings.json` (`vercel@claude-plugins-official: true`). Installed by BJ on 2026-05-28 alongside the CLI auth. The plugin also surfaced a Vercel MCP (`plugin:vercel:vercel` at `https://mcp.vercel.com`) which currently shows `! Needs authentication` in `claude mcp list`. **Routing today:** the CLI is sufficient for the BASEPLATE deploy path; the Vercel plugin MCP auth is DEFERRED until a real Vercel-MCP-only capability is needed.

---

## 9. Tool inventory categories (the taxonomy the OS tracks)

- Active MCPs (callable now).
- Candidate MCPs (in docs, not installed).
- APIs (direct REST / SDK).
- Local scripts (repo).
- Repo skills (`.claude/skills/`).
- User skills (`~/.claude/skills/`).
- Design tools.
- Creative / media tools.
- CRM / logging tools.
- Payment / admin tools.
- Publishing / distribution tools.
- Research / search tools.
- Local file / backup automation.
- Tools mentioned in source docs but not yet activated.
- Tools active in another terminal / session but not visible here.

---

## 10. The required audit before any "manual" claim

Before saying anything must be manual, unavailable, or done by a designer / human workaround, check:

1. MCP servers in the session (deferred tool list, plugin install dirs).
2. Plugin / connector configs (`~/.claude/`, `~/.claude.json`, plugin cache).
3. Config files referencing the relevant tool (search by name).
4. Repo scripts that touch the task domain.
5. User skills (`ls ~/.claude/skills/`).
6. Repo skills (`ls .claude/skills/`).
7. Prior automation artifacts in `Downloads/` or repo (community intel docs, prior outputs, precedent files).
8. CLI availability for the task tool (`which`, `command -v`).
9. Environment variables / tokens where safe to inspect.
10. Whether another terminal / session has the tool active.
11. Whether an importable or API-compatible fallback exists if the direct tool isn't live.

Only after every line returns "no" can the answer be "manual." **No manual fallback before tool audit. This is the locked rule.**

---

## 11. Routing logic (task class → route target)

| Task class | Route to |
|---|---|
| Reasoning-only (advice, analysis, decision support) | Conversation / skill |
| File creation / edit (repo, docs, configs) | Edit / Write tools + commit protocol |
| External artifact creation (Figma file, design, PDF, image, video, slides) | MCP (Figma, Higgsfield) → `/canvas-design` or `/web-artifacts-builder` → Chrome-headless / pandoc → manual last |
| External system update (Notion, Stripe, calendar, DNS) | MCP if installed → API → manual last |
| Research / current-info | Search MCP / WebFetch / WebSearch → corpus → manual last |
| Payment / admin | Stripe MCP / API (gated on 147C + bank) → manual now |
| Design / media | Figma MCP / Adobe for Creativity → Higgsfield MCP → CLI tools → manual last |
| Automation (multi-step workflows) | repo scripts + cron / n8n later → manual now |
| Publishing / distribution | repo site tooling + publishing API → manual last |
| Email / inbox | Gmail connector (approval-gated for sending) → manual last |
| Analytics | Adobe Analytics MCP / CJA MCP when authed and traffic exists → manual / defer until then |

Manual is always last. It is the fallback, not the default.

---

## 12. Skill / tool trigger examples

- **Dossier / design** → Figma MCP before manual Figma. `/canvas-design` when speed matters and brand-bible precision is not the bottleneck. `/theme-factory` when the design needs a reusable theme system.
- **HTML artifact / landing prototype / interactive report** → `/web-artifacts-builder` before manual HTML.
- **Concept film / motion / visual assets** → Higgsfield MCP or its CLI before generic prompt-only. `sniped-higgsfield-pipeline` skill wraps it.
- **CRM / proof log** → Notion MCP when installed; local PROOF_LOOPS + SNIPED proof log SOP today.
- **Payments / invoices** → Stripe / Pixieset only after 147C + business bank account.
- **Site changes** → repo `baseplate_site/` tooling, not abstract copy.
- **Backups** → COMMAND_CENTER_SURVIVAL_AND_RECOVERY workflow, not memory.
- **Research / current-info** → search MCP / WebFetch / WebSearch when post-corpus current data is required.
- **Docs / playbooks** → repo file edits via Edit / Write + commit protocol.
- **Content / campaigns** → Adobe for Creativity for image editing, retouching, compositing; Figma for layouts; Higgsfield for motion; `sniped-*` skills for SNIPED workflows.
- **Custom MCP creation** → `/mcp-builder` only when a real external service needs a bespoke integration.
- **New skill creation** → `/skill-creator` only after a workflow repeats enough to deserve a skill.
- **Analytics** → Adobe Analytics MCP or CJA MCP once traffic exists. Not now.

---

## 13. Context-bloat rule

- Tool index lives here (this doc). Activate only relevant tool(s) per task.
- **Skills first** for reasoning and workflow consistency (skills do not burn tool-description tokens).
- **MCPs / APIs** when external execution is needed.
- **Scripts** for local / repo automation.
- **No 20-MCP spiral.** Over 5 active MCPs burns context on tool descriptions before any question lands.
- **No installing tools without a live job.** Each install needs a real task that depends on it.

---

## 14. Max plan utilization standard

- Less generic chatting about how a task could be done.
- More artifact creation that produces real outputs.
- More connected execution through MCPs / APIs / scripts.
- More structured tool routing before defaulting to advice.
- More use of the existing OS instead of re-deriving.
- Fewer repeated reminders from BJ about tools already installed.
- Decisions turn into files, designs, sites, workflows, assets, commits, logs, or real external outputs.

If a turn ends without an artifact when one was possible, the turn under-used Max.

---

## 15. Near-term approved toolchain posture

| Tool | Status | Trigger |
|---|---|---|
| Figma MCP (cloud plugin) | ACTIVE / PROVEN | Any design, layout, dossier, brand visual |
| Gmail connector | AVAILABLE / CONNECTED | Email tasks, approval-gated for sending |
| Adobe for Creativity | VISIBLE / ADDED | Creative-production tasks (edits, polish, composites) |
| Airtable connector | AVAILABLE / CONNECTED | CRM, proof log, content calendar, structured records |
| Higgsfield CLI + 5 skills | ACTIVE / AUTHED (Plus, 992 credits) | Image / motion / Marketing Studio / Soul / marketplace generation |
| Higgsfield MCP (claude.ai connector) | ACTIVE / CONNECTED | Parallel surface to CLI; route via CLI today |
| Google Drive | CONNECTED (temp bridge) | Personal Google + admin@snipedmedia.com bridges; no cross-account moves; no permanent BASEPLATE Workspace anchoring |
| Google Calendar | CONNECTED (temp bridge) | Same temp-bridge posture as Drive |
| Stripe MCP | QUEUE post EIN correction + bank | EIN legal-name correction PENDING (2026-05-28); business bank account opening also gated |
| Notion MCP | QUEUE for CRM / proof | Discovery-call logging volume |
| Adobe Analytics MCP | CANDIDATE analytics | When traffic exists |
| Customer Journey Analytics MCP | CANDIDATE analytics | When journey data exists |
| Search / Research MCP | DEFER | Only when current-info task arises |
| Microsoft 365 | AVAILABLE | Only if M365-resident workflow appears |
| Notion connector | AVAILABLE / NOT ADDED | Only on a real Notion workflow |
| HubSpot | AVAILABLE / NOT ADDED | Only if BASEPLATE outgrows lighter CRM |
| Zoom | AVAILABLE / NOT ADDED | Only when call recording automation is needed |
| figma-desktop local bridge | REGISTERED / FAILING | Defer; cloud Figma plugin covers current needs |
| Vercel CLI 50.42.0 | ✓ AUTHED as brycedenj-3481 | Ready for deploy once `baseplateworks.com` registers + URLs wire |
| Vercel plugin v0.43.0 (Claude Code) | INSTALLED / ENABLED | MCP needs auth, deferred; CLI covers current needs |
| n8n / automation | DEFER | When a repeatable workflow exists |

Do not install 20 MCPs. Install on a job, not on a hope.

---

## 16. Guardrails (carry every session)

- No tool spiral.
- No installing tools without a live job.
- **No AI-generated fake proof.**
- No fake clients, fake facilities, fake crews, fake testimonials, fake metrics.
- No BASEPLATE / SNIPED contamination (separate brands, separate surfaces, no cross-redirects).
- No skipping IRS / admin gates (147C → bank → Stripe, in that order).
- No replacing real proof with creative output. Higgsfield and Adobe for Creativity are concept, atmosphere, polish; never client evidence on BASEPLATE. SNIPED may publish AI-forward creative openly as art and mythology, never as fake client proof.
- No context bloat from too many MCPs.
- No public / private leakage (Direction Stack stays private; EIN stays off public surfaces; employer information stays off all BASEPLATE / SNIPED material).
- **No manual fallback before tool audit. This is the locked rule.**
- Anchor-class: markdown-only, not chunked, not in master files, total_chunks unchanged at 1,837. No master / raw / Bible / site changes from this doc.

---

## 17. Persistence and updates

- This doc is the single source of truth for tool layer status. Updated whenever a tool is added, authed, queued, or deferred. The Status field is authoritative.
- A targeted amendment to `COMMAND_CENTER_RESPONSE_PROTOCOL.md` is a separate gated edit that inserts the §1 mandatory tool-layer check into the routing step. That edit is queued, not done in this pass.
- A `/tool-audit` or `/execute-via-toolchain` skill may be built later via `/skill-creator` after the doctrine has been used enough to deserve one. Not now.

---

## 18. Sources consulted / OS routing receipt

- **Level:** 4 (operating doctrine).
- **Sources:** TOOL_LAYER_INTEGRATION_PASS (in-thread, 2026-05-27), the live Figma MCP build session (2026-05-27, dossier file `p7qWs3AhjTHZa6vDZGoKGE`), `COMMAND_CENTER_RESPONSE_PROTOCOL.md`, `FIGMA_MCP_COMMUNITY_INTEL.md`, Claude Code plugin install (`figma` v2.2.12), Claude Directory connector list confirmed by BJ on 2026-05-27, the user-level `sniped-*` skill library, the repo `.claude/skills/` library, BASEPLATE thesis docs, SNIPED architecture docs, `COMMAND_CENTER_SURVIVAL_AND_RECOVERY.md`.
- **Skipped (and why):** master corpus / raw / Bible (out of scope by design); `baseplate_site/` (no edits required for this doctrine).
- **Proof-loop link:** the locked rule (no manual fallback before tool audit) is observable. Every future turn either routes through this doc or violates it. The Figma MCP build of the sample dossier is the first proof point.
- **Guardrails applied:** the §16 set.
