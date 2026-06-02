# RESTART_RECOVERY_STATE · 2026-05-28

**Captured:** 2026-05-28T16:16:14Z (Thu May 28 09:16:14 PDT 2026)
**Repo:** /Users/sniper/AI-Brain-Refinery
**Branch:** main (no remote, local-only)
**total_chunks:** 1837 (unchanged)

**WHY THIS FILE EXISTS:** BJ's macOS terminal froze mid-session while preparing to install the Higgsfield MCP via `claude mcp add`. He may need to restart. This file captures the exact state so a fresh Claude Code session can pick up perfectly.

---

## How to resume in a fresh Claude Code session

Paste this exact instruction into the fresh session:

> Read `00_COMMAND_CENTER/RESTART_RECOVERY_STATE_2026-05-28.md` first, then run `git status` and wait.

Do NOT let the fresh session reset, clean, delete, stash, or commit anything until BJ reviews. Everything below is intact uncommitted work.

---

## Git state (captured at 2026-05-28T16:16:14Z)

```
git status --short
 M 00_COMMAND_CENTER/COMMAND_CENTER_RESPONSE_PROTOCOL.md
?? 00_COMMAND_CENTER/BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md
?? 00_COMMAND_CENTER/FULL_DOWNLOADS_AND_OS_COVERAGE_LEDGER.md
?? 00_COMMAND_CENTER/TOOLCHAIN_ACTIVATION.md
?? 00_COMMAND_CENTER/concept_film_v1/
?? 00_COMMAND_CENTER/sample_dossier_v1/

git diff --stat
 .../COMMAND_CENTER_RESPONSE_PROTOCOL.md            | 39 +++++++++++++++++-----
 1 file changed, 31 insertions(+), 8 deletions(-)
```

### Last 15 commits

```
15f17f7 relock BASEPLATE domain to baseplateworks
51056ac add SNIPED cash now activation system
4ad5332 add Direction Stack private method brief
338c1c9 add SNIPED full thesis
9c304af add SNIPED camera lane architecture
44491b4 add proof log operating SOP
847b7c2 add sample dossier build playbook
8262290 add proposal invoice playbook
9ac57bd add discovery qualification playbook
7b4f37f add outbound persuasion canon
beb1330 add Command Center survival layer
7f99235 add outbound and admin operating system
4e2a37f add internal tightness build sequence
ab60ddb add operator-review skill
b60aeef add current state continuity checkpoint
```

---

## MCP status (captured live, 2026-05-28T16:16Z)

```
claude.ai Airtable                  ✓ Connected      https://mcp.airtable.com/mcp
claude.ai Adobe for creativity      ✓ Connected      https://adobe-creativity.adobe.io/mcp
claude.ai Google Drive              ! Needs auth     https://drivemcp.googleapis.com/mcp/v1
claude.ai Google Calendar           ! Needs auth     https://calendarmcp.googleapis.com/mcp/v1
claude.ai Gmail                     ✓ Connected      https://gmailmcp.googleapis.com/mcp/v1
plugin:figma:figma                  ✓ Connected      https://mcp.figma.com/mcp (used tonight, proven)
figma-desktop                       ✗ Failed         http://127.0.0.1:3845/mcp (local bridge, separate from plugin)
higgsfield                          NOT INSTALLED YET
```

**Higgsfield install was about to happen when the terminal froze.** This is the next action after restart.

---

## All uncommitted files · status, content, safety

### Tracked, modified

| Path | Status | Contains | Safe to keep? | Commit plan |
|---|---|---|---|---|
| `00_COMMAND_CENTER/COMMAND_CENTER_RESPONSE_PROTOCOL.md` | M | Pass B amendment: new §7 (mandatory tool-layer check) + renumbered §8-§13 + added stop condition + appendix mentions TOOLCHAIN_ACTIVATION. 31 inserts / 8 deletes vs committed. | YES, intentional Pass B work, em-dash clean. | HOLD for explicit BJ approval. Stale baseplate.systems references in §11 are out-of-scope drift that should be cleaned in a follow-up pass before commit. |

### Untracked, new

| Path | Status | Contains | Safe to keep? | Commit plan |
|---|---|---|---|---|
| `00_COMMAND_CENTER/TOOLCHAIN_ACTIVATION.md` | ?? | Pass A doctrine doc (322 lines, 20.7 KB). Single canonical tool-layer reference. Tracks Figma (active/proven), Higgsfield (CANDIDATE), Adobe Creativity, Gmail, Stripe queued, Notion queued, etc. + 11-item audit checklist + routing logic. | YES, intentional, em-dash 0. | HOLD for explicit BJ approval. Will be updated post-Higgsfield-install to swap to BJ's sharper 7-step toolchain check and promote Higgsfield to ACTIVE. |
| `00_COMMAND_CENTER/BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md` | ?? | v2 upgrade of the concept film doc (94 lines, 11.6 KB). 6 shots (was 7), literal industrial baseplate motif, named-operator credit on wordmark, locked operator styling, sound spec, 9:16 social cut spec, asset job declared. | YES, intentional Track B work, em-dash 0. The PRE-EXISTING v1 of this file was also untracked (never committed); v2 fully replaced v1 via Write. | HOLD for explicit BJ approval. Commit alongside concept_film_v1/ after first 3-still test validates the doc. |
| `00_COMMAND_CENTER/concept_film_v1/` | ?? (dir) | Contains `FIRST_TEST_PROMPT_PACKAGE.md` (157 lines, 10.1 KB). Paste-ready prompt package for Shots 1, 3, 6 stills test in Nano Banana Pro at 16:9, MASTER STYLE block, evaluation rubric, permission-gate note. | YES, intentional Track B work, em-dash 0. | HOLD for explicit BJ approval. |
| `00_COMMAND_CENTER/sample_dossier_v1/` | ?? (dir) | 6 files: `SAMPLE_CAPABILITY_DOSSIER_v1.md` (text source), `sample_dossier_v1.html` (styled render), `sample_dossier_v1.pdf` (8-page Chrome-headless render), `FIGMA_BUILD_SPEC.md`, `figma_cover.png`, `figma_content_row.png` (screenshots from the live Figma file). | YES, all from tonight's PhaseLine Talent Partners dossier build. The Figma file itself lives at `figma.com/design/p7qWs3AhjTHZa6vDZGoKGE`. | HOLD for explicit BJ approval. |
| `00_COMMAND_CENTER/FULL_DOWNLOADS_AND_OS_COVERAGE_LEDGER.md` | ?? | Pre-existing untouched (244.7 KB). NOT created or modified this session. | YES, leave alone. | OUT of any current commit plan. Separate decision later. |

### Not touched this session (explicit no-touch list)

- `01_KNOWLEDGE_BASE/` (master corpus) - unchanged, total_chunks still 1837
- `raw/` - unchanged
- Any SPIRITUAL_FOUNDATION / Bible file - unchanged
- `baseplate_site/` - unchanged
- `.git/` - only standard git operations from this session, no destructive ops

---

## What changed in this session (high level)

### Already committed earlier in this session

- `15f17f7 relock BASEPLATE domain to baseplateworks` · the domain re-lock from `baseplate.systems` to `baseplateworks.com` across `BASEPLATE_DOMAIN_AND_EMPIRE_ARCHITECTURE.md`, `CURRENT_STATE.md`, `EVERGREEN_CORE_INDEX.md`.
- All prior commits (sample dossier playbook, persuasion canon, SNIPED layer, Direction Stack brief, etc.) are pre-this-session.

### Uncommitted work produced this session

1. **PhaseLine Talent Partners sample dossier (v1)** built via the live Figma MCP. File key `p7qWs3AhjTHZa6vDZGoKGE`. Local sources + PDF render + screenshots in `sample_dossier_v1/`.
2. **TOOLCHAIN_ACTIVATION.md** (Pass A) · the new tool-layer doctrine. Tracks installed/queued/deferred MCPs and connectors. Includes Adobe split (creativity vs analytics) and the new Claude Directory skills (`/canvas-design`, `/web-artifacts-builder`, `/mcp-builder`, `/theme-factory`, `/skill-creator`).
3. **COMMAND_CENTER_RESPONSE_PROTOCOL.md** (Pass B amendment) · inserted new §7 mandatory tool-layer check with BJ's locked operating rule. Renumbered §7-§12 to §8-§13. Added tool-audit stop condition.
4. **BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md** v2 upgrade · 6 shots, literal baseplate motif, named-operator credit, sound spec.
5. **concept_film_v1/FIRST_TEST_PROMPT_PACKAGE.md** · runnable spec for the first 3-still Higgsfield test (Shots 1, 3, 6).

---

## What was completed

- Pass A (TOOLCHAIN_ACTIVATION.md write) · verified clean, holding for commit approval.
- Pass B (COMMAND_CENTER_RESPONSE_PROTOCOL.md amendment) · verified clean, holding for commit approval.
- Track B (concept film v2 + first-test prompt package) · verified clean, holding for commit approval.

## What was pending when the terminal froze

- **Track A · BJ installing the official Higgsfield MCP via `claude mcp add`.** Not started in the terminal. The install steps were queued but never executed.

---

## Higgsfield install · resume from here

BJ had committed to:

1. Open Higgsfield.
2. Go to the MCP / CLI tab.
3. Copy the connector URL.
4. Run in terminal:
   ```
   claude mcp add --transport http higgsfield <connector-url>
   ```
5. Complete OAuth in the browser.
6. Verify:
   ```
   claude mcp list
   ```
7. Confirm `higgsfield` appears with `✓ Connected`.

After "connected" is confirmed, the next Claude Code session should:

1. Run `claude mcp list` from a Bash call to confirm `higgsfield` is registered in the project's view (not just Claude Desktop).
2. Use `ToolSearch` to load the Higgsfield MCP tool schemas into the session (likely namespace `mcp__plugin_higgsfield_*` or similar; grep ToolSearch's response for the actual name).
3. If Higgsfield exposes a `whoami` or identity tool, call it (read-only, no credits) to confirm auth and workspace identity.
4. Surface to BJ: the loaded tool names, the auth target, the credit-cost estimate per generation if visible.
5. Ask explicitly: "Approve the first 3-still test as one batch unit?" Wait for yes. NO generations until BJ replies yes.
6. On approval, execute the first 3-still test using the prompts in `00_COMMAND_CENTER/concept_film_v1/FIRST_TEST_PROMPT_PACKAGE.md`.
7. Save outputs to `00_COMMAND_CENTER/concept_film_v1/outputs/` (BJ may need to create this dir if the MCP doesn't auto-create).
8. Run the 6-item evaluation rubric on each returned PNG.
9. Decide motion next batch based on the decision tree in the prompt package.

---

## Pickup checklist for the fresh session

After paste-and-read, the fresh Claude Code session should:

1. Read this file (`RESTART_RECOVERY_STATE_2026-05-28.md`) end to end.
2. Run `git status` and confirm output matches §Git state above. If it differs, STOP and flag the difference.
3. Run `claude mcp list` and confirm Higgsfield status (was NOT installed at capture time; may or may not be installed now).
4. Read `TOOLCHAIN_ACTIVATION.md` (the tool-layer doctrine).
5. Read the modified `COMMAND_CENTER_RESPONSE_PROTOCOL.md` (the §7 mandatory tool-layer check is locked).
6. Read `BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md` (v2 concept film spec) if the concept film work is the active job.
7. Read `concept_film_v1/FIRST_TEST_PROMPT_PACKAGE.md` if proceeding to the Higgsfield first test.
8. Ask BJ which task to pick up:
   - Higgsfield install (if not done) and first-test generation
   - Commit any/all of the held files (TOOLCHAIN_ACTIVATION, COMMAND_CENTER_RESPONSE_PROTOCOL amendment, BASEPLATE_CONCEPT_FILM_HIGGSFIELD v2, concept_film_v1/, sample_dossier_v1/)
   - Cleanup pass on the stale baseplate.systems references in COMMAND_CENTER_RESPONSE_PROTOCOL.md §11
   - Different priority

---

## Warnings (strict, follow these)

- **DO NOT** run `git reset`, `git stash`, `git clean`, `git checkout --`, or any destructive git operation without BJ's explicit per-command approval. Every uncommitted file in §All uncommitted files is intentional, valuable work.
- **DO NOT** commit anything until BJ explicitly approves which files to stage.
- **DO NOT** delete or modify `concept_film_v1/`, `sample_dossier_v1/`, `BASEPLATE_CONCEPT_FILM_HIGGSFIELD.md`, `TOOLCHAIN_ACTIVATION.md`, or the amendment to `COMMAND_CENTER_RESPONSE_PROTOCOL.md`.
- **DO NOT** install new MCPs in the fresh session beyond Higgsfield (which is the pending one). No tool spiral.
- **DO NOT** run Higgsfield generations without explicit batch approval. Permission gates ON.
- **DO NOT** auto-resume "the next thing" without confirming with BJ which thread to pick up.
- **DO NOT** touch `01_KNOWLEDGE_BASE/`, `raw/`, `baseplate_site/`, or any Bible / SPIRITUAL_FOUNDATION file.
- **DO NOT** rewrite `TOOLCHAIN_ACTIVATION.md` with a "new" version. The existing one is correct. Updates to that file should be targeted edits post-Higgsfield-install.

---

## Off-machine backup

A zip of the uncommitted recovery state was created at:

```
~/BASEPLATE_RESTART_RECOVERY_2026-05-28.zip
```

Contains: this recovery report + all the uncommitted files and directories listed in §All uncommitted files above. Excludes `.git/`, `raw/`, `01_KNOWLEDGE_BASE/`, `node_modules/`, Bible / SPIRITUAL_FOUNDATION.

If the local repo gets corrupted on restart, the zip is the recovery payload. Extract into a fresh `AI-Brain-Refinery/` and the uncommitted work survives.

---

## Memory and continuity

- The user memory system at `~/.claude/projects/-Users-sniper/memory/` is unchanged this session. All `feedback_*`, `project_*`, `intel_*`, `user_*` files are intact.
- The corpus at `01_KNOWLEDGE_BASE/` is unchanged. `MASTER_CHUNK_MAP.json` still reads `"total_chunks": 1837`.
- No master / raw / Bible mutations from this session.

End of recovery report.
