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
        <SiteHeader />
        <main className="flex-1">{children}</main>
        <SiteFooter />
      </body>
    </html>
  );
}
