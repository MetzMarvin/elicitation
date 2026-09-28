---
n: 006
record: 006
url: https://docs.flowx.ai/5.9/ai-platform/patterns/agent-typologies
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Ten agent patterns as prose; no artefact on the page. One of them states the process binding in words: "the surrounding BPMN process presents it to a person as a User Task - the agent workflow and the human step share the same process context." Collectable without a diagram?
page_publishes: prose-binding
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from another named source (the site's own glossary, or a label read in this page's figure).
screenshot: 006_agent-typologies.png
artefacts:
  - screenshot: 006_agent-typologies.png
bpmn_evidence: |
  No artefact on the page at all (0 figures, 0 diagram fences, no .bpmn model): ten agent patterns as
  prose, each with a "How to build it" paragraph. One of them publishes the process binding in words:
  "How to build it: a Condition node detects the escalation case, and the surrounding BPMN process
  presents it to a person as a User Task - the agent workflow and the human step share the same process
  context." The page points at the node palette instead of drawing anything: "The implementations below
  use the nodes as they exist in the platform - see AI node types for the full palette."
ai_evidence: |
  The AI elements are the ten typologies themselves (Document extractor and validator, Grounded
  generator, Classifier and router, Voice intake, Predictive scorer, Privacy-guarded extractor,
  Knowledge-validated extractor, Relationship reasoner, Human handoff) and the node palette they are
  built from. The page's closing pointer is "Integrating agents in BPMN processes".
note: |
  Read from the page's own published markdown twin (https://docs.flowx.ai/5.9/ai-platform/patterns/agent-typologies.md), and - where a Mintlify component renders differently from the twin - from the page as displayed in the browser, on 2026-09-25; nothing on this page was paraphrased. The capture next to this record is a text render of the page's own diagram/prose, because the page publishes its process as prose-binding rather than as a diagram image. The page publishes no BPMN-notation diagram: it carries no figure at all. The evidence above is quoted verbatim from that page.
