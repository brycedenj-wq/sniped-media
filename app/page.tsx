import { Hero } from "./_components/sections/Hero";
import { Problem } from "./_components/sections/Problem";
import { KitSummary } from "./_components/sections/KitSummary";
import { KitProduces } from "./_components/sections/KitProduces";
import { DeploymentLedger } from "./_components/sections/DeploymentLedger";
import { Process } from "./_components/sections/Process";
import { AudienceFit } from "./_components/sections/AudienceFit";
import { FAQ } from "./_components/sections/FAQ";
import { ClosingCTA } from "./_components/sections/ClosingCTA";
import { FadeIn } from "./_components/FadeIn";

export default function HomePage() {
  return (
    <>
      <Hero />
      <FadeIn>
        <Problem />
      </FadeIn>
      <FadeIn>
        <KitSummary />
      </FadeIn>
      <FadeIn>
        <KitProduces />
      </FadeIn>
      <FadeIn>
        <DeploymentLedger />
      </FadeIn>
      <FadeIn>
        <Process />
      </FadeIn>
      <FadeIn>
        <AudienceFit />
      </FadeIn>
      <FadeIn>
        <FAQ />
      </FadeIn>
      <FadeIn>
        <ClosingCTA />
      </FadeIn>
    </>
  );
}
