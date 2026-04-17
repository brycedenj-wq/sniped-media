import Link from "next/link";
import type { ComponentPropsWithoutRef } from "react";

type Variant = "primary" | "secondary";
type Size = "sm" | "md" | "lg";

type CtaButtonProps = Omit<ComponentPropsWithoutRef<typeof Link>, "href"> & {
  href?: string;
  variant?: Variant;
  size?: Size;
};

const base =
  "inline-flex items-center justify-center font-medium rounded-md transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-foreground focus-visible:ring-offset-2 focus-visible:ring-offset-background";

const variants: Record<Variant, string> = {
  primary: "bg-foreground text-background hover:bg-foreground/90",
  secondary:
    "bg-transparent text-foreground border border-foreground hover:bg-foreground hover:text-background",
};

const sizes: Record<Size, string> = {
  sm: "h-9 px-4 text-sm",
  md: "h-11 px-5 text-sm",
  lg: "h-14 px-8 text-base",
};

export function CtaButton({
  href = "/book",
  variant = "primary",
  size = "md",
  className = "",
  children,
  ...rest
}: CtaButtonProps) {
  return (
    <Link
      href={href}
      className={`${base} ${variants[variant]} ${sizes[size]} ${className}`.trim()}
      {...rest}
    >
      {children}
    </Link>
  );
}
