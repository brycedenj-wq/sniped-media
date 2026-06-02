# COMMAND_CENTER_SURVIVAL_AND_RECOVERY

**Date:** 2026-05-27
**Status:** Durability, backup, and recovery layer for the OS. Anchor-class: markdown-only, not chunked, not a chunk source, not in the master files. This makes the Command Center survivable if Claude/ChatGPT disappears, a chat is lost, a file is deleted, the Mac fails, or BJ returns months later.
**Headline:** the irreplaceable layer is about 10 MB. The 9 GB repo is almost all replaceable (4.5 GB of copyrighted books in raw/ + a 4.3 GB git history bloated by committing them). Survival is therefore easy: protect the 10 MB off-machine.

---

## 1. What persists if AI tools disappear
Everything committed to git. Claude and ChatGPT are editors, not the system. The OS is files on disk. The 250-commit history holds: the 99 Command Center docs, the 10 skills (`.claude/skills/`), the corpus (1,837 chunks), the MASTER files, the site, and the raw source docs. If both AIs vanished, none of these files change. The git history, not any chat, is the source of truth.

## 2. What is vulnerable
1. **No remote, no off-machine copy (the single point of failure).** All of it lives only on this Mac. Drive failure, theft, loss, or an OS wipe = total loss. Git history is worthless if the disk dies.
2. **Memory lives outside the repo and is gitignored.** 43 files (268 KB) at `~/.claude/projects/-Users-sniper/memory/`, including the work-style memories, are not in git and not in the repo tree. A Claude reset/reinstall/profile-clear loses them, unrecoverable from git. (Snapshot handling: section 9.)
2b. **Uncommitted files** are lost if deleted before commit.
3. **No zip snapshot, no dated release, no checksum manifest.**
4. **The 9 GB bloat blocks the easy remote** (file-size and repo-size limits; slow push).
5. **Copyright + sensitivity:** raw/ holds 305 copyrighted books; committed docs reference the employer and private strategy. Any remote must be private.

## 3. Essential-file manifest
- `00_COMMAND_CENTER/` (about 4.3 MB, 99 docs) :: irreplaceable
- `.claude/skills/` (10 skills) :: irreplaceable, in repo
- `CLAUDE.md`, `AGENTS.md` :: irreplaceable
- Memory dir + `MEMORY.md` (268 KB, 43 files) :: irreplaceable, OUTSIDE repo, gitignored (section 9)
- `01_KNOWLEDGE_BASE/MASTER_INDEX.md`, `MASTER_CHUNK_MAP.json`, `ACTIVE_KNOWLEDGE_STATE.md` :: irreplaceable
- Corpus chunk jsonl (`01_KNOWLEDGE_BASE/batches/*_CHUNKS.jsonl`, about 2.8 MB, 57 files) :: irreplaceable
- `baseplate_site/` (about 1.1 MB) :: irreplaceable
- Source audits / coverage ledger (in `00_COMMAND_CENTER/`) :: irreplaceable
- `raw/` (4.5 GB, 777 files, 305 books) :: replaceable (re-downloadable), copyright-encumbered, immutable intake
- Bible: `SPIRITUAL_FOUNDATION` held, never chunked (exclusion intact)

## 4. Precious layer definition
The irreplaceable subset is small: `00_COMMAND_CENTER/` + `.claude/skills/` + the memory dir + `MASTER_INDEX` + `MASTER_CHUNK_MAP` + `ACTIVE_KNOWLEDGE_STATE` + the chunk jsonl + `baseplate_site/` + `CLAUDE.md`/`AGENTS.md`. **Combined: about 10 MB.** That is the entire ballgame and it fits on anything. Everything else in the 9 GB is replaceable book binaries or git history bloat.

## 5. Backup strategy
1. **Off-machine copy of the precious layer, today (about 10 MB, 2 minutes).** Zip the precious layer (section 4) and put it on a private cloud (iCloud/Drive/Dropbox) AND a USB stick. This single act removes the catastrophic risk.
2. **Commit discipline** (already strong: 250 gated commits). Keep committing approved work; commit stragglers before closing a major session.
3. **Local zip snapshot:** dated `BASEPLATE_OS_SNAPSHOT_YYYY-MM-DD.zip` of the precious layer (include the live memory dir in the zip, since git does not protect it).
4. **Private cloud copy + external drive/USB copy:** keep the latest snapshot in at least two places.
5. **Private remote ONLY if used:** a PRIVATE GitHub/GitLab repo for the precious layer only. Do not push the 9 GB / 4.3 GB-history repo; use a fresh clean repo or a filtered export of the precious layer. Private only, never public.
6. **Raw book library (4.5 GB) backed up separately:** to an external drive or private cloud. It is replaceable and copyright-encumbered, so it does not belong on a code remote.
7. **Dated release snapshots:** monthly, following 3-2-1 (3 copies, 2 media types, 1 offsite).
8. **Checksum manifest:** a SHA-256 list of the essential files to verify integrity after any restore.

## 6. Recovery procedure
- **Restore from git:** `git clone` or `git checkout -- <path>` restores committed files. `git reflog` + `git fsck --lost-found` recover deleted commits.
- **Restore from zip:** unzip the latest dated snapshot into place.
- **Restore memory:** copy the memory files from the off-machine zip back to `~/.claude/projects/-Users-sniper/memory/`. (The in-repo `MEMORY_SNAPSHOT/` holds the manifest of what should exist; the content comes from the zip.)
- **Rebuild corpus from raw (if chunks lost but raw/ survives):** re-run the staging/batch skills to regenerate the chunks.
- **Verify total_chunks / master files:** the 3-way reconcile must equal 1,837: header `total_chunks` == sum of `batches[].chunk_count` == sum of jsonl line counts. Confirm every `source_file` resolves.

## 7. Daily-use protocol
Open `CURRENT_STATE.md` first to check `PROOF_LOOPS_30_60_90.md` to operate via `COMMAND_CENTER_RESPONSE_PROTOCOL.md` to invoke skills as needed (`/challenge`, `/save`, `/boardroom`, `/operator-review`) to commit useful changes. At the end of a major session: run `/session-save` and drop a dated snapshot. No dependence on any single chat.

## 8. Future-upgrade protocol
New resource: drop in `raw/` intake to run the coverage audit against the corpus to decide activation (chunk / summarize / skill-activate / park) to update the skill or playbook to commit to snapshot. New AI tool/model: it is just a new editor. Point it at `CURRENT_STATE.md` + the evergreen core (`EVERGREEN_CORE_INDEX.md`), or paste `project_sniped_spine_portable.md`, and it picks up the OS.

## 9. Memory snapshot rule
The live memory lives at `~/.claude/projects/-Users-sniper/memory/` and is gitignored, so git does not protect it. **Because at least one memory file references the employer, raw memory content is NOT committed to the repo.** Instead:
- The in-repo `00_COMMAND_CENTER/MEMORY_SNAPSHOT/` holds a MANIFEST only (filenames + restore instructions), never the raw content.
- The actual memory CONTENT is backed up off-machine inside the dated zip snapshot (section 5), which is private and not on any code remote.
- Never edit the live memory dir from the snapshot; restore FROM the zip if the live dir is lost.
- Refresh the manifest whenever memory files are added or removed.

## 10. What NOT to do
- No public GitHub/GitLab repo, ever.
- No raw copyrighted books in any public repo.
- No exposing private strategy or employer references externally (keep them in the private local repo + private off-machine backup only).
- Do not rely on chat history as the source of truth. The committed files are the truth; chats are disposable.

---

## Guardrails (unchanged)
Durability layer only, no strategy change. Private backups only, never public. Raw books and the Bible stay as they are (immutable intake; Bible held). No master/raw/Bible/site/chunking changes from this doc. total_chunks unchanged at 1,837. Anchor-class: not chunked, not in the master files.
