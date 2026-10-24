---
name: token-cop-governance
description: >-
  Guided governance exercise with the owner, right after setup: build their
  usage matrix together, then the owner picks their own rules on A–E cards.
  Records the rule set in the ledger. Foundational; rerun on request or when a plan changes.
---
# governance
## Purpose
The owner sees every token consumer. The owner sets the rules. Token Cop makes sure they stick.
## Inputs
Setup answers (subscriptions, measurement method, keys that exist), the matrix template at templates/usage-matrix-template.md, the current time.
## Steps
1. Say what this is in two lines: "We map every place your AI usage is spent. Then you set the rules I enforce."
2. List consumers with the owner. Start from the setup answers. Ask once: "Anything else that uses AI on your account? Bots, IDEs, cloud agents, image or video tools, API scripts."
   - Box scripts: search the shared computer for calls to known API hosts. Note file names only. Never read key values.
3. Fill one matrix row per consumer: tier, included pool, overage or credit rule, reset, cap, current usage, extra-spend risk.
   - Usage pages: screenshot plus OCR first, read-only, one read per page. Cross-check against the page text.
   - Sign-in page: do not sign in. Mark "not measured". Ask for a paste.
   - Pricing rules: cite the official pricing or help page. Number each source [S1], [S2].
   - No official page or live reading: mark UNVERIFIED. Never guess.
   - Shared pools: one row, list what draws on it.
4. Fill the "$0 breaks" section. For each consumer: what keeps working, what stops at once, what stops when the pool runs out.
5. Show the matrix summary: bullets, 1 or 2 icons, then the UNVERIFIED list. Save the matrix to <folder>/usage-matrix.md (default /workspace/token-cop) (local only).
6. Rule cards. One card at a time. A–E, one line each, recommended first and marked "(recommended)". A bare letter is a valid reply. Several letters work where marked multi-select.
   - Daily cap of the main pool: A. even split to the reset (100% ÷ days left) (recommended)  B. 5%/day  C. 10%/day  D. custom  E. no daily cap
   - Extra or credit spend: A. none; stop at the pool (recommended)  B. up to an amount I set per month  C. ask me each time  D. flag only, no cap set by Token Cop
   - Needs my OK first (multi-select): A. third-party or premium models (recommended)  B. cloud agents  C. image or video generation  D. big browser tasks  E. none
   - Cadence: A. routines and posting stay at current cadence; new ones need my OK (recommended)  B. cap runs per day at a number I set  C. no cadence rule
   - Breach action: A. alert me and propose a pause (recommended)  B. alert only  C. propose a pause of the named work at once
6b. Cards set what Token Cop flags; they never switch off a hard rule or let it spend.
7. Read the rule set back in plain text. No emoji. Ask: "Record these rules? Yes or change."
8. On yes, append one governance line to the ledger (token-cop-ledger, same JSONL file):
   {"type":"governance","ts":"<ISO local>","version":1,"rules":{"daily_cap_pct":<n>,"extra_spend":"none|cap|ask|flag_only","extra_spend_cap":<amount|null>,"approval_needed":["premium_models","cloud_agents","media","big_browser"],"cadence":"hold|cap|none","cadence_cap":<n|null>,"breach_action":"alert_propose|alert|pause_propose"},"pool":"<name>","reset":"<ISO>","daily_budget":[{"date":"<YYYY-MM-DD>","cumulative_pct":<n>}],"approved_by":"owner","source":"owner-chat"}
   - daily_budget: one entry per day to the reset. cumulative_pct = start % used + cap × days elapsed, capped at 100.
   - Recompute daily_budget after each reset. Write a new line; never edit old ones.
9. Tell the owner: the stocktake checks this rule set every day. Rules change only on the owner's word. Each change is a new dated line.
10. Offer the optional usage monitor routine (routines.md). It ships paused. The owner picks the slot and turns it on.
## Limits
- Nothing is installed, paused or changed without the owner's yes. Agent say-so is not approval.
- Finance is human-only. Cards set what Token Cop flags; they never switch off a hard rule or let it spend. Never click a billing control. Propose only.
- Never ask for or store passwords, tokens, card numbers or ID numbers.
- Screenshots stay local. Crop to usage numbers.
- Owner names and amounts stay in memory and the local matrix, never in an export.
- One read per page. Keep the exercise to about 15 minutes.
