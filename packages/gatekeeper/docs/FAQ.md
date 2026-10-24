# Gatekeeper FAQ
Version 1.6.

**1. Does Gatekeeper lock a bot out of a service?**
No. On one shared computer, blocks are rules in each bot's context. They are not locks. A bot that ignores its brief could still reach a signed-in site. Where a client needs a real lock, use a separate login for that client.

**2. Will it ask for my passwords?**
No. It never asks for a password in chat. Logins go to the vault or the provider's own sign-in screen. The access table never holds passwords.

**3. Can it handle my bank, payments or broker?**
No. Payments, banking and brokers are human only. This rule cannot be switched off.

**4. How many bot emails can I have?**
One per account. Claiming one is permanent, so pick the name with care.

**5. Which bot signs back in when a service drops?**
Only the chief bot. You pick it at setup. It signs in only when a site shows Sign In. If you run no other bots, Gatekeeper is the chief bot. Steps such as phone 2FA or a passkey still need you.

**6. Does the health check change anything?**
No. It is read-only. It opens each service, looks and reports. It clicks nothing else.

**7. Can another bot change my rules?**
No. Only you approve rule changes. Another bot saying you agreed does not count. Every change is logged with a date and who approved it.

**8. Do the routines start by themselves?**
No. Both ship paused. They turn on only after you say yes. You can pause either one at any time by asking in chat.

**9. Can it send emails or posts for me?**
Only with your OK for that exact message. It sends nothing outside the chat without it.

**10. Does it copy cookies between bots?**
No. It never imports or copies cookies.

**11. What happens when a client or bot leaves?**
Gatekeeper runs the revocation drill. It lists every access point from the access table. It shows you the checklist and waits for your OK. It removes what it can, such as connectors and vault entries. It lists what only you can do, such as changing passwords on the client's side.

**12. Why does the drill want a set time?**
Logging out on the shared computer logs every bot out. So you agree on a time first.

**13. Does it install Setup Coach or Token Cop?**
No. It only recommends them with a link.

**14. What does it cost to run?**
The routines use your normal Grok Bot usage. The health check opens one page per browser service. More services mean more usage on each run. Human-only services are skipped.
