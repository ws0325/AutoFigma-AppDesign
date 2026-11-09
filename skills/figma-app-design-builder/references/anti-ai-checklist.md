# Not-AI-looking checklist

The "AI look" is not one mistake. It is a pile of average decisions: each looks fine alone, together they look like a template. Below, common symptoms in four groups (visual, structure, copy, data) and what real, well-regarded designs do instead. Use it as a constraint while designing and a checklist while reviewing.

## 1. Visual

| Common in AI output | What good real designs do |
|---|---|
| Cards inside cards, grey frame inside grey frame | Two layers at most: background + card |
| Border and shadow on every block | Layers separated by fill; shadows faint or none |
| Purple-blue or pink-purple gradients, gradient text, glows | Neutral greys + one accent, used only for state and the main action |
| Accent colour everywhere | The accent covers little area, which is why it stands out; primary buttons are often near-black |
| Mixed radii (4, 8, 12, 16, 20 on one screen) | One pill + one card radius; inner radii concentric |
| Every option outlined | Only the selected option is filled; unselected options are text only |
| Text in icon buttons, icons in text buttons, plus a badge | Icon buttons hold only an icon, text buttons only text |
| Icons from different sets with different strokes | One icon set: 24 frame, 16 live area, one stroke width and cap style |
| Illustration, photos, 3D and emoji mixed | One image style per app |
| Emoji used as icons | Line icons or real images |
| Frosted glass everywhere | Liquid Glass only for the control layer floating over content (Tab Bar, toolbars) |
| Everything centred | One leading alignment line shared by titles, search, cards and section headers |
| Pure #000000 text and buttons | Near-black (#111, #1C1C1E…); pure black only for a deliberate full-black screen |
| Big bold numbers | Big Regular / Medium numbers with a small grey unit |

## 2. Structure

| Common in AI output | What good real designs do |
|---|---|
| Everything the same size, no focal point | One clear hero per screen |
| Home = greeting + three feature cards + chart + recommendations | Home built around the one thing the user most likely wants now |
| Same spacing between groups and inside groups | Spacing inside a group is about half the spacing between groups |
| Every section has a title + "See all" | Only sections that really have more content |
| Dialogs as centred cards | Bottom Sheets with a large top radius |
| A full-width top bar with a background | No bar background; avatar or back on the left, 1–2 circle buttons on the right |
| A docked full-width Tab Bar with a divider | A floating pill Tab Bar (or the system Liquid Glass Tab Bar) |
| An empty card drawn as a placeholder for missing data | Hide what does not exist; when needed, an empty state that says what to do |

## 3. Copy

| Common in AI output | Better |
|---|---|
| "Unlock your potential", "Seamless experience", "Elevate your journey" | Say the specific thing: "Book a quiet room in 2 taps" |
| "Welcome back, John! 👋" | Remove it, or keep only useful information ("2 bookings today") |
| "We're processing your request" | Describe the state: "Paying…", "Held until 2:15 PM" |
| Buttons labelled "Submit", "OK", "Click here" | Verb + object: "Book Room", "Pay $24" |
| "Error occurred" / "Invalid input" | Say how to fix it: "Enter a 6-digit code" |
| Title, body and button repeat the same verb | Each says something different; do not repeat what is visible |
| Lots of 12 px grey captions | Keep only what is needed; delete the rest |
| One concept, several names (Order / Booking / Reservation) | One word per concept, everywhere |

## 4. Data

| Common in AI output | Better |
|---|---|
| Lorem ipsum, John Doe, Item 1, $99.99 | Realistic names, places and prices (prices fit the industry) |
| Total ≠ sum of items; Home says 3 orders, the list shows 5 | Numbers agree across every screen |
| Decorative charts with random trends | Charts only where the user needs a trend, with plausible data |
| Every date "Jan 1, 2024" | Plausible recent dates, consistent across screens |
| Every card 4.9 ★ and "Popular" | Ratings and labels vary like real data |

## 5. Quick self-check questions

1. Cover the logo: could you still tell which app this is? (Yes → it has its own style; no → too template-like.)
2. Which three elements could be removed to make the screen better?
3. What is the hero? Can you find it at a glance?
4. How many times does the accent appear? More than 3, and each one must justify itself.
5. How many radii, greys and weights? Should be ≤ 2, ≤ 2 (text) and ≤ 3.
6. Do all numbers agree across screens?
7. Is there a line of copy that would fit any app? If so, rewrite it.
