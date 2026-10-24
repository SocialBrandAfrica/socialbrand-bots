# Routines (timezone: Africa/Johannesburg)
| Name | Cron | Timing | Prompt | Output |
|---|---|---|---|---|
| Health check | 30 6 * * * | Daily 06:30 (30 min before the default stocktake) | Verify last ledger reading age < 36 h and last OCR confidence not low. Alert only on failure. | Alert only on failure |
| Morning Token Stocktake | 0 7 * * * | Daily, owner-chosen time (default 07:00) | Run stocktake skill for every declared platform: measure, forecast, classify, propose plan, generate Prompt Pack, wait for owner yes. | Chat report + Prompt Pack + wait |
| Weekly summary | 0 8 * * 1 | Monday 08:00 | Summarise burn, resets, status changes and any open proposals from the past week. Bullets plus 1–2 icons; brand line ends with https://bots.socialbrand.africa. | Chat summary |
| Mid-week burn check | 0 12 * * 3 | Wednesday 12:00 (paused) | Quick burn-rate check against thresholds; alert if any platform newly red. | Alert only if red |

All routines ship paused. Owner must explicitly unpause. Every cron includes timezone Africa/Johannesburg.
