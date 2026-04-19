import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Container } from "../_components/Container";
import { FadeIn } from "../_components/FadeIn";

export const metadata: Metadata = {
  title: "The Work",
  description:
    "Seven years of Los Angeles photography. Editorial portraits, lifestyle, and brand work across studio and on-location assignments.",
  openGraph: {
    title: "The Work | Sniped Media",
    description:
      "Seven years of Los Angeles photography. Editorial portraits, lifestyle, and brand work across studio and on-location assignments.",
    url: "/work",
  },
};

export default function WorkPage() {
  return (
    <>
      <section className="relative isolate flex min-h-[85vh] items-end overflow-hidden bg-foreground text-background sm:min-h-[92vh]">
        <Image
          src="/images/hero.jpg"
          alt=""
          fill
          priority
          quality={95}
          sizes="100vw"
          className="absolute inset-0 -z-10 object-cover object-center opacity-80"
        />
        <div className="absolute inset-0 -z-10 bg-gradient-to-t from-foreground/85 via-foreground/30 to-foreground/10" />
        <Container className="py-section">
          <div className="max-w-4xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-background/60">
              The Archive · 2019 — 2026
            </span>
            <h1 className="mt-6 font-heading text-5xl font-semibold leading-[0.95] tracking-tight text-balance sm:text-7xl lg:text-[128px]">
              The Work.
            </h1>
            <p className="mt-6 max-w-xl text-base text-background/75 sm:mt-8 sm:text-lg">
              Seven years. One standard. Editorial portraits, lifestyle, and brand work across Los Angeles.
            </p>
          </div>
        </Container>
      </section>

      <section className="border-b border-border bg-background py-section">
        <Container>
          <FadeIn>
            <p className="mx-auto max-w-3xl font-heading text-xl font-medium leading-relaxed tracking-tight text-foreground sm:text-3xl">
              Every frame is a commercial-grade decision. We don&apos;t snap.
              We direct. We compose. We execute. The session is the product.
              The photos are the receipt.
            </p>
          </FadeIn>
        </Container>
      </section>

      {/* CHAPTER 01 · EDITORIAL PORTRAITS */}
      <section className="py-section">
        <Container>
          <FadeIn>
            <div className="mb-12 flex items-baseline justify-between gap-8 border-b border-border pb-6 sm:mb-16">
              <div>
                <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
                  Chapter 01
                </span>
                <h2 className="mt-3 font-heading text-3xl font-semibold tracking-tight sm:text-5xl">
                  Editorial Portraits
                </h2>
              </div>
              <span className="hidden font-heading text-sm tracking-[0.25em] uppercase text-muted sm:block">
                Studio · On-Location
              </span>
            </div>
          </FadeIn>

          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-6">
            <FadeIn>
              <figure className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                <Image
                  src="/images/work/archive/archive-09.jpg"
                  alt="Editorial studio portrait, San Francisco"
                  fill
                  quality={95}
                  sizes="(min-width: 640px) 50vw, 100vw"
                  className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                />
              </figure>
            </FadeIn>

            <div className="grid grid-cols-2 gap-4 sm:gap-6">
              <FadeIn delayMs={100}>
                <figure className="relative aspect-[3/4] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-03.jpg"
                    alt="Attorney editorial headshot"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 25vw, 50vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
              <FadeIn delayMs={200}>
                <figure className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-10.jpg"
                    alt="Editorial portrait"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 25vw, 50vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
              <FadeIn delayMs={300}>
                <figure className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-14.jpg"
                    alt="Editorial portrait series"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 25vw, 50vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
              <FadeIn delayMs={400}>
                <figure className="relative aspect-[3/4] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-01.jpg"
                    alt="Editorial portrait"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 25vw, 50vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
            </div>
          </div>
        </Container>
      </section>

      {/* PULLQUOTE · uses the panorama letterboxed so no subject cut-off */}
      <section className="relative isolate flex items-center overflow-hidden bg-foreground text-background">
        <Image
          src="/images/work/archive/archive-08.jpg"
          alt=""
          fill
          quality={95}
          sizes="100vw"
          className="absolute inset-0 -z-10 object-cover object-center opacity-55"
        />
        <div className="absolute inset-0 -z-10 bg-gradient-to-r from-foreground/85 via-foreground/60 to-foreground/40" />
        <Container className="py-section">
          <FadeIn>
            <p className="max-w-2xl font-heading text-2xl font-medium leading-tight tracking-tight text-balance sm:text-5xl">
              The job is not to capture a moment.
              The job is to construct one.
            </p>
          </FadeIn>
        </Container>
      </section>

      {/* CHAPTER 02 · LIFESTYLE & FAMILY */}
      <section className="py-section">
        <Container>
          <FadeIn>
            <div className="mb-12 flex items-baseline justify-between gap-8 border-b border-border pb-6 sm:mb-16">
              <div>
                <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
                  Chapter 02
                </span>
                <h2 className="mt-3 font-heading text-3xl font-semibold tracking-tight sm:text-5xl">
                  Lifestyle &amp; Family
                </h2>
              </div>
              <span className="hidden font-heading text-sm tracking-[0.25em] uppercase text-muted sm:block">
                Directed · Natural
              </span>
            </div>
          </FadeIn>

          <div className="flex flex-col gap-4 sm:gap-6">
            <FadeIn>
              <figure className="relative aspect-[3/2] w-full overflow-hidden bg-foreground/5">
                <Image
                  src="/images/work/archive/archive-07.jpg"
                  alt="Environmental lifestyle portrait"
                  fill
                  quality={95}
                  sizes="100vw"
                  className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                />
              </figure>
            </FadeIn>

            <div className="grid grid-cols-1 gap-4 sm:grid-cols-3 sm:gap-6">
              <FadeIn delayMs={100}>
                <figure className="relative aspect-[4/3] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-02.jpg"
                    alt="Lifestyle portrait"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 33vw, 100vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
              <FadeIn delayMs={200}>
                <figure className="relative aspect-[4/3] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-04.jpg"
                    alt="Lifestyle portrait"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 33vw, 100vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
              <FadeIn delayMs={300}>
                <figure className="relative aspect-[4/3] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-05.jpg"
                    alt="Lifestyle portrait"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 33vw, 100vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
            </div>

            <FadeIn delayMs={400}>
              <figure className="relative mx-auto aspect-[3/4] w-full max-w-md overflow-hidden bg-foreground/5">
                <Image
                  src="/images/work/archive/archive-06.jpg"
                  alt="Lifestyle portrait"
                  fill
                  quality={95}
                  sizes="(min-width: 768px) 28rem, 100vw"
                  className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                />
              </figure>
            </FadeIn>
          </div>
        </Container>
      </section>

      {/* CHAPTER 03 · BRAND & COMMERCIAL */}
      <section className="py-section">
        <Container>
          <FadeIn>
            <div className="mb-12 flex items-baseline justify-between gap-8 border-b border-border pb-6 sm:mb-16">
              <div>
                <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
                  Chapter 03
                </span>
                <h2 className="mt-3 font-heading text-3xl font-semibold tracking-tight sm:text-5xl">
                  Brand &amp; Commercial
                </h2>
              </div>
              <span className="hidden font-heading text-sm tracking-[0.25em] uppercase text-muted sm:block">
                Campaign · Case Study
              </span>
            </div>
          </FadeIn>

          <div className="flex flex-col gap-4 sm:gap-6">
            <FadeIn>
              <figure className="relative aspect-[2/1] w-full overflow-hidden bg-foreground/5">
                <Image
                  src="/images/work/archive/archive-08.jpg"
                  alt="Brand campaign panoramic"
                  fill
                  quality={95}
                  sizes="100vw"
                  className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                />
              </figure>
            </FadeIn>

            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-6">
              <FadeIn delayMs={120}>
                <figure className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-17.jpg"
                    alt="Commercial portrait on location"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 50vw, 100vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
              <FadeIn delayMs={240}>
                <figure className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                  <Image
                    src="/images/work/archive/archive-19.jpg"
                    alt="Commercial portrait on location"
                    fill
                    quality={95}
                    sizes="(min-width: 640px) 50vw, 100vw"
                    className="object-cover object-center transition-transform duration-700 hover:scale-[1.02]"
                  />
                </figure>
              </FadeIn>
            </div>
          </div>
        </Container>
      </section>

      <section className="border-t border-border bg-foreground py-section text-background">
        <Container>
          <div className="max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-background/60">
              End Credits
            </span>
            <h2 className="mt-6 font-heading text-3xl font-semibold tracking-tight text-balance sm:text-5xl">
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
