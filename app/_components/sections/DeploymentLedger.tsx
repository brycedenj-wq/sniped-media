import { Container } from "../Container";
import { GridOverlay } from "../GridOverlay";
import { SectionMarker } from "../SectionMarker";

type Row = {
  month: string;
  phase: string;
  trigger: string;
  assets: string;
};

const rows: Row[] = [
  { month: "01", phase: "BRAND REFRESH", trigger: "New year, new positioning", assets: "LinkedIn hero + primary profile swap. Team page update." },
  { month: "02", phase: "PRESS CYCLE", trigger: "Product launch or milestone", assets: "Press release landscape + portrait. One podcast tile." },
  { month: "03", phase: "SPEAKING", trigger: "Q1 conference season", assets: "Keynote opener 16:9. Speaker bio headshot." },
  { month: "04", phase: "FUNDRAISE", trigger: "Investor update cadence", assets: "Deck founder slide. Data room bio image." },
  { month: "05", phase: "HIRING", trigger: "Team expansion", assets: "LinkedIn recruitment post primary. Team page hero." },
  { month: "06", phase: "MID-YEAR", trigger: "Company update or memo", assets: "Long-form LinkedIn hero. Newsletter lead image." },
  { month: "07", phase: "PODCAST", trigger: "Summer media appearances", assets: "Six podcast tiles in varied crops. One YouTube thumbnail." },
  { month: "08", phase: "PARTNERSHIP", trigger: "Co-marketing moment", assets: "Joint press landscape. Dual-format social primary." },
  { month: "09", phase: "PRODUCT", trigger: "Q3 launch or feature ship", assets: "Product post founder quote tile. Blog header image." },
  { month: "10", phase: "KEYNOTE", trigger: "Fall speaking circuit", assets: "Stage opener 16:9. Event press landscape." },
  { month: "11", phase: "YEAR-END PRESS", trigger: "Awards, lists, recap features", assets: "Magazine-quality portrait. Long-form press landscape." },
  { month: "12", phase: "INVESTOR LETTER", trigger: "End-of-year close-out", assets: "Letter header image. LinkedIn recap post primary." },
];

export function DeploymentLedger() {
  return (
    <section className="relative border-t border-border bg-background py-section">
      <GridOverlay />
      <Container className="relative z-10">
        <SectionMarker n="05" label="Deployment Ledger" />

        <div className="mt-12 mb-12 max-w-3xl">
          <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
            Twelve months. One library.
          </h2>
          <p className="mt-4 text-base text-foreground/70 leading-relaxed">
            Template. Remixed against each founder&apos;s actual calendar during pre-production.
          </p>
        </div>

        <div className="overflow-x-auto border border-border bg-surface">
          <table className="w-full min-w-[720px] border-collapse font-heading text-[13px] tabular-nums">
            <thead>
              <tr className="border-b border-border bg-background/40">
                <th className="w-[80px] px-5 py-4 text-left text-[11px] font-semibold tracking-[0.25em] uppercase text-muted">
                  Month
                </th>
                <th className="w-[140px] px-5 py-4 text-left text-[11px] font-semibold tracking-[0.25em] uppercase text-muted">
                  Phase
                </th>
                <th className="px-5 py-4 text-left text-[11px] font-semibold tracking-[0.25em] uppercase text-muted">
                  Trigger
                </th>
                <th className="px-5 py-4 text-left text-[11px] font-semibold tracking-[0.25em] uppercase text-muted">
                  Deployed Assets
                </th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r, i) => (
                <tr
                  key={r.month}
                  className={`group border-b border-border/60 transition-colors duration-150 last:border-b-0 hover:bg-accent/[0.05] ${
                    i % 2 === 1 ? "bg-background/30" : ""
                  }`}
                >
                  <td className="px-5 py-4 font-semibold text-foreground group-hover:text-accent">
                    {r.month}
                  </td>
                  <td className="px-5 py-4 text-[11px] font-semibold tracking-[0.2em] uppercase text-accent">
                    {r.phase}
                  </td>
                  <td className="px-5 py-4 font-medium text-foreground/85">
                    {r.trigger}
                  </td>
                  <td className="px-5 py-4 font-sans text-sm text-foreground/75">
                    {r.assets}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <p className="mt-6 text-xs text-muted">
          § Template. Adjusted per founder during creative direction call.
        </p>
      </Container>
    </section>
  );
}
