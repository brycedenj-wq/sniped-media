# OS SOURCE MAP

The OS knows the whole machine without crawling it. AI-Brain-Refinery is the command center; everything else is mapped, prioritized, and routed. Built 2026-06-07 from a read-only scan. Source of truth: `EXTERNAL_SOURCE_REGISTRY.csv`; rules: `OS_SOURCE_PRIORITY_RULES.md`; router: `scripts/os_source_router.py`.

## The folders that exist (verified read-only)
| Folder | Role | Freshness | What it is for |
| --- | --- | --- | --- |
| `/Users/sniper/AI-Brain-Refinery` | command_center | current | execution root + all gates/libraries/current-state truth |
| `…/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001` | active_project | active | Alma Love edits/selects/exports |
| `~/Downloads/    SNIPED_OS` (4 leading spaces) | legacy_os / source_library | legacy | deep doctrine, history, books, prompts, frameworks, creative systems |
| `~/Documents/BJ-WIKI` | books_frameworks / second brain | active | long-term memory + synthesis (10 domains) |
| `~/sniped-media` | active_project (web) | legacy | the site/web project (Apr) |
| `~/Pictures` (+ `~/Pictures/Lightroom`) | media_assets | active | photo raws (CR3/xmp) + Lightroom catalog for the photo workflow |
| `~/Documents/Photography` | media_assets | unknown | photo reference/archive |
| `~/ClaudeBusiness` | client_files | unknown | business/admin/client records |
| `~/Downloads`, `~/Desktop` | archive/intake | unknown | staging only; new material lands here |

## Not found at the named paths (so not claimed as wired)
`/Users/sniper/SNIPED_OS` (it lives in `~/Downloads/    SNIPED_OS`), `/Users/sniper/Sniped Media Business Files`, `/Users/sniper/Lightroom_Master_Catalog` (the real catalog is `~/Pictures/Lightroom/Lightroom Catalog.lrcat`).

## How SNIPED_OS is used going forward
A **high-priority legacy/source library**, not current truth. The router sends brand-strategy, book-framework, and history questions there for depth, then reconciles against AI-Brain-Refinery current-state. On any conflict, the newer proven AI-Brain-Refinery truth wins (see priority rules).

## How AI-Brain-Refinery stays command center
It holds the gates (reference, story, premium-stack, source), the libraries, the loaders, and the current-state docs. Every router answer returns to it for execution. External folders are consulted, never promoted above current-state.

## Wired vs external
- **Wired into the OS:** the registry + router + scanner + priority rules (this layer); AI-Brain-Refinery and the active Alma project.
- **Mapped but external (consulted on demand):** SNIPED_OS, BJ-WIKI, Pictures/Lightroom, ClaudeBusiness, sniped-media, Downloads/Desktop.
- **Needs compression next:** the SNIPED_OS book/framework corpus -> decision-principle cards (do not read raw each time).
- **Stale/duplicate/risky:** Downloads (duplicate/intake), Desktop (scratch), sniped-media (legacy Apr); Pictures/ClaudeBusiness contain client/identity info (private handling).

## Command
```
python3 00_COMMAND_CENTER/scripts/os_source_router.py "<your decision or query>"
python3 00_COMMAND_CENTER/scripts/os_source_map_scan.py --verify     # read-only freshness check
```
