# Pre-Delivery Design Checklist

Run through every item before delivering any website or landing page. Mark each as PASS, FAIL, or N/A.

---

## Visual Quality

- [ ] **No emoji icons** — All UI icons are SVG from a single library (Lucide, Heroicons, etc.)
- [ ] **Consistent icon style** — Same stroke weight, same size, same library throughout
- [ ] **Brand logo is an SVG** — Not styled text pretending to be a logo
- [ ] **Hover states on all clickable elements** — Buttons, links, cards, nav items
- [ ] **Active/pressed states** — Visual feedback on click (scale, darken, or depress)
- [ ] **Consistent border-radius** — Using a defined scale (e.g., 4/8/12/16/9999px)
- [ ] **Consistent shadow system** — Elevation shadows from defined tokens (sm/md/lg/xl)
- [ ] **Color tokens, not hardcoded values** — Using CSS variables or design tokens
- [ ] **No orphaned headings** — Every heading has content below it
- [ ] **Image aspect ratios preserved** — No stretched or squished images
- [ ] **Favicon present** — Custom favicon, not browser default
- [ ] **Loading states** — Skeleton screens or spinners for async content

---

## Interaction & Behavior

- [ ] **Cursor: pointer on all clickable elements** — Buttons, links, cards, toggles
- [ ] **Hover transitions are smooth** — 150-300ms with appropriate easing
- [ ] **Focus states visible** — 2px+ outline on all focusable elements (not just color)
- [ ] **Tab order follows visual layout** — Logical keyboard navigation flow
- [ ] **No hover-only functionality** — Everything works on touch/click
- [ ] **Modals close via X, Escape, and backdrop click** — Three close methods
- [ ] **Modal focus trap** — Tab stays inside open modal
- [ ] **Destructive actions have confirmation** — Delete, remove, cancel with confirm dialog
- [ ] **Form validation is inline** — Errors show as user completes fields
- [ ] **Error messages are specific** — Say what went wrong and how to fix it
- [ ] **Button loading states** — Shows spinner and prevents double-submit
- [ ] **Empty states have guidance** — Not just "No data" — show what to do next
- [ ] **Scroll position preserved** — Back navigation restores position

---

## Light Mode & Dark Mode

- [ ] **Dark background is dark gray, not pure black** — #0a0a0b to #18181b range
- [ ] **Dark mode has subtle borders** — Cards/sections have visible borders in dark mode
- [ ] **Adjusted shadow opacity** — Shadows are more subtle or replaced with borders in dark
- [ ] **Saturated colors are desaturated for dark** — Primary colors shift lighter/softer
- [ ] **Images have reduced brightness in dark** — `filter: brightness(0.9)` or similar
- [ ] **Text contrast meets 4.5:1** — Verified in both light and dark modes
- [ ] **Form inputs have visible borders** — Inputs don't disappear into background
- [ ] **Toggle/switch for mode** — User can manually switch (not just system preference)

---

## Layout & Responsive

- [ ] **Max content width set** — Body content max-width 1200-1440px, centered
- [ ] **Mobile tested at 320px** — Nothing overflows or breaks
- [ ] **Tablet tested at 768px** — Layout adapts appropriately
- [ ] **Desktop tested at 1440px+** — Content doesn't stretch unnaturally
- [ ] **Navigation collapses on mobile** — Hamburger menu or equivalent
- [ ] **Fixed/floating elements don't block content** — Especially on mobile
- [ ] **Card grids align consistently** — Equal heights, aligned content
- [ ] **Sidebar collapses on mobile** — Transforms to drawer or stacks
- [ ] **Tables scroll horizontally on mobile** — Or transform to card layout
- [ ] **No horizontal scroll on any viewport** — Content fits within bounds
- [ ] **Spacing follows a system** — 8px base unit used consistently

---

## Accessibility

- [ ] **Alt text on all meaningful images** — Decorative images have empty alt
- [ ] **Form labels visible** — Not just placeholders
- [ ] **Color is not the only indicator** — Icons/text accompany color-coded info
- [ ] **Contrast ratio 4.5:1 minimum** — Checked with a contrast tool
- [ ] **Skip navigation link** — "Skip to main content" for keyboard users
- [ ] **Semantic heading hierarchy** — h1 > h2 > h3, no skipping levels
- [ ] **ARIA labels on icon-only buttons** — `aria-label="Close"` on X button
- [ ] **Reduced motion respected** — `prefers-reduced-motion` media query used
- [ ] **Keyboard operable** — All features work without a mouse
- [ ] **Focus visible** — Not hidden by `outline: none`
- [ ] **Screen reader tested** — Or at minimum, semantic HTML verified
- [ ] **Language attribute set** — `<html lang="en">` present

---

## Performance

- [ ] **Images optimized** — WebP/AVIF format, appropriate dimensions
- [ ] **Images lazy-loaded** — Below-fold images use `loading="lazy"`
- [ ] **Explicit image dimensions** — Width/height or aspect-ratio set to prevent CLS
- [ ] **Fonts preloaded** — Critical fonts use `<link rel="preload">`
- [ ] **Font-display: swap** — Text visible during font loading
- [ ] **Maximum 2-3 font families** — Not loading excessive font weights
- [ ] **CSS is not render-blocking** — Critical CSS inlined or async loaded
- [ ] **No layout shift on load** — CLS score under 0.1
- [ ] **Code split by route** — Dynamic imports for non-critical routes
- [ ] **Third-party scripts deferred** — Analytics/chat loaded after main content

---

## Typography

- [ ] **Body text minimum 16px** — Not smaller than 1rem
- [ ] **Line height 1.5-1.8** — Comfortable reading spacing
- [ ] **Line length max 65ch** — Paragraphs don't span the full viewport
- [ ] **Heading hierarchy is visually clear** — h1 largest, h2 smaller, h3 smaller
- [ ] **Font fallbacks specified** — System fonts as fallback stack
- [ ] **No more than 2-3 font families** — Heading + body + optional mono
- [ ] **Consistent font weights** — Using defined weight scale, not random values
- [ ] **Letter-spacing appropriate** — Headings may be tighter, body normal

---

## SEO Basics

- [ ] **Semantic HTML** — Using header, main, nav, section, article, footer
- [ ] **Single h1 per page** — Describes the page topic
- [ ] **Heading hierarchy intact** — h1 > h2 > h3, logically nested
- [ ] **Meta title and description** — Present and appropriately sized
- [ ] **Open Graph tags** — og:title, og:description, og:image for social sharing
- [ ] **Canonical URL** — Set to prevent duplicate content issues
- [ ] **Sitemap** — XML sitemap available
- [ ] **Robots.txt** — Present and correctly configured
- [ ] **Structured data** — Schema.org markup where relevant
- [ ] **Image alt text** — Descriptive and keyword-relevant

---

## Final Verification

- [ ] **Tested in Chrome, Firefox, Safari** — No layout or functionality breaks
- [ ] **Tested on real mobile device** — Not just browser responsive mode
- [ ] **All links work** — No 404s or broken anchors
- [ ] **Forms submit correctly** — Test with valid and invalid data
- [ ] **Analytics installed** — Tracking is active and verified
- [ ] **SSL certificate active** — HTTPS with no mixed content warnings
- [ ] **404 page exists** — Custom error page with navigation back
- [ ] **Print styles** — Content prints reasonably (if applicable)
