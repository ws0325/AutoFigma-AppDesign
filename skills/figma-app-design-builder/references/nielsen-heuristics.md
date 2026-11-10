# Nielsen's 10 usability heuristics (mobile app version)

> Ten heuristics published by Jakob Nielsen in 1994 and still in wide use. HIG decides whether the interface is built right; Nielsen decides whether people get through it smoothly. Used in four places:
> - **Step 2, extraction**: check the Behance references so their usability problems are not copied;
> - **Step 4, rules**: turn each heuristic into concrete practice for this product (DESIGN.md §10);
> - **Step 5, every screen**: list the heuristics a screen involves before drawing and check them after;
> - **Step 6, walkthrough**: walk each main task step by step, asking the questions below at every step.

## Severity (Nielsen 0–4)

| Level | Name | Meaning | Action |
|---|---|---|---|
| 0 | Not a problem | The reviewer does not consider it a usability problem | None |
| 1 | Cosmetic | Affects only appearance | Fix if time allows |
| 2 | Minor | Occasionally slows people down | Low priority |
| 3 | Major | Often stops people or causes mistakes | High priority, fix before handoff |
| 4 | Catastrophe | People cannot finish the task, or it causes loss (money, data, privacy) | Must fix |

Judge by three factors together: **frequency** (how many people hit it), **impact** (how hard it is to recover), **persistence** (whether it keeps happening once learned).

---

## The ten heuristics with mobile questions

### #1 Visibility of system status
Keep people informed with timely feedback.
- Is there visual feedback within 0.1 s of a tap (pressed state, spinner in the button)?
- Do waiting actions show progress? Is it a determinate bar when progress can be measured?
- Is it obvious which tab or step you are on (step indicator in multi-step flows)?
- Is the status of orders, bookings and uploads shown prominently (status pill, live card)?
- Are offline, sync failure and save success reported?

### #2 Match between the system and the real world
Use the user's words and concepts, in real-world order.
- Is the copy in the user's words, not the back end's ("Order #A8F3-Status=2" ✗)?
- Are icons used in their common meaning? Are uncertain icons labelled?
- Are time, currency and units formatted for the user's region?
- Does the flow follow real-world order (date before time, not the reverse)?

### #3 User control and freedom
Give an obvious way out of mistakes.
- Can every drill-down screen go back? Do modal flows have Cancel / Close?
- Can Sheets be swiped away? Is there a confirmation when changes are unsaved?
- Can important actions be undone (Undo after delete, confirmation before cancelling a booking)?
- Can multi-step flows go back a step without losing what was entered?
- Can permissions, notifications and subscriptions be turned off in Settings?

### #4 Consistency and standards
The same thing looks and is named the same everywhere; follow platform conventions (HIG here).
- Is each concept called by one word throughout?
- Are primary buttons, selected states, cards and list rows the same on every screen?
- Are Back at top left, Tab Bar at the bottom and Sheet Cancel/Done where iOS puts them?
- Does each colour mean the same thing everywhere?

### #5 Error prevention
Better than a good error message is not letting the error happen.
- Do destructive actions (delete, cancel, log out, pay) have a confirmation that states the consequence?
- Do inputs use the right keyboard (number, email, phone) and show the expected format?
- Are unavailable dates and slots disabled up front rather than rejected after choosing?
- Are dangerous buttons far from common ones and not styled as primary?
- Is there a complete summary (time, place, amount) before payment?

### #6 Recognition rather than recall
Show options and information; do not make people remember.
- Can recent items, favourites and search history be tapped directly?
- Do later steps of a form show what was chosen earlier (summary row)?
- Are icons unlabelled only when they are extremely common?
- Do empty states say what can be done next?

### #7 Flexibility and efficiency of use
Usable for newcomers, faster for experts.
- Do frequent tasks have shortcuts (Book Again, repeat last order, home shortcuts)?
- Are system accelerators supported: Face ID / passkey sign-in, Apple Pay, one-time-code and address autofill?
- Are there sensible defaults (default duration, last choice)?
- Are gestures supported (swipe to delete, pull to refresh) with a visible button alternative?

### #8 Aesthetic and minimalist design
Every extra element takes attention from the others.
- Does each screen have one and only one hero (largest title, number or image)?
- Can any text, icon or decoration be removed without hurting understanding?
- Is data shown that the user does not actually have (empty cards, fake data)?
- Is secondary information moved into drill-downs or Sheets?
(Closely tied to `anti-ai-checklist.md`; review them together.)

### #9 Help users recognize, diagnose, and recover from errors
Say what went wrong and how to fix it, in plain words.
- Is the error shown next to where it happened (under the field), not only at the top?
- Does the copy say how to fix it, not whose fault it is ("Enter the same password in both fields" ✓, "Invalid input" ✗)?
- Is there an icon or text, not just red?
- Is entered content kept after an error?
- Do network failures offer Retry?

### #10 Help and documentation
Ideally no help is needed; when it is, it is easy to find, specific and short.
- Do complex features have a short tip where they are used, rather than an up-front tour?
- Is there a Help / FAQ / Contact entry in Settings or Profile?
- Can skipped onboarding be found again in Help?

---

## Putting the heuristics into the spec (Step 4, DESIGN.md §10)

Do not copy the ten heuristics. Write each as "heuristic → what this app does", for example:

```markdown
| Heuristic | What this app does |
|---|---|
| #1 Status | From 30 minutes before a booking, a live card at the top of Home (countdown + progress bar); the pay button shows "Paying…" |
| #3 Control | Cancel booking: a Sheet shows the refund first, then confirm; Undo available for 5 s after cancelling |
| #5 Prevention | Full slots are disabled and marked "Full", not tappable |
| #7 Efficiency | Order detail offers "Book Again" with last time's room and duration |
```

## Walkthrough log format (Step 6)

Walk each main task step by step and note which heuristic each problem touches:

```markdown
### Task: book a room and pay
| Step | Screen | Problem | Heuristic | Severity | Suggestion |
|---|---|---|---|---|---|
| 3 | Pick time | Full slots can be tapped and only then show an error | #5 | 3 | Disable + "Full" |
```
