#!/bin/zsh
# Extract labeled per-beat frames from the 4K master v2 (~30s, new edit order) for the QA harness.
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
MASTER="ALMA_LOVE_FINAL_4K_MASTER.mp4"
OUT="qa_frames"
rm -rf "$OUT"; mkdir -p "$OUT"
F() { ffmpeg -nostdin -loglevel error -y "$@"; }
beats=(
 "beat01_dice_HOOK:0.65"
 "beat02_hero_open:2.9"
 "beat03_walk:5.3"
 "beat04_cherry_macro:6.8"
 "beat05_incar_DRIVING:8.5"
 "beat06_gas:11.1"
 "beat07_plural_club:13.55"
 "beat08_mirror_product:15.1"
 "beat09_solitaire:16.8"
 "beat10_hood_product:18.5"
 "beat11_establish:20.2"
 "beat12_gamble_card:22.2"
 "beat13_night_payoff:25.2"
 "beat14_endcard:28.7"
)
for b in $beats; do
  name=${b%%:*}; tc=${b#*:}
  F -ss "$tc" -i "$MASTER" -frames:v 1 -vf "scale=1280:-1" "$OUT/${name}.png"
done
# tight crops of the product-critical beats
F -ss 6.8 -i "$MASTER" -frames:v 1 -vf "crop=in_w/2:in_h/2:in_w/4:in_h/4,scale=1000:-1" "$OUT/beat04_cherry_CROP.png"
F -ss 8.5 -i "$MASTER" -frames:v 1 -vf "crop=in_w/1.6:in_h/1.6:in_w/5:in_h/5,scale=1000:-1" "$OUT/beat05_incar_CROP.png"
magick montage "$OUT"/beat0*.png "$OUT"/beat1[0-4]*.png -tile 4x4 -geometry 360x203+3+3 -background black "$OUT/_CONTACT_SHEET.png" 2>/dev/null || true
echo "FRAMES: $(ls "$OUT"/*.png | wc -l | tr -d ' ') -> $OUT"