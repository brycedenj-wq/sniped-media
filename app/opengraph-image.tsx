import { ImageResponse } from "next/og";

export const alt = "Sniped Media — In Development";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

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
  const [spaceGrotesk700, spaceGrotesk500] = await Promise.all([
    loadGoogleFont("Space Grotesk", 700),
    loadGoogleFont("Space Grotesk", 500),
  ]);

  const fonts: LoadedFont[] = [];
  if (spaceGrotesk700)
    fonts.push({ name: "Space Grotesk", data: spaceGrotesk700, weight: 700, style: "normal" });
  if (spaceGrotesk500)
    fonts.push({ name: "Space Grotesk", data: spaceGrotesk500, weight: 500, style: "normal" });

  const headingFont = spaceGrotesk700 ? "Space Grotesk" : "system-ui, sans-serif";

  // Match site palette
  const ink = "#141414";
  const paper = "#F5F3EE";
  const paperMuted = "rgba(245, 243, 238, 0.55)";
  const accent = "#A67D2B";

  // Faint 12-col grid background
  const gridLines = Array.from({ length: 11 }).map((_, i) => {
    const left = `${((i + 1) * 100) / 12}%`;
    return (
      <div
        key={i}
        style={{
          position: "absolute",
          top: 0,
          bottom: 0,
          left,
          width: "1px",
          background: "rgba(245, 243, 238, 0.05)",
        }}
      />
    );
  });

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          background: ink,
          color: paper,
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          padding: "64px 80px",
          fontFamily: headingFont,
          position: "relative",
        }}
      >
        {gridLines}

        {/* Top bar: wordmark left, location/version right */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            position: "relative",
          }}
        >
          <span
            style={{
              fontSize: "18px",
              fontWeight: 700,
              letterSpacing: "5px",
              textTransform: "uppercase",
              color: paper,
            }}
          >
            Sniped Media
          </span>
          <div style={{ display: "flex", alignItems: "center", gap: "20px" }}>
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
                width: "40px",
                height: "1px",
                background: "rgba(245, 243, 238, 0.3)",
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
              V2.0 / On File
            </span>
          </div>
        </div>

        {/* Center: section marker + headline */}
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "32px",
            position: "relative",
          }}
        >
          <span
            style={{
              fontSize: "20px",
              fontWeight: 700,
              letterSpacing: "8px",
              textTransform: "uppercase",
              color: accent,
            }}
          >
            § 00 / In Development
          </span>
          <span
            style={{
              fontSize: "200px",
              fontWeight: 700,
              lineHeight: 0.95,
              letterSpacing: "-6px",
              color: paper,
            }}
          >
            Developing.
          </span>
          <span
            style={{
              fontSize: "26px",
              fontWeight: 500,
              lineHeight: 1.4,
              maxWidth: "900px",
              color: "rgba(245, 243, 238, 0.75)",
              letterSpacing: "0px",
            }}
          >
            The next version of Sniped Media is on the bench. Same studio. Same standard. New positioning underway.
          </span>
        </div>

        {/* Bottom: tap counter + url */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            position: "relative",
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
    ),
    { ...size, fonts: fonts.length > 0 ? fonts : undefined }
  );
}
