# -*- coding: utf-8 -*-
"""Close out the loyjoy census: 122 non-/bpmn/ docs rows + 16 marketing rows,
the six records for the artefacts found outside /bpmn/, an extended header line
and the footer. Appends only; never rewrites earlier rows."""
import io, json, re, os, shutil
from PIL import Image

LED = 'ledgers/loyjoy.jsonl'
DATEC = '2026-09-24'

def load(p):
    b = open(p, 'rb').read()
    for enc in ('utf-8', 'cp1252', 'latin-1'):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    return b.decode('utf-8', 'replace')

def ptext(path):
    raw = load(path)
    body = re.sub(r'(?is)<(script|style|svg|noscript|head|nav|footer)[^>]*>.*?</\1>', ' ', raw)
    t = re.sub(r'\s+', ' ', re.sub(r'(?s)<[^>]+>', ' ', body))
    t = re.sub(r'&[a-z#0-9]+;', ' ', t)
    return re.sub(r'\s+', ' ', t)

def h1of(path):
    raw = load(path)
    m = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''

JUNK = re.compile(r'Skip to main content|LoyJoy Docs|On this page|^Previous |^Next |Getting Started'
                  r'|Copy page|Was this page helpful|\||Hinweis zum Alter|So funktioniert es|Einloggen'
                  r'|Book a demo|Sign in|Cookie|Newsletter')
def quote(t, lo=7, hi=45):
    for s in re.split(r'(?<=[.!?]) ', t):
        s = s.strip()
        if not (20 <= len(s) <= 320) or JUNK.search(s):
            continue
        w = s.split()
        if lo <= len(w) <= hi:
            return ' '.join(w[:25])
    return ' '.join(t.split()[:20])

# ---------------------------------------------------------------- rest pages
urls = json.load(io.open('ledgers/_lj_rest_urls.json', encoding='utf-8'))
NORAST = ('no process artefact: the page carries no figure at all - every inline <svg> on it is an '
          'interface glyph (viewBox "0 -960 960 960") or the one shared LoyJoy logo SVG, and no raster '
          'image is published on it; page text: "%s"')
FIG = ('no process artefact: the page\'s figures are %s - no process model is drawn anywhere on it; '
       'page text: "%s"')
CHAT = ('the artefact exists but is not BPMN 2.0 notation: the page\'s figure is a chat-interface '
        'screenshot (%s) - the rendering of a conversation with the end user, which rule 3 lists '
        'explicitly as a not-BPMN artefact, not a process model; page text: "%s"')
ARCH = ('the artefact exists but is not BPMN 2.0 notation: the figure is a technical architecture '
        'illustration, not a process model - labelled boxes "CUSTOMER QUESTION", "USER DATA", '
        '"CHATGPT AI", "EMBEDDING", "KNOWLEDGE DATABASE", "CONTEXT", "GENERATED ANSWER" joined by '
        'arrows; page text: "%s"')
CANVAS = ('the process figure on the page contains no AI/LLM element inside the process: %s; no AI, '
          'GPT, LLM or agent term appears on the page or in its figures; page text: "%s"')

# page -> (code, judgment, figure sentence or CANVAS structure)
REST = {
 10: ('E0', False, 'branding settings panels and chat-widget previews (branding_start, branding_header, branding_chatpreview, branding_bubble, branding_actioncall)'),
 11: ('E0', False, 'browser dev-tools screenshots (inspect, style, branding)'),
 13: ('E2', False, 'CANVAS|the figure is the editor canvas: start event -> module "#1 Email" -> module "#2 Snapshot" -> end event, beside the Modules palette (control flow: Loop, Decision gateway, Gateway; events: End, Timer start). The page\'s other figure is the Experiences menu'),
 14: ('E0', False, 'language-settings panels (select_language, default_language, translation_example, language_example_text)'),
 17: ('E0', False, 'module condition panels (condition_at_module, condition_in_module)'),
 20: ('E0', False, 'function dialogs (set_variable, condition_function, interpolation_function)'),
 21: ('E2', False, 'CANVAS|the figure is the editor\'s module list: "#1 Decision gateway" with Yes/No branches -> "#2 Variable" -> "#3 Automatic jump" -> "#4 Variable", plus module cards "#5 Questionnaire" / "#6 Product gallery" / "#7 Product gallery"'),
 22: ('E0', False, 'interface crops of the editor (copy_and_paste, refresh_preview, warning_bubble)'),
 23: ('E0', False, 'publish-dialog screenshots (publish_button, publish, change_background_imprint_url, settings1, settings2)'),
 29: ('E0', False, 'browser dev-tools screenshots (inspect, style, branding)'),
 30: ('E0', False, 'template-store screenshots (new_agent "Download template", choose_agent "Welcome to the LoyJoy Template Store")'),
 31: ('E0', False, 'custom-text tables (textold, textpic, textlanguage)'),
 32: ('E0', False, 'a version-history table (versions_tab)'),
 34: ('E2', True, 'CANVAS|the analytics figures embed a process diagram as the object being measured (modules "#1 ...", "Branches", "#4 End of chat", start and end events) and no element of it is an AI element'),
 35: ('E2', False, 'CANVAS|the dashboard figure embeds a process diagram (branches, module boxes, start and end events) as the object being measured, with no AI element in it'),
 36: ('E0', False, 'an overview dashboard and a date-filter panel (overview, dateFilter)'),
 37: ('E2', False, 'CANVAS|the figure is a heatmap drawn over a process: start event, "#1 Welcome" ... "#4 Thank you", "#5 Goodbye", end event, with per-step colour intensities'),
 38: ('E2', True, 'CANVAS|one figure embeds a process diagram as the object being measured; the remaining figures are charts, and one of them is an AI usage counter panel (number_ai: "Questions received", "Generated answers", "Fallback responses") that counts AI answers without placing an AI element in a process'),
 49: ('E0', False, 'a JavaScript-event configuration dialog (choose_event)'),
 50: ('E0', False, 'a ten-step WhatsApp sign-up wizard (step x10)'),
 52: ('E1', True, 'CHAT|the Knowledge search chat widget (a chat-interface screenshot)'),
 54: ('E1', True, 'CHAT|the Search module chat widget (a chat-interface screenshot)'),
 55: ('E1', True, 'CHAT|AI writing-assistant panels (magicfill, useGPT) and a chat-widget preview (shortarticle)'),
 56: ('E1', True, 'CHAT|the prompt-detail and knowledge-topic configuration screens (prompt_detail, topics)'),
 62: ('E0', False, 'knowledge-source crawl configuration screens (ai_sources_input_pdf, ai_sources_bulk_upload, ai_sources_sitemap, ai_sources_expert_settings, ai_sources_css_selectors, ai_sources_exclusions_rules, ai_sources_crawling_errors)'),
 64: ('E0', False, 'a live-chat template screen (live_template)'),
 65: ('E0', True, 'live-chat agent admin screens (agent_profile, agent_profile_settings, live_agent_switcher)'),
 66: ('E0', False, 'a live-chat archive screen (live_archive)'),
 67: ('E0', False, 'the products list screen (products_list)'),
 71: ('E0', False, 'an invitation/roles table (Invitation_Roles)'),
 72: ('E0', False, 'the sign-in screen (sign_in)'),
 73: ('E0', False, 'tenant-management tables (manage, manage_tenant, tenant_security)'),
 75: ('E0', False, '2FA / security-key screens (click_icon, account, security_keys, security_keys2)'),
 76: ('E0', False, 'widget card-settings screenshots (ValueProposition, shortButtons)'),
 78: ('E0', False, 'the alt-text management screen (manage_alt_text)'),
 80: ('E0', False, 'Azure portal screenshots (create_azure_ai)'),
 81: ('E0', False, 'Azure OpenAI / AI Foundry deployment screenshots (create_azure_openai_basics, create_azure_openai_deployment, azure_ai_foundry_deploy_models, azure_ai_foundry_create_content_filter, loyjoy_azure_settings)'),
 82: ('E0', False, 'a facts/dimensions dashboard (facts, dimensions)'),
 84: ('E1', True, 'CHAT|the Search chat widget (a chat-interface screenshot)'),
 89: ('E0', False, 'Excel/CSV export screenshots (csv_to_excel_tabs, csv_excel_1, csv_excel_2, csv_excel_3)'),
 92: ('E0', False, 'Facebook Messenger setup screenshots (image1 ... image19)'),
 96: ('E0', False, 'a location-parameter settings panel (location_param)'),
 99: ('E0', False, 'home-view settings screenshots (Homeviews)'),
100: ('E0', False, 'an export wizard with Excel screenshots (download_step1 ... download_step4)'),
103: ('E0', False, 'Claude / MCP connector screenshots (claude, edit)'),
104: ('E0', False, 'a SharePoint embed setting (sharepoint_embed)'),
105: ('E0', False, 'mobile-login security-key screens (acc1, security_keys3, security_keys4, security_keys5)'),
107: ('E0', False, 'pause-state screens (pause, paused)'),
108: ('E0', False, 'voice-intro and browser-test settings (voice_intro, browser_test)'),
110: ('E0', False, 'secret-manager screens (add_secret, paste_secret)'),
111: ('E0', False, 'an identity-provider connection screen (connect_identity_provider)'),
112: ('E0', False, 'SMTP settings with an email icon (email_icon)'),
113: ('E0', False, 'plan/pricing and Stripe screenshots (manage, LoyJoy_Plan, book_plan, stripe)'),
117: ('E0', False, 'a D-ID AI-avatar settings panel (did_agent_id_setting)'),
119: ('E0', False, 'template-store cards (get_template, see_template)'),
}

def rest_row(n, i):
    url = urls[i - 1]
    hp = 'ledgers/loyjoy.raw/html_rest/%03d.html' % i
    t = ptext(hp)
    q = quote(t)
    title = h1of(hp) or url.rstrip('/').rsplit('/', 1)[-1]
    if i == 85:   # /guides/central_ai/ - the GPT-gateway process
        return {"n": n, "url": url, "title": title, "verdict": "INCLUDE",
                "judgment": False,
                "evidence": ('AI elements inside the depicted process: the figure (alt "Central AI '
                             'Agent", title "Central AI Agent Configuration in LoyJoy Backend") shows a '
                             'message start event -> module "#1 Simple message" -> module "#2 GPT '
                             'gateway" -> exclusive gateway with flows "Branch 1/2/3" -> modules "#3 GPT '
                             'Knowledge", "#5 GPT Follow-up question", "#7 GPT Smalltalk" -> end event; '
                             'page text: "%s"' % q),
                "record": 'corpus/loyjoy/005_central-ai-gpt-branching-process.md',
                "needs_visual_check": False, "needs_human_ruling": False, "accessed": DATEC}
    if i == 83:   # /guides/building/ - the "AI helps" message-panel affordance
        return {"n": n, "url": url, "title": title, "verdict": "UNCERTAIN",
                "judgment": False,
                "evidence": ('the figure whose alt and title is "AI helps" shows the message module\'s '
                             'properties panel in the process editor (heading "Welcoming recurrent '
                             'customers", text field "Glad you\'re back") with a GPT-style swirl icon '
                             'circled in its toolbar; the page\'s canvases contain no AI module, so '
                             'whether a text-assist control on a module panel is an AI element inside '
                             'the process is unresolved - see the record\'s question; page title: '
                             '"How to Build an AI Agent"'),
                "record": 'corpus/loyjoy/006_building-guide-ai-helps-message-panel.md',
                "needs_visual_check": False, "needs_human_ruling": True,
                "question": ('The message module\'s panel carries a GPT-marked text-assist control '
                             '(figure alt "AI helps") while no AI module is drawn in any of the page\'s '
                             'canvases. Is that control an AI element inside the process (artefact) or '
                             'an editor convenience outside the process model (E2-no-ai-element)?'),
                "accessed": DATEC}
    if i == 109:  # RAG architecture illustration
        return {"n": n, "url": url, "title": title, "verdict": "EXCLUDE",
                "reason": "E1-not-bpmn", "judgment": True,
                "evidence": ARCH % q, "record": None,
                "needs_visual_check": False, "needs_human_ruling": False}
    if i in REST:
        code, judgment, figs = REST[i]
        if figs.startswith('CANVAS|'):
            ev = CANVAS % (figs.split('|', 1)[1], q)
        elif figs.startswith('CHAT|'):
            ev = CHAT % (figs.split('|', 1)[1], q)
        else:
            ev = FIG % (figs, q)
    else:
        code, judgment, ev = 'E0', False, NORAST % q
    return {"n": n, "url": url, "title": title, "verdict": "EXCLUDE", "reason": code,
            "judgment": judgment, "evidence": ev, "record": None,
            "needs_visual_check": False, "needs_human_ruling": False, "accessed": DATEC}

# ------------------------------------------------------------------ marketing
def mkt_row(n, url, title, verdict, code, judgment, ev, record=None, dup=None,
            vis=False, ruling=False, question=None):
    r = {"n": n, "url": url, "title": title, "verdict": verdict}
    if verdict == "EXCLUDE":
        r["reason"] = code
    r["judgment"] = judgment
    r["evidence"] = ev
    r["record"] = record
    if dup:
        r["duplicate_of"] = dup
    r["needs_visual_check"] = vis
    r["needs_human_ruling"] = ruling
    if question:
        r["question"] = question
    r["accessed"] = DATEC
    return r

M = 'https://www.loyjoy.com'
SAME = ('the page republishes byte-identical asset files on the second URL: its HTML references '
        '%s with the same content hash as the German page, so the artefact is the same image under '
        'two URLs; page text: "%s"')
MKT = [
 mkt_row(273, M + '/de/platform/', 'LoyJoy Platform (German)', 'INCLUDE', None, False,
   'AI elements inside the depicted processes on this page: the hero figure "no-code-bpmn" shows a '
   'process in the LoyJoy editor (start/globe event -> module "#1 Welcoming" -> the cursor dragging '
   'module "#2 AI Agent" into the flow -> exclusive gateway) and the figure "process-orchestration" '
   'shows start event -> module "#1 AI Agent" -> exclusive gateway with flows "Branch 1/2/3" -> '
   'modules "#2 GPT Knowledge", "#3 GPT follow-up question", "#4 GPT Smalltalk" -> "#4 Automatic '
   'jump" -> end event; page text: "Eine no-code BPMN-Engine modelliert Dialoge und Prozesse mit '
   'Regeln, Routing, Experimenten und Analytics."',
   record='corpus/loyjoy/007_platform-process-orchestration-ai-agent.md'),
 mkt_row(274, M + '/en/platform/', 'LoyJoy Platform (English)', 'EXCLUDE', 'E3-duplicate', False,
   SAME % ('no-code-bpmn.Be3QCK8a_9QMdK.webp and process-orchestration.CgbVPyh5_aqxij.webp',
           'your business team builds AI Agents visually or in conversation with its AI assistant'),
   dup=273),
 mkt_row(275, M + '/de/platform/bpmn/', 'BPMN 2.0 Prozessautomatisierung (German)', 'UNCERTAIN', None, False,
   'a marketing screenshot of the LoyJoy process editor: the canvas shows a model in the editor\'s '
   'notation (start event, modules "#1 ...", "#2 Decision gateway", "#3 Simple message", "#4 Product '
   'gallery", exclusive gateways, end event) and the "Modules" palette beside it lists the section '
   '"control flow" with Loop, Gateway, Decision gateway and "GPT gateway" (the GPT gateway entry '
   'carries the OpenAI-style swirl icon). No GPT module is placed inside the depicted process itself; '
   'page text: "LoyJoy basiert auf dem Modellierungsstandard BPMN 2.0"',
   record='corpus/loyjoy/008_platform-bpmn-palette-gpt-gateway-de.md', ruling=True,
   question='The page is a marketing screenshot of the BPMN editor whose module palette shows a "GPT '
            'gateway" entry (AI module available in the palette) while the process drawn on the canvas '
            'contains no AI module. Is a GPT module visible in the editor palette, but not placed in '
            'the depicted process, an AI element inside the artefact (INCLUDE), or does the artefact '
            'contain no AI element (E2-no-ai-element)? I could not resolve this without a ruling.'),
 mkt_row(276, M + '/en/platform/bpmn/', 'BPMN 2.0 Process Automation (English)', 'UNCERTAIN', None, False,
   'the English twin of the German page: same editor screenshot with the "Modules" palette section '
   '"control flow" listing Loop, Gateway, Decision gateway and "GPT gateway" (GPT swirl icon), and a '
   'canvas whose drawn process (start event, "#1 ...", "#2 Decision gateway", "#3 Simple message", '
   '"#4 Product gallery", gateways, end event) contains no AI module; the canvas annotation reads '
   '"Simply remove or add modules using drag & drop."; page text: "LoyJoy seamlessly connects BPMN '
   '2.0 process automation with agentic AI."',
   record='corpus/loyjoy/009_platform-bpmn-palette-gpt-gateway-en.md', ruling=True,
   question='Same question as the German twin: the editor palette advertises a "GPT gateway" module '
            'while the process drawn on the canvas has no AI element. Is the palette entry an AI '
            'element inside the artefact (INCLUDE) or is the artefact AI-free (E2-no-ai-element)?'),
 mkt_row(277, M + '/de/blog/loyjoy-features-bpmn-process-engine/', 'LoyJoy Now Features a BPMN Process Engine to Automate Processes With Chatbots', 'EXCLUDE', 'E2-no-ai-element', False,
   'CANVAS|the figures are editor screenshots of the LoyJoy process editor - module boxes "Welcome", '
   '"Region", "Welcome call to action", "Prizes" between start and end events, with the "Process '
   'bricks" palette (control flow, events, essential) - and no AI-named module appears in any of them; '
   'page text: "We are happy to release LoyJoy 2.0 offering companies to flexibly design, build and '
   'publish chatbot-powered business processes on websites, portals, Facebook and Instagram."'),
 mkt_row(278, M + '/en/blog/loyjoy-features-bpmn-process-engine/', 'LoyJoy Now Features a BPMN Process Engine to Automate Processes With Chatbots (English)', 'EXCLUDE', 'E3-duplicate', False,
   SAME % ('the two editor screenshots (e.g. the simple_side_by_side pair)',
           'now an integral part of the LoyJoy Conversational AI Cloud'),
   dup=277),
 mkt_row(279, M + '/de/blog/new-release-makes-bpmn-process-automation-fun/', 'Unser neues Release macht BPMN-Prozessautomatisierung zum Vergnügen', 'UNCERTAIN', None, False,
   'the page embeds a YouTube video whose poster frame is a screenshot of the LoyJoy process editor: '
   'a "Modules" palette on the left and a canvas with the editor\'s rounded module boxes, exclusive '
   'gateways and a "Drop module" placeholder. The poster is published at 600 x 600 px and the video '
   'is blurred behind the play button, so the palette entries and module labels cannot be read: I '
   'cannot tell whether an AI/GPT module appears in the palette or in the drawn process; page text: '
   '"Modelliere und pflege komplexere Geschäftsprozesse mit Gateways."',
   record='corpus/loyjoy/010_blog-video-poster-unreadable.md', vis=True),
 mkt_row(280, M + '/en/blog/new-release-makes-bpmn-process-automation-fun/', 'Our New Release Makes BPMN Process Automation Fun', 'EXCLUDE', 'E3-duplicate', False,
   SAME % ('the YouTube poster frame WYnxC36CFkFmE1TJRQC1RfnF6rI.CdSK3yVi_1d0HL.webp',
           'AI in general and the LoyJoy Platform in particular are evolving rapidly'),
   dup=279),
 mkt_row(281, M + '/de/blog/reworking-loyjoys-bpmn-process-editor/', 'Reworking LoyJoy\'s BPMN Process Editor', 'EXCLUDE', 'E2-no-ai-element', False,
   'CANVAS|the page\'s editor screenshots show the LoyJoy process editor - start and end events, '
   'module boxes "#1 Welcoming", "#2 Questionnaire", "#3 Goodbye", "#4 Simple message", "#5 Goodbye" '
   '(and a cropped fragment with "condition 1/2/3" flow labels on a gateway) - and no AI/GPT module '
   'appears in any of them; page text: "Die neuen Möglichkeiten des Editors am Beispiel einer '
   'Versicherungsgesellschaft"'),
 mkt_row(282, M + '/en/blog/reworking-loyjoys-bpmn-process-editor/', 'Reworking LoyJoy\'s BPMN Process Editor (English)', 'EXCLUDE', 'E3-duplicate', False,
   SAME % ('the six editor screenshots (e.g. 0eCUs2VkNTIj5LmxrOn4gyMSvE and pnzCkrHyJcEsiYAymYALH5bLo)',
           'Reworking LoyJoy\'s BPMN Process Editor'),
   dup=281),
 mkt_row(283, M + '/de/blog/what-is-conversational-platform-bpmn-engine/', 'Was ist eine Conversational Platform und wie funktioniert eine BPMN Engine?', 'EXCLUDE', 'E0-no-artefact', False,
   'no process artefact: the figures are definition text cards ("Was ist eine Conversational '
   'Platform?", "Was ist eine BPMN Engine?") and flat illustrations of people and gears - no process '
   'model is drawn; page text: "Hier könnte uns Jonathan, unser Head of AI Engineering, weiterhelfen." '
   '(the AI wording on this page is the job title of the interviewee, not a process element)'),
 mkt_row(284, M + '/en/blog/what-is-conversational-platform-bpmn-engine/', 'What Is a Conversational Platform and How Does a BPMN Engine Work?', 'EXCLUDE', 'E3-duplicate', False,
   SAME % ('the three figures (37bQS2Q2iRWAC2QEZgSv2Q8DYc, 4eyQRzLbhy0fiEKDLDP7BDo1sk, dNgqmAeFAPyG2nmBLnvT41MgWs)',
           'our Head of AI Engineering could help us out'),
   dup=283),
 mkt_row(285, M + '/de/templates/ai_agent_feedback/', 'AI Agent mit Feedback-Frage (Template)', 'EXCLUDE', 'E1-not-bpmn', True,
   'the artefact exists but is not BPMN 2.0 notation: the page\'s figures are chat-interface '
   'screenshots (chat_flow_feedback, chat_flow_no_feedback) and a marketing thumbnail - the rendering '
   'of a conversation with the end user, which rule 3 lists explicitly as a not-BPMN artefact. The AI '
   'wording I am dismissing is the template description "Vorkonfigurierter AI Agent mit Anbindung an '
   'die LoyJoy-Wissensdatenbank", which refers to the agent the template configures in prose, not to '
   'any AI-named element drawn in a process; page text: "Vorlage für Qualitäts-KI mit Feedback-Abfrage '
   'und nahtlosem Handover an menschliche Mitarbeiter"'),
 mkt_row(286, M + '/en/templates/ai_agent_feedback/', 'AI agent with feedback question (template)', 'EXCLUDE', 'E1-not-bpmn', True,
   'same artefact on the English twin URL: chat-interface screenshots (chat_flow_feedback and '
   'chat_flow_no_feedback are the same files as on the German page) plus an English marketing '
   'thumbnail; the AI wording dismissed is the template description, not an element of a process '
   'model; page text: "The template extends a knowledge-based AI agent with a quality assurance layer."'),
 mkt_row(287, M + '/de/templates/insurance_application/', 'Antragsstrecke (Template)', 'EXCLUDE', 'E1-not-bpmn', False,
   'the artefact exists but is not BPMN 2.0 notation: the figures are a chat-interface screenshot '
   '(chat_flow: the German SecuraShield widget with the buttons "Ja, auf jeden Fall" / "Bisher nicht") '
   'and template thumbnails (antragsstrecke_template, altersvorsorge-depot-chatbot-vorlage) - no '
   'process model and no AI element; page text: "%s"' % quote(ptext('ledgers/loyjoy.marketing/364.html'))),
 mkt_row(288, M + '/en/templates/insurance_application/', 'Insurance application flow (template)', 'EXCLUDE', 'E1-not-bpmn', False,
   'the artefact exists but is not BPMN 2.0 notation: an English chat-interface screenshot '
   '(chat_flow.C4lPpGKH_2kQTWM.webp) and template thumbnails - the shared altersvorsorge-depot '
   'thumbnail is byte-identical with the German page\'s, the application-flow thumbnail is a separate '
   'English render; no process model and no AI element; page text: "Insurance application flow: '
   'chatbot template"'),
]

# ------------------------------------------------------------------- assemble
rows = [rest_row(150 + i, i) for i in range(1, 123)] + MKT
print('generated', len(rows), 'rows; first n=%d last n=%d' % (rows[0]['n'], rows[-1]['n']))
for r in MKT[:4]:
    print(r['n'], r['verdict'], r['evidence'][:150].encode('ascii', 'replace').decode())
with io.open(LED, 'a', encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

# ------------------------------------------------------------------- frontier
old = [l.strip() for l in io.open('ledgers/loyjoy.frontier.txt', encoding='utf-8') if l.strip()]
assert len(old) == 150, len(old)
murls = [r['url'] for r in MKT]
with io.open('ledgers/loyjoy.frontier.txt', 'w', encoding='utf-8') as f:
    for u in old + urls + murls:
        f.write(u + '\n')
print('frontier now', len(old + urls + murls))

# -------------------------------------------------------------------- records
CC = 'corpus/loyjoy'
RAW = 'ledgers/loyjoy.raw'
def cp(src, dst):
    shutil.copyfile(src, dst)
    print('capture', dst, Image.open(dst).size)
import glob
def pick(pat):
    g = glob.glob(pat)
    assert len(g) == 1, (pat, g)
    return g[0]

def png_from(src, dst, w=None):
    im = Image.open(src).convert('RGB')
    if w and im.width > w:
        im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    im.save(dst)
    print('capture', dst, im.size)

# 005 - /guides/central_ai/ (INCLUDE)
cp(pick(RAW + '/rest_imgs/085_02__central_ai-*'), CC + '/005_central-ai-gpt-branching-process.png')
io.open(CC + '/005_central-ai-gpt-branching-process.md', 'w', encoding='utf-8').write('''---
n: 235
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: Centralized AI Handling
url: https://docs.loyjoy.com/guides/central_ai/
accessed: 2026-09-24
verdict: INCLUDE
needs_visual_check: false
needs_human_ruling: false
bpmn_evidence: "a LoyJoy process-editor figure: message start event (circle) -> module box '#1 Simple message' -> module box '#2 GPT gateway' (carrying a green '1' annotation badge) -> exclusive gateway (diamond with X) whose outgoing sequence flows are labelled 'Branch 1', 'Branch 2' and 'Branch 3' -> module boxes '#3 GPT Knowledge', '#5 GPT Follow-up question', '#7 GPT Smalltalk'; '#3 GPT Knowledge' flows on to '#4 Questionnaire' (with an email icon), '#5' to '#6 Automatic jump' -> end event, and '#4'/'#7' rejoin at a second exclusive gateway -> end event; a second fragment shows a message start event -> '#8 Automatic jump' -> end event. The page's own image metadata names it 'Central AI Agent Configuration in LoyJoy Backend'"
bpmn_evidence_quote: "add a Message start module as usual, but instead of adding the AI modules"
ai_evidence: "four GPT modules sit inside the depicted process: '#2 GPT gateway' immediately after the start event, and '#3 GPT Knowledge', '#5 GPT Follow-up question' and '#7 GPT Smalltalk' on the three gateway branches. The page documents the pattern: the central agent 'handles the generative AI for several or all your agents'"
ai_evidence_quote: "LoyJoy allows you to use one central AI agent that handles the generative AI for several or all your agents in LoyJoy."
artefacts:
  screenshot: corpus/loyjoy/005_central-ai-gpt-branching-process.png
  archive: ledgers/loyjoy.raw/html_rest/085.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 915
capture_method: chrome-devtools-mcp/curl, the page's figure asset https://docs.loyjoy.com/assets/images/central_ai-*.png (alt "Central AI Agent", title "Central AI Agent Configuration in LoyJoy Backend"), downloaded to ledgers/loyjoy.raw/rest_imgs/ and copied to corpus/loyjoy/. Page HTML archived to ledgers/loyjoy.raw/html_rest/085.html
---

## What the page shows

`/guides/central_ai/` is the guide for running one central AI agent for several LoyJoy agents. Its
figure `central_ai-*.png` (915 x 1455 native, alt "Central AI Agent") is the strongest single
AI-in-process artefact found outside the `/bpmn/` section.

**The AI-in-BPMN artefact, element by element** (read off the capture):

- a **start event** (plain circle) -> module box **"#1 Simple message"**;
- module box **"#2 GPT gateway"** with a green "1" badge - the AI element directly in the flow;
- an **exclusive gateway** (X diamond) with the outgoing flows labelled **"Branch 1"**, **"Branch 2"**,
  **"Branch 3"**;
- the three branches feed **"#3 GPT Knowledge"**, **"#5 GPT Follow-up question"** and
  **"#7 GPT Smalltalk"**;
- **"#3"** continues to **"#4 Questionnaire"**; **"#5"** to **"#6 Automatic jump"** -> end event;
  **"#4"** and **"#7"** rejoin at a second exclusive gateway -> end event;
- a separate fragment below: **message start event -> "#8 Automatic jump" -> end event**.

The page is a *guide*, not a module reference page, and the figure is the published diagram of the
pattern (no editor chrome). The modules are drawn in the same notation the `/bpmn/` reference pages
use ("#N" module boxes, round events, X-diamond gateways).

## Observations (description only, no interpretation)

- **AI activity - function:** the GPT gateway classifies the user's message into one of the three
  branches; each branch module then answers (knowledge lookup, follow-up question, smalltalk).
- **AI activity - element type:** four module boxes inside the process; one of them (the GPT gateway)
  is directly adjacent to an exclusive gateway.
- **Authority - downstream:** the branches continue into further modules (questionnaire, automatic
  jump); the central-agent pattern means other agents jump into this agent's AI configuration.
- **Authority - data:** not visible on the page.
- **Authority - control:** the exclusive gateway and the "Branch 1/2/3" labels are the control
  structure; the branching decision itself is taken by the GPT gateway module.
- **Input provenance:** the start event (a chat message).
- **Guards present:** none drawn.
- **Prompt / model detail visible:** none on this page (the guide documents configuration elsewhere).

## Notes for the researcher

- Found by the secondary sweep of the docs host, i.e. it lies **outside** the `/bpmn/` section that
  the first 150 rows cover - this is exactly the kind of row the exhaustiveness claim depends on.
- The page's second figure (`other_agent-*.png`, 574 x 1020, alt "Other Agent") shows a two-module
  canvas fragment; both figures are archived in `ledgers/loyjoy.raw/rest_imgs/`.
- The page text does not contain the string "GPT gateway": the module names are read from the figure
  itself, which is legible at native resolution.
''')

# 006 - /guides/building/ (UNCERTAIN)
cp(pick(RAW + '/rest_imgs/083_13__gpt-*'), CC + '/006_building-guide-ai-helps-message-panel.png')
io.open(CC + '/006_building-guide-ai-helps-message-panel.md', 'w', encoding='utf-8').write('''---
n: 233
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: Build an Agent / How to Build an AI Agent
url: https://docs.loyjoy.com/guides/building/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: false
needs_human_ruling: true
question: "The guide's message-configuration figure (alt and title 'AI helps') shows the properties panel of a message module inside the process editor; its toolbar carries a GPT-style swirl icon (circled in the figure) beside the link, smiley and variable icons. The figure demonstrates an AI text-assist affordance attached to a process module, but no AI module is drawn as a step of the process itself, and the surrounding prose does not name that control. Is an AI text-assist control on a module's properties panel an AI/LLM element inside the process (so this row is an artefact), or only an editor convenience outside the process model (so this row is E2-no-ai-element)? The other figures on the page (editor canvases with '#1 Email'/'#2 Snapshot', the Process-bricks palette, new-experience menus) carry no AI label at all."
bpmn_evidence: "a crop of the LoyJoy process editor's message-module properties panel: the heading 'Welcoming recurrent customers' with a clock icon, the text field 'Glad you're back' (highlighted), the language label 'en', and the panel toolbar with a circled pencil icon, a GPT-style swirl icon, a link icon, a smiley icon and a '$' variable icon; beside it the image-upload box reading '1200 x 630 px / 500 KB'. The page's other figures are editor canvases: start event -> module '#1 Email' -> module '#2 Snapshot' -> end event, a '#1 Questionnaire' single-module canvas, and the 'Modules' palette with its 'control flow'/'events'/'essential' sections"
bpmn_evidence_quote: "Add bricks to editor"
ai_evidence: "the figure's own alt and title text is 'AI helps' and it points at the GPT-style swirl icon in the message panel's toolbar; the page is titled 'How to Build an AI Agent'. The AI element is therefore an editor affordance attached to a message module, not a module placed in the drawn process: no GPT/AI module appears in any of the page's canvases"
ai_evidence_quote: "AI helps"
artefacts:
  screenshot: corpus/loyjoy/006_building-guide-ai-helps-message-panel.png
  archive: ledgers/loyjoy.raw/html_rest/083.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1038
capture_method: curl of the page's figure asset https://docs.loyjoy.com/assets/images/gpt-*.png (1038 x 276 native, alt/title "AI helps"), archived in ledgers/loyjoy.raw/rest_imgs/083_13__gpt-*.png and copied to corpus/loyjoy/. Page HTML archived to ledgers/loyjoy.raw/html_rest/083.html
---

## What the page shows

`/guides/building/` is the 20-figure builder guide for LoyJoy agents (h1 "How to Build an AI
Agent"). It contains editor canvases, palette figures, menus - and one figure whose alt/title is
literally **"AI helps"**, reproduced here.

**What the captured figure shows:** the properties panel of a **message module** inside the process
editor - heading "Welcoming recurrent customers" with a clock icon, the message text field
("Glad you're back", highlighted), the language chip "en", and the panel's toolbar: a circled
pencil icon, a **GPT-style swirl icon**, a link icon, a smiley icon and a "$" variable icon. Beside
the panel sits the image-upload box ("1200 x 630 px / 500 KB").

**Why this row is UNCERTAIN rather than E2.** The AI affordance is *visible* (a GPT-marked control
in a module's panel) and the figure is *titled* "AI helps", but it is not an AI element drawn as a
step of the process: the page's canvases ("#1 Email" -> "#2 Snapshot", "#1 Questionnaire",
"Process bricks") contain no GPT/AI module. Whether a text-assist control on a module panel counts
as an AI element *inside the process* is a judgement call, and rule 3 forbids E2 for ambiguous
cases, so the row is recorded with a record and a question.

## Observations (description only, no interpretation)

- **AI activity - function:** if counted, generating or rewriting the module's message text from the
  text field ("Glad you're back").
- **AI activity - element type:** a toolbar control of the message module's properties panel; no
  module box and no event.
- **Authority - downstream:** the message text reaches the end user.
- **Authority - data:** not visible.
- **Authority - control:** the panel is a property of a module that sits in the process; the process
  structure itself (gateways, branches) is unaffected.
- **Input provenance:** the text typed in the module's message field.
- **Guards present:** none.
- **Prompt / model detail visible:** none - no model name, no prompt field.

## Notes for the researcher

- The figure is a native 1038 x 276 crop; the labels are legible at that size.
- The page's canvases were inspected one by one (21 raster assets under
  `ledgers/loyjoy.raw/rest_imgs/083_*`): none contains an AI-named module; the only AI-marked pixel
  content on the page is this message-panel control.
''')

# 007 - /de|/en platform (INCLUDE)
png_from(pick(RAW + '/mkt_imgs/m314__process-orchestration.*'), CC + '/007_platform-process-orchestration-ai-agent.png')
io.open(CC + '/007_platform-process-orchestration-ai-agent.md', 'w', encoding='utf-8').write('''---
n: 273
source: loyjoy
source_name: LoyJoy (marketing site, product pages)
source_type: vendor marketing page
title: LoyJoy Platform (German landing page)
url: https://www.loyjoy.com/de/platform/
accessed: 2026-09-24
verdict: INCLUDE
needs_visual_check: false
needs_human_ruling: false
bpmn_evidence: "a marketing figure of a process in the LoyJoy editor's notation: a start event (circle with a globe icon on a white card) -> module box '#1 AI Agent' (green '1' annotation badge) -> exclusive gateway (diamond with X) whose outgoing flows are labelled 'Branch 1', 'Branch 2', 'Branch 3' -> module boxes '#2 GPT Knowledge', '#3 GPT follow-up question', '#4 GPT Smalltalk' -> module box '#4 Automatic jump' -> end event (plain circle). The same page's second canvas figure ('no-code-bpmn') shows start event -> module '#1 Welcoming' -> the editor cursor dragging module '#2 AI Agent' into the flow -> exclusive gateway"
bpmn_evidence_quote: "Eine no-code BPMN-Engine modelliert Dialoge und Prozesse mit Regeln, Routing, Experimenten und Analytics."
ai_evidence: "the module boxes '#1 AI Agent', '#2 GPT Knowledge', '#3 GPT follow-up question' and '#4 GPT Smalltalk' are steps inside the drawn process, and the second figure shows '#2 AI Agent' being placed into the flow; the page prose describes exactly that: the business team builds AI Agents visually"
ai_evidence_quote: "Ihre Fachabteilung baut AI Agents visuell oder im Dialog mit ihrem KI-Assistenten."
artefacts:
  screenshot: corpus/loyjoy/007_platform-process-orchestration-ai-agent.png
  archive: ledgers/loyjoy.marketing/314.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1167
capture_method: curl of the page's figure asset https://www.loyjoy.com/_astro/process-orchestration.CgbVPyh5_aqxij.webp (1167 x 976 native), converted to PNG with PIL; the page's other canvas asset no-code-bpmn.Be3QCK8a_9QMdK.webp is archived beside it in ledgers/loyjoy.raw/mkt_imgs/. Page HTML archived to ledgers/loyjoy.marketing/314.html
---

## What the page shows

The German platform landing page carries 33 figure assets, of which two are process canvases. The
captured one (`process-orchestration`) is the clearest AI-in-process artefact on the marketing host.

**The AI-in-BPMN artefact, element by element** (read off the capture):

- a **start event** (circle with a globe glyph) at the top;
- module box **"#1 AI Agent"** with a green "1" badge, directly after the start event;
- an **exclusive gateway** (X diamond) with three outgoing flows labelled **"Branch 1"**,
  **"Branch 2"**, **"Branch 3"**;
- the branches feed **"#2 GPT Knowledge"**, **"#3 GPT follow-up question"** and
  **"#4 GPT Smalltalk"**;
- a module box **"#4 Automatic jump"** and an **end event** below;
- the figure is composited over a photograph of a person at a laptop (marketing hero treatment).

The second canvas figure on the same page (`no-code-bpmn`) shows **"#1 Welcoming"** with the editor
cursor dragging **"#2 AI Agent"** into the flow, ending in an exclusive gateway.

## Observations (description only, no interpretation)

- **AI activity - function:** the AI Agent handles the request; the three gateway branches route to
  knowledge lookup, a follow-up question or smalltalk - the same pattern the docs' `/guides/central_ai/`
  page documents (`corpus/loyjoy/005_central-ai-gpt-branching-process.md`).
- **AI activity - element type:** module boxes inside the process ("AI Agent", "GPT Knowledge",
  "GPT follow-up question", "GPT Smalltalk"), one of them the first step after the start event.
- **Authority - downstream:** an automatic jump and the end event; the marketing page's other figures
  advertise the surrounding platform (knowledge, integrations, live-chat handover).
- **Authority - data:** the page names the knowledge layer ("ai-agent-knowledge" figure card) and the
  model choice (a chat LLM on LoyJoy hardware, Enterprise choice of GPT/Claude/own LLM).
- **Authority - control:** the exclusive gateway with the three named branches.
- **Input provenance:** the start event (a customer message).
- **Guards present:** none drawn.
- **Prompt / model detail visible:** the page's AI-model figure (`ai_model_de`) shows a settings
  dropdown, not the process.

## Notes for the researcher

- **Outside the docs host.** This row comes from the documented secondary sweep of the marketing site
  (see the ledger header note); it is not part of the `/bpmn/` census.
- The English twin `/en/platform/` publishes the *same two canvas files* (identical content hashes)
  and is recorded as `E3-duplicate` in the ledger.
- 33 page assets were inspected by contact sheet and zooms; the remaining AI-named cards
  (`ai-agent`, `agentic-ai`, `ai-quality-check`, `ai-testing-automation`, `smart-product-advisor`)
  are UI/illustration cards, not process diagrams - except `process-orchestration` and `no-code-bpmn`.
''')

# 008 / 009 - platform/bpmn twin pages (UNCERTAIN)
png_from(pick(RAW + '/mkt_imgs/m317__bpmn_de.*'), CC + '/008_platform-bpmn-palette-gpt-gateway-de.png', 1024)
io.open(CC + '/008_platform-bpmn-palette-gpt-gateway-de.md', 'w', encoding='utf-8').write('''---
n: 275
source: loyjoy
source_name: LoyJoy (marketing site, product pages)
source_type: vendor marketing page
title: BPMN 2.0 Prozessautomatisierung (German)
url: https://www.loyjoy.com/de/platform/bpmn/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: false
needs_human_ruling: true
question: "The page's figure is a screenshot of the LoyJoy BPMN editor: the canvas shows a process (start event, module boxes, exclusive gateways, end event) and the 'Modules' palette beside it lists the section 'control flow' with Loop, Gateway, Decision gateway and 'GPT gateway' (the last carrying the OpenAI-style swirl icon). No GPT module is placed inside the process drawn on the canvas. Is a GPT module that is visible in the editor's palette (i.e. available, AI-bound, and part of the artefact) an AI element inside the artefact, or does the artefact contain no AI element (E2-no-ai-element)? The same question applies to the English twin."
bpmn_evidence: "a marketing screenshot of the LoyJoy process editor: title bar 'LoyJoy / My Experience', the 'Modules' palette on the left with the section headings 'control flow' (Loop, Gateway, Decision gateway, 'GPT gateway'), 'events' (End, Wait, Message start, Timer start) and 'essential' (Add variables, Appointment scheduler, Automatic jump, Clipboard, Conversion, Create PDF, Decision jump, Email, External link, Goodbye), and on the canvas a process drawn in the editor's notation: start event, module boxes ('#1 ...', '#2 Decision gateway', '#3 Simple message', '#4 Product gallery'), exclusive gateways and an end event, with German annotations ('No-Code Ansatz durch BPMN 2.0 Modellierung.') drawn over it"
bpmn_evidence_quote: "LoyJoy basiert auf dem Modellierungsstandard BPMN 2.0"
ai_evidence: "the palette entry 'GPT gateway' with the GPT swirl icon is part of the depicted editor; the German annotation 'Kontinuierliche Weiterentwicklung der BPMN-Prozessmodule.' points at the palette. No GPT/AI module is placed in the process drawn on the canvas, and the page prose about AI is about the platform, not about the depicted model"
ai_evidence_quote: "BPMN 2.0 Prozessautomatisierung nahtlos mit agentischer KI"
artefacts:
  screenshot: corpus/loyjoy/008_platform-bpmn-palette-gpt-gateway-de.png
  archive: ledgers/loyjoy.marketing/317.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1024
capture_method: curl of the page's figure asset https://www.loyjoy.com/_astro/bpmn_de.CZTki966_Z1xvGuj.webp (1024 x 600 native), converted to PNG with PIL; the palette region was additionally re-examined at 4x zoom (ledgers/loyjoy.raw/mont3/pal.jpg, pal2.jpg). Page HTML archived to ledgers/loyjoy.marketing/317.html
---

## What the page shows

`/de/platform/bpmn/` is LoyJoy's German BPMN marketing page. Its single figure is a **screenshot of
the LoyJoy process editor** with the "Modules" palette open beside the canvas.

**What the capture shows** (read off the figure; palette labels verified at 4x zoom):

- the editor shell: title "LoyJoy", breadcrumb "My Experience", the Process/Branding/Language/
  Publish/Texts/Assets tabs;
- the **Modules palette**, section by section: **control flow** - Loop, Gateway, Decision gateway,
  **"GPT gateway"** (with the GPT swirl icon); **events** - End, Wait, Message start, Timer start;
  **essential** - Add variables, Appointment scheduler, Automatic jump, Clipboard, Conversion,
  Create PDF, Decision jump, Email, External link, Goodbye;
- the **canvas**: start event, module boxes ("#1 ...", "#2 Decision gateway", "#3 Simple message",
  "#4 Product gallery"), exclusive gateways, end event;
- German marketing annotations over the screenshot: "No-Code Ansatz durch BPMN 2.0 Modellierung.",
  "Kontinuierliche Weiterentwicklung der BPMN-Prozessmodule.", "Module einfach per Drag & Drop
  entfernen oder hinzufügen."

**Why UNCERTAIN.** The GPT element is on screen (a palette entry, and the palette is how the editor
offers AI modules), but the process that is *drawn* contains no AI module. A reader could argue
either way, and rule 3 forbids E2 for ambiguous cases.

## Observations (description only, no interpretation)

- **AI activity - function:** if the palette entry is counted, an AI gateway module available for
  insertion into the process.
- **AI activity - element type:** a palette tile labelled "GPT gateway" (diamond icon with the GPT
  swirl); nothing placed on the canvas.
- **Authority - downstream:** not visible.
- **Authority - data:** not visible.
- **Authority - control:** the canvas's exclusive gateways are the drawn control structure.
- **Input provenance:** not visible.
- **Guards present:** none.
- **Prompt / model detail visible:** none.

## Notes for the researcher

- The German and English pages do **not** share the figure file (`bpmn_de` vs `bpmn_en`, different
  hashes), so both are recorded - they are similar-but-different artefacts, not duplicates. The
  editor UI inside both is English; only the marketing annotations differ.
- The palette region is the only place a GPT module is visible; the earlier 4x zoom is archived at
  `ledgers/loyjoy.raw/mont3/pal2.jpg` so the researcher can re-check the label.
''')
png_from(pick(RAW + '/mkt_imgs/m737__bpmn_en.*'), CC + '/009_platform-bpmn-palette-gpt-gateway-en.png', 1024)
io.open(CC + '/009_platform-bpmn-palette-gpt-gateway-en.md', 'w', encoding='utf-8').write('''---
n: 276
source: loyjoy
source_name: LoyJoy (marketing site, product pages)
source_type: vendor marketing page
title: BPMN 2.0 Process Automation (English)
url: https://www.loyjoy.com/en/platform/bpmn/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: false
needs_human_ruling: true
question: "Same question as the German twin (/de/platform/bpmn/, corpus/loyjoy/008_...): the editor screenshot's 'Modules' palette lists 'GPT gateway' while the process drawn on the canvas contains no AI module. Is a GPT module visible in the editor palette, but not placed in the depicted process, an AI element inside the artefact, or does the artefact contain no AI element (E2-no-ai-element)?"
bpmn_evidence: "a marketing screenshot of the LoyJoy process editor: the 'Modules' palette with the sections 'control flow' (Loop, Gateway, Decision gateway, 'GPT gateway'), 'events' and 'essential', and on the canvas a process in the editor's notation - start event, module boxes ('#1 ...', '#2 Decision gateway', '#3 Simple message', '#4 Product gallery'), exclusive gateways, end event - with the English annotations 'No-code approach through BPMN 2.0 modelling.', 'Continuous development of the BPMN process modules.' and 'Simply remove or add modules using drag & drop.'"
bpmn_evidence_quote: "LoyJoy is based on the BPMN 2.0 modeling standard"
ai_evidence: "the palette tile 'GPT gateway' (diamond icon carrying the GPT swirl) is the only AI-marked content of the screenshot; the canvas shows no AI module. The page's prose AI claim is about the platform: 'LoyJoy seamlessly connects BPMN 2.0 process automation with agentic AI.' - which the figure does not depict"
ai_evidence_quote: "LoyJoy seamlessly connects BPMN 2.0 process automation with agentic AI."
artefacts:
  screenshot: corpus/loyjoy/009_platform-bpmn-palette-gpt-gateway-en.png
  archive: ledgers/loyjoy.marketing/737.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1024
capture_method: curl of the page's figure asset https://www.loyjoy.com/_astro/bpmn_en.CttUSZB9_ZpLfDt.webp (1024 x 600 native), converted to PNG with PIL; palette region re-examined at 4x zoom (ledgers/loyjoy.raw/mont3/pal2.jpg, where 'GPT gateway' is legible). Page HTML archived to ledgers/loyjoy.marketing/737.html
---

## What the page shows

The English twin of `/de/platform/bpmn/`. Its figure is the same editor screenshot in an English
annotated render: palette section "control flow" with Loop, Gateway, Decision gateway and
**"GPT gateway"**, the canvas with a process that contains no AI module, and three English
annotations pointing at BPMN 2.0 modelling and the module palette.

**Verified at 4x zoom** (`ledgers/loyjoy.raw/mont3/pal2.jpg`): the tile reads "GPT gateway" beneath
the section label "control flow", with the GPT swirl icon on the diamond - so the module name is
not an inference from the file name or the URL.

**Why UNCERTAIN:** identical to `corpus/loyjoy/008_platform-bpmn-palette-gpt-gateway-de.md` - the
GPT element is in the palette, not in the drawn process.

## Observations (description only, no interpretation)

- **AI activity - function:** if counted, an AI gateway module offered by the editor palette.
- **AI activity - element type:** a palette tile ("GPT gateway"); nothing placed on the canvas.
- **Authority - downstream / data / control:** not visible in the figure; the page prose names
  knowledge-based advice and process permissions.
- **Input provenance:** not visible.
- **Guards present:** none.
- **Prompt / model detail visible:** none.

## Notes for the researcher

- The `bpmn_en` and `bpmn_de` files are different renders (different content hashes) of the same
  editor state, so both rows exist; if the researcher rules the palette entry irrelevant, both fall
  together.
- The English platform landing page (`/en/platform/`) is a separate row (`E3-duplicate` of the
  German landing page, identical canvas assets) and is unaffected by this question.
''')

# 010 - blurred video poster (UNCERTAIN)
png_from(pick(RAW + '/mkt_imgs/m102__WYnxC36*'), CC + '/010_blog-video-poster-unreadable.png')
io.open(CC + '/010_blog-video-poster-unreadable.md', 'w', encoding='utf-8').write('''---
n: 279
source: loyjoy
source_name: LoyJoy (marketing site, blog)
source_type: vendor marketing page
title: Unser neues Release macht BPMN-Prozessautomatisierung zum Vergnügen
url: https://www.loyjoy.com/de/blog/new-release-makes-bpmn-process-automation-fun/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: true
needs_human_ruling: false
bpmn_evidence: "the page embeds a YouTube video whose poster frame is a screenshot of the LoyJoy process editor: the 'Modules' palette on the left (control-flow diamonds, event and essential tiles) and a canvas with the editor's rounded module boxes, exclusive gateways, a 'Drop module' placeholder and a '#1 ...' label; the editor's left navigation is also visible (Experiences, NLU, Push, Live). The poster is published at 600 x 600 px and the video frame is blurred behind the play button, so the palette entries and the module labels cannot be read"
bpmn_evidence_quote: "Modelliere und pflege komplexere Geschäftsprozesse mit Gateways."
ai_evidence: "unresolved: the poster cannot be read at 600 x 600 px, so I cannot tell whether a GPT/AI module appears in the palette or in the drawn process. The page prose is about the release's BPMN features (gateways, process automation) and carries no AI element that I could tie to the figure"
ai_evidence_quote: "Unsere Top 5 Highlights auf einen Blick"
artefacts:
  screenshot: corpus/loyjoy/010_blog-video-poster-unreadable.png
  archive: ledgers/loyjoy.marketing/102.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 600
capture_method: curl of the page's YouTube poster asset https://www.loyjoy.com/_astro/WYnxC36CFkFmE1TJRQC1RfnF6rI.CdSK3yVi_1d0HL.webp (600 x 600 native), converted to PNG with PIL. The video itself (YouTube embed) was not opened - the poster is the only published still. Page HTML archived to ledgers/loyjoy.marketing/102.html
---

## What the page shows

The German blog post for the 2022 release. Its only figure-bearing element is an embedded YouTube
video whose **poster frame is an editor screenshot**: "Modules" palette on the left, canvas on the
right with rounded module boxes, X-diamond gateways, a "#1 ..." label and a "Drop module"
placeholder, and the editor's left navigation (Experiences, NLU, Push, Live).

**Why UNCERTAIN / needs_visual_check.** At 600 x 600 px, blurred behind the play button, neither
the palette entries nor the module labels can be read. Rule 5 forbids excluding an unresolved image
and rule 3 forbids E2 on an ambiguous AI question, so the row is recorded for a human look (the
original video would settle it).

## Observations (description only, no interpretation)

- **AI activity - function:** unknown (unresolved).
- **AI activity - element type:** unknown; the visible structure is a process canvas in the editor's
  notation plus the module palette.
- **Authority - downstream / data / control:** not readable.
- **Input provenance:** not readable.
- **Guards present:** not readable.
- **Prompt / model detail visible:** none visible.

## Notes for the researcher

- The English twin `/en/blog/new-release-makes-bpmn-process-automation-fun/` embeds the **same poster
  file** (identical content hash) and is recorded as `E3-duplicate`.
- Everything I could resolve is in the capture; the video's later frames are the only way to read the
  palette, and opening a YouTube embed was outside this read-only pass.
''')

# ---------------------------------------------------------------- header/footer
with io.open(LED, 'a', encoding='utf-8') as f:
    f.write(json.dumps({
        "type": "header",
        "source": "loyjoy",
        "census": True,
        "population_size": 288,
        "enumeration_method": (
            "Two-part, both parts finite and enumerable. (a) Docs host: https://docs.loyjoy.com/sitemap.xml "
            "lists 272 <loc> URLs - 150 under /bpmn/ (the first 150 rows) and 122 elsewhere on the host (rows "
            "151-272) - all 272 fetched and judged; every one of the host's 284 + 165 + 157 raster assets was "
            "downloaded and inspected, all 64 published .svg files proved to be one identical logo, and every "
            "inline <svg> on the 122 non-/bpmn/ pages is a 24px interface glyph (viewBox '0 -960 960 960'). "
            "(b) Marketing host: https://www.loyjoy.com/sitemap-0.xml lists 842 URLs; because a strict BPMN-term "
            "scan matches 841 of them on boilerplate navigation, a documented heuristic (BPMN slug, or >=2 "
            "BPMN-term body hits, or a BPMN-named asset) selected 18 pages whose 59 assets were downloaded and "
            "inspected, and the 16 artefact-bearing pages among them are rows 273-288. LIMIT, stated plainly: "
            "the other 830 marketing URLs were screened textually only, so the marketing part is not exhaustive "
            "in the way the docs part is."
        ),
        "entry_points": [
            "https://docs.loyjoy.com/sitemap.xml",
            "https://docs.loyjoy.com/bpmn/",
            "https://docs.loyjoy.com/bpmn/subprocesses/ai_agent/",
            "https://www.loyjoy.com/sitemap-0.xml",
            "https://www.loyjoy.com/de/platform/",
            "https://www.loyjoy.com/en/platform/bpmn/"
        ],
        "access": "public",
        "date_start": "2026-09-24",
        "agent_model": "deepseek-v4.1-flash:cloud",
        "browser_tool": "chrome-devtools-mcp --browser-url 127.0.0.1:9222",
        "queries": [
            "site map enumeration only; no search-engine result lists were used as a population"
        ],
        "note": (
            "EXTENDED HEADER (supersedes the first header line; this row records the population actually "
            "censused). Rules applied: docs /bpmn/ pages by module/event/gateway semantics; non-/bpmn/ docs "
            "pages by the same artefact criteria; marketing pages only where a figure was inspected. "
            "False-positive AI terms in this source that were checked and rejected as non-AI: 'agent' (human "
            "live-chat agents, e.g. agent_profile, live_agent_switcher), 'recommend(er)' (deterministic tag "
            "matching, /bpmn/subprocesses/products/ and /templates/contact_search/), 'Knowledge'/'Wissen' "
            "(navigation labels), 'AI' inside the marketing banner 'AI Agents ... in Claude, ChatGPT Work and "
            "OpenWork' that appears on all 842 marketing pages, and 'KI'/'AI' in the job title 'Head of AI "
            "Engineering'. Rows 151-288 were added after a second sweep; rows 1-150 (the /bpmn/ census) are "
            "unchanged. Judgement convention (see footer): judgment=true marks the EXCLUDE rows where I had to "
            "rule on whether AI-feature content visible in a figure is an AI element inside a process."
        )
    }, ensure_ascii=False) + '\n')

from collections import Counter
latest = {}
for line in io.open(LED, encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    o = json.loads(line)
    if o.get('type'):
        continue
    latest[o['n']] = o
data = list(latest.values())
n_all = len(data)
cnt = Counter(r['verdict'] for r in data)
exc = Counter(r['reason'] for r in data if r['verdict'] == 'EXCLUDE')
print('rows=%d include=%d uncertain=%d exclude=%d blocked=%d' % (
    n_all, cnt['INCLUDE'], cnt['UNCERTAIN'], cnt['EXCLUDE'], cnt['BLOCKED']))
print('exclusions', dict(exc))
judg = sum(1 for r in data if r.get('judgment') is True and r['verdict'] == 'EXCLUDE')
print('judgement exclusions', judg, '%.1f%%' % (100.0 * judg / n_all))
with io.open(LED, 'a', encoding='utf-8') as f:
    f.write(json.dumps({
        "type": "footer",
        "date_end": "2026-09-24",
        "rows": n_all,
        "include": cnt['INCLUDE'],
        "uncertain": cnt['UNCERTAIN'],
        "exclude": dict(exc),
        "blocked": 0,
        "judgement_exclusion_share": "%d judgement EXCLUDE rows of %d (%.1f%%)" % (judg, n_all, 100.0 * judg / n_all),
        "self_audit_flips": (
            "Two corrections were made during the secondary sweep and are visible as earlier rows: (1) page 22 "
            "/docs/agents/process/ and page 23 /docs/agents/publish/ were first noted as canvas pages and are "
            "E0-no-artefact after their figure assets were read (copy_and_paste/refresh_preview/warning_bubble "
            "and publish_button/settings1/settings2); (2) the Product gallery 'Recommender' (row 102) was "
            "flipped from E2 to UNCERTAIN after reading the deprecated AI Recommender module page."
        ),
        "convention": (
            "judgment=true marks EXCLUDE rows where the exclusion required ruling that AI-feature content "
            "visible in the page's own figures is not an AI element inside a process (rows 34, 38, 52, 54, 55, "
            "56, 65, 84, 109, 285, 286). Rows whose pages carry no figure at all are mechanical E0 and are not "
            "flagged."
        ),
        "status": "COMPLETE"
    }, ensure_ascii=False) + '\n')
print('header+footer appended')
