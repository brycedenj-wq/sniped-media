# 09 · MIGRATION PLAN · From SNIPED to BASEPLATE STUDIO

**Locked:** 2026-05-13 (evening · v2 · updated for actual brand bible + two-account architecture)

Migration is simpler than v1 of this file outlined. Since the @baseplate.studio account, domain, handles, logo files, and brand bible are all already built (since 2026-04-11), this is a deployment plan, not a brand-creation plan.

---

## The migration window

| Day | Date | Phase |
|---|---|---|
| Wed | 2026-05-13 | DECISION DAY · BJ commits to BASEPLATE STUDIO |
| Wed | 2026-05-13 evening | CH01 Yae HERO posts under SNIPED · do not touch · already locked |
| Thu | 2026-05-14 | OS file find-replace · memory layer update · low-cognition work |
| Fri | 2026-05-15 | CH01 Yae Card posts under SNIPED · chapter seals end of day |
| Sat | 2026-05-16 | Figma session · rebuild Card master in BASEPLATE STUDIO industrial register |
| Sun | 2026-05-17 | Two-account migration · CH02 Mimi Card produced under BASEPLATE STUDIO |
| Mon | 2026-05-18 | CH02 Mimi Build 1 posts from @baseplate.studio · brand goes live publicly |

Total window: 5 days. Most steps are 15-60 min each. The Saturday Figma session is the longest single block (2-3 hours).

---

## Migration steps (sequenced)

### Step 1 · OS-wide find-and-classify audit (30 min · Thu morning)

Goal: classify every SNIPED reference in the OS by needed action.

Categories:
- **Active production docs** (`/05_PRODUCTION/chapter_rollout_doctrine_v1.md` · `ch02_mimi_production_brief_v1.md` · etc.) → UPDATE references to BASEPLATE STUDIO
- **Active brief docs** (`/00_BRIEF/CURRENT_STATE.md` · `OPERATOR_QUESTIONS_2026-05-13.md` · etc.) → UPDATE references with footnote noting the rebrand
- **Historical / locked canonical docs** (`CANONICAL_TRUTHS.md` · `100Q_AUDIT_OPTIMIZATIONS_2026-05-13.md` · `THE_LINEAGE_DOCTRINE.md` · etc.) → ADD top-of-file footnote · do not rewrite content
- **Legacy / superseded** (anything tagged "v1 legacy" · old preset backups) → LEAVE as historical record
- **Memory layer files** (in `/Users/sniper/.claude/projects/-Users-sniper/memory/`) → UPDATE user_role · project_sniped_* files · MEMORY.md index

Classification first · then update intentionally. Avoid blind find-replace.

### Step 2 · Update active operating files (60 min · Thu morning)

Files to update with BASEPLATE STUDIO references:

- `/00_BRIEF/CURRENT_STATE.md` · top section · "primary side venture: BASEPLATE STUDIO (formerly SNIPED · rebrand 2026-05-13)"
- `/00_BRIEF/THE_SPINE.md` · header + brand section
- `/00_BRIEF/CANONICAL_TRUTHS.md` · add Truth 13: "BASEPLATE STUDIO is the brand · SNIPED was the prototype"
- `/00_BRIEF/OPERATING_LOCKS_2026-05-12.md` · add Lock 15: "BASEPLATE STUDIO brand locked through 2028-12-31"
- `/00_BRIEF/ACTIVE_THREADS.md` · add Thread 1z: "Brand migration · SNIPED → BASEPLATE STUDIO"
- `/05_PRODUCTION/chapter_rollout_doctrine_v1.md` · update CH02 applied rollout to read BASEPLATE STUDIO
- `/05_PRODUCTION/ch02_mimi_production_brief_v1.md` · update header + caption convention

Each file: top-of-file note: `Rebrand 2026-05-13: SNIPED → BASEPLATE STUDIO. Historical SNIPED references preserved as context.`

### Step 3 · Create rebrand log (15 min · Thu morning)

Create `/00_BRIEF/REBRAND_LOG_2026-05-13.md` · the single source of truth for the migration. Include:

- Decision date · 2026-05-13
- Reason · file 01 audit summary
- New name · BASEPLATE STUDIO
- Existing assets discovered · brand bible 2026-04-11 · logo files · handles · domain
- Architecture · single brand (file 05)
- Files updated
- Surfaces migrated
- Surfaces deliberately left unchanged · CH01 Yae Card · legacy OS docs

### Step 4 · Update Claude memory layer (15 min · Thu morning)

- `user_role.md` · update SNIPED → BASEPLATE STUDIO · note SNIPED as legacy prototype phase
- `project_sniped_media.md` · rename or add footnote
- `project_sniped_spine.md` · rename or add footnote
- `MEMORY.md` index · update entries

Preserve SNIPED context as historical record · don't erase the prototype phase.

### Step 5 · Saturday Figma session · Card master rebuild (2-3 hours · Sat afternoon)

Per file 08 visual identity brief. Full Figma session brief there. Summary:

1. Open existing Chapter Card master Figma (`AiMtRfT8W33yZRf4khjnds`)
2. Archive Page 1 + Page 2 (SNIPED-era warm-archival) → rename to `LEGACY · SNIPED v1`
3. Create new Page 3 · `BASEPLATE STUDIO · MASTER v1`
4. Build 5 Card variants in industrial register:
   - DARK STANDARD (default · `#0F0F0F` background · white wordmark)
   - LIGHT STANDARD (alternate · `#FFFFFF` background · black wordmark)
   - DARK + BLUE ACCENT (special edition · single `#0055FF` element)
   - 1:1 SQUARE (grid format)
   - 9:16 STORY (vertical format)
5. Import BASEPLATE wordmark + B-mark PNG/SVG from `/Users/sniper/Downloads/BASEPLATE/Logo Files/`
6. Set Helvena (or Helvetica Neue / Inter fallback) as primary typeface
7. Build text styles · color styles
8. Test against CH02 Mimi leather coat standing front frame · apply Card · verify register
9. Export each variant PNG · file in `/04_DELIVERABLES/CH02_mimi/cards/baseplate_studio_v1/`

Output: BASEPLATE STUDIO Card master ready for Sunday production.

### Step 6 · CH02 Mimi Card production (60 min · Sun morning)

- Pull CH02 Mimi leather coat standing front frame
- Run through Evoto backdrop swap (Option A plaster `#BEB8AE` · per Mimi brief) · NOTE: this backdrop reads as gray-warm · check it sits cleanly inside the dark Card frame
- Run v3 LUXURY edit pass in Lightroom · then B&W desaturate
- Drop into DARK STANDARD variant of new Card master
- Update text fields:
  - Masthead: BASEPLATE STUDIO + B-mark
  - VOL · II · CHAPTER 02
  - MIMI · LOS ANGELES · MAY 2026
  - Cover line: TBD (working: "Texture as power.")
  - Colophon: EDITION I · MMXXVI · CHAPTER 02 · SERIAL 01 / 01 · direction & photography · BRYCE DENJ · LINEAGE · [tbd]
- Export Card · file ready for Tue 5/26 publish per chapter rollout doctrine

### Step 7 · Two-account social migration (45 min total · scattered Thu-Sun)

#### Update existing SNIPED account (the old one · stays as archive)

- Sun 5/17 evening:
  - Display name → `BASEPLATE STUDIO · ARCHIVE · CH01`
  - Bio → `Vol I · The prototype era · CH02+ at @baseplate.studio`
  - Pinned post → simple announcement "CH02+ at @baseplate.studio" (no carousel · single image · per voice rules)
- Account goes dormant after pinned post · never delete

#### Update @baseplate.studio account (the new primary)

- Sun 5/17 evening:
  - Display name → `BASEPLATE STUDIO`
  - Bio → `BASEPLATE STUDIO · A named archive · LA · est. 2026`
  - Profile picture → BASEPLATE B-mark from `/Users/sniper/Downloads/BASEPLATE/Logo Files/Profile/Verson 3.jpg` or 4
  - Story highlights → empty for now · build over time
  - Link in bio → `baseplate.studio` domain (placeholder page if needed)

### Step 8 · Other surfaces migration (cumulative 30 min · scattered Thu-Sun)

- **LinkedIn role / headline** → "Photographer · BASEPLATE STUDIO"
- **LinkedIn About** → use founder bio template from file 06
- **LinkedIn header banner** → BASEPLATE STUDIO wordmark on dark mode
- **Email signature** → "Bryce Denj · BASEPLATE STUDIO · baseplate.studio"
- **TikTok bio** → match IG bio
- **X bio** → match IG bio
- **Trademark filing prep** → not now · within 90 days · file in Class 41 (Education/Cultural Services) and Class 16 (Printed matter)

### Step 9 · Brand attribution test (15 min · Sun)

Before Mon 5/18 launch · smoke test:

1. Read your LinkedIn About out loud · does it sound like BASEPLATE STUDIO brand voice?
2. Read your IG bio · does it pass file 07 voice anchors (Named · Sealed · Quiet · Lineage)?
3. Read the new CH02 Mimi Card colophon · does the industrial register hold visually?
4. Compare side-by-side: the CH01 Yae warm-archival Card vs the CH02 Mimi industrial Card · does the brand evolution read as deliberate evolution (good) or as inconsistent (bad)? If inconsistent · adjust Card master before launch.

### Step 10 · Mon 5/18 BASEPLATE STUDIO public launch (15 min · Mon morning)

- Post CH02 Mimi Build 1 ("Mimi · 01") to @baseplate.studio
- First comment (the transition announcement · per file 07 voice):

```
Photography · @brycedenj
Direction · BASEPLATE STUDIO
Composite · @[rejuar handle]

The archive previously published under SNIPED · CH02 opens BASEPLATE STUDIO · Vol II.
```

- The migration is complete · BASEPLATE STUDIO is live

---

## What we explicitly do NOT migrate

### CH01 Yae (preserve · do not retroactively rebrand)

- Yae · 01 + Yae · 02 IG posts stay on the SNIPED account as historical record
- Yae HERO posts tonight on SNIPED account · caption stays · credits cite SNIPED
- Yae Card posts Fri 5/15 on SNIPED account · existing warm-paper Playfair Card is the closing artifact of the prototype phase
- These artifacts read as "the SNIPED-era · the prototype" in the future monograph · footnoted appropriately

### Legacy OS files

- `/05_PRODUCTION/sniped_operating_system_v1_legacy.md` · already named legacy · stays
- Old preset backups · stay
- Historical drafts · stay

### The SNIPED name in archive

SNIPED stays in the historical record · doesn't get erased from the OS · doesn't resurface as a methodology trademark or sub-brand. Closed chapter.

---

## Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| BJ second-guesses BASEPLATE STUDIO after committing | Low (brand bible is a month old · this is recommitment not first commitment) | Files 04 + 01 captured the rationale · read back if doubt surfaces |
| The new Card master in industrial register doesn't land aesthetically | Medium | Saturday Figma session includes test pass against CH02 Mimi frame · adjust before Sunday production |
| CH02 Mimi production rushed by migration overhead | Low-Medium | Migration tasks are mostly low-cognition · run in 2-5pm slump · protect 10am-2pm for production per Q1 lock |
| Audience confusion over the rebrand | Negligible | Pre-audience phase · ~0 followers to confuse · the one-line first-comment note on CH02 Mimi Build 1 is sufficient announcement |
| Trademark conflict surfaces during USPTO search | Low | Run preliminary TESS search before filing · file within 90 days |
| The Helvena font isn't licensable | Low | Helvetica Neue (Apple-shipped) or Inter (free) substitute within 5% visually |

---

## Migration completion check

The migration is "complete" when:

- [ ] All Step 1-9 tasks are done
- [ ] CH02 Mimi Build 1 posts from @baseplate.studio Mon 5/18
- [ ] BJ's LinkedIn / IG / TikTok / X / email signature all read BASEPLATE STUDIO
- [ ] baseplate.studio domain has at least a placeholder page
- [ ] OS files are updated · rebrand log filed
- [ ] CH02 Mimi Card built in BASEPLATE STUDIO industrial register · ready for Tue 5/26 publish
- [ ] Trademark filing is calendared for within 90 days
- [ ] SNIPED account has pinned redirect post + dormant status

---

## Post-migration first 30 days

Days 1-12: CH02 Mimi rollout (per chapter rollout doctrine v1.1 · breath day discipline)
Days 13-26: CH03 Jada rollout
Days 27-30: Breath / planning · CH04 enters intake

By Day 30 · BASEPLATE STUDIO has 2 chapters in the canonical archive (CH02 · CH03) plus the SNIPED-era CH01 prototype. The brand is operating · trademark filed · domain live.

The pre-audience phase continues. But it continues under the right name, with the right visual system, with the right architecture. Compound interest starts now.
