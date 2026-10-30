# Token Cop troubleshooting

Version 0.7. These are the top failures from live testing, with fixes.

## 1. OCR is not installed
**Sign:** screenshot readings fail, or the setup check says OCR is missing.

**Fix:**
- Token Cop can install tesseract OCR on the shared computer.
- Setup checks for it. Re-run setup, or ask Token Cop to check OCR.

## 2. OCR misreads numbers
**Sign:** a figure looks wrong. OCR can return nothing, or a wrong digit, at normal screen resolution.

**Fix:**
- Token Cop enlarges each screenshot about 3 times, in greyscale, before OCR.
- It then checks every OCR figure against the page text read by the browser.
- If they disagree, it uses the page text and flags the OCR miss.
- If a number still looks wrong, paste the correct one. Token Cop records it as a paste.

## 3. A usage page shows a sign-in screen
**Sign:** the platform shows as "not measured", or a figure has low confidence from a paste.

**Fix:**
- Open the shared computer's browser and sign in to that page once.
- Ask Token Cop to take a new reading.
- Token Cop never asks for your password, and never guesses a missing number.

## 4. Cursor's page opens the Grok usage page
**Sign:** Cursor has no separate usage page. Its dashboard redirects to the Grok account page.

**Fix:**
- This is expected. Cursor and Grok share one pool.
- Token Cop tracks them as one row.
- If you see two rows for the same pool, ask Token Cop to merge them.

## 5. The forecast is only an estimate
**Sign:** the burn rate is marked as an estimate, with medium confidence or lower.

**Fix:**
- This happens when there is only one reading.
- Take a second reading 6 to 24 hours after the first. Ask in chat, or let the morning stocktake run.
- Two readings give a real burn rate.
- Some pages show the reset date but not the time. Days to reset is then approximate.

## Also: screenshots do not land in the screens folder
**Sign:** the browser saves a screenshot elsewhere, not in `/workspace/token-cop/screens/`.

**Fix:**
- Ask Token Cop to copy the screenshot from where the browser saved it into the screens folder.
- If a screenshot is missing, ask Token Cop to retake it.
- Screenshots stay on the shared computer either way.

## Still stuck?
- Check the routine is unpaused. All routines ship paused.
- The daily health check alerts you if the last reading is over 36 hours old or the last OCR confidence was low.
- Paste the numbers yourself as a fallback. Token Cop records them as a paste.
