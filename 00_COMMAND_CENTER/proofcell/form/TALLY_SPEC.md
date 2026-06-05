# TALLY FORM SPEC (rebuild in ~2 min; your account; do NOT publish until you decide)

The lowest-friction version. Recreate exactly in Tally (or Google Forms). No domain needed , Tally gives a private share link.

## Form title (internal)
`ACHROMAH` (NAME PENDING brand checklist , do not treat as final). No real name anywhere.

## Welcome / header block (text, not a field)
> **One character. One world. Rendered the same, every time.**
> Most AI imagery is a sea of faces that never repeat. This is the opposite: a single owned character, held across a still and a moving frame. Same face, same light, no one on camera.
> Quiet, monochrome, editorial. Built to repeat, not to chase a moment.

(Optional: upload the hero still + the 4s loop as a header image/embed , the certified assets in `site/assets/`.)

## Fields (in order)
| # | type | label | required | notes |
|---|---|---|---|---|
| 1 | Checkbox (single) | `Send me the breakdown of how this consistent character system was built.` | no | = Rail A (method_interest) |
| 2 | Checkbox (single) | `Tell me if the first frame becomes available as a limited print.` | no | = Rail C (print_interest) |
| 3 | Email | `email` | **yes** | the only required field |
| 4 | Short text | `what do you make? (optional)` | no | = intent (low friction) |
| 5 | Hidden field | `source` , default value `private_link` | hidden | for channel attribution later |

## Button / submit text
`Get the first frames`

## Confirmation message (after submit)
> Got it. You will get one note when there is something worth seeing. No spam.

## Settings
- Collect email responses: ON. Require login: OFF. CAPTCHA: optional.
- **Do NOT** add a custom domain. **Do NOT** use a real-name workspace/brand. Tally free private link only.
- Notifications: to a NON-employer, non-personal-primary inbox (a fresh alias is ideal).
- Close/limit: leave open; you control distribution by where you put the link.

## Export → OS
Tally → Submissions → Export CSV. Then: `python3 os_form_ingest.py <export.csv>` , it auto-maps these exact labels into RESPONSES.csv. Then `python3 os_form_score.py`.
