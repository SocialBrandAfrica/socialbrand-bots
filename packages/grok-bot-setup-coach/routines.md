# Routines (timezone: owner's, default Africa/Johannesburg)
| Name | Cron | Timing | Prompt | Output |
|---|---|---|---|---|
| Weekly backup | `0 20 * * 0` | Sunday 20:00 | "Copy the bot's skills, routine list and key notes to the owner's backup folder. Report only if it fails." | Silent, or a failure alert |
| Monthly setup checkup (health/check routine) | `0 9 1 * *` | 1st of the month, 09:00 | "Run setup-coach-checkup." | One short report |
| Day-2 follow-up (one-off) | the next day at 09:00 | once | "Ask how the first routine went, then offer to adjust it or add the next skill." | One message |
