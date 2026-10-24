# Token Cop

Version 0.3.2 · Category DEV-AGENTS · Risk level: Low

## What it does
Token Cop helps you avoid hitting your AI usage limits too early.

- It reads your usage pages each morning.
- It forecasts how many days are left before each limit.
- It marks each platform green, amber or red.
- It names the best model for one-off work today.
- It proposes a plan for the day. You approve it or not.
- It writes a Morning Prompt Pack: one ready-to-paste briefing per AI tool. You paste them. Token Cop never sends them.
- It keeps a local log of every reading.

It proposes. You decide. Nothing changes without your yes.

## Who it's for
- Owners who run several Grok Bots, routines and outside AI tools.
- Anyone on a shared usage pool or a monthly usage cap.
- Anyone who has found out about a limit only after hitting it.

## Install
Two routes:

- **Read and paste (main route):** open the bot page and copy the full text. https://bots.socialbrand.africa/bots/token-cop
- **One-click install:** https://x.ai/bot/kikx0ydzAGu5ogL2Hfato

Setup takes about 15 minutes, plus one-time sign-ins to your usage pages. See SETUP.md.

## Startup questions
Token Cop asks these in order on first run. Each choice uses lettered options. You can reply with just the letter, or several letters where more than one applies.

1. **Bot email.** Confirm or claim the bot's email address, and say which tasks it may use it for. It only reads notices with it.
2. **Your subscriptions** (pick all that apply):
   - A. Grok (Premium, Super or Ultra)
   - B. Claude Max (5x or 20x)
   - C. Cursor
   - D. fal.ai
   - E. Other (OpenAI, Gemini, OpenRouter, Anthropic API, xAI API, or something else)
3. **How to measure** (pick one or more):
   - A. Screenshot plus OCR (recommended)
   - B. API, where a normal key can read your limits
   - C. You paste the numbers
   - D. Estimate from activity
   - Tip: A plus C, or A plus D, works well.
4. **How strict:**
   - A. Balanced: propose a pause at red (recommended, the default)
   - B. Strict: propose a pause at amber
   - C. Loose: alert only
5. **Who approves pauses and hand-offs:**
   - A. You only (recommended, the default)
   - B. You plus one named advisor bot
6. **Morning stocktake time** (Africa/Johannesburg by default):
   - A. 07:00 (recommended, the default)
   - B. 06:00
   - C. 08:00
   - D. Custom time
7. **Keys you already have.** List them. Token Cop only checks that a key file or vault entry exists. It never asks for the key itself.
8. **The work you do most:**
   - A. Ad-hoc testing
   - B. Ongoing projects
   - C. High-volume routines
   - D. Media generation
   - E. Mixed

After the answers you get a one-page summary. It lists the bot email, the platforms tracked, the method for each, the stocktake time and how to undo each choice.

## Routines
All times are Africa/Johannesburg. Each runs in a flexible window of about ±15 minutes.

| Routine | When | What it does |
|---|---|---|
| Health check | Daily 06:30 | Checks the last reading is under 36 hours old and the last OCR confidence was not low. Alerts only if something fails. |
| Morning Token Stocktake | Daily 07:00 (or the time you chose) | Measures each platform, forecasts, classifies work, proposes a plan, writes the Prompt Pack, then waits for your yes. |
| Weekly summary | Monday 08:00 | Sums up the week: burn, resets, status changes and open proposals. |
| Mid-week burn check | Wednesday 12:00 | Quick burn check. Alerts only if a platform has newly turned red. |

**All four routines ship paused.** Only you can unpause them.

To pause or resume one, ask Token Cop in chat. For example:
- "Unpause the morning stocktake"
- "Pause the weekly summary"
- "Move the stocktake to 08:00"

Token Cop confirms which routine and time before it changes anything.

## Skills
Six skills. Each name starts with `token-cop-`.

| Skill | What it does |
|---|---|
| token-cop-getting-started | Runs the startup questions, checks each usage page is signed in, checks OCR is installed, sets up the ledger and crop areas, and shows the companion card once. |
| token-cop-stocktake | Measures each platform, forecasts days to limit, assigns red, amber or green, classifies open work and proposes the day's plan. |
| token-cop-routing | Picks a model for a one-off task. Most spare capacity before its reset comes first, then the cheapest capable model. |
| token-cop-prompt-pack | Writes one ready-to-paste briefing per AI tool you use. |
| token-cop-ledger | Writes readings to the local ledger, works out burn rates and builds reports. |
| token-cop-delegation | Suggests handing work down to cheaper options or up to a stronger model or to you. Proposes only. |

## How work is classified
Each piece of open work gets one label and a one-line reason:
keep, pause, reprioritise, diarize, delegate down, escalate up or scrap.

## Status colours
Default thresholds. You can change them.

- **Green:** 40% or more left, and the forecast lasts more than one day past the reset.
- **Amber:** 15% to 40% left, or the forecast runs out within a day of the reset.
- **Red:** under 15% left, or already at the limit, or the monthly extra-usage cap is hit.

Prepaid credits with no reset are judged by balance and burn, not by percentage.

## Companion
Token Cop recommends **Grok Bot Setup Coach**: https://bots.socialbrand.africa/bots/grok-bot-setup-coach

- Setup Coach gets each new bot working in one sitting, with a backup.
- Token Cop shows its card once, at the end of the first-run setup.
- It recommends only. It never installs Setup Coach for you.

## Tone
Everyday tone.

- Long messages, like stocktakes and reports, use bullets plus 1 or 2 icons, for example 🟢🟡🔴 for status.
- Choices come as lettered options A to E, with the recommended one first.
- Short replies stay plain.
- No emoji in rules, warnings, approvals, money amounts or errors.
- The Prompt Pack has no emoji and no site link, because you send it to other tools.

## What it never does without your yes
- Pause, cancel, delete or change another bot's routine or work.
- Send any message outside this chat.
- Install, pause or hand off anything.
- Unpause its own routines.

## What it never does at all
- Contact customers or suppliers.
- Handle payments, banking, brokers, medical or legal actions. These are for humans only.
- Raise caps, buy credits or change billing. It can propose these. It never clicks.
- Ask for or store passwords, tokens, card numbers or ID numbers.
- Accept API keys in chat. If you paste one, it refuses and asks you to store it on the shared computer or in the vault.
- Upload raw screenshots. Screenshots stay local and are cropped to the usage numbers.
- Put your names into an export.

## More
- SETUP.md: first run and how to test it.
- FAQ.md: common questions.
- TROUBLESHOOTING.md: common failures and fixes.

By SocialBrand · socialbrand.africa · https://bots.socialbrand.africa
