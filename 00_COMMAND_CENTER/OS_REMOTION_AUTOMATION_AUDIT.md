# OS REMOTION AUTOMATION AUDIT

> Surveyed read-only 2026-06-06. Status: **PREFERRED-PENDING** (source present, not scaffolded).

## What exists
- `~/remotion` = the official Remotion monorepo (source). `node_modules` empty at root -> not installed/usable as-is.
- Remotion = programmatic video via React: `useCurrentFrame()` + `interpolate()` define every frame; render to MP4/WebM/GIF via CLI, browser Studio, or AWS Lambda.

## Activation (smallest proof, no spend)
1. In a sandbox dir: `npx create-video@latest` (scaffolds a project; downloads packages).
2. `npx remotion render` on the default comp -> a few-second MP4. That is the ACTIVE proof (local, no cloud, no credits).
3. (Optional) `npx remotion studio` for live browser preview.

## Capability
- `interpolate(frame,[0,30],[0,1])` = the time->value primitive for all animation.
- `<Sequence from={60} durationInFrames={90}>` = declarative time-shifted sub-scenes.
- `staticFile()` + `inputProps` = one template, N data-driven variants (the strength: data-driven motion graphics).
- `@remotion/lambda` = parallel cloud render for long/4K (cost; defer).

## Remotion vs HyperFrames vs AE (titles decision)
- **HyperFrames**: HTML/CSS/GSAP -> deterministic MP4. Best when you want web/design-tool authoring and alpha overlays. Already the HYBRID title spine.
- **Remotion**: React + data. Best when titles/cards are **data-driven** (N variants from a dataset) or need React component reuse.
- **AE**: true motion-graphics depth (expressions, mattes, native effects) when code-defined isn't enough.
Order for titles: HyperFrames (proven spine) -> Remotion (data-driven) -> AE (depth). All three can replace AE for *simple* titles; AE wins for complex MG.

## License note
Free for individuals/small; **commercial license required** for company use. Flag before any for-profit deployment.

## Honest boundary
Not ACTIVE until a local `npx remotion render` produces an MP4. Cards extracted; route slot #4 (programmable).
