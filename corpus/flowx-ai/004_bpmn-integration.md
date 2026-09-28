---
n: 004
record: 004
url: https://docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: The source's own doctrine page for agents in BPMN: three ASCII arrow sketches whose nodes are BPMN elements (Service Task, gateway) with the agent calls in them, plus prose binding AI to gateways and boundary error events. Collectable as an artefact, or is it a documentation page about a pattern rather than a process?
page_publishes: ascii-process
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from another named source (the site's own glossary, or a label read in this page's figure).
screenshot: 004_bpmn-integration.png
artefacts:
  - screenshot: 004_bpmn-integration.png
bpmn_evidence: |
  The page is the source's own doctrine for putting agents into a BPMN process, published as three ASCII
  arrow sketches whose nodes are BPMN elements:
    "User uploads document → Service Task calls extraction agent → Agent returns structured data →
     Process continues with data"
    "Process reaches gateway → Service Task calls decision agent → Agent returns recommendation →
     Gateway routes based on result"
    "Process collects data → Service Task calls generation agent → Agent produces content →
     Content stored/sent"
  The steps name the BPMN nodes: "Add a Service Task node to your process where you want to trigger the
  agent." The page also binds AI to gateways and to boundary events: "Make AI-powered decisions at
  process gateways", "Route to manual review if confidence is low", and the Error handling section
  ("Use boundary error events to catch agent failures"). No figure, no .bpmn model, and no BPMN 2.0
  notation: the artefacts are ASCII sketches.
ai_evidence: |
  "Integrate AI agents directly into your BPMN processes to automate document processing, make
  intelligent decisions, and generate content without user interaction." The four capabilities listed
  are the AI elements: "Automate document processing in the background", "Make AI-powered decisions at
  process gateways", "Generate content automatically within workflows", "Validate data using AI
  analysis". Two integration methods are documented: the Start Integration Workflow action on a Service
  Task, and the Custom Agent Node in Integration Designer for "Multi-step AI workflows".
note: |
  Read from the page's own published markdown twin (https://docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration.md), and - where a Mintlify component renders differently from the twin - from the page as displayed in the browser, on 2026-09-25; nothing on this page was paraphrased. The capture next to this record is a text render of the page's own diagram/prose, because the page publishes its process as ascii-process rather than as a diagram image. The page publishes no BPMN-notation diagram: it carries no figure at all. The evidence above is quoted verbatim from that page.
