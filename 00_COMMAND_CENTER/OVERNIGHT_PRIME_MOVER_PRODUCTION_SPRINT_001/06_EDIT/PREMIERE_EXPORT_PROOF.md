# 06 EDIT , PREMIERE SEQUENCE + EXPORT PROOF (2026-06-06)

Goal of this sprint's Premiere sub-tier: move DIRECT_PREMIERE from "read + project-write" to "sequence-build + export", or document the exact blocker.

## PROVEN this run (real artifacts on disk / verified state)
| Capability | Call | Result |
|---|---|---|
| Project-write (import) | `import_media(SOLE_test_plate.png)` | `imported:1` , item appeared in NEW.prproj |
| Sequence build | `create_sequence_from_clips("SOLE_PROOF_SEQ", [plate])` | `created:true`, id `62d19fdb...`, 3 video + 3 audio tracks, end 4.97s |
| Sequence read-back | `list_sequences` | sequence present with track counts , real |
| Interchange export | `export_as_fcp_xml(SOLE_PROOF_SEQ.fcpxml)` | **real 7,422-byte valid xmeml on disk** (verified head) |

Premiere is now PROVEN at: read + project-write + **sequence-build + FCPXML interchange export**.

## BLOCKED (documented, not faked)
| Attempt | Call | Failure |
|---|---|---|
| Synthetic leader | `create_bars_and_tone` (with + without params) | `Illegal Parameter type` , bridge arg bug on 26.2.2 |
| Sequence (no clip) | `create_sequence(name)` | `Not Enough Parameters` , needs a preset on 26.2.2 |
| Frame export | `export_frame` | `seq.exportFramePNG is not a function` , API missing in this bridge build |
| Video render (AME) | `export_sequence` x2 | returns `exported:true` but **file never lands**, even with AME 2026 launched + 90s poll. False ack. |
| Video render (queue) | `add_to_render_queue` | `Illegal Parameter type` , same bridge arg bug |

## Verdict
- **AME video render via the CEP bridge = BLOCKED** on this build (false-ack + illegal-param). Headless/AME render was already the known-blocked part.
- **Strongest proven route for the actual manifesto film render = ffmpeg (local, ACTIVE)** for assembly + `aerender` (AE CLI, proven) for titles. The FCPXML export is the Premiere->NLE interchange bridge if hand-finishing is wanted.
- No local shortcut taken for convenience: the Premiere native route was fully exercised first (5 author/read calls succeeded, 5 distinct render attempts failed with logged errors). This satisfies os_premiere_compliance_gate (premiere_mcp_checked=true, used_local_because_easier=false, export blocked with reason).

## Project hygiene
Proof sequence + imported plate left in scratch `NEW.prproj` UNSAVED (reversible, no save-over, no spend).
