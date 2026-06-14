#!/usr/bin/env bash
set -euo pipefail

WORK="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_EDITOR_HANDOFF_001/_v5_work"
FINAL="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_EDITOR_HANDOFF_001/ALMA_REEL_INHOUSE_V5_MOMENT_CUT.mp4"
WEB="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/ALMA_EDITOR_HANDOFF_001/ALMA_REEL_INHOUSE_V5_web.mp4"
LUT="/Users/sniper/alma_lut.cube"

LOGO_OPEN="/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/logo/ALMA_LOVE_wordmark_red.png"
LOGO_CLOSE="/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/05_EXPORTS/DELIVERABLES/ALMA_LOVE_BRAND_KIT/logo/ALMA_LOVE_lockup_SWIM_red.png"

SRC_9509="/Users/sniper/Downloads/IMG_9509.MOV"
SRC_D3320="/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/01_RAW_VIDEO/D94A3320.MP4"
SRC_9541="/Users/sniper/Downloads/IMG_9541.MOV"
SRC_9524="/Users/sniper/Downloads/IMG_9524.MOV"
SRC_D3316="/Users/sniper/AI-Brain-Refinery/ALMA_LOVE_PRODUCTION_001/New Folder With Items/01_RAW_VIDEO/D94A3316.MP4"
SRC_9542="/Users/sniper/Downloads/IMG_9542.MOV"

echo "=== STEP 1: Building segments ==="

echo "--- seg_1: HOOK (IMG_9509, iphone, no transpose) ---"
ffmpeg -y -ss 3.4 -t 1.2 -i "$SRC_9509" \
  -vf "eq=gamma_r=1.03:gamma_b=0.984,scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" \
  -an -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/seg_1.mp4"

echo "--- seg_2: MOVEMENT (D94A3320, canon, transpose=2) ---"
ffmpeg -y -ss 7.6 -t 2.9 -i "$SRC_D3320" \
  -vf "transpose=2,colortemperature=temperature=4500:pl=1,eq=gamma_r=1.0:gamma_b=1.0,scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" \
  -an -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/seg_2.mp4"

echo "--- seg_3: PRODUCT (IMG_9541, iphone, no transpose) ---"
ffmpeg -y -ss 0 -t 1.7 -i "$SRC_9541" \
  -vf "eq=gamma_r=1.03:gamma_b=0.98,scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" \
  -an -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/seg_3.mp4"

echo "--- seg_4: TURN (IMG_9524, iphone, no transpose) ---"
ffmpeg -y -ss 3.3 -t 2.5 -i "$SRC_9524" \
  -vf "colortemperature=temperature=5200:pl=1,eq=gamma_r=1.0:gamma_b=1.0,scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" \
  -an -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/seg_4.mp4"

echo "--- seg_5: TRANSITION (D94A3320, canon, transpose=2) ---"
ffmpeg -y -ss 10.9 -t 1.4 -i "$SRC_D3320" \
  -vf "transpose=2,colortemperature=temperature=4500:pl=1,eq=gamma_r=1.0:gamma_b=1.0,scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" \
  -an -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/seg_5.mp4"

echo "--- seg_6: HERO (D94A3316, canon, transpose=2) ---"
ffmpeg -y -ss 31 -t 3.0 -i "$SRC_D3316" \
  -vf "transpose=2,eq=gamma_r=1.03:gamma_b=0.97,scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" \
  -an -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/seg_6.mp4"

echo "--- seg_7: CLOSE (IMG_9542, iphone, no transpose) ---"
ffmpeg -y -ss 17.8 -t 2.8 -i "$SRC_9542" \
  -vf "colortemperature=temperature=5500:pl=1,eq=gamma_r=1.0:gamma_b=1.0,scale=-2:1920,crop=1080:1920,fps=30,lut3d=${LUT}" \
  -an -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/seg_7.mp4"

echo "=== STEP 2: Writing concat list ==="
cat > "${WORK}/list.txt" << 'LISTEOF'
file 'seg_1.mp4'
file 'seg_2.mp4'
file 'seg_3.mp4'
file 'seg_4.mp4'
file 'seg_5.mp4'
file 'seg_6.mp4'
file 'seg_7.mp4'
LISTEOF

echo "=== STEP 3: Concatenating ==="
ffmpeg -y -f concat -safe 0 -i "${WORK}/list.txt" \
  -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${WORK}/concat.mp4"

echo "=== STEP 4: Brand layer ==="
TOTAL_DUR=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "${WORK}/concat.mp4")
echo "Total duration: ${TOTAL_DUR}s"

CLOSE_START=$(python3 -c "print(max(0, float('${TOTAL_DUR}') - 1.5))")
echo "Close overlay starts at: ${CLOSE_START}s"

ffmpeg -y \
  -i "${WORK}/concat.mp4" \
  -i "$LOGO_OPEN" \
  -i "$LOGO_CLOSE" \
  -filter_complex "\
[1:v]scale=420:-1[open_scaled];\
[open_scaled]format=rgba[open_fmt];\
[2:v]scale=520:-1[close_scaled];\
[close_scaled]format=rgba[close_fmt];\
[0:v][open_fmt]overlay=x=(W-w)/2:y=H*0.74:enable='between(t,0,1.4)',format=yuv420p[v_open];\
[v_open][close_fmt]overlay=x=(W-w)/2:y=H*0.70:enable='between(t,${CLOSE_START},${TOTAL_DUR})',format=yuv420p[v_final];\
[v_final]fade=t=in:st=0:d=0.3:alpha=0[vopen_fade]" \
  -map "[vopen_fade]" \
  -c:v libx264 -crf 19 -pix_fmt yuv420p \
  "${FINAL}" || {
    echo "Brand layer with fade failed, trying simpler approach..."
    ffmpeg -y \
      -i "${WORK}/concat.mp4" \
      -i "$LOGO_OPEN" \
      -i "$LOGO_CLOSE" \
      -filter_complex "\
[1:v]scale=420:-1,format=rgba,fade=t=in:st=0:d=0.3:alpha=1,fade=t=out:st=1.1:d=0.3:alpha=1[open_overlay];\
[2:v]scale=520:-1,format=rgba,fade=t=in:st=0:d=0.4:alpha=1[close_overlay];\
[0:v][open_overlay]overlay=x=(W-w)/2:y=H*0.74:enable='between(t,0,1.4)'[v_with_open];\
[v_with_open][close_overlay]overlay=x=(W-w)/2:y=H*0.70:enable='between(t,${CLOSE_START},${TOTAL_DUR})'[v_final]" \
      -map "[v_final]" \
      -c:v libx264 -crf 19 -pix_fmt yuv420p \
      "${FINAL}"
  }

echo "=== STEP 5: Web version ==="
ffmpeg -y -i "${FINAL}" \
  -vf "scale=-2:1280" \
  -c:v libx264 -crf 23 -movflags +faststart \
  "${WEB}"

echo "=== STEP 6: Verify ==="
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "${FINAL}"
ffprobe -v quiet -show_entries stream=width,height -of csv=p=0 "${FINAL}" | head -1

echo "=== BUILD COMPLETE ==="
