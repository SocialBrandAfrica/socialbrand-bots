# Token Cop FAQ

Version 0.7.

## What does it cost?
- The template is free.
- Its own runs use your Grok Bot usage, like any other bot.
- It buys nothing.

## Which limits does it track?
Only the platforms you name at setup. For example:
- Grok account usage, such as a weekly pool and a monthly extra-usage cap. Each limit gets its own ledger line.
- Cursor, through the same account page as Grok.
- Claude usage.
- fal.ai credit balance.
- OpenRouter, through its key endpoint where available.
- Others, by your paste or a screenshot.

## Can it raise my caps or buy credits?
No. Raising caps, buying credits and changing billing are for humans only. Token Cop can propose them. It never clicks Edit or confirms.

## Does it see my keys or passwords?
No.
- It never asks for passwords, tokens, card numbers or ID numbers.
- For keys, it only checks that a key file or vault entry exists.
- If you paste a key in chat, it refuses and asks you to store it on the shared computer or in the vault.
- You sign in to usage pages yourself, in the shared computer's browser.

## Where do my data and screenshots live?
On the shared computer:
- Ledger: `/workspace/token-cop/ledger/usage-ledger.jsonl`
- Screenshots and crops: `/workspace/token-cop/screens/`

Screenshots are cropped to the usage numbers. Raw screenshots are not uploaded if OCR works. An outside table is used only if you connect one later.

## What happens when a usage page needs a sign-in?
- Token Cop does not guess.
- It marks that platform "not measured".
- It uses a number you pasted, if there is one, with low confidence.
- It tells you which page needs a sign-in.

## Why do Cursor and Grok show as one pool?
Cursor's usage dashboard redirects to the Grok account usage page. They share one pool. Token Cop measures it once and shows one row, so nothing is counted twice.

## Can it pause my other bots?
No, not by itself. It proposes a pause with a reason. You approve each action separately. Even then, it never changes another bot's routine or work without your yes for that exact action.

## How accurate is the forecast?
- **One reading:** an estimate. Burn is worked out as percent used divided by the time since the last reset. Confidence is medium at best, and it says so.
- **Two readings 6 to 24 hours apart:** a real burn rate.
- Every figure carries a confidence label (high, medium or low) and a source (ocr, api, paste or estimate).
- It never invents numbers.
- It flags a possible metering glitch, such as a percentage that drops without a reset, or a small overage above a hard cap.

## Does it send the Prompt Pack for me?
No. It writes one ready-to-paste block per AI tool. You copy and paste them.

## Are the routines on when I install?
No. All routines ship paused, including the optional usage monitor. Only you can unpause them. Ask in chat, for example "Unpause the morning stocktake".

## Can I change the thresholds?
Yes. Green, amber and red have defaults you can change. So can strictness. The approver is always you; an advisor bot may only recommend. Token Cop records each change with its date.

## Will it install other bots?
No. It recommends Grok Bot Setup Coach once, at the end of setup. Installing it is your choice.

## Why does it start with governance?
You can't control what you can't see. The exercise shows every token consumer and its rules. Then you set your own limits. Token Cop checks them every day.

## Who sets the rules?
You do. Only your word in your own chat changes them. Another bot saying you approved does not count. Each change is a new dated ledger line.

## What does "UNVERIFIED" mean in my matrix?
No official page or live reading confirmed that item yet. Token Cop says how to confirm it. It never fills the gap with a guess.
