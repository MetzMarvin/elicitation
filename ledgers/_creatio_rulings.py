#!/usr/bin/env python3
"""Write the two ruling files the Creatio ledger rows are built from.

  ledgers/_creatio/_creatio_figs_rulings.json   page URL -> notation of its figures
  ledgers/_creatio/_creatio_rulings.json        page URL -> the whole ledger row (AI pages)

The notation comes from the caption pass (ledgers/_creatio_figs_rulings.py) with OVERRIDES for the
pages whose captions did not decide it and which I then read in the contact sheets
(ledgers/_creatio/sheet_*.png, 2026-09-24) - the override text is what I saw, not an inference.

Row policy for pages that carry an AI/LLM keyword AND publish figures:
  * figure is BPMN and the AI mention is about something else  -> EXCLUDE E2, judgment True
  * figure is not BPMN                                         -> EXCLUDE E1
  * notation not resolved                                      -> UNCERTAIN + needs_visual_check
  * AI element documented INSIDE the process:
      - implement-prediction-models (BPMN figure showing the Predict data element as a task)
                                                                 -> INCLUDE + record
      - call-creatio-ai-element, predict-data-process-element (element documented, UI panel only)
                                                                 -> UNCERTAIN + needs_human_ruling

  python ledgers/_creatio_rulings.py --write
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
TODAY = "2026-09-24"
HOST = "https://academy.creatio.com"

# page slug -> (kind, what the figures actually are, according to sheet_*.png)
OVERRIDES = {
    "guides_ai-studio_creatio-ai-studio-overview":
        ("not-bpmn", "product screens: the AI Studio operations centre, the prompt-agent designer "
                     "and the agent-flow canvas (an agent canvas in the product UI, not BPMN 2.0)"),
    "guides_ai-studio_ai-twin-overview":
        ("not-bpmn", "the AI Twin chat/build panel in the product UI"),
    "guides_ai-studio_runtime_runtime-overview":
        ("not-bpmn", "the Runtime environments and deployments tables in the product UI"),
    "guides_ai-studio_set-ai-budget":
        ("not-bpmn", "the AI-credits budget panel in the product UI"),
    "guides_no-code-customization_ai-tools_creatio-ai_use-text-files":
        ("not-bpmn", "file/text configuration panels in the product UI"),
    "guides_no-code-customization_ai-tools_creatio-ai_connect-custom-llm":
        ("not-bpmn", "the custom-LLM connection form in the product UI"),
    "guides_no-code-customization_ai-tools_creatio-ai_creatio-ai-architecture":
        ("not-bpmn", "an architecture box diagram (external / DMZ / local network with firewall and "
                     "proxy boxes per channel) - a deployment sketch, not BPMN 2.0"),
    "guides_no-code-customization_ai-tools_creatio-ai_creatio-ai-overview":
        ("not-bpmn", "product screens plus a Creatio.ai box-and-arrow architecture sketch"),
    "guides_no-code-customization_ai-tools_creatio-ai_develop-ai-agent_develop-ai-agent-example":
        ("not-bpmn", "the agent setup form in the product UI"),
    "guides_no-code-customization_ai-tools_creatio-ai_develop-ai-skill_develop-ai-skill-example":
        ("not-bpmn", "the sub-agent setup form and the Creatio.ai chat in the product UI"),
    "guides_no-code-customization_ai-tools_creatio-ai_outlook_creatio-ai-for-outlook":
        ("not-bpmn", "the Creatio.ai add-in screen and its chat panel"),
    "guides_no-code-customization_ai-tools_creatio-ai_outlook_develop-ai-skill-outlook-addin":
        ("not-bpmn", "the add-in setup screens and the chat panel"),
    "guides_no-code-customization_ai-tools_predictive-models_implement-prediction-models":
        ("bpmn", "the process designer canvas: a signal start event ('Account added') -> the "
                 "'Predict account category' task -> an end event, plus the element setup panel "
                 "and the Predict data mini page"),
    "guides_no-code-customization_ai-tools_predictive-models_lookup-value-prediction-model":
        ("not-bpmn", "the lookup-prediction model mini page and the ML model parameters tab"),
    "guides_no-code-customization_ai-tools_predictive-models_numeric-field-value-prediction":
        ("not-bpmn", "the numeric-prediction model mini page and its parameters tab"),
    "guides_no-code-customization_ai-tools_predictive-models_predictive-scoring":
        ("not-bpmn", "the predictive-scoring mini page and its parameters tab"),
    "guides_no-code-customization_ai-tools_predictive-models_recommendation-prediction":
        ("not-bpmn", "the recommendation model mini page, its parameters tab and a contact page "
                     "carrying the recommendation"),
    "guides_no-code-customization_ai-tools_predictive-models_similar-text-search":
        ("not-bpmn", "the similar-text-search mini page and its parameters tab"),
    "guides_no-code-customization_ai-tools_predictive-models_train-prediction-models":
        ("not-bpmn", "the training progress panel and the factor list in the product UI"),
    "guides_no-code-customization_ai-tools_predictive-models_predictive-data-analysis":
        ("not-bpmn", "product screens of the predictive-analysis section"),
    "guides_no-code-customization_base-integrations_oauth-2-0_authorization-code-grant":
        ("not-bpmn", "the Azure app-registration screens and a columnar OAuth sequence diagram "
                     "(numbered steps between client and server bands) - not BPMN 2.0"),
    "guides_no-code-customization_base-integrations_microsoft-email-contacts-and-calendar":
        ("not-bpmn", "the Azure portal screens and the calendar settings dialog"),
    "guides_no-code-customization_bpm-tools_bpm-process-examples_how-send-emails-via-business-processes":
        ("bpmn", "the process designer canvases: the 'Meeting process', the Send email element "
                 "setup area and the parameter picker"),
    "guides_no-code-customization_bpm-tools_business-process-setup_process-collections":
        ("bpmn", "the process designer canvas and the element palette"),
    "guides_no-code-customization_bpm-tools_business-process-setup_process-designer-basics":
        ("bpmn", "the process designer canvas with elements being dragged from the palette"),
    "guides_no-code-customization_bpm-tools_business-process-setup_process-designer":
        ("bpmn", "the process designer canvas and its panels"),
    "guides_no-code-customization_bpm-tools_business-process-setup_process-data":
        ("bpmn", "the process designer canvas and its panels"),
    "guides_no-code-customization_bpm-tools_business-process-setup_process-events":
        ("bpmn", "the process designer canvas with event elements"),
    "guides_no-code-customization_bpm-tools_business-process-setup_process-parameters":
        ("bpmn", "the process designer canvas and the parameter panels"),
    "guides_no-code-customization_bpm-tools_business-process-setup_process-formulas":
        ("bpmn", "the process designer canvas and the formula dialog"),
    "guides_no-code-customization_customization-tools_app-management_apps-management":
        ("not-bpmn", "the application gallery and the 'select the app' cards in the product UI"),
    "guides_no-code-customization_customization-tools_app-management_alm-portal":
        ("not-bpmn", "the ALM portal screens in the product UI"),
    "guides_no-code-customization_customization-tools_ui-and-business-logic-customization_UI-designer":
        ("not-bpmn", "the UI designer screens (page and layout editing) in the product UI"),
    "guides_no-code-customization_customization-tools_ui-and-business-logic-customization_implement-a-custom-web-service":
        ("not-bpmn", "the code/IDE screens of the web-service editor"),
    "guides_no-code-customization_customization-tools_custom-localization_localize-core-resources-of-the-app":
        ("not-bpmn", "the localisation table screens in the product UI"),
}

# Pages whose contact-sheet reading did not settle the notation: UNCERTAIN, needs a human look.
UNRESOLVED = {
    "guides_no-code-customization_bpm-tools_business-process-administration_activate-process":
        "the process-administration screens (process library, process log, activation panels) - "
        "administration UI, and I could not tell whether a process diagram is published too",
    "guides_no-code-customization_bpm-tools_business-process-administration_cancel-process":
        "the process log screen with the cancel action - administration UI, process diagram not "
        "excluded",
    "guides_no-code-customization_bpm-tools_business-process-administration_set-up-permissions-to-a-process":
        "the process-permission screens - administration UI, process diagram not excluded",
    "guides_no-code-customization_bpm-tools_business-process-administration_view-process-execution-data":
        "the process log screens - administration UI, process diagram not excluded",
    "guides_no-code-customization_bpm-tools_business-process-administration_view-process-properties":
        "the process property screens - administration UI, process diagram not excluded",
    "guides_no-code-customization_bpm-tools_process-elements-reference_user-actions_approval-process-element":
        "the element's setup panel; the contact sheet also carries process fragments from "
        "neighbouring element pages and I could not attribute them to this one",
    "guides_no-code-customization_bpm-tools_process-elements-reference_user-actions_task-process-element":
        "the element's setup panel; same attribution problem as the Approval element page",
    "guides_no-code-customization_bpm-tools_process-elements-reference_user-actions_auto-generated-page-process-element":
        "the element's setup panel plus a small process fragment on the same sheet that I could "
        "not attribute to this page with certainty",
}

RELEASE_NOTES = [
    "guides_resources_release-notes_7171-release-notes",
    "guides_resources_release-notes_7172-release-notes",
    "guides_resources_release-notes_7174-release-notes",
    "guides_resources_release-notes_7182-release-notes",
    "guides_resources_release-notes_7185-release-notes",
    "guides_resources_release-notes_8-3-1-twin-release-notes",
    "guides_resources_release-notes_8-3-2-twin-release-notes",
    "guides_resources_release-notes_8-3-4-twin-release-notes",
    "guides_resources_release-notes_801-atlas-release-notes",
    "guides_resources_release-notes_8010-atlas-release-notes",
    "guides_resources_release-notes_807-atlas-release-notes",
    "guides_resources_release-notes_82-energy-release-notes",
]
RN_NAMED = ("release-note illustrations: product screenshots and animated GIFs of the changed "
            "screens, plus the 'release highlights overview' webinar banner - no process model")

BULK = {
    "not-bpmn": (
        "the product UI screens this page publishes (settings, forms, lists and panels)",
        ["guides_dev_development-on-creatio-platform_getting-started_development-recommendations",
         "guides_dev_development-on-creatio-platform_integrations-and-api_chat-channels-integration",
         "guides_mobile_basics_creatio-ai-in-mobile-creatio",
         "guides_no-code-customization_bpm-tools_process-elements-reference_system-actions_delete-data-element",
         "guides_resources_update-guide",
         "guides_no-code-customization_bpm-tools_dynamic-case-setup_case-designer-elements-reference_approval-case-element",
         "guides_no-code-customization_bpm-tools_dynamic-case-setup_case-designer-workflows_add-case-elements",
         "guides_no-code-customization_bpm-tools_dynamic-case-setup_case-designer-workflows_execute-case",
         "guides_no-code-customization_bpm-tools_dynamic-case-setup_case-designer-workflows_set-up-approval-case",
         "guides_no-code-customization_bpm-tools_dynamic-case-setup_case-designer-workflows_set-up-case-stages"],
        "the Case Designer stage and setup panels - Case Designer is Creatio's own case-management "
        "modeller, not BPMN 2.0",
    ),
    "bpmn": (
        "the process designer canvases this page publishes (start and end events, tasks, "
        "gateways, sequence flows)",
        ["guides_no-code-customization_bpm-tools_bpm-process-examples_update-currency-exchange-rates-with-web-service-integration",
         "guides_no-code-customization_bpm-tools_process-element-use-cases_how-to-use-sub-processes",
         "guides_no-code-customization_bpm-tools_process-element-use-cases_use-process-parameters"],
        "the BPMN process models in the process designer",
    ),
}

# The pages where an AI/ML element is documented as an element INSIDE a process.
SPECIAL = {
    "guides_no-code-customization_ai-tools_predictive-models_implement-prediction-models": {
        "verdict": "INCLUDE",
        "record": "corpus/creatio/001_implement-prediction-models.md",
        "note": ("The page's own figure (Fig. 1, 'An ML model implementation process') is a BPMN "
                 "process in the Creatio process designer whose task is the ML prediction element: "
                 "a signal start event 'Account added' -> the 'Predict account category' task -> an "
                 "end event, and the page text walks through adding that element to the process. "
                 "The AI/ML element sits inside the process model, so the artefact meets the "
                 "criterion."),
    },
    "guides_no-code-customization_bpm-tools_process-elements-reference_system-actions_call-creatio-ai-element": {
        "verdict": "UNCERTAIN", "record": "corpus/creatio/002_call-creatio-ai-element.md",
        "needs_human_ruling": True,
        "question": ("The source's own anchor page for the in-process AI element ('Call Creatio.ai') "
                     "documents the element, its Skill parameters and its result handling, but the "
                     "two figures it publishes are the element's parameter panels - no BPMN diagram "
                     "in which the element appears. Does the source contribute an artefact here "
                     "(prose-documented AI element inside a process, capture = element panels), or "
                     "does the absence of a published process model mean E1/E0? Recorded as "
                     "UNCERTAIN because a wrong exclusion is unrecoverable (shared rules 1-2)."),
    },
    "guides_no-code-customization_bpm-tools_process-elements-reference_system-actions_predict-data-process-element": {
        "verdict": "UNCERTAIN", "record": "corpus/creatio/003_predict-data-process-element.md",
        "needs_human_ruling": True,
        "question": ("This page documents the 'Predict data' element - the ML-model element that is "
                     "placed INSIDE a business process - but the single figure is the element's "
                     "setup panel (Machine learning model, prediction type, record to predict), not "
                     "a process model. Same boundary question as the Call Creatio.ai page: does an "
                     "AI element placed in a process count as an artefact when only its parameter "
                     "panel is published?"),
    },
}


def quote(text, needle=None, words=22):
    """A verbatim window of the page text: around `needle` if given, else the opening words."""
    t = re.sub(r"\s+", " ", text or "").strip()
    if needle and needle in t:
        i = t.index(needle)
        seg = t[max(0, i - 60):i + 220]
    else:
        seg = t
    parts = seg.split()
    return " ".join(parts[:words]) + (" ..." if len(parts) > words else "")


def main():
    idx = json.loads((OUT / "figs_index.json").read_text(encoding="utf-8"))
    arts = json.loads((OUT / "articles.json").read_text(encoding="utf-8"))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "figscls", pathlib.Path(__file__).resolve().parent / "_creatio_figs_rulings.py")
    figscls = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(figscls)

    SCOPE = ("/guides/no-code-customization/", "/guides/ai-studio/", "/guides/ai-development/")
    by_page = {}
    for it in idx:
        by_page.setdefault(it["slug"], []).append(it)
    # every in-scope figure page must carry a notation call, including the ones whose figures were
    # never downloaded (their captions are still evidence): classify them here as well
    for slug, a in arts.items():
        if slug in by_page or not a.get("imgs"):
            continue
        path = "/" + slug[:-5].replace("_", "/")
        # in-scope pages are the population; outside them, only the AI-keyword pages are ledgered
        # (the unfiltered check), so both need a notation call
        if not (any(path.startswith(p) for p in SCOPE) or a.get("kw")):
            continue
        by_page[slug] = [{"file": None, "slug": slug, "page": path, "src": "",
                          "alt": i.get("alt", ""), "text_before": i.get("text_before", ""),
                          "text_after": i.get("text_after", "")} for i in a["imgs"]]

    notation, rulings = {}, {}
    stats = {"bpmn": 0, "not-bpmn": 0, "unsure": 0}
    for slug, figs in sorted(by_page.items()):
        page = figs[0]["page"]
        key = slug[:-5] if slug.endswith(".html") else slug
        if key in OVERRIDES:
            kind, named = OVERRIDES[key]
        elif key in UNRESOLVED:
            kind, named = "unsure", UNRESOLVED[key]
        elif key in RELEASE_NOTES:
            kind, named = "not-bpmn", RN_NAMED
        elif any(key in keys for _, (_, keys, _) in BULK.items()):
            kk = next(k for k, (_, keys, _) in BULK.items() if key in keys)
            kind, named = kk, BULK[kk][2]
        else:
            ks = [figscls.classify(f.get("alt", ""), f.get("text_before", ""),
                                   f.get("text_after", "")) for f in figs]
            kind = ("bpmn" if any(k[0] == "bpmn" for k in ks)
                    else "unsure" if any(k[0] == "unsure" for k in ks) else "not-bpmn")
            named = next(k[1] for k in ks if k[0] == kind)
        alts = " | ".join(filter(None, [f.get("alt", "") for f in figs]))[:260]
        notation[key] = {
            "kind": kind, "named": named, "page": page,
            "figures_looked_at": [f["file"] for f in figs if f["file"]],
            "figure_captions": alts,
            "figure_evidence": (f"contact-sheet reading {TODAY}: {len(figs)} figure(s) downloaded "
                                f"and looked at" if key in OVERRIDES or key in UNRESOLVED
                                or key in RELEASE_NOTES or any(key in k for _, (_, k, _) in BULK.items()) else
                                f"caption/alt of the {len(figs)} downloaded figure(s)"),
            "evidence": quote(arts.get(slug, {}).get("text", "")),
        }
        stats[kind] += 1

        a = arts.get(slug, {})
        text = a.get("text", "") or ""
        kw = a.get("kw", {}) or {}
        if not kw:
            continue                                   # no AI keyword: the row is built from notation
        if key in SPECIAL:
            sp = SPECIAL[key]
            rulings[key] = {
                "title": a.get("h1", ""), "verdict": sp["verdict"], "reason": None, "judgment": True,
                "evidence": quote(text, "predict" if "predict" in text else None),
                "record": sp.get("record"),
                "needs_visual_check": False,
                "needs_human_ruling": bool(sp.get("needs_human_ruling")),
                "question": sp.get("question"),
                "note": sp.get("note") or (
                    "An AI element that the product places INSIDE a business process is documented "
                    "on this page, but the page publishes no process model of its own - the record "
                    "captures the wording and the researcher decides the boundary."),
                "figure_evidence": notation[key]["figure_evidence"],
            }
            continue
        first_kw = next(iter(kw))
        if kind == "unsure":
            rulings[key] = {
                "title": a.get("h1", ""), "verdict": "UNCERTAIN", "reason": None, "judgment": False,
                "evidence": quote(text, first_kw),
                "record": None, "needs_visual_check": True, "needs_human_ruling": False,
                "question": None,
                "note": ("The page carries AI/LLM vocabulary in its article text and publishes "
                         f"figures, but I could not settle the figure notation from the contact "
                         f"sheet ({named}). Not excluded: the notation is the only open question."),
                "figure_evidence": notation[key]["figure_evidence"],
            }
            continue
        reason = "E1-not-bpmn" if kind == "not-bpmn" else "E2-no-ai-element"
        note = (f"The page's figures are {named}." if kind == "not-bpmn" else
                f"The page publishes a BPMN process model ({named}), but the AI/LLM vocabulary in "
                f"its text is not an element inside that process: the keyword that put it in the "
                f"AI screen is '{first_kw}'.")
        rulings[key] = {
            "title": a.get("h1", ""), "verdict": "EXCLUDE", "reason": reason,
            "judgment": kind == "bpmn", "evidence": quote(text, first_kw),
            "record": None, "needs_visual_check": False, "needs_human_ruling": False,
            "question": None, "note": note,
            "figure_evidence": notation[key]["figure_evidence"],
        }

    print("notation: pages", len(notation), stats)
    print("rulings (AI pages):", len(rulings),
          {v: sum(1 for r in rulings.values() if r["verdict"] == v)
           for v in ("INCLUDE", "UNCERTAIN", "EXCLUDE")})
    if "--write" not in sys.argv:
        print("preview only (no --write)")
        return
    (OUT / "_creatio_figs_rulings.json").write_text(
        json.dumps(notation, indent=1, ensure_ascii=False), encoding="utf-8")
    (OUT / "_creatio_rulings.json").write_text(
        json.dumps(rulings, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote both ruling files")


if __name__ == "__main__":
    main()
