# Building in Figma

## Prerequisites

- Writing to Figma needs the Figma MCP server (tools such as `use_figma`, `create_new_file`). Before calling them, load the skills the Figma plugin provides: `figma-use` (required), plus `figma-generate-design` for full screens and `figma-generate-library` for variables and components. They explain correct API use and common pitfalls; they are not repeated here.
- If the user gave a Figma file link, work in that file; otherwise create one named `<App name> – Design`.
- If the Figma tools are unavailable (not connected or not authorised), tell the user to connect Figma in their client; until then, produce HTML screens (end of this file).

## Pages

```
📄 Cover          App name, version, date
📄 Rules          Visual version of the spec: palette, type scale, spacing, radii, component specs
📄 Components     Component library
📄 Hi-fi · 01 …   High fidelity, one page per flow (Light)
📄 Hi-fi · Dark   The same screens in Dark mode
📄 Archive        Old versions
```

## Build order

Bottom layer first. Changing one token then updates everything, and the AI cannot invent a different set of values on each screen (a major source of the AI look).

### 1. Variables
Built straight from the DESIGN.md §13 quick-reference table:

| Collection | Variables | Notes |
|---|---|---|
| `color` | `bg`, `surface`, `text/primary`, `text/secondary`, `accent`, `on-accent`, `destructive`, `border` (if any) | Light and Dark modes |
| `space` | `1`=4, `2`=8, `3`=12, `4`=16, `5`=24, `6`=32, `page`=24 | |
| `radius` | `card`, `sheet`, `pill`=999 | |
| `size` | `tap`=44, `button`=56, `input`=48, `icon`=24 | |

### 2. Text styles
From the DESIGN.md §3 type scale, named by role: `Title/Large`, `Title/Section`, `Body/Regular`, `Body/Emphasis`, `Caption`… Fixed line heights; only the weights the spec allows.

### 3. Components
Auto Layout everywhere, sizes and colours bound to variables, states as variants:

| Component | Variant properties |
|---|---|
| Button | `type`: primary / secondary / destructive / icon; `state`: default / pressed / disabled / loading |
| Input | `state`: empty / filled / focused / error |
| Chip / Slot | `selected`: true / false; `state`: default / disabled |
| List Row | `leading`: icon / avatar / none; `trailing`: chevron / pill / none |
| Info Row | label / value |
| Card | as needed |
| Top Bar | `type`: home / title / back |
| Tab Bar | `active`: each tab |
| Sheet | `size`: medium / large |
| Progress | `type`: bar / steps |
| Empty State | |

### 4. Screens
- Frame: the design size the user chose in DESIGN.md (default 393×852), named `<number> <screen name>`, such as `03 Room Detail`.
- Placeholders for the status bar and Home indicator; content inside the safe area.
- Place the hero first, then the rest; every spacing value is a variable, never typed by hand.
- Realistic sample data that agrees across screens (`anti-ai-checklist.md` §4).
- Screens of one flow in a row from left to right, a new row per flow, a text label above each row naming the flow.
- Other states of a screen (empty, loading, error) to its right.

### 5. HIG + Nielsen check for every screen

Each screen goes through this loop; the result goes in `design/screens.md`:

```markdown
## 05 Checkout
**Site map node:** Book › Checkout (modal, Tab Bar hidden)
**Hero:** total $24.00
**Figma:** <link or node ID>

Before drawing · rules this screen involves
- Payment: Apple Pay first, no smaller than other buttons [HIG · Apple Pay]
- Full summary before paying (time, room, amount) [Nielsen #5, #6]
- While waiting the button shows "Paying…" [HIG · Buttons][Nielsen #1]

After drawing · checks
- [x] DESIGN.md §14 checklist passes
- [x] Relevant HIG §15 items pass; contrast #6B6B6B/#FFFFFF = 5.3:1 (contrast.py)
- [x] Not AI-looking: clear hero, accent used once
- [ ] Fixed: Cancel was styled as primary, changed to secondary [HIG · Buttons]

Borrowed (if any)
- Collapsible price breakdown [Behance · <work> · <author> · <URL> · image 7]
```

After each flow, take a screenshot and check the flow looks consistent as a whole.

### 6. When out of ideas
When a screen has no counterpart in the 3 references, search Behance for that screen as described in `behance-research.md` §9, borrow its structure and interaction, keep DESIGN.md's visuals, and record it in DESIGN.md §15 and `screens.md`.

### 7. Building many screens faster with subagents
When the client can run subagents and there are more than about 8 screens:
1. Build steps 1–3 (variables, text styles, components, icons) yourself, in one sequential pass. Every screen depends on them, so they must exist before anyone draws.
2. Write a shared brief file next to the spec (e.g. `design/screens/_agent-brief.md`) with: the Figma file key; where the IDs of pages, variables, text styles and components are recorded; the frame rules (size, status bar, safe area, tab bar position); and **one block of sample data that every screen must use** (names, dates, weights, totals). Without it, parallel agents invent different numbers and the screens stop agreeing.
3. Give each subagent its own Figma page (or a fixed x-range on a shared page) and a list of screens. Tell it to touch nothing outside that area, and to change no variables or components.
4. Each subagent writes its per-screen check log (§5) to its own file. Merge the files into `screens.md` afterwards.
5. When they finish, run the walkthrough audit (SKILL.md Step 6) over all pages yourself. Problems that span flows only show up there.

## Deliverable: high fidelity, Light and Dark
The skill designs **straight in high fidelity**: the spec's real palette, type, components and data from the first screen. There is no separate low-fi deliverable; the user's chance to check structure is the per-screen log and the walkthrough audit (Step 6).

- **Light:** one page per flow, `Hi-fi · 01 …`, `Hi-fi · 02 …`.
- **Dark:** clone the finished screens to a `Hi-fi · Dark` page and set each frame's explicit variable mode to `Dark` (`setExplicitVariableModeForCollection`). Because every fill is a variable, the screens switch on their own. Check contrast in Dark with `scripts/contrast.py`. [HIG · Color]
- **States:** main state of each screen, plus the loading, empty, error, sheet and system presentations the flow needs (Live Activities, permission screens).
- **Images:** use real or licensed images. If none exist yet, use a light block with a centred icon and name the layer `… placeholder (replace with …)`, so the gap is obvious at handoff.

## HTML output when Figma is unavailable
- One `design/screens.html`: CSS variables at the top (named like the §13 table), one container per screen at the chosen size, laid out horizontally and grouped by flow.
- Only the system font stack (`-apple-system, "SF Pro Text", "Inter", sans-serif`) or the typeface the spec names.
- It can be imported into Figma later with a Figma plugin (such as `figma-code-workflows`).
