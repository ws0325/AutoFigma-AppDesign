# Step 1: Behance candidates and the 3 picks

**Data read on 2026-11-09.** Numbers come from each project page (`stats` on the page) 〔Behance data · project page · read 2026-11-09〕. Raw data: `01-candidates.csv`.

## How the pool was built

- Search term: `fitness app` (one term only; `references/behance-research.md` suggests 2–3. One was enough here because the pool already held 32 works; a narrower product would need more terms)
- Lists, top 15 of each (sort values verified in the address bar):
  - Most Appreciated: `https://www.behance.net/search/projects?search=fitness%20app&sort=appreciations`
  - Most Viewed: `…&sort=views`
  - Most Discussed: `…&sort=comments`
- After merging duplicates: **32 candidates**.
- The lists are not strictly sorted by the numbers (under Most Appreciated the first results had 78, 37, 163, 31, 939 appreciations), so ranking was recomputed with `scripts/rank_candidates.py`.

## Hard filters (5 excluded)

| Work | Reason |
|---|---|
| Healthcare & Wellness Brand Identity System | Brand identity, not an app |
| Fitness App Pitch Deck | Presentation, not an app |
| Redesign Kaimen \| Fitness App \| Website \| HR Dashboard | Mixed app + website + dashboard |
| SYRO — AI Gym Companion & Fitness App | A single long image; screens cannot be measured separately |
| Kolo: Daily Recovery Tracker | Fewer than 6 front-facing screens (almost all tilted or hand-held). Found only after checking all 13 images; it had been picked in an earlier run |

## Visual review

16 works were opened and every image was checked (contact sheets of all images). The top 8 by popularity gave only 2 distinct styles (most are "dark + neon" or "light + one bright accent"), so ranks 9–16 were reviewed as well.

## Final ranking (`rank_candidates.py --final 3`)

| # | Work | Popularity | Visual | Style guide | Total | Style |
|---|---|---|---|---|---|---|
| 1 | [Fitness mobile app \| UX/UI design](https://www.behance.net/gallery/243053067/Fitness-mobile-app-UXUI-design) **(picked)** | 0.69 | 0.80 | yes | 0.81 | light;fill;brand;large;photo |
| 2 | [LGrow - Personal Coaching Fitness App \| UX/UI](https://www.behance.net/gallery/254678997/LGrow-Personal-Coaching-Fitness-App-UXUI) **(picked)** | 0.82 | 0.65 | yes | 0.77 | dark;fill;neutral;large;photo |
| 3 | [AI Fitness & Health Mobile App](https://www.behance.net/gallery/255349787/AI-Fitness-Health-Mobile-App) | 0.61 | 0.75 | yes | 0.74 | light;fill;brand;large;photo |
| 4 | [Indore Cycling & Fitness Mobile App Design](https://www.behance.net/gallery/221311011/Indore-Cycling-Fitness-Mobile-App-Design) | 0.83 | 0.60 | yes | 0.74 | dark;fill;brand;large;photo |
| 5 | [AI Habit & Fitness Tracker Mobile App \| UI UX Design](https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design) **(picked)** | 0.52 | 0.80 | yes | 0.74 | light;fill;neutral;large;cutout |
| 6 | [AI Food Calorie Tracker App UI/UX](https://www.behance.net/gallery/254567479/AI-Food-Calorie-Tracker-App-UIUX-Nutrition-Fitness) | 0.73 | 0.65 | yes | 0.73 | light;shadow;brand;large;photo |

Ranks 3, 4 and 6 were skipped because their style tags were too close to a pick (fewer than 2 of 5 tags different). Full output: `final.txt`.

## The 3 picks

| | A · Femotion | B · LGrow | C · NutriPal |
|---|---|---|---|
| Work | [Fitness mobile app \| UX/UI design](https://www.behance.net/gallery/243053067/Fitness-mobile-app-UXUI-design) | [LGrow - Personal Coaching Fitness App \| UX/UI](https://www.behance.net/gallery/254678997/LGrow-Personal-Coaching-Fitness-App-UXUI) | [AI Habit & Fitness Tracker Mobile App \| UI UX Design](https://www.behance.net/gallery/250740123/AI-Habit-Fitness-Tracker-Mobile-App-UI-UX-Design) |
| Author | Oksana Bashkatova (Оксана Башкатова), with ШКОЛА ДИЗАЙНА | Tobi Bui & Design Team Ekotek | Sriraj Mohan |
| Data | 439 appreciations · 2,584 views · 326 comments | 939 · 11,412 · 308 | 294 · 5,350 · 96 |
| Style | Light grey + white cards, lime and lavender accents, real photos | Black, white primary buttons, blue glow, dot-matrix numbers | Off-white, black/white monochrome, data first, floating dark tab bar |
| Why | Best visual score (0.80) with the most complete UX: research, user flow, skeleton screens, full style guide | Most popular work in the pool (in all three lists) and the only strong dark style | Highest polish with a full style guide; the only monochrome option; includes workout screens |

None of the picked works' images, branding or copy are used in the design; they are studied for patterns and values only.
