import io,json,os,subprocess,re,time
rows=json.load(io.open('ledgers/_lj_rest_imgs.json',encoding='utf-8'))
man=[]
for i,u,n,imgs in rows:
    for k,src in enumerate(imgs):
        base=src.split('/')[-1].split('?')[0]
        fn='ledgers/loyjoy.raw/rest_imgs/%03d_%02d__%s'%(i,k,base)
        if not (os.path.exists(fn) and os.path.getsize(fn)>800):
            subprocess.run(['curl','-sL','-o',fn,'--max-time','25','-A','Mozilla/5.0',src],capture_output=True)
        man.append({'page':i,'url':u,'src':src,'file':fn,'ok':os.path.exists(fn) and os.path.getsize(fn)>800})
        time.sleep(0.2)
io.open('ledgers/_lj_rest_imgman.json','w',encoding='utf-8').write(json.dumps(man,ensure_ascii=False,indent=1))
print('done',sum(1 for m in man if m['ok']),'/',len(man))
