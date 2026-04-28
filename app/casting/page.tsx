import type { Metadata } from "next";
import Link from "next/link";
import { Suspense } from "react";
import { Container } from "../_components/Container";
import { CastingForm } from "./CastingForm";

export const metadata: Metadata = {
  title: "Casting — May 1 / 3",
  description:
    "Casting submission for an upcoming Sniped Media editorial. Two shoot windows: May 1 and May 3. LA local only.",
  openGraph: {
    title: "Casting | Sniped Media",
    description:
      "Casting submission for an upcoming Sniped Media editorial. Two shoot windows: May 1 and May 3. LA local only.",
    url: "/casting",
  },
  robots: { index: false, follow: false },
};

export default function CastingPage() {
  return (
    <div className="min-h-screen bg-foreground text-background">
      <section className="relative isolate overflow-hidden border-b border-background/10 py-section">
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
          <span>CASTING / MAY 2026</span>
        </div>

        <Container>
          <Link
            href="/"
            className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 transition-colors hover:text-accent-bright tabular-nums"
          >
            ← Sniped Media
          </Link>
          <span className="mt-8 block font-heading text-[11px] font-semibold tracking-[0.4em] uppercase text-accent-bright tabular-nums">
            § Casting / May 1 + 3
          </span>
          <h1 className="mt-6 max-w-4xl font-heading text-4xl font-bold leading-[1.02] tracking-tight text-balance sm:text-6xl lg:text-7xl">
            Casting submission.
          </h1>
          <p className="mt-6 max-w-2xl text-lg leading-relaxed text-background/85">
            Two shoot windows, May 1 and May 3, AM and PM blocks. LA local only. If selected, you&apos;ll hear back within 48 hours of submission with shoot day, call time, and location.
          </p>
        </Container>
      </section>

      <section className="py-section">
        <Container>
          <div className="mx-auto max-w-2xl">
            <Suspense fallback={<div className="h-96 border border-background/15 bg-foreground" />}>
              <CastingForm />
            </Suspense>
          </div>
        </Container>
      </section>

      <section className="border-t border-background/10 py-12">
        <Container>
          <div className="mx-auto max-w-2xl text-center">
            <p className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums">
              Questions
            </p>
            <p className="mt-3 font-heading text-sm font-semibold tracking-[0.2em] uppercase tabular-nums">
              <a
                href="mailto:hello@snipedmedia.com"
                className="text-background/85 underline decoration-background/30 underline-offset-4 transition-colors hover:text-accent-bright hover:decoration-accent-bright"
              >
                hello@snipedmedia.com
              </a>
            </p>
            <Link
              href="/"
              className="mt-10 inline-block font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 transition-colors hover:text-accent-bright"
            >
              ← Sniped Media
            </Link>
          </div>
        </Container>
      </section>
    </div>
  );
}
