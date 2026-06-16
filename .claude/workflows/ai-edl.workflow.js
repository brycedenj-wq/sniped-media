export const meta = {
  name: 'ai-edl',
  description: 'Generic, reusable edit-decision-list + assembly-plan harness. Turns loose shots/stills/renders/clips (AI fashion film, short film, teaser, still-image-to-video, client edit, or render selection) into an EDL table, a missing-shot list, a regenerate list, an assembly checklist, and a QA verdict. Grounded in the SNIPED OS editing doctrine; no project-specific behavior.',
  whenToUse: 'Run after assets exist (generated or shot) and before any NLE timeline is cut. Use for any edit-planning job where the inputs are a folder or list of media and a brief, and the output must be a defensible cut plan, not a finished render.',
  phases: [
    { title: 'Inventory', detail: 'ls + probe the asset dir or list; build the moment-aware asset inventory (NLE_MOMENT_BASED_EDITING_OS).' },
    { title: 'Selects', detail: 'selects vs rejects via os-vision-reject-gate criteria + REAL_FILM_PRODUCTION_OS kill criteria F1-F7.' },
    { title: 'Beat map', detail: 'map story-beat order on the open-strong / but-therefore curve (EDITING_DISCIPLINE structure).' },
    { title: 'EDL build', detail: 'build the EDL TABLE: # | asset | in/out | duration | beat | transition | sound.' },
    { title: 'Durations', detail: 'assign shot durations with pacing contrast >= 2.2x; hero = longest hold.' },
    { title: 'Transitions', detail: 'cut-on-action default; motivated-only; hard cuts unless a reason proves otherwise.' },
    { title: 'Sound', detail: 'diegetic-first sound map; owned music belongs to finishing, never in a generation prompt.' },
    { title: 'Continuity', detail: 'continuity risk scan: identity/grade drift, screen direction, one-world (os-world-bible).' },
    { title: 'Gaps', detail: 'missing-shots list + regenerate list (the shots the edit needs that the assets do not provide).' },
    { title: 'QA + proof', detail: 'Commercial Craft 12-axis + kill criteria self-score, then hand to adversarial-verify; emit the proof checklist.' },
  ],
}

const A = args || {}
const assets = A.assets
const brief = A.brief || A.concept || ''
const target = A.target_duration_s || 30
const declaredFormat = A.format || ''
const bpm = A.bpm || ''

// ---- ASK-THE-HUMAN PATH: no assets, nothing to edit. Return immediately. ----
if (!assets || (Array.isArray(assets) && assets.length === 0)) {
  log('ai-edl: args.assets is empty. Cannot build an EDL with no media.')
  return {
    ask_human: 'Supply args.assets: either a directory path (the workflow will ls + probe it) or an array of file paths to the shots/stills/renders/clips. Optionally pass args.brief (story/intent), args.target_duration_s (default 30), args.format, and args.bpm.',
    inventory: null, selects: null, beat_map: null, edl_table: null,
    missing_shots: null, regenerate_list: null, assembly_checklist: null, qa_verdict: null,
  }
}

const assetsDesc = Array.isArray(assets)
  ? `an explicit list of ${assets.length} files:\n${assets.join('\n')}`
  : `a directory path: ${assets}`

// Shared doctrine block. Every agent re-reads the law each phase (goal-drift defense, orchestration law 2).
const DOCTRINE = `You are an edit-decision-list builder operating under the SNIPED OS editing doctrine. These files are LAW; whole-read the relevant ones, never skim (No-Sampling Law). Cite the rule by name when you apply it. Em-dashes are banned from everything you output (use commas, periods, parentheses, or colons).

LAW SOURCES (read before deciding):
- 00_COMMAND_CENTER/OS_AUTOEDIT_DOCTRINE.md: every auto-editor is ingest -> selects -> bad-take cleanup -> best-moment detection -> beat grid -> rough-cut build -> VFX/transition apply -> revision package. You build that pipeline, you do not buy it. Bad-take cleanup uses reject rules (wrong person, BTS, AI anatomy, broken plate). Best-moment detection = HERO/PRIMARY/INSERT/ALT, director-label-is-truth-until-disproven. Beat grid = BPM half-beat snap when a BPM is known.
- 00_COMMAND_CENTER/_standards/REAL_FILM_PRODUCTION_OS.md: a FILM SHOT shows a subject performing an action that CHANGES across the shot; a photograph shows a state. The PUSH-IN LAW (Task 7): a still + push-in is NOT a film shot and may only be a memory beat, an insert, a product detail, a transition, or an intentional poster moment; it can never carry emotional climax, realization, or scene action. KILL CRITERIA F1-F7: F1 only-camera motion on a non-insert beat, F2 subject does nothing start-to-end, F3 does not read muted, F4 does not advance story, F5 identity/grade drift, F6 AI-uncanny, F7 cannot answer why-camera-moves and why-cut-here. Editing rhythm E1-E4: classify format then apply its ASL band; jagged edge not monotone; every cut motivated; hero hold is longest, montage beats shortest; pacing contrast IS the craft signal. Continuity C1-C4: lock the look (identity), one grade + one light logic + one world, cut on motion / match on action, hold screen direction and eyelines.
- 00_COMMAND_CENTER/_standards/EDITING_DISCIPLINE.md: hard straight cuts only unless a reference proves a transition; cut on motion and on a fresh tableau; anchor cutting to the music pulse; five-line spine before the timeline (situation, desire, conflict, change, result); desire early, conflict immediately after; end on a result that delivers closure (AIDA); open with the hook as the single most important beat; story first, tool second; keep every shot pulling toward one throughline; do NOT keep a shot just because it is beautiful (story contribution is the only keep criterion); a push-in/zoom is ONE shot not two; mark per-shot whether SUBJECT moves and whether CAMERA moves; expect AI identity/asset drift on every regenerate and plan to re-feed references.
- 00_COMMAND_CENTER/_standards/NLE_MOMENT_BASED_EDITING_OS.md: the edit unit is the MOMENT (a timestamped action/change/beat), not the clip and not the frame. 3-frame strips are TRIAGE ONLY, never the judge. Log moments not clips; one clip can yield several moments. Cut from timestamped moments with explicit in/out to the action. THE 8 MOMENT ROLES every edit must fill: best hook, best attitude, best movement, best product/body, best weird/deadpan, best transition, best hero, best ending/button. THE NEW LAW: if a human remembers a strong moment and the OS does not surface it, the OS failed.
- 00_COMMAND_CENTER/COMMERCIAL_CRAFT_BENCHMARK_V2.md: CLASSIFY THE FORMAT FIRST, then apply that format's ASL band. Format profiles (ASL band, cuts/min): comedy 1.3-3.5s >=12; product spot 1.5-4.0s >=10; beauty/fashion reel 1.0-4.5s >=10; luxury manifesto 3.5-9.0s >=3; social teaser 0.6-2.5s >=16; BTS 2.0-8.0s >=5; tutorial 4.0-18.0s >=2; generic fallback 1.5-6.5s. Slow fails ONLY when the hold is unmotivated, repetitive (uniform lengths), or has no payoff. The 12-axis scorecard (0-3 each, ELITE >=30/36, no axis 0-1): hook_strength, shot_variety, subject_continuity, audio_motivates_cuts, transition_logic, pacing_asl_by_type, visual_hierarchy, typography_captions, payoff, commercial_clarity, rewatch_value, premium_feel. Expensive = motivated cuts, pacing CONTRAST (hero is the longest hold regardless of band), consistent grade, audio-led cutting, restraint, one aggressive hero angle, subject/world continuity.
- The doctrine packs in 00_COMMAND_CENTER/scripts/os_doctrine.py (motion + visual_grade) carry the same motivated-motion and one-grade rules at runtime.

JOB CONTEXT:
- Target duration: ${target}s.
- Declared format: ${declaredFormat || 'NOT DECLARED -> you must classify it from the brief + assets and state which Commercial Craft profile you chose.'}
- BPM / beat grid: ${bpm || 'none supplied -> note where a beat-snap would help but do not invent a tempo.'}
- Brief / story intent: ${brief || 'NOT SUPPLIED -> infer a working story intention from the assets, but FLAG every inferred assumption and tell the caller to confirm story intention and target emotion before this EDL is treated as locked (ask-the-human).'}`

// ===================== PHASE 1: INVENTORY =====================
phase('Inventory')
const inventory = await agent(
  `${DOCTRINE}

PHASE 1, INVENTORY THE ASSETS. The assets are ${assetsDesc}.
If this is a directory: actually run shell to inspect it. List it recursively (ls -R or find), and for media files probe duration/resolution/codec where a tool is available (ffprobe -v error -show_entries stream=width,height,codec_type:format=duration). For stills, note dimensions. Do not guess what you can probe.
If this is a file list: inspect each path that exists; note any path that does not resolve on disk (surface it, do not silently drop it).
Build a MOMENT-AWARE inventory (NLE_MOMENT_BASED_EDITING_OS): for each video asset, note the likely usable MOMENT windows (timestamp ranges of an action/change), not just the whole-clip label; for each still/render, note whether it is a true film-shot candidate or a still that can only legally be a push-in/insert/poster/transition under the Push-In Law. 3-frame impressions are triage only; say so where you only triaged.

Return JSON per the schema.`,
  { schema: {
      type: 'object',
      properties: {
        kind: { type: 'string', description: 'still-image-to-video | clip-edit | mixed-render-selection | short-film | teaser | client-edit' },
        total_assets: { type: 'number' },
        unresolved_paths: { type: 'array', items: { type: 'string' } },
        assets: { type: 'array', items: { type: 'object', properties: {
          id: { type: 'string' }, file: { type: 'string' }, media: { type: 'string', description: 'video|still|render' },
          duration_s: { type: 'string' }, resolution: { type: 'string' },
          moment_windows: { type: 'array', items: { type: 'string' }, description: 'timestamp ranges of usable actions/changes; empty for stills' },
          still_legal_use: { type: 'string', description: 'for stills only: insert | product-detail | poster | transition | memory | film-shot-candidate' },
          triage_only: { type: 'boolean' },
        } } },
        probe_notes: { type: 'string' },
      },
      required: ['kind','total_assets','assets'],
    }, label: 'inventory', phase: 'Inventory', model: 'sonnet' }
)

// ===================== PHASE 2: SELECTS vs REJECTS =====================
phase('Selects')
const selects = await agent(
  `${DOCTRINE}

PHASE 2, SELECTS vs REJECTS. Inventory:
${JSON.stringify(inventory)}

Apply the os-vision-reject-gate criteria and REAL_FILM_PRODUCTION_OS kill criteria F1-F7 + the EDITING_DISCIPLINE keep law. REJECT: wrong person/subject, BTS, AI-uncanny (plastic skin, melted hands, wrong physics), broken plate, identity/grade drift, a still that can only be a push-in but is being asked to carry action (F1/F2), or a beautiful shot that does not advance the story (story contribution is the only keep criterion). SELECT the rest and label each select HERO / PRIMARY / INSERT / ALT (director-label-is-truth-until-disproven). For each reject give the exact kill rule it failed.

Return JSON.`,
  { schema: {
      type: 'object',
      properties: {
        selects: { type: 'array', items: { type: 'object', properties: {
          id: { type: 'string' }, role: { type: 'string', description: 'HERO|PRIMARY|INSERT|ALT' }, why: { type: 'string' },
        }, required: ['id','role'] } },
        rejects: { type: 'array', items: { type: 'object', properties: {
          id: { type: 'string' }, failed_rule: { type: 'string', description: 'e.g. F6 AI-uncanny, F2 no subject change, beauty-without-story' },
        }, required: ['id','failed_rule'] } },
        format_classified: { type: 'string', description: 'the Commercial Craft profile chosen + one-line reason' },
      },
      required: ['selects','rejects','format_classified'],
    }, label: 'selects', phase: 'Selects', model: 'sonnet' }
)

// ===================== PHASE 3: BEAT MAP =====================
phase('Beat map')
const beatMap = await agent(
  `${DOCTRINE}

PHASE 3, MAP THE STORY-BEAT ORDER. Selects + roles:
${JSON.stringify(selects)}

Lock the five-line spine first (situation, desire, conflict, change, result) per EDITING_DISCIPLINE. Then order the beats on the open-strong curve: the hook is the single most important beat and lands the strongest moment in the first ~3s (open the loop), desire early, conflict immediately after, end on a result that delivers closure. Connect every beat to the next by BUT or THEREFORE, never AND-THEN; if two beats only join by and-then, cut one. Confirm the 8 moment roles are covered (hook, attitude, movement, product/body, weird/deadpan, transition, hero, ending/button) and name any role that no available asset fills (that becomes a missing-shot in Phase 9).

Return JSON.`,
  { schema: {
      type: 'object',
      properties: {
        five_line_spine: { type: 'object', properties: {
          situation: { type: 'string' }, desire: { type: 'string' }, conflict: { type: 'string' }, change: { type: 'string' }, result: { type: 'string' },
        } },
        beats: { type: 'array', items: { type: 'object', properties: {
          n: { type: 'number' }, beat: { type: 'string' }, connector: { type: 'string', description: 'BUT | THEREFORE | (open)' },
          candidate_asset_ids: { type: 'array', items: { type: 'string' } }, moment_role: { type: 'string' },
        }, required: ['n','beat'] } },
        unfilled_moment_roles: { type: 'array', items: { type: 'string' } },
      },
      required: ['five_line_spine','beats'],
    }, label: 'beat-map', phase: 'Beat map', model: 'opus' }
)

// ===================== PHASES 4-7: EDL TABLE + DURATIONS + TRANSITIONS + SOUND (one coherent build) =====================
phase('EDL build')
phase('Durations')
phase('Transitions')
phase('Sound')
const edl = await agent(
  `${DOCTRINE}

PHASES 4 to 7, BUILD THE EDL. Beat map:
${JSON.stringify(beatMap)}
Selects:
${JSON.stringify(selects)}
Inventory (for in/out timestamps to the action):
${JSON.stringify(inventory)}

Build ONE EDL table that fits the ${target}s target. Rules you must obey:
- DURATIONS (Phase 5): set durations from the classified format's ASL band. Enforce pacing CONTRAST >= 2.2x between the longest hold and the fastest beat. The HERO beat gets the longest motivated hold; montage/chaos beats are the shortest. Never a monotone string of equal lengths (jagged edge). Sum should land within +/- 10 percent of ${target}s; state the running total.
- IN/OUT (Phase 4): cut from timestamped MOMENTS, not blind whole-clip in-points. For video assets cite in/out to the action window from the inventory. For stills, in/out is the on-screen duration and the row must declare a legal Push-In-Law use (insert/product/poster/transition/memory), never scene action.
- TRANSITIONS (Phase 6): hard straight cut is the default; cut-on-action / match-on-action to hide the seam. A non-cut transition (dissolve, whip, motion-graphic) is allowed ONLY if you can name the story reason; otherwise hard cut. No dissolves to fill time.
- SOUND (Phase 7): diegetic-first, every action has its sound (note the SFX per row). Owned music is a finishing concern: name a tempo/mood and where scene-changes should land on the track's dips, but DO NOT put music into any generation prompt. The cut must read MUTED (hook + payoff legible with sound off).
${bpm ? `- BEAT GRID: BPM is ${bpm}; note half-beat snap points where cuts should land.` : ''}

Return the EDL as a markdown table with EXACTLY these columns: # | asset | in/out | duration | beat | transition | sound. Also return the running total and the contrast ratio achieved.`,
  { schema: {
      type: 'object',
      properties: {
        edl_markdown: { type: 'string', description: 'the markdown table: # | asset | in/out | duration | beat | transition | sound' },
        total_duration_s: { type: 'number' },
        contrast_ratio: { type: 'string', description: 'longest hold / shortest beat, must be >= 2.2x' },
        hero_row: { type: 'string', description: 'which # is the hero (longest motivated hold)' },
        sound_plan: { type: 'string', description: 'diegetic SFX summary + owned-music tempo/mood + dip-sync notes' },
      },
      required: ['edl_markdown','total_duration_s','contrast_ratio'],
    }, label: 'edl-table', phase: 'Sound', model: 'opus' }
)

// ===================== PHASES 8-9: CONTINUITY + GAPS (parallel, independent) =====================
phase('Continuity')
phase('Gaps')
const [continuity, gaps] = (await parallel([
  () => agent(
    `${DOCTRINE}

PHASE 8, CONTINUITY RISK SCAN. EDL:
${edl.edl_markdown}
Beat map:
${JSON.stringify(beatMap)}

Using os-world-bible discipline and REAL_FILM_PRODUCTION_OS C1-C4, find the continuity risks across the cut: identity drift (same subject every shot or kill it), grade/look drift (one grade, one light logic, one world), screen-direction and eyeline breaks, and any place an AI regenerate will likely re-drift (re-feed references). For each risk give the beat numbers and the fix.

Return JSON.`,
    { schema: { type: 'object', properties: {
        risks: { type: 'array', items: { type: 'object', properties: {
          beats: { type: 'string' }, risk: { type: 'string' }, rule: { type: 'string' }, fix: { type: 'string' },
        }, required: ['risk','fix'] } },
      }, required: ['risks'] }, label: 'continuity', phase: 'Continuity', model: 'sonnet' }
  ),
  () => agent(
    `${DOCTRINE}

PHASE 9, MISSING-SHOTS + REGENERATE LIST. EDL:
${edl.edl_markdown}
Unfilled moment roles from the beat map: ${JSON.stringify((beatMap && beatMap.unfilled_moment_roles) || [])}
Rejects (from selects): ${JSON.stringify((selects && selects.rejects) || [])}

MISSING SHOTS: the beats/moment-roles the EDL needs that no surviving asset provides (e.g. the cut needs a clean hero hold or an ending button but none exists). For each, specify the shot the edit needs (subject + action verb + size + why) so production can generate or shoot it.
REGENERATE LIST: assets that were rejected for a fixable reason (AI-uncanny, identity/grade drift, broken plate) AND are needed for a beat, with the exact reason and the re-feed/reference instruction (EDITING_DISCIPLINE: expect drift, re-feed references).

Return JSON.`,
    { schema: { type: 'object', properties: {
        missing_shots: { type: 'array', items: { type: 'object', properties: {
          beat: { type: 'string' }, needed_shot: { type: 'string' }, action_verb: { type: 'string' }, size: { type: 'string' }, why: { type: 'string' },
        }, required: ['needed_shot'] } },
        regenerate_list: { type: 'array', items: { type: 'object', properties: {
          asset_id: { type: 'string' }, reason: { type: 'string' }, refeed_instruction: { type: 'string' },
        }, required: ['asset_id','reason'] } },
      }, required: ['missing_shots','regenerate_list'] }, label: 'gaps', phase: 'Gaps', model: 'sonnet' }
  ),
])).filter(Boolean)

// ===================== PHASE 10: QA SELF-SCORE + PROOF CHECKLIST + ADVERSARIAL HANDOFF =====================
phase('QA + proof')
const qa = await agent(
  `${DOCTRINE}

PHASE 10, QA + PROOF. The full plan:
EDL:
${edl.edl_markdown}
Total ${edl.total_duration_s}s, contrast ${edl.contrast_ratio}, hero ${edl.hero_row || '(unstated)'}.
Continuity risks: ${JSON.stringify(continuity || {})}
Missing/regenerate: ${JSON.stringify(gaps || {})}

Do TWO things:
1) SELF-SCORE the EDL on the Commercial Craft 12-axis scorecard (0-3 each: hook_strength, shot_variety, subject_continuity, audio_motivates_cuts, transition_logic, pacing_asl_by_type, visual_hierarchy, typography_captions, payoff, commercial_clarity, rewatch_value, premium_feel). ELITE is >=30/36 with no axis at 0-1. Then run the kill criteria F1-F7 and the Push-In Law over the EDL and name any row that fails.
2) Write the ASSEMBLY + PROOF CHECKLIST the caller must complete before this EDL is locked. It MUST name, in order: build the rough cut from these in/out moments; /watch the assembled cut and confirm each beat's intended MOMENT is on screen (NLE_MOMENT_BASED_EDITING_OS rule 6); pass the standing adversarial-verify workflow (.claude/workflows/adversarial-verify.workflow.js) which tries to break the cut from fresh context (no self-crowning, self-preferential-bias law); record artifacts + gates with os_proof_manifest.py and emit an OS_RECEIPT via os_receipt.py (the Stop hook blocks done/final/client-ready without it).

This self-score is NOT the final verdict. State explicitly that the cut is not crowned until adversarial-verify passes from a fresh context.

Return JSON.`,
  { schema: {
      type: 'object',
      properties: {
        scorecard: { type: 'object', description: 'the 12 axes with 0-3 each' },
        total_score: { type: 'string', description: 'sum/36 and whether ELITE' },
        kill_criteria_flags: { type: 'array', items: { type: 'string' }, description: 'any EDL row failing F1-F7 or the Push-In Law, empty if none' },
        verdict: { type: 'string', description: 'PASS-pending-adversarial | NEEDS-REBUILD, with the reason; never a crown' },
        assembly_checklist: { type: 'array', items: { type: 'string' } },
        not_crowned_note: { type: 'string' },
      },
      required: ['total_score','verdict','assembly_checklist'],
    }, label: 'qa-verdict', phase: 'QA + proof', model: 'opus' }
)

return {
  ask_human: brief ? null : 'No brief was supplied. Confirm the story intention and target emotion before locking this EDL; every inferred assumption is flagged in the beat map.',
  inventory,
  selects,
  beat_map: beatMap,
  edl_table: edl.edl_markdown,
  edl_meta: { total_duration_s: edl.total_duration_s, contrast_ratio: edl.contrast_ratio, hero_row: edl.hero_row || null, sound_plan: edl.sound_plan || null },
  continuity_risks: (continuity && continuity.risks) || [],
  missing_shots: (gaps && gaps.missing_shots) || [],
  regenerate_list: (gaps && gaps.regenerate_list) || [],
  assembly_checklist: qa.assembly_checklist,
  qa_verdict: qa,
}

