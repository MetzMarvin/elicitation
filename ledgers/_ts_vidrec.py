"""trisotech: write the corpus records + poster captures for the AI-signal video pages.

One record per video page whose artefact is the recording (see the ledger header, video_family):
the page publishes only the recording's poster frame, so the record states what the poster shows,
quotes the page's own notation sentence and AI sentence, and says plainly that the recording was not
watched and that live demonstrations are not covered by the paired slide deck.

  python ledgers/_ts_vidrec.py            -- write the records + captures listed in TABLE
"""
import glob, json, os, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(ROOT)
RAW = os.path.join(ROOT, "trisotech.raw")
VID = os.path.join(RAW, "vid")
CORP = os.path.join(BASE, "corpus", "trisotech")

# slug -> (record number, page title, deck slug or "", bpmn sentence, ai sentence, question)
TABLE = {
 "ai-agents-in-healthcare": (9, "AI Agents You Can Actually Trust in Healthcare: From Opaque to Governed Automation (webinar recording)", "ai-agents-in-healthcare-presentation",
  "Using BPM+ standards, orchestration, decisions, and AI capabilities are kept separate.",
  "Healthcare AI is only as valuable as the trust clinicians and patients place in it. The barrier isn't capability, it's reliability and governance.",
  "the recording likely shows BPM+ models with AI kept as a separate, governed element; no such model is published as an image."),
 "ai-driven-healthcare-orchestration": (10, "AI-Driven Healthcare Orchestration: Insights from Dana-Farber and Veteran Health Administration (webinar recording)", "ai-driven-healthcare-orchestration-presentation",
  "Hosted by Denis Gagne, CEO and CTO of Trisotech, this session delves into the integration of BPM+ Health and AI to automate clinical workflows and improve decision-making processes.",
  "Explore the transformative potential of AI in healthcare orchestration with insights from renowned leaders at Dana-Farber Cancer Institute and the Veteran Health Administration.",
  "the abstract places AI inside BPM+ Health clinical workflows; no model is published as an image on the page."),
 "ai-fhir-and-bpm-in-suicide-prevention": (11, "AI, FHIR, and BPM+ in Suicide Prevention: From Early Detection to Coordinated Care (webinar recording)", "ai-fhir-and-bpm-in-suicide-prevention-presentation",
  "This session explores how AI-powered monitoring, BPM+ visual standards, and FHIR interoperability work together to detect suicidal ideation early and coordinate interventions across emergency departments, mental health specialists, and primary care.",
  "This session explores how AI-powered monitoring, BPM+ visual standards, and FHIR interoperability work together.",
  "this is the recording of the talk whose written version (the blog 'Suicide Prevention with Modeling Tools') is already in the corpus as record 001 with a BPMN figure carrying an LLM task; the recording itself may show more of the same models."),
 "automation-of-loan-origination": (12, "Automation of Loan Origination using Process and Decision Services (webinar recording)", "automation-of-loan-origination-presentation",
  "Learn how using the Trisotech Digital Enterprise Suite (DES) allows you to visually define processes and decisions that are directly automated to streamline loan origination processes.",
  "As presented by: Brian Stucky, Quicken Loans, Team Lead - Rocket Technology Ethical AI, MISMO - Residential Governance Board",
  "the talk is about automating loan origination from visual process and decision models; no model is published as an image on the page."),
 "clinician-centric-data-and-ai-integration-in-healthcare": (13, "Clinician-Centric Data and AI Integration in Healthcare (webinar recording)", "clinician-centric-data-and-ai-integration-in-healthcare-presentation",
  "",
  "Gain insights into the orchestration of data, knowledge and AI in support of decision-making in healthcare.",
  "the abstract is about orchestrating AI inside clinical decision-making; no model is published as an image on the page."),
 "enterprise-ai-in-2026": (14, "Enterprise AI in 2026: From Experimentation to Operational Value (webinar recording)", "enterprise-ai-in-2026-presentation",
  "The page's own text speaks of decision models rather than naming a notation.",
  "By 2026, enterprise AI is no longer about experimentation or bold claims of full autonomy. The focus has shifted to building systems that work in production, under real constraints, and at enterprise scale.",
  "the talk covers putting enterprise AI into production under governance; whether models with AI-bound elements are shown is unresolved."),
 "generative-ai-and-regulatory-compliance": (15, "Generative AI and Regulatory Compliance Across the Enterprise (webinar recording)", "generative-ai-and-regulatory-compliance-presentation",
  "",
  "Generative AI can aid businesses, especially in the banking and finance industry, to meet regulatory compliance challenges by extracting important terms, creating concept models, and generating rules.",
  "the abstract says GenAI creates concept models and rules; whether those are drawn as BPMN/DMN elements is unresolved."),
 "harness-genai-and-agentic-ai": (16, "DecisionCAMP2025: Harness GenAI and Agentic AI without Repeating Yesterday's Flaws (webinar recording)", "harness-genai-and-agentic-ai-presentation",
  "Standard BPM+ process, case, and decision models remain the clearest way to express intent, assign accountability, and embed human judgment.",
  "Marketing now trumpets generative AI (GenAI) assistants and loosely coupled agent swarms (Agentic AI) as the next leap.",
  "the abstract argues for BPM+ models as the harness for GenAI/agentic AI, so models with AI elements are very likely on screen."),
 "hl7-ai-challenge-winners": (17, "Unleashing Innovation: HL7 AI Challenge Winners Transforming Healthcare with Standards-Based AI (webinar recording)", "hl7-ai-challenge-winners-presentation",
  "Trisotech demonstrates how deterministic BPM+ models, HL7 integration patterns, and explicit decision logic create AI agents that remain explainable, governable and clinically trustworthy.",
  "This on-demand session highlights the inaugural HL7 AI Challenge winners, organizations proving that healthcare AI can be powerful and trustworthy when built on open standards.",
  "the winning entry is explicitly about BPM+ models driving AI agents; the models themselves are not published as images on the page."),
 "it-takes-all-kinds-of-ai-and-humans-to-make-good-business-decision": (18, "It takes all kinds of AI and Humans to make Good Business Decision (webinar recording)", "it-takes-all-kinds-of-ai-and-humans-to-make-good-business-decision-presentation",
  "",
  "In today's rapidly evolving markets, the integration of human insight with advanced AI technologies is crucial for making sophisticated, timely decisions.",
  "the talk is about combining human and AI decision-makers; whether a model with AI task performers is shown is unresolved."),
 "knowledge-worker-copilot-in-the-loop": (19, "Knowledge Worker Copilot in the Loop: AI-Powered Contract Workflows (webinar recording)", "knowledge-worker-copilot-in-the-loop-presentation",
  "In this webinar, we will demonstrate how the KW-Copilot keeps a living memory of every evolving case, capturing events, documents, and stakeholder roles, then orchestrates BPM+ workflows and AI reasoning to automate follow-ups.",
  "Discover how the Knowledge Worker Copilot streamlines contract and regulation-driven work.",
  "the abstract says the copilot orchestrates BPM+ workflows and AI reasoning, so a model with an AI element is likely on screen."),
 "low-code-neuro-symbolic-agents": (20, "Low Code Neuro-Symbolic Agents: Prompt Engineering through Process and Decision Orchestration (webinar recording)", "low-code-neuro-symbolic-agents-presentation",
  "",
  "This presentation aims to provide a comprehensive understanding of a form of neuro-symbolic AI, prompt engineering, and the role of process and decision orchestration.",
  "the talk is about neuro-symbolic AI driven by process and decision orchestration; no model is published as an image on the page."),
 "mastering-decision-orchestration": (21, "Mastering Decision Centric Orchestration: Balancing Human Insight and AI Automation (webinar recording)", "mastering-decision-orchestration-presentation",
  "",
  "We will explore how various types of artificial intelligence (AI) support decision automation, with a particular emphasis on the crucial role of context.",
  "the talk is about AI types supporting decision automation; whether a drawn decision or process model is shown is unresolved."),
 "optimizing-preoperative-assessments": (22, "Optimizing Preoperative Assessments: From Rules to Decisions. From Decisions to Value. (webinar recording)", "optimizing-preoperative-assessments-presentation",
  "In this session, we will introduce and demonstrate visual modeling and automation for preauthorization based on a set of international open standards called BPM+. Automated BPM+ visual models can help to achieve these goals, with SmileCDR providing and collecting the standardized data.",
  "The same models can be used to risk stratify patients, to prepare dashboards to quickly visualize data and to prepare data for predictive analytics (AI).",
  "the abstract says the same BPM+ visual models feed predictive analytics; the models are not published as images on the page."),
 "the-role-of-genai": (23, "Turn Unstructured Data into Business Actions: The Role of GenAI (webinar recording)", "the-role-of-genai-presentation",
  "",
  "Large Language Models (LLMs) hold the key to unlocking their potential - when used right.",
  "the talk is about turning unstructured text into business actions with LLMs; whether the models that orchestrate them are shown is unresolved."),
 "who-made-that-decision-governing-decisions-in-the-age-of-ai-agents": (24, "Who Made That Decision? Governing Decisions in the Age of AI Agents (webinar recording)", "who-made-that-decision-governing-decisions-in-the-age-of-ai-agents-presentation",
  "Using decision-centric orchestration and BPM+ concepts, we will examine a practical framework for classifying AI participation across a spectrum that includes AI tools, assistants, performers, agents, and AI orchestrators.",
  "We explore how organizations can move beyond model-centric governance toward decision-centric governance.",
  "the abstract classifies AI participation by role (tools, assistants, performers, agents, orchestrators) inside BPM+ orchestration, so a model with AI performers is likely on screen; 48 of the paired deck's 52 slides carry AI text, so the deck row is where this talk should be judged."),
 "ai-and-bpm": (25, "AI and BPM (Sandy Kemsley vlog, 8 minutes)", "",
  "",
  "there's a lot of interest in this intersection between AI and BPM. Now, I've been at a couple of conferences in the last month ... And it's not just one answer, because there's several places where AI and Process Management come together.",
  "the vlog is about where AI and BPM meet, and the transcript goes through a 'process modeling scenario' where models exist but no model is published as an image on the page; this is the only notation-adjacent video page with no paired slide deck."),
}


def main():
    made = []
    for slug, (num, title, deck, nbpmn, ai, question) in sorted(TABLE.items(), key=lambda kv: kv[1][0]):
        hits = glob.glob(os.path.join(VID, slug[:60] + "__*.jpg"))
        cap = ""
        if hits:
            from PIL import Image
            src = max(hits, key=os.path.getsize)
            cap = "%03d_%s-poster-frame.png" % (num, slug)
            Image.open(src).convert("RGB").save(os.path.join(CORP, cap))
        body = []
        body.append("# %s — UNCERTAIN (trisotech)\n" % title)
        body.append("url: https://www.trisotech.com/%s/" % slug)
        body.append("accessed: 2026-09-25")
        body.append("title: %s" % title)
        body.append("record: %03d\n" % num)
        body.append("bpmn_evidence:")
        if cap:
            body.append("  The artefact is the recording. The page publishes one content image, the video's poster")
            body.append("  frame (%s), viewed at full size; no diagram is published." % cap.split("-")[0])
        else:
            body.append("  The artefact is the recording; the page publishes no diagram image.")
        if nbpmn:
            body.append("  The page's own notation sentence: \"%s\"" % nbpmn)
        if deck:
            body.append("  The same talk is also published as a slide deck at /%s/, which" % deck)
            body.append("  is judged on its own page and its own slides.")
            body.append("  A deck covers the slides, not the live demonstrations this source's webinars also run,")
            body.append("  so the recording can still hold a model the slides do not.")
        else:
            body.append("  There is no paired slide deck for this recording.")
        body.append("  The recording was not watched (operator rule for the video family: do not transcribe videos).\n")
        body.append("ai_evidence:")
        body.append("  \"%s\"\n" % ai)
        body.append("screenshot: %s" % cap if cap else "screenshot: null")
        body.append("capture_quality: null")
        body.append("")
        body.append("question for the researcher (needs_visual_check):")
        body.append("  The artefact is a video frame, and %s" % question)
        body.append("  Watch the recording, or rule that the recording family is out of scope for the corpus.")
        p = os.path.join(CORP, "%03d_%s.md" % (num, slug))
        open(p, "w", encoding="utf-8").write("\n".join(body) + "\n")
        made.append((num, slug, cap))
    for num, slug, cap in made:
        print("%03d %-58s %s" % (num, slug[:58], cap))


if __name__ == "__main__":
    main()
