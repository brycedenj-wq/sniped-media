type TextureFallbackProps = {
  baseColor: string;
};

// Renders when the AI texture image hasn't been dropped in yet.
// Layered radial gradients give the section visual depth without
// looking like a flat CSS placeholder.
export function TextureFallback({ baseColor }: TextureFallbackProps) {
  return (
    <div
      aria-hidden="true"
      className="absolute inset-0"
      style={{
        background: `
          radial-gradient(ellipse at 30% 20%, rgba(255, 255, 255, 0.18), transparent 55%),
          radial-gradient(ellipse at 70% 80%, rgba(0, 0, 0, 0.45), transparent 65%),
          radial-gradient(ellipse at 50% 50%, ${baseColor}, ${baseColor})
        `,
      }}
    />
  );
}
