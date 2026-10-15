"""Step 2, second sub-step: group annotated AI chains into candidate clusters.

Reads annotations/<source>/NNN.yaml (read-only) and writes into annotations/clustering/out/:
  chains.csv        one row per chain, coded features
  distance.csv      pairwise Gower distance
  clusters.md       proposed clusters with shared features and members
  dendrogram.png    average-linkage tree, cut line
  heatmap.png       feature matrix in dendrogram order, cluster bands
  map.png           2-D classical MDS of the distance matrix, coloured by cluster
  silhouette.png    mean silhouette per number of clusters

Distance = Gower over the security-relevant dimensions of 004_method.tex (function, authority,
provenance) plus guards; each feature group weighs equally. `unknown` is treated as missing (the
feature is skipped for that pair), never as `none`. Business semantics and sensitive-data kind
are not in the distance; sensitive data is only reported per cluster.

Usage: .venv/Scripts/python.exe cluster.py [--k N]
"""
import argparse
import collections
import csv
import glob
import os

import numpy as np
import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from scipy.spatial.distance import squareform

HERE = os.path.dirname(os.path.abspath(__file__))
ANN = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")

AUTONOMY = {"suggests": 0, "decides": 1, "acts": 2}
WRITER = {"system-generated": 0, "insider-writable": 1, "outsider-writable": 2}
SHAPE = {"closed-label": 0, "structured": 1, "free-text": 2}
MUTATES = {"none": 0, "internal-records": 1, "external-systems": 2}
OPS = ["classify", "extract", "summarise", "generate", "decide", "plan-act"]
STRUCT = ["single-call", "fixed-sequence", "agent-loop"]
AUD = ["control-flow", "internal-system", "internal-human", "external-recipient", "public"]
GUARDS = ["human-review", "error-path-to-human", "validation", "prompt-guard", "confidence-threshold"]


def invokes_bin(v):
    if v == "unknown" or v is None:
        return None
    v = int(v)
    return 0 if v == 0 else 1 if v <= 2 else 2 if v <= 5 else 3


INV_LABEL = ["0", "1-2", "3-5", "6+"]


def load():
    rows, skipped = [], []
    for f in sorted(glob.glob(os.path.join(ANN, "*", "*.yaml"))):
        d = yaml.safe_load(open(f, encoding="utf-8"))
        if not d.get("annotatable"):
            skipped.append(d["artefact"])
            continue
        for c in d["chains"]:
            writers = [r["writer"] for r in c["reads_untrusted"]]
            known_w = [WRITER[w] for w in writers if w in WRITER]
            sinks = []
            for s in c["output"]["sinks"]:
                g = s["human_gate"]
                gate = "gated" if g is True else "ungated" if g is False else "gate?"
                sinks.append(f"{s['audience']}/{gate}")
            mut = c["authority"]["mutates"]
            inv = c["authority"]["invokes_without_gate"]
            rows.append({
                "id": f"{d['artefact']}/{c['id']}",
                "artefact": d["artefact"],
                "source": d["artefact"].split("/")[0],
                "description": c["function"]["description"],
                "ai_elements": c["ai_elements"],
                "structure": c["structure"],
                "operations": set(c["function"]["operations"]),
                "autonomy": c["function"]["autonomy"],
                "writer": max(known_w) if known_w else None,
                "writer_unknown": "unknown" in writers,
                "sensitive": sorted({r["kind"] for r in c["reads_sensitive"]}),
                "shape": c["output"]["shape"],
                "sinks": set(sinks),
                "audiences": {s["audience"] for s in c["output"]["sinks"]},
                "invokes": inv,
                "invokes_bin": invokes_bin(inv),
                "mutates": MUTATES.get(mut),
                "mutates_raw": mut,
                "guards": set(c["guards"]),
            })
    return rows, skipped


def jaccard(a, b):
    if not a and not b:
        return 0.0
    return 1 - len(a & b) / len(a | b)


def ordinal(a, b, span):
    if a is None or b is None:
        return None
    return abs(a - b) / span


# (name, distance function) — one entry per equally weighted feature group
FEATURES = [
    ("structure", lambda x, y: float(x["structure"] != y["structure"])),
    ("operations", lambda x, y: jaccard(x["operations"], y["operations"])),
    ("autonomy", lambda x, y: ordinal(AUTONOMY[x["autonomy"]], AUTONOMY[y["autonomy"]], 2)),
    ("writer", lambda x, y: ordinal(x["writer"], y["writer"], 2)),
    ("shape", lambda x, y: ordinal(SHAPE[x["shape"]], SHAPE[y["shape"]], 2)),
    ("sinks", lambda x, y: jaccard(x["sinks"], y["sinks"])),
    ("invokes", lambda x, y: ordinal(x["invokes_bin"], y["invokes_bin"], 3)),
    ("mutates", lambda x, y: ordinal(x["mutates"], y["mutates"], 2)),
    ("guards", lambda x, y: jaccard(x["guards"], y["guards"])),
]


def gower(rows):
    n = len(rows)
    D = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            vals = [d for _, f in FEATURES if (d := f(rows[i], rows[j])) is not None]
            D[i, j] = D[j, i] = sum(vals) / len(vals)
    return D


def silhouette(D, labels):
    n, s = len(labels), []
    for i in range(n):
        same = [j for j in range(n) if labels[j] == labels[i] and j != i]
        if not same:
            s.append(0.0)
            continue
        a = D[i, same].mean()
        b = min(D[i, [j for j in range(n) if labels[j] == c]].mean()
                for c in set(labels) if c != labels[i])
        s.append((b - a) / max(a, b) if max(a, b) > 0 else 0.0)
    return float(np.mean(s))


def mds(D):
    n = len(D)
    J = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * J @ (D ** 2) @ J
    w, v = np.linalg.eigh(B)
    idx = np.argsort(w)[::-1][:2]
    return v[:, idx] * np.sqrt(np.maximum(w[idx], 0)), w[idx] / w[w > 0].sum()


def onehot(rows):
    cols, M = [], []
    inv_names = {v: k for k, v in WRITER.items()}
    for r in rows:
        M.append([])
    def add(name, fn):
        cols.append(name)
        for r, m in zip(rows, M):
            m.append(fn(r))
    for s in STRUCT:
        add(f"structure: {s}", lambda r, s=s: float(r["structure"] == s))
    for o in OPS:
        add(f"op: {o}", lambda r, o=o: float(o in r["operations"]))
    for a in AUTONOMY:
        add(f"autonomy: {a}", lambda r, a=a: float(r["autonomy"] == a))
    for w in WRITER:
        add(f"writer: {w}", lambda r, w=w: float(r["writer"] == WRITER[w]))
    add("writer: unknown only", lambda r: float(r["writer"] is None))
    for s in SHAPE:
        add(f"shape: {s}", lambda r, s=s: float(r["shape"] == s))
    for a in AUD:
        add(f"sink: {a} (ungated)", lambda r, a=a: float(f"{a}/ungated" in r["sinks"]))
        add(f"sink: {a} (gated/?)", lambda r, a=a: float(any(x.startswith(a + "/") and not x.endswith("/ungated") for x in r["sinks"])))
    for i, lab in enumerate(INV_LABEL):
        add(f"ungated calls: {lab}", lambda r, i=i: float(r["invokes_bin"] == i))
    for m in MUTATES:
        add(f"mutates: {m}", lambda r, m=m: float(r["mutates_raw"] == m))
    for g in GUARDS:
        add(f"guard: {g}", lambda r, g=g: float(g in r["guards"]))
    keep = [i for i, _ in enumerate(cols) if any(m[i] for m in M)]
    return [cols[i] for i in keep], np.array([[m[i] for i in keep] for m in M]), inv_names


def profile(members):
    """Values shared by >= 2/3 of the members, per feature."""
    n, out = len(members), []
    def share(label, values):
        c = collections.Counter(values)
        for v, k in c.most_common():
            if k / n >= 2 / 3:
                out.append(f"{label}={v} ({k}/{n})")
    share("structure", [m["structure"] for m in members])
    share("autonomy", [m["autonomy"] for m in members])
    for o in OPS:
        k = sum(o in m["operations"] for m in members)
        if k / n >= 2 / 3:
            out.append(f"op {o} ({k}/{n})")
    inv_w = {v: k for k, v in WRITER.items()}
    share("writer", [inv_w.get(m["writer"], "unknown") for m in members])
    share("shape", [m["shape"] for m in members])
    for s in sorted({s for m in members for s in m["sinks"]}):
        k = sum(s in m["sinks"] for m in members)
        if k / n >= 2 / 3:
            out.append(f"sink {s} ({k}/{n})")
    share("ungated calls", [INV_LABEL[m["invokes_bin"]] if m["invokes_bin"] is not None else "unknown" for m in members])
    share("mutates", [m["mutates_raw"] for m in members])
    gs = collections.Counter(g for m in members for g in m["guards"])
    none = sum(not m["guards"] for m in members)
    if none / n >= 2 / 3:
        out.append(f"no guards ({none}/{n})")
    for g, k in gs.items():
        if k / n >= 2 / 3:
            out.append(f"guard {g} ({k}/{n})")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, help="number of clusters (default: best silhouette in 4..20)")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)

    rows, skipped = load()
    ids = [r["id"] for r in rows]
    D = gower(rows)
    Z = linkage(squareform(D, checks=False), method="average")

    ks = list(range(2, 26))
    sil = {k: silhouette(D, fcluster(Z, k, "maxclust")) for k in ks}
    k = args.k or max(range(4, 21), key=lambda k: sil[k])
    labels = fcluster(Z, k, "maxclust")
    # renumber clusters in dendrogram leaf order so figures and report agree
    order = dendrogram(Z, no_plot=True)["leaves"]
    remap = {}
    for i in order:
        remap.setdefault(labels[i], len(remap) + 1)
    labels = np.array([remap[l] for l in labels])
    cut = (Z[-k, 2] + Z[-k + 1, 2]) / 2 if k > 1 else Z[-1, 2]

    # ---- tables
    with open(os.path.join(OUT, "chains.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "cluster", "source", "ai_elements", "structure", "operations", "autonomy",
                    "writer", "writer_unknown_too", "sensitive", "shape", "sinks", "invokes_without_gate",
                    "mutates", "guards", "description"])
        inv_w = {v: k for k, v in WRITER.items()}
        for r, l in zip(rows, labels):
            w.writerow([r["id"], l, r["source"], r["ai_elements"], r["structure"],
                        " ".join(sorted(r["operations"])), r["autonomy"],
                        inv_w.get(r["writer"], "unknown"), r["writer_unknown"], " ".join(r["sensitive"]),
                        r["shape"], " ".join(sorted(r["sinks"])), r["invokes"], r["mutates_raw"],
                        " ".join(sorted(r["guards"])), r["description"]])
    with open(os.path.join(OUT, "distance.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow([""] + ids)
        for i, row in enumerate(D):
            w.writerow([ids[i]] + [f"{x:.3f}" for x in row])

    # ---- report
    L = [f"# Candidate clusters (proposal, k = {k})", "",
         f"Chains: {len(rows)} from {len({r['artefact'] for r in rows})} annotatable artefacts; "
         f"{len(skipped)} artefacts not annotatable (stay in the denominator).",
         f"Average-linkage Gower distance, cut at {cut:.3f}. Mean silhouette {sil[k]:.3f}.",
         "Pattern status needs >= 3 distinct artefacts (method, minimum-instance rule); "
         "this is a proposal for the researcher, not the classification step.", "",
         "Silhouette by k: " + ", ".join(f"{kk}: {sil[kk]:.2f}" for kk in ks), ""]
    for c in sorted(set(labels)):
        mem = [r for r, l in zip(rows, labels) if l == c]
        arts = {m["artefact"] for m in mem}
        src = collections.Counter(m["source"] for m in mem)
        idx = [i for i, l in enumerate(labels) if l == c]
        within = D[np.ix_(idx, idx)][np.triu_indices(len(idx), 1)].mean() if len(idx) > 1 else 0.0
        sens = collections.Counter(s for m in mem for s in m["sensitive"])
        status = "candidate pattern" if len(arts) >= 3 else "below threshold"
        L += [f"## Cluster {c}: {len(mem)} chains, {len(arts)} artefacts, {len(src)} sources ({status})", "",
              f"Mean within-cluster distance {within:.3f}.",
              "Shared (>= 2/3): " + ("; ".join(profile(mem)) or "nothing"),
              "Sources: " + ", ".join(f"{s} {n}" for s, n in src.most_common()),
              "Sensitive data (descriptor only): " + ", ".join(f"{s} {n}" for s, n in sens.most_common()), ""]
        for m in mem:
            L.append(f"- `{m['id']}`: {m['description']}")
        L.append("")
    L += ["## Not annotatable", "", ", ".join(skipped), ""]
    open(os.path.join(OUT, "clusters.md"), "w", encoding="utf-8").write("\n".join(L))

    # ---- figures
    cmap = plt.get_cmap("tab20")
    colour = {c: matplotlib.colors.to_hex(cmap((c - 1) % 20)) for c in set(labels)}

    fig, ax = plt.subplots(figsize=(10, 18))
    dendrogram(Z, labels=ids, orientation="left", color_threshold=cut, above_threshold_color="#999999",
               leaf_font_size=7, ax=ax)
    for t in ax.get_yticklabels():
        t.set_color(colour[labels[ids.index(t.get_text())]])
    ax.axvline(cut, ls="--", c="k", lw=0.8)
    ax.set_xlabel("Gower distance (average linkage)")
    ax.set_title(f"AI chains, {k} clusters (cut at {cut:.2f})")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "dendrogram.png"), dpi=150); plt.close(fig)

    cols, M, _ = onehot(rows)
    Mo = M[order]
    fig, ax = plt.subplots(figsize=(14, 18))
    ax.imshow(Mo, aspect="auto", cmap="Greys", interpolation="nearest")
    ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols, rotation=90, fontsize=7)
    ax.set_yticks(range(len(order))); ax.set_yticklabels([ids[i] for i in order], fontsize=6)
    for y, i in enumerate(order):
        ax.add_patch(plt.Rectangle((-2.5, y - 0.5), 1.5, 1, color=colour[labels[i]], clip_on=False))
    for y in range(1, len(order)):
        if labels[order[y]] != labels[order[y - 1]]:
            ax.axhline(y - 0.5, c="red", lw=0.8)
    prev = None
    for x, cname in enumerate(cols):
        grp = cname.split(":")[0]
        if prev is not None and grp != prev:
            ax.axvline(x - 0.5, c="#4c72b0", lw=0.6)
        prev = grp
    ax.set_title("Coded features per chain, dendrogram order (red lines = cluster borders)")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "heatmap.png"), dpi=150); plt.close(fig)

    X, var = mds(D)
    rng = np.random.default_rng(0)
    Xj = X + rng.normal(0, 0.006, X.shape)  # separate identical codings
    fig, ax = plt.subplots(figsize=(12, 10))
    for c in sorted(set(labels)):
        sel = labels == c
        ax.scatter(Xj[sel, 0], Xj[sel, 1], s=40, c=colour[c], label=f"{c} (n={sel.sum()})", edgecolor="k", lw=0.3)
        cx, cy = X[sel].mean(0)
        ax.annotate(str(c), (cx, cy), fontsize=13, weight="bold", ha="center", va="center",
                    bbox=dict(boxstyle="circle,pad=0.2", fc="white", ec=colour[c], alpha=0.8))
    for i, t in enumerate(ids):
        ax.annotate(t.replace("/C1", ""), Xj[i], fontsize=5, alpha=0.6, xytext=(3, 2), textcoords="offset points")
    ax.legend(title="cluster", fontsize=8, loc="best")
    ax.set_xlabel(f"MDS 1 ({var[0]:.0%} of variance)"); ax.set_ylabel(f"MDS 2 ({var[1]:.0%})")
    ax.set_title("AI chains by Gower distance (classical MDS; points jittered)")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "map.png"), dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(ks, [sil[x] for x in ks], marker="o")
    ax.axvline(k, ls="--", c="k", lw=0.8)
    ax.set_xlabel("number of clusters"); ax.set_ylabel("mean silhouette")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "silhouette.png"), dpi=150); plt.close(fig)

    print(f"{len(rows)} chains, k={k}, silhouette={sil[k]:.3f}, cut={cut:.3f}")
    for c in sorted(set(labels)):
        mem = [r for r, l in zip(rows, labels) if l == c]
        print(c, len(mem), len({m["artefact"] for m in mem}))


if __name__ == "__main__":
    main()
