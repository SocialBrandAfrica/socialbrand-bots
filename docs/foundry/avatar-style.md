# SocialBrand bot avatar style guide v1 (24-10-2026)

Why: the early setup-type bots all landed on a checkmark, so the catalogue read as one "tick" family. Now the **site category** (`category_id` in profile.json) decides the symbol family and colour family. The bot's own job picks the exact symbol inside that family.

This guide sits alongside check #12 of the [bot standard](standard.md) (one bold, high-contrast, logo-style central object; no people, no logos). It does not replace it. Where the two differ, follow this guide for symbol and colour, and #12 for contrast.

## Shared rules (every category)

1. **Style:** flat vector, logo-style, thick shapes, no fine detail, no gradients, no 3D bevel, no drop shadow, no glow, no vignette.
2. **Shape:** rounded-square tile, 1024x1024, corner radius 18% (applied by a finishing script after generation). Keep the symbol inside the central circle (about 70% of the width) so a round crop still works.
3. **One central symbol:** it fills 50-60% of the tile. Add at most one small accent in the category's accent colour.
4. **No text:** no letters, numbers, initials or words, not even an "S" placeholder.
5. **48px test:** shrink to 48x48 and the symbol must still read. If it doesn't, simplify it.
6. **Contrast:** a white symbol on the category's dark background. In categories with a light background (OWN-GROWTH), use the category's ink colour.
7. **Corner mark:** a small white four-point spark at 79%/79% (bottom right, inside the round-crop safe zone), 80% opacity. The finishing script adds it. Never ask the image model to draw it.
8. **Checkmark rule:** the checkmark is reserved for bots whose core job is approving or verifying (an auditor, a checker, a reviewer). Even then it is a **secondary detail**: a badge or label no bigger than about 20% of the symbol. It is **never the main symbol** and never the biggest stroke in the image. Every other bot uses no tick at all.
9. **Background rule:** a full-bleed, solid, flat category background. No rings, frames or circles around the symbol, and no white or transparent background. Bots in the same category vary their symbol, not their background. If two bots in one category look too alike, move one of them to the category's alt background.
10. **Variety inside a category:** each bot gets a different symbol from its family. Don't reuse another bot's main symbol.

## Category → symbol family and colours

| Category | Symbol family (pick one per bot) | Background | Alt background | Symbol | Accent | Background rule |
|---|---|---|---|---|---|---|
| DEV-TOOLS (Code and repos) | code brackets `</>` as shapes, git branch, terminal window, merge arrows | slate #1E293B | #0F172A | white #FFFFFF | electric blue #38BDF8 | dark solid |
| DEV-AGENTS (Bots and automation) | guard and control instruments: shield, gate, keyhole, key, gauge or meter, lens | deep teal #0F5E5A | teal #0E7C7B (or #01AEB4, Token Cop's) | white #FFFFFF | amber #F59E0B | dark teal solid |
| DEV-DATA (Data and APIs) | bar chart, radar sweep, pulse line, telescope, database cylinder | violet #4C1D95 | #5B21B6 | white #FFFFFF | cyan #22D3EE | dark solid |
| LIFE-MONEY (Personal money) | coin, coin stack, ledger book, wallet, piggy bank | emerald #065F46 | #047857 | white #FFFFFF | gold #FBBF24 | dark solid |
| LIFE-HOME (Home, family, travel) | house, suitcase, key ring, map pin, family calendar | terracotta #9A3412 | #C2410C | white #FFFFFF | peach #FDBA74 | dark solid |
| LIFE-WELL (Health, learning, hobbies) | leaf, sprout, open book, dumbbell, paintbrush | forest #365314 | #3F6212 | white #FFFFFF | lime #A3E635 | dark solid |
| PA-DESK (Desk and setup) | envelope, calendar page, desk lamp, speech bubble with tool, inbox tray | navy #0B1F3F | #13294B | white #FFFFFF | sky blue #60A5FA | dark solid |
| PA-COMMS (Content and comms) | megaphone, pen nib, quote marks, microphone, speech bubbles | plum #831843 | #9D174D | white #FFFFFF | pink #F472B6 | dark solid |
| OWN-OPS (Store and operations) | shipping box, crate, delivery truck, pallet, receipt or invoice sheet, shelf | charcoal #1F2937 | #374151 | white #FFFFFF | safety orange #F97316 | dark solid |
| OWN-GROWTH (Sales and customers) | funnel, rising arrow, target, handshake shapes, star rating | amber #F59E0B | #FBBF24 | ink #111827 | coral #EF4444 | light solid; the symbol is dark |

## Ready prompt templates for GenerateImage

Fill in `{SYMBOL}` (one item from the family, adapted to the bot's job) and `{ACCENT_DETAIL}` (one small detail). Then run the finishing script on the result. It adds the rounded corners and the corner mark.

Common tail (append to every prompt):
`Symbol fills about 55% of the canvas, centred, generous padding. No text, no letters, no numbers, no checkmark unless stated as a tiny secondary badge, no people, no logos, no ring or frame. Flat, no gradient, no shadow. Readable at 48px.`

- **DEV-TOOLS:** `Flat vector app icon, square, full-bleed solid slate background (#1E293B). One bold central white symbol: {SYMBOL} (e.g. a git branch with three nodes), thick simple geometry, logo-style. One small electric blue (#38BDF8) accent: {ACCENT_DETAIL}.` + tail
- **DEV-AGENTS:** `Flat vector app icon, square, full-bleed solid deep teal background (#0F5E5A). One bold central white symbol: {SYMBOL} (e.g. a shield with a keyhole cut-out), thick simple geometry, logo-style. One small amber (#F59E0B) accent: {ACCENT_DETAIL}.` + tail
- **DEV-DATA:** `Flat vector app icon, square, full-bleed solid violet background (#4C1D95). One bold central white symbol: {SYMBOL} (e.g. a radar sweep with one blip), thick simple geometry, logo-style. One small cyan (#22D3EE) accent: {ACCENT_DETAIL}.` + tail
- **LIFE-MONEY:** `Flat vector app icon, square, full-bleed solid emerald background (#065F46). One bold central white symbol: {SYMBOL} (e.g. a stack of three coins), thick simple geometry, logo-style. One small gold (#FBBF24) accent: {ACCENT_DETAIL}.` + tail
- **LIFE-HOME:** `Flat vector app icon, square, full-bleed solid terracotta background (#9A3412). One bold central white symbol: {SYMBOL} (e.g. a simple house with a door), thick simple geometry, logo-style. One small peach (#FDBA74) accent: {ACCENT_DETAIL}.` + tail
- **LIFE-WELL:** `Flat vector app icon, square, full-bleed solid forest green background (#365314). One bold central white symbol: {SYMBOL} (e.g. a sprout with two leaves), thick simple geometry, logo-style. One small lime (#A3E635) accent: {ACCENT_DETAIL}.` + tail
- **PA-DESK:** `Flat vector app icon, square, full-bleed solid deep navy background (#0B1F3F). One bold central white symbol: {SYMBOL} (e.g. an envelope with a curved return arrow), thick simple geometry, logo-style. One small sky blue (#60A5FA) accent: {ACCENT_DETAIL}.` + tail
- **PA-COMMS:** `Flat vector app icon, square, full-bleed solid plum background (#831843). One bold central white symbol: {SYMBOL} (e.g. a megaphone), thick simple geometry, logo-style. One small pink (#F472B6) accent: {ACCENT_DETAIL}.` + tail
- **OWN-OPS:** `Flat vector app icon, square, full-bleed solid charcoal background (#1F2937). One bold central white symbol: {SYMBOL} (e.g. a closed shipping box with taped lid), thick simple geometry, logo-style. One small safety orange (#F97316) accent: {ACCENT_DETAIL}.` + tail
- **OWN-GROWTH:** `Flat vector app icon, square, full-bleed solid amber background (#F59E0B). One bold central dark ink (#111827) symbol: {SYMBOL} (e.g. a sales funnel with a small arrow out of the bottom), thick simple geometry, logo-style. One small coral (#EF4444) accent: {ACCENT_DETAIL}.` + tail

Checker or verifier bots only: add `Secondary detail only: a tiny {accent colour} circular badge containing a small tick, much smaller than the main symbol.`

## Where approved avatars live

Each published bot's approved avatar sits at a stable public path. Installed bots download their avatar from there.

| Bot | Category | Avatar | Public path |
|---|---|---|---|
| Token Cop | DEV-AGENTS | Option A: white stopwatch gauge on teal | https://bots.socialbrand.africa/bots/token-cop/avatar.png |
| Grok Bot Setup Coach | PA-DESK | Style-guide avatar: spanner in a speech bubble on navy | https://bots.socialbrand.africa/bots/grok-bot-setup-coach/avatar.png |
| Gatekeeper | DEV-AGENTS | Option A: shield with a tick (approved before this guide) | https://bots.socialbrand.africa/bots/gatekeeper/avatar.png |
| Supplier Order Checker | OWN-OPS | Style-guide avatar: shipping box with an orange label on charcoal | https://bots.socialbrand.africa/bots/supplier-order-checker/avatar.png |

Approved avatars are flagged, never silently replaced. A new avatar needs the publisher's approval and a date in profile.json (`avatar_approved`, `avatar_approved_date`, `avatar_approved_option`).

By SocialBrand · socialbrand.africa
