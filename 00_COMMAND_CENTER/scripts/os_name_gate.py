#!/usr/bin/env python3
"""os-name-gate: forces a domain/collision check before a brand/project name ships.
Usage: python3 os_name_gate.py <name>
Checks .com via whois; flags AVAILABLE/TAKEN; prints the manual checklist that must still pass."""
import sys, subprocess, re
if len(sys.argv)<2: print("usage: os_name_gate.py <name>"); sys.exit(2)
name=sys.argv[1].strip().lower(); dom=re.sub(r'[^a-z0-9-]','',name)+".com"
try:
    out=subprocess.run(["whois",dom],capture_output=True,text=True,timeout=20).stdout.lower()
except Exception as e:
    out=""; print(f"whois error: {e}")
avail = bool(re.search(r"no match|not found|no data found|no entries found|status: free", out)) and "registrar:" not in out
print(f"NAME: {name} | DOMAIN: {dom} | .com: {'AVAILABLE (likely)' if avail else 'TAKEN/registered'}")
print("MANUAL CHECKLIST (gate not passed until all yes):")
print("  [ ] no major brand/app/company owns the name (web + app stores)")
print("  [ ] USPTO TESS trademark clear for the category")
print("  [ ] social handles available (IG/TikTok/YT/X)")
print("  [ ] coined/distinctive (not generic) per name-availability memory")
print("  [ ] no collision with an existing OS brand/lane name")
sys.exit(0 if avail else 1)
