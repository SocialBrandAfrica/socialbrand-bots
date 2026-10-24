# Routines (timezone: Africa/Johannesburg)
| Name | Cron | Timing | Prompt | Output |
|---|---|---|---|---|
| Login health check (login-health-check) | 0 7 * * 1-5 | Weekdays 07:00 | Run @gatekeeper-health-check. It is read-only: check which services in the access table show Sign In, skipping human-only services. Change nothing. Copy no cookies. For each dropped service, send the chief bot one short line naming the service and asking it to sign in again. Update 'last checked'. If everything is signed in, send nothing. | Alert only on failure: one line per dropped service to the chief bot |
| Agent-risk watch (agent-risk-watch) | 0 9 * * 1 | Mondays 09:00 | Scan X and the web for news from the past week. Look for services in the access table, or common ones like email, WhatsApp, social and AI tools, that started blocking or restricting AI agents or automated browser use. Compare with earlier reports. If something relevant changed, send the owner a short note here. Name the service, the change and the source link. Offer: A move it to human only (recommended); B keep as is. If nothing changed, send nothing. | Short note to the owner only if something changed |

All routines ship paused. The owner must say yes before either one runs. Every cron uses timezone Africa/Johannesburg.
On Mondays the two routines run two hours apart (07:00 and 09:00), so their ±15-minute windows cannot overlap.
To pause a routine, ask Gatekeeper in chat, for example: "Pause the login health check."
