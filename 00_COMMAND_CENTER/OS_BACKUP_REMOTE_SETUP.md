# Off-machine backup , remote setup (run these yourself; nothing is pushed until you do)

The backup script (`scripts/os_backup.sh`) already supports `status | dry-run | commit | push` with a
private remote named `osbackup`. It only ever pushes OS-TEXT (books/media/raw/giant files excluded).

## Exact commands (you run these once)
1. Create a PRIVATE repo on your host (GitHub/GitLab/Gitea). Keep it private (the OS has strategy + memory).
2. Add it as the `osbackup` remote:
   `cd /Users/sniper/AI-Brain-Refinery`
   `git remote add osbackup git@github.com:<you>/<private-os-backup>.git`   (SSH preferred)
3. Verify:
   `./00_COMMAND_CENTER/scripts/os_backup.sh status`   (should show the remote URL + ahead/behind)
4. Dry-run FIRST (no push, shows what would commit):
   `./00_COMMAND_CENTER/scripts/os_backup.sh dry-run`
5. Then push safe OS-text only:
   `./00_COMMAND_CENTER/scripts/os_backup.sh push`

## Safety already enforced
- `.gitignore` excludes *.epub/pdf/mobi/azw3/djvu/mp4/jpg/zip + raw/ + the heavy media sandboxes.
- `os_backup.sh` aborts if any staged file > 25MB and never uses `git add -A`.
- Nightly launchd job `com.bryce.osbackup` commits locally at 02:30; add `push` to it after the remote is verified.

Until you run step 2, backups are LOCAL ONLY (by your instruction). No data leaves the machine.
