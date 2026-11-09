# DESIGN.md template

`design/DESIGN.md` is the app's single design spec, in three parts: reference research (written in Step 3) → user choices (Step 4) → final rules (end of Step 4, kept up to date in Steps 5–6). A complete finished set of rules is in `assets/example-design-rules.md`; match its level of detail and tone.

Every value and judgement carries a source tag (see "Cite complete sources" in SKILL.md).

```markdown
# <App name> design spec

**What this is:** one sentence.
**Based on:** 3 Behance references (§1.2) + user choices (Part 2) + Apple HIG (date checked) + Nielsen's 10 heuristics.
**Version / date:**

---

# Part 1: Reference research

## 1.1 How the works were picked
Search terms, the three lists, pool size, exclusions, scoring method; one paragraph + link to 01-candidates.md.

## 1.2 The three references
| | A | B | C |
|---|---|---|---|
| Work | title + full URL | | |
| Author | | | |
| Data | appreciations / views / comments (date read) | | |
| Style in one line | | | |
| Style guide | yes / no | | |
| Extraction file | research/a.md | | |

## 1.3 UI comparison
One row per dimension, each cell a value + source; mark cells that break HIG with ⚠ and the basis.
| Dimension | A | B | C | HIG |
|---|---|---|---|---|
| Design width | | | | — |
| Side margins | | | | — |
| Background layers | | | | |
| Typeface / scale / weights | | | | Min 11 pt, nothing lighter than Regular [HIG · Typography] |
| Text colours and contrast | | | | 4.5:1 for ≤17 pt [HIG · Accessibility] |
| Accent and its use | | | | One colour, one meaning [HIG · Color] |
| Radius | | | | Concentric [HIG · Layout] |
| Cards | | | | |
| Primary button | | | | ≥44 pt, 1–2 prominent buttons per screen [HIG · Buttons] |
| Input | | | | |
| Selected state | | | | |
| Top bar | | | | |
| Tab Bar | | | | [HIG · Tab bars] |
| Dialogs | | | | [HIG · Sheets] |
| Icons | | | | |
| Imagery | | | | |

## 1.4 UX comparison
| Dimension | A | B | C |
|---|---|---|---|
| Main task flow (steps) | | | |
| Navigation | | | |
| Status feedback | | | |
| Sign-in / permission timing | | | |
| Empty states / errors | | | |

## 1.5 Check results
For each work, practices that break HIG / Nielsen (not adopted) and practices worth learning, with sources.

---

# Part 2: User choices
| Round / Q | Question | Choice | Value | Source |
|---|---|---|---|---|
Items where all 3 works agree and were adopted directly are listed too, with choice "same in all 3".

---

# Part 3: Final rules

## 0. How to read
- Source tags: [Spec] author's style guide · [Measured ≈] grid measurement · [Observed] pattern seen · [HIG] · [Nielsen] · [User choice] · [AI suggestion]
- Priority when rules conflict: accessibility [HIG] > other [HIG] > user choices > reference works > AI suggestions

## 1. Core principles (6–10)
This app's own style decisions, one sentence each + source.

## 2. Layout and grid
Design size, grid, margins, alignment line, safe area, spacing inside / between groups, Dynamic Type.

## 3. Typography
Typeface, allowed weights, type scale (role | size/line height | weight | colour token).

## 4. Colour
Token table: name | light hex | dark hex | use | contrast against its background (computed with contrast.py). Where the accent is used.

## 5. Shape and radius
Pill / card / circle; concentric rule; image radius; Sheet top radius.

## 6. Components
For each: size, states (default / pressed / selected / disabled / loading), use, what not to do. At least: buttons (primary / secondary / destructive / icon), input, selection, list row, info row, card, top bar, Tab Bar, Sheet, progress, empty state.

## 7. Page patterns
Home screen top to bottom (ASCII), and any other patterns this app uses: detail, booking / checkout flow, success screen…

## 8. System behaviour
Only what this app uses: onboarding, permissions (when each is requested), accounts (when to sign in, methods, account deletion), payment, notifications (which events notify and which do not), Live Activities.

## 9. Accessibility
Tap targets, minimum text size, contrast, never colour alone, Reduce Motion.

## 10. Nielsen's heuristics in this app
| Heuristic | What this app does (down to screens and components) |

## 11. Writing
Writing rules, glossary (one word per concept), formats (time, date, duration, currency), button capitalisation.

## 12. Not AI-looking
The 5–8 points that matter most for this app, as "don't → do".

## 13. Quick reference (becomes Figma variables)
| Item | Value | Figma variable | Source |
|---|---|---|---|
| Design size | 393×852 | — | [User choice · 1/Q2] |
| Grid | 8 (4 for details) | space/* | |
| Side margin | 24 | space/page | |
| Type scale | … | text/* | |
| Radius | pill / 24 | radius/pill, radius/card | |
| Primary button height | 56 | size/button | |
| Colours | … | color/* | |

## 14. Per-screen checklist
Layout / type and colour / shape and components / behaviour / copy and data, 3–6 items each; ticked for every screen in Step 5.

## 15. Borrowing record
| Screen | What was borrowed (structure / interaction) | Source |
|---|---|---|

## 16. Decision record
| # | Decision | Reason | Source | Date |
Record: deliberate departures from HIG, mixed choices, rules changed after the audit.

## 17. Limitations, references and disclaimer
Measurement error, sample size, date HIG was checked; every reference work (title, author, full link).

> **Disclaimer.** This spec is an independent summary written for this project. It is not affiliated with or endorsed by Apple, Adobe Behance, Figma or Nielsen Norman Group. The reference works belong to their authors and are cited only for the patterns observed; their branding, images and copy are not used. Measured values are approximate. Check the official HIG before relying on a number.
```

## Writing reminders
- Every rule must be checkable against a screen. "Clean and elegant" is not a rule; "one primary button per screen" is.
- Every value in Part 3 must be traceable to Part 1 or Part 2. If it is not, it is an [AI suggestion], and the decision record says why it was chosen.
- The file must work on its own for another AI or designer, without this conversation.
