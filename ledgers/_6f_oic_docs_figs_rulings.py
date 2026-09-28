#!/usr/bin/env python3
"""Write _6f_oic_docs_figs_rulings.json from my visual reading of the contact sheets.

The classes below are what I saw in ledgers/_6f_docs/sheet_*.png (140 figures, 5 sheets,
cell numbers = figs_index.json `cell`). Filenames are used only as keys back to the cell I
looked at - the class is a record of the picture, not an inference from the name.
"""
import json
import pathlib
import re

OUT = pathlib.Path(__file__).resolve().parent / "_6f_docs"
index = json.loads((OUT / "figs_index.json").read_text(encoding="utf-8"))

BPMN = {
    "human-submit.png": "the BPMN user-task marker, as a notation illustration",
    "human-approve.png": "the BPMN manual/approve task marker, as a notation illustration",
    "service-task.png": "the BPMN service-task marker, as a notation illustration",
    "timer-start.png": "the BPMN timer start-event symbol, as a notation illustration",
    "exclusive-gateway.png": "the BPMN exclusive-gateway diamond, as a notation illustration",
    "upload-form-process.png": "a BPMN process fragment in the process designer (start event, "
                              "user task, collapsed sub-process with the expand marker, end event)",
    "none-end-example.png": "a BPMN process fragment (start event, user tasks, end event) in the "
                            "process designer",
    "cor-order-process.png": "a BPMN process fragment with sequence flows and an end event",
    "cor-vendor-process.png": "a BPMN process fragment with sequence flows and an end event",
    "event-subprocess-example.png": "a BPMN process with an event sub-process and a boundary event",
    "error-start-da.png": "a BPMN process with an event sub-process and a boundary error event",
    "subprocess-1.png": "a BPMN process fragment with an expanded sub-process",
    "subprocess-2.png": "a BPMN process fragment with collapsed and expanded sub-processes",
    "abstract-activity-error.png": "the process designer canvas holding a BPMN process, with the "
                                   "activity palette",
    "abstract-activity-changetype.png": "the process designer canvas holding a BPMN process, with "
                                        "the activity palette",
    "exclusive-flow.png": "a BPMN process fragment with an exclusive gateway and Yes/No branches",
    "unconditional-flow.png": "the process designer canvas holding a BPMN process with a gateway",
    "conditional-flow.png": "the process designer canvas holding a BPMN process with a gateway",
    "draft-property1.png": "the process designer canvas with a task, a gateway and an open "
                           "properties menu",
    "draft-property2.png": "the process designer canvas with a task and its properties panel",
    "activity-open-prop.png": "the process designer canvas with a task's context menu open",
    "dp-human-task-activity.png": "a human-task card as it appears inside the process designer",
}

DMN = ("a DMN 1.x boxed expression, decision table or decision-requirements graph rendered in the "
       "Decision Model editor")
ANALYTICS = "an analytics dashboard or chart in the Process Automation Analytics web UI"
CLOUD = "a screenshot of the Oracle Cloud Infrastructure console or sign-in page"
NONBPMN_DEFAULT = ("a screenshot of the Process Automation web application UI (dialog, properties "
                   "panel or form)")

SPECIAL = {
    "lifecycle-versions.png": "a box-and-arrow diagram of Designer, Workspace and the activated "
                              "application - an architecture sketch, not BPMN",
    "lifecycle2.png": "a circular application-lifecycle illustration (design, test, activate), not BPMN",
    "identity-domain-config.png": "a platform architecture box diagram (tenancy, identity domain, "
                                  "Oracle Cloud applications) with people icons, not BPMN",
    "idcs-iam-config.png": "a platform architecture box diagram (tenancy, identity domain, Oracle "
                           "Cloud applications) with people icons, not BPMN",
    "oauth-flow.png": "an OAuth sequence diagram (two vertical bands, Client Application and "
                      "Authorization Server, with numbered steps and a purple end circle), not BPMN",
    "dmn-function-canvas.png": "a FEEL boxed-expression canvas in the Decision Model editor",
    "dmn-decisionmodel-graphview.png": "a DMN decision-requirements diagram (DRD) graph view",
    "analytics-activity-graphical.png": "an analytics screen carrying a small embedded process "
                                        "diagram view",
    "rest1.png": "a screenshot of a block of plain text/configuration prose, not a diagram",
    "rest2.png": "a screenshot of a block of plain text/configuration prose, not a diagram",
    "edit-properties-gray.png": "the grey pencil 'edit properties' icon - page chrome, not a figure",
    "advanced-search-tracking.png": "a search dialog in the task workspace UI",
    "base64.png": "a Custom Payload dialog holding a JSON/Base64 blob, not a diagram",
    "sign.png": "an Oracle Cloud sign-in page",
    "sign-iddomains.png": "an Oracle Cloud sign-in page",
    "idcs-sync.png": "an Oracle Cloud Infrastructure console page",
    "fa-display-name.png": "an Oracle Cloud Infrastructure console page",
    "error-details.png": "an inline validation callout in the form designer UI ('Fix / Needs an "
                         "associated form')",
    "milestone-details.png": "a stage/milestone detail card in the process workspace UI",
    "stage-details.png": "a stage detail card in the process workspace UI",
}


def classify(name):
    if name in BPMN:
        return "bpmn", BPMN[name]
    if name in SPECIAL:
        return "not-bpmn", SPECIAL[name]
    if name.startswith("dmn-"):
        return "not-bpmn", DMN
    if name.startswith("analytics-"):
        return "not-bpmn", ANALYTICS
    if name.startswith(("sign", "idcs", "oauth", "fa-")):
        return "not-bpmn", CLOUD
    return "not-bpmn", NONBPMN_DEFAULT


def page_quote(url, fig_src):
    """Verbatim sentence describing that figure on the page (<=25 words), else the page opener."""
    p = OUT / "pages" / url.split("/en/cloud/paas/", 1)[1].replace("/", "__")
    if not p.exists():
        return None
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", p.read_text(encoding="utf-8", errors="replace"),
               flags=re.S | re.I)
    txt = " ".join(re.sub("<[^>]+>", " ", t).split())
    base = fig_src.split("/")[-1]
    m = re.search(re.escape(base) + r"\s*(.{0,400}?)(?:\.\s|$)", txt)
    if m and len(m.group(1).split()) >= 5:
        seg = m.group(1)
    else:
        # fall back to the page's own opening words after the boilerplate banner
        seg = re.sub(r"^.*?display this content\s*", "", txt)
    words = seg.replace("Description of the illustration", "Description of the illustration").split()
    return " ".join(words[:25]) + (" ..." if len(words) > 25 else "")


rulings, pages = {}, {}
for it in index:
    name = it["file"].split("_", 1)[1]
    kind, named = classify(name)
    pg = pages.setdefault(it["page"], {"title": it["title"], "kinds": [], "named": [],
                                       "figs": [], "srcs": []})
    pg["kinds"].append(kind)
    pg["named"].append(named)
    pg["figs"].append(name)
    pg["srcs"].append(it["src"])

for url, pg in pages.items():
    # the page publishes a BPMN model if ANY figure I looked at is BPMN
    kind = "bpmn" if "bpmn" in pg["kinds"] else "not-bpmn"
    named = next((n for k, n in zip(pg["kinds"], pg["named"]) if k == kind), pg["named"][0])
    if len(set(pg["named"])) > 1:
        named = named + " (page also publishes: " + "; ".join(
            sorted({n for n in pg["named"] if n != named})) + ")"
    quote = page_quote(url, pg["srcs"][0])
    rulings[url] = {
        "kind": kind, "named": named, "figures_looked_at": pg["figs"],
        "evidence": quote,
        "figure_evidence": (f"contact-sheet reading 2026-09-24: {len(pg['figs'])} figure(s) "
                            f"downloaded and looked at ({', '.join(pg['figs'])}) - first figure: "
                            f"{named}"),
    }

(OUT / "_6f_oic_docs_figs_rulings.json").write_text(
    json.dumps(rulings, indent=1, ensure_ascii=False), encoding="utf-8")

print("pages classified:", len(rulings))
print("  bpmn   :", sum(1 for r in rulings.values() if r["kind"] == "bpmn"))
print("  not-bpmn:", sum(1 for r in rulings.values() if r["kind"] == "not-bpmn"))
missing = [u for u, r in rulings.items() if not r["evidence"]]
print("  pages without a quote:", len(missing))
for u in missing[:6]:
    print("     ", u)
