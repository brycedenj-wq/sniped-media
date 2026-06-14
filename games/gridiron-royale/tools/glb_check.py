import json, struct, sys, base64

def load(path):
    with open(path,'rb') as f: data=f.read()
    magic, ver, length = struct.unpack('<III', data[:12])
    assert magic == 0x46546C67, 'not glb'
    off=12
    js=None; binbuf=None
    while off < length:
        clen, ctype = struct.unpack('<II', data[off:off+8]); off+=8
        chunk = data[off:off+clen]; off+=clen
        if ctype == 0x4E4F534A: js=json.loads(chunk.decode('utf-8'))
        elif ctype == 0x004E4942: binbuf=chunk
    return js, binbuf

def accessor_minmax(js, binbuf, idx):
    acc=js['accessors'][idx]
    bv=js['bufferViews'][acc['bufferView']]
    comp={5126:('f',4)}[acc['componentType']]
    n={'SCALAR':1,'VEC3':3,'VEC4':4}[acc['type']]
    off=bv.get('byteOffset',0)+acc.get('byteOffset',0)
    vals=[]
    for i in range(acc['count']):
        v=struct.unpack_from('<'+comp[0]*n, binbuf, off+i*comp[1]*n)
        vals.append(v)
    return vals

for path in sys.argv[1:]:
    js, binbuf = load(path)
    print('==', path)
    print('  meshes:', len(js.get('meshes',[])), ' skins:', len(js.get('skins',[])), ' images:', len(js.get('images',[])))
    print('  materials alphaMode:', [m.get('alphaMode','OPAQUE') for m in js.get('materials',[])])
    anims=js.get('animations',[])
    print('  animations:', [a.get('name','?') for a in anims])
    nodes=js.get('nodes',[])
    for a in anims:
        for ch in a['channels']:
            if ch['target'].get('path')=='scale':
                node=nodes[ch['target']['node']].get('name','?')
                if any(k in node.lower() for k in ('hip','root','pelvis','armature')):
                    sampler=a['samplers'][ch['sampler']]
                    vals=accessor_minmax(js,binbuf,sampler['output'])
                    flat=[x for v in vals for x in v]
                    print(f"  ROOT-SCALE channel on '{node}': min={min(flat):.4f} max={max(flat):.4f}")
