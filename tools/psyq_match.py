# r607: match PSY-Q library OBJ signatures (lab313ru/psx_psyq_signatures JSON) against the PS1 EXE.
# usage: python -I psyq_match.py <sigroot> <exe> <out_prefix>
import json,os,re,sys
root,exe,out=sys.argv[1],sys.argv[2],sys.argv[3]
data=open(exe,'rb').read();text=data[0x800:];base=0x80010000  # PS-X EXE: header 0x800, t_addr 0x80010000
def rx(sig):
    parts=[b'.' if t=='??' else re.escape(bytes([int(t,16)])) for t in sig.split()]
    return re.compile(b''.join(parts),re.DOTALL)
versions=sorted(d for d in os.listdir(root) if d.isdigit())
score={}
best=None
for v in versions:
    hits=[];n=0
    for f in sorted(os.listdir(os.path.join(root,v))):
        if not f.endswith('.json'):continue
        for obj in json.load(open(os.path.join(root,v,f))):
            if 'sig' not in obj or len(obj['sig'].split())<16:continue
            n+=1;m=[x.start() for x in rx(obj['sig']).finditer(text)]
            if len(m)==1:hits.append((f[:-5],obj,m[0]))
    nbytes=sum(len(o['sig'].split()) for _,o,_ in hits)
    score[v]=(len(hits),nbytes);print(v,'objs matched',len(hits),'of',n,'bytes',nbytes,flush=True)
    if best is None or nbytes>score[best][1]:best=v;besthits=hits
print('BEST',best)
with open(out+'-functions.txt','w') as o:
    for lib,obj,at in sorted(besthits,key=lambda h:h[2]):
        for lab in obj['labels']:
            nm=lab['name']
            if re.match(r'(loc|text|data|bss|rdata|sdata|sbss)_',nm):continue
            o.write(f"{base+at+lab['offset']-0x80000000:05x} {lib} {obj['name']} {nm}\n")
    print('wrote',out+'-functions.txt')
