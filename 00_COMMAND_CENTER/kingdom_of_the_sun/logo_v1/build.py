import os
D="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/kingdom_of_the_sun/logo_v1"
NAVY="#0B1F3A"; GOLD="#F4B41A"; ORANGE="#E8651E"; CREAM="#F7F2E7"
OFFY=8  # optical recenter (shift down)

# ----------------------------------------------------------------------------
# Crown / Sun Rays · refined geometry (2026-06-01 brand pass).
# Refinement, not a redraw: same 5-peak crown-as-sunrise concept, hardened for
# small sizes and embroidery. Three geometry levels:
#   full   = 5 peaks, primary identity (header, deck, cards, program)
#   simple = 3 bold peaks, single thick bar, bigger disc (favicon / small <=24px)
#   emb    = 3 fat peaks, no thin bar, thick strokes (shirt / embroidery)
# The sun disc was strengthened across all three (improves one-color + small use).
# ----------------------------------------------------------------------------

def body_full(o):
    # widened valleys vs v1 so the 5 spikes stay distinct as they shrink
    pts=[(44,150),(60,80),(76,108),(91,60),(106,106),(120,46),(134,106),(149,60),(164,108),(180,80),(196,150)]
    return "M "+" L ".join(f"{x},{y+o}" for x,y in pts)+" Z"

def body_simple(o):
    # 3 bold peaks for favicon / small size
    pts=[(50,150),(73,84),(96,112),(120,52),(144,112),(167,84),(190,150)]
    return "M "+" L ".join(f"{x},{y+o}" for x,y in pts)+" Z"

def body_emb(o):
    # 3 fat peaks, shallow valleys, fewer fragile thin points for stitching
    pts=[(52,150),(76,92),(98,110),(120,58),(142,110),(164,92),(188,150)]
    return "M "+" L ".join(f"{x},{y+o}" for x,y in pts)+" Z"

def emblem(ray, sun, band, moat, mode="full", shadow=False):
    o=OFFY; cx=120; p=[]
    if mode=="full":
        body=body_full(o); soften=3.5; moat_r=30; sun_r=24; cy=118+o
        bars=[(40,150,160,13,5),(54,168,132,7,3.5)]   # main bar + thin lower accent
    elif mode=="simple":
        body=body_simple(o); soften=5.5; moat_r=34; sun_r=27; cy=120+o
        bars=[(50,150,140,17,7)]                       # one thick rounded bar
    else:  # emb
        body=body_emb(o); soften=8; moat_r=35; sun_r=28; cy=120+o
        bars=[(54,152,132,18,9)]                       # one fat bar, no thin details
    sid=""
    if shadow:
        sid=' filter="url(#sh)"'
    g=f'<g{sid}>'
    # rounded joins via same-color stroke = softened tips/valleys
    g+=f'<path d="{body}" fill="{ray}" stroke="{ray}" stroke-width="{soften}" stroke-linejoin="round"/>'
    for (x,y,w,h,r) in bars:
        g+=f'<rect x="{x}" y="{y+o}" width="{w}" height="{h}" rx="{r}" fill="{band}"/>'
    g+=f'<circle cx="{cx}" cy="{cy}" r="{moat_r}" fill="{moat}"/>'
    g+=f'<circle cx="{cx}" cy="{cy}" r="{sun_r}" fill="{sun}"/>'
    g+='</g>'
    return g

def svg(bg, ray, sun, band, moat=None, mode="full", transparent=False, shadow=False):
    moat = (NAVY if transparent else bg) if moat is None else moat
    bgrect='' if transparent else f'<rect width="240" height="240" fill="{bg}"/>'
    defs=''
    if shadow:
        defs=('<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%">'
              '<feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#000" flood-opacity="0.45"/>'
              '</filter></defs>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">'
            f'{defs}{bgrect}{emblem(ray,sun,band,moat,mode,shadow)}</svg>')

variants={
 # --- primary system (5-peak, strengthened disc) ---
 "primary_gold_on_navy.svg": svg(NAVY, GOLD, ORANGE, GOLD),
 "inverse_navy_on_cream.svg": svg(CREAM, NAVY, ORANGE, NAVY),
 "reversed_navy_on_gold.svg": svg(GOLD, NAVY, ORANGE, NAVY, moat=GOLD),
 "cream_on_navy.svg":        svg(NAVY, CREAM, NAVY, CREAM, moat=CREAM),   # 1-color cream, sun = navy knockout
 # --- one-color ---
 "onecolor_navy.svg":        svg(CREAM, NAVY, CREAM, NAVY, moat=NAVY),    # navy mark, sun = cream knockout
 "onecolor_gold.svg":        svg(NAVY, GOLD, NAVY, GOLD, moat=GOLD),      # gold mark, sun = navy knockout
 # --- on-photo (transparent + soft shadow, drop onto any photography) ---
 "on_photo_gold.svg":        svg(NAVY, GOLD, ORANGE, GOLD, transparent=True, shadow=True),
 "transparent_gold.svg":     svg(NAVY, GOLD, ORANGE, GOLD, transparent=True),
 # --- favicon / small size (3-peak, bigger disc, single bar) ---
 "favicon_navybg.svg":       svg(NAVY, GOLD, ORANGE, GOLD, mode="simple"),
 "favicon_creambg.svg":      svg(CREAM, NAVY, ORANGE, NAVY, mode="simple"),
 # --- embroidery-safe (fat peaks, thick bar, no fragile detail) ---
 "embroidery_gold_on_navy.svg": svg(NAVY, GOLD, ORANGE, GOLD, mode="emb"),
 "embroidery_onecolor.svg":     svg(NAVY, GOLD, NAVY, GOLD, moat=GOLD, mode="emb"),  # 1-thread gold
}
for n,c in variants.items(): open(os.path.join(D,n),"w").write(c)

# clear-space + min-size usage frame
CS=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 300" width="360" height="300">
<rect width="360" height="300" fill="{CREAM}"/>
<rect x="70" y="40" width="220" height="200" fill="none" stroke="#bbb" stroke-dasharray="5 5"/>
<rect x="100" y="58" width="160" height="160" fill="none" stroke="#cf2b2b" stroke-width="1"/>
<g transform="translate(70,28) scale(0.83)">{emblem(NAVY,ORANGE,NAVY,CREAM)}</g>
<text x="180" y="262" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#0B1F3A">Clear space = X on all sides (X = main-bar height)</text>
<text x="180" y="280" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#666">Min digital: full mark >=32px · use favicon variant at <=24px</text>
</svg>'''
open(os.path.join(D,"usage_clearspace.svg"),"w").write(CS)

SUBLINE="53RD ANNUAL  ·  EST. 1974  ·  THE ORIGINAL  ·  OCALA, FL"
def stacked(bg,rf,sf,bf,tf,moat):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 360" width="560" height="360">
  <rect width="560" height="360" fill="{bg}"/>
  <g transform="translate(160,8)">{emblem(rf,sf,bf,moat)}</g>
  <text x="280" y="296" text-anchor="middle" fill="{tf}" font-family="'Futura','Avenir Next','Helvetica Neue',sans-serif" font-weight="700" font-size="33" letter-spacing="4">KINGDOM OF THE SUN</text>
  <text x="280" y="324" text-anchor="middle" fill="{tf}" font-family="'Avenir Next','Helvetica Neue',sans-serif" font-weight="500" font-size="13" letter-spacing="2" opacity="0.85">{SUBLINE}</text>
</svg>'''
def horiz(bg,rf,sf,bf,tf,moat):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 240" width="780" height="240">
  <rect width="780" height="240" fill="{bg}"/>
  <g transform="translate(6,4) scale(0.92)">{emblem(rf,sf,bf,moat)}</g>
  <text x="248" y="118" fill="{tf}" font-family="'Futura','Avenir Next','Helvetica Neue',sans-serif" font-weight="700" font-size="48" letter-spacing="3">KINGDOM OF THE SUN</text>
  <text x="250" y="150" fill="{tf}" font-family="'Avenir Next','Helvetica Neue',sans-serif" font-weight="500" font-size="14.5" letter-spacing="2" opacity="0.85">53RD ANNUAL · EST. 1974 · THE ORIGINAL · OCALA, FL</text>
</svg>'''
open(os.path.join(D,"lockup_stacked_navy.svg"),"w").write(stacked(NAVY,GOLD,ORANGE,GOLD,CREAM,NAVY))
open(os.path.join(D,"lockup_horizontal_cream.svg"),"w").write(horiz(CREAM,NAVY,ORANGE,NAVY,NAVY,CREAM))
print("refined Crown build written")
