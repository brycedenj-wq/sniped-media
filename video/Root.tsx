import { Composition } from "remotion";
import {
  HelloWorld,
  HELLO_WORLD_DURATION_IN_FRAMES,
  HELLO_WORLD_FPS,
  HELLO_WORLD_HEIGHT,
  HELLO_WORLD_WIDTH,
} from "./HelloWorld";
import {
  ChronixelScene01,
  CHRONIXEL_DURATION_IN_FRAMES,
  CHRONIXEL_FPS,
  CHRONIXEL_HEIGHT,
  CHRONIXEL_WIDTH,
} from "./ChronixelScene01";

// Register every Remotion composition here. Each <Composition> shows up as an
// entry in the Remotion Studio and as a render target for `remotion render`.
export const RemotionRoot = () => {
  return (
    <>
      <Composition
        id="HelloWorld"
        component={HelloWorld}
        durationInFrames={HELLO_WORLD_DURATION_IN_FRAMES}
        fps={HELLO_WORLD_FPS}
        width={HELLO_WORLD_WIDTH}
        height={HELLO_WORLD_HEIGHT}
        defaultProps={{ title: "Sniped Media" }}
      />
      <Composition
        id="ChronixelScene01"
        component={ChronixelScene01}
        durationInFrames={CHRONIXEL_DURATION_IN_FRAMES}
        fps={CHRONIXEL_FPS}
        width={CHRONIXEL_WIDTH}
        height={CHRONIXEL_HEIGHT}
      />
    </>
  );
};
