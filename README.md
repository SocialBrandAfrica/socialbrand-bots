# SocialBrand Bots: bots.socialbrand.africa

Static site (plain HTML, CSS, JS; no build step) for Vercel. `vercel.json` sets `cleanUrls` and `trailingSlash: false`, so pages serve at `/about` and `/bots/<slug>`.

- Bot pages: `/bots/token-cop`, `/bots/grok-bot-setup-coach`, `/bots/gatekeeper`, `/bots/supplier-order-checker`
- One-click install links live in **one place**: `assets/js/config.js` (`installLinks`). Token Cop's is empty until its link exists; the page shows "Install link coming soon".
- Upvotes are stored per browser (localStorage). No backend.
- Share builds a "Shared by @handle" card; the SocialBrand line and site link always stay. No credit system.

How we keep it free: some links are referral links, and we say so next to them. Every link also has a plain version. There are no referral links yet.

By SocialBrand · socialbrand.africa
