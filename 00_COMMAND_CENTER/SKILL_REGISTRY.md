# SKILL REGISTRY — sniped-media

> Living index of the Claude Code skills, workflows, and MCP integrations
> available to this project. Generated 2026-06-14. Update as the toolset changes.
>
> Invoke a skill by typing `/<name>` or asking Claude to run it. MCP tools are
> called by Claude automatically when a request matches.

## Project at a glance

- **Stack:** Next.js 16 (App Router) + React 19 + Tailwind v4 + TypeScript
- **Media engine:** Remotion 4 (`video/`, `remotion.config.ts`, `video:preview` / `video:render` scripts)
- **Domain:** media / creative campaign site ("sniped-media")

---

## ⭐ Highest-leverage skills for this project

| Skill | What it does | When to reach for it |
|-------|--------------|----------------------|
| `/run` | Launches and drives the app to see a change working | After any UI/page/Remotion change — confirm it renders for real |
| `/verify` | Runs the app and observes behavior to confirm a fix | Validating a bug fix or feature before pushing |
| `/code-review` | Reviews the current diff for bugs + cleanups | Before every commit/PR |
| `/security-review` | Security review of pending branch changes | Before shipping anything touching forms, auth, env, uploads |
| `/simplify` | Applies reuse/simplification/efficiency cleanups to the diff | After a feature lands, before review |
| `/review` | Reviews a pull request | When a PR is open |

## Supporting skills

| Skill | Purpose |
|-------|---------|
| `/init` | (Re)generate CLAUDE.md codebase docs |
| `/update-config` | Edit settings.json — permissions, env vars, hooks ("whenever X do Y") |
| `/session-start-hook` | Set up a SessionStart hook so web sessions can run tests/linters |
| `/fewer-permission-prompts` | Build an allowlist of safe read-only calls to cut prompts |
| `/keybindings-help` | Customize keyboard shortcuts |
| `/loop` | Run a prompt/command on a recurring interval (polling, babysitting) |
| `/deep-research` | Multi-source, fact-checked research report |
| `/claude-api` | Reference for the Claude API / Anthropic SDK |

---

## MCP integrations (connect on session start)

Highest-leverage for a media/creative + Next.js project:

| Server | Leverage here |
|--------|---------------|
| **Vercel** | Deploy previews, inspect deployments/logs, domain checks for the Next.js app |
| **Higgsfield** | Generate image / video / audio assets; virality prediction for clips |
| **Adobe (Firefly)** | Image edits, background removal, vectorize, video quick-cut/resize |
| **Figma** | Design → code and code → design; design-system sync |
| **github** | PRs, issues, CI status, reviews (scoped to brycedenj-wq/sniped-media) |
| **Notion / Airtable** | Campaign/asset tracking, content calendars |
| **Google Drive / Gmail / Calendar** | Asset intake, client comms, scheduling |
| **Semrush** | SEO / competitive research for the marketing site |

> MCP availability depends on the session. If a server shows as disconnected,
> the matching capability is temporarily unavailable.

---

## Conventions

- Read `node_modules/next/dist/docs/` before writing Next.js code (per AGENTS.md —
  this Next.js has breaking changes vs. training data).
- Develop on the assigned feature branch; commit + push there. No PRs unless asked.
- Remotion render output goes to `out/` (gitignored). Headless render needs
  `remotion.media` egress (or a system Chrome) — blocked in some sandboxes.
