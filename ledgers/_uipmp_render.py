# Offline render of an archived listing page to PNG: scripts/iframes/video stripped (no YouTube fetch),
# main listing region kept; headless Edge with a throwaway profile. Usage: python _uipmp_render.py n out.png
import gzip, os, re, subprocess, sys, tempfile
n, out = int(sys.argv[1]), os.path.abspath(sys.argv[2])
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uipath-marketplace.raw')
s = gzip.open(os.path.join(RAW, 'html', f'{n:04d}.html.gz'), 'rt', encoding='utf-8').read()
s = re.sub(r'(?is)<(script|iframe|video|audio|noscript)\b.*?</\1>', '', s)
s = re.sub(r'(?is)<(iframe|video|audio|link)\b[^>]*>', '', s)
s = re.sub(r'(?is)<style\b.*?</style>', '', s)
a = s.find('<h1 class="mp-listing-name"'); b = s.find('Similar Listings', a)
body = s[a:b] if a > 0 and b > 0 else s
page = ('<html><head><meta charset="utf-8"><style>body{font:15px Arial;max-width:1500px;margin:20px}'
        'img{max-width:1400px;display:block;margin:8px 0}</style></head><body>'
        f'<p style="color:#888">Offline render of archived listing (n={n}); scripts and video iframes removed.</p>' + body + '</body></html>')
tmp = tempfile.mkdtemp()
f = os.path.join(tmp, 'p.html'); open(f, 'w', encoding='utf-8').write(page)
edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
import pathlib
subprocess.run([edge, '--headless=new', '--disable-gpu', '--user-data-dir=' + os.path.join(tmp, 'prof'), '--hide-scrollbars',
                '--window-size=1500,2400', '--screenshot=' + out, pathlib.Path(f).as_uri()],
               capture_output=True, timeout=90)
print(out, os.path.exists(out))
