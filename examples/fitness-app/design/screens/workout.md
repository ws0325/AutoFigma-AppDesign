# Workout flow (page "02 Today & Workout", x ≥ 1000)

Modal flow: no tab bar on any of these screens. Frames 393 × 852, 80 apart from x 1000.
Status bar cloned from `01 Onboarding · Goal` (node 12:235) so it is identical across screens.

## 05 Active Workout
**Figma node:** 21:92
**Site map:** Today → Start Workout → Active Workout (modal)
**Hero:** exercise title "Bench Press" (Title/Page)
Before drawing · rules this screen involves
- Modal top bar: Cancel (left) / Finish (right, Semibold), elapsed "18:42" centred with timer icon [HIG · Sheets] [Nielsen #1]
- "EXERCISE 1 OF 6" + "Set 3 of 4" in the header, elapsed time in the top bar [Nielsen #1]
- Cancel opens a "Discard workout?" confirmation before anything is thrown away (not drawn; behaviour) [Nielsen #3]
- Weight and reps set with Steppers, no free typing [Nielsen #5]
- Last time's "77.5 × 5" in every set row [Nielsen #6]
- Done circle 44; stepper circles 36 with 44 tap area [HIG · Accessibility]
After drawing · checks
- [x] One hero; one leading edge at 16
- [x] Only Inter Regular / Medium / Semibold via text styles; nothing under 11 pt
- [x] Text colours text/primary and text/secondary only
- [x] No green on this screen
- [x] Tap targets ≥ 44 (done circles 44, text buttons 44 high, Add Set 44 high); one primary button (Next Exercise)
- [x] Pill and radius 20 only; no shadow; the only stroke is the 2 pt ring on the current set's done circle (state indicator)
- [x] Tab bar hidden (modal)
- [x] Sample data: sets 80 / 80 / 82.5 / 82.5 × 5, previous 77.5 × 5, next Overhead Press 3 × 8 · 40 kg
- [ ] fixed: the set row does not fit 329 pt with five columns and two stock Steppers (128 each). Changed to: SET and PREVIOUS stacked in the first column (header "SET" over "PREVIOUS", row: number over "77.5 × 5"); Stepper instances narrowed by overriding spacing to 0 and value width (weight 116, reps 84). Rows stay 64 high; 7 pt between steppers so 44 tap areas do not overlap.
- [ ] fixed: card itemSpacing made rows 8 apart; set to 0 and gave the column header 40 pt instead.
- [ ] fixed: first stepper override (resizing the value text) did not take inside the instance; resized the instance with the value text set to Fill.

## 06 Active Workout · Resting
**Figma node:** 21:234
**Site map:** Active Workout, state right after set 2 is ticked
**Hero:** live rest card "1:24" (Number/Hero on color/action)
Before drawing · rules this screen involves
- Rest card mirrors the Live Activity shown on the Lock Screen / Dynamic Island while resting [HIG · Live Activities]
- Determinate bar: 6 high, track text/secondary, fill on-action at 30 % (36 s of 2:00 elapsed) [HIG · Progress indicators]
- Rest countdown, set 3 of 4, elapsed 18:42 all visible [Nielsen #1]
- "+30 s" and "Skip" pills 44 high inside the card [HIG · Accessibility]
- Text on the rest card in on-action at full opacity (no reduced-opacity text)
After drawing · checks
- [x] Rest card is the only hero; same table as 05 (rows 1–2 done, row 3 current ring, row 4 pending)
- [x] Only text/primary, text/secondary, and on-action on action fill
- [x] No green; tap targets ≥ 44; one primary button
- [x] Radius 20 card, pills; no shadow
- [x] Tab bar hidden
- [ ] note: the "Next: Overhead Press" card from 05 is replaced by the rest card while resting (both do not fit above Next Exercise)

## 07 Workout Summary
**Figma node:** 23:190
**Site map:** Active Workout → Finish → Summary (end of modal)
**Hero:** title "Push A done" with the 64 check mark
Before drawing · rules this screen involves
- Finish shows a summary before saving; Save Workout is the single primary action [Nielsen #5]
- PR marked with trophy icon + "PR" label + green marker, never colour alone [HIG · Accessibility] [HIG · Color]
- Label-over-number pairs for VOLUME / SETS / TIME [Borrowed: NutriPal img 04 pattern, DESIGN.md §15]
After drawing · checks
- [x] One hero; leading edge 16
- [x] Styles: Title/Page + Title/Page Secondary, Label, Number/Card, Heading/Card, Subhead, Callout, Button
- [x] Green used once (PR marker, with "PR" text in text/primary)
- [x] One primary button; Done text button 44 high
- [x] Sample data adds up: volume 1,625 + 960 + 720 + 288 + 900 + 450 = 4,943 kg; sets 4 + 5 × 3 = 19; 52 min
- [x] Tab bar hidden
- [ ] open: "Done" (top right) and "Save Workout" both end the flow; Done should mean Save, or be removed. Kept as briefed.
Borrowed: label-over-number stats card [Behance · NutriPal · Sriraj Mohan · image 04]

## 08 Sign In Sheet
**Figma node:** 23:262
**Site map:** Summary → Save Workout (first time) → Sign In sheet
**Hero:** sheet title "Save History"
Before drawing · rules this screen involves
- Sign-in asked late (on first save, after value is shown), not at launch; Sign in with Apple offered; working without an account allowed [HIG · Managing accounts]
- Sheet: surface, top radius 28 (radius/sheet), 36 × 5 grabber in data/track, page behind dimmed #000000 40 % [HIG · Sheets]
- Two clear choices, so no Cancel / Done in the sheet [HIG · Sheets]
- Apple button: pill 52, action fill, white text; glyph is a placeholder layer "Apple logo placeholder (use official asset)"
After drawing · checks
- [x] Summary behind is a copy of 07; home indicator kept on top of the sheet
- [x] Body: first sentence text/primary, second text/secondary
- [x] One filled action (Sign in with Apple) + secondary Button "Not Now"; both 52 high
- [x] Tap targets ≥ 44; no shadow; tab bar hidden
- [ ] note: dim rectangle uses hard-coded #000000 at 40 % (no variable exists for it; value comes from the brief)
- [ ] to do before shipping: replace the glyph placeholder with Apple's official Sign in with Apple button asset

## Writing trims (coordinator rule, HIG · Writing, Dec 16 2025)
- 08 sheet title "Save your history" → "Save History" (no possessive).
- 08 body "Sign in to keep your workouts on all your devices. Without an account, they stay on this iPhone." → "Keep workouts on all your devices. Without an account, they stay on this iPhone."
- 07 / 08 subtitle "Fri, Nov 13 · 52 min" → "Fri, Nov 13" (52 min is already in the TIME stat).
- 07 / 08 PR eyebrow "New personal record" → "New record" (the PR marker already says PR).
- 05 / 06: nothing to cut ("EXERCISE 1 OF 6", "Set 3 of 4", "Next: Overhead Press", "3 × 8 · 40 kg", "Add Set", "Next Exercise", "REST", "+30 s", "Skip").
