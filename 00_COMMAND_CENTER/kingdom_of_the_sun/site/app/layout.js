import "./globals.css";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";

export const metadata = {
  metadataBase: new URL("https://thekingdomofthesun.com"),
  title: {
    default: "Kingdom of the Sun · The Original. Since 1974.",
    template: "%s · Kingdom of the Sun",
  },
  description:
    "The Kingdom of the Sun is the original national high school holiday basketball tournament. 53rd Annual, December 28-31, 2026, Vanguard High School, Ocala, Florida.",
  openGraph: {
    title: "Kingdom of the Sun · The Original. Since 1974.",
    description:
      "The original national high school holiday basketball tournament. 53rd Annual, December 28-31, 2026, Ocala, Florida.",
    type: "website",
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Nav />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
