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
