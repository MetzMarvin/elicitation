---
n: 24
source: ifs-cloud-docs
source_name: IFS Cloud (technical documentation, Business Process Automation)
source_type: vendor documentation
title: IFS AI - Technical Documentation For IFS Cloud
url: https://docs.ifs.com/techdocs/26r1/040_tailoring/500_business_process_automation/050_business_process_modeling/070_ifs_ai/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: downloadable BpmnSmartEditorAITaskExample.bpmn (bpmn 2.0 XML, 6881 bytes) with one <bpmn:process>, 3 <bpmn:serviceTask>, 4 <bpmn:sequenceFlow>, 1 <bpmn:startEvent>, 1 <bpmn:endEvent>, and a full BPMNDiagram/BPMNPlane/BPMNShape/BPMNEdge section; the same task XML is also printed inline in the page body
bpmn_evidence_quote: "<bpmn:serviceTask id=\"Activity_1dvrfcu\" name=\"IFS AI: Smart Editor Model\" camunda:class=\"com.ifsworld.fnd.bpa.delegate.IfsAiDelegate\">"
ai_evidence: an IFS AI service task bound to business use case smart-editor-generation and model SMART_EDITOR_IMPROVE_COMMAND, wired between an IFS API read task and an IFS API update task
ai_evidence_quote: "When a new record is created in an entity, the system invokes an ML model to enhance the clarity, grammar, and overall quality of the text added under the description."
artefacts:
  screenshot: corpus/ifs-cloud-docs/003_ifs-ai-task-smart-editor-ai-section.png
  archive: null
  bpmn_xml: corpus/ifs-cloud-docs/003_ifs-ai-task-smart-editor.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: 1624
capture_method: chrome-devtools-mcp, evaluate_script fetch() of the linked .bpmn resource (status 200, text/xml) plus get_network_request filePath on the figure asset
---

## What the page shows

`070_ifs_ai/` documents the IFS AI Task node type. The page prints the task's generated XML
inline and links the complete example model as
`resources/BpaSmartEditorAITaskExample.bpmn`, which was fetched and read.

The example process is linear: `<bpmn:startEvent>` then three `<bpmn:serviceTask>` elements
in sequence with four `<bpmn:sequenceFlow>` connections, then one `<bpmn:endEvent>`. The
three tasks are named, verbatim:

1. `IFS API: Read Regulatory Body`, `camunda:class="com.ifsworld.fnd.bpa.IfsProjectionDelegate"`,
   `ifsBpaProjectionAction` = `READ`, `ifsBpaProjectionName` = `RegulatoryBodyHandling`,
   `ifsBpaProjectionEntitySetName` = `RegulatoryBodySet`.
2. `IFS AI: Smart Editor Model`,
   `camunda:class="com.ifsworld.fnd.bpa.delegate.IfsAiDelegate"`, with
   `ifsBpaAiBusinessUseCase` = `smart-editor-generation`,
   `ifsBpaAiModelName` = `SMART_EDITOR_IMPROVE_COMMAND`,
   `ifsBpaAiOutputVariableName` = `SMART_EDITOR_IMPROVE_COMMAND_Response`, and an
   `ifsBpaAiModelParameters` map whose keys are `page_name`, `note_field_name` and `value`.
3. `IFS API: Update Regulatory Body`, `ifsBpaProjectionAction` = `UPDATE`,
   `ifsBpaProjectionName` = `RegulatoryBodyHandling`.

The page's own walkthrough of the same example, verbatim: "Use Case: When a new record is
created in an entity, the system invokes an ML model to enhance the clarity, grammar, and
overall quality of the text added under the description. Pre-requisites: ADCOM component,
and the smart_editor_generation business use case should be enabled in IFS Cloud." The
step-by-step guide reads: "Step 01: Create a new Workflow with the process key,
BpaSmartEditorAITaskExample. Step 02: Add an IFS API Task to read the projection,
RegulatoryBodyHandling. Step 03: Add an IFS AI Task from the menu, to invoke the ML model.
Select the Business Use Case as smart-editor-generation, and the Model Name as
SMART_EDITOR_IMPROVE_COMMAND. Under parameters, pass the RegulatoryBodyDesc variable as
input for the model. Filter Raw Output to retrieve the content from the response, and store
it in the variable, Model_Content. Step 04: Add an IFS API Task to update the description,
RegulatoryBodyDesc, with the generated response using variable, Model_Content. Step 05:
Validate the BPMN, save and deploy the Workflow."

## Observations (description only, no interpretation)

- **AI activity - function:** the task invokes an ML model to improve text. Page, verbatim:
  "the system invokes an ML model to enhance the clarity, grammar, and overall quality of
  the text added under the description."
- **AI activity - element type:** a dedicated `serviceTask` named `IFS AI: Smart Editor
  Model` whose implementation class is `com.ifsworld.fnd.bpa.delegate.IfsAiDelegate`; in
  the designer it is added "from the menu" as an "IFS AI Task".
- **Authority - downstream:** model invocation only, as configured: business use case
  `smart-editor-generation`, model `SMART_EDITOR_IMPROVE_COMMAND`. No tool list, connector
  or sub-process is present in the model.
- **Authority - data:** the AI task writes the variable
  `SMART_EDITOR_IMPROVE_COMMAND_Response` (`ifsBpaAiOutputVariableName`); the walkthrough
  then reads a field of that output into a variable named `Model_Content` ("Filter Raw
  Output to retrieve the content from the response, and store it in the variable,
  Model_Content"), and the following `IFS API: Update Regulatory Body` task writes
  `RegulatoryBodyDesc` back to entity set `RegulatoryBodySet`.
- **Authority - control:** the process is linear. No gateway, no human task and no
  conditional branch appears in the example model (there is no `exclusiveGateway` in the
  XML); the human step is upstream, outside the model, as the trigger ("When a new record is
  created in an entity").
- **Input provenance:** the record's description field `RegulatoryBodyDesc`, read out of
  `RegulatoryBodySet` / projection `RegulatoryBodyHandling` by the preceding IFS API task;
  page states "pass the RegulatoryBodyDesc variable as input for the model".
- **Guards present:** an information banner about token consumption: "An information banner
  is provided on top of the Properties panel, and the Inspect BPA pane to notify on the
  toke[n consumption]" and "AI models consume IFS tokens for every invocation. Similarly,
  tokens are consumed during troubleshooting, in production, and on each retry attempt with
  an IFS AI Task." BPMN deployment validations are referenced: "Refer the Deployment
  Validations page for more details on BPMN validations when using the IFS AI Task." No
  human review step is present in the model.
- **Prompt / model detail visible:** model and business use case names only
  (`SMART_EDITOR_IMPROVE_COMMAND`, `smart-editor-generation`) plus the parameter map keys
  `page_name`, `note_field_name`, `value`; output routing via
  `ifsBpaAiOutputVariableName` and `ifsBpaAiOutputs`. No prompt text is shown.

## Notes for the researcher

- The page additionally describes the IFS AI Task's Properties panel and its fields
  (figures `ifs_ai_task_property_panel.png`, `properties_parameters.png`,
  `properties_show_raw_outputs.png`, `properties_outputs.png`, `properties_log_errors.png`,
  `properties_show_status_code.png`, `auth_section.png`), and a second figure set for the
  walkthrough (`example_step03_subsec.png`, `example_step04_ifsapiupdate.png`,
  `example_step05_ai_section.png`).
- Extra capture stored alongside this record:
  `003_ifs-ai-task-smart-editor-use-case.png` (the `use_case_example.png` asset, 1164 px,
  below the 1400 px rule, hence not the record's `screenshot`).
- `archive` is `null`: the page HTML is the documentation shell plus this page; the page is
  reproducible at the URL above and the decisive evidence is the `.bpmn` model, which is
  captured in full.
- The same page also carries the token-consumption notice discussed on the "IFS AI Task
  Considerations" page; treat the two pages as one narrative when reconciling.
