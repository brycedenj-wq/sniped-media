type SectionMarkerProps = {
  n: string;
  label: string;
  tone?: "light" | "dark";
};

export function SectionMarker({
  n,
  label,
  tone = "light",
}: SectionMarkerProps) {
  const base =
    tone === "light" ? "text-muted border-border" : "text-background/60 border-background/20";

  return (
    <div
      className={`flex items-center gap-4 border-b pb-3 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase tabular-nums ${base}`}
    >
      <span>§ {n}</span>
      <span className="h-px flex-1 bg-current opacity-30" />
      <span>{label}</span>
    </div>
  );
}
