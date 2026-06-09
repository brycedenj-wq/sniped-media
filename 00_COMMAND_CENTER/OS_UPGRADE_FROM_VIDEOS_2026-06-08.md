# OS UPGRADE FROM VIDEOS · 2026-06-08

Source: 4 dissected videos on Claude Code's new orchestration surfaces (Dynamic Workflows, Managed Agents, Routines) plus the six composable workflow patterns. Synthesized into concrete upgrades for the SNIPED OS (activation spine, conductor, proof gates, 78 skills, just-started Workflow use, hooks, /watch).

---

## 1. THE THESIS

These four videos collectively say one thing: **stop operating single-threaded and manual. The unit of work is no longer a chat turn, it is a harness.** Claude Code now ships three native ways to run a harness, and they stack into a ladder:

- **Dynamic Workflows** (a runtime script that fans work across dozens-to-hundreds of fresh-context subagents, with phases, parallel/pipeline primitives, and a saved `.workflow.js` file) are the answer to long, parallel, or adversarial work. They exist because a single long-context agent degrades in three named ways: **agentic laziness** (declares done at 35 of 50 items), **self-preferential bias** (cannot judge its own output against a rubric), and **goal drift** (loses "don't do X" constraints across lossy compaction). A workflow fixes all three structurally by giving each subagent one isolated goal and its own context.

- **Managed Agents** (hosted in Anthropic's cloud, defined as version-controlled YAML, built on Agent / Session / Environment / Credential Vault) are the answer to recurring single-job work that should run unattended without you managing infrastructure. An agent is "an AI employee with one very specific task." Tighter scope plus narrower tools equals better outcomes.

- **Routines** (scheduled local or remote runs, prompt-as-reasoning-layer, cron + API + GitHub triggers) are the answer to cadence: laptop-off, recurring, connector-driven jobs. The reasoning (prompt) stays identical local to remote; only the engine moves to the cloud.

The connecting law across all three: **the human approval gate moves to the boundary, not the middle.** There is no mid-run pause in routines and no human-in-the-loop inside a fan-out phase. Approval lives between two harnesses (Routine A drafts and posts for review, operator approves, Routine B ships), or at the plan-approval step before a workflow runs, or as a per-tool permission policy in the agent spec. And the second connecting law: **adversarial verification is a first-class phase, not an afterthought.** Every high-stakes harness ends with a fresh-context agent trying to break the result before a human sees it. That is exactly our Gemini hostile-critic lane, promoted from a side script to a standing Verify phase.

For SNIPED specifically: this is the operating-system upgrade that turns our 78 skills from things-we-invoke into **agentType targets a conductor fans out to**, turns our locked SOPs into **saved named workflows with a hard approval gate at the authorize step**, turns our proof gates into a **mandatory Verify phase no result is crowned without**, and turns our daily/weekly cadence skills into **scheduled routines that run with the laptop closed.** Default working mode flips from manual single-thread to orchestrate / monitor / promote.

---

## 2. PER-VIDEO: CORE FEATURE + HIGHEST-VALUE ADOPT

### Video 1 · Sean Kochel, "Claude Code Workflows Are A Gift" (27m)
- **Core feature:** Reusable `.claude/workflows/*.workflow.js` files: a dynamic harness written in natural language, compiled to a strict JS schema, orchestrating subagents via three primitives: `agent()` (per-agent model / isolation / schema / agentType), `parallel()` (fan out + barrier), `pipeline()` (ordered stages). Six composable patterns on top: Classify-And-Act, Fanout-And-Synthesize, Adversarial Verification, Generate-And-Filter, Tournament, Loop-Until-Done. The real lesson is that every real workflow **stacks about three patterns.**
- **Single highest-value adopt:** **Rebuild our Gemini second-model lane as an Adversarial Verification workflow** (N parallel fresh-context skeptics, each scoped to one axis: face-lock, grade-drift, claim-truth). He calls adversarial his favorite because LLMs lock onto a narrative and fresh-context debate breaks the lock. This is the single most aligned upgrade to our existing narrative-lock defense.

### Video 2 · Chase AI, "The Most Powerful Claude Code Feature In Months" (15m)
- **Core feature:** Dynamic Workflows as a built-in "harness for every task," exposed through a new `/effort` tier called **`ultracode` (= xhigh effort + dynamic workflow orchestration)** and the `/workflows` command, shipping bundled workflows like `/deep-research`. Runs detached in the background; you monitor via a phases-and-subagents progress view (controls: up/down select, x stop, p pause, esc back, s save). Proof of scale: Bun ported Zig to Rust, ~750k lines, 99.8% tests passing, 11 days, hundreds of agents with two reviewers per file.
- **Single highest-value adopt:** **Defend against the three named failure modes explicitly in `os_stop_check`.** (a) Agentic laziness: gate must count items done vs required and refuse "done" on partial (we already do this for master chunk counts; generalize it). (b) Self-preferential bias: never let the generating model crown its own output, route to the second-model gate. (c) Goal drift: persist the original goal plus "don't do X" constraints in a pinned file the workflow re-reads each phase (our STANDING_ORDER / NEXT_ACTION, made re-read-per-phase). This is the precise, named diagnosis of why manual long-context runs fail us, with the fix.

### Video 3 · Build Great Products, "Claude Managed Agents" (16m)
- **Core feature:** Hosted agent platform in the Claude Console built on 4 primitives (Agent / Session / Environment / Credential Vault). The agent is a portable YAML/JSON spec (name, model, system, mcp_servers, tools, default_config.permission_policy) you POST to `/v1/agents`. Runs in Anthropic's cloud sandbox; credential vault stores OAuth once. Bills the API key, not a subscription. Session transcript logs every step, tool call, token count, and error inline.
- **Single highest-value adopt:** **Ship the Gemini read-only hostile-critic lane as the first Managed Agent** (read-only, scheduled, evidence-only output: lowest risk, proves the pipeline). Its session transcript IS an `os_proof_manifest`: an adapter pulls the trace and emits our manifest format, and `os_stop_check` gates "done" on it (inline errors = automatic stop). This validates trace-to-proof before we ever hand a write/spend agent the keys.

### Video 4 · AI Master, "How to Use Claude Routines" (21m)
- **Core feature:** Claude Routines: scheduled Local (4 fields: Name, Description, Instructions, Schedule) or Remote (adds Repository, Environment, Triggers, Connectors) runs. The prompt is the reasoning layer and stays identical local to remote. Triggers: Schedule (1hr floor), API (HTTPS endpoint + bearer, fires immediately), GitHub events. Secrets go in the cloud Environment Variables panel, never `.env` (gitignored, fails silently). Remote runs are stateless: persist via push-to-GitHub or connector. Branch guardrail: Claude can only push `claude/*`. Session log reads like a PR diff.
- **Single highest-value adopt:** **The two-step human-approval architecture as standing OS law.** Routines have no mid-run pause, so our `os_stop_check` / `os_proof_manifest` gates must live BETWEEN two routines: Routine A generates plus writes the proof manifest plus posts to a review surface, operator approves, Routine B publishes via API trigger. This makes autonomous SNIPED work safe by construction and matches our existing "operator authorizes" discipline.

---

## 3. CONCRETE OS UPGRADES

### 3.1 New directory + first workflows
Create `00_COMMAND_CENTER/.claude/workflows/` and convert these chained-skill routines into saved `.workflow.js` files (natural-language description using the exact pattern vocabulary so generation is deterministic; commit each; `s` to save and name):

1. **`adversarial-verify.workflow.js`** (Adversarial Verification + Fanout). N parallel fresh-context skeptics, each scoped to one fail-definition: face-lock (reuse `os-face-lock`, `os-vision-reject-gate`), grade-drift (reuse `composite-master-qa`, `platform-mastering`), claim-truth (reuse the Gemini lane). Barrier-synthesize into one verdict. This is the standing Verify phase appended to every other workflow.
2. **`hero-finish.workflow.js`** (Loop-Until-Done). Wrap `os_proof_manifest` / `os_stop_check`: a hero is auto-"finished" only when proof criteria pass, tied to `/goal`. No hand-crowning.
3. **`batch-sop.workflow.js`** (the locked 7-step batch SOP as a saved workflow). Inventory to plan to AUTHORIZE (hard human-approval gate, matches "operator authorizes the copy pass") to stage to extract to chunk+validate (Loop-Until-Done against `jsonl-validation`) to consolidate. Each batch's extract/chunk/validate is an isolated-context subagent so a 30-file batch never poisons the parent (directly supports the "escalate at 70% context" rule).
4. **`route-and-act.workflow.js`** (Classify-And-Act). Make the 78 routable skills the agentType targets, driven by `sniped-command-router`. Evolve the 16-field routing receipt into automatic routing instead of a manual think.
5. **`mine-os-md.workflow.js`** (Fanout + Adversarial + Loop, PROPOSE-ONLY). Mine Claude Code session history in parallel chunks, two skeptic lenses (structure/inferable, novelty/truth), stop after 2 clean rounds, emit paste-ready candidate blocks for CLAUDE.md / AGENTS.md / ACTIVE_KNOWLEDGE_STATE.md. Never auto-writes, per our `/ingest` no-auto-write law.
6. **`creative-tournament.workflow.js`** (Tournament + Generate-And-Filter). For caption / hook / landing / title lanes: generators produce candidates, pairwise judges run a bracket (cycles default 3) judged against `sniped-canonical-truths` + brand memory as the rubric, keep the winner, discard the rest.

### 3.2 Workflow conventions (standardize these in every workflow file)
- **Per-phase model routing as a cost law.** Default subagents to Sonnet/Haiku, reserve Opus for the single hardest phase. Fits premium-stack-maximization-law and prevents the million-token blowups he warned about (his own React tournament would have matched quality on Sonnet at far lower cost).
- **Hard token budget + `maxRounds` (<=6) + cycle cap in every workflow**, plus a token-budget sentence in the prompt ("you can only use 100,000 tokens for this entire run"; the model adheres). Wire `/goal` into `os_stop_check` for a measurable stop. This is the biggest cost-safety lever and matches our count-before-assuming rule.
- **`isolation: 'worktree'` for any file-writing workflow** (composite builds, batch-extraction, web edits) so parallel agents commit independently. Pairs with our branch-first git rule and the routines `claude/*`-only branch guardrail.
- **Backlog-file convention.** Discovery-phase workflows write findings to a durable backlog md so reruns skip rediscovery, exactly like MASTER_INDEX.md / ACTIVE_KNOWLEDGE_STATE.md already do.
- **Every workflow ends with the Verify phase** (`adversarial-verify`). No result is crowned until a dedicated adversarial pass tries to break it.

### 3.3 ultracode tier in the activation spine
Add an **ULTRACODE mode** to `os_activate.py` / the master conductor: highest gate-discipline + dynamic-workflow fan-out. The conductor sets `/effort ultracode` and spawns a workflow instead of one long agent when a task is **long, parallel, or adversarial** (full batch extraction, whole-Mac source routing, a multi-hero composite QA sweep). Adopt the docs "When to use a workflow" decision table as a router rule in `sniped-command-router`: classify by who holds the plan (Claude turn-by-turn = subagent, lead-supervises-peers = agent team, runtime script decides = workflow) and by agent count (a few = subagent, dozens-to-hundreds = workflow). The router stops defaulting to a single agent.

### 3.4 The six patterns as named conductor routines, wired to existing skills
- **Classify-And-Act** = `sniped-command-router` (already a classifier).
- **Fanout-And-Synthesize** = Gemini second-model lane + corpus retrieval run.
- **Generate-And-Filter** = banana/seedream plate generation to `composite-master-qa` rubric, keep best.
- **Tournament** = pairwise adversarial judging for hero selection / title-idea selection.
- **Loop-Until-Done** = batch chunk to `jsonl-validation` to re-chunk until pass.
- **Adversarial Verification** = the standing Verify phase / Gemini lane.

### 3.5 Managed Agents lane (cloud, unattended)
- Stand up `00_COMMAND_CENTER/managed_agents/*.yaml` as version-controlled agent specs the conductor can register and route to, mirroring how we register the 78 skills. Our skills are already paragraph job descriptions: they convert ~1:1 into the agent `system` block.
- Map our primitives onto the 4: skills/spines = Agent system prompts; `os_activate.py` session = Session; blender_sandbox + permission gates = Environment; a new **Credential Vault** for MCP keys (Notion, Higgsfield, ElevenLabs, Adobe) instead of scattered tokens (hardens the credential story in memory).
- **Per-tool permission_policy:** `always_allow` only for read-only/safe MCP tools; require-approval for write/spend tools (Higgsfield generate, anything that costs API budget). Operationalizes "prove any skip with the exact blocker" + premium-stack law.
- **Session-trace-to-proof-manifest adapter:** pull a Managed Agent session trace, emit it in `os_proof_manifest` format, gate "done" on it via `os_stop_check`. Inline errors = automatic stop trigger.
- **API budget standing order.** Managed Agents bill the API key, not a subscription. Add a budget line + Analytics watch to ACTIVE_KNOWLEDGE_STATE / STANDING_ORDER before any agent runs on a schedule.
- **First agent = Gemini read-only critic** (lowest risk, proves trace-to-proof before any write/spend agent).

### 3.6 Routines lane (cadence, laptop-off)
- Build **`os_routine_emit.py`**: exports any of the 78 skills into a Routine spec (Local 4-field; Remote adds Repository/Env/Triggers/Connectors).
- **Two-step approval law (standing):** Routine A generates + writes proof manifest + posts to review surface; operator approves; Routine B publishes via API trigger. Encode in AGENTS.md.
- **First production routines:** `sniped-operator-plan` (/today) and `sniped-monday-cockpit` as remote routines, weekday/Monday 8am local (timezone-aware), pulling Calendar + Gmail connectors. The Gemini lane as a nightly remote routine that critiques the day's drops to a review surface, never crowning final.
- **Structured-context-by-file:** store volatile state (active client list, current operating lock, NEXT_ACTION) as repo files the routine reads at runtime; update the file, not the prompt. Mirrors ACTIVE_KNOWLEDGE_STATE.md.
- **Secrets discipline (add to AGENTS.md):** keys go in the cloud Environment Variables panel, never `.env`; every remote routine prompt includes "The API key is available as an environment variable. Do not look for a .env file." Local MCP stack (Premiere, After Effects, Blender, ElevenLabs, Higgsfield) is NOT reachable remotely: any remote routine needing them uses cloud connectors / a hosted custom-connector URL, otherwise keep that work LOCAL.
- **Statelessness rule:** a remote routine cannot rely on local disk; 01_KNOWLEDGE_BASE master writes must be committed to GitHub within the run or they vanish. Reinforces "master-consolidation only writes master files."
- **Branch guardrail (`claude/*` only) + `os_quality_gates`** as the human review step before merge for any repo-touching routine.
- **Keep n8n as the plumbing layer** (we have n8n-mcp): high-frequency triggers POST to a routine's API endpoint for the reasoning-heavy SNIPED step. Collaborators, not competitors.

### 3.7 Settings / hooks to add
- **`/loop` cadence** for recurring chores: nightly os-backup, daily operator-plan, Monday cockpit. Maps onto CronCreate/schedule we already have; standardize daily/weekly skills behind one recurring loop.
- **Background + monitor pattern:** run long jobs detached, pair the workflow with the Monitor tool emitting one line per phase completion/failure, and a PushNotification on terminal states. Upgrades our Workflow usage from foreground-blocking to detached-with-progress-view.
- **`os_stop_check` hardened** against the three failure modes (count items, route judging to second model, re-read pinned goal each phase).
- **Tight "when to use" blocks** in every workflow file, because workflows can auto-trigger.

### 3.8 What changes about our DEFAULT way of working
**From:** one long single-threaded manual Claude Code session per task. **To:** the conductor classifies every arriving task (Classify-And-Act) and routes it to the right harness:
- A few delegated steps → subagent.
- Lead supervising peers → agent team.
- Runtime decides, dozens-to-hundreds of agents, resumable, background → **workflow**.
- One recurring scoped job, unattended cloud → **Managed Agent**.
- Cadence, laptop-off → **Routine**.

We operate via **orchestrate (spawn the harness) → monitor (progress view + Monitor + notifications) → promote (save the good harness, approve at the boundary, crown only after the Verify phase).** Manual single-thread becomes the exception, used only for genuinely interactive creative judgment.

---

## 4. PRIORITIZED ACTION LIST

1. **Create `00_COMMAND_CENTER/.claude/workflows/` and build `adversarial-verify.workflow.js`** (rebuild the Gemini lane as N parallel fresh-context skeptics: face-lock / grade-drift / claim-truth). Highest-aligned, reuses existing gate skills, becomes the standing Verify phase for everything else. (Videos 1+2+3)
2. **Harden `os_stop_check` against the three named failure modes** (laziness: count done vs required; bias: never self-crown, route to second model; drift: re-read pinned STANDING_ORDER/NEXT_ACTION each phase). Cheap, foundational, makes every future harness safe. (Video 2)
3. **Encode the two-step approval law + secrets discipline + statelessness rule into AGENTS.md** (Routine A drafts/posts → operator approves → Routine B ships; keys in env panel not `.env`; commit master writes within the run). Governs all autonomous work before we turn any on. (Video 4)
4. **Build `hero-finish.workflow.js` (Loop-Until-Done) and `batch-sop.workflow.js`** with the hard approval gate at the authorize step, per-phase model routing, token budget, `maxRounds<=6`, and `isolation: 'worktree'`. Converts our two most-run SOPs to saved harnesses. (Videos 1+2)
5. **Ship the Gemini read-only critic as the first Managed Agent** + write the session-trace-to-`os_proof_manifest` adapter. Proves the cloud + trace-to-proof pipeline at lowest risk. (Video 3)
6. **Schedule `sniped-operator-plan` and `sniped-monday-cockpit` as remote routines** (8am local, Calendar+Gmail connectors), plus the Gemini nightly-critique routine to a review surface. First real laptop-off production cadence. (Video 4)
7. **Add ULTRACODE mode to `os_activate.py` + the "when to use a workflow" decision table to `sniped-command-router`** so the conductor auto-routes long/parallel/adversarial tasks to workflows instead of a single agent. Flips the default operating mode. (Videos 1+2)
8. **Build `mine-os-md.workflow.js` (propose-only) and `creative-tournament.workflow.js`**, then `os_routine_emit.py` to export any skill to a routine spec. Compounding leverage once the core harnesses are proven. (Videos 1+4)
