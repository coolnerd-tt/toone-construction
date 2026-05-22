# Toone Construction Co.

A fictional Utah commercial + civil general contractor. This repo is the **default tenant** of a reusable digital-engagement proposal template — the showcase deliverable for prospective construction-industry clients.

## What this is

Everything you see here was originally built for a real Utah heavy-civil contractor (Jones × Callus). When that deal didn't close, the work was duplicated and genericized into a portable template that we can re-skin for any new construction-industry prospect in roughly 30 minutes.

The default content portrays **Toone Construction Co.** — a ~35-year-old Utah GC doing commercial buildings + civil work. Use this as-is to show prospects the depth of what a 90-day digital engagement produces, or swap the tenant config to demo the same proposal for a specific prospect.

## Structure

```
toone-construction/
├── tenant.json              ← edit this to re-skin
├── proposal/                ← PDF builders (read tenant.json)
├── site/                    ← single-brand website concept
├── landing/                 ← public proposal landing page
├── marketing-os/            ← diagram, day-in-the-life, sample, interactive mock
├── assets/                  ← logo, photography, brand kit
└── outputs/                 ← generated PDFs
```

## Re-skin for a new prospect (30 minutes)

1. **Copy this repo** to a new folder: `cp -r toone-construction newclient-name`
2. **Edit `tenant.json`** — replace Toone fields with the prospect's:
   - `company.*` (name, founded, services, market)
   - `comp_set.competitors` (research 5–8 LinkedIn peers in their region)
   - `comp_set.tenant_starting_*` (their current LinkedIn / GBP baseline)
   - `pricing.*` (adjust scope; keep MOS retainer model)
   - `target_keywords` (their geo + service combos)
   - `case_studies` (their real projects, if available, or remove the section)
3. **Drop in their logo** at `assets/logo/` and update `brand.primary_color` in `tenant.json`
4. **Re-run the build:** `python3 proposal/build_proposal.py`
5. **Preview the landing page** locally, push to a per-prospect GitHub Pages URL, or just email the PDF

## Build commands

```bash
# Full proposal PDF (~17 pages)
python3 proposal/build_proposal.py

# 1-page executive leave-behind
python3 proposal/build_one_pager.py

# Open landing page locally
open landing/landing.html
```

## What's in scope for the Toone case study

- One coordinated brand refresh (no sub-brand)
- One production website (`tooneconstruction.com`) with services pages, service-area pages, project showcase, and careers
- Photography + video (3-day jobsite shoot)
- SEO foundation: Google Business Profile, structured data, business listings, target-keyword SA pages
- Content engine: 90-day post library + 2 hype videos
- Marketing Operating System: five agents, approval queue, brand-voice training, full support, monthly reporting

## Pricing model (Toone defaults)

| Item | One-time | Monthly |
|------|---------:|--------:|
| Brand refresh | $7,500 | — |
| Website | $22,500 | — |
| SEO foundation | $5,000 | — |
| Photography | $7,500 | — |
| Content engine | $5,000 | — |
| Marketing Operating System (build) | $17,700 | — |
| **Build total** | **$65,200** | |
| Concierge retainer (months 1–3 post-launch) | — | Included in MOS build |
| Co-pilot retainer (months 4–6 post-launch) | — | $850 |
| Self-serve retainer (month 7+) | — | up to $350 + ~$200 infra |

## Credits

© 2026  JTC Communications & Consulting, LLC and Coolnerd, LLC

Built from the Jones × Callus engagement (2026). Toone Construction Co. is a fictional company used solely for demonstration purposes.
