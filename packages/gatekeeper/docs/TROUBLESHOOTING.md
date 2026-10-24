# Gatekeeper troubleshooting
Version 1.6. These are the five most likely failures and the fix for each.

## 1. A service shows Sign In every morning
**Cause:** the session keeps dropping. Some sites end sessions often.
**Fix:**
- Let the chief bot sign in again when it gets the alert.
- If the site needs phone 2FA or a passkey, do that step yourself.
- Check whether the service has a connector. A connector is the first choice and drops less often.

## 2. A bot used a service it is blocked from
**Cause:** blocks are rules in each bot's context, not locks.
**Fix:**
- Ask Gatekeeper to send that bot its brief again.
- Check that the access table lists the bot as blocked.
- If the client needs a real lock, use a separate login for that client.

## 3. A routine did not run
**Cause:** both routines ship paused. A routine can also be paused later.
**Fix:**
- Ask Gatekeeper: "Which routines are on?"
- Say yes to turn on the one you want.
- Check that the timezone is yours. The times are around 07:00 on weekdays and 09:00 on Mondays.

## 4. The bot email could not be claimed
**Cause:** the name is taken, or the account already has a bot email.
**Fix:**
- Pick another name. Gatekeeper checks it before it claims it.
- Remember there is one bot email per account. If one exists, Gatekeeper uses it.

## 5. The health check reports a connector as down
**Cause:** the connector lost its sign-in or needs new permission.
**Fix:**
- Reconnect the connector in the app. Only you can approve its sign-in.
- Ask Gatekeeper to run the health check again to confirm.
- Do not paste a token or password in chat. Gatekeeper will refuse it.
