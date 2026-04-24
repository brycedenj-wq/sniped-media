import Link from "next/link";
import { Container } from "../Container";
import { CtaButton } from "../CtaButton";

export function Hero() {
  return (
    <section className="relative isolate flex min-h-[90vh] items-end overflow-hidden border-b border-background/10 bg-foreground text-background">
      <div
        aria-hidden="true"
        className="pointer-events-none absolute inset-0 opacity-[0.04]"
        style={{
          backgroundImage:
            "linear-gradient(to right, #F5F3EE 1px, transparent 1px)",
          backgroundSize: "calc(100% / 12) 100%",
        }}
      />

      <div className="pointer-events-none absolute top-6 right-6 hidden items-center gap-4 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums sm:flex">
        <span>LOS ANGELES</span>
        <span className="h-px w-10 bg-background/30" />
        <span>V1.0 / ON FILE</span>
      </div>

      <Container className="py-section">
        <div className="max-w-4xl">
          <span className="font-heading text-[11px] font-semibold tracking-[0.4em] uppercase text-background/55 tabular-nums">
            § 00 / Sniped Media
          </span>
          <h1 className="mt-8 font-heading text-5xl font-bold leading-[1.02] tracking-tight text-balance sm:text-6xl lg:text-7xl">
            The commercial portrait system for LA founders.
          </h1>
          <p className="mt-6 max-w-[60ch] text-lg leading-relaxed text-background/90">
            One structured shoot. 60 to 80 deployed-ready images. A 12-month deployment plan. For Series A to C founders and senior operators running a personal brand alongside the company.
          </p>
          <div className="mt-10 flex flex-wrap items-center gap-6">
            <CtaButton href="/book" size="lg">
              Book a Qualifying Call
            </CtaButton>
            <Link
              href="/kit"
              className="text-sm font-semibold text-background/85 underline decoration-background/30 underline-offset-4 transition-colors hover:text-background hover:decoration-background"
            >
              See the Kit
            </Link>
          </div>
        </div>
      </Container>

      <div
        aria-hidden="true"
        className="pointer-events-none absolute bottom-8 left-1/2 hidden -translate-x-1/2 lg:block motion-reduce:hidden"
      >
        <span className="block h-10 w-[1px] animate-[scrollHint_3s_ease-in-out_infinite] bg-background/50" />
      </div>

      <style>{`
        @keyframes scrollHint {
          0%, 100% { transform: scaleY(0.4); transform-origin: top; opacity: 0.4; }
          50% { transform: scaleY(1); transform-origin: top; opacity: 1; }
        }
      `}</style>
    </section>
  );
}
