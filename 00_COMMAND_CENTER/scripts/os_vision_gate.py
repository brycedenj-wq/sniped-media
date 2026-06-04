#!/usr/bin/env python3
"""os-vision-reject-gate: gate any generated frame/video/product-shot/composite before it ships.
Usage: os_vision_gate.py <image_or_video_path>
Vision cannot run inside a bash hook, so this prints the binding checklist + emits the review
contract. The actual review: the model Reads the asset and scores each item (see os-vision-reject-gate skill).
Exit 0 = checklist emitted (review still required); exit 1 = file missing."""
import sys, os
if len(sys.argv)<2 or not os.path.exists(sys.argv[1]):
    print("VISION GATE: file missing , cannot ship."); sys.exit(1)
f=sys.argv[1]
print(f"VISION REJECT-GATE for: {os.path.basename(f)}")
print("Model MUST Read the asset and score each (any hard-fail = REJECT, do not ship):")
for item in [
 "SLOP: generic AI smear, mushy detail, over-smoothing -> beat-source or reject",
 "HANDS: correct fingers/joints/count, no fusion/extra digits",
 "SKIN: melanin-rich rendered true (no ashy/grey/green), texture not plastic",
 "CLOTHING PHYSICS: drape/seams/folds plausible, no melting/impossible fabric",
 "TEXT ARTIFACTS: any on-image text is real words, not garbled glyphs (or remove)",
 "IDENTITY CONSISTENCY: matches the CRS across frames (no drift)",
 "BRAND CONSISTENCY: v3 LUXURY register, no teal/orange, on-palette",
 "COPYRIGHT/LIKENESS: owned character only, no real-celebrity likeness (legal/ban risk)",
 "BEAT-SOURCE: does it beat an honest camera frame? if not, it fails",
]:
    print(f"  [ ] {item}")
print("VERDICT REQUIRED: SHIP / FIX / REJECT. Log a REJECT to the error dashboard.")
