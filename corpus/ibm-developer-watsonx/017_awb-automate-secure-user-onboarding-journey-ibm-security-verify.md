---
n: 1417
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Automate a secure user onboarding journey using IBM Security Verify - the page's flow figure, drawn as a plain flowchart with an imported .bpmn file behind it"
url: https://developer.ibm.com/tutorials/awb-automate-secure-user-onboarding-journey-ibm-security-verify/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's Step 7 has the reader import a .bpmn file into IBM Security Verify's Flow designer ('upload the .bpmn file located at flows > ldap_to_okta_migration') and then edit named nodes of it ('Select the SetVars function', 'Select the Ask for username task', 'Select the Resolve IdP task'), so the model behind the page's flow figure is a BPMN 2.0 file. But the figure as published carries no BPMN markers: its terminators are 'Start' and 'Stop' stadiums, its decisions are plain diamonds labelled True/False, and there are no events, task types, gateways or pools. Is this a BPMN 2.0 model rendered in the vendor's own house style, so the corpus records it, or a non-BPMN process drawing that E1-not-bpmn excludes? (Separately: the page contains no AI, LLM or agent mention at all, so E2-no-ai-element cannot be applied as written - E2 requires quoting the AI mention being dismissed and there is none to quote, the same code-list gap as record 003.)"
needs_visual_check: false
bpmn_evidence: "png, the page's first figure fetched at full size (908x662) and viewed; the page's other 25 figures are IBM Security Verify console screenshots (branding theme, flow-designer menu, OIDC identity-provider form, agent type list), checked as SHEET_BPMN141701 and at full size (Picture-11 = the branding theme console). the page's first figure is a process flow drawn in dark-teal boxes on white: an 'Start' stadium terminator, a 'Username entered' rectangle, a decision diamond 'Check migratedtoOkta' with True and False edge labels, a 'Redirect to Okta login page for authentication' rectangle, a 'Redirect to login page' rectangle, a decision diamond 'Authenticate against Active Directory', a rounded 'Create user in Okta & update migratedtoOkta value to true' box, a 'User Landing page' rectangle and a 'Stop' stadium terminator, with free-text edge labels ('Successful Authentication', 'Unsuccessful Authentication'). The tutorial's Step 7 tells the reader to import a .bpmn file into IBM Security Verify's Flow designer and then to 'Select the SetVars function', 'Select the Ask for username task' and 'Select the Resolve IdP task' - so the artefact behind this drawing is a BPMN file, while the drawing itself carries no BPMN events, task types, gateways or pools. The page has no AI, LLM or agent mention anywhere (its digest AI-token list is empty). I hesitated between a BPMN model rendered in the vendor's own style and an ordinary flowchart; hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Click the Import icon (adjacent to the Create flow button). Enter the details and upload the .bpmn file located at flows > ldap_to_okta_migration"
ai_evidence: "there is no AI, LLM or agent element anywhere on the page and none drawn inside the figure: the page's digest carries an empty AI-token list, and its figure and text are entirely about identity orchestration (Active Directory, Okta, OIDC, LDAP migration). So this is the same code-list situation as record 003 - the artefact may be BPMN 2.0 and E2-no-ai-element cannot be applied as written, because E2 requires quoting the AI mention being dismissed and there is none to quote."
ai_evidence_quote: "Click the Import icon (adjacent to the Create flow button). Enter the details and upload the .bpmn file located at flows > ldap_to_okta_migration"
artefacts:
  screenshot: 017_1417F_flow.png
  assets: [017_1417F_flow.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/tutorials/awb-automate-secure-user-onboarding-journey-ibm-security-verify/` (api, ledger row n=1417), figure `figs/1417F_flow`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's first figure fetched at full size (908x662) and viewed; the page's other 25 figures are IBM Security Verify console screenshots (branding theme, flow-designer menu, OIDC identity-provider form, agent type list), checked as SHEET_BPMN141701 and at full size (Picture-11 = the branding theme console). the page's first figure is a process flow drawn in dark-teal boxes on white: an 'Start' stadium terminator, a 'Username entered' rectangle, a decision diamond 'Check migratedtoOkta' with True and False edge labels, a 'Redirect to Okta login page for authentication' rectangle, a 'Redirect to login page' rectangle, a decision diamond 'Authenticate against Active Directory', a rounded 'Create user in Okta & update migratedtoOkta value to true' box, a 'User Landing page' rectangle and a 'Stop' stadium terminator, with free-text edge labels ('Successful Authentication', 'Unsuccessful Authentication'). The tutorial's Step 7 tells the reader to import a .bpmn file into IBM Security Verify's Flow designer and then to 'Select the SetVars function', 'Select the Ask for username task' and 'Select the Resolve IdP task' - so the artefact behind this drawing is a BPMN file, while the drawing itself carries no BPMN events, task types, gateways or pools. The page has no AI, LLM or agent mention anywhere (its digest AI-token list is empty). I hesitated between a BPMN model rendered in the vendor's own style and an ordinary flowchart; hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

there is no AI, LLM or agent element anywhere on the page and none drawn inside the figure: the page's digest carries an empty AI-token list, and its figure and text are entirely about identity orchestration (Active Directory, Okta, OIDC, LDAP migration). So this is the same code-list situation as record 003 - the artefact may be BPMN 2.0 and E2-no-ai-element cannot be applied as written, because E2 requires quoting the AI mention being dismissed and there is none to quote.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
