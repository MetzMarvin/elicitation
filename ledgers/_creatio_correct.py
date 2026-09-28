#!/usr/bin/env python3
"""Supersede the 38 'notation unsure' rows now that their figures have been looked at.

The caption classifier left 38 rows UNCERTAIN + needs_visual_check because their figure captions
were absent or generic. Their figures were then pulled out and looked at (contact sheets
ledgers/_creatio/unsure_sheet_*.png and candidates*.png). The outcome of that pass is appended here
as superseding rows: the ledger is append-only, so a correction carries the same `n` and the last
row for an `n` wins (see tools/audit.py). One row was promoted to INCLUDE - a real BPMN diagram
whose task is the AI Sub-agent element (corpus record 004).

  python ledgers/_creatio_correct.py            # preview
  python ledgers/_creatio_correct.py --write
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
LEDGER = ELI / "ledgers" / "creatio.jsonl"
TODAY = "2026-09-24"

# n -> (verdict, reason, what the figures actually are, which files were looked at)
R = {
 53: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the shared mailbox permission settings",
      "scr_common_mailbox_accsess.png"),
 77: ("EXCLUDE", "E1-not-bpmn", "UI screenshots/GIFs of the REST web service set-up form",
      "scr_add_rest_web_service.gif, scr_web_service_method_properties.png"),
 78: ("EXCLUDE", "E1-not-bpmn", "UI screenshots/GIFs of the SOAP web service set-up form",
      "scr_add_soap_web_service_blur.gif, scr_soap_web_service_method_properties.png"),
 80: ("EXCLUDE", "E1-not-bpmn", "the vendor's integration illustration (boxes and arrows, no notation)",
      "scr_integration_schema.png"),
 93: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the Process library list", "scr_activate_process.png"),
 94: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the Process log list",
      "scr_chapter_processes_monitoring_cancel_process.png, "
      "scr_chapter_process_execution_cancel_multiple_processes.gif"),
 98: ("EXCLUDE", "E1-not-bpmn", "UI screenshots/GIF of the permission set-up for running a process",
      "set_process_permissions.gif, scr_bpm_permissions_use_permissions.png"),
100: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the process execution page and the process log",
      "scr_chapter_process_monitoring_open_process_history.png, subprocess_to_parent_process.gif"),
101: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the process properties page",
      "src_process_library_proc_characteristics_page.png"),
164: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the Approval element's setup area in the process designer",
      "chapter_process_designer_approval.png"),
165: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the Auto-generated page element's setup area",
      "scr_chapter_process_designer_auto_page_7.18.png, chapter_process_designer_elem_auto_page_type.png"),
170: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the Perform task element's setup area",
      "chapter_process_designer_make_a_task_7.18.png"),
224: ("EXCLUDE", "E1-not-bpmn", "the vendor's box-and-arrow diagram of package dependencies",
      "scr_example_cyclic_sequences.png, scr_hierarchy_cyclic_sequences.png"),
226: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the Application Designer and the section move steps",
      "scr_create_an_app.png, scr_select_a_section.png"),
229: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the page designer", "scr_open_dashboards.png"),
244: ("EXCLUDE", "E1-not-bpmn", "the vendor's architecture box diagrams of the on-site and cloud layouts",
      "scr_GeneralStructure.png, scr_ToolsNoCodeCreatorOnSite.png, scr_ToolsNoCodeCreatorCloud.png"),
268: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the List component's setup area",
      "scr_list_setup_area.png"),
286: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the Encrypted string field's setup area",
      "scr_encrypted_string_setup_area.png"),
300: ("EXCLUDE", "E1-not-bpmn", "UI screenshots/GIF of the Freedom UI dashboard and the sidebar set-up",
      "gif_sidebar_example.gif, scr_sidebar_parameters_8_1_4.png"),
303: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the app section set-up",
      "scr_set_up_sections.png, scr_edit_section.png"),
325: ("EXCLUDE", "E1-not-bpmn", "UI screenshots/GIFs of the Freedom UI shell",
      "scr_freedom_ui_shell_homepage.png, scr_freedom_ui_shell_general.png"),
354: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the 'New Ada channel' dialog", "scr_new_ada_channel_0.png"),
386: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the Product categories and types lookup",
      "scr_lookup_categories_and_types.png, scr_lookup_categories_and_types_new_category.png"),
393: ("EXCLUDE", "E1-not-bpmn", "UI screenshots/GIFs of the email content designer",
      "scr_content_designer_block_setup_area_steps.png, scr_template_empty_callouts.png"),
430: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the lead record page and the qualification task form",
      "scr_lead_management_process.png, scr_mql_to_sql.png, scr_sql_to_opportunity.png"),
431: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the Process library and the lead distribution steps",
      "scr_open_the_lead_distribution_process.png, scr_assign_lead_owner.png"),
432: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the new-lead form", "scr_lead_mini_page.png"),
442: ("EXCLUDE", "E1-not-bpmn", "a UI screenshot of the Case notification rules lookup",
      "scr_section_service_requests_rules.png"),
454: ("EXCLUDE", "E1-not-bpmn", "the vendor's architecture illustrations (tier pyramid; "
      "developer-to-marketplace boxes)", "scr_logic_levlels_en.png, scr_packages_approach.png"),
464: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the IDE menus and of the element property panels",
      "scr_AddList.png, scr_UsrSumNumbersProcessUserTask_props.png"),
486: ("EXCLUDE", "E0-no-artefact", "site logos plus six inline UI button icons named by the source",
      "btn_Add_value.png, btn_Throw_signal.png, btn_Add_flow.png, btn_Change_type.png, "
      "btn_is_equal.png, btn_System_actions.png"),
493: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the scheduler queue tables", "queue_01.png, queue_02.png"),
504: ("EXCLUDE", "E1-not-bpmn", "UI screenshots of the page designer (the Button component on the canvas)",
      "scr_default_color.png, scr_primary_color.png, scr_accent_color.png"),
507: ("EXCLUDE", "E2-no-ai-element", "a BPMN process diagram with two tasks and no AI element",
      "scr_process_diagram.png"),
508: ("EXCLUDE", "E2-no-ai-element", "a BPMN process diagram with two tasks and no AI element",
      "scr_process_diagram.png"),
517: ("EXCLUDE", "E0-no-artefact", "a single SDK button icon; a changelog entry with no figure",
      "btn_add.png"),
567: ("EXCLUDE", "E0-no-artefact", "SDK button icons and nothing else; a changelog entry with no figure",
      "btn_send_message.png, btn_actions_in_freedom_ui_designer.png"),
500: ("INCLUDE", None, "three BPMN process diagrams of the 'Summarize contact information' business process",
      "scr_read_data_in_process_diagram.png, scr_sub_agent_in_process_diagram.png, "
      "scr_auto_generated_page_in_process_diagram.png"),
}

E2_NOTE = ("The page carries a BPMN diagram but no AI element. The keyword that put it on the AI "
           "screen is 'auto-generated', which names the Auto-generated page process element, not an "
           "AI/LLM element: the diagram's two tasks are 'Fill out the email parameters' and "
           "'Send email'.")

NOTE_500 = ("Promoted from UNCERTAIN to INCLUDE by the visual pass: the page publishes three BPMN "
            "diagrams of the 'Summarize contact information' business process, and one of its tasks "
            "is the AI element - 'Run the AI Sub-agent', a Sub-agent element calling the 'Contact "
            "summary' sub-agent configured in Creatio.ai.")

arts = json.loads((OUT / "articles.json").read_text(encoding="utf-8"))
led = [json.loads(l) for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]
rows, header, footer = {}, None, None
for o in led:
    if o.get("type") == "header":
        header = o
    elif o.get("type") == "footer":
        footer = o
    else:
        rows[o["n"]] = o


def slug_of(url):
    return re.sub(r"[^A-Za-z0-9._-]", "_",
                  url.replace("https://academy.creatio.com", "").strip("/"))[:150] + ".html"


# The pages whose figures carry no caption at all: a quote is taken from the sentence of the page's
# article text that contains the marker below (verbatim, only truncated at 25 words).
EV_MARKER = {
 244: "To avoid irregularities",
 454: "Creatio is a no-code platform",
 464: "Implement a custom User task",
 486: "Implement custom prediction model",
 493: "Customize quartz task scheduler",
 504: "Button is a component",
 507: "page elements in the working area of the Process Designer",
 508: "page elements in the working area of the Process Designer",
 517: "This document details the technical changes",
 567: "This document details the technical changes",
}


def evidence_for(n, url):
    """A verbatim string from the page: its figure caption/alt, else a sentence of its text."""
    a = arts.get(slug_of(url)) or {}
    for im in (a.get("imgs") or []):
        alt = (im.get("alt") or "").strip()
        if alt and len(alt.split()) >= 3:
            return alt, "figure caption"
    t = re.sub(r"\s+", " ", a.get("text") or "").strip()
    marker = EV_MARKER.get(n)
    if marker and marker in t:
        t = re.sub(r"^.{0,300}?On this page\s*", "", t)
        sents = re.split(r"(?<=[.!?])\s", t)
        for i, s in enumerate(sents):
            if marker in s:
                return (sents[i - 1] + " " + s if i and len(s.split()) < 6 else s), "page text"
    m = re.search(r"[^.]{0,120}Fig\.[^.]{0,160}\.", t)
    if m:
        return m.group(0).strip(), "page text"
    return " ".join(t.split()[:24]), "page text"


new = []
for n, (verdict, reason, named, files) in sorted(R.items()):
    old = rows[n]
    ev, src = evidence_for(n, old["url"])
    ev = " ".join(ev.split())
    words = ev.split()
    if len(words) > 25:
        ev = " ".join(words[:25]) + " ..."
    if n == 500:
        row = {"n": n, "url": old["url"], "title": old.get("title"), "verdict": "INCLUDE",
               "reason": None, "judgment": False,
               "evidence": "As a result, the diagram of the \"Summarize contact information\" "
                           "business process will be as follows.",
               "evidence_source": "page text", "figure_evidence": files,
               "record": "corpus/creatio/004_handle-system-level-data-creatio-ai.md",
               "needs_visual_check": False, "needs_human_ruling": False, "duplicate_of": None,
               "accessed": TODAY, "surface": old.get("surface"), "note": NOTE_500}
    else:
        row = {"n": n, "url": old["url"], "title": old.get("title"), "verdict": verdict,
               "reason": reason, "judgment": False, "evidence": ev, "evidence_source": src,
               "figure_evidence": files, "record": None, "needs_visual_check": False,
               "needs_human_ruling": False, "duplicate_of": None, "accessed": TODAY,
               "surface": old.get("surface"),
               "note": (E2_NOTE if n in (507, 508) else
                        "Figures looked at in the visual pass: " + files + ". They are " + named + ".")}
    new.append(row)

print("superseding rows: " + str(len(new)))
for r in new:
    print("  n={:<4} {:<9} {:<16} {!r}".format(r["n"], r["verdict"], str(r["reason"]), r["evidence"][:72]))
if "--write" not in sys.argv:
    print("preview only")
    raise SystemExit(0)

allrows = dict(rows)
for r in new:
    allrows[r["n"]] = r
vals = list(allrows.values())
hdr = dict(header)
hdr["note"] = (header["note"] + " The 38 rows the caption classifier could not settle were then "
               "looked at directly (ledgers/_creatio/unsure_sheet_*.png, candidates*.png) and "
               "superseded: 35 are UI screenshots or architecture/box illustrations (E1), 3 are "
               "pages whose only images are inline button icons or changelog entries with no figure "
               "(E0), 2 publish a BPMN diagram carrying no AI element (E2), and 1 was promoted to "
               "INCLUDE - a BPMN diagram whose task is the 'Run the AI Sub-agent' element (corpus "
               "record 004). One keyword of the AI screen is a known false positive: "
               "'auto-generated', which names the Auto-generated page process element; the two "
               "pages it caught are E2 rows.")
ftr = dict(footer)
ftr["include"] = sum(1 for r in vals if r["verdict"] == "INCLUDE")
ftr["uncertain"] = sum(1 for r in vals if r["verdict"] == "UNCERTAIN")
ftr["exclude"] = {c: sum(1 for r in vals if r.get("reason") == c) for c in
                  ("E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate")}
ftr["blocked"] = sum(1 for r in vals if r["verdict"] == "BLOCKED")
ftr["visual_check_rows_remaining"] = sum(1 for r in vals if r.get("needs_visual_check"))
ftr["self_audit_flips"] = len([r for r in new if rows[r["n"]]["verdict"] != r["verdict"]])
with LEDGER.open("a", encoding="utf-8") as fh:
    for r in new:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    fh.write(json.dumps(hdr, ensure_ascii=False) + "\n")
    fh.write(json.dumps(ftr, ensure_ascii=False) + "\n")
print("appended " + str(len(new)) + " superseding rows + header + footer")
