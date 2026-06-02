// Kingdom of the Sun · single source of site content.
// Confirmed reality (2026-06-01): 53rd Annual, Dec 28-31 2026, invitation-only,
// 16-team field (10 named + 6 TBA), NFHS streaming, contact set.
// History numbers corrected from the 2025 program book: 79 / 215 / 140.

export const site = {
  name: "Kingdom of the Sun",
  edition: "53rd Annual",
  year: 2026,
  datesLabel: "December 28-31, 2026",
  location: "Vanguard High School · Ocala, Florida",
  invitationOnly: true,
  tagline: "The Original. Since 1974.",

  contact: {
    name: "Coach Eric Jones",
    role: "Tournament Committee",
    email: "Eric.jones@marion.k12.fl.us",
    phone: "407-625-1026",
    domain: "thekingdomofthesun.com",
  },

  // Top-line tournament stats (2026 ops, kept clean).
  stats: [
    { n: "53rd", l: "Annual" },
    { n: "16", l: "Teams" },
    { n: "4", l: "Days" },
    { n: "1", l: "Champion" },
  ],

  history: {
    founded: 1974,
    founder: "Jim Haley",
    story:
      "In the spring of 1974, a young coach named Jim Haley told Vanguard's principal he wanted to host a sixteen-team tournament. Told it could not be done in Florida, Haley committed all sixteen teams within twenty-four hours. The next day he and Bob Murphy cold-called Ocala businesses and raised the first $7,500 in sponsorships. An Ocala institution was born.",
    storyCont:
      "From the late 1970s through the 1990s the Kingdom grew into one of the premier high school tournaments in the country. Coach Haley passed in November 2018. The Vanguard court is named Jim Haley Court in his honor.",
    positioning:
      "The original sixteen-team national high school holiday tournament. The King of the Bluegrass, the Arby's Classic, and the City of Palms Classic all followed the format the Kingdom created.",
    reach:
      "79 State Champions, 215 different Florida schools, and 140 out-of-state teams from more than 25 states, plus the Bahamas and Canada, have played in the Kingdom. Two national champions have been crowned on this floor.",
    legacyStats: [
      { n: "79", l: "State Champions" },
      { n: "215", l: "Florida Schools" },
      { n: "140", l: "Out-of-State Teams" },
      { n: "30+", l: "NBA Players" },
      { n: "2", l: "National Champions" },
    ],
  },

  schedule: [
    { day: "Mon · Dec 28", label: "Opening Round", note: "Tip-off times announced soon" },
    { day: "Tue · Dec 29", label: "Quarterfinals", note: "Tip-off times announced soon" },
    { day: "Wed · Dec 30", label: "Semifinals · Dunk & 3-Point Contest", note: "Tip-off times announced soon" },
    { day: "Thu · Dec 31", label: "Championship", note: "Tip-off times announced soon" },
  ],

  teams: [
    { name: "Vanguard Knights", city: "Ocala, FL", host: true },
    { name: "North Marion", city: "Citra, FL" },
    { name: "Windermere Prep", city: "Windermere, FL" },
    { name: "P.K. Yonge", city: "Gainesville, FL" },
    { name: "Peachtree Ridge", city: "Suwanee, GA" },
    { name: "Viera", city: "Viera, FL" },
    { name: "Tallahassee Godby", city: "Tallahassee, FL" },
    { name: "Wildwood", city: "Wildwood, FL" },
    { name: "Wekiva", city: "Apopka, FL" },
    { name: "South Lake", city: "Groveland, FL" },
  ],
  teamSlots: 16,

  watchLive: {
    provider: "NFHS Network",
    embedUrl: "",
    note: "Every game streams live on NFHS Network. The watch link goes live closer to tip-off.",
  },

  experience: [
    { t: "Nightly Team Meals", d: "Hospitality for every visiting program, all four nights." },
    { t: "Dunk & 3-Point Contests", d: "Showcase events on semifinal night." },
    { t: "College & Scout Exposure", d: "A tournament that has always drawn college representatives." },
    { t: "All-Tournament Team", d: "Recognition for the top performers in the field." },
    { t: "Ocala Experiences", d: "Silver Springs and the World Equestrian Center." },
    { t: "Official Media", d: "Professional tournament photography and video coverage." },
  ],

  sponsors: {
    tiers: ["Crown · Title", "Court · Gold", "Sideline · Silver", "Community · Local"],
    note: "Partnership tiers available for the 53rd Annual. Details provided on inquiry.",
  },
};
