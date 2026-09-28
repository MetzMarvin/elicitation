import json,io,os,collections
def rj(p):
    x=json.loads(io.open(p,encoding='utf-8').read())
    if isinstance(x,str): x=json.loads(x)
    return x
pages=json.load(io.open('ledgers/_lj_pages.json',encoding='utf-8'))
hits={}
for i in range(1,6):
    p='ledgers/_lj_b%d.json'%i
    if not os.path.exists(p): continue
    for r in rj(p):
        hits[r['u']]={'nh':r.get('nh',0),'hits':r.get('hits',[])}
cls={}
for i in ['1','2','3','4','5a','5b','6']:
    p='ledgers/loyjoy.raw/_cls_%s.txt'%i
    if not os.path.exists(p): continue
    for line in io.open(p,encoding='utf-8',errors='replace'):
        if line.count('|')<3: continue
        parts=[x.strip() for x in line.split('|')]
        if '__' not in parts[0]: continue
        cls[parts[0]]={'class':parts[1],'desc':parts[2],'ai':parts[3]}
out=[]
for p,v in pages.items():
    sl=p.strip('/').replace('/','_'); pref=sl+'__'
    imgs=v.get('imgs',[])
    mine=[]; unm=[]
    for d in imgs:
        key=pref+d['n']
        if key in cls:
            c=cls[key]; mine.append({'n':d['n'],'w':d['st']['w'],'h':d['st']['h'],'class':c['class'],'desc':c['desc'],'ai':c['ai']})
        else: unm.append(d['n'])
    classes=collections.Counter(m['class'] for m in mine)
    ai=[{'img':m['n'],'label':m['ai'],'desc':m['desc']} for m in mine if m['ai'].lower()!='none']
    h=hits.get(p,{})
    out.append({'p':p,'n_img':len(imgs),'unmatched':unm,'classes':dict(classes),'imgs':mine,'ai':ai,'nh':h.get('nh',0),'hits':h.get('hits',[]),'len':v.get('len',0)})
io.open('ledgers/_lj_table.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=1))
print('pages',len(out),'classified-imgs',len(cls))
print('unmatched keys:',sorted({b for o in out for b in o['unmatched']}))
print('pages with canvas:',sum(1 for o in out if o['classes'].get('bpmn-canvas') or o['classes'].get('editor-canvas+panel')))
print('pages with ai-label imgs:',sum(1 for o in out if o['ai']))
