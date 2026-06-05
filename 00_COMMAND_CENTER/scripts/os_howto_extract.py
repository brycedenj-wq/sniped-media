#!/usr/bin/env python3
"""
os_howto_extract.py , turn how-to docs into APPLIED capability, not summaries.

The operating truth (operator): every doc is how-to game. Names mislead, so classify by CONTENT, read
every page, and extract techniques the OS can APPLY to self-solve problems. This engine:
  - extracts text from .docx/.txt (pdf -> note)
  - classifies each doc by TOOL/technique keyword density (regardless of filename)
  - emits a content map so we know what each doc ACTUALLY contains
  - extracts full text for reading/segmenting + a technique-candidate pass

  os_howto_extract.py scan <folder>            , content map of every doc (tool density, words)
  os_howto_extract.py extract <file> <out.txt> , full text extraction
  os_howto_extract.py techniques <txt>          , pull candidate how-to lines (imperatives + tool verbs)
"""
import os, sys, zipfile, re, html, glob, argparse

TOOLS = ["photoshop","lightroom","camera raw","premiere","after effects","illustrator","indesign",
         "firefly","express","adobe","blender","midjourney","runway","figma","capcut","davinci",
         "nano banana","seedance","higgsfield","kling","sora","veo","topaz","comfyui","stable diffusion"]
TECH = ["mask","composite","generative fill","generative expand","remove background","retouch","grade",
        "color grade","dodge","burn","frequency separation","luminosity","curves","layer","blend mode",
        "depth of field","3 point","three point","key light","rim light","volumetric","geometry node",
        "bevel","subdivision","remesh","uv","emission","bloom","lut","keyframe","easing","transition",
        "kinetic type","track matte","rotoscope","upscale","prompt","reference image","control net"]

def extract_docx(path):
    try:
        z=zipfile.ZipFile(path); xml=z.read("word/document.xml").decode("utf-8","ignore")
    except Exception as e:
        return ""
    xml=re.sub(r"</w:p>","\n",xml); xml=re.sub(r"<w:tab[^>]*/>","\t",xml)
    txt=html.unescape(re.sub(r"<[^>]+>","",xml))
    return re.sub(r"\n{3,}","\n\n","\n".join(l.rstrip() for l in txt.splitlines())).strip()

def extract_any(path):
    p=path.lower()
    if p.endswith(".docx"): return extract_docx(path)
    if p.endswith(".txt") or p.endswith(".md"):
        return open(path,errors="ignore").read()
    return ""

def density(txt):
    low=txt.lower(); n=max(1,len(low.split()))
    tools={t:low.count(t) for t in TOOLS if low.count(t)>0}
    tech={t:low.count(t) for t in TECH if low.count(t)>0}
    return tools, tech, len(low.split())

def cmd_scan(folder):
    files=[]
    for ext in ("*.docx","*.txt","*.md","*.pdf"):
        files+=glob.glob(os.path.join(folder,"**",ext),recursive=True)
        files+=glob.glob(os.path.join(folder,ext))
    files=sorted(set(files))
    print(f"scanning {len(files)} docs in {folder}\n")
    rows=[]
    for f in files:
        if f.lower().endswith(".pdf"):
            print(f"  [PDF , needs OCR/extract] {os.path.basename(f)}"); continue
        txt=extract_any(f)
        if not txt: print(f"  [empty/unreadable] {os.path.basename(f)}"); continue
        tools,tech,w=density(txt)
        top_tools=sorted(tools.items(),key=lambda x:-x[1])[:6]
        top_tech=sorted(tech.items(),key=lambda x:-x[1])[:6]
        rows.append((os.path.basename(f),w,top_tools,top_tech))
    rows.sort(key=lambda r:-r[1])
    for name,w,tt,tc in rows:
        print(f"\n== {name}  ({w} words)")
        print(f"   TOOLS: {', '.join(f'{k}:{v}' for k,v in tt) or '-'}")
        print(f"   TECH : {', '.join(f'{k}:{v}' for k,v in tc) or '-'}")
    return 0

def cmd_extract(path,out):
    txt=extract_any(path)
    open(out,"w").write(txt); print(f"wrote {out} ({len(txt.split())} words, {txt.count(chr(10))+1} lines)")
    return 0

def cmd_techniques(txt_path):
    lines=open(txt_path,errors="ignore").read().splitlines()
    verbs=("open ","select ","use ","click ","add ","set ","apply ","create ","drag ","mask ","paint ","increase ","lower ","drop ","duplicate ","render ","export ","import ","enable ","turn ")
    out=[]
    for l in lines:
        s=l.strip().lower()
        if any(s.startswith(v) for v in verbs) and any(t in s for t in TECH+TOOLS):
            out.append(l.strip())
    for l in out[:120]: print(" -",l)
    print(f"\n{len(out)} candidate technique lines")
    return 0

def main():
    ap=argparse.ArgumentParser(prog="os_howto_extract.py"); sub=ap.add_subparsers(dest="cmd")
    s=sub.add_parser("scan"); s.add_argument("folder")
    e=sub.add_parser("extract"); e.add_argument("path"); e.add_argument("out")
    t=sub.add_parser("techniques"); t.add_argument("txt")
    a=ap.parse_args()
    if a.cmd=="scan": return cmd_scan(a.folder)
    if a.cmd=="extract": return cmd_extract(a.path,a.out)
    if a.cmd=="techniques": return cmd_techniques(a.txt)
    ap.print_help(); return 1

if __name__=="__main__": sys.exit(main())
