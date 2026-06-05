#!/usr/bin/env python3
"""
os_adobe_cloud.py , the Adobe upload handshake, scripted + repeatable (promotes Adobe-MAX to ACTIVE).

Adobe MCP image tools only accept assets in Adobe storage (external URLs are rejected). This makes the
handshake a logged, repeatable workflow. The MCP init/finalize calls are agent-invoked; the byte-prep
and the presigned PUT are scripted here.

Flow (proven on the DEED hero):
  1. os_adobe_cloud.py prep <src> <out.jpg>           , downscale to <=1400px JPEG, print size + media_type
  2. [agent] asset_initialize_file_upload(path, file_size, media_type)  -> transfer_document (presigned PUT URL)
  3. os_adobe_cloud.py put <presigned_url> <out.jpg>   , curl PUT the bytes (follows 308)
  4. [agent] asset_finalize_file_upload(filename, transfer_document)     -> presignedAssetUrl
  5. [agent] image_crop_and_resize / image_remove_background / image_generative_expand / document_render
  6. os_adobe_cloud.py fetch <output_short_url> <out>  , download the Adobe-produced artifact

  os_adobe_cloud.py prep <src> <out.jpg> [--max 1400]
  os_adobe_cloud.py put <presigned_url> <file>
  os_adobe_cloud.py fetch <url> <out>
"""
import os, sys, argparse, subprocess

def prep(src, out, mx):
    from PIL import Image
    im = Image.open(src).convert("RGB"); im.thumbnail((mx, mx)); im.save(out, "JPEG", quality=90)
    sz = os.path.getsize(out)
    print(f"file: {out}\nfile_size: {sz}\nmedia_type: image/jpeg\ndims: {im.size}")
    print(f"NEXT (agent): asset_initialize_file_upload(path='{os.path.basename(out)}', file_size={sz}, media_type='image/jpeg')")
    return sz

def put(url, f):
    r = subprocess.run(["curl", "-s", "-L", "-X", "PUT", "-H", "Content-Type: image/jpeg",
                        "--data-binary", f"@{f}", url, "-w", "%{http_code}"], capture_output=True, text=True)
    print(f"PUT http {r.stdout.strip()[-3:]}")
    print("NEXT (agent): asset_finalize_file_upload(filename, transfer_document with _links.finalize)")
    return r.stdout.strip()[-3:]

def fetch(url, out):
    r = subprocess.run(["curl", "-s", "-L", url, "-o", out, "-w", "%{http_code}"], capture_output=True, text=True)
    print(f"fetch http {r.stdout.strip()} -> {out} ({os.path.getsize(out) if os.path.exists(out) else 0} bytes)")

def main():
    ap = argparse.ArgumentParser(prog="os_adobe_cloud.py"); sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("prep"); p.add_argument("src"); p.add_argument("out"); p.add_argument("--max", type=int, default=1400)
    pu = sub.add_parser("put"); pu.add_argument("url"); pu.add_argument("file")
    fe = sub.add_parser("fetch"); fe.add_argument("url"); fe.add_argument("out")
    a = ap.parse_args()
    if a.cmd == "prep": prep(a.src, a.out, a.max)
    elif a.cmd == "put": put(a.url, a.file)
    elif a.cmd == "fetch": fetch(a.url, a.out)
    else: ap.print_help()
    return 0

if __name__ == "__main__": sys.exit(main())
