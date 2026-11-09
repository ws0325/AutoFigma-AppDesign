# Apple HIG rules (iOS, with numbers)

> Summarised from the online Apple Human Interface Guidelines (including Liquid Glass), checked November 2026. The HIG changes; when possible, check a number at https://developer.apple.com/design/human-interface-guidelines/ before relying on it, and write the date checked in the spec.
> This file is an independent summary in our own words and is not affiliated with or endorsed by Apple.

## Contents
1. Layout · 2. Accessibility · 3. Typography · 4. Color · 5. Buttons · 6. Sheets · 7. Tab bars · 8. Onboarding · 9. Privacy · 10. Accounts · 11. Apple Pay · 12. Notifications · 13. Progress · 14. Live Activities · 15. Checklist

---

## 1. Layout
- Put the most important content at the top and on the leading side; aligned items read as related.
- Group with space, containers or dividers; use progressive disclosure (drill-down, expandable rows, Sheets) to show less at first.
- Separate controls from content with Liquid Glass and scroll edge effects, not a solid strip behind the controls; let background content run under the Tab Bar and toolbars.
- Keep content inside the safe area (status bar, Dynamic Island, Home indicator).
- Support Dynamic Type: as text grows, side-by-side items stack, line heights grow, and text is never clipped.

## 2. Accessibility
| Item | Value |
|---|---|
| Tap target | 44×44 pt default, 28×28 pt minimum |
| Spacing around controls | About 12 pt around bordered controls, about 24 pt around borderless ones |
| Text size | 17 pt default, 11 pt minimum; must scale to at least 200% |
| Contrast | 4.5:1 for text ≤17 pt; 3:1 for text ≥18 pt or bold |
| Colour | Never the only signal; add shape, icon or text |
| Motion | Respect Reduce Motion: replace zooms and bounces with fades; avoid flashing |

## 3. Typography
- Avoid Ultralight, Thin and Light; use Regular, Medium, Semibold and Bold.
- Build hierarchy with size, weight and colour; use as few typefaces as possible.
- iOS default styles (size/line height): Large Title 34/41 · Title 1 28/34 · Title 2 22/28 · Title 3 20/25 · Headline 17/22 Semibold · Body 17/22 · Callout 16/21 · Subheadline 15/20 · Footnote 13/18 · Caption 1 12/16 · Caption 2 11/13.

## 4. Color
- One colour, one meaning.
- Use colour sparingly: for state and the main action.
- To emphasise a primary action, colour its **background**, not only its text or icon; do not fill the backgrounds of several controls at once.
- Prepare light, dark and high-contrast versions of every colour.

## 5. Buttons
- Tap target ≥ 44×44 pt.
- 1–2 prominent buttons per screen; mark the recommended option with a stronger style, not a bigger size.
- Destructive actions (delete, remove, cancel booking, log out) are never the primary button; use the Destructive (red) style.
- Labels start with a verb; HIG uses title case (Add to Cart). If you choose sentence case, use it everywhere and record it in the decision record.
- When an action takes time, show progress inside the button ("Checkout" → "Checking out…").

## 6. Sheets
- For simple tasks that finish quickly; long or complex flows get a full screen.
- Two detents: medium (about half height) and large; a resizable sheet shows a grabber.
- Swipe down to dismiss; confirm first if there are unsaved changes.
- Cancel at top left, Done at top right; in multi-step sheets Back replaces Cancel.
- One sheet at a time; never stack them.

## 7. Tab bars
- As few tabs as possible; every tab has a text label, ideally one word.
- Floats above content with a Liquid Glass background.
- Stays visible when moving between sections; only full-screen modal flows may cover it.
- Tabs are destinations, not actions; never hide or disable an empty tab, explain why it is empty.
- Badges only for important information.

## 8. Onboarding
- Ideally people learn by using the app; if onboarding is needed, keep it fast, enjoyable and skippable.
- Prefer a short tip where it is needed over an up-front tour.
- Never force a skipped tutorial again, but keep it reachable from Help or Settings.
- No terms and conditions in onboarding; let people use the app before asking for ratings or payment.

## 9. Privacy (requesting permission)
- Ask when the feature needs it; ask at launch only if the app cannot work without it.
- An optional pre-permission screen before the system alert: **exactly one button**, labelled "Continue" or "Next", never "Allow"; no Cancel, Close or other way out; must not imitate the system alert or point at its "Allow" button.
- Never offer a reward for a permission or lock unrelated features when it is denied; offer a manual alternative ("Choose an area" instead of location).
- The system alert's purpose string is a complete, active sentence saying what the data is used for.

## 10. Managing accounts
- Require an account only when a core feature needs it, and as late as possible: let people browse first and sign in when they must (a shopping app at checkout).
- Prefer Sign in with Apple, then passkeys; with passwords add two-factor authentication. Name the method on the button ("Sign In with Face ID").
- If people can create an account they must be able to delete it (not just deactivate it): easy to find, say when deletion will finish, confirm when it has.

## 11. Apple Pay
- Where supported, Apple Pay is the first payment option: listed first, no smaller than the others, visible without scrolling.
- Do not put Apple Pay behind its own step.
- The payment sheet shows only what is needed; the total line reads "Pay <merchant>".
- No custom spinner over the system payment sheet.
- Show a confirmation after payment; never require an account before payment; invite sign-up on the confirmation screen instead.

## 12. Notifications
- Only timely, valuable information readable at a glance; never send the same thing twice.
- If the person is looking at the content, update the UI instead of notifying; show errors in the app, not as notifications.
- Short title-case title; the body is a full sentence; no sensitive data and no app name.
- Up to 4 actions, only time-savers (such as Snooze); never "Open app".

## 13. Progress indicators
- Use a determinate bar when progress can be measured; a spinner only when it cannot.
- Never let progress stall; keep the pace steady.
- Add a label only if it helps; "Loading…" alone does not.
- Offer Cancel when cancelling is safe.

## 14. Live Activities (Dynamic Island / Lock Screen)
| Item | Rule |
|---|---|
| Use for | Tasks with a clear start and end, ideally ≤ 8 hours |
| Content | Only what matters at a glance; tapping deep-links to the right screen |
| Never | Ads or promotions; sensitive data on the Lock Screen |
| Text | Large, Medium or heavier; avoid small text |
| Background | The Dynamic Island is opaque black; the Lock Screen version may use a custom colour if contrast holds |
| Corners and margins | Concentric: inner radius = outer radius − margin; standard Lock Screen margin 14 pt |
| Height | About 84–160 pt on the Lock Screen and when expanded |
| Interaction | Simple and direct, ideally a single control |
| Updates | Only when content really changes; no push notification for the same event while it runs |
| Ending | End when the event ends; may stay on the Lock Screen up to 4 hours, usually 15–30 minutes |
| Animation | ≤ 2 seconds; numeric transitions for changing numbers; move existing elements instead of rebuilding |
| Presentations | Compact (both sides of the camera), Minimal (28 pt circle), Expanded (long press), Lock Screen |

---

## 15. HIG checklist (per-screen check in Step 5, walkthrough in Step 6)

**Layout and accessibility**
- [ ] Content inside the safe area; background runs under the Tab Bar
- [ ] Every tappable element ≥ 44×44 pt
- [ ] No text smaller than 11 pt
- [ ] Contrast: text ≤17 pt ≥ 4.5:1; large or bold ≥ 3:1 (compute with `scripts/contrast.py`)
- [ ] Colour is never the only signal
- [ ] No Light / Thin / Ultralight weights

**Components**
- [ ] ≤ 2 prominent buttons per screen; destructive actions are not primary
- [ ] Button labels start with a verb; one capitalisation style throughout
- [ ] Waiting buttons show progress inside
- [ ] Sheets: one at a time, grabber, swipe to dismiss, Cancel left / Done right
- [ ] Tab Bar: one-word labels, visible between sections, covered only by modal flows
- [ ] Determinate progress where progress can be measured

**Behaviour**
- [ ] Permissions requested in context; any pre-permission screen has a single "Continue"
- [ ] Sign-in as late as possible; account deletion available
- [ ] Apple Pay first where supported
- [ ] No duplicate notifications; no push while a Live Activity or live card shows the same event
- [ ] Onboarding skippable, no terms, no rating or payment requests
- [ ] Every colour has a dark-mode value (high fidelity)
