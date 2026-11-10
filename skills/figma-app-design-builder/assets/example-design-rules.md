# Mobile App UI Design Guidelines

**What this is:** A set of rules for designing iOS-style mobile app screens. It combines two kinds of research:

1. **Apple Human Interface Guidelines (HIG):** 14 topics, summarised as rules with numbers.
2. **A study of 9 well-known app design case studies on Behance:** layouts measured on an 8 pt grid and turned into common patterns.

**Who it is for:** Designers, and AI agents that generate or review mobile UI. Each rule is written so it can be checked against a screen.

**Version:** 1.0 · November 2026

> **Disclaimer.** This document is an independent summary written in our own words. It is not affiliated with or endorsed by Apple. The HIG changes over time; check the official site before relying on a number: https://developer.apple.com/design/human-interface-guidelines/. The case studies belong to their authors and are listed in §15 for reference only. Do not copy their branding.

---

## 0. How to read this document

Every rule carries a tag that says where it comes from and how much to trust it.

| Tag | Meaning | Trust |
|---|---|---|
| **[HIG]** | From Apple's Human Interface Guidelines | High. Platform rule |
| **[Spec]** | A value published on a case study's own style-guide page | High. Given by the author |
| **[Measured ≈]** | Measured on case-study screenshots with an 8 pt grid | Medium. About ±2 pt |
| **[Observed]** | A pattern seen across case studies, not a number | Medium |
| **[Recommended]** | A default we suggest, based on the above | A starting point. Change it if the product needs to |

**How measurements were taken:** Case studies show presentation images, not source files. Screen width was taken as 375 pt (older iPhones) or 393 pt (iPhone 14/15/16) and an 8 pt grid was laid over it. Font sizes were estimated from cap height (about 0.7 × font size). Treat measured values as "which band it falls in", not exact values.

**Priority when rules conflict:**

1. Accessibility rules [HIG]
2. Other platform rules [HIG]
3. Patterns [Spec] / [Measured ≈] / [Observed]
4. Defaults [Recommended]

---

## 1. Core principles

1. **One hero per screen.** Each screen has one thing that is clearly the largest: a title, a number or an image. [Observed]
2. **Most important first.** Put the most important content at the top and on the leading side. Things that are aligned are read as related. [HIG]
3. **Group with space, not lines.** Space inside a group is about half the space between groups. Use dividers only between list rows. [Observed] [HIG]
4. **Neutral greys plus one accent.** Use colour only for state and the main action. [HIG] [Observed]
5. **Everything tappable is a pill or a circle, at least 44 pt.** [HIG] [Observed]
6. **Selected = filled. Unselected = nothing.** Do not outline every option. [Observed]
7. **Cut words.** Every word must earn its place. If it does not fit, remove words; do not shrink the text. [HIG]
8. **Never rely on colour alone.** Pair colour with a shape, icon or text. [HIG]
9. **Every visual element must do a job.** No decorative blocks, fake data or icons that carry no information. [Recommended]
10. **Show only data the user actually has.** If there is no booking, hide the booking card. Do not show an empty card for it. [Recommended]

---

## 2. Layout and grid

### 2.1 Grid and margins

| Rule | Value | Source |
|---|---|---|
| Base grid | 8 pt. Use 4 pt only for very small gaps | [Measured ≈] |
| Side margins | 16–24 pt. Use 24 for most screens and 16 for card-heavy screens | [Measured ≈] |
| Forms and screens with little content | Wider margins are fine (about 48 pt in one case) | [Observed] |
| Edge-to-edge content | 0 pt margin only works on a pure-black background, where the device frame acts as the margin | [Spec] |
| Bento (tile) home screens | Tile gaps and side margins as small as 8 pt. This only works with large corner radii | [Measured ≈] |

### 2.2 Alignment

- **One leading edge per screen.** Titles, search fields, cards and section headers share the same left line. Trailing items such as "See all" and icon buttons share one right line. No element is indented on its own. [Observed]
- **Safe area.** Keep content clear of the status bar, Dynamic Island and Home indicator. [HIG]
- **Background reaches the edges.** Let background content run under floating tab bars and toolbars. Do not put a solid strip behind the controls. [HIG]

### 2.3 Progressive disclosure

- Show less at first and reveal more on demand, for example with drill-down, expandable rows or sheets. [HIG]

### 2.4 Dynamic Type

- Support larger text sizes. When text grows, side-by-side items stack vertically and line heights grow. Text must never be clipped. [HIG]

---

## 3. Typography

### 3.1 Rules

1. **One typeface per app.** Every case study used a single family. [Spec]
2. **2–3 weights.** Build hierarchy with size and colour, not by piling on weights. [Spec]
3. **Allowed weights.** Use Regular, Medium, Semibold and Bold. Avoid Ultralight, Thin and Light. [HIG]
4. **Two text colours.** Use near-black for primary text and one mid-grey for secondary text. Do not use three or four greys for text. [Observed]
5. **Big numbers, light weight.** Show key numbers at 32–56 pt in Regular or Medium, with a small grey unit next to them (for example `816` + `kWh`). The size contrast does the work that bold would do. [Measured ≈]
6. **Tight titles, loose body.** Large titles use a line height of about 1.05–1.1 × size. Body text uses about 1.5 × size. [Measured ≈]
7. **Two-line titles.** Large page titles are often split across two lines on purpose. [Observed]
8. **Minimum size.** 11 pt is the minimum. 17 pt is the default body size. [HIG]

### 3.2 iOS default type styles [HIG]

| Style | Size / line height (pt) |
|---|---|
| Large Title | 34 / 41 |
| Title 1 | 28 / 34 |
| Title 2 | 22 / 28 |
| Title 3 | 20 / 25 |
| Headline | 17 / 22, Semibold |
| Body | 17 / 22 |
| Callout | 16 / 21 |
| Subheadline | 15 / 20 |
| Footnote | 13 / 18 |
| Caption 1 | 12 / 16 |
| Caption 2 | 11 / 13 |

### 3.3 Sizes by role, seen in the case studies [Spec] [Measured ≈]

| Role | Size | Weight / note |
|---|---|---|
| Page title | 28–36 | Medium to Semibold, often two lines |
| Key number or marketing figure | 30–56 | Regular / Medium in newer apps, bold in older ones |
| Navigation-bar title (screens with a back button) | 16–20 | Centred |
| Section header | 18–20 | Semibold |
| Card title | 16–18 | Semibold |
| Body / value | 14–16 | Regular |
| Caption / label / unit | 11–13 | Regular, grey |

Typical published scales have 5–6 steps, with the largest about 2–3 × the smallest. Examples: `36 / 28 / 20 / 16 / 12` and `24 / 20 / 18 / 16 / 14 / 12`. Marketing banners sometimes use one size above the scale. [Spec]

---

## 4. Colour

1. **Neutrals plus one accent.** 7 of 9 case studies had a single main accent colour. [Spec]
2. **Use the accent sparingly.** Use it for the main button, the selected state, key numbers, the current tab and a few icons. Because it covers little area, it stands out. [Observed]
3. **Near-black can be the accent.** Newer apps often make the main button, selected chip and current tab near-black, and keep the brand colour for one or two key points such as price, play or add-to-cart. [Observed]
4. **Two background layers.** Put white cards on a light-grey background, or light-grey cards on white. Separate layers by fill, not by outline. [Spec] [Observed]
5. **"Black" is rarely pure black.** Near-blacks such as #010101, #282828 and #333333 are common. Pure #000000 was used only for a deliberate edge-to-edge look. [Spec]
6. **One colour, one meaning.** Do not reuse the accent for unrelated things. [HIG]
7. **Fill the background of a primary action.** Colour the button's background, not only its text or icon. Do not fill the backgrounds of several controls at once. [HIG]
8. **Plan three variants.** Every colour needs a light, a dark and a high-contrast version. [HIG]
9. **Contrast.** Text ≤ 17 pt needs at least 4.5:1. Text ≥ 18 pt, or bold text, needs at least 3:1. Mid-grey #808080 on white is only about 3.9:1, so do not use it for small text. [HIG]
10. **Wireframes stay greyscale.** Add the accent only at high fidelity. [Observed]

---

## 5. Shape and corner radius

1. **Three shape types:**
   - **Pill**, where the radius is half the height: buttons, inputs, chips, tab bars and segmented controls.
   - **Card radius.**
   - **Circle:** icon buttons and avatars.

   [Measured ≈]
2. **One radius set per app.** A pill plus one card radius covers almost everything. Do not mix 3, 5, 10 and 16. [Observed]
3. **Radii have grown over time.** Card radii were about 8–16 pt in 2018–2020 designs and about 20–32 pt in 2024–2026 designs. [Measured ≈]
4. **Images match their container.** A photo inside a card uses the card's radius. [Observed]
5. **Concentric corners.** An inner shape's radius = outer radius − padding. Do not pick inner radii at random. [HIG]
6. **Sheets** have a large top radius, about 24–32 pt. [Measured ≈]

---

## 6. Components

### 6.1 Size reference [Measured ≈ unless marked]

| Component | Size | Notes |
|---|---|---|
| Tap target | ≥ 44 × 44 pt, absolute minimum 28 × 28 [HIG] | Every tappable circle in the case studies was ≥ 40, most were 44 |
| Primary button | Height 48–60, full width, pill | Newer designs use 52–60 |
| Input / search field | Height 44–48, pill or underline-only | A circular action button often sits at the trailing end |
| Circular icon button (back, bell, avatar) | 40–48, most often 44; up to 52–56 in some newer apps | |
| Segmented control | About 40 high, pill | |
| Chip / filter | 32–40 high (older) or 44–56 (newer), pill | |
| Icon | 24 pt frame with a 16 pt live area and about 1.5 pt round-cap stroke [Spec] | |
| Horizontal carousel card | About 70% of screen width, with the next card peeking in | |
| Card | Radius 20–24, padding 16–20 | |

### 6.2 Buttons

- **Prominent buttons:** 1–2 per screen at most. To mark the recommended option, give it a stronger style; do not make it bigger. [HIG]
- **Labels:** start with a verb. HIG uses title case ("Add to Cart"). If you choose sentence case, use it everywhere. [HIG]
- **Destructive actions** (delete, remove, cancel booking, log out) are never the primary button. Use the destructive (red) style at high fidelity, or a secondary style in wireframes. [HIG]
- **Waiting:** show progress inside the button ("Checkout" → "Checking out…"). [HIG]
- **Position:** primary buttons sit at the bottom, full width, on forms, payment and onboarding screens. [Observed]
- **Arrow button:** a common modern variant is a pill with a circular arrow button inset at its trailing end. [Observed]
- **One kind of content:** icon buttons hold only an icon, and text buttons hold only text. [Observed]

### 6.3 Selection (chips, time slots, dates, tabs)

| State | Treatment |
|---|---|
| Selected | Filled: a grey, accent or near-black pill with contrasting text |
| Unselected | Text only, or a faint fill. **No outline** |

Because only the selected item is filled, the choice is obvious and the row stays calm. This is the biggest difference between older designs, which used outlined options, and newer ones. [Observed]

### 6.4 Information rows

- **Label/value rows:** grey Regular label on the left, black Semibold value on the right. Rows are about 44–48 pt high, with no dividers. Use them for receipts, totals and booking details. [Measured ≈]
- **List rows:**
  - Leading: a 40–56 pt icon tile or circle.
  - Middle: two lines (title 14–16 + grey caption 11–13).
  - Trailing: a chevron or a status pill.

  Separate rows either by an 8 pt gap with each row as its own card, or by whitespace only. [Observed]
- **Inline detail:** put secondary detail after the value in a lighter grey on the same line, for example `10:00–10:45 (45 min)`. [Observed]
- **Status** goes in a small pill on the trailing side (for example "Confirmed"). [Observed]

### 6.5 Navigation bar (top)

- **Leading:** avatar, brand name or a back button.
- **Trailing:** 1–2 circular buttons.
- **Screens with a title:** the title is centred, with a circular button on each side.
- **No bar:** no full-width bar background and no bottom divider.

[Observed]

### 6.6 Tab bar

- **Contents:** as few tabs as possible. Each tab has a one-word label. [HIG]
- **Placement:**
  - Floats above the content. [HIG]
  - Newer designs use a floating pill, sometimes icon-only, with the current item in a small filled circle or pill. [Observed]
  - A "+" action, if any, is a separate circle next to the bar, not a tab. [Observed]
- **Visibility:** stays visible when moving between sections. Only full-screen modal flows (booking, payment, password reset) may cover it. [HIG]
- **Tabs are destinations, not actions.** Never hide or disable an empty tab; explain why it is empty. [HIG]
- **Badges:** only for important information. [HIG]

### 6.7 Sheets (bottom sheets)

- **Use:** for short, simple tasks. Use a full screen for long or complex flows. [HIG]
- **Sizes:** medium (about half height) and large. A resizable sheet shows a grabber. [HIG]
- **Closing:** swipe down to dismiss. If there are unsaved changes, confirm first. [HIG]
- **Header buttons:** Cancel at top-left and Done at top-right. In multi-step sheets, Back replaces Cancel. [HIG]
- **One at a time:** never stack sheets. [HIG]
- **Typical layout:**
  - Behind: the page is dimmed.
  - Sheet: white with a large top radius.
  - First row: title on the left, close on the right.
  - Body: options as separate cards 16–24 pt apart.
  - Bottom: a summary row, then the full-width primary button.

  [Observed]

### 6.8 Progress

- If progress can be measured, use a determinate bar. Use a spinner only when it cannot. [HIG]
- Never let a bar stall, and keep its pace steady. [HIG]
- Add a label only if it helps. "Loading…" alone does not. [HIG]
- Offer Cancel when cancelling is safe. [HIG]
- **Step progress** (for example 3 steps): use dots on a line, with filled = done, ringed = pending, and the label of the current step emphasised. [Recommended]

### 6.9 Cards and images

- **At most two layers:** background plus card. No card inside a card. [Observed]
- **Shadows:** very soft, or none. Separate layers by fill. [Observed]
- **One image style per app:** illustration, photography or poster tiles. Do not mix them. [Observed]
- **Cut-out subjects:** in newer apps, products and people are cut out and placed on a light rounded tile instead of full-bleed photos. Full-bleed photos are kept for onboarding, banners and hero cards. [Observed]
- **Missing image:** use a light-grey block with a small centred icon. [Observed]

---

## 7. Page patterns [Observed]

### 7.1 Home screen, top to bottom

```
Status bar
Top bar: leading = avatar / brand / back · trailing = 1–2 circular buttons
Greeting (small, grey)
Large title (two lines, heavy)
Search / input field (full width, pill, optional trailing circle button)
Section header ……………………… "See all" (same baseline)
Horizontal cards (next card peeking in)
Section header ……………………… "See all"
Vertical list or grid
Floating pill tab bar (+ optional separate "+" circle)
```

### 7.2 Other patterns

| Pattern | Structure |
|---|---|
| **Map screen** | The map fills the screen. Information sits on floating white cards above it, for example a from/to card with a hairline between the two rows |
| **Detail screen** | A large photo or portrait on top, with a white panel with a large top radius sliding over it |
| **Booking flow** | 1. Panel title with "‹ Month ›" on the trailing side. 2. A horizontal strip of days (selected = filled tile). 3. A row of times (selected = filled pill, others text only). 4. A full-width near-black primary button |
| **Success screen** | Round check → large title ("You're booked in") → grey subtitle → white panel sliding up, holding a summary row, a status pill and 3 label/value rows |
| **Schedule cards** | One card per day (radius about 20, 12–16 pt apart). Left column: weekday plus a very large date number. Right column: time, an event pill and location. A circular arrow button at top-right |
| **Bento home** | White tiles of different sizes on a light-grey background, with 8 pt gaps. Works because the radii are large |
| **Onboarding** | A large centred title, one illustration, and a single "Next" or "Continue" at the bottom. Short and skippable (§8.1) |

### 7.3 Live status card (in-app Live Activity pattern) [Recommended]

Use this for anything with a clear start and end that changes while the user watches: an upcoming booking, an ongoing session, a delivery or a payment being processed. It is the in-app version of iOS Live Activities.

```
┌───────────────────────────────────────────────┐
│ (●)  Title (Medium, white)           12  min  │  ← big number + small unit
│      Subtitle (grey)                          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  ← progress, or ●──●──○ steps
│ [ Action ]                [ Action ]          │  ← optional, max two pills
└───────────────────────────────────────────────┘
```

- **Shape:**
  - Opaque near-black background, radius about 30, padding about 16–20.
  - A 44 pt icon circle on the leading side.
- **Text:**
  - Medium weight or heavier. Avoid small text.
  - The key number is large, with a small unit beside it.
- **Progress:**
  - A 6 pt determinate bar (dark track, white fill).
  - Or a dotted 3-step line: done = filled, pending = ring, current label emphasised.
- **One per screen:** it is the only black hero on the screen.
- **Lifetime:** only while the event is live, ideally no longer than about 8 hours.
- **No duplicate alerts:** while the card shows an event, do not also send a push notification about the same event (§8.5).

---

## 8. System behaviour

### 8.1 Onboarding [HIG]

- **Teach through use.** If onboarding is needed, keep it fast, enjoyable and skippable.
- **Help in place:** prefer a short tip where it is needed over an up-front tour.
- **Skipped tutorials:**
  - Never force them again.
  - Keep them reachable from Help or Settings.
- **Not in onboarding:**
  - No terms and conditions.
  - No requests for ratings or payment until the person has used the app.

### 8.2 Permissions [HIG]

- **When to ask:** at the moment the feature needs it. Ask at launch only if the app cannot work without the permission.
- **Pre-permission screen** (optional):
  - Exactly **one** button, labelled "Continue" or "Next" and never "Allow".
  - No Cancel or Close.
  - It must not imitate the system alert or point at its "Allow" button.
- **No bargaining:** never offer a reward for granting a permission, and never lock unrelated features when it is denied. Offer a manual alternative, for example "Choose an area" instead of location.
- **Purpose string:** a complete, active sentence that says what the data is used for. Example: "The app uses your location to show rooms near you."

### 8.3 Accounts [HIG]

- **When to require sign-in:** only when a core feature needs an account, and as late as possible. Let people browse first; a shopping app asks at checkout.
- **Sign-in methods:**
  - Prefer Sign in with Apple, then passkeys.
  - If passwords are used, add two-factor authentication.
  - Name the method on the button ("Sign In with Face ID").
- **Account deletion:**
  - If people can create an account, they must be able to delete it (not just deactivate it).
  - Make the option easy to find.
  - Say when deletion will finish, and confirm when it has.

### 8.4 Payments (Apple Pay) [HIG]

- **Order:** when the device supports Apple Pay, it is the first payment option, no smaller than the others and visible without scrolling.
- **No extra step:** do not put Apple Pay behind its own step.
- **Payment sheet:** show only what is needed. The total line reads "Pay [Merchant]".
- **No custom spinner** over the system payment sheet.
- **After payment:**
  - Show a confirmation.
  - Never require an account before payment; invite sign-up on the confirmation screen instead.

### 8.5 Notifications [HIG]

- **Content:** only timely, valuable information that can be read at a glance.
- **No repeats:** never send the same thing twice.
- **In-app instead of push:**
  - If the person is looking at the content, update the UI instead of notifying.
  - Show errors in-app, not as notifications.
- **Wording:**
  - Short, title-case title.
  - The body is a full sentence.
  - No sensitive data and no app name.
- **Actions:** up to 4, and only ones that save time (such as Snooze). Never "Open app".

### 8.6 Live Activities (system Dynamic Island / Lock Screen) [HIG]

| Topic | Rule |
|---|---|
| Use for | Tasks or events with a clear start and end, ideally ≤ 8 hours |
| Content | Only what matters at a glance. Tapping deep-links to the right screen |
| Never | Ads or promotions; sensitive data on the Lock Screen |
| Text | Large and Medium or heavier. Avoid small text |
| Background | The Dynamic Island is opaque black. The Lock Screen version may use a custom colour if contrast holds |
| Corners and margins | Concentric with the outer shape. Standard Lock Screen margin is 14 pt |
| Separating content | Use inset container shapes or thick lines. Do not run content to the edges |
| Height | About 84–160 pt on the Lock Screen and when expanded. Shrink when there is little content |
| Interaction | Simple and direct, ideally a single control |
| Updates | Only when content really changes. Alert only for important changes. Do not also send a push for the same event |
| Ending | End as soon as the event ends. It may stay on the Lock Screen up to 4 hours; 15–30 minutes is usually enough |
| Animation | ≤ 2 seconds. Use numeric transitions for changing numbers. Move existing elements rather than rebuilding the layout |
| Presentations | Compact (two sides around the camera), Minimal (a dot that fits a 28 pt circle when several activities run), Expanded (on long press) and Lock Screen |

---

## 9. Accessibility [HIG]

| Item | iOS value |
|---|---|
| Tap target | 44 × 44 pt by default, 28 × 28 pt minimum |
| Spacing around controls | About 12 pt around bordered controls, about 24 pt around borderless ones |
| Text size | 17 pt default, 11 pt minimum. Must scale to at least 200% |
| Contrast | 4.5:1 for text ≤ 17 pt; 3:1 for text ≥ 18 pt or bold |
| Colour | Never the only signal. Add a shape, icon or text |
| Motion | Respect Reduce Motion: replace zooms and bounces with fades. Avoid flashing |

---

## 10. Writing (UX copy) [HIG + Recommended]

1. **Every word earns its place.** If you can remove a word without losing meaning, remove it.
2. **Front-load.** Put the most important words first. One screen covers one idea.
3. **Don't repeat what is visible.** If the amount is on the card, the caption does not restate it. The title, body and button should not repeat the same verb.
4. **Describe the thing, not the company.** Avoid "we / our". Write "Held until 2:15 PM", not "We're holding your room".
5. **Errors say how to fix it, not whose fault it is.** Write "Enter the same password in both fields."
6. **Too long? Cut words, don't shrink the text.** Do not abbreviate where there is room. Abbreviate only in tiny surfaces such as the Dynamic Island.
7. **Button labels** start with a verb. Pick one capitalisation style and use it everywhere.
8. **Consistent terms.** Choose one word per concept and keep it.
9. **Consistent formats:**

   | Content | Example |
   |---|---|
   | Time | `2:00 PM` |
   | Range | `2:00–3:00 PM` |
   | Date | `Fri, Nov 6` |
   | Duration | `30 min`, `1 hr` |

10. **Realistic, consistent sample data.** Numbers must agree across screens; for example, a total equals the sum of the items listed.

---

## 11. Avoiding the "AI-generated" look [Observed]

| Common in AI-generated screens | What the case studies do instead |
|---|---|
| Cards inside cards, grey frame on grey frame | Two layers at most: background + card |
| Every block has a border and a shadow | Layers separated by fill; shadows faint or absent |
| Many 12 px grey captions | Small text only for truly secondary information; the rest removed |
| Mixed corner radii | One pill shape and one card radius |
| Every button has an icon, text and a badge | Icon buttons have only an icon; text buttons have only text |
| Everything the same size, no focal point | One clearly largest element per screen |
| Every option outlined | Only the selected option is filled |
| Decorative blocks and placeholder data | Every element carries information the user actually has |

---

## 12. Older and newer styles compared [Observed]

| Aspect | 2018–2022 designs | 2024–2026 designs |
|---|---|---|
| Card radius | 8–16 | 20–32 |
| Tappable elements | 32–48, some rectangular buttons | 44–56, all pills or circles |
| Selected state | Often outlined | Filled only; unselected has nothing |
| Inputs | Underline or outlined box | Pill on light grey or white, no outline |
| Primary button colour | Brand colour | Often near-black; brand colour saved for 1–2 points |
| Big numbers | Bold | Regular / Medium with a small unit |
| Shadows | Visible | Faint or none; layers by fill |
| Top bar | Full-width bar with a centred title | Circular buttons and an avatar, no bar |
| Dialogs | Centred modal cards | Bottom sheets with a large top radius |
| Images | Illustrations or full photos | Cut-outs on light rounded tiles |
| Tab bar | Docked full-width bar | Floating pill, often icon-led |

---

## 13. Quick reference [Recommended]

Based on a 393 pt wide screen.

| Item | Default |
|---|---|
| Grid | 8 pt (4 pt for tiny gaps) |
| Side margin | 24 pt (16 pt on card-heavy screens) |
| Type scale | 32 / 24 / 20 / 16 / 14 / 12 (large title 28–36); never below 11 |
| Weights | 2–3 |
| Line height | Titles × 1.1, body × 1.5 |
| Text colours | Near-black + one mid-grey that passes 4.5:1 |
| Circular button | 44 |
| Input / search | 48 high, pill |
| Primary button | 56 high, full width, pill |
| Chip | 32–36 high (up to 44 in newer styles), pill |
| Icon | 24 frame / 16 live area / 1.5 stroke |
| Card | Radius 20–24, padding 16–20 |
| Sheet | Top radius 24–32 |
| Spacing inside a group | 8–16 |
| Spacing between groups | 24–32 |
| Colour | 4–6 greys + 1 accent + 2 background layers |
| Prominent buttons per screen | 1 (max 2) |

---

## 14. Self-check before handing off a screen

**Layout**
- [ ] One clear hero element.
- [ ] One leading alignment line.
- [ ] Space inside groups is smaller than space between groups.
- [ ] Content stays within the safe area.

**Type and colour**
- [ ] One typeface and 2–3 weights.
- [ ] Nothing smaller than 11 pt.
- [ ] Text contrast ≥ 4.5:1 (≥ 3:1 for large or bold text).
- [ ] One accent colour, used only for state and the main action.
- [ ] Colour is never the only signal.

**Shape and components**
- [ ] All tap targets ≥ 44 pt.
- [ ] One pill shape and one card radius; no card inside a card.
- [ ] At most 1–2 prominent buttons; no destructive action as the primary button.
- [ ] Selected options filled, unselected not outlined.
- [ ] At most one sheet at a time, with a grabber and swipe-to-dismiss.
- [ ] The tab bar stays visible except in full-screen modal flows.

**Behaviour**
- [ ] Permissions requested in context; any pre-permission screen has one "Continue" button.
- [ ] Sign-in requested as late as possible; account deletion available.
- [ ] Apple Pay first where supported.
- [ ] Determinate progress where it can be measured.
- [ ] No push notification duplicating a live card or Live Activity.

**Copy and data**
- [ ] No words that can be cut.
- [ ] No repetition of what is already visible.
- [ ] No "we".
- [ ] Error messages say how to fix the problem.
- [ ] Only real, consistent data the user would actually have.

---

## 15. Limitations

1. **Small sample.**
   - Only 9 case studies.
   - 5 of them were among the most-appreciated mobile app projects on Behance (from a crawl of 756 projects for "app", "mobile app" and "app design", excluding websites, dashboards and collections).
   - 4 are recent projects chosen for their contemporary style.
   - This is not a statistical survey.
2. **Measurement error.** Measured values are within about ±2 pt. Presentation images are compressed and some phones are tilted; only front-facing screens were measured.
3. **Appreciation counts are not a quality score.** They depend heavily on how long a project has been published.
4. **Point-in-time summary.** The HIG summary reflects the online HIG as of November 2026, including Liquid Glass. Apple updates it, so verify numbers on the official site.

## 16. References

**Apple**
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Topics summarised:
  - Live Activities, Layout, Accessibility, Typography, Color
  - Onboarding, Privacy, Managing accounts, Apple Pay
  - Buttons, Sheets, Tab bars, Notifications, Progress indicators
  - Writing

**Behance case studies** (all rights belong to their authors; used here only as references for the observed patterns)

| Project | Author | Link |
|---|---|---|
| Starbucks – UI/UX Redesign | Tofu Design (Daniel Tan) | https://www.behance.net/gallery/73284301/Starbucks-UIUX-Redesign |
| Boston taxi | — | https://www.behance.net/gallery/73541223/Boston-taxi |
| Education app design (praktika) | Anastasia Chernenko | https://www.behance.net/gallery/181095369/Education-app-design-UXUI |
| Travel app "Toucan" | Roman Lieli | https://www.behance.net/gallery/93390455/Travel-app-Toucan |
| Disney+, But Better. | — | https://www.behance.net/gallery/141700011/Disney-But-Better |
| Luxury Fashion Mobile App | Sheikh Raihan | https://www.behance.net/gallery/214607369/Luxury-Fashion-Mobile-App |
| Team Management Mobile App | Imran Jakir | https://www.behance.net/gallery/214855313/Team-Management-Mobile-App |
| Healthcare Mobile App Design | Vlad G. (Arounda) | https://www.behance.net/gallery/254164097/Healthcare-Mobile-App-Design |
| Smart home mobile app "homai" | Pocolo | https://www.behance.net/gallery/257634173/Smart-home-mobile-app-homai |
