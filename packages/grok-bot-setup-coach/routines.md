# Routines (timezone: Africa/Johannesburg)
All routines ship paused. The owner switches them on during setup (step 7) or later.

| Name | Cron | Timing | Prompt | Output |
|---|---|---|---|---|
| Weekly backup | `0 20 * * 0` | Sunday 20:00, flexible ±15 min | "Make a weekly backup of this bot's setup: its memory summary, skill list, routine list and connector list. Save it to the connected drive the owner chose during setup; if they didn't choose one, save it as a dated file on the bot's computer. Only add new copies; never delete or overwrite older backups. Report to the owner in this chat only if the backup fails; if it succeeds, send nothing." | Silent, or a failure alert |
| Monthly setup checkup (health/check routine) | `0 9 1 * *` | 1st of the month 09:00, flexible ±15 min | "Run the setup-coach-checkup skill on this bot's setup (read-only review of connectors, skills, routines, backup and avatar). Change nothing. Send the owner in this chat one short report with what's healthy and any suggested fixes, each needing their yes before applying." | One short report |
| Day-2 follow-up (one-off, created only after the owner's yes) | the day after setup at 09:00 (Africa/Johannesburg), exact | once | "Ask how the first routine went, then offer to adjust it or add the next skill." | One message |
