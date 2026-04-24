import type { Metadata } from "next";
import Link from "next/link";
import { Container } from "../_components/Container";
import { FadeIn } from "../_components/FadeIn";

export const metadata: Metadata = {
  title: "About",
  description:
    "Sniped Media builds commercial portrait libraries for LA founders. About the studio and the craft.",
  openGraph: {
    title: "About | Sniped Media",
    description:
      "Sniped Media builds commercial portrait libraries for LA founders. About the studio and the craft.",
    url: "/about",
  },
};

const refuses = [
  "Not a wedding photographer. Different craft, different clientele.",
  "Not a corporate event shooter. Different job, different deliverables.",
  "Not a family portrait studio. Personal work, not commercial.",
  "Not an actor or model portfolio shop. Industry-specific, and not mine.",
];

export default function AboutPage() {
  return (
    <>
      <section className="border-b border-border bg-background py-section">
        <Container>
          <div className="max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
              About
            </span>
            <h1 className="mt-6 font-heading text-4xl font-medium leading-[1.05] tracking-tight text-balance sm:text-5xl">
              I&apos;m Bryceden Jones. I build commercial portrait libraries for LA founders.
            </h1>
          </div>
        </Container>
      </section>

      <section className="bg-surface py-section">
        <Container>
          <div className="mx-auto max-w-3xl space-y-6">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
              Why This Work
            </span>
            <p className="text-lg text-foreground/85 leading-relaxed">
              Seven years of commercial work. Every category a camera can be pointed at. The work I kept coming back to was founder portraits, the frames that had to do real operational work on public surfaces for twelve months at a stretch.
            </p>
            <p className="text-lg text-foreground/85 leading-relaxed">
              Sniped Media is that work, and only that work. One product. One buyer. One standard of delivery.
            </p>
          </div>
        </Container>
      </section>

      <section className="border-t border-border bg-background py-section">
        <Container>
          <div className="mx-auto max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
              What I Refuse
            </span>
            <ul className="mt-10 space-y-4">
              {refuses.map((item) => (
                <li
                  key={item}
                  className="border-b border-border pb-4 text-lg text-foreground/75 leading-relaxed"
                >
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </Container>
      </section>

      <FadeIn>
        <section className="border-t border-border bg-foreground py-section text-background">
          <Container>
            <div className="mx-auto max-w-3xl space-y-8">
              <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-background/60">
                Craft
              </span>
              <p className="text-lg leading-relaxed text-background/85 sm:text-xl">
                Surgical subject. Degraded background. Subject pops, environment recedes. That is the signature, and it holds across every frame the studio ships.
              </p>
              <p className="text-lg leading-relaxed text-background/85 sm:text-xl">
                The tuning is specific and it is earned. Skin reads dimensional, not flat. Backgrounds carry texture without competing. Light is controlled where it needs to be and available where it should be. A frame is either committed to or it does not ship.
              </p>
              <p className="font-heading text-2xl font-medium leading-snug tracking-tight text-balance sm:text-3xl">
                Every frame is a commercial-grade decision. The studio does not snap. It directs. It composes. It executes.
              </p>
            </div>
          </Container>
        </section>
      </FadeIn>

      <section className="border-t border-border bg-surface py-section">
        <Container>
          <div className="mx-auto max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
              Credentials
            </span>
            <ul className="mt-10 space-y-4 text-lg text-foreground/80 leading-relaxed">
              <li className="border-b border-border pb-4">Seven years professional. Los Angeles based.</li>
              <li className="border-b border-border pb-4">
                Founder Kit clients: list updates as Kits deliver.
              </li>
            </ul>

            <div className="mt-12">
              <Link
                href="/book"
                className="inline-flex h-14 items-center justify-center bg-foreground px-8 text-base font-semibold text-background transition-colors hover:bg-foreground/90"
              >
                Book a Qualifying Call
              </Link>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}
