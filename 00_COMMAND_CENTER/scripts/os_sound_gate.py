#!/usr/bin/env python3
"""
os_sound_gate.py , the SOUND department gate. A campaign film/ad/teaser is not COMPLETE without a sound
decision. (Sound was the one RED lane in the Big Lanes Audit.) Voice via ElevenLabs; music TBD (Suno/Udio).

Checks a proof.json:
  sound_present (bool)             , does the deliverable have VO/music/SFX at all?
  voice_engine ("elevenlabs"/None) , reachable + write-scope key if agent
  script_tagged (bool)            , V3 emotional tags applied at chosen intensity (or N/A for music-only)
  voice_locked (bool)             , brand voice_id locked
  cost_capped (bool)              , minute/credit cap set (for agents)
  customer_facing (bool)          , if true, must be isolated_deploy=True (not personal app)
  isolated_deploy (bool)

  os_sound_gate.py check <proof.json>
  os_sound_gate.py template
"""
import sys, json
def check(p):
    P=json.load(open(p)); fails=[]; oks=[]; warns=[]
    print("SOUND GATE")
    if not P.get("sound_present"): fails.append("no sound at all (VO/music/SFX). A campaign film with no sound is half a deliverable.")
    else: oks.append("sound present")
    ve=P.get("voice_engine")
    if ve: oks.append(f"voice engine: {ve}")
    else: warns.append("no voice engine wired (ElevenLabs not connected) , music-only is acceptable, VO is not")
    if P.get("script_tagged"): oks.append("script emotionally tagged (V3)")
    else: warns.append("script not tagged , VO may sound flat (elv_v3_emotional_tags)")
    if P.get("voice_locked"): oks.append("brand voice_id locked")
    else: warns.append("voice not locked , inconsistent VO across pieces")
    if P.get("customer_facing"):
        if P.get("isolated_deploy"): oks.append("customer-facing agent isolated-deployed")
        else: fails.append("customer-facing agent NOT isolated , do not run from personal app (vagent_commercial_caveat)")
        if not P.get("cost_capped"): fails.append("live agent without cost/minute cap (vagent_cost_gate)")
        else: oks.append("agent cost-capped")
    verdict="PASS" if not fails else "FAIL"
    print(f"\n  VERDICT: {verdict}")
    for o in oks: print(f"   + {o}")
    for w in warns: print(f"   ! {w}")
    for f in fails: print(f"   X {f}")
    return 0 if verdict=="PASS" else 1
def template():
    print(json.dumps({"sound_present":True,"voice_engine":"elevenlabs","script_tagged":True,"voice_locked":True,
        "cost_capped":True,"customer_facing":False,"isolated_deploy":False},indent=2)); return 0
if __name__=="__main__":
    a=sys.argv[1:]
    if len(a)>=2 and a[0]=="check": sys.exit(check(a[1]))
    if a and a[0]=="template": sys.exit(template())
    print(__doc__); sys.exit(1)
