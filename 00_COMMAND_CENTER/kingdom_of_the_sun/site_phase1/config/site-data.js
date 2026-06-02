/* ============================================================================
   Kingdom of the Sun · Phase 1 site data config
   ----------------------------------------------------------------------------
   SINGLE source of content. assets/app.js reads window.SITE, hard-codes nothing.
   Updated 2026-06-01 with dad's confirmed answers: 53rd Annual, Dec 28-31 2026,
   invitation-only, 16-team field (10 named + 6 TBA), contact, Watch Live slot.

   PHASE 2: split into JSON, fetch(). PHASE 3: live source for teams/bracket.
   PLACEHOLDERS: "" or [brackets] = pending real value. Nothing invented.
   ============================================================================ */
window.SITE = {
  tournament: {
    name: "Kingdom of the Sun",
    edition: "53rd Annual",                 // dad confirmed 53rd (overrode the 52nd guess)
    year: 2026,
    datesLabel: "December 28-31, 2026",      // confirmed
    datesConfirmed: true,
    location: "Vanguard High School · Ocala, Florida",
    invitationOnly: true,                    // NEW: not open registration, confirm invited teams
    tagline: "The Original. Since 1974."
  },

  contact: {
    confirmEmail: "Eric.jones@marion.k12.fl.us",  // invited-coach confirmations route here for now
    email: "Eric.jones@marion.k12.fl.us",
    phone: "407-625-1026",
    qrTarget: ""   // PLACEHOLDER · set to thekingdomofthesun.com once the domain is live
  },

  credits: {
    photography: "[Photography credit pending]",
    site: "[Site credit pending]"
  },

  stats: [
    { n: "53rd", l: "Annual" },
    { n: "16",   l: "Teams" },
    { n: "4",    l: "Days" },
    { n: "1",    l: "Champion" }
  ],

  history: {
    founded: 1974,
    founder: "Jim Haley",
    story: "In the spring of 1974, a young coach named Jim Haley told Vanguard's principal he wanted to host a sixteen-team tournament. Told it could not be done in Florida, Haley committed all sixteen teams within twenty-four hours. The next day he and Bob Murphy cold-called Ocala businesses and raised the first $7,500 in sponsorships. An Ocala institution was born. Coach Haley passed in November 2018, and the Vanguard court is named in his honor.",
    positioning: "The original sixteen-team national high school holiday tournament. The King of the Bluegrass, the Arby's Classic, and the City of Palms Classic all followed the format the Kingdom created.",
    reach: "79 State Champions, 215 different Florida schools, and 140 out-of-state teams from more than 25 states, plus the Bahamas and Canada, have played in the Kingdom. Two national champions have been crowned on this floor.",
    legacyStats: [
      { n: "79",  l: "State Champions" },
      { n: "215", l: "Florida Schools" },
      { n: "140", l: "Out-of-State Teams" },
      { n: "30+", l: "NBA Players" },
      { n: "2",   l: "National Champions" }
    ],
    alumniHeadliners: [
      { name: "Joel Embiid",  note: "2023 NBA MVP" },
      { name: "Dwight Howard", note: "Hall of Fame 2025" },
      { name: "Kwame Brown",  note: "No. 1 Overall Pick" }
    ],
    alumniCoaches: [
      { name: "Joe Mazzulla", note: "NBA Champion Head Coach" },
      { name: "Dan Hurley",   note: "2x NCAA Champion Head Coach" }
    ],
    alumni: ["Christian Laettner", "Jamal Mashburn", "Kerry Kittles", "Sherman Douglas", "Vernon Maxwell", "Jamaal Magloire", "Thaddeus Young", "JJ Barea", "Michael Carter-Williams", "Nassir Little", "Langston Galloway", "DeShawn Stevenson"]
  },

  // Full champions roll 1974-2024 (2020 cancelled, COVID). Source: 2025 program book.
  // honor: "National" | "State" | "" . app.js renders the badge + the cancelled row.
  champions: [
    { y: 2024, champ: "St Thomas Aquinas", ru: "Gibbs", score: "80-64", mvp: "Dwayne Wimbley", honor: "State" },
    { y: 2023, champ: "Winter Haven", ru: "St Thomas Aquinas", score: "78-75 OT", mvp: "Isaac Celicsar", honor: "" },
    { y: 2022, champ: "Winter Haven", ru: "Olympia", score: "74-69", mvp: "Isaac Celicsar", honor: "" },
    { y: 2021, champ: "Eagle's Landing (GA)", ru: "IMG Academy Blue", score: "63-60", mvp: "AJ Barnes", honor: "" },
    { y: 2020, cancelled: true },
    { y: 2019, champ: "Columbia (GA)", ru: "Jones", score: "66-58", mvp: "Devin Longstreet", honor: "" },
    { y: 2018, champ: "Windermere", ru: "Orlando Christian Prep", score: "61-41", mvp: "Dante Love", honor: "" },
    { y: 2017, champ: "Buford (GA)", ru: "Vanguard", score: "75-54", mvp: "Marcus Watson", honor: "" },
    { y: 2016, champ: "Madison Memorial (WI)", ru: "LaSalle (OH)", score: "43-38", mvp: "Chris Knight", honor: "" },
    { y: 2015, champ: "Dillard", ru: "LaSalle (OH)", score: "49-42", mvp: "Jordan Wright", honor: "State" },
    { y: 2014, champ: "Cardinal Gibbons", ru: "Zion Lutheran", score: "53-51", mvp: "Maverick Rowan", honor: "State" },
    { y: 2013, champ: "Berkeley Prep", ru: "Cardinal Gibbons", score: "59-56", mvp: "Justin Gray", honor: "" },
    { y: 2012, champ: "Ballard (KY)", ru: "Deerfield Beach", score: "72-67", mvp: "Kelan Martin", honor: "" },
    { y: 2011, champ: "Montverde Academy", ru: "Blanche Ely", score: "67-53", mvp: "Kasey Hill", honor: "" },
    { y: 2010, champ: "Dwyer", ru: "LaSalle (OH)", score: "53-50", mvp: "Jacoby Brissett", honor: "State" },
    { y: 2009, champ: "Providence", ru: "East Ridge", score: "48-41", mvp: "Patrick Young", honor: "State" },
    { y: 2008, champ: "Christian Life (LA)", ru: "Wolfson", score: "73-71", mvp: "Patrick Robinson", honor: "" },
    { y: 2007, champ: "McEachern (GA)", ru: "Berkeley Prep", score: "65-62 OT", mvp: "Trae Golden", honor: "" },
    { y: 2006, champ: "LaSalle (OH)", ru: "Columbia (GA)", score: "63-57", mvp: "Bobby Austin", honor: "" },
    { y: 2005, champ: "Columbia (GA)", ru: "Christian Life (LA)", score: "54-52 OT", mvp: "Anu Saaka", honor: "State" },
    { y: 2004, champ: "St Benedict's (NJ)", ru: "Lakewood", score: "65-55", mvp: "Eugene Harvey", honor: "National" },
    { y: 2003, champ: "Tabor Academy (MA)", ru: "Bakersfield (CA)", score: "60-58", mvp: "Bilal Abdullah", honor: "" },
    { y: 2002, champ: "LaSalle (OH)", ru: "Tabor Academy (MA)", score: "60-48", mvp: "John Thinnes", honor: "" },
    { y: 2001, champ: "Miami Christian", ru: "Leesburg", score: "66-52", mvp: "Jesus Vadejo", honor: "State" },
    { y: 2000, champ: "Miami Christian", ru: "Tabor Academy (MA)", score: "67-61", mvp: "Carlos Morban", honor: "" },
    { y: 1999, champ: "Glenn Academy (GA)", ru: "Tabor Academy (MA)", score: "70-63", mvp: "DJ Jackson", honor: "" },
    { y: 1998, champ: "Mercer Island (WA)", ru: "Lenore (AL)", score: "52-47", mvp: "Tyler Besecker", honor: "State" },
    { y: 1997, champ: "Wolfson", ru: "Butler (KY)", score: "57-56", mvp: "Kenny Walker", honor: "" },
    { y: 1996, champ: "St Anthony's (NJ)", ru: "Ft Walton Beach", score: "76-63", mvp: "Anthony Perry", honor: "State" },
    { y: 1995, champ: "Eastern Commerce (CN)", ru: "Dr Phillips", score: "69-50", mvp: "Jamaal Magloire / Teddy Dupay", honor: "State" },
    { y: 1994, champ: "Memphis East (TN)", ru: "Miami", score: "44-43", mvp: "Tony Harris", honor: "" },
    { y: 1993, champ: "Alcoa (TN)", ru: "Vanguard", score: "74-65", mvp: "Micah Marsh", honor: "" },
    { y: 1992, champ: "Fletcher", ru: "Sarasota Riverview", score: "67-64", mvp: "Jeremy Hyatt", honor: "" },
    { y: 1991, champ: "Christ the King (NY)", ru: "Marist (NJ)", score: "62-50", mvp: "Jason Cipolla", honor: "" },
    { y: 1990, champ: "Christian Brothers (NJ)", ru: "Lafayette (KY)", score: "58-56", mvp: "Jason Fichter", honor: "" },
    { y: 1989, champ: "Dunbar (DC)", ru: "Miami", score: "100-98", mvp: "Deon Murray", honor: "State" },
    { y: 1988, champ: "Bartow", ru: "Scott (OH)", score: "76-71", mvp: "Patrick Sams", honor: "" },
    { y: 1987, champ: "Miami Carol City", ru: "Vanguard", score: "57-56", mvp: "Robert McKie", honor: "State" },
    { y: 1986, champ: "Miami", ru: "Countryside", score: "75-61", mvp: "Jose Ramos", honor: "State" },
    { y: 1985, champ: "Hialeah Miami Lakes", ru: "Sumter (SC)", score: "71-56", mvp: "Chris Corchiani", honor: "State" },
    { y: 1984, champ: "Spingarn (DC)", ru: "Martin County", score: "75-60", mvp: "Sherman Douglas", honor: "National" },
    { y: 1983, champ: "St Anthony's (NJ)", ru: "Mackin (DC)", score: "51-48", mvp: "David Rivers", honor: "State" },
    { y: 1982, champ: "Decatur (GA)", ru: "Vanguard", score: "53-49", mvp: "Darryl Gresham", honor: "" },
    { y: 1981, champ: "Vanguard", ru: "Martin County", score: "38-37", mvp: "Victor Johnson", honor: "State" },
    { y: 1980, champ: "Clearwater", ru: "Marianna", score: "64-63 2OT", mvp: "David Stuart", honor: "State" },
    { y: 1979, champ: "Lakeland", ru: "Vanguard", score: "81-57", mvp: "Alonzo Allen", honor: "" },
    { y: 1978, champ: "Vanguard", ru: "Clay", score: "52-47", mvp: "Kenny Vaughns / Zeb Howell", honor: "State" },
    { y: 1977, champ: "Vanguard", ru: "Miami Central", score: "68-54", mvp: "Kenny Vaughns", honor: "State" },
    { y: 1976, champ: "Deland", ru: "Vanguard", score: "76-75", mvp: "Allie Goodwin", honor: "State" },
    { y: 1975, champ: "Deland", ru: "Vanguard", score: "55-52", mvp: "Oliver Lee", honor: "" },
    { y: 1974, champ: "Lake Weir", ru: "Mainland", score: "63-50", mvp: "Frank Johnson", honor: "State" }
  ],

  // dates now confirmed Dec 28-31
  schedule: [
    { day: "Dec 28", label: "Opening Round", note: "Times announced soon" },
    { day: "Dec 29", label: "Quarterfinals", note: "Times announced soon" },
    { day: "Dec 30", label: "Semifinals · Dunk & 3-Point Contest", note: "Times announced soon" },
    { day: "Dec 31", label: "Championship", note: "Times announced soon" }
  ],

  // 16-team field confirmed. 10 named below; app.js pads to teamSlots with TBA.
  teams: [
    { name: "Vanguard Knights", host: true },
    { name: "North Marion" },
    { name: "Windermere Prep" },
    { name: "PK Young" },
    { name: "Peachtree Ridge", loc: "GA" },
    { name: "Viera" },
    { name: "Tallahassee Godby" },
    { name: "Wildwood" },
    { name: "Wekiva", loc: "Orlando" },
    { name: "South Lake" }
  ],
  teamSlots: 16,

  // Watch Live is an embed/link SLOT, not custom infrastructure.
  // Dad confirmed the Vanguard gym already has NFHS (Pixellot camera) installed.
  // Drop the NFHS Network event/game link in embedUrl when it goes live. No build needed.
  watchLive: {
    provider: "NFHS Network",   // confirmed: gym already has NFHS hardware
    embedUrl: "",               // PLACEHOLDER · the event/game link drops closer to tip-off
    note: "Every game streams live on NFHS Network. Watch link goes here closer to tip-off."
  },

  experience: [
    { t: "Nightly Team Meals", d: "Hospitality for every visiting program." },
    { t: "Dunk & 3-Point Contests", d: "Showcase events on semifinal night." },
    { t: "College & Scout Exposure", d: "A tournament that draws college representatives." },
    { t: "All-Tournament Team", d: "Recognition for the top performers." },
    { t: "Ocala Experiences", d: "Silver Springs and the World Equestrian Center." },
    { t: "Professional Media", d: "Official tournament photography and video coverage." }
  ],

  sponsors: {
    tiers: ["Founding Partner", "Gold", "Silver", "Community"],
    note: "Partnership tiers available. Details provided on inquiry."
  },

  media: { placeholders: 8 }
};
