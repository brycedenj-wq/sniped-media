import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    qualities: [75, 95],
  },
  async redirects() {
    return [
      { source: "/kit", destination: "/", permanent: false },
      { source: "/work", destination: "/", permanent: false },
      { source: "/about", destination: "/", permanent: false },
      { source: "/book", destination: "/", permanent: false },
    ];
  },
};

export default nextConfig;
