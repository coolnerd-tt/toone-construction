"""
Toone Construction Co. ×  — Proposal v5
v5 incorporates the first round of stakeholder edits:
- Cover: "Complete Digital Proposal" replaces "Full-Stack"
- Executive Summary: 35-year company, founded 1990, "Why Act Now"
  callout with new market-momentum framing, stat strip removed
- Global propagation of the 1990 founding / 35-year tenure
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Image
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

# ── COLORS ─────────────────────────────────────────────────────────────────────
BLACK    = HexColor('#0C0E10')
CHARCOAL = HexColor('#161A1D')
ORANGE   = HexColor('#E8621A')
AMBER    = HexColor('#F5A623')
WHITE    = HexColor('#FFFFFF')
OFF_WHITE= HexColor('#F4F2EE')
GRAY_50  = HexColor('#FAFAF8')
GRAY_100 = HexColor('#F0EFEB')
GRAY_300 = HexColor('#D1CFC9')
GRAY_500 = HexColor('#8A8880')
GRAY_700 = HexColor('#4A4845')
GRAY_900 = HexColor('#26241F')
SPARK    = HexColor('#D93B18')
SPARK_DK = HexColor('#A82C12')
TEAL     = HexColor('#2E7D8C')
TEAL_LT  = HexColor('#3D9BAD')
TEAL_BG  = HexColor('#1A3840')

W, H = letter
CONTENT_W = 6.6 * inch  # 0.7" margins each side

BASE = "/Users/tylertoone/Desktop/Claude Work/inbox/excavating-site"
JONES_LOGO   = os.path.join(BASE, "jones-assets/jones-logo.png")
CALLUS_LOGO  = os.path.join(BASE, "callus-logo-concepts/callus-logo-hz.png")

OUTPUT = os.path.join(BASE, "outputs/toone_proposal.pdf")

# ── STYLES ─────────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

# Cover
cover_label  = S('CL', fontName='Helvetica-Bold', fontSize=8,  textColor=ORANGE,   leading=12, spaceAfter=4)
cover_title  = S('CT', fontName='Helvetica-Bold', fontSize=42, textColor=WHITE,   leading=46, spaceAfter=0)
cover_title2 = S('CT2',fontName='Helvetica-Bold', fontSize=42, textColor=ORANGE,  leading=46, spaceAfter=0)
cover_amp    = S('CA', fontName='Helvetica-BoldOblique', fontSize=24, textColor=GRAY_500, leading=28)
cover_meta   = S('CM', fontName='Helvetica',      fontSize=9,  textColor=GRAY_300, leading=14)

# Chapter
chapter_num   = S('CN', fontName='Helvetica-Bold', fontSize=8,  textColor=ORANGE, leading=11, spaceAfter=4)
chapter_title = S('CTI',fontName='Helvetica-Bold', fontSize=26, textColor=BLACK,  leading=30, spaceAfter=14)
chapter_kicker= S('CK', fontName='Helvetica-Oblique', fontSize=10, textColor=GRAY_500, leading=14, spaceAfter=24)

# Headings
h2 = S('H2',  fontName='Helvetica-Bold', fontSize=14, textColor=BLACK,  leading=18, spaceBefore=18, spaceAfter=6)
h3 = S('H3',  fontName='Helvetica-Bold', fontSize=10.5, textColor=ORANGE, leading=14, spaceBefore=12, spaceAfter=4)
h3_teal = S('H3T', fontName='Helvetica-Bold', fontSize=10.5, textColor=TEAL, leading=14, spaceBefore=12, spaceAfter=4)
h3_spark= S('H3S', fontName='Helvetica-Bold', fontSize=10.5, textColor=SPARK, leading=14, spaceBefore=12, spaceAfter=4)

# Body — denser
body  = S('Bd', fontName='Helvetica',      fontSize=9,   textColor=GRAY_700, leading=14, spaceAfter=7)
body_lead = S('BL', fontName='Helvetica', fontSize=10, textColor=BLACK, leading=15, spaceAfter=9)
bullet_s = S('Bu', fontName='Helvetica',  fontSize=9,   textColor=GRAY_700, leading=13.5, spaceAfter=4, leftIndent=12)

# Labels
label_s  = S('Lb', fontName='Helvetica-Bold', fontSize=7.5, textColor=ORANGE, leading=11, spaceAfter=3)
label_teal = S('LbT', fontName='Helvetica-Bold', fontSize=7.5, textColor=TEAL, leading=11, spaceAfter=3)
label_spark= S('LbS', fontName='Helvetica-Bold', fontSize=7.5, textColor=SPARK, leading=11, spaceAfter=3)

# TOC
toc_num   = S('TN', fontName='Helvetica-Bold', fontSize=10, textColor=ORANGE,  leading=20)
toc_entry = S('TE', fontName='Helvetica',      fontSize=10, textColor=GRAY_700,leading=20)
toc_pg    = S('TP', fontName='Helvetica',      fontSize=9,  textColor=GRAY_500,leading=20, alignment=TA_RIGHT)

# Callouts
callout_t = S('CaT', fontName='Helvetica-Bold', fontSize=11, textColor=WHITE,    leading=15, spaceAfter=4)
callout_t_big = S('CaTB', fontName='Helvetica-Bold', fontSize=18, textColor=WHITE, leading=22, spaceAfter=8)
callout_b = S('CaB', fontName='Helvetica',      fontSize=9,  textColor=GRAY_300, leading=13.5, spaceAfter=0)

# Stat
stat_num_s = S('StN', fontName='Helvetica-Bold', fontSize=24, textColor=ORANGE, leading=27, alignment=TA_CENTER)
stat_lbl_s = S('StL', fontName='Helvetica-Bold', fontSize=7,  textColor=GRAY_500, leading=10, alignment=TA_CENTER)

# Table cells — denser
c_hdr  = S('CH',  fontName='Helvetica-Bold',        fontSize=7.5, textColor=WHITE,    leading=10)
c_body = S('CB',  fontName='Helvetica',             fontSize=8,   textColor=GRAY_700, leading=11)
c_body_b = S('CBB', fontName='Helvetica-Bold',      fontSize=8,   textColor=BLACK,    leading=11)
c_pri  = S('CPr', fontName='Helvetica-Bold',        fontSize=8,   textColor=ORANGE,   leading=11)
c_num  = S('CN',  fontName='Helvetica-Bold',        fontSize=8.5, textColor=BLACK,    leading=11, alignment=TA_RIGHT)
c_num_g = S('CNg',fontName='Helvetica',             fontSize=8.5, textColor=GRAY_500, leading=11, alignment=TA_RIGHT)
c_num_orange = S('CNo', fontName='Helvetica-Bold',  fontSize=8.5, textColor=ORANGE,   leading=11, alignment=TA_RIGHT)
# Centered numeric variants
c_num_c        = S('CNc',  fontName='Helvetica-Bold', fontSize=8.5, textColor=BLACK,  leading=11, alignment=TA_CENTER)
c_num_orange_c = S('CNoc', fontName='Helvetica-Bold', fontSize=8.5, textColor=ORANGE, leading=11, alignment=TA_CENTER)
c_body_c       = S('CBc',  fontName='Helvetica',      fontSize=8,   textColor=GRAY_700, leading=11, alignment=TA_CENTER)
c_pri_c        = S('CPrc', fontName='Helvetica-Bold', fontSize=8,   textColor=ORANGE,   leading=11, alignment=TA_CENTER)

# Pricing
pr_item   = S('PI',  fontName='Helvetica-Bold', fontSize=10, textColor=BLACK,   leading=13)
pr_item_h = S('PIh', fontName='Helvetica-Bold', fontSize=10, textColor=WHITE,   leading=13)
pr_note   = S('PN',  fontName='Helvetica',      fontSize=8.5,textColor=GRAY_500,leading=12)
pr_note_h = S('PNh', fontName='Helvetica',      fontSize=8.5,textColor=GRAY_300,leading=12)
pr_price  = S('PP',  fontName='Helvetica-Bold', fontSize=14, textColor=ORANGE,  leading=18, alignment=TA_RIGHT)
pr_price_h= S('PPh', fontName='Helvetica-Bold', fontSize=14, textColor=WHITE,   leading=18, alignment=TA_RIGHT)

# ── HELPERS ────────────────────────────────────────────────────────────────────
def P(text, style=body): return Paragraph(str(text), style)
def sp(h=10): return Spacer(1, h)
def hr(color=GRAY_300, t=0.5, sb=6, sa=6):
    return HRFlowable(width='100%', thickness=t, color=color, spaceAfter=sa, spaceBefore=sb)

def bullet(text):  return Paragraph(f'<font color="#E8621A"><b>\u25AA</b></font>  {text}', bullet_s)

def section_header(num, title, kicker=None, accent=ORANGE):
    n = f'0{num}' if num < 10 else str(num)
    n_style = S(f'cn{accent.hexval()}', fontName='Helvetica-Bold', fontSize=8,
                textColor=accent, leading=11, spaceAfter=4)
    rows = [[P(f'CHAPTER  {n}', n_style)],
            [P(title, chapter_title)]]
    if kicker:
        rows.append([P(kicker, chapter_kicker)])
    # Append an empty spacer row so we can keep the breathing room
    # below the kicker/title WITHOUT the accent bar extending through
    # the empty space.
    rows.append([Spacer(1, 30)])
    t = Table(rows, colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
        # Accent bar stops at the kicker/title row and does NOT extend
        # through the spacer row at the bottom.
        ('LINEBEFORE',(0,0),(0,-2), 3, accent),
    ]))
    return t

def callout(title, body_text, bg=CHARCOAL, accent=ORANGE, big_title=False):
    pad = 16
    title_style = callout_t_big if big_title else callout_t
    inner = Table([
        [P(title, title_style)],
        [P(body_text, callout_b)],
    ], colWidths=[CONTENT_W - pad*2 - 4])
    inner.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), bg),
        ('TOPPADDING',(0,0),(-1,-1), pad),
        ('BOTTOMPADDING',(0,0),(-1,-1), pad),
        ('LEFTPADDING',(0,0),(-1,-1), pad),
        ('RIGHTPADDING',(0,0),(-1,-1), pad),
    ]))
    wrap = Table([[inner]], colWidths=[CONTENT_W])
    wrap.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),
        ('LINEBEFORE',(0,0),(-1,-1),3, accent),
    ]))
    return wrap

def two_col(left, right, gap=0.25*inch):
    cw = (CONTENT_W - gap) / 2
    def col(items):
        rows = [[i] for i in items]
        t = Table(rows, colWidths=[cw])
        t.setStyle(TableStyle([
            ('TOPPADDING',(0,0),(-1,-1),1),
            ('BOTTOMPADDING',(0,0),(-1,-1),1),
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),0),
        ]))
        return t
    out = Table([[col(left), Spacer(gap,1), col(right)]],
                colWidths=[cw, gap, cw])
    out.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    return out

def stat_strip(items):
    """items: [(num, label), ...]"""
    cells = []
    for num, lbl in items:
        cell = Table([[P(num, stat_num_s)], [P(lbl, stat_lbl_s)]],
                     colWidths=[CONTENT_W/len(items)])
        cell.setStyle(TableStyle([
            ('TOPPADDING',(0,0),(-1,-1),2),
            ('BOTTOMPADDING',(0,0),(-1,-1),2),
        ]))
        cells.append(cell)
    t = Table([cells], colWidths=[CONTENT_W/len(items)]*len(items))
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), GRAY_50),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),16),
        ('BOTTOMPADDING',(0,0),(-1,-1),16),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('LINEABOVE',(0,0),(-1,0),2, ORANGE),
        ('LINEBELOW',(0,-1),(-1,-1),0.5, GRAY_300),
    ]))
    return t

def phase_card_basic(num, title, weeks, items, bg=GRAY_50, accent=ORANGE):
    """Module-level phase card so it's usable across chapters."""
    ph_s = S('ps2', fontName='Helvetica-Bold', fontSize=8, textColor=accent, leading=11)
    ti_s = S('pt2', fontName='Helvetica-Bold', fontSize=11, textColor=BLACK, leading=14)
    wk_s = S('pw2', fontName='Helvetica-Bold', fontSize=7.5, textColor=GRAY_500, leading=10)
    it_s = S('pi2', fontName='Helvetica',     fontSize=8.5, textColor=GRAY_700, leading=12)
    items_html = '<br/>'.join([f'\u2022 {x}' for x in items])
    data = [[P(num, ph_s), P(title, ti_s), P(weeks.upper(), wk_s), P(items_html, it_s)]]
    t = Table(data, colWidths=[0.85*inch, 1.4*inch, 0.95*inch, 3.4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), bg),
        ('TOPPADDING',(0,0),(-1,-1),12),
        ('BOTTOMPADDING',(0,0),(-1,-1),12),
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LINEBEFORE',(0,0),(0,-1),3, accent),
    ]))
    return t


def price_row(item, price, note='', highlight=False):
    if highlight:
        bg, ist, nst, pst = ORANGE, pr_item_h, pr_note_h, pr_price_h
    else:
        bg, ist, nst, pst = GRAY_50, pr_item, pr_note, pr_price
    data = [[P(item, ist), P(note, nst), P(price, pst)]]
    t = Table(data, colWidths=[2.0*inch, 2.8*inch, 1.8*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), bg),
        ('TOPPADDING',(0,0),(-1,-1),11),
        ('BOTTOMPADDING',(0,0),(-1,-1),11),
        ('LEFTPADDING',(0,0),(-1,-1),12),
        ('RIGHTPADDING',(0,0),(-1,-1),12),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LINEBELOW',(0,0),(-1,-1),0.5, WHITE),
    ]))
    return t

def comp_table(rows, center=False):
    """rows: header + data rows, each a list of strings.
       First column = company name (bold), numeric columns right-aligned
       by default. Pass center=True to center-align all non-name columns
       (used for the GBP benchmark table where columns are paired
       categorical values, not magnitudes)."""
    table_rows = []
    # Header — center alignment of header cells matches body when center=True
    if center:
        c_hdr_style = S('CHc', fontName='Helvetica-Bold', fontSize=7.5, textColor=WHITE, leading=10, alignment=TA_CENTER)
    else:
        c_hdr_style = c_hdr
    hdr = [P(rows[0][0], c_hdr)] + [P(c, c_hdr_style) for c in rows[0][1:]]
    table_rows.append(hdr)
    for r in rows[1:]:
        is_jones = 'Jones' in r[0]
        name_style = c_pri if is_jones else c_body_b
        out = [P(r[0], name_style)]
        for v in r[1:]:
            if center:
                # All non-name columns centered, regardless of digit content
                if any(ch.isdigit() for ch in v) and not v.endswith(')'):
                    style = c_num_orange_c if is_jones else c_num_c
                else:
                    style = c_pri_c if is_jones else c_body_c
                out.append(P(v, style))
            else:
                # Default: right-align numbers, left-align text
                if any(ch.isdigit() for ch in v) and not v.endswith(')'):
                    style = c_num_orange if is_jones else c_num
                    out.append(P(v, style))
                else:
                    out.append(P(v, c_body if not is_jones else c_pri))
        table_rows.append(out)
    n_cols = len(rows[0])
    col_w = CONTENT_W / n_cols
    widths = [col_w * 1.4] + [(CONTENT_W - col_w*1.4) / (n_cols-1)] * (n_cols-1)
    t = Table(table_rows, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0), CHARCOAL),
        ('TOPPADDING',(0,0),(-1,-1),8),
        ('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),9),
        ('RIGHTPADDING',(0,0),(-1,-1),9),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE, GRAY_50]),
        ('LINEBELOW',(0,0),(-1,-1),0.4, GRAY_300),
    ]))
    return t

# ── PAGE CANVAS ────────────────────────────────────────────────────────────────
class Canv:
    def on_page(self, c, doc):
        page = doc.page
        c.saveState()
        if page == 1:
            # Cover background
            c.setFillColor(BLACK); c.rect(0,0,W,H,fill=1,stroke=0)
            # Side accents
            c.setFillColor(ORANGE);   c.rect(0,0,5,H,fill=1,stroke=0)
            c.setFillColor(SPARK);    c.rect(W-5,0,5,H,fill=1,stroke=0)
            # Bottom split bar
            c.setFillColor(ORANGE);   c.rect(0,0,W/2,4,fill=1,stroke=0)
            c.setFillColor(SPARK);    c.rect(W/2,0,W/2,4,fill=1,stroke=0)
            # Subtle grid
            c.setStrokeColor(HexColor('#15181B')); c.setLineWidth(0.4)
            for x in range(0,int(W)+1,40): c.line(x,0,x,H)
            for y in range(0,int(H)+1,40): c.line(0,y,W,y)
            # Watermark logos
            try:
                c.saveState()
                c.setFillAlpha(0.07)
                c.drawImage(ImageReader(JONES_LOGO),
                            -1.0*inch, H/2 - 1.0*inch + 0.5*inch,
                            width=4.6*inch, height=2.0*inch,
                            mask='auto', preserveAspectRatio=True)
                c.setFillAlpha(0.05)
                c.drawImage(ImageReader(CALLUS_LOGO),
                            W - 4.2*inch, H/2 - 0.8*inch,
                            width=4.0*inch, height=2.0*inch,
                            mask='auto', preserveAspectRatio=True)
                c.restoreState()
            except Exception:
                pass
            c.setFont('Helvetica-Bold', 7)
            c.setFillColor(GRAY_700)
            c.drawRightString(W-30, H-26, 'CONFIDENTIAL  |  PROPOSAL v5  |  APRIL 2026')
        else:
            # Top header bar
            c.setFillColor(ORANGE); c.rect(0,H-3,W,3,fill=1,stroke=0)
            c.setFillColor(CHARCOAL); c.rect(0,H-32,W,29,fill=1,stroke=0)
            c.setFont('Helvetica-Bold', 7.5); c.setFillColor(WHITE)
            c.drawString(30, H-21, 'JONES \u00D7 CALLUS')
            c.setFillColor(ORANGE); c.drawString(30+82, H-21, '|')
            c.setFillColor(GRAY_300); c.setFont('Helvetica', 7.5)
            c.drawString(30+90, H-21, 'Digital Proposal  \u00B7  v5  \u00B7  2026')
            c.setFont('Helvetica-Bold', 7.5); c.setFillColor(ORANGE)
            c.drawRightString(W-30, H-21, f'{page}')
            # Footer bar
            c.setFillColor(GRAY_100); c.rect(0,0,W,22,fill=1,stroke=0)
            c.setFont('Helvetica', 6.5); c.setFillColor(GRAY_500)
            c.drawString(30, 8, 'CONFIDENTIAL  \u00B7  prepared for Toone Construction Co.  \u00B7  \u00A9 2026  JTC Communications & Consulting, LLC and Coolnerd, LLC')
        c.restoreState()

# ── DOCUMENT ───────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=letter,
        leftMargin=0.7*inch, rightMargin=0.7*inch,
        topMargin=0.7*inch,  bottomMargin=0.45*inch,
        title='Jones \u00D7 Callus \u2014 Proposal v5',
    )
    s = []
    cb = Canv()

    # ═══ COVER ═══════════════════════════════════════════════════════════════
    s.append(sp(0.9*inch))
    s.append(P('DIGITAL PROPOSAL', cover_label))
    s.append(P('BRAND  \u00B7  WEB  \u00B7  SEO  \u00B7  SOCIAL', cover_label))
    s.append(sp(14))

    # Real logo lockup
    j_img = Image(JONES_LOGO,  width=2.4*inch, height=0.95*inch, kind='proportional')
    c_img = Image(CALLUS_LOGO, width=2.0*inch, height=1.25*inch, kind='proportional')
    logo_row = Table([[j_img, '', c_img]],
                     colWidths=[2.7*inch, 0.3*inch, 2.3*inch])
    logo_row.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('ALIGN',(0,0),(0,0),'LEFT'),
        ('ALIGN',(2,0),(2,0),'LEFT'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(logo_row)
    s.append(sp(20))

    # Big title
    s.append(P('TOONE CONSTRUCTION', cover_title2))
    s.append(P('&amp;', cover_amp))
    s.append(P('', cover_title))
    s.append(sp(24))

    # Dual rule
    rl = Table([['']], colWidths=[1.4*inch])
    rl.setStyle(TableStyle([('LINEBELOW',(0,0),(-1,-1),2,ORANGE),
                            ('TOPPADDING',(0,0),(-1,-1),0),
                            ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    rr = Table([['']], colWidths=[1.4*inch])
    rr.setStyle(TableStyle([('LINEBELOW',(0,0),(-1,-1),2,SPARK),
                            ('TOPPADDING',(0,0),(-1,-1),0),
                            ('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    drule = Table([[rl, Spacer(0.15*inch,1), rr]],
                  colWidths=[1.4*inch, 0.15*inch, 1.4*inch])
    drule.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),0),
                                ('RIGHTPADDING',(0,0),(-1,-1),0)]))
    s.append(drule)
    s.append(sp(24))

    s.append(P('A two-brand digital proposal covering brand, web,', cover_meta))
    s.append(P('search visibility, and social for two Utah contractors.', cover_meta))
    s.append(sp(40))

    meta_row = Table([
        [P('PREPARED FOR', cover_label), P('PROPOSAL VERSION', cover_label), P('STATUS', cover_label)],
        [P('Toone Construction Co.<br/>', cover_meta),
         P('v5  \u00B7  May 2026', cover_meta),
         P('For Review', cover_meta)],
    ], colWidths=[2.4*inch, 2.2*inch, 1.7*inch])
    meta_row.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(meta_row)

    # Confidentiality line at bottom of cover
    s.append(sp(28))
    confid_style = S('confid', fontName='Helvetica-Oblique', fontSize=7.5,
                     textColor=GRAY_500, leading=10, alignment=TA_LEFT)
    s.append(P(
        'This proposal contains proprietary methodology and pricing, shared in confidence with '
        'Toone Construction Co. leadership. Not for external distribution.',
        confid_style))
    s.append(sp(6))
    s.append(P(
        '© 2026&nbsp; JTC Communications &amp; Consulting, LLC and Coolnerd, LLC',
        confid_style))

    s.append(PageBreak())

    # ═══ TOC ═════════════════════════════════════════════════════════════════
    s.append(section_header(0, 'Contents'))
    s.append(sp(8))
    toc_rows = [
        ('01', 'Executive Summary',           '03'),
        ('02', 'The Opportunity',             '04'),
        ('03', 'Brand &amp; Web Strategy',    '06'),
        ('04', 'SEO &amp; Local Search',      '08'),
        ('05', 'Social &amp; Content',        '09'),
        ('06', 'The Marketing Operating System',            '10'),
        ('07', 'Investment &amp; Timeline',   '14'),
        ('08', 'Next Steps',                  '17'),
    ]
    rows = [[P(n, toc_num), P(t, toc_entry), P(p, toc_pg)] for n,t,p in toc_rows]
    toc = Table(rows, colWidths=[0.55*inch, 5.55*inch, 0.5*inch])
    toc.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),5),
        ('BOTTOMPADDING',(0,0),(-1,-1),5),
        ('LINEBELOW',(0,0),(-1,-1),0.4, GRAY_300),
    ]))
    s.append(toc)
    s.append(PageBreak())

    # ═══ 01 EXECUTIVE SUMMARY ════════════════════════════════════════════════
    s.append(section_header(1, 'Executive Summary',
        kicker='What we are building, who it is for, and why it pays for itself.'))
    s.append(P(
        'Toone Construction Co. is an 35-year-old Utah commercial and civil general contractor specializing in '
        'commercial buildings, site work, and utilities, founded in 1990.  is its welding and '
        'custom-fabrication arm. Both companies do excellent work; it is time their digital '
        'presence reflects it.',
        body_lead))
    s.append(P(
        'This proposal lays out a coordinated plan for two distinct brands, two new '
        'websites, and a 90-day rollout to make both companies easier to find, easier to '
        'vet, and easier to hire than any regional competitor in their category.',
        body))

    s.append(P('What you get', h2))
    s.append(bullet('<b>One coordinated brand system</b> covering both companies \u2014 distinct identities that '
                    'still read as a family.'))
    s.append(bullet('<b>Two production websites</b>: a refreshed tooneconstruction.com and a new .'))
    s.append(bullet('<b>Local SEO + Google Business Profile (GBP) overhaul</b> to reposition both brands in the '
                    'highest-leverage channel for this category.'))
    s.append(bullet('<b>Social media content engine:</b> LinkedIn-focused and sustainable post-launch.'))
    s.append(bullet('<b>90-day fixed-price build</b>, with options for ongoing support and maintenance.'))

    s.append(sp(8))
    s.append(callout(
        'Why Act Now',
        'Construction investment is at a decade high, putting a spotlight on exactly the '
        'specialized work Jones delivers. Now is the time to turn that market momentum into '
        'wins. A polished, modern digital presence positions Jones as the clear, credible '
        'choice for owners, GCs, and engineers, elevates you in search results, and helps you '
        'recruit the field and office talent needed to scale. Just one additional mid-size '
        'deep-foundation or shoring award can range from $500K\u2013$5M+; if improved '
        'visibility and trust help Jones win even one new bid per year, this investment can '
        'pay back 10\u00D7\u2013100\u00D7.',
        bg=CHARCOAL, accent=ORANGE, big_title=True))

    s.append(PageBreak())

    # ═══ 02 THE OPPORTUNITY (MARKET DATA) ════════════════════════════════════
    s.append(section_header(2, 'The Opportunity',
        kicker='Where Jones stands against competitors.'))

    s.append(P(
        'Before designing anything, we conducted market research. Two takeaways drive this proposal: '
        '<b>(1) LinkedIn is where Utah commercial and civil B2B happens</b>, and <b>(2) Google Business Profile '
        'is critical to building local awareness of your business.</b> Both are areas of opportunity for Jones and Callus.',
        body_lead))

    s.append(P('LinkedIn Competitive Landscape', h2))
    s.append(P(
        'LinkedIn is where commercial GCs, owners\u2019 reps, developers, and project managers '
        'vet contractors before short-listing. Jones can become a player within this space within '
        '12 months.',
        body))

    s.append(comp_table([
        ['Company',                     'LinkedIn',  'Founded',  'Notes'],
        ['BHI',                         '~19k',      '~2000',    'Excavation + construction'],
        ['W.W. Clyde &amp; Co.',        '~14k',      '1926',     'Clyde Companies'],
        ['Staker Parson',               '~6,100',    '1952',     'Materials + civil'],
        ['Geneva Rock Products',        '~6,000',    '1954',     'Clyde Companies'],
        ['Sunroc / Suncore',            '~6,000',    '1937',     'Clyde Companies'],
        ['Hadco',                       '~1,300',    '1989',     'Excavation'],
        ['Toone Construction Co.',        '331',       '1990',     'Excavation, Shoring, Utilities'],
    ], center=True))
    s.append(sp(4))
    s.append(P(
        'LinkedIn followings as of May 2026, rounded. Sources: company LinkedIn pages, '
        'agc-utah.org member directory.',
        ParagraphStyle('cap', fontName='Helvetica-Oblique', fontSize=7.5,
                       textColor=GRAY_500, leading=10)))

    s.append(P('Why this gap matters', h3))
    s.append(bullet('LinkedIn is where <b>80% of B2B social leads</b> come from, and it converts about '
                    '<b>4\u00d7</b> better than Facebook or X for commercial work.'))
    s.append(bullet('<b>89% of B2B marketers</b> use LinkedIn for lead generation, and <b>40%</b> rate as their '
                    'most effective channel.'))

    s.append(P('Google Business Profile: Maximize SEO', h2))
    s.append(P(
        'Google Maps is where most buyers build their short list. When someone searches for any of '
        'your services (excavating, deep foundation, custom fabrication, welding), Google shows three '
        'local businesses at the top of the page, with star ratings, reviews, photos, and a '
        'tap-to-call button. That box appears before any regular search results. Miss that spot and '
        'Jones and Callus are invisible at the moment a buyer is ready to act. A strong Google Business Profile '
        'and an active review program help build instant trust, drive inbound calls, and route '
        'qualified traffic to the new website.',
        body))

    s.append(PageBreak())

    # \u2500\u2500 GBP benchmark table with grouped two-row header \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    gbp_hdr_grp = S('GbpHG', fontName='Helvetica-Bold', fontSize=8,   textColor=WHITE,
                    leading=11, alignment=TA_CENTER)
    gbp_hdr_sub = S('GbpHS', fontName='Helvetica-Bold', fontSize=7.5, textColor=WHITE,
                    leading=10, alignment=TA_CENTER)
    gbp_data    = S('GbpD',  fontName='Helvetica-Bold', fontSize=8.5, textColor=BLACK,
                    leading=11, alignment=TA_CENTER)
    gbp_label   = S('GbpL',  fontName='Helvetica-Bold', fontSize=8,   textColor=BLACK,
                    leading=11, alignment=TA_LEFT)

    gbp_rows = [
        # Super-header: groups three sections
        [P('', gbp_hdr_grp),
         P('Where you want to be', gbp_hdr_grp), '',
         P('Average company', gbp_hdr_grp),
         P('Where you are today', gbp_hdr_grp), ''],
        # Sub-header: brand-level labels under each group (Average company cell
        # is empty here because it merges with the row above via SPAN)
        [P('Benchmark', gbp_hdr_sub),
         P('Jones', gbp_hdr_sub),
         P('Callus', gbp_hdr_sub),
         '',
         P('Jones', gbp_hdr_sub),
         P('Callus', gbp_hdr_sub)],
        # Data rows
        [P('Google review count',              gbp_label),
         P('100+',    gbp_data), P('50+',    gbp_data), P('20\u201380',   gbp_data),
         P('18',      gbp_data), P('1',      gbp_data)],
        [P('Star rating (jobsite category)',   gbp_label),
         P('4.5\u20134.7', gbp_data), P('4.5\u20134.7', gbp_data), P('4.0\u20134.4', gbp_data),
         P('4.4',     gbp_data), P('5.0',    gbp_data)],
        [P('GBP photos (recent, geo-tagged)',  gbp_label),
         P('40+',     gbp_data), P('30+',    gbp_data), P('10\u201320',   gbp_data),
         P('2',       gbp_data), P('6',      gbp_data)],
        [P('Owner replies to reviews',         gbp_label),
         P('100%',    gbp_data), P('100%',   gbp_data), P('~50%',    gbp_data),
         P('0%',      gbp_data), P('0%',     gbp_data)],
        [P('Service area pages (linked from GBP)', gbp_label),
         P('8\u201312',    gbp_data), P('4\u20136',    gbp_data), P('3\u20136',     gbp_data),
         P('0',       gbp_data), P('0',      gbp_data)],
    ]
    # Column widths: benchmark column wider, 5 value columns equal
    gbp_widths = [1.95*inch] + [(CONTENT_W - 1.95*inch) / 5] * 5
    gbp_t = Table(gbp_rows, colWidths=gbp_widths, repeatRows=2)
    gbp_t.setStyle(TableStyle([
        # Backgrounds
        ('BACKGROUND',(0,0),(-1,0), CHARCOAL),
        ('BACKGROUND',(0,1),(-1,1), HexColor('#2A2F33')),
        ('ROWBACKGROUNDS',(0,2),(-1,-1), [WHITE, GRAY_50]),
        # Super-header spans
        ('SPAN',(1,0),(2,0)),  # 'Where you want to be' over Jones + Callus
        ('SPAN',(4,0),(5,0)),  # 'Where you are today' over Jones + Callus
        ('SPAN',(3,0),(3,1)),  # 'Average company' merges vertically across both header rows
        # Make sure the merged Average company cell has the dark super-header background
        ('BACKGROUND',(3,0),(3,1), CHARCOAL),
        # Padding
        ('TOPPADDING',(0,0),(-1,-1),6),
        ('BOTTOMPADDING',(0,0),(-1,-1),6),
        ('LEFTPADDING',(0,0),(-1,-1),9),
        ('RIGHTPADDING',(0,0),(-1,-1),9),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        # Subtle separators
        ('LINEBELOW',(0,1),(-1,1), 0.4, GRAY_500),
        ('LINEBELOW',(0,2),(-1,-1), 0.4, GRAY_300),
        # Vertical separators between group sections (after Callus, after Typical)
        ('LINEAFTER',(2,0),(2,-1), 0.4, GRAY_300),
        ('LINEAFTER',(3,0),(3,-1), 0.4, GRAY_300),
    ]))
    s.append(gbp_t)
    s.append(sp(4))
    s.append(P(
        'Each additional Google review correlates with <b>+80 website visits, +63 direction requests, '
        'and +16 calls</b> per year for the average local business (BrightLocal, 2025). For a contractor '
        'whose average ticket is six figures, the unit economics are obvious.',
        body))

    s.append(PageBreak())

    # ═══ 03 BRAND & WEB STRATEGY ═════════════════════════════════════════════
    s.append(section_header(3, 'Brand &amp; Web Strategy',
        kicker='Two brands, two sites, one coordinated team.'))

    s.append(P(
        'Jones and Callus are different businesses serving different buyers. They should look '
        'related \u2014 same family, same standards \u2014 without sharing a brand.',
        body_lead))

    s.append(P('Toone Construction Co. \u2014 Brand refresh', h3))
    s.append(P(
        'Jones already has equity. The J-mark is the most recognizable element you have, '
        'and 80 years of commercial buildings, site work, and utilities work back it up. The refresh sharpens the typography, '
        'modernizes the palette, and tightens the visual system while keeping core elements people know.',
        body))
    s.append(bullet('Logo: keep the original mark; refresh the original and add a horizontal version '
                    'for web/social.'))
    s.append(bullet('Tagline: &quot;Built for the Tough Jobs.&quot;'))
    s.append(bullet('Palette: charcoal and orange as the core colors, with amber accents on highlights '
                    'and a soft off-white background for sections with a lot of text.'))
    s.append(bullet('Typography: bold, condensed headlines paired with clean, readable body text. '
                    'Industrial feel that loads fast on any device.'))
    s.append(bullet('Photography: add on-site photos and video from active jobs.'))

    s.append(P(' \u2014 Brand build (Spark direction)', h3_spark))
    s.append(P(
        'Callus has a solid starting point. We refined it into the Spark direction: '
        'an industrial badge feel, dark steel tones, a glove-and-spark mark, and rugged headline '
        'type. The brand speaks directly to the people who hire welders, including GCs, plant '
        'managers, and foremen working by the hour or by the project.',
        body))
    s.append(bullet('Logo: glove + spark mark, with horizontal and vertical options.'))
    s.append(bullet('Tagline: &quot;Built tough. Welded right.&quot;'))
    s.append(bullet('Family link: Callus carries a &quot;proud part of the Toone Construction family&quot; line in the banner, '
                    'about, and footer, borrowing trust without diluting the new brand.'))

    s.append(P('Web build \u2014 both sites', h2))
    s.append(P(
        'Both sites will use modern technology so they are fast, easy to update, and search-friendly. '
        'Each site is built for the company\u2019s needs.',
        body))

    s.append(P('Built to save time and bring in leads', h3))
    s.append(bullet('<b>Update without a developer.</b> Add a new project, post a blog, or change a service '
                    'description in minutes. The site stays current without becoming a chore for your team.'))
    s.append(bullet('<b>Built for the phone.</b> Most customers, GCs, and crew look at the site from the '
                    'jobsite or the truck, not a desktop. Pages load fast and read cleanly on mobile, '
                    'where the decision to call actually happens.'))
    s.append(bullet('<b>Found by Google.</b> Every page is structured so search engines recognize Jones '
                    'and Callus, their services, and their projects, putting you in front of buyers '
                    'searching for excavation work right now.'))

    s.append(PageBreak())
    s.append(P('Page set', h3))
    s.append(two_col([
        P('<b>tooneconstruction.com</b>', body),
        bullet('Home page content and menu'),
        bullet('Company services and sub pages'),
        bullet('Projects (case studies, filterable)'),
        bullet('About (history, leadership, etc.)'),
        bullet('Careers'),
        bullet('Service areas'),
        bullet('Contact / Get a quote'),
    ], [
        P('<b></b>', body),
        bullet('Home page content and menu'),
        bullet('Company services and sub pages'),
        bullet('Shop (capabilities, equipment, certifications)'),
        bullet('Projects (gallery)'),
        bullet('About'),
        bullet('Careers'),
        bullet('Service areas'),
        bullet('Contact / Get a Quote'),
    ]))
    s.append(PageBreak())

    # ═══ 04 SEO & LOCAL ═════════════════════════════════════════════════════
    s.append(section_header(4, 'SEO &amp; Local Search',
        kicker='The highest-leverage channel for both brands.', accent=TEAL))

    s.append(P(
        'For excavating and fabrication, the search journey is local-first: Someone types a '
        'job-site need into Google, sees a map of local providers, and calls one of the top '
        'three. The website matters \u2014 but only after they have found you on Google Maps.',
        body_lead))

    s.append(P('Google Business Profile (GBP)', h3_teal))
    s.append(bullet('Claim and verify both GBPs (Jones is partially claimed; Callus needs to be added).'))
    s.append(bullet('Categorize your primary and secondary services (Excavating Contractor, Earthworks, '
                    'General Contractor, Construction Services for Jones; Welder, Welding Supply, '
                    'Custom Fabricator for Callus).'))
    s.append(bullet('List and claim all the service areas where you do business.'))
    s.append(bullet('Ensure hours, contacts, attributes, accessibility, payment methods, and languages are '
                    'consistent across both businesses.'))
    s.append(bullet('Add 30+ recent geo-tagged jobsite photos in batch, then continue adding 4\u20136 per month '
                    'consistently.'))
    s.append(bullet('Create a review program with a text template to send to clients after every completed '
                    'job, with a direct GBP link.'))
    s.append(bullet('Set up a process so you can respond to all reviews quickly, positive or negative.'))

    s.append(P('Technical SEO foundation', h3_teal))
    s.append(bullet('Add structured data tags to every relevant page (business, services, projects, FAQs) '
                    'so search engines can read your site cleanly.'))
    s.append(bullet('Tune every page for fast load times.'))
    s.append(bullet('Create smart internal linking so service pages connect to relevant project case '
                    'studies, helping visitors and search engines find the right work.'))
    s.append(bullet('Connect your sitemaps to the major search engines (Google, Bing) so pages get indexed '
                    'quickly.'))
    s.append(bullet('Ensure your business information is consistent across 30+ directories (BBB, AGC of '
                    'Utah, Yelp, BuildZoom, Procore, and others).'))

    s.append(P('Target keywords', h3_teal))
    s.append(two_col([
        P('<b>Toone Construction</b>', body),
        bullet('excavating contractor utah'),
        bullet('deep foundation salt lake city'),
        bullet('shoring contractor utah'),
        bullet('site work contractor west jordan'),
        bullet('drilling contractor wasatch front'),
        bullet('utility excavation utah county'),
        bullet('commercial excavation salt lake'),
    ], [
        P('<b></b>', body),
        bullet('mobile welder west jordan'),
        bullet('welding contractor utah'),
        bullet('custom fabrication salt lake'),
        bullet('mig welding wasatch front'),
        bullet('line boring utah'),
        bullet('industrial welding salt lake'),
        bullet('emergency welding utah'),
    ]))

    s.append(PageBreak())

    # ═══ 05 SOCIAL & CONTENT ═════════════════════════════════════════════════
    s.append(section_header(5, 'Social &amp; Content',
        kicker='Where the competition already lives, and where Jones and Callus can catch up fastest.'))

    s.append(P('LinkedIn \u2014 the priority channel', h3))
    s.append(bullet('We will refresh the Jones LinkedIn page (banner, about copy, and post cadence) '
                    'and create a Callus LinkedIn company page to launch with the website.'))
    s.append(bullet('Posting cadence: <b>3 posts/week per brand</b> mixing project milestones, behind-the-scenes '
                    'shop/yard content, hiring posts, and short ownership notes.'))
    s.append(bullet('Employee advocacy: foremen, PMs, and ownership reshare from personal accounts to boost '
                    'social engagement and amplify reach.'))
    s.append(bullet('Each month, send 50\u2013100 personalized connection requests on LinkedIn to potential clients.'))

    s.append(P('Content pillars', h3))
    s.append(two_col([
        P('<b>Jones</b>', body),
        bullet('Jobsite milestones'),
        bullet('Video and photo action shots'),
        bullet('Equipment in action (drone, video)'),
        bullet('Crew spotlights / safety wins'),
        bullet('Project case studies'),
        bullet('Industry commentary from leadership'),
        bullet('Create a hype video'),
    ], [
        P('<b>Callus</b>', body),
        bullet('Welding before/after'),
        bullet('Time-lapse videos'),
        bullet('Same-day service moments'),
        bullet('Crew skill spotlights'),
        bullet('Quick how-it-was-done write-ups'),
        bullet('Create a hype video'),
    ]))

    s.append(P('Instagram + Facebook', h3))
    s.append(bullet('<b>Instagram</b> is where the visual story lives. Jobsite photos and short videos '
                    'put Jones and Callus in front of GCs, project managers, field workers, and recruits '
                    'who respond to seeing the work, not just reading about it.'))
    s.append(bullet('<b>Facebook</b> reaches Utah professionals, local community pages, and crew families '
                    'who share what they see. Everything cross-posts from Instagram automatically, so '
                    'you cover both audiences with one effort.'))
    s.append(bullet('<b>Reels (short videos):</b> one per brand each month showing a time-lapse project, '
                    'a build progression, or equipment in action. Cheap to produce, and the single biggest '
                    'credibility and recruiting lift available on social media.'))
    s.append(bullet('<b>Tag every post with the jobsite city and &quot;Utah&quot;</b> so people in your '
                    'service area discover you when they search nearby. This is free visibility that '
                    'compounds month over month.'))

    s.append(P('Content', h3))
    s.append(bullet('<b>We provide professional photography and videography.</b> Drone, jobsite, and shop '
                    'coverage captured during 4 day shoots that will produce 8\u201310 weeks of posts across '
                    'both brands.'))
    s.append(bullet('<b>We train your team so they know how to capture content easily.</b> Someone in '
                    'your office can then take those photos and video clips and post them manually to '
                    'your social media platforms.'))

    s.append(PageBreak())

    # ═══ 06 THE MARKETING OS ═════════════════════════════════════════════════
    s.append(section_header(6, 'The Marketing Operating System',
        kicker='A marketing system you can manage, not an agency you rent.'))

    s.append(P(
        'Most marketing engagements end one of two ways. The agency keeps billing forever, or '
        'the client tries to take it in-house and the work quietly stops. Neither outcome is good '
        'for Jones or Callus. This chapter describes the third option.',
        body_lead))

    s.append(P(
        'The Marketing Operating System is a custom-built system that automates roughly 80% of the '
        'ongoing marketing work: social posts, review replies, SEO content, and lead triage. A human '
        '(you) approves every item before it publishes. We build it, train it on your brand voice, '
        'and hand it over. After 90 days you have a working system, not an agency dependency.',
        body))

    s.append(P('Why this is possible now', h2))
    s.append(bullet('Modern AI tools are good enough to draft brand-voice content from a two-sentence '
                    'note and three photos sent by a foreman from a jobsite.'))
    s.append(bullet('Today\u2019s workflow tools can route those drafts into approval queues, post on '
                    'schedule, and track performance without custom engineering.'))
    s.append(bullet('Google, Meta, and LinkedIn now offer stable connections so we can publish to them '
                    'reliably, without workarounds.'))
    s.append(bullet('The result: <b>MARKETING WORK</b> that used to require a part-time hire can run on '
                    'a 15-minute-a-day approval routine for an office manager.'))

    s.append(P('Your five AI agents', h2))
    s.append(P(
        'Five specialized AI agents handle distinct jobs. Each one drafts. A human approves. '
        'Nothing publishes without a click.',
        body))

    s.append(P('Field-to-Content Agent', h3))
    s.append(P(
        'A foreman or PM sends photos and a short note via text message ("Finished the Lehi sewer '
        'tie-in, biggest job of the year, 14 hours"). The agent generates a LinkedIn post, '
        'Google Business Profile post, Instagram caption, blog snippet, and internal newsletter '
        'blurb, all in Jones or Callus voice. Office manager taps approve.',
        body))

    s.append(P('Reputation Agent', h3))
    s.append(P(
        'This agent watches your Google and Facebook reviews on both brands. When a new review '
        'comes in, it drafts a reply in your brand voice and adjusts the tone to match the rating. '
        'A 5-star review gets a friendly thank-you. A 1- or 2-star review gets a measured response '
        'with a private offer to resolve the issue. The office manager approves and the reply posts.',
        body))

    s.append(P('SEO Content Agent', h3))
    s.append(P(
        'Each month, this agent looks at how your search rankings are changing, finds one or two '
        'pages or blog posts that would help you compete better in your service areas, drafts the '
        'full content, and sends it to you for approval. Over 12 months, this closes the search '
        'gap between you and your competitors without hiring a copywriter.',
        body))

    s.append(P('Lead Triage Agent', h3))
    s.append(P(
        'This agent classifies inbound inquiries into excavation, fabrication, spam, and general '
        'categories. It extracts contact info and potential project info, then drafts an internal '
        'message alert and a 3-line auto-reply. Hot leads are routed directly to you in under a '
        'minute.',
        body))

    s.append(PageBreak())
    s.append(P('Orchestrator + Approval Queue', h3))
    s.append(P(
        'A central scheduler routes events to the right agent and lands all drafts in a single '
        'approval queue: one screen, one inbox, every brand. Approved items publish on the right '
        'schedule. Rejected items improve the prompts inside each agent.',
        body))

    s.append(callout(
        'What this replaces',
        'A marketing coordinator at $50,000 to $70,000 per year or an agency retainer for '
        'thousands of dollars per month. The Marketing Operating System does the same job with '
        'a 15-minute approval routine and roughly $200 per month in infrastructure.',
        bg=CHARCOAL, accent=ORANGE))

    s.append(PageBreak())

    s.append(P('System architecture', h2))
    s.append(P(
        'The pipeline is intentionally simple. Each box is replaceable; nothing is locked in.',
        body))

    # Inline architecture diagram as a table-of-cards
    arch_lbl  = S('AL', fontName='Helvetica-Bold', fontSize=7, textColor=ORANGE, leading=10, alignment=TA_CENTER)
    arch_box  = S('AB', fontName='Helvetica-Bold', fontSize=8.5, textColor=BLACK, leading=11, alignment=TA_CENTER)
    arch_note = S('AN', fontName='Helvetica', fontSize=7, textColor=GRAY_500, leading=9.5, alignment=TA_CENTER)
    arch_arrow= S('AA', fontName='Helvetica-Bold', fontSize=14, textColor=ORANGE, leading=16, alignment=TA_CENTER)

    def abox(label, title, note, bg=GRAY_50, accent=ORANGE):
        inner = Table([
            [P(label.upper(), arch_lbl)],
            [P(title, arch_box)],
            [P(note, arch_note)],
        ], colWidths=[1.95*inch])
        inner.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,-1), bg),
            ('TOPPADDING',(0,0),(-1,-1), 6),
            ('BOTTOMPADDING',(0,0),(-1,-1), 6),
            ('LEFTPADDING',(0,0),(-1,-1), 8),
            ('RIGHTPADDING',(0,0),(-1,-1), 8),
            ('LINEBEFORE',(0,0),(0,-1), 2.5, accent),
        ]))
        return inner

    arr = P('\u2192', arch_arrow)

    # Row 1: Inputs
    row1 = Table([[
        abox('INPUT', 'Foreman text-in', 'Photos + 2-sentence note via SMS'),
        arr,
        abox('AGENT', 'Field-to-Content', 'Drafts 5 outputs in brand voice'),
        arr,
        abox('HUMAN', 'Approval queue', 'Office manager: 15 min/day'),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row1.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row1)
    s.append(sp(8))

    row2 = Table([[
        abox('INPUT', 'Google review', 'New review on either brand', accent=TEAL),
        arr,
        abox('AGENT', 'Reputation', 'Drafts reply tuned to rating', accent=TEAL),
        arr,
        abox('HUMAN', 'Approval queue', 'Same single inbox', accent=TEAL),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row2.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row2)
    s.append(sp(8))

    row3 = Table([[
        abox('INPUT', 'Monthly schedule', 'Keyword + ranking data', accent=SPARK),
        arr,
        abox('AGENT', 'SEO Content', 'Drafts service-area page', accent=SPARK),
        arr,
        abox('HUMAN', 'Approval queue', 'Edit + publish to site', accent=SPARK),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row3.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row3)
    s.append(sp(8))

    row4 = Table([[
        abox('INPUT', 'Site contact form', 'Free-form inquiry text'),
        arr,
        abox('AGENT', 'Lead Triage', 'Classifies + drafts alert'),
        arr,
        abox('OUTPUT', 'Estimating + auto-reply', 'Hot lead routed in &lt;1 min'),
    ]], colWidths=[1.95*inch, 0.3*inch, 1.95*inch, 0.3*inch, 1.95*inch])
    row4.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(row4)

    s.append(sp(14))
    s.append(P(
        'Built on modern technology with direct connections to LinkedIn, Google Business Profile, '
        'and Meta.',
        body))

    s.append(P('Three-phase ownership transfer', h2))
    s.append(P(
        'You do not buy this and figure it out. We run it with you, then alongside you, then behind '
        'you. By month 7 your office manager is running the system in 15 minutes a day and we are on '
        'a maintenance retainer.',
        body))

    s.append(phase_card_basic('Phase 1', 'Concierge', 'Months 1\u20133',
        ['We run the system day-to-day while training it on your voice',
         '90 days of approved content captured to teach the system how you sound',
         'Office manager observes while we document everything on how to run the system']))
    s.append(sp(6))
    s.append(phase_card_basic('Phase 2', 'Co-pilot', 'Months 4\u20136',
        ['Office manager runs the approval queue while we maintain the system',
         'Weekly check-ins while we handle voice tuning and integrations',
         'Performance review at month 6 to right-size phase 3']))
    s.append(sp(6))
    s.append(phase_card_basic('Phase 3', 'Self-serve', 'Month 7+',
        ['You run it. We are on retainer for system maintenance only',
         'Quarterly strategy review and updates as Google and AI tools change',
         'Cancel anytime. The system keeps running either way']))

    # ── Realistic 12-month targets — compact comparison panel ────────────
    # Side-by-side brand layout - sits at the end of chapter 06.
    s.append(sp(10))

    cm_eyebrow  = S('CmEy', fontName='Helvetica-Bold', fontSize=7.5,
                    textColor=ORANGE, leading=10, alignment=TA_CENTER)
    cm_title    = S('CmTi', fontName='Helvetica-Bold', fontSize=13,
                    textColor=WHITE, leading=16, alignment=TA_CENTER, spaceAfter=2)
    cm_brand_j  = S('CmBJ', fontName='Helvetica-Bold', fontSize=9,
                    textColor=ORANGE, leading=12, alignment=TA_LEFT)
    cm_brand_c  = S('CmBC', fontName='Helvetica-Bold', fontSize=9,
                    textColor=SPARK, leading=12, alignment=TA_LEFT)
    cm_col_lbl  = S('CmCL', fontName='Helvetica-Bold', fontSize=6.5,
                    textColor=GRAY_500, leading=9, alignment=TA_CENTER)
    cm_col_lbl_with_o = S('CmCLwO', fontName='Helvetica-Bold', fontSize=6.5,
                    textColor=ORANGE, leading=9, alignment=TA_CENTER)
    cm_col_lbl_with_s = S('CmCLwS', fontName='Helvetica-Bold', fontSize=6.5,
                    textColor=SPARK, leading=9, alignment=TA_CENTER)
    cm_plat     = S('CmPl', fontName='Helvetica-Bold', fontSize=7.5,
                    textColor=GRAY_500, leading=10, alignment=TA_LEFT)
    cm_to_dim   = S('CmTd', fontName='Helvetica-Bold', fontSize=10,
                    textColor=GRAY_300, leading=13, alignment=TA_RIGHT)
    cm_to_full  = S('CmTf', fontName='Helvetica-Bold', fontSize=12,
                    textColor=WHITE, leading=15, alignment=TA_RIGHT)
    cm_lift     = S('CmLf', fontName='Helvetica-Bold', fontSize=7.5,
                    textColor=AMBER, leading=10, alignment=TA_CENTER)
    cm_foot_lbl = S('CmFL', fontName='Helvetica-Bold', fontSize=7.5,
                    textColor=AMBER, leading=10, alignment=TA_CENTER)
    cm_foot_val = S('CmFV', fontName='Helvetica-Bold', fontSize=11,
                    textColor=WHITE, leading=14, alignment=TA_CENTER)

    def _cm_ratio(without_n, with_n):
        try:
            w = int(str(without_n).replace(',', '').replace('+', ''))
            wi = int(str(with_n).replace(',', '').replace('+', ''))
            if w <= 0:
                return ''
            return f'{wi / w:.2f}×'
        except Exception:
            return ''

    def cm_metric_row(platform, without_n, with_n, brand_color):
        plat_style = S(f'cmpl{brand_color.hexval()}',
                       fontName='Helvetica-Bold', fontSize=7.5,
                       textColor=brand_color, leading=10, alignment=TA_LEFT)
        t = Table([[
            P(platform.upper(), plat_style),
            P(str(without_n), cm_to_dim),
            P(str(with_n),    cm_to_full),
            P(_cm_ratio(without_n, with_n), cm_lift),
        ]], colWidths=[0.7*inch, 0.62*inch, 0.7*inch, 0.5*inch])
        t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('TOPPADDING',(0,0),(-1,-1),2),
            ('BOTTOMPADDING',(0,0),(-1,-1),2),
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),3),
        ]))
        return t

    def cm_brand_block(brand_label, brand_style, accent, metrics):
        hdr = Table([[
            P('PLATFORM', cm_plat),
            P('W/O',  cm_col_lbl),
            P('W/MOS', cm_col_lbl_with_o if accent is ORANGE else cm_col_lbl_with_s),
            P('LIFT', cm_col_lbl),
        ]], colWidths=[0.7*inch, 0.62*inch, 0.7*inch, 0.5*inch])
        hdr.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('TOPPADDING',(0,0),(-1,-1),2),
            ('BOTTOMPADDING',(0,0),(-1,-1),4),
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),3),
            ('LINEBELOW',(0,0),(-1,-1),0.5, GRAY_700),
        ]))

        block = Table([
            [P(brand_label, brand_style)],
            [hdr],
        ] + [[cm_metric_row(p, w, m, accent)] for (p, w, m) in metrics],
        colWidths=[2.95*inch])
        block.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,-1), HexColor('#0E1115')),
            ('LEFTPADDING',(0,0),(-1,-1),10),
            ('RIGHTPADDING',(0,0),(-1,-1),10),
            ('TOPPADDING',(0,0),(0,0),8),
            ('BOTTOMPADDING',(0,-1),(-1,-1),8),
            ('LINEBEFORE',(0,0),(0,-1), 3, accent),
        ]))
        return block

    jones_block = cm_brand_block('JONES', cm_brand_j, ORANGE, [
        ('LinkedIn',  '600', '1,100'),
        ('Instagram', '600', '750'),
        ('Facebook',  '215', '300'),
    ])
    callus_block = cm_brand_block('CALLUS', cm_brand_c, SPARK, [
        ('LinkedIn',  '400', '550'),
        ('Instagram', '190', '350'),
        ('Facebook',  '100', '200'),
    ])

    cards_row = Table([[jones_block, '', callus_block]],
                      colWidths=[2.95*inch, 0.2*inch, 2.95*inch])
    cards_row.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
    ]))

    foot_strip = Table([
        [P('AVERAGE LIFT WITH MARKETING OS', cm_foot_lbl)],
        [P('1.6× more followers across both brands', cm_foot_val)],
    ], colWidths=[CONTENT_W - 32])
    foot_strip.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,-1),3),
        ('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))

    targets_panel = Table([
        [P('REALISTIC 12-MONTH TARGETS', cm_eyebrow)],
        [P('With and without the Marketing Operating System', cm_title)],
        [HRFlowable(width='100%', thickness=0.5, color=GRAY_700,
                    spaceBefore=6, spaceAfter=8)],
        [cards_row],
        [HRFlowable(width='100%', thickness=0.5, color=GRAY_700,
                    spaceBefore=8, spaceAfter=6)],
        [foot_strip],
    ], colWidths=[CONTENT_W])
    targets_panel.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), CHARCOAL),
        ('LEFTPADDING',(0,0),(-1,-1),16),
        ('RIGHTPADDING',(0,0),(-1,-1),16),
        ('TOPPADDING',(0,0),(0,0),12),
        ('BOTTOMPADDING',(0,-1),(-1,-1),12),
        ('TOPPADDING',(0,1),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-2),0),
        ('LINEBEFORE',(0,0),(0,-1), 3, ORANGE),
    ]))
    s.append(targets_panel)

    s.append(PageBreak())

    # ═══ 07 INVESTMENT & TIMELINE ════════════════════════════════════════════
    s.append(section_header(7, 'Investment &amp; Timeline',
        kicker='Fixed-price build, three-tier ongoing model.'))

    s.append(P('Build phase: fixed price', h2))

    s.append(price_row('Brand system: Jones',
                       '$3,500',
                       'Logo refresh, palette, typography, usage guide.'))
    s.append(price_row('Brand system: Callus',
                       '$4,500',
                       'New brand identity from the ground up: logo system, palette, tone of voice, and brand guidelines.'))
    s.append(price_row('Website: tooneconstruction.com',
                       '$8,500',
                       '7 templated pages plus service-area pages.'))
    s.append(price_row('Website: ',
                       '$7,500',
                       '7 templated pages plus shop section.'))
    s.append(price_row('SEO foundation (both)',
                       '$3,500',
                       'Google Business Profile setup, structured data, business listings, technical audit, on-page work.'))
    s.append(price_row('Content shoot + initial library',
                       '$8,000',
                       '3-day shoot at Jones sites and 1-day shoot at Callus shop. Photo and video, plus a 90-day post library.'))
    s.append(price_row('Hype video: Jones',
                       '$1,000',
                       'Branded hype video edited from shoot footage. ~10 hours of editing.'))
    s.append(price_row('Hype video: Callus',
                       '$1,000',
                       'Branded hype video edited from shoot footage. ~10 hours of editing.'))
    s.append(price_row('Build phase total',
                       '$37,500',
                       'One-time. Static buildout: brand, websites, SEO foundation, and content library.',
                       highlight=True))

    s.append(sp(8))
    s.append(P('Marketing Operating System', h2))
    s.append(P(
        'A separate, one-time build that delivers the agents, approval queue, and integrations. '
        'Operated under a monthly retainer (three tiers below) that covers ongoing support and '
        'maintenance.',
        body))

    s.append(price_row('Marketing Operating System build',
                       '$17,700',
                       'Five agents, central scheduler, approval queue, brand-voice training, and integrations. Full support for the Marketing Operating System and a monthly report.'))
    s.append(price_row('Combined build total',
                       '$55,200',
                       'Build phase ($37,500) plus Marketing Operating System build ($17,700). 40% on signature, 30% at design approval, 30% at launch.',
                       highlight=True))

    s.append(P('Engagement at a glance', h2))
    s.append(P(
        'The full arc on one axis: a 90-day build, then a phased retainer that steps down as your team takes the wheel.',
        body))
    s.append(sp(4))

    # \u2500\u2500 Engagement timeline strip \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    eg_period = S('egp', fontName='Helvetica-Bold', fontSize=7,
                  textColor=GRAY_500, leading=10, alignment=TA_CENTER)
    eg_phase  = S('egn', fontName='Helvetica-Bold', fontSize=11,
                  textColor=WHITE, leading=14, alignment=TA_CENTER)
    eg_cost   = S('egc', fontName='Helvetica-Bold', fontSize=8.5,
                  textColor=WHITE, leading=12, alignment=TA_CENTER)
    eg_sub    = S('egs', fontName='Helvetica', fontSize=7.5,
                  textColor=HexColor('#F0EFEA'), leading=10, alignment=TA_CENTER)

    periods = [
        P('WEEKS 1\u201312', eg_period),
        P('MONTHS 1\u20133 POST-LAUNCH', eg_period),
        P('MONTHS 4\u20136', eg_period),
        P('MONTHS 7+', eg_period),
    ]
    phases = [
        P('BUILD', eg_phase),
        P('CONCIERGE', eg_phase),
        P('CO-PILOT', eg_phase),
        P('SELF-SERVE', eg_phase),
    ]
    costs = [
        [P('$55,200', eg_cost), P('one-time', eg_sub)],
        [P('Included', eg_cost), P('in build', eg_sub)],
        [P('$850 / mo', eg_cost), P('infra included', eg_sub)],
        [P('\u2264 $350 / mo', eg_cost), P('+ ~$200 infra', eg_sub)],
    ]

    eg_data = [periods, phases, costs]
    eg = Table(eg_data, colWidths=[1.85*inch]*4, rowHeights=[0.32*inch, 0.42*inch, 0.6*inch])
    eg.setStyle(TableStyle([
        # Period row (light gray bg)
        ('BACKGROUND',(0,0),(-1,0), GRAY_50),
        ('VALIGN',(0,0),(-1,0),'MIDDLE'),
        # Phase row colors
        ('BACKGROUND',(0,1),(0,1), ORANGE),
        ('BACKGROUND',(1,1),(1,1), HexColor('#C9501A')),  # darker orange
        ('BACKGROUND',(2,1),(2,1), AMBER),
        ('BACKGROUND',(3,1),(3,1), HexColor('#4A4845')),   # GRAY_700
        ('VALIGN',(0,1),(-1,1),'MIDDLE'),
        # Cost row colors (slightly darker variants)
        ('BACKGROUND',(0,2),(0,2), HexColor('#B84A14')),
        ('BACKGROUND',(1,2),(1,2), HexColor('#9C3D10')),
        ('BACKGROUND',(2,2),(2,2), HexColor('#C8861C')),
        ('BACKGROUND',(3,2),(3,2), HexColor('#2F2D2A')),
        ('VALIGN',(0,2),(-1,2),'MIDDLE'),
        # Universal padding
        ('LEFTPADDING',(0,0),(-1,-1),6),
        ('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),4),
        ('BOTTOMPADDING',(0,0),(-1,-1),4),
        # Thin white separators between phase columns
        ('LINEAFTER',(0,1),(2,2), 1, WHITE),
    ]))
    s.append(eg)
    s.append(sp(4))
    s.append(P(
        '<font size="8" color="#8A8880"><i>Build is one-time. Retainer phases begin at launch (weeks 10\u201312) and can step down a tier with 30 days\u2019 notice after month 3.</i></font>',
        body))
    s.append(sp(14))

    s.append(P('Marketing Operating System retainer: three tiers', h2))
    s.append(P(
        'Pick the tier that matches how hands-on you want to be. The descriptions below detail what each phase covers.',
        body))

    s.append(price_row('Concierge: we run it',
                       'No fee<br/><font size="8">infrastructure included</font>',
                       '<b>First 3 months after launch.</b> Default tier. Included in the Marketing Operating System build above. We operate the system and you receive a monthly report.',
                       highlight=False))
    s.append(price_row('Co-pilot: you run it, we maintain',
                       '$850 / mo<br/><font size="8">infrastructure included</font>',
                       '<b>Months 4\u20136 post-launch.</b> Recommended next step. Office manager runs the queue while we tune the system.'))
    s.append(price_row('Self-serve: system maintenance',
                       'up to $350 / mo<br/><font size="8">or $150/hour, whichever is less</font><br/><font size="8" color="#8A8880">+ ~$200/mo infrastructure</font>',
                       '<b>Month 7+ post-launch.</b> Quarterly strategy review, voice updates, and integration patches. Infrastructure (AI, hosting, scheduler, email) passes through at cost — billed through us at zero markup, or moved to your own accounts.'))

    s.append(PageBreak())
    s.append(P('Timeline: 90 days to launch', h2))

    def phase_card(num, title, weeks, items, bg=GRAY_50, accent=ORANGE):
        ph_s = S('ps', fontName='Helvetica-Bold', fontSize=8, textColor=accent, leading=11)
        ti_s = S('pt', fontName='Helvetica-Bold', fontSize=11, textColor=BLACK, leading=14)
        wk_s = S('pw', fontName='Helvetica-Bold', fontSize=7.5, textColor=GRAY_500, leading=10)
        it_s = S('pi', fontName='Helvetica',     fontSize=8.5, textColor=GRAY_700, leading=12)
        items_html = '<br/>'.join([f'\u2022 {x}' for x in items])
        data = [[P(num, ph_s), P(title, ti_s), P(weeks.upper(), wk_s), P(items_html, it_s)]]
        t = Table(data, colWidths=[0.55*inch, 1.65*inch, 1.0*inch, 3.4*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,-1), bg),
            ('TOPPADDING',(0,0),(-1,-1),12),
            ('BOTTOMPADDING',(0,0),(-1,-1),12),
            ('LEFTPADDING',(0,0),(-1,-1),12),
            ('RIGHTPADDING',(0,0),(-1,-1),12),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LINEBEFORE',(0,0),(0,-1),3, accent),
        ]))
        return t

    s.append(phase_card('01', 'Discovery + Brand', 'Weeks 1\u20133',
        ['Stakeholder interviews; site audit',
         'Jones brand refresh; Callus brand build',
         'Photography and videography for 4 days at active jobsites + shop',
         'Google Business Profile setup and business listing pass',
         'You approve the brand work before we start the website']))
    s.append(sp(6))
    s.append(phase_card('02', 'Design + Build', 'Weeks 4\u20139',
        ['Both sites designed and built for each company’s needs',
         'Content drafted with leadership input',
         'You approve the design and content before we launch']))
    s.append(sp(6))
    s.append(phase_card('03', 'Launch + Activate', 'Weeks 10\u201312',
        ['Soft launch \u2192 final QA \u2192 hard launch',
         'LinkedIn relaunch with refreshed pages and content',
         'Review ask program activated for both brands',
         'Marketing Operating System goes live. Concierge phase begins (included in build).']))


    s.append(sp(14))
    s.append(callout(
        'What you own at the end',
        'You own all your data, content, brand identity, and historical drafts. To keep operating '
        'the Marketing Operating System, you can stay on the $350/mo Self-serve retainer or pay '
        '$150/hour for support, whichever is less. Move on whenever you want, and your data, '
        'content, and brand work come with you.',
        bg=CHARCOAL, accent=ORANGE))
    s.append(PageBreak())

    # ═══ 08 NEXT STEPS ═══════════════════════════════════════════════════════
    s.append(section_header(8, 'Next Steps',
        kicker='What we need to start, and when we can start.'))

    s.append(P('Approvals required', h3))
    s.append(bullet('Sign-off on this proposal (this PDF and a brief Master Service Agreement).'))
    s.append(bullet('Decision on Callus concept. The Spark direction is the recommended path '
                    'and what the website concept reflects today.'))
    s.append(bullet('Designated point of contact at each company for weekly check-ins.'))

    s.append(P('What we need from you', h3))
    s.append(bullet('Google Business Profile and social account access (or the green light to claim/create).'))
    s.append(bullet('Domain access for both tooneconstruction.com and .'))
    s.append(bullet('Two to three upcoming jobsites we can shoot in weeks 2\u20133.'))
    s.append(bullet('A list of 3\u20135 case-study-worthy projects from the last 5 years.'))

    s.append(P('Kickoff', h3))
    s.append(P(
        'On signature we hold a 60-minute kickoff with leadership from both companies, agree on the '
        'first jobsite shoot date, and start the brand work the same week. The 90-day clock starts '
        'on signature.',
        body))

    s.append(sp(20))
    s.append(callout(
        'A note on the work',
        'Jones has built something real over four generations. Callus is a chance to build '
        'something new on top of that foundation. The deliverables in this proposal exist to '
        'serve that, not the other way around. If anything in here does not fit how you want '
        'to be in the world, tell us and we will adjust before we start. We work for you.',
        bg=CHARCOAL, accent=ORANGE))

    s.append(sp(28))

    # Sign-off block
    sign_lbl = S('SL', fontName='Helvetica-Bold', fontSize=8, textColor=ORANGE, leading=11)
    sign_body= S('SB', fontName='Helvetica',      fontSize=9, textColor=GRAY_700, leading=13)
    sign_line= S('SLn',fontName='Helvetica-Bold', fontSize=10, textColor=BLACK, leading=14)

    sign_data = [
        [P('PREPARED BY', sign_lbl), '', P('APPROVED BY', sign_lbl)],
        [P('Project Lead', sign_body), '', P('Toone Construction Co., Authorized Signer', sign_body)],
        [P('_________________________', sign_line), '', P('_________________________', sign_line)],
        [P('Date', sign_body), '', P('Date', sign_body)],
    ]
    sign = Table(sign_data, colWidths=[2.7*inch, 0.5*inch, 3.4*inch])
    sign.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),3),
        ('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
    ]))
    s.append(sign)

    # Build
    doc.build(s, onFirstPage=cb.on_page, onLaterPages=cb.on_page)
    print(f'PDF saved -> {OUTPUT}')

if __name__ == '__main__':
    build()
