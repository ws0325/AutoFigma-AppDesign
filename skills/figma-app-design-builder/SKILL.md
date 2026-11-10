---
name: figma-app-design-builder
description: Reference-driven iOS app UI design in Figma that avoids the generic "AI look". When someone says "design me a ... app": ask about purpose, features and desired feel; collect similar app designs on Behance from the Most Appreciated, Most Viewed and Most Discussed lists and score them to pick 3 works with distinct styles; extract their UI and UX pixel by pixel with a 1-cell = 1-pixel grid (or take values straight from a published Design Style Guide) into a local Markdown design spec; let the user choose cards, buttons, widths, colours and more through sourced multiple-choice questions; then design every screen in Figma, checking each one against Apple's Human Interface Guidelines and Nielsen's 10 usability heuristics, and finish with a full walkthrough audit. Every claim carries a complete source. Use this skill whenever someone wants to design or build a whole mobile app or a set of app screens, turn Behance references into a design spec or style guide, make an AI-generated UI look less AI-made, or mentions app UI design in Figma, Behance references, HIG, Nielsen heuristics or a DESIGN.md, even if they only ask for one of these steps.
---

# Figma App Design Builder: from Behance references to Figma screens

## Why it works this way

Left to its own taste, an AI draws the average of its training data: cards inside cards, a border and shadow on everything, purple-blue gradients, no focal point and empty copy. That is the "AI look".

This skill avoids it by **learning from real work first, letting the user decide, then designing by the rules**:
1. Pick 3 well-received, stylistically distinct apps of the same kind on Behance and measure them precisely.
2. Record everything measured, UI and UX, in a local Markdown file, with a source for every number.
3. Let the user choose between the 3 references dimension by dimension; their choices become the design spec.
4. Design in Figma from that spec, checking every screen against **Apple HIG (is the interface right?)** and **Nielsen's heuristics (is it easy to use?)**.

## Rule for the whole run: cite complete sources

To keep hallucination out, **every number and design judgement, in every message to the user and in every Markdown file, carries a source tag**. If there is no source, label it an AI suggestion; never present it as fact.

| Tag | Use for | Example |
|---|---|---|
| Behance work | A practice seen in a reference | [Behance · Kolo: Daily Recovery Tracker · Illia Aristov · https://www.behance.net/gallery/… · image 3, Home] |
| Measured | A value read from the pixel grid | [Measured ≈ · Kolo · research/kolo/03_overview.png · edges --row 250 · ±1 pt] |
| Behance data | Appreciations, views, comments | [Behance data · project page · read 2026-11-09] |
| HIG | Apple guideline | [HIG · Buttons] |
| Nielsen | Usability heuristic | [Nielsen #5 Error prevention] |
| User choice | Decided in the choice questions | [User choice · round 2 Q3] |
| AI suggestion | A judgement with no outside source | [AI suggestion] |

Ground rules:
- Only write Behance numbers you actually read on the page. If you could not read it, write "not read"; never estimate.
- Write full URLs, never "a Behance project".
- When references disagree on a value, list each value with its own source. Do not average them and attribute the average to one of them.

## Language

Talk to the user and write the project's Markdown files in the user's language. Keep component names, HIG terms and units in English (Tab Bar, Sheet, 44 pt).

## Workflow

```
0 Brief → 1 Pick 3 on Behance → 2 Grid extraction → 3 Write DESIGN.md → 4 User choices → 5 Design in Figma → 6 Walkthrough audit
 [ask user]   [report picks]                                              [ask user]                          [report to user]
```

All output goes in a `design/` folder inside **the project folder of the app being designed** (or wherever the user says):

```
design/
├── 00-brief.md                 Brief and site map
├── 01-candidates.csv           Behance candidate pool (script input)
├── 01-candidates.md            Scores and the 3 picks
├── research/<app>/             Screenshots and grid images
├── research/<app>.md           Full extraction for one work
├── DESIGN.md                   ★ The design spec (reference comparison + user choices + final rules)
├── screens.md                  Screen list, Figma links, per-screen checks
└── audit.md                    Walkthrough audit report
```

---

## Step 0: Understand the brief

When the user says "design me a fitness app", do not start searching yet. Ask these in one message (skip anything they already told you):

1. **Purpose**: who is it for, what problem does it solve, which 2–3 things will people do most?
2. **Features**: the must-have list. Does it involve sign-in, payment, maps, notifications or social features (these bring system rules with them)?
3. **Feel**: what impression should it give (professional, relaxed, premium, playful…)? Any apps they love or dislike? Any fixed brand colour, logo or typeface?
4. **Scope**: iPhone only? (The skill designs directly in high fidelity, Light and Dark.)

Then draft a **site map**: an indented list of every screen and which tab it belongs to, marking modal flows (cover the Tab Bar) and drill-down screens. Confirm it with the user and save it to `00-brief.md`. The site map is the only list of screens to draw.

---

## Step 1: Pick 3 works on Behance

Details in `references/behance-research.md`. Outline:

1. **Search terms**: turn the app type into 2–3 English queries (`fitness app`, `fitness app ui`, `workout tracker app`).
2. **Take about the top 15 from each of three lists**: Most Appreciated, Most Viewed and Most Discussed. Merge them into one pool and note which lists each work appeared on.
   - Behance mixes relevance and recency into its sorting; **the lists are not strictly ordered by the numbers**, so read the numbers and rank them yourself.
   - The search page shows appreciations and views only. Comments are on each project page.
3. **Hard filters**: exclude anything that is not a phone app, has fewer than 6 front-facing full screens, or only shows tilted mockups or posters. Write the reason in the `excluded` column. While on the project page, check for a **Design Style Guide** page and write `yes` in `style_guide` if there is one (it earns a bonus and its values are used directly later).
4. **Popularity score**: fill `01-candidates.csv` and run `python scripts/rank_candidates.py design/01-candidates.csv --top 8`. It scores appreciations, views, comments, appreciation rate (appreciations ÷ views, which is fairer to newer work) and how many lists a work appeared on.
5. **Visual review**: open the top 8 and score 5 criteria from 1 to 5 (polish, hierarchy, HIG compliance, Nielsen flow, not-AI-looking), plus 5 style tags. Popular is not the same as good, so this step weighs more.
6. **Pick 3**: run `python scripts/rank_candidates.py design/01-candidates.csv --final 3`. It ranks by popularity 40% + visual 60% (+0.05 with a style guide) and guarantees the 3 picks differ clearly in style, so the user has real options in Step 4.

Write `01-candidates.md`: the full ranking, the 3 picks each with complete source and reason, and why high-scoring works were not picked. Tell the user briefly which 3 were chosen, with links and a one-line style for each, then carry on.

---

## Step 2: Grid extraction (pixel-level learning)

Extract every front-facing screen of the 3 works. Method in `references/behance-research.md` §6–§8.

**First look for a Design Style Guide.** If the work includes a style guide, design system or UI kit page (palette, type scale, spacing, component specs), **use its values directly**, tag them `[Spec]` and say which image they came from. The author's numbers beat measurements. Measure only what the guide does not cover; where the screens differ from the guide, record both.

**Then measure on a grid where one cell is one pixel.** "Pixel" here means one @1x design pixel (1 pt): the script scales the screen in the screenshot back to its design width (such as 393), so each cell equals one pixel in Figma and can go straight into the spec.

1. Save the work's images in `design/research/<app>/` (for analysis only, never placed in the final design).
2. Measure with `scripts/grid_extract.py` (`--crop` frames one screen):
   ```bash
   python scripts/grid_extract.py info     design/research/kolo/03.png --crop 120,80,520,946   # is the image sharp enough for 1-cell accuracy?
   python scripts/grid_extract.py overview design/research/kolo/03.png --crop 120,80,520,946 -o design/research/kolo/03_overview.png
   python scripts/grid_extract.py edges    design/research/kolo/03.png --crop 120,80,520,946 --row 250   # reads margins and widths
   python scripts/grid_extract.py zoom     design/research/kolo/03.png --crop 120,80,520,946 --region 16,192,64,240 -o design/research/kolo/03_zoom_card.png
   python scripts/grid_extract.py colors   design/research/kolo/03.png --crop 120,80,520,946
   ```
   `overview` locates things, `edges` reads exact values (margins, sizes, gaps), `zoom` enlarges a region with one line per cell for corner radii, icons and letter heights.
3. Record the UX: steps in the main task, navigation, status feedback, empty states, errors, when sign-in and permissions are requested.
4. Check the work against HIG and Nielsen: which practices break the rules (do not adopt) and which are good.

Write one `research/<app>.md` per work (template in `references/behance-research.md` §8) with all UI and UX information and a source for every value.

---

## Step 3: Write DESIGN.md

Create `design/DESIGN.md` from `references/design-spec-template.md`. Write **Part 1, the reference comparison**, now: the 3 works side by side, one row per dimension (layout, type, colour, radius, cards, buttons, inputs, Tab Bar, top bar, selection, imagery, key flows…), every cell sourced. Mark practices that break HIG.

This table is the raw material for Step 4.

---

## Step 4: Let the user choose

Ask **multiple-choice questions** in plain chat messages. Format and question list in `references/user-choices.md`. Key points:

- Options come from the 3 references' real practices, plus the HIG default where there is one. Each option states exact values and its **complete source**.
- Practices that break HIG are not offered. If the user asks for one anyway, explain the conflict and log it in the decision record.
- Give a recommendation with a sourced reason.
- Ask in 2–3 rounds of 3–5 questions: global choices first (overall style, screen size, margins), component details later.
- The user may answer "recommended" for one question or for all the rest.

Write each round's answers into DESIGN.md Part 2, "User choices". When all rounds are done, write **Part 3, the final rules** (with the quick-reference table and the per-screen checklist), show the rules and table to the user, and start designing after they confirm.

---

## Step 5: Design screen by screen in Figma

Draw the site map one screen at a time, **using only values and components from DESIGN.md**. With many screens and subagents available, build the foundations yourself first and then split pages across subagents with a shared brief and shared sample data (`references/figma-build.md` §7).

**Design straight in high fidelity**, Light first, then a Dark copy of every screen made by switching the variable mode (`references/figma-build.md`, "Deliverable"). Figma build order (variables → text styles → components → screens) is in `references/figma-build.md`. Before calling Figma write tools, load the skills the Figma plugin provides (`figma-use`; add `figma-generate-design` for full screens and `figma-generate-library` for the component library). If Figma is not available, tell the user to connect it, and produce HTML screens in the meantime.

**Every screen goes through two HIG + Nielsen checks:**
- **Before drawing**: list the rules this screen involves (payment → Apple Pay first [HIG · Apple Pay]; delete → confirmation [Nielsen #5]).
- **After drawing**: go through the DESIGN.md checklist, `references/apple-hig-rules.md` §15 and `references/anti-ai-checklist.md`; fix failures on the spot. Compute contrast with `python scripts/contrast.py "#fg" "#bg"` instead of guessing.
- Log the result under that screen in `screens.md`.

**When you run out of ideas, borrow from Behance.** If a screen or feature does not exist in any of the 3 references (paywall, empty state, onboarding, settings, search results…), search Behance for that screen (`fitness app paywall`), pick one or two good examples, and use their **structure and interaction** on this screen:
- Visuals always follow DESIGN.md; do not bring over their colours, fonts or illustrations, or the app turns into a patchwork.
- Borrowed patterns go through the same HIG and Nielsen checks.
- Add a line to DESIGN.md's borrowing record: which screen, what was borrowed, complete source.
- This covers how to design a screen that is already planned. Adding a feature that is not in the site map changes the product's scope, so ask the user first.

Habits that decide how "AI" it looks: give every screen one hero; use realistic sample data that agrees across screens (the total equals the sum of the items, names sound like real people); show only what the user would really have; **use as few words as possible** — HIG: "Check each word to be sure it needs to be there. If you can use fewer words, do so." (`references/apple-hig-rules.md` §14a): no caption that repeats what is already on screen, no "we", few "your"; buttons start with a verb, errors say how to fix them.

---

## Step 6: Walkthrough audit

Once all screens are done, stop looking at screens one by one and **walk each main task end to end**, looking for problems a single screen cannot show (a flow that is too long, a missing way out, inconsistent wording, a live card and a push notification for the same event…):

1. **Nielsen**: one walkthrough table per main task from `references/nielsen-heuristics.md`, recording each problem, its heuristic and severity (0–4).
2. **Apple HIG**: the `references/apple-hig-rules.md` §15 checklist across the whole app.
3. **Not AI-looking**: the self-check questions in `references/anti-ai-checklist.md` §5.

Write `design/audit.md`: what already complies first, then problems by severity (location, current state, basis [source], suggestion). **It is a report; the user decides what to change.** Change things after they confirm; if a problem comes from a rule, revise DESIGN.md and log it in the decision record.

Finally report: which screens were made (Figma link), where the spec is and its key decisions, the audit conclusions, and what is not done yet (dark mode, high fidelity…).

## Reference files

| File | Read when |
|---|---|
| `references/behance-research.md` | Steps 1–2: search, scoring, visual review rubric, grid extraction, extraction template |
| `references/user-choices.md` | Step 4: question format and question list |
| `references/design-spec-template.md` | Steps 3–4: structure of DESIGN.md |
| `references/apple-hig-rules.md` | Steps 2, 4, 5, 6: HIG rules with numbers and checklist |
| `references/nielsen-heuristics.md` | Steps 2, 5, 6: heuristics, questions, severity, walkthrough table |
| `references/anti-ai-checklist.md` | Steps 1, 5, 6: symptoms of the AI look and what to do instead |
| `references/figma-build.md` | Step 5: Figma build order, naming, per-screen check log |
| `assets/example-design-rules.md` | Step 4: a complete finished spec, for level of detail and tone |
| `scripts/rank_candidates.py` | Step 1: popularity score, total score, 3 picks with distinct styles |
| `scripts/grid_extract.py` | Step 2: 1-cell = 1-pixel measuring: overview, zoom, edge reading, colours (needs `pip install pillow`) |
| `scripts/contrast.py` | Steps 5–6: WCAG contrast ratio |
