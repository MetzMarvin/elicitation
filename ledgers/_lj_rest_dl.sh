#!/bin/sh
while IFS="	" read -r u f; do
  [ -s "$f" ] || curl -sS -L --max-time 30 -A "Mozilla/5.0" -o "$f" "$u"
  sleep 0.4
done < ledgers/_lj_rest_dl.tsv
