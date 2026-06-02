#!/bin/bash
# setup_shoot_folder.sh · scaffold a new shoot folder per PRODUCTION_OS Section 1.1 + 1.3
#
# Usage:
#   ./setup_shoot_folder.sh 2026-06-15 DavisLaw Reset
#   ./setup_shoot_folder.sh 2026-06-22 Sasha FreeCollab
#
# Creates the 9-subfolder skeleton on the working SSD with the locked naming convention.

set -e

# Working SSD path · adjust if your SSD mounts under a different name
WORKING_ROOT="$HOME/SNIPED_PRODUCTION"
# Mounted external SSD example: WORKING_ROOT="/Volumes/SNIPED_HOT/SNIPED_PRODUCTION"

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 YYYY-MM-DD ClientLastName TYPE"
    echo "  TYPE values: Reset, Sprint, OpKit, BrandSystem, FreeCollab,"
    echo "               FreeCommunity, FreeAccess, Personal, ArtSeries,"
    echo "               CulturalDoc, BTSDay"
    echo ""
    echo "Example: $0 2026-06-15 DavisLaw Reset"
    exit 1
fi

DATE=$1
CLIENT=$2
TYPE=$3
YEAR=${DATE:0:4}

# Validate date format
if ! [[ $DATE =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo "ERROR: date must be YYYY-MM-DD format (got: $DATE)"
    exit 1
fi

# Validate type against locked list
VALID_TYPES="Reset Sprint OpKit BrandSystem FreeCollab FreeCommunity FreeAccess Personal ArtSeries CulturalDoc BTSDay"
if ! echo "$VALID_TYPES" | grep -qw "$TYPE"; then
    echo "ERROR: invalid TYPE '$TYPE'"
    echo "Valid: $VALID_TYPES"
    exit 1
fi

SHOOT_ID="${DATE}_${CLIENT}_${TYPE}"
SHOOT_PATH="$WORKING_ROOT/$YEAR/$SHOOT_ID"

if [ -d "$SHOOT_PATH" ]; then
    echo "ERROR: shoot folder already exists at $SHOOT_PATH"
    exit 1
fi

# Create the 9 subfolders
mkdir -p "$SHOOT_PATH"/{00_BRIEF,10_RAW,20_CULLED,30_HEROES,40_SELECTS,50_PROOFS,60_DELIVERY,70_BTS,80_CONTENT,90_NOTES}

# Drop a starter README in each subfolder so the structure documents itself
cat > "$SHOOT_PATH/00_BRIEF/README.md" <<EOF
# ${SHOOT_ID} · 00_BRIEF

Pre-shoot brief, signed contract, model release, mood references.

## To populate
- [ ] Pre-shoot brief email screenshot (sent 24h before)
- [ ] Signed contract PDF (Reset MSA / Collab / Op Kit MSA)
- [ ] Model release if applicable
- [ ] Mood reference frames (3-5 SNIPED archive frames or Pinterest pulls)
- [ ] Wardrobe confirmation (client reply screenshot)
- [ ] Location confirmation (parking, code, contact)
EOF

cat > "$SHOOT_PATH/90_NOTES/post_shoot.md" <<EOF
# ${SHOOT_ID} · post-shoot notes

Captured immediately after the client leaves. 5-10 min.

## Shoot summary
- Date: ${DATE}
- Client: ${CLIENT}
- Type: ${TYPE}
- Frame count (raw):
- Setup used:
- Lighting pattern:
- Wardrobe:
- Protocol surfaced (if Reset / Op Kit):

## What worked
-
-

## What did not work
-
-

## Subject's energy / behavior
-

## Casual referral question (asked on the way out)
-

## Next action
- [ ] Same-day ingest + backup complete
- [ ] Notion · Shoots DB updated
- [ ] BTS Reel cut within 24h
- [ ] Cull tomorrow morning
EOF

# Print the path for piping into other commands
echo "✓ Shoot folder created at:"
echo "  $SHOOT_PATH"
echo ""
echo "Next steps:"
echo "  1. Drop pre-shoot brief screenshot into 00_BRIEF/"
echo "  2. SD card import → 10_RAW/"
echo "  3. Run: sniped_backup '$SHOOT_PATH'"
