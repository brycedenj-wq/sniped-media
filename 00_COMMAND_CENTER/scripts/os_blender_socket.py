#!/usr/bin/env python3
"""
os_blender_socket.py , GATED client for the Blender add-on socket (localhost:9876).

The Blender MCP *server* is not registered in this Claude Code session, but the add-on socket is
reachable. This drives it directly , and EVERY code payload is gated by os_blender_gate first
(sandbox-only render path, no destructive/network/eval code) before it is sent. Non-destructive: it
builds a NEW scene, never resets the open file.

  os_blender_socket.py ping
  os_blender_socket.py proof              , the smallest safe proof (new scene + cube + camera + light + render)
"""
import os, sys, json, socket, importlib.util, argparse

HERE = os.path.dirname(os.path.abspath(__file__)); CC = os.path.dirname(HERE)
SANDBOX = os.path.join(CC, "OS_PRIME_MOVER_ACTIVATION_001", "05_SECURITY_AND_MCP", "blender_sandbox")
HOST, PORT = "localhost", 9876

def _gate():
    s = importlib.util.spec_from_file_location("os_blender_gate", os.path.join(HERE, "os_blender_gate.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def send_code(code, strict_json=False, timeout=300.0):
    request = json.dumps({"type": "execute", "code": code, "strict_json": strict_json}) + "\0"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout); sock.connect((HOST, PORT)); sock.sendall(request.encode("utf-8"))
        buf = bytearray()
        while True:
            chunk = sock.recv(65536)
            if not chunk: break
            buf.extend(chunk)
            if b"\0" in buf: break
    line, _, _ = buf.partition(b"\0")
    return json.loads(line.decode("utf-8"))

def gated_send(code, render_path, is_test=True):
    g = _gate()
    verdict, reasons = g.check_action("python", render_path, code, is_test)
    print(f"  os_blender_gate: {verdict} ({'; '.join(reasons)})")
    if verdict == "DENY":
        raise SystemExit("  BLOCKED by os_blender_gate , not sent.")
    if verdict == "CONFIRM" and not is_test:
        raise SystemExit("  needs per-action confirmation (not a test). Stopping.")
    return send_code(code)

PROOF_CODE = r'''
import bpy, bmesh, os
sc = bpy.data.scenes.new("OS_DEED_PROOF")
coll = sc.collection
me = bpy.data.meshes.new("proof_cube")
bm = bmesh.new(); bmesh.ops.create_cube(bm, size=2.0); bm.to_mesh(me); bm.free()
cube = bpy.data.objects.new("proof_cube", me); cube.location = (0,0,1); coll.objects.link(cube)
cam_d = bpy.data.cameras.new("proof_cam"); cam = bpy.data.objects.new("proof_cam", cam_d)
cam.location = (7,-7,5); cam.rotation_euler = (1.1,0,0.785); coll.objects.link(cam); sc.camera = cam
lt_d = bpy.data.lights.new("proof_light", type='AREA'); lt_d.energy = 1200
lt = bpy.data.objects.new("proof_light", lt_d); lt.location = (4,-4,8); coll.objects.link(lt)
sc.render.resolution_x = 800; sc.render.resolution_y = 800
try: sc.render.engine = 'BLENDER_EEVEE_NEXT'
except Exception: pass
sc.render.filepath = os.path.expanduser("__OUT__")
try:
    with bpy.context.temp_override(scene=sc):
        bpy.ops.render.render(write_still=True)
except Exception as e:
    sc.render.filepath = os.path.expanduser("__OUT__")
    bpy.context.window.scene = sc
    bpy.ops.render.render(write_still=True)
result = {"scene": sc.name, "objects": [o.name for o in sc.objects], "render": sc.render.filepath}
'''

def main():
    ap = argparse.ArgumentParser(prog="os_blender_socket.py"); sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("ping"); sub.add_parser("proof")
    a = ap.parse_args()
    if a.cmd == "ping":
        r = gated_send("result = {'blender': bpy.app.version_string}", os.path.join(SANDBOX, "renders", "x.png"))
        print(json.dumps(r, indent=2)); return 0
    if a.cmd == "proof":
        os.makedirs(os.path.join(SANDBOX, "renders"), exist_ok=True)
        out = os.path.join(SANDBOX, "renders", "blender_proof.png")
        code = PROOF_CODE.replace("__OUT__", out)
        r = gated_send(code, out, is_test=True)
        print("  response:", json.dumps(r)[:300])
        ok = os.path.exists(out) and os.path.getsize(out) > 0
        print(f"  proof artifact exists: {ok} ({out})")
        return 0 if ok else 1
    ap.print_help(); return 0

if __name__ == "__main__": sys.exit(main())
