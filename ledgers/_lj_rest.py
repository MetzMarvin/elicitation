import subprocess,os,io,time
urls=[l.strip() for l in io.open('ledgers/_lj_rest_urls.txt',encoding='utf-8') if l.strip()]
for i,u in enumerate(urls,1):
    fn='ledgers/loyjoy.raw/html_rest/%03d.html'%i
    if os.path.exists(fn) and os.path.getsize(fn)>1500: continue
    r=subprocess.run(['curl','-sL','-o',fn,'-w','%{http_code}','--max-time','25','-A','Mozilla/5.0',u],capture_output=True,text=True)
    print(i,u,r.stdout.strip(),os.path.getsize(fn) if os.path.exists(fn) else 0,flush=True)
    time.sleep(0.5)
print('DONE')
