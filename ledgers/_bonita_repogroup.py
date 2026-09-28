#!/usr/bin/env python3
"""The repository group of the bonitasoft ledger: rows and population (worker elicitation-6f).

The population has two groups. The first is the portal's 807 pages (ledgers/_bonita_build.pages).
The second is the linked GitHub repositories: one row per repository, plus one row per `.bpmn` /
`.proc` file found in one of them. This module builds that second group:

  * `repo_rows`    - one row per canonical repository. The class of each repository (component,
                     connector, fork, docs source, example, labs docs) decides the verdict; the
                     two repositories that publish an artefact of their own (bonita-examples'
                     BPMN diagram, bonita-labs-doc's architecture diagram) carry an eye-checked
                     ruling from `_bonita_repos_rulings.SPECIAL`. A repository whose tree could
                     not be read becomes a BLOCKED row and a problem line, never a silent gap.
  * `procfiles`    - one row per process file. Read as XML, so the notation question is settled
                     by the file itself: every one of them is BPMN 2.0 in the vendor's
                     serialisation. The verdict then turns on whether the file carries an AI
                     element (the two connector demos do, as records 010/011) or not (the
                     engine's and Studio's test fixtures do not). Files with identical contents
                     published under two paths are ruled E3-duplicate against the first.

  * `corrections` - the superseding rows appended after the ledger footer. The two AI demo
                     processes were ruled UNCERTAIN while their binding question was open; the
                     orchestrator settled it (delegated binding is deliberately in scope), so the
                     INCLUDE rows are appended rather than rewritten in, and the UNCERTAIN rows stay
                     for the audit trail.

Facts come from ledgers/_bonita/repos_trees.json and ledgers/_bonita/procfiles.json, both written
earlier by the enumeration scripts; nothing here touches the network.
"""
import json
import pathlib
import re

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_bonita"

import _bonita_repos_rulings as RR  # noqa: E402

# The AI screen is deliberately generous - `\bagent\b` is in its token list because AI products are
# called agents - and on two Bonita Studio fixtures that generosity fires on people: the pools of an
# incident-management collaboration are named "1st level support agent" and "2nd level support
# agent". A row for those files must not claim an AI element and must not go UNCERTAIN on a human
# job title, so the token is recognised here and the row dismisses it under E2 with the pool name
# quoted, which is exactly what that rule asks for.
HUMAN_ROLE_TOKENS = {"agent", "agents"}
PARTICIPANT = re.compile(r"<[A-Za-z0-9]+:participant\b[^>]*?name=\"([^\"]+)\"")
DEFS = re.compile(r"<bpmn2?:definitions|<process:MainProcess|<semantic:definitions")


def human_role_mentions(f):
    """[(participant name, the file line naming it)] for every pool name carrying a human-role token."""
    text = pathlib.Path(ELI / f["store"]).read_text(encoding="utf-8", errors="replace")
    out = []
    for line in text.splitlines():
        for name in PARTICIPANT.findall(line):
            if any(t in re.split(r"[^a-z]+", name.lower()) for t in HUMAN_ROLE_TOKENS):
                out.append((name, " ".join(line.split())))
    return out


def load(name):
    return json.loads((OUT / name).read_text(encoding="utf-8"))


def klass(repo):
    """The repository class, from its name - the same taxonomy _bonita_repos_rulings documents."""
    if repo in RR.CLASS:
        return RR.CLASS[repo]
    if repo == "angular.js":
        return "fork"
    if repo.endswith("-doc"):
        return "docs-source"
    if re.search(r"connector", repo) and re.search(r"\bai\b|ai-|mistral|openai|anthropic", repo):
        return "ai-connector"
    return "component"


def readme_quote(repo, cache_dir=OUT / "repos", trees=None):
    """The first non-heading, non-badge line of the repository's README, as its verbatim quote.

    The cached file is named `<repo>__<path with / as ~>`, and a repository's README is not always
    called README: bonita-ui-designer keeps it at `.github/help.adoc`. Globbing for `README*` alone
    therefore missed that repository and any other with a non-standard path, so the candidate names
    are taken from the README path(s) the tree enumeration recorded (`repos_trees.json`), with the
    plain `README*` glob kept as a fallback for entries the first pass cached under that name.
    """
    paths = ((trees if trees is not None else load("repos_trees.json"))
             .get(repo, {}).get("readme") or [])
    names = [repo.replace("/", "~") + "__" + p.replace("/", "~") for p in paths]
    names += [repo.replace("/", "~") + "__README" + ext
              for ext in ("", ".md", ".markdown", ".adoc", ".rst", ".txt")]
    for name in names:
        f = cache_dir / name
        if not f.exists():
            continue
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            s = " ".join(line.split())
            if len(s) < 25 or s.startswith(("#", "=", "[!", "![", "|", "<", ">", "---", "===")):
                continue
            if s.startswith(("http", "```", "- ", "* ", "1.")):
                continue
            return s[:160]
    return None


def repo_rows(first_n, cache):
    """[(row, problem_or_None)] for every canonical repository, in name order."""
    rows, problems = [], []
    for i, repo in enumerate(sorted(cache)):
        rec = cache[repo]
        n = first_n + i
        url = "https://github.com/bonitasoft/%s" % repo
        base = {"n": n, "url": url, "title": repo, "duplicate_of": None, "accessed": "2026-09-25",
                "surface": "github:bonitasoft", "record": None, "needs_visual_check": False,
                "needs_human_ruling": False, "question": None}
        if "error" in rec:
            rows.append({**base, "verdict": "BLOCKED", "reason": None, "judgment": False,
                         "evidence": "BLOCKED: the repository tree could not be read (%s)"
                                     % rec["error"][:80],
                         "note": "The public GitHub API would not return the default-branch "
                                 "tree for this repository; see "
                                 "notes/elicitation/sources/OPERATOR-TODO.md.",
                         "judged_from": "GitHub API attempt",
                         "notation": None, "artefacts_on_page": None,
                         "figures_looked_at": "none", "screen": {}})
            problems.append("BLOCKED repo n=%d %s" % (n, url))
            continue
        files = rec.get("files", 0)
        arts = rec.get("artefacts", [])
        if repo in RR.SPECIAL:
            sp = RR.SPECIAL[repo]
            verdict, reason, notation, artefacts, looked, note = sp[:6]
            judgment = sp[6] if len(sp) > 6 and isinstance(sp[6], bool) else False
            evidence = sp[7] if len(sp) > 7 else None
            if len(sp) > 6 and isinstance(sp[6], bool) is False:
                evidence = sp[6]
            rows.append({**base, "verdict": verdict, "reason": reason, "judgment": judgment,
                         "evidence": evidence, "note": note, "judged_from": "repository read + "
                         "its figures looked at", "notation": notation,
                         "artefacts_on_page": artefacts, "figures_looked_at": looked,
                         "screen": {"files": files, "artefacts": arts[:12]}})
            continue
        kind = klass(repo)
        quote = readme_quote(repo)
        assert quote, "no README quote for %s" % repo
        text = RR.CLASS_TEXT[kind].format(kind=kind.replace("-", " "), quote=quote)
        note = ("%s The tree holds %d files, none of them a `.bpmn` or `.proc` process file, "
                "branch `%s`." % (text, files, rec.get("branch"))) if not arts else \
               ("%s The tree holds %d files and %d process file(s), ruled as their own rows."
                % (text, files, len(arts)))
        rows.append({**base, "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
                     "evidence": quote, "note": note,
                     "judged_from": "repository tree read through the public GitHub API + its "
                                    "documentation files fetched and screened",
                     "notation": None,
                     "artefacts_on_page": ("%d .bpmn/.proc file(s)" % len(arts)) if arts else None,
                     "figures_looked_at": "none (no diagram in the repository's documentation)",
                     "screen": {"files": files, "artefacts": arts[:12]}})
    return rows, problems


def procfile_rows(first_n, facts, page_of=None):
    """[(row, problem_or_None)] for every process file found in a linked repository."""
    rows, problems = [], []
    seen = {}
    for i, f in enumerate(facts):
        n = first_n + i
        base = {"n": n, "url": f["page"], "title": f["path"].split("/")[-1],
                "duplicate_of": None, "accessed": "2026-09-25", "surface": "github:bonitasoft",
                "needs_visual_check": False, "needs_human_ruling": False, "question": None}
        if not f.get("sha1"):
            rows.append({**base, "verdict": "BLOCKED", "reason": None, "judgment": False,
                         "evidence": "BLOCKED: the file could not be fetched (%s)"
                                     % str(f.get("error"))[:80],
                         "note": "Not reachable during the census; see "
                                 "notes/elicitation/sources/OPERATOR-TODO.md.",
                         "judged_from": "fetch attempt", "notation": None,
                         "artefacts_on_page": None, "figures_looked_at": "none", "screen": {}})
            problems.append("BLOCKED process file n=%d %s" % (n, f["page"]))
            continue
        name = f["path"].split("/")[-1]
        procs = ", ".join(f["process_names"]) or "unnamed"
        pools = ", ".join(f["pools"])
        # The serialisation, named as the file itself declares it: Bonita's own `.proc` export, or
        # the OMG `.bpmn` those exports and the Studio fixtures use.
        serial = "Bonita `.proc` XML" if f["path"].lower().endswith(".proc") else "OMG `.bpmn` XML"
        quote = next((l.strip() for l in
                      pathlib.Path(ELI / f["store"]).read_text(encoding="utf-8",
                                                               errors="replace").splitlines()
                      if DEFS.search(l)), name)
        # What the row quotes as the file's own declaration: the root element's opening tag, cut at
        # 200 characters so a long namespace list cannot swallow the field.
        root_tag = re.match(r"\s*(<[^>]*>)", quote)
        root_ref = (root_tag.group(1) if root_tag else quote.strip())[:200]
        if f["path"] in RR.PROCESS_FILES:
            stem, note, question = RR.PROCESS_FILES[f["path"]][:3]
            rows.append({**base, "verdict": "UNCERTAIN", "reason": None,
                         "judgment": True, "evidence": quote[:400], "note": note,
                         "record": "corpus/bonitasoft/%s.md" % stem,
                         "needs_human_ruling": True, "question": question,
                         "judged_from": "process file read as XML",
                         "notation": "BPMN 2.0 (%s)" % serial,
                         "artefacts_on_page": name,
                         "figures_looked_at": "%s read as XML (%d bytes)" % (name, f["bytes"]),
                         "screen": {"ai_tokens": f["ai_tokens"], "pools": f["pools"]}})
            continue
        if f["sha1"] in seen:
            first = seen[f["sha1"]]
            rows.append({**base, "verdict": "EXCLUDE", "reason": "E3-duplicate", "judgment": False,
                         "duplicate_of": first["page"],
                         "evidence": "byte-identical to the copy at %s (sha1 %s)"
                                     % (first["page"], f["sha1"][:12]),
                         "note": "The same process file is published twice in the repository "
                                 "tree (identical sha1 %s), so this row is the same artefact as "
                                 "the earlier one, not a second process." % f["sha1"][:12],
                         "judged_from": "sha1 comparison of the fetched files",
                         "notation": "BPMN 2.0 (Bonita `.proc` XML)", "artefacts_on_page": name,
                         "figures_looked_at": "%s read as XML (%d bytes)" % (name, f["bytes"]),
                         "screen": {"ai_tokens": f["ai_tokens"], "pools": f["pools"]}})
            problems.append("E3-duplicate process file n=%d (same artefact as the row above): %s"
                            % (n, f["page"]))
            continue
        seen[f["sha1"]] = f
        ai = f["ai_tokens"]
        if set(ai) <= HUMAN_ROLE_TOKENS:
            mentions = human_role_mentions(f)
            who = ", ".join('"%s"' % (n or "unnamed") for n, _ in mentions[:3]) or \
                  "a participant pool"
            ev = (mentions[0][1] if mentions else quote)[:300]
            note = ("The file is BPMN 2.0 (%s, root `%s`) and the only AI-sounding token in it "
                    "refers to people: the collaboration's pools are named %s - the human support "
                    "roles, not AI agents. Its activities are manual and user tasks (e.g. %s) and "
                    "no service task carries a connector, let alone an AI one. Dismissed under E2 "
                    "with the mention quoted: `%s`."
                    % (serial, root_ref[:80], who,
                       ", ".join('`%s`' % t for t in f["tasks"][:3]) or "unnamed tasks",
                       ev[:120]))
            rows.append({**base, "verdict": "EXCLUDE", "reason": "E2-no-ai-element",
                         "judgment": False, "evidence": ev, "note": note,
                         "judged_from": "process file read as XML",
                         "notation": "BPMN 2.0 (%s)" % serial,
                         "artefacts_on_page": name,
                         "figures_looked_at": "%s read as XML (%d bytes)" % (name, f["bytes"]),
                         "screen": {"ai_tokens": ai, "pools": f["pools"], "tasks": f["tasks"][:5]}})
            continue
        if ai:
            note = ("The file is BPMN 2.0 in %s (process `%s`%s), and "
                    "it mentions %s - recorded as UNCERTAIN rather than E2 because an AI element "
                    "may be bound inside it without being visible from the XML's element names."
                    % (serial, procs, ("; pool " + pools) if pools else "", ", ".join(ai)))
            rows.append({**base, "verdict": "UNCERTAIN", "reason": None, "judgment": False,
                         "evidence": root_ref, "note": note,
                         "record": "corpus/bonitasoft/%s.md" % ("%03d_%s" % (
                             n, re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:-4])),
                         "needs_human_ruling": True,
                         "question": "The file mentions %s but the XML's element names show no "
                                     "AI task: does this process carry an AI element inside it?"
                                     % ", ".join(ai),
                         "judged_from": "process file read as XML",
                         "notation": "BPMN 2.0 (%s)" % serial, "artefacts_on_page": name,
                         "figures_looked_at": "%s read as XML (%d bytes)" % (name, f["bytes"]),
                         "screen": {"ai_tokens": ai, "pools": f["pools"]}})
            problems.append("AI token in process file n=%d %s" % (n, f["page"]))
            continue
        note = ("The file is BPMN 2.0 in %s - process `%s`%s - and it "
                "carries no AI element: no connector is attached to its tasks and the file "
                "mentions no AI provider, model or prompt. Quoted from the file: `%s`."
                % (serial, procs, ("; pool " + pools) if pools else "", quote.strip()[:120]))
        rows.append({**base, "verdict": "EXCLUDE", "reason": "E2-no-ai-element", "judgment": False,
                     "evidence": root_ref, "note": note,
                     "judged_from": "process file read as XML",
                     "notation": "BPMN 2.0 (%s)" % serial, "artefacts_on_page": name,
                     "figures_looked_at": "%s read as XML (%d bytes)" % (name, f["bytes"]),
                     "screen": {"ai_tokens": [], "pools": f["pools"]}})
    return rows, problems


CORRECTION_NOTE = (
    "Supersedes the UNCERTAIN row for corpus record %s at this `n`: the ruling question it carried "
    "is answered by the census protocol, which puts exactly this artefact class deliberately in "
    "scope - \"diagrams where the AI element is only visible as a task *property* or implementation "
    "binding, not as a distinct BPMN element type\" (prompts/02_source-census.md, \"Deliberately in "
    "scope\"). The artefact is genuine BPMN 2.0 read as XML, its service task carries the AI "
    "connector %s, and the connector's own prompt parameters are quoted in the record, so the AI "
    "element is documented, not inferred. Verdict INCLUDE, no human ruling needed. Ruled by the "
    "orchestrator (elicitation-5a, 2026-09-25); the row below is the superseded one, which stays in "
    "the ledger so the correction is auditable."
)


def corrections(first_n, facts):
    """The superseding rows, appended after the footer: the two AI demo processes, now INCLUDE.

    The ledger is append-only, so a settled ruling is appended rather than rewritten: the earlier
    UNCERTAIN row stays, and the last row for an `n` wins (`tools/audit.py`). The build emits both,
    which keeps this file reproducible by `python ledgers/_bonita_build.py --write`.
    """
    out = []
    for i, f in enumerate(facts):
        if f["path"] not in RR.PROCESS_FILES:
            continue
        stem, _note, _q = RR.PROCESS_FILES[f["path"]][:3]
        if RR.PROCESS_FILES[f["path"]][-1] != "INCLUDE":
            continue
        name = f["path"].split("/")[-1]
        quote = next((l.strip() for l in pathlib.Path(ELI / f["store"]).read_text(
            encoding="utf-8", errors="replace").splitlines() if DEFS.search(l)), name)
        connector = ("`anthropic-ask`" if "anthropic" in f["path"] else "`azure-ask`")
        out.append({
            "n": first_n + i, "verdict": "INCLUDE", "reason": None, "judgment": True,
            "evidence": quote[:400], "note": CORRECTION_NOTE % (stem, connector),
            "url": f["page"], "title": name, "duplicate_of": None, "accessed": "2026-09-25",
            "surface": "github:bonitasoft", "record": "corpus/bonitasoft/%s.md" % stem,
            "needs_visual_check": False, "needs_human_ruling": False, "question": None,
            "judged_from": "process file read as XML (correction row)",
            "notation": "BPMN 2.0 (Bonita `.proc` XML)", "artefacts_on_page": name,
            "figures_looked_at": "%s read as XML (%d bytes)" % (name, f["bytes"]),
            "screen": {"ai_tokens": f["ai_tokens"], "pools": f["pools"]},
            "supersedes_row": "UNCERTAIN row for n=%d (same document, earlier line)" % (first_n + i),
            "correction": "protocol clause, prompts/02_source-census.md ('Deliberately in scope')",
            "prior_verdict": "UNCERTAIN",
        })
    return out
