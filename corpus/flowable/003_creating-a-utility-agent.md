---
n: 285
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
source_type: vendor docs
title: Creating a Utility Agent
url: https://documentation.flowable.com/latest/reactmodel/agent/example/utility-agent/index.html
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the page is a step-by-step tutorial that builds a BPMN process ("5.1 Create a New BPMN Process", "5.2 Add a Form for the Start Event", "5.4 Add a User Task to Show Results"); the AI Agent Task's property panel (figure 11) names the element and its binding. NOTE (sighted pass): no rendered process diagram is published - the figure whose alt reads "Empty BPMN process model" shows the model-creation dialog instead
bpmn_evidence_quote: "To use the agent now as part of a process or case, there is an Agent Task for BPMN and CMMN."
ai_evidence: an AI Agent Task drawn in the process, bound to a Utility Agent operation; the figure of the task's property panel is headed "AI Agent" and shows the operation and its parameter bindings
ai_evidence_quote: "Drag in an AI Agent Task . Configure it to: Use the Utility Agent and the Fetch Weather operation"
artefacts:
  screenshot: 003_agent-task-input-binding.png
  archive: 003_creating-a-utility-agent.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1166
capture_method: curl-equivalent (urllib) on https://documentation.flowable.com/latest/assets/images/11-agent-task-input-binding-affb5205491cd6c14f7f71fdae998076.png and .../12-agent-task-output-binding-9fbe902a086f121386422dca6c958e85.png, both 1166x803, src read from the page DOM; labels first read with RapidOCR, then confirmed by sight in the visual pass (elicitation-aa, 2026-09-25)
---

## What the page shows

A tutorial (marked "2025.1.01 +") in three parts: define a Utility Agent and its operation in
Flowable Design, test it, then "Step 5: Build a Process to Use the Agent". The process is named
"Fetch Typical Weather", has a start event carrying an input form, an AI Agent Task in the middle,
and a User Task afterwards. The captured figures are the property panel of that AI Agent Task
(input binding) and the same panel's output binding.

## Observations (description only, no interpretation)

- **AI activity - function:** answering a natural-language question with structured data - "Provide
  the typical weather for the given location and time of the year." returning temperature,
  precipitation and wind. The page's own framing: "you will create and use a Utility Agent in
  Flowable to handle a simple AI task".
- **AI activity - element type:** a dedicated BPMN element, the **AI Agent Task**, placed between
  the start event and a user task. The page names the element and the placement - "5.3 Add an AI
  Agent Task / Drag in an AI Agent Task" and "After the agent task, add a User Task". This is the
  case where the AI is a first-class element of the diagram, not only a task property.
- **Authority - downstream:** the process. The agent task's output parameters are bound to process
  variables and consumed by the following user task's form: "Bind output parameters to process
  variables" and "The User Task form will display the structured result."
- **Authority - data:** the agent operation's declared parameters. Input: `location`, `timeOfYear`
  (both String, "Map data to agent input parameter" in the captured figure). Output: `temperature`
  (Double), `precipitation`, `wind` (String), mapped "from output parameter to Process".
- **Authority - control:** the process controls the sequencing (start event form -> agent task ->
  user task). No gateway and no explicit guard on the agent task is shown; the human step follows
  the AI step rather than gating it.
- **Input provenance:** the start event's form fields. "5.2 Add a Form for the Start Event / Attach
  to the start event a form called Weather Information Input Form with the following fields:
  Location (Text), Time of Year (Text)"; then "Bind input parameters to form fields".
- **Guards present:** none observed in the figures. The only gate-like device in the tutorial is the
  interactive Test tab, which is outside the process.
- **Prompt / model detail visible:** the system and user messages of the operation are published
  verbatim: "Provide the typical weather for the given location and time of the year." and "What is
  the typical weather for ${location} in ${timeOfYear}?" with the note "You can reference input
  parameters using ${parameterName}". The page says the response is "returned by the LLM" but names
  no provider, model or version.

## Notes for the researcher

**Sighted confirmation (visual pass elicitation-aa, 2026-09-25).** All 13 figures on the page were
fetched from the live page and looked at; each is a legible 1166x803 Flowable Design or Flowable Work
UI capture. The verdict is confirmed, with one correction to the evidence above.

*Correction:* the page publishes **no rendered BPMN process diagram**. The figure whose `alt` reads
"Empty BPMN process model" (`9-process-create-...png`) actually shows the "Open or create a new
model" dialog - Model Type "Process", Name "Fetch Typical Weather", Key `fetchTypicalWeather`, Palette
type "Flowable Work BPMN" - not a canvas. The census's `bpmn_evidence` field leaned on that alt text,
so it overstated what the page shows. Everything else in the tutorial is likewise a panel or form:
app creation, agent definition, type selection, operation, input parameters, output parameters,
prompts, test result, input form, the two agent-task binding tabs, and the resulting Work task form.

What the page *does* establish, and what makes it an INCLUDE, is the AI element inside the process
evidenced through its **binding panel**: figures 11 and 12 are the property panel of the process
element `AgentTask_1`, headed "AI Agent" with the subtitle "Get typical weather (AgentTask_1)" and the
tabs Agent model / Operation / Input / Output.

- Input tab: `${location}` maps to agent input parameter `location` (String); `${timeOfYear}` maps to
  `timeOfYear` (String).
- Output tab: agent outputs `temperature` (Double), `precipitation` (String), `wind` (String) map to
  the process variables `temperature`, `precipitation`, `wind`.
- Figure 14 closes the loop from the process side: the Flowable Work task form "Display result" shows
  Temperature 20.50, Precipitation moderate, Wind light breeze - i.e. the AI Agent Task's output
  arriving in the downstream human task.

So this is the method's "AI element visible only as a task property or implementation binding" case:
the element is named "AI Agent Task" and typed as such, bound to the Utility Agent's "Fetch weather"
operation, but the page never shows it on a canvas. A reviewer weighing this record should weigh prose
plus binding panels, not a diagram. The prose on its own certifies both BPMN and the AI element
("To use the agent now as part of a process or case, there is an Agent Task for BPMN and CMMN";
"Drag in an AI Agent Task. Configure it to: Use the Utility Agent and the Fetch Weather operation").

Method note, retained for audit: the census could not receive image content, so labels were first
obtained from RapidOCR; the sighted pass above supersedes that reading.
