# B · LGrow

**Source:** [Behance · LGrow - Personal Coaching Fitness App | UX/UI · Tobi Bui & Design Team Ekotek · https://www.behance.net/gallery/254678997/LGrow-Personal-Coaching-Fitness-App-UXUI] read on 2026-11-09
**Data:** 939 appreciations · 11,412 views · 308 comments [Behance data · project page]
**Why picked:** total 0.77, style `dark;fill;neutral;large;photo`; the most popular work in the pool and on all three lists
**Style guide:** partial: image 04 (typefaces), image 05 (palette). No sizes or spacing.
**Screens measured:** image 07, Welcome screen (crop 560,161,879,852), design width 393.
**Accuracy warning:** 1 pt = 0.81 image px. `grid_extract.py info` warns that 1-cell accuracy is not possible; error about ±1.2 pt. Values below are bands, not exact.
**Context:** personal fitness goals plus a connection to a human coach: workouts, running routes, nutrition scan, sleep, chat with the coach, smartwatch and ring sync.
**Style in one line:** pure black with white primary buttons, a blue glow behind key moments, dot-matrix numbers for metrics.

## UI

| Item | Value | Tag | Source |
|---|---|---|---|
| Design width | 393 | [Measured ≈] | 07.png: screen 319 × 691 px, ratio matches 393 × 852 |
| Typefaces | Inter (UI) + Doto (decorative dot-matrix, for big numbers) | [Spec] | image 04 |
| Palette | Blue Glow #4B45F4 · African Turquoise #000000 · Solid Black #0C0C0C · Refresh Black #121212 · Electric Black #292929 · Boulder #78787B · Chinese Silver #C2C2C2 · Full White #FFFFFF | [Spec] | image 05 |
| Background | #000000 (with blue glows) | [Measured ≈] | 07.png · `sample` (30,300) = #000003 |
| Side margins | about 15–20 | [Measured ≈ ±1.2] | 07.png · `edges --row 470` (left 14.8, right 19.7) |
| Input | about 44 tall, fill #19191C, no border; country code field 72 wide, 8 gap | [Measured ≈ ±1.2] | 07.png · `edges --row 405`, `--col 260` |
| Primary button | about 50 tall, full width, white fill, black text, radius about 6 | [Measured ≈ ±1.2] | 07.png · `edges --col 260`: 448.4 → 498.9; 07_zoom_button.png |
| Gap input → button | about 20 | [Measured ≈ ±1.2] | 07.png · `edges --col 260` |
| Cards | dark surfaces (#121212–#292929), larger radius than buttons (not measured: image too small) | [Observed] | images 10, 14 |
| Big numbers | Doto dot-matrix, white, e.g. "93.2", with a small unit | [Observed] | images 01, 06 |
| Data colour | multi-colour bars (purple, orange, pink) on dark | [Observed] | image 01 |
| Imagery | dramatic gym photography, dark | [Observed] | images 06, 07, 10 |
| Effects | blue radial glow behind headers and key screens | [Observed] | images 01, 07, 09, 11 |

## Screen structure (Welcome, image 07 centre)

```
Status bar
Blue glow (top)
"Join with us" chip
"Welcome to Our Zone" (two-line large title, Regular)
Subtitle
[+32 ▾] [Enter your phone number]
[ Login Now ]  (white)
—— Or With ——
Google · Facebook · Apple (circle buttons)
Blue glow (bottom)
```

## UX

| Item | Practice | Source |
|---|---|---|
| Sign-in | Phone number + one-time code, or Google / Facebook / Apple; no password | image 07 |
| Sign-in timing | At the start, before using the app | image 07 |
| Onboarding | "A few details": name, email, birth date, height, weight | image 08 |
| Device setup | Connect watch or ring, with "Connecting…" state | image 08 |
| Main areas | Daily process (metrics), workouts, running route, nutrition scan, sleep, chat with coach, achievements | images 01, 10–14 |
| Status feedback | Connecting state; progress bars | image 08 |

## HIG / Nielsen check

| Finding | Basis | Verdict |
|---|---|---|
| Sign-in required at the start | [HIG · Managing accounts] as late as possible | Do not adopt; sign in at first save |
| Apple shown as one of three equal circle icons | [HIG · Managing accounts] prefer Sign in with Apple; use the official button | Do not adopt the icon-only version |
| No password, one-time code | [Nielsen #7] [HIG · Managing accounts] passkeys preferred | Pattern can be adopted |
| White button on black: 21:1 | [HIG · Accessibility] | Can adopt |
| Boulder #78787B on black: 4.77:1 | [HIG · Accessibility] passes 4.5:1, only just | Use only ≥ 15 pt |
| Blue glow behind content | [anti-ai-checklist §1] glows read as AI-generated | Do not adopt as decoration |
| Dot-matrix numbers for metrics | — | Distinctive; option in the choice questions |
| Personal data asked before any value (height, weight…) | [Nielsen #8] [HIG · Onboarding] | Ask later, in context |

## 3 things worth learning / 3 things not to copy
- Learn: strong single-colour primary button; one distinctive numeric face for metrics; no-password sign-in.
- Do not copy: sign-in wall at launch; decorative glows; social sign-in as tiny icons.
