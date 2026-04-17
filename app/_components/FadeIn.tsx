"use client";

import { useEffect, useRef, useState, type HTMLAttributes } from "react";

type FadeInProps = HTMLAttributes<HTMLDivElement> & {
  delayMs?: number;
  threshold?: number;
};

export function FadeIn({
  className = "",
  children,
  delayMs = 0,
  threshold = 0.15,
  ...rest
}: FadeInProps) {
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
          observer.disconnect();
        }
      },
      { threshold, rootMargin: "0px 0px -40px 0px" }
    );

    observer.observe(node);
    return () => observer.disconnect();
  }, [threshold]);

  return (
    <div
      ref={ref}
      style={{ transitionDelay: delayMs ? `${delayMs}ms` : undefined }}
      className={`transition-[opacity,transform] duration-700 ease-out will-change-[opacity,transform] ${
        visible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
      } ${className}`.trim()}
      {...rest}
    >
      {children}
    </div>
  );
}
