import os
D="/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/kingdom_of_the_sun/logo_v1"
NAVY="#0B1F3A"; GOLD="#F4B41A"; ORANGE="#E8651E"; CREAM="#F7F2E7"

# Unified crown body (one path), 5 points, solid to base. Sun nested in body, framed by a bg-color moat.
BODY_FULL = ("M 44,150 L 60,76 L 75,108 L 90,56 L 105,104 L 120,40 "
             "L 135,104 L 150,56 L 165,108 L 180,76 L 196,150 Z")
BODY_SIMPLE = ("M 50,150 L 70,78 L 95,112 L 120,44 L 145,112 L 170,78 L 190,150 Z")  # 3 points

def emblem(bg_for_moat, ray_fill, sun_fill, band_fill, simplified=False):
    body = BODY_SIMPLE if simplified else BODY_FULL
    moat_r = 32 if simplified else 28
    sun_r  = 24 if simplified else 21
    cx,cy = 120,(122 if simplified else 120)
    p=[]
    p.append(f'<path d="{body}" fill="{ray_fill}"/>')
    # base band
    if simplified:
        p.append(f'<rect x="42" y="150" width="156" height="22" rx="6" fill="{band_fill}"/>')
    else:
        p.append(f'<rect x="40" y="150" width="160" height="17" rx="5" fill="{band_fill}"/>')
        p.append(f'<rect x="50" y="172" width="140" height="9" rx="4" fill="{band_fill}"/>')
    # sun nested: bg-color moat then sun disc
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{moat_r}" fill="{bg_for_moat}"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{sun_r}" fill="{sun_fill}"/>')
    return "\n  ".join(p)

def svg(bg, ray_fill, sun_fill, band_fill, simplified=False, transparent=False):
    moat = NAVY if transparent else bg  # on transparent, frame sun with navy
    bgrect = '' if transparent else f'<rect width="240" height="240" fill="{bg}"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">
  {bgrect}
  {emblem(moat,ray_fill,sun_fill,band_fill,simplified)}
</svg>'''

variants = {
 "primary_gold_on_navy.svg":  svg(NAVY, GOLD, ORANGE, GOLD),
 "inverse_navy_on_cream.svg": svg(CREAM, NAVY, ORANGE, NAVY),
 "onecolor_navy.svg":         svg(CREAM, NAVY, NAVY, NAVY),
 "onecolor_gold.svg":         svg(NAVY, GOLD, GOLD, GOLD),
 "transparent_gold.svg":      svg(NAVY, GOLD, ORANGE, GOLD, transparent=True),
 "favicon_navybg.svg":        svg(NAVY, GOLD, ORANGE, GOLD, simplified=True),
 "favicon_creambg.svg":       svg(CREAM, NAVY, ORANGE, NAVY, simplified=True),
}
for n,c in variants.items(): open(os.path.join(D,n),"w").write(c)

def lockup_stacked(bg,rf,sf,bf,tf):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 360" width="520" height="360">
  <rect width="520" height="360" fill="{bg}"/>
  <g transform="translate(140,14)">{emblem(bg,rf,sf,bf)}</g>
  <text x="260" y="292" text-anchor="middle" fill="{tf}" font-family="'Avenir Next Condensed','Futura','Arial Narrow',sans-serif" font-weight="700" font-size="44" letter-spacing="3">KINGDOM OF THE SUN</text>
  <text x="260" y="320" text-anchor="middle" fill="{tf}" font-family="'Avenir Next','Helvetica Neue',sans-serif" font-weight="500" font-size="13.5" letter-spacing="2" opacity="0.85">52ND ANNUAL  ·  EST. 1974  ·  THE ORIGINAL  ·  OCALA, FL</text>
</svg>'''
def lockup_horizontal(bg,rf,sf,bf,tf):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 240" width="780" height="240">
  <rect width="780" height="240" fill="{bg}"/>
  <g transform="translate(8,8) scale(0.92)">{emblem(bg,rf,sf,bf)}</g>
  <text x="248" y="118" fill="{tf}" font-family="'Avenir Next Condensed','Futura','Arial Narrow',sans-serif" font-weight="700" font-size="50" letter-spacing="3">KINGDOM OF THE SUN</text>
  <text x="250" y="150" fill="{tf}" font-family="'Avenir Next','Helvetica Neue',sans-serif" font-weight="500" font-size="15" letter-spacing="2" opacity="0.85">52ND ANNUAL · EST. 1974 · THE ORIGINAL · OCALA, FL</text>
</svg>'''
open(os.path.join(D,"lockup_stacked_navy.svg"),"w").write(lockup_stacked(NAVY,GOLD,ORANGE,GOLD,CREAM))
open(os.path.join(D,"lockup_horizontal_cream.svg"),"w").write(lockup_horizontal(CREAM,NAVY,ORANGE,NAVY,NAVY))
print("rebuilt")
