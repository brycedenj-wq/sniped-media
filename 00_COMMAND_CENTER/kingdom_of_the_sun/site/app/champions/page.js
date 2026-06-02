import { champions } from "@/data/champions";

export const metadata = {
  title: "Champions",
  description: "Every Kingdom of the Sun champion from 1974 to 2025: champion, runner-up, final score, and tournament MVP.",
};

export default function Champions() {
  return (
    <>
      <header className="pagehead">
        <div className="wrap">
          <div className="eyebrow">Since 1974</div>
          <h1>Champions</h1>
          <p className="lead">Every champion of the Kingdom of the Sun, from the first tournament in 1974 to today. The 2020 tournament was cancelled due to COVID.</p>
        </div>
      </header>

      <section className="section">
        <div className="wrap">
          <div className="tablewrap">
            <table className="tbl">
              <thead>
                <tr><th>Year</th><th>Champion</th><th>Runner-Up</th><th>Score</th><th>MVP</th></tr>
              </thead>
              <tbody>
                {champions.map((c) =>
                  c.cancelled ? (
                    <tr className="cancelled" key={c.y}>
                      <td className="yr">{c.y}</td>
                      <td colSpan={4}>Tournament cancelled · COVID</td>
                    </tr>
                  ) : (
                    <tr key={c.y}>
                      <td className="yr">{c.y}</td>
                      <td className="ch">
                        {c.champ}
                        {c.honor === "National" ? <span className="hb nat">National</span> : c.honor === "State" ? <span className="hb">State</span> : null}
                      </td>
                      <td className="dim">{c.ru}</td>
                      <td className="dim">{c.score}</td>
                      <td className="dim">{c.mvp}</td>
                    </tr>
                  )
                )}
              </tbody>
            </table>
          </div>
          <p className="muted" style={{ marginTop: 14, fontSize: 12 }}>
            National = the program was a national champion that season. State = a state champion. Source: official tournament program.
          </p>
        </div>
      </section>
    </>
  );
}
