# User choice questions (Step 4)

## Why multiple choice

People rarely know what corner radius they want, but they can easily pick between three real examples. Every option comes from a measured value or style guide of the 3 references and carries a complete source, so the user can open the link and check, and the AI has no room to invent numbers.

## Format

Ask in a plain chat message, 3–5 questions per round. The user answers with question number + letter ("1A 2C 3 recommended"). Each question looks like this:

```markdown
### Q3 Card style (round 1, 3/4)

A. White cards on a light-grey background, no shadow or border, radius 24, padding 20
   [Behance · LGrow - Personal Coaching Fitness App · Multiple Owners · https://www.behance.net/gallery/… · image 4, Home]
   [Measured ≈ · research/lgrow/04.png · edges --row 250 / 04_zoom_card.png]
B. Light-grey cards on white, radius 16, 12 between cards
   [Behance · Kolo: Daily Recovery Tracker · Illia Aristov · https://www.behance.net/gallery/… · image 12, Style Guide][Spec]
C. Dark cards #1C1C1E on black, radius 28, layered by brightness
   [Behance · Home workout app for fitness · Multiple Owners · https://www.behance.net/gallery/… · image 2]
   [Measured ≈ · research/home-workout/02.png]

Recommended: A. Layers are separated by fill alone, so cards need no shadow, which is the least "AI-looking" option [anti-ai-checklist §1]; inner radii follow from the concentric rule [HIG · Layout].
```

Rules:
- **Every option states exact values and a complete source** (title, author, full URL, image number; plus the measurement file for measured values).
- Options are usually A/B/C for the 3 works. Where HIG has a clear default for the dimension, add a D option tagged [HIG · page name].
- Dimensions where all 3 works agree are not asked. Say at the end of the message "These items are the same in all 3 and are adopted directly: …", with sources.
- **Practices that break HIG are not offered.** Add a line under the question: "<work> uses 10 pt captions, below the HIG minimum of 11 pt [HIG · Typography], so it is not listed."
- Give a reason for the recommendation, with sources; if there is no outside basis, tag it [AI suggestion].
- The user may say "recommended" for one question or "recommended for the rest", or mix ("A's radius with B's colours"). After a mix, check for conflicts (contrast, for example) and point them out.
- If the user asks for something outside the options, do it, record it as [User choice · custom], and still check it against HIG.

## Question list

Ask in rounds, global first, details later. Drop questions the product does not need (no form, no input question).

### Round 1: global

| # | Question | Where the options come from |
|---|---|---|
| 1 | **Overall style**: which work leads? | One-line style of each work + a representative image number |
| 2 | **Design size**: which device to draw on? | Fixed options: A. 393×852 (iPhone 15/16, most common) B. 402×874 (iPhone 16 Pro) C. 440×956 (iPhone 16 Pro Max) D. 375×812 (older / mini) [AI suggestion · confirm against Apple's device specs]; also state which width each reference was drawn at |
| 3 | **Side margins** | Measured values of the 3 works (commonly 16 / 20 / 24) |
| 4 | **Background layering**: white base with grey cards / grey base with white cards / dark | The 3 works |
| 5 | **Light, dark or both** | Fixed options; HIG expects a dark version of every colour [HIG · Color] |

### Round 2: visual language

| # | Question | Where the options come from |
|---|---|---|
| 6 | **Accent and its use**: brand colour as the primary button, or near-black primary button with the brand colour in 1–2 places | The 3 works + any existing brand colour |
| 7 | **Typeface** | The 3 works' typefaces; D. SF Pro (system) [HIG · Typography] |
| 8 | **Type scale**: large title size and weight, body size | The 3 works' scales; D. iOS default styles [HIG · Typography] |
| 9 | **Radius system**: pill + which card radius | Measured in the 3 works |
| 10 | **Card style**: fill / shadow / border, padding | Measured in the 3 works |
| 11 | **Imagery**: photos / cutouts / illustration / none | The 3 works |

### Round 3: components

| # | Question | Where the options come from |
|---|---|---|
| 12 | **Primary button**: height, colour, shape, inset arrow circle or not | Measured in the 3 works |
| 13 | **Input**: height, fill, border or not | Measured in the 3 works |
| 14 | **Selected state**: fill / outline / underline | The 3 works; recommend "selected filled, unselected without outline" [anti-ai-checklist §1] |
| 15 | **Tab Bar**: system Liquid Glass / floating pill / icons only | The 3 works; D. system Tab Bar [HIG · Tab bars] (every item needs a text label) |
| 16 | **Top bar**: no background with circle buttons / centred title / large title | The 3 works |
| 17 | **Dialogs**: bottom Sheet / centred card | The 3 works; recommend Sheet [HIG · Sheets] |
| 18 | **Button capitalisation**: title case (Book Room) / sentence case (Book room) | HIG uses title case [HIG · Buttons]; sentence case goes in the decision record |

## Recording in DESIGN.md

Write each round's answers into DESIGN.md Part 2 straight away:

```markdown
| Round / Q | Question | Choice | Value | Source |
|---|---|---|---|---|
| 1 / Q3 | Side margins | A | 24 pt | [Behance · LGrow · … · image 4][Measured ≈ · research/lgrow/04.png] |
| 2 / Q6 | Accent | custom | #2F6BFF, progress and current tab only | [User choice · custom] |
```

After the last round, show the user the final rules (Part 3) and the quick-reference table, and start drawing once they confirm.
