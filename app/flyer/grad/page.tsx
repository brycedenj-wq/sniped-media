import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Grad Flyer",
  robots: { index: false, follow: false },
};

export default function GradFlyerPage() {
  return (
    <div className="min-h-screen bg-foreground px-6 py-16 text-background">
      <div className="mx-auto flex max-w-3xl flex-col items-center gap-8">
        <div className="text-center">
          <span className="font-heading text-xs font-semibold tracking-[0.4em] uppercase text-background/60">
            Internal · Flyer Preview
          </span>
          <h1 className="mt-3 font-heading text-3xl font-semibold tracking-tight sm:text-4xl">
            Grad Season 2026 · IG Story Flyer
          </h1>
          <p className="mt-3 text-sm text-background/70">
            1080 × 1920 · Story + Reel ad ready
          </p>
        </div>

        <div className="w-full max-w-sm overflow-hidden rounded-xl border border-background/20 shadow-2xl">
          {/* Live preview image. Loads from /flyer/grad/opengraph-image */}
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src="/flyer/grad/opengraph-image"
            alt="Grad season 2026 flyer"
            width={1080}
            height={1920}
            className="block h-auto w-full"
          />
        </div>

        <div className="flex flex-col items-center gap-3">
          <a
            href="/flyer/grad/opengraph-image"
            download="sniped-media-grad-flyer.png"
            className="inline-flex h-12 items-center justify-center rounded-md bg-background px-6 text-sm font-semibold text-foreground transition-colors hover:bg-background/90"
          >
            Download PNG
          </a>
          <p className="text-xs text-background/55">
            Right-click the image above &rarr; Save As, or use the button.
          </p>
        </div>
      </div>
    </div>
  );
}
