#!/bin/bash
# sniped_backup.sh · mirror a shoot folder from Hot SSD to Warm HDD
# Per PRODUCTION_OS Section 1.5 (3-2-1 backup discipline)
#
# Usage:
#   ./sniped_backup.sh ~/SNIPED_PRODUCTION/2026/2026-06-15_DavisLaw_Reset
#   ./sniped_backup.sh ~/SNIPED_PRODUCTION/2026/   (mirror entire year)
#   ./sniped_backup.sh                              (mirror everything)
#
# To install as a shell function (recommended):
#   1. Copy this script to ~/bin/sniped_backup
#   2. chmod +x ~/bin/sniped_backup
#   3. Add to ~/.zshrc:
#      export PATH="$HOME/bin:$PATH"
#      alias snibak='sniped_backup'
#   4. Reload: source ~/.zshrc
#   5. Run: snibak ~/SNIPED_PRODUCTION/2026/2026-06-15_DavisLaw_Reset

set -e

# Adjust these paths to match your setup
HOT_ROOT="$HOME/SNIPED_PRODUCTION"
WARM_ROOT="/Volumes/SNIPED_WARM/SNIPED_PRODUCTION"

# Default to mirroring everything if no argument given
SOURCE="${1:-$HOT_ROOT}"

# Verify Warm HDD is mounted
if [ ! -d "/Volumes/SNIPED_WARM" ]; then
    echo "ERROR: Warm HDD not mounted at /Volumes/SNIPED_WARM"
    echo "Plug in the 8TB external drive labeled SNIPED_WARM and try again."
    exit 1
fi

# Verify source exists
if [ ! -d "$SOURCE" ]; then
    echo "ERROR: source folder does not exist: $SOURCE"
    exit 1
fi

# Calculate relative path from HOT_ROOT
REL_PATH="${SOURCE#$HOT_ROOT/}"
DEST="$WARM_ROOT/$REL_PATH"

# Create destination parent if needed
mkdir -p "$(dirname "$DEST")"

echo "═══════════════════════════════════════════"
echo "SNIPED backup · $(date +%Y-%m-%d_%H:%M:%S)"
echo "Source: $SOURCE"
echo "Dest:   $DEST"
echo "═══════════════════════════════════════════"
echo ""

# Run rsync · archive mode + verbose + human-readable + progress
# --delete is intentionally OMITTED. We do not want backup to mirror deletions.
# If you want to PURGE a shoot from Warm, do it manually with explicit rm.
rsync -avh --progress "$SOURCE/" "$DEST/"

echo ""
echo "═══════════════════════════════════════════"
echo "✓ Backup complete"
echo "  Source size: $(du -sh "$SOURCE" | cut -f1)"
echo "  Dest size:   $(du -sh "$DEST" | cut -f1)"
echo "═══════════════════════════════════════════"
echo ""
echo "Next: verify with 'verify_backup.sh $SOURCE'"
