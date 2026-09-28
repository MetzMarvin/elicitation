# Known-positive artefacts (seeded recall test)

Nine AI-enabled BPMN artefacts found by hand in July 2026. The captures were deleted in
commit `f58422d` because the screenshots were too pixelated to analyse; the *findings*
below are still valid and the pages are known to contain qualifying artefacts.

They have two jobs now:

1. **Re-capture targets.** Each must re-enter the corpus through the normal Pass 2 census
   of its source, captured at the resolution rules of `prompts/02_source-census.md`
   (original asset or element screenshot at a large viewport, never a scaled-down
   re-render). Do not shortcut them into the corpus by hand: they should be found.
2. **A seeded recall test.** Pass 3 checks each of these URLs against the census ledgers.
   A known positive that the census did not surface, or surfaced as an exclusion, is
   direct evidence of an agent recall failure - the one failure mode that is otherwise
   invisible. Report every miss; do not quietly add the item.

Census agents: do **not** read this file. It would bias your enumeration and destroy the
test. Only Pass 3 and the researcher use it.

| # | Source | What it showed | URL |
|---|---|---|---|
| 01 | Camunda (vendor blog) | AI Task Agent looping over an ad-hoc sub-process of tools (Slack / email / get more info) in a message-delivery process | https://camunda.com/blog/2025/05/benefits-bpmn-ai-agents/ |
| 02 | FireStart (vendor product page) | German-labelled quote process: AI classification service task feeding a gateway, human review of the AI-prefilled offer | https://www.firestart.com/en/ai-workflows |
| 03 | IBM Developer (watsonx Orchestrate tutorial) | Whole BPMN order-processing flow converted into one autonomous agent owning all six steps as tools | https://developer.ibm.com/tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/ |
| 04 | IBM BAMOE (vendor docs, tech preview) | Dedicated native "AI Agent Task" BPMN node type, Langflow-connected | https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=ia-using-ai-agent-tasks-in-workflows-tech-preview (announcement: https://community.ibm.com/community/user/blogs/adarsh-v-k/2025/11/28/introducing-ai-agent-task-advanced-ai-integration) |
| 05 | Camunda (vendor blog, MCP post) | AI Agent with MCP tools in an ad-hoc sub-process, human confirmation gate on the filesystem tool | https://camunda.com/blog/2025/09/camunda-model-context-protocol-practical-overview/ |
| 06 | IFS Cloud (vendor docs) | "IFS AI task" node between two API tasks, LLM rewriting a text field on an ERP record | https://docs.ifs.com/techdocs/26r1/040_tailoring/500_business_process_automation/050_business_process_modeling/070_ifs_ai/#example_use_case |
| 07 | UiPath Maestro (vendor docs) | Mixed robot / AI agent / human invoice pipeline, agent resolving discrepancies with a parallel human Action Center task | https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/how-to-complex-process |
| 08 | Frends iPaaS (vendor docs) | AI Connector verification feeding a human-vs-AI routing gateway, with an AI decision audit log | https://docs.frends.com/frends-development/agentic-ai/intelligent-ai-connector |
| 09 | UiPath Marketplace, opened in Studio Web | `serviceTask` bound to "Start and wait for agent"; agent (gpt-4o) prompt interpolates downloaded email attachments via `<files>{{ files }}</files>` | https://cloud.uipath.com/masterthesismetz/marketplace_/listings/summarize-outlook-email-attachments-with-ai |

Companion analysis of the UiPath mechanic (delegated implementation binding, no visual
signal at diagram level) survives in `notes/uipath-promotion-pattern/analysis.md` and is
unaffected by the deletion.

## Why the first captures failed

Screenshots were taken as scaled page renders rather than as the underlying asset: file
sizes ran from 10.7 KB to 224 KB, and task labels were unreadable at the level of detail
the pattern abstraction needs (element labels, task-type icons, implementation bindings).
The capture rules in `prompts/02_source-census.md` Step C exist to prevent exactly this:
prefer `.bpmn` XML, then the original image asset at native resolution, then an element
screenshot at a large viewport - and verify the pixel width of what actually landed on
disk before writing the record.
