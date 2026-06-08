# OS FINISHING DEPARTMENT · DASHBOARD

Live board for the finishing department. Doctrine: `OS_FINISHING_DEPARTMENT_STANDARD.md`. Updated per finishing pass.

Last updated: 2026-06-07.

---

## Department status

| Piece | State | Location |
|---|---|---|
| Standard (doctrine) | ✅ written | `00_COMMAND_CENTER/OS_FINISHING_DEPARTMENT_STANDARD.md` |
| Dashboard (this) | ✅ written | `00_COMMAND_CENTER/OS_FINISHING_DEPARTMENT_DASHBOARD.md` |
| `os_visual_selects_engine.py` (Mode B) | ✅ written + tested | `00_COMMAND_CENTER/scripts/` |
| `os_finish_plan.py` (handoff) | ✅ written + tested | `00_COMMAND_CENTER/scripts/` |
| `os_finish_gate.py` (excellence gate) | ✅ written + tested | `00_COMMAND_CENTER/scripts/` |

---

## Tool route readiness (premium stack)

| Tool | Status | Proof / blocker |
|---|---|---|
| Premiere (premiere-pro MCP, ~300 tools) | ✅ LIVE, source-audited clean | `~/Adobe_Premiere_Pro_MCP` (hetpatel-11). Bridge = stdio + `/tmp/premiere-mcp-bridge`. |
| Premiere `apply_lut` / `color_correct` / `apply_effect` | 🔴 BLOCKED (2026-06-07 retest) | QE DOM effect engine empty: apply_lut "Could not apply Lumetri", apply_effect "Effect not found", list_available_effects `[]`, color_correct returns true w/ empty changes. Fix = relaunch Premiere to re-init QE DOM. |
| Premiere `export_sequence` / `add_to_render_queue` | 🔴 BLOCKED (2026-06-07 retest) | `exported:true` but NO file on disk after 60s+ (AME running, batch never started). Fix = open AME Queue panel + Start Queue, or relaunch AME. |
| After Effects MCP | 🟡 PARTIAL | `create-composition` works; keyframe Position/Scale/Rotation/Opacity works. BLOCKED: no import-footage/add-layer, no render/save. |
| Adobe Cloud (remove-bg / select-subject) | ✅ LIVE | proven via block-upload handshake. |
| Higgsfield | ✅ LIVE | balance present, Plus plan; `nano_banana_2` world backplate proven. |
| ElevenLabs | 🟡 PARTIAL | `text_to_sound_effects` ✅ free; `compose_music` 402 paid-gated → synth bed. |
| Figma | ✅ LIVE | Bryce pro; review boards. |
| Blender | ✅ LIVE | scene control proven. |
| ffmpeg | ✅ LIVE | assembly/export spine + per-frame animated blur (fallback only). |
| Chat Video Pro (CEP) | ✅ operator-side | inside Premiere; NOT MCP-drivable; grade/VFX/B-roll human-in-the-loop route. |

---

## Active jobs

### ALMA LOVE COMMERCIAL · "Deadpan Summer" — MODE B
- **Current internal deliverable:** V4.2 (graded + IG-mastered) — `ALMA_LOVE_COMMERCIAL_V4_2_HERO.mp4` (28s), `_V4_2_15s.mp4` (17.6s), `_V4_2_6s_hook.mp4` (7.7s). All 1080x1920, brand LUT, -14 LUFS.
- **Route:** ffmpeg + brand LUT (Premiere render/effects blocked this session — see blocker log).
- **Package:** `05_EXPORTS/FINISHING_PASS_001/V4_2_PACKAGE/` (gate scorecard, blocker log, finishing summary, review board, Premiere handoff).
- **Gate:** 23/33, checklist 6/7 YES. **Single hard blocker = tracked plate blur (D94A3308 ~16-17.5s).** NOT client-deliverable until cleared.
- **Selects:** locked (`ALMA_LOVE_V4_1_EDL.csv`, 16 beats), unchanged.
- **Next:** complete tracked plate blur (AE mask) -> re-score -> client review.

---

## Standing queue (future modes)

- **Mode A first job:** any interview/testimonial/UGC-with-voice → Story Cutter + silence-removal route. Not yet exercised.
- **Premiere automated-finishing proof:** run the smallest-safe `apply_lut` + `export_sequence` test on the Alma sequence to convert the 🟡 RE-TEST rows to ✅ or a documented blocker.

## Tooling candidates to evaluate (2026-06-07)
- **yumehiko/ae-agent-skills** (cloned to ~/AI-Brain-Refinery/ae-agent-skills): CLI/script control of After Effects via a coding agent (compositions, expressions, Essential Properties, JSON->comp). CANDIDATE to UNBLOCK the AE finishing route (AE-MCP has no import/render this session). Evaluate + wire after current AI-max build. Author note: good for repetitive ops + applying known expressions, not for "feel" of motion.
- Context: Composio "CLI tools for Claude Code" (ripgrep/ffmpeg/gh/tmux/lazygit/fzf) + @adobe/aio-cli installed. ripgrep already wired for Gemini lane.
- Do NOT git-add the cloned tool repos in the project root (ae-agent-skills, skills, impeccable, claude-obsidian, codex-plugin-cc, etc.) — they are external tooling, not OS content.
