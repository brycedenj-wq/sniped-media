import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Container } from "../_components/Container";

const GRAD_URLS: Record<"short-film" | "feature-length", string> = {
  "short-film": "",
  "feature-length": "",
};

const DM_FALLBACK_URL = "https://instagram.com/sniped.media";

function tierHref(tier: "short-film" | "feature-length"): string {
  return GRAD_URLS[tier] || DM_FALLBACK_URL;
}

export const metadata: Metadata = {
  title: "Grad Sessions: Roll Credits",
  description:
    "Cinematic graduation portraits across Los Angeles. DTLA studio or on-campus. Sessions booking now through mid-June.",
  robots: { index: false, follow: false },
  openGraph: {
    title: "Grad Sessions: Roll Credits | Sniped Media",
    description:
      "Cinematic graduation portraits across Los Angeles. DTLA studio or on-campus. Sessions booking now through mid-June.",
    url: "/grad",
    images: [
      {
        url: "/opengraph-image",
        width: 1200,
        height: 630,
        alt: "Sniped Media | High-Impact Los Angeles Photography",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Grad Sessions: Roll Credits | Sniped Media",
    description:
      "Cinematic graduation portraits across Los Angeles. DTLA studio or on-campus. Sessions booking now through mid-June.",
    images: ["/opengraph-image"],
  },
};

type Tier = {
  id: "short-film" | "feature-length";
  name: string;
  price: string;
  highlight?: boolean;
  includes: string[];
  cta: string;
};

const tiers: Tier[] = [
  {
    id: "short-film",
    name: "Short Film",
    price: "$275",
    includes: [
      "45 minutes of expert direction",
      "One location: DTLA studio or your campus",
      "5 retouched high-resolution images",
      "Private proofing gallery",
      "Full payment at booking",
    ],
    cta: "Reserve Short Film",
  },
  {
    id: "feature-length",
    name: "Feature Length",
    price: "$550",
    highlight: true,
    includes: [
      "90 minutes of expert direction",
      "One location: DTLA studio or your campus",
      "15 to 20 retouched high-resolution images",
      "Private proofing gallery",
      "50% deposit holds your date; balance auto-invoiced 48 hours prior",
    ],
    cta: "Reserve Feature Length",
  },
];

export default function GradPage() {
  return (
    <>
      <section className="relative isolate flex min-h-[80vh] items-end overflow-hidden bg-foreground text-background">
        <Image
          src="/images/grad-hero.jpg"
          alt=""
          fill
          priority
          quality={95}
          sizes="100vw"
          className="absolute inset-0 -z-10 object-cover object-top opacity-75"
        />
        <div className="absolute inset-0 -z-10 bg-gradient-to-t from-foreground/85 via-foreground/40 to-foreground/20" />

        <Container className="py-section">
          <div className="max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.3em] uppercase text-background/70">
              Now Streaming · LA Grad Season 2026
            </span>
            <h1 className="mt-6 font-heading text-5xl font-semibold tracking-tight text-balance sm:text-6xl lg:text-7xl">
              Roll Credits.
            </h1>
            <p className="mt-6 max-w-xl text-lg text-background/80">
              Close out your four-year feature with portraits that earn the title card. LA studio and on-campus sessions booking now through mid-June.
            </p>
            <div className="mt-10">
              <Link
                href="#packages"
                className="inline-flex h-14 items-center justify-center rounded-md bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
              >
                Lock Your Spot
              </Link>
            </div>
          </div>
        </Container>
      </section>

      <section className="py-section">
        <Container>
          <div className="grid gap-12 lg:grid-cols-2 lg:gap-16">
            <div>
              <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
                The Hook
              </h2>
              <p className="mt-6 text-base leading-relaxed text-muted">
                Most grad photos fail because they rush the moment. Parents scrambling with phones on the stage. Formal portraits that look like yearbook stock. You walked four years for this. Your final frames should match the work. We replace the chaos with directed, cinematic portraits: studio-grade lighting, intentional composition, zero awkwardness.
              </p>
            </div>
            <div>
              <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
                The Set
              </h2>
              <p className="mt-6 text-base leading-relaxed text-muted">
                Pick your stage. Our DTLA studio is a pre-lit editorial environment with cinematic light, clean sightlines, and commercial-grade control. Or bring us to your campus — USC, UCLA, LMU, your high school — and we execute the same standard outdoors. Same photographer. Same direction. Two different canvases.
              </p>
            </div>
          </div>
        </Container>
      </section>

      <section className="py-section">
        <Container>
          <div className="mb-10 flex items-end justify-between gap-8">
            <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
              Past Sessions
            </h2>
            <p className="hidden text-sm text-muted sm:block">
              Seven years of grads. One standard.
            </p>
          </div>
          <div className="grid gap-4 sm:grid-cols-3 sm:grid-rows-2 sm:gap-6">
            <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5 sm:col-span-1 sm:row-span-2 sm:aspect-auto">
              <Image
                src="/images/grad-work-1.jpg"
                alt="Editorial graduation portrait on location"
                fill
                quality={95}
                sizes="(min-width: 640px) 33vw, 100vw"
                className="object-cover transition-transform duration-700 hover:scale-[1.02]"
              />
            </div>
            <div className="relative aspect-[3/2] w-full overflow-hidden bg-foreground/5 sm:col-span-2">
              <Image
                src="/images/grad-work-2.jpg"
                alt="LMU graduate with mascot on campus"
                fill
                quality={95}
                sizes="(min-width: 640px) 66vw, 100vw"
                className="object-cover transition-transform duration-700 hover:scale-[1.02]"
              />
            </div>
            <div className="relative aspect-[5/4] w-full overflow-hidden bg-foreground/5 sm:col-span-2">
              <Image
                src="/images/grad-work-3.jpg"
                alt="Graduate with family, studio portrait"
                fill
                quality={95}
                sizes="(min-width: 640px) 66vw, 100vw"
                className="object-cover transition-transform duration-700 hover:scale-[1.02]"
              />
            </div>
          </div>
        </Container>
      </section>

      <section className="border-y border-border bg-surface py-section">
        <Container>
          <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
            The Run
          </h2>
          <ol className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
            {[
              "Lock your spot. Full payment for Short Film, 50% deposit for Feature Length.",
              "Tell us your location at booking: DTLA studio or your campus.",
              "Arrive in your cap, gown, and the look that captures your four years.",
              "We direct you step by step. No forced smiles, no awkward posing.",
              "Receive a private proofing gallery and select your final frames.",
            ].map((step, i) => (
              <li key={i}>
                <span className="font-heading text-sm font-semibold tracking-[0.2em] text-muted">
                  {String(i + 1).padStart(2, "0")}
                </span>
                <p className="mt-3 text-sm leading-relaxed text-foreground">{step}</p>
              </li>
            ))}
          </ol>
        </Container>
      </section>

      <section id="packages" className="py-section scroll-mt-20">
        <Container>
          <div className="mb-12">
            <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
              The Features
            </h2>
            <p className="mt-4 text-base text-muted">
              Two tiers. Choose the coverage that fits. Cinematic short film add-on available: ask at booking.
            </p>
          </div>
          <div className="grid gap-6 lg:grid-cols-2 lg:max-w-5xl">
            {tiers.map((t) => (
              <div
                key={t.id}
                className={`relative flex flex-col border p-8 ${
                  t.highlight
                    ? "border-foreground bg-foreground text-background"
                    : "border-border bg-surface text-foreground"
                }`}
              >
                {t.highlight ? (
                  <span className="absolute -top-3 left-8 bg-background px-3 py-1 font-heading text-[10px] font-semibold tracking-[0.25em] uppercase text-foreground border border-foreground">
                    Most Popular
                  </span>
                ) : null}
                <h3 className="font-heading text-xl font-semibold">{t.name}</h3>
                <div className="mt-4 font-heading text-4xl font-semibold tracking-tight">
                  {t.price}
                </div>
                <ul
                  className={`mt-8 space-y-3 text-sm ${
                    t.highlight ? "text-background/85" : "text-muted"
                  }`}
                >
                  {t.includes.map((line) => (
                    <li key={line} className="flex items-start gap-3">
                      <span
                        aria-hidden
                        className={`mt-[7px] inline-block h-1 w-3 flex-none ${
                          t.highlight ? "bg-background/60" : "bg-foreground/60"
                        }`}
                      />
                      <span>{line}</span>
                    </li>
                  ))}
                </ul>
                <div className="mt-10 pt-6 border-t border-current/20">
                  <Link
                    href={tierHref(t.id)}
                    className={`block w-full text-center px-6 py-3 font-semibold transition-colors ${
                      t.highlight
                        ? "bg-background text-foreground hover:bg-background/90"
                        : "bg-foreground text-background hover:bg-foreground/90"
                    }`}
                  >
                    {t.cta}
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </Container>
      </section>

      <section className="border-t border-border bg-foreground py-section text-background">
        <Container>
          <div className="max-w-3xl">
            <h2 className="font-heading text-3xl font-semibold tracking-tight text-balance sm:text-4xl">
              Your four-year feature deserves better than a cap-and-gown selfie.
            </h2>
            <p className="mt-6 max-w-2xl text-base text-background/75">
              Final scenes book out fast. Sessions run now through mid-June for every LA college and high school. When the calendar fills, credits roll.
            </p>
            <div className="mt-10 flex flex-wrap items-center gap-4">
              <Link
                href="#packages"
                className="inline-flex h-14 items-center justify-center rounded-md bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
              >
                Lock Your Spot
              </Link>
              <a
                href={DM_FALLBACK_URL}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-background/70 hover:text-background"
              >
                Or DM &ldquo;GRAD&rdquo; on Instagram
              </a>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}
