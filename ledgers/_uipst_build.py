"""Build records, frontier and ledger for the UiPath Studio template gallery (7 Maestro BPMN templates).

Population fixed by the researcher on 2026-10-11: Studio Web > Templates, Project type 'Maestro BPMN',
search 'AI'. Solutions were exported by the researcher via 'Create in Local Workspace' into
corpus/uipath-marketplace/<solution>/. Run from the repo root: python -I ledgers/_uipst_build.py
"""
import json
import shutil
from pathlib import Path

ROOT = Path.cwd()
CORPUS = ROOT / "corpus" / "uipath-marketplace"
GALLERY = "https://cloud.uipath.com/masterthesismetz/studio_/templates"
ACCESSED = "2026-10-11"
SOURCE = "uipath-marketplace"
SOURCE_NAME = "UiPath Studio Web template gallery (Maestro BPMN solutions)"

ITEMS = [
    dict(
        slug="email-management", title="Email Management",
        bpmn="Email Management/Email Management Agentic Process/Email Management Process.bpmn",
        listing="The Email Management agent is designed to organize Outlook inboxes by categorizing and moving emails based on their content, urgency, and relevance.",
        used="Used in 754 automations",
        shows="Process 'Email Management Process': start, gateway 'Testing?', service task 'Read Latest Outlook Email' (or script 'Use Test Inputs'), service task 'Analyze & Categorize', service task 'Move Outlook Email', script 'Prepare Output', end.",
        ai="Service task 'Analyze & Categorize'; the solution ships agent project 'Email Management Agent' (agent.json, gpt-4o-2024-11-20) whose tools are processes 'ReadLatestOutlookEmail' and 'MoveOutlooEmail'.",
        ai_quote="categorize the email to the best of your ability into one of the below categories (and move to respective folders)",
        element_type="BPMN service task without binding in the shipped .bpmn; the agent is a separate project in the same solution.",
        downstream="Agent tools 'ReadLatestOutlookEmail' and 'MoveOutlooEmail' (RPA processes, Outlook 'Get Newest Email - Inbox' / 'Move Email'); in the BPMN, service task 'Move Outlook Email' follows the AI task.",
        data="Agent output schema: 'DestinationFolder' and 'Reasoning' (strings). Moves the email to a mailbox folder.",
        control="No gateway or human step consumes the output; 'Prepare Output' script, then end.",
        provenance="Latest email of the Outlook inbox (subject, body, message ID), or test subject/body from start-event variables.",
        guards="none observed",
        prompt="System prompt (agent.json): 'You are a helpful email management assistant.' Folders: High Priority, Meetings, Social, Finance, Project X, Customer Support, Notifications, Inbox. Step 6: 'run MoveOutlookEmail tool'.",
        notes="Service tasks in the .bpmn carry no implementation binding; the AI binding is established by the agent project shipped in the solution and the listing text.",
    ),
    dict(
        slug="summarize-outlook-email-attachments-with-ai", title="Summarize Outlook email attachments with AI",
        bpmn="Summarize Outlook email attachments with AI/Maestro - Process Attachments without RPA/Process.bpmn",
        listing="A Maestro pattern that retrieves the newest email from a specified Outlook folder, downloads its attachments, and uses an AI agent to generate a concise description of each file's contents.",
        used="Used in 158 automations",
        shows="Process: start, 'Get Newest Email' (Integration Service), 'Get Attachment List' (HTTP request), script 'Get the Array of Attachments', 'Download Email Attachments', service task 'Agent - Analyze Attachments', end.",
        ai="Service task 'Agent - Analyze Attachments' bound to Orchestrator.StartAgentJob (binding 'Agent - Analyze Attachments'); the agent's only tool 'Analyze Files' is described as analysing files 'with an LLM'.",
        ai_quote="Agent - Analyze Attachments",
        element_type="Service task with implementation Orchestrator.StartAgentJob; agent project in the same solution.",
        downstream="Agent tool 'Analyze Files' (internal tool: 'Analyze one or more files with an LLM to extract, synthesize, or answer queries about their content.').",
        data="Output schema 'file_Summaries': array of {filename, description}.",
        control="Agent task flows directly to the end event; no gateway or human step.",
        provenance="Attachments of the newest email in a configured Outlook folder.",
        guards="none observed",
        prompt="System prompt: 'You are a file description assistant. You receive one or more files and return a concise description of each file's contents.' Model gpt-4o-2024-11-20.",
        notes="",
    ),
    dict(
        slug="extract-meeting-minutes-and-action-items-from-transcripts", title="Extract Meeting Minutes and Action Items From Transcripts",
        bpmn="Extract Meeting Minutes and Action Items From Transcripts/Agentic Process/Process.bpmn",
        listing="Process meeting transcripts from Teams, Zoom, or Google Meet to extract structured summaries, decisions, risks, and action items, then generate Jira-ready task details for each follow-up.",
        used="Used in 111 automations",
        shows="Process: start, flow 'User Input' to 'Assign Value For Agent Input in BPMN' (RPA job), service task 'Communication Extractor Agent', service task 'JIRA Tickets Creation' (RPA job), end.",
        ai="Service task 'Communication Extractor Agent' (Orchestrator.StartAgentJob); agent.json: 'You are an AI meeting-analysis agent.' No tools configured.",
        ai_quote="You are an AI meeting-analysis agent. Your job is to extract structured insights from raw meeting transcripts.",
        element_type="Service task with implementation Orchestrator.StartAgentJob.",
        downstream="Service task 'JIRA Tickets Creation' starts RPA process 'Create JIRA Ticket' ('Deserialize JSON', 'For Each', 'Create Issue') over the agent's 'jira_tickets' output.",
        data="Agent output: 'agentRawOutput' and 'agentRawOutput_Markdown' (strings) with summary, decisions, risks, action items, Jira tickets.",
        control="No gateway or human step between the agent and Jira issue creation.",
        provenance="Meeting transcript ('Raw transcript text from Teams, Zoom, or Google Meet.'), assigned by RPA job 'Assign Value For Agent Input in BPMN' after the 'User Input' start.",
        guards="none observed",
        prompt="'Do not add information that is not explicitly stated in the transcript.' User prompt: 'Please process the following meeting transcript ... {{meeting_transcript}}'. Model gpt-4o-2024-11-20.",
        notes="",
    ),
    dict(
        slug="insurance-claims-adjudication-and-settlement", title="Insurance Claims Adjudication & Settlement",
        bpmn="Insurance Claims Adjudication & Settlement/Claims Adjudication Process/ClaimsAdjudication.bpmn",
        listing="An agentic process built with Maestro, modeled using BPMN to coordinate policy validation, fraud scoring, payout estimation, reinsurance checks, and settlement issuance.",
        used="Used in 21 automations",
        shows="Message start 'Claim Ready for Adjudication', agent validation, gateway 'Coverage Valid?', parallel fraud scoring / payout estimation / reinsurance check, user task 'Claims Officer Review & Final Decision', full or partial settlement payment with payment-confirmation waits.",
        ai="Four service tasks with Orchestrator.StartAgentJob and tag caseTaskType=agent: 'Validate Claim Against Policy Terms & Limits Agent', 'Fraud Scoring Agent (patterns, history, anomalies)', 'Estimate Claim Payout Agent (rules engine + adjuster input)', 'Check Reinsurance Applicability Agent (treaty thresholds)'.",
        ai_quote="Fraud Scoring Agent (patterns, history, anomalies)",
        element_type="Service tasks with implementation Orchestrator.StartAgentJob, no agent bound (no agent project in the solution, output 'sampleOutput').",
        downstream="Not visible on the page: agents have no bound tools.",
        data="not visible on the page",
        control="'Coverage Valid?' after validation agent; 'Fraud Risk?' (High -> user task 'Fraud Investigator Review'); all branches join before user task 'Claims Officer Review & Final Decision', which precedes payments.",
        provenance="Message start event 'Claim Ready for Adjudication'; data mappings not modelled.",
        guards="User tasks 'Fraud Investigator Review' (High risk) and 'Claims Officer Review & Final Decision' before payment; timer SLA boundaries escalate.",
        prompt="not visible on the page",
        notes="Industry template: agent tasks are placeholders with no agent bound (a blank scaffold whose tasks are AI-bound by type).",
    ),
    dict(
        slug="claim-submission-and-status-provider-to-payer", title="Claim Submission & Status (Provider to Payer)",
        bpmn="Claim Submission & Status (Provider to Payer)/Claim Submission and Status Process/ClaimSubmissionStatus.bpmn",
        listing="An agentic process built with Maestro, modeled using BPMN to manage claim validation, eligibility checks, clearinghouse submission, payer acknowledgments, and status tracking.",
        used="Used in 13 automations",
        shows="Message start 'Claim Ready for Submission', parallel pre-submission validations (coding agent, eligibility service task, completeness agent), 'Submit Claim to Clearinghouse (837 EDI)', 'Transmit Claim to Payer', payer response handling with 'Rejection Reason Parsing & Worklisting Agent'.",
        ai="Three service tasks with Orchestrator.StartAgentJob: 'Validate Coding & Modifiers Agent (ICD, CPT, DRG)', 'Check Completeness Agent (attachments, clinical notes, required fields)', 'Rejection Reason Parsing & Worklisting Agent'.",
        ai_quote="Rejection Reason Parsing & Worklisting Agent",
        element_type="Service tasks with implementation Orchestrator.StartAgentJob, no agent bound.",
        downstream="Not visible on the page: agents have no bound tools.",
        data="not visible on the page",
        control="'Coding Valid?' (Invalid -> user task 'Coder Correction'); completeness agent error boundary 'Missing Data' -> user task 'Staff Correction'; merge -> automated clearinghouse submission and payer transmission; denial parsing agent -> end 'Claim Rejected: Payer Denial'.",
        provenance="Message start 'Claim Ready for Submission'; payer denial message ('Payer Denied Claim') feeds the parsing agent; data mappings not modelled.",
        guards="Error boundary to human 'Staff Correction'; 'Coder Correction' on invalid coding.",
        prompt="not visible on the page",
        notes="Industry template: agent tasks are placeholders with no agent bound.",
    ),
    dict(
        slug="insurance-first-notice-of-loss-fnol", title="Insurance First Notice of Loss (FNOL)",
        bpmn="Insurance First Notice of Loss (FNOL)/First Notice of Loss Process/FirstNoticeOfLoss.bpmn",
        listing="An agentic process built with Maestro, modeled using BPMN to guide claim intake, coverage checks, fraud screening, claim record creation, and adjuster assignment.",
        used="Used in 12 automations",
        shows="Message start 'Claim Notification Received (FNOL)', user task 'Collect Incident Details & Evidence', 'Validate Policy Agent', parallel coverage / fraud / enrichment agents, 'Evaluation Outcome', 'Fraud Investigator Review', 'Assign Claims Adjuster', claim record creation, acknowledgement to policyholder.",
        ai="Four service tasks with Orchestrator.StartAgentJob: 'Validate Policy Agent', 'Coverage Validation Agent', 'Fraud Screening Agent', 'Loss Intake Data Enrichment Agent'.",
        ai_quote="Loss Intake Data Enrichment Agent",
        element_type="Service tasks with implementation Orchestrator.StartAgentJob, no agent bound.",
        downstream="Not visible on the page: agents have no bound tools.",
        data="not visible on the page",
        control="'Policy Active?' after the policy agent; 'Evaluation Outcome' after the join (Coverage Excluded -> end; Fraud Suspicion -> 'Fraud Investigator Review'; else -> user task 'Assign Claims Adjuster'), then record creation and notifications.",
        provenance="Message start 'Claim Notification Received (FNOL)' and user task 'Collect Incident Details & Evidence'.",
        guards="User tasks 'Fraud Investigator Review' and 'Assign Claims Adjuster' before claim record creation; timer SLA boundaries escalate.",
        prompt="not visible on the page",
        notes="Industry template: agent tasks are placeholders with no agent bound.",
    ),
    dict(
        slug="patient-appointment-scheduling", title="Patient Appointment Scheduling",
        bpmn="Patient Appointment Scheduling/Patient Appointment Scheduling Process/PatientAppointmentScheduling.bpmn",
        listing="An agentic process built with Maestro, modeled using BPMN to manage scheduling requests, provider availability checks, insurance eligibility, waitlist handling, and confirmations.",
        used="Used in 11 automations",
        shows="Message start 'Patient Appointment Request Received', user task 'Capture Patient Preferences', 'Check Provider Availability', alternatives agent with patient response wait, parallel 'Reserve Appointment Slot' and 'Verify Insurance Eligibility Agent', 'Eligibility Result', confirmation generation and sending.",
        ai="Two service tasks with Orchestrator.StartAgentJob: 'Offer Alternatives / Add to Waitlist Agent', 'Verify Insurance Eligibility Agent'.",
        ai_quote="Offer Alternatives / Add to Waitlist Agent",
        element_type="Service tasks with implementation Orchestrator.StartAgentJob, no agent bound.",
        downstream="Not visible on the page: agents have no bound tools.",
        data="not visible on the page",
        control="Alternatives agent -> event-based gateway 'Patient Response' (message 'Patient Accepts Alternative' or timer). Eligibility agent -> join -> gateway 'Eligibility Result' (Not Eligible -> cancel; Eligible -> 'Generate Appointment Confirmation', 'Send Confirmation to Patient').",
        provenance="Message start 'Patient Appointment Request Received' and user task 'Capture Patient Preferences'.",
        guards="Timer boundary 'Eligibility Check Delayed' on the eligibility agent -> end 'Escalated: Eligibility SLA Breach'.",
        prompt="not visible on the page",
        notes="Industry template: agent tasks are placeholders with no agent bound. Downloaded first by the researcher.",
    ),
]


def q(s):
    return json.dumps(s, ensure_ascii=False)


frontier, rows = [], []
header = {
    "type": "header", "source": SOURCE, "source_name": SOURCE_NAME, "census": False, "population_size": 7,
    "enumeration_method": "Researcher-prescribed population (2026-10-11): Studio Web Templates tab, filter 'Project type: Maestro BPMN', search term 'AI'; gallery shows '1 - 7 / 7'. Not a census of the gallery; supplements ledgers/uipath-marketplace.jsonl (marketplace.uipath.com sitemap census). Solutions exported by the researcher via 'Create in Local Workspace'.",
    "entry_points": [GALLERY], "access": "free-account", "date_start": ACCESSED, "agent_model": "claude-opus-5-5",
    "browser_tool": "Claude in Chrome extension (gallery listing text); local .bpmn / agent.json files",
    "queries": ["AI"], "note": "Researcher pre-vetted all 7 as in scope.",
}
rows.append(header)

for i, it in enumerate(ITEMS, 1):
    n = f"{i:03d}"
    bpmn_name = f"{n}_{it['slug']}.bpmn"
    shutil.copyfile(CORPUS / it["bpmn"], CORPUS / bpmn_name)
    rec = f"{n}_{it['slug']}.md"
    url = f"{GALLERY}#{it['slug']}"
    frontier.append(f"{url}\t{it['title']}")
    md = f"""---
n: {i}
source: {SOURCE}
source_name: {SOURCE_NAME}
source_type: vendor marketplace
title: {q(it['title'])}
url: {GALLERY}
accessed: {ACCESSED}
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: {q(it['ai'])}
ai_evidence_quote: {q(it['ai_quote'])}
artefacts:
  screenshot: null
  archive: {q(str(Path(it['bpmn']).parts[0]) + '/')}
  bpmn_xml: {bpmn_name}
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "{it['listing']}"

Card footer: "Created by UiPath", "{it['used']}", type "Solution".

{it['shows']}

## Observations (description only, no interpretation)

- **AI activity - function:** {it['ai']}
- **AI activity - element type:** {it['element_type']}
- **Authority - downstream:** {it['downstream']}
- **Authority - data:** {it['data']}
- **Authority - control:** {it['control']}
- **Input provenance:** {it['provenance']}
- **Guards present:** {it['guards']}
- **Prompt / model detail visible:** {it['prompt']}

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `{Path(it['bpmn']).parts[0]}/`. {it['notes']}
"""
    (CORPUS / rec).write_text(md, encoding="utf-8")
    rows.append({
        "n": i, "url": url, "title": it["title"], "verdict": "INCLUDE", "reason": None, "judgment": False,
        "evidence": it["ai_quote"], "record": f"corpus/{SOURCE}/{rec}", "needs_visual_check": False,
        "needs_human_ruling": False, "question": None, "accessed": ACCESSED,
        "note": "Pre-vetted by the researcher; gallery has no per-template URL, fragment is the record slug.",
    })

rows.append({"type": "footer", "date_end": ACCESSED, "rows": 7, "include": 7, "uncertain": 0, "exclude": {},
             "blocked": 0, "judgment_exclusion_share": 0.0, "self_audit_flips": 0, "status": "COMPLETE"})
(ROOT / "ledgers" / "uipath-studio-templates.frontier.txt").write_text("\n".join(frontier) + "\n", encoding="utf-8")
with open(ROOT / "ledgers" / "uipath-studio-templates.jsonl", "w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print("ok", len(ITEMS))
