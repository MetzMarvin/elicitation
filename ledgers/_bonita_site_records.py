"""Emit corpus records 012-016 (the five UNCERTAIN www.ofelia.com site pages).

The notes/questions already live in `_bonita_sitegen.RECORDS` (written for the ledger
rulings); this script adds the record-shaped front matter and writes the markdown, so the
ledger row and the corpus record cannot drift apart.

Run: python ledgers/_bonita_site_records.py [--write]
"""
import pathlib
import sys

import _bonita_sitegen as G

ELI = pathlib.Path(__file__).resolve().parent.parent
CORPUS = ELI / "corpus" / "bonitasoft"

# stem -> (verdict, bpmn_evidence, ai_evidence, capture_quality, extra sections)
EXTRA = {
    "012": (
        "UNCERTAIN",
        "The page publishes a diagram, and it is BPMN 2.0. The only textual proof is the SVG's "
        "own provenance comment, quoted verbatim from the file: `<!-- created with bpmn-js / "
        "http://bpmn.io -->`. It is the only one of the page group's SVGs that carries it. The "
        "canvas is 2492x270 and its labels (read from the pixels, because the export draws text "
        "as paths) are the sequence \"Customer onboarding request pending | Collect customer "
        "information | Verify identity | Perform standard due diligence | Check background | "
        "Integrate data | Approve final data | Create account | Customer successfully "
        "onboarded\", plus the branch \"Perform enhanced due diligence | Review data\".",
        "The AI mention is in the article prose around the diagram, not in the diagram's labels. "
        "Quoted verbatim from the page: \"Artificial intelligence (AI) and machine learning tools "
        "can analyze customer data and compare submitted documents—such as passports or "
        "driver's licenses—against official databases\". That describes AI/ML doing the "
        "document "
        "comparison inside the KYC scrutiny the drawn tasks (\"Verify identity\", \"Check "
        "background\") stand for - which is exactly the ambiguity the question records.",
        "marginal",
        "",
    ),
    "013": (
        "UNCERTAIN",
        "The figure is a Figma export, so no `<text>` node and no bpmn-js provenance comment "
        "survive: the notation had to be read from the pixels. What the mockup draws is two "
        "lanes - \"Risk Assessment Lane\" (start -> Verify -> Review) and \"Compliance Lane\" "
        "(Check -> end) - inside a Bonita Studio window frame. Lanes and tasks are drawn, but "
        "this is the vendor's own product mockup, not a BPMN 2.0 model; there are no pools, "
        "events, gateways or sequence flows of the BPMN kind.",
        "The AI is visible in the drawing as a product panel, not as a process element: the "
        "Studio window shows an \"AI Assistant\" beside the lanes, whose cards read \"Process "
        "Suggestion - Add parallel gateway for faster review\", \"Risk Analysis - Bottleneck "
        "detected at approval step\", \"Compliance Check - GDPR compliant, SOC 2 ready\" and "
        "\"Action Required - Review timeout configuration\". The AI is design-time advice about "
        "the model, not an AI element inside a running process.",
        "legible",
        "The page is `/downloads`, the Bonita Studio download page; the figure is "
        "`Bonita_studio_illu.svg` (472x376 as published; the capture is the same figure at "
        "944x752).",
    ),
    "014": (
        "UNCERTAIN",
        "The figure `Ofelia_workflow.svg` draws a process view with real control flow - "
        "\"Employee request\" -> \"Manager approval\" -> a branch into \"Finance review\" and "
        "\"Auto-approved\" -> \"Complete & notify\" - but in the vendor's proprietary card "
        "notation (a dark card headed \"Ofelia Workflow\" with a green \"Published\" badge). "
        "There are no pools, lanes, events, gateways or sequence flows, and no bpmn-js "
        "provenance: on the notation test alone this would be E1-not-bpmn, and it is recorded as "
        "UNCERTAIN only because \"a process depiction in proprietary notation\" is the kind of "
        "near-miss the researcher may still want to see.",
        "No AI element is drawn in the workflow card. The page is the Ofelia Assistant product "
        "page and its other figure, `Visuel.svg`, is a chat mockup of the assistant "
        "(\"Ofelia Agent\"), so any AI on the page is the assistant being sold, not an AI element "
        "inside the drawn process.",
        "legible",
        "The page is `/ofelia-assistant`; the figure is `Ofelia_workflow.svg` (440x313 as "
        "published; the capture is the same figure at 880x626).",
    ),
    "015": (
        "UNCERTAIN",
        "The figure `Frame 2147263655.svg` is a boxes-and-arrows architecture diagram of the "
        "Ofelia agent runtime, not a BPMN 2.0 model. It is a Figma-style export with zero "
        "`<text>` nodes and no bpmn-js provenance, so the box labels below were read from the "
        "pixels. Its boxes are: \"User message (Slack / "
        "Teams)\" -> \"Tool Mapping Agent (Intent classifier)\" -> \"User confirms action\" -> "
        "\"Action Agent (Exec. procedures)\", \"Answerer Agent (RAG responses)\", \"Out-of-scope "
        "(Graceful decline)\", \"Action Result (Feedback format)\", with \"Knowledge Retrieval "
        "System\" (Vector Search / Knowledge Graph / Key-value Lookup), \"Deterministic Execution "
        "-> BPA Engine Handoff\", \"Action execution (API calls under user token)\", \"Workflow "
        "Orchestration (BPMN sequencing & SLA)\" and \"Grounded Response\". One box names BPMN "
        "(\"BPMN sequencing & SLA\") and one names an engine handoff, but the drawing itself is "
        "an architecture diagram.",
        "The AI is the subject of the diagram rather than an element inside a process: three of "
        "the boxes are agents (\"Tool Mapping Agent (Intent classifier)\", \"Action Agent (Exec. "
        "procedures)\", \"Answerer Agent (RAG responses)\") and one is the knowledge store they "
        "retrieve from (\"Knowledge Retrieval System\" with \"Vector Search / Knowledge Graph / "
        "Key-value Lookup\"). The page's other figures are a layered architecture stack "
        "(`dev-engine_visual.svg`) and a nested security stack (`Image Container.svg`).",
        "legible",
        "The page is `/product/it-hub`; the figure is `Frame 2147263655.svg` (774x443 as "
        "published; the capture is the same figure at 1400x801).",
    ),
    "016": (
        "UNCERTAIN",
        "There is no diagram on this page at all. The only figure is a promotional banner, "
        "`Text to BPMN EN.png`, 700x200, reading \"Transform your business processes into a BPMN "
        "model with AI\" over a speech-bubble graphic with the call to action \"Try the BPMN AI "
        "generator!\". Naming BPMN is not drawing BPMN: the banner depicts no process, so on the "
        "artefact test this would be E0-no-artefact. It is kept as a record because it is the "
        "promotion pattern the thesis already tracks in the design-time-AI family - see "
        "`notes/uipath-promotion-pattern/analysis.md` - and the reviewer may want the corpus to "
        "carry the promotion alongside the artefacts it advertises.",
        "The AI mention is the banner's own claim: AI turns business processes into a BPMN "
        "model. That is design-time AI (the diagram generator), not an AI element inside a "
        "process. The article text around it is prose about AI in business process automation.",
        "legible",
        "The page is the blog article \"From data to decisions: the role of AI in business "
        "process automation\". The identical banner is republished by two further blog articles "
        "(`how-does-ai-challenge-traditional-process-automation-36fc1` and "
        "`what-is-hyperautomation-4be39`), which are the two E3 rows of this source.",
    ),
}


def dims(png):
    from PIL import Image
    with Image.open(png) as im:
        return im.size


def records():
    out = []
    for page, (stem, notation, artefacts, note, question, looked) in G.RECORDS.items():
        num = stem.split("_")[0]
        verdict, bpmn_ev, ai_ev, quality, extra = EXTRA[num]
        png = CORPUS / (stem + ".png")
        w, h = dims(png)
        url = "https://www.ofelia.com" + page
        body = [
            "---",
            "n: 0",
            f"url: {url}",
            "source: bonitasoft",
            "accessed: 2026-09-25",
            f"verdict: {verdict}",
            "needs_human_ruling: true",
            "question: >-",
        ]
        body += ["  " + l for l in wrap(question)]
        body += ["bpmn_evidence: >-"]
        body += ["  " + l for l in wrap(bpmn_ev)]
        body += ["ai_evidence: >-"]
        body += ["  " + l for l in wrap(ai_ev)]
        body += [
            "artefacts:",
            f"  - screenshot: {stem}.png",
            f"  - figure: {artefacts}",
            f"capture_quality: {quality}",
            f"capture_width_px: {w}",
            f"capture_height_px: {h}",
            "---",
            "",
            "## What the page shows",
            "",
            note,
            "",
            "## Observations",
            "",
            f"- Notation: {notation}.",
            f"- Evidence looked at: {looked}.",
        ]
        if extra:
            body += ["- " + extra]
        body += [
            "- This is the pixel-level finding; the same wording is the ledger row for this "
            "page, so the two cannot disagree.",
            "",
            "## Notes for the researcher",
            "",
            "One of the five www.ofelia.com pages ruled UNCERTAIN in this source (records "
            "012-016). The other 127 judged site pages are E0/E1/E2/E3 ledger rows without "
            "records.",
            "",
        ]
        out.append((stem, "\n".join(body) + ""))
    return out


def wrap(text, width=88):
    words = " ".join(text.split()).split(" ")
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def main():
    write = "--write" in sys.argv
    recs = records()
    for stem, text in recs:
        print(f"{stem}  {len(text)} chars")
        if write:
            (CORPUS / (stem + ".md")).write_text(text, encoding="utf-8")
    print(f"{len(recs)} records" + (" written" if write else " (dry run)"))


if __name__ == "__main__":
    main()
