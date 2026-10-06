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

## [2026-10-06] ingest | Claude Code 101 — course notes
User-dropped `raw/claude-code-101-notes.md` renamed verbatim to `raw/2026-10-06-claude-code-101-notes.md` with a frontmatter block added. Created [[claude-code-101-course-notes]], [[agentic-loop]], [[explore-plan-code-commit]], [[context-management]], [[claude-md]], [[subagents]], [[claude-code-hooks]], and synthesis [[claude-code-extension-points]]. Rewrote [[claude-code]] (seed → growing). Updated [[claude-skills]], [[model-context-protocol]] (→ growing), [[claude-connectors]], [[claude-in-chrome]], [[claude]], [[choosing-a-claude-surface]], [[llm-wiki-pattern]], [[overview]] (thesis 5), [[index]].
Flagged: no contradictions (desktop mode labels differ only in naming); "Your first prompt" and "Skills" lessons video-only; course platform inferred, not stated; thresholds time-sensitive.

## [2026-10-06] ingest | AI Fluency: Key Terminology Cheat Sheet
User-dropped `raw/AI_Fluency_vocabulary_cheat_sheet.pdf` renamed (unchanged) to `raw/2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf`. Created [[ai-fluency-vocabulary-cheat-sheet]], [[ai-fluency-glossary]] (study sheet with folded self-test — user wants to train on the terms later), [[human-ai-interaction-modes]], [[hallucination]]. Rewrote [[ai-fluency]] (12 sub-competencies, authors Rick Dakan & Joseph Feller; → growing, confidence high). Updated [[prompting-fundamentals]] (technique vocabulary), [[lightweight-evals]], [[retrieval-augmented-generation]] (grounding view), [[context-management]], [[claude]], [[choosing-a-claude-surface]] (interaction modes), [[overview]], [[index]].
Flagged: no contradictions; resolves the "AI Fluency known only second-hand" gap; 4Ds × modes relationship unstated.

## [2026-10-06] schema | lint.py resolves non-markdown raw sources
First PDF raw source. `scripts/lint.py` now resolves extension-bearing links to any non-`.md` file in `raw/` (previously only `raw/assets/`). PDF sources are cited with their extension, e.g. `[[2026-10-06-ai-fluency-vocabulary-cheat-sheet.pdf]]`, as Obsidian requires.

## [2026-10-06] ingest | Claude Platform 101 — course notes
User's `~/Downloads/Claude-platform-notes.md` saved verbatim to `raw/2026-10-06-claude-platform-notes.md` with a frontmatter block added. Created [[claude-platform-101-course-notes]], [[claude-platform]], [[claude-managed-agents]], [[tool-use]], [[extended-thinking]], [[model-selection]], and synthesis [[who-runs-the-agent-loop]]. Updated [[agentic-loop]] (→ growing), [[context-management]] (retitled; API patterns; → growing), [[claude-skills]] (→ growing), [[model-context-protocol]], [[claude]] (→ growing), [[claude-code]], [[lightweight-evals]], [[hallucination]], [[choosing-a-claude-surface]], [[claude-code-extension-points]], [[overview]] (thesis 6), [[index]].
Flagged: sample-size tension (5–10 vs 20–30 examples), assessed as different purposes; model names / beta flags time-sensitive; prompt caching and the "controls" layer uncovered.
