"""
One-page executive summary — leave-behind for prospects.
Reads tenant.json so it stays in sync with the full proposal.
"""
import os, json
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

BLACK    = HexColor('#0C0E10')
CHARCOAL = HexColor('#161A1D')
ORANGE   = HexColor('#E8621A')
AMBER    = HexColor('#F5A623')
WHITE    = HexColor('#FFFFFF')
GRAY_50  = HexColor('#FAFAF8')
GRAY_300 = HexColor('#D1CFC9')
GRAY_500 = HexColor('#8A8880')
GRAY_700 = HexColor('#4A4845')

W, H = letter

# ── TENANT CONFIG ─────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE, 'tenant.json'), 'r', encoding='utf-8') as _f:
    TENANT = json.load(_f)
COMPANY = TENANT['company']
PRICING = TENANT['pricing']
COMPS   = TENANT['comp_set']
META    = TENANT['proposal_meta']

LOGO_PATH = os.path.join(BASE, 'assets/logo/toone-logo.png')
OUTPUT    = os.path.join(BASE, 'outputs', f"{COMPANY['short_name'].lower().replace(' ', '_')}_one_pager.pdf")

# Derived numbers
BUILD_TOTAL    = sum(PRICING['build'].values())
COMBINED_TOTAL = BUILD_TOTAL + PRICING['mos_build']

def S(n, **kw): return ParagraphStyle(n, **kw)

eyebrow = S('eb', fontName='Helvetica-Bold', fontSize=8, textColor=ORANGE,
            leading=11, spaceAfter=6, alignment=TA_LEFT)
title   = S('ti', fontName='Helvetica-Bold', fontSize=24, textColor=BLACK,
            leading=27, spaceAfter=4)
subtitle= S('st', fontName='Helvetica-Oblique', fontSize=11, textColor=GRAY_500,
            leading=14, spaceAfter=12)
h2      = S('h2', fontName='Helvetica-Bold', fontSize=11, textColor=ORANGE,
            leading=14, spaceBefore=6, spaceAfter=3)
body    = S('bd', fontName='Helvetica', fontSize=8.5, textColor=GRAY_700,
            leading=11, spaceAfter=4)
body_b  = S('bdb',fontName='Helvetica-Bold', fontSize=8.5, textColor=BLACK,
            leading=11, spaceAfter=4)
small   = S('sm', fontName='Helvetica', fontSize=7.5, textColor=GRAY_500,
            leading=10)
white_h = S('wh', fontName='Helvetica-Bold', fontSize=10, textColor=WHITE, leading=13)
white_b = S('wb', fontName='Helvetica',     fontSize=9,  textColor=WHITE, leading=12.5)
price_n = S('pn', fontName='Helvetica-Bold', fontSize=18, textColor=ORANGE,
            leading=22, alignment=TA_CENTER)
price_n_sm = S('pnsm', fontName='Helvetica-Bold', fontSize=13, textColor=ORANGE,
               leading=17, alignment=TA_CENTER)
price_l = S('pl', fontName='Helvetica-Bold', fontSize=7,  textColor=GRAY_500,
            leading=10, alignment=TA_CENTER)

def bullet(t):
    return Paragraph(f'<font color="#E8621A"><b>▪</b></font>  {t}',
                     S('bu', fontName='Helvetica', fontSize=8.5, textColor=GRAY_700,
                       leading=11, leftIndent=10, spaceAfter=2))

def stat_card(num, label, num_style=None):
    style = num_style if num_style else price_n
    t = Table([[Paragraph(num, style)], [Paragraph(label, price_l)]],
              colWidths=[1.4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), GRAY_50),
        ('TOPPADDING',(0,0),(-1,-1), 8),
        ('BOTTOMPADDING',(0,0),(-1,-1), 10),
        ('LINEBEFORE',(0,0),(0,-1), 2.5, ORANGE),
    ]))
    return t

class Cover:
    def on_page(self, c, doc):
        c.saveState()
        c.setFillColor(BLACK)
        c.rect(0, H-50, W, 50, fill=1, stroke=0)
        # Tenant logo
        try:
            img = ImageReader(LOGO_PATH)
            iw, ih = img.getSize()
            ratio = ih / iw
            disp_w = 90
            disp_h = disp_w * ratio
            c.drawImage(img, 36, H - 28 - disp_h/2,
                        width=disp_w, height=disp_h, mask='auto')
        except Exception:
            pass
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 8)
        c.drawRightString(W-36, H-30,
            f"EXECUTIVE SUMMARY  ·  {META['month'].upper()} {META['year']}")
        # Footer
        c.setFillColor(GRAY_500)
        c.setFont('Helvetica', 7)
        c.drawString(36, 24,
            '© 2026  JTC Communications & Consulting, LLC and Coolnerd, LLC')
        c.drawRightString(W-36, 24, 'Page 1 of 1')
        c.restoreState()

def build():
    doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                            leftMargin=0.5*inch, rightMargin=0.5*inch,
                            topMargin=0.78*inch, bottomMargin=0.45*inch,
                            title=f"{COMPANY['name']} - Executive Summary")
    s = []
    s.append(Paragraph('PROPOSAL AT A GLANCE', eyebrow))
    s.append(Paragraph(f"{COMPANY['name']} &mdash; {META['year']} Digital Engagement", title))
    s.append(Paragraph(
        'A refreshed brand, a new website, and a Marketing Operating System built for the team to run.',
        subtitle))
    s.append(HRFlowable(width='100%', thickness=0.5, color=GRAY_300, spaceAfter=10))

    # The opportunity (compressed)
    s.append(Paragraph('The opportunity', h2))
    s.append(Paragraph(
        f"{COMPANY['short_name']} is a {COMPANY['heritage_years']}-year-old Utah commercial and civil "
        f"general contractor with a digital presence that does not match the work. The Utah commercial-GC "
        f"comp set sits between 1,300 and 19,000 LinkedIn followers; {COMPANY['short_name']} is at "
        f"{COMPS['tenant_starting_followers']}. One additional mid-size commercial or public-works award "
        f"per year (typical $1M–$15M+) pays for this engagement 20–200× over.", body))

    # Two-column: what we build / what they own
    left = [
        Paragraph('What we build (90 days)', h2),
        bullet('<b>Brand refresh</b> &mdash; updated wordmark, palette, typography, and brand voice document.'),
        bullet(f"<b>One production website</b> &mdash; new {COMPANY['domain']} with commercial and civil division pages, service-area pages, and project showcase."),
        bullet('<b>SEO foundation</b> &mdash; Google Business Profile setup, structured data, business listings, target service-area pages.'),
        bullet('<b>Content engine</b> &mdash; 3-day jobsite + project photo and video shoot, 90-day post library, 2 hype videos.'),
        bullet('<b>Marketing Operating System</b> &mdash; five agents, approval queue, brand-voice training, full support and monthly reporting.'),
    ]
    right = [
        Paragraph('What you own at the end', h2),
        bullet('Your data, content, brand identity, and historical drafts &mdash; all yours.'),
        bullet('Tenant configuration: brand voice, services, target keywords.'),
        bullet('90 days of approved content as training data for ongoing tuning.'),
        bullet('All accounts, integrations, and admin access.'),
        bullet('Standard operating procedures and a 15-minute-per-day office-manager runbook.'),
    ]
    cols = Table([[left, right]], colWidths=[3.7*inch, 3.7*inch])
    cols.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(cols)
    s.append(Spacer(1, 6))

    # Marketing Operating System quick description
    s.append(Paragraph('The Marketing Operating System', h2))
    s.append(Paragraph(
        'A superintendent sends photos and a short note via text from a jobsite. Five specialized agents '
        f"draft {COMPANY['short_name']}-voice posts, replies, pages, and lead alerts. Office manager taps approve. "
        'Nothing publishes without a click. Replaces a marketing coordinator or agency retainer '
        'at a fraction of the cost, with a 15-minute-per-day routine and ~$200/mo in infrastructure.',
        body))

    # Sample-output callout
    cs = Table([[Paragraph(
        '<b>See it working: </b>'
        'coolnerd-tt.github.io/toone-construction/marketing-os/sample.html '
        f"— real generated drafts, in {COMPANY['short_name']} voice, from one superintendent text-in.",
        white_b)]],
        colWidths=[7.4*inch])
    cs.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), CHARCOAL),
        ('LEFTPADDING',(0,0),(-1,-1),14),
        ('RIGHTPADDING',(0,0),(-1,-1),14),
        ('TOPPADDING',(0,0),(-1,-1),10),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),
        ('LINEBEFORE',(0,0),(0,-1), 3, ORANGE),
    ]))
    s.append(cs)

    # Pricing strip
    s.append(Paragraph('Investment', h2))
    pricing = Table([[
        stat_card(f'${COMBINED_TOTAL:,}', 'COMBINED BUILD &mdash; ONE TIME'),
        stat_card('INCLUDED', 'CONCIERGE &mdash; MO 1–3', num_style=price_n_sm),
        stat_card(f"${PRICING['mos_retainer']['copilot_monthly']}", 'CO-PILOT &mdash; MO 4–6'),
        stat_card(f"up to ${PRICING['mos_retainer']['selfserve_monthly']}", 'SELF-SERVE &mdash; MO 7+', num_style=price_n_sm),
        stat_card(f"~${PRICING['mos_retainer']['infra_estimate']}", 'INFRA &mdash; AT COST'),
    ]], colWidths=[1.5*inch]*5)
    pricing.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),5),
    ]))
    s.append(pricing)
    s.append(Spacer(1, 6))
    s.append(Paragraph(
        f"Build phase ${BUILD_TOTAL:,} + Marketing Operating System build ${PRICING['mos_build']:,}. "
        f"Self-serve billed at the lesser of ${PRICING['mos_retainer']['selfserve_monthly']}/mo or "
        f"${PRICING['mos_retainer']['selfserve_hourly']}/hour. Tier-down with 30 days’ notice after month 3.",
        small))

    # 90-day timeline strip
    s.append(Paragraph('90 days, three phases', h2))
    tl = Table([[
        Paragraph('<b>WEEKS 1–3</b><br/>Discovery + Brand', body),
        Paragraph('<b>WEEKS 4–9</b><br/>Design + Build + OS', body),
        Paragraph('<b>WEEKS 10–12</b><br/>Launch + Activate', body),
    ]], colWidths=[2.5*inch]*3)
    tl.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), GRAY_50),
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),10),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),
        ('LINEBEFORE',(0,0),(0,-1), 2.5, ORANGE),
        ('LINEBEFORE',(1,0),(1,-1), 2.5, AMBER),
        ('LINEBEFORE',(2,0),(2,-1), 2.5, HexColor('#6FB65A')),
    ]))
    s.append(tl)

    # Next step
    s.append(Spacer(1, 8))
    s.append(Paragraph('Next step', h2))
    s.append(Paragraph(
        f"A 60-minute kickoff with {COMPANY['short_name']} leadership. On signature, the 90-day clock starts "
        'and the first jobsite shoot is scheduled inside week 2.', body_b))

    cb = Cover()
    doc.build(s, onFirstPage=cb.on_page, onLaterPages=cb.on_page)
    print(f'PDF -> {OUTPUT}')

if __name__ == '__main__':
    build()
