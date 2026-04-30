import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Image from "next/image";
import fs from "node:fs";
import path from "node:path";
import { palettes, paletteSlugs, POSE_RULE_LIST } from "../_data/palettes";
import { LightingDiagram } from "../_components/LightingDiagram";
import { PoseDiagram } from "../_components/PoseDiagram";
import { TextureFallback } from "../_components/TextureFallback";
import { SectionFade } from "../_components/SectionFade";

export function generateStaticParams() {
  return paletteSlugs.map((slug) => ({ slug }));
}

export const dynamicParams = false;

type Params = { slug: string };

export async function generateMetadata(props: {
  params: Promise<Params>;
}): Promise<Metadata> {
  const { slug } = await props.params;
  const p = palettes[slug];
  if (!p) return { title: "Moodboard", robots: { index: false, follow: false } };
  return {
    title: `Moodboard / ${p.hero.replace(".", "")}`,
    description: p.concept,
    openGraph: {
      title: `Moodboard / ${p.hero.replace(".", "")} | Sniped Media`,
      description: p.concept,
      url: `/moodboard/${p.slug}`,
    },
    robots: { index: false, follow: false },
  };
}

export default async function MoodboardPage(props: {
  params: Promise<Params>;
}) {
  const { slug } = await props.params;
  const p = palettes[slug];
  if (!p) notFound();

  const sectionClass =
    "relative flex h-screen w-full snap-start snap-always items-center justify-center overflow-hidden";

  // Texture image is optional. Only render the Image component if the file
  // actually exists at build time. Otherwise the layered CSS fallback carries
  // the section. Drop AI-rendered textures into /public/images/moodboard/
  // and the page picks them up automatically on next build.
  const textureFsPath = path.join(process.cwd(), "public", p.textureSrc);
  const textureExists = fs.existsSync(textureFsPath);

  return (
    <main className="h-screen w-full snap-y snap-mandatory overflow-y-scroll bg-foreground text-background">
      {/* SECTION 1 — WASH */}
      <section
        className={sectionClass}
        style={{ backgroundColor: p.washColor, color: p.washTextColor }}
      >
        <div
          aria-hidden="true"
          className="pointer-events-none absolute inset-0 mix-blend-multiply opacity-[0.08]"
          style={{
            backgroundImage: `radial-gradient(circle at 25% 30%, currentColor 1px, transparent 1px), radial-gradient(circle at 75% 70%, currentColor 1px, transparent 1px)`,
            backgroundSize: "8px 8px, 12px 12px",
          }}
        />
        <SectionFade className="relative px-6 text-center sm:px-10">
          <h1
            className="font-heading font-bold leading-none tracking-[-0.04em]"
            style={{
              fontSize: "clamp(120px, 24vw, 320px)",
              color: p.washTextColor,
            }}
          >
            {p.hero}
          </h1>
        </SectionFade>
      </section>

      {/* SECTION 2 — CONCEPT */}
      <section className={`${sectionClass} bg-foreground`}>
        <SectionFade className="mx-auto max-w-5xl px-6 sm:px-10">
          <p
            className="font-heading font-medium leading-[1.05] tracking-tight text-balance text-background"
            style={{ fontSize: "clamp(36px, 6vw, 96px)" }}
          >
            {p.concept}
          </p>
          <div className="mt-12 space-y-2 font-heading text-base font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-xl">
            <p>
              {p.shootLabel} / {p.shootDate}
            </p>
            <p>{p.callTime}</p>
            <p>{p.location}</p>
          </div>
        </SectionFade>
      </section>

      {/* SECTION 3 — PALETTE */}
      <section className={`${sectionClass} bg-foreground`}>
        <div className="mx-auto flex h-full w-full max-w-7xl flex-col px-6 py-section sm:px-10">
          <SectionFade>
            <div className="space-y-2 font-heading text-base font-semibold uppercase tracking-[0.3em] text-background/65 tabular-nums sm:text-lg">
              {p.paletteIntro.map((line) => (
                <p key={line}>{line}</p>
              ))}
            </div>
          </SectionFade>

          <div className="mt-12 grid flex-1 grid-cols-5 gap-2 sm:gap-3">
            {p.swatches.map((s, i) => (
              <SectionFade key={s.hex} className="flex h-full flex-col">
                <div
                  className="flex-1 border border-background/10"
                  style={{ backgroundColor: s.hex, transitionDelay: `${i * 60}ms` }}
                />
                <div className="mt-3 space-y-1 sm:mt-4">
                  <p className="font-heading text-xs font-semibold uppercase tracking-[0.25em] text-background sm:text-sm">
                    {s.name}
                  </p>
                  <p className="font-heading text-[10px] font-semibold uppercase tracking-[0.2em] text-background/55 tabular-nums sm:text-xs">
                    {s.hex}
                  </p>
                </div>
              </SectionFade>
            ))}
          </div>
        </div>
      </section>

      {/* SECTION 4 — TEXTURE */}
      <section className={`${sectionClass} bg-foreground`}>
        <TextureFallback baseColor={p.washColor} />
        {textureExists ? (
          <Image
            src={p.textureSrc}
            alt=""
            fill
            quality={88}
            sizes="100vw"
            className="object-cover object-center"
          />
        ) : null}
        <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-foreground/90 via-foreground/40 to-transparent">
          <div className="mx-auto max-w-7xl px-6 py-6 sm:px-10 sm:py-10">
            <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background tabular-nums sm:text-sm">
              {p.textureCaption}
            </p>
          </div>
        </div>
      </section>

      {/* SECTION 5 — LIGHTING */}
      <section className={`${sectionClass} bg-foreground`}>
        <SectionFade className="mx-auto flex w-full max-w-5xl flex-col items-center px-6 sm:px-10">
          <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-accent-bright tabular-nums sm:text-sm">
            § 05 / Lighting
          </p>
          <div className="mt-8 w-full">
            <LightingDiagram />
          </div>
          <div className="mt-12 grid w-full max-w-2xl grid-cols-1 gap-4 font-heading text-sm font-semibold uppercase tracking-[0.25em] text-background/85 tabular-nums sm:text-base">
            <p>
              <span className="text-accent-bright">KEY:</span> {p.lighting.key}
            </p>
            <p>
              <span className="text-accent-bright">RIM:</span> {p.lighting.rim}
            </p>
            <p>
              <span className="text-accent-bright">FILL:</span> {p.lighting.fill}
            </p>
          </div>
        </SectionFade>
      </section>

      {/* SECTION 6 — POSE ARCHITECTURE */}
      <section className={`${sectionClass} bg-foreground`}>
        <div className="mx-auto grid h-full w-full max-w-7xl grid-cols-1 items-center gap-12 px-6 py-section sm:px-10 lg:grid-cols-[auto_1fr] lg:gap-20">
          <SectionFade className="flex justify-center lg:justify-start">
            <PoseDiagram />
          </SectionFade>

          <SectionFade>
            <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-accent-bright tabular-nums sm:text-sm">
              § 06 / Pose Architecture
            </p>
            <ol className="mt-8 space-y-4 font-heading text-base font-medium uppercase tracking-[0.2em] text-background tabular-nums sm:text-lg">
              {POSE_RULE_LIST.map((rule, i) => (
                <li key={rule} className="flex items-start gap-4">
                  <span className="text-accent-bright">
                    {String(i + 1).padStart(2, "0")}.
                  </span>
                  <span>{rule}</span>
                </li>
              ))}
            </ol>
          </SectionFade>
        </div>
      </section>

      {/* SECTION 7 — WARDROBE */}
      <section className={`${sectionClass} bg-foreground items-start`}>
        <div className="mx-auto h-full w-full max-w-5xl overflow-y-auto px-6 py-section sm:px-10">
          <SectionFade>
            <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-accent-bright tabular-nums sm:text-sm">
              § 07 / Wardrobe
            </p>
            <h2 className="mt-6 font-heading text-3xl font-medium tracking-tight text-background sm:text-4xl">
              The brief.
            </h2>

            <div className="mt-12 space-y-10">
              <div>
                <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                  The Palette
                </p>
                <div className="mt-4 space-y-2 text-base text-background/85 leading-relaxed sm:text-lg">
                  {p.wardrobe.paletteCopy.map((line) => (
                    <p key={line}>{line}</p>
                  ))}
                </div>
              </div>

              <div>
                <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                  The Garments
                </p>
                <ol className="mt-4 space-y-3 text-base text-background/85 leading-relaxed tabular-nums sm:text-lg">
                  {p.wardrobe.garments.map((item, i) => (
                    <li key={item} className="flex items-start gap-4">
                      <span className="font-heading text-sm font-semibold text-background/55">
                        {String(i + 1).padStart(2, "0")}.
                      </span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ol>
              </div>

              <div>
                <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                  Restrictions
                </p>
                <ul className="mt-4 space-y-2 font-heading text-sm font-semibold uppercase tracking-[0.2em] text-background/85 tabular-nums sm:text-base">
                  {p.wardrobe.restrictions.map((line) => (
                    <li key={line}>— {line}</li>
                  ))}
                </ul>
              </div>

              <div>
                <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                  Jewelry
                </p>
                <div className="mt-4 space-y-2 text-base text-background/85 leading-relaxed sm:text-lg">
                  {p.wardrobe.jewelry.map((line) => (
                    <p key={line}>{line}</p>
                  ))}
                </div>
              </div>

              {p.wardrobe.footwear ? (
                <div>
                  <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                    Footwear
                  </p>
                  <div className="mt-4 space-y-2 text-base text-background/85 leading-relaxed sm:text-lg">
                    {p.wardrobe.footwear.map((line) => (
                      <p key={line}>{line}</p>
                    ))}
                  </div>
                </div>
              ) : null}

              {p.wardrobe.makeupNote ? (
                <div>
                  <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                    Makeup Note
                  </p>
                  <div className="mt-4 space-y-2 text-base text-background/85 leading-relaxed sm:text-lg">
                    {p.wardrobe.makeupNote.map((line) => (
                      <p key={line}>{line}</p>
                    ))}
                  </div>
                </div>
              ) : null}

              <div className="border-t border-background/15 pt-6">
                <p className="font-heading text-base font-semibold uppercase tracking-[0.3em] text-accent-bright tabular-nums sm:text-lg">
                  {p.wardrobe.bringPolicy}
                </p>
              </div>
            </div>
          </SectionFade>
        </div>
      </section>

      {/* SECTION 8 — TEAM DIRECTION */}
      <section className={`${sectionClass} bg-foreground items-start`}>
        <div className="mx-auto h-full w-full max-w-5xl overflow-y-auto px-6 py-section sm:px-10">
          <SectionFade>
            <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-accent-bright tabular-nums sm:text-sm">
              § 08 / Team Direction
            </p>
            <h2 className="mt-6 font-heading text-3xl font-medium tracking-tight text-background sm:text-4xl">
              Hair, makeup, attitude.
            </h2>

            <div className="mt-12 grid grid-cols-1 gap-10 lg:grid-cols-3 lg:gap-12">
              <div>
                <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                  Hair
                </p>
                <div className="mt-4 space-y-2 text-base text-background/85 leading-relaxed">
                  {p.teamDirection.hair.map((line) => (
                    <p key={line}>{line}</p>
                  ))}
                </div>
              </div>

              <div>
                <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                  Makeup
                </p>
                <div className="mt-4 space-y-2 text-base text-background/85 leading-relaxed">
                  {p.teamDirection.makeup.map((line) => (
                    <p key={line}>{line}</p>
                  ))}
                </div>
              </div>

              <div>
                <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/60 tabular-nums sm:text-sm">
                  Attitude
                </p>
                <div className="mt-4 space-y-2 text-base text-background/85 leading-relaxed">
                  {p.teamDirection.attitude.map((line) => (
                    <p key={line}>{line}</p>
                  ))}
                </div>
              </div>
            </div>
          </SectionFade>
        </div>
      </section>

      {/* SECTION 9 — CONTACT / SIGNATURE */}
      <section className={`${sectionClass} bg-foreground`}>
        <SectionFade className="mx-auto flex w-full max-w-3xl flex-col px-6 sm:px-10">
          <div className="space-y-10 text-background sm:space-y-12">
            <div>
              <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/55 tabular-nums sm:text-sm">
                Shot by
              </p>
              <p className="mt-3 font-heading text-3xl font-medium tracking-tight sm:text-4xl">
                Bryceden Jones
              </p>
            </div>
            <div>
              <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/55 tabular-nums sm:text-sm">
                Produced by
              </p>
              <p className="mt-3 font-heading text-3xl font-medium tracking-tight sm:text-4xl">
                Sniped Media
              </p>
            </div>
            <div>
              <p className="font-heading text-xs font-semibold uppercase tracking-[0.3em] text-background/55 tabular-nums sm:text-sm">
                Contact
              </p>
              <div className="mt-3 space-y-2 font-heading text-lg font-medium tracking-tight sm:text-xl">
                <a
                  href="mailto:hello@snipedmedia.com"
                  className="block text-background underline decoration-background/30 underline-offset-4 transition-colors hover:text-accent-bright hover:decoration-accent-bright"
                >
                  hello@snipedmedia.com
                </a>
                <a
                  href="https://snipedmedia.com"
                  className="block text-background underline decoration-background/30 underline-offset-4 transition-colors hover:text-accent-bright hover:decoration-accent-bright"
                >
                  snipedmedia.com
                </a>
              </div>
            </div>
          </div>

          <div className="mt-20 border-t border-background/10 pt-6">
            <p className="font-heading text-[10px] font-semibold uppercase tracking-[0.4em] text-background/45 tabular-nums">
              Sniped Media. Los Angeles.
            </p>
            <p className="mt-1 font-heading text-[10px] font-semibold uppercase tracking-[0.4em] text-background/45 tabular-nums">
              A visual media production studio.
            </p>
          </div>
        </SectionFade>
      </section>
    </main>
  );
}
