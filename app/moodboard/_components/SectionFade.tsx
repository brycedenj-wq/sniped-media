"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";

type SectionFadeProps = {
  children: ReactNode;
  className?: string;
};

// Lightweight intersection-driven fade. 200ms per spec.
// Respects prefers-reduced-motion.
export function SectionFade({ children, className = "" }: SectionFadeProps) {
  const ref = useRef<HTMLDivElement>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const node = ref.current;
    if (!node) return;

    if (
      typeof window === "undefined" ||
      typeof IntersectionObserver === "undefined"
    ) {
      setVisible(true);
      return;
    }

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      setVisible(true);
      return;
    }

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setVisible(true);
        }
      },
      { threshold: 0.25 }
    );

    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  return (
    <div
      ref={ref}
      className={`transition-[opacity,transform] duration-200 ease-out ${
        visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-3"
      } ${className}`}
    >
      {children}
    </div>
  );
}
