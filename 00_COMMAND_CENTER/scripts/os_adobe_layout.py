#!/usr/bin/env python3
"""
os_adobe_layout.py , layout / typography layer (closes the Illustrator/InDesign gap, locally + logged).

Renders branded campaign layouts from a hero image + text. Deterministic, reversible, logged.
SNIPED editorial kit: Didot display, Baskerville body, Arial UI; neutral paper, ink, auction-red accent.

  titlecard --out IMG --w W --h H [--kicker K] --title T [--subtitle S] [--bg ink|paper]
  poster    --src HERO --out IMG --masthead M [--lot "LOT 00"] [--logline L] [--footer F]
  onesheet  --src HERO --out IMG --title T --logline L [--details "k:v;k:v"]
  landing   --src HERO --out IMG --headline H [--sub S] [--cta "Request access"]
  lookbook  --src HERO --out IMG [--caption C]
  carousel  --src HERO --outdir DIR --slides slides.json
  board     --out IMG --title T --manifest board.json     (grid contact / pitch board)
"""
import os, sys, json, argparse, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
def _asset():
    s = importlib.util.spec_from_file_location("os_adobe_asset", os.path.join(HERE, "os_adobe_asset.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

SUP = "/System/Library/Fonts/Supplemental/"
INK = (20, 17, 15); PAPER = (236, 231, 221); CREAM = (216, 207, 190)
RED = (142, 28, 22); GREY = (138, 138, 140); FAINT = (120, 116, 110)

def _font(kind, size):
    from PIL import ImageFont
    table = {
        "display": [(SUP+"Didot.ttc", 0), (SUP+"Baskerville.ttc", 0), (SUP+"Georgia Bold.ttf", None)],
        "display_it": [(SUP+"Didot.ttc", 1), (SUP+"Georgia Italic.ttf", None)],
        "body": [(SUP+"Baskerville.ttc", 0), (SUP+"Georgia.ttf", None)],
        "ui": [(SUP+"Arial.ttf", None)], "ui_bold": [(SUP+"Arial Bold.ttf", None)],
        "mono": [(SUP+"Arial Narrow.ttf", None)],
    }
    for path, idx in table.get(kind, table["body"]):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size, index=idx) if idx is not None else ImageFont.truetype(path, size)
            except Exception: continue
    return ImageFont.load_default()

def _cover(im, w, h, fx=0.5, fy=0.5):
    from PIL import Image
    iw, ih = im.size; t = w/h
    if iw/ih > t: cw, ch = int(ih*t), ih
    else: cw, ch = iw, int(iw/t)
    x = int(max(0, min(fx*iw - cw/2, iw-cw))); y = int(max(0, min(fy*ih - ch/2, ih-ch)))
    return im.crop((x, y, x+cw, y+ch)).resize((w, h), Image.LANCZOS)

def _tracked(draw, xy, text, font, fill, tracking=0, anchor=None):
    if tracking == 0:
        draw.text(xy, text, font=font, fill=fill, anchor=anchor); return
    x, y = xy
    if anchor and "m" in anchor[0:1]:
        total = sum((draw.textlength(c, font=font) + tracking) for c in text) - tracking
        x -= total/2
    for c in text:
        draw.text((x, y), c, font=font, fill=fill, anchor=("l"+anchor[1]) if anchor else None)
        x += draw.textlength(c, font=font) + tracking

def _scrim(im, top=False, bottom=True, strength=190):
    from PIL import Image
    w, h = im.size; ov = Image.new("L", (w, h), 0); import numpy as np
    a = np.zeros((h, w), np.uint8); g = np.linspace(0, 1, h)
    col = np.zeros(h)
    if bottom: col = np.maximum(col, np.clip((g-0.5)/0.5, 0, 1)**1.4 * strength)
    if top: col = np.maximum(col, np.clip((0.42-g)/0.42, 0, 1)**1.4 * strength)
    a = (col[:, None] * np.ones((1, w))).astype(np.uint8)
    ov = Image.fromarray(a, "L"); black = Image.new("RGB", (w, h), (8, 7, 6))
    return Image.composite(black, im, ov)

def _wrap(draw, text, font, maxw):
    words = text.split(); lines = []; cur = ""
    for wd in words:
        t = (cur+" "+wd).strip()
        if draw.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    if cur: lines.append(cur)
    return lines

def titlecard(out, w, h, kicker, title, subtitle, bg, log=None):
    from PIL import Image, ImageDraw
    base, fg = (INK, PAPER) if bg == "ink" else (PAPER, INK)
    im = Image.new("RGB", (w, h), base); d = ImageDraw.Draw(im)
    cx = w//2
    d.line([(cx-40, int(h*0.30)), (cx+40, int(h*0.30))], fill=RED, width=3)
    if kicker: _tracked(d, (cx, int(h*0.36)), kicker.upper(), _font("ui", max(14, w//60)), RED, tracking=max(3, w//240), anchor="mm")
    tf = _font("display", max(40, w//12))
    for i, ln in enumerate(_wrap(d, title, tf, int(w*0.82))):
        d.text((cx, int(h*0.46)+i*int(tf.size*1.05)), ln, font=tf, fill=fg, anchor="mm")
    if subtitle:
        sf = _font("display_it", max(20, w//34))
        d.text((cx, int(h*0.70)), subtitle, font=sf, fill=FAINT if bg=="paper" else CREAM, anchor="mm")
    im.save(out)
    if log: _asset().log_edit(log, "layout:titlecard", out, out, f"{w}x{h} bg={bg}", title)
    return out

def poster(src, out, masthead, lot, logline, footer, log=None, tagline="EDITORIAL CAMPAIGN"):
    from PIL import Image, ImageDraw
    W, H = 1500, 2100
    hero = _cover(Image.open(src).convert("RGB"), W, H, 0.52, 0.5)
    im = _scrim(hero, top=True, bottom=True, strength=205); d = ImageDraw.Draw(im)
    # top masthead
    mf = _font("display", 150)
    d.text((W//2, 150), masthead.upper(), font=mf, fill=PAPER, anchor="mm")
    if tagline:
        _tracked(d, (W//2, 250), tagline.upper(), _font("ui", 26), CREAM, tracking=10, anchor="mm")
    # bottom lot + logline
    if lot:
        lf = _font("display", 130); d.text((90, H-300), lot, font=lf, fill=PAPER)
        d.line([(92, H-180), (92+ d.textlength(lot, font=lf), H-180)], fill=RED, width=4)
    if logline:
        for i, ln in enumerate(_wrap(d, logline, _font("display_it", 46), W-180)):
            d.text((90, H-150+i*56), ln, font=_font("display_it", 46), fill=CREAM)
    if footer:
        _tracked(d, (W//2, H-52), footer.upper(), _font("ui", 22), CREAM, tracking=8, anchor="mm")
    im.save(out)
    if log: _asset().log_edit(log, "layout:poster", src, out, f"{W}x{H}", masthead)
    return out

def onesheet(src, out, title, logline, details, log=None):
    from PIL import Image, ImageDraw
    W, H = 1700, 2200; im = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(im)
    hero = _cover(Image.open(src).convert("RGB"), W-160, 1180, 0.52, 0.42)
    im.paste(hero, (80, 80))
    y = 1330
    _tracked(d, (80, y), "LOT 00  ,  THE ESTATE OF HER", _font("ui", 24), RED, tracking=6); y += 60
    tf = _font("display", 96)
    for ln in _wrap(d, title, tf, W-160): d.text((80, y), ln, font=tf, fill=INK); y += int(tf.size*1.02)
    y += 20; bf = _font("display_it", 44)
    for ln in _wrap(d, logline, bf, W-160): d.text((80, y), ln, font=bf, fill=FAINT); y += 56
    y += 30; d.line([(80, y), (W-80, y)], fill=(190,182,168), width=2); y += 30
    if details:
        for kv in details.split(";"):
            if ":" in kv:
                k, v = kv.split(":", 1)
                _tracked(d, (80, y), k.strip().upper(), _font("ui_bold", 22), INK, tracking=4)
                d.text((520, y-4), v.strip(), font=_font("body", 34), fill=(60,56,52)); y += 58
    im.save(out)
    if log: _asset().log_edit(log, "layout:onesheet", src, out, f"{W}x{H}", title)
    return out

def landing(src, out, headline, sub, cta, log=None):
    from PIL import Image, ImageDraw
    W, H = 1440, 900
    hero = _cover(Image.open(src).convert("RGB"), W, H, 0.55, 0.42)
    im = _scrim(hero, bottom=True, top=True, strength=170); d = ImageDraw.Draw(im)
    # faux browser chrome
    d.rectangle([0,0,W,40], fill=(28,26,24))
    for i,c in enumerate([(237,106,94),(245,191,79),(98,197,84)]): d.ellipse([18+i*26,14,32+i*26,28], fill=c)
    _tracked(d, (W//2, 20), "private preview  ,  not hosted", _font("ui", 15), (150,146,140), tracking=2, anchor="mm")
    _tracked(d, (90, 110), "THE ESTATE OF HER", _font("ui", 22), CREAM, tracking=10)
    hf = _font("display", 92)
    for i, ln in enumerate(_wrap(d, headline, hf, int(W*0.62))):
        d.text((90, 360+i*int(hf.size*1.02)), ln, font=hf, fill=PAPER)
    if sub:
        d.text((92, 560), sub, font=_font("display_it", 38), fill=CREAM)
    # CTA button
    bx, by, bw, bh = 92, 660, 360, 70
    d.rectangle([bx, by, bx+bw, by+bh], fill=RED)
    d.text((bx+bw//2, by+bh//2), cta, font=_font("ui_bold", 26), fill=PAPER, anchor="mm")
    im.save(out)
    if log: _asset().log_edit(log, "layout:landing", src, out, f"{W}x{H}", headline)
    return out

def lookbook(src, out, caption, log=None):
    from PIL import Image, ImageDraw
    W, H = 1600, 2000; im = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(im)
    hero = _cover(Image.open(src).convert("RGB"), W-200, H-360, 0.52, 0.45); im.paste(hero, (100, 110))
    _tracked(d, (100, H-200), "PLATE 01", _font("ui", 22), RED, tracking=8)
    if caption:
        for i, ln in enumerate(_wrap(d, caption, _font("display_it", 40), W-200)):
            d.text((100, H-150+i*50), ln, font=_font("display_it", 40), fill=(70,66,62))
    im.save(out)
    if log: _asset().log_edit(log, "layout:lookbook", src, out, f"{W}x{H}", "plate")
    return out

def carousel(src, outdir, slides_path, log=None):
    from PIL import Image, ImageDraw
    os.makedirs(outdir, exist_ok=True)
    slides = json.load(open(slides_path)); W = H = 1080; outs = []
    hero = Image.open(src).convert("RGB")
    for i, s in enumerate(slides):
        kind = s.get("kind", "text")
        if kind == "cover":
            im = _scrim(_cover(hero, W, H, 0.52, 0.42), top=True, bottom=True, strength=200); d = ImageDraw.Draw(im)
            d.text((W//2, 120), s.get("masthead","LOT 00").upper(), font=_font("display", 120), fill=PAPER, anchor="mm")
            _tracked(d, (W//2, 210), s.get("kicker","THE ESTATE OF HER").upper(), _font("ui",20), CREAM, tracking=8, anchor="mm")
            if s.get("title"):
                for j, ln in enumerate(_wrap(d, s["title"], _font("display_it",44), W-160)):
                    d.text((W//2, H-220+j*54), ln, font=_font("display_it",44), fill=CREAM, anchor="mm")
        elif kind == "image":
            im = _cover(hero, W, H, s.get("fx",0.5), s.get("fy",0.5)); d = ImageDraw.Draw(im)
            if s.get("cap"):
                im = _scrim(im, bottom=True, strength=180); d = ImageDraw.Draw(im)
                d.text((60, H-120), s["cap"], font=_font("display_it",40), fill=PAPER)
        else:
            im = Image.new("RGB",(W,H), INK if s.get("bg")=="ink" else PAPER); d = ImageDraw.Draw(im)
            fg = PAPER if s.get("bg")=="ink" else INK
            d.line([(60,150),(140,150)], fill=RED, width=3)
            if s.get("kicker"): _tracked(d,(60,180), s["kicker"].upper(), _font("ui",18), RED, tracking=4)
            tf=_font("display",64); y=260
            for ln in _wrap(d, s.get("title",""), tf, W-120): d.text((60,y), ln, font=tf, fill=fg); y+=int(tf.size*1.05)
            y+=20; bf=_font("body",34)
            for ln in _wrap(d, s.get("body",""), bf, W-120): d.text((60,y), ln, font=bf, fill=fg); y+=46
        out = os.path.join(outdir, f"slide_{i+1:02d}.png"); im.save(out); outs.append(out)
        if log: _asset().log_edit(log, "layout:carousel", src, out, f"slide {i+1} {kind}", "")
    return outs

def thumbnail(src, out, title_lines, kicker, log=None):
    from PIL import Image, ImageDraw
    import numpy as np
    W, H = 1280, 720
    im = _cover(Image.open(src).convert("RGB"), W, H, 0.55, 0.40); d = ImageDraw.Draw(im)
    a = (np.clip((np.linspace(0, 1, W)-0.42)/0.58, 0, 1)[None, :]*np.ones((H, 1))*205).astype('uint8')
    im = Image.composite(Image.new("RGB", (W, H), (8, 7, 6)), im, Image.fromarray(a, "L")); d = ImageDraw.Draw(im)
    x = 770; y = 250; tf = _font("display", 92)
    if kicker: _tracked(d, (x+4, y-46), kicker.upper(), _font("ui", 22), RED, tracking=6)
    d.line([(x, y), (x, y+len(title_lines)*int(tf.size*1.02))], fill=RED, width=5)
    for ln in title_lines:
        d.text((x+22, y), ln, font=tf, fill=PAPER); y += int(tf.size*1.02)
    im.save(out)
    if log: _asset().log_edit(log, "layout:thumbnail", src, out, f"{W}x{H}", " / ".join(title_lines))
    return out

def dashboard(out, title, sub, rows, log=None):
    """rows = [(label, status, note)] ; status in ACTIVE/AMBER/RED/PASS/FAIL/WARN."""
    from PIL import Image, ImageDraw
    W = 1400; rowh = 58; top = 200; half = (len(rows)+1)//2; Hh = top + half*rowh + 80
    im = Image.new("RGB", (W, Hh), (22, 20, 18)); d = ImageDraw.Draw(im)
    d.text((40, 40), title, font=_font("display", 62), fill=PAPER)
    _tracked(d, (44, 128), sub.upper(), _font("ui", 20), RED, tracking=5)
    col = {"ACTIVE": (98,197,84), "PASS": (98,197,84), "GREEN": (98,197,84),
           "AMBER": (245,191,79), "WARN": (245,191,79), "FIX": (245,191,79),
           "RED": (237,106,94), "FAIL": (237,106,94), "REJECT": (237,106,94)}
    for i, (label, st, note) in enumerate(rows):
        cx = 40 if i < half else 720; y = top + (i % half)*rowh
        c = col.get(str(st).upper(), (150,146,140))
        d.ellipse([cx, y+12, cx+18, y+30], fill=c)
        d.text((cx+34, y), label, font=_font("body", 28), fill=(232,227,217))
        if note: d.text((cx+34, y+30), note[:46], font=_font("ui", 14), fill=(120,116,110))
        d.text((cx+632, y+4), str(st), font=_font("ui_bold", 17), fill=c, anchor="ra")
    g = sum(1 for _, s, _ in rows if str(s).upper() in ("ACTIVE","PASS","GREEN"))
    a = sum(1 for _, s, _ in rows if str(s).upper() in ("AMBER","WARN","FIX"))
    r = sum(1 for _, s, _ in rows if str(s).upper() in ("RED","FAIL","REJECT"))
    d.text((40, Hh-52), f"{g} ACTIVE   .   {a} AMBER   .   {r} RED      (of {len(rows)})",
           font=_font("ui_bold", 24), fill=PAPER)
    im.save(out)
    if log: _asset().log_edit(log, "layout:dashboard", out, out, f"{len(rows)} rows", title)
    return out

def board(out, title, manifest_path, log=None):
    from PIL import Image, ImageDraw
    man = json.load(open(manifest_path)); cells = man["cells"]
    cols = man.get("cols", 3); cw, ch = 520, 360; pad = 24; head = 150
    rows = (len(cells)+cols-1)//cols
    W = cols*cw + (cols+1)*pad; Hh = head + rows*(ch+70) + pad
    im = Image.new("RGB", (W, Hh), (24,22,20)); d = ImageDraw.Draw(im)
    d.text((pad, 36), title, font=_font("display", 72), fill=PAPER)
    _tracked(d, (pad, 116), man.get("sub","INTERNAL CONTROL ROOM , NOT FOR RELEASE").upper(), _font("ui",18), RED, tracking=6)
    for i, c in enumerate(cells):
        x = pad + (i%cols)*(cw+pad); y = head + (i//cols)*(ch+70)
        d.rectangle([x-2,y-2,x+cw+2,y+ch+2], outline=(70,66,60), width=2)
        if c.get("img") and os.path.exists(c["img"]):
            th = _cover(Image.open(c["img"]).convert("RGB"), cw, ch, c.get("fx",0.5), c.get("fy",0.5)); im.paste(th,(x,y))
        else:
            d.rectangle([x,y,x+cw,y+ch], fill=(40,38,35))
            d.text((x+cw//2,y+ch//2), c.get("placeholder","?"), font=_font("ui",30), fill=(120,116,110), anchor="mm")
        _tracked(d, (x, y+ch+10), c.get("label","").upper(), _font("ui_bold",18), PAPER, tracking=2)
        st = c.get("status","")
        col = {"ACTIVE":(98,197,84),"AMBER":(245,191,79),"RED":(237,106,94)}.get(st,(150,146,140))
        d.text((x, y+ch+38), st, font=_font("ui",16), fill=col)
    im.save(out)
    if log: _asset().log_edit(log, "layout:board", out, out, f"{len(cells)} cells", title)
    return out

def main():
    ap = argparse.ArgumentParser(prog="os_adobe_layout.py"); sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("titlecard"); p.add_argument("--out",required=True); p.add_argument("--w",type=int,default=1080); p.add_argument("--h",type=int,default=1350)
    p.add_argument("--kicker",default=""); p.add_argument("--title",required=True); p.add_argument("--subtitle",default=""); p.add_argument("--bg",default="ink"); p.add_argument("--log",default="")
    p = sub.add_parser("poster"); p.add_argument("--src",required=True); p.add_argument("--out",required=True); p.add_argument("--masthead",required=True)
    p.add_argument("--lot",default="LOT 00"); p.add_argument("--logline",default=""); p.add_argument("--footer",default=""); p.add_argument("--log",default="")
    p = sub.add_parser("onesheet"); p.add_argument("--src",required=True); p.add_argument("--out",required=True); p.add_argument("--title",required=True); p.add_argument("--logline",default=""); p.add_argument("--details",default=""); p.add_argument("--log",default="")
    p = sub.add_parser("landing"); p.add_argument("--src",required=True); p.add_argument("--out",required=True); p.add_argument("--headline",required=True); p.add_argument("--sub",default=""); p.add_argument("--cta",default="Request access"); p.add_argument("--log",default="")
    p = sub.add_parser("lookbook"); p.add_argument("--src",required=True); p.add_argument("--out",required=True); p.add_argument("--caption",default=""); p.add_argument("--log",default="")
    p = sub.add_parser("carousel"); p.add_argument("--src",required=True); p.add_argument("--outdir",required=True); p.add_argument("--slides",required=True); p.add_argument("--log",default="")
    p = sub.add_parser("board"); p.add_argument("--out",required=True); p.add_argument("--title",default="OS CONTROL ROOM"); p.add_argument("--manifest",required=True); p.add_argument("--log",default="")
    a = ap.parse_args()
    if a.cmd=="titlecard": print(titlecard(a.out,a.w,a.h,a.kicker,a.title,a.subtitle,a.bg,a.log or None))
    elif a.cmd=="poster": print(poster(a.src,a.out,a.masthead,a.lot,a.logline,a.footer,a.log or None))
    elif a.cmd=="onesheet": print(onesheet(a.src,a.out,a.title,a.logline,a.details,a.log or None))
    elif a.cmd=="landing": print(landing(a.src,a.out,a.headline,a.sub,a.cta,a.log or None))
    elif a.cmd=="lookbook": print(lookbook(a.src,a.out,a.caption,a.log or None))
    elif a.cmd=="carousel": print("\n".join(carousel(a.src,a.outdir,a.slides,a.log or None)))
    elif a.cmd=="board": print(board(a.out,a.title,a.manifest,a.log or None))
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
