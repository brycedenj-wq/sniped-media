# NEXT ACTION

> Single source of truth for "what to do next" in sniped-media.
> Keep the top item actionable. Update at the start/end of each session.

## ▶ Current focus

- [ ] Decide the next concrete deliverable for the Remotion integration
      (e.g. a vertical 1080×1920 captioned template, or a real campaign clip).

## Recently done

- [x] 2026-06-14 — Integrated Remotion into the Next.js app (`video/`,
      `remotion.config.ts`, `/studio` Player page, `video:preview` / `video:render`).
- [x] 2026-06-14 — Created Command Center (`00_COMMAND_CENTER/`) + skill registry.

## Backlog (unordered)

- [ ] Add a vertical short-form Remotion template with captions.
- [ ] Wire `remotion render` in CI / an env that allows `remotion.media` egress.
- [ ] Resolve pre-existing lint errors: `app/moodboard/_components/SectionFade.tsx`
      (set-state-in-effect ×?) and `app/work/page.tsx` (unused `Container`).
- [ ] Consider a SessionStart hook so web sessions auto-run lint/typecheck
      (see `/session-start-hook`).

## How to use this file

1. Open with `00_COMMAND_CENTER/NEXT_ACTION.md`.
2. Work the top unchecked item under **Current focus**.
3. Move finished items to **Recently done** with a date.
4. See `SKILL_REGISTRY.md` for which skill/workflow to apply.
