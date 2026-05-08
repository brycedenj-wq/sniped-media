import { ImageResponse } from "next/og";
import { readFile } from "node:fs/promises";
import { join } from "node:path";

export const alt = "Selected Work, Sniped Media";
export const size = { width: 1200, height: 630 };
export const contentType = "image/jpeg";

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

export default async function OpengraphImage() {
  const [spaceGrotesk700, spaceGrotesk500, photoBuffer] = await Promise.all([
    loadGoogleFont("Space Grotesk", 700),
    loadGoogleFont("Space Grotesk", 500),
    readFile(join(process.cwd(), "public/images/portfolio-3.jpg")),
  ]);

  const fonts: LoadedFont[] = [];
  if (spaceGrotesk700)
    fonts.push({ name: "Space Grotesk", data: spaceGrotesk700, weight: 700, style: "normal" });
  if (spaceGrotesk500)
    fonts.push({ name: "Space Grotesk", data: spaceGrotesk500, weight: 500, style: "normal" });

  const headingFont = spaceGrotesk700 ? "Space Grotesk" : "system-ui, sans-serif";

  const photoBase64 = photoBuffer.toString("base64");
  const photoSrc = `data:image/jpeg;base64,${photoBase64}`;

  const ink = "#141414";
  const paper = "#F5F3EE";
  const paperMuted = "rgba(245, 243, 238, 0.7)";
  const accent = "#A67D2B";

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          background: ink,
          color: paper,
          display: "flex",
          fontFamily: headingFont,
          position: "relative",
        }}
      >
        {/* Full-bleed lead photo */}
        <img
          src={photoSrc}
          alt=""
          width={1200}
          height={630}
          style={{
            position: "absolute",
            inset: 0,
            width: "100%",
            height: "100%",
            objectFit: "cover",
            objectPosition: "center 30%",
          }}
        />

        {/* Top scrim for legibility */}
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            height: "180px",
            background:
              "linear-gradient(to bottom, rgba(20,20,20,0.78) 0%, rgba(20,20,20,0) 100%)",
          }}
        />

        {/* Bottom scrim for legibility */}
        <div
          style={{
            position: "absolute",
            bottom: 0,
            left: 0,
            right: 0,
            height: "260px",
            background:
              "linear-gradient(to top, rgba(20,20,20,0.92) 0%, rgba(20,20,20,0) 100%)",
          }}
        />

        {/* Top bar */}
        <div
          style={{
            position: "absolute",
            top: "44px",
            left: "70px",
            right: "70px",
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
          }}
        >
          <span
            style={{
              fontSize: "20px",
              fontWeight: 700,
              letterSpacing: "6px",
              textTransform: "uppercase",
              color: paper,
            }}
          >
            Sniped Media
          </span>
          <div style={{ display: "flex", alignItems: "center", gap: "22px" }}>
            <span
              style={{
                fontSize: "16px",
                fontWeight: 700,
                letterSpacing: "5px",
                textTransform: "uppercase",
                color: paperMuted,
              }}
            >
              Los Angeles
            </span>
            <span
              style={{
                width: "44px",
                height: "1px",
                background: "rgba(245, 243, 238, 0.4)",
              }}
            />
            <span
              style={{
                fontSize: "16px",
                fontWeight: 700,
                letterSpacing: "5px",
                textTransform: "uppercase",
                color: paperMuted,
              }}
            >
              Studio
            </span>
          </div>
        </div>

        {/* Bottom block: section label + headline + footer */}
        <div
          style={{
            position: "absolute",
            left: "70px",
            right: "70px",
            bottom: "44px",
            display: "flex",
            flexDirection: "column",
            gap: "18px",
          }}
        >
          <span
            style={{
              fontSize: "18px",
              fontWeight: 700,
              letterSpacing: "8px",
              textTransform: "uppercase",
              color: accent,
            }}
          >
            Selected Work
          </span>
          <span
            style={{
              fontSize: "112px",
              fontWeight: 700,
              lineHeight: 0.95,
              letterSpacing: "-4px",
              color: paper,
            }}
          >
            Commercial Portrait.
          </span>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "space-between",
              marginTop: "8px",
            }}
          >
            <span
              style={{
                fontSize: "16px",
                fontWeight: 700,
                letterSpacing: "5px",
                textTransform: "uppercase",
                color: paperMuted,
              }}
            >
              hello@snipedmedia.com
            </span>
            <span
              style={{
                fontSize: "16px",
                fontWeight: 700,
                letterSpacing: "5px",
                textTransform: "uppercase",
                color: paperMuted,
              }}
            >
              snipedmedia.com
            </span>
          </div>
        </div>
      </div>
    ),
    { ...size, fonts: fonts.length > 0 ? fonts : undefined }
  );
}
