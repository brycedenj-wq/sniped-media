# THE CLAUDE OPERATING MANUAL (2026-06-04)

> How Claude should run inside Bryce's OS. Grounded in the verified corpus (full source digest: `OS_CLAUDE_DOCTRINE_DIGEST.md`) plus the hard lessons of the OS engagement run. This is the practical manual the `os-command-router` and the operating modes execute against.

## 0. THE GOVERNING LAW
**Context architecture beats prompt tuning (the 95/5 rule).** 95% of leverage is the workspace (CLAUDE.md, skills, folder structure, doctrine on disk, the right files loaded); only ~5% is prompt wording. So the manual optimizes the SYSTEM, not the sentence. Corollary: avoid chatbot mode , long message history dilutes instructions ~26% and causes drift. Minimal history + maximum upfront context + state on disk = maximum clarity.

## 1. PROMPTING PATTERNS (use these, in order of leverage)
- **TCREI** , Task, Constraint, Role, Example, Intent. Minimum frame for any generative output. Examples (few-shot) are the single most effective technique; concrete instantiation beats abstract description.
- **Stage / Task / Rules** , the 3-part structure for any skill or instruction block.
- **Constraint-first** , "keep X identical, change Y" beats open-ended generation. Specificity over creativity in edit instructions.
- **6-part visual prompt** (for image/composite) , Subject + Action + Environment + Art Style + Lighting + Camera Specs. Technical vocabulary carries ~80% of photorealism.
- **Reference density as entropy control** , 3-14 reference images + annotation beats prompt-gambling. More references = less hallucination. (CRS for characters, image-order convention: 1=base, 2=identity, 3+=refs.)
- **Empty-prompt-first gate** , for context-aware tools (Generative Fill), start empty; 6-attempt cap before manual escalation.
- **Metaprompting** , use Claude to expand a 3-word intent into a 100-word production-ready prompt (the "creative director layer"); JSON-prompt standardization turns prompt-craft into system engineering for batch runs.
- **promptimizer move** , before any generative task, diagnose the draft's core gap (vague goal / missing format / buried info) and REWRITE, do not patch.
- **Hook-first copy** , Hook (<=8 words) + Context (3-5 lines) + Deployment + CTA. No em-dashes, no AI-tell transitions.

## 2. AGENT / WORKFLOW ORCHESTRATION
- **Single agent first.** Sub-agents only if a single agent fails. **Complexity budget: 2 (single) / 6 (sub-agents, hub-and-spoke) / 8+ (agent teams).** Over-engineering = token waste = quality failure.
- **Do NOT spawn a sub-agent just to gather context and return it** , that breaks reasoning coherence; keep context-dependent work in-session.
- **Parallel bulk work** , sub-agents/workflows for N independent tasks; batch sweet spot ~100-200 items; beyond that, deterministic tooling. Context stays clean (pass summaries, not raw).
- **Skills = persistent markdown workflows** (trigger + inputs + output spec + numbered steps), not inline prompts. Wrap any process at 7+ steps. **Built manually 3x = capture as a skill.** Commands chain skills one-line.
- **Dispatch leverage test** , anything definable as a skill/command should be dispatched (run while the operator is away), not done synchronously. "Can this run while I'm on set/in transit?" If yes, queue it.
- **Two-stage reduce for big synthesis** , chunk-digest (cheap) then merge (strong); never feed one agent >~200k tokens (the 1M-context gate).
- **Worktrees for parallel mutation** , isolate agents that write files in parallel.

## 3. TOOL-ROUTING / MCP (the connected-toolchain default)
**11-step toolchain audit BEFORE any manual execution is authorized:** Claude Code skills > MCP tools > Zapier/n8n > Instantly/Super Search > sub-agents > community skills > scripts/cron > browser-assisted > Vercel serverless > existing connectors > manual (last resort). Tool-first routing; manual only after the audit returns no path. Full routing table: `OS_CAPABILITY_TOOL_ROUTING.md`. Live connectors: Adobe, Figma, Airtable, Gmail, Drive/Calendar (temp bridge), Higgsfield, Notion (queued), Stripe (gated). Per-batch approval on credit-spend tools; no global "always allow."

## 4. MODEL SELECTION + COST
- **haiku** , cheap whole-reads, segment reads, bulk extraction, classification.
- **sonnet** , synthesis, consolidation, critique, design judgment (most weekly headroom , use it for quality).
- **opus (main loop)** , high-judgment reasoning, strategy, final framing. Per-token expensive , keep turns LEAN.
- Check `/usage` before and after major runs. Size waves to the session window; one wave at a time (never concurrent). Stop-and-ask on large spend, < 25GB disk, or a real risk.

## 5. CONTEXT / TOKEN DISCIPLINE (reliability core)
- **Read cap = ~25,000 tokens/call; it ERRORS, not truncates.** Never segment by raw words/lines. Re-wrap to ~180-char lines, segment by CHAR count (<=40k chars approx 10k tokens). (`os-token-safe-reader`.)
- **Coverage proven, not assumed** , `read_verified` only when every token-safe segment lands (got==total, fail==0).
- **Minimal history** , don't carry a bloated thread; put state on disk, load only what the task needs (the active-domain spine row, not the whole OS).

## 6. EVALUATION / CRITIQUE
- **Adversarial by default in Critique mode** , verify each claim, default to skeptical; majority-refute kills a finding.
- **Gate before done** , run the mode's exit gates (`os-quality-gates`); a "done" without the completion-verification gate is a false claim.
- **No rubber-stamp** , agreement is not a review.

## 7. RELIABILITY / RECOVERY
- Log every partial read / failed conversion / OCR gap / tool error to its status + the error dashboard. Nothing silently dropped or silently "done."
- Bad run: stop -> read manifest/journal for what actually landed -> re-grade by coverage -> re-fire only failed/poisoned segments (cache-bust labels) -> reconcile dashboards from the manifest.
- Session-limit mid-run: grade what landed, save state, resume after reset; cache-bust the poisoned step.

## 8. OPTIMIZATION (operator maturity ladder)
Task maturity: one-off request -> folder-based multi-session -> project with memory -> skill-wrapped workflow -> scheduled/dispatched skill. Push every recurring task UP the ladder. Plugin-worthiness gate (build only if 2 of 3: repeats weekly+, multi-step, client/brand-sensitive). 9-phase operator rollout: Chat -> Projects -> Claude Code -> Skills/Commands -> Sub-agents -> MCP -> Cowork/Dispatch -> Teams -> Workspace-as-Asset. Capability harvest is MANDATORY after every major build (extract new skills/connectors/gates/routing into the capability map).

## 9. HOW THIS MANUAL IS USED
The `os-command-router` reads this to pick the mode + tools + cost tier; the operating modes (architecture Section 3) execute against it; `os-quality-gates` enforces it at completion. It is doctrine, not law , today's proof + the operator's instruction always win. Full corpus evidence: `OS_CLAUDE_DOCTRINE_DIGEST.md`.
