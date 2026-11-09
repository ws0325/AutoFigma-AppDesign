# Screens

**Figma file:** https://www.figma.com/design/4OA6e0F7zsToQrgMqzkW6Z (high fidelity; Light pages per flow + `Hi-fi · Dark`)
**Spec:** `DESIGN.md` · **Audit:** `audit.md`

| # | Screen | Figma page | Node (Light) | Node (Dark) |
|---|---|---|---|---|
| 01 | Onboarding · Goal | Hi-fi · 01 Onboarding | 12:234 | 40:897 |
| 02 | Onboarding · Experience | Hi-fi · 01 Onboarding | 12:274 | 40:935 |
| 03 | Today | Hi-fi · 02 Today & Workout | 17:2 | 40:973 |
| 04 | Workout Preview | Hi-fi · 02 Today & Workout | 17:320 | 40:1092 |
| 05 | Active Workout | Hi-fi · 02 Today & Workout | 21:92 | 40:1162 |
| 06 | Active Workout · Resting | Hi-fi · 02 Today & Workout | 21:234 | 40:1239 |
| 07 | Workout Summary | Hi-fi · 02 Today & Workout | 23:190 | 40:1325 |
| 08 | Sign In Sheet | Hi-fi · 02 Today & Workout | 23:262 | 40:1392 |
| 09 | Library | Hi-fi · 03 Library & Progress | 17:154 | 40:1471 |
| 10 | Exercise Detail | Hi-fi · 03 Library & Progress | 17:419 | 40:1505 |
| 11 | Progress | Hi-fi · 03 Library & Progress | 21:446 | 40:1547 |
| 12 | Session Detail | Hi-fi · 03 Library & Progress | 23:471 | 40:1617 |
| 13 | Profile | Hi-fi · 04 Profile & Account | 12:2 | 40:1679 |
| 14 | Account | Hi-fi · 04 Profile & Account | 12:92 | 40:1745 |
| 15 | Delete Account Sheet | Hi-fi · 04 Profile & Account | 12:146 | 40:1778 |
| 16 | Reminders Permission | Hi-fi · 04 Profile & Account | 12:210 | 40:1821 |
| 20 | Live Activity · Lock Screen | Hi-fi · 05 System | 17:261 | (system surface, not themed) |
| 21 | Live Activity · Dynamic Island | Hi-fi · 05 System | 17:292 | (system surface, not themed) |

The blocks below are the per-screen logs written while drawing (rules checked before, checklist after). Screens were drawn in parallel by four subagents from `screens/_agent-brief.md`; later fixes from the walkthrough are listed in `audit.md`.


---

# Onboarding and system screens (pages "01 Onboarding" and "05 System (Live Activity)")

## 01 Onboarding · Goal
**Figma node:** 12:234
**Site map:** First launch → Onboarding step 1 of 2 (modal flow, no tab bar)
**Hero:** Page title "What’s your goal?" / "Pick one. You can change it later."
Before drawing · rules this screen involves
- Onboarding is short (2 questions), skippable on every step, no sign-in and no permission requests [HIG · Onboarding] [DESIGN §8]
- Step indicator "1 of 2" shows where the user is in the flow [Nielsen #1]
- "You can change it later" lowers the cost of the choice [Nielsen #3]
- Selected option = action fill + on-action text + check icon, so state is not shown by colour alone; unselected = surface, no outline [DESIGN §1.5] [HIG · Accessibility]
- One primary button ("Continue"), ends 34 above the bottom; no tab bar in a modal flow [DESIGN §6] [_agent-brief]
After drawing · checks
- [x] One leading edge at 16; content column (title + options) is auto-layout, 361 wide, ends at y 488
- [x] Option cards 361 × 72, surface / action fill, radius bound to radius/card, padding bound to space/4, no shadow or border
- [x] Only Inter via text styles (Title/Page, Title/Page Secondary, Heading/Card, Subhead, Callout, Label); smallest text Label 12
- [x] Text colours only text/primary, text/secondary, and on-action on the selected card; no green
- [x] Skip tap area 56 × 44; options 72 high; Continue 52 high at y 766 (ends at 818 = 852 − 34)
- [x] Title line 2 wraps to two lines at 28 pt without clipping
- [ ] fixed: straight apostrophe in "What's" replaced with a typographic ’
Borrowed (if any): large full-width option list for a single-choice onboarding question [Behance · Home workout app for fitness · SK RADWOAN et al. · https://www.behance.net/gallery/251510807/Home-workout-app-for-fitness · images 04, 06]

## 02 Onboarding · Experience
**Figma node:** 12:274
**Site map:** First launch → Onboarding step 2 of 2 (modal flow, no tab bar)
**Hero:** Page title "How long have you been lifting?" / "This sets your starting weights."
Before drawing · rules this screen involves
- Same layout as step 1 so the flow feels like one task [Nielsen #4] [HIG · Onboarding]
- Line 2 explains why the question is asked (starting weights) [HIG · Onboarding] [Nielsen #2]
- Skip available; "2 of 2" tells the user this is the last question [Nielsen #1] [Nielsen #3]
After drawing · checks
- [x] Title line 1 wraps to two lines, line 2 to two lines; no clipping; content ends at y 522, well above the button at 766
- [x] "3–12 Months" selected with action fill, on-action text and check icon (strokes bound to on-action)
- [x] Frame placed at x 473 (80 to the right of 01)
- [x] One primary button; no tab bar; no green
Borrowed (if any): same option-list pattern as 01 [Behance · Home workout app for fitness · SK RADWOAN et al. · https://www.behance.net/gallery/251510807/Home-workout-app-for-fitness · images 04, 06]

## 20 Live Activity · Lock Screen
**Figma node:** 17:261
**Site map:** System → Lock Screen while resting between sets (Active Workout running)
**Hero:** Countdown "1:24" in the Live Activity banner
Before drawing · rules this screen involves
- Live Activity shows only the one time-sensitive thing (rest left), with a determinate progress bar; no ads, no promotional content [HIG · Live Activities] [Nielsen #1]
- At most one interactive element ("Skip Rest"); the rest of the banner opens the app [HIG · Live Activities]
- Text at Medium weight or heavier for Lock Screen legibility [HIG · Live Activities]
- Banner is 361 wide, 14 inside margins, radius 24 (system-like Live Activity shape) [_agent-brief]
- Rest is the same data as Active Workout: 1:24 left of 2:00 (30% done), next set 3 · 82.5 kg × 5 [DESIGN §7] [_agent-brief sample data]
- No push notification for the same event [HIG · Live Activities] [DESIGN §8]
After drawing · checks
- [x] Whole frame set to the Dark mode of the Color collection; every fill is a variable: bg #000000, surface #1C1C1E, text/primary white, text/secondary #A1A1AA, data/track #3A3A3C, action white — no hard-coded colours
- [x] Banner 361 × 158 at x 16, y 600; padding 14; progress track 6 high with 30% fill (100 of 333)
- [x] "Skip Rest" is the Button component (Primary), resized to 120 × 44 — white pill with dark text in Dark mode; the only interactive element
- [x] "Next: Set 3 · 82.5 kg × 5" in Callout (Medium) text/secondary, about 6.6:1 on #1C1C1E
- [x] Home indicator and status bar in text/primary (white)
- Note: the Lock Screen clock "9:41" uses Number/Hero overridden to Inter Semi Bold 88/100, because no text style is big enough for the system clock. It stands for system UI, not app type.
- Not met: the countdown "1:24" uses Number/Hero (Inter Regular 48) as assigned; HIG asks for Medium or heavier text in Live Activities. Changing it would detach the text style.
Borrowed (if any): none (Live Activity layout follows [HIG · Live Activities])

## 21 Live Activity · Dynamic Island
**Figma node:** 17:292
**Site map:** System → Dynamic Island while resting (app in background)
**Hero:** Countdown "1:24" in the Expanded state
Before drawing · rules this screen involves
- Compact: leading timer icon, trailing countdown; Minimal: icon only; Expanded: title, countdown, progress, one button [HIG · Live Activities]
- Island is pure black so it blends with the camera housing [HIG · Live Activities]
- Same data and words as the Lock Screen banner [Nielsen #4]
After drawing · checks
- [x] Each island node set to Dark mode and filled with color/bg (#000000); text and icons text/primary (white); frame background is color/bg Light (#F8F8F8) so the black islands are visible
- [x] Compact 126 × 37 pill (radius/pill), Minimal 28 circle, Expanded 361 × 160 radius 44; each with a Label caption above
- [x] Expanded progress bar 30% (94 of 313); Skip Rest Button instance 120 × 44
- Not met: frame height is 393, not 200 — the Expanded state alone is 160 high, so the three states with captions cannot fit in 200. The frame hugs its content.
- Not met: Minimal is 28 as specified (the real system minimal view is about 37); its tap target is below 44, but the system owns that touch area.
- Note: the countdown uses Number/Hero (Regular) as in 20; see the note there.
Borrowed (if any): none (layout follows [HIG · Live Activities])

---

# Today & Workout Preview (page "02 Today & Workout", x 0–900)

## 03 Today
**Figma node:** 17:2
**Site map:** Today (tab root)
**Hero:** Workout card "Push A" with Start Workout inside it
Before drawing · rules this screen involves
- Two-line page title "Today" / "Fri, Nov 13", calendar Icon Button 44 on the right, centred on the title block [HIG · Layout] [DESIGN §7]
- Week strip: trained = filled action circle + check, today = ring + label in text/primary, rest/future = surface-muted circle with the date [DESIGN §6] [Nielsen #1]
- This week: label-over-number pairs (VOLUME 12,450 kg, SESSIONS 2 of 3) + volume ticks 4 wide / 8 gap, done in action, remaining in data/track [Nielsen #1]
- Start Workout reachable in one tap from the tab root [Nielsen #7] [HIG · Buttons]
- Green only once: PR marker dot, with the text "PR" and the trophy icon [HIG · Color] [HIG · Accessibility]
- Floating Tab Bar instance Active=Today at y 754; content ends ≥ 16 above it [HIG · Tab bars] [HIG · Layout]
After drawing · checks
- [x] One hero; one leading edge at 16 (content column x 16, w 361)
- [x] Only Inter Regular / Medium / Semi Bold through the text styles; nothing under 11 pt (smallest: Label 12, Tab 11)
- [x] Text colours only text/primary and text/secondary; every fill bound to a color/* variable
- [x] Accent once (PR dot) with label "PR"
- [x] Tap targets ≥ 44 (Icon Button 44, Button 52, Tab Bar 64); one primary button
- [x] Pill or radius 20 (bound to radius/card) only; no shadow; the only stroke is the today ring the week-strip spec asks for
- [x] Tab bar visible; content ends at y 736 (≤ 738)
- [x] Sample data matches the brief (Push A rows, 12,450 kg, 2 of 3, Deadlift 140 kg × 5 Wed)
- [ ] fixed: nothing needed after the screenshot
Notes
- To fit above the tab bar with 24 between groups, the Latest PR row sits inside the This week card (16 below the ticks) instead of its own card. A separate card needs ~100 pt more than is available.
- Week circles are 32 (display only; the calendar button is the tap target). Trained days show the check in place of the date, so 9 and 11 are not printed.
- Ticks: 27 total, 19 done = 12,450 of ~17,400 kg planned for the week (Mon + Wed done + Push A 4,943).
Borrowed: two-line title + circle action, label-over-number + ticks, floating dark tab bar [Behance · AI Habit & Fitness Tracker Mobile App | UI UX Design (NutriPal) · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design · image 04]

## 04 Workout Preview
**Figma node:** 17:320
**Site map:** Today → Workout Preview (drill-down, tab bar visible)
**Hero:** Title "Push A" / "6 exercises · about 55 min"
Before drawing · rules this screen involves
- Drill-down top bar: Icon Button chevron-left at x 16, y 54 [HIG · Navigation] [brief]
- Two-line title under the back button (line 2 measures 347 pt, fits 361 without wrapping)
- One card with all 6 exercises as rows: 44 muted circle with index, name (Body), "sets × reps · weight" (Subhead secondary), chevron [DESIGN §6 List row]
- Bench Press shows "Last time 77.5 kg × 5" [Nielsen #6]
- Start Workout pinned above the tab bar, Edit Plan as a text button below it [Nielsen #7] [HIG · Buttons]
After drawing · checks
- [x] One hero; one leading edge at 16
- [x] Only Inter Regular / Medium / Semi Bold; nothing under 11 pt
- [x] Text colours only text/primary and text/secondary
- [x] No accent on this screen
- [x] Tap targets ≥ 44 (back 44, rows 60, Start Workout 52, Edit Plan 44 high full width); one primary button
- [x] Radius 20 card / pills / circles only; no shadow, no border
- [x] Tab bar visible (Active=Today); bottom actions end at y 738, card ends at 608 (30 above the button)
- [x] Sample data matches the brief (6 exercises, weights, previous 77.5 kg × 5)
- [ ] fixed: nothing needed after the screenshot
Notes
- Exercise rows are 60 high (44 thumbnail + 8 top/bottom), Bench Press 78 with the extra line; the List Row spec says 64, but 6 × 64 does not fit above the pinned buttons. Rows are built from frames (not List Row instances) because the List Row thumbnail cannot hold an index number.
- Status bar cloned from 03 Today so both screens are identical.
Borrowed: floating dark tab bar [Behance · AI Habit & Fitness Tracker Mobile App | UI UX Design (NutriPal) · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design · image 04]

---

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

---

# Page "03 Library & Progress" · screen log

State shown: after today's workout (Push A, Fri, Nov 13) was saved. Frames 393 × 852, 80 apart from x 0.
Audit after drawing (all four frames): every fill outside instances is bound to a colour variable; every text node uses a text style; Inter Regular / Medium / Semi Bold only; smallest text 11 (tab labels); no strokes or effects; green (`color/data/positive`) used on 0 / 0 / 1 / 1 nodes.

Writing pass (coordinator rule, [HIG · Writing] Dec 16, 2025: "use fewer words"), applied to all four screens after the first drawing:
- 09: placeholder "Search exercises" → "Search" (the page is already the exercise library); row subtitles "Chest · Barbell" etc. → "Barbell", "Dumbbell", "Cable", "Bodyweight", "Machine" (the selected Chest chip already says Chest).
- 10: How-to steps cut to one line each: "Eyes under the bar." / "Lower to mid-chest, elbows 45°." / "Press until arms are straight."; no "Your best" heading (card layer renamed "Best Set").
- 11: "Personal records" → "Records".
- 12: Bench Press summary "4 sets · 1,625 kg" → "1,625 kg" (the four set rows are visible right below it).

## 09 Library
**Figma node:** 17:154
**Site map:** Library (tab root)
**Hero:** page title "Library" / "142 exercises"
Before drawing · rules this screen involves
- Tab Bar instance Active=Library, labels on every tab, at y 754 [HIG · Tab bars]
- Search field is a pill (48 high, surface fill) with a search icon and placeholder in text/secondary (5.30:1 on surface) [HIG · Accessibility]
- Selected chip = filled near-black, unselected = white, no outline (DESIGN §1.5); chips 8 apart, row runs off the right edge as a scroll hint
- Rows use the List Row component (64 high, 44 thumbnail, chevron) [Nielsen #4]
- Content ends at least 16 above the tab bar [HIG · Layout]
After drawing · checks
- [x] One hero (two-line title); leading edge 16
- [x] All six exercises fit; content ends at y 674 (tab bar at 754)
- [x] No green; text colours only primary / secondary
- [ ] fixed: the chip row was clipped at x 377 by its auto-layout parent; clipping turned off so the chips run to the screen edge (the scroll hint)
- [ ] fixed: List Row already has 16 side padding, so the list card uses 0 side / 8 top and bottom padding. The visual inset is still 16, with no 32-pt double inset.
- [ ] fixed (writing pass): placeholder and subtitles trimmed, see above
Borrowed: none

## 10 Exercise Detail
**Figma node:** 17:419
**Site map:** Library › Exercise Detail (drill-down; Tab Bar Active=Library)
**Hero:** "Bench Press" / "Chest · Barbell"
Before drawing · rules this screen involves
- Chevron-left Icon Button (44 circle) at x 16, y 54 [HIG · Accessibility]
- Best set shown so the lifter does not have to remember it [Nielsen #6]
- Three-step form guide [Nielsen #10]
- One primary button "Add to Workout" (title case, verb first) [HIG · Buttons]
- Label-over-number pairs [Behance · NutriPal · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design · image 04]
- Content ends at least 16 above the tab bar [HIG · Layout]
After drawing · checks
- [x] Image placeholder 361 × 200, surface-muted, radius 20, centred 32 dumbbell icon in text/secondary, layer "Exercise demo placeholder (cut-out figure)"
- [x] BEST SET 82.5 kg × 5 · Fri, Nov 13 matches the new PR on other screens
- [x] One primary button; content ends at y 732
- [ ] fixed: with the long step text (two lines each) and a "Your best" heading, the content ended at y 826, 88 below the limit. A temporary fix (heading removed, 12 gaps, image 160 high) was replaced in the writing pass: one-line steps freed the space, so the image is back at 361 × 200.
Data note: LAST 4 WEEKS = 4,775 kg over 3 workouts, an assumed Bench Press history: today 1,625 (80×5×2 + 82.5×5×2), Fri, Nov 6 1,550 (4 × 5 × 77.5), rest week, Fri, Oct 23 1,600 (4 × 5 × 80, the previous best).
Borrowed: label-over-number pair [Behance · NutriPal · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design · image 04]

## 11 Progress
**Figma node:** 21:446
**Site map:** Progress (tab root)
**Hero:** VOLUME 17,393 kg
Before drawing · rules this screen involves
- Tab Bar Active=Progress [HIG · Tab bars]
- Status of the week (3 of 3, change vs last week) [Nielsen #1]
- Green only once: this week's bar, with the label "THIS WEEK" under it [HIG · Accessibility] (never colour alone)
- Rest week drawn as an empty data/track slot, labelled "REST" (not a fake zero bar) (DESIGN §12)
- Label-over-number + segmented slots [Behance · NutriPal · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design · image 04]
- "See All" sits on the same baseline as "History", with a 44 tap area [HIG · Accessibility]
After drawing · checks
- [x] 17,393 vs 14,050 = +23.8% → "up 24%"
- [x] 8 bars from the sample data, heights to scale (max 17,393 = 56 pt); every week has a data/track slot, filled in color/action; this week in data/positive
- [x] PR rows: trophy icon + name + date + value; dates Fri, Nov 13 / Wed, Nov 11 / Mon, Nov 9
- [x] History: one row (Push A · Fri, Nov 13 · 52 min · 4,943 kg); a second row does not fit above the tab bar
- [ ] fixed: content ended at 740 (2 over); the hero card's inner gap went from 16 to 12, so content now ends at 736
- [ ] fixed (writing pass): "Personal records" → "Records"
- Note: week labels are sparse (SEP 21, OCT 5, REST, THIS WEEK). Labels on all 8 weeks overlap at 12 pt in a 329-wide card. "THIS WEEK" is right-aligned to the card edge under the green bar.
Borrowed: label-over-number and segmented track [Behance · NutriPal · Sriraj Mohan · image 04, URL above]

## 12 Session Detail
**Figma node:** 23:471
**Site map:** Progress › History › Session Detail (drill-down; Tab Bar Active=Progress)
**Hero:** "Push A" / "Fri, Nov 13 · 52 min"
Before drawing · rules this screen involves
- Chevron-left Icon Button at x 16, y 54 [HIG · Accessibility]
- PR marker = green pill + trophy icon + "PR" text in text/primary, never colour alone [HIG · Accessibility]
- "Repeat Workout" secondary button for a one-tap restart [Nielsen #7]
- Set rows read like the Active Workout rows: set number in secondary, weight × reps in primary [Nielsen #4]
- Label-over-number pairs VOLUME / SETS [Behance · NutriPal · image 04, URL above]
After drawing · checks
- [x] Totals add up: Bench 1,625 + OHP 960 + Incline DB 720 + Lateral 288 + Pushdown 900 + Cable Fly 450 = 4,943 kg; sets 4 + 5 × 3 = 19
- [x] Green once (the PR marker on set 3, 82.5 kg × 5)
- [x] No primary button (the Secondary button is the only button); content ends at y 734
- [x] No cards in cards: set rows sit directly in the exercise card
- [ ] fixed (writing pass): "4 sets · 1,625 kg" → "1,625 kg"
- Note: set rows are 30 high and the other-exercise rows 32 high so everything fits above the tab bar. These rows are not interactive, so the 44 tap-target rule does not apply.
Borrowed: label-over-number pair [Behance · NutriPal · image 04, URL above]

---

# Profile & Account screens (page "04 Profile & Account")

## 13 Profile
**Figma node:** 12:2
**Site map:** Profile (tab root)
**Hero:** Name "Daniel Park" with avatar; stats card WORKOUTS 46 · THIS MONTH 9 · STREAK 4 wk
Before drawing · rules this screen involves
- Tab Bar visible with Active=Profile; labels on every tab [HIG · Tab bars]
- Content clears the floating tab bar by at least 16 [HIG · Layout]
- Label-over-number stats, no fire emoji, streak in weeks [DESIGN §1, §12]
- Settings rows show current value on the right so state is visible without opening each row [Nielsen #1] [Nielsen #6]
- Account deletion reachable from Profile → Account [HIG · Managing accounts]
After drawing · checks
- [x] One leading edge at 16; content column 361 wide, auto-layout everywhere
- [x] Only Inter Regular / Medium / Semi Bold via text styles; smallest text is Label 12
- [x] Text colours only text/primary and text/secondary; no green on this screen
- [x] Rows 52 high (tap ≥ 44); no primary button on screen
- [x] Cards radius 20 bound to radius/card, no shadow or border
- [x] Sample data consistent (Push / Pull / Legs, kg, rest 2:00, 46 workouts)
- [ ] fixed: content column ended at y 740, only 14 above the tab bar (754). Moved column from y 70 to y 64; it now ends at 734 (20 clear).
- Note: the two list cards use 4 vertical padding (16 horizontal) instead of 16, because each 52-high row already insets its text by 15; the visual inset from the card edge is about 19. With 16 vertical padding the screen does not fit above the tab bar.
Borrowed (if any): none beyond the shared tab bar and label-over-number card [Behance · NutriPal · image 04]

## 14 Account
**Figma node:** 12:92
**Site map:** Profile → Account (drill-down)
**Hero:** Page title "Account" / "Signed in with Apple"
Before drawing · rules this screen involves
- Account deletion is easy to find (on the Account screen, not buried) and says when it finishes ("Takes up to 24 hours") [HIG · Managing accounts]
- Destructive action uses the destructive (secondary-shape) style, never the primary style [HIG · Buttons]
- Destructive button separated by 32 from Sign Out to avoid mis-taps [Nielsen #5]
- Consequence stated before the action in the footnote [Nielsen #5]
- Drill-down: back chevron at x 16, y 54; Tab Bar Active=Profile [HIG · Tab bars]
After drawing · checks
- [x] Info rows: label 15 secondary left / value 16 Medium right; longest value "Stored on this iPhone and in iCloud" fits on one line
- [x] No primary button; Sign Out secondary, Delete Account destructive
- [x] Footnote in text/secondary, wraps to two lines, no clipping
- [x] Content ends at y 581, well above the tab bar
Borrowed (if any): none

## 15 Delete Account Sheet
**Figma node:** 12:146
**Site map:** Profile → Account → Delete Account (sheet)
**Hero:** Sheet title "Delete your account?"
Before drawing · rules this screen involves
- Confirmation before deletion, stating exactly what is deleted (46 workouts, plan, 3 personal records) and that it cannot be undone [HIG · Managing accounts] [Nielsen #5]
- Confirm button keeps the destructive style; it is not promoted to primary [HIG · Buttons]
- Sheet: surface fill, top radius 28 (radius/sheet), grabber, page behind dimmed 40% black [HIG · Sheets]
- Cancel is always available as a clear exit [Nielsen #3]
After drawing · checks
- [x] Sheet height 310, sits at bottom; home indicator kept on top
- [x] Body wraps to 3 lines, no clipping; data matches 13 Profile (46 workouts) and PRs list (3 records)
- [x] Tab bar is covered by the dim and sheet (sheets hide the tab bar)
- Note: the sheet uses the two stacked buttons from the brief instead of the Cancel / Done top bar listed in DESIGN §6 Sheet; a destructive confirmation reads better as an action-sheet-style stack, and Cancel is still present [HIG · Sheets] [Nielsen #3]
Borrowed (if any): none

## 16 Reminders Permission
**Figma node:** 12:210
**Site map:** Profile → Reminders toggle → pre-permission explainer → system notification alert
**Hero:** Title "Workout-day reminders" / "One notification on Mon, Wed and Fri"
Before drawing · rules this screen involves
- Ask in context (only when the user turns Reminders on), explain the benefit first [HIG · Privacy] [DESIGN §8]
- Pre-permission screen has exactly one button, "Continue", which leads to the system alert; no "Not Now" / "Cancel" [HIG · Privacy]
- Full-screen step, so no tab bar [DESIGN brief]
After drawing · checks
- [x] Exactly one button (Primary "Continue"), 52 high, at y 766
- [x] Bell icon in an 80 surface-muted circle, icon strokes bound to text/primary
- [x] Title line 2 wraps to two lines at 28 pt without clipping; body two lines
- [x] Only text/primary and text/secondary; no green
- Note: the back chevron (drill-down feel) remains as navigation; it is not an extra action button. If a strict reading of HIG wants no way back, remove it.
Borrowed (if any): none
