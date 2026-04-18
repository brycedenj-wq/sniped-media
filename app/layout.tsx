import type { Metadata } from "next";
import { Inter, Space_Grotesk } from "next/font/google";
import { SiteHeader } from "./_components/SiteHeader";
import { SiteFooter } from "./_components/SiteFooter";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const spaceGrotesk = Space_Grotesk({
  variable: "--font-space-grotesk",
  subsets: ["latin"],
  display: "swap",
});

const SITE_URL = "https://snipedmedia.com";
const SITE_NAME = "Sniped Media";
const SITE_DESCRIPTION =
  "Expertly directed portraits and reliable event coverage in Los Angeles. Transparent pricing, seamless delivery, and a direct path to booking.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "Sniped Media | High-Impact Los Angeles Photography",
    template: "%s | Sniped Media",
  },
  description: SITE_DESCRIPTION,
  applicationName: SITE_NAME,
  keywords: [
    "Los Angeles photographer",
    "LA portrait photography",
    "headshots Los Angeles",
    "lifestyle photography",
    "event photography",
  ],
  openGraph: {
    type: "website",
    locale: "en_US",
    url: SITE_URL,
    siteName: SITE_NAME,
    title: "Sniped Media | High-Impact Los Angeles Photography",
    description: SITE_DESCRIPTION,
  },
  twitter: {
    card: "summary_large_image",
    title: "Sniped Media | High-Impact Los Angeles Photography",
    description: SITE_DESCRIPTION,
  },
  robots: { index: true, follow: true },
};

const localBusinessJsonLd = {
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": `${SITE_URL}#business`,
  name: SITE_NAME,
  url: SITE_URL,
  description: SITE_DESCRIPTION,
  image: `${SITE_URL}/opengraph-image`,
  logo: `${SITE_URL}/icon.svg`,
  priceRange: "$275 - $1,200+",
  areaServed: [
    { "@type": "City", name: "Los Angeles" },
    { "@type": "State", name: "California" },
  ],
  address: {
    "@type": "PostalAddress",
    addressLocality: "Los Angeles",
    addressRegion: "CA",
    addressCountry: "US",
  },
  makesOffer: [
    {
      "@type": "Offer",
      name: "The Baseline",
      price: "275",
      priceCurrency: "USD",
      description:
        "45-minute expertly directed session, one location, 5 final retouched images.",
    },
    {
      "@type": "Offer",
      name: "The Standard",
      price: "550",
      priceCurrency: "USD",
      description:
        "Up to 90 minutes of dedicated direction with multiple looks, 15 to 20 final retouched images.",
    },
    {
      "@type": "Offer",
      name: "Event Coverage",
      price: "1200",
      priceCurrency: "USD",
      description:
        "4 hours of comprehensive coverage, 50+ final delivered images.",
    },
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${spaceGrotesk.variable} scroll-smooth h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-background text-foreground selection:bg-foreground selection:text-background">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(localBusinessJsonLd) }}
        />
        <SiteHeader />
        <main className="flex-1">{children}</main>
        <SiteFooter />
      </body>
    </html>
  );
}
