import io,re,os,html,json
urls=[l.strip() for l in io.open('ledgers/loyjoy.frontier.txt',encoding='utf-8') if l.strip()]
STRICT=re.compile(r'\bA\.I\.|\bAI\b|\bKI\b|GPT|LLM|artificial intelligence|machine learning|generative|intelligen|copilot|\bNLU\b|Smart Search',re.I)
def page_text(i):
    fn='ledgers/loyjoy.raw/html/%03d.html'%i
    if not os.path.exists(fn): return '',''
    d=io.open(fn,encoding='utf-8',errors='replace').read()
    d=re.sub(r'<(script|style)[^>]*>.*?</\1>','',d,flags=re.S)
    m=re.search(r'<article[^>]*>(.*?)</article>',d,re.S) or re.search(r'<main[^>]*>(.*?)</main>',d,re.S)
    body=m.group(1) if m else d
    body=re.sub(r'</(p|div|li|h1|h2|h3|h4|td|tr|section|article)>',' ',body,flags=re.I)
    t=html.unescape(re.sub(r'<[^>]+>','',body))
    t=re.sub(r'[ \t]+',' ',t).replace('​','').replace('’',"'").replace('\xa0',' ')
    t=re.sub(r'\s*\n\s*',' ',t).strip()
    h=re.search(r'<h1[^>]*>(.*?)</h1>',d,re.S)
    h1=html.unescape(re.sub(r'<[^>]+>','',h.group(1))).strip() if h else ''
    return h1,t
def ev_quote(t):
    sents=re.split(r'(?<=[.!?])\s+',t)
    for pat,lo,hi in [(r'BPMN|process module|chat flow|start event|module|gateway|canvas',6,40),(r'',6,40)]:
        for s in sents:
            s=' '.join(s.split())
            n=len(s.split())
            if lo<=n<=hi and (not pat or re.search(pat,s,re.I)):
                return ' '.join(s.split()[:25])
    return ' '.join(t.split()[:25])
out=[]
for i,u in enumerate(urls,1):
    h1,t=page_text(i)
    out.append({'n':i,'url':u,'h1':h1,'ev':ev_quote(t),'strict':len(STRICT.findall(t)),'len':len(t)})
io.open('ledgers/_lj_ev.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=1))
print('pages:',len(out),'empty:',sum(1 for o in out if o['len']==0))
print('strict-AI pages:',sum(1 for o in out if o['strict']))
print([(o['n'],o['strict']) for o in out if o['strict']])
