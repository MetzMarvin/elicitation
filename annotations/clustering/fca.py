"""Partial-profile review (PATTERN-SPEC.md: FCA only after the crisp run, to judge merges).

For the medium level: drop k slots (k = 0..4) and find every partial profile shared by >= 3 workflows.
Partial profiles must keep the writer slot, >= 1 function slot and >= 1 authority slot. Identical
member sets are collapsed into one concept, listed with its closure (all slots its members agree on).
Also: nearest-neighbour distance (number of differing slots) of every chain to a chain of another
workflow.

Lower bound only: a chain counts on a kept slot only if that slot is determined.
Writes annotations/clustering/out-patterns/fca.md, fca-coverage.png, fca-distance.png.
"""
import collections
import itertools
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from patterns import load, slots, show, OUT, MIN_WORKFLOWS

import sys
LEVEL = sys.argv[1] if len(sys.argv) > 1 else "medium"
FUNCTION = {"structure", "operations", "autonomy"}
AUTHORITY = {"shape", "ungated-reach", "outward-ungated", "mutates"}
MAX_DROP = 4


def main():
    chains, skipped, arts = load()
    n_all, n_ann = len(arts), len(arts) - len(skipped)
    names = [n for n, _ in slots(chains[0]["raw"], LEVEL)]
    for c in chains:
        c["s"] = [v for _, v in slots(c["raw"], LEVEL)]

    def det(c, i):
        return next(iter(c["s"][i])) if len(c["s"][i]) == 1 else None

    concepts = {}          # member-artefact frozenset -> (k, kept slots, values, chains)
    per_k = {}
    for k in range(MAX_DROP + 1):
        cov, count = set(), 0
        for kept in itertools.combinations(range(len(names)), len(names) - k):
            kn = {names[i] for i in kept}
            if "writer" not in kn or not (kn & FUNCTION) or not (kn & AUTHORITY):
                continue
            groups = collections.defaultdict(list)
            for c in chains:
                vals = tuple(det(c, i) for i in kept)
                if None not in vals:
                    groups[vals].append(c)
            for vals, mem in groups.items():
                arts_ = frozenset(m["artefact"] for m in mem)
                if len(arts_) < MIN_WORKFLOWS:
                    continue
                count += 1
                cov |= arts_
                if arts_ not in concepts or concepts[arts_][0] > k:
                    concepts[arts_] = (k, kept, vals, mem)
        per_k[k] = (count, cov)

    def closure(mem):
        out = []
        for i, n in enumerate(names):
            vs = {det(m, i) for m in mem}
            if len(vs) == 1 and None not in vs:
                out.append(f"{n}={show(vs.pop())}")
        return out

    # nearest neighbour (determined slots of both; undetermined slot = no mismatch)
    nn = []
    for c in chains:
        best = None
        for d in chains:
            if d["artefact"] == c["artefact"]:
                continue
            dist = sum(1 for i in range(len(names))
                       if det(c, i) is not None and det(d, i) is not None and det(c, i) != det(d, i))
            best = dist if best is None else min(best, dist)
        nn.append(best)
    nn_hist = collections.Counter(nn)

    L = [f"# Partial-profile review ({LEVEL} level, lower bound)", "",
         f"{len(chains)} chains / {n_ann} annotatable / {n_all} workflows. Slots: {', '.join(names)}.",
         "Kept slots must include writer, >= 1 of structure/operations/autonomy, >= 1 of shape/ungated-reach/mutates.", "",
         "## Coverage when k slots are left open", "",
         "| k open | partial profiles with >= 3 workflows | workflows covered (of 90) | of 72 |", "|---|---|---|---|"]
    for k, (cnt, cov) in per_k.items():
        L.append(f"| {k} | {cnt} | {len(cov)} ({len(cov)/n_all:.0%}) | {len(cov)/n_ann:.0%} |")
    L += ["", "## Nearest neighbour", "",
          "Differing slots between a chain and the closest chain of another workflow (undetermined slots count as agreeing):", "",
          "| differing slots | chains |", "|---|---|"]
    L += [f"| {d} | {nn_hist[d]} |" for d in sorted(nn_hist)]
    L += ["", "## Concepts (distinct member sets), by fewest open slots then size", ""]
    ordered = sorted(concepts.items(), key=lambda kv: (kv[1][0], -len(kv[0])))
    for i, (arts_, (k, kept, vals, mem)) in enumerate(ordered, 1):
        dropped = [names[j] for j in range(len(names)) if j not in kept]
        srcs = collections.Counter(a.split("/")[0] for a in arts_)
        L += [f"### K{i}: {len(arts_)} workflows, {k} slot(s) open ({', '.join(dropped) or '-'}), "
              f"{len(srcs)} source(s)", "",
              "Defined by: " + "; ".join(f"{names[j]}={show(v)}" for j, v in zip(kept, vals)),
              "Closure (all members agree): " + "; ".join(closure(mem)),
              "Sources: " + ", ".join(f"{s} {n}" for s, n in srcs.most_common()),
              "Members: " + ", ".join(sorted(m["id"] for m in mem)), ""]
    open(os.path.join(OUT, f"fca-{LEVEL}.md"), "w", encoding="utf-8").write("\n".join(L))

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ks = list(per_k)
    ax.plot(ks, [len(per_k[k][1]) / n_all for k in ks], marker="o")
    for k in ks:
        ax.annotate(f"{len(per_k[k][1])/n_all:.0%}", (k, len(per_k[k][1]) / n_all), xytext=(4, 4),
                    textcoords="offset points", fontsize=8)
    ax.axhline(0.5, ls=":", c="k", lw=0.8)
    ax.set_xlabel(f"slots left open (of {len(names)})"); ax.set_ylabel("share of 90 workflows covered"); ax.set_ylim(0, 1)
    ax.set_title(f"{LEVEL} level: coverage by partial profiles (>= 3 workflows)")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, f"fca-coverage-{LEVEL}.png"), dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(6, 3.5))
    ds = sorted(nn_hist)
    ax.bar(ds, [nn_hist[d] for d in ds], color="#2a6f97")
    ax.set_xlabel("differing slots to nearest chain of another workflow"); ax.set_ylabel("chains")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, f"fca-distance-{LEVEL}.png"), dpi=150); plt.close(fig)

    for k, (cnt, cov) in per_k.items():
        print(k, cnt, len(cov))
    print("nn", dict(sorted(nn_hist.items())))


if __name__ == "__main__":
    main()
