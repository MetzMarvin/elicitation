"""Crisp pattern formation per PATTERN-SPEC.md (fixed 2026-10-07).

Reads annotations/<source>/NNN.yaml (read-only), writes into annotations/clustering/out-patterns/:
  patterns.md       summary per level, patterns with members, residue
  profiles-<level>.csv   every candidate profile with lower / upper support
  rank-size.png     profile sizes per level with the >= 3 threshold
  coverage.png      workflow coverage per level (lower / upper bound)

Usage: .venv/Scripts/python.exe patterns.py
"""
import collections
import csv
import glob
import itertools
import os

import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ANN = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out-patterns")
MIN_WORKFLOWS = 3

WRITERS = ["system", "insider", "outsider"]
WRITER_IDX = {"system-generated": 0, "insider-writable": 1, "outsider-writable": 2}
MUTATES = ["none", "internal-records", "external-systems"]
OUTWARD = {"external-recipient", "public"}
OP_BIN = {"classify": "classify-or-decide", "decide": "classify-or-decide", "extract": "extract",
          "generate": "generate-or-summarise", "summarise": "generate-or-summarise", "plan-act": "plan-act"}


def fs(*v):
    return frozenset(v)


def subsets(items):
    items = sorted(items)
    return [frozenset(c) for r in range(len(items) + 1) for c in itertools.combinations(items, r)]


# ---- raw possibility sets (medium granularity), coarse / fine derived from them
def writer_set(c):
    ws = [r["writer"] for r in c["reads_untrusted"]]
    known = [WRITER_IDX[w] for w in ws if w in WRITER_IDX]
    if "unknown" not in ws and known:
        return fs(WRITERS[max(known)])
    lo = max(known) if known else 0
    return frozenset(WRITERS[i] for i in range(lo, 3))


def mutates_set(c):
    m = c["authority"]["mutates"]
    return fs(m) if m in MUTATES else frozenset(MUTATES)


def sinks(c):
    return [(s["audience"], s["human_gate"]) for s in c["output"]["sinks"]]


def reach_medium(c):
    certain = {a for a, g in sinks(c) if g is False}
    maybe = {a for a, g in sinks(c) if g not in (True, False)} - certain
    return frozenset(frozenset(certain) | s for s in subsets(maybe))


def reach_fine(c):
    tokens, open_ = set(), []
    for a, g in sinks(c):
        if g is True:
            tokens.add(f"{a}/gated")
        elif g is False:
            tokens.add(f"{a}/ungated")
        else:
            open_.append(a)
    opts = [[f"{a}/gated", f"{a}/ungated"] for a in open_]
    return frozenset(frozenset(tokens | set(combo)) for combo in itertools.product(*opts))


def guards_medium(g):
    return "human-review" if "human-review" in g else "none" if not g else "other-only"


def slots(c, level):
    """Ordered (slot name, set of possible values) for one chain at one level."""
    st, aut, shape = c["structure"], c["function"]["autonomy"], c["output"]["shape"]
    ops, g = c["function"]["operations"], set(c["guards"])
    w, m = writer_set(c), mutates_set(c)
    if level == "posture":
        return [
            ("structure", fs("agent" if st == "agent-loop" else "non-agent")),
            ("autonomy", fs(aut)),
            ("writer", w),
            ("shape", fs("free-text" if shape == "free-text" else "bounded")),
            ("outward-ungated", frozenset("yes" if s & OUTWARD else "no" for s in reach_medium(c))),
            ("mutates", frozenset("none" if x == "none" else "some" for x in m)),
            ("human-review", fs("yes" if "human-review" in g else "no")),
        ]
    if level == "coarse":
        return [
            ("structure", fs("agent" if st == "agent-loop" else "non-agent")),
            ("autonomy", fs("suggests" if aut == "suggests" else "decides-or-acts")),
            ("writer", frozenset("outsider" if x == "outsider" else "not-outsider" for x in w)),
            ("shape", fs("free-text" if shape == "free-text" else "not-free-text")),
            ("outward-ungated", frozenset("yes" if s & OUTWARD else "no" for s in reach_medium(c))),
            ("mutates", frozenset("none" if x == "none" else "some" for x in m)),
            ("human-review", fs("yes" if "human-review" in g else "no")),
        ]
    common = [("structure", fs(st))]
    if level == "medium":
        common.append(("operations", fs(frozenset(OP_BIN[o] for o in ops))))
    else:
        common.append(("operations", fs(frozenset(ops))))
    common += [("autonomy", fs(aut)), ("writer", w), ("shape", fs(shape))]
    if level == "medium":
        common += [("ungated-reach", reach_medium(c)), ("mutates", m), ("guards", fs(guards_medium(g)))]
    else:
        common += [("sinks", reach_fine(c)), ("mutates", m), ("guards", fs(frozenset(g)))]
    return common


def variation(members):
    """Variable parts of the posture level, counted over a pattern's member chains."""
    out = {}
    def add(name, vals):
        out[name] = ", ".join(f"{v} {k}" for v, k in collections.Counter(vals).most_common())
    raw = [m["raw"] for m in members]
    add("structure", [c["structure"] for c in raw])
    add("operations", [show(frozenset(OP_BIN[o] for o in c["function"]["operations"])) for c in raw])
    add("shape", [c["output"]["shape"] for c in raw])
    add("internal ungated audiences",
        [show(frozenset(a for a, g in sinks(c) if g is False and a not in OUTWARD)) for c in raw])
    add("mutates", [c["authority"]["mutates"] for c in raw])
    add("other guards", [show(frozenset(set(c["guards"]) - {"human-review"})) for c in raw])
    add("sensitive (descriptor)", [show(frozenset(r["kind"] for r in c["reads_sensitive"])) for c in raw])
    return out


def show(v):
    if isinstance(v, frozenset):
        return "{" + ", ".join(sorted(v)) + "}" if v else "{}"
    return str(v)


def load():
    chains, skipped, arts = [], [], []
    for f in sorted(glob.glob(os.path.join(ANN, "*", "*.yaml"))):
        d = yaml.safe_load(open(f, encoding="utf-8"))
        arts.append(d["artefact"])
        if not d.get("annotatable"):
            skipped.append(d["artefact"])
            continue
        for c in d["chains"]:
            chains.append({"id": f"{d['artefact']}/{c['id']}", "artefact": d["artefact"],
                           "source": d["artefact"].split("/")[0], "raw": c,
                           "description": c["function"]["description"]})
    return chains, skipped, arts


def analyse(chains, level):
    names = [n for n, _ in slots(chains[0]["raw"], level)]
    for ch in chains:
        ch[level] = [v for _, v in slots(ch["raw"], level)]
        ch[level + "_det"] = all(len(v) == 1 for v in ch[level])
    profiles = {tuple(next(iter(v)) for v in ch[level]) for ch in chains if ch[level + "_det"]}
    rows = []
    for p in profiles:
        lower = [ch for ch in chains if ch[level + "_det"] and tuple(next(iter(v)) for v in ch[level]) == p]
        upper = [ch for ch in chains if all(pv in v for pv, v in zip(p, ch[level]))]
        rows.append({"profile": p, "lower": lower, "upper": upper,
                     "lw": {c["artefact"] for c in lower}, "uw": {c["artefact"] for c in upper},
                     "sources": collections.Counter(a.split("/")[0] for a in {c["artefact"] for c in lower})})
    rows.sort(key=lambda r: (-len(r["lw"]), -len(r["uw"]), [show(x) for x in r["profile"]]))
    pats_l = [r for r in rows if len(r["lw"]) >= MIN_WORKFLOWS]
    pats_u = [r for r in rows if len(r["uw"]) >= MIN_WORKFLOWS]
    cov_l = set().union(*[r["lw"] for r in pats_l]) if pats_l else set()
    cov_u = set().union(*[r["uw"] for r in pats_u]) if pats_u else set()
    undetermined = sum(not ch[level + "_det"] for ch in chains)
    return names, rows, pats_l, pats_u, cov_l, cov_u, undetermined


def main():
    os.makedirs(OUT, exist_ok=True)
    chains, skipped, arts = load()
    n_all, n_ann = len(arts), len(arts) - len(skipped)
    levels = ["posture", "coarse", "medium", "fine"]
    res = {lv: analyse(chains, lv) for lv in levels}

    L = ["# Crisp patterns per PATTERN-SPEC.md", "",
         f"{len(chains)} chains from {n_ann} annotatable workflows; {n_all} workflows in the denominator "
         f"({len(skipped)} not annotatable). Pattern = complete profile with >= {MIN_WORKFLOWS} workflows.", "",
         f"| Level | Profiles | Patterns (lower / upper) | Chains undetermined | Covered of {n_all} (lower / upper) | Covered of {n_ann} (lower / upper) | Largest pattern (workflows) |",
         "|---|---|---|---|---|---|---|"]
    for lv in levels:
        names, rows, pl, pu, cl, cu, und = res[lv]
        big = len(pl[0]["lw"]) if pl else 0
        L.append(f"| {lv} | {len(rows)} | {len(pl)} / {len(pu)} | {und} | "
                 f"{len(cl)} ({len(cl)/n_all:.0%}) / {len(cu)} ({len(cu)/n_all:.0%}) | "
                 f"{len(cl)/n_ann:.0%} / {len(cu)/n_ann:.0%} | {big} |")
    L.append("")

    for lv in levels:
        names, rows, pl, pu, cl, cu, und = res[lv]
        L += [f"## {lv.capitalize()}", "",
              f"Slots: {', '.join(names)}. Profiles: {len(rows)}; of these with 1 workflow: "
              f"{sum(len(r['lw']) == 1 for r in rows)}.", ""]
        shown = [r for r in rows if len(r["uw"]) >= MIN_WORKFLOWS]
        for i, r in enumerate(shown, 1):
            status = "PATTERN" if len(r["lw"]) >= MIN_WORKFLOWS else "pattern only in upper bound"
            flag = " (single source: template reuse?)" if len(r["sources"]) == 1 and r["lw"] else ""
            L += [f"### {lv[0].upper()}{i}: {len(r['lw'])} workflows lower / {len(r['uw'])} upper, {status}{flag}", "",
                  "; ".join(f"{n}={show(v)}" for n, v in zip(names, r["profile"])), "",
                  "Sources: " + (", ".join(f"{s} {k}" for s, k in r["sources"].most_common()) or "-"), ""]
            if lv == "posture" and r["lower"]:
                L += [f"- variable {k}: {v}" for k, v in variation(r["lower"]).items()] + [""]
            L += [f"- `{c['id']}`: {c['description']}" for c in r["lower"]]
            extra = [c for c in r["upper"] if c not in r["lower"]]
            L += [f"- (upper only) `{c['id']}`" for c in extra]
            L.append("")
        residue = sorted({c["artefact"] for c in chains} - cl)
        L += [f"Residue at {lv} (lower bound): {len(residue)} annotatable workflows in no pattern.", ""]
        if lv in ("posture", "medium"):
            L += [", ".join(residue), ""]

        with open(os.path.join(OUT, f"profiles-{lv}.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(names + ["workflows_lower", "workflows_upper", "sources", "members"])
            for r in rows:
                w.writerow([show(v) for v in r["profile"]] + [len(r["lw"]), len(r["uw"]),
                           " ".join(f"{s}:{k}" for s, k in r["sources"].items()),
                           " ".join(c["id"] for c in r["lower"])])
    L += ["## Not annotatable (in the denominator, never covered)", "", ", ".join(skipped), ""]
    open(os.path.join(OUT, "patterns.md"), "w", encoding="utf-8").write("\n".join(L))

    fig, axes = plt.subplots(1, len(levels), figsize=(5 * len(levels), 4), sharey=True)
    for ax, lv in zip(axes, levels):
        rows = res[lv][1]
        lw = [len(r["lw"]) for r in rows]
        ax.bar(range(1, len(lw) + 1), lw, color=["#2a6f97" if x >= MIN_WORKFLOWS else "#bbbbbb" for x in lw])
        ax.axhline(MIN_WORKFLOWS - 0.5, ls="--", c="red", lw=0.8)
        ax.set_title(f"{lv}: {len(rows)} profiles, {len(res[lv][2])} patterns")
        ax.set_xlabel("profile rank")
    axes[0].set_ylabel("workflows (lower bound)")
    fig.suptitle(f"Profile sizes per level (blue = pattern, >= {MIN_WORKFLOWS} workflows)")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "rank-size.png"), dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4))
    x = range(len(levels))
    lo = [len(res[lv][4]) / n_all for lv in levels]
    up = [len(res[lv][5]) / n_all for lv in levels]
    ax.bar([i - 0.2 for i in x], lo, 0.4, label="lower bound", color="#2a6f97")
    ax.bar([i + 0.2 for i in x], up, 0.4, label="upper bound", color="#9ecae1")
    for i in x:
        ax.text(i - 0.2, lo[i] + 0.01, f"{lo[i]:.0%}", ha="center", fontsize=8)
        ax.text(i + 0.2, up[i] + 0.01, f"{up[i]:.0%}", ha="center", fontsize=8)
    ax.axhline(0.5, ls=":", c="k", lw=0.8)
    ax.set_xticks(list(x)); ax.set_xticklabels(levels); ax.set_ylim(0, 1)
    ax.set_ylabel(f"share of all {n_all} workflows in >= 1 pattern"); ax.legend()
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "coverage.png"), dpi=150); plt.close(fig)

    for lv in levels:
        names, rows, pl, pu, cl, cu, und = res[lv]
        print(f"{lv}: {len(rows)} profiles, patterns {len(pl)}/{len(pu)}, covered {len(cl)}/{len(cu)} of {n_all}, "
              f"sizes {[len(r['lw']) for r in pl]}")


if __name__ == "__main__":
    main()
