import { site } from "@/data/site";

export const metadata = {
  title: "Watch Live",
  description: "Every game of the Kingdom of the Sun streams live on NFHS Network.",
};

export default function Watch() {
  const w = site.watchLive;
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">Watch</div>
          <h1>Watch Live</h1>
          <p className="lead">{w.note}</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          {w.embedUrl ? (
            <div className="tablewrap" style={{ aspectRatio: "16/9" }}>
              <iframe
                src={w.embedUrl}
                title="Kingdom of the Sun live on NFHS Network"
                style={{ width: "100%", height: "100%", border: 0 }}
                allowFullScreen
              />
            </div>
          ) : (
            <div className="panel">
              <div className="big">Streaming on {w.provider}</div>
              <p className="muted" style={{ marginTop: 8, fontSize: 13 }}>
                The Vanguard gym is equipped for {w.provider}. The live watch link appears here closer to tip-off.
              </p>
            </div>
          )}
        </div>
      </section>
    </>
  );
}
