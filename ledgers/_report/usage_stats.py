"""Token/usage statistics from Claude Code transcripts of this project (main sessions + subagents)."""
import json, glob, os, collections, re
from pathlib import Path
P = Path(os.path.expanduser("~")) / ".claude/projects/C--Users-muffi-Desktop-Uni-Master-thesis-elicitation"
out = {}
for f in sorted(P.rglob("*.jsonl")):
    if "memory" in f.parts: continue
    rel = f.relative_to(P).as_posix()
    top = rel.split("/")[0].replace(".jsonl", "")
    seen = set(); u = collections.Counter(); models = collections.Counter(); tools = collections.Counter()
    ts = []; turns_user = 0; first_prompt = None; names = set(); cwd = None; api_err = 0
    with open(f, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try: d = json.loads(line)
            except Exception: continue
            t = d.get("timestamp")
            if t: ts.append(t)
            cwd = cwd or d.get("cwd")
            if d.get("type") == "user" and not d.get("isMeta"):
                m = d.get("message", {})
                c = m.get("content")
                if isinstance(c, str):
                    turns_user += 1
                    if first_prompt is None and not c.startswith("<"): first_prompt = c[:160]
            if d.get("type") in ("custom-title", "agent-name") or "sessionName" in d:
                names.add(str(d.get("customTitle") or d.get("agentName") or d.get("sessionName")))
            if d.get("type") != "assistant": continue
            m = d.get("message", {}); mid = m.get("id") or d.get("requestId") or d.get("uuid")
            for c in m.get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use":
                    key = (mid, c.get("id"))
                    if key not in seen: tools[c.get("name")] += 1; seen.add(key)
            if ("u", mid) in seen: continue
            seen.add(("u", mid))
            if d.get("isApiErrorMessage"): api_err += 1
            models[m.get("model")] += 1
            us = m.get("usage") or {}
            for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"):
                v = us.get(k)
                if isinstance(v, int): u[k] += v
    out[rel] = dict(session=top, subagent="/" in rel, bytes=f.stat().st_size, start=min(ts) if ts else None, end=max(ts) if ts else None,
                    api_calls=sum(models.values()), models=dict(models), usage=dict(u), tool_calls=sum(tools.values()),
                    top_tools=dict(tools.most_common(12)), user_turns=turns_user, first_prompt=first_prompt, names=sorted(names), cwd=cwd, api_errors=api_err)
json.dump(out, open(Path(__file__).parent / "usage_stats.json", "w", encoding="utf-8"), indent=1)
agg = collections.defaultdict(lambda: collections.Counter()); meta = {}
for rel, d in out.items():
    s = d["session"]; a = agg[s]
    a["files"] += 1; a["subagents"] += d["subagent"]; a["api_calls"] += d["api_calls"]; a["tool_calls"] += d["tool_calls"]
    for k, v in d["usage"].items(): a[k] += v
    m = meta.setdefault(s, {"start": d["start"], "end": d["end"], "models": collections.Counter(), "names": set(), "prompt": None})
    if d["start"] and (not m["start"] or d["start"] < m["start"]): m["start"] = d["start"]
    if d["end"] and (not m["end"] or d["end"] > m["end"]): m["end"] = d["end"]
    m["models"].update(d["models"]); m["names"].update(d["names"])
    if not d["subagent"]: m["prompt"] = d["first_prompt"]
for s, a in sorted(agg.items(), key=lambda x: meta[x[0]]["start"] or ""):
    m = meta[s]
    print(s[:8], m["start"], m["end"], dict(m["models"]), sorted(m["names"]), dict(a), "|", (m["prompt"] or "")[:100])
