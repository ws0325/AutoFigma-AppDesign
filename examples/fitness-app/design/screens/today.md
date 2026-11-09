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
