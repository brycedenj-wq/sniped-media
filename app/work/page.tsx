import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Container } from "../_components/Container";
import { FadeIn } from "../_components/FadeIn";

export const metadata: Metadata = {
  title: "The Work",
  description:
    "Seven years of Los Angeles photography. Editorial portraits, lifestyle, and events across studio and on-location work.",
  openGraph: {
    title: "The Work | Sniped Media",
    description:
      "Seven years of Los Angeles photography. Editorial portraits, lifestyle, and events across studio and on-location work.",
    url: "/work",
  },
};

type Slot = { src: string; alt: string };

const editorial: Slot[] = [
  { src: "/images/work/archive/archive-03.jpg", alt: "Attorney editorial headshot" },
  { src: "/images/work/archive/archive-09.jpg", alt: "San Francisco studio portrait" },
  { src: "/images/work/archive/archive-01.jpg", alt: "Editorial portrait" },
  { src: "/images/work/archive/archive-07.jpg", alt: "Editorial portrait on location" },
  { src: "/images/work/archive/archive-08.jpg", alt: "Brand campaign portrait" },
  { src: "/images/work/archive/archive-10.jpg", alt: "Editorial portrait" },
  { src: "/images/work/archive/archive-11.jpg", alt: "Editorial portrait" },
];

const lifestyle: Slot[] = [
  { src: "/images/work/archive/archive-02.jpg", alt: "Lifestyle portrait" },
  { src: "/images/work/archive/archive-04.jpg", alt: "Family lifestyle portrait" },
  { src: "/images/work/archive/archive-05.jpg", alt: "Lifestyle portrait" },
  { src: "/images/work/archive/archive-06.jpg", alt: "Lifestyle portrait" },
  { src: "/images/work/archive/archive-12.jpg", alt: "Lifestyle portrait" },
  { src: "/images/work/archive/archive-13.jpg", alt: "Lifestyle portrait" },
];

const events: Slot[] = [
  { src: "/images/work/archive/archive-14.jpg", alt: "Event coverage" },
  { src: "/images/work/archive/archive-15.jpg", alt: "Event coverage" },
  { src: "/images/work/archive/archive-16.jpg", alt: "On-location portrait" },
  { src: "/images/work/archive/archive-17.jpg", alt: "On-location portrait" },
  { src: "/images/work/archive/archive-18.jpg", alt: "On-location portrait" },
  { src: "/images/work/archive/archive-19.jpg", alt: "On-location portrait" },
];

export default function WorkPage() {
  return (
    <>
      <section className="relative isolate flex min-h-[92vh] items-end overflow-hidden bg-foreground text-background">
        <Image
          src="/images/hero.jpg"
          alt=""
          fill
          priority
          quality={95}
          sizes="100vw"
          className="absolute inset-0 -z-10 object-cover opacity-80"
        />
        <div className="absolute inset-0 -z-10 bg-gradient-to-t from-foreground/85 via-foreground/25 to-foreground/10" />
        <Container className="py-section">
          <div className="max-w-4xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-background/60">
              The Archive · 2019 — 2026
            </span>
            <h1 className="mt-6 font-heading text-6xl font-semibold leading-[0.95] tracking-tight text-balance sm:text-7xl lg:text-[128px]">
              The Work.
            </h1>
            <p className="mt-8 max-w-xl text-lg text-background/75">
              Seven years. One standard. Editorial portraits, lifestyle, and events across Los Angeles.
            </p>
          </div>
        </Container>
      </section>

      <section className="border-b border-border bg-background py-section">
        <Container>
          <FadeIn>
            <p className="mx-auto max-w-3xl font-heading text-2xl font-medium leading-relaxed tracking-tight text-foreground sm:text-3xl">
              Every frame is a commercial-grade decision. We don&apos;t snap.
              We direct. We compose. We execute. The session is the product.
              The photos are the receipt.
            </p>
          </FadeIn>
        </Container>
      </section>

      <section className="py-section">
        <Container>
          <FadeIn>
            <div className="mb-16 flex items-baseline justify-between gap-8 border-b border-border pb-6">
              <div>
                <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
                  Chapter 01
                </span>
                <h2 className="mt-3 font-heading text-4xl font-semibold tracking-tight sm:text-5xl">
                  Editorial Portraits
                </h2>
              </div>
              <span className="hidden font-heading text-sm tracking-[0.25em] uppercase text-muted sm:block">
                Studio · On-Location
              </span>
            </div>
          </FadeIn>

          <div className="grid grid-cols-1 gap-4 sm:grid-cols-4 sm:grid-rows-[auto_auto_auto] sm:gap-6">
            <FadeIn className="sm:col-span-2 sm:row-span-2">
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5 sm:aspect-auto sm:h-full">
                <Image
                  src={editorial[0].src}
                  alt={editorial[0].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 50vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={100}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={editorial[1].src}
                  alt={editorial[1].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 25vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={200}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={editorial[2].src}
                  alt={editorial[2].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 25vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={300}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={editorial[3].src}
                  alt={editorial[3].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 25vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={400}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={editorial[4].src}
                  alt={editorial[4].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 25vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={500} className="sm:col-span-2">
              <div className="relative aspect-[16/10] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={editorial[5].src}
                  alt={editorial[5].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 50vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={600} className="sm:col-span-2">
              <div className="relative aspect-[16/10] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={editorial[6].src}
                  alt={editorial[6].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 50vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
          </div>
        </Container>
      </section>

      <section className="relative isolate flex min-h-[60vh] items-center overflow-hidden bg-foreground text-background">
        <Image
          src={editorial[2].src}
          alt=""
          fill
          quality={95}
          sizes="100vw"
          className="absolute inset-0 -z-10 object-cover object-top opacity-60"
        />
        <div className="absolute inset-0 -z-10 bg-gradient-to-r from-foreground/75 via-foreground/45 to-foreground/25" />
        <Container className="py-section">
          <FadeIn>
            <p className="max-w-2xl font-heading text-3xl font-medium leading-tight tracking-tight text-balance sm:text-5xl">
              The job is not to capture a moment.
              The job is to construct one.
            </p>
          </FadeIn>
        </Container>
      </section>

      <section className="py-section">
        <Container>
          <FadeIn>
            <div className="mb-16 flex items-baseline justify-between gap-8 border-b border-border pb-6">
              <div>
                <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
                  Chapter 02
                </span>
                <h2 className="mt-3 font-heading text-4xl font-semibold tracking-tight sm:text-5xl">
                  Lifestyle &amp; Family
                </h2>
              </div>
              <span className="hidden font-heading text-sm tracking-[0.25em] uppercase text-muted sm:block">
                Directed · Natural
              </span>
            </div>
          </FadeIn>

          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3 sm:gap-6">
            <FadeIn className="sm:col-span-2 sm:row-span-2">
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5 sm:aspect-auto sm:h-full">
                <Image
                  src={lifestyle[0].src}
                  alt={lifestyle[0].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 66vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={100}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={lifestyle[1].src}
                  alt={lifestyle[1].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={200}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={lifestyle[2].src}
                  alt={lifestyle[2].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={300}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={lifestyle[3].src}
                  alt={lifestyle[3].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={400}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={lifestyle[4].src}
                  alt={lifestyle[4].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={500}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={lifestyle[5].src}
                  alt={lifestyle[5].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
          </div>
        </Container>
      </section>

      <section className="py-section">
        <Container>
          <FadeIn>
            <div className="mb-16 flex items-baseline justify-between gap-8 border-b border-border pb-6">
              <div>
                <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
                  Chapter 03
                </span>
                <h2 className="mt-3 font-heading text-4xl font-semibold tracking-tight sm:text-5xl">
                  Events &amp; On Location
                </h2>
              </div>
              <span className="hidden font-heading text-sm tracking-[0.25em] uppercase text-muted sm:block">
                Reliable · Hands-Off
              </span>
            </div>
          </FadeIn>

          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3 sm:gap-6">
            <FadeIn className="sm:col-span-3">
              <div className="relative aspect-[21/9] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={events[0].src}
                  alt={events[0].alt}
                  fill
                  quality={95}
                  sizes="100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={120}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={events[1].src}
                  alt={events[1].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={240}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={events[2].src}
                  alt={events[2].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={360}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={events[3].src}
                  alt={events[3].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={480} className="sm:col-span-2">
              <div className="relative aspect-[16/10] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={events[4].src}
                  alt={events[4].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 66vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
            <FadeIn delayMs={600}>
              <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src={events[5].src}
                  alt={events[5].alt}
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 33vw, 100vw"
                  className="object-cover transition-transform duration-700 hover:scale-[1.02]"
                />
              </div>
            </FadeIn>
          </div>
        </Container>
      </section>

      <section className="border-t border-border bg-foreground py-section text-background">
        <Container>
          <div className="max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-background/60">
              End Credits
            </span>
            <h2 className="mt-6 font-heading text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
              Seen enough? Let&apos;s get on the calendar.
            </h2>
            <p className="mt-6 max-w-2xl text-base text-background/75">
              The work above took seven years. Yours takes 45 to 90 minutes. Review the investment, pick a tier, lock the date.
            </p>
            <div className="mt-10 flex flex-wrap items-center gap-6">
              <Link
                href="/portfolio-pricing"
                className="inline-flex h-14 items-center justify-center rounded-md bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
              >
                View Pricing
              </Link>
              <Link
                href="/book"
                className="text-sm text-background/70 underline decoration-background/30 underline-offset-4 transition-colors hover:text-background hover:decoration-background"
              >
                Or check availability directly
              </Link>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}
