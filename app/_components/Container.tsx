import type { HTMLAttributes } from "react";

type ContainerProps = HTMLAttributes<HTMLDivElement>;

export function Container({ className = "", children, ...rest }: ContainerProps) {
  return (
    <div
      className={`mx-auto w-full max-w-7xl px-6 sm:px-8 ${className}`.trim()}
      {...rest}
    >
      {children}
    </div>
  );
}
