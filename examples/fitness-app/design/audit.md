# Walkthrough audit: Repwise v1.0

**Date:** 2026-11-09, colour update 2026-11-10 · **Scope:** 18 hi-fi screens (16 app screens in Light and Dark, 2 system presentations) · **Spec:** `DESIGN.md`
**Method:** each main task walked end to end against Nielsen's 10 heuristics; the whole app checked against `apple-hig-rules.md` §15 (including the new §14a Writing) and `anti-ai-checklist.md` §5. Contrast computed with `scripts/contrast.py`. Severity uses Nielsen's 0–4 scale.

## Already complies

- **One hero per screen**, one leading edge at 16, content inside the safe area, tab bar hidden in modal flows. [HIG · Layout] [HIG · Tab bars]
- **One accent:** cyan #22D3EE (since v1.1; green before) only on actions, selected states and one data highlight per screen, always with the text "PR" or "THIS WEEK"; text on cyan is near-black (10.31:1). [HIG · Color] [HIG · Accessibility]
- **Contrast:** text/primary 16.7:1 and text/secondary 4.99:1 on the Light base; white 21:1 and #A1A1AA 8.19:1 on the Dark base; destructive 4.83:1 (Light) and 4.99:1 (Dark). [HIG · Accessibility]
- **Account rules:** sign-in only when saving the first workout, with Sign in with Apple and a "Not Now" that keeps data on the iPhone; Delete Account is easy to find, never the primary style, states what is removed and when. [HIG · Managing accounts] [HIG · Buttons]
- **Permission:** reminders explainer has exactly one "Continue" button and appears when the user turns reminders on. [HIG · Privacy]
- **Live Activity:** one control (Skip Rest), determinate bar, countdown in Medium weight; no push for the same rest event. [HIG · Live Activities]
- **Data agrees across screens:** 12,450 + 4,943 = 17,393 kg; 19 sets; 52 min; Bench Press 82.5 kg × 5 PR on Summary, Exercise Detail, Progress and Session Detail.
- **Not AI-looking:** no gradients, glows, emoji or shadows; one icon set; one pill + one card radius; no "Welcome back".

## Task walkthroughs (Nielsen)

### Task 1: start today's workout and log the first exercise
| Step | Screen | Finding | Heuristic | Severity | Status |
|---|---|---|---|---|---|
| 1 | 03 Today | "Start Workout" reachable in one tap from the home screen | #7 | 0 | complies |
| 2 | 04 Workout Preview | "Last time 77.5 kg × 5" shown before starting | #6 | 0 | complies |
| 3 | 05 Active Workout | "Set 3 of 4", elapsed time and previous values always visible | #1 #6 | 0 | complies |
| 4 | 05 Active Workout | "Cancel" should ask "Discard workout?"; the dialog is specified but not drawn | #3 | 2 | **open** |
| 5 | 06 Resting | Rest countdown with a determinate bar, +30 s and Skip | #1 #3 | 0 | complies |
| 6 | 07 Summary | Two actions did the same thing ("Done" and "Save Workout") | #4 | 2 | **fixed**: "Done" removed |

### Task 2: save the first workout without an account
| Step | Screen | Finding | Heuristic | Severity | Status |
|---|---|---|---|---|---|
| 1 | 08 Sign In Sheet | "Not Now" keeps data on the device; no forced sign-up | #3 | 0 | complies |
| 2 | 08 Sign In Sheet | Apple logo is a placeholder circle; must use Apple's official asset before release | #4 | 3 | **open** (asset) |

### Task 3: check progress and repeat a workout
| Step | Screen | Finding | Heuristic | Severity | Status |
|---|---|---|---|---|---|
| 1 | 11 Progress | Only 4 of 8 week labels fit under the chart | #6 | 1 | open (cosmetic) |
| 2 | 11 Progress | One history row fits above the tab bar; "See All" leads to more | #8 | 0 | complies |
| 3 | 12 Session Detail | "Repeat Workout" shortcut | #7 | 0 | complies |

### Task 4: turn on reminders, delete the account
| Step | Screen | Finding | Heuristic | Severity | Status |
|---|---|---|---|---|---|
| 1 | 16 Reminders | Back chevron offered a way out of the pre-permission screen | HIG Privacy | 3 | **fixed**: removed |
| 2 | 15 Delete Sheet | Consequence stated before deleting; Cancel available | #3 #5 | 0 | complies |

## Fixed during the audit

| # | Problem | Basis | Fix |
|---|---|---|---|
| 1 | Too many words: "TODAY · PUSH A" above "Push A"; "Personal record · Wed" next to a "PR" marker; plan repeated under the profile name; "Sign-in" row repeating the page subtitle; reminders body repeating its subtitle; "your" in several places | [HIG · Writing] "If you can use fewer words, do so." | Trimmed on 9 strings, 3 rows/sentences removed; rule added to the skill (`apple-hig-rules.md` §14a) and DESIGN.md §11 |
| 2 | "SESSIONS" / "sessions" while the spec says "workout" | [Nielsen #4] [HIG · Writing] consistent terms | Changed to "WORKOUTS" / "workouts" |
| 3 | Live Activity countdown in Regular | [HIG · Live Activities] Medium or heavier | Set to Medium on Lock Screen and both island states |
| 4 | List Row text area had an unbound white fill: invisible in Light, white blocks in Dark | Tokens must cover every fill | Fill removed in the component; all pages scanned for unbound white fills (2 more found in status-bar icons and removed) |
| 5 | Profile screens used a different status bar drawing | [Nielsen #4] | Replaced with the shared status bar |
| 6 | Dark mode: unselected tab label #8E8E93 on the white Dark tab bar = 3.26:1 | [HIG · Accessibility] | Dark value changed to #6B6B70 (5.30:1) |
| 7 | Reminders subtitle broke "6:00 / PM" across lines | [HIG · Writing] | "Mon, Wed, Fri · 6:00 PM" |
| 8 | System presentations were themed by the app's Dark mode, hiding the black island on a black page | System surfaces are not app-themed | Excluded from `Hi-fi · Dark` |

## Open items (for the next iteration)

| # | Item | Severity | Note |
|---|---|---|---|
| 1 | "Discard workout?" confirmation for Cancel in Active Workout | 2 | Specified in DESIGN.md §10; not drawn |
| 2 | Official Sign in with Apple button asset | 3 | Placeholder layer is named "Apple logo placeholder (use official asset)" |
| 3 | Exercise demo images | 2 | Placeholder on Exercise Detail; needs licensed or commissioned cut-outs |
| 4 | Today: latest PR sits inside the "This week" card; Workout Preview rows 60 high instead of 64 | 1 | Space compromises above the floating tab bar |
| 5 | Progress chart shows 4 of 8 week labels | 1 | Consider a scrollable chart or shorter labels |
| 6 | Custom floating tab bar instead of the system Liquid Glass bar | 1 | Deliberate (decision record #3); labels kept on every tab |
| 7 | Settings cards on Profile use 4 pt vertical padding | 1 | Needed to fit above the tab bar |
| 8 | Empty, loading and error states (e.g. first launch with no workouts, save failure with Retry) | 2 | Specified in DESIGN.md §10 (#9); not drawn in v1 |

## Self-check questions (anti-AI-checklist §5)
1. Cover the name: the monochrome cards, numbers-first layout and dark floating tab bar still read as one app.
2. Three removable elements per screen: removed during the writing pass (fix #1).
3. Hero: one per screen (Today: workout card; Resting: countdown; Progress: 17,393 kg).
4. Accent count: ≤ 1 per screen.
5. Radii: pill + 20 (+ 28 on sheets); greys for text: 2; weights: 3.
6. Numbers agree across screens: yes (see above).
7. Generic copy: none found after the writing pass.

## Colour update (2026-11-10)
The user asked for a more vivid colour instead of the all-black UI. Cyan #22D3EE replaced near-black as the action colour and green as the data colour. Checked again after the change: white text on cyan fails (1.81:1), so on-action is near-black #0B1418 (10.31:1); the tab bar got its own `nav` colour so it does not turn cyan; Sign in with Apple was rebound to black / white; past weeks in the progress chart are near-black so this week's cyan bar stands out. Dark mode re-checked on all 16 copies.
