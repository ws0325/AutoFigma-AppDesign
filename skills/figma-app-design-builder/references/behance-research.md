# Behance research: picking works and grid extraction

## Contents
1. Search and the three lists
2. Reading the data into the candidate table
3. Hard filters
4. Visual review and style tags
5. Picking 3
6. Using a Design Style Guide directly
7. Grid extraction (one cell = one pixel)
8. Extraction template `research/<app>.md`
9. Searching for a borrowed screen pattern (Step 5)
10. Copyright and sources

---

## 1. Search and the three lists

- **Search terms**: translate the app type into English and combine 2–3: `<type> app`, `<type> app ui`, `<type> mobile app`, `<scenario> app` (for example `fitness app`, `workout tracker app`).
- **URL**: `https://www.behance.net/search/projects?search=<terms>&sort=appreciations` (`sort=appreciations` verified November 2026).
- **The three lists**: in the sort menu at the top right, switch to **Most Appreciated**, **Most Viewed** and **Most Discussed** in turn (the menu also has Most Recent, not used here). After switching, note the `sort=` value in the address bar so you can edit the URL directly next time.
- Take roughly the top 15 of each list (about a screen and a half; scrolling loads more).
- **The sorting is loose**: under Most Appreciated the first results had 78, 37, 163, 31 and 939 appreciations, so Behance mixes in relevance and recency. Treat the lists only as entry points into the pool; rank them yourself.
- Plain web fetching usually fails (the page is rendered with JavaScript and direct requests get HTTP 403). **Open it in a browser.** If no browser is available, ask the user for links or screenshots.

## 2. Reading the data into the candidate table

Each card on the **search results page** shows title, author, appreciations and views. The page text reads like "939 appreciations for <title>" and "11,409 views for <title>". Read the full numbers, not the "11.4K" abbreviation.

Each **project page** (open every candidate) shows comments, the publish date, all images, and whether there is a style guide page.

Fill `design/01-candidates.csv` (UTF-8, header row first):

```csv
title,url,author,appreciations,views,comments,year,lists,excluded,style_guide,visual_polish,visual_hierarchy,visual_hig,visual_nielsen,visual_not_ai,style
LGrow - Personal Coaching Fitness App,https://www.behance.net/gallery/...,Multiple Owners,939,11409,12,2024,appreciated;viewed,,yes,,,,,,
```

- `lists`: which lists it appeared on, `appreciated;viewed;discussed`.
- `comments` is only known after opening the project page. If you did not read it, leave it empty; the script reweights. **Never estimate.**
- At the top of `01-candidates.md`, write "Data read on YYYY-MM-DD".

Then run:

```bash
python scripts/rank_candidates.py design/01-candidates.csv --top 8
```

## 3. Hard filters

Write a reason in `excluded` to drop a work:
- Not a phone app (website, dashboard, brand identity, poster, collection)
- Fewer than 6 front-facing, complete, untilted phone screens
- Only 3D mockups, animations or concept posters
- Visually inconsistent within the work (the author had no system)
- Mainly tablet or watch

## 4. Visual review and style tags

Open each of the top 8 and **look through every image of the project, not only the first few**: style guide pages and the cleanest front-facing screens are often near the end, and a work that looks fine at the top can turn out to be all tilted mockups. A quick way is a labelled contact sheet of all images (thumbnails in a grid with image numbers). Re-check the hard filters (§3) on the full set before scoring. Score each criterion from 1 to 5:

| Column | What to look at | 5 | 1 |
|---|---|---|---|
| `visual_polish` polish and consistency | Spacing, radii and type scale consistent throughout | Every screen uses the same components | Every screen does its own thing |
| `visual_hierarchy` hierarchy | A clear hero per screen, clear grouping | The focus is obvious | Everything the same size |
| `visual_hig` HIG compliance | Tap targets, text ≥ 11 pt, contrast, Tab Bar and Sheet use (`apple-hig-rules.md`) | Almost no violations | Several clear violations |
| `visual_nielsen` flow | Whether the main flow, status feedback, errors and empty states are shown (`nielsen-heuristics.md`) | Complete flow with states | A few pretty, disconnected screens |
| `visual_not_ai` not AI-looking | Against `anti-ai-checklist.md` | Distinct, restrained style | Gradients, nested cards, emoji icons |

**Style tags** (`style` column, 5 values in a fixed order, separated by `;`):

| Position | Dimension | Values |
|---|---|---|
| 1 | Background | `light` / `dark` / `color` (large areas of colour) |
| 2 | Card layering | `fill` / `shadow` / `outline` / `bento` / `flat` (no cards) |
| 3 | Primary button | `neutral` (near-black on light, near-white on dark) / `brand` / `gradient` / `outline` |
| 4 | Radius | `small` ≤12 / `medium` 13–20 / `large` ≥21 |
| 5 | Imagery | `photo` / `cutout` / `illustration` / `3d` / `none` |

Example: `light;fill;neutral;large;cutout`

## 5. Picking 3

```bash
python scripts/rank_candidates.py design/01-candidates.csv --final 3
```

- Total = popularity 40% + visual 60%, plus 0.05 with a style guide.
- Any two picks must differ in at least 2 of the 5 style tags; one that is too similar is skipped and the next one moves up.
- If fewer than 3 come out: review the next candidates by popularity (ranks 9–16), then widen the pool (other search terms, more per list), or check whether the style tags are too coarse. In practice many fitness works share "dark + neon" or "light + one bright accent", so expect to review 12–16 works to find 3 distinct styles.

In `01-candidates.md` write: the ranking table (script output), the 3 picks each with complete source and reason (quote the scores and review notes), and why high scorers were not picked.

## 6. Using a Design Style Guide directly

Many Behance case studies include one or more **Style Guide / Design System / UI Kit** pages (palette, typeface and type scale, spacing, radii, button and input specs, icons). When there is one:

1. **Use its values directly**, tag them `[Spec]`, and cite the exact image: [Behance · <project> · <author> · <URL> · image 12, Style Guide].
2. The author's values **take precedence** over measurements. When they differ, use the style guide but record the difference in the extraction file (for example "Style guide says 24 margin, home screen measures 20"). It means the author's screens do not fully follow their own guide; both values can be offered in the choice questions.
3. Measure with the grid anything the guide does not cover (often interaction states, empty states, Sheets and Tab Bar details).
4. Take colours from the hex labels on the image, not by sampling the swatch (compression shifts colour).

## 7. Grid extraction (one cell = one pixel)

A "cell" is one @1x design pixel (= 1 pt). The phone in a Behance image has been scaled up or down, so the script first scales the screen back to its design width (393 for iPhone 15/16). Each cell you measure is then one pixel in Figma and can go straight into the spec.

### 7.1 Preparation
- Save the work's front-facing screen images in `design/research/<app>/`, named in order: `01.png`, `02.png`… (open the image URL and save it; images live under `mir-s3-cdn-cf.behance.net`, and the project page usually links a larger version; take the largest).
- If one image contains several phones, handle each screen separately: find the original-image pixel coordinates of the screen's corners and pass them as `--crop x0,y0,x1,y1` (screen content only, not the case or shadow).
- Device width: a Dynamic Island-era status bar means 393 (Pro models may be 402); a notch means 375 or 390. If unsure, use 393 and say so in the file.

### 7.2 Measuring order

```bash
# 1. Is the image sharp enough for 1-cell accuracy? (warns when a cell is under 1 image pixel)
python scripts/grid_extract.py info design/research/kolo/03.png --crop 120,80,520,946

# 2. Whole-screen overview: a thin line every 8 cells, a thick labelled line every 40, for locating things
python scripts/grid_extract.py overview design/research/kolo/03.png --crop 120,80,520,946 -o design/research/kolo/03_overview.png

# 3. Exact values: scan a row or column for edges, giving margins, sizes and gaps directly
python scripts/grid_extract.py edges design/research/kolo/03.png --crop 120,80,520,946 --row 250
python scripts/grid_extract.py edges design/research/kolo/03.png --crop 120,80,520,946 --col 100

# 4. Details: enlarge a region with one line per cell (radii, icons, letter strokes, hairlines)
python scripts/grid_extract.py zoom design/research/kolo/03.png --crop 120,80,520,946 --region 16,192,64,240 -o design/research/kolo/03_zoom_card.png

# 5. Colours: dominant colours with share, and point sampling
python scripts/grid_extract.py colors design/research/kolo/03.png --crop 120,80,520,946 --top 8
python scripts/grid_extract.py sample design/research/kolo/03.png --crop 120,80,520,946 --at 24,120 196,420
```

### 7.3 How to measure each item

| Item | Method |
|---|---|
| Side margins | `edges --row` through a card or title; the first edge's x |
| Component heights, gaps | `edges --col` through a column of components; read the segment lengths |
| Card and button widths | Segment lengths from `edges --row` |
| Corner radius | `zoom` on a card corner: cells from where the straight edge starts curving to the corner |
| Font size | `zoom` on a capital letter or digit: measure cap height; size ≈ cap height ÷ 0.7. `edges --col` through the letter also gives the height |
| Line height | Cells between the baselines of two lines |
| Font weight | `zoom` on the strokes and compare with common weights at that size; write "about Medium" and tag ≈ |
| Icons | `zoom`: frame size, stroke width in cells, round or square caps |
| Colour | Backgrounds with `colors`; text with `sample` at the stroke centre; with a style guide, use the labelled hex |
| Contrast | `python scripts/contrast.py "#text" "#background"` |

- The edge threshold defaults to 8 (a white card on light grey differs by only about 11). Noisy images can use `--threshold 12`; fainter separations can go down to 5.
- Round readings to 1 cell, then see whether they fall on multiples of 4 or 8. If not, record them as they are; do not force them.
- Every value names its source: which image and which command or grid image.

## 8. Extraction template `research/<app>.md`

```markdown
# <Work title>

**Source:** [Behance · <title> · <author> · <full URL>] read on YYYY-MM-DD
**Data:** N appreciations · N views · N comments [Behance data · project page]
**Why picked:** total 0.xx, style tags … (see 01-candidates.md)
**Style guide:** yes (images 12–14) / no
**Screens measured:** 01 Onboarding, 03 Home, 05 Detail… (N screens); design width taken as 393
**Style in one line:** e.g. "White cards on light grey + near-black primary button, orange only for numbers"

## UI

| Item | Value | Tag | Source |
|---|---|---|---|
| Side margins | 24 | [Spec] | image 12, Style Guide |
| Home card gap | 16 | [Measured ≈] | 03.png · edges --col 196 |
| Card radius | 20 | [Measured ≈] | 03_zoom_card.png |
| Typeface | Inter | [Spec] | image 12 |
| Type scale | 32/24/18/16/14/12 | [Spec] | image 12 |
| Weights | Regular / Semibold | | |
| Text colours | #111111 / #6B6B6B | | |
| Background layers | #F4F4F4 base + #FFFFFF cards | | |
| Accent and where used | #FF6A00, numbers and progress only | | |
| Primary button | 56 high, full width, pill, #111111 | | |
| Input | | | |
| Selected / unselected | | | |
| Top bar | | | |
| Tab Bar | | | |
| Sheet | | | |
| Icons | 24 frame / 1.5 stroke / round caps | | |
| Imagery | | | |
| Shadows | none | | |

## Screen structure
For each measured screen, the structure top to bottom (ASCII is fine), and what its hero is.

## UX

| Item | Practice | Source |
|---|---|---|
| Main task flow | Home → Detail → Pick time → Confirm → Pay → Success (6 steps) | images 03–09 |
| Navigation | | |
| Status feedback | | |
| Empty states / errors | not shown | |
| Sign-in, permission timing | | |

## HIG / Nielsen check

| Finding | Basis | Verdict |
|---|---|---|
| 10 pt captions | [HIG · Typography] minimum 11 | Do not adopt |
| Deleting a workout has no confirmation | [Nielsen #5] | Do not adopt |
| Success screen shows a full summary | [Nielsen #1, #6] | Can adopt |

## Differences between the style guide and the screens (if any)

## 3 things worth learning / 3 things not to copy
```

## 9. Searching for a borrowed screen pattern (Step 5)

When a screen exists in none of the 3 references:
- Search `<type> app <screen>`, for example `fitness app paywall`, `meditation app onboarding`, `app empty state`, `app settings screen`.
- Use only the Most Appreciated list and pick 1–2 works that do this screen well; no full scoring needed.
- Learn the structure and interaction: order of information, which elements, where the buttons go, how states change.
- Visuals always follow DESIGN.md.
- Record in DESIGN.md's borrowing record: which screen, what was borrowed, complete source.

## 10. Copyright and sources

- Study patterns and values; **never put the other work's images, illustrations, logos, icons, brand colour combinations or copy into the design**.
- Images in `research/` are for analysis only and never go into the Figma deliverable.
- List every reference work (title, author, link) at the end of DESIGN.md.
