# Repwise design spec

**What this is:** the single design spec for Repwise, a strength-training log for gym-goers past their first month (see `00-brief.md`).
**Based on:** 3 Behance references (§1.2) + user choices (Part 2) + Apple HIG (checked 2026-11-09) + Nielsen's 10 heuristics.
**Version / date:** 0.1 (Part 1 only) · 2026-11-09

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
| 1 / Q2 | Design size | *pending confirmation* | 440 × 956 (16 Pro Max) or 393 × 852 (16) | [User choice · 1/Q2] |
| 1 / Q3 | Side margins | A | 16 pt | [User choice · 1/Q3] [Spec · Femotion img 12] [Measured · Femotion 17.png, NutriPal 04.png] |
| 1 / Q4 | Background layers | A | #F8F8F8 base + #FFFFFF cards, no shadow | [User choice · 1/Q4] [Measured · Femotion 17.png] |
| 1 / Q5 | Light / dark | *not answered yet* | — | — |

---

# Part 3: Final rules

*Written after all choice rounds (Step 4).*

---

## Limitations, references and disclaimer
- Measurements come from presentation images, not source files. Accuracy per work is listed in §1.2; LGrow values are bands (±1.2 pt).
- Three references are a small sample; they show patterns, not statistics.
- HIG summary checked on 2026-11-09.
- References: see §1.2.

> **Disclaimer.** This spec is an independent summary written for this project. It is not affiliated with or endorsed by Apple, Adobe Behance, Figma or Nielsen Norman Group. The reference works belong to their authors and are cited only for the patterns observed; their branding, images and copy are not used. Measured values are approximate. Check the official HIG before relying on a number.
