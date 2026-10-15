"""Digest a UiPath Maestro .bpmn: elements, bindings, flows. Usage: python -I _uipst_digest.py FILE.bpmn"""
import sys
import xml.etree.ElementTree as ET

NS = {"bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL", "uipath": "http://uipath.org/schema/bpmn"}
B = "{%s}" % NS["bpmn"]
U = "{%s}" % NS["uipath"]
SKIP = {"incoming", "outgoing", "extensionElements", "sequenceFlow", "conditionExpression", "script",
        "documentation", "laneSet", "lane", "flowNodeRef", "text", "association", "dataInputAssociation",
        "dataOutputAssociation", "sourceRef", "targetRef"}

root = ET.parse(sys.argv[1]).getroot()
names = {}
for el in root.iter():
    if el.get("id"):
        names[el.get("id")] = el.get("name") or el.get("id")


def binding(el):
    ext = el.find(B + "extensionElements")
    if ext is None:
        return ""
    bits = []
    for x in ext.iter():
        t = x.tag.replace(U, "u:")
        if t in ("u:type", "u:serviceType", "u:bindings", "u:activityType"):
            bits.append(f"{t}={x.get('value') or x.attrib}")
        elif t == "u:context":
            for c in x:
                if c.get("name") in ("name", "folderPath", "resourceKey", "resource", "connector", "operation", "objectName"):
                    bits.append(f"{c.get('name')}={(c.get('value') or (c.text or '')).strip()[:80]}")
        elif t in ("u:input",) and x.get("name") in ("prompt", "userPrompt", "systemPrompt", "instructions"):
            bits.append(f"{x.get('name')}={(x.text or x.get('value') or '')[:200]!r}")
    return "; ".join(bits)


def walk(parent, depth=0):
    for el in parent:
        tag = el.tag.replace(B, "")
        if not tag.startswith("{") and tag not in SKIP:
            extra = ""
            if tag == "boundaryEvent":
                extra = f" attachedTo={names.get(el.get('attachedToRef'))}"
                defs = [d.tag.replace(B, "") for d in el if d.tag.endswith("EventDefinition")]
                extra += f" {defs}"
            if tag.endswith("Event") and tag != "boundaryEvent":
                defs = [d.tag.replace(B, "") for d in el if d.tag.endswith("EventDefinition")]
                if defs:
                    extra += f" {defs}"
            if tag == "textAnnotation":
                extra = " TEXT=" + repr((el.findtext(B + "text") or "")[:200])
            if tag == "adHocSubProcess" or tag == "subProcess":
                extra += " {"
            print("  " * depth + f"{tag} [{el.get('id')}] {el.get('name')!r}{extra}  {binding(el)}")
            if tag in ("subProcess", "adHocSubProcess", "process", "transaction"):
                walk(el, depth + 1)
                print("  " * depth + "}")
        if tag == "process":
            pass


for proc in root.findall(B + "process"):
    print(f"PROCESS {proc.get('id')} {proc.get('name')!r}")
    walk(proc, 1)
    for ls in proc.iter(B + "lane"):
        print(f"  LANE {ls.get('name')!r}: {[names.get(r.text) for r in ls.findall(B + 'flowNodeRef')]}")
print("COLLAB:", [(p.get("name"), p.get("processRef")) for p in root.iter(B + "participant")])
print("FLOWS:")
for f in root.iter(B + "sequenceFlow"):
    cond = f.findtext(B + "conditionExpression") or ""
    print(f"  {names.get(f.get('sourceRef'))} -> {names.get(f.get('targetRef'))}"
          + (f" [{f.get('name')}]" if f.get("name") else "") + (f" ({cond.strip()[:120]})" if cond else ""))
for f in root.iter(B + "messageFlow"):
    print(f"  MSG {names.get(f.get('sourceRef'))} => {names.get(f.get('targetRef'))}")
for f in root.iter(B + "association"):
    print(f"  ASSOC {names.get(f.get('sourceRef'))} .. {names.get(f.get('targetRef'))}")
