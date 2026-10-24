---
name: token-cop-ledger
description: >-
  Read and write the local usage ledger, calculate burn rates and produce
  reports.
---
# ledger
## Inputs
New reading (provider, used, remaining, reset, source, confidence, notes).
## Steps
1. Append JSONL line to local ledger file (default /workspace/token-cop/ledger/usage-ledger.jsonl). One line per limit, so a platform with weekly and monthly limits gets two lines.
2. Compute burn rate and days-to-limit when two readings exist; with one, estimate from time since last reset and mark it.
3. Support daily, immediate-red and weekly summary queries.
## Output
Updated ledger, calculated fields, report text.
## Limits
Local by default. No external upload of raw data. Owner-specific names never exported.
