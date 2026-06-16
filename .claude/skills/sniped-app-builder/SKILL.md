---
name: sniped-app-builder
description: Plan and build a mobile/software app from an idea using the proven no-code-to-code workflow (feasibility + API check, no-code visual prototype, screenshot UI/UX upgrade, implementation plan before code, React Native + Expo build, Expo Go device preview, QA). Use for app ideas, MVP plans, React Native / Expo builds, no-code-to-code, UI/UX upgrades from app screenshots, and product MVP planning. NOT for landing pages or websites (use sniped-web-builder).
---

# SNIPED App Builder

Turn an app idea into a working MVP without skipping the steps that make it actually ship. This skill plans and drives the build; Cursor writes the code, Expo runs it on device.

## When to use
App or software idea, app prototype, React Native / Expo build, no-code-to-code conversion, UI/UX upgrade from app screenshots, or product MVP planning. NOT a landing page or marketing site (route those to sniped-web-builder). NOT a film/copy task.

## Inputs required
The idea (one paragraph), who it is for, the one core job the app does, the platform (iOS, Android, or both), any must-have integrations, and any screenshots of a prototype or reference app. Missing inputs trigger the ask-human path below.

## Steps (run in order; do not skip ahead)
1. **App feasibility check** , can this be built by one operator with current tools? Name the core feature, the data it stores, the screens needed, and the single hardest technical risk. If the risk is unsolved, stop and surface it.
2. **API / data / integration check** , list every external API, data source, auth, and integration the core feature needs. For each: does a public API exist, is it paid, what is the rate/quota. If the user does not know what an API is, explain it plainly before continuing. No unresolved integration = no build.
3. **No-code prototype pass** , build the visual flow in a no-code tool (lovable / replit / similar) to SEE the user experience. This is throwaway: it proves the screens and flow, not the product. Capture screenshots of the main screens.
4. **Screenshot-to-UI-upgrade pass** , feed the screenshots to a UI/UX critique with the frame "you are a world-class UI/UX designer, improve these screens." Improve layout, visual hierarchy, interaction patterns, and conversion/retention logic (onboarding friction, the one core action, return triggers). Produce an upgraded mockup per screen.
5. **Implementation plan BEFORE code** , write the build plan: stack, screens, data model, navigation, the MVP cut line. Hand the upgraded screenshots + plan to Cursor and tell it explicitly to produce a PLAN and take NO action yet, so you can confirm it understands the vision before a line is written.
6. **React Native / Expo build path** , once the plan matches the vision, build in React Native (one codebase, iOS + Android) via Cursor. Give broad-but-guided instructions: enough freedom to solve, clear guardrails on the vision. Build the wireframe/skeleton first (the screens as empty pages from the screenshots), then fill features one at a time.
7. **Device preview / Expo Go check** , run the build through Expo Go on a real device to see what exists so far. Preview after each feature, not at the end.
8. **QA / test checklist** , the core action works end to end on a real device; navigation has no dead ends; data persists; no crash on the happy path; offline/empty/error states handled; the MVP cut line held (nothing past it shipped).

## Output format
- Feasibility verdict (buildable now / blocked + the blocker)
- API + integration table (api | exists | paid | quota | risk)
- Screen list + upgraded mockup notes per screen
- Implementation plan (stack, data model, navigation, MVP cut line)
- The Cursor plan-first instruction (verbatim, plan-no-action)
- Build order (wireframe first, then features)
- QA checklist with pass/fail per item

## Quality gate (pass/fail)
- Feasibility + UX direction are clear BEFORE any code (fail = stop).
- A plan was confirmed against the vision BEFORE coding (plan-before-action).
- Smallest working MVP only; anything past the cut line is rejected.
- Visual prototype (no-code) stays separate from production code (React Native).
- No build is called working without an Expo Go device preview + the QA checklist passing (no preview/test proof = not done).

## Proof / receipt
Log: the idea + core job, feasibility verdict, API/integration decisions + assumptions, the screens and MVP cut line, the build steps taken, the QA checklist results (pass/fail per item), and what still needs the human (real API keys, paid-tier confirmation, app-store accounts, brand assets). On a serious build, the conductor RECEIPT requirement (OS_RECEIPT) applies; do not claim done without the preview proof.

## Ask the human when
- The idea, target user, or core job is unclear.
- A required API is paid, gated, or has no public access (cost/approval call).
- App-store / developer accounts, real keys, or brand assets are missing.
- The platform (iOS / Android / both) is unconfirmed.

## Depends on
sniped-strategy-execution (the MVP-scope and what-to-build-first decision), os-quality-gates (completion-verification, output-usefulness), sniped-web-builder (sibling for any marketing page the app needs). Tools: Cursor, React Native + Expo (Expo Go), a no-code tool (lovable / replit), a UI/UX critique model. EXTERNAL-RESOURCE GAP: current per-tool specifics (Expo SDK version, React Native nav library, API pricing) are not encoded here; pull them live at build time.
