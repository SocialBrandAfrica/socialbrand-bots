# Bot creation recipe (run by the LLM project manager in steps)
PG rule (24-10-2026): one recipe per bot. It goes to the LLM that is project-managing the bot (Grok, Expert, on grok.com). It runs as **separate steps in one chat, never as a single prompt**. After each step Grok stops and waits. The build lead checks the output against generator/README.md, then sends either the next step or a fix-up message. Only one step is open at a time.

How to run it:
- Open one new Grok chat per bot and name it "Foundry: <Bot name>". Keep every step in that chat, so Grok carries its own context forward.
- Send STEP 0 with the recipe and the standard attached, then each next step as its own message.
- Save each step's output to packages/<slug>/steps/<NN>-<step>.md. If a step fails the build lead's check, send "FIX: <what failed>" and re-check before moving on.
- Every step ends with Grok's line "STEP <n> DONE. Waiting for the next step." If that line is missing, the step isn't finished.

---
## STEP 0: Kick-off (build lead sends; attach this recipe, generator/README.md, site/brand-manifesto.md)
"You are the project manager for one SocialBrand bot: <Bot name>. We'll work through the attached recipe one step at a time, in this chat. Do ONLY the step I send. Don't run ahead. End each step with 'STEP n DONE. Waiting for the next step.' Fixed decisions you must keep: companion <name> (link https://bots.socialbrand.africa/bots/<companion-slug>), category <ID>, version v0.3, skill prefix <slug>-, timezone Africa/Johannesburg, routine times <list, 30+ min apart>. Reply only with a one-paragraph restatement of the bot's job and the fixed decisions."
Check: the restatement matches; no extra work.

## STEP 1: Overlap and consolidation
"List every existing or planned SocialBrand bot (attached list) that overlaps with this one. Say whether we should merge 3-4 jobs into one specialist, and which jobs this bot absorbs. Table plus a one-line recommendation."
Check: no duplicate of an existing bot; the field is clear.

## STEP 2: Viral need and USP (live X and web search)
"Research the real need: 3-5 real posts with full URLs, dates and engagement; how loud the need is; 3-5 incumbents with prices and their gap; a one-sentence USP; the screenshot moment; an X hook under 120 characters; a verdict of build, reshape or drop with need, virality and fit scores out of 10. Only quote real posts."
Check: The build lead opens at least 3 URLs. A build verdict is needed to continue.

## STEP 3: Qualify
"Fill spec.md §0: 4 gates and the 100-point score (setup x4, differentiation x4, demand x4, frequency x3, proof x3, maintenance x2), using Step 2 as proof."
Check: 70 or more to continue, otherwise Park or Kill.

## STEP 4: Plan
"Write the build plan: jobs, the getting-started flow (bot email first), 2+ speciality skills with names, routines (cron + timezone, 1 health check, all paused, 30+ min apart), tools/connectors, security and hard rules (copied word for word), what it flags, what it proposes for approval, its tone level (serious, everyday or friendly) for README checks 21-23 (A-E lettered choices, emoji and icon use matched to tone, an occasional site mention if it has a one-click install), the economy-routing approach, and the test plan with at least one refusal test."
Check: The build lead approves the plan against the checklist before any files are written.

## STEP 5: Build files part 1
"Write profile.json, instructions.md, startup-questions.md and routines.md in === FILE: path === format."
Check: brand line, companion, category tag, hard rules, cron timezones, house-style rules 21-23 and writing style check 26 (short sentences, no fluff, only the opening hello is excited) in instructions.md.

## STEP 6: Build files part 2
"Write every skills/<slug>-<skill>/SKILL.md in === FILE: path === format."
Check: prefix, getting-started skill present, no secrets asked for.

## STEP 7: Build files part 3
"Write catalogue-card.md, test-script.md, avatar-prompt.md (3 options) and CHANGELOG.md."
Check: refusal test, pass rule per row, avatar rule.

## STEP 8: Economy version
"Write economy-version.md: a self-contained text that works pasted into a new bot, keeps every hard rule, and splits into an X thread of posts under 280 characters each. No audit in this file."
Check: it works on its own, nothing is trimmed from safety, the character counts fit.

## STEP 9: Self-audit
"Write self-audit.md: run all 20 checks and the grep from the standard, PASS/FAIL each with evidence."
Check: The build lead re-runs the checks and greps independently.

## STEP 10: Launch kit
"Write the X release thread (hook post with image notes, economy text posts, a last post with the site link and the install link as secondary), a single boost post with 3 hook variants, and the bot page copy for its 7 sections."
Check: claims check (nothing unprovable), all posts under 280 characters, check 26: only the hook post and boost post sound excited with a true first-to-market FOMO hook, and every other post uses short, plain sentences with no fluff.

## STEP 11: Documentation (added 24-10-2026, PG)
"Write the bot's proper documentation as docs/ in the package:
- README.md: what it does, who it's for, the one-click install, the startup questions, every routine (time, what it does, how to pause it), the skills, the companion bot, the house style tone level, and what it never does without a yes.
- SETUP.md: a step-by-step first run, including the connectors it needs and how to test that it works.
- FAQ.md: at least 8 real questions with answers, including limits and costs.
- TROUBLESHOOTING.md: the 5 most likely failures and the fix for each.
Plain words, no claims that can't be proved, and every fact must match the package files."
Check: The build lead cross-checks the docs against profile.json, routines.md and the skills (times, names, versions), and confirms every link works.

## STEP 12: Deploy via GitHub (build lead, not Grok)
Repo https://github.com/SocialBrandAfrica/socialbrand-bots. Vercel deploys main to https://bots.socialbrand.africa and gives every pull request its own preview link.
1. Make a branch called bot/<slug>-v<version>.
2. Add the package to packages/<slug>/: the files, docs/, CHANGELOG and avatar. Leave out secrets and private notes. Run the build so the bot page appears under bots/<slug>/.
3. Open a pull request titled "<Bot> v<version>". Its description lists the 23 checks with pass or fail, the test result, and the Vercel preview link.
4. Put the preview link in PG's single approval message. Nothing merges before PG's OK.
5. After the OK, merge (Vercel deploys), PG clicks the template card, the install link goes into config, and the publisher posts.

## After the recipe (build lead, not Grok)
Avatars (3 options to PG), create the bot, desk test plus live test if it's a flagship, stage the template, Step 12 pull request, then one PG approval moment (template card, avatar, thread, boost and preview link). Merge, the publisher posts, and the site page goes live.

## Capturing Grok's files (24-10-2026)
After each files step, copy Grok's reply with its Copy button so the markdown is kept. Split the files into the package with `python3 generator/split_files.py stepN.md packages/<slug>`. Page-text capture loses the markdown, so it's only a backup.
