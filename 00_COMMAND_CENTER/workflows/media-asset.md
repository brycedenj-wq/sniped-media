# Workflow: Generate a media asset

For images, video, or audio used in campaigns or Remotion compositions.

1. **Define the brief** — format, aspect ratio, duration, style, target platform.
2. **Generate** (MCP, when connected):
   - Image/video/audio → **Higgsfield** (`generate_image` / `generate_video` /
     `generate_audio`); use `virality_predictor` to sanity-check clip hooks.
   - Edits (bg removal, vectorize, color, quick-cut/resize) → **Adobe / Firefly**.
   - Design frames / templates → **Figma**.
   - Local source media? Use the server's upload widget — remote MCP tools can't
     read chat attachments.
3. **Bring into the app** — drop finals into `public/` or reference from a
   Remotion composition in `video/`.
4. **Compose / render** — preview at `/studio` or `npm run video:preview`;
   render with `npm run video:render` (needs `remotion.media` egress or a
   system Chrome).
5. **Track** — log the asset in Notion/Airtable if used for the project.
