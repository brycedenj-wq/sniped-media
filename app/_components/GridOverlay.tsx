export function GridOverlay() {
  return (
    <div
      aria-hidden="true"
      className="pointer-events-none absolute inset-0 z-0 hidden overflow-hidden sm:block"
    >
      <div className="mx-auto h-full w-full max-w-7xl px-6 sm:px-8 lg:px-12">
        <div className="relative h-full w-full">
          {Array.from({ length: 11 }).map((_, i) => (
            <span
              key={i}
              className="absolute top-0 bottom-0 w-px bg-foreground/[0.06]"
              style={{ left: `${((i + 1) * 100) / 12}%` }}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
