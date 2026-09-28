---
n: 005
record: 005
url: https://docs.flowx.ai/5.9/docs/platform-deep-dive/integrations/custom-agent-node
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: The AI element (the Custom Agent node) is documented and pictured inside the vendor's Integration Designer canvas, which this source's own glossary calls "Not a BPMN process"; the only BPMN claim is one sentence saying BPMN processes invoke such workflows through the Start Integration Workflow action. Collectable, or is this an AI node in a workflow (a different artefact class)?
page_publishes: ui-canvas
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from another named source (the site's own glossary, or a label read in this page's figure).
screenshot: 005_custom-agent-node.png
artefacts:
  - screenshot: 005_custom-agent-node.png
bpmn_evidence: |
  The page's 11 figures are screenshots of the Custom Agent node inside the vendor's Integration Designer
  canvas - a canvas this source's own glossary says is 'Not a BPMN process': ca1 "Custom Agent Node",
  ca2 "Add Custom Agent", ca3 "Custom Agent AI Config", ca4 "Agent Tools Tab", ca-add-tool-menu "The Add
  tool menu on the Custom Agent node, offering MCP Server, Workflow, Function, Web Search, and
  Built-in ...", ca5 "Agent Node Logs". The BPMN link is one sentence, under Related resources: "For
  BPMN process workflows, use the Start Integration Workflow action to invoke workflows that contain
  Custom Agent nodes."
  So the AI element is documented and pictured, but inside a workflow canvas, not inside a BPMN diagram;
  the only BPMN-specific claim is that BPMN processes invoke it through the action documented in record
  003.
ai_evidence: |
  The node is an LLM agent: "Select Custom Agent from the available node types", its response is written
  to process data ("responseKey ... The key in the process data where the agent's response will be
  stored"), it is configured with Instructions/Context, MCP servers, knowledge-base retrieval and
  workflow tools, and it can "state its reasoning before it answers". The tool menu its own figure shows
  is "MCP Server, Workflow, Function, Web Search, and Built-in Tools".
note: |
  Read from the page's own published markdown twin (https://docs.flowx.ai/5.9/docs/platform-deep-dive/integrations/custom-agent-node.md), and - where a Mintlify component renders differently from the twin - from the page as displayed in the browser, on 2026-09-25; nothing on this page was paraphrased. The capture next to this record is a contact sheet of the page's 11 figures. The page publishes no BPMN-notation diagram: its 11 figures are node-configuration panels, not a process diagram. The evidence above is quoted verbatim from that page.
