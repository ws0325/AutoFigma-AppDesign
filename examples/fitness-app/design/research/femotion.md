# A · Femotion

**Source:** [Behance · Fitness mobile app | UX/UI design · Oksana Bashkatova (Оксана Башкатова) with ШКОЛА ДИЗАЙНА · https://www.behance.net/gallery/243053067/Fitness-mobile-app-UXUI-design] read on 2026-11-09
**Data:** 439 appreciations · 2,584 views · 326 comments [Behance data · project page]
**Why picked:** total 0.81, style `light;fill;brand;large;photo` (see 01-candidates.md)
**Style guide:** yes, images 12 (grid), 13 (typography + colour), 14 (components)
**Screens measured:** image 17, Home (crop 1154,874,1646,2342) and My bookings (crop 1154,2502,1646,3570); design width 402 from the style guide. 1 pt = 1.22 image px (edges may be off by 1 cell).
**Context:** an app for a chain of yoga and fitness studios in Russia: class schedule, booking, memberships, QR entry, step tracker, trainer profiles. Screens are in Russian.
**Style in one line:** light grey base with white cards, lime primary buttons and lavender highlights, real photos of people in brand colours.

## UI

| Item | Value | Tag | Source |
|---|---|---|---|
| Design size | 402 × 874 (iPhone 16 Pro) | [Spec] | image 12, Grid system |
| Grid | 4 pt modular grid; spacing steps 4 / 8 / 12 / 16 / 20 / 24 / 36 / 48 | [Spec] | image 12 |
| Side margins | 16 | [Spec] | image 12 |
| Side margins (screens) | 16.3–17.2 | [Measured ≈] | 17.png Home · `edges --row 345`, `--row 480` |
| Column gutter | 12 | [Spec] | image 12 |
| Typeface | Onest | [Spec] | image 13 |
| Type scale (size / line height / weight) | Display 1 34/41 Regular · Display 2 28/35 Medium · Display 3 25/22 Medium (line height smaller than size, likely a typo) · Display 4 17/20 Medium · Body 17/21 Regular · CTA medium 15/20 Regular · Label semibold 14/18 · Label medium 14/18 · CTA small 13/18 Regular or Medium · Caption 11/13 Regular | [Spec] | image 13 |
| Neutrals | 100 #0C0C0C · 75 #A5A5A4 · 60 #E0E0E0 · 50 #DADADA · 30 #E8E8E8 · 15 #F4F4F4 · 5 #F8F8F8 · 0 #FFFFFF | [Spec] | image 13 |
| Accents | Brand 1 #C5FF74 (lime) · Brand 2 #E3D6FF (lavender) · Brand 3 #2C2D35 (near-black) | [Spec] | image 13 |
| Error | #FF383C | [Spec] | image 13 |
| Background layers | #F8F8F8 base + #FFFFFF cards | [Measured ≈] | 17.png · `sample` (6,100) and (200,330) |
| Card radius | 12 | [Spec] + [Measured ≈] | image 12 card sample; 17_zoom_photo_corner.png |
| Story cards | about 105 × 108, 12 apart, horizontal carousel | [Measured ≈] | 17.png · `edges --row 200`, `--col 30` |
| Gap story row → club card | 36 (a spacing step) | [Measured ≈] | 17.png · `edges --col 30`: 250 → 286 |
| Photo cards | full width (16 margins), about 186 tall, caption below | [Measured ≈] | 17.png · `edges --col 30`: 423 → 609 |
| Primary button | about 50 tall, lime #C5FF74 fill, dark text, radius about 12 | [Spec] + [Measured ≈] | image 14; 17.png bookings · `edges --col 60`: 376.7 → 427.3 |
| Secondary button | white with 1 pt dark outline, same size, 12 below the primary | [Spec] + [Measured ≈] | image 14; 17.png bookings: 440.4 → 491.9 |
| Disabled button | grey fill, grey text | [Spec] | image 14 |
| Segmented control | grey track, white selected segment | [Spec] | image 14 |
| Inputs | white, 1 pt border; dark border when focused, red when invalid, clear button | [Spec] | image 14 |
| Chips | selected = lavender fill | [Observed] | 17.png bookings ("Тренировки") |
| Tab Bar | docked, 5 tabs, icon + label; selected = dark, others grey | [Spec] + [Observed] | image 14; 17.png |
| Top bar | none on Home (avatar + greeting + 2 circle buttons); back + centred title on drill-downs | [Observed] | 17.png |
| Imagery | real photos, people wearing lime / lavender | [Observed] | 17, 19 |
| Shadows | none; layers by fill | [Observed] | 17.png |

## Screen structure (Home, image 17)

```
Status bar
Avatar · "Привет, Оксана" (large greeting)          bell · heart (circles)
Story carousel: 3 tiles 105×108, lavender / lime fills, photo + text
Club card (white): "Мой клуб" chip · club name · load indicator · QR button
Photo card "Мои записи" (my bookings)
Photo card "Мои абонементы" (my memberships)
Photo card "Фитнес трекер"
Docked Tab Bar (5)
```
Hero: the greeting and the story carousel share the top; the club card is the only interactive status element.

## UX

| Item | Practice | Source |
|---|---|---|
| Research | Competitor analysis of 5 apps, 8 interviews, personas, conclusions | images 05, 07 |
| Main task flow | Home → Schedule → class → Book → booking appears in My bookings; Add to calendar / Cancel | images 17–19 |
| Navigation | 5 tabs: Главная (Home), Каталог (Catalog), Расписание (Schedule), Тренеры (Trainers), Профиль (Profile) | image 14 |
| Status feedback | Skeleton screens while loading; notifications for waitlist spots | images 16, 17 |
| Speed | QR entry reachable from Home in one tap (sheet) | image 17 |
| Empty states / errors | Input error state only | image 14 |
| Sign-in timing | Not shown | — |

## HIG / Nielsen check

| Finding | Basis | Verdict |
|---|---|---|
| Neutral 75 #A5A5A4 used for secondary text on #F8F8F8: 2.32:1 | [HIG · Accessibility] text ≤17 pt needs 4.5:1 (`contrast.py`) | Do not adopt for text |
| Lime button with dark text #2C2D35: 11.69:1 | [HIG · Accessibility] | Can adopt |
| Tab labels are small and grey | [HIG · Tab bars] labels required; contrast to be checked | Keep labels, darken unselected |
| "Cancel training" is an outline button, not red | [HIG · Buttons] destructive actions use the destructive style | Adopt the layout, use destructive style |
| Skeleton screens while loading | [Nielsen #1] | Can adopt |
| QR in one tap from Home | [Nielsen #7] | Can adopt (pattern) |
| Waitlist notification when a spot frees | [Nielsen #1] | Can adopt |
| Design size 402 (Pro) | — | Option in the choice questions |

## Differences between the style guide and the screens
- Side margins: guide 16, screens 16.3–17.2: within measuring error.
- Display 3 line height 22 is smaller than its size 25; probably a typo in the guide.

## 3 things worth learning / 3 things not to copy
- Learn: a complete published style guide; fill-only layering with no shadows; one bright accent for the main action.
- Do not copy: grey #A5A5A4 for text; photo-card-only home with little information; non-destructive styling for cancel.
