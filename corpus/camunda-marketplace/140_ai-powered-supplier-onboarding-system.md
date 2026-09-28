---
n: 140
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI-Powered Supplier Onboarding System
url: https://marketplace.camunda.com/apps/636570/ai-powered-supplier-onboarding-system
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagrams published as the listing's own assets (Camunda Web Modeler, element templates applied); no .bpmn downloadable. Read natively: the main process runs start 'Form Submitted' -> 'Process Documents' -> 'Check vendor duplicity' -> gateway 'Duplicate?' -> 'Compliance Checks' -> 'Finance Checks' -> gateway 'Approved?' -> 'Push to Vendor Master' -> gateway -> 'Send email' -> end 'Supplier Onboarded'; the called processes 'Process Documents' (ad-hoc sub-process) and 'Email Communication' are published as their own diagrams.
bpmn_evidence_quote: "Process Documents"
ai_evidence: The AI work is drawn inside the processes, not only described: the ad-hoc sub-process 'Process Documents' carries the violet agentic-AI glyph and holds the document tasks ('Check required docs', 'Process ISO', 'Process HACCP', 'Process Insurance', 'Process Banking Proof', 'Process Tax Compliance'), and 'Dates Standardization' and 'Name normalization' carry the same glyph; the 'Email Communication' ad-hoc sub-process contains the task 'AI Mail Draft'. The page's own copy claims the same: 'AI and DMN rules classify suppliers by risk level' and 'AI drafts supplier communication emails'.
ai_evidence_quote: "AI and DMN rules classify suppliers by risk level, check sanction lists, and flag license expiries"
artefacts:
  screenshot: 140_ai-powered-supplier-onboarding-system.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/636570/overview/img5193696540788166540-2x.png 1100x202 and screenshot/img1414786421743902000.png 1197x327, img13499044469888451945.png 632x362); native reads at full size
---

## What the page shows

Acheron's AI-Powered Supplier Onboarding System (blueprint, partner). The listing publishes four diagrams: the main onboarding flow from submitted form to onboarded supplier, the 'Process Documents' ad-hoc sub-process that extracts and validates supplier documents, the 'Email Communication' ad-hoc sub-process that drafts and sends supplier mail, and the compliance/finance validation sub-processes with their human 'Verify ... Details' tasks.

## Observations (description only, no interpretation)

- **AI activity - function:** document extraction and validation across six document types; data standardization ('Dates Standardization', 'Name normalization'); drafting supplier emails ('AI Mail Draft').
- **AI activity - element type:** ad-hoc sub-processes carrying the violet agentic-AI glyph (BPMN `adHocSubProcess`), and ordinary `serviceTask`s carrying the same glyph ('Dates Standardization', 'Name normalization', 'AI Mail Draft'), with orange document glyphs on the six extraction tasks.
- **Authority - downstream:** 'Push to Vendor Master' (the ERP write), 'Send email' and the mail tasks inside 'Email Communication'.
- **Authority - data:** supplier documents (tax forms, banking details, certifications); the page says the blueprint unifies supplier data across ERP and CRM.
- **Authority - control:** the gateways 'Duplicate?', 'Approved?' and the two 'Required?' gates inside the compliance and finance sub-processes.
- **Authority - control (human):** the user tasks 'MDM Review', 'Verify Finance Details' and 'Verify Compliance Details' - each sits behind a 'Required?' gateway that answers Yes, i.e. the human is invoked on the exception path.
- **Input provenance:** the submitted supplier form and the documents uploaded to it.
- **Guards present:** duplicate detection before compliance, and the 'Required?' human-verification gates on the compliance and finance paths; the page's benefit list frames this as 'keeping humans in the loop for critical exceptions'.
- **Prompt / model detail visible:** none - no model, provider or prompt is named anywhere on the page; the AI tasks are identified only by their template glyphs and labels.

## Notes for the researcher

The clearest 'AI inside the process' artefact in this batch: two ad-hoc sub-processes carrying the violet agentic-AI glyph, one of them reached from the main flow as a called task. The listing never names a model or provider, so the AI binding is evidenced by element-template glyphs plus the page's own AI claims - worth a look if the method wants provider attribution.
