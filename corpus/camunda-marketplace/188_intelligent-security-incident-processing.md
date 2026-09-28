---
n: 188
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Intelligent Security Incident Processing
url: https://marketplace.camunda.com/apps/830621/intelligent-security-incident-processing
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN published twice over: as the overview asset (a wide canvas strip) and as two downloadable .bpmn files. Read from the XML: process 'AI Incident Investigation Blueprint' - 'Start Process' -> callActivity 'Call Scenario Processor' -> serviceTask 'AI INCIDENT PLANNER' -> subProcess 'Prepare Incident Context' -> subProcess 'Analyze Threat (AI)' -> exclusiveGateway 'Mindestens 1 Tool ausgewählt?' -> adHocSubProcess 'AI Investigation Tools' -> gateways -> 'Content Enrichment' -> userTask 'ISMS Incident Review' -> 'Initialize Timestamp' -> 'Ticket Creation' -> 'ISO Post Evaluate' -> 'Create Audit Sections' -> userTask 'ISMS Audit Report' -> 'Prozess Ende', with abort paths ('Vorgang abbrechen', 'Kein DSGVO Ticket', 'Ticket Creation Skipped'). Second file: process 'Start Incident Type Selection' - 'KI Agent: Szenario generieren' -> userTask 'ISMS Scenario Type Selection' -> scriptTask 'Incident Type'. The published figure renders the same flow; inside 'AI Investigation Tools' it shows the sequence 'Threat Intelligence Lookup' -> 'AI Interpretation Layer' -> 'Parse Threat AI Analysis' with 'check_gdpr_relevance' and 'Asset Infrastructure Lookup' beside it.
bpmn_evidence_quote: "AI INCIDENT PLANNER"
ai_evidence: Ten AI-bound elements inside the process, all bound to the AWS Bedrock connector's element template (zeebe:modelerTemplate io.camunda.connectors.aws.bedrock.v1, modelerTemplateVersion 3, task type io.camunda:aws-bedrock:1): 'AI INCIDENT PLANNER', 'Prepare Incident Context', 'Analyze Threat (AI)', 'Threat Interpretation AI', 'Short_Description AI', 'llm_explanation AI', 'write_iso_report', 'check_gdpr_relevance', the adHocSubProcess 'AI Investigation Tools', and - in the second file - 'KI Agent: Szenario generieren'. In the figure these tasks carry the violet Camunda AI glyph. The .bpmn also carries the LLM prompt text itself: the GDPR-relevance step's German instructions (DSGVO only if personal data is explicitly mentioned; 'RISIKO-EINSCHÄTZUNG: LOW, MEDIUM oder HIGH') and the ISO-27001 report structure for the audit-log output.
ai_evidence_quote: "AI-powered security incident analysis and decisions"
artefacts:
  screenshot: 188_intelligent-security-incident-processing.png
  archive: null
  bpmn_xml: 188_intelligent-security-incident-processing.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/830621/overview/img8555919120970456732-2x.png, 1100x205) and of both .bpmn files reached through the listing's own Modeler import links; the image read natively at full size (plus a 4x crop of the ad-hoc sub-process), the two XML files read directly
---

## What the page shows

The Intelligent Security Incident Processing blueprint (Ilume Informatik AG, solution accelerator, tags 'BPMN, Agentic AI orchestration, AI Services'). Incoming security events are structured, planned and analysed by Bedrock-bound AI steps, checked for GDPR relevance, enriched, reviewed by a human, and turned into an ISO-27001 audit report and ticket.

## Observations (description only, no interpretation)

- **AI activity - function:** a chain of LLM calls: plan the investigation ('AI INCIDENT PLANNER'), interpret the threat ('Analyze Threat (AI)', 'Threat Interpretation AI'), decide GDPR relevance ('check_gdpr_relevance'), write the ISO report and audit sections ('write_iso_report', 'Create Audit Sections'), and explain the outcome ('llm_explanation AI', 'Short_Description AI').
- **AI activity - element type:** serviceTask, subProcess and adHocSubProcess elements bound to the AWS Bedrock outbound connector template (io.camunda:aws-bedrock:1), i.e. connector calls to a hosted LLM service, not a Camunda AI Agent element. A second file adds 'KI Agent: Szenario generieren' in the incident-intake process.
- **Authority - downstream:** the AI output is the incident assessment itself: it feeds the tool-selection gateway, the GDPR-relevance branch, the audit-report generation and the ticket content.
- **Authority - data:** script tasks extract the incident's IPs and ISO-text fragments ('Extract Incident IP', 'Find IP in Topic', 'Extract ISO Mapping', 'Evaluate ISO Controls'); the LLM receives the incident input plus a threat-intelligence lookup against external sources.
- **Authority - control:** gateways 'Mindestens 1 Tool ausgewählt?' and 'DSGVO Untersuchung starten?' route the flow, and script tasks score it ('Detect Real Incident', 'Confidence Calculation', 'Process Failure Check').
- **Authority - control (human):** userTasks 'ISMS Incident Review' and 'ISMS Audit Report' (plus 'Manager Entscheidung' gateways and 'ISMS Scenario Type Selection' in the second file) hold the AI's output for human sign-off.
- **Input provenance:** the raw security alert (raw_alert), external threat-intelligence data via an HTTP connector, and the asset registry lookup.
- **Guards present:** tool-selection and GDPR gateways, abort and skip paths ('Vorgang abbrechen', 'Kein DSGVO Ticket', 'Ticket Creation Skipped', 'DSGVO Skipped'), and explicit confidence/plausibility scripts.
- **Prompt / model detail visible:** the German prompt text is inside the .bpmn for the GDPR and ISO-report steps (output-format rules: plain text only, no Markdown, no JSON, exact headings '1. VORFALL:', '2. UMGEHEND AUSFÜHREN:', '3. ISO 27001 MAPPING:', '---' after section 3); the model id itself is not visible in the published fields.

## Notes for the researcher

The page's own copy almost avoids the word AI - its only AI mention is the details line 'AI-powered security incident analysis and decisions' - while the published process is the most AI-dense artefact in this source so far: ten Bedrock-bound elements, two of them containers, plus the German prompt text embedded in the file. Another instance of the .bpmn-first reading rule (cf. n=136). Two details worth the researcher's eye: (1) the published figure labels an element 'AI Interpretation Layer' inside 'AI Investigation Tools', and no element carries that name in the downloadable .bpmn, so figure and file are not the same revision of the blueprint; (2) the listing's 'Watch Demo' resource is a youtu.be link, which was not opened.
