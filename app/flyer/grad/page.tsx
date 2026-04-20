import type { Metadata } from "next";
import { GRAD_VARIANTS } from "../_shared/gradFlyer";

export const metadata: Metadata = {
  title: "Grad Flyer Variants",
  robots: { index: false, follow: false },
};

const variants = [
  GRAD_VARIANTS.hero,
  GRAD_VARIANTS.mascot,
  GRAD_VARIANTS.editorial,
  GRAD_VARIANTS.family,
];

export default function GradFlyerIndexPage() {
  return (
    <div className="min-h-screen bg-foreground px-6 py-16 text-background">
      <div className="mx-auto max-w-6xl">
        <div className="text-center">
          <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-background/60">
            Internal · Flyer A/B Variants
          </span>
          <h1 className="mt-3 font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
            Grad Season 2026 · IG Story Flyers
          </h1>
          <p className="mt-3 text-sm text-background/70">
            1080 × 1920 · Four photo variants, same layout. Test which stops scroll hardest.
          </p>
        </div>

        <div className="mt-12 grid gap-8 sm:grid-cols-2">
          {variants.map((v) => {
            const pngUrl = `/flyer/grad-${v.slug}/opengraph-image`;
            return (
              <div key={v.slug} className="flex flex-col gap-4">
                <div className="overflow-hidden rounded-xl border border-background/20 shadow-2xl">
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img
                    src={pngUrl}
                    alt={`Grad flyer · ${v.label}`}
                    width={1080}
                    height={1920}
                    className="block h-auto w-full"
                  />
                </div>
                <div className="flex flex-col gap-1">
                  <div className="flex items-baseline justify-between gap-3">
                    <span className="font-heading text-lg font-semibold tracking-tight">
                      {v.label}
                    </span>
                    <span className="font-heading text-[10px] font-semibold tracking-[0.3em] uppercase text-background/50">
                      {v.slug}
                    </span>
                  </div>
                  <p className="text-sm text-background/70">{v.note}</p>
                </div>
                <a
                  href={pngUrl}
                  download={`sniped-media-grad-${v.slug}.png`}
                  className="inline-flex h-11 items-center justify-center rounded-md bg-background px-5 text-sm font-semibold text-foreground transition-colors hover:bg-background/90"
                >
                  Download {v.label} PNG
                </a>
              </div>
            );
          })}
        </div>

        <div className="mt-16 max-w-2xl text-sm leading-relaxed text-background/70">
          <p>
            Tip: post the same caption across all four as stories, watch which one people
            tap through from, then promote the winner as a reel or feed ad. Layout and copy
            are identical on purpose so the only variable is the photo.
          </p>
        </div>
      </div>
    </div>
  );
}
