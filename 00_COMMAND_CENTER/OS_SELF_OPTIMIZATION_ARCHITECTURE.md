# OS SELF-OPTIMIZATION + CONTINUITY ARCHITECTURE (2026-06-04)

> The machine that keeps the machine alive. Not strategy. Infrastructure for how Claude operates the OS so every next answer, asset, campaign, and proof loop is stronger, and so the OS survives resets, failed runs, cost limits, tool errors, and file sprawl without depending on one chat, one memory, one file, or one fragile run.
>
> Born from the OS engagement run that hit and solved: the 25k-token Read cap, mid-run session caps, the 1M-context consolidation gate, poisoned-cache resumes, inflated-completion claims, and derivative-doc anchoring. Those lessons are now law below.

---

## 1. SOURCE OF TRUTH

**Canonical tiers (highest authority first):**
1. **Today's proof + the live operator's current instruction** , overrides everything below.
2. **Memory** (`~/.claude/projects/-Users-sniper/memory/*.md` + `MEMORY.md` index) , locked operating rules + identity/context.
3. **Master doctrine + capability map** (`OS_MASTER_DOCTRINE.md`, `OS_CAPABILITY_MAP.md` + per-dimension) , the distilled, verified synthesis.
4. **Manifest** (`OS_ENGAGEMENT_MANIFEST.csv`) , the only ledger of what is verified vs pending. The manifest is the source of truth for coverage, never a dashboard.
5. **Doctrine docs** (`OS_DOCTRINE_*.md`) , distilled per-source intelligence.
6. **Raw sources** (`/Downloads/    SNIPED_OS/`, `/raw/`) , evidence, read-on-demand.

**Folder roles:**
- `00_COMMAND_CENTER/` , canonical OS artifacts: doctrine, capability, dashboards, architecture, protocols, manifests, this file.
- raw corpus (`Downloads/    SNIPED_OS/`, `raw/`) , RAW SOURCES (evidence only).
- `OS_DOCTRINE_*` , DOCTRINE (distilled).
- `OS_CAPABILITY_*` , extracted capability (skills/connectors/gates/routing).
- `.claude/skills/` , SKILLS (executable).
- `OS_ENGAGEMENT_JOURNAL.md` , append-only LOGS.
- `OS_*_DASHBOARD.md` , DASHBOARDS (derived, never source).
- `OS_FROMZERO_* / OS_POSSIBILITY_* / OS_OFFGRID_*` , EXPERIMENTS / strategy outputs (evidence, never law).
- `*_archive*`, `.prev` siblings , ARCHIVES (preserved, never deleted).

**How old docs inform without controlling:** old docs are court evidence (pattern + survival + contradiction), never law. Recency and confidence do NOT win; current proof wins. A doc dated before today is downgraded the moment it conflicts with today's reality. Old offer NAMES, lane names, and directions are quoted as evidence and explicitly tagged `[old/derivative, evidence-only]` so they never become accidental law. The `proof-before-crowning` and `anti-old-lane-anchoring` gates (Section 9) enforce this on every answer.

---

## 2. STATE MANAGEMENT

**Session start protocol (read in this order, stop at first sufficient):**
1. `MEMORY.md` index (auto-loaded) , the locked rules + context.
2. `00_BRIEF/CURRENT_STATE.md`, `STANDING_ORDER.md`, `NEXT_ACTION.md` , what is live now.
3. `OS_ENGAGEMENT_DASHBOARD.md` (the engaged %, audit taxonomy) + tail of `OS_ENGAGEMENT_JOURNAL.md` (last 3 batch entries) , what changed.
4. `00_BRIEF/ROUTING_MANIFEST.md` only for the active domain , pull the row, do not preload the OS.
5. The relevant doctrine/capability doc ONLY for the task at hand.

**Session end protocol:** append a journal entry (what changed / promoted / weakened / contradictions / pending / next exact step); update `CURRENT_STATE.md` + `NEXT_ACTION.md`; never leave a run claiming "done" without the completion-verification gate passing.

**Current-state summarization:** one source of live truth = `CURRENT_STATE.md`. If two state files conflict, the newer timestamp + manifest reconcile; the older is archived with a note. Never maintain two "current state" files.

**Cross-tool handoffs (Claude Code / ChatGPT / Obsidian / local):** the portable spine (`00_BRIEF/THE_SPINE.md`) is the bootstrap , paste into any AI to restore context. State lives ON DISK, never only in a chat thread. Obsidian mirrors `00_COMMAND_CENTER` doctrine + dashboards (read-only mirror). A handoff packet = THE_SPINE + CURRENT_STATE + NEXT_ACTION + the relevant doctrine doc.

**Reset survival / resume:** because state is on disk, a reset loses nothing. To resume unfinished work without guessing: read `NEXT_ACTION.md` + the journal tail + the manifest's non-`read_verified` rows. For an interrupted workflow, resume by `resumeFromRunId` (cached agents return instantly); if the cache is poisoned (session-limit strings), cache-bust the failed step's label/prompt and re-run only that step.

---

## 3. CLAUDE OPERATING MODES

Ten modes. Each: trigger, must-read, allowed tools, forbidden, output format, exit gate.

| Mode | When | Must read | Tools | NOT allowed | Output | Exit gate |
|---|---|---|---|---|---|---|
| **Strategy** | "what should I / what's possible / which lane" | master doctrine, capability map, READY_FOR_STRATEGY | read/grep, Web (current market), workflow (fan-out) | crown a lane, lock identity, lean on unverified pile silently | options + trade-offs + proof loops, cited | proof-before-crowning + optionality + identity-collapse gates |
| **Execution** | a concrete task to advance state | NEXT_ACTION, the domain spine row | edit/write, bash, MCP per routing | invent new strategy, scope-creep | the artifact + state update | completion-verification + output-usefulness gates |
| **Research** | needs facts/market/current data | the question; existing OS first | Web/WebFetch, grep corpus | present stale OS as current; skip sourcing | cited findings + freshness note | source-freshness + anti-hallucination gates |
| **Critique** | review/red-team/pressure-test | the target artifact + relevant doctrine | read, adversarial sub-agents | rubber-stamp; agree by default | findings + verdict + fixes | anti-hallucination (verify each claim) gate |
| **Build** | make a skill/pipeline/tool/site | capability map, existing skills | write/edit, bash, node, MCP | bloat; duplicate an existing skill | the working artifact + test | completion-verification + skill-lifecycle gates |
| **Writing** | copy/article/caption/script | voice memory, positioning doctrine | write, read | em-dashes (lifetime rule); AI-tell transitions | the copy, on-voice | output-usefulness + voice gates |
| **Design** | UI/visual/layout/brand asset | visual doctrine, v3 LUXURY, gates | Figma/Adobe MCP, image tools | break the reject gates; teal/orange | the asset + QA scorecard | composite/photo QA + beat-source gates |
| **Automation** | recurring/scheduled/agentic | tool-routing map, cost protocol | workflow, cron/launchd, MCP | runaway swarms; unbounded loops | the automation + a kill switch | cost/runaway + completion gates |
| **Proof-loop** | design a test that kills/keeps/scales | proof-loop doctrine | read, write | declare success without a metric | the loop (24h/7d, kill/keep/scale, $ path) | proof-before-crowning gate |
| **Recovery / Audit** | something failed / verify completion / repair | manifest, journal, error dashboard | bash, read, token-safe-reader | claim done without proof; delete | the audit + repaired state | completion-verification + reliability gates |

**Mode discipline:** one mode at a time. The router (Section 4) assigns the mode before any answer. Strategy mode NEVER crowns; Execution mode NEVER invents strategy; Recovery mode NEVER fakes completion.

---

## 4. COMMAND ROUTER

Built as a skill (`.claude/skills/os-command-router/SKILL.md`). Every request is classified BEFORE answering. Routing decisions:
- Mode (the 10 above).
- Verified-doctrine required? (almost always yes , cite it.)
- Current web research required? (facts/market/2026-state , yes.)
- Legal/ethical/employer-conflict risk? (anything employer-adjacent, identity-exposing, or likeness-based , raise the gate, may refuse/redirect.)
- Must refuse to crown a lane? (any strategy/identity question , yes.)
- Tool route (which MCP/local/web/manual , per the tool-routing map).
- Cost tier (cheap haiku reads vs sonnet synthesis vs opus judgment).
- Output format + exit gate.

The router outputs a one-line routing receipt (mode · doctrine · tools · gates · cost-tier) before executing. Refuses only on a Class-A hard constraint (legal/employer-conflict/destructive). Defaults to ROUTING, not refusal.

---

## 5. RELIABILITY PROTOCOL

**The non-negotiable lessons, now law:**
- **Token-cap rule:** Read errors (does not truncate) above ~25,000 tokens. NEVER segment by raw words/lines. Re-wrap to ~180-char lines, segment by CHAR count (<=40k chars approx 10k tokens). (`os-token-safe-reader` skill.)
- **Coverage is proven, never assumed:** a source is `read_verified` ONLY when every token-safe segment lands (got == total, fail == 0), beginning-middle-end covered. Partial = `partial_read_only` -> targeted re-read.
- **No false done:** the completion-verification gate must pass before any "done." "Conversion returned text" != read. "Workflow completed" != read. Check the manifest, not a vibe.
- **Everything logged:** partial reads, failed conversions, OCR gaps, visual books, video files, tool errors -> their own status (`needs_ocr` / `needs_visual_review` / `needs_transcription` / `partial_read_only` / `conversion_failed`) in the manifest + the error/quarantine dashboard. Nothing silently dropped, nothing silently "done."
- **Complete vs pending:** the manifest status column is the single arbiter. Dashboards derive from it; if a dashboard disagrees, the manifest wins and the dashboard is corrected.
- **Consolidation safety:** keep any single agent's input under ~200k tokens (avoid the 1M-context gate) , <=12 books/shelf or raise shelf count; two-stage reduce (chunk-digest -> merge) for big syntheses.

---

## 6. NO-BREAK WORKFLOW (git / backup / recovery)

- **Git:** version the OS *text* (`00_COMMAND_CENTER/*.md`, `*.csv`, `.claude/skills/`, `00_BRIEF/`). `.gitignore`: books, media, `*.epub/pdf/mobi/azw3/djvu/mp4`, `/tmp` artifacts, `raw/` heavy binaries, converted-text caches. NEVER commit books/media.
- **Backup:** OS text -> git remote (private) + a cloud-mirrored copy of `00_COMMAND_CENTER`. Raw corpus -> local + one cloud cold copy (not git). `.prev` siblings on any destructive-ish edit for instant rollback.
- **Versioned:** doctrine, skills, dashboards, protocols, manifest. **Archived (not versioned):** superseded syntheses, old-export docs, batch logs. **Never deleted:** anything , classify (`derivative`/`archive`), never `rm`.
- **Recovery from a bad run:** (1) stop the run (TaskStop); (2) read the manifest + journal to see what actually landed; (3) re-grade by coverage, not by the run's claim; (4) re-fire only the failed/poisoned segments (cache-bust labels); (5) reconcile the dashboard from the manifest.
- **Anti-drift:** one `CURRENT_STATE.md`, one manifest, one dashboard-of-record per concern. A consistency check (no duplicate manifest paths, no empty statuses, no orphan dashboards) runs at every major checkpoint. Duplicate doctrines are merged with the newer kept and the older archived.

---

## 7. COST + USAGE CONTROL

- **Model tiering:** haiku for cheap whole-reads/segment reads; sonnet for synthesis/consolidation (it has weekly headroom , use it for quality); opus (main loop) kept LEAN (short turns , it is the per-token-expensive driver).
- **Budgets:** check `/usage` before and after any major run. Session cap is a 5-hour window; week caps reset weekly. Sonnet has the most headroom; opus the least slack.
- **Batch sizing:** size a wave to fit session headroom; NEVER run waves concurrently (concurrent waves drain the session mid-run , proven failure). One wave at a time. ~700-800 segments/wave max; split bigger.
- **Stop-and-ask triggers:** book-layer/large spend before committing; storage < 25GB free; a real destructive/credential/legal risk; cost materially exceeding the stated estimate.
- **Runaway prevention:** every workflow capped (1000 agents hard); loops bounded by budget or a kill counter; overnight runs sequential + self-grading + journaled, never an unbounded swarm.
- **Overnight policy:** one wave at a time, grade by coverage, save state + journal after each, resume after session reset, write a morning report. Stop only for destructive/credential/storage/irreversible risk.

---

## 8. SKILL + CAPABILITY MANAGEMENT (lifecycle)

- **Create:** a skill is born when a workflow/prompt/checklist/gate repeats >=2x or proves itself (e.g., `os-token-safe-reader`). New skill = `.claude/skills/<name>/SKILL.md` with name + description + trigger + inputs + outputs + the rule it enforces.
- **Test before official:** run it on 2-3 real cases; it is `candidate` until it passes; then it is official.
- **Deprecate without deleting:** outdated skills get a `DEPRECATED` header + a pointer to the replacement; never removed (optionality + recovery).
- **Selection:** the router picks the skill via the tool-routing map + the capability SKILLS backlog.
- **Every project improves the OS:** capability harvest is MANDATORY after any major build (extract new skills/connectors/gates/routing/decision/doctrine upgrades into the capability map). The capability-growth mandate (memory) enforces this.
- **Stay generic:** decision/routing/strategy skills stay lane-neutral to protect optionality , never hard-coded to one business identity.

---

## 9. QUALITY GATES (built as definitions; see `os-quality-gates` skill)

Each gate: what it checks · pass/fail · where it fires.
1. **Anti-hallucination** , every factual/strategic claim cites a verified source or is labeled inference; uncited claims fail. Fires in Research/Critique/Strategy.
2. **Anti-old-lane anchoring** , old offer/lane names tagged `[old/evidence-only]`; an answer that grants an old doc authority fails. Fires in Strategy.
3. **Optionality protection** , answer keeps lanes/identity open unless explicit proof + operator decision; collapsing optionality fails. Fires in Strategy/Decision.
4. **Proof-before-crowning** , no lane/identity crowned without current proof; "the answer is X" without proof fails. Fires in Strategy.
5. **Legal/ethical risk** , scans for employer data/relationships/likeness/IP/ToS exposure; flags and may refuse/redirect. Fires on every build/output.
6. **Employer-conflict** , anything employer-adjacent, identity-exposing, on company time/tools/data fails. Fires on every off-grid build.
7. **Output-usefulness** , does it advance state / can the operator act on it; vague output fails. Fires on every deliverable.
8. **Completion-verification** , manifest/coverage proves done; a "done" claim without proof fails. Fires on every "done."
9. **Source-freshness** , market/factual claims dated + current; stale-as-current fails. Fires in Research/Strategy.
10. **Cost/runaway** , run sized to budget + session; unbounded swarm/concurrent waves fail. Fires before any workflow.
11. **Identity-collapse** , Bryce stays the operator/possibility engine; reducing him to one output fails. Fires in Strategy/Writing.

---

## 10. MEMORY / DOCTRINE / RETRIEVAL RULES

- **Into memory:** durable operating rules (feedback), who the operator is (user), ongoing constraints not in code (project), external pointers (reference). One fact per file + `MEMORY.md` index line.
- **Never into memory:** anything the repo/manifest already records; one-conversation ephemera; raw source text; secrets/credentials; unverified strategy.
- **Stays in doctrine:** distilled, verified, reusable intelligence (the OS_DOCTRINE/CAPABILITY/MASTER docs).
- **Stays in raw sources:** the corpus , evidence, retrieved on-demand only.
- **Auto-retrieved:** `MEMORY.md` (always), the active-domain spine row, CURRENT_STATE.
- **On-relevance only:** specific doctrine docs, raw sources, capability dimensions , grep/Read when the task needs them; never preload the whole OS.
- **Citation:** every recommendation names the doctrine/skill/gate it used; any unverified-pile dependency is disclosed.
- **Old informs, current decides:** doctrine is weighed as evidence; current proof + today's instruction win on any conflict.

---

## 11. DASHBOARDS (schema)

Each dashboard = a derived `.md` (never source), reconciled from the manifest/journal at every checkpoint:
- **OS Health** , verified %, pending pile, consistency-check result, last-checkpoint date, open contradictions count.
- **Source Engagement** (`OS_ENGAGEMENT_DASHBOARD.md`) , status taxonomy counts (existing).
- **Skill** , skills official/candidate/deprecated, last-used, leverage rank.
- **Cost** , $ total + by model, session/week %, last-run cost, est-vs-actual.
- **Project** , active models/builds, stage, next action, kill/keep/scale signal.
- **Proof-loop** , live loops, 24h/7d status, metric, verdict.
- **Error / Quarantine** , needs_ocr / visual / transcription / conversion_failed / poisoned-run log.
- **Capability Growth** , skills created/queued, connectors, gates, doctrine promoted, optionality preserved (existing).
- **Autonomy / Overnight** , last overnight run, waves completed, failures, morning-report link.

---

## 12. IN-HOUSE FOREVER PLAN

- **Now (Mac):** Claude Code is the brain; `00_COMMAND_CENTER` is the body; workflows are the hands.
- **Move to local scripts:** deterministic mechanics , conversion (`convert_wave.sh`), `token_segment.py`, manifest reconciliation, consistency checks, dashboard rebuilds. (No model tokens needed.)
- **Stay inside Claude:** judgment , synthesis, critique, strategy, writing, design, routing.
- **Mirror to Obsidian:** read-only mirror of doctrine + dashboards + THE_SPINE for human browsing/handoff.
- **Automate (cron/launchd):** nightly git backup, manifest consistency check, dashboard rebuild, cost snapshot, `.prev` cleanup.
- **Cloud backup:** private git remote for OS text; cold cloud copy for raw corpus.
- **CLI tool later:** wrap the common ops (`os read <file>`, `os status`, `os checkpoint`, `os harvest`, `os backup`) into a local `os` command.
- **Private app/interface eventually:** a local dashboard UI over the manifest/journal/skills once the text machine is stable.

---

## 13. FIRST APPLICATION: THE ONE-PERSON CAMPAIGN HOUSE

Full pipeline in `OS_CAMPAIGN_HOUSE_PIPELINE.md`. It is the first LIVE TEST of the optimized OS operating correctly, NOT a business decision. Stages: idea intake -> world premise -> style-ref system -> character-ref (CRS) system -> product/ref system -> prompt generation -> image gen -> motion gen -> edit/finish -> caption -> post -> proof tracking -> kill/keep/scale -> reusable-skill extraction. Automated vs manual split defined there (taste stays manual at the gates).

---

## OUTPUTS INDEX (this build)
- This architecture (sections 1-13).
- `os-command-router` skill (Section 4).
- `os-quality-gates` skill (Section 9).
- `os-token-safe-reader` skill (already built; the reliability core).
- `OS_CAMPAIGN_HOUSE_PIPELINE.md` (Section 13).
- Session start/end + backup + recovery + cost protocols (Sections 2, 6, 7).
- Dashboard schema (Section 11).
- Skill backlog (ranked) + first-10-builds + first-build , below.

## SKILL BACKLOG, RANKED BY LEVERAGE
1. `os-command-router` , routes every request (built now). 2. `os-quality-gates` , the 11 gates (built now). 3. `os-token-safe-reader` , reliability core (built). 4. `os-checkpoint` , one command: reconcile manifest -> rebuild dashboards -> journal -> consistency check. 5. `os-capability-harvest` , mandatory post-build harvest. 6. `os-campaign-house` , the production pipeline runner. 7. `os-session-start` / `os-session-end` , the state protocols. 8. `os-backup` , git + cloud + .prev. 9. `os-cost-guard` , pre-run budget/session check. 10. `os-recovery` , bad-run repair.

## FIRST 10 BUILDS, IN ORDER
1. `os-command-router` skill. 2. `os-quality-gates` skill. 3. `OS_CAMPAIGN_HOUSE_PIPELINE.md`. 4. `os-checkpoint` (local script + skill). 5. Folder/git hygiene (`.gitignore`, init, first commit of OS text). 6. Session start/end skills. 7. Dashboard rebuild script (manifest -> all dashboards). 8. `os-backup` (cron nightly). 9. `os-capability-harvest` skill (mandatory post-build). 10. Run the campaign-house pipeline once end-to-end (the live test).

## WHAT TO EXECUTE IMMEDIATELY (24h)
Build #1 (`os-command-router`) + #2 (`os-quality-gates`) + #3 (campaign-house pipeline doc) , the brain that routes + the gates that keep it honest + the first application to point them at. Then a single end-to-end dry run of the campaign house on one made-up brief to prove the machine routes, gates, produces, and self-checks.

## WHAT GETS AUTOMATED vs STAYS MANUAL
- **Automated:** conversion, segmentation, manifest reconciliation, dashboard rebuilds, backups, consistency checks, cost snapshots, routing receipts, coverage grading, prompt scaffolding.
- **Manual (taste still matters):** the world premise, character design approval, the reject/beat-source gates on every frame, final cut selection, voice on copy, kill/keep/scale judgment, any strategy/identity decision. The OS does the mechanics; the operator owns the taste and the throne (which stays empty until proof).
