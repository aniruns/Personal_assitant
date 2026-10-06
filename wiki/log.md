# Log

Append-only record of operations. Entry format: `## [YYYY-MM-DD] <op> | <title>` where op ∈
ingest | query | lint | research | schema | filed. `grep "^## \[" wiki/log.md | tail -5` → last five.

## [2026-09-17] schema | Bootstrap the KB
Wrote `CLAUDE.md` (canonical schema; `AGENTS.md` now points to it), four page templates, `scripts/lint.py`,
directory layout `wiki/{sources,entities,concepts,syntheses}` + `overview.md` + `index.md` + `log.md`,
Obsidian attachment folder → `raw/assets/`.

## [2026-09-17] ingest | LLM Wiki: a pattern for building personal knowledge bases using LLMs
Raw: `raw/2026-09-17-llm-wiki-pattern.md` (pasted, author unverified). Created [[llm-wiki-idea-file]] (source page), [[llm-wiki-pattern]] (concept),
[[retrieval-augmented-generation]], [[memex]], [[obsidian]], [[qmd]], [[vannevar-bush]], [[overview]]. Updated [[index]].
Flagged: authorship unverified; index-first retrieval claim untested; primary source gap for Memex ("As We May Think").

## [2026-09-18] ingest | Two way notification Integration with FRM for CardWorks: Contract (Orcus)
Obsidian Web Clipper capture of a Zeta Confluence page, found in `raw/assets/Notification center/`;
moved verbatim to `raw/2026-09-18-two-way-notification-frm-cardworks.md` and the three Confluence
diagrams downloaded to `raw/assets/two-way-notification-frm-cardworks/`. Created
[[two-way-notification-frm-cardworks-contract]], [[two-way-notification]],
[[post-approval-risk-assessment]], [[orcus]], [[featurespace]], [[luminous]], [[atropos]], [[cardworks]].
Updated [[index]], [[overview]] (new domain: Zeta card payments & fraud risk). Flagged: tenant-id
600309 vs 600335 discrepancy; no timeout/correlation semantics for 2WAYNOTI.

## [2026-09-18] ingest | Luminos Notification (LNS / LNC) — PCMM capability matrix
Pasted TSV saved to `raw/2026-09-18-luminos-notification-pcmm.md`. Created [[luminos-notification-pcmm]], [[luminos-notification-system]], [[luminos-notification-center]], [[notification-product]], [[receiver-preference-order]], [[notification-channels-and-routes]], [[pcmm]], [[tachyon]], [[twilio]]. Renamed entity `luminous` → [[luminos]] (PCMM + user usage spell it Luminos; `aliases: [Luminous, …]` added) and repointed links in [[orcus]], [[atropos]], [[cardworks]], [[post-approval-risk-assessment]], [[two-way-notification]], the contract source page, [[overview]], [[index]]. Updated [[two-way-notification]] (2-way as a Luminos channel via Twilio Flow; delivery-channel open question). Flagged: LNS "event" vs LNC "template" naming; the SharePoint design doc "LN Including product and event level preferences" is still unread (empty clipping).

## [2026-09-18] ingest | Communication Preferences in CLM (Aries)
Clipping moved from `raw/assets/…` to `raw/2026-09-18-communication-preferences-in-clm-aries.md` (the sample pre-prod auth token was redacted before commit — Gitleaks hook). Created [[communication-preferences-in-clm-aries]], [[communication-preferences]], [[clm]], [[point-of-presence]], [[notification-message-types]]. Updated [[notification-channels-and-routes]] (providers-in-use table), [[luminos]] (Notifications Centre = Luminos; CLM overrides its consent copy), [[cardworks]] (Inbox + printed-letter channels; `ifiID` 600309), [[tachyon]] (API namespace), [[twilio]], [[overview]] (new domain row, thesis 3: consent vs delivery-preference layers), [[index]]. Flagged: consent × preference-order combination rule undocumented; `CALL` vs "Flow" channel naming.

## [2026-10-06] ingest | Claude 101 — course notes (Anthropic Academy)
User-dropped `raw/claude-101-notes.md` renamed verbatim to `raw/2026-10-06-claude-101-notes.md` with a frontmatter block added. Created [[claude-101-course-notes]], [[claude]], [[claude-code]], [[claude-cowork]], [[claude-in-chrome]], [[model-context-protocol]], [[prompting-fundamentals]], [[ai-fluency]], [[lightweight-evals]], [[claude-projects]], [[claude-skills]], [[claude-connectors]], [[claude-artifacts]], and the first synthesis [[choosing-a-claude-surface]]. Updated [[retrieval-augmented-generation]] (Projects' automatic RAG fallback), [[llm-wiki-pattern]] (knowledge/process/access parallel; KB runs on Claude Code), [[overview]] (new domain + thesis 4), [[index]].
Flagged: plan/beta gating is time-sensitive (confidence medium); AI Fluency and MCP known only second-hand.
