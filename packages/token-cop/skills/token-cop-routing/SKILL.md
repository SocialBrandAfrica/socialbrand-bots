---
name: token-cop-routing
description: Capacity-first decision for a one-off task or testing request.
---
# routing
## Inputs
Task description, current platform statuses, owner's declared models and keys (existence only).
## Steps
1. Rank platforms by spare capacity before next reset ("use it or lose it").
2. Among green or amber, pick cheapest capable model.
3. Ongoing projects stay on assigned model unless red.
4. Propose route + fallback + reason. Wait for yes if hand-off required.
## Output
Routing recommendation table. No unilateral action.
## Limits
No model picker inside Grok Bot; route outward only. Hard cap of one escalation.
