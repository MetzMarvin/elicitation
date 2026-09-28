import json,io,collections,re
T=json.load(io.open('ledgers/_lj_table.json',encoding='utf-8'))
EV={o['n']:o for o in json.load(io.open('ledgers/_lj_ev.json',encoding='utf-8'))}
urls=[l.strip() for l in io.open('ledgers/loyjoy.frontier.txt',encoding='utf-8') if l.strip()]
INCLUDE={7:'corpus/loyjoy/001_message-start-event-gpt-gateway.md',
         12:'corpus/loyjoy/002_ai-agent-module-canvas.md',
         14:'corpus/loyjoy/003_ai-knowledge-gpt-flow.md'}
UNCERTAIN={102:'corpus/loyjoy/004_product-gallery-recommender.md'}
QUESTION=("The Product gallery module's settings panel offers a 'Recommender' feature (Off/Filter/Smart) and the "
 "same page documents Smart as deterministic tag matching ('products are sorted based on the number of matching tags'), "
 "while LoyJoy separately publishes a deprecated 'AI Recommender' module that generates product recommendations via SQL. "
 "Is the Product gallery 'Recommender' an AI element inside the depicted process (so this row is an artefact), or the "
 "deterministic tag filter described on this page (so this row is E2-no-ai-element)? "
 "See corpus/loyjoy/004_product-gallery-recommender.md.")
CANVAS=('bpmn-canvas','editor-canvas+panel')
def q(o):
    s=o['ev']
    for pre in ('Overview ','Introduction ','Typical Use Cases ','How to Use the Module ','On this page '):
        if s.startswith(pre): s=s[len(pre):]
    return s
SPECIAL={
 9:('E2-no-ai-element',False,'process-editor view: the figure shows the start-event icon magnified over the module "#1 Welcoming" in the editor canvas; no AI label in the image'),
 39:('E1-not-bpmn',True,'artefacts are DMN decision-table screenshots (a decision table with Rules/Input/Output columns and "Add rule") plus editor module tiles - a modelling notation, but not BPMN'),
 90:('E2-no-ai-element',True,'the canvas figure\'s panel shows the poll question "#1.1 Is A.I. able to make the world a better place?" - poll question content, not a feature label'),
 118:('E1-not-bpmn',True,'images are a Salesforce OAuth scope/credential screen, a contact table and a chat preview - no process diagram; the AI text "Access Einstein GPT services (einstein_gpt_api)" is a third-party OAuth scope in a credentials dialog, not an element of a LoyJoy process'),
 122:('E1-not-bpmn',True,'images are a knowledge-base admin screen ("Smart Search ON", "GPT ON", "NLU OFF") and a chat preview - no process diagram; the AI toggles belong to the knowledge-base admin, not to a depicted BPMN element'),
}
rows=[]
for i in range(1,151):
    o=T[i-1]; ev=EV[i]; u=urls[i-1]
    classes=o['classes']; imgs=o['imgs']; ai=o['ai']
    names_c=[im['n'] for im in imgs if im['class'] in CANVAS]
    classes_s=', '.join(sorted(classes)) if classes else 'none'
    quote=q(ev); nimg=o['n_img']
    title=ev['h1'] or u.rstrip('/').split('/')[-1]
    reason=None; judgment=False; record=None; nr=False; question=None
    if i in INCLUDE:
        verdict='INCLUDE'; record=INCLUDE[i]
        ev_txt='AI module(s) named inside the depicted process; page text: "%s"'%quote
    elif i in UNCERTAIN:
        verdict='UNCERTAIN'; record=UNCERTAIN[i]; judgment=True; nr=True; question=QUESTION
        ev_txt='canvas figure whose module panel is headed "Recommender" (Off/Filter/Smart); ambiguity unresolved; page text: "%s"'%quote
    elif i in SPECIAL:
        code,jd,note=SPECIAL[i]; verdict='EXCLUDE'; reason=code; judgment=jd
        ev_txt='%s; page text: "%s"'%(note,quote)
    elif any(c in classes for c in CANVAS):
        verdict='EXCLUDE'; reason='E2-no-ai-element'
        extra=''
        other=[a['label'].replace('YES: ','').strip() for a in ai if a.get('label')]
        if other: extra='; the image text %s is navigation/admin UI, not a process element'%('; '.join(other[:2]))
        ev_txt='process-editor canvas figure(s) %s; no AI/LLM element inside the process%s; page text: "%s"'%(', '.join(names_c)[:120],extra,quote)
    elif nimg==0:
        verdict='EXCLUDE'; reason='E0-no-artefact'
        ev_txt='no figure at all: page body is text only (%d chars, 0 images); page text: "%s"'%(ev['len'],quote)
    elif 'chat-ui' in classes:
        verdict='EXCLUDE'; reason='E1-not-bpmn'
        ev_txt='artefact is a chat-interface screenshot (images: %s), no process diagram; page text: "%s"'%(classes_s,quote)
    else:
        verdict='EXCLUDE'; reason='E0-no-artefact'
        head = ('no process artefact: all %d images are %s'%(nimg,classes_s)) if nimg!=1 else ('no process artefact: the only image on the page is %s'%classes_s)
        ev_txt=head+'; page text: "%s"'%quote
    r={'n':i,'url':u if u.startswith('http') else 'https://docs.loyjoy.com'+u,'title':title,'verdict':verdict,
       'reason':reason,'judgment':judgment,'evidence':ev_txt,'record':record,
       'needs_visual_check':False,'needs_human_ruling':nr,'accessed':'2026-09-24'}
    if nr: r['question']=question
    rows.append(r)
io.open('ledgers/_rows.jsonl','w',encoding='utf-8').write('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n')
v=collections.Counter(r['verdict'] for r in rows); ex=collections.Counter(r['reason'] for r in rows if r['verdict']=='EXCLUDE')
jud=[r['n'] for r in rows if r['judgment'] and r['verdict']=='EXCLUDE']
print('verdicts',dict(v)); print('exclusions',dict(ex)); print('judgement exclusions',jud,'share %.3f'%(len(jud)/len(rows)))
