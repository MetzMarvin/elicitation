#!/usr/bin/env bash
# camunda-docs-blog: fetch the blog population, one URL per second, resumable.
#   bash ledgers/_cmdb_fetch.sh [MAX]
# Stops after MAX new fetches (default 100000) so it can run inside a foreground call.
# Writes ledgers/camunda-docs-blog.raw/blog/NNNN.html and appends to fetch.log.
set -u
cd /c/Users/muffi/Desktop/Uni/Master_thesis/elicitation
RAW=ledgers/camunda-docs-blog.raw
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
MAX=${1:-100000}
got=0
fail=0
while IFS=$'\t' read -r n url; do
  url="${url%$'\r'}"          # the frontier file is CRLF (written in text mode on Windows)
  [ "$got" -ge "$MAX" ] && break
  f=$(printf "%s/blog/%04d.html" "$RAW" "$n")
  if [ -s "$f" ] && [ "$(stat -c%s "$f")" -gt 2000 ]; then continue; fi
  code=$(curl -s -m 40 -A "$UA" --retry 3 --retry-all-errors --retry-delay 2 -o "$f" -w "%{http_code} %{size_download}" "$url")
  printf "%s\t%s\t%s\n" "$n" "$url" "$code" >> "$RAW/fetch.log"
  got=$((got + 1))
  case "$code" in 000*) fail=$((fail + 1));; esac
  if [ $((got % 25)) -eq 0 ]; then echo "fetched $got (last n=$n code=$code)"; fi
  sleep 1
done < ledgers/camunda-docs-blog.frontier.txt
echo "stopped: fetched=$got fails=$fail"
