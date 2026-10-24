# SocialBrand Bots: PM pack for PM
Updated 24-10-2026, 09:30 SAST (UTC+2). Compiled by the build lead from the Foundry files in `bot-foundry/`. Only facts from those files are used. Anything not found there is marked UNKNOWN.

**Your job (PM):** update the business plan to v3 for the whole bots site and the bot rollout. Use this pack as the single source of facts. Return a structured plan with every workstream marked done, in progress, blocked, deployed or planned, each with an owner and a next action. The plan lands in GitHub at `docs/business-plan/` in https://github.com/SocialBrandAfrica/socialbrand-bots. The machine-readable status lives in `docs/pm/status.json`.

Roles: **PG** (the owner) decides and approves. **The build lead** (chief-of-staff bot) writes briefs, checks every output and builds bots. **Grok** (grok.com, Expert) researches, plans and writes packages, one step per message. **The publisher** (publisher bot) posts published rows on X (@Soc_Bran_Africa).

---

## 1. Mission and model
Source: `site/brand-manifesto.md`, `generator/README.md`.

- **AI agents for work.** Each agent does one niche task and runs routines or loops. Economy first, no compromise on quality. Connected to the tools people already use. Shared with the community, free.
- Every agent: Analyze, Flag, Automate, Act, Coordinate, Learn.
- It proposes, the owner approves, every time. The owner decides access and who may ask it to act.
- "Security-first" is used in public copy, not "enterprise-grade", until there is a certification or audit.
- **Open-Text Publishing:** every public bot ships as a working economy text on X plus the full text on bots.socialbrand.africa. Safety is never trimmed. The one-click install link is on both but never the headline.
- **Specialists, not many small bots:** 3-4 jobs in one field merge into one specialist.
- **Companions:** related bots recommend each other both ways (recommend only, never installed for you). Links point to stable site pages `https://bots.socialbrand.africa/bots/<slug>`.
- **3 avatar options per bot**, approved by PG before publish.
- **Upvote and Share** on every bot page. Share makes the visitor's own card with their name and handle. No credit or referral system for sharing.
- **Monetisation:** disclosed referral/affiliate links only (see section 7). There are no referral links live yet.
- **Versioning:** first release v0.3, then +0.3, every third rounds up: v0.3, v0.6, v1.0, v1.3, v1.6, v2.0. Fix releases use vX.X.1.

## 2. The bot standard (checks 1-26, brief)
Source: `generator/README.md` (full copy in `docs/foundry/standard.md`).

1. Every file present, no empty headings.
2. Getting-started skill plus 2+ speciality skills.
3. A health-check routine; every cron has a timezone.
4. No name, email or phone.
5. Nothing asks for a password, token, card or ID number.
6. All hard rules: no customer contact, owner OKs every external send, finance is human-only.
7. Bot email is the first startup question.
8. A refusal test; every test has pass criteria.
9. A trading bot carries the "demo-tested first, no profit promises, not financial advice" warning.
10. Every OPEN item names an owner and an action.
11. Refusal test counts on its own.
12. Avatar rule: no real people or logos; one bold high-contrast object.
13. Category tag identical in profile.json, spec.md, catalogue-card.md and valid in taxonomy.md.
14. Brand line "By SocialBrand · socialbrand.africa." and publisher "SocialBrand (socialbrand.africa)".
15. One companion bot named in profile, spec, card and instructions.
16. Avatar approved by PG with a date before publish.
17. Need evidence: 3+ real quoted posts with full URLs, a USP and a build verdict.
18. Output hygiene: self-audit separate from economy text, `<slug>-` skill prefix, routines 30+ min apart, no citation placeholders.
19. Economy version works alone, keeps all hard rules, fits an X thread.
20. Live test passed for a flagship or boosted bot.
21. Lettered A-E choices, recommended option first.
22. Longer messages use bullets, icons and emoji matched to tone (serious, everyday, friendly). None in rules, warnings, approvals, money or errors.
23. Bots with a live one-click install mention https://bots.socialbrand.africa about once a week.
24. Docs: docs/README.md, SETUP.md, FAQ.md, TROUBLESHOOTING.md matching the package.
25. Ships only through a GitHub pull request with a Vercel preview link; nothing merges before PG's OK.
26. Short sentences, one idea each, no fluff. Only the intro (thread post 1, boost post, opening hello) is excited, with a true first-to-market hook.

## 3. The recipe (Steps 0-12)
Source: `generator/recipe.md` (full copy in `docs/foundry/recipe.md`). One Grok chat per bot, one step per message, never a single prompt. The build lead checks each step before the next.

- **Step 0 Kick-off:** Grok restates the job and the fixed decisions (companion, category, v0.3, prefix, timezone, routine times).
- **Step 1 Overlap:** overlapping bots and whether to merge into one specialist.
- **Step 2 Need and USP:** 3-5 real posts with URLs, incumbents and prices, USP, hook, verdict with scores. The build lead opens 3+ URLs.
- **Step 3 Qualify:** 4 gates and the 100-point score; 70+ to build.
- **Step 4 Plan:** jobs, getting-started, skills, paused routines, hard rules, tone level, tests. The build lead approves.
- **Step 5 Files 1:** profile.json, instructions.md, startup-questions.md, routines.md.
- **Step 6 Files 2:** every skills/<slug>-<skill>/SKILL.md.
- **Step 7 Files 3:** catalogue-card.md, test-script.md, avatar-prompt.md (3 options), CHANGELOG.md.
- **Step 8 Economy version:** self-contained, all hard rules, X-thread sized.
- **Step 9 Self-audit:** all checks and the grep, PASS/FAIL with evidence.
- **Step 10 Launch kit:** X thread, boost post with 3 hooks, bot page copy.
- **Step 11 Documentation:** README, SETUP, FAQ (8+), TROUBLESHOOTING (5).
- **Step 12 Deploy via GitHub (build lead):** branch bot/<slug>-v<version>, PR with checks and Vercel preview, PG OK, merge, template card click, install link into config, the publisher posts.

## 4. Site facts
- **URL:** https://bots.socialbrand.africa (live 24-10-2026, Valid Configuration on Vercel).
- **Vercel project:** socialbrand-bots (team socialbrandafricas-projects). Auto-deploys `main`. Each PR gets a preview link.
- **GitHub repo:** https://github.com/SocialBrandAfrica/socialbrand-bots (public).
- **Stack:** static HTML, CSS and JS. No backend, no cookies, no tracking. Upvotes in the visitor's browser only (localStorage).
- **Rebuild:** `python3 site/build/build.py` regenerates `site/live` (index, about, bots/*, sitemap.xml, robots.txt, vercel.json). Then commit and push in `site/live`. Push to main deploys. `site/build/test.py` needs playwright, which is not installed.
- **Install links:** one place only, `assets/js/config.js` (`installLinks`). Empty string shows "Install link coming soon".
- **Pages that exist:** `/`, `/about`, and bot pages:

| Page | Install link in config |
|---|---|
| /bots/token-cop | https://x.ai/bot/kikx0ydzAGu5ogL2Hfato |
| /bots/grok-bot-setup-coach | https://x.ai/bot/duonwBK5SXXQTAy6NNg2r |
| /bots/gatekeeper | https://x.ai/bot/D03y99U4zXKh0cshnhgah |
| /bots/supplier-order-checker | empty (coming soon) |

- **Known stale items on the live site:** build.py lists Gatekeeper as v1.3 and Setup Coach as v1.0 "live" while the published template link is still v0.6. The About page says "16 checks before publishing" (the standard now has 26). The "Coming soon" badge overlap on the mockup is unfixed.
- **Not built yet (from the PM plan):** analytics events, affiliate disclosure / "How we make money" page, `/go/<service>` referral redirects, public publish log, standard page, contribute form.
- **docs/** in the repo holds this pack, the standard, the recipe and status. It is excluded from Vercel deploys by `.vercelignore`.

## 5. Bots
Sources: `publish-log.md`, `STATUS-24-10-2026.md`, `batch-01/batch.md`, `packages/*/profile.json`, `packages/*/CHANGELOG.md`.

| Bot | Category | Live version (template) | Staged version | Status | Template link | Avatar | X post | Companion |
|---|---|---|---|---|---|---|---|---|
| Token Cop (flagship) | DEV-AGENTS | v0.3.1 published 24-10-2026 | v0.3.2 (house style, writing style, docs) | 0.3.2 card waits on PG click in Token Cop chat | https://x.ai/bot/kikx0ydzAGu5ogL2Hfato | A chosen 24-10-2026 (avatars/A.jpg); B and C exist | Thread rewritten (11 posts, `x-posts/02-token-cop.txt`), held by the publisher until PG OKs; boost drafts in `x-posts/token-cop-boost.md` (PG pays) | Grok Bot Setup Coach |
| Grok Bot Setup Coach | PA-DESK | v0.6 published 24-10-2026 | v1.0 (template v4, house style, docs) | Card waits on PG click in Setup Coach chat | https://x.ai/bot/duonwBK5SXXQTAy6NNg2r | A approved by PG 24-10-2026; B and C need PG approval | Draft `x-posts/03-setup-coach.txt`, pending | Token Cop (v1.0); Gatekeeper secondary |
| Gatekeeper by SocialBrand | DEV-AGENTS | v1.3 | v1.4 (template v4, house style, docs, restored "No customer or supplier contact") | Card waits on PG click in Gatekeeper chat | https://x.ai/bot/D03y99U4zXKh0cshnhgah | avatar.png navy shield; confirm it is the one set (UNKNOWN); B/C options UNKNOWN | Draft `x-posts/04-gatekeeper.txt`, not posted; economy text written, PG to OK | Grok Bot Setup Coach (main), Token Cop (secondary) |
| Supplier Order Checker | OWN-OPS | none (unpublished) | v0.3 building | Building; open-text page on site with install "coming soon" | none | Not approved; 3 options still to make | none | Gatekeeper (interim) |
| Inbox Keeper (Batch 01) | PA-DESK | none | v0.3 | Recipe Step 5 of 12 (files part 1 written; re-saving with formatting). Score 88 (Grok 94, the build lead corrected), BUILD. Main rival: Inbox Zero | none | not started | none | Finance Clerk |
| Sales Pipeline (Batch 01) | OWN-GROWTH | none | v0.3 | Queued after Inbox Keeper | none | not started | none | Inbox Keeper |
| Finance Clerk (Batch 01) | OWN-OPS | none | v0.3 | Queued after Sales Pipeline | none | not started | none | Inbox Keeper |
| Publisher routine (internal) | UNKNOWN | internal, not a public template | - | Running, 5 checks a day; posts published rows from publish-log.md | - | - | Holding the Token Cop thread | - |

Batch 01 routines (all paused at install, Africa/Johannesburg): Inbox Keeper 07:00 daily triage, 16:30 weekdays follow-up check, Mon 08:00 health check. Sales Pipeline 08:30 weekdays nudge, Fri 14:00 review, Mon 09:00 health check. Finance Clerk 09:30 weekdays sweep, Fri 15:00 cash summary, 1st of month 10:00 health check. Batch 01 ends in one approval message to PG for all three.

Other X drafts: site launch thread `x-posts/01-site-launch.txt` (PG to OK). Images in `x-posts/img/` (1600x900 cards, boost 1600x900 and 1080x1080). Posting order: Token Cop, site launch, Gatekeeper, Setup Coach v1.0. Nothing has been posted.

## 6. Roadmap v2 and the PM plan's open decisions
Sources: `research/pm-plan/socialbrand-roadmap-v2-grok.md`, `research/pm-plan/socialbrand-bots-pm-plan-grok.md`.

**Roadmap v2: 6 field specialists** (replaces the fleet-tooling top 10; Usage Forecaster folded into Token Cop, Publish Checklist into the publisher):

| # | Specialist | Field | Jobs absorbed | Companion | Need research verdict |
|---|---|---|---|---|---|
| 1 | Inbox Keeper | Inbox and calendar | silent follow-up, meeting prep, timezone clash | Finance Clerk | Build (8/7/9) |
| 2 | Finance Clerk | Finance and admin | invoice chaser, expense sorter, SaaS audit, renewals | Inbox Keeper | Build (7/6/8) |
| 3 | Content Voice | Content and social | content gap, mention watch, newsletter, feedback digest | Sales Pipeline | Reshape (6/6/7) |
| 4 | Ops Flow | Ops and stock | stock watch, onboarding, PR nudge, issue labels | Supplier Order Checker | Build or reshape (6/5/7) |
| 5 | Sales Pipeline | Sales and CRM | lead follow-up, CRM cleanup, testimonials | Content Voice | Build (7/6/8) |
| 6 | Research Scout | Research | competitor watch, content research, signals | Token Cop | Build, lightweight (6/5/7) |

Scores are need / virality / fit out of 10 from `research/need-usp/need-usp-research-grok.md` (Token Cop: Build flagship 10/9/10). Roadmap v2 said build Inbox Keeper, Finance Clerk, Content Voice first. Batch 01 runs Inbox Keeper, Sales Pipeline, Finance Clerk instead (Content Voice was "Reshape"). Batch 01 companions differ from the roadmap map (Sales Pipeline points to Inbox Keeper, not Content Voice).

**PM plan headline (90 days to 22-01-2027):** site live and SEO-ready, 4 new bots plus Token Cop and Supplier Order Checker, grow PG's X internationally (+500 non-SA followers, assumption), affiliate tracking for 3 programmes. Weekly rhythm: Mon Grok review, Tue-Wed the build lead builds, Thu PG/Grok review, Fri the publisher posts. Cash burn year 1 under $500 (assumption). 12-month affiliate scenarios (all assumptions): low ~$1,650, base ~$6,750, high ~$20,250 gross.

**8 open decisions for PG (none answered in the files: status UNKNOWN):**
1. Affiliate priority order. Rec: n8n and Make first, then ElevenLabs, then Vercel if confirmed.
2. Site stack. Rec: static. (Built as static HTML on Vercel, so effectively decided.)
3. X frequency beyond publisher releases. Rec: 1 primary post a weekday plus replies; PG approves any increase.
4. Community start date. Rec: soft-launch an X Community at day 90 if metrics hit.
5. Disclosure wording. Build lead note: use the honest line "some links are referral links, and we say so next to them, with a plain link too", not "we only recommend what we use".
6. Next bot after the first four. Rec was Usage Forecaster; superseded by roadmap v2 (folded into Token Cop).
7. Public vs private publish log. Rec: public summary, full log internal.
8. Year 1 tools/hosting budget ceiling. Rec: under $500, re-check at day 90.

The build lead's check notes on the PM plan: the plan still says "16 checks" (now 26); partnerships and creator outreach are done by PG himself, never by a bot.

## 7. Monetisation and referral research
Sources: `research/monetisation/brief.md`, `research/monetisation/referral-research-grok.md`. PG's decision: the only monetisation is disclosed referral/affiliate links.

- **Real cash, confirmed:** ElevenLabs 22% for 12 months (PartnerStack), n8n 30% for 12 months on Cloud (PartnerStack, min ~EUR 100), Make 35% for 12 months (Wise, min $100 and 3 paying users).
- **Possible:** Vercel (affiliate terms exist; 25% recurring reported by third parties, unverified). Manus ~10% (unverified).
- **No cash programme:** Anthropic, OpenAI, xAI/Grok, Kimi, Gemini, Mistral, DeepSeek, OpenRouter, Perplexity (ended), Cursor (ended), fal.ai, Replicate, Together, Groq. Poe pays creators per message on their own bots, not referrals. Zapier unverified.
- **Top 5 by fit:** ElevenLabs, n8n, Make, Manus (verify first), Vercel.
- **Disclosure:** FTC (clear, next to the link), South Africa CPA / ARB (plainly identifiable marketing), X Paid Partnership toggle plus text. Always pair a referral link with the plain link.
- **Implementation idea:** central links.json and `bots.socialbrand.africa/go/<service>` redirects with click counts; public "How we make money" page. Not built.
- **Open for PG:** which programmes to join, which accounts, payout details (PG enters them himself), final disclosure wording, legal review.
- Note: Grok's research file still carries citation placeholders instead of URLs in several table rows.

## 8. Constraints
- **Shared usage allowance:** builds run one at a time to stay inside it.
- **PG approves** every publish, X post, boost, payment and rule change. An agent's approval never counts. Template cards are approved only by PG in that bot's own chat. Payments, banking and boosts are PG's own actions.
- **No customer contact by any bot.** Outreach to people (creators, partners) is PG's own action.
- Standing OK from PG: every publish is also posted on X (the publisher posts rows marked published).
- Dates DD-MM-YYYY, times SAST (UTC+2).
- No secrets, customer data or personal contacts in any public file.

## 9. Workstream status (24-10-2026)
Machine-readable copy: `docs/pm/status.json`.

| ID | Workstream | Area | Status | Owner | Blocked by | Next action |
|---|---|---|---|---|---|---|
| site-live | bots.socialbrand.africa live on Vercel | site | deployed | Build lead | - | Keep main green; deploy only via PR |
| site-stale | Site copy refresh (Gatekeeper v1.3 label, Setup Coach version, "16 checks" on About) | site | planned | Build lead | PG card clicks for v1.4 / v1.0 | Update build.py after the cards are approved, ship via PR |
| site-pages-3 | Site pages and docs for Token Cop 0.3.2, Setup Coach v1.0, Gatekeeper v1.4 | site | blocked | Build lead | Bots finishing docs, then PG card clicks | Open GitHub PR with Vercel preview; merge (PG OK given 24-10 09:03) |
| site-analytics | Privacy-friendly analytics events | site | planned | PM | PG decision on tool and budget | Propose tool and events in business plan v3 |
| site-disclosure | "How we make money" page and /go/<service> redirects | site | planned | PM | PG to join referral programmes and approve wording | Spec the page and links.json |
| site-test | Automated site test (build/test.py) | infra | blocked | Build lead | Test runner not set up yet | Set up the site test or drop it |
| tc-published | Token Cop v0.3.1 published | bot | deployed | PG | - | - |
| tc-032 | Token Cop v0.3.2 (house style, writing style, docs) | bot | blocked | Token Cop | PG card click in Token Cop chat | PG approves the card |
| tc-live-test | Token Cop live test (2nd reading) | bot | in_progress | Build lead | Partial: one provider reading still pending | Second reading around 14:00 SAST 24-10-2026 |
| sc-v10 | Grok Bot Setup Coach v1.0 | bot | blocked | Grok Bot Setup Coach | PG card click in Setup Coach chat | PG approves the card |
| gk-v14 | Gatekeeper v1.4 | bot | blocked | Gatekeeper by SocialBrand | PG card click in Gatekeeper chat | PG approves the card and economy text |
| gk-avatar | Gatekeeper avatar confirmation | bot | blocked | PG | PG to confirm the navy shield is the set avatar | PG confirms |
| soc-build | Supplier Order Checker v0.3 | bot | in_progress | Build lead | - | Finish build; make 3 avatar options for PG |
| batch-ik | Inbox Keeper v0.3 | batch | in_progress | PM | - | Re-save Step 5 with formatting; then Step 6 skills |
| batch-sp | Sales Pipeline v0.3 | batch | planned | PM | Inbox Keeper finishing | Start Step 0 after Inbox Keeper |
| batch-fc | Finance Clerk v0.3 | batch | planned | PM | Sales Pipeline finishing | Start Step 0 after Sales Pipeline |
| batch-approval | Batch 01 single approval message to PG | batch | planned | Build lead | All 3 bots ready | Send one message: cards, avatars, threads, preview links |
| x-tc-thread | Token Cop X thread | x | blocked | Publisher | PG OK on the rewritten thread | PG reads x-posts/02-token-cop.txt and says OK |
| x-tc-boost | Token Cop boost post | x | blocked | PG | Thread live first; PG pays and boosts | PG picks a variant and boosts |
| x-site-launch | Site launch thread | x | blocked | Publisher | PG OK | PG approves x-posts/01-site-launch.txt |
| x-gk | Gatekeeper back-post | x | blocked | Publisher | PG card click for v1.4 and PG OK | Post after approval |
| x-sc | Setup Coach v1.0 thread | x | blocked | Publisher | PG card click for v1.0 and PG OK | Post after approval |
| publisher | Publisher routine | x | done | Publisher | - | Works through publish-log.md 5 times a day |
| standard | Bot standard checks 1-26 and recipe Steps 0-12 | business | done | Build lead | - | PG approves any further rule change |
| companion-handoffs | Real working handoffs between companion pairs | business | blocked | PG | PG decision (currently cross-promotion only) | PG answers yes or no |
| referrals | Join referral programmes | business | blocked | PG | PG decision and sign-up (payout details are PG's) | PG picks programmes (rec: ElevenLabs, n8n, Make) |
| pm-decisions | PM plan open decisions 1-8 | business | blocked | PG | PG answers | PM folds answers into business plan v3 |
| bp-v3 | Business plan v3 (site + rollout) | business | in_progress | PM | - | PM writes v3 from this pack into docs/business-plan/ |
| social-scheduler | Social scheduler for LinkedIn, X, TikTok (PG-approved drafts only) | business | blocked | PG | PG scope and timing answers | PG answers scope questions |
| docs-repo | docs/ in GitHub (PM pack, standard, recipe, status) | infra | in_progress | Build lead | - | PR open; PG or the build lead merges after review |
