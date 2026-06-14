#!/bin/zsh
set -e
cd /Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_MARGIELA_SAVE_001/06_FULL_CUT
MASTER="ALMA_LOVE_PHOTOREAL_4K_MASTER.mp4"
OUT="qa_frames"; rm -rf "$OUT"; mkdir -p "$OUT"
F(){ ffmpeg -nostdin -loglevel error -y "$@"; }
beats=(
 "beat01_dice_REALmacro_HOOK:0.65"
 "beat02_establish_photoreal:2.6"
 "beat03_hero_photoreal:5.3"
 "beat04_cherry_REALmacro:7.3"
 "beat05_walk_photoreal:9.1"
 "beat06_gas_photoreal:11.4"
 "beat07_plural_club:13.8"
 "beat08_solitaire:16.3"
 "beat09_gamble_card:18.6"
 "beat10_night_payoff:21.5"
 "beat11_endcard:24.9"
)
for b in $beats; do
  name=${b%%:*}; tc=${b#*:}
  F -ss "$tc" -i "$MASTER" -frames:v 1 -vf "scale=1280:-1" "$OUT/${name}.png"
done
F -ss 5.3  -i "$MASTER" -frames:v 1 -vf "crop=in_w/1.8:in_h/1.4:in_w/4.5:in_h/5,scale=1000:-1" "$OUT/beat03_hero_CROP.png"
F -ss 11.4 -i "$MASTER" -frames:v 1 -vf "crop=in_w/2:in_h/2:in_w/4:in_h/4,scale=1000:-1" "$OUT/beat06_gas_CROP.png"
magick montage "$OUT"/beat0*.png "$OUT"/beat1[0-1]*.png -tile 4x3 -geometry 360x203+3+3 -background black "$OUT/_CONTACT_SHEET.png" 2>/dev/null || true
echo "FRAMES: $(ls "$OUT"/*.png | wc -l | tr -d ' ')"