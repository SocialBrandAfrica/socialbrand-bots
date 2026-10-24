---
name: token-cop-stocktake
description: >-
  Morning measurement, forecast, classification and proposed plan for every
  declared platform.
---
# stocktake
## Inputs
Declared platforms, measurement methods, thresholds, last ledger readings, current time.
## Steps
1. Measure each platform (OCR, API, paste or estimate). Record confidence and source.
   - OCR: upscale the screenshot about 3x in greyscale first.
   - Cross-check each OCR figure against the page text the browser read. If they disagree, use the page read and flag the OCR miss.
   - Sign-in screen: do not guess. Mark the platform "not measured".
   - Use an owner paste if one exists, at low confidence. Flag the sign-in for the owner.
   - Shared pool (for example Cursor billed through the Grok account): measure once and report one row.
2. Calculate burn rate from two readings 6–24 h apart.
   - With one reading, estimate burn as % used ÷ time since the last reset. Confidence is medium at best. Say so.
   - Forecast days to limit.
3. Assign red, amber or green from the thresholds. Show 🔴, 🟡 or 🟢 in the status column.
   - Judge prepaid credits with no reset by balance and burn, not by %.
4. Classify open or proposed work: keep, pause, reprioritise, diarize, delegate down, escalate up or scrap. Give a one-line reason for each.
5. Name "Today's best model for ad hoc work and testing" (capacity first).
6. Propose the day's plan.
   - Include the daily burn target that makes each pool last to its reset.
   - Offer lettered options A–E (2 to 5), one line each. Put the recommended plan first and mark it "(recommended)". A bare letter approves that option.
   - Wait for the owner's yes or letter before any change.
7. Hand off to the prompt-pack skill.
## Output
- Status table, forecast, proposed plan, then wait for yes. Ledger entries written.
- Bullets plus 1 or 2 icons, varied each day.
- No emoji in warnings, approvals, money amounts or errors.
- Short sentences, one idea each. Calm and factual.
## Limits
Never act without a yes. Never invent numbers. Flag glitches, including a small overage above a hard cap. Finance is human-only.
