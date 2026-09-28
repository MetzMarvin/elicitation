#!/usr/bin/env python3
"""Restate fifteen rulings of the bonitasoft ledger in the full tuple shape (worker
elicitation-6f).

The ruling tuple is

    (verdict, reason, notation, artefacts_on_page, figures_looked_at, note,
     record_stem, question, evidence, judgment)

Fifteen rows in `_bonita_write.py` were written one argument short, so their trailing `judgment`
flag landed in the `evidence` slot: the ledger would have carried `evidence: true` for them and
an empty `note`, and their judgment would have defaulted to False. Nothing about the verdicts was
wrong - all fifteen are E2 or E1 exclusions resting on what the figure is - but the ledger's
evidence field is the thing a reviewer audits, so the rows are restated here in the full shape:

  * `evidence` is left None on purpose: the build fills it with the page's own quoted text
    (`ledgers/_bonita_build.ruling_row`), which is what the evidence rule asks for.
  * `note` names the notation and states the page's AI status - for all fifteen the AI screen
    does not fire on the page's content region at all, so there is no AI mention to dismiss and
    the note says so rather than implying one.
  * `judgment` keeps the value the original call intended.

Called at the end of `_bonita_write.py` via `apply(RULINGS, D)`.
"""
E2_NOTE = (
    "The page's diagram is BPMN 2.0 (%s) and the page's own text is about %s. Every activity on "
    "the canvas is a human task or a plain gateway, no service task carries a connector, and the "
    "page carries no AI mention at all - the AI screen does not fire on its content region. The "
    "dismissal is E2: the artefact is BPMN but contains no AI element inside the process."
)

# url suffix -> (note, judgment)
E2_ROWS = {
    "/bonita/latest/getting-started/declare-business-variables": (
        E2_NOTE % ("select-process-pool.gif, declare-business-variable.gif, define-condition.gif",
                   "configuring process variables and a condition"), True),
    "/bonita/latest/getting-started/declare-contracts": (
        E2_NOTE % ("contract-MVC.PNG, declare-process-instantiation-contract.gif, "
                   "declare-user-task-contract.gif, operation.png",
                   "declaring process and user-task contracts"), True),
    "/bonita/latest/getting-started/draw-bpmn-diagram": (
        E2_NOTE % ("new-default-diagram.png, switch-from-parallel-to-exclusive-gateway.png, "
                   "process-diagram-before-transitions-configured.png and the rest of its 13 "
                   "figures", "drawing a pool, tasks and gateways in Bonita Studio"), True),
    "/bonita/latest/pages-and-forms/manage-control-in-forms": (
        E2_NOTE % ("leave_request_management_process.png plus the Studio form screenshots",
                   "how form controls are shown to the user who claims a leave request"), True),
    "/bonita/latest/process/diagram-tasks": (
        E2_NOTE % ("leave_request_management_process_tasklist.png plus tasklist screenshots",
                   "how a task is shown on the task list"), True),
    "/bonita/latest/process/optimize-user-tasklist": (
        E2_NOTE % ("leave_request_management_process_tasklist.png plus tasklist screenshots",
                   "configuring the task list"), True),
    "/bonita/latest/process/gateways": (
        E2_NOTE % ("papde_pm_diag_gateways_parallel_gate.png, "
                   "papde_pm_diag_gateways_exclusive_gate.png and "
                   "papde_pm_diag_gateways_inclusive_gate.png",
                   "the three gateway types and their merge/divergence behaviour"), True),
    "/bonita/latest/process/web-service-connector-overview": (
        E2_NOTE % ("webservice_diagram.png",
                   "a tutorial process whose activity is bound to the SOAP web service "
                   "connector, not to an AI connector"), True),
    "/bonita/latest/process/web-service-tutorial": (
        E2_NOTE % ("webservice_diagram.png",
                   "the same tutorial process and its SOAP web service connector"), True),
    "/bonita/latest/runtime/user-process-list": (
        E2_NOTE % ("Actor-mapping.png, Set-as-initiator.png, user_process_list.png",
                   "who can start a process and the end-user process list"), True),
}

# the five notation exclusions: written with the "looked at" text in the artefacts slot and the
# intended note in the looked slot. (artefacts, note, judgment); `looked` is taken from the row.
E1_ROWS = {
    "/labs/latest/bici/architecture": (
        "bici_architecture.png (alt \"Bonita Intelligent Continuous Improvement Add-on "
        "Architecture\")",
        "The page's only artefact is a deployment architecture diagram (bici_architecture.png, "
        "910x551): boxes for the Bonita Database, the BICI connection pool, Elasticsearch and the "
        "two Living Applications, joined by arrows - components and data flow, not a process "
        "model. Quoted from the page: \"Bonita Intelligent Continuous Improvement (BICI) extracts "
        "data of the Bonita Database, transforms it, and stores documents in an Elasticsearch "
        "storage engine.\" The page carries no AI mention at all, so the dismissal rests on the "
        "notation.", False),
    "/bcd/latest/": (
        "bcd_capabilities.png (alt \"Bonita Continuous Delivery Capabilities\")",
        "The page's only figure is a deployment-pipeline diagram (bcd_capabilities.png, "
        "1004x503): a Living App repository cylinder, then Checkout Repository -> Build Living App "
        "-> Deploy Living App -> Test Living App under a Bonita Platform box. Boxes and arrows for "
        "build stages are not BPMN 2.0 - no pools, lanes, events, gateways or sequence flows. "
        "Quoted from the page: \"we are moving to a new deployment mode that no longer relies on "
        "the \\\"BCD\\\" mechanism as you know it\". The page carries no AI mention.", True),
    "/bonita/latest/bonita-overview/project-structure": (
        "bonita-project-elements.png (alt \"bonita project elements\")",
        "The page's only figure is a radial concept map (bonita-project-elements.png, 665x491): "
        "one grey \"Bonita Automation Project\" circle with Processes, Data, Identity Management, "
        "Extensions and Living Applications around it - an overview graphic with no events, tasks, "
        "gateways or sequence flows. The word BPMN appears only in a table that describes the "
        "elements of a project - quoted: \"Diagrams BPMN diagram that describes your business "
        "processes\" - naming the notation without publishing a diagram in it. The page carries no "
        "AI mention.", True),
    "/bonita/latest/data/data-management": (
        "uid_data_management_wizard.png, uid_data_model_panel.png, uid_graphql_voyager.png "
        "(alt \"graphql_voyager\")",
        "The page's diagram is a data-model graph and the page itself names the notation: \"we are "
        "using the graphql-voyager tool, which represents a GraphQL\" ... \"A graphical view of "
        "the relationships between business objects (with their attributes) is displayed in a new "
        "tab of your browser.\" uid_graphql_voyager.png (1000x688) is that Voyager window - a Type "
        "list and linked type boxes (com_company_model_ExpenseReport, ...Line, ...LineQuery). A "
        "GraphQL schema graph is not BPMN 2.0. The page carries no AI mention.", False),
    "/ui-builder/latest/git/resolve-merge-conflicts": (
        "seperate-conflicts-git.png (alt \"seperate conflicts git\"), remote-conflicts.png "
        "(alt \"remote conflicts\")",
        "The page's figures are version-control diagrams: seperate-conflicts-git.png (1326x458) "
        "draws a Staging branch and a Feature branch as chains of commits converging on a \"Merge "
        "Conflict\" marker, and remote-conflicts.png draws remote and local branch boxes with two "
        "developers. Commit chains and branch lines are not BPMN 2.0. Quoted from the page: "
        "\"Resolving these conflicts is necessary to merge branches successfully.\" The page "
        "carries no AI mention.", True),
}


def apply(rulings, D):
    """Restate every short-shaped ruling in the full 10-tuple shape. Returns the count."""
    fixed = 0
    for suffix in list(E2_ROWS) + list(E1_ROWS):
        url = D + suffix
        t = list(rulings[url])
        assert len(t) == 9 and isinstance(t[8], bool), "already reshaped: %s" % url
        verdict, reason, notation, artefacts, looked = t[:5]
        if suffix in E1_ROWS:
            artefacts, note, judgment = E1_ROWS[suffix]
            looked = t[3]
        else:
            note, judgment = E2_ROWS[suffix]
        rulings[url] = (verdict, reason, notation, artefacts, looked, note,
                        None, None, None, judgment)
        fixed += 1
    return fixed
