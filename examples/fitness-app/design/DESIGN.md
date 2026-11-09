# Repwise design spec

**What this is:** the single design spec for Repwise, a strength-training log for gym-goers past their first month (see `00-brief.md`).
**Based on:** 3 Behance references (§1.2) + user choices (Part 2) + Apple HIG (checked 2026-11-09) + Nielsen's 10 heuristics.
**Version / date:** 1.0 · 2026-11-09 (Parts 1–3; rounds 2–3 decided by the AI on recommended options, see §16)

Source tags: [Spec] author's style guide · [Measured ≈] grid measurement · [Observed] pattern seen · [HIG] · [Nielsen] · [User choice] · [AI suggestion]

---

# Part 1: Reference research

## 1.1 How the works were picked
Search `fitness app` on Behance; top 15 of Most Appreciated (`sort=appreciations`), Most Viewed (`sort=views`) and Most Discussed (`sort=comments`); 32 candidates, 5 excluded by hard filters, 16 reviewed image by image; ranked with `rank_candidates.py` (popularity 40% + visual 60% + 0.05 for a style guide) with the rule that picks differ in at least 2 of 5 style tags. Details: `01-candidates.md`.

## 1.2 The three references

| | A · Femotion | B · LGrow | C · NutriPal |
|---|---|---|---|
| Work | [link](https://www.behance.net/gallery/243053067/Fitness-mobile-app-UXUI-design) | [link](https://www.behance.net/gallery/254678997/LGrow-Personal-Coaching-Fitness-App-UXUI) | [link](https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design) |
| Author | Oksana Bashkatova, with ШКОЛА ДИЗАЙНА | Tobi Bui & Design Team Ekotek | Sriraj Mohan |
| Data (2026-11-09) | 439 / 2,584 / 326 | 939 / 11,412 / 308 | 294 / 5,350 / 96 |
| Style | Light grey + white cards, lime + lavender, photos | Black, white buttons, blue glow, dot-matrix numbers | Off-white, monochrome, colour only in charts |
| Style guide | yes (grid, type, colour, components) | partial (typefaces, palette) | yes (grid, palette, type, icons) |
| Measuring accuracy | ±1 pt (1.22 px/pt) | ±1.2 pt (0.81 px/pt) | 1 cell (7.23 px/pt) |
| Extraction file | research/femotion.md | research/lgrow.md | research/nutripal.md |

## 1.3 UI comparison
⚠ = breaks HIG; not offered as an option.

| Dimension | A · Femotion | B · LGrow | C · NutriPal | HIG |
|---|---|---|---|---|
| Design width | 402 [Spec · img 12] | 393 [Measured ≈ · img 07] | 393 [Spec · img 14] | — |
| Grid | 4 pt; steps 4/8/12/16/20/24/36/48 [Spec · img 12] | not published | 5 pt [Spec · img 14] | — |
| Side margins | 16 [Spec]; 16.3–17.2 [Measured · 17.png] | 15–20 [Measured ≈ ±1.2 · 07.png] | 20 [Spec]; 16.3 [Measured · 04.png] | Keep content in the safe area [HIG · Layout] |
| Background layers | #F8F8F8 base + #FFFFFF cards [Measured] | #000000 base, #121212–#292929 surfaces [Spec · img 05] | #FAFAFA base + #FFFFFF cards, faint shadow [Measured] | — |
| Typeface | Onest [Spec · img 13] | Inter + Doto for numbers [Spec · img 04] | Lufga [Spec · img 16] | Few typefaces [HIG · Typography] |
| Weights | Regular, Medium, Semibold [Spec] | not published | ⚠ Light, Regular, Medium, Semibold [Spec] | No Light or thinner [HIG · Typography] |
| Large title | 34/41 Regular (Display 1) [Spec] | two-line Regular, about 28–32 [Observed · img 07] | two-line, about 24 Medium, black + grey [Measured · col 21–23] | Large Title 34/41 [HIG · Typography] |
| Body | 17/21 Regular [Spec] | not published | not published | Body 17/22 [HIG · Typography] |
| Smallest text | Caption 11/13 [Spec] | not published | not published | Minimum 11 pt [HIG · Accessibility] |
| Primary text | #0C0C0C on #F8F8F8: 18.4:1 | #FFFFFF on #000000: 21:1 | #121212 on #FAFAFA: 17.9:1 | ≥ 4.5:1 [HIG · Accessibility] |
| Secondary text | ⚠ #A5A5A4 on #F8F8F8: 2.32:1 | #78787B on #000000: 4.77:1 (only just) | ⚠ #9D9D9D on #FAFAFA: 2.60:1 | ≥ 4.5:1 small, ≥ 3:1 large [HIG · Accessibility] |
| Accent and its use | Lime #C5FF74 for primary buttons and highlights; lavender #E3D6FF for chips and story tiles [Spec + Observed] | Blue #4B45F4 for glows and data; white for primary buttons [Spec + Observed] | None in UI; green #24DA4D and red/orange only in charts [Spec + Observed] | One colour, one meaning; colour the primary action's background [HIG · Color] |
| Card radius | 12 [Spec + Measured] | larger than buttons, not measurable | about 20 [Measured ≈ ±2] | Concentric corners [HIG · Layout] |
| Cards | white on grey, no shadow | dark surfaces on black | white on off-white, faint shadow | — |
| Primary button | about 50 tall, lime fill, dark text, radius 12 [Spec + Measured] | about 50 tall, white fill, black text, radius about 6 [Measured ≈] | dark pill actions (no full-width button in measured screen) [Observed] | ≥ 44 pt; 1–2 prominent per screen [HIG · Buttons] |
| Secondary / destructive | white with 1 pt outline; ⚠ "Cancel training" uses it instead of a destructive style | — | — | Destructive style for destructive actions [HIG · Buttons] |
| Input | white, 1 pt border, focus and error states [Spec · img 14] | about 44 tall, #19191C fill, no border [Measured ≈] | — | — |
| Selected state | lavender fill (chips), white segment on grey track | — | white pill on dark (tab bar) | Never colour alone [HIG · Accessibility] |
| Tab Bar | docked, 5 tabs, icon + label | not clear in screens | floating dark pill, 58 tall; ⚠ unselected tabs icon-only; "+" as a separate circle | Labels on every tab; floats over content [HIG · Tab bars] |
| Top bar | none on Home; back + centred title on drill-downs | back circle + share circle | none; title on the left, circle button on the right | — |
| Big numbers | step count in a ring, Medium | Doto dot-matrix, white | Regular with all-caps grey label | — |
| Imagery | real photos of people in brand colours | dark gym photography | food cut-outs, 3D exercise figures | One image style per app [anti-ai-checklist §1] |
| Effects | none | blue glows (⚠ for the AI look, not HIG) | none | — |

## 1.4 UX comparison

| Dimension | A · Femotion | B · LGrow | C · NutriPal |
|---|---|---|---|
| Main flow | Schedule → class → Book → My bookings (Add to calendar / Cancel) | Sign in → details → device → daily metrics, workouts, coach chat | Snap meal → AI identifies → confirm; AI workout plans by muscle group |
| Navigation | 5 docked tabs with labels | not clear | 4 icons in a floating pill + "+" circle |
| Status feedback | Skeleton screens; waitlist notifications | "Connecting…" state; progress bars | Remaining calories always visible |
| Sign-in timing | not shown | ⚠ at launch, before any value | not shown |
| Shortcuts | QR entry in one tap from Home | no-password sign-in | photo logging |
| Research shown | competitors, 8 interviews, personas, user flow | — | pain points, user flow |

## 1.5 Check results

**Not adopted (break HIG or Nielsen):**
- Grey secondary text under 4.5:1 (A, C) [HIG · Accessibility]
- Light weight (C) [HIG · Typography]
- Icon-only tabs (C) [HIG · Tab bars]
- Sign-in at launch (B) [HIG · Managing accounts]
- Non-destructive style for "Cancel" (A) [HIG · Buttons]
- Decorative glows (B) [anti-ai-checklist §1]

**Worth learning:**
- Fill-only layering, one bright accent for the main action (A)
- Skeleton screens and one-tap shortcut on Home (A) [Nielsen #1, #7]
- A distinctive numeric face for metrics (B)
- Colour reserved for data, two-line title, "+" kept out of the tab bar (C) [HIG · Tab bars]
- "Remaining" always visible (C) [Nielsen #1]: for Repwise, sets left and rest time

---

# Part 2: User choices

| Round / Q | Question | Choice | Value | Source |
|---|---|---|---|---|
| 1 / Q1 | Overall style | C · NutriPal | Off-white base, monochrome UI, colour only for data | [User choice · 1/Q1] [Behance · NutriPal · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design · images 04, 15] |
| 1 / Q2 | Design size | A | 393 × 852 (iPhone 16). The answer mentioned both "16 Pro Max" and "16"; the last word, "16", was used | [User choice · 1/Q2, interpreted] [Spec · NutriPal img 14] [Measured · LGrow 07.png] |
| 1 / Q3 | Side margins | A | 16 pt | [User choice · 1/Q3] [Spec · Femotion img 12] [Measured · Femotion 17.png, NutriPal 04.png] |
| 1 / Q4 | Background layers | A | #F8F8F8 base + #FFFFFF cards, no shadow | [User choice · 1/Q4] [Measured · Femotion 17.png] |
| 1 / Q5 | Light / dark | A (recommended) | Light first; dark mode values defined, drawn at hi-fi | [User delegated: "just do a version"] [HIG · Color] |
| 2 / Q6 | Accent | C (recommended) | No UI accent; near-black #18181B for actions; colour only for data | [User delegated] [Spec · NutriPal img 15] |
| 2 / Q7 | Typeface | B (recommended) | Inter (Lufga is a paid "Premium Font") | [User delegated] [Spec · LGrow img 04] [Spec · NutriPal img 16] |
| 2 / Q8 | Type scale | C + B (recommended) | iOS default sizes; NutriPal two-line page title with a darker grey | [User delegated] [HIG · Typography] [Measured · NutriPal 04.png] |
| 2 / Q9 | Big numbers | B (recommended) | Regular numbers with a small all-caps label above | [User delegated] [Observed · NutriPal img 04] |
| 2 / Q10 | Card radius | B (recommended) | 20 | [User delegated] [Measured ≈ · NutriPal 04_zoom_card.png] |
| 2 / Q11 | Imagery | C (recommended) | Exercise cut-outs on light circles; grey placeholders in v1 | [User delegated] [Observed · NutriPal img 04, 24] |
| 3 / Q12–18 | Components | recommended | See Part 3 §6; round 3 was not asked | [User delegated] |

---

# Part 3: Final rules

> Rounds 2 and 3 were decided by the AI on the recommended options after the user said "just do a version, don't ask me". Every such rule is tagged [AI suggestion] or with the reference it came from, and listed in §16 so it can be revisited.

## 0. How to read
Priority when rules conflict: accessibility [HIG] > other [HIG] > user choices > reference works > AI suggestions.

## 1. Core principles
1. **Numbers are the hero.** Every screen has one large number or title; weights, reps and time are what people came for. [Observed · NutriPal img 04] [AI suggestion]
2. **Monochrome UI, colour only for data.** Actions are near-black; green appears only in charts and PR markers, always with a label. [User choice · 2/Q6] [HIG · Color]
3. **Layer by fill.** #F8F8F8 base, #FFFFFF cards, no shadows, no borders. [User choice · 1/Q4]
4. **One pill shape and one card radius (20).** [User choice · 2/Q10] [anti-ai-checklist §1]
5. **Selected = filled near-black; unselected = white, no outline.** [anti-ai-checklist §1]
6. **Two text colours only.** #18181B and #6B6B70. [anti-ai-checklist §1] [HIG · Accessibility]
7. **Real, consistent sample data.** Kilograms, realistic lifts, totals that add up. [anti-ai-checklist §4]

## 2. Layout and grid
| Rule | Value | Source |
|---|---|---|
| Design size | 393 × 852 (iPhone 16) | [User choice · 1/Q2] |
| Grid | 4 pt base; use 8 for most gaps | [Spec · Femotion img 12] |
| Side margins | 16 | [User choice · 1/Q3] |
| Inside a card | padding 16 | [AI suggestion] |
| Gap inside a group | 8–12 | [AI suggestion] |
| Gap between groups | 24–32 | [Spec · Femotion img 12 steps] [Measured · Femotion: 36 between groups] |
| Safe area | content below the status bar; last content clears the floating tab bar by 16 | [HIG · Layout] |

## 3. Typography (Inter)
Weights: Regular, Medium, Semibold only. [HIG · Typography]

| Role | Size / line height | Weight | Colour |
|---|---|---|---|
| Page title (two lines) | 28 / 34 | Semibold (line 1), Regular (line 2) | line 1 text/primary, line 2 text/secondary |
| Hero number | 48 / 52 | Regular | text/primary |
| Card number | 28 / 34 | Regular | text/primary |
| Section header | 20 / 25 | Semibold | text/primary |
| Card title | 17 / 22 | Semibold | text/primary |
| Body | 17 / 22 | Regular | text/primary |
| Callout / row value | 16 / 21 | Medium | text/primary |
| Subhead / row label | 15 / 20 | Regular | text/secondary |
| Label (all caps, +0.5 tracking) | 12 / 16 | Medium | text/secondary |
| Tab label | 11 / 13 | Medium | on tab bar |
Minimum 11 pt. [HIG · Accessibility] Sizes from the iOS default scale. [HIG · Typography]

## 4. Colour
| Token | Light | Dark | Use | Contrast |
|---|---|---|---|---|
| bg | #F8F8F8 | #000000 | page base | — |
| surface | #FFFFFF | #1C1C1E | cards, sheets | — |
| surface-muted | #EFEFF1 | #2C2C2E | segmented track, empty slots, image placeholders | — |
| text/primary | #18181B | #FFFFFF | titles, values, body | 16.7:1 on bg |
| text/secondary | #6B6B70 | #A1A1AA | labels, captions | 4.99:1 on bg, 5.30:1 on surface, 4.62:1 on surface-muted |
| action | #18181B | #FFFFFF | primary button, selected chip, tab bar | white on it 17.7:1 |
| on-action | #FFFFFF | #18181B | text on action | — |
| tab-unselected | #A1A1AA | #6B6B70 | unselected tab icon + label (the bar is action-coloured: dark in Light, white in Dark) | 6.91:1 on #18181B; 5.30:1 on #FFFFFF |
| data/positive | #24DA4D | #30D158 | chart fills, PR marker (never text) | graphics only |
| data/track | #E4E4E7 | #3A3A3C | chart remaining ticks | — |
| destructive | #D92D20 | #FF6B60 | delete, discard | 4.83:1 on surface |
Contrast computed with `scripts/contrast.py`. Dark values are [AI suggestion], drawn at hi-fi. [HIG · Color]

## 5. Shape
- Pill (radius = height / 2): buttons, chips, inputs, steppers, tab bar. [anti-ai-checklist §1]
- Card radius 20; sheet top radius 28; circles for icon buttons and exercise thumbnails. [User choice · 2/Q10] [Observed · NutriPal img 04]
- No shadows. [User choice · 1/Q4]

## 6. Components
| Component | Spec | Source |
|---|---|---|
| Primary button | 52 high, full width, pill, action fill, on-action text 17 Semibold; loading shows "Saving…" inside | [AI suggestion] [Measured · Femotion ~50, LGrow ~50] [HIG · Buttons] |
| Secondary button | 52 high, pill, surface-muted fill (surface on bg), text/primary | [AI suggestion] |
| Destructive button | secondary shape, destructive text; never the primary | [HIG · Buttons] |
| Icon button | 44 circle, surface fill, 24 icon, 1.5 stroke | [HIG · Accessibility] [Observed · NutriPal img 04] |
| Chip | 36 high pill; selected action fill + on-action text; unselected surface + text/primary | [AI suggestion] [anti-ai-checklist §1] |
| Segmented control | 40 high pill track surface-muted; selected segment surface | [Spec · Femotion img 14] |
| Set row | 64 high: first column = set number over previous (secondary); weight stepper (116 wide) · reps stepper (84 wide) · 44 done circle; done = action circle with check, current = 2 pt ring, pending = muted | [AI suggestion] (revised after drawing: five side-by-side columns did not fit 329 pt) |
| Stepper | value 20 Medium between two 36 circles (tap area 44) | [HIG · Accessibility] |
| List row | 64 high; 44 circle thumbnail; title 17 + subtitle 15 secondary; chevron | [AI suggestion] |
| Info row | label left (15 secondary) / value right (16 Medium) | [Observed · example-design-rules §6.4] |
| Card | surface, radius 20, padding 16 | [User choice] |
| Tab Bar | floating pill 64 high, 16 from the sides, action fill; 4 tabs with icon + label; selected tab = white pill with dark icon + label | [Observed · NutriPal img 04] [HIG · Tab bars] (labels on every tab) |
| Sheet | surface, top radius 28, grabber, Cancel / Done | [HIG · Sheets] |
| Live rest card | action fill card radius 20; "REST" label, 48 countdown, determinate bar; Skip / +30 s | [HIG · Live Activities] [HIG · Progress indicators] |
| Week strip | 7 days; trained = filled circle, planned = ring, today = label emphasised | [AI suggestion] [example-design-rules §6.8] |
| Volume ticks | vertical ticks 4 wide, 8 gap; done = action, remaining = data/track | [Observed · NutriPal img 04] |

## 7. Page patterns
```
Today
Status bar
"Today" / "Thu, Nov 12"                                   (calendar circle)
Week strip  M T W T F S S
Workout card: PUSH DAY A · 6 exercises · about 55 min
              exercise preview list (3)  [ Start Workout ]
This week card: VOLUME 12,450 kg · SESSIONS 2 of 3 · volume ticks
Latest PR row: Bench Press 82.5 kg × 5  (green marker + "PR" label)
Floating tab bar: Today · Library · Progress · Profile
```
Active Workout (modal, tab bar hidden): top bar Cancel · elapsed time · Finish; exercise title; set rows; rest card appears after a set is ticked.

## 8. System behaviour
- Onboarding: 2 questions (goal, experience), Skip on each; no sign-in, no permissions. [HIG · Onboarding]
- Sign-in: Sign in with Apple sheet when saving the first workout; Continue without account keeps data on device. [HIG · Managing accounts]
- Notifications: permission asked when the user turns on reminders in Settings, with a one-button "Continue" explainer. [HIG · Privacy]
- Rest timer: Live Activity on the Lock Screen and Dynamic Island while resting; no push for the same event. [HIG · Live Activities]
- Account deletion in Account, with a confirmation sheet stating what is deleted. [HIG · Managing accounts]

## 9. Accessibility
Tap targets ≥ 44; text ≥ 11; contrast per §4; PRs marked with label + icon, never colour alone; Reduce Motion replaces timer pulse with a fade. [HIG · Accessibility]

## 10. Nielsen's heuristics in Repwise
| Heuristic | What Repwise does |
|---|---|
| #1 Status | Rest countdown with a determinate bar; "Set 3 of 4" in the exercise header; elapsed time in the top bar |
| #2 Real world | Kilograms and reps, the words lifters use (set, rep, PR, volume) |
| #3 Control | Cancel in Active Workout asks "Discard workout?"; ticking a set can be undone by tapping again |
| #4 Consistency | One primary button style; same set row in Active Workout and Session Detail |
| #5 Prevention | Steppers instead of free typing; previous set shown as a hint; Finish shows a summary before saving |
| #6 Recognition | Last time's weight × reps in each set row ("Previous") |
| #7 Efficiency | Start Workout from Today in one tap; "Repeat last" on Session Detail |
| #8 Minimalism | One hero number per screen; no decorative images |
| #9 Errors | Save failure keeps the workout and offers Retry |
| #10 Help | Exercise Detail explains form in 3 steps |

## 11. Writing
**Fewest words that still make sense.** "Check each word to be sure it needs to be there. If you can use fewer words, do so." [HIG · Writing]
- A screen carries one idea; the most important words come first. [HIG · Writing]
- No caption that repeats what is already on screen (a label above a card that says the same as its title, a subtitle that restates the number). [HIG · Writing]
- No "we"; "your" only where it changes the meaning ("History", not "Your history"). [HIG · Writing]
- Sheet titles ≤ 2 lines; a body sentence only when the user needs it to decide (e.g. what Delete removes). [HIG · Alerts]
- Settings: plain labels; describe what happens when on, if needed. [HIG · Writing]
- Title-case buttons, verb first ("Start Workout", "Finish Workout"). [HIG · Buttons]
- Formats: `82.5 kg`, `5 reps`, `1:24` rest, `Fri, Nov 13`, `55 min`. One word per concept: workout (not session) in UI; set; rep; PR.

## 12. Not AI-looking
- No glows or gradients → flat fills only.
- No emoji icons → one line icon set, 1.5 stroke.
- No "Welcome back, Alex! 👋" → title is the day and date.
- No fake charts → volume ticks from the sample data, totals that add up.
- No cards in cards → set rows sit directly in the exercise card.
- Accent appears at most once per screen (green PR marker or chart).

## 13. Quick reference (Figma variables)
| Item | Value | Variable |
|---|---|---|
| Frame | 393 × 852 | — |
| Margin | 16 | space/page |
| Spacing | 4, 8, 12, 16, 24, 32 | space/1–6 |
| Radius | pill 999, card 20, sheet 28 | radius/pill, radius/card, radius/sheet |
| Sizes | tap 44, button 52, chip 36, row 64, tabbar 64 | size/* |
| Colours | §4 | color/* (Light, Dark modes) |
| Text styles | §3 | Title/Page, Number/Hero, Number/Card, Heading/Section, Heading/Card, Body, Callout, Subhead, Label, Tab |

## 14. Per-screen checklist
- [ ] One hero; one leading edge at 16
- [ ] Only Inter Regular / Medium / Semibold; nothing under 11 pt
- [ ] Text colours only text/primary and text/secondary
- [ ] Accent (green) at most once, always with a label
- [ ] All tap targets ≥ 44; ≤ 1 primary button
- [ ] Pill or radius 20 only; no shadow, no border
- [ ] Tab bar visible except in modal flows
- [ ] Sample data consistent with other screens
- [ ] Every word needed; no text repeats what is already visible; no "we" [HIG · Writing]

## 15. Borrowing record
| Screen | What was borrowed | Source |
|---|---|---|
| Today | Two-line title, circle action at right | [Behance · NutriPal · Sriraj Mohan · https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design · image 04] |
| This week card | Label-over-number pairs and segmented ticks | [same · image 04] |
| Tab bar | Floating dark pill, selected white pill (labels added) | [same · image 04] |
| Onboarding | Large-option selection list | [Behance · Home workout app for fitness · SK RADWOAN et al. · https://www.behance.net/gallery/251510807/Home-workout-app-for-fitness · images 04, 06] |

## 16. Decision record
| # | Decision | Reason | Source | Date |
|---|---|---|---|---|
| 1 | Rounds 2–3 decided by the AI on recommended options | User asked not to be asked and to "just do a version" | [User · chat] | 2026-11-09 |
| 2 | Design size 393 × 852 | Answer named both 16 Pro Max and 16; last word used | [User choice · 1/Q2] | 2026-11-09 |
| 3 | Custom floating dark tab bar instead of the system Liquid Glass bar | Matches the chosen reference; keeps labels on every tab to stay within HIG | [HIG · Tab bars] [Observed · NutriPal] | 2026-11-09 |
| 4 | Inter instead of Lufga | Lufga is a paid font | [Spec · NutriPal img 16] | 2026-11-09 |
| 5 | Designed directly in high fidelity: Light pages per flow + a Dark copy of every screen; exercise images are named placeholders | The skill delivers hi-fi only; no licensed exercise images exist yet | [User · chat: "just do hi-fi"] [HIG · Color] | 2026-11-09 |

---

## Limitations, references and disclaimer
- Measurements come from presentation images, not source files. Accuracy per work is listed in §1.2; LGrow values are bands (±1.2 pt).
- Three references are a small sample; they show patterns, not statistics.
- HIG summary checked on 2026-11-09.
- References: see §1.2.

> **Disclaimer.** This spec is an independent summary written for this project. It is not affiliated with or endorsed by Apple, Adobe Behance, Figma or Nielsen Norman Group. The reference works belong to their authors and are cited only for the patterns observed; their branding, images and copy are not used. Measured values are approximate. Check the official HIG before relying on a number.
