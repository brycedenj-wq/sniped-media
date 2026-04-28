import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { Container } from "../_components/Container";
import { FadeIn } from "../_components/FadeIn";

export const metadata: Metadata = {
  title: "Selected Work",
  description: "Selected work by Sniped Media. Los Angeles.",
  openGraph: {
    title: "Selected Work | Sniped Media",
    description: "Selected work by Sniped Media. Los Angeles.",
    url: "/work",
  },
  robots: { index: false, follow: false },
};

type Frame = {
  src: string;
  alt: string;
  aspect: string; // tailwind aspect-ratio class
  span: string; // tailwind col-span class for desktop
};

const frames: Frame[] = [
  {
    src: "/images/portfolio-1.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[3/4]",
    span: "lg:col-span-4",
  },
  {
    src: "/images/portfolio-2.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[4/3]",
    span: "lg:col-span-8",
  },
  {
    src: "/images/portfolio-3.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[4/5]",
    span: "lg:col-span-12",
  },
  {
    src: "/images/portfolio-4.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-square",
    span: "lg:col-span-4",
  },
  {
    src: "/images/portfolio-5.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[3/4]",
    span: "lg:col-span-4",
  },
  {
    src: "/images/portfolio-7.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[3/4]",
    span: "lg:col-span-4",
  },
  {
    src: "/images/portfolio-6.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[4/3]",
    span: "lg:col-span-8",
  },
  {
    src: "/images/portfolio-8.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-square",
    span: "lg:col-span-4",
  },
  {
    src: "/images/portfolio-9.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[4/3]",
    span: "lg:col-span-8",
  },
  {
    src: "/images/portfolio-10.jpg",
    alt: "Portrait — Sniped Media",
    aspect: "aspect-[3/4]",
    span: "lg:col-span-4",
  },
];

export default function WorkPage() {
  return (
    <div className="min-h-screen bg-foreground text-background">
      {/* Minimal top: back link + corner tag */}
      <header className="relative flex items-center justify-between px-6 py-6 sm:px-10 sm:py-8">
        <Link
          href="/"
          className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 transition-colors hover:text-accent-bright tabular-nums"
        >
          ← Sniped Media
        </Link>
        <div className="hidden items-center gap-4 font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 tabular-nums sm:flex">
          <span>Los Angeles</span>
          <span className="h-px w-10 bg-background/30" />
          <span>Selected Work</span>
        </div>
      </header>

      {/* The work — varied editorial mosaic */}
      <section className="px-6 pb-24 pt-4 sm:px-10 sm:pb-32 sm:pt-8 lg:px-16">
        <div className="mx-auto grid max-w-7xl grid-cols-1 gap-3 sm:gap-4 lg:grid-cols-12 lg:gap-5">
          {frames.map((f, i) => (
            <FadeIn
              key={f.src}
              delayMs={Math.min(i * 80, 480)}
              className={`col-span-1 ${f.span}`}
            >
              <figure
                className={`relative w-full overflow-hidden bg-background/5 ${f.aspect}`}
              >
                <Image
                  src={f.src}
                  alt={f.alt}
                  fill
                  quality={92}
                  sizes="(min-width: 1024px) 66vw, 100vw"
                  priority={i < 2}
                  className="object-cover object-center"
                />
              </figure>
            </FadeIn>
          ))}
        </div>
      </section>

      {/* Minimal closing — email + back link only */}
      <footer className="border-t border-background/10 px-6 py-12 sm:px-10">
        <div className="mx-auto flex max-w-7xl flex-col items-center gap-6 text-center sm:flex-row sm:justify-between sm:text-left">
          <a
            href="mailto:hello@snipedmedia.com"
            className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/85 underline decoration-background/30 underline-offset-4 transition-colors hover:text-accent-bright hover:decoration-accent-bright tabular-nums"
          >
            hello@snipedmedia.com
          </a>
          <Link
            href="/"
            className="font-heading text-[11px] font-semibold tracking-[0.3em] uppercase text-background/55 transition-colors hover:text-accent-bright tabular-nums"
          >
            ← Sniped Media
          </Link>
        </div>
      </footer>
    </div>
  );
}
