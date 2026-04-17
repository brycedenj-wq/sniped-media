import { Hero } from "./_components/sections/Hero";
import { WorkTeaser } from "./_components/sections/WorkTeaser";
import { OperatorPromise } from "./_components/sections/OperatorPromise";
import { PricingAnchor } from "./_components/sections/PricingAnchor";
import { FadeIn } from "./_components/FadeIn";

export default function HomePage() {
  return (
    <>
      <Hero />
      <FadeIn>
        <WorkTeaser />
      </FadeIn>
      <FadeIn>
        <OperatorPromise />
      </FadeIn>
      <FadeIn>
        <PricingAnchor />
      </FadeIn>
    </>
  );
}
