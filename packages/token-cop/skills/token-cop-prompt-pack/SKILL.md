---
name: token-cop-prompt-pack
description: Generate one ready-to-paste Token Cop briefing per LLM the owner uses.
---
# prompt-pack
## Inputs
Current stocktake results, prioritised list, capacity ranking.
## Steps
1. Fill the template for each declared LLM.
2. Include budget state, what to work on, services to prioritise, delegate down, escalate up, pause or diarize.
3. Output ready-to-copy blocks. Remind owner to paste; bot never sends.
## Output
Markdown code blocks, one per LLM.
## Limits
Never send the pack. No secrets inside. No emoji and no site link inside the packs; they are text the owner sends to others.
