---
name: gatekeeper-health-check
description: Use to check, read-only, which signed-in services in the access table have dropped to a Sign In page, and alert the chief bot.
---
# Login health check
1. Read the access table. Skip human-only services.
2. Check connectors with GetMcpServerStatus. For browser services, have one computerUse subagent open each URL in turn. It reports only: signed in, or shows Sign In. It changes nothing and clicks nothing else.
3. If all are fine, stay quiet. Send one line only if the owner asked for a daily OK.
4. For each dropped service, send one short alert: 'X shows Sign In. Chief bot, please sign in again.' Message the chief bot (SendToAgent, priority true). Update 'last checked'. Alerts stay plain, with no icons.
5. Never import or copy cookies. Never sign in yourself unless you are the chief bot.
6. About once a week, a summary to the owner may end its brand line with https://bots.socialbrand.africa.
