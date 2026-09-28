"""trisotech video class: decode captured frames and build contact sheets.

The frames are captured by an in-page canvas grab (evaluate_script -> frames.json,
a list of {t, j} where j is a JPEG data URL) from the YouTube *embed* loaded in my own
cdp1 tab with a Referer header naming the page that really embeds it.

  python _ts_vid.py decode <slug> [cell]   -> writes frame_*.jpg + sheet_*.png
  python _ts_vid.py list                   -> the 22 video slugs -> youtube id
  python _ts_vid.py js <slug>              -> prints the capture script for that video
"""
import base64, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
VID = os.path.join(RAW, "video")

VIDS = json.load(open(os.path.join(RAW, "vid_index.json"), encoding="utf-8"))


def index():
    out = []
    for e in VIDS:
        stem = e["file"][:-4]
        slug, _, yid = stem.rpartition("__")
        out.append({"n": e["n"], "slug": slug, "yid": yid})
    return out


# the 22 UNCERTAIN video rows of the trisotech ledger
WANT = ["5-min-intro-to-bpmn", "ai-agents-in-healthcare", "ai-and-bpm", "ai-driven-healthcare-orchestration",
        "ai-fhir-and-bpm-in-suicide-prevention", "automation-of-loan-origination",
        "bpmn-user-tasks-for-humans-and-ai-agents", "clinician-centric-data-and-ai-integration-in-healthcare",
        "contracts-and-the-knowledge-worker-copilot", "decision-framework-for-machine-learning-webinar",
        "enterprise-ai-in-2026", "generative-ai-and-regulatory-compliance", "harness-genai-and-agentic-ai",
        "hl7-ai-challenge-winners", "how-bpm-health-complements-fhir",
        "it-takes-all-kinds-of-ai-and-humans-to-make-good-business-decision", "knowledge-worker-copilot-in-the-loop",
        "low-code-neuro-symbolic-agents", "mastering-decision-orchestration",
        "optimizing-preoperative-assessments", "the-role-of-genai",
        "who-made-that-decision-governing-decisions-in-the-age-of-ai-agents"]


def by_slug(slug):
    for r in index():
        if r["slug"] == slug or slug.startswith(r["slug"]) or r["slug"].startswith(slug[:45]):
            return r
    return None


# The capture routine. Stored once in the embed origin's localStorage as a *string* and
# re-evaluated per video with one short call, so the body does not have to be re-pasted.
#
# Two resolutions: a frame whose 128x72 grey signature differs from the last *kept* frame
# by >= THR is a slide transition and is kept at full video resolution; every other frame
# is kept at 320x180 only. The signature-diff distribution measured over this source's
# videos is bimodal -- static stretches 0.0-0.4, slide transitions 3.2-85.9 -- so THR=2.0
# sits in the empty middle with a wide margin on both sides. The grid is fine (~1/110 of
# the runtime, i.e. 17 s on a 31-minute webinar) because a slide that is on screen between
# two samples and gone by the next would otherwise be invisible.
CAP = """async (YID, CHAPTERS) => {
  const v = document.querySelector('video');
  if (!v) return {err: 'no video', url: location.href};
  const THR = 2.0;
  const wait = ms => new Promise(r => setTimeout(r, ms));
  v.muted = true;
  try { await v.play(); } catch (e) {}
  for (let i = 0; i < 40 && !(v.readyState >= 2 && v.videoWidth); i++) await wait(250);
  const dur = v.duration;
  if (!isFinite(dur)) return {err: 'no duration', url: location.href};
  const step = Math.max(4, Math.ceil(dur / 110));
  const times = [];
  for (let t = 2; t < dur - 1; t += step) times.push(Math.round(t));
  for (const ch of (CHAPTERS || [])) if (ch < dur - 1) times.push(ch);
  times.sort((a, b) => a - b);
  const c = document.createElement('canvas');
  const cctx = c.getContext('2d');
  const s = document.createElement('canvas'); s.width = 128; s.height = 72;
  const sctx = s.getContext('2d');
  const sm = document.createElement('canvas'); sm.width = 320; sm.height = 180;
  const smctx = sm.getContext('2d');
  const grab = t => new Promise(res => {
    let fired = false;
    const fin = () => { if (!fired) { fired = true; v.removeEventListener('seeked', on); res(); } };
    const on = () => { v.requestVideoFrameCallback(() => setTimeout(fin, 30)); };
    v.addEventListener('seeked', on);
    v.currentTime = t;
    setTimeout(fin, 2500);
  });
  const out = [];
  let prev = null;
  for (const t of times) {
    await grab(t);
    c.width = v.videoWidth; c.height = v.videoHeight;
    cctx.drawImage(v, 0, 0);
    sctx.drawImage(v, 0, 0, 128, 72);
    const px = sctx.getImageData(0, 0, 128, 72).data;
    let m = null;
    if (prev) { let acc = 0; for (let i = 0; i < px.length; i += 4) acc += Math.abs(px[i] - prev[i]); m = acc / (128 * 72); }
    const changed = !prev || m >= THR;
    prev = px;
    let j;
    if (changed) { j = c.toDataURL('image/jpeg', 0.85); }
    else { smctx.drawImage(v, 0, 0, 320, 180); j = sm.toDataURL('image/jpeg', 0.72); }
    out.push({t: Math.round(v.currentTime * 10) / 10, c: changed, d: m === null ? null : Math.round(m * 100) / 100, j});
  }
  return {id: YID, dur, step, vw: v.videoWidth, vh: v.videoHeight, frames: out};
}"""


CAPS = """async () => {
  const pr = window.ytInitialPlayerResponse || {};
  const tr = (((pr.captions || {}).playerCaptionsTracklistRenderer) || {}).captionTracks || [];
  if (!tr.length) return {err: 'no caption tracks'};
  const out = [];
  for (const c of tr.slice(0, 2)) {
    const r = await fetch(c.baseUrl + '&fmt=json3');
    out.push({lang: c.languageCode, kind: c.kind || 'manual', body: await r.text()});
  }
  return {title: ((pr.videoDetails || {}).title), tracks: out};
}"""



# Chunked variant, because a single call over a long video blows the CDP
# Runtime.callFunctionOn timeout (measured: the ai-fhir-and-bpm-in-suicide-prevention capture died
# that way). It works a time range at a time, stopping itself after BUDGET ms of wall clock and
# reporting `resumeAt`, and accumulates every frame in window.__acc so one short final call can hand
# the lot to a file. Same detector, same two resolutions as CAP.
CAPC = """async (YID, FROM) => {
  const THR = 2.0, BUDGET = 55000;
  const t0 = Date.now();
  const v = document.querySelector('video');
  if (!v) return {err: 'no video', url: location.href};
  const wait = ms => new Promise(r => setTimeout(r, ms));
  v.muted = true;
  try { await v.play(); } catch (e) {}
  for (let i = 0; i < 40 && !(v.readyState >= 2 && v.videoWidth); i++) await wait(250);
  const dur = v.duration;
  if (!isFinite(dur)) return {err: 'no duration', url: location.href};
  const step = Math.max(4, Math.ceil(dur / 110));
  const to = Math.min(dur - 1, FROM + step * 110);
  const c = document.createElement('canvas');
  const cctx = c.getContext('2d');
  const s = document.createElement('canvas'); s.width = 128; s.height = 72;
  const sctx = s.getContext('2d');
  const sm = document.createElement('canvas'); sm.width = 320; sm.height = 180;
  const smctx = sm.getContext('2d');
  const grab = t => new Promise(res => {
    let fired = false;
    const fin = () => { if (!fired) { fired = true; v.removeEventListener('seeked', on); res(); } };
    const on = () => { v.requestVideoFrameCallback(() => setTimeout(fin, 30)); };
    v.addEventListener('seeked', on);
    v.currentTime = t;
    setTimeout(fin, 2500);
  });
  if (!window.__acc) window.__acc = [];
  let t = FROM, prev = window.__prev || null, n = 0;
  while (t < to) {
    await grab(t);
    c.width = v.videoWidth; c.height = v.videoHeight;
    cctx.drawImage(v, 0, 0);
    sctx.drawImage(v, 0, 0, 128, 72);
    const px = sctx.getImageData(0, 0, 128, 72).data;
    let m = null;
    if (prev) { let acc = 0; for (let i = 0; i < px.length; i += 4) acc += Math.abs(px[i] - prev[i]); m = acc / (128 * 72); }
    const changed = !prev || m >= THR;
    prev = px;
    let j;
    if (changed) { j = c.toDataURL('image/jpeg', 0.85); }
    else { smctx.drawImage(v, 0, 0, 320, 180); j = sm.toDataURL('image/jpeg', 0.72); }
    window.__acc.push({t: Math.round(v.currentTime * 10) / 10, c: changed,
                       d: m === null ? null : Math.round(m * 100) / 100, j});
    n++;
    t += step;
    if (Date.now() - t0 > BUDGET) break;
  }
  window.__prev = prev;
  return {done: t >= to, resumeAt: t, n, dur, step, vw: v.videoWidth, vh: v.videoHeight,
          total: window.__acc.length};
}"""


def store_js():
    """The one call that installs CAP + CAPS in the embed origin's localStorage."""
    return ("async () => { localStorage.setItem('tscap', %s); localStorage.setItem('tscaps', %s); "
            "localStorage.setItem('tscapc', %s); "
            "return [localStorage.getItem('tscap').length, localStorage.getItem('tscaps').length, "
            "localStorage.getItem('tscapc').length]; }"
            % (json.dumps(CAP), json.dumps(CAPS), json.dumps(CAPC)))


def call_js(slug, chapters=None):
    r = by_slug(slug)
    return ("async () => await eval(localStorage.getItem('tscap'))(%s, %s)"
            % (json.dumps(r["yid"]), json.dumps(chapters or [])))


def decode(slug, cell=300, cols=6, per=24):
    """Decode frames.json -> per-frame JPEGs (full-res on slide transitions, 320x180
    otherwise), a full-grid contact sheet, and a 'changes' sheet holding only the
    transition frames -- the sheet to actually look at, one cell per distinct slide.

    The transition flag comes from the capture itself (128x72 grey signature diff >= 2.0
    against the last kept frame), which is what makes the fine grid affordable: see the
    CAP docstring for the measured separation between static stretches and transitions.
    """
    from PIL import Image, ImageDraw
    d = os.path.join(VID, slug)
    obj = json.load(open(os.path.join(d, "frames.json"), encoding="utf-8"))
    if "err" in obj:
        print("ERR", obj)
        return []
    fr = obj["frames"]
    print("%s  id=%s  dur=%.0fs step=%ds grid=%d frames  size=%dx%d"
          % (slug, obj["id"], obj["dur"], obj["step"], len(fr), obj["vw"], obj["vh"]))
    paths, keep = [], []
    for i, f in enumerate(fr):
        p = os.path.join(d, "f%03d_%04d.jpg" % (i, int(f["t"])))
        with open(p, "wb") as fh:
            fh.write(base64.b64decode(f["j"].split(",")[1]))
        paths.append((i, int(f["t"]), p))
        if f.get("c") or i == 0:
            keep.append(i)
    print("  transitions (%d): %s" % (len(keep),
          " ".join("f%03d=%ds" % (paths[i][0], paths[i][1]) for i in keep)))
    print("  diff series: " + " ".join("%ds:%s" % (int(f["t"]), f.get("d")) for f in fr if f.get("d") is not None))

    ch = int(cell * obj["vh"] / obj["vw"])
    lab = 20

    def sheet(chunk, name):
        rows = (len(chunk) + cols - 1) // cols
        sh = Image.new("RGB", (cols * cell, rows * (ch + lab)), "white")
        dr = ImageDraw.Draw(sh)
        for k, (i, t, p) in enumerate(chunk):
            x, y = (k % cols) * cell, (k // cols) * (ch + lab)
            sh.paste(Image.open(p).resize((cell, ch)), (x, y))
            dr.rectangle([x, y + ch, x + cell, y + ch + lab], fill="black")
            dr.text((x + 4, y + ch + 4), "f%03d t=%ds" % (i, t), fill="white")
        sh.save(os.path.join(d, name))
        print("  %s  (%d cells)" % (name, len(chunk)))

    for s in range(0, len(paths), per * 2):
        sheet(paths[s:s + per * 2], "sheet_%d.png" % (s // (per * 2) + 1))
    if len(keep) > 0.7 * len(paths):
        print("  continuous motion: %d of %d frames flagged, chg sheets are useless here - "
              "read the full sheets instead" % (len(keep), len(paths)))
    else:
        for s in range(0, len(keep), per):
            sheet([paths[i] for i in keep[s:s + per]], "chg_%d.png" % (s // per + 1))
    return paths


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "list":
        for r in index():
            mark = "*" if any(r["slug"].startswith(w[:45]) for w in WANT) else " "
            print("%s %2d %-64s %s" % (mark, r["n"], r["slug"], r["yid"]))
    elif cmd == "store":
        print(store_js())
    elif cmd == "call":
        ch = json.loads(sys.argv[3]) if len(sys.argv) > 3 else None
        print(call_js(sys.argv[2], ch))
    elif cmd == "decode":
        a = sys.argv[2:]
        decode(a[0])
    elif cmd == "pick":
        # pick <slug> <cell> <cols> <fNNN> [fNNN ...] -- labelled sheet of chosen frames
        from PIL import Image, ImageDraw
        a = sys.argv[2:]
        slug, cell, cols = a[0], int(a[1]), int(a[2])
        d = os.path.join(VID, slug)
        want = a[3:]
        files = []
        for f in sorted(os.listdir(d)):
            if f.startswith("f") and f.endswith(".jpg") and f.split("_")[0] in want:
                files.append(f)
        files.sort(key=lambda f: int(f.split("_")[0][1:]))
        if not files:
            print("no frames matched", want)
            raise SystemExit(1)
        im0 = Image.open(os.path.join(d, files[0]))
        ch = int(cell * im0.height / im0.width)
        rows = (len(files) + cols - 1) // cols
        sh = Image.new("RGB", (cols * cell, rows * (ch + 20)), "white")
        dr = ImageDraw.Draw(sh)
        for k, f in enumerate(files):
            x, y = (k % cols) * cell, (k // cols) * (ch + 20)
            sh.paste(Image.open(os.path.join(d, f)).resize((cell, ch)), (x, y))
            dr.rectangle([x, y + ch, x + cell, y + ch + 20], fill="black")
            dr.text((x + 4, y + ch + 4), f[:-4], fill="white")
        out = os.path.join(d, "pick_%s.png" % "_".join(want))
        sh.save(out)
        print(out, sh.size)
    elif cmd == "crop":
        # crop <slug> <frame-file> <x0> <y0> <x1> <y1> [scale]  -- zoom into a frame
        from PIL import Image
        a = sys.argv[2:]
        p = os.path.join(VID, a[0], a[1])
        im = Image.open(p)
        box = tuple(int(x) for x in a[2:6])
        sc = float(a[6]) if len(a) > 6 else 2.0
        c = im.crop(box)
        c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
        out = p.replace(".jpg", "_crop.png")
        c.save(out)
        print(out, c.size)
    elif cmd == "url":
        r = by_slug(sys.argv[2])
        print("https://www.youtube.com/embed/%s?autoplay=1&mute=1&playsinline=1"
              "&origin=https%%3A%%2F%%2Fwww.trisotech.com" % r["yid"])
    elif cmd == "file":
        print("C:\\Users\\muffi\\Desktop\\Uni\\Master_thesis\\elicitation\\ledgers\\"
              "trisotech.raw\\video\\%s\\frames.json" % sys.argv[2])
    else:
        print(__doc__)
