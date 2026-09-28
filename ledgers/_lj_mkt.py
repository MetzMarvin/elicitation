import re,os,subprocess,time,json,html
d=open('ledgers/_lj_marketing_sitemap0.xml',encoding='utf-8',errors='replace').read()
locs=re.findall(r'<loc>(.*?)</loc>',d)
out=[]
for i,u in enumerate(locs,1):
    fn='ledgers/loyjoy.marketing/%03d.html'%i
    if not (os.path.exists(fn) and os.path.getsize(fn)>500):
        r=subprocess.run(['curl','-sL','-o',fn,'-w','%{http_code}','--max-time','25','-A','Mozilla/5.0',u],capture_output=True,text=True)
        code=r.stdout.strip()
        time.sleep(0.15)
    else:
        code='cached'
    try:
        h=open(fn,encoding='utf-8',errors='replace').read()
    except Exception:
        h=''
    txt=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S|re.I)
    txt=html.unescape(re.sub(r'<[^>]+>',' ',txt))
    txt=re.sub(r'\s+',' ',txt)
    imgs=[m for m in re.findall(r'<img[^>]+src="([^"]+)"',h)]
    out.append({'url':u,'file':fn,'code':code,'len':len(txt),'bpmn':'BPMN' in txt or 'bpmn' in u,
                'ai':bool(re.search(r'\bAI\b|artificial intelligence|agentic|\bLLM\b|GPT',txt)),'imgs':len(imgs),'txt':txt[:400]})
json.dump(out,open('ledgers/_lj_mkt.json','w',encoding='utf-8'),ensure_ascii=False)
print('fetched',len(out))
