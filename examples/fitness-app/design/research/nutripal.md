# C · NutriPal

**Source:** [Behance · AI Habit & Fitness Tracker Mobile App | UI UX Design · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design] read on 2026-11-09. The app in the case study is called NutriPal.
**Data:** 294 appreciations · 5,350 views · 96 comments [Behance data · project page]
**Why picked:** total 0.74, style `light;fill;neutral;large;cutout`; the only monochrome option
**Style guide:** yes: image 14 (grid), 15 (palette), 16 (typography), 23 (icons)
**Screens measured:** image 04, Food / Today (crop 1381,1778,4224,7943), design width 393. 1 pt = 7.23 image px: sharp enough for 1-cell accuracy.
**Context:** AI nutrition and fitness companion: food logging by photo, calories and macros, workouts by muscle group, rep explanations.
**Style in one line:** off-white base, white cards, near-black text and a dark floating tab bar; colour only in charts.

## UI

| Item | Value | Tag | Source |
|---|---|---|---|
| Design size | 393 wide | [Spec] | image 14 |
| Grid | "5 point grid system" | [Spec] | image 14 |
| Side margins | 20 | [Spec] | image 14 |
| Side margins (screens) | 16.3 (card 16.3 → 377.7) | [Measured] | 04.png · `edges --row 400` |
| Typeface | Lufga: Light, Regular, Medium, Semibold | [Spec] | image 16 |
| Palette | Primary / Texts #18181B · Charts / Metrics #24DA4D · Containers #FFFFFF · "Surface #0E0E0E" (label; the screens use an off-white base) | [Spec] | image 15 |
| Background | #FAFAFA | [Measured] | 04.png · `sample` (40,95) |
| Text colours | #121212 primary; #9D9D9D secondary | [Measured] | 04.png · `edges --col 21` |
| Page title | Two lines: "Today" near-black + date grey, both about 24 pt (cap height 16.5), Medium | [Measured] | 04.png · `edges --col 21–23`: 67.5 → 84.0 |
| Cards | white on #FAFAFA, very faint shadow, radius about 20 | [Measured ≈ ±2] (edge is faint) | 04_zoom_card.png |
| Card (macros) | 361 wide, about 272 tall | [Measured] | 04.png · `edges --row 400`, `--col 30` |
| Big numbers | Regular, about 28–32, with a small all-caps grey label above (CONSUMED / REMAINING) | [Observed] | image 04 |
| Progress | segmented vertical ticks, black filled / light grey remaining | [Observed] | image 04 |
| Charts | coloured only here (#24DA4D and red / orange for macros) | [Spec] + [Observed] | images 04, 15 |
| Tab Bar | floating dark pill #1C1C1C, about 58 tall, 12 from the edges; selected = white pill with icon + label; others icon only | [Measured] | 04.png · `edges --row 787`, `--col 30`: 758.9 → 816.8 |
| "+" action | separate dark circle about 64, next to the tab bar | [Measured] | 04.png · `edges --col 352`: 755.9 → 819.9 |
| Circle buttons | white circle, line icon (calendar) | [Observed] | image 04 |
| Imagery | food cut-outs in circles; 3D exercise figures | [Observed] | images 04, 24 |
| Icons | line icons, rounded | [Spec] | image 23 |

## Screen structure (Food / Today, image 04)

```
Status bar
"Today" / "13 Mar, Monday" (two-line title, black + grey)        calendar circle
Date ruler: 10 11 12 [13] 14 15 16 with tick marks
White card: CONSUMED 1908 · REMAINING 592 · segmented bar
            three macro gauges (Protein / Carbs / Fats)
Page dots
"Your Intake" ……………………… "356 of 712 Cal" (+)
Food card: photo cut-out · name · macros · kcal pill · ×
Floating dark tab bar (Home · Docs · [Food] · Profile) + separate "+" circle
```
Hero: the consumed / remaining numbers.

## UX

| Item | Practice | Source |
|---|---|---|
| Logging | Snap a photo → AI identifies the meal → confirm; or describe in text | image 22 |
| Workouts | AI workout plans, train by muscle group, rep explanation, exercise demos | images 22, 24 |
| Onboarding | Height and other details with a large number picker | image 19 |
| Date navigation | Horizontal date ruler | image 04 |
| Status feedback | Remaining calories always visible | image 04 |

## HIG / Nielsen check

| Finding | Basis | Verdict |
|---|---|---|
| Grey date #9D9D9D on #FAFAFA: 2.60:1 | [HIG · Accessibility] even large text needs 3:1 (`contrast.py`) | Do not adopt; darken the grey |
| Lufga Light listed as a weight | [HIG · Typography] avoid Light | Do not use Light |
| Unselected tabs are icon only | [HIG · Tab bars] every tab needs a text label | Do not adopt; keep labels |
| "+" as a separate circle, not a tab | [HIG · Tab bars] tabs are not actions | Can adopt |
| Green #24DA4D on white: 1.87:1 | Fine for chart fills, not for text | Charts only |
| Remaining calories always visible | [Nielsen #1] | Can adopt (remaining sets / rest time) |
| Photo logging with confirm step | [Nielsen #5] [Nielsen #7] | Pattern can be adopted |
| Style guide margin 20 vs screens 16.3 | — | Both offered in the choice questions |

## Differences between the style guide and the screens
- Side margins: guide 20, measured 16.3.
- "Surface #0E0E0E" in the palette, but screens use #FAFAFA as the base (the label may describe a dark-mode surface).

## 3 things worth learning / 3 things not to copy
- Learn: colour reserved for data; strong two-line title; floating dark tab bar with a separate add action.
- Do not copy: low-contrast grey text; icon-only tabs; Light weight.
