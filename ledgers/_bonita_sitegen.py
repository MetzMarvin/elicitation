#!/usr/bin/env python3
"""Generate the marketing-site half of the bonitasoft rulings (worker elicitation-6f).

  python ledgers/_bonita_sitegen.py            # preview: class counts + notes for a sample
  python ledgers/_bonita_sitegen.py --write     # write ledgers/_bonita_site_rulings.py

Every page of www.ofelia.com that the screen sends to judgement (132 of the 254 site pages,
ledgers/_bonita_rows.py `tier()` == "judged") gets exactly one ruling here. The class of each
page - what its figures actually are - comes from the eyeball pass over the source's figures:
the four contact sheets over the 216 raster site figures (ledgers/_bonita/sh_s1..4.png) plus
the targeted zooms of every diagram-shaped or mockup-shaped figure (z_cand, z_ucA-C, z_spot1-5,
z_svg_bcf, z_svg_a/b, z_studio_illu).

The line drawn, applied uniformly to all 132 rows:

  * a figure that shows a process's *structure* - steps plus the control-flow relations between
    them (sequence, branching, roles/lanes), in any notation - is a process artefact worth a
    record (verdict UNCERTAIN, the notation question is the human's);
  * a figure that shows something else process-shaped but without control flow - a product-UI
    screenshot, a chat or dashboard mockup, an architecture box diagram, a lifecycle
    infographic - is E1-not-bpmn, naming what it is;
  * a page with no process artefact at all - photography, logos, CTA banners, icon sets, a
    pricing or legal or listing page - is E0-no-artefact.

`judged` (the 4th field) is the ledger's `judgment` flag: True only where the verdict turned on
what the pixels show, i.e. where the deciding figure's own name, alt text or caption did NOT
settle it (a "care.jpg" or "CTA 1 - EN.png" is settled by its name; "Image Container.svg" or a
"Screenshot 2026-..png" is not). Where the page's prose and figure names settle it the row is
screen-decided, judgment stays False - the same convention as the docs half (_bonita_write.py).
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _bonita_rows as S  # noqa: E402

OUT = ELI / "ledgers" / "_bonita"
TARGET = ELI / "ledgers" / "_bonita_site_rulings.py"

# suffix | CODE | judged | what the figure is (used verbatim in the note; empty for E0)
MAP = """
| E0 | 0 |
/blog-article/3-key-benefits-of-building-process-automation-applications-in-house-75613 | E0 | 0 |
/blog-article/a-year-aboard-the-bonita-express-a-recap-of-our-journey-20266 | E0 | 0 |
/blog-article/accounts-payable-automation-invoice-payment-bonita-work-hub | E0 | 0 |
/blog-article/afd-chooses-bonita-to-transform-and-optimize-its-operational-processes-4cda8 | E0 | 0 |
/blog-article/ai-act-when-regulation-drives-of-responsible-innovation-26bf6 | E0 | 0 |
/blog-article/all-aboard-the-bonita-express-1f7be | E0 | 0 |
/blog-article/beyond-off-the-shelf-why-and-how-process-automation-customization-can-make-a-critical-difference-ac111 | E0 | 0 |
/blog-article/bonita-2023-1-and-self-contained-applications-are-here-60886 | E1 | 0 | release call-to-action banners plus a Bonita Central product screenshot (an application-health dashboard of app tiles, not a diagram)
/blog-article/bonita-2023-2-and-the-new-bonita-test-toolkit-are-here-8eb09 | E2 | 1 | BPMN 2.0
/blog-article/bonita-community-edition-or-bonita-enterprise-edition-1b16d | E0 | 0 |
/blog-article/bonita-process-automation-software-in-forrester-dpa-wave-q4-2023-112d1 | E0 | 0 |
/blog-article/bonita-rated-again-as-top-performer-in-business-process-management-bpm-software-96baf | E0 | 0 |
/blog-article/bonitasoft-and-luminess-formalize-technological-partnership-a2caf | E0 | 0 |
/blog-article/bonitasoft-announces-the-appointment-of-its-new-ceo-christophe-bouron-d1f23 | E0 | 0 |
/blog-article/bonitasoft-earns-trustradius-top-rated-2023-award-db651 | E0 | 0 |
/blog-article/bonitasoft-introduces-self-contained-applications-for-composable-business-process-automation-67355 | E1 | 0 | a Bonita Central product screenshot (an application-health dashboard of app tiles, not a diagram)
/blog-article/bonitasoft-is-positioned-as-technology-leader-in-2023-spark-matrix-for-dpa-software-25bbe | E0 | 0 |
/blog-article/bonitasoft-is-technology-leader-in-ibpms-spark-matrix-for-4th-consecutive-year-6ffa6 | E0 | 0 |
/blog-article/bonitasoft-reinforces-its-cicd-ready-approach-and-introduces-improved-automated-testing-to-accelerate-time-to-market-832e5 | E2 | 1 | BPMN 2.0
/blog-article/bpm-for-future-ready-government-public-sector-4-things-you-need-to-know-74908 | E0 | 0 |
/blog-article/bpm-puts-people-at-the-heart-of-banking-and-financial-services-06e1e | E0 | 0 |
/blog-article/business-process-automation-what-benefits-does-bpm-have-to-offer-the-insurance-industry-305c1 | E0 | 0 |
/blog-article/buy-or-build-process-automation-how-to-make-the-right-choice-80336 | E0 | 0 |
/blog-article/celebrating-excellence-the-bonita-day-mexico-awards-2023-2b926 | E0 | 0 |
/blog-article/claimly-insurance-claims-management-handled-end-to-end-with-bonita-fabric | E0 | 0 |
/blog-article/continuous-performance-monitoring-of-business-processes-the-key-to-efficiency-621fb | E0 | 0 |
/blog-article/deep-visualization-monitoring-added-to-bonita-dpa-platform-ad71f | E0 | 0 |
/blog-article/devops-digest-predictions-for-2023-c4f23 | E0 | 0 |
/blog-article/embracing-the-future-tech-predictions-for-2024-dfd78 | E0 | 0 |
/blog-article/from-chaos-to-clarity-the-power-of-process-modeling-with-bpmn-ac7d9 | E2 | 1 | BPMN 2.0
/blog-article/from-data-to-decisions-the-role-of-ai-in-business-process-automation-a7a19 | RECORD | 1 | promotional banner
/blog-article/how-ai-based-hyperautomation-enriches-traditional-bpm-0cf56 | E0 | 0 |
/blog-article/how-bpm-can-improve-healthcare-processes-and-outcomes-7d5de | E0 | 0 |
/blog-article/how-custom-automation-transforms-complex-workflows-and-unique-information-system-stacks-ffac8 | E0 | 0 |
/blog-article/how-does-ai-challenge-traditional-process-automation-36fc1 | E3 | 1 | promotional banner
/blog-article/how-iberostar-revolutionized-its-process-management-with-bonita-automation-and-sustainability-bdb10 | E0 | 0 |
/blog-article/how-in-house-automation-can-improve-data-security-and-compliance-174da | E0 | 0 |
/blog-article/how-process-automation-accelerates-digital-transformation-in-the-public-sector-f4daf | E0 | 0 |
/blog-article/how-process-automation-supports-regulated-sectors-to-ensure-compliance-and-risk-management-bbb86 | E0 | 0 |
/blog-article/intelligent-cio-get-to-know-the-new-ceo-of-bonitasoft-83909 | E0 | 0 |
/blog-article/it-modernization-2021-part-2-4-steps-to-get-the-job-done-1d219 | E0 | 0 |
/blog-article/low-code-automation-for-developers-definition-advantages-examples-dc50b | E0 | 0 |
/blog-article/mastering-gdpr-compliance-with-process-automation-10017 | E0 | 0 |
/blog-article/mastering-process-automation-keys-to-success-and-best-practices-7f260 | E0 | 0 |
/blog-article/meet-the-bonita-ui-builder-faster-better-ui-design-for-bonita-application-developers-39b71 | E1 | 1 | UI Builder editor screenshots (a widget palette and a "Choose a template" dialog)
/blog-article/modern-uis-deeper-insights-redefining-business-efficiency-with-bonita-4ef2f | E1 | 1 | four Bonita Process Insights dashboard screenshots (Process Explorer, Operational Task Monitoring, Application Overview, User Activity Insights)
/blog-article/new-process-podcast-rethinking-processes-with-charles-souillard-4c7e1 | E0 | 0 |
/blog-article/ofelia-orchestrer-agents-ia-eti-lesechos | E0 | 0 |
/blog-article/open-source-software-definition-and-advantages-8a8ab | E0 | 0 |
/blog-article/operational-efficiency-its-more-than-just-automation-e2f7b | E1 | 1 | two Bonita Process Insights dashboard screenshots (a Process Overview dashboard and a Process Compare dashboard)
/blog-article/optimizing-operational-efficiency-with-bpm-some-key-concepts-75a72 | E1 | 1 | marketing infographics (a two-column "BPM vs workflow" comparison table and a modelling/execution/optimisation/monitoring wheel) with "PROCESS" at the centre
/blog-article/process-automation-with-bpm-7-key-advantages-and-benefits-30f34 | E0 | 0 |
/blog-article/process-intelligence-is-key-to-process-automation-heres-why-ef4d7 | E1 | 1 | a marketing infographic (a circular "BPM + Process Intelligence" lifecycle of Conception, Optimization, Analysis, Automation, Modelization)
/blog-article/process-intelligence-with-process-automation-1e300 | E1 | 1 | a Bonita Process Insights dashboard screenshot (a Process Overview dashboard)
/blog-article/revolutionizing-talent-acquisition-with-bpm-3d6ce | E0 | 0 |
/blog-article/self-contained-apps-in-bpm-improve-agility-and-competitiveness | E0 | 0 |
/blog-article/shamil-hassanaly-appointed-chief-operating-officer-of-bonitasoft-ca778 | E0 | 0 |
/blog-article/streamlining-business-processes-the-power-of-bpm-in-overcoming-integration-challenges | E0 | 0 |
/blog-article/the-5-essential-steps-of-implementing-a-bpm-approach-938a0 | E0 | 0 |
/blog-article/the-legendre-group-accelerates-its-digital-transformation-with-bonitasoft-f9b22 | E0 | 0 |
/blog-article/the-new-version-of-bonita-is-here | E0 | 0 |
/blog-article/the-power-of-automated-kyc-transforming-banking-and-insurance-e0c48 | RECORD | 1 | BPMN 2.0
/blog-article/top-eight-benefits-of-self-contained-apps-for-bpm-based-process-automation | E0 | 0 |
/blog-article/trends-in-it-ai-business-process-analysis-and-sustainability | E0 | 0 |
/blog-article/unleash-the-power-of-bpm-master-end-to-end-process-orchestration-e4077 | E1 | 1 | an "Everest Group - Process Orchestration Solution: Key Components" architecture box diagram, a product-UI illustration with flow-shaped nodes and a robot mascot illustration
/blog-article/unlocking-business-insights-leveraging-process-data-for-performance-optimization | E1 | 1 | Bonita Process Insights dashboard screenshots (a process-selection list and overview / compare dashboards) plus a two-piece puzzle graphic
/blog-article/vmblog-interviews-charles-souillard-innovation-self-contained-apps | E0 | 1 | a 133x132 author portrait (the "..._pp.webp" file)
/blog-article/what-does-the-future-of-business-process-automation-look-like | E0 | 1 | two 700x200 call-to-action banners ("What's coming in the world of business process automation?" and "What's ahead for business processes? Lighter applications") and the same author portrait
/blog-article/what-is-hyperautomation-4be39 | E3 | 1 | promotional banner
/blog-category/bonita-bonitasoft | E0 | 0 |
/blog-category/bpm-automation | E0 | 0 |
/blog-category/tech-trends | E0 | 0 |
/bonita-fabric | E1 | 1 | an architecture box diagram (Ofelia Agentic / Bonita BPM / Bonita Fabric / Bonita Work Hub over an Execution Engine and a BPA Engine "Core Orchestrator")
/bonita-work-hub | E0 | 0 |
/compare | E0 | 0 |
/compare-bonita-bpm/bonita-bpm | E0 | 0 |
/compare-ofelia-agentic/microsoft-copilot | E0 | 0 |
/demo | E0 | 1 |
/downloads | RECORD | 1 | Bonita Studio mockup
/event/ai-powered-automation-future-of-workflows | E0 | 0 |
/event/compliance-by-design | E0 | 0 |
/event/hands-on-building-your-first-agent | E0 | 0 |
/event/investigation-bancaire-augmentee-replay | E0 | 0 |
/event/ofelia-live-product-deep-dive | E0 | 0 |
/event/scaling-governance-across-teams | E0 | 0 |
/glossary | E0 | 0 |
/ofelia-assistant | RECORD | 1 | workflow card
/ofelia-by-departments | E0 | 0 |
/ofelia-workflow | E1 | 1 | Ofelia Agent chat-UI mockups (a message thread with a checklist and an "Approve" button on a "Manager Approval Required - Step 3 of 3" card)
/operations-and-sales | E0 | 0 |
/partners | E0 | 0 |
/partners/corus | E0 | 0 |
/partners/grain-strategy | E0 | 0 |
/partners/keinavo | E0 | 0 |
/partners/konsultex-informatica | E0 | 0 |
/partners/smartwave | E0 | 0 |
/partners/sqli | E0 | 0 |
/partners/t-impact | E0 | 0 |
/partners/tecnologias-plexus | E0 | 0 |
/partners/wave-informatica | E0 | 0 |
/personal-data-processing-agreement | E0 | 0 |
/personal-data-protection-policy | E0 | 0 |
/pricing | E0 | 0 |
/product/bonita-bpm | E0 | 1 |
/product/it-hub | RECORD | 1 | architecture diagram
/product/ofelia-agentic | E1 | 0 | product-UI mockup cards (Ofelia "Ask", "Act" and "Scale" containers)
/professional-services | E0 | 0 |
/success-story/alliance-healthcare | E0 | 1 |
/success-story/cafat | E0 | 1 |
/success-story/icade | E0 | 1 |
/success-story/mif-customer-story | E0 | 1 |
/success-story/multiasistencia | E0 | 1 |
/success-story/odu | E0 | 1 |
/success-story/premiere-digital-services | E0 | 1 |
/success-story/softwarecompany | E0 | 1 |
/success-story/tempo-assist | E0 | 1 |
/success-story/trane-technologies | E0 | 1 |
/success-story/university-queensland | E0 | 1 |
/success-story/vis-insurance-ltd | E0 | 1 |
/success-story/voo | E0 | 1 |
/use-case-bonita-automated-inventory-management | E0 | 1 |
/use-case-bonita-automated-loan-processing | E0 | 1 |
/use-case-bonita-care-management | E0 | 1 |
/use-case-bonita-clinical-workflow-automation | E0 | 1 |
/use-case-bonita-compliance-automation | E0 | 1 |
/use-case-bonita-employee-onboarding-automation | E1 | 1 | chat-UI mockups (an Ofelia agent card, a task-status checklist and a Slack thread carrying a numbered four-step onboarding list)
/use-case-bonita-it-process-automation | E0 | 1 |
/use-case-bonita-kyc-automation | E0 | 1 |
/use-case-bonita-risk-management-automation | E0 | 1 |
/use-case-bonita-student-enrollment-management | E0 | 1 |
/use-case-bonita-supply-chain-automation | E0 | 1 |
"""

# --- the record pages ------------------------------------------------------------------------
# The artefacts with real process structure, and the one promotional claim worth a human
# ruling. Captures live in corpus/bonitasoft/ (012-016), records are written beside them.
STUDIO_Q = ("The figure is a Bonita Studio illustration with an AI Assistant panel: does a "
            "design-time assistant panel inside a Studio mockup count as an AI element *in a "
            "process*, or is it design-time AI (E2)?")
RUNTIME_Q = ("The figure is a boxes-and-arrows agent-runtime diagram, not BPMN 2.0, but it "
             "does show an AI agent sequence with control flow: is such a proprietary agent "
             "diagram inside the artefact criteria (BPMN 2.0 only), or a find in its own right?")
WORKFLOW_Q = ("The figure is Ofelia's own workflow view (a stack of step cards with a branch), "
              "not BPMN 2.0: does a vendor's proprietary workflow depiction count as a "
              "process artefact for the census, or is it E1-not-bpmn?")
BANNER_Q = ("The page advertises \"Try the BPMN AI generator!\" and shows no diagram at all: "
            "does a marketed AI-generates-BPMN claim fall inside the artefact criteria, or is "
            "it out of scope (no artefact on the page)?")
KYC_Q = ("The page's AI/ML mention describes document comparison inside the KYC process "
         "(authenticity checks on passports) and the bpmn-js diagram draws a \"Verify "
         "identity\" / \"Check background\" task: is that AI element inside the process, i.e. "
         "does this page meet the artefact criteria?")

# --- the three pages that publish a real BPMN 2.0 diagram ------------------------------------
BPMN_DIAGRAM = {
    "bonita-2023-2-and-the-new-bonita-test-toolkit-are-here-8eb09": (
        "a BPMN 2.0 pool with the lanes Team Assistant / Approver / Accountant, the tasks "
        "\"Assign Approver\", \"Approve Invoice\", \"Prepare Bank Transfer\" and \"Archive "
        "Invoice\", the gateways \"Invoice approved?\" and \"Review successful?\" and the end "
        "events \"Invoice processed\" / \"Invoice not processed\"",
        "the page's figure \"Bonita Test Toolkit_2_0.png\" (the invoice-approval process the "
        "Test Toolkit ships as an example)"),
    "bonitasoft-reinforces-its-cicd-ready-approach-and-introduces-improved-automated-testing-to-accelerate-time-to-market-832e5": (
        "a BPMN 2.0 pool with the lanes Team Assistant / Approver / Accountant, the tasks "
        "\"Assign Approver\", \"Approve Invoice\", \"Prepare Bank Transfer\" and \"Archive "
        "Invoice\", the gateways \"Invoice approved?\" and \"Review successful?\" and the end "
        "events \"Invoice processed\" / \"Invoice not processed\"",
        "the page's figure \"Bonita Test Toolkit_2_0_0.png\", the 600x296 copy of the "
        "invoice-approval diagram"),
    "from-chaos-to-clarity-the-power-of-process-modeling-with-bpmn-ac7d9": (
        "a BPMN 2.0 pool with the lanes Human Resources / New employee, the tasks \"New hire\", "
        "\"Prepare contract\", \"Update contract\", \"Registration in other apps\", \"Prepare "
        "first week\", \"Set up work station\" and \"Email sign-in details\", the gateways "
        "\"Contract ready for review?\", \"Is contract signed?\" and \"Split preparation "
        "steps\", end events, and the annotation \"Triggered by another process\"",
        "the page's figure \"image (56)\" (a new-employee onboarding process)"),
}

BANNER = ["/blog-article/from-data-to-decisions-the-role-of-ai-in-business-process-automation-a7a19",
          "/blog-article/how-does-ai-challenge-traditional-process-automation-36fc1",
          "/blog-article/what-is-hyperautomation-4be39"]

RECORDS = {
    "/blog-article/the-power-of-automated-kyc-transforming-banking-and-insurance-e0c48": (
        "012_kyc-bpmn-diagram", "BPMN 2.0, rendered by bpmn-js",
        "the page's own BPMN 2.0 diagram (diagram KYC.svg)",
        "The page publishes a BPMN 2.0 diagram: the figure \"diagram KYC.svg\" opens with the "
        "tool provenance comment \"<!-- created with bpmn-js / http://bpmn.io -->\" (the only "
        "one of the 202 site SVGs that does) and its 2492x270 canvas carries the labelled "
        "sequence \"Customer onboarding request pending | Collect customer information | Verify "
        "identity | Perform standard due diligence | Check background | Integrate data | Approve "
        "final data | Create account | Customer successfully onboarded\" plus the branch "
        "\"Perform enhanced due diligence | Review data\". The page's AI mention puts AI/ML "
        "document comparison inside that scrutiny (\"Artificial intelligence (AI) and machine "
        "learning tools can analyze customer data and compare submitted documents - such as "
        "passports or driver's licenses - against official databases to confirm their "
        "authenticity\"), which is what makes this a ruling for the researcher rather than a "
        "clean exclusion.",
        KYC_Q,
        "diagram KYC.svg looked at in full at 2492x270, and the page's own prose read for its "
        "AI mention"),
    "/downloads": (
        "013_bonita-studio-ai-assistant-illu", "a Figma-drawn product mockup, texts as paths",
        "the Bonita Studio illustration with its AI Assistant panel (Bonita_studio_illu.svg)",
        "The page's figure \"Bonita_studio_illu.svg\" is a Bonita Studio mockup (a Figma export: "
        "every text is drawn as a path, no <text> node survives, and the file carries no "
        "bpmn-js provenance). Inside it: a \"Risk Assessment Lane\" (start -> Verify -> Review) "
        "and a \"Compliance Lane\" (Check -> end) beside an \"AI Assistant\" panel whose cards "
        "read \"Process Suggestion - Add parallel gateway for faster review\", \"Risk Analysis - "
        "Bottleneck detected at approval step\", \"Compliance Check - GDPR compliant, SOC 2 "
        "ready\" and \"Action Required - Review timeout configuration\". The lanes are drawn, "
        "but the notation is the vendor's own mockup, not BPMN 2.0 - and the AI sits in the "
        "design-time assistant, not in a process element.",
        STUDIO_Q,
        "Bonita_studio_illu.svg looked at in full (472x376) and its own prose read"),
    "/ofelia-assistant": (
        "014_ofelia-workflow-card", "a proprietary workflow view (step cards with a branch)",
        "the \"Ofelia Workflow\" card (Ofelia_workflow.svg)",
        "The page's figure \"Ofelia_workflow.svg\" shows Ofelia's own workflow view: a dark card "
        "headed \"Ofelia Workflow\" with a green \"Published\" badge, and the drawn sequence "
        "\"Employee request\" -> \"Manager approval\" -> a branch into \"Finance review\" and "
        "\"Auto-approved\" -> \"Complete & notify\". It is a process depiction with named steps "
        "and real control flow (a branch and a merge), but in the vendor's proprietary card "
        "notation: no pools, lanes, events, gateways or sequence flows.",
        WORKFLOW_Q,
        "Ofelia_workflow.svg looked at in full (440x313) alongside the page's other figures "
        "(Visuel.svg: an Ofelia Agent chat mockup)"),
    "/product/it-hub": (
        "015_ofelia-agent-runtime-diagram", "a boxes-and-arrows architecture diagram",
        "the Ofelia agent-runtime diagram (Frame 2147263655.svg)",
        "The page's figure \"Frame 2147263655.svg\" is a boxes-and-arrows diagram of the Ofelia "
        "agent runtime, and the boxes are AI agents: \"User message (Slack / Teams)\" -> \"Tool "
        "Mapping Agent (Intent classifier)\" -> \"User confirms action\" -> \"Action Agent "
        "(Exec. procedures)\", \"Answerer Agent (RAG responses)\", \"Out-of-scope (Graceful "
        "decline)\", \"Action Result (Feedback format)\", with a \"Knowledge Retrieval System\" "
        "(Vector Search / Knowledge Graph / Key-value Lookup), \"Deterministic Execution -> BPA "
        "Engine Handoff\", \"Action execution (API calls under user token)\", \"Workflow "
        "Orchestration (BPMN sequencing & SLA)\" and \"Grounded Response\". It names BPMN inside "
        "one of its boxes, but the drawing itself is an architecture diagram, not a BPMN 2.0 "
        "model. The page's other figures are a layered architecture stack (dev-engine_visual) "
        "and a nested security stack (Image Container).",
        RUNTIME_Q,
        "Frame 2147263655.svg looked at in full (774x443), with dev-engine_visual.svg and "
        "Image Container.svg"),
    "/blog-article/from-data-to-decisions-the-role-of-ai-in-business-process-automation-a7a19": (
        "016_ai-bpmn-generator-promo", "a promotional banner (no diagram of any kind)",
        "the \"Transform your business processes into a BPMN model with AI\" banner "
        "(Text to BPMN EN.png)",
        "The page's only figure is a promotional banner: it reads \"Transform your business "
        "processes into a BPMN model with AI\" over a speech-bubble graphic and carries the call "
        "to action \"Try the BPMN AI generator!\". No diagram of any kind is shown - this is the "
        "vendor advertising that an AI generates BPMN, which is design-time AI and the same "
        "pattern the thesis already tracks (notes/uipath-promotion-pattern/analysis.md), not an "
        "AI element in a process. The page's article text is prose about AI in BPA. The same "
        "banner is republished by two further blog articles "
        "(how-does-ai-challenge-traditional-process-automation-36fc1 and "
        "what-is-hyperautomation-4be39), which are ruled E3 against this row.",
        BANNER_Q,
        "Text to BPMN EN.png looked at in full (700x200) and the page's own prose read"),
}

E0_SITE = (
    "No process artefact on the page: the screen finds no BPMN marker, no .bpmn/.proc link and "
    "no figure whose name, alt text or caption names a diagram, and the eyeball pass over the "
    "source's figures agrees - %s. The token that put the page on the judgement worklist is not "
    "an AI element inside a process either: \"%s\". Nothing to collect."
)
E1_SITE = (
    "The page's only process-shaped figure is not BPMN 2.0: it is %s. There are no pools, "
    "lanes, events, gateways or sequence flows drawn in it and nothing in it is a process "
    "element; the whole AI-connector vocabulary of the docs portal is absent from the marketing "
    "site. Figures looked at: %s. The page's own AI token, \"%s\", is site chrome - the "
    "footer's demo call-to-action - not a process element."
)
E2_SITE = (
    "The page publishes a real BPMN 2.0 diagram - %s. It carries no AI/LLM element inside the "
    "process: every activity drawn is a human task, and the page's only AI mention is the "
    "site-wide footer call-to-action \"%s\" (quoted here because the exclusion rests on "
    "dismissing it: it advertises Ofelia, it is not an element of this process). Figures looked "
    "at: %s."
)
E3_SITE = (
    "Not a second artefact: this page republishes the identical image already recorded under "
    "%s - the same %s. Both pages serve it from the identical Webflow asset (%s, published at "
    "the same 700x200 pixels), so this is one picture on two pages, not two artefacts. Quoted "
    "from this page: \"%s\"."
)


def parse_map():
    out = {}
    for line in MAP.strip().splitlines():
        parts = [p.strip() for p in line.split("|")]
        if not parts[0] and len(parts) < 3:
            continue
        out[parts[0] or "/"] = (parts[1], parts[2] == "1", parts[3] if len(parts) > 3 else "")
    return out


def quote(text, width=25):
    """A <=25-word verbatim window starting at the sentence holding the page's first AI token."""
    t = " ".join(text.split())
    m = S.AI.search(t)
    if not m:
        return " ".join(t.split()[:width])
    start = max(t.rfind(". ", 0, m.start()), t.rfind("! ", 0, m.start()),
                t.rfind("? ", 0, m.start()))
    seg = t[start + 2:] if start >= 0 else t
    return " ".join(seg.split()[:width])


def dec_names(sc):
    """The page's figure file names, url-decoded and with the asset-id prefix stripped."""
    import urllib.parse
    out = []
    for f in sc["figures"]:
        n = f or ""
        for _ in range(4):  # Webflow stores asset names url-encoded up to three times over
            d = urllib.parse.unquote(n)
            if d == n:
                break
            n = d
        out.append(re.sub(r"^(?:[0-9a-f]{20,}_)+", "", n))
    return out


def figs_of(sc, limit=5):
    names = [n for n in dec_names(sc)
             if n and not re.search(r"placeholder|BG_texture|grad-lat|_black|_white", n)]
    return ", ".join(names[:limit]) + (" ..." if len(names) > limit else "")


def site_pages():
    """[(url, suffix, sc)] for the judged site pages, in population order."""
    pop = json.loads((OUT / "population.json").read_text(encoding="utf-8"))
    idx = json.loads((OUT / "index.json").read_text(encoding="utf-8"))
    out = []
    pages_dir = OUT / "pages"
    for u in pop["site_urls"]:
        rec = idx.get(u)
        if not rec or rec.get("status") != 200 or not rec.get("file"):
            continue
        if not (pages_dir / rec["file"]).exists():
            continue
        sc = S.screen(u, S.html_of(rec))
        if S.tier(u, sc) == "judged":
            out.append((u, u.replace("https://www.ofelia.com", "") or "/", sc))
    return out


def build():
    cls = parse_map()
    pages = site_pages()
    seen = [s for _, s, _ in pages]
    missing = [s for s in seen if s not in cls]
    extra = [s for s in cls if s not in seen]
    if missing or extra:
        raise SystemExit("map/ledger mismatch:\n  missing=%s\n  extra=%s" % (missing, extra))
    first_banner = next(s for s in seen if s in BANNER)
    rulings, dups = {}, {}
    for url, suffix, sc in pages:
        code, judged, kind = cls[suffix]
        q = quote(sc["text"])
        looked = figs_of(sc) or "the page carries no figure at all"
        stem = question = notation = artefacts = None
        if code == "E0":
            verdict, reason = "EXCLUDE", "E0-no-artefact"
            looked = (looked if not kind else "%s; the figures are %s" % (looked, kind))
            note = E0_SITE % (looked, q)
        elif code == "E1":
            verdict, reason = "EXCLUDE", "E1-not-bpmn"
            notation = artefacts = kind or "a marketing illustration"
            note = E1_SITE % (notation, looked, q)
        elif code == "E2":
            verdict, reason = "EXCLUDE", "E2-no-ai-element"
            diagram, looked = BPMN_DIAGRAM[suffix.rsplit("/", 1)[-1]]
            notation = "BPMN 2.0"
            artefacts = "BPMN diagram: %s" % diagram
            note = E2_SITE % (diagram, q, looked)
        elif code == "E3":
            verdict, reason = "EXCLUDE", "E3-duplicate"
            notation = artefacts = kind or "promotional banner"
            asset = next((n for n in dec_names(sc) if "BPMN" in n or "banner" in n.lower()),
                         kind or "the banner")
            dups[url] = "https://www.ofelia.com" + first_banner
            note = E3_SITE % ("https://www.ofelia.com" + first_banner, notation, asset, q)
        elif code == "RECORD":
            verdict, reason = "UNCERTAIN", None
            stem, notation, artefacts, note, question, looked = RECORDS[suffix]
        else:
            raise SystemExit("bad code %s for %s" % (code, suffix))
        rulings[url] = (verdict, reason, notation, artefacts, looked, note, stem, question,
                        q, judged)
    return rulings, dups, pages


def emit(rulings, dups):
    lines = ['"""Generated by ledgers/_bonita_sitegen.py - do not edit by hand.',
             '',
             'The 132 judged pages of www.ofelia.com: their class (from the eyeball pass over the',
             'source\'s figures), their note, and the five records the site half of the census',
             'writes. See _bonita_sitegen.py for the line that was drawn and the convention behind',
             'the `judgment` field.',
             '"""',
             '',
             'SITE_RULINGS = {']
    for url, t in sorted(rulings.items()):
        lines.append("  %r: %r," % (url, t))
    lines.append("}")
    lines.append("")
    lines.append("SITE_DUPLICATE_OF = {")
    for url, d in sorted(dups.items()):
        lines.append("  %r: %r," % (url, d))
    lines.append("}")
    lines.append("")
    lines.append("SITE_RECORDS_WRITTEN = [")
    for stem in sorted({t[6] for t in rulings.values() if t[6]}):
        lines.append("  %r," % stem)
    lines.append("]")
    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote %s (%d rulings, %d duplicates)" % (TARGET.name, len(rulings), len(dups)))


if __name__ == "__main__":
    r, d, pages = build()
    from collections import Counter
    codes = Counter((t[0], t[1]) for t in r.values())
    print("judged site pages %d" % len(pages))
    for k, v in sorted(codes.items(), key=lambda kv: -kv[1]):
        print("   %-10s %-16s %d" % (k[0], k[1] or "-", v))
    print("judgment=True rows: %d" % sum(1 for t in r.values() if t[9]))
    print("records: %s" % ", ".join(sorted(t[6] for t in r.values() if t[6])))
    if "--write" in sys.argv:
        emit(r, d)
    else:
        for url in list(r)[:2] + list(r)[-3:]:
            print("\n--- %s\n%s" % (url, r[url][5]))
