import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Container } from "../_components/Container";
import { FadeIn } from "../_components/FadeIn";

export const metadata: Metadata = {
  title: "The Work",
  description:
    "Editorial founder portraits, environmental founder portraits, and structured studio work by Sniped Media in Los Angeles.",
  openGraph: {
    title: "The Work | Sniped Media",
    description:
      "Editorial founder portraits, environmental founder portraits, and structured studio work by Sniped Media in Los Angeles.",
    url: "/work",
  },
  robots: { index: false, follow: false },
};

type Frame = {
  src: string;
  alt: string;
  caption: string;
};

const frames: Frame[] = [
  {
    src: "/images/work/archive/archive-09.jpg",
    alt: "Editorial studio portrait",
    caption: "Editorial studio portrait · Los Angeles · Deployed as LinkedIn hero",
  },
  {
    src: "/images/work/archive/archive-03.jpg",
    alt: "Editorial headshot",
    caption: "Editorial headshot · Los Angeles · Deployed as press bio",
  },
  {
    src: "/images/work/archive/archive-10.jpg",
    alt: "Editorial portrait",
    caption: "Editorial portrait · Los Angeles · Deployed as speaking deck opener",
  },
  {
    src: "/images/work/archive/archive-14.jpg",
    alt: "Editorial portrait series",
    caption: "Editorial portrait · Los Angeles · Deployed as press release",
  },
  {
    src: "/images/work/archive/archive-01.jpg",
    alt: "Editorial portrait",
    caption: "Editorial portrait · Los Angeles · Deployed as web hero",
  },
  {
    src: "/images/work/archive/archive-07.jpg",
    alt: "Environmental portrait",
    caption: "Environmental portrait · Los Angeles · Deployed as company about page",
  },
  {
    src: "/images/work/archive/archive-02.jpg",
    alt: "Editorial portrait",
    caption: "Editorial portrait · Los Angeles · Deployed as LinkedIn post",
  },
  {
    src: "/images/work/archive/archive-04.jpg",
    alt: "Editorial portrait",
    caption: "Editorial portrait · Los Angeles · Deployed as podcast tile",
  },
  {
    src: "/images/work/archive/archive-05.jpg",
    alt: "Editorial portrait",
    caption: "Editorial portrait · Los Angeles · Deployed as keynote intro",
  },
  {
    src: "/images/work/archive/archive-06.jpg",
    alt: "Editorial portrait",
    caption: "Editorial portrait · Los Angeles · Deployed as newsletter header",
  },
  {
    src: "/images/work/archive/archive-08.jpg",
    alt: "Brand campaign portrait",
    caption: "Environmental portrait · Los Angeles · Deployed as campaign landing page",
  },
  {
    src: "/images/work/archive/archive-17.jpg",
    alt: "Environmental commercial portrait",
    caption: "Environmental portrait · Los Angeles · Deployed as recruiting page",
  },
  {
    src: "/images/work/archive/archive-19.jpg",
    alt: "Environmental commercial portrait",
    caption: "Environmental portrait · Los Angeles · Deployed as investor letter",
  },
];

export default function WorkPage() {
  return (
    <>
      <section className="border-b border-border bg-background py-section">
        <Container>
          <div className="max-w-3xl">
            <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-muted">
              The Work
            </span>
            <h1 className="mt-6 font-heading text-4xl font-medium leading-[1.05] tracking-tight text-balance sm:text-5xl">
              Editorial, environmental, studio.
            </h1>
            <p className="mt-6 max-w-xl text-base text-foreground/75 sm:text-lg">
              Founder-adjacent work across Los Angeles. Every image selected for the library it was built to serve.
            </p>
          </div>
        </Container>
      </section>

      <section className="bg-foreground py-section text-background">
        <Container>
          <FadeIn>
            <p className="mx-auto max-w-3xl font-heading text-xl font-medium leading-relaxed tracking-tight text-background sm:text-3xl">
              Every frame is a commercial-grade decision. The studio does not snap. It directs. It composes. It executes. The session is the product. The photos are the receipt.
            </p>
          </FadeIn>
        </Container>
      </section>

      <section className="py-section">
        <Container>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 sm:gap-6 lg:grid-cols-3">
            {frames.map((frame, i) => (
              <FadeIn key={frame.src} delayMs={Math.min(i * 60, 480)}>
                <figure className="flex flex-col gap-3">
                  <div className="relative aspect-[4/5] w-full overflow-hidden bg-foreground/5">
                    <Image
                      src={frame.src}
                      alt={frame.alt}
                      fill
                      quality={95}
                      sizes="(min-width: 1024px) 33vw, (min-width: 640px) 50vw, 100vw"
                      className="object-cover object-center transition-transform duration-500 hover:scale-[1.02]"
                    />
                  </div>
                  <figcaption className="text-xs text-muted leading-relaxed">
                    {frame.caption}
                  </figcaption>
                </figure>
              </FadeIn>
            ))}
          </div>
        </Container>
      </section>

      <section className="border-t border-border bg-foreground py-section text-background">
        <Container>
          <div className="max-w-3xl">
            <h2 className="font-heading text-3xl font-medium tracking-tight text-balance sm:text-4xl">
              Ready to build your own library?
            </h2>
            <p className="mt-6 max-w-2xl text-base text-background/75">
              One structured shoot. 60 to 80 deployed-ready images. A 12-month deployment plan.
            </p>
            <div className="mt-10 flex flex-wrap items-center gap-6">
              <Link
                href="/book"
                className="inline-flex h-14 items-center justify-center bg-background px-8 text-base font-semibold text-foreground transition-colors hover:bg-background/90"
              >
                Book a Qualifying Call
              </Link>
              <Link
                href="/kit"
                className="text-sm text-background/70 underline decoration-background/30 underline-offset-4 transition-colors hover:text-background hover:decoration-background"
              >
                See the full Kit
              </Link>
            </div>
          </div>
        </Container>
      </section>
    </>
  );
}
