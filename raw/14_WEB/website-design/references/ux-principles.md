# UX Principles Quick Reference

> Condensed from 80+ UX rules. Use this as a manual fallback when Python search is unavailable.

---

## CRITICAL Priority (Must-Have)

### 1. Color Contrast Minimum 4.5:1
All text must meet WCAG AA contrast ratio. Large text (18px+ bold or 24px+) needs 3:1 minimum.
- **Do:** Use `#1a1a1a` on `#ffffff` (ratio 17.4:1)
- **Don't:** Use `#999` on `#fff` (ratio 2.8:1 — fails)

### 2. Never Rely on Color Alone
Color-coded info must also use text, icons, or patterns.
- **Do:** Error = red color + error icon + descriptive message
- **Don't:** Field turns red with zero other indication

### 3. All Images Need Alt Text
Meaningful images get descriptive alt; decorative images get `alt=""`.
- **Do:** `alt="Product dashboard showing weekly analytics"`
- **Don't:** `alt="image1.png"` or missing alt entirely

### 4. Form Inputs Need Visible Labels
Every input needs a `<label>` — placeholders are not labels.
- **Do:** `<label for="email">Email</label><input id="email">`
- **Don't:** `<input placeholder="Email">` with no label

### 5. Keyboard Navigation Must Work
Every interactive element must be reachable and operable via keyboard.
- **Do:** Tab order follows visual layout; all buttons/links focusable
- **Don't:** Custom dropdown that only opens on mouse click

### 6. Visible Focus States
Focused elements need a clearly visible indicator.
- **Do:** `outline: 2px solid #2563eb` with offset
- **Don't:** `outline: none` on everything

### 7. Touch Targets Minimum 44x44px
Interactive elements need adequate size for touch.
- **Do:** Button with `padding: 12px 24px` (44px+ touch target)
- **Don't:** 16x16px icon button with no padding

### 8. No Hover-Only Functionality
Critical features must work on tap/click, not just hover.
- **Do:** Dropdown opens on click/tap
- **Don't:** Submenu appears only on mouseenter

### 9. Responsive Design at 320px
Nothing should break at 320px viewport width.
- **Do:** Content wraps and remains readable at 320px
- **Don't:** Buttons overflow causing horizontal scroll

---

## HIGH Priority (Should-Have)

### 10. Semantic HTML Structure
Use proper heading hierarchy (h1-h6) and semantic landmarks.
- **Do:** Single h1, then h2 for sections, h3 for subsections
- **Don't:** Multiple h1 tags or skip from h1 to h4

### 11. Skip Navigation Link
Provide a "Skip to main content" link for keyboard users.

### 12. Cursor Pointer on Clickable Elements
All clickable items show `cursor: pointer`.

### 13. Hover States on All Interactive Elements
Every clickable element needs a visible hover state change.

### 14. Consistent Spacing System
Use 4px or 8px base unit. Common scale: 4/8/12/16/24/32/48/64px.

### 15. Maximum Content Width
Body content: `max-width: 1200px` with `margin: 0 auto`.

### 16. Line Height for Readability
Body text: `line-height: 1.5` to `1.8`.

### 17. Maximum Line Length
Paragraphs: `max-width: 65ch` (65-75 characters per line).

### 18. Minimum Body Font Size
Body text: minimum `16px` (`1rem`).

### 19. Heading Hierarchy Visual Weight
Each heading level must be visually distinct. Example: h1 48px / h2 36px / h3 24px.

### 20. Transition Duration 150-300ms
UI transitions: 150-300ms. Page transitions: 300-500ms.

### 21. Skeleton Loading Screens
Show skeleton placeholders matching layout while data loads.

### 22. Error States with Recovery
Error pages explain what happened AND offer a path forward (retry, go home).

### 23. Inline Form Validation
Show validation as user types, not only on submit.

### 24. Specific Error Messages
- **Do:** "Password must be at least 8 characters with one number"
- **Don't:** "Invalid input"

### 25. Clear Current Page in Navigation
Active nav link must be visually distinct (bold, underline, color).

### 26. Mobile Hamburger Menu
Navigation collapses to accessible hamburger on mobile.

### 27. Button Hierarchy
One primary CTA per section. Use secondary/ghost variants for other actions.

### 28. No Emoji as Functional Icons
Use SVG icon libraries (Lucide, Heroicons), never emoji for UI icons.

### 29. Consistent Icon Style
All icons from one library with matching stroke weight and size.

### 30. Dark Mode: Use Dark Gray Not Pure Black
- **Do:** `background: #0f0f10`
- **Don't:** `background: #000000`

---

## MEDIUM Priority (Nice-to-Have)

- Click/active feedback (scale 0.98 or darken on press)
- Adequate spacing between touch targets (8px min gap)
- Fixed/sticky navbar on scroll
- Breadcrumbs for pages 2+ levels deep
- Labels above inputs (not beside)
- Multi-step form progress indicators
- Disabled states with reduced opacity + tooltip
- Modal closes via X, Escape, and backdrop click
- Modal focus trap
- Confirm destructive actions
- Responsive tables (horizontal scroll or card transform)
- Sortable column indicators in tables
- Optimistic UI updates
- Progress indicators for operations >3 seconds
- Search result count and term highlighting

---

## Quick Decision Matrix

| Situation | Rule |
|-----------|------|
| Adding a new button | Pointer cursor, hover state, active state, focus ring, 44px+ target |
| Adding a form | Visible labels, inline validation, specific errors, keyboard accessible |
| Adding images | Alt text, lazy loading below fold, explicit width/height |
| Adding a modal | Focus trap, Escape close, backdrop close, X button |
| Adding animation | 150-300ms duration, ease-out entry, respect reduced-motion |
| Adding dark mode | Dark gray not black, adjust saturation, add borders, reduce image brightness |
| Adding a table | Horizontal scroll on mobile, hover rows, sort indicators |
| Adding navigation | Clear active state, hamburger on mobile, skip-nav link |
