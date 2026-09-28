#!/usr/bin/env bash
# camunda-docs-blog: fetch the posts still missing from the raw blog dir.
#   bash ledgers/_cmdb_fetch2.sh [MAX]
# Reads ledgers/camunda-docs-blog.raw/missing.txt (n, one per line), writes blog/NNNN.html,
# appends one line per attempt to fetch2.log (n, code, size, seconds), and curl's stderr to
# fetch2.err on failure. Stops after MAX attempts (default 100000).
set -u
cd /c/Users/muffi/Desktop/Uni/Master_thesis/elicitation
RAW=ledgers/camunda-docs-blog.raw
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
MAX=${1:-100000}
got=0
fail=0
while read -r n; do
  n="${n%$'\r'}"
  [ -z "$n" ] && continue
  [ "$got" -ge "$MAX" ] && break
  url=$(sed -n "${n}p" ledgers/camunda-docs-blog.frontier.txt | cut -f2 | tr -d '\r')
  f=$(printf "%s/blog/%04d.html" "$RAW" "$n")
  code=$(curl -s -m 45 -A "$UA" -o "$f" -w "%{http_code} %{size_download} %{time_total}" "$url" 2>>"$RAW/fetch2.err")
  printf "%s\t%s\t%s\n" "$n" "$code" "$(date +%H:%M:%S)" >> "$RAW/fetch2.log"
  got=$((got + 1))
  case "$code" in 000*) fail=$((fail + 1));; esac
  if [ $((got % 25)) -eq 0 ]; then echo "attempted $got (n=$n) $code"; fi
  sleep 1
done < "$RAW/missing.txt"
echo "stopped: attempted=$got fails=$fail"
