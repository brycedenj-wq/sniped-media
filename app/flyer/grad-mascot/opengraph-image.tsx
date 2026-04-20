import { GRAD_VARIANTS, flyerContentType, flyerSize, renderGradFlyer } from "../_shared/gradFlyer";

export const alt = "Sniped Media · Grad Season · Mascot variant";
export const size = flyerSize;
export const contentType = flyerContentType;

export default async function OG() {
  return renderGradFlyer(GRAD_VARIANTS.mascot);
}
