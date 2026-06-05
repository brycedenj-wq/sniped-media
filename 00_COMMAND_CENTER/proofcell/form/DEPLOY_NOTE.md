# DEPLOY NOTE , 3 ready versions (you wire one manually; nothing hosted by the OS)

The form is COMPLETE in three forms. Pick ONE when you decide to test. Each touches YOUR account , that is why the OS stops here.

## Version 1 , TALLY (lowest friction, recommended)
Rebuild from `TALLY_SPEC.md` (2 min). Tally gives a private link. No domain, no HTML hosting.

## Version 2 , STATIC + FORMSPREE (use the built HTML)
`site/index.html` is ready. To make it collect:
1. Create a Formspree (or Basin/Tally-embed) form in YOUR account , get the endpoint URL.
2. In `site/index.html`, replace `action="REPLACE_WITH_YOUR_FORM_ENDPOINT"` with that URL. (That is the ONLY edit.)
3. Host `site/` (Version 3).

## Version 3 , NETLIFY / VERCEL DROP (host the static site privately)
- The deployable unit is the **`site/`** folder (index.html + assets + vercel.json). `netlify.toml` publishes it.
- Netlify: drag `site/` onto app.netlify.com/drop (your account). Vercel: `vercel deploy` in `site/`.
- Use the auto-generated `*.netlify.app` / `*.vercel.app` URL , **do NOT add a custom domain**, do NOT use a real-name team.

## After responses come in
`python3 os_form_ingest.py <tally_or_formspree_export.csv>` -> appends to RESPONSES.csv (dedup by email).
`python3 os_form_score.py` -> SCORE.md (A/C/both/source/intent + keep/kill/scale verdict).

## Held at your line (OS will not do these)
Creating any account · hosting · adding an endpoint · buying a domain · finalizing the name · posting/sharing the link.
