#!/bin/bash
# bridge_check.sh - verify + repair the Premiere and After Effects MCP bridges.
# Run at the start of any session:  ! bash 00_COMMAND_CENTER/scripts/bridge_check.sh
# Repairs the temp-dir symlink (reboot-safe), confirms CEP debug mode, and live-pings both bridges.

PASS="PASS"; FAIL="FAIL"
echo "===== ALMA / SNIPED BRIDGE CHECK ====="
TMP="${TMPDIR%/}"

# --- 1. CEP PlayerDebugMode (unsigned panels need this = 1) ---
dbg_ok=1
for v in 9 10 11 12; do
  val=$(defaults read com.adobe.CSXS.$v PlayerDebugMode 2>/dev/null || echo 0)
  [ "$val" != "1" ] && dbg_ok=0 && echo "  CSXS.$v PlayerDebugMode=$val (will set)" && defaults write com.adobe.CSXS.$v PlayerDebugMode 1 2>/dev/null
done
[ "$dbg_ok" = "1" ] && echo "CEP PlayerDebugMode: $PASS (panels allowed to load)" || echo "CEP PlayerDebugMode: set to 1 (relaunch the Adobe app for it to take)"

# --- 2. Repair Premiere bridge temp dir + symlink (server uses /tmp, panel uses TMPDIR) ---
mkdir -p "$TMP/premiere-mcp-bridge"
ln -sfn "$TMP/premiere-mcp-bridge" /tmp/premiere-mcp-bridge
echo "Premiere bridge dir: $TMP/premiere-mcp-bridge"
echo "  /tmp symlink -> $(readlink /tmp/premiere-mcp-bridge)"

# --- 3. Ensure AE bridge dir ---
mkdir -p "$HOME/Documents/ae-mcp-bridge"
echo "AE bridge dir: $HOME/Documents/ae-mcp-bridge"

# --- 4. Live-ping Premiere (panel must be OPEN to consume) ---
PB="$TMP/premiere-mcp-bridge"; ID="chk$$"
printf '%s' '(function(){try{return JSON.stringify({ok:true,v:app.version});}catch(e){return JSON.stringify({ok:false,e:String(e)});}})()' > "$PB/cmd_${ID}.jsx"
prem=$FAIL
for i in $(seq 1 20); do
  if [ -f "$PB/res_${ID}.json" ] || [ ! -f "$PB/cmd_${ID}.jsx" ]; then prem=$PASS; break; fi
  perl -e 'select(undef,undef,undef,0.25)'
done
rm -f "$PB/cmd_${ID}.jsx" "$PB/res_${ID}.json" 2>/dev/null
echo "PREMIERE bridge live-ping: $prem"
[ "$prem" = "$FAIL" ] && echo "  -> Open Premiere panel: Window > Extensions > MCP Bridge (it auto-starts since the dir exists)."

# --- 5. Live-ping AE (panel must be OPEN; auto-runs) ---
AE="$HOME/Documents/ae-mcp-bridge"
before=$(stat -f %m "$AE/ae_mcp_result.json" 2>/dev/null || echo 0)
printf '%s' '{"command":"getProjectInfo","args":{},"status":"pending"}' > "$AE/ae_command.json"
ae=$FAIL
for i in $(seq 1 24); do
  after=$(stat -f %m "$AE/ae_mcp_result.json" 2>/dev/null || echo 0)
  st=$(grep -o '"status"[^,}]*' "$AE/ae_command.json" 2>/dev/null)
  if [ "$after" != "$before" ] || echo "$st" | grep -q "completed"; then ae=$PASS; break; fi
  perl -e 'select(undef,undef,undef,0.25)'
done
echo "AFTER EFFECTS bridge live-ping: $ae"
[ "$ae" = "$FAIL" ] && echo "  -> Open AE panel: Window > Extensions > MCP Bridge Auto (Auto-run stays ON)."

echo "===== END (Premiere=$prem  AE=$ae) ====="
