---
name: website-design
description: "Complete website design system. Python-powered search across 50+ styles, 90+ color palettes, 50+ font pairings, landing page patterns, and UX rules. Generates full design systems from keywords. Actions: design, build, create, implement, review websites, landing pages, dashboards, e-commerce, SaaS, portfolios. Supports React, Next.js, Vue, Svelte, HTML+Tailwind, shadcn/ui."
---

# Website Design System

A complete, self-contained website design toolkit. Search 50+ visual styles, 90+ color palettes, 50+ font pairings, 25+ landing page patterns, and 80+ UX rules to generate professional design systems in seconds.

---

## Workflow

Every website design task follows this sequence:

### Step 1: Understand the Project

Before touching any tool, answer these questions:

- **WHO** is the audience? (developers, executives, parents, Gen-Z, enterprise buyers)
- **WHAT** is the product/service? (SaaS tool, e-commerce store, portfolio, agency site)
- **WHY** does this site exist? (convert signups, sell products, showcase work, inform)
- **WHAT TONE** should it convey? (professional, playful, luxurious, technical, warm)
- **WHAT CONSTRAINTS** exist? (existing brand colors, framework requirements, accessibility standards)
- **WHAT MAKES IT DIFFERENT?** What should a visitor remember 5 minutes after leaving?

### Step 2: Generate Design System

Use the Python search tool to generate a complete design system recommendation.

```bash
# Generate full design system from keywords
python3 scripts/search.py "modern SaaS dark premium" --design-system

# With project name and markdown output
python3 scripts/search.py "fintech trust professional" --design-system -p "Acme Finance" -f markdown

# Search specific domains
python3 scripts/search.py "elegant serif luxury" --domain typography
python3 scripts/search.py "glassmorphism blur" --domain style
python3 scripts/search.py "startup conversion" --domain pattern
python3 scripts/search.py "accessibility forms" --domain ux
python3 scripts/search.py "warm earth organic" --domain color

# Get stack-specific implementation tips
python3 scripts/search.py "SaaS dashboard" --design-system --stack nextjs-shadcn
python3 scripts/search.py "portfolio minimal" --design-system --stack svelte-tailwind
```

The tool searches all CSV databases using TF-IDF keyword matching and returns:
- **Visual style** with CSS properties and avoidance notes
- **Color palette** with hex codes, mood, and accessibility notes
- **Typography** with heading/body fonts, Google Fonts URL, and pairing rationale
- **Page pattern** with section breakdown and conversion focus
- **Key UX rules** relevant to the project type
- **Alternatives** for each category so you can mix and match

### Step 3: Apply Distinctive Aesthetics

A design system is the foundation. Now make it distinctive. Follow these principles:

**Typography as Identity**
- Never default to Inter, Roboto, or system-ui for a marketing site. These are invisible. Choose fonts with personality that match the brand.
- Heading fonts carry the personality. Body fonts carry the content. They serve different jobs.
- Use `font-size: clamp()` for fluid typography that feels designed at every viewport.
- Letter-spacing on headings (-0.02em to -0.04em for large text, 0.05em+ for small caps/labels).

**Color with Purpose**
- The primary palette from the tool is a starting point. Customize it:
  - Shift the primary hue 5-10 degrees to make it yours
  - Add one unexpected accent color that creates visual tension
  - Define semantic colors: success, warning, error, info — don't reuse primary
- Dark mode is not an afterthought. Design it simultaneously:
  - Dark gray (#0f0f10) not pure black (#000)
  - Desaturate primary colors for dark backgrounds
  - Add subtle borders where shadows disappear
  - Reduce image brightness slightly

**Motion as Meaning**
- Every animation must answer: "What information does this motion convey?"
- Entrance: `ease-out`, 200-300ms, subtle translateY(8-16px) + opacity
- State change: `ease-in-out`, 150-200ms
- Exit: `ease-in`, 150ms
- Always respect `prefers-reduced-motion`
- Scroll-triggered animations: once per element, 20px max translate, no rotation

**Spatial Composition**
- Whitespace is a design element, not empty space. More whitespace = more premium feel.
- Use a consistent spacing scale: 4/8/12/16/24/32/48/64/96/128px
- Hero sections: 80-120px vertical padding minimum
- Section breaks: 64-96px
- Card padding: 24-32px
- Dense UIs (dashboards): 12-16px

**Backgrounds and Texture**
- Flat solid backgrounds are generic. Layer subtle depth:
  - Subtle noise texture (opacity 0.02-0.05)
  - Soft radial gradients behind hero sections
  - Dot grid or line patterns at very low opacity
  - Gradient mesh for creative/AI products
- Backgrounds should enhance, never distract from content

**Anti-Generic Rules**
- No purple gradients on white cards (the 2024 startup clone look)
- No stock hero images of people pointing at screens
- No centered-everything layouts (asymmetry creates visual interest)
- No gray-on-white with blue buttons (the default SaaS template)
- If your site could be mistaken for a template, it needs more design work

### Step 4: Validate Against UX Principles

Before building, verify the design system against critical UX rules:

```bash
python3 scripts/search.py "accessibility contrast focus" --domain ux
python3 scripts/search.py "forms validation labels" --domain ux
python3 scripts/search.py "responsive mobile touch" --domain ux
```

**Priority levels for UX rules:**
1. **CRITICAL** — Must fix before any delivery. Accessibility violations, broken keyboard nav, no responsive support.
2. **HIGH** — Should fix before delivery. Poor contrast, missing hover states, no loading states.
3. **MEDIUM** — Fix if time allows. Optimistic updates, breadcrumbs, sort indicators.
4. **LOW** — Polish items. Animation easing, CSS optimizations.

**Non-negotiable rules for every project:**
- Color contrast: 4.5:1 minimum (WCAG AA)
- Touch targets: 44x44px minimum
- Keyboard navigation: everything reachable via Tab
- Focus states: visible on all interactive elements
- Form labels: visible, not just placeholders
- Alt text: on all meaningful images
- Responsive: works at 320px minimum
- No hover-only functionality

### Step 5: Build with Stack Best Practices

```bash
# Get framework-specific guidelines
python3 scripts/search.py "" --stack nextjs-shadcn
python3 scripts/search.py "" --stack react-tailwind
python3 scripts/search.py "" --stack vue-tailwind
python3 scripts/search.py "" --stack html-tailwind
python3 scripts/search.py "" --stack svelte-tailwind
```

**Available stacks:**
| Stack | Best For |
|-------|----------|
| `html-tailwind` | Static sites, landing pages, email templates |
| `nextjs-tailwind` | Full-stack apps, SSR/SSG sites, content sites |
| `nextjs-shadcn` | SaaS dashboards, admin panels, complex UIs |
| `react-tailwind` | SPAs, client-side apps, widget embeds |
| `vue-tailwind` | Progressive apps, team-friendly codebases |
| `svelte-tailwind` | Performance-critical sites, lightweight apps |

**Universal implementation rules:**
- Define design tokens as CSS custom properties in `:root`
- Use semantic color names: `--color-primary`, `--color-surface`, `--color-text`
- Component-first architecture: build small, compose large
- Mobile-first CSS: base styles for mobile, `@media (min-width)` for larger
- Use `clamp()` for fluid typography and spacing
- Lazy-load images below the fold
- Preload critical fonts with `font-display: swap`
- Code-split routes for performance

### Step 6: Run Pre-Delivery Checklist

Before delivering, run through the complete checklist at `references/design-checklist.md`.

Quick summary of critical checks:
- [ ] No emoji icons in UI
- [ ] Consistent icon library
- [ ] Cursor pointer on all clickable elements
- [ ] Hover + focus + active states on interactive elements
- [ ] Light and dark mode both work
- [ ] Responsive at 320px, 768px, and 1440px+
- [ ] Alt text on images
- [ ] Form labels visible
- [ ] Color contrast 4.5:1+
- [ ] Loading states for async content
- [ ] Error states with recovery paths
- [ ] Empty states with guidance
- [ ] No horizontal scroll at any viewport
- [ ] Semantic HTML with proper heading hierarchy

---

## UX Rules Quick Reference (by Category)

### Accessibility (CRITICAL)
- Contrast 4.5:1 minimum for text
- Never rely on color alone — add icons/text
- Alt text on all images
- Visible form labels (not just placeholders)
- Keyboard navigation must work
- Focus states must be visible
- Touch targets 44x44px+

### Touch & Interaction (HIGH)
- `cursor: pointer` on all clickable elements
- Hover states on all interactive elements
- Active/pressed state feedback
- 8px+ gap between touch targets
- No hover-only functionality

### Layout (HIGH)
- Consistent spacing system (8px base)
- Max content width (1200-1440px)
- Responsive at 320px, 768px, 1024px+
- Fixed navbar on scroll for long pages
- Z-index management scale
- Card grids with consistent height

### Typography (HIGH)
- Body: 16px+ minimum, line-height 1.5-1.8
- Max line length: 65ch
- Visual heading hierarchy (each level distinct)
- Font fallback stack specified

### Performance (MEDIUM-HIGH)
- Lazy-load images below fold
- Font preload with `font-display: swap`
- Minimize layout shift (explicit image dimensions)
- Code-split routes

### Animation (MEDIUM)
- Transitions: 150-300ms
- Entrance animations: once per element
- Respect `prefers-reduced-motion`
- Skeleton loaders for loading states

### Dark Mode (HIGH when applicable)
- Dark gray (#0f0f10) not pure black
- Borders replace shadows
- Desaturate primary colors
- Reduce image brightness

### Forms (HIGH)
- Inline validation (not just on submit)
- Specific error messages
- Labels above inputs
- Disabled states with explanation

### Navigation (HIGH)
- Clear current page indicator
- Mobile hamburger menu
- Breadcrumbs for deep pages

---

## Common Design Patterns

### Professional SaaS
```
Style: Corporate Modern or Dark Mode Premium
Colors: Professional Blue, Slate Dark, or Fintech Trust
Typography: Modern Professional (Space Grotesk + Inter) or Startup Hero (Plus Jakarta Sans)
Pattern: SaaS Dashboard Preview or Feature Showcase
```

### Creative Agency
```
Style: Brutalism, Swiss Design, or Bento Grid
Colors: Creative Orange, Fashion Monochrome, or Gradient Mesh
Typography: Agency Portfolio (Clash Display + Satoshi) or Dramatic Contrast (DM Serif + DM Sans)
Pattern: Portfolio Grid or Hero-Centric
```

### E-commerce
```
Style: Minimalism, Corporate Modern, or E-commerce Grid
Colors: Warm Neutral, Cool Minimal, or brand-specific
Typography: E-commerce Clear (Urbanist) or Clean Corporate (Figtree)
Pattern: E-commerce Product or Feature Showcase
```

### Luxury Brand
```
Style: Luxury, Art Deco, or Monochrome
Colors: Luxury Gold, Rose Gold, or Fashion Monochrome
Typography: Elegant Luxury (Cormorant Garamond + Nunito Sans) or Boutique Chic (Bodoni Moda + Outfit)
Pattern: Full Bleed Media or Storytelling Scroll
```

### Developer Tool
```
Style: Dark Mode Premium or Dashboard UI
Colors: Midnight SaaS, Serious Dark, or Slate Dark
Typography: Technical Mono (JetBrains Mono + IBM Plex Sans) or Dashboard Data (Geist Sans + Geist Mono)
Pattern: Documentation Hub or SaaS Dashboard Preview
```

### Health & Wellness
```
Style: Organic, Japandi, or Pastel Soft
Colors: Sage Wellness, Healthcare Calm, or Modern Mint
Typography: Rounded Friendly (Nunito + Nunito Sans) or Eco Natural (Gilda Display + Karla)
Pattern: Storytelling Scroll or Hero-Centric
```

---

## Search Reference

### Domain Keywords
| Domain | Key search terms |
|--------|-----------------|
| `style` | glass, minimal, brutalist, dark, retro, luxury, playful, organic, grid, neon |
| `color` | saas, fintech, health, gaming, luxury, warm, cool, pastel, neon, earth, dark |
| `typography` | serif, sans, mono, elegant, bold, playful, modern, editorial, technical, rounded |
| `pattern` | hero, saas, ecommerce, portfolio, landing, lead-gen, pricing, app, community |
| `ux` | accessibility, forms, navigation, responsive, animation, dark-mode, loading, buttons |

### Stack Options
| Stack key | Framework |
|-----------|-----------|
| `html-tailwind` | Static HTML + Tailwind CSS |
| `nextjs-tailwind` | Next.js App Router + Tailwind |
| `nextjs-shadcn` | Next.js + shadcn/ui + Tailwind |
| `react-tailwind` | React (Vite) + Tailwind |
| `vue-tailwind` | Vue 3 + Tailwind |
| `svelte-tailwind` | SvelteKit + Tailwind |

---

## If Python Is Not Available

If you cannot run the Python search tool, use these fallback references:

1. **`references/ux-principles.md`** — Top 30 UX rules organized by priority with do/don't examples. Covers all critical and high-priority rules.

2. **`references/design-checklist.md`** — Complete pre-delivery checklist covering visual quality, interaction, light/dark mode, layout, accessibility, performance, typography, and SEO.

3. **CSV files can be read directly** — Open `data/styles.csv`, `data/colors.csv`, `data/typography.csv`, `data/patterns.csv`, or `data/ux-rules.csv` and scan the `keywords` and `best_for` columns to find relevant entries manually.

4. **Common Design Patterns section above** — Use the pre-built pattern combinations for common project types (SaaS, agency, e-commerce, luxury, dev tool, wellness).

The references contain the most impactful subset of the full databases and are sufficient for most design decisions.
