# Shared brief for screen-building agents (Repwise demo)

Read this whole file before drawing. Everything visual comes from `examples/fitness-app/design/DESIGN.md` Part 3 (§1–§14); read it too.

## Figma
- File: https://www.figma.com/design/4OA6e0F7zsToQrgMqzkW6Z (fileKey `4OA6e0F7zsToQrgMqzkW6Z`).
- Create your own session with `create_session` (fileKey above) and pass it on every call.
- IDs of pages, variables, text styles, components and icons: `C:\Users\wangs\AppData\Local\Temp\claude\13b91c2c81314ffc\c0015816-558f-492e-bdca-252b8adb08de\scratchpad\repwise-figma-state.json`. Never guess IDs.
- Load the `figma:figma-use` and `figma:figma-generate-design` skills before your first `use_figma` call; pass `skillNames: "figma-use,figma-generate-design"`.
- Work ONLY on your assigned page(s) and inside your assigned x-range. Do not edit variables, text styles, components or icons. Other agents are drawing on other pages at the same time.
- Font: Inter, styles "Regular", "Medium", "Semi Bold" only. Apply the text styles by ID (`setTextStyleIdAsync`).
- Bind fills to the colour variables (`setBoundVariableForPaint`); never hard-code colours. Use instances of the components (Button, Icon Button, Chip, Tab Bar, List Row, Stepper, Icon/*). To recolour an icon instance, rebind the strokes of its vectors.

## Screen frame rules
- Frame 393 × 852, fill `color/bg`, name `NN Screen Name` (e.g. `03 Today`), clipsContent on.
- Status bar: top 54 pt; "9:41" (Body style, Semi Bold is fine via Heading/Card) at x 32, y 18; on the right three small shapes for signal / Wi-Fi / battery in text/primary. Keep it simple and identical on every screen.
- Home indicator: 134 × 5 pill, text/primary, centred, 8 pt from the bottom.
- Content column: x 16, width 361 (side margin 16). Use auto-layout for the content column and for every card.
- Tab Bar instance (when the screen is a tab root or a drill-down inside a tab): x 16, y 754 (852 − 34 − 64). Content must end at least 16 above it. Hidden on modal screens (Active Workout, Summary, Onboarding, sheets).
- Cards: fill `color/surface`, radius 20 (bind `radius/card`), padding 16, no stroke, no shadow.
- Page title: two lines, line 1 `Title/Page` text/primary, line 2 `Title/Page Secondary` text/secondary.
- Large numbers: `Number/Hero` or `Number/Card` with an all-caps `Label` above in text/secondary.
- Green `color/data/positive` at most once per screen, only for chart fills or a PR marker, always with a text label.
- Drill-down top bar: Icon Button with chevron-left at x 16, y 54; centred title (Heading/Card) or none.
- Modal top bar: text buttons "Cancel" (left) / action (right), Callout style.
- Sheets: surface fill, top radius 28, 36 × 5 grabber in data/track, page behind dimmed with a #000000 40% rectangle.

## Sample data (must be identical on every screen)
- Today is **Fri, Nov 13** (2026). User: **Daniel Park**. Units: kg.
- Plan: **Push / Pull / Legs**, 3 days: Mon **Legs A** (done), Wed **Pull A** (done), Fri **Push A** (today).
- Week before today's workout: VOLUME **12,450 kg** (Mon 6,820 + Wed 5,630), SESSIONS **2 of 3**.
- Latest PR before today: **Deadlift 140 kg × 5**, Wed.
- **Push A**: 6 exercises, about 55 min
  1. Bench Press 4 × 5 · 80 kg (previous: 77.5 kg × 5)
  2. Overhead Press 3 × 8 · 40 kg
  3. Incline Dumbbell Press 3 × 10 · 24 kg
  4. Lateral Raise 3 × 12 · 8 kg
  5. Triceps Pushdown 3 × 12 · 25 kg
  6. Cable Fly 3 × 12 · 12.5 kg
- During the workout: elapsed **18:42**; Bench Press sets: 1 = 80 × 5 done, 2 = 80 × 5 done, 3 = 82.5 × 5 (current), 4 = 82.5 × 5 (pending). Rest after set 2: **1:24** left of 2:00.
- After the workout: Bench sets 80×5, 80×5, 82.5×5, 82.5×5. Duration **52 min**, **19 sets**, VOLUME **4,943 kg**. New PR: **Bench Press 82.5 kg × 5** (previous best 80 kg × 5).
- Week after: **17,393 kg**, **3 of 3** sessions.
- PRs list: Bench Press 82.5 kg × 5 (Fri, Nov 13) · Deadlift 140 kg × 5 (Wed, Nov 11) · Back Squat 110 kg × 5 (Mon, Nov 9).
- Weekly volume, last 8 weeks (kg): 9,820 · 11,240 · 10,960 · 12,880 · 13,410 · 0 (rest week, show as empty) · 14,050 · 17,393 (this week).

## Writing rules
Title-case buttons, verb first. No "we", no emoji, no exclamation marks, no "Welcome back". Formats: `82.5 kg`, `5 reps`, `1:24`, `Fri, Nov 13`, `52 min`.

## When done with each screen
1. Take ONE screenshot of the screen, check it against DESIGN.md §14 and fix problems (clipped text, overlaps, contrast, missing labels). Take one more screenshot only after a fix.
2. Append a block to your log file `examples/fitness-app/design/screens/<your-log>.md` in this format:

```markdown
## 03 Today
**Figma node:** <id>
**Site map:** Today (tab root)
**Hero:** ...
Before drawing · rules this screen involves
- ... [HIG · ...] / [Nielsen #n]
After drawing · checks
- [x] ...
- [ ] fixed: ...
Borrowed (if any): ... [source]
```
3. In your final report return: every frame name + node ID, any rule you could not meet, and anything you changed after the screenshot check.
