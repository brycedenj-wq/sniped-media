# soul_id_op_refs · BASEPLATE concept film Soul ID reference set

**Purpose:** collect 5 to 20 face reference photos for training the Higgsfield Soul ID `op`. Used for identity-anchored generation on BASEPLATE concept film Shots 1 and 3 and forward motion (Shots 2 and 4).

**Status:** awaiting photos as of 2026-05-28.

---

## Rules

- Personal source photos are gitignored (`*.png / *.jpg / *.jpeg / *.heic / *.webp / *.gif / *.tif / *.tiff / *.bmp / *.raw`). They never enter the repo's history.
- Once Soul training completes, the soul reference ID + the balance-change receipt are recorded in `00_COMMAND_CENTER/concept_film_v1/soul_id_op_training_receipt.md` (committable).
- The dir itself + this README + the .gitignore are tracked so the audit trail of "Soul `op` exists and lives at <ref_id>" is in the repo.

## Photo guidance (per the Higgsfield Soul training skill)

- 5 to 20 face photos.
- Varied angles: front, three-quarter, profile, slight tilt.
- Varied lighting: natural, indoor, low-key (matches BASEPLATE register).
- No sunglasses. Eyes visible.
- Mix of framings: a few close-ups (head + shoulders), a few mediums (torso up), one or two full.
- No filters that distort the face.
- Recent photos preferred over older ones.

## Workflow

1. Drop 5 to 10 face photos in this directory. AirDrop from phone works; drag-and-drop into Finder works.
2. Tell Claude "photos are in" or list the filenames.
3. Claude runs `higgsfield soul-id create --name op --soul-2 --image <path> ...` (CLI auto-uploads each).
4. Claude captures the returned soul reference ID and runs `higgsfield soul-id wait <id>` until training finishes (silent polling, typically 5 to 15 minutes).
5. Claude writes the training receipt (`soul_id_op_training_receipt.md` one directory up) with the ref ID, training cost (balance change), variant (`--soul-2`), and timestamp.
6. After training, the source photos can be deleted from this directory (the Soul ref lives in Higgsfield's account; the photos are not needed locally for future generation). Or kept for re-training if Higgsfield's account loses them.

## After training

The Soul ref ID is used downstream as `--soul-id <id>` on every Soul-aware Higgsfield generation, primarily:

- `higgsfield generate create text2image_soul_v2 --prompt "..." --soul-id <id> --aspect_ratio 16:9 --resolution 2k`
- `higgsfield generate create soul_cinematic --prompt "..." --soul-id <id> --aspect_ratio 16:9`

Re-running Shot 1 + Shot 3 with `--soul-id <op_id>` produces identity-anchored versions (the operator IS Bryceden Jones, not archetypal).
