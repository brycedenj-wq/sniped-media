/* Kingdom of the Sun · Phase 1 render layer.
   Component-style functions read window.SITE (config/site-data.js) and inject
   into the section containers in index.html. No content is hard-coded here.

   PHASE 2: swap the synchronous SITE reads for `await fetch('config/*.json')`.
   PHASE 3: for live sections (bracket, scores) subscribe to Supabase realtime
   or poll a Google Sheet JSON; only the data fetch changes, the renderers stay. */
(function () {
  var S = window.SITE;
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s).replace(/[&<>]/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[c]; }); };

  // --- header / hero text ---
  document.title = S.tournament.name + " · " + S.tournament.edition;
  setText("brand-name", S.tournament.name);
  setText("hero-title", S.tournament.tagline);
  setText("hero-sub", S.tournament.name + " · " + S.tournament.edition + " · " + S.tournament.datesLabel + " · " + S.tournament.location.replace(" · ", ", "));

  // --- registration CTA (placeholder-aware) ---
  // PHASE 2: point registrationLink at a real form. Until then, degrade gracefully.
  renderCTA("hero-cta");
  renderCTA("nav-cta");
  renderCTA("register-cta");

  // --- stats band ---
  $("stats").innerHTML = S.stats.map(function (s) {
    return '<div><div class="n">' + esc(s.n) + '</div><div class="l">' + esc(s.l) + '</div></div>';
  }).join("");

  // --- history / legacy ---
  setText("history-story", S.history.story);
  setText("history-positioning", S.history.positioning || "");
  setText("history-reach", S.history.reach);
  $("alumni").innerHTML = S.history.alumni.map(function (a) { return '<span>' + esc(a) + '</span>'; }).join("");
  if (S.history.legacyStats && $("legacy-stats")) {
    $("legacy-stats").innerHTML = S.history.legacyStats.map(function (s) {
      return '<div><div class="n">' + esc(s.n) + '</div><div class="l">' + esc(s.l) + '</div></div>';
    }).join("");
  }
  renderHeadCards("alumni-headliners", S.history.alumniHeadliners);
  renderHeadCards("alumni-coaches", S.history.alumniCoaches);

  // --- champions roll (legacy table, powered by config) ---
  if (S.champions && $("champions-table")) {
    var rows = S.champions.map(function (c) {
      if (c.cancelled) {
        return '<tr class="cancelled"><td class="yr">' + esc(c.y) + '</td><td colspan="4">Tournament cancelled · COVID</td></tr>';
      }
      var badge = c.honor === "National" ? ' <span class="hb nat">National</span>'
                : c.honor === "State" ? ' <span class="hb">State</span>' : '';
      return '<tr><td class="yr">' + esc(c.y) + '</td><td class="ch">' + esc(c.champ) + badge
           + '</td><td class="ru">' + esc(c.ru) + '</td><td class="sc">' + esc(c.score)
           + '</td><td class="mv">' + esc(c.mvp) + '</td></tr>';
    }).join("");
    $("champions-table").innerHTML = '<thead><tr><th>Year</th><th>Champion</th><th>Runner-Up</th><th>Score</th><th>MVP</th></tr></thead><tbody>' + rows + '</tbody>';
  }

  // --- schedule ---
  $("schedule-grid").innerHTML = S.schedule.map(function (d) {
    return '<div class="card day"><div class="tag">' + esc(d.day) + '</div><h3>' + esc(d.label) + '</h3><div class="note">' + esc(d.note) + '</div></div>';
  }).join("");

  // --- teams (pad host list to teamSlots with TBA) ---
  // PHASE 2: replace the padding with the confirmed 16-team field.
  var teams = S.teams.slice();
  while (teams.length < S.teamSlots) teams.push({ tba: true });
  $("teams-grid").innerHTML = teams.map(function (t) {
    if (t.tba) return '<div class="team tba">TBA</div>';
    return '<div class="team' + (t.host ? ' host' : '') + '">' + (t.host ? '<span class="badge">Host</span>' : '') + '<span>' + esc(t.name) + '</span>' + (t.loc ? '<span class="badge">' + esc(t.loc) + '</span>' : '') + '</div>';
  }).join("");

  // --- watch live note (embed/link slot) ---
  setText("watchlive-note", (S.watchLive && S.watchLive.note) ? S.watchLive.note : "");

  // --- experience ---
  $("experience-grid").innerHTML = S.experience.map(function (e) {
    return '<div class="card"><h3>' + esc(e.t) + '</h3><p>' + esc(e.d) + '</p></div>';
  }).join("");

  // --- sponsors (tiers, no prices) ---
  $("tiers").innerHTML = S.sponsors.tiers.map(function (name) {
    return '<div class="tier"><div class="name">' + esc(name) + '</div><div class="price">Inquire</div></div>';
  }).join("");
  setText("sponsor-note", S.sponsors.note);

  // --- media (placeholder gallery + your credit) ---
  var shots = "";
  for (var i = 0; i < S.media.placeholders; i++) shots += '<div class="shot">photo</div>';
  $("media").innerHTML = shots;
  setText("media-credit", "Photography: " + S.credits.photography);

  // --- footer ---
  setText("foot-name", S.tournament.name + " · Ocala, Florida");
  setText("foot-credit", "Site: " + S.credits.site);
  setText("foot-year", String(S.tournament.year));

  function setText(id, txt) { var el = $(id); if (el) el.textContent = txt; }

  function renderHeadCards(id, items) {
    var el = $(id); if (!el || !items) return;
    el.innerHTML = items.map(function (a) {
      return '<div class="head-card"><span class="hn">' + esc(a.name) + '</span><span class="ht">' + esc(a.note) + '</span></div>';
    }).join("");
  }

  function renderCTA(id) {
    var el = $(id); if (!el) return;
    var c = S.contact, inv = S.tournament.invitationOnly;
    var label = (id === "register-cta") ? (inv ? "Confirm Your Spot" : "Register Your Program") : (inv ? "Confirm Spot" : "Register");
    var mail = c.confirmEmail || c.email;
    if (c.registrationLink) { el.outerHTML = a(c.registrationLink, label); }
    else if (mail) { el.outerHTML = a("mailto:" + mail + "?subject=" + encodeURIComponent("Kingdom of the Sun " + S.tournament.edition + " - team confirmation"), label); }
    else if (c.phone) { el.outerHTML = a("tel:" + c.phone, label); }
    else if (id === "nav-cta") { el.outerHTML = a("#register", label); }
    else { el.outerHTML = '<span class="btn disabled" id="' + id + '">Details soon</span>'; }
    function a(href, t) { return '<a class="btn" id="' + id + '" href="' + href + '">' + t + '</a>'; }
  }
})();
