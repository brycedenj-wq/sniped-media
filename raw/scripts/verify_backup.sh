#!/bin/bash
# verify_backup.sh · confirm Hot SSD and Warm HDD copies are bit-identical
# Per PRODUCTION_OS Section 1.5 (verification step before card format)
#
# Usage:
#   ./verify_backup.sh ~/SNIPED_PRODUCTION/2026/2026-06-15_DavisLaw_Reset
#
# Returns:
#   0 = both copies match (safe to format card)
#   1 = mismatch detected (DO NOT FORMAT CARD)

set -e

HOT_ROOT="$HOME/SNIPED_PRODUCTION"
WARM_ROOT="/Volumes/SNIPED_WARM/SNIPED_PRODUCTION"

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 /path/to/shoot/folder"
    exit 1
fi

SOURCE="$1"

if [ ! -d "/Volumes/SNIPED_WARM" ]; then
    echo "ERROR: Warm HDD not mounted"
    exit 1
fi

if [ ! -d "$SOURCE" ]; then
    echo "ERROR: source folder does not exist: $SOURCE"
    exit 1
fi

REL_PATH="${SOURCE#$HOT_ROOT/}"
DEST="$WARM_ROOT/$REL_PATH"

if [ ! -d "$DEST" ]; then
    echo "ERROR: backup destination does not exist: $DEST"
    echo "Run sniped_backup.sh first."
    exit 1
fi

echo "Verifying backup integrity..."
echo "  Source: $SOURCE"
echo "  Dest:   $DEST"
echo ""

# rsync --dry-run --checksum prints any files that differ between source and dest
DIFF=$(rsync -anc --out-format='%n' "$SOURCE/" "$DEST/" | grep -v '/$' || true)

if [ -z "$DIFF" ]; then
    echo "✓ All files match · backup verified"
    echo "✓ SD card from this shoot can now be formatted"
    exit 0
else
    echo "✗ MISMATCH DETECTED · DO NOT FORMAT CARD"
    echo ""
    echo "Files that differ between source and backup:"
    echo "$DIFF"
    echo ""
    echo "Recovery: re-run sniped_backup.sh, then re-verify."
    exit 1
fi
