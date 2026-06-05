# OS LESSONS LEARNED , Overnight Sprint 001
1. Two environments are not one. claude.ai-app plugins (Twilio, Zapier, business skills) are NOT callable from this Claude Code CLI. "Installed" != "callable here". Always inventory the live session, never the screenshots.
2. Adobe MCP only accepts assets in its own trusted storage. External/cloud URLs (Higgsfield CDN) are rejected. Adobe-at-depth needs an upload handshake first.
3. World copy must flow from the world JSON, never be hard-coded in a layout function. A single hard-coded string (THE ESTATE OF HER) bled the wrong brand onto a new world.
4. Never reuse a function parameter name as a local variable. `money` (path) shadowed by `money` (text) crashed the engine. Lint for shadowing.
5. Generate cheap (1k) to gate, then 4K only the winners. Killing weak worlds at the JUDGING stage (never generating them) saved the most credits.
6. The gate that returns REJECT/FIX on an under-spec asset is the gate WORKING. A rubber-stamp gate is the real failure.
7. One moving pipeline beats a drawer of tools. os_engine (one intent -> full chain) is what makes the OS feel like an operating system, not a toolbox.
