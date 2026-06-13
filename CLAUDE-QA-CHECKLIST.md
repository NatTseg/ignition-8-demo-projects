# Claude HMI Visual-QA Self-Checklist

A self-review checklist Claude runs **before declaring any Ignition Perspective
(or general dashboard/HMI) work "done."** It is phrased as questions to ask
*myself* while looking at a rendered screenshot of the actual page — not at the
JSON. **If I can't see it rendered, I haven't verified it.**

> Rule zero: **Always screenshot the real page and look at it.** Most of these
> defects are invisible in the view JSON and only show up in a render.

---

## 1. Spacing & padding

- [ ] Does every text element have breathing room — is there padding between text and the edge of its container/box? (No text touching a border.)
- [ ] Is there consistent padding *inside* cards/panels (e.g. 12–20px), not text jammed into the corner?
- [ ] Is there consistent spacing *between* sibling elements (gaps, not collisions, and not wildly uneven gaps)?
- [ ] Do KPI/stat cards have enough internal height that the number and its label aren't crammed together?
- [ ] Are icon + label pairs spaced so the icon isn't kissing the text?

## 2. Text not cramped / truncation

- [ ] Is any text clipped, cut off, or `…`-truncated when it shouldn't be?
- [ ] Does any label wrap awkwardly to a second line and overflow its box?
- [ ] Are long values (units, timestamps, names) given enough width, or do they collide with the next column?
- [ ] Is line-height comfortable (not lines stacked tight on top of each other)?
- [ ] Do numbers + units stay on one line where a break would look broken ("78.6\nMW")?

## 3. Overlap & occlusion

- [ ] Is any **text** overlapping other text or a shape so it's hard to read? (This is a defect.)
- [ ] **Exception:** overlapping *shapes* are fine and expected where intentional — e.g. SLD symbols sitting on bus lines, a status dot over a corner, a badge on a card. Overlap of *shapes* ≠ defect; overlap of *text* = defect.
- [ ] Do tooltips/popovers/legends sit on top of content without hiding the thing they describe?
- [ ] Does a scrollbar overlap content or clip the last row?

## 4. Contrast & legibility

- [ ] Is every piece of readable text clearly visible against its background? (On dark `#060B18`/`#0D1526`, secondary text must be **`#94A3B8` or lighter** — never `#475569`, which disappears.)
- [ ] Are muted/secondary labels still readable, not just barely-there?
- [ ] Do status colors (red/amber/green) remain distinguishable and not muddy on the chosen background?
- [ ] Is text over a colored fill (e.g. a progress bar, a colored badge) still legible?
- [ ] `#475569`-class colors are for *decorators only* (dividers, placeholders), not readable text.

## 5. Alignment & visual order

- [ ] Are columns of numbers/labels aligned to a consistent edge (left labels / right-aligned numerics where appropriate)?
- [ ] Do cards in a row share the same height and baseline?
- [ ] Are things that should line up actually on the same grid (no 1–3px drift)?
- [ ] Is the layout balanced — no large empty dead-zone next to a cramped cluster?

## 6. Sizing & responsiveness

- [ ] At the intended viewport width, does content fit without an unexpected horizontal scrollbar?
- [ ] Do flex rows have `overflow: hidden` + `flexShrink: 0` so each row doesn't grow its own scrollbar? (Known Perspective gotcha — the *list* scrolls, not the rows.)
- [ ] Do charts/canvases fill their allotted space rather than collapsing to 0 height or overflowing?
- [ ] Does nothing get comically stretched (a 16px icon blown up to 80px, a bird canvas distorted)?

## 7. Data, state & units

- [ ] Does every numeric value show its **unit** (MW, Hz, kV, %, m/s, °C)?
- [ ] Do status indicators clearly map to state (online/offline/maintenance) via both color *and* text/icon (not color alone)?
- [ ] Are timestamps in a consistent, readable format?
- [ ] Do progress bars / gauges visually match their numeric value (a "61%" bar is actually ~61% full)?
- [ ] Are placeholder/zero/no-data states handled (not a blank or a raw `null`/`NaN`)?

## 8. Consistency

- [ ] One color token system used throughout (same blue, same surface, same border) — no stray off-palette hex?
- [ ] Consistent corner radius, border weight, and shadow treatment across cards?
- [ ] Consistent typographic scale (a small set of sizes/weights, not a dozen)?
- [ ] Same component pattern reused for the same concept (all KPI cards look like siblings)?
- [ ] Navigation reflects the active page (active tab is visibly distinct)?

## 9. Interaction affordances

- [ ] Do clickable things look clickable (buttons/tabs/links visually distinct from static text)?
- [ ] Is the active/selected state visible (active time-range button, active nav tab)?
- [ ] Do "View all →"/drill-down links actually go somewhere and read as links?

## 10. SLD / single-line-diagram specific

- [ ] Are device symbols and labels spaced so labels don't overlap *each other* or sit unreadably on a line?
- [ ] Overlapping of symbols *onto* bus lines/connections is expected and fine — don't "fix" it.
- [ ] Is every drawn element electrically real (ANSI/IEC basis: 52 breaker, CT, PT/PR, PM, bus, transformer, ground)? **No decorative/hallucinated boxes** (e.g. an invented "switchgear enclosure") unless explicitly requested.
- [ ] Do connection lines actually connect (endpoints meet symbols, no floating stubs)?
- [ ] Is the legend complete for every symbol type used?

## 11. Domain accuracy (engineering)

- [ ] Are device numbers, CT ratios, voltage levels, and labels technically plausible?
- [ ] Do simulated/demo values stay in realistic ranges (frequency ~59.95–60.05 Hz, not 47 Hz)?
- [ ] No invented components, ratings, or relationships that a domain engineer would flag as wrong.

---

## How to use this

1. Build the page.
2. **Render it and screenshot it** (real browser / Playwright / the browser MCP) — at the intended viewport size.
3. Read the screenshot against each section above.
4. Fix what fails. Re-screenshot. Repeat until clean.
5. Only then report it as done — and say what was verified.

The single highest-value habit: **look at the rendered pixels, every time.**
