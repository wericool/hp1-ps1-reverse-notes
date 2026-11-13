# r607: union of unique PSY-Q OBJ matches over ALL versions (newest wins per address), EURO1.GAM mapping base 0x80010000 / header 0x800.
import json,os,re,sys
root,exe,out=sys.argv[1],sys.argv[2],sys.argv[3]
text=open(exe,'rb').read()[0x800:]
def rx(sig):return re.compile(b''.join(b'.' if t=='??' else re.escape(bytes([int(t,16)])) for t in sig.split()),re.DOTALL)
cover={};names={}
for v in sorted((d for d in os.listdir(root) if d.isdigit()),key=lambda d:int(d.ljust(4,'0'))):
    for f in sorted(os.listdir(os.path.join(root,v))):
        if not f.endswith('.json'):continue
        for obj in json.load(open(os.path.join(root,v,f))):
            if 'sig' not in obj:continue
            sig=obj['sig'].split()
            if len(sig)<24:continue
            m=[x.start() for x in rx(obj['sig']).finditer(text)]
            if len(m)!=1:continue
            at=m[0];cover[at]=(len(sig),v,f[:-5],obj['name'])
            for lab in obj['labels']:
                if re.match(r'(loc|text|data|bss|rdata|sdata|sbss|jpt)_',lab['name']):continue
                names[0x10000+at+lab['offset']]=(lab['name'],f[:-5],obj['name'],v)
bytes_=sum(c[0] for c in cover.values())
print('objs',len(cover),'bytes',bytes_,'functions',len(names))
with open(out,'w') as o:
    for a in sorted(names):n,l,ob,v=names[a];o.write(f"{a:05x} {l} {ob} {n} v{v}\n")
