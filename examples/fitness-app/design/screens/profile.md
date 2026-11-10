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
