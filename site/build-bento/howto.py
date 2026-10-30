"""'How it works' click-flow blocks, shared by build.py and one-off patches."""
import html
E = lambda s: html.escape(s, quote=True)

STEPS = [
    ('browse', 'Pick a bot', 'Browse the catalogue. Every bot page shows its full text: rules, skills and routines.'),
    ('install', 'Click Install', 'The install link opens the bot on x.ai. Prefer to paste? Copy the text instead.'),
    ('add', 'Add it to Grok Bot', 'Add it to your own Grok Bot. The bot is free, with the full text open.'),
    ('setup', 'Answer a few A–E questions', 'Say hello and setup starts in the chat. Short lettered choices. Reply with one letter.'),
    ('run', 'It runs. You approve.', 'Routines start paused. You turn them on. Nothing changes without your yes.'),
]

ICONS = {  # simple 24px line icons, no external assets
    'browse': '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
    'install': '<path d="M12 4v11"/><path d="M7 10l5 5 5-5"/><path d="M5 20h14"/>',
    'add': '<rect x="4" y="4" width="16" height="16" rx="4"/><path d="M12 8v8M8 12h8"/>',
    'setup': '<path d="M5 6h14v9H9l-4 4z"/><path d="M9 10.5h6"/>',
    'run': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
}

def _icon(k):
    return f'<svg class="flow-ico" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg>'

def flow_home():
    tiles = ['c-mag h1', 'c-red h2', 'c-amb h2', 'c-teal h3', 'c-lime hot m-full t-full d-2']  # heat-map run: cool to hot
    lis = ''.join(f'<li class="flow-step tile lift reveal {tiles[i]}"><span class="flow-num" aria-hidden="true">0{i+1}</span>{_icon(k)}<h3>{E(t)}</h3><p>{E(d)}</p></li>' for i, (k, t, d) in enumerate(STEPS))
    return f'''  <section class="section flow" id="how-it-works" aria-labelledby="flow-title">
    <div class="eyebrow cyan">How it works</div>
    <h2 class="section-title" id="flow-title">From click to working bot in five steps</h2>
    <ol class="flow-steps bento">{lis}</ol>
    <p class="flow-foot">Nothing to sign up for on this site. You stay in control the whole way.</p>
  </section>
'''

def flow_compact(name, live=True):
    chips = ''.join(f'<li class="flow-chip"><span class="flow-num" aria-hidden="true">0{i+1}</span>{_icon(k)}<span>{E(t)}</span></li>' for i, (k, t, d) in enumerate(STEPS))
    note = (f'Install opens {E(name)} on x.ai. Add it to Grok Bot, answer a few A–E questions, then approve what it does.'
            if live else f'{E(name)} is in build. The install link comes with its release. You can read and paste the text now.')
    return f'''    <section class="flow-compact" aria-label="How it works">
      <div class="eyebrow cyan">How it works</div>
      <ol class="flow-chips">{chips}</ol>
      <p class="flow-foot">{note} <a href="/#how-it-works">More</a></p>
    </section>
'''

CSS = '''
/* How it works: click flow */
.flow-steps { list-style: none; display: grid; grid-template-columns: repeat(5, 1fr); gap: 1rem; margin-top: 1.5rem; counter-reset: none; }
.flow-step { position: relative; border: 1px solid var(--border); border-radius: 14px; padding: 1.1rem 1rem 1.2rem; background: linear-gradient(160deg, #141414, #0A0A0A); transition: transform .2s ease, border-color .2s ease; }
.flow-step:hover { transform: translateY(-3px); border-color: var(--cyan); }
.flow-step h3 { font-size: 1.05rem; margin: .6rem 0 .35rem; }
.flow-step p { color: var(--secondary); font-size: .9rem; }
.flow-num { font-family: 'JetBrains Mono', monospace; font-size: .8rem; color: #000; background: var(--lime); border-radius: 999px; padding: .1rem .55rem; margin-right: .5rem; }
.flow-ico { color: var(--cyan); vertical-align: middle; }
.flow-step:nth-child(2) .flow-ico, .flow-chip:nth-child(2) .flow-ico { color: var(--pink); }
.flow-step:nth-child(4) .flow-ico, .flow-chip:nth-child(4) .flow-ico { color: var(--pink); }
.flow-step:not(:last-child)::after { content: "→"; position: absolute; right: -0.85rem; top: 1.2rem; color: var(--lime); font-weight: 700; }
.flow-foot { color: var(--secondary); margin-top: 1rem; font-size: .9rem; }
.flow-foot a { color: var(--cyan); }
.flow-compact { margin: 1.25rem 0 .5rem; border: 1px solid var(--border); border-radius: 14px; padding: .9rem 1rem; }
.flow-chips { list-style: none; display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .5rem; }
.flow-chip { display: flex; align-items: center; gap: .35rem; border: 1px solid var(--border); border-radius: 999px; padding: .3rem .75rem .3rem .35rem; font-size: .85rem; background: #111; }
.flow-chip .flow-num { margin-right: 0; }
.flow-chip .flow-ico { width: 18px; height: 18px; }
@media (prefers-reduced-motion: no-preference) {
  .flow-step { animation: flow-in .5s ease both; }
  .flow-step:nth-child(2) { animation-delay: .08s; } .flow-step:nth-child(3) { animation-delay: .16s; }
  .flow-step:nth-child(4) { animation-delay: .24s; } .flow-step:nth-child(5) { animation-delay: .32s; }
}
@keyframes flow-in { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
@media (max-width: 900px) { .flow-steps { grid-template-columns: 1fr 1fr; } .flow-step::after { display: none; } }
@media (max-width: 600px) { .flow-steps { grid-template-columns: 1fr; } }
'''
