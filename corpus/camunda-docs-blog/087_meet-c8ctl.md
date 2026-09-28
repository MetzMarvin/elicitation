---
n: 517
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Meet c8ctl, the CLI that Makes Camunda 8 Feel Like Home"
url: https://camunda.com/blog/2026/03/meet-c8ctl/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': loan application process with credit score and risk gateways; the page names BPMN itself: 'You’ve got a Camunda 8.8+ cluster running. Maybe it’s local via c8run , maybe it’s in our SaaS environment—either works.'"
bpmn_evidence_quote: "You’ve got a Camunda 8.8+ cluster running. Maybe it’s local via c8run , maybe it’s in our SaaS environment—either works."
ai_evidence: "the page binds AI to a process element (Anthropic/Claude): 'c8ctl ships with an MCP (Model Context Protocol) proxy that bridges local AI tools—Claude Desktop, VS Code Copilot, or any MCP-compatible client to your Camunda'; the contact-sheet pass reads the captured figure as ai_visible=no"
ai_evidence_quote: "c8ctl ships with an MCP (Model Context Protocol) proxy that bridges local AI tools—Claude Desktop, VS Code Copilot, or any MCP-compatible client to your Camunda"
artefacts:
  screenshot: 087_meet-c8ctl.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1999
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Meet c8ctl, the CLI that Makes Camunda 8 Feel Like Home".
It opens on its subject directly: "With this post, we have provided a bit of a tutorial with examples of how to use and work with c8ctl. Grab a drink."
The line the record quotes on the AI element is: "c8ctl ships with an MCP (Model Context Protocol) proxy that bridges local AI tools—Claude Desktop, VS Code Copilot, or any MCP-compatible client to your Camunda 8 cluster:"

The captured figure is the page's 1999x575 asset with alt text "Image18". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=no, in its own words: loan application process with credit score and risk gateways

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "c8ctl ships with an MCP (Model Context Protocol) proxy that bridges local AI tools—Claude Desktop, VS Code Copilot, or any MCP-compatible client to your Camunda" - the AI-bearing element it names is Anthropic/Claude
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=no), in its words: loan application process with credit score and risk gateways
- **Authority - downstream:** the page: "Create a process instance using variables: c8 create pi --id=Process_loanR --variables'{"applicantID": 123456, "requestedLoan": 125000, "fullName": "Joyce Jones", "annualSalary": 455000, "applicantEmail": "<a href="mailto:joyce.johnson@camunda.com">joyce.johnson@camunda.com</a>"}' This returns the"
- **Authority - data:** the page: "Switch to JSON mode once, and every subsequent command emits machine-parseable output."
- **Authority - control:** the page: "check for a specific error message (in this case error messages including Exception ), use c8 search inc --ierrorMessage='*Exception*' , which provides this for output"
- **Input provenance:** the page: "You’ve modeled your BPMN, crafted your DMN, and polished all your forms."
- **Guards present:** the page: "Do you have any building blocks (you might know about these, but check them out in our documentation )?"
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1999x575 asset, downloaded at w=1400 and stored as 087_meet-c8ctl.png; the contact-sheet reading of the same asset is class bpmn / ai_visible no. Figure choice: alt 'Image18' + sheet note 'loan application process with credit score and risk gateways'.
