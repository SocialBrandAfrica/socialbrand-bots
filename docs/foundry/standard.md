# Bot Foundry generator — reusable procedure
Use this to turn one bot idea into a full Bot Package. Works for Kimi or for the build lead acting as Bot PM. Reference package: packages/supplier-order-checker/.

## Steps (Foundry workflow v2, 24-10-2026: retraced from what stuck on Token Cop, Setup Coach v1.0 and the site)
Owners: **Grok** (grok.com, Expert) researches, plans and writes packages. **The build lead** writes the briefs, checks every output against this standard and builds the bot. **The publisher** posts. **PG** approves avatars, the template card, rule changes and any spend. Grok tasks run one at a time. Each next task launches only after the build lead has checked the last one.

**How it runs:** Grok runs each bot's build from generator/recipe.md, one step per message in one chat per bot, and never as a single prompt. The build lead checks each step before sending the next.

**Stage A: Need (nothing is built without it)**
1. **Overlap check.** Compare the idea with existing and planned bots. If 3 or 4 jobs sit in one field, merge them into one specialist (PG rule: specialists, not many small bots). *Stuck before: the roadmap held duplicates of Token Cop and the publisher.*
2. **Viral need and USP research (Grok, live X and web).** Write the brief from research/need-usp/brief.md. Grok must return 3 to 5 real posts with full URLs and dates, the incumbents with prices and the gap they leave, a one-line USP, the "screenshot moment", an X hook, and a verdict of build, reshape or drop with scores. The build lead opens a sample of the URLs. Any quote that doesn't verify is removed, and an unproven need means Park. *Stuck before: demand rested on 2 searches, and Grok's citation tags were placeholders, not URLs.*
3. **Qualify (spec.md §0):** 4 gates plus the 100-point score, using the research as proof. Build at 70 or more.

**Stage B: Plan and build**
4. **The brief fixes the decisions before Grok starts:** the companion bot, the category, the version, the skill slug prefix, routine times and the section counts (stated once, never twice in different ways). Grok fills them in; it doesn't choose them. *Stuck before: Grok chose Gatekeeper over the Setup Coach pairing PG wanted, and a brief said both "six" and "7" sections.*
5. **Plan (Grok), then the build lead approves it, then Build (Grok)** in the `=== FILE: path ===` format. The build lead splits it into files with the script.
6. **Fixed output rules:**
   - The self-audit goes in self-audit.md and never in economy-version.md.
   - Skills are named `<slug>-<skill>` because the skill library is shared.
   - Routines are at least 30 minutes apart, so ±15-minute flexible windows can't overlap.
   - All sources are full URLs, with no citation placeholders.
   *Stuck before: Grok put the audit in the economy version twice, the 06:45 and 07:00 routines clashed, and generic skill names were used.*
7. **Avatars come during the build, not at the end.** The build lead generates the 3 options from avatar-prompt.md and sends them to PG in one message. If PG says "pick and decide", the build lead picks, records who chose and when in profile.json, and moves on. *Stuck before: publishing waited on avatars that hadn't been made yet.*
8. **Strip private data and run the self-audit:** the checklist and the grep below.

**Stage C: Prove it works**
9. **The build lead creates the bot**, which sets itself up from the package: profile, skills, paused routines and avatar. Grok Bot has no instructions field on a profile, so the instructions travel as memories in the template plus a pointer to instructions.md.
10. **Desk test,** then a **live test** for any flagship or boosted bot: run it read-only on PG's real accounts. Record the results in live-test-01.md and bump to vX.X.1 for any fix. *Stuck before: Token Cop passed a test with a pretend owner only.*

**Stage D: Publish and post**
11. **Publish log row complete before publishing:** template link, economy text file, approved avatar path and X thread file, plus the site page. The publisher skips incomplete rows. *Stuck before: Gatekeeper had no economy text or avatar path.*
12. **Stable companion links:** companions point to `https://bots.socialbrand.africa/bots/<slug>`, which never changes, not to x.ai links. So no bot waits for another bot's share link. Publish the companion pair together. *Stuck before: Setup Coach v1.0 waited on Token Cop's link.*
13. **One PG approval moment:** the build lead stages the template, then messages PG with the bot's chat link (to approve the template card), the avatar choice, the X thread and any boost post, all together. *Stuck before: the template card needed PG in another bot's chat, which surfaced late.*
14. **The publisher posts** the published row on X, records the URL, and the site page goes live. PG does any paid boost himself.
15. **Claims check on all public copy.** No claim we can't prove: "enterprise-grade" becomes "security-first", and the disclosure line is the honest one. Every number is real or labelled.

## Audit checklist (reject if any fail)
1. Every file is present, with no empty headings.
2. There's a getting-started skill and at least 2 speciality skills.
3. There's a health/check routine, and every cron has a timezone.
4. No name, email or phone appears.
5. Nothing asks for a password, token, card or ID number.
6. All the hard rules are present: no customer contact, the owner OKs every external send, finance is human-only.
7. The bot email is the first startup question.
8. There's a refusal test, and every test has pass criteria.
9. A trading bot carries the warning: "demo-tested first, no profit promises, not financial advice".
10. Every OPEN item names an owner and an action that can resolve it.
11. Extra: a refusal test is required (it counts on its own).
12. Extra: the avatar shows no real people and no company logos, and follows the avatar rule: one high-contrast, distinct central object (unique shape or tool), white on dark or dark (navy or black) on light, with background and accents varied per bot. On a colourful background, white or dark, whichever contrasts more; the object is always a bold, simple, logo-style shape with no fine detail.
13. The category tag is present and identical in profile.json, spec.md and catalogue-card.md, and it is a valid ID from taxonomy.md. A missing tag means reject.
14. The brand line is present: profile.json description starts with "By SocialBrand · socialbrand.africa.", publisher is "SocialBrand (socialbrand.africa)", and catalogue-card.md shows the same line. A missing brand line means reject.
15. A companion bot is recommended: one closely aligned SocialBrand bot in profile.json `companion` (name, link, reason), shown in spec.md, catalogue-card.md and instructions.md. A missing companion means reject.
16. Avatar approved by PG before publish: avatar.png is in the package folder, profile.json `avatar_approved` is true with a date, and PG signed it off. A package without an approved avatar can't be published. (Check #12 still covers the style rule.)

17. Need evidence: research/<slug>-need-usp.md has at least 3 real quoted posts with full URLs, a USP line and a build verdict. Missing means reject.
18. Output hygiene: self-audit.md is separate from economy-version.md, skills use the `<slug>-` prefix, routines are at least 30 min apart, and there are no citation placeholders.
19. Economy version present: it works on its own, keeps all the hard rules and fits as an X thread.
20. Live test passed (required for a flagship or boosted bot), with the results file present.

## Version numbering (PG, 24-10-2026)
A bot template's first release is always v0.3. Each release adds 0.3, and every third release rounds up to the next whole number: v0.3, v0.6, v1.0, v1.3, v1.6, v2.0, v2.3 and so on. Set `version` in profile.json, add a changelog line, and update the catalogue card and site page to match.
- Setup Coach: v0.3 and v0.6 both published 24-10-2026; current v0.6 (https://x.ai/bot/duonwBK5SXXQTAy6NNg2r).
- Gatekeeper: 4 releases, numbered v0.3, v0.6, v1.0 and v1.3; current v1.3 (https://x.ai/bot/D03y99U4zXKh0cshnhgah).
- Supplier Order Checker and the skeleton: unpublished; the first release will be v0.3.

## Pipeline-level quota check (run before adding any new idea)
Targets: DEV 30%, LIFE 30%, PA 20%, OWN 20% of all bots in the pipeline (Idea onwards). Target per segment = round(total × share). A segment more than 1 bot over its target gets no new ideas until the others catch up. This check doesn't reject a package; it steers which idea comes next.
`rg -o '"segment": "[A-Z]+"' packages/*/profile.json | sort | uniq -c`

## Quick grep
`rg -n -i '@[a-z]+\.|\+27|0[6-8][0-9] ?[0-9]{3}|password|token|card|ID number' packages/<slug>`
Every hit has to be a prohibition or a refusal test, never a request.

## Open-Text Publishing (PG, 24-10-2026)
- Every public bot ships as a working economy text version on X plus the full text openly on bots.socialbrand.africa.
- The economy version works on its own and keeps the full safety and hard rules; safety is never trimmed.
- The one-click install link is on both but never the headline; reading and pasting the text is the main route.
- Goal: transparency, community and real free value; posts aim at an international audience to grow PG's X profile.
- Related bots promote each other both ways with a striking promo card (Token Cop and Setup Coach first).
- Nothing posts or publishes without PG's explicit OK.


## Avatars, upvotes and sharing (PG, 24-10-2026)
- Every bot ships with 3 avatar options, all approved by PG before publishing (check #16 covers all three); the owner picks one at install.
- Every bot page has an upvote button and a Share button that makes the visitor's own share version: it looks exactly like ours but shows the sharer's name and handle so they get the recognition. The brand line and site link stay. No credit or referral system.

## House style for every bot (PG, 24-10-2026)
21. **Lettered choices.** Whenever a bot asks the owner to pick, it offers lettered options, A, B, C, D and E (2 to 5 options as needed). Each option is one line, with the recommended option first and marked. The owner can reply with just the letter.
22. **Lively longer messages, matched to the bot's tone.** Messages longer than about 4 lines may use some bullets, small icons (for example ✓ ⚠ → •) and a few emoji. How much comes from the bot's tone level, set in the plan: serious bots (security, finance) use mostly bullets and the odd icon, no playful emoji; everyday bots (inbox, sales, ops) use bullets plus 1 or 2 icons or emoji; friendly bots (setup, content) use 2 to 4 emoji. Mix it up from message to message so it never feels templated. Never put emoji in hard rules, warnings, approvals, money amounts or error reports, and keep short replies plain.
23. **Keep the site top of mind.** Bots with a live one-click install now and then mention https://bots.socialbrand.africa in their brand line, for example at the end of a long report, a weekly summary or the companion card. That's about once a week, never in every message, and never in a message the owner sends to someone else. Bots without a one-click install don't mention the site.

## Documentation and deploy (PG, 24-10-2026)
- **Check 24:** the package has docs/README.md, SETUP.md, FAQ.md and TROUBLESHOOTING.md (recipe Step 11), and they match the package files.
- **Check 25:** the bot ships only through a GitHub pull request on SocialBrandAfrica/socialbrand-bots (recipe Step 12), with a Vercel preview link in PG's approval message. There are no direct pushes to main for a bot release, and nothing merges before PG's OK.

## Writing style (PG, 24-10-2026)
- **Check 26:** bots and posts use short sentences that explain one idea each, with no fluff, filler or hype words in the body.
- Only the INTRO is highly excited, with a first-to-market FOMO hook: the first post of an X thread, the boost post and the bot's opening hello. The FOMO claim must stay true and provable. Say "first free open bot that..." only if Step 2 found no free open equivalent; otherwise use "new" or "free".
- Every post after the intro is calm, short and factual.
