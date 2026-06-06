# OS VIDEO EDIT AUTOMATION STANDARD

LOCKED 2026-06-05. **Video editing must be AUTOMATED or EXPLICITLY BLOCKED.** The OS knows how to edit video and assemble the package. The operator is not the editor. A human handoff is acceptable ONLY after every automated route is verified blocked.

## The rule
For any max campaign-film package, the motion/edit layer must resolve to exactly one of:
1. DIRECT_PREMIERE_AUTOMATED
2. ADOBE_VIDEO_MCP_AUTOMATED
3. AFTER_EFFECTS_AUTOMATED
4. CAPCUT_AUTOMATED
5. HYPERFRAMES_PLUS_FFMPEG_AUTOMATED
6. HYBRID_AUTOMATED
7. BLOCKED_AFTER_VERIFICATION (only if 1-6 all fail)

"Human handoff by default" is banned. Generating FCPXML / EDL / FCPXML that Premiere can open counts as a partial automated bridge, not a handoff.

## How the OS decides
Run `os_video_edit_router.py routes` (probes every route, writes OS_VIDEO_EDIT_ROUTE_MATRIX.csv) then `os_video_edit_router.py pick`. Priority: HYBRID > HyperFrames+ffmpeg > After Effects > Adobe video MCP > CapCut > Premiere-direct > BLOCKED.

## Verified machine state (2026-06-05)
| Route | Status | Automation | Verdict |
| --- | --- | --- | --- |
| DIRECT_PREMIERE | BLOCKED | project-file bridge | Premiere 2026 installed, no headless render; FCPXML/EDL bridge instead |
| ADOBE_VIDEO_MCP | AVAILABLE | conditional | quick_cut/video_resize callable, needs cloud upload |
| AFTER_EFFECTS | AVAILABLE | full-auto | aerender headless; needs template/build jsx |
| CAPCUT | BLOCKED | blocked | not installed; 7 doctrine cards, apply inside callable route |
| HYPERFRAMES+FFMPEG | ACTIVE | full-auto | ffmpeg+xfade+HyperFrames, fully local |
| HYBRID | **ACTIVE (SELECTED)** | full-auto | HF+ffmpeg spine + FCPXML/EDL Premiere bridge |

## Proof (credit-free acceptance test)
`os_video_edit_router.py selftest` assembled a 3-clip edit: HyperFrames title card + ffmpeg content clip + HyperFrames end card, two xfade transitions, exported 1280x720 h264 6.00s, plus FCPXML + EDL. Log: OS_VIDEO_EDIT_SELFTEST/VIDEO_EDIT_SELFTEST_LOG.txt. Human handoff required: NO.

## In a real run
- Titles / lower-thirds / kinetic type: HyperFrames render (HTML -> mp4), or After Effects via aerender for heavier motion-graphics.
- Cutting / transitions / pacing / aspect exports (9:16, 16:9, 1:1) / durations (6s, 15s, 30s): ffmpeg (xfade, concat, scale/pad, trim on beat).
- Captions / hook structure / transition feel: apply CapCut + Premiere DOCTRINE cards (the doctrine is callable even though CapCut the app is not).
- Premiere finishing pass (optional, never required): open the auto-generated FCPXML/EDL.
- Adobe video MCP: cloud quick-cut/reframe when an asset is already uploaded.

## Files
os_video_edit_router.py, OS_VIDEO_EDIT_ROUTE_MATRIX.csv, OS_PREMIERE_AUTOMATION_AUDIT.md, OS_AFTER_EFFECTS_AUTOMATION_AUDIT.md, OS_CAPCUT_DOCTRINE_AUDIT.md, OS_VIDEO_EDIT_SELFTEST/.
