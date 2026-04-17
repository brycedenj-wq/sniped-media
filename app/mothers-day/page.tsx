import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Container } from "../_components/Container";

const MOTHERS_DAY_URLS: Record<"moment" | "feature", string> = {
  moment: "https://snipedmedia.pixieset.com/booking/mothers-day-moment",
  feature: "https://snipedmedia.pixieset.com/booking/mothers-day-feature",
};

const DM_FALLBACK_URL = "https://instagram.com/snipedmedia";

function tierHref(tier: "moment" | "feature"): string {
  return MOTHERS_DAY_URLS[tier] || DM_FALLBACK_URL;
}

export const metadata: Metadata = {
  title: "Mother's Day Studio Sessions",
  description:
    "Curated editorial portraits at a DTLA studio. Strictly limited spots for May 2 and 3.",
  robots: { index: false, follow: false },
  openGraph: {
    title: "Mother's Day Studio Sessions | Sniped Media",
    description:
      "Curated editorial portraits at a DTLA studio. Strictly limited spots for May 2 and 3.",
    url: "/mothers-day",
  },
};

type Tier = {
  id: "moment" | "feature";
  name: string;
  price: string;
  highlight?: boolean;
  includes: string[];
  cta: string;
};

const tiers: Tier[] = [
  {
    id: "moment",
    name: "The Moment",
    price: "$275",
    includes: [
      "30-minute studio session",
      "3 retouched high-resolution images",
      "Private proofing gallery",
    ],
    cta: "Reserve The Moment",
  },
  {
    id: "feature",
    name: "The Feature",
    price: "$550",
    highlight: true,
    includes: [
      "60-minute studio session",
      "5 retouched high-resolution images",
      "1 fine-art 8x10 physical print",
      "Private proofing gallery",
    ],
    cta: "Reserve The Feature",
  },
];

export default function MothersDayPage() {
  return (
    <>
      <section className="relative isolate flex min-h-[70vh] items-end overflow-hidden bg-foreground text-background">
        <Image
          src="/images/work-lifestyle.jpg"
          alt=""
          fill
          priority
          sizes="100vw"
          className="absolute inset-0 -z-10 object-cover opacity-70"
        />
        <div className="absolute inset-0 -z-10 bg-gradient-to-t from-foreground/85 via-foreground/40 to-foreground/20" />

        <Container className="py-section">
          <div className="max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.3em] uppercase text-background/70">
              Limited · 12 Spots · May 2–3
            </span>
            <h1 className="mt-6 font-heading text-4xl font-semibold tracking-tight text-balance sm:text-5xl lg:text-6xl">
              Mother&apos;s Day Studio Sessions: DTLA
            </h1>
            <p className="mt-6 max-w-xl text-lg text-background/80">
              Curated editorial portraits. Strictly limited spots for May 2 and 3.
            </p>
            <div className="mt-10">
              <Link
                href={tierHref("feature")}
                className="inline-flex h-14 items-center justify-center rounded-md bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
              >
                Reserve Your Slot
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
                Most family photos fail because they rely on forced smiles and awkward posture. You deserve portraits that look like a Vanity Fair editorial. We are replacing the chaotic photo experience with a pre-designed, high-end set. You are not walking into a blank room to guess what to do with your hands. You are stepping onto a pre-lit stage designed specifically to remove tension and create natural, flattering geometry.
              </p>
            </div>
            <div>
              <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
                The Environment
              </h2>
              <p className="mt-6 text-base leading-relaxed text-muted">
                We built a custom set inside our DTLA studio. Warm peach seamless paper. Minimalist physical anchors. Gridded strobe lighting engineered to carve out jawlines and create beautiful dimension. It is a commercial-grade environment applied directly to your family portrait.
              </p>
            </div>
          </div>
        </Container>
      </section>

      <section className="border-y border-border bg-surface py-section">
        <Container>
          <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
            The Mechanics
          </h2>
          <ol className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
            {[
              "Secure your spot with a 50% deposit.",
              "Arrive at 2715 S Main St, Los Angeles on May 2 or 3.",
              "We direct you with specific physical protocols to eliminate awkwardness and give your hands a job.",
              "We execute the session efficiently within your booked time window.",
              "You receive a private proofing gallery to select your final retouched assets, with the option to purchase additional frames.",
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

      <section className="py-section">
        <Container>
          <div className="mb-12">
            <h2 className="font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
              The Packages
            </h2>
            <p className="mt-4 text-base text-muted">
              Two tiers. Choose the coverage that fits. Additional frames available through your gallery after the shoot.
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
                <ul className={`mt-8 space-y-3 text-sm ${t.highlight ? "text-background/85" : "text-muted"}`}>
                  {t.includes.map((line) => (
                    <li key={line} className="flex items-start gap-3">
                      <span aria-hidden className={`mt-[7px] inline-block h-1 w-3 flex-none ${t.highlight ? "bg-background/60" : "bg-foreground/60"}`} />
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
              Expert direction. Zero posing experience required.
            </h2>
            <p className="mt-6 max-w-2xl text-base text-background/75">
              Walk in. Let us direct. Walk out with editorial portraits you actually love. Twelve spots across May 2 and 3. When they are gone, they are gone.
            </p>
            <div className="mt-10 flex flex-wrap items-center gap-4">
              <Link
                href={tierHref("feature")}
                className="inline-flex h-14 items-center justify-center rounded-md bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
              >
                Reserve Your Slot
              </Link>
              <a
                href={DM_FALLBACK_URL}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-background/70 hover:text-background"
              >
                Or DM &ldquo;MOM&rdquo; on Instagram
              </a>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}
