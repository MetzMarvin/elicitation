import subprocess,os,io,json,time
urls=[l.strip() for l in io.open('ledgers/loyjoy.frontier.txt',encoding='utf-8') if l.strip()]
base='https://docs.loyjoy.com'
for i,u in enumerate(urls,1):
    fn='ledgers/loyjoy.raw/html/%03d.html'%i
    if os.path.exists(fn) and os.path.getsize(fn)>2000: continue
    full=u if u.startswith('http') else base+u
    r=subprocess.run(['curl','-sL','-o',fn,'-w','%{http_code}','--max-time','25','-A','Mozilla/5.0',full],capture_output=True,text=True)
    print(i,r.stdout.strip(),os.path.getsize(fn) if os.path.exists(fn) else 0,flush=True)
    time.sleep(0.7)
print('DONE')
