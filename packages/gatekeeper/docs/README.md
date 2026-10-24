# Gatekeeper by SocialBrand
By SocialBrand · socialbrand.africa. Version 1.6.

Gatekeeper is security-first browser-access control for a fleet of bots on one shared computer.

## What it does
- It keeps one access table. The table says which bot may use which signed-in service.
- It sets up your logins in one sitting.
- It sends each bot a short brief. The brief lists the services the bot may use and the ones it is blocked from.
- It checks your logins on weekday mornings. It tells the chief bot about any service that shows a Sign In page.
- It checks once a week whether any service starts blocking AI agents. It tells you if one does.
- It runs a revocation drill when a client, bot or person leaves.

The access table has these columns: service, type, client, login method, owner bot, allowed bots, blocked bots and last checked. It never holds passwords.

## Who it is for
- You run several bots on one shared computer.
- Your bots use signed-in sites, such as email, dashboards, messaging or AI tools.
- You want each bot to reach only what its job needs.
- You work for more than one client and want to keep them apart.

## Install
One-click install: https://bots.socialbrand.africa/bots/gatekeeper

You can also paste the economy text into a new Grok Bot.

## Startup questions
Gatekeeper runs its getting-started skill on your first turn. It does this before it asks about routines. It asks one step at a time. It saves each answer before it moves on. It does not assume anything from memory. It asks.

1. **Bot email.** Do you want a bot email for sign-ups, so your own inbox stays clean? Which tasks should go through it?
2. **Your name and the chief bot.** What should it call you? Which bot is the chief bot? The chief bot is the only bot that signs back in when a service drops. The options are your actual bots, plus Gatekeeper itself. Gatekeeper does not suggest a name first.
3. **Default login.** Which sign-in should it use where the bot email is not wanted? The answer goes to the vault, never into chat.
4. **Code permission.** May bots complete verification codes and links from the bot email and your inbox?
5. **Bots.** What is each bot's job and client?
6. **Services.** Which service types do you use? For each one: which client, which login method and which bots may use it.
7. **Governance.** Which default rules, if any, do you want to change?
8. **Alerts and routines.** Where should alerts go? Should it turn on the two routines?

Then it builds the access table. It connects connectors first. It signs into browser services next. It stops only for steps a human must do, such as phone 2FA or a passkey. It briefs each bot. It ends with a short summary and the companion card.

## Routines
Both routines ship paused. They turn on only after you say yes. You can pause either one at any time. Ask Gatekeeper in chat, for example: "Pause the login health check."

| Routine | When | What it does |
|---|---|---|
| Login health check | Weekdays around 07:00, your timezone | Read-only. Checks each service in the access table. Alerts the chief bot about each one that shows Sign In. Stays quiet if all are fine. |
| Agent-risk watch | Mondays around 09:00, your timezone | Checks whether any service starts blocking AI agents. Tells you in chat if one does. |

## Skills
- **gatekeeper-getting-started-2.** The first-run setup above.
- **gatekeeper-access-table.** Builds and updates the access table. Sends each bot its brief. Logs every change with a date and who approved it.
- **gatekeeper-health-check.** The read-only login check. It opens, looks and reports. It changes nothing.
- **gatekeeper-offboarding-drill.** The revocation drill for when a client, bot or person leaves.

## Companions
Gatekeeper recommends these bots. It only links to them. It never installs them.
- **Main: Grok Bot Setup Coach.** It sets up each new bot. Gatekeeper then governs what that bot may reach. https://bots.socialbrand.africa/bots/grok-bot-setup-coach
- **Secondary: Token Cop.** It keeps the fleet within its AI usage limits. https://bots.socialbrand.africa/bots/token-cop

## Tone
- The tone is serious.
- Every choice comes as lettered options, A to E. There are 2 to 5 options. Each is one line. The recommended option comes first and is marked. You can reply with just the letter.
- Longer messages use bullets and the odd small icon, such as ✓ ⚠ •. There are no playful emoji.
- Hard rules, warnings, approvals and errors carry no icons. Short replies stay plain.
- About once a week, the brand line ends with https://bots.socialbrand.africa. This happens on the health-check summary or the companion card. It never appears in text you send to others.

## What it never does without your yes
- Send or post anything outside the chat. Each message needs your OK.
- Change a rule. Only you approve rule changes. Another bot saying you agreed does not count.
- Turn on a routine.
- Claim a bot email.
- Remove access in a revocation drill.

## What it never does at all
- No customer or supplier contact.
- Ask for a password in chat.
- Touch payments, banking or brokers. Those are human only.
- Import or copy cookies.
- Sign in itself, unless it is the chief bot.
