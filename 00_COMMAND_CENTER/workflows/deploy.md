# Workflow: Deploy

1. **Gate** — `npx tsc --noEmit`, `npm run lint`, and `npm run build` all clean.
2. **Review** — `/code-review` (and `/security-review` if user-facing/sensitive).
3. **Deploy** — via **Vercel** MCP (`deploy_to_vercel`) or your Vercel pipeline.
4. **Verify** — check the deployment + runtime logs (`get_deployment`,
   `get_runtime_logs`); open the preview URL and smoke-test key pages
   (`/`, `/studio`, forms).
5. **Record** — note the deploy URL in `00_COMMAND_CENTER/NEXT_ACTION.md`.

> Don't deploy to production without explicit confirmation.
