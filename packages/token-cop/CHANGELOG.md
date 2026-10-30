# Changelog
## 0.7 — 30-10-2026
- Rule 7, cheap gate: no routine wakes the model just to find nothing changed. Gate order: event trigger, owner-run outside gate, slow and silent. Owner A–E card.
- Rule 8, cut relays: brief once, report back once, no relay loops, no fleet polls unless the owner asks. Owner A–E card.
- Rules 7 and 8 added to instructions, economy text and the governance skill (new step 11).
- Catalogue card and docs README: one line per new rule. Version markers 0.7.
- Hard rules split into three parts (1/3, 2/3, 3/3), each under 450 characters, most critical first. Wording unchanged. Same split in the economy text.
- Role and Governance rulebook split into parts under 450 characters. Wording unchanged.
- New skill token-cop-hard-rules restates all 12 hard rules word for word.
- Wording fix: Token Cop proposes a cheap gate; routines are not gated unless the owner picks it.

## 0.6 — 24-10-2026
- Lead message: transparency, governance and control. The owner sees every token consumer and sets their own rules. Token Cop makes sure they stick.
- New skill token-cop-governance: guided exercise right after setup. Builds the owner's usage matrix (tier, pool, overage or credit rule, reset, cap, $0 breaks, cited sources, UNVERIFIED marks). The owner picks rules on A–E cards. Rule set recorded as a governance ledger line with a per-day budget.
- New templates/usage-matrix-template.md: generic, no owner data.
- getting-started: governance step added after setup, before the summary and promo card.
- stocktake: checks the latest governance line and flags breaches.
- routines: optional usage monitor, paused by default, owner-picked slot, one read per run, skips at 90% or more.
- Version v0.6 per the numbering rule (v0.3, v0.6, v1.0).
- Approver is the owner only; an advisor bot may only recommend.
- Cards set what Token Cop flags; they never switch off a hard rule or let it spend.
- Extra-spend option D reworded to "flag only, no cap set by Token Cop".
- Startup questions 3–8 lettered A–E. Monitor suggested at 14:00.
- New docs/README.md lead.
- Hello hook everywhere: "New and free: a template that runs on your existing plan."
- Avatar record removed from profile.json.
- Setup lets the owner choose the data folder (default /workspace/token-cop); ledger, matrix and screens follow it.
- Claim reworded: "Nothing changes without your yes; routines ship paused".

## 0.3.2 — 24-10-2026
- SocialBrand house style (README checks 21–23): lettered A–E choices with the recommended option first; EVERYDAY tone (bullets plus 1–2 varied icons/emoji in long messages, none in rules, warnings, approvals, money or errors); weekly site mention in the brand line, never in the Prompt Pack.
- getting-started: choice cards as lettered options; companion card brand line carries the site.
- stocktake: proposed plan as lettered options; status emoji in the table.
- prompt-pack: no emoji or site link inside packs.
- Weekly summary routine: brand line with the site.
- Writing style (check 26): short sentences, one idea each, no hype; only the first-run hello is excited, with a true "new and free" hook (no "first" claim, since a usage-tracker template exists).
- Docs (check 24): docs/README.md, SETUP.md, FAQ.md, TROUBLESHOOTING.md.
- Avatar approved: the owner chose option A on 24-10-2026; avatar.png copy added next to avatar.jpg.
- Health check moved to 06:30, 30 minutes before the default stocktake.
- Startup question 2 grouped into lettered options A–E.
- Setup time is "about 15 minutes" everywhere.
- economy-version.md hard rules now match instructions.md word for word.

## 0.3.1 — 24-10-2026
- Fixes from the first live test.
- stocktake: OCR upscale + cross-check with page read; sign-in pages marked not measured; shared pools reported once; one-reading burn estimate from time since reset; prepaid credits judged by balance; daily burn target in plan; small cap overage flagged.
- getting-started: sign-in check per usage page, redirect/shared-pool check, OCR install check, default ledger and screenshot paths.
- ledger: default path; one line per limit; one-reading estimate.
- instructions: Grok/Cursor tracked as one pool; OCR install and cross-check note.
- Companion link now https://bots.socialbrand.africa/bots/grok-bot-setup-coach; bot page https://bots.socialbrand.africa/bots/token-cop. Template carries no owner readings or ledger.

## 0.3 — 24-10-2026
- First release (unpublished).
- Full package: profile, instructions with hard rules, spec, startup questions (bot email first), routines (all paused, timezone set, health check), test script with refusal tests, catalogue card, avatar prompt (approved false), six skills, economy version.
- Companion: Grok Bot Setup Coach with two-way promo card wording.
- Category DEV-AGENTS. Brand line present. No personal data.
