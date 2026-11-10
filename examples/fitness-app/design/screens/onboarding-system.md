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
