---
n: 007
record: 007
url: https://docs.flowx.ai/5.1/setup-guides/access-management/roles-permissions-matrix
source: flowx-ai
surface: docs:flowx-ai:5.1
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: A permissions matrix is the whole page and the only artefact-like content is one row: the aiagent_edit permission "Controls visibility of config-time agents (AI Assistant, Analyst, Designer, Developer), the AI floating action button, the Chat UI component, and AI actions on BPMN nodes." This is the only place in the population where "AI actions on BPMN nodes" appears, and it publishes no diagram: collectable, or E0?
page_publishes: prose-binding
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from another named source (the site's own glossary, or a label read in this page's figure).
screenshot: 007_roles-permissions-matrix.png
artefacts:
  - screenshot: 007_roles-permissions-matrix.png
bpmn_evidence: |
  No artefact on the page (0 figures, 0 diagram fences): it is a permissions matrix, and the only
  process-relevant content is one row's description, which names AI actions attached to BPMN nodes:
  "Gated by the `aiagent_edit` permission. Controls visibility of config-time agents (AI Assistant,
  Analyst, Designer, Developer), the AI floating action button, the Chat UI component, and AI actions on
  BPMN nodes."
  This is the only place in the whole 945-page population where the phrase "AI actions on BPMN nodes"
  appears; the 5.9 version of the same page replaced that row with three "AI agents" rows and no longer
  carries it.
ai_evidence: |
  The AI surfaces the permission gates are named in the same row: "config-time agents (AI Assistant,
  Analyst, Designer, Developer), the AI floating action button, the Chat UI component, and AI actions on
  BPMN nodes". Three further rows gate "AI providers", "AI models" and "AI agents" per role.
note: |
  Read from the page's own published markdown twin (https://docs.flowx.ai/5.1/setup-guides/access-management/roles-permissions-matrix.md), and - where a Mintlify component renders differently from the twin - from the page as displayed in the browser, on 2026-09-25; nothing on this page was paraphrased. The capture next to this record is a text render of the page's own diagram/prose, because the page publishes its process as prose-binding rather than as a diagram image. The page publishes no BPMN-notation diagram: it carries no figure at all. The evidence above is quoted verbatim from that page.
