import { ImageResponse } from "next/og";

export const alt = "Sniped Media | High-Impact Los Angeles Photography";
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

type LoadedFont = { name: string; data: ArrayBuffer; weight: 400 | 500 | 600 | 700; style: "normal" };

export default async function OpengraphImage() {
  const [spaceGrotesk700, inter500, inter400] = await Promise.all([
    loadGoogleFont("Space Grotesk", 700),
    loadGoogleFont("Inter", 500),
    loadGoogleFont("Inter", 400),
  ]);

  const fonts: LoadedFont[] = [];
  if (spaceGrotesk700) fonts.push({ name: "Space Grotesk", data: spaceGrotesk700, weight: 700, style: "normal" });
  if (inter500) fonts.push({ name: "Inter", data: inter500, weight: 500, style: "normal" });
  if (inter400) fonts.push({ name: "Inter", data: inter400, weight: 400, style: "normal" });

  const headingFont = spaceGrotesk700 ? "Space Grotesk" : "system-ui, sans-serif";
  const bodyFont = inter400 ? "Inter" : "system-ui, sans-serif";

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          background: "#121212",
          color: "#fafafa",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          padding: "80px",
          fontFamily: bodyFont,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: "20px" }}>
          <div
            style={{
              width: "56px",
              height: "56px",
              borderRadius: "12px",
              background: "#fafafa",
              color: "#121212",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontSize: "36px",
              fontWeight: 700,
              fontFamily: headingFont,
            }}
          >
            S
          </div>
          <span
            style={{
              fontSize: "24px",
              fontWeight: 500,
              letterSpacing: "6px",
              textTransform: "uppercase",
              fontFamily: headingFont,
            }}
          >
            Sniped Media
          </span>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: "28px" }}>
          <div
            style={{
              fontSize: "108px",
              fontWeight: 700,
              lineHeight: 1.02,
              letterSpacing: "-3px",
              display: "flex",
              flexDirection: "column",
              fontFamily: headingFont,
            }}
          >
            <span>Capture the Moment.</span>
            <span>Skip the Friction.</span>
          </div>
          <div
            style={{
              fontSize: "30px",
              color: "rgba(250,250,250,0.72)",
              maxWidth: "900px",
              lineHeight: 1.4,
              fontWeight: 400,
            }}
          >
            High-impact Los Angeles photography. Transparent pricing, seamless delivery.
          </div>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            fontSize: "18px",
            color: "rgba(250,250,250,0.55)",
            letterSpacing: "4px",
            textTransform: "uppercase",
            fontWeight: 500,
          }}
        >
          <span>Los Angeles, CA</span>
          <span>snipedmedia.com</span>
        </div>
      </div>
    ),
    { ...size, fonts: fonts.length > 0 ? fonts : undefined }
  );
}
