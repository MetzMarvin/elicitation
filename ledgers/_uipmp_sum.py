import json,re,sys
want=set(map(int,sys.argv[1:]))
for l in open('uipath-marketplace.raw/scan.jsonl',encoding='utf-8'):
    r=json.loads(l)
    if r['n'] in want and r['http']==200:
        m=re.search(r'\n\s*Summary\s*\n\s*(.+)',r['text'])
        print(r['n'],'|',r['type'],'|',r['title'],'| S:',(m.group(1).strip() if m else '')[:220],'| AI:',' || '.join(v.replace('\n',' ')[20:130] for v in list(r['ai'].values())[:2]))
