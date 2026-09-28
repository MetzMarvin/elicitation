# Pass 2 parallel run: queue split and shared-browser rules (2026-09-24)

Orchestrator: session `elicitation-5a`. Three workers share one Chrome (`cdp1`, port 9222).

## Queues (each worker runs its own list top to bottom)

| Worker | Queue |
|---|---|
| `elicitation-3a` | bizagi · atamya · citeck-ecos · quantumbpm · newgen · aletyx · appian · ibm-developer-watsonx · frends-docs |
| `elicitation-6f` | oracle-oic · creatio · scheer-pas · bonitasoft · ibm-bamoe · processmaker · flowx-ai · trisotech |
| `elicitation-74` | ifs-cloud-docs · loyjoy · cib-seven · uipath-maestro-docs · flowable · firestart · camunda-docs-blog · camunda-marketplace |
| reassigned 2026-09-25 | `elicitation-74` is now `elicitation-aa` (Flowable visual pass only). Its remaining queue moved: camunda-docs-blog → `elicitation-6f` (after its trisotech video checks); camunda-marketplace → `elicitation-aa` (after Flowable, 2026-09-26); firestart → `elicitation-3a` (after frends-docs). Appian was ruled OUT (C2) by the operator. |
| held back | uipath-marketplace (needs a logged-in UiPath session; the orchestrator assigns it later) |

Never work on a source outside your queue. A source whose assignment file shows `status:`
other than `READY` belongs to someone else or is finished.

## Shared-browser rules

1. At the start, open **your own tab** with `new_page` and note its page id. Do all your work
   in that tab (`select_page` it again if you are ever unsure which page is selected).
2. Never navigate, reload, close or read another tab. Do not use `list_pages` to pick up
   someone else's page.
3. When a page needs a second tab (popup, new window), close that extra tab yourself when done.
4. Global pacing: at most about one page load per second **per worker**. If a vendor serves a
   bot challenge, stop hitting that domain, and write a `BLOCKED` row plus an OPERATOR-TODO
   entry.
5. At the end of your queue, close your own tab only.

## Shared files

- `sources/OPERATOR-TODO.md` and `tools/audit.py` are shared. Append to OPERATOR-TODO under
  `## Pass 2 blockers` in one edit, re-reading the file just before. Never edit
  `tools/audit.py` or `tools/accepted_shares.json` (operator-owned): report problems with it to the orchestrator.
- Everything under `ledgers/<slug>*` and `corpus/<slug>/` belongs to whoever owns that slug.
- When you start a source, set its assignment frontmatter to
  `status: IN-PROGRESS (<your session name>)`. When it passes the audit, set it to `status: DONE (...)`.
