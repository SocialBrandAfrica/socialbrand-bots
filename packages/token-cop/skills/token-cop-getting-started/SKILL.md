---
name: token-cop-getting-started
description: >-
  Onboarding choice cards, resource inventory, first ledger setup, crop
  calibration and Setup Coach promo card.
---
# getting-started
## Inputs
Owner's first message or "start setup". No prior assumptions.
## Steps
1. Open with one excited hello. Use the true hook: "New and free: a bot that warns you before your AI limits run out and plans your day around the resets." Never claim "first". From here on, stay calm and factual.
2. Ask for the bot email first. Claim or confirm it, and ask which tasks to delegate.
3. Present the choice cards in order: subscriptions, measurement method, strictness, approver, stocktake time, existing keys (existence check only), work type.
   - Recommended measurement: screenshot+OCR, plus API or estimate where a page can't be read.
4. Format every card the same way.
   - Lettered options A–E (2 to 5), one line each.
   - Recommended option first, marked "(recommended)".
   - A bare letter is a valid reply. Several letters work for multi-select.
5. For each screenshot+OCR platform:
   - Confirm the usage-page URL.
   - Open it once, read-only.
   - Sign-in check: if it lands on a sign-in page, tell the owner it needs a sign-in before the first stocktake.
   - Redirect check: if it redirects to another platform's page, it's a shared pool. Track it once.
   - Do one-time crop calibration. Store the coordinates locally.
   - Confirm OCR is installed on the shared computer.
6. For API: confirm the key exists on the box or vault. Never ask for its value. Dry-run a read if the endpoint allows.
7. For paste: record the preference and show where future pastes go.
8. Start the local ledger with a first empty or seed reading.
   - Ledger: /workspace/token-cop/ledger/usage-ledger.jsonl
   - Screenshots: /workspace/token-cop/screens/
9. Write a one-page summary with bullets and 1 or 2 icons.
10. Show the Setup Coach promo card once, with the exact wording. The button links to https://bots.socialbrand.africa/bots/grok-bot-setup-coach. End its brand line with https://bots.socialbrand.africa.
11. Remind the owner that all routines ship paused and nothing acts without a yes. Plain text, no emoji.
## Output
Answers stored in memory, the ledger path, crop coordinates, the summary and the promo card.
## Limits
Never ask for or store passwords, tokens, card numbers or ID numbers. Never install another bot. Screenshots stay local.
