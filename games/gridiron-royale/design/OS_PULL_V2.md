# OS_PULL_V2 · Gridiron Royale v2 · SNIPED OS synthesis

Pulled 2026-06-12 from four OS reader lanes (craft-doctrine, hit-mechanics, status-psych, voice-copy) plus the qa-gates lane. Deduplicated, prioritized, and compiled into directives a programmer can implement without reading the sources.

Build target: Three.js arcade football. Rigged GLB characters (hero runner + 12 defender instances), announcer VO, sky-island world. Config frozen in `design/thresholds.md`; loop frozen in `design/plan.md`.

No em-dashes anywhere in this file or in any copy it defines. Lifetime rule.

---

## 1. The 18 laws (priority order) with exact v2 directives

### P1 · Performance is motion. The skeleton must change across every clip.
Source: REAL_FILM_PRODUCTION_OS.md lines 12-14, 43-46.
A moving camera over a static rig is a moving photograph, not gameplay animation.
DIRECTIVE: Every GLB animation clip (run, sprint, juke L/R, spin, tackle-fall, catch, celebrate, skydive) must fail a start-vs-end pose diff if the skeleton is static. Implement `assertClipMoves(clip)`: sample the quaternion of hips, spine, both hands and both feet at t=0 and t=duration; if total angular delta < 15 degrees summed, log REJECT and refuse to register the clip at boot in dev mode. Run cycle must show foot plant + weight shift (hip sway on Z), not a slide. No GLB ships with a "pose held + translate" clip.

### P2 · Author a START and an END pose for every beat. One continuous motion, no mid-clip cuts.
Source: OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md lines 61-62, 75-76.
DIRECTIVE: Each hero beat is defined as a (startPose, endPose, duration, verb) tuple in a `BEATS` table: SKYDIVE (spread-eagle to landing crouch, 2.0s), JUKE (plant-foot lean to opposite-shoulder drive, 0.25s), SPIN (ball-tuck to arm-out exit, 0.4s), TOUCHDOWN_CELEBRATE (ball-raise to chest-pound, 2.0s). Use THREE.AnimationMixer crossfade 0.1s between clips; never hard-swap mid-clip. Micro layer: on tackle, play a 4-frame head-snap toward the tackler before ragdoll; on TD catch-equivalent (goal-line cross), close the free hand over the ball across 6 frames at 60 Hz. Micro beats cost zero draw calls and read as emotion.

### P3 · Motivated camera only. The camera follows action; it never invents motion.
Source: OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md line 10; REAL_FILM_PRODUCTION_OS.md lines 33-34.
DIRECTIVE: One chase camera, offset behind-above the hero, lerp position at 6.0/s, lookAt the hero chest bone. Camera state changes ONLY on game events: TD scored, tackled, golden ball grabbed, MVP reached. No timer-driven cuts, no idle orbits. If the celebration uses a 360 view, rotate the PLAYER (celebrate clip spins the rig) and let the camera hold or follow; the body motion justifies the move. Name every camera state by the action it covers: `CAM_CHASE_RUN`, `CAM_TD_WIDE`, `CAM_TD_TIGHT`, `CAM_TACKLE_IMPACT`, `CAM_MVP_HERO`.

### P4 · Cover the touchdown in 3 sizes and cut with contrast. Uniform pacing reads amateur.
Source: REAL_FILM_PRODUCTION_OS.md lines 48-50, 59-63; COMMERCIAL_CRAFT_BENCHMARK_V2.md lines 5-6.
DIRECTIVE: On TD, run a 3-shot scripted replay before next drive: WIDE (FOV 38, sideline height, full field, 1.0s), MEDIUM (FOV 52, hero + nearest beaten defender, 0.8s), TIGHT (FOV 70, ball and hands isolation, 2.4s hold, slow-mo 0.4x). The tight hero hold is the LONGEST; the contrast ratio (2.4s vs 0.8s = 3x) is the craft signal. Cut on motion (mid-stride momentum carries across the cut), trigger each cut on an action frame, not a timer rounded to seconds. Total replay <= 4.2s so the 120s clock pressure holds (clock pauses during replay).

### P5 · Diegetic sound first. The game must read muted.
Source: OS_ELEVATED_AI_FILM_DOCTRINE_2026-06-09.md line 22; REAL_FILM_PRODUCTION_OS.md lines 65-69.
DIRECTIVE: Key SFX to physics/state events at the exact frame: footstep loop rate tied to run speed, pad-contact thump on tackle collision callback, whoosh on juke dash start, laces-whistle on golden ball spawn. Crowd roar triggers on GAME EVENTS (TD, golden ball, first down equivalent = wave clear), never on camera cuts. Duck the crowd bed by 6 dB for 0.5s when the hero plants for a juke so the diegetic action punches through. Mix per thresholds.md: music -18 dBFS, SFX -10 to -12 dBFS, true peak <= -3 dBFS (code gains: music 0.35, SFX 0.8). ACCEPTANCE TEST: play 5s of gameplay muted; every block, juke, and score must read on visuals alone, or the blocking (P1/P2) is weak and gets fixed first.

### P6 · Lock identity once. One grade across every camera.
Source: REAL_FILM_PRODUCTION_OS.md lines 53-57.
DIRECTIVE: The hero GLB (jersey number, helmet decal, palette) is instantiated ONCE at match start and reused across gameplay, replays, and end screen; no model swap, no material re-randomization between camera states. One post pass for the whole game: a single tone-mapping + color grade (ACESFilmicToneMapping + one Lut or vignette pass) applied at the renderer level, never per camera. Screen direction holds: the drive always runs toward -Z on screen-up; replays never mirror the field.

### P7 · The announcer's intensity scales with the play. Status is read from the voice in milliseconds.
Source: The Status Game (Storr), CULTURE_AND_STATUS_CHUNKS.jsonl chunks 002-003.
DIRECTIVE: Record/generate VO in 3 intensity tiers and route by play value. Tier 1 calm (wave clear, routine pickup), Tier 2 rising (golden ball, style chain x2), Tier 3 full roar (touchdown, hot hand, MVP). Crowd roar gain is proportional to points value: golden ball roar at 0.5 gain, TD at 0.8, MVP at 1.0 plus stadium light pulse. Implement `announce(eventKey)` that picks the VO file and sets crowd gain from one `EVENT_INTENSITY` table. Never play a Tier 3 read over a 3-yard moment.

### P8 · Status is conferred by others, never self-declared. State the WHY of praise.
Source: Storr chunk 004; Cialdini influence excerpts; Guidara principle.
DIRECTIVE: The game never tells the player "you are awesome." All praise arrives through the crowd, the announcer, the leaderboard, and defender behavior. Announcer lines name the evidence: "Three scores in one half" not "you are great." Defender AI respects rank: at ALL-STAR rank or above, spawn one extra deep-safety pattern (visible respect = conferred status). Crowd-energy meter on the HUD rises from crowd response to plays; the player cannot fill it directly, only earn it.

### P9 · Visible, earned, losable status ladder. Badges beat points.
Source: Elephant in the Brain via intel_status_psychology.md; Cialdini commitment-consistency; Storr chunk 007.
DIRECTIVE: Implement a 4-rung in-match rank ladder driven only by measurable play stats (points + style chain peaks): ROOKIE (start), PRO (7 pts), ALL-STAR (14 pts), HALL OF FAME (21 pts, replaces no other reward, coexists with MVP CHAMPION). Rank chip is always visible in the HUD. HOT HAND badge: render above the helmet after 2 consecutive TDs without a tackle; it is LOST on tackle with an explicit "STREAK OVER." card. Losing the badge must be visibly marked; loss aversion is the engine. Zero RNG in any rank or badge trigger.

### P10 · Make the achievement public. The observation is the reward.
Source: Adam Smith via de Botton in intel_status_psychology.md; status synthesis chunks 015-016.
DIRECTIVE: On TD: 3s on-screen celebration card with ascending animation (score value counts up 0 to 7), stadium board texture in the sky-island world swaps to the event text, announcer + crowd synchronized to the visual within 2 frames. Recognition ticker strip at screen bottom fires one line per earned event ("HOT HAND ACTIVE", "WAVE 4 CLEARED", "ALL-STAR"). BEST score renders beside SCORE at all times so rank movement is observed live. End screen shows a persistent local Hall of Fame: top 5 best scores (localStorage), so the same target names/scores are seen on every replay (repetition compounds recognition; Hit Makers exposure law).

### P11 · Engineer unpromised moments. Surprise beats predictability.
Source: Guidara Unreasonable Hospitality via intel_hospitality_layer.md; Cialdini reciprocation.
DIRECTIVE: Two hospitality systems, both EARNED-triggered but not advertised anywhere in UI copy: (1) CROWD SURGE: after a TD scored with the style chain at x2 or higher, next drive starts with +500 bonus points banked and an extra crowd swell. (2) LEGENDARY MOMENT: after 3 consecutive wave clears without a tackle, fire a one-off scripted beat: stadium lights pulse with crowd rhythm, slow-mo replay of the last juke, unique fanfare sting. Cap each at once per match so it stays a gift, not an economy. Never show these in the tutorial or controls copy; the surprise is the point.

### P12 · MAYA: familiar core, one novel element per play.
Source: Hit Makers (Thompson), BATCH_001_CHUNK_077.
DIRECTIVE: The verb set stays pure football-arcade (run, sprint, juke, spin, score); do not add exotic mechanics. The novelty budget is spent in exactly two places: (a) announcer reacts to the OUTCOME in real time (brutal-honest Tier 1 line on a 4th-down turnover, over-the-top Tier 3 on a walk-off TD), (b) the golden ball bounces with seeded unpredictable physics when dropped. Anything novel beyond those two is cut.

### P13 · Open with a curiosity gap. Withhold the payoff, then reveal at the climax.
Source: Made to Stick BATCH_009_CHUNK_068; story rules S1-S4, doctrine lines 19-25; chapter cadence chunks 050/053.
DIRECTIVE: Log line for the whole game, locked: "Eighty yards, four downs, one runner against the wave; score 21 and the stadium remembers the name." Title screen states the goal as a gap ("Score 21+ to take MVP CHAMPION") with the field visible below; first meaningful action stays one input away. In-match: NO premature MVP fanfare; at 14+ points the announcer goes quieter, not louder (withhold), the crowd bed drops 3 dB, then the 21st point releases the full Tier 3 roar + lights + MVP card (reveal). Final score is not shown on screen during the last drive; only on resolution.

### P14 · One explicit CTA per end screen. Route the next action.
Source: Hormozi BATCH_009_CHUNK_064; Godin BATCH_009_CHUNK_047.
DIRECTIVE: End screen renders exactly two buttons and one of three context-picked headline asks: if score < best, headline is "Beat {best}?" with RUN IT BACK primary; if new best, headline is "New best. Prove it." with COPY CHALLENGE primary; if MVP reached, headline is "MVP. Now defend it." with RUN IT BACK primary. Never more than two actions on screen (no multi-CTA mess; voice-copy failure mode 5).

### P15 · Build social currency into the share. The sharer must look good.
Source: Contagious (Berger) BATCH_009_CHUNK_030/031/033; Hit Makers broadcast law.
DIRECTIVE: COPY CHALLENGE writes one line to the clipboard: "I dropped {score} in Gridiron Royale. Beat that. {url}". If MVP was earned the line upgrades: "MVP. {score} points in Gridiron Royale. Your move. {url}". High-arousal, sharer-flattering, zero hashtags. One share path only (clipboard), pointed at wherever the operator's single launch channel is (P16).

### P16 · One atomic network before any spread.
Source: Cold Start Problem (Chen) BATCH_002_CHUNK_102; smallest viable audience BATCH_009_CHUNK_076.
DIRECTIVE (operator-level, recorded here so the build supports it): launch into ONE community channel only; the share URL and any launch copy point at that single channel until it is self-sustaining. No multi-platform share buttons in v2. The game ships with the clipboard share only; platform-specific integrations are out of scope until the first channel proves retention.

### P17 · SNIPED voice on every string. Restraint is the moat.
Source: sniped-caption-writer SKILL.md; sniped-positioning-phrases SKILL.md; /Users/sniper/.claude/CLAUDE.md; feedback_visual_direction_luxury_editorial.md.
DIRECTIVE: All player-visible text lives in `strings.js` only (no literals in game.js/logic.js). Rules enforced at review: short declarative sentences; HUD elements all-caps; zero em-dashes (scan the file for U+2014 before every ship); no crutch words (obsessed, stunner, fire, literally, honestly); no emojis; no exclamation stacking (max one "!" per string); observation over claim; periods and middle dots as separators. The full locked copy set is Section 2 of this file. Any new string goes through the same scan.

### P18 · PASS is not done. Nothing is crowned without receipts.
Source: OS_FINISHING_DEPARTMENT_STANDARD.md lines 9-13; os-quality-gates SKILL.md Gate 8; OS_UPGRADE_FROM_VIDEOS_2026-06-08.md Section 2.
DIRECTIVE: v2 does not ship on "looks okay." The 12-gate checklist in Section 3 runs in order; any FAIL halts the ship and names the remediation. Gates 1-10 require numeric proof artifacts (fps trace JSON, network screenshot, test runner output); Gate 12 produces the deploy receipt the operator approves. A fresh-context adversarial pass (Gate 9 harness) runs before the human sees the build; the builder never crowns its own output.

---

## 2. Final copy set (locked · SNIPED voice · zero em-dashes)

Drop-in replacement for `public/strings.js`. v1 strings retained where already in voice; v2 additions marked.

```js
// All player-visible text lives here. Switching language = swapping this file.
// Voice: SNIPED rules. Short. Declarative. Zero em-dashes, ever. Max one "!" per string.
export const STR = {
  // Title and entry
  title: "GRIDIRON ROYALE",
  tagline: "Drop in. Juke everything. Take it to the house.",
  tapToDrop: "TAP OR PRESS ANY KEY TO DROP IN",
  goal: "Score 21+ to take MVP CHAMPION",
  controlsKeyboard: "WASD or Arrows run · Shift sprint · Q/E juke · Space spin",
  controlsTouch: "Left side: stick · Right side: SPRINT / JUKE / SPIN",
  controlsPad: "Gamepad: stick run · A sprint · LB/RB juke · B spin",
  loading: "SUITING UP...",

  // HUD
  score: "SCORE",
  best: "BEST",
  time: "TIME",
  downs: "DOWNS",
  wave: "WAVE",
  style: "STYLE",
  stamina: "STAMINA",
  crowd: "CROWD",                            // v2: crowd-energy meter label (P8)

  // Rank ladder (v2 · P9)
  rankRookie: "ROOKIE",
  rankPro: "PRO",
  rankAllStar: "ALL-STAR",
  rankHallOfFame: "HALL OF FAME",
  rankUp: "RANK UP · {rank}",

  // Play events
  touchdown: "TOUCHDOWN! +7",
  goldenBall: "GOLDEN BALL! +3",
  styleBonus: "STYLE BONUS",
  chain2: "STYLE CHAIN x2",
  chain3: "STYLE CHAIN x3 · UNTOUCHABLE",
  boostPad: "TURBO!",
  tackled: "TACKLED!",
  clutch: "CLUTCH MODE. SPEED UP.",
  lastDown: "LAST DOWN. MAKE IT COUNT.",

  // Status layer (v2 · P9, P11)
  hotHand: "HOT HAND",
  hotHandLost: "STREAK OVER.",
  crowdSurge: "CROWD SURGE · +500",
  legendary: "LEGENDARY MOMENT",
  waveCleared: "WAVE {n} CLEARED",

  // Recognition ticker lines (v2 · P10; pick by event)
  tickerHotHand: "HOT HAND ACTIVE",
  tickerAllStar: "ALL-STAR. EARNED.",
  tickerHallOfFame: "HALL OF FAME. REMEMBER THE NAME.",
  tickerDefenseBeat: "DEFENSE NEVER SAW IT.",

  // End screen
  gameOverClock: "FULL TIME",
  gameOverDowns: "TURNOVER ON DOWNS",
  mvp: "MVP CHAMPION",
  finalScore: "FINAL SCORE",
  hallOfFameBoard: "HALL OF FAME",           // v2: local top-5 board header (P10)
  // Context headline, pick one (P14)
  endHeadlineBeatBest: "Beat {best}?",
  endHeadlineNewBest: "New best. Prove it.",
  endHeadlineMvp: "MVP. Now defend it.",
  playAgain: "RUN IT BACK",
  shareChallenge: "COPY CHALLENGE",
  shareCopied: "COPIED. SEND IT.",
  shareText: "I dropped {score} in Gridiron Royale. Beat that.",
  shareTextMvp: "MVP. {score} points in Gridiron Royale. Your move.",  // v2 (P15)

  // System
  sprint: "SPRINT",
  jukeL: "JUKE L",
  jukeR: "JUKE R",
  spin: "SPIN",
  paused: "PAUSED · CLICK TO RESUME",
  endzoneA: "GRIDIRON",
  endzoneB: "ROYALE",
  nightShow: "NIGHT GAME. LIGHTS ON.",
  webglRequired: "This game needs WebGL. Open it in a normal browser (Chrome, Safari, Firefox).",
};

// Announcer VO scripts (v2 · P7, P8, P13). Tier sets delivery intensity.
// Praise names the evidence. The game never says "you are awesome."
export const VO = {
  vo_welcome:    { tier: 1, text: "Welcome to Gridiron Royale. Eighty yards. Four downs. The crowd is yours to win." },
  vo_waveclear:  { tier: 1, text: "Wave down. Keep moving." },
  vo_goldenball: { tier: 2, text: "Golden ball. Three more on the board." },
  vo_chain:      { tier: 2, text: "Second one in a row. He is feeling it." },
  vo_touchdown:  { tier: 3, text: "Touchdown! That is seven." },
  vo_hothand:    { tier: 3, text: "Two straight scores. Hot hand. Nobody can touch him right now." },
  vo_tackled:    { tier: 1, text: "Brought down. That one hurt." },
  vo_turnover:   { tier: 1, text: "Fourth down gone. That is the ball game." },
  vo_lastdown:   { tier: 2, text: "Last down. Whole stadium on its feet." },
  vo_mvp:        { tier: 3, text: "Twenty one. Three scores in one half. MVP. Remember the name." },
};
```

Pre-ship copy scan (mandatory): `grep -n $'\xe2\x80\x94' public/strings.js` must return nothing (U+2014 byte scan); grep for crutch words (obsessed, stunner, fire, literally, honestly) must return nothing; no string carries more than one "!".

---

## 3. Pre-ship QA gate checklist (all 12 must PASS · any FAIL halts and names remediation)

Sources: os-quality-gates SKILL.md, composite-master-qa SKILL.md, os-vision-reject-gate SKILL.md, OS_UPGRADE_FROM_VIDEOS_2026-06-08.md Section 2, design/thresholds.md.

- [ ] GATE 1 · Frame-rate proof. 30s recorded runs on 3 scenes (title, mid-match 12 defenders, TD + confetti). Desktop Chrome: 95%+ frames <= 17ms. Mobile-throttled (DevTools, iPhone 11 class): 95%+ frames <= 33ms. Export Performance trace JSON, parse frame deltas. FAIL on any sustained dip below target.
- [ ] GATE 2 · Input coverage, all 3 paths. Keyboard (WASD + Arrows + Shift + Q/E + Space), touch (responsive mode: stick deadzone 50px, 4 buttons), gamepad (axes deadzone 0.18; buttons 0 sprint, 1 spin, 4 jukeL, 5 jukeR). Each path must fire {x, z, sprint, jukeL, jukeR, spin} in the cmd object and visibly move the player. FAIL on any silent path or wrong binding.
- [ ] GATE 3 · Asset 404 sweep on the LIVE URL, not localhost. Every hardcoded asset (cover.png, sky_pano.png, hero + defender GLBs, music.m4a, all sfx_*, all vo_*) returns 200 with content-length > 0. Screenshot the Network tab. FAIL on any 404, zero-length body, or CORS error.
- [ ] GATE 4 · Asset visual inspection. sky_pano: no banding, no repeated-texture seams, believable at full-sphere wrap, >= 8/10. cover: hero legible, on-brand contrast (no teal/orange), title readable at clamp(14px, 2.6vw, 22px), >= 8/10. GLB renders: no melted geometry, jersey number and helmet decal intact, >= 8/10. FAIL on any score < 8 or any hard artifact.
- [ ] GATE 5 · Copy + VO scan. strings.js: zero em-dashes, zero crutch words, max one "!" per string. Every VO line triggered in-game, transcription accuracy >= 90% against the VO table, tier routing correct (no Tier 3 read on a routine play). Levels: music -18 dBFS, SFX -10 to -12 dBFS, true peak <= -3 dBFS. FAIL on any mumble, mismatch, wrong tier, or clipping.
- [ ] GATE 6 · Feature parity vs plan.md. All verbs fire with frozen numbers (sprint drain 30/s regen 18/s, juke 6u over 0.25s with 0.4s untouchable + 1.2s cooldown, spin 2.0u break + 3s cooldown). Loop verified across 5 full matches: drop, 80u drive, TD +7, golden +3, 4 downs = over, 21+ = MVP, clutch +4% per lost down. v2 layer verified: rank ladder at 7/14/21, hot hand on 2 straight TDs and lost on tackle, crowd surge and legendary each fire at most once. FAIL on any missing verb, wrong number, or broken loop.
- [ ] GATE 7 · Live-URL smoke from 2 networks (WiFi + phone 4G). Load <= 3s to first frame, one full match each, input-to-action latency <= 50ms, restart returns to title, reload-from-cache works, zero console errors. FAIL on any 5xx, timeout > 5s, latency > 100ms, or console error.
- [ ] GATE 8 · Budget proof. Draw calls peak <= 150 with all entities live (12 defenders, 600 confetti instanced, 1200 crowd instanced), per-frame heap delta 0 across a 60s match (no unbounded growth in the trace), devicePixelRatio capped at 1.5. FAIL on any budget exceeded.
- [ ] GATE 9 · Headless regression harness, fresh-context run. 7 asserts: init state, movement integration (z += speed * dt), sprint economy, juke invulnerability + cooldown, tackle = lost down, TD scoring + wave increment, MVP at 21. Plus 3 v2 asserts: rank thresholds, hot hand gain/loss, clip-motion check (P1 assertClipMoves passes for every registered clip). 10/10 required. FAIL on any assert.
- [ ] GATE 10 · Build manifest. public/ structure complete (index.html with viewport meta, game.js, strings.js, logic.js, vendor three.module.js, assets/ full per Gate 3 list), zip < 25 MiB, audio total < 4 MiB, git tag v2.0 created with gates 1-9 results in the message. FAIL on size breach, missing file, or no tag.
- [ ] GATE 11 · Legal + brand scan. No secrets/PII in any source (grep password, key, token, secret, email). No real-world marks (NFL, Nike, named athletes) in cover, sky, GLB textures, or copy. VO is synthetic/licensed, no celebrity voice clone. No third-party analytics or consent-free cookies. Title cleared internally. FAIL on any hit.
- [ ] GATE 12 · Deploy receipt + operator handoff. Receipt lists game_id, deploy timestamp, each gate's result with its proof artifact path, then commit "Deploy v2.0 [gates 1-12 PASS] + receipt", push tag, post live URL + receipt to operator. Ship only on operator approval. FAIL on incomplete receipt or unreachable URL.

Gate order is fixed. The builder agent never signs Gate 9 or Gate 12 on its own output; a fresh-context verify pass runs them.

## Addendum · build amendments (recorded 2026-06-12, conductor decision, surfaced to operator in the ship report)
1. P11 CROWD SURGE amended: reward is full stamina + 3s turbo, copy "CROWD SURGE · FULL TANK". Reason: +500 banked points breaks football score semantics (7/3 increments are the legible currency of the game).
2. Rank copy schema: rankNames array in strings.js instead of four separate keys; copy identical. Lock the array schema.
3. VO table: lines exist as generated announcer wavs wired in game.js AUDIO_FILES (voWelcome/voTouchdown/voMvp/voLastdown/voHothand/voTurnover/voGoldenball); the per-line text lives in design/assets.csv rows. vo_waveclear and vo_chain deferred.
4. Deferred scope (not claimed anywhere): P10 recognition ticker, LEGENDARY MOMENT, waveCleared card, crowd-energy meter label.
5. Ambience: dedicated stadium walla loop generated (sfx_crowd_loop) after hostile review rejected the looped roar stinger; 6th SFX is a recorded deviation from the 5-SFX guideline, justified by the P5 diegetic-audio law.
6. Hot hand now carries a real +8% speed buff (refuter finding: label-only status is fake depth).
