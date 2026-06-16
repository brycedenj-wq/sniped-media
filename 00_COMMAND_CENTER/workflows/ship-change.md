# Workflow: Ship a code change

End-to-end loop for any feature or fix.

1. **Orient** — read `00_COMMAND_CENTER/NEXT_ACTION.md`; pick the top item.
2. **Branch** — confirm you're on the assigned feature branch (not `main`).
3. **Build** — make the change.
   - Next.js code? Read the relevant guide in `node_modules/next/dist/docs/` first.
4. **Typecheck + lint** — `npx tsc --noEmit` and `npm run lint`. Fix new issues
   (ignore pre-existing ones noted in NEXT_ACTION.md).
5. **Run it** — `/run` (or `/verify` for a fix) to see it work for real.
   Remotion change? `npm run video:preview` or visit `/studio`.
6. **Self-review** — `/code-review`, then `/simplify` for cleanups.
7. **Security** — `/security-review` if the change touches forms, env, auth,
   uploads, or external input.
8. **Commit + push** to the feature branch. No PR unless asked.
9. **Close out** — move the item to "Recently done" in NEXT_ACTION.md.
