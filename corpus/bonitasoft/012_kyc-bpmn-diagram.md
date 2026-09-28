---
n: 0
url: https://www.ofelia.com/blog-article/the-power-of-automated-kyc-transforming-banking-and-insurance-e0c48
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page's AI/ML mention describes document comparison inside the KYC process
  (authenticity checks on passports) and the bpmn-js diagram draws a "Verify identity" /
  "Check background" task: is that AI element inside the process, i.e. does this page meet
  the artefact criteria?
bpmn_evidence: >-
  The page publishes a diagram, and it is BPMN 2.0. The only textual proof is the SVG's
  own provenance comment, quoted verbatim from the file: `<!-- created with bpmn-js /
  http://bpmn.io -->`. It is the only one of the page group's SVGs that carries it. The
  canvas is 2492x270 and its labels (read from the pixels, because the export draws text
  as paths) are the sequence "Customer onboarding request pending | Collect customer
  information | Verify identity | Perform standard due diligence | Check background |
  Integrate data | Approve final data | Create account | Customer successfully onboarded",
  plus the branch "Perform enhanced due diligence | Review data".
ai_evidence: >-
  The AI mention is in the article prose around the diagram, not in the diagram's labels.
  Quoted verbatim from the page: "Artificial intelligence (AI) and machine learning tools
  can analyze customer data and compare submitted documents—such as passports or driver's
  licenses—against official databases". That describes AI/ML doing the document comparison
  inside the KYC scrutiny the drawn tasks ("Verify identity", "Check background") stand
  for - which is exactly the ambiguity the question records.
artefacts:
  - screenshot: 012_kyc-bpmn-diagram.png
  - figure: the page's own BPMN 2.0 diagram (diagram KYC.svg)
capture_quality: marginal
capture_width_px: 1400
capture_height_px: 152
---

## What the page shows

The page publishes a BPMN 2.0 diagram: the figure "diagram KYC.svg" opens with the tool provenance comment "<!-- created with bpmn-js / http://bpmn.io -->" (the only one of the 202 site SVGs that does) and its 2492x270 canvas carries the labelled sequence "Customer onboarding request pending | Collect customer information | Verify identity | Perform standard due diligence | Check background | Integrate data | Approve final data | Create account | Customer successfully onboarded" plus the branch "Perform enhanced due diligence | Review data". The page's AI mention puts AI/ML document comparison inside that scrutiny ("Artificial intelligence (AI) and machine learning tools can analyze customer data and compare submitted documents - such as passports or driver's licenses - against official databases to confirm their authenticity"), which is what makes this a ruling for the researcher rather than a clean exclusion.

## Observations

- Notation: BPMN 2.0, rendered by bpmn-js.
- Evidence looked at: diagram KYC.svg looked at in full at 2492x270, and the page's own prose read for its AI mention.
- This is the pixel-level finding; the same wording is the ledger row for this page, so the two cannot disagree.

## Notes for the researcher

One of the five www.ofelia.com pages ruled UNCERTAIN in this source (records 012-016). The other 127 judged site pages are E0/E1/E2/E3 ledger rows without records.
