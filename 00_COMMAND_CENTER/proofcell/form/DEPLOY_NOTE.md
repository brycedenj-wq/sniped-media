# FORM , how to make it collect (operator step only; nothing public yet)

The form (index.html) is COMPLETE: copy, fields, asset pair, styling. It currently collects NOTHING (action = placeholder). To turn it into a live private proof loop, YOU do one of these , I cannot, because each touches an account/identity:

1. **Lowest friction:** recreate the form in Tally or Google Forms (paste the copy + the 2 checkboxes + email + optional intent). Get a private share link. No domain, no real name in the form title (use ACHROMAH, pending).
2. **Use this HTML:** add your OWN form endpoint (Formspree/Basin/Tally embed) into `action="..."`, then host the folder privately (Netlify drop / Vercel / a hosted file). Endpoint + host = your account.

Constraints to hold when you do it: no real-name metadata, no employer email, no domain purchase, name stays ACHROMAH (pending brand checklist), private link only (no posting/ads).

Record every response in RESPONSES.csv (one row each). The columns map straight to Rail A (method_interest) and Rail C (print_interest).
