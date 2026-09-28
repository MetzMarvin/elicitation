"""camunda-docs-blog: fetch the blog population from the sitemap, one URL per second.

Writes:
  ledgers/camunda-docs-blog.frontier.txt   n<TAB>url, frozen before judging
  ledgers/camunda-docs-blog.raw/blog/NNNN.html   the page as served
  ledgers/camunda-docs-blog.raw/fetch.log  one line per URL: n, http status, bytes

Resumable: an already-saved non-empty NNNN.html is not re-fetched.
"""
import os, re, subprocess, sys, time

RAW = "ledgers/camunda-docs-blog.raw"
BLOG = os.path.join(RAW, "blog")
FRONTIER = "ledgers/camunda-docs-blog.frontier.txt"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/140.0.0.0 Safari/537.36")

os.makedirs(BLOG, exist_ok=True)

xml = open(os.path.join(RAW, "blog_sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", xml)
posts, seen = [], set()
for u in locs:
    u = u.strip()
    if not re.match(r"https://camunda\.com/blog/\d{4}/\d{2}/", u):
        continue
    if u in seen:
        continue
    seen.add(u)
    posts.append(u)

if not os.path.exists(FRONTIER):
    with open(FRONTIER, "w", encoding="utf-8") as fh:
        for i, u in enumerate(posts, 1):
            fh.write("%d\t%s\n" % (i, u))
    print("frontier written:", len(posts))

log = open(os.path.join(RAW, "fetch.log"), "a", encoding="utf-8")
start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
for i, u in enumerate(posts, 1):
    if i < start:
        continue
    p = os.path.join(BLOG, "%04d.html" % i)
    if os.path.exists(p) and os.path.getsize(p) > 2000:
        continue
    r = subprocess.run(["curl", "-s", "-m", "40", "-A", UA, "-o", p, "-w", "%{http_code} %{size_download}"],
                       capture_output=True)
    out = r.stdout.decode(errors="replace").strip()
    log.write("%d\t%s\t%s\n" % (i, u, out))
    log.flush()
    if i % 50 == 0:
        print("fetched", i, "/", len(posts), out, flush=True)
    time.sleep(1.0)
log.close()
print("done", len(posts))
