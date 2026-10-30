#!/usr/bin/env python3
"""Generates the static site in ../live from the Foundry packages. Output is plain HTML; no build step needed to deploy."""
import html, json, re, shutil, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def need_env(name, what):
    v = os.environ.get(name)
    if not v or not Path(v).is_dir():
        sys.exit(f'build.py: set {name} to {what} (got: {v or "unset"})')
    return Path(v)
import sys
OUT = need_env('SITE_OUT', 'the site repo checkout (output, and the source of packages/)')
PK = need_env('FOUNDRY_PACKAGES', 'the folder with the bot packages not yet in the site repo')
TCP = OUT / 'packages/token-cop'  # Token Cop source of truth: the package in the site repo
SITE = 'https://bots.socialbrand.africa'
import sys; sys.path.insert(0, str(Path(__file__).resolve().parent)); from howto import flow_home, flow_compact
GK_SKILLS = need_env('GK_SKILLS_DIR', 'the folder with the Gatekeeper skill folders')
TC_PAGE = SITE + '/bots/token-cop'
E = lambda s: html.escape(s, quote=True)
RAW_QUOTE_PAGES = {'token-cop'}  # pages whose text blocks keep quotes as typed (matches the live pages)
CUR = {'slug': None}
EP = lambda s: html.escape(s, quote=CUR['slug'] not in RAW_QUOTE_PAGES)

def rd(p): return Path(p).read_text(encoding='utf-8').replace('TOKEN_COP_LINK', TC_PAGE).strip() + '\n'

def skill(path):
    t = rd(path)
    m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    name, desc = Path(path).parent.name, ''
    if m:
        fm = m.group(1)
        n = re.search(r'^name:\s*(.+)$', fm, re.M)
        if n: name = n.group(1).strip()
        d = re.search(r'^description:\s*(>-)?\s*(.*?)(?=^\w+:|\Z)', fm, re.M | re.S)
        if d: desc = ' '.join(d.group(2).split())
    return dict(name=name, desc=desc, text=t)

def md_table(md):
    rows = [l for l in md.splitlines() if l.strip().startswith('|')]
    if len(rows) < 2: return ''
    cells = lambda l: [c.strip().strip('`') for c in l.strip().strip('|').split('|')]
    head, body = cells(rows[0]), [cells(r) for r in rows[2:]]
    h = '<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th>{E(c)}</th>' for c in head) + '</tr></thead><tbody>'
    for r in body: h += '<tr>' + ''.join(f'<td data-label="{E(head[i]) if i < len(head) else ""}">{E(c)}</td>' for i, c in enumerate(r)) + '</tr>'
    return h + '</tbody></table></div>'

def lst(items): return '<ul>' + ''.join(f'<li>{E(i)}</li>' for i in items) + '</ul>'

# ---------------- Bot data ----------------
tc = json.loads(rd(TCP/'profile.json'))
sc = json.loads(rd(OUT/'packages/grok-bot-setup-coach/profile.json'))
so = json.loads(rd(PK/'supplier-order-checker/profile.json'))
def selling_from_card(p):
    t = rd(p); return t.split('\n', 1)[1].strip() if t.startswith('#') else t

BOTS = []
BOTS.append(dict(
    slug='token-cop', name='Token Cop', version='v0.7', updated='30-10-2026', tag='DEV-AGENTS', status='live',
    color='#0D9488', headline=('TOKEN COP', 'AI USAGE GOVERNANCE'), neon='cyan',
    pitch='See every place your AI usage goes. Set your own rules. Token Cop checks them.',
    hello='New and free: a template that runs on your existing plan.',
    meta_extra='Runs on your existing plan.',
    first_job='First job, right after setup: Token Cop maps your AI usage with you: plan, pool, overage, reset, cap and what stops at $0. Each rule cites an official page. Then you pick your own rules on A–E cards: a daily cap, extra spend, approvals and cadence. Every stocktake checks them and flags any breach.',
    docs='token-cop', setup_time='About 15 minutes, plus one-time sign-ins to your usage pages.',
    profile=f"{tc['title']}\n{tc['description']}\nCategory: {tc['category_id']} · {tc['category']}\nVersion: {tc['version']} · Risk: {tc['risk_level']}\nPlatform: {tc['platform']}\nPublisher: {tc['publisher']}\nCompanion: Grok Bot Setup Coach ({SITE}/bots/grok-bot-setup-coach)",
    instructions=rd(TCP/'instructions.md'),
    skills=[skill(TCP/f'skills/{s}/SKILL.md') for s in ['token-cop-getting-started','token-cop-governance','token-cop-stocktake','token-cop-routing','token-cop-prompt-pack','token-cop-ledger','token-cop-delegation','token-cop-hard-rules']],
    routines=rd(TCP/'routines.md'), routines_note='All routines ship paused. You unpause them yourself. The usage monitor is optional.',
    avatars=[('token-cop/avatar.png','A · White stopwatch-meter on teal (approved)'),('token-cop/avatars/B.jpg','B · Black stopwatch-meter on lime'),('token-cop/avatars/C.jpg','C · White shield gauge on hot pink')],
    avatar_more=False, avatar_prompt=rd(OUT/'packages/token-cop/avatar-prompt.md'),
    selling=selling_from_card(TCP/'catalogue-card.md').replace('https://x.ai/bot/duonwBK5SXXQTAy6NNg2r', SITE+'/bots/grok-bot-setup-coach'),
    economy=rd(TCP/'economy-version.md'),
    can=['Your shared computer: signed-in browser for usage pages, OCR, a local ledger','Usage dashboards you declare, by screenshot+OCR or paste','Optional API scripts (keys stay on your computer or vault)','Messages to your other bots (batched, non-priority)'],
    cannot=['Customer or supplier contact','Payments, banking, brokers, medical, legal','Passwords, tokens, card or ID numbers','External email, social or payment services',"Another bot's routines without your explicit yes"],
    new=['Rule 7, cheap gate: Token Cop proposes a cheap gate so routines stop waking the model for nothing. Your pick on an A–E card.','Rule 8, cut relays: bots brief once and report back once. Your pick on an A–E card.'],
    rules=['Nothing changes without your yes; routines ship paused.','Your rules set what it flags. They never switch off a hard rule or let it spend.','Finance actions are human-only. Propose only.','Screenshots stay local, cropped to numbers.','Never invents numbers. Marks confidence and source.'],
    companion='grok-bot-setup-coach', promo=('SET UP THE REST', 'THE SAME WAY', 'Token Cop keeps the usage under control. Setup Coach gets each new bot working in one sitting, with a backup.', 'teal'),
))
BOTS.append(dict(
    slug='grok-bot-setup-coach', name='Grok Bot Setup Coach', version='v1.0', updated='24-10-2026', tag='PA-DESK', status='live',
    color='#0D0D0D', headline=('SETUP COACH', 'ONE SITTING'), neon='lime',
    pitch='New: your bot, actually working, in one sitting. Bot email, connectors, a first skill, a first routine, a weekly backup and a shareable my-bot card.',
    docs='grok-bot-setup-coach',
    profile=f"Grok Bot Setup Coach: {sc['title']}\n{sc['description']}\nCategory: {sc['category_id']} · {sc['category']}\nVersion: {sc['version']} · Risk: {sc['risk_level']}\nPlatform: {sc['platform']}\nPublisher: {sc['publisher']}\nCompanion: Token Cop ({TC_PAGE})",
    instructions=rd(OUT/'packages/grok-bot-setup-coach/instructions.md'),
    skills=[skill(OUT/'packages/grok-bot-setup-coach/skills/setup-coach-getting-started/SKILL.md'),
            skill(OUT/'packages/grok-bot-setup-coach/skills/setup-coach-connector-wizard/SKILL.md'),
            skill(OUT/'packages/grok-bot-setup-coach/skills/setup-coach-first-routine/SKILL.md'),
            skill(OUT/'packages/grok-bot-setup-coach/skills/setup-coach-share-my-bot/SKILL.md'),
            skill(OUT/'packages/grok-bot-setup-coach/skills/setup-coach-checkup/SKILL.md')],
    routines=rd(OUT/'packages/grok-bot-setup-coach/routines.md'), routines_note="Routines use your timezone (default Africa/Johannesburg) and ship paused until you say yes.",
    avatars=[('grok-bot-setup-coach/avatars/approved.png','Spanner in a speech bubble (approved 24-10-2026)')], avatar_more=False,
    avatar_prompt=rd(OUT/'packages/grok-bot-setup-coach/avatar-prompt.md'),
    selling=selling_from_card(OUT/'packages/grok-bot-setup-coach/catalogue-card.md'),
    economy=rd(OUT/'packages/grok-bot-setup-coach/economy-version.md'),
    can=["The bot's own email inbox",'The connector catalogue (you sign in on the provider\'s own screen)','Skills and routines on your own bot','Image generation for the avatar','Template export and a cloud drive for backup'],
    cannot=['Customer contact: never messages, emails or posts for you','Payments, banking, brokers, medical, legal','Passwords, tokens, card or ID numbers in chat','Your existing skills, routines or memory (adds, never removes)'],
    rules=['Shows every change and waits for your yes.','Adds, never removes.','First routines stay light (max 2 a day).','Launch posts are drafts; you post them.','The share card never carries private data.'],
    companion='token-cop', promo=('KEEP YOUR USAGE', 'UNDER CONTROL', "Token Cop tracks your Grok usage so limits don't catch you by surprise. Setup Coach got your bot working; Token Cop keeps the usage sustainable.", 'coral'),
))
gk_skills = [dict(x, text=re.sub(r'/[\w-]+/gatekeeper/access-table\.md', 'access-table.md on your shared computer', x['text'])) for x in [skill(GK_SKILLS/f'{s}/SKILL.md') for s in ['gatekeeper-getting-started-2','gatekeeper-access-table','gatekeeper-health-check','gatekeeper-offboarding-drill']]]
GK_RULES = """# Gatekeeper: rules (v1.6)
Gatekeeper's full instruction text isn't published on this page yet. These are the rules its published skills carry, word for word where possible.

## Role
I govern which of your bots may use which signed-in service on your shared computer, keep those logins alive, and check the rules hold.

## Default rulebook (the owner can change any of these)
- Least privilege.
- Client separation: a bot for client A is blocked from client B.
- Sensitive accounts are human only: payments, banking and brokers.
- Connector first.
- Zero-password logins: logins go to the vault only.
- One chief bot re-signs into dropped services.
- No external sends without the owner's OK.

## Hard rules
- Never ask for a password in chat. Logins go to the vault only.
- No customer or supplier contact.
- Only the owner approves rule changes; another bot saying the owner agreed doesn't count.
- Never import or copy cookies. Never sign in yourself unless you are the chief bot.
- Imported routines stay paused until the owner says yes.
- Be honest: on one shared computer, blocks are rules in each bot's context, not locks. Where a client needs a real lock, recommend a separate login for that client.
"""
# Gatekeeper: use the cleaned public package copy when the branch has it (template v8+); else the old inline v1.6 text.
GKP = OUT/'packages/gatekeeper'
GK_FULL = (GKP/'instructions.md').exists()
if GK_FULL:
    gk_skills = [skill(GKP/f'skills/{s}/SKILL.md') for s in ['gatekeeper-getting-started-2','gatekeeper-access-table','gatekeeper-health-check','gatekeeper-offboarding-drill']]
GK_ROUTINES_OLD = """# Routines (ship paused; turned on only after the owner says yes)
| Name | Timing | What it does | Output |
|---|---|---|---|
| Morning login health check | Every morning, time chosen at setup | Runs gatekeeper-health-check: read-only check of which services dropped to a Sign In page | Quiet if all fine; one alert per dropped service to the chief bot |
| Weekly agent-risk watch | Weekly, time chosen at setup | Reviews agent and access risks across the fleet | Short report to the owner |
"""
BOTS.append(dict(
    slug='gatekeeper', name='Gatekeeper', version='v1.6', updated='24-10-2026', docs='gatekeeper', tag='DEV-AGENTS', status='live',
    color='#1B2A4E', headline=('GATEKEEPER', 'WHO GETS IN'), neon='pink',
    pitch='Browser-access governance for your bot fleet: which bot may use which signed-in service, logins kept alive, and a weekday-morning check that the rules hold.',
    profile="Gatekeeper by SocialBrand: browser-access governance for your bot fleet\n" + json.loads(rd((GKP if GK_FULL else PK/'gatekeeper')/'profile.json'))['description'] + "\nCategory: DEV-AGENTS · Bots and automation\nVersion: 1.6 · Risk: Low\nPlatform: Grok Bot\nPublisher: SocialBrand (socialbrand.africa)\nWritten by SocialBrand (socialbrand.africa)\nCompanion: Grok Bot Setup Coach (" + SITE + "/bots/grok-bot-setup-coach); also Token Cop (" + TC_PAGE + ")",
    instructions=rd(GKP/'instructions.md') if GK_FULL else GK_RULES, instructions_note=None if GK_FULL else "Full instruction text coming soon. Shown here: the rules from Gatekeeper's published skills.",
    skills=gk_skills,
    routines=rd(GKP/'routines.md') if GK_FULL else GK_ROUTINES_OLD, routines_note='Both routines ship paused. Timezone: Africa/Johannesburg. Gatekeeper asks before turning either on.',
    avatars=[('gatekeeper/avatars/approved.png','White shield with a keyhole on teal (approved 24-10-2026)')], avatar_more=False,
    avatar_prompt="One bold central object: a white shield with a keyhole and a short amber bar near its base, on deep teal. No text, no people, no logos, no fine detail. Square 1024x1024.\n",
    selling="""- Sign your bots up to new tools with a bot email, so your own inbox stays clean.
- Keep each client's dashboards and WhatsApp limited to that client's bot.
- Each weekday morning, tell you which logins dropped and get them fixed before work starts.
- One access table: service, type, client, login method, allowed and blocked bots, last checked. No passwords.
- A revocation drill for when a client, bot or person leaves.
Risk level: Low. Read-only checks; changes only after your OK.
Companion: Grok Bot Setup Coach, which sets up each new bot in one sitting.
""",
    economy=rd((GKP if GK_FULL else PK/'gatekeeper')/'economy-version.md').replace(' Owner to OK before posting.', ''),
    can=['The access table on your shared computer (no passwords)','Connector status checks','Opening service pages read-only to see if they show Sign In','Messages to your chief bot and other bots (their access briefs)'],
    cannot=['Customer or supplier contact','Payments, banking, brokers (human only)','Passwords in chat; logins live in the vault only','Copying or importing cookies','Signing in itself unless it is the chief bot','Rule changes without the owner'],
    rules=['No customer or supplier contact.','Owner alone approves rule changes.','Least privilege and client separation by default.','Routines ship paused.','Blocks are rules, not locks; says so plainly.'],
    companion='grok-bot-setup-coach', promo=('NEW BOT?', 'SET IT UP RIGHT', 'Setup Coach gets each new bot working in one sitting, with a backup. Gatekeeper then keeps its logins in line.', 'teal'),
))
BOTS.append(dict(
    slug='supplier-order-checker', name='Supplier Order Checker', version='v0.3', updated='24-10-2026', tag='OWN-OPS', status='coming-soon',
    color='#262626', headline=('SUPPLIER ORDER', 'CHECKER'), neon='lime',
    pitch='Checks every supplier invoice against your order before you pay it. Flags short deliveries, substitutions, price rises and missing credits, and drafts the claim.',
    profile=f"Supplier Order Checker: {so['title']}\n{so['description']}\nCategory: {so['category_id']} · {so['category']}\nVersion: 0.3 (first release, in build) · Risk: {so['risk_level']}\nPlatform: {so['platform']}\nPublisher: {so['publisher']}\nCompanion: Gatekeeper ({SITE}/bots/gatekeeper)",
    instructions=rd(PK/'supplier-order-checker/instructions.md'),
    skills=[skill(PK/f'supplier-order-checker/skills/{s}/SKILL.md') for s in ['getting-started','invoice-check','claim-draft','supplier-scorecard']],
    routines=rd(PK/'supplier-order-checker/routines.md'), routines_note='All routines ship paused. Timezone: Africa/Johannesburg.',
    avatars=[('supplier-order-checker/avatars/approved.png','Shipping box with an orange label (approved 24-10-2026)')], avatar_more=False, avatar_prompt=rd(PK/'supplier-order-checker/avatar-prompt.md'),
    selling=selling_from_card(PK/'supplier-order-checker/catalogue-card.md').replace('(x.ai link added after export)', '(link comes with the first release)'),
    economy=None,
    note='Coming soon. This bot is still in build and testing. The text below is the working draft, shared openly.',
    can=["The bot's own inbox, for forwarded invoices and delivery notes",'Cloud drives or docs where orders or price lists are kept (optional)','Order and stock exports or photos (never a login)','Alerts to you only'],
    cannot=['Supplier, rep or customer contact','Paying, approving or rejecting invoices','Banking details, payments, brokers','Passwords, tokens, card or ID numbers; supplier-portal logins'],
    rules=['Flag only. You decide.','Claims are drafts; you send them.','One flag message a day, only when needed.','Supplier and store names never leave your memory.'],
    companion='gatekeeper', promo=('ONE BOT PER STORE?', 'KEEP THEM IN LINE', 'Gatekeeper keeps your store bots on only the supplier and email sites they need.', 'cyan'),
))
BY = {b['slug']: b for b in BOTS}

# ---------------- Assets ----------------
def setup_assets():
    img = OUT/'assets/img'
    for b in BOTS:
        d = img/'bots'/b['slug']; d.mkdir(parents=True, exist_ok=True)
        new = []
        for i, (src, label) in enumerate(b['avatars']):
            sp = next((p for p in (OUT/'packages'/src, PK/src) if p.exists()), None)
            if sp is None: sys.exit(f'build.py: avatar not found: {src}')
            letter = 'ABC'[i]
            dst = d/f'{letter}.jpg'
            if IMAGES: Image.open(sp).convert('RGB').resize((512, 512), Image.LANCZOS).save(dst, quality=88, optimize=True)
            new.append((f'/assets/img/bots/{b["slug"]}/{letter}.jpg', label))
            if IMAGES and i == 0:  # stable public path for the approved avatar; installed bots download it
                (OUT/'bots'/b['slug']).mkdir(parents=True, exist_ok=True)
                shutil.copyfile(sp, OUT/'bots'/b['slug']/'avatar.png')
        if not new and IMAGES:  # placeholder tile, clearly not an avatar
            ph = Image.new('RGB', (512, 512), '#262626'); dr = ImageDraw.Draw(ph)
            f = ImageFont.truetype(FONT_BLACK, 220); t = b['name'][0]
            w = dr.textlength(t, font=f); dr.text(((512-w)/2, 120), t, font=f, fill='#A3A3A3')
            ph.save(d/'placeholder.jpg', quality=85); b['card_avatar'] = f'/assets/img/bots/{b["slug"]}/placeholder.jpg'
        else:
            b['card_avatar'] = new[0][0]
        b['avatar_files'] = new
        make_og(b, d/'og.png')
        b['og'] = f'{SITE}/assets/img/bots/{b["slug"]}/og.png'

# Fonts: set SITE_FONT_DIR to a folder holding ArchivoBlack-Regular.ttf, Archivo-VariableFont_wdth,wght.ttf
# and JetBrainsMono-VariableFont_wght.ttf. If unset, image generation is skipped and the images in the repo are kept.
_FD = os.environ.get('SITE_FONT_DIR')
def _font(pat):
    return next(iter(sorted(Path(_FD).rglob(pat))), None) if _FD else None
FONT_BLACK, FONT_REG, FONT_MONO = _font('ArchivoBlack-Regular.ttf'), _font('Archivo-VariableFont*.ttf'), _font('JetBrainsMono-VariableFont*.ttf')
IMAGES = all((FONT_BLACK, FONT_REG, FONT_MONO))
if not IMAGES: print('build.py: SITE_FONT_DIR unset or fonts missing; skipping image generation (repo images kept)')
FONT_BLACK, FONT_REG = str(FONT_BLACK), str(FONT_REG)
NEON = {'pink': '#FF2E9A', 'lime': '#B6FF00', 'cyan': '#00E5FF'}

def wraptext(dr, text, font, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if dr.textlength(t, font=font) > maxw and cur: lines.append(cur); cur = w
        else: cur = t
    if cur: lines.append(cur)
    return lines

def make_og(b, path, avatar_path=None):
    if not IMAGES: return
    W, H = 1200, 630
    im = Image.new('RGB', (W, H), '#0A0A0A'); dr = ImageDraw.Draw(im)
    dr.rectangle([24, 24, W-25, H-25], outline='#262626', width=2)
    src = None
    if b.get('avatar_files'): src = OUT/b['avatar_files'][0][0].lstrip('/')
    elif b.get('card_avatar'): src = OUT/b['card_avatar'].lstrip('/')
    if avatar_path: src = avatar_path
    if src: im.paste(Image.open(src).convert('RGB').resize((380, 380)), (60, 125))
    x = 480
    mono = ImageFont.truetype(str(FONT_MONO), 24)
    dr.text((x, 70), 'SOCIALBRAND BOTS · FREE · OPEN TEXT', font=mono, fill=NEON['pink'])
    fb = ImageFont.truetype(FONT_BLACK, 62)
    y = 120
    for line in wraptext(dr, b['name'].upper(), fb, 680)[:2]:
        tw = dr.textlength(line, font=fb)
        col = NEON[b['neon']]
        dr.rectangle([x-8, y-4, x+tw+10, y+74], fill=col)
        dr.text((x+4, y+4), line, font=fb, fill='#000' if b['neon'] == 'pink' else '#fff')
        dr.text((x, y), line, font=fb, fill='#fff' if b['neon'] == 'pink' else '#000')
        y += 92
    fr = ImageFont.truetype(FONT_REG, 28)
    try: fr.set_variation_by_name('Regular')
    except Exception: pass
    for line in wraptext(dr, b['pitch'], fr, 680)[:4]:
        dr.text((x, y+10), line, font=fr, fill='#D4D4D4'); y += 38
    dr.text((x, 540), f"{b['version']} · bots.socialbrand.africa", font=mono, fill=NEON['lime'])
    im.save(path, optimize=True)

def site_assets():
    if not IMAGES: return
    img = OUT/'assets/img'
    # favicon
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#0A0A0A"/><rect x="6" y="14" width="52" height="36" fill="#FF2E9A"/><text x="34" y="44" font-family="Arial Black,Archivo,sans-serif" font-weight="900" font-size="28" text-anchor="middle" fill="#000">SB</text><text x="32" y="42" font-family="Arial Black,Archivo,sans-serif" font-weight="900" font-size="28" text-anchor="middle" fill="#fff">SB</text></svg>'
    (OUT/'favicon.svg').write_text(svg)
    def fav(size):
        im = Image.new('RGB', (size, size), '#0A0A0A'); dr = ImageDraw.Draw(im)
        s = size/64; dr.rectangle([6*s, 14*s, 58*s, 50*s], fill='#FF2E9A')
        f = ImageFont.truetype(FONT_BLACK, int(26*s))
        w = dr.textlength('SB', font=f); tx = (size-w)/2; ty = 15*s
        dr.text((tx+2*s, ty+2*s), 'SB', font=f, fill='#000'); dr.text((tx, ty), 'SB', font=f, fill='#fff')
        return im
    fav(180).save(OUT/'apple-touch-icon.png'); fav(32).save(OUT/'favicon-32.png')
    fav(64).save(OUT/'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    # home og: four avatars
    W, H = 1200, 630
    im = Image.new('RGB', (W, H), '#0A0A0A'); dr = ImageDraw.Draw(im)
    dr.rectangle([24, 24, W-25, H-25], outline='#262626', width=2)
    fb = ImageFont.truetype(FONT_BLACK, 76)
    dr.text((70, 70), 'AI TEAMMATES FOR WORK', font=fb, fill='#fff')
    t = 'FREE, OPEN TEXT'; tw = dr.textlength(t, font=fb)
    dr.rectangle([62, 170, 70+tw+14, 262], fill='#FF2E9A'); dr.text((74, 178), t, font=fb, fill='#000'); dr.text((70, 174), t, font=fb, fill='#fff')
    xx = 70
    for b in BOTS:
        im.paste(Image.open(OUT/b['card_avatar'].lstrip('/')).convert('RGB').resize((200, 200)), (xx, 310)); xx += 230
    mono = ImageFont.truetype(str(FONT_MONO), 26)
    dr.text((70, 550), 'bots.socialbrand.africa · By SocialBrand', font=mono, fill='#B6FF00')
    im.save(img/'og-home.png', optimize=True)

# ---------------- Templates ----------------
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">'
DISCLOSURE = 'This is how we keep the bots free: some links are referral links, and we say so next to them. Every link also has a plain version.'

def head(title, desc, path, og, kind='website'):
    url = SITE + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{kind}">
<meta property="og:site_name" content="SocialBrand Bots">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@Soc_Bran_Africa">
<meta name="twitter:title" content="{E(title)}">
<meta name="twitter:description" content="{E(desc)}">
<meta name="twitter:image" content="{og}">
<meta name="theme-color" content="#0A0A0A">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def nav(active=''):
    a = lambda k: ' class="active"' if k == active else ''
    return f'''<nav class="nav">
  <a href="/" class="logo">SocialBrand Bots<span class="dot">.</span></a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-menu" aria-label="Menu"><span class="bars" aria-hidden="true"></span></button>
  <div class="nav-menu" id="nav-menu">
  <div class="nav-links">
    <a href="/#catalogue"{a('bots')}>Bots</a>
    <a href="/#categories">Categories</a>
    <a href="/#how">How it works</a>
    <a href="/about"{a('about')}>About</a>
    <a href="/about#contribute">Contribute</a>
  </div>
  <button class="search-pill" type="button" onclick="var i=document.getElementById('hero-search'); if(i){{i.focus();}}else{{location.href='/#catalogue';}}">Search… <kbd>Ctrl K</kbd></button>
  <a href="https://x.com/Soc_Bran_Africa" target="_blank" rel="noopener" class="x-link">X</a>
  </div>
</nav>
'''

SHARE_MODAL = '''<div class="modal" id="share-modal" role="dialog" aria-modal="true" aria-labelledby="share-title">
  <div class="modal-content">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <strong id="share-title">Share</strong>
      <button class="close-x" type="button" data-close-share aria-label="Close">×</button>
    </div>
    <p class="modal-note">Make your own version. It looks exactly like ours but carries your name and handle, so the find is yours. The SocialBrand line and site link stay. No points, no leaderboard.</p>
    <label for="share-name">Your name (optional)</label>
    <input id="share-name" type="text" maxlength="40" placeholder="Your name" autocomplete="name">
    <label for="share-handle">Your handle</label>
    <input id="share-handle" type="text" maxlength="32" placeholder="@handle">
    <div class="share-preview" id="share-preview">
      <div class="shared-by" id="shared-by-label">Shared by @handle</div>
      <div style="display:flex; gap:0.75rem; align-items:center; margin:0.5rem 0;">
        <img id="share-avatar" class="avatar-img" src="/apple-touch-icon.png" alt="">
        <div><strong id="share-bot-name"></strong><div class="meta" id="share-bot-meta"></div></div>
      </div>
      <p class="modal-note" id="share-bot-pitch"></p>
      <div class="meta" style="margin-top:0.5rem;" id="share-url">bots.socialbrand.africa</div>
    </div>
    <div class="row">
      <button class="btn-primary" type="button" id="share-copy-text">Copy share text</button>
      <button class="btn-secondary" type="button" id="share-copy-link">Copy link</button>
    </div>
    <div class="row">
      <button class="btn-secondary" type="button" id="share-download">Download card image</button>
      <button class="btn-secondary" type="button" id="share-x">Post on X</button>
    </div>
  </div>
</div>
'''

def footer():
    bots = ''.join(f'<li><a href="/bots/{b["slug"]}">{E(b["name"])}</a></li>' for b in BOTS)
    return f'''<footer class="footer-note" id="free">
  <div class="disclosure"><p><strong>How we keep it free.</strong> {DISCLOSURE} Free templates. A Grok Bot plan is required to run them. There are no referral links on this site yet.</p></div>
  <div class="footer-cols">
    <div><h4>Bots</h4><ul>{bots}</ul></div>
    <div><h4>Site</h4><ul><li><a href="/">Home</a></li><li><a href="/#how">How Open-Text works</a></li><li><a href="/about">About</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul></div>
    <div><h4>SocialBrand</h4><ul><li>Contact: <a href="https://socialbrand.africa" target="_blank" rel="noopener">socialbrand.africa</a></li><li>On X: <a href="https://x.com/Soc_Bran_Africa" target="_blank" rel="noopener">@Soc_Bran_Africa</a></li></ul></div>
  </div>
  <p style="margin-top:1.25rem;">SocialBrand Bots · bots.socialbrand.africa · By SocialBrand · socialbrand.africa · Open-Text Publishing. Bots run on Grok Bot (<a href="https://x.ai/bot" target="_blank" rel="noopener">x.ai/bot</a>); SocialBrand is independent and not affiliated with, sponsored or endorsed by xAI.</p>
</footer>
<script src="/assets/js/config.js"></script>
<script src="/assets/js/site.js"></script>
</body>
</html>
'''

def share_attrs(b):
    return f'data-share="{b["slug"]}" data-name="{E(b["name"])}" data-version="{b["version"]}" data-pitch="{E(b["pitch"])}" data-avatar="{b["card_avatar"]}"'

PAL = ['mag', 'red', 'amb', 'lime', 'teal', 'blue', 'vio']  # brand clock palette (brand-bible/clocks/flat-v1/palette.json)
def pal(i): return PAL[i % len(PAL)]

TAG_CLS = {'DEV-AGENTS': 'cat-dev', 'PA-DESK': 'cat-pa', 'OWN-OPS': 'cat-own'}

def card(b, i=0):
    soon = b['status'] == 'coming-soon'
    badges = f'<span class="tag {TAG_CLS.get(b["tag"], "")}">{b["tag"]}</span>'.replace('tag ">', 'tag">')
    if soon: badges = '<span class="coming-badge">COMING SOON</span>' + badges
    elif b['status'] == 'install-soon': badges += '<span class="tag" style="color:var(--lime)">NEW</span>'
    else: badges += '<span class="tag" style="color:var(--lime)">LIVE</span>'
    search = ' '.join([b['name'], b['tag'], b['pitch']] + [s['name'] for s in b['skills']]).lower()
    meta = f'{b["version"]} · ' + ('In build' if soon else (f'Updated {b["updated"]}' if b['updated'] else 'Live'))
    return f'''      <article class="card clickable tile lift reveal c-{pal([4, 3, 5, 1, 6, 0, 2][i % 7])} h{2 if i == 0 else 1} m-full d-3{' coming-soon' if soon else ''}" data-slug="{b['slug']}" data-search="{E(search)}">
        <div class="card-top">{badges}</div>
        <div class="card-header">
          <img class="avatar-img" src="{b['card_avatar']}" alt="{E(b['name'])} avatar" width="48" height="48" loading="lazy">
          <div><h3><a href="/bots/{b['slug']}">{E(b['name'])}</a></h3><div class="meta">{meta}</div></div>
        </div>
        <p class="pitch">{E(b['pitch'])}</p>
        <div class="card-actions">
          <button class="upvote" type="button" data-upvote="{b['slug']}" aria-pressed="false">▲ Upvote</button>
          <button class="share-btn" type="button" {share_attrs(b)}>Share</button>
          <a class="btn" href="/bots/{b['slug']}">Read full text →</a>
        </div>
      </article>
'''

CAPS = [('Analyze', 'Turn data into answers.'), ('Flag', 'Catch what needs attention before it\'s a problem.'), ('Automate', 'Turn complex processes into automated workflows and bots.'), ('Act', 'Take real action on your instructions.'), ('Coordinate', 'Coordinate people, bots and workflows.'), ('Learn', 'Gets smarter with every conversation.')]
def caps_html(extra='', big=False):
    def cls(i):
        c = f'cap tile lift reveal c-{pal(i)} h{3 - (i % 3)}'
        if big and i == 0: c += ' hot d-2 d-r2'
        return c
    return '<div class="caps bento">' + ''.join(f'<div class="{cls(i)}"><div class="k">0{i+1}</div><h3>{E(n)}</h3><p>{E(d)}</p></div>' for i, (n, d) in enumerate(CAPS)) + extra + '</div>'

CATEGORIES = (Path(__file__).resolve().parent / 'categories.html').read_text(encoding='utf-8')  # taxonomy v1 section (PR #11)

def index_page():
    cats = sorted({b['tag'] for b in BOTS})
    chips = ''.join(f'<button type="button" class="chip" data-chip="{E(b["name"].lower())}">{E(b["name"])}</button>' for b in BOTS)
    chips += ''.join(f'<button type="button" class="chip" data-chip="{c.lower()}">{c}</button>' for c in cats)
    chips += '<button type="button" class="chip" data-chip="routine">Routines</button><button type="button" class="chip" data-chip="invoice">Invoices</button>'
    cards = ''.join(card(b, i) for i, b in enumerate(BOTS))
    h = head('SocialBrand Bots: free Grok Bot templates for real work', 'Free, open-text Grok Bot templates. A Grok Bot plan is required to run them. Each AI teammate gets one real job, a clear cadence and a specific output. It proposes, you approve, every time. We do the homework so you get a safe head start.', '/', SITE + '/assets/img/og-home.png')
    return h + nav('bots') + f'''<main id="main">
  <section class="hero hero-bento">
   <div class="bento">
    <div class="tile t-hero reveal c-mag h2 m-full t-full d-4 d-r2">
    <div class="eyebrow pink">Grok Bot templates · by SocialBrand</div>
    <h1>AI TEAMMATES<br><span class="neon">FOR REAL WORK</span></h1>
    <p class="hero-sub">One concrete job each. A clear cadence, a specific output, and your OK before anything goes out.</p>
    <form class="hero-search" id="hero-search-form" role="search">
      <input id="hero-search" type="search" placeholder="Search bots, skills, routines…" aria-label="Search bots">
      <button type="submit">Search</button>
    </form>
    <div class="chips">{chips}</div>
    </div>
    <div class="tile lift reveal c-teal h2 m-full t-full d-2"><p class="lead"><strong>We scout the use-cases and do the homework,</strong> so you get a head start. Every bot is a Grok Bot template: skills and routines for one job, connected to the tools you already use. Easy, safe rollouts. <strong>Economy first, with no compromise on quality.</strong> Free, with the full text open. A Grok Bot plan is required to run them.</p></div>
    <div class="tile lift reveal hot c-amb m-full t-full d-2"><p class="lead"><strong>Not a chatbot you have to babysit.</strong> It proposes, you approve, every time. You decide exactly what it can access and who's allowed to ask it to act.</p></div>
    <div class="tile t-mono reveal h1 m-full t-full d-6"><p class="indep">Built for <a href="https://x.ai/bot" target="_blank" rel="noopener">Grok Bot</a> (official site: <a href="https://x.ai" target="_blank" rel="noopener">x.ai</a>). SocialBrand is independent: not affiliated with, sponsored or endorsed by xAI.</p></div>
   </div>
  </section>

{flow_home()}
  <section class="section" id="bots">
    <div class="eyebrow lime">Catalogue</div>
    <h2 class="section-title">{len(BOTS)} bots, full text open</h2>
    <div class="sort-row"><span class="meta">Sort:</span><button type="button" class="chip on" data-sort="new">Newest</button><button type="button" class="chip" data-sort="upvoted">My upvotes first</button></div>
    <div class="grid bento" id="catalogue">
{cards}    </div>
    <p class="empty-note hidden" id="no-results">No bot matches that yet. Try another word, or tell us what you need on X.</p>
  </section>

{CATEGORIES}
  <section class="section">
    <div class="eyebrow cyan">What every SocialBrand bot does</div>
    <h2 class="section-title">Six jobs, one standard</h2>
    {caps_html('<p class="statement tile reveal c-vio h3 m-full t-full d-3">Every week you do it by hand <span class="neon">is a week someone automated it</span></p>', big=True)}
  </section>

  <section class="section" id="how">
    <div class="eyebrow pink">Open-Text Publishing</div>
    <h2 class="section-title">How Open-Text works</h2>
    <ol class="numbered bento">
      <li class="tile lift reveal c-mag h1 m-full d-2"><div><strong>The full text is on the page.</strong> Every instruction, skill, routine and avatar prompt, with a copy button on each. Nothing hidden.</div></li>
      <li class="tile lift reveal c-red h2 m-full d-2"><div><strong>X carries the economy version.</strong> A shorter text that works on its own and keeps every safety and hard rule. Safety is never trimmed.</div></li>
      <li class="tile lift reveal c-amb h3 m-full d-2"><div><strong>Paste to run.</strong> Reading and pasting the text into a new Grok Bot is the main route. You see exactly what you install.</div></li>
      <li class="tile lift reveal c-lime h1 m-full d-2"><div><strong>One-click install is there, never the headline.</strong> Each bot page shows its install link in the side panel, with the plain URL.</div></li>
      <li class="tile lift reveal c-teal h2 hot m-full d-2"><div><strong>Nothing changes without your yes.</strong> Routines ship paused. No bot contacts your customers. Every external send needs your OK for that exact message.</div></li>
      <li class="tile lift reveal c-blue h3 m-full d-2"><div><strong>Share it as yours.</strong> The Share button makes your own version with your name and handle. Our brand line and site link stay. No points, no credit system.</div></li>
    </ol>
  </section>

  <section class="section">
    <div class="eyebrow lime">Latest</div>
    <h2 class="section-title">Latest updates</h2>
    <ul class="updates bento">
      <li class="tile lift reveal c-lime h3 m-full d-2"><span class="date">24-10-2026</span> · bots.socialbrand.africa opens with Open-Text Publishing: full text here, economy text on X.</li>
      <li class="tile lift reveal c-teal h3 m-full d-2"><span class="date">30-10-2026</span> · Token Cop v0.7: proposes a cheap gate so routines stop waking the model for nothing, and bots brief once with no relay loops.</li>
      <li class="tile lift reveal c-teal h3 m-full d-2"><span class="date">24-10-2026</span> · Token Cop v0.6: map your AI usage and set your own rules, right after setup.</li>
      <li class="tile lift reveal c-blue h2 m-full d-2"><span class="date">24-10-2026</span> · Earlier: Token Cop v0.3.2 went live.</li>
      <li class="tile lift reveal c-vio h2 m-full d-2"><span class="date">24-10-2026</span> · Grok Bot Setup Coach v1.0 text published. Token Cop becomes its companion.</li>
      <li class="tile lift reveal c-mag h1 m-full d-2"><span class="date">24-10-2026</span> · Gatekeeper v1.6 listed. Browser-access governance for bot fleets.</li>
      <li class="tile lift reveal c-red h1 m-full d-2"><span class="date">24-10-2026</span> · Supplier Order Checker v0.3 in build. Draft text open now.</li>
    </ul>
  </section>

  <section class="section">
    <div class="eyebrow pink">FAQ</div>
    <h2 class="section-title">Common questions</h2>
    <ol class="numbered bento faq">
      <li class="tile lift reveal c-teal h1 m-full d-3"><div><strong>How do I install a bot?</strong> Copy the economy text or the full text into a new Grok Bot. The one-click link is there too, as the secondary route.</div></li>
      <li class="tile lift reveal c-amb h1 m-full d-3"><div><strong>Are the bots free?</strong> Yes, the templates are free. A Grok Bot plan is required to run them. See <a href="#free" style="color:var(--cyan)">How we keep it free</a> below.</div></li>
      <li class="tile lift reveal c-mag h1 m-full d-2"><div><strong>Who approves actions?</strong> You do. Every bot waits for your explicit yes. Nothing is installed, paused, sent or delegated until you say so.</div></li>
      <li class="tile lift reveal c-blue h1 m-full d-2"><div><strong>Can I share a bot as mine?</strong> Yes. Share makes a version with your name and handle. Our brand line and link stay on it.</div></li>
      <li class="tile lift reveal c-lime h1 m-full t-full d-2"><div><strong>How do upvotes work?</strong> Your upvote is saved in your browser for now. Shared counts come later.</div></li>
    </ol>
  </section>
</main>
''' + SHARE_MODAL + footer()

SEC_C = {'pink': 'mag', 'lime': 'lime', 'cyan': 'teal', 'teal': 'teal'}
def fold(inner, label='Show all'):
    """Long full-text block: open on desktop, collapsed by default on mobile (site.js), with a big Copy button in the header."""
    return f'<details class="fold" data-fold-mobile open><summary class="fold-sum"><span class="when-closed">{label}</span><span class="when-open">Show less</span></summary><div class="fold-body">{inner}</div></details>'

def section(id_, title, color, body, copy_id=None, extra_btn=''):
    btn = f'<button class="copy-btn" type="button" data-copy="{copy_id}">Copy</button>' if copy_id else ''
    return f'''      <section class="section-block tile reveal c-{SEC_C.get(color, 'teal')} h1" id="{id_}">
        <div class="header-row"><h2 class="neon-header {color}">{title}</h2><div>{extra_btn}{btn}</div></div>
{body}
      </section>
'''

def pre(id_, text, trunc=False):
    t = ' truncated' if trunc else ''
    s = f'<pre class="block-text{t}" id="{id_}">{(E if id_ == 'selling-text' else EP)(text)}</pre>'
    if trunc: s += f'<button class="show-all" type="button" data-toggle="{id_}">Show all</button>'
    return s

def bot_page(b):
    CUR['slug'] = b['slug']
    c = BY[b['companion']]
    slug = b['slug']
    h = head(f'{b["name"]} {b["version"]} · SocialBrand Bots', f'{b["pitch"]}{(" " + b["meta_extra"]) if b.get("meta_extra") else ""} Free, full open text. A Grok Bot plan is required to run it. By SocialBrand.', f'/bots/{slug}', b['og'], 'article')
    soon = b['status'] == 'coming-soon'
    neon = b['neon']
    style = {'pink': '', 'lime': ' style="background:var(--lime); color:#000; text-shadow:3px 3px 0 #fff;"', 'cyan': ' style="background:var(--cyan); color:#000; text-shadow:3px 3px 0 #fff;"'}[neon]
    badges = f'<span class="badge strong">{b["version"]}</span>' + (f'<span class="badge">Last updated {b["updated"]}</span>' if b['updated'] else '<span class="badge">Live</span>')
    badges += '<span class="badge">In build · not yet published</span>' if soon else '<span class="badge strong">Full open text</span><span class="badge strong">Routines ship paused</span>'
    badges += '<span class="badge">By SocialBrand · socialbrand.africa</span>'
    note = b.get('note')
    banner = f'<div class="banner{" soon" if soon else ""}"><div class="inner">{E(note)}</div></div>' if note else ''
    toc = ''.join(f'<a href="#{i}">{t}</a>' for i, t in [('economy', 'Economy text'), ('profile', 'Profile'), ('instructions', 'Instructions'), ('skills', 'Skills'), ('routines', 'Routines'), ('avatar', 'Avatar'), ('selling', 'Selling points')] + ([('docs', 'Docs')] if b.get('docs') else []) + [('companion', 'Companion')])
    # economy
    if b['economy']:
        econ = f'''      <section class="section-block economy tile reveal c-lime h2" id="economy">
        <div class="header-row"><h2 class="neon-header lime">Economy text · paste to run</h2><button class="copy-btn" type="button" data-copy="economy-text">Copy</button></div>
        {fold(pre('economy-text', b['economy'], True))}
        <p class="econ-note">The short version that works on its own and keeps every safety and hard rule. This is the text we post on X. The full text is below.</p>
      </section>
'''
    else:
        econ = '''      <section class="section-block economy tile reveal c-lime h2" id="economy">
        <div class="header-row"><h2 class="neon-header lime">Economy text · paste to run</h2></div>
        <p class="econ-note">Economy text coming soon. Until then, copy the full text in the sections below.</p>
      </section>
'''
    skills = ''
    for i, s in enumerate(b['skills']):
        sid = f'skill-{i+1}'
        skills += f'''        <div class="skill-full">
          <div class="skill-head"><div><span class="skill-name">{E(s['name'])}</span><div class="skill-desc">{E(s['desc'])}</div></div><button class="copy-btn" type="button" data-copy="{sid}">Copy</button></div>
          {pre(sid, s['text'], True)}
        </div>
'''
    skills_all = '\n\n'.join(s['text'] for s in b['skills'])
    skills += f'<textarea class="hidden" id="skills-all" aria-hidden="true" tabindex="-1">{E(skills_all)}</textarea>'
    routines = md_table(b['routines']) + f'<div class="paused-note">{E(b["routines_note"])}</div><textarea class="hidden" id="routines-text" aria-hidden="true" tabindex="-1">{E(b["routines"])}</textarea>'
    av = '<p class="avatar-note">' + ('Three options. Pick one at install; the bot sets that exact image on first run.' if len(b['avatar_files']) == 3 else (('The current avatar. More options coming.' if b['avatar_more'] else f'The approved avatar. Installed bots download it from {SITE}/bots/{b["slug"]}/avatar.png.') if b['avatar_files'] else 'Avatar options coming, after review.')) + '</p><div class="avatar-options">'
    for src, label in b['avatar_files']:
        av += f'<figure class="avatar-opt"><img src="{src}" alt="{E(b["name"])} avatar {'option' if len(b['avatar_files']) > 1 else '·'} {E(label)}" width="140" height="140" loading="lazy"><figcaption class="avatar-label">{E(label)}</figcaption></figure>'
    if b['avatar_more']:
        av += '<figure class="avatar-opt more"><div class="avatar-sq">More options coming</div><figcaption class="avatar-label">B and C</figcaption></figure>'
    av += '</div>' + pre('avatar-prompt', b['avatar_prompt'], True)
    instr_note = f'<p class="meta" style="margin-bottom:.5rem;">{E(b["instructions_note"])}</p>' if b.get('instructions_note') else ''
    pc = b['promo']
    comp_link = f'/bots/{c["slug"]}'
    promo = f'''      <section class="companion-promo reveal {pc[3]}" id="companion">
        <div class="avatar-lg"><img src="{c['card_avatar']}" alt="{E(c['name'])} avatar" width="140" height="140" loading="lazy"></div>
        <div>
          <div class="eyebrow">Companion bot · {E(c['name'])}</div>
          <h2>{E(pc[0])}<br><span class="switched">{E(pc[1])}</span></h2>
          <p>{E(pc[2])}</p>
          <div class="promo-btns">
            <a href="{comp_link}" class="btn-primary">Get {E(c['name'])} free →</a>
            <a href="{comp_link}#instructions" class="btn-secondary">Read its full text</a>
          </div>
        </div>
      </section>
'''
    body = econ
    body += section('profile', 'Profile', 'pink', fold(pre('profile-text', b['profile'])), 'profile-text')
    body += section('instructions', 'Instructions', 'lime', instr_note + fold(pre('instr-text', b['instructions'], True)), 'instr-text')
    body += section('skills', f'Skills · {len(b["skills"])}', 'cyan', skills, 'skills-all')
    body += section('routines', 'Routines', 'pink', routines, 'routines-text')
    body += section('avatar', 'Avatar', 'lime', av, 'avatar-prompt').replace('data-copy="avatar-prompt">Copy<', 'data-copy="avatar-prompt">Copy prompt<')
    body += section('selling', 'Selling points', 'cyan', pre('selling-text', b['selling']), 'selling-text')
    if b.get('docs'):
        base = f'https://github.com/SocialBrandAfrica/socialbrand-bots/blob/main/packages/{b["docs"]}/docs/'
        dl = ''.join(f'<li><a href="{base}{f}.md" target="_blank" rel="noopener" style="color:var(--cyan);">{f}.md</a> · {E(d)}</li>' for f, d in [('README', 'What it does, routines, skills, hard rules'), ('SETUP', 'Step-by-step first run and a short test'), ('FAQ', 'Common questions, limits and costs'), ('TROUBLESHOOTING', 'The most likely failures and the fix for each')])
        st = f'<p class="meta" style="margin-bottom:.5rem;">Setup time: {E(b["setup_time"])}</p>' if b.get('setup_time') else ''
        body += f'''      <section class="section-block tile reveal c-mag h1" id="docs">
        <div class="header-row"><h2 class="neon-header pink">Docs</h2></div>
        {st}<ul>{dl}</ul>
      </section>
'''
    body += promo
    install_html = '<span class="install-soon">Install link coming soon</span>' if b['status'] != 'live' else '<a class="btn-secondary" href="https://x.ai/bot/" target="_blank" rel="noopener">One-click install (secondary)</a>'
    n_routines = md_table(b['routines']).count('<tr>') - 1  # same rows the Routines table shows
    return h + nav() + f'''<div class="banner shared-banner" id="shared-banner"><div class="inner" id="shared-banner-text"></div></div>
{banner}
<main id="main">
  <section class="hero bot-hero">
    <div class="eyebrow cyan">{b['tag']} · Grok Bot · {b['version']}</div>
    <h1>{E(b['headline'][0])}<br><span class="neon"{style}>{E(b['headline'][1])}</span></h1>
    <div class="bento summary">
      <div class="tile reveal c-teal h2 m-full t-full d-3 sum-what"><div class="tile-label">What it does</div><p class="lead">{(('<strong>' + E(b['hello']) + '</strong> ') if b.get('hello') else '') + E(b['pitch'])}</p></div>
      <div class="tile lift reveal hot c-lime m-full d-1 sum-ver"><div class="tile-label">Version</div><div class="big">{b['version']}</div><div class="tile-sub">{('Last updated ' + b['updated']) if b['updated'] else 'Live'}</div></div>
      <a class="tile lift reveal c-amb h2 d-1 sum-num" href="#routines"><div class="tile-label">Routines</div><div class="big">{n_routines}</div><div class="tile-sub">{'In build' if soon else 'Routines ship paused'}</div></a>
      <a class="tile lift reveal c-vio h2 d-1 sum-num" href="#skills"><div class="tile-label">Skills</div><div class="big">{len(b['skills'])}</div><div class="tile-sub">Full open text</div></a>
      <div class="tile reveal c-mag h2 m-full d-2 sum-install"><div class="tile-label">Install</div><p class="small">Main route: copy the economy text or the full text and paste it into a new Grok Bot. One-click is secondary.</p><div class="install-box" data-install="{slug}">{install_html}</div></div>
      <div class="tile reveal c-blue h1 m-full t-full d-4 sum-act"><div class="trust-badges">{badges}</div>
        <div class="hero-actions">
          <button class="upvote" type="button" data-upvote="{slug}" aria-pressed="false">▲ Upvote</button>
          <button class="btn-primary" type="button" {share_attrs(b)}>Share</button>
          <a class="btn-secondary" href="/#catalogue">← Catalogue</a>
        </div></div>
      {('<div class="tile reveal c-red h2 m-full t-full d-6 sum-job"><p class="first-job"><span class="badge strong">New</span> ' + E(b['first_job']) + '</p></div>') if b.get('first_job') else ''}
    </div>
    <nav class="toc" aria-label="On this page">{toc}</nav>
{flow_compact(b['name'], b['status'] == 'live')}  </section>
  <div class="bot-layout">
    <div class="main">
{body}    </div>
    <aside class="side-panel tile reveal c-teal h1">
      <h4>Can access</h4>{lst(b['can'])}
      <h4>Cannot access</h4>{lst(b['cannot'])}
      {('<h4>New in ' + b['version'] + '</h4>' + lst(b['new']) + chr(10) + '      ') if b.get('new') else ''}<h4>Hard rules</h4>{lst(b['rules'])}
      <h4>Install</h4>
      <p class="small">Main route: copy the economy text or the full text and paste it into a new Grok Bot. One-click is secondary.</p>
      <div class="install-box" data-install="{slug}">{'<span class="install-soon">Install link coming soon</span>' if b['status'] != 'live' else f'<a class="btn-secondary" href="https://x.ai/bot/" target="_blank" rel="noopener">One-click install (secondary)</a>'}</div>
      <h4 style="margin-top:1.5rem;">More</h4>
      <p class="small"><a href="/about#contribute" style="color:var(--cyan);">Contribute</a> · <a href="https://x.com/Soc_Bran_Africa" target="_blank" rel="noopener" style="color:var(--cyan);">Follow on X</a></p>
    </aside>
  </div>
</main>
''' + SHARE_MODAL + footer()

def about_page():
    h = head('About SocialBrand Bots', 'AI teammates for real work: free Grok Bot templates by SocialBrand. A Grok Bot plan is required to run them. Economy first, no compromise on quality. It proposes, you approve, every time.', '/about', SITE + '/assets/img/og-home.png')
    return h + nav('about') + f'''<main id="main">
  <section class="hero">
    <div class="eyebrow pink">About · Manifesto</div>
    <h1>AI TEAMMATES<br><span class="neon">FOR REAL WORK</span></h1>
    <div class="prose">
      <p class="lead">Grok Bot teammates for very specific niche jobs, running routines on a clear cadence to automate what we do. We scout the use-cases and do the homework, so you get a head start. <strong>Economy first, with no compromise on quality.</strong> Connected to the tools you already use, working right alongside your team. Then shared with the community, free. A Grok Bot plan is required to run them.</p>
    </div>
  </section>
  <section class="section">
    <div class="eyebrow lime">What every SocialBrand bot does</div>
    <h2 class="section-title">Six jobs</h2>
    {caps_html()}
  </section>
  <section class="section">
    <div class="eyebrow cyan">How they behave</div>
    <h2 class="section-title">Not a chatbot you babysit</h2>
    <div class="prose">
      <p><strong>It proposes, you approve, every time.</strong> You decide exactly what it can access and who's allowed to ask it to act.</p>
      <p><strong>Any workflow you can imagine, across your work tools, can be automated.</strong></p>
      <p><strong>Built security-first from day one,</strong> so it's not just fast, it's safe to run your real work through. No bot contacts your customers. Every external send needs your OK for that exact message. Payments, banking and brokers stay human-only. Passwords never go in chat.</p>
      <p><strong>Specialists, not a pile of bots.</strong> Where jobs overlap, we fold them into one specialist per field, so you run a few strong bots instead of ten small ones.</p>
    </div>
    <p class="statement">Every week you keep doing this by hand <span class="neon">is a week someone else already automated it</span></p>
  </section>
  <section class="section">
    <div class="eyebrow pink">The Foundry standard</div>
    <h2 class="section-title">How a bot gets on this site</h2>
    <ol class="numbered">
      <li><div><strong>16 checks before publishing.</strong> Hard rules present, no private data, a refusal test, a health-check routine, a category tag and a brand line.</div></li>
      <li><div><strong>Versions step by 0.3.</strong> v0.3, v0.6, v1.0, v1.3 and on. Each release gets a changelog line.</div></li>
      <li><div><strong>Three avatar options.</strong> One bold object, no people, no logos. You pick one at install.</div></li>
      <li><div><strong>A companion bot.</strong> Related bots recommend each other both ways. Recommend only; never installed for you.</div></li>
      <li><div><strong>Routines ship paused.</strong> You turn them on.</div></li>
    </ol>
  </section>
  <section class="section" id="contribute">
    <div class="eyebrow lime">Contribute</div>
    <h2 class="section-title">Contribute a bot</h2>
    <div class="prose"><p>Got a niche job your bot does well? Tell us on X at <a href="https://x.com/Soc_Bran_Africa" target="_blank" rel="noopener" style="color:var(--cyan)">@Soc_Bran_Africa</a>. Contributions follow the same Foundry standard: full open text, three avatar options, routines paused. A contribute form comes later.</p>
    <p>Contact: <a href="https://socialbrand.africa" target="_blank" rel="noopener" style="color:var(--cyan)">socialbrand.africa</a></p></div>
  </section>
</main>
''' + footer()

def main():
    # clean generated content but keep assets css/js
    for p in (['bots', 'assets/img'] if IMAGES else []):
        shutil.rmtree(OUT/p, ignore_errors=True)
    (OUT/'assets/img').mkdir(parents=True, exist_ok=True)
    setup_assets(); site_assets()
    (OUT/'index.html').write_text(index_page())
    (OUT/'about.html').write_text(about_page())
    for b in BOTS:
        d = OUT/'bots'/b['slug']; d.mkdir(parents=True, exist_ok=True)
        page = bot_page(b)
        # live bots: static fallback link = configured link (JS re-renders from config.js anyway)
        links = {'token-cop': 'https://x.ai/bot/kikx0ydzAGu5ogL2Hfato', 'grok-bot-setup-coach': 'https://x.ai/bot/duonwBK5SXXQTAy6NNg2r', 'gatekeeper': 'https://x.ai/bot/D03y99U4zXKh0cshnhgah'}
        if b['slug'] in links: page = page.replace('href="https://x.ai/bot/"', f'href="{links[b["slug"]]}"')
        (d/'index.html').write_text(page)
    urls = ['/', '/about'] + [f'/bots/{b["slug"]}' for b in BOTS]
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}{u if u != "/" else "/"}</loc><lastmod>2026-10-24</lastmod></url>\n' for u in urls) + '</urlset>\n')
    (OUT/'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    (OUT/'vercel.json').write_text(json.dumps({
        "cleanUrls": True, "trailingSlash": False,
        "headers": [{"source": "/(.*)", "headers": [
            {"key": "X-Content-Type-Options", "value": "nosniff"},
            {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
            {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
            {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"}]},
            {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600"}]}]
    }, indent=2) + '\n')
    print('built', urls)

main()
