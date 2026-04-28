import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Container } from "../_components/Container";
import { FadeIn } from "../_components/FadeIn";
import { GridOverlay } from "../_components/GridOverlay";

export const metadata: Metadata = {
  title: "Selected Work",
  description:
    "Selected commercial portrait work by Sniped Media in Los Angeles.",
  openGraph: {
    title: "Selected Work | Sniped Media",
    description:
      "Selected commercial portrait work by Sniped Media in Los Angeles.",
    url: "/work",
  },
  robots: { index: false, follow: false },
};

type Frame = {
  src: string;
  alt: string;
  index: string;
  context: string;
  specs: string;
  deployment: string;
  span?: "wide" | "tall" | "default";
};

const frames: Frame[] = [
  {
    src: "/images/work/archive/archive-09.jpg",
    alt: "Editorial portrait, controlled light",
    index: "01",
    context: "EDITORIAL / CONTROLLED LIGHT",
    specs: "85mm f/1.8",
    deployment: "PRESS COVER",
    span: "wide",
  },
  {
    src: "/images/work/archive/archive-03.jpg",
    alt: "Environmental portrait, natural light",
    index: "02",
    context: "ENVIRONMENTAL / NATURAL LIGHT",
    specs: "35mm f/2.8",
    deployment: "BRAND HERO",
  },
  {
    src: "/images/work/archive/archive-17.jpg",
    alt: "Studio portrait, high key",
    index: "03",
    context: "STUDIO / HIGH KEY",
    specs: "50mm f/4",
    deployment: "EDITORIAL OPENER",
  },
  {
    src: "/images/work/archive/archive-10.jpg",
    alt: "Outdoor portrait, golden hour",
    index: "04",
    context: "OUTDOOR / GOLDEN HOUR",
    specs: "85mm f/2.2",
    deployment: "CAMPAIGN PORTRAIT",
  },
  {
    src: "/images/work/archive/archive-19.jpg",
    alt: "Environmental portrait, overcast",
    index: "05",
    context: "ENVIRONMENTAL / OVERCAST",
    specs: "35mm f/4",
    deployment: "ABOUT PAGE",
  },
  {
    src: "/images/work/archive/archive-01.jpg",
    alt: "Studio portrait, low key",
    index: "06",
    context: "STUDIO / LOW KEY",
    specs: "85mm f/2",
    deployment: "MAGAZINE FEATURE",
    span: "wide",
  },
];

export default function WorkPage() {
  return (
    <>
      {/* Hero — dark, matches coming-soon visual register */}
      <section className="relative isolate flex min-h-[55vh] items-end overflow-hidden border-b border-background/10 bg-foreground py-section text-background">
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
          <span>SELECTED WORK</span>
        </div>

        <Container>
          <Link
            href="/"
            className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 transition-colors hover:text-accent-bright tabular-nums"
          >
            ← Sniped Media
          </Link>
          <h1 className="mt-8 max-w-4xl font-heading text-5xl font-bold leading-[0.98] tracking-tight text-balance sm:text-6xl lg:text-7xl">
            Selected work.
          </h1>
          <p className="mt-6 max-w-xl text-lg leading-relaxed text-background/80">
            A curated cut from the archive. Editorial, environmental, studio. Los Angeles.
          </p>
        </Container>
      </section>

      {/* Pullquote — signature phrasing, third person */}
      <section className="bg-foreground py-section text-background">
        <Container>
          <FadeIn>
            <p className="mx-auto max-w-3xl font-heading text-xl font-medium leading-relaxed tracking-tight text-background sm:text-2xl">
              Every frame is a commercial-grade decision. The studio does not snap. It directs. It composes. It executes.
            </p>
          </FadeIn>
        </Container>
      </section>

      {/* Curated grid — varied spans, dense editorial layout */}
      <section className="relative bg-background py-section">
        <GridOverlay />
        <Container className="relative z-10">
          <div className="grid grid-cols-1 gap-6 sm:grid-cols-6 sm:gap-4 lg:gap-6">
            {frames.map((f, i) => (
              <FadeIn
                key={f.src}
                delayMs={Math.min(i * 80, 480)}
                className={
                  f.span === "wide"
                    ? "sm:col-span-6"
                    : "sm:col-span-3"
                }
              >
                <figure className="group flex flex-col gap-3">
                  <div
                    className={`relative w-full overflow-hidden bg-foreground/5 ${
                      f.span === "wide"
                        ? "aspect-[16/9]"
                        : "aspect-[4/5]"
                    }`}
                  >
                    <Image
                      src={f.src}
                      alt={f.alt}
                      fill
                      quality={95}
                      sizes={
                        f.span === "wide"
                          ? "(min-width: 640px) 100vw, 100vw"
                          : "(min-width: 640px) 50vw, 100vw"
                      }
                      className="object-cover object-center transition-transform duration-700 group-hover:scale-[1.015]"
                    />
                    <div className="pointer-events-none absolute inset-x-0 bottom-0 bg-gradient-to-t from-foreground/90 via-foreground/30 to-transparent p-5 opacity-0 transition-opacity duration-200 group-hover:opacity-100 motion-reduce:transition-none">
                      <p className="font-heading text-[11px] font-semibold tracking-[0.25em] uppercase text-background tabular-nums">
                        {f.context} · {f.specs}
                      </p>
                      <p className="mt-1 font-heading text-[11px] font-semibold tracking-[0.25em] uppercase text-background/80 tabular-nums">
                        {f.deployment}
                      </p>
                    </div>
                  </div>
                  <figcaption className="flex items-center justify-between gap-2 border-t border-border pt-2 font-heading text-[11px] font-semibold tracking-[0.2em] uppercase text-muted tabular-nums">
                    <span>{f.index}</span>
                    <span className="truncate">{f.specs}</span>
                  </figcaption>
                </figure>
              </FadeIn>
            ))}
          </div>
        </Container>
      </section>

      {/* Closing — minimal, no broken CTAs */}
      <section className="border-t border-border bg-foreground py-section text-background">
        <Container>
          <div className="mx-auto max-w-3xl text-center">
            <p className="font-heading text-[11px] font-semibold tracking-[0.4em] uppercase text-background/55 tabular-nums">
              § Continued
            </p>
            <h2 className="mt-6 font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
              The next version is in development.
            </h2>
            <p className="mt-6 text-base text-background/70 leading-relaxed">
              Inquiries handled directly until the new site lands.
            </p>
            <p className="mt-8 font-heading text-sm font-semibold tracking-[0.3em] uppercase tabular-nums">
              <a
                href="mailto:hello@snipedmedia.com"
                className="text-background/85 underline decoration-background/30 underline-offset-4 transition-colors hover:text-accent-bright hover:decoration-accent-bright"
              >
                hello@snipedmedia.com
              </a>
            </p>
            <Link
              href="/"
              className="mt-12 inline-block font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 transition-colors hover:text-accent-bright"
            >
              ← Sniped Media
            </Link>
          </div>
        </Container>
      </section>
    </>
  );
}
