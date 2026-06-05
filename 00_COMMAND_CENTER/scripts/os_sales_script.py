#!/usr/bin/env python3
"""
os_sales_script.py , the sales script library (VIB DM, discovery, objection, decline).

Doctrine: WWP (win without pitching, sell expertise), intel_trust_equation (low self-orientation),
Mom Test (talk about their problem), feedback_vib_outreach, feedback_referral_handling. Drafts only,
never auto-send; faceless-safe.

  os_sales_script.py dm        , the VIB cold/warm DM frame
  os_sales_script.py discovery , the discovery-call frame (diagnose before prescribe)
  os_sales_script.py objection , price/scope objection responses
  os_sales_script.py decline   , clean decline (protect positioning)
"""
import sys
S={
"dm":["VIB DM (soft-opener + post-language callback; draft, never auto-send):",
 " 1 Soft opener that references THEIR specific work/post (not about you).",
 " 2 One observation that shows you see what they're building (trust: intimacy).",
 " 3 A single relevant value line (the outcome you create), no pitch, no link.",
 " 4 Low-friction ask: a question about THEIR goal, not a meeting demand.",
 " Mom Test: ask about their problem/past behavior, not 'would you buy'."],
"discovery":["DISCOVERY (replace presentation with conversation; diagnose before prescribe):",
 " 1 Diagnose: what's the real outcome they need? what's it worth? what's the cost of not?",
 " 2 Reflect the problem back in their words (trust).",
 " 3 Only then prescribe: present BEST option first (anchor), then BETTER (target).",
 " 4 Proof before price; premium = insurance. Trade scope, never price."],
"objection":["OBJECTION (price/scope):",
 " 'Too expensive' -> reframe to value/outcome + premium-as-insurance; if real, REDUCE scope, hold price.",
 " 'Can you do it cheaper' -> 'I can do LESS for less' (scope lever), never discount the number.",
 " 'Send me your rates' -> 'Happy to , first, what outcome are you trying to hit?' (diagnose first)."],
"decline":["DECLINE (protect positioning, WWP):",
 " 'This isn't the right fit for what you need , I'd point you to someone better suited.'",
 " Decline off-lane / price-shopper / identity-exposing work cleanly. Don't be precious; trade scope or refer."],
}
def main():
    k=sys.argv[1] if len(sys.argv)>1 else ""
    if k in S: [print(x) for x in S[k]]; return 0
    print("scripts: "+", ".join(S)); return 1
if __name__=="__main__": sys.exit(main())
