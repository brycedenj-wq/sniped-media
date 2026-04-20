import fs from "node:fs/promises";
import path from "node:path";
import { ImageResponse } from "next/og";

export const flyerSize = { width: 1080, height: 1920 };
export const flyerContentType = "image/png";

export type GradVariant = {
  slug: "hero" | "mascot" | "editorial" | "family";
  label: string;
  note: string;
  photoFile: string;
  photoPosition: string;
  overlay: "default" | "heavy" | "light";
};

export const GRAD_VARIANTS: Record<GradVariant["slug"], GradVariant> = {
  hero: {
    slug: "hero",
    label: "Hero",
    note: "Cinematic arches. Brand-matching atmosphere.",
    photoFile: "grad-hero.jpg",
    photoPosition: "top center",
    overlay: "default",
  },
  mascot: {
    slug: "mascot",
    label: "Mascot",
    note: "LMU lion. Local campus social proof.",
    photoFile: "grad-work-2.jpg",
    photoPosition: "center center",
    overlay: "heavy",
  },
  editorial: {
    slug: "editorial",
    label: "Editorial",
    note: "On-location portrait. Craft signal.",
    photoFile: "grad-work-1.jpg",
    photoPosition: "center center",
    overlay: "default",
  },
  family: {
    slug: "family",
    label: "Family",
    note: "Studio with family. Hooks the parent paying.",
    photoFile: "grad-work-3.jpg",
    photoPosition: "center center",
    overlay: "default",
  },
};

async function loadPhotoAsDataUrl(filename: string): Promise<string> {
  const filePath = path.join(process.cwd(), "public/images/flyer", filename);
  const buffer = await fs.readFile(filePath);
  return `data:image/jpeg;base64,${buffer.toString("base64")}`;
}

async function loadGoogleFont(family: string, weight: number): Promise<ArrayBuffer | null> {
  try {
    const cssUrl = `https://fonts.googleapis.com/css2?family=${family.replace(/ /g, "+")}:wght@${weight}`;
    const cssResponse = await fetch(cssUrl, {
      headers: {
        "User-Agent":
          "Mozilla/5.0 (X11; Linux x86_64; rv:20.0) Gecko/20121202 Firefox/20.0",
      },
    });
    if (!cssResponse.ok) return null;
    const css = await cssResponse.text();
    const match =
      css.match(/src:\s*url\(([^)]+)\)\s+format\('truetype'\)/) ??
      css.match(/src:\s*url\(([^)]+)\)\s+format\('opentype'\)/) ??
      css.match(/src:\s*url\(([^)]+)\)\s+format\('woff'\)/);
    if (!match) return null;
    const fontResponse = await fetch(match[1]);
    if (!fontResponse.ok) return null;
    return await fontResponse.arrayBuffer();
  } catch {
    return null;
  }
}

type LoadedFont = {
  name: string;
  data: ArrayBuffer;
  weight: 400 | 500 | 600 | 700;
  style: "normal";
};

function gradientFor(overlay: GradVariant["overlay"]): string {
  switch (overlay) {
    case "heavy":
      return "linear-gradient(180deg, rgba(10,10,10,0.70) 0%, rgba(10,10,10,0.35) 35%, rgba(10,10,10,0.65) 70%, rgba(10,10,10,0.95) 100%)";
    case "light":
      return "linear-gradient(180deg, rgba(10,10,10,0.40) 0%, rgba(10,10,10,0.05) 35%, rgba(10,10,10,0.45) 70%, rgba(10,10,10,0.88) 100%)";
    case "default":
    default:
      return "linear-gradient(180deg, rgba(10,10,10,0.55) 0%, rgba(10,10,10,0.15) 35%, rgba(10,10,10,0.55) 70%, rgba(10,10,10,0.92) 100%)";
  }
}

export async function renderGradFlyer(variant: GradVariant): Promise<ImageResponse> {
  const [sg700, sg500, inter500, inter400, photoDataUrl] = await Promise.all([
    loadGoogleFont("Space Grotesk", 700),
    loadGoogleFont("Space Grotesk", 500),
    loadGoogleFont("Inter", 500),
    loadGoogleFont("Inter", 400),
    loadPhotoAsDataUrl(variant.photoFile),
  ]);

  const fonts: LoadedFont[] = [];
  if (sg700) fonts.push({ name: "Space Grotesk", data: sg700, weight: 700, style: "normal" });
  if (sg500) fonts.push({ name: "Space Grotesk", data: sg500, weight: 500, style: "normal" });
  if (inter500) fonts.push({ name: "Inter", data: inter500, weight: 500, style: "normal" });
  if (inter400) fonts.push({ name: "Inter", data: inter400, weight: 400, style: "normal" });

  const heading = sg700 ? "Space Grotesk" : "system-ui, sans-serif";
  const body = inter400 ? "Inter" : "system-ui, sans-serif";

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          position: "relative",
          background: "#0a0a0a",
          color: "#fafafa",
          fontFamily: body,
        }}
      >
        <img
          src={photoDataUrl}
          width={1080}
          height={1920}
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            objectFit: "cover",
            objectPosition: variant.photoPosition,
            opacity: 0.72,
          }}
        />

        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            display: "flex",
            background: gradientFor(variant.overlay),
          }}
        />

        <div
          style={{
            position: "relative",
            width: "100%",
            height: "100%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            padding: "140px 90px 160px",
          }}
        >
          <div style={{ display: "flex", flexDirection: "column", gap: "24px" }}>
            <div
              style={{
                fontFamily: heading,
                fontWeight: 500,
                fontSize: "28px",
                letterSpacing: "8px",
                textTransform: "uppercase",
                color: "rgba(250,250,250,0.85)",
                display: "flex",
              }}
            >
              Now Streaming · LA Grad Season 2026
            </div>
            <div
              style={{
                width: "120px",
                height: "2px",
                background: "rgba(250,250,250,0.55)",
                display: "flex",
              }}
            />
          </div>

          <div style={{ display: "flex", flexDirection: "column", gap: "40px" }}>
            <div
              style={{
                fontFamily: heading,
                fontWeight: 700,
                fontSize: "248px",
                lineHeight: 0.9,
                letterSpacing: "-8px",
                display: "flex",
                flexDirection: "column",
              }}
            >
              <span>Roll</span>
              <span>Credits.</span>
            </div>
            <div
              style={{
                fontSize: "38px",
                lineHeight: 1.35,
                fontWeight: 400,
                color: "rgba(250,250,250,0.85)",
                maxWidth: "820px",
                display: "flex",
                flexDirection: "column",
              }}
            >
              <span>Cinematic graduation portraits.</span>
              <span>DTLA studio or your LA campus.</span>
            </div>
          </div>

          <div style={{ display: "flex", flexDirection: "column", gap: "48px" }}>
            <div
              style={{
                display: "flex",
                flexDirection: "row",
                gap: "32px",
                alignItems: "stretch",
              }}
            >
              <div
                style={{
                  flex: 1,
                  display: "flex",
                  flexDirection: "column",
                  padding: "28px 32px",
                  border: "2px solid rgba(250,250,250,0.7)",
                  gap: "10px",
                }}
              >
                <span
                  style={{
                    fontFamily: heading,
                    fontSize: "22px",
                    fontWeight: 500,
                    letterSpacing: "5px",
                    textTransform: "uppercase",
                    color: "rgba(250,250,250,0.7)",
                    display: "flex",
                  }}
                >
                  Short Film
                </span>
                <span
                  style={{
                    fontFamily: heading,
                    fontSize: "56px",
                    fontWeight: 700,
                    letterSpacing: "-1px",
                    display: "flex",
                  }}
                >
                  $275
                </span>
                <span
                  style={{
                    fontSize: "22px",
                    color: "rgba(250,250,250,0.75)",
                    display: "flex",
                  }}
                >
                  45 min · 5 retouched
                </span>
              </div>
              <div
                style={{
                  flex: 1,
                  display: "flex",
                  flexDirection: "column",
                  padding: "28px 32px",
                  background: "#fafafa",
                  color: "#0a0a0a",
                  gap: "10px",
                }}
              >
                <span
                  style={{
                    fontFamily: heading,
                    fontSize: "22px",
                    fontWeight: 500,
                    letterSpacing: "5px",
                    textTransform: "uppercase",
                    color: "rgba(10,10,10,0.6)",
                    display: "flex",
                  }}
                >
                  Feature Length
                </span>
                <span
                  style={{
                    fontFamily: heading,
                    fontSize: "56px",
                    fontWeight: 700,
                    letterSpacing: "-1px",
                    display: "flex",
                  }}
                >
                  $550
                </span>
                <span
                  style={{
                    fontSize: "22px",
                    color: "rgba(10,10,10,0.7)",
                    display: "flex",
                  }}
                >
                  90 min · 15 to 20 retouched
                </span>
              </div>
            </div>

            <div
              style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "flex-start",
                gap: "18px",
              }}
            >
              <div
                style={{
                  fontFamily: heading,
                  fontSize: "34px",
                  fontWeight: 700,
                  letterSpacing: "2px",
                  textTransform: "uppercase",
                  color: "#fafafa",
                  display: "flex",
                }}
              >
                DM &ldquo;GRAD&rdquo; to lock your spot
              </div>
              <div
                style={{
                  display: "flex",
                  flexDirection: "row",
                  justifyContent: "space-between",
                  alignItems: "center",
                  width: "100%",
                }}
              >
                <span
                  style={{
                    fontSize: "26px",
                    color: "rgba(250,250,250,0.85)",
                    display: "flex",
                  }}
                >
                  @sniped.media
                </span>
                <span
                  style={{
                    fontFamily: heading,
                    fontSize: "20px",
                    fontWeight: 500,
                    letterSpacing: "6px",
                    textTransform: "uppercase",
                    color: "rgba(250,250,250,0.65)",
                    display: "flex",
                  }}
                >
                  Sniped Media
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    ),
    { ...flyerSize, fonts: fonts.length > 0 ? fonts : undefined }
  );
}
