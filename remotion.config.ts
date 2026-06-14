// Remotion CLI configuration. Only affects `remotion studio` / `remotion render`
// — it does not touch the Next.js build.
// See: https://www.remotion.dev/docs/config
import { Config } from "@remotion/cli/config";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
