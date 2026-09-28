#!/usr/bin/env python3
"""Write the marketplace rows into the creatio ledger (surface: marketplace / marketplace-blog).

Two phases, each one leaving the ledger self-consistent (population_size == rows == frontier lines):

  --phase1 : the items whose page carries NO process-model language anywhere. Judged mechanically from
             the cached page (judged_from: marketplace-cache): the item publishes no process artefact,
             so E0-no-artefact, with the listing's own first descriptive sentence as the verbatim
             evidence. No figure on such a page is presented as a process model - which is what the
             eye pass over the candidates confirmed for the sections they sit in.
  --phase2 : the items whose page DOES mention a process model (or carries the "Business Process
             Element" / "AI Workflow" tag). Every one of these had its figures looked at, figure by
             figure, and the verdicts come from the tables below, which are filled in from that pass.

  python ledgers/_creatio_mp_write.py --phase1 [--write]
  python ledgers/_creatio_mp_write.py --phase2 [--write]

WHAT THE EYE PASS SAW (phase 2), in one paragraph: every non-chrome figure of the 143 candidates was
tiled into contact sheets (ledgers/_creatio_mp_sheets.py, 883 figures at 56/sheet) and read; the 46
figures that sheet's noise filter had dropped were tiled separately and read too
(ledgers/_creatio_mp_noise_sheet.py - they are marketing cards and product banners, no diagram). The
figures that ARE process models are in E2 below: 22 listings publishing a Creatio process-designer
model. The rest are the app's own product screenshots and the vendor's marketing cards, with a handful
of named non-BPMN artefacts (SPECIAL below).
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
LEDGER = ELI / "ledgers" / "creatio.jsonl"
FRONTIER = ELI / "ledgers" / "creatio.frontier.txt"
TODAY = "2026-09-24"
BASE = "https://marketplace.creatio.com"

sys.path.insert(0, str(ELI / "ledgers"))
import _creatio_mp_rows as M  # noqa: E402

# ---------------------------------------------------------------------------------------------------
# The notation, as it is recognisable on this surface. Two designers look superficially alike and are
# NOT the same thing, so the note names the tells that separate them:
#   * the process designer (BPMN 2.0)  - event CIRCLES, gateway DIAMONDS with Yes/No labels, rounded
#     tasks with element icons, and a SAVE / RUN / CANCEL / ACTIONS toolbar with a ZOOM bar;
#   * the campaign designer (proprietary) - square step TILES with round icon badges, dotted
#     connectors, an "Exit from campaign" tile, no events and no gateways, and a SAVE / CANCEL toolbar
#     (no RUN, no ACTIONS).
# ---------------------------------------------------------------------------------------------------
BPMN = ("BPMN 2.0 in Creatio's process designer: event circles (the terminate drawn as a red-bordered "
        "circle with a filled dot), gateway diamonds carrying Yes/No flow labels, tasks drawn as "
        "rounded rectangles with element icons, and the SAVE/RUN/CANCEL/ACTIONS toolbar with its ZOOM "
        "bar and left element palette.")
NO_AI = ("No AI/LLM element sits inside that model, and no AI/LLM token occurs anywhere on the page - "
         "not in its body text, not in any image alt text and not in any image file name - so there is "
         "no AI claim on the page to weigh.")

# link -> (the figures that were looked at, what the published process model contains)
E2 = {
    "/app/upsale": (
        "upsale.png",
        "an orange gateway diamond with Yes/no flow labels between the tasks 'Find upsale products' and "
        "'Offer upsale products to client', a plain start circle, 'Increase upsale product's rating' on "
        "a second path, and two red-bordered terminate end events"),
    "/app/twilio-sms-pro-integration-creatio": (
        "KF_4.png (under the listing's own 'Automated bulk messaging workflows' heading)",
        "a 'Timer December 31' start event, the tasks 'Create a greeting mascCabo' and 'Filling out the "
        "list of participants', an orange 'Send a message 1' task and a red-bordered terminate end event"),
    "/app/twilio-sms-connector-creatio": (
        "BusinessProcess_0.png; ContactCard_0.png; SystemSettings_0.png",
        "'Send SMS through Twilio': a start event, a 'Send SMS' task and a terminate end event"),
    "/app/email-approvals-creatio": (
        "Process.png; Approval.png; Email.png; Template.png",
        "'Send email approval for order': a start event, the approval user task and a terminate end event"),
    "/app/ddata-nbu-creatio": (
        "Process_1.png; Process_1_0.png; Process_2.png; 1 Presentation.png; Lookup_1.png",
        "'DDATA NBU Integration (periodicity)': a timer start event and the rate-update tasks"),
    "/app/business-trip-request": (
        "visasubprocess.png; businesstriprequest.png",
        "the 'visa subprocess' and the parent business-trip model, with approval user tasks"),
    "/app/import-contacts-salesforce": (
        "sc1_SF_process.png; sc2_SF_webs1_enu.png; sc5_SF_webs_enu.png",
        "'Get contacts from Salesforce': a start event, the import tasks and a terminate end event"),
    "/app/dimex-creatio": (
        "KEY_F01.png; DMS_IMPORT_MAPPING_1.png; DMS_IMPORT_LOOKUP_MAPPING.png",
        "a timer start event, the 'Import Contact' and 'Export Accounts' tasks and a terminate end event"),
    "/app/popup-element-business-processes": (
        "sc1_popup_element.png; sc2_popup_element.png",
        "'Daily team meeting' with this app's own 'Open popup window' element dropped on the canvas"),
    "/app/termination-employment": (
        "termination_0.png",
        "'Send request to HR department', 'Notify employee about dismissal', 'Prepare a dismissal "
        "order', 'Receive dismissal letter', 'Update information about the dismissed employee', 'Send "
        "notifications to other departments', 'Notify the head of the department about the termination' "
        "and 'Send notifications to accounting department', with gateway diamonds and a terminate event"),
    "/app/psiog-whatsapp-connector-creatio": (
        "WhatsappConnector_2.png; WhatsAppConnector_2.png; WhatsappConnector_3.png; WhatsAppConnector_4.png",
        "'Send WhatsApp': a start event, 'Read Contact', 'Generate accessToken', 'Send WhatsApp "
        "Message', 'Process response' and a 'Reply mechanism' branch to the terminate end event"),
    "/app/event-participation-planning": (
        "event_mgmt_resized.png; logo_placement.png; stand_preparation.png; report_preparation.png; "
        "handouts_for_participants_kit.png; mention_in_press_release.png",
        "'Prepare stand for an event', 'Prepare report for an event', a 'Logo placement' gateway, "
        "'Prepare materials for participants kit', 'Review mention in press release', 'Review results "
        "of participation in the event' and 'Fill in feedback on event participation'"),
    "/app/employee-onboarding": (
        "onboarding1.png",
        "the onboarding flow: 'Prepare an employee's kit for the first working day', 'Prepare a "
        "workplace', 'Meeting with HR', 'Getting access to the necessary systems', 'Introduction to the "
        "team and getting to know the employees', 'Complete employee probationary period'"),
    "/app/recruitment": (
        "recruitment2.png",
        "the recruitment flow with Accepted/Denied gateway branches: 'Invite candidates for an "
        "interview', 'Conduct an interview', 'Select candidate', 'Make a job offer', 'Find out "
        "candidate's decision', 'Add new employee'"),
    "/app/renewal-opportunity": (
        "Untitled1.png; Untitled2.png; Untitled3.png; sc5_renewal_opp.png",
        "a 'Run every day' timer start event, a 'Qualified as account?' gateway with Yes/No branches, "
        "'Create Opportunity', 'Calculate the renewal opportunity', 'Specify new date for the renewal "
        "opportunity' and 'Notify the manager responsible for renewal'"),
    "/app/refresh-active-page-process-element-creatio": (
        "Element.png; toolbox.png",
        "the 'Refresh page sample' process with this app's own 'Refresh active page' element on the "
        "canvas ('ELEMENT: Refresh active page', 'Code: UsrRefreshPage')"),
    "/app/15-second-leads-creatio": (
        "sc1_15second_leads_bp.png; sc2_15second_leads_template.png",
        "the '15 Seconds Lead Notification Process': gateway diamonds, 'Send Email', 'Send SMS', 'Send "
        "Lead to Email' tasks and a terminate end event"),
    "/app/email-users-within-functional-or-organizational-role-creatio": (
        "Agiliz_Screenshot1.png; Agiliz_ScreenShot2.png",
        "the 'Agiliz - Send Email To All Users in a Role' sub-process, with an 'If no users' gateway and "
        "a terminate end event"),
    "/app/messages-delivery-using-queue": (
        "image003.png",
        "the 'IBM WebSphere MQ Connector' model with this app's own 'IBM WMQ write and read messages' "
        "user task and its 'Process element parameters' panel"),
    "/app/proximavision": (
        "0_screen_0.png; 1_screen_0.png; 2_screen_0.png; 3_screen.png; 4_screen.png",
        "the tool's own BPMN tab ('process analysis | Event Map | KPI | Dashboard | BPMN | Diff "
        "detector'): 'Create purchase order', 'Send Purchase Order', 'Receive Goods', 'Run Invoice', "
        "'Book Invoice' with a 'Change price' gateway and event circles"),
    "/app/employee-internal-transfer": (
        "employee_internal_transfer_0.png",
        "the transfer flow: 'Pre-interview with the employee', 'Conduct a cycle of interviews', 'Agree "
        "transfer terms with the current manager', 'Agree transfer terms with the new manager', "
        "'Approve transfer', 'Update employee's information', 'Notify employee of transfer decision'"),
    "/app/banza-bot-constructor-creatio": (
        "b_BanzaChatBotConstructor_08_0.png; b_BanzaChatBotConstructor_00_0.png; "
        "b_BanzaChatBotConstructor_02_0.png; KF(1).png",
        "the 'Banza Bot Process': a 'Chat is started' start event, 'Identify client' and 'Find client in "
        "the database', the gateway diamonds 'Client is not known' and 'Language selected?' with "
        "Yes/No/Ukrainian/Russian flow labels, 'Register client', 'Save data', 'Set language' and a "
        "terminate end event"),
}
# the one E2 listing whose page carries an AI-ish word, and what that word refers to instead
E2_AI_NOTE = {
    "/app/banza-bot-constructor-creatio":
        "The page's only AI-ish word is 'assistant', in 'The chatbot is B2C/B2B assistant for active "
        "and personalized communication with your clients' - it names the chatbot the app builds, not "
        "any element inside the published process model, and the model holds no AI/LLM task.",
}

# link -> (code, notation, what the figures are, the figures looked at, extra sentence)
SPECIAL = {
    "/app/zapier-connector-creatio": (
        "E1-not-bpmn", "Zapier's proprietary Zap editor (an iPaaS flow builder), not BPMN 2.0",
        "Zapier's own Zap editor and the vendor's marketing cards ('Seamless multi-app integration', "
        "'Trigger any business process')",
        "Zapier connector for Creatio screenshot 1.png; Key feature 1-3.png; Highlight screenshot 1.png",
        ""),
    "/app/experceo-makecom-connector-creatio": (
        "E1-not-bpmn", "Make.com's proprietary scenario editor (an iPaaS flow builder), not BPMN 2.0",
        "Make.com scenario screenshots: the 'M' rail, the 'Run once' scheduler, the "
        "CONTROLS/TOOLS/FAVORITES groups and an 'AI BETA' pill",
        "creatio-make-1..5.png; 01.png; 02.png; 5_0.png",
        "The 'AI BETA' pill is Make.com's own AI assistant button, not an element inside a process "
        "model."),
    "/app/twilio-smsmms-connector-creatio": (
        "E1-not-bpmn", "a proprietary iPaaS scenario editor (Make.com), not BPMN 2.0",
        "4_1.png is a Creatio order page; 5_0.png - the figure the listing puts under 'Marketing "
        "Campaign Integration' - is a screenshot of a Make.com scenario, 'Creatio x DocuSign - Wait for "
        "Signed Envelopes' (Run once / Every 15 minutes scheduler, CONTROLS/TOOLS/FAVORITES groups)",
        "1_1.png; 2_1.png; 3_1.png; 4_0.png; 5.png; 1_2.png; 2_2.png; 3_2.png; 4_1.png; 5_0.png",
        "The page claims a 'dedicated business process element' but publishes no model of it: the only "
        "flow figure is the vendor's Make.com screenshot, unrelated to SMS."),
    "/app/consimple-messenger-campaigns-creatio": (
        "E1-not-bpmn", "Creatio's campaign designer - a proprietary step notation, not BPMN 2.0",
        "Campaign.PNG is the campaign-designer canvas 'Return of customer churn': square step TILES with "
        "round icon badges ('Launch marketing campaign', 'Message sent to the client', 'Wait 1 minute', "
        "'Message received', 'Add new record to campaign'), dotted connectors and a SAVE/CANCEL toolbar",
        "Campaign.PNG; 1_0.PNG; 2_0.PNG; 3_0.PNG; 4_0.PNG; 5_0.PNG; 6_0.PNG; 7_0.PNG; 8_0.PNG; 9_0.PNG",
        "It is demonstrably not the process designer: no event circles, no gateway diamonds, and no RUN "
        "or ACTIONS button on the toolbar."),
    "/app/dialpad-smsmms-connector-creatio": (
        "E1-not-bpmn", "Creatio's campaign designer - a proprietary step notation, not BPMN 2.0",
        "4_NEW (1).png, under the listing's 'Automated Messaging in Business Processes' heading, is a "
        "'Solutions Metrix / Campaign Messaging' card whose screenshot is a campaign-designer canvas "
        "('New Your campaign', CAMPAIGN FLOW tab, 'Exit from campaign' tile)",
        "1_2.png; 2_4.png; 3_3.png; 4_1.png; 1_0.png; 2_0.png; 3_1.png; 4_NEW (1).png",
        "The page claims a 'business process UserTask \"Send Dialpad SMS\"' but publishes no model of "
        "it; the only flow figure is the campaign designer, which is not BPMN."),
    "/app/event-management": (
        "E1-not-bpmn", "Creatio's campaign designer - a proprietary step notation, not BPMN 2.0",
        "'Key Features' screens are vendor marketing cards; screen 4, under the vendor's 'AI-powered "
        "audience segmentation' heading, shows a 'Campaign Generation Agent' card whose screenshot is a "
        "campaign-designer canvas (CAMPAIGN FLOW tab, 'Signal-Based Campaign Trigger', 'Wait 2 days', "
        "'Exit from campaign')",
        "Event Managment Key Features screen 1-4.jpg; Event Management Highlighted screen 01-02.jpg",
        "The 'Segmentation Agent' / 'Campaign Generation Agent' AI panel in that screenshot is a side "
        "panel that GENERATES the flow - it quotes the plan it wrote and the existing campaign elements "
        "it picked - it is not an element inside the model, and no AI task appears on the canvas."),
    "/app/lead-generation": (
        "E1-not-bpmn", "none - no process model is published on the page",
        "marketing cards with product screenshots, among them 'Segmentation Agent' and 'Landing Page "
        "Generation Agent' cards that show a Creatio section list and a side AI chat panel",
        "Lead Generation Key Feature screen 01-07.jpg; Segmentation Agent Key Feature.jpg; "
        "Lead Generation Highlighted screen 01-03.jpg",
        "The page says 'Easily tailor the process using the Creatio business process designer' and "
        "'let the Segmentation Agent create accurate dynamic marketing segments', but it publishes no "
        "process model: the AI it names is a platform agent and a chat panel, not an element visible "
        "inside a process."),
    "/app/interweave-quickbooks-integration": (
        "E1-not-bpmn", "an architecture box diagram, not BPMN 2.0",
        "the figure the listing itself heads 'Architecture / Workflow Diagram' is an integration "
        "architecture box diagram (Creatio and the accounting system exchanging data through secure "
        "APIs), plus 'Functional Highlights' feature panels",
        "7_2.png; 2_5.png; 4_5.png; 5_3.png; QB - Functional Highlights.png; 1_8.png",
        ""),
    "/app/interweave-sage-intacct-integration": (
        "E1-not-bpmn", "an architecture box diagram, not BPMN 2.0",
        "the figure headed 'Architecture / Workflow Diagram' is an integration architecture diagram "
        "('the integration architecture connects Creatio directly with financial and ERP applications "
        "through the InterWeave Integration Engine'), plus feature panels",
        "7.png; 2_2.png; 4_2.png; 5_0.png; Sage - Functional Highlights.png; 1_6.png",
        ""),
    "/app/interweave-ms-dynamics-integration": (
        "E1-not-bpmn", "an architecture box diagram, not BPMN 2.0",
        "the figure headed 'Architecture / Workflow diagram' is an integration architecture diagram "
        "('Creatio sends customer, order, and workflow data into InterWeave, where mapping, validation, "
        "and business rules are applied'), plus 'Implementation Approach & Timeline' panels",
        "7_3.png; 4_6.png; 3_6.png; 5_4.png; 8.png; MSD - Functional Highlights.png",
        ""),
    "/app/interweave-ecommerce-gateway": (
        "E1-not-bpmn", "an architecture box diagram, not BPMN 2.0",
        "integration architecture / feature panels ('Real-Time or Scheduled Order Processing', "
        "'End-to-End Order Status & Shipment Tracking'), no process model",
        "2_3.png; 3_3.png; 4_3.png; 5_1.png; 6.png; 7_0.png; 9.png",
        ""),
    "/app/interweave-payment-gateway": (
        "E1-not-bpmn", "an architecture box diagram, not BPMN 2.0",
        "integration architecture / feature panels ('Configurable Payment Flow Automation', "
        "'Tokenization & Secure Customer Payment Profiles'), no process model",
        "2_4.png; 3_4.png; 4_4.png; 5_2.png; 6_0.png; 7_1.png; 9_0.png",
        ""),
    "/app/gumu-sage-intacct-integration": (
        "E1-not-bpmn", "none - no process model is published on the page",
        "record-detail screenshots ('Account Promote', 'Contact Promote', 'Invoice Promote', 'Order "
        "Promote') with the vendor's promotion wording",
        "Account Promote.png; Contact Promote.png; Import Routines.png; Invoice Promote.png; "
        "Order Promote.png",
        ""),
    "/app/syntech-relation-diagram-creatio": (
        "E1-not-bpmn", "an entity-relationship map, not BPMN 2.0",
        "'Relationship Diagram with Team-Based Views', 'Build custom relationship maps' - a "
        "network/ER map of records, not a process model",
        "194.png; 195.png; 196.png; 197.png; 198.png; 1_3.png; 1_4.png; 194_0.png; 195_0.png; 196_0.png",
        ""),
    "/app/syntech-kanban-view-creatio": (
        "E1-not-bpmn", "a Kanban board, not BPMN 2.0",
        "Kanban boards ('Universal Kanban board', 'Real-time updates & seamless navigation') - the "
        "listing visualises *stages of* a business process as board columns, which is not a process model",
        "1_11.png; 11.png; 12.png; 17.png; 31.png; 67.png; 68.png; 69.png; 70.png; 17_0.png; 12_0.png; 18.png",
        ""),
    "/app/mastercrm-kanban-view-creatio": (
        "E1-not-bpmn", "a Kanban board, not BPMN 2.0",
        "Kanban board screenshots (kanban3.jpg, kanban4.jpg, Key1.png)",
        "kanban3.jpg; kanban4.jpg; Key1.png",
        ""),
    "/app/syntech-whiteboard-creatio": (
        "E1-not-bpmn", "a whiteboard / board view, not BPMN 2.0",
        "whiteboard boards with sticky notes and columns ('Design Processes Visually', 'Build Timelines "
        "with AI', 'Communicate Inside the Board')",
        "1_0.png; 10.png; 2.png; 256.png; 265.png; 5.png; 6.png; 1_1.png; 267.png; 260.png; 255.png; "
        "265_0.png; 263.png; 262.png",
        "The one AI mention - 'Build Timelines with AI: Automatically create timelines or other views "
        "using AI' - is about AI GENERATING a board view, not an AI element inside a process model."),
    "/app/syntech-map-creatio": (
        "E1-not-bpmn", "a geographic map component, not BPMN 2.0",
        "map screenshots ('Automatic Address Geocoding', 'Heatmap / Choropleth mode', 'Live Filter "
        "Integration')",
        "193.png; 270.png; 277.png; 61 (1).png; 63.png; 64 (2).png; 65.png; 66.png; 61_0.png; 64_0.png; "
        "65_0.png; 63_0.png",
        ""),
    "/app/syntech-file-core-creatio": (
        "E1-not-bpmn", "none - no process model is published on the page",
        "a 'Google Workspace integration' card and file/attachment UI screenshots ('In-app file creation "
        "and editing')",
        "1_1-1.png; 2_1-1.png; 3_1-1.png; 5_1-1.png; 71.png; 72.png; 75.png",
        "The page carries the 'Business Process Element' compatibility tag and nothing else about a "
        "process; no figure shows one."),
    "/app/starfish-etl": (
        "E1-not-bpmn", "the vendor's own job/mapping designer and an AI-builds-the-mapping illustration",
        "Mapping feature.png is an illustration of an AI assistant producing a field mapping; "
        "ChatAI Feature.png is a 'Chat with your data' style illustration; security/scripting/low-code "
        "feature.png are the vendor's own design-tool panels; the 'Connect Creatio to your business "
        "systems' cards show a marketing flow strip of boxes joined by a line",
        "Mapping feature.png; ChatAI Feature.png; security feature.png; scripting feature.png; "
        "Low code feature.png; error log feature.png; First/second/third Highlight.png",
        "The AI mention - 'Leverage AI to automatically map fields between systems' - describes an AI "
        "feature of the ETL tool, and the figure that carries it is an illustration of AI producing a "
        "mapping, not an element inside a published process model."),
    "/app/whitedoc": (
        "E1-not-bpmn", "document-template editor screens and an AI-assistant chat card",
        "K7.png ('Advanced Template Builder') and the document UI screens are the app's template editor; "
        "K9.png ('Built-in business process logic') is a participant/role panel for document routing; "
        "K12.png ('AI Assistant') is a chat card whose panel offers to summarise and extract from the "
        "document",
        "1_2.png; 2_2.png; 3_2.png; 6_1.png; 7_1.png; 8_1.png; 9_1.png; 10_1.png; K7.png; K9.png; "
        "K12.png; 1_3.png",
        "The AI mention - 'Leverage the AI Assistant to analyze document content, generate summaries' - "
        "belongs to that chat card: it is an AI feature of the template editor, not an element inside a "
        "process model."),
    "/app/docstudio": (
        "E1-not-bpmn", "document-template editor screens and an AI-assistant chat card",
        "the 'Template builder' screens are the app's document editor, '1_4.png' sits under the vendor's "
        "own 'AI assistant' heading and shows the assistant chat, and the rest are generated-document "
        "and record screens",
        "1_1.png; 2_1.png; 3_1.png; 10_0.png; 7 (1).png; 12 (1).png; 1_4.png",
        "The AI mention is the same 'AI Assistant ... analyze document content, generate summaries' "
        "feature, shown as an editor side panel, not as an element inside a process."),
    "/app/writer-ai-assistant-creatio": (
        "E1-not-bpmn", "conversation-analytics cards, not a process model",
        "waa-screen-1.png is a 'Save your time on routine tasks' card showing the app's Conversation "
        "Analysis panel (scores, conversation criteria); waa-feature-1/2 are 'DIARIZATION' and "
        "'CUSTOMIZABLE SCRIPTS' cards",
        "waa-screen-1.png; waa-screen-2.png; waa-feature-1.png; waa-feature-2.png",
        "The app IS an AI application ('an AI-powered conversation intelligence solution'), but it "
        "publishes no process model at all, so no AI element inside a process is on view."),
    "/app/cpq-agent-creatio": (
        "E1-not-bpmn", "conversational-UI screenshots, not a process model",
        "Screenshot 2026-06-11 ...png and c5bbdb79-...png are cards and screenshots of a conversation "
        "with the CPQ agent ('Conversational product discovery', 'One-conversation quoting')",
        "Screenshot 2026-06-11 164501/164519/165358/165426.png; c5bbdb79-...png",
        "The page speaks of 'AI Agent configuration ... business process deployment, and end-to-end "
        "testing' but publishes no process model: the AI it names is a conversational agent, visible "
        "only as a chat."),
    "/app/formgenie-ai-creatio": (
        "E1-not-bpmn", "marketing cards, not a process model",
        "1/2/3.png are 'About FormGenie AI' and 'Goal of FormGenie AI' cards; 1_3/2_2/3_2.png are "
        "record and document screens",
        "1_3.png; 2_2.png; 3_2.png; 1.png; 2.png; 3.png",
        "The AI ('a smart assistant that converts uploaded documents ... into ... records') is the "
        "product itself, shown as a card and a form, never as an element inside a process model."),
    "/app/creatioai-knowledge-library": (
        "E1-not-bpmn", "configuration screens, not a process model",
        "record and configuration screens ('Section Knowledge Sources', 'File Knowledge Sources', "
        "'Agent Knowledge Configuration and Access Control')",
        "1_0.png; 2_0.png; 3_0.png; 4.png; Screenshot 2026-04-29 115441/121104.png",
        "The AI terms - 'retrieval-augmented generation (RAG)', 'Agentic Platform', 'Agents' - name "
        "knowledge sources and their access control, not elements inside a process model; no process "
        "model is published."),
    "/app/helper-gpt-creatio": (
        "E1-not-bpmn", "an AI chat product's screenshots, not a process model",
        "HelperGPT-for-Creatio-2 (1).png and sc1/sc2_helper_gpt.png are screenshots of the GPT chat",
        "HelperGPT-for-Creatio-2 (1).png; sc1_helper_gpt (2).png; sc2_helper_gpt.png",
        "The page offers 'Workflow to Business Process Conversion ... guidance on mapping', that is the "
        "GPT answering questions; the product publishes no process model."),
    "/app/m-bot-ocr-ai": (
        "E1-not-bpmn", "document-extraction UI screenshots, not a process model",
        "Screenshot 01-10.png are the app's extraction screens and cards, 'Screenshot 02 (1).png' under "
        "the vendor's own 'AI-Powered Invoice & PO Data Extraction' heading",
        "Screenshot 01-10.png; Screenshot 04 (1).png; Screenshot 02 (1).png",
        "The AI ('Automated extraction of data from your documents using newest AI & ML algorithms') is "
        "the app's own function, displayed as a document screen, not as an element inside a process."),
    "/app/salesup-multichannel-chatbots-creatio": (
        "E1-not-bpmn", "chatbot configuration cards and phone mockups, not a process model",
        "ChatBot_ADV_1..6.jpg are marketing cards: 'Interactive navigation buttons for chatbots in "
        "popular messengers' (phone mockups), 'Dynamic preview of the future message template' (a phone "
        "plus a button table), 'Creatio AI integration', 'Creating records from chatbot'",
        "ChatBot_ADV_1.jpg; ChatBot_ADV_2.jpg; ChatBot_ADV_3.jpg; ChatBot_ADV_4.jpg; ChatBot_ADV_5.jpg; "
        "ChatBot_ADV_6.jpg",
        "The AI the page claims - 'send user requests to Creatio AI directly through the chatbot ... "
        "after the AI agent processes the request' - is described in prose and shown only as a chat; the "
        "'business process' it mentions is claimed ('using a preconfigured business process') but no "
        "model of it is published."),
    "/app/conversive-sms-magic": (
        "E1-not-bpmn", "product screenshots and feature cards, not a process model",
        "conversive+creatio.png and the Screenshot 2025-* files are UI/card images ('Smart Campaigns', "
        "'Unified Timeline of Every Customer Interaction')",
        "conversive+creatio.png; 1.png; Screenshot 2025-06-10 ...png; Screenshot 2025-07-30 ...png; "
        "Screenshot 2025-07-31 ...png",
        "The AI mention - 'SMS, WhatsApp, Voice, RCS, LINE, and AI-powered chat into one seamless "
        "conversation orchestration ... AI agents assist' - describes the vendor's platform services, "
        "and no process model is published to hold them."),
    "/app/webitel-telemarketing-creatio": (
        "E1-not-bpmn", "product UI screenshots, not a process model",
        "1_19.png..5_9.png are the app's own UI screens (call queue and script configuration)",
        "1_19.png; 2_17.png; 3_16.png; 4_10.png; 5_9.png",
        "The page says scripts are configured 'using the native Creatio business process designer' but "
        "publishes no model; the 'predictive' token is the predictive DIALER, an outbound-call pacing "
        "mechanism, not an AI element inside a process."),
    "/app/dialong-chats-creatio": (
        "E1-not-bpmn", "chat-configuration UI screens, not a process model",
        "304.png ('Business process triggers') is a 'Setting up chats' UI card; the other screens are "
        "chat routing, templates and schedules in the Creatio chat panel",
        "205.png?; 201.png; 505.png; 302.png; 304.png; 303.png; 206.png; 307.png; mainImg1.png; mainImg2.png",
        "The listing's own feature name is 'Business process triggers' but the figure shows the chat "
        "setup screen, not a process model."),
    "/app/call-center-360-creatio": (
        "E1-not-bpmn", "a Freedom UI screen layout, not a process model",
        "strategy_element.png ('Sales panel / Strategy element') is a page-layout designer screen with "
        "panels and fields; the rest are panels of the agent workspace",
        "auto_links.png; backoffice.png; hr_panel.png; popup.png; quick_actions.png; roles.png; "
        "sales_panel.png; service_panel.png; strategy_element.png",
        ""),
    "/app/call-scripts-creatio": (
        "E1-not-bpmn", "the add-on's call-script decision tree rendered as buttons on a record page",
        "dynamic-call-script-classic-ui_1.png shows a contact page with an automated pop-up of branch "
        "buttons ('YES IS VETERAN', 'NO, IS NOT THE RIGHT TIME', 'NOT INTERESTED', 'CALLED'), not a "
        "process model",
        "call-script-input-classic-ui_1.png; dynamic-call-script-classic-ui_1.png",
        ""),
    "/app/time-and-duration-calculation-creatio": (
        "E1-not-bpmn", "a Microsoft Power BI report screenshot, not BPMN 2.0",
        "3_0.jpg and 4_0_0.jpg are Power BI Desktop report pages ('Microsoft | Standard Store', 'What "
        "if' / forecasting visuals) and a record screen",
        "3_0.jpg; 4_0_0.jpg",
        ""),
    "/app/email-process-elements-creatio": (
        "E1-not-bpmn", "email-composer screenshots, not a process model",
        "ExistingEmail.png and NewEmail.png are the email element's forms in the designer's parameter "
        "panel, not a canvas",
        "ExistingEmail.png; NewEmail.png",
        ""),
    "/app/ddata-hrms-creatio": (
        "E1-not-bpmn", "record screens of the HR app, not a process model",
        "01 Home / 04 Department / 07 Employees / 13 SMM-manager / 21 Applications / 23 Onboardings / "
        "24 FR / 25 Skills screens are all section and record pages",
        "01. Home_1_1.png; 04. Department_1_1.png; 07. Employees_1_1.png; 21. Applications_1_0.png; "
        "23. Onboardings_0_1.png; 24. FR_0_1.png; 25. Skills_0_1.png",
        "The AI mention - 'by means of full HR processes automation and employment of artificial "
        "intelligence elements' - is a prose claim about the product; the page publishes no process "
        "model, so no AI element inside a process is visible."),
    "/app/finserv-application-management": (
        "E1-not-bpmn", "marketing cards and record screens, not a process model",
        "the Key Feature screens are cards with product screenshots ('Structured application lifecycle', "
        "'Centralized evaluation management'), plus 'Highlighted screen' cards",
        "Finserv Application Management Key Feature screen 05/07.png; Commercial sales pipeline.png; "
        "Finserv Application Management Highlighted screen 1-5.png",
        "The AI mentions - 'Built as part of the Bank.AI platform', 'AI insights: Surface behavioral "
        "insights, risk indicators' - describe the platform's analytics, not an element inside a "
        "published process."),
    "/app/velvetel-pulse-creatio": (
        "E1-not-bpmn", "speaker-deck slides and UI screens, not a process model",
        "Slide 16_9-1..4.png are deck slides; Next-best phrases.png is a mockup card showing the 'Pulse "
        "AI Suggestion' panel; AI chat-bot.png is a call record with an 'AI chat' tab",
        "Slide 16_9 - 1.png; Slide 16_9 - 2.png; Slide 16_9 - 3.png; Slide 16_9 - 4.png; "
        "Next-best phrases.png; AI chat-bot.png",
        "The 'AI-driven communication' of the page and the 'Pulse AI Suggestion' in the figure are a "
        "real-time suggestion panel inside a call, not an element inside a process model."),
    "/app/velvetel-telephony-creatio": (
        "E1-not-bpmn", "speaker-deck slides, not a process model",
        "Slide_16_9-1_0.png, -2_0.png and Slide16_9-3_0.png are vendor deck slides ('ALL CALLS & "
        "MESSAGES. ONE CREATIO TIMELINE.')",
        "Slide_16_9-1_0.png; Slide_16_9-2_0.png; Slide16_9-3_0.png",
        ""),
    "/app/beesender-chat-master-creatio": (
        "E1-not-bpmn", "chat-workspace screens and feature cards, not a process model",
        "03.png and the other screens are the agent chat workspace; the cards are 'Quick replies and "
        "template search', 'Assign categories and subcategories on closure', 'Chat summary by Creatio AI'",
        "Beesender-Chat-Master-for-Creatio-....png; 03.png; 04.png",
        "The AI mention - 'Chat summary by Creatio AI: When a chat ends, Creatio's AI auto-generates a "
        "summary' - is a summarisation feature of the chat workspace, shown as a record panel, not as "
        "an element inside a published process."),
    "/app/beesender-bot-master-creatio": (
        "E1-not-bpmn", "feature cards, not a process model",
        "KF1.png ('Messages with action buttons' - a phone mockup and a configuration panel), KF2.png, "
        "Highlight1/2.png and the other cards",
        "Beesender-Bot-Master-for-Creatio-4.0_KF1.png; KF2.png; Highlight1.png; Highlight2.png",
        "The page says 'You can use the Creatio business process designer to set a rule-based chatbot' "
        "and the cards say the buttons 'trigger subprocesses', but no sub-process model is published; "
        "the 'Chat summary by Creatio AI' claim belongs to the same platform AI as above."),
    "/app/beesender-outbound-creatio": (
        "E1-not-bpmn", "product cards, not a process model",
        "the Beesender-Outbound cards (including the 'Ban'/'Med' variants) are feature cards",
        "Beesender-Outbound-for-Creatio-2.0.png; Beesender-Outbound-for-Creatio-Ban.png; "
        "Beesender-Outbound-for-Creatio-Med.png",
        ""),
    "/app/productivity": (
        "E1-not-bpmn", "marketing cards, not a process model",
        "the 'Productivity key features' cards and the 'highlighted screenshot' cards ('AI Meeting "
        "Planning', 'Flexible and configurable calendar')",
        "Productivity key features 1-4.png; Productivity highlighted screenshot 1-5.png",
        "The AI mentions - 'AI Meeting Planning: Automatically find the best available time slots', "
        "'The Productivity Agent is now available' - name a platform agent feature shown in a card, and "
        "no process model is published."),
    "/app/customer-360": (
        "E1-not-bpmn", "marketing cards, not a process model",
        "the 'Customer 360 Key Feature' cards and 'Highlighted screenshot' cards ('Enrich account data "
        "with AI power', 'Simplify the workflow', 'Segment customers')",
        "Customer 360 Key Feature 01-07.png; Customer 360 Highlighted screenshots 01-02.png",
        "The AI mention - 'Automatically enrich account data with AI-generated company insights' and "
        "'The Sales Agent is now available' - names a platform feature in a card; no process model is "
        "published."),
    "/app/order-and-contract-management": (
        "E1-not-bpmn", "marketing cards, not a process model",
        "the 'Order and Contract Management Key Feature' cards and 'Highlighted screenshot' cards "
        "('Product Management', 'Approvals Management', 'Analytics')",
        "Order and Contract Management Key Feature 02-06.png; Highlighted screenshots 01-03.png",
        "The AI mentions - 'Accelerate product onboarding with AI-generated product descriptions', "
        "'Leverage Creatio.ai skills and an AI sales agent' - describe platform AI shown in cards, and "
        "no process model is published."),
    "/app/lead-and-opportunity-management": (
        "E1-not-bpmn", "marketing cards, not a process model",
        "the 'Key Feature' cards, including one under the vendor's heading 'Sales Process Automation' "
        "which is a card with a CRM screenshot, and one under 'Lead and Opportunity Summarization AI "
        "Skills'",
        "Lead and Opportunity Management Key Feature screenshots 01-18.png; Highlighted screenshots 01-02.png",
        "The page says 'Manage all opportunities using the out-of-the-box business process' and offers "
        "'Lead and Opportunity Summarization AI Skills: Provides concise summaries', but publishes no "
        "process model - the AI is a summarisation Skill card."),
    "/app/email-marketing": (
        "E1-not-bpmn", "marketing cards, not a process model",
        "the 'Email Marketing Key Features screenshot' cards and 'Highlighted screenshot' cards "
        "('Design emails in one go', 'Get clarity on bounce reasons')",
        "Email Marketing Key Features screenshot 01-04.png; Highlighted screenshots 01-02.png",
        ""),
    "/app/social-marketing-creatio": (
        "E1-not-bpmn", "feature cards and UI screens, not a process model",
        "the ten figures are cards and screens for scheduled publishing and destination sync "
        "('PER DESTINATION DELIVERY TRACKING', 'Automated scheduled publishing')",
        "Auto Destinatin sync.png; Automated scheduled posting.png; Multi Destination Feature.png; "
        "Per Destination tracing.png; Secure Connection.png; Secure Authraization.png",
        "The page's 'let a scheduler business process publish when the time is reached' is a prose "
        "claim; the figures show the scheduling UI, not a process model."),
    "/app/storekeeper-creatio": (
        "E1-not-bpmn", "warehouse record screens, not a process model",
        "Btech_WMS_Creatio_1..5.png and key feature WMS1.png are inventory and warehouse record screens",
        "Btech_WMS_Creatio_1.png; Btech_WMS_Creatio_2.png; Btech_WMS_Creatio_3.png; "
        "key feature WMS1.png",
        "The page mentions 'business processes can be developed on a separate paid request' - a paid "
        "add-on, not a published model."),
    "/app/sla-tracker-creatio": (
        "E1-not-bpmn", "record screens with calculated columns, not a process model",
        "2.png, 3.png, 3_0.png, 4.png are Lead/record screens showing the app's calculated duration "
        "columns ('Due time calculation setting')",
        "2.png; 3.png; 4.png; 3_0.png",
        ""),
    "/app/hrm-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "HRM_BeTech_Creatio_1..4.png are vacancy and applicant record screens",
        "HRM_BeTech_Creatio_1.png; HRM_BeTech_Creatio_2.png; HRM_BeTech_Creatio_3.png; "
        "HRM_BeTech_Creatio_4.png",
        ""),
    "/app/prozemli-creatio": (
        "E1-not-bpmn", "record screens and maps, not a process model",
        "Screenshot_1/2/4/5/8/9_0.png are land-register record screens and map views",
        "Screenshot_1_0.png; Screenshot_2_0.png; Screenshot_4_0.png; Screenshot_5.png; Screenshot_8.png; "
        "Screenshot_9.png",
        ""),
    "/app/paymaze-payments-management-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "the Screenshot 2022-06-07 files are the app's Programs / Payments record screens",
        "Screenshot 2022-06-07 at 10.*.png",
        ""),
    "/app/servicepoint-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "ServicePoint_EN_1..3.png are service-desk record screens",
        "ServicePoint_EN_1.png; ServicePoint_EN_2.png; ServicePoint_EN_3.png",
        ""),
    "/app/alphasms-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "sc1/sc2/sc3_alphasms_connector screens are SMS record and settings screens",
        "sc1_alphasms_connector_1.jpg; sc2_alphasms_connector_0.png; sc3_alphasms_connector_1_0.png",
        ""),
    "/app/change-object-assignee-creatio": (
        "E1-not-bpmn", "record screens and a settings pop-up, not a process model",
        "1_6.png, 2_4.png, 3_3.png are record screens with the app's reassignment action",
        "1_6.png; 2_4.png; 3_3.png",
        ""),
    "/app/record-metadata-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "page.png, pageLegendVisible.png and sysSetting.png are a record page, its legend and a system "
        "setting screen",
        "page.png; pageLegendVisible.png; sysSetting.png",
        ""),
    "/app/mass-task-builder-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "BtechMassTasks-creatio_1/2/4/5.png are record and wizard screens",
        "BtechMassTasks-creatio_1.png; BtechMassTasks-creatio_2.png; BtechMassTasks-creatio_4.png; "
        "BtechMassTasks-creatio_5.png",
        ""),
    "/app/mass-updating-pro-creatio": (
        "E1-not-bpmn", "record screens and cards, not a process model",
        "1_1.png..4_0.png and the key features cards are update-wizard screens",
        "1_1.png; 2_3.png; 3_2.png; 4_0.png; key features 1.png; key features 2.png",
        "The page contrasts itself with 'a simple no-code alternative without bpmn process to SQL "
        "queries' - it is the alternative, and no model is published."),
    "/app/deduplication-freedom-ui-enhancements": (
        "E1-not-bpmn", "record screens, not a process model",
        "AccountDeduplication.png, ContactScreenshot.png and Screenshot 2026-03-05*.png are the "
        "duplicate-search screens",
        "AccountDeduplication.png; ContactScreenshot.png; Screenshot 2026-03-05 145017/145143/150241/"
        "150414.png",
        ""),
    "/app/excel-reports-builder-creatio": (
        "E1-not-bpmn", "report-configuration screens, not a process model",
        "sc1_report_setup_new.png, sc2_report_list_new.png, sc3_run_report_in_section.png are the "
        "report builder's screens",
        "sc1_report_setup_new.png; sc2_report_list_new.png; sc3_run_report_in_section.png",
        "The release note says 'Added a business process element' - claimed, not shown; no figure on "
        "the page is a process model."),
    "/app/object-structure-export-creatio": (
        "E1-not-bpmn", "configuration screens, not a process model",
        "sc1/sc2/sc3_sctructure_export.png are configuration and output screens",
        "sc1_sctructure_export.png; sc2_structure_export.png; sc3_structure_export.png",
        "The page mentions exporting 'using preconfigured business process' - claimed, not shown."),
    "/app/process-elements-disabling-creatio": (
        "E1-not-bpmn", "process-log screens, not a process model",
        "skip1sc.png ('Skip Hanging Process Elements') and skip2sc.png show the process LOG with the "
        "app's skip action, not a canvas",
        "skip1sc.png; skip2sc.png",
        ""),
    "/app/organizational-structure": (
        "E1-not-bpmn", "record screens, not a process model",
        "sc1/sc2_OrgENU_DivisionPage.png and _StaffUnitPage.png are division and staff-unit record pages",
        "sc1_OrgENU_DivisionPage.png; sc1_OrgENU_DivisionPage_0.png; sc2_OrgENU_StaffUnitPage.png; "
        "sc2_OrgENU_StaffUnitPage_0.png",
        "The page says the structure is used 'for approval process automation' - the artefact is the "
        "structure itself, not a process."),
    "/app/printable-attachment-email-creatio": (
        "E1-not-bpmn", "a designer parameter screenshot, not a process model",
        "screenshot-attachments-mkplace.png shows the app's element in the designer's settings panel",
        "screenshot-attachments-mkplace.png",
        "The text tells the reader to 'open existed or create new business process' in the Process "
        "library, but no model is published."),
    "/app/health-monitor-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "Health_HomaPage.jpg and Health_Lookup.jpg are the app's health-status screens",
        "Health_HomaPage.jpg; Health_Lookup.jpg",
        "The page mentions 'a business process of the same name' that updates the directory - claimed, "
        "not shown."),
    "/app/horoshop-connector-creatio": (
        "E1-not-bpmn", "record and settings screens, not a process model",
        "10_0.png..13_0.png are the connector's settings and record screens",
        "10_0.png; 11_0.png; 12_0.png; 13_0.png",
        "The page says 'Start business process \"Start sync Horoshop\"' - the app's process is named, "
        "not shown."),
    "/app/shop-express-connector-creatio": (
        "E1-not-bpmn", "settings screens, not a process model",
        "1_2_0.png and 2_1_0.png are the connector's settings screens",
        "1_2_0.png; 2_1_0.png",
        "The page says 'Start business process \"Start sync Shop-Express\"' - named, not shown."),
    "/app/phonet-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "Screenshot_1..4_0_0.png are telephony record screens",
        "Screenshot_1_0_0.png; Screenshot_2_0_0.png; Screenshot_3_0_0.png; Screenshot_4_0_0.png",
        ""),
    "/app/nbu-currency-rate-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "BtechNBUCourses-creatio_1..5.png are currency-rate record screens",
        "BtechNBUCourses-creatio_1.png; BtechNBUCourses-creatio_2.png; BtechNBUCourses-creatio_3.png",
        "The page says rates are used 'in CRM business processes for currency conversions' - the "
        "artefact shown is the rate record, not a process."),
    "/app/sage-100-connector-creatio": (
        "E1-not-bpmn", "settings and record screens, not a process model",
        "S100 - 1..5.png and the Key Feature screens are the connector's wizard and record screens",
        "S100 - 1.png; S100 - 2.png; S100 - 3.png; Key Features - 1.png; KeyFeature_nonMktg_2.png",
        "The page tells the reader to filter the 'business process list' for the app's process - named, "
        "not shown."),
    "/app/sage-intacct-connector-creatio": (
        "E1-not-bpmn", "record and settings screens, not a process model",
        "sc1/sc2/sc3_intacct screens are object-mapping and account-page screens",
        "sc1_intacct_objects.png; sc2_intacct_account_page.png; sc3_intacct_maps.png",
        "The page says syncs can be triggered 'through Creatio's business process engine' - claimed, "
        "not shown."),
    "/app/docuware-connector-creatio": (
        "E1-not-bpmn", "settings screens, not a process model",
        "sc2_docuware_upd.png and Screenshot2.png are the connector's configuration screens",
        "sc2_docuware_upd.png; Screenshot2.png",
        "The page tells the reader to 'Create Business Processes in Creatio to upload documents' - "
        "the instruction is prose, no model is published."),
    "/app/zugferd-einvoices-creatio": (
        "E1-not-bpmn", "document and validation screens, not a process model",
        "sc1/sc2/sc3_zugferd.png and ZFD-screenshot-1..3.png are invoice and XML-validation screens",
        "sc1_zugferd.png; sc2_zugferd.png; ZFD-screenshot-1.png; ZFD-screenshot-2.png",
        ""),
    "/app/dropbox-connector-creatio": (
        "E1-not-bpmn", "settings screens, not a process model",
        "sc1/sc2/sc3_dropbox.png are the connector's configuration screens",
        "sc1_dropbox.png; sc2_dropbox.png; sc3_dropbox.png",
        "The page says 'Connect your Creatio to your DropBox using business process' - claimed, not "
        "shown."),
    "/app/scim-integration": (
        "E1-not-bpmn", "configuration and log screens, not a process model",
        "a/b/c/d/e/f_*_resaved.png and the OAuth screens are provisioning configuration and logs",
        "a_profile_list_0_resaved.png; b_initial_setup_0_resaved.png; OAuth_screen_1_resaved.png; "
        "provision_logs_screen_4_resaved.png",
        "The page notes that 'custom business processes that affect SysAdminUnit ... can influence "
        "provisioning behaviour' - a caveat in prose, no model published."),
    "/app/hootsuite-connector-creatio": (
        "E1-not-bpmn", "record screens and cards, not a process model",
        "NewUI0..4.png and the Key Feature cards ('Case Creation from Social Posts')",
        "NewUI0.png; NewUI1.png; NewUI2.png; Hootsuite connector Key Feature screenshots 01-03.png",
        "The page says to use 'Creatio business process engine to automate follow-ups' - claimed, not "
        "shown."),
    "/app/smarttender-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "SmarTenderConnector21/22/23.png are tender record screens",
        "SmarTenderConnector21.png; SmarTenderConnector22.png; SmarTenderConnector23.png",
        "The page says to 'Launch a business process for obtaining data' - named, not shown."),
    "/app/goto-meeting-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "1_0.png..6_0.png are meeting record screens",
        "1_0.png; 2_0.png; 3_0.png; 4_0.png; 5_0.png; 6_0.png",
        "The 'Schedule meetings via business process' item is listed as 'Coming soon' - a roadmap "
        "entry, not an artefact."),
    "/app/visual-studio-extension-creatio": (
        "E1-not-bpmn", "an IDE screenshot, not BPMN 2.0",
        "11_1.png..55_0.png are Visual Studio screens (code and the extension's panels)",
        "11_1.png; 22_0.png; 33_1.png; 44_0.png; 55_0.png",
        "The page mentions creating 'business processes with the \"Script-Task\" executable element' - "
        "the figures are the IDE, not a process model."),
    "/app/banza-jira-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "sc1..sc8_jira.png are the connector's project and issue record screens",
        "sc1_jira.png; sc2_jira.png; sc3_jira.png; sc4_jira.png; sc5_jira.png; sc6_jira.png; "
        "sc7_jira.png; sc8_jira.png",
        "The page says to 'Start the [Import lookup data from Jira] business process' - named, not "
        "shown."),
    "/app/banza-zabbix-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "Zabbix 1..4.png are Zabbix-event record screens",
        "Zabbix 1.png; Zabbix 2.png; Zabbix 3.png; Zabbix 4.png",
        ""),
    "/app/banza-analytical-segmentation-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "Sc0_segm.png..sc4_segm.png are account-category and segment record screens",
        "Sc0_segm.png; sc1_segm.png; sc2_segm.png; sc3_segm.png; sc4_segm.png",
        ""),
    "/app/banza-data-scoring-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "Screenshot_2_0.png ('Contact scoring card'), Screenshot_3_0.png, Screenshot_5.png ('Scoring "
        "cards') and Screenshot_6_0.png are record screens",
        "Screenshot_2_0.png; Screenshot_3_0.png; Screenshot_5.png; Screenshot_6_0.png",
        "The page says 'Setting up scoring rules using a business process or C# method' and 'Use a new "
        "process element [Scoring] for that' - claimed, not shown."),
    "/app/banza-files-extended-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "Files extended 1_0..6_0.png are file record screens",
        "Files extended 1_0.png; Files extended 2_0.png; Files extended 3_0.png; Files+extended+1_0.png",
        ""),
    "/app/banza-chat-aggregator-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "b_Chat_aggregator (1..6).png are chat and team record screens",
        "b_Chat_aggregator (1).png; b_Chat_aggregator (2).png; b_Chat_aggregator (3).png",
        "The page says it becomes 'easier for the company to process requests from chats and launch "
        "internal business processes' - claimed, not shown."),
    "/app/mastercrm-e-chat-integration-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "the three Screenshot 2023-10-24 files are chat record screens",
        "Screenshot 2023-10-24 092941.png; Screenshot 2023-10-24 093701.png; Screenshot 2023-10-24 093812.png",
        "The page offers to 'Use business processes for initiating' chats - claimed, not shown."),
    "/app/mastercrm-bas-integration-creatio": (
        "E1-not-bpmn", "configuration screens, not a process model",
        "1c_sc1.png and 1c_sc2.png are the integration rule and 1C configuration screens",
        "1c_sc1.png; 1c_sc2.png",
        "The page speaks of 'end-to-end business process using best and specific capabilities of both "
        "systems' - the figures are the mapping rules, not a process model."),
    "/app/mastercrm-automotive-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "the Cyrillic-named screenshots are the app's lead, test-drive and contract record screens",
        "Снимок экрана 2023-03-31 в 17.44.10.png; ... 17.45.01.png; ... 17.49.57.png",
        ""),
    "/app/sirma-insuite-creatio": (
        "E1-not-bpmn", "record screens and banners, not a process model",
        "Claim/Contact/InsuredObject/Policy record screens plus four 'banners' marketing images",
        "Claim_GeneralInfoTab.PNG; Contact_InsuranceInfo.PNG; InsuredObject_motorVehicle.PNG; "
        "Policy_GeneralInfoTab.PNG; banners-creatio-*.png",
        ""),
    "/app/consimple-messenger-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "1.PNG..9.PNG are message and record screens",
        "1.PNG; 2.PNG; 3.PNG; 4.PNG; 5.PNG; 6.PNG; 7.PNG; 8.PNG; 9.PNG",
        "The page says 'Pre-configured element in the designer of business processes' - claimed, not "
        "shown."),
    "/app/infobip-omnichannel-messaging-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "the four 2023-01-04 screenshots are Creatio SMS and settings screens",
        "2023-01-04 13_56_17-Creatio_0.png; 2023-01-04 13_59_19-Window_0.png; "
        "2023-01-04 14_05_08-Window_0.png; 2023-01-04 14_23_27-Window_0.png",
        "The page says 'Send SMS from business processes in Creatio Studio' - claimed, not shown."),
    "/app/syntech-lifecell-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "01_0.png..04_0.png and 03.png are campaign and message record screens",
        "01_0.png; 02_0.png; 03_0.png; 04_0.png; 03.png",
        "The page says messages are sent 'triggered by system events, including during business process "
        "execution' - claimed, not shown."),
    "/app/mitra-docusign-sonnector-creatio": (
        "E1-not-bpmn", "record and DocuSign page screens, not a process model",
        "A_Opportunity+Page.PNG, B_Docusign+Creatio+Page.PNG, C/D_Docusign+Page.PNG and "
        "E_Contract+Page.PNG are record and DocuSign screens",
        "A_Opportunity+Page.PNG; B_Docusign+Creatio+Page.PNG; C_Docusign+Page.PNG; E_Contract+Page.PNG",
        "The only AI-looking token on the page is the substring 'ai.' inside the vendor's e-mail "
        "address 'creatiosales@mitrai.com' - a false positive of the screen, not an AI claim."),
    "/app/confero-docusign-connector-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "Docusign_Overview_1_0/2_0.png and Docusign_KF_1..4.png are request and record screens",
        "Docusign_Overview_1_0.png; Docusign_KF_1.png; Docusign_KF_2.png; Docusign_KF_4.png",
        "The page says the solution 'accelerates business processes' - the figures are the DocuSign "
        "request records, not a process model."),
    "/app/intrasign-certificate-based-internal-signature-creatio": (
        "E1-not-bpmn", "marketing cards and record screens, not a process model",
        "IntraSign_Overview_1.png is a 'Secure Document-to-Record Linkage' card with a Creatio "
        "screenshot; the KF screens are signing panels",
        "IntraSign_Overview_1.png; IntraSign_Overview_2.png; IntraSign_Overview_3.png; IntraSign_KF_1.png",
        "The page says IntraSign 'simplifies document signing workflows, accelerates business "
        "processes' - no model is published."),
    "/app/credit-union-package-creatio": (
        "E1-not-bpmn", "marketing cards with UI screenshots, not a process model",
        "++Workflow list - Screenshot 3.png sits under the vendor's 'Guided Member Workflows' heading "
        "and is a card with a member-record screenshot; the rest are member screens",
        "++Member 360 -Screenshot 2.png; ++Member authentication - Pic 1.png; ++Workflow list - "
        "Screenshot 3.png",
        "The workflow mentioned is the 'Popup element in business processes' product from the same "
        "marketplace, referenced in prose."),
    "/app/pandadoc-document-management-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "1600x800*.png and pandadoc.png are document and record screens",
        "1600x800.png; 1600x800-1.png; 1600x800-2.png; pandadoc.png",
        "The page's instruction is 'Run the \"Actualize CSP header\" business process' - named, not "
        "shown."),
    "/app/document-tools-creatio": (
        "E1-not-bpmn", "file-viewer screens, not a process model",
        "Convert to pdf.png, Download file.png, MergePopup.png and Preview File.png are the app's file "
        "viewer and conversion screens",
        "Convert to pdf.png; Download file.png; MergePopup.png; Preview File.png",
        ""),
    "/app/whatsapp-connector-creatio": (
        "E1-not-bpmn", "record, phone and chat screens, not a process model",
        "the WhatsApp 1-5 May '24 screens are the contact record with the chat panel and the message "
        "templates",
        "WhatsApp 1 May '24.png; WhatsApp 2 May '24.png; WhatsApp 3 May '24.png; WhatsApp 4 May '24.png; "
        "WhatsApp 5 May '24.png",
        "The page says to 'Utilize the new element process \"BGlobal: Send WhatsApp Template\" ... "
        "directly from your business processes' - the element is claimed, and no figure shows the "
        "canvas."),
    "/app/nova-poshta-integration-creatio": (
        "E1-not-bpmn", "marketing cards and record screens, not a process model",
        "Btech_NP_Creatio_3.png is a 'From order to waybill: fast & easy in Creatio' card with an "
        "order-page screenshot; the KF screens are record screens",
        "Btech_NP_Creatio_1.png; Btech_NP_Creatio_2.png; Btech_NP_Creatio_3.png; KF1.png; KF2.png",
        "The page says 'Business processes for creating an express waybill from the Sales and Orders "
        "sections' - claimed, not shown."),
    "/app/salesup-viber-chat-channel-creatio": (
        "E1-not-bpmn", "record screens, not a process model",
        "VCC_1_0..4_0.jpg and VCC_3.jpg are chat and record screens",
        "VCC_1_0.jpg; VCC_2_0.jpg; VCC_3_0.jpg; VCC_4_0.jpg; VCC_3.jpg",
        "The AI token on the page is the product name 'Ada AI chatbot' in a list of messengers the app "
        "connects to - not an element inside a process, and the page says only 'Integrate chats into "
        "business processes'."),
    "/app/salesup-multichannel-bulk-messaging-creatio": (
        "E1-not-bpmn", "record and wizard screens, not a process model",
        "Bulk_P1.jpg is a 'Multichannel demo day' card with a template and phone preview; the other "
        "figures are setup-wizard and analytics screens",
        "Bulk_P1.jpg; Alternative channels.jpg; Bulk_P3.jpg; Bulk_P4.jpg; Bulk_P5.jpg; Bulk_P6.jpg; "
        "Bulk_P7.jpg",
        ""),
    "/app/salesup-multichannel-notifications-creatio": (
        "E1-not-bpmn", "notification-configuration screens, not a process model",
        "MN_P1.jpg is the notification setting 'Meeting reminder 1 hour before' with its recipients "
        "list; the other figures are configuration screens",
        "MN_P1.jpg; MN_P1_0.jpg; MN_P3.jpg; 5_shell_sumnfc.jpg; 6_shell_sumnfc.jpg",
        ""),
    "/app/prengi-service-creatio": (
        "E1-not-bpmn", "maintenance record screens, not a process model",
        "1_1.png..7 (2).png are equipment and maintenance record screens",
        "1_1.png; 2_1.png; 3_1.png; 4_1.png; 5_1.png; 6_1.png; 7 (2).png",
        "The 'predictive' token is 'predictive maintenance schedule' - a maintenance planning field in "
        "a record, not an AI element inside a process."),
    "/app/payment-transactions": (
        "E1-not-bpmn", "payment record screens, not a process model",
        "sc1_ENU_PaymentsList.png and sc2_ENU_PaymentsPage.png are the payment list and record screens",
        "sc1_ENU_PaymentsList.png; sc2_ENU_PaymentsPage.png",
        "The page says payments can be bound to invoices 'using a business process or data' - claimed, "
        "not shown."),
    "/app/customer-journey": (
        "E1-not-bpmn", "account pages with a journey widget, not a process model",
        "sc1_customer_journey.png and sc2_cust_journ.png are account record pages with the app's "
        "'NEXT STEPS' / customer-journey widget; csenu3/4/5.png the same widget in other states",
        "sc1_customer_journey.png; sc2_cust_journ.png; csenu3.png; csenu4.png; csenu5.png",
        "The page's instruction is to 'run \"Fill in account stage\" business process' - named, not "
        "shown."),
    "/app/engaging-dormant-customers": (
        "E1-not-bpmn", "a calendar screenshot, not a process model",
        "ENU_calendar_sc1.png is the activity calendar the app creates tasks in",
        "ENU_calendar_sc1.png",
        "The page describes 'The \"Automatic creation of tasks on dormant customers\" business process "
        "starts every working day at 12.15 AM' - claimed, not shown; the single figure is the calendar."),
    "/blog/transforming-behavioral-health-operations-no-code-how-interweave-smartsolutions-powers-cbc": (
        "E1-not-bpmn", "marketing cards, not a process model",
        "the three figures are a 'How CBC integrated its CRM with InterWeave QuickBooks' card with a "
        "browser mockup, a QuickBooks 'Powered by InterWeave' card and an author portrait",
        "885x545_Cognitive & Behavioral.png; Quickbooks Updated for Creatio.png; "
        "Screen-Shot-2023-07-31-at-2.44.46-.png",
        "The AI token is 'Document Management AI Workflow automation' in the post's product-tag row - "
        "a service label, not an element inside a process model."),
    "/blog/digital-gridlock-fast-lane-how-writer-supercharged-meestchinas-crm-lightning-fast-logistics": (
        "E1-not-bpmn", "a case-study card, not a process model",
        "885x545_Social_MeestChina.png is the case-study card ('How MeetsChina Improved CRM "
        "Performance by 50% Using Writer Bot'); test.png is a second image of the post",
        "885x545_Social_MeestChina.png; test.png",
        ""),
}

# The three phase-2 items whose process language is incidental and which publish no artefact figure.
E0 = {
    "/app/experceo-qr-code-generator-creatio": (
        "Experceo-QRCodeGenerator.1.0_2_2.png; Experceo-QRCodeGenerator.1.0_3_1.png",
        "The page's process language is an instruction - 'Add User Task: Integrate a User Task element "
        "into your business process' and 'You can use the Formula editor to set the value from all "
        "Business Process elements' - and its two figures are the app's own screen captures beside that "
        "instruction; nothing on the page is presented as a process model."),
    "/app/experceo-barcode-generator-creatio": (
        "experceo-barcode-1.png; experceo-barcode-2_.png",
        "Same pattern as the vendor's QR app: the text instructs the reader to 'Integrate a User Task "
        "element' and points at the 'Generate Barcode and save to Contact' business process by name, "
        "and the two figures are the app's own screen captures; no figure is presented as a process "
        "model."),
    "/app/business-processes-basic-steps-working-data": (
        "(none - the listing has no figure at all)",
        "The listing is a free learning template ('The template allows users to learn how to leverage "
        "basic elements in business processes') and publishes no figure at all, so nothing on the page "
        "is a process artefact: the model lives inside the downloadable package. Flagged in the note "
        "because a blank scaffold whose tasks could be AI-bound is the kind of item the researcher may "
        "want to look at in the vendor's designer; the page itself shows nothing."),
}

DEFAULT_NOTE = (
    "Judged by eye from the cached listing page (judged_from: marketplace-cache) after the eye pass "
    "over its figures: every non-chrome figure of this listing was tiled into the contact sheets "
    "(ledgers/_creatio/mp_sheets.py) and read, and the figures the sheet's noise filter had dropped were "
    "tiled and read separately (ledgers/_creatio_mp_noise_sheet.py; for this listing: %s). They are the "
    "app's own product screenshots and the vendor's marketing cards (a coloured panel with a heading and "
    "a product screenshot) - no process model of any kind, so there is no BPMN artefact to hold an AI "
    "element. The page's process language is a claim rather than a published model.")


def load():
    items = json.loads((OUT / "mp_items.json").read_text(encoding="utf-8"))
    pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
    blog = json.loads((OUT / "mp_blog_index.json").read_text(encoding="utf-8"))
    blogpages = json.loads((OUT / "mp_blog_pages.json").read_text(encoding="utf-8"))
    led = [json.loads(l) for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]
    rows, header, footer = {}, None, None
    for o in led:
        if o.get("type") == "header":
            header = o
        elif o.get("type") == "footer":
            footer = o
        else:
            rows[o["n"]] = o
    return items, pages, blog, blogpages, rows, header, footer


def evidence_of(p, rx=None):
    """A verbatim sentence of the listing (<=25 words), preferring one that carries `rx`."""
    t = re.sub(r"\s+", " ", M.body(p))
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s", t) if len(s.split()) >= 6]
    pick = None
    if rx:
        for s in sents:
            if re.search(rx, s, re.I):
                pick = s
                break
    if not pick:
        for s in sents:
            if not re.match(r"^(Install|Overview|Download|Price|Categories|Type|Launched)", s):
                pick = s
                break
    if not pick:
        pick = t
    w = pick.split()
    return " ".join(w[:25]) + (" ..." if len(w) > 25 else "")


def noise_names(link):
    """The figures of this listing that the contact sheets' noise filter dropped, if any were read."""
    sheets = json.loads((OUT / "mp_figsel.json").read_text(encoding="utf-8"))
    shown = {e["file"] for e in sheets if e["link"] == link}
    p = (PAGES.get(link) or {})
    dropped = [i["src"].split("/")[-1] for i in (p.get("imgs") or [])
               if i["src"].split("/")[-1] not in shown]
    return "; ".join(d[:40] for d in dropped[:4]) + (" ..." if len(dropped) > 4 else "")


def ai_line(p):
    hay = M.hay_of(p)
    hard = sorted({m.group(0) for m in re.finditer(M.AI, hay, re.I)})
    soft = sorted({m.group(0) for m in re.finditer(M.SOFT, hay, re.I)})
    if hard:
        return ("The AI screen over the page finds the token(s) %s, but they name a platform AI feature "
                "of the product, not an element inside a published process model." % ", ".join(hard[:4]))
    if soft:
        return ("The AI screen over the page finds only the soft token(s) %s - words about the "
                "product's own chat or its human operators, not an AI element inside a published "
                "process model." % ", ".join(soft[:4]))
    return "No AI/LLM token occurs anywhere on the page."


def phase2_row(link, p, n, kind):
    if link in E2:
        files, what = E2[link]
        note = ("The listing DOES publish a process model: %s It is %s And %s Files looked at: %s."
                % (what, BPMN, E2_AI_NOTE.get(link, NO_AI), files))
        return {"n": n, "url": BASE + link,
                "title": p["title"].replace(" | Creatio Marketplace", ""),
                "verdict": "EXCLUDE", "reason": "E2-no-ai-element", "judgment": True,
                "evidence": evidence_of(p, None), "evidence_source": "page text",
                "figure_evidence": files, "judged_from": "marketplace-cache", "notation": BPMN,
                "record": None, "needs_visual_check": False, "needs_human_ruling": False,
                "duplicate_of": None, "accessed": TODAY,
                "surface": "marketplace" if kind == "app" else "marketplace-blog", "note": note}
    if link in E0:
        files, why = E0[link]
        return {"n": n, "url": BASE + link,
                "title": p["title"].replace(" | Creatio Marketplace", ""),
                "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": True,
                "evidence": evidence_of(p, None), "evidence_source": "page text",
                "figure_evidence": files, "judged_from": "marketplace-cache",
                "notation": None, "record": None, "needs_visual_check": False,
                "needs_human_ruling": False, "duplicate_of": None, "accessed": TODAY,
                "surface": "marketplace" if kind == "app" else "marketplace-blog",
                "note": why + " " + ai_line(p)}
    if link in SPECIAL:
        code, notation, what, files, extra = SPECIAL[link]
        note = ("Judged by eye from the cached listing page after the eye pass over its figures. The "
                "figures are %s. Notation: %s - so it is not a BPMN 2.0 artefact. %s%s Files looked "
                "at: %s." % (what, notation, extra + " " if extra else "", ai_line(p), files))
        return {"n": n, "url": BASE + link,
                "title": p["title"].replace(" | Creatio Marketplace", ""),
                "verdict": "EXCLUDE", "reason": code, "judgment": True,
                "evidence": evidence_of(p, None), "evidence_source": "page text",
                "figure_evidence": files, "judged_from": "marketplace-cache", "notation": notation,
                "record": None, "needs_visual_check": False, "needs_human_ruling": False,
                "duplicate_of": None, "accessed": TODAY,
                "surface": "marketplace" if kind == "app" else "marketplace-blog", "note": note}
    files = M.names(p, k=4)
    return {"n": n, "url": BASE + link, "title": p["title"].replace(" | Creatio Marketplace", ""),
            "verdict": "EXCLUDE", "reason": "E1-not-bpmn", "judgment": True,
            "evidence": evidence_of(p, None), "evidence_source": "page text",
            "figure_evidence": files, "judged_from": "marketplace-cache",
            "notation": "none - no process model appears on the page",
            "record": None, "needs_visual_check": False, "needs_human_ruling": False,
            "duplicate_of": None, "accessed": TODAY,
            "surface": "marketplace" if kind == "app" else "marketplace-blog",
            "note": DEFAULT_NOTE % (noise_names(link) or "none dropped") + " " + ai_line(p)}


PAGES = {}


def main():
    global PAGES
    phase = 2 if "--phase2" in sys.argv else 1
    items, pages, blog, blogpages, rows, header, footer = load()
    PAGES = pages
    census = ([("app", i["link"], i) for i in items["items"]]
              + [("blog", b, None) for b in blog["articles"]])
    have = {r["url"].rstrip("/") for r in rows.values()}
    n = max(rows) + 1
    new = []
    for kind, link, it in census:
        url = BASE + link
        if url.rstrip("/") in have:
            continue
        p = (pages if kind == "app" else blogpages).get(link)
        if not p or p.get("status") != "ok":
            new.append({"n": n, "url": url, "title": link, "verdict": "BLOCKED", "reason": None,
                        "judgment": False, "evidence": "(page could not be fetched: %s)"
                        % (p or {}).get("error", "not cached"), "evidence_source": "none",
                        "judged_from": "marketplace-cache", "record": None,
                        "needs_visual_check": False, "needs_human_ruling": False, "duplicate_of": None,
                        "accessed": TODAY, "surface": "marketplace" if kind == "app" else "marketplace-blog",
                        "note": "BLOCKED: the listing page did not return to a plain GET; see "
                                "sources/OPERATOR-TODO.md."})
            n += 1
            continue
        hay = M.hay_of(p)
        proc = bool(M.EYES.search(hay))
        if phase == 1 and proc:
            continue
        if phase == 2 and not proc:
            continue
        if proc:
            row = phase2_row(link, p, n, kind)
        else:
            fig_names = "; ".join(i["src"].split("/")[-1][:44] for i in (p.get("imgs") or [])[:5])
            row = {"n": n, "url": url,
                   "title": p["title"].replace(" | Creatio Marketplace", ""),
                   "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
                   "evidence": evidence_of(p, None), "evidence_source": "page text",
                   "judged_from": "marketplace-cache", "notation": None, "record": None,
                   "needs_visual_check": False, "needs_human_ruling": False, "duplicate_of": None,
                   "accessed": TODAY,
                   "surface": "marketplace" if kind == "app" else "marketplace-blog",
                   "note": ("Judged mechanically from the cached %s (judged_from: marketplace-cache): "
                            "the page carries no process-model language anywhere - not in its body "
                            "text, not in any image alt text, not in any image file name, and not the "
                            "'Business Process Element' compatibility tag - so it publishes no process "
                            "artefact at all. The AI screen over the same text found %s. Its figures "
                            "are the listing's own product screenshots and marketing images (%s)."
                            % ("listing page" if kind == "app" else "blog page",
                               ("an AI/LLM token" if re.search(M.AI, hay, re.I) else
                                ("only a soft token (%s)" % ", ".join(sorted(set(re.findall(M.SOFT, hay, re.I))))[:80]
                                 if re.search(M.SOFT, hay, re.I) else "no AI/LLM token")),
                               fig_names))}
        new.append(row)
        n += 1

    print("phase %d: %d rows to append (population would become %d)" % (phase, len(new), len(rows) + len(new)))
    for r in new[:4]:
        print("   n=%-5d %-9s %-16s %-60s %r" % (r["n"], r["verdict"], str(r["reason"]),
                                                 r["url"][:60], r["evidence"][:60]))
    if phase == 2:
        bad = [r["url"] for r in new if r["reason"] not in
               ("E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate")]
        if bad:
            print("  !! rows with an out-of-list reason:", bad)
    if "--write" not in sys.argv:
        print("preview only")
        return
    allrows = dict(rows)
    for r in new:
        allrows[r["n"]] = r
    ordered = [allrows[k] for k in sorted(allrows)]
    with LEDGER.open("a", encoding="utf-8") as fh:
        for r in new:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with FRONTIER.open("w", encoding="utf-8") as fh:
        for r in ordered:
            fh.write(r["url"] + "\n")
    hdr = dict(header)
    hdr["population_size"] = len(ordered)
    if phase == 2:
        hdr["enumeration_method"] = header["enumeration_method"] + (
            " THIRD SURFACE - marketplace.creatio.com: enumerated from the catalogue's own JSON "
            "endpoint, seen in the browser's network panel and then used headlessly: POST "
            "/search/ai with ai_filter null reports numFound = 524, the exact unfiltered total "
            "(ledgers/_creatio_mp_crawl.py; every listing page is server-rendered HTML, so all 524 "
            "were cached and judged from the cache). The platform's own is_ai flag marks 26 items; "
            "it was NOT used to narrow the population, and the cross-check is recorded: all 26 "
            "flagged items also carry a hard AI token in their page text, while the same screen "
            "finds AI tokens in many unflagged items, so nothing AI-related was excluded by the "
            "facet. The blog index (marketplace.creatio.com/blog?page=N) walks to exhaustion at 13 "
            "articles. Judgement split: the 394 items whose page carries no process-model language "
            "at all (body text, image alt text, image file names, the 'Business Process Element' and "
            "'AI Workflow' tags) are E0-no-artefact, judged mechanically from the cache. The 143 that "
            "do carry such language had EVERY figure looked at by eye - 883 non-chrome figures tiled "
            "into contact sheets by ledgers/_creatio_mp_sheets.py and read, plus the 46 figures that "
            "sheet's noise filter had dropped, tiled and read separately by "
            "ledgers/_creatio_mp_noise_sheet.py (they are marketing cards and product banners, no "
            "diagram among them). What that pass found: 22 listings publish a Creatio "
            "process-designer model (BPMN 2.0) - rows with reason E2-no-ai-element - and NONE of "
            "them contains an AI/LLM element inside the model; the remaining 121 publish no process "
            "model at all, their figures being product screenshots and marketing cards, with named "
            "non-BPMN artefacts among them (Zapier's and Make.com's proprietary iPaaS editors, "
            "Creatio's campaign designer - square step tiles, dotted connectors and a SAVE/CANCEL "
            "toolbar, distinct from the process designer's event circles, gateway diamonds and "
            "SAVE/RUN/CANCEL/ACTIONS toolbar - InterWeave's architecture box diagrams, Kanban boards, "
            "a whiteboard, a relationship map, a Power BI report, a call-script decision tree). The "
            "surface therefore yields no AI-in-process example, which is a result and not a gap: the "
            "marketplace apps that ARE AI ('AI Skill', 'AI Agent', 'AI Workflow' tags) expose their "
            "AI as a chat panel or a card, never as an element inside a published process model.")
    ftr = dict(footer)
    ftr["rows"] = len(ordered)
    ftr["include"] = sum(1 for r in ordered if r["verdict"] == "INCLUDE")
    ftr["uncertain"] = sum(1 for r in ordered if r["verdict"] == "UNCERTAIN")
    ftr["exclude"] = {c: sum(1 for r in ordered if r.get("reason") == c) for c in
                      ("E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate")}
    ftr["blocked"] = sum(1 for r in ordered if r["verdict"] == "BLOCKED")
    ftr["judgment_exclusion_share"] = round(
        sum(1 for r in ordered if r.get("judgment") is True and r["verdict"] == "EXCLUDE") / max(1, len(ordered)), 4)
    ftr["visual_check_rows_remaining"] = sum(1 for r in ordered if r.get("needs_visual_check"))
    ftr["rows_judged_from_bfs_cache"] = sum(1 for r in ordered if r.get("judged_from") == "bfs-cache")
    ftr["figures_looked_at"] = {"contact_sheet": 883, "noise_sheet": 46, "zoomed_at_native_size": 78}
    ftr["surfaces"] = {s: sum(1 for r in ordered if r.get("surface") == s) for s in
                       ("academy", "academy-outside-scope", "creatio.com-landing", "marketplace",
                        "marketplace-blog")}
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(hdr, ensure_ascii=False) + "\n")
        fh.write(json.dumps(ftr, ensure_ascii=False) + "\n")
    print("appended %d rows + header + footer; population now %d" % (len(new), len(ordered)))


if __name__ == "__main__":
    main()
