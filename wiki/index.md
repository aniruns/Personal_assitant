# Index

Catalog of every page in the wiki, by category. The agent reads this first on every query and
updates it on every ingest or filing. See [[overview]] for the big picture and [[log]] for history.

## Sources

- [[llm-wiki-idea-file|LLM Wiki: a pattern for building personal knowledge bases]] — the idea file this KB implements: compile a wiki, don't RAG; three layers, three ops, index + log. _Ingested 2026-09-17_
- [[two-way-notification-frm-cardworks-contract|Two way notification Integration with FRM for CardWorks: Contract]] — Zeta Confluence contract: Orcus ↔ Featurespace post-approval flow and the 2WAYNOTI action via Luminos. _Ingested 2026-09-18_
- [[luminos-notification-pcmm|Luminos Notification (LNS / LNC) — PCMM]] — capability matrix: two Beta modules, four capabilities each, 29 prioritised features incl. product/event/receiver preference order. _Ingested 2026-09-18_
- [[communication-preferences-in-clm-aries|Communication Preferences in CLM (Aries)]] — eight message types, channel/provider table, per-address consent tags in CLM, update API, CLM→Luminos sync. _Ingested 2026-09-18_
- [[claude-101-course-notes|Claude 101 — course notes (Anthropic Academy)]] — the user's notes on 12 lessons: prompting, 4Ds, evals, projects/skills/connectors, artifacts, research, surfaces. _Ingested 2026-10-06_
- [[claude-code-101-course-notes|Claude Code 101 — course notes]] — the user's notes on 11 lessons: agentic loop, permission modes, explore→plan→code→commit, context, CLAUDE.md, subagents, MCP, hooks. _Ingested 2026-10-06_
- [[ai-fluency-vocabulary-cheat-sheet|AI Fluency: Key Terminology Cheat Sheet]] — Anthropic / Dakan & Feller glossary: 4Ds × 3 sub-competencies, 3 interaction modes, ~30 technical + prompting terms. _Ingested 2026-10-06_

## Concepts

- [[llm-wiki-pattern]] — LLM compiles and maintains a persistent wiki from immutable raw sources; the design behind this KB. _Updated 2026-10-06_
- [[retrieval-augmented-generation]] — retrieve-then-generate over raw docs; the stateless foil to the wiki pattern; Claude Projects use it as a scaling fallback. _Updated 2026-10-06_
- [[memex]] — Bush's 1945 curated knowledge store with associative trails; ancestor of the wiki pattern. _Updated 2026-09-17_
- [[post-approval-risk-assessment]] — CardRT (pre) + CardNRT (post) fraud scoring, FOLLOW UP tag, and the five queue-tag actions. _Updated 2026-09-18_
- [[two-way-notification]] — 2WAYNOTI: ask the customer to approve/deny a txn via Luminos; block + FS feedback on the answer; delivery channel still open. _Updated 2026-09-18_
- [[receiver-preference-order]] — Luminos: which contact vector to try first, set at product / event (template) / individual-receiver level; the "product and event level preference" feature. _Updated 2026-09-18_
- [[communication-preferences]] — CLM consent model: per-address `COMMUNICATION_PREFERENCE` tags by message type with `disallowedChannels`; `isCommunicationAllowed` gate; CLM overrides Luminos. _Updated 2026-09-18_
- [[notification-message-types]] — the eight types (Critical, Directed, OTP, Authentication, Promotional, Announcement, Transactional, Default); OTP bypasses opt-out. _Updated 2026-09-18_
- [[notification-channels-and-routes]] — channels = modes, routes = delivery paths, providers = vendors; the channel/provider table across both sources. _Updated 2026-09-18_
- [[notification-product]] — Luminos's top-level config unit: receivers, vectors, default preference, templates, languages, Tachyon mapping. _Updated 2026-09-18_
- [[point-of-presence]] — CLM's labelled group of an account holder's addresses; where preference tags hang. _Updated 2026-09-18_
- [[pcmm]] — Zeta's Module → Capability → Feature matrix format with maturity and P1–P3 priority. _Updated 2026-09-18_
- [[prompting-fundamentals]] — stage → task → rules, the problem→fix table, iterate, ask for the deliverable. _Updated 2026-10-06_
- [[ai-fluency]] — Dakan & Feller's 4Ds, each with 3 sub-competencies; Description and Discernment share Product/Process/Performance. _Updated 2026-10-06_
- [[human-ai-interaction-modes]] — Automation / Augmentation / Agency: who decides the steps; maps onto Chat vs Cowork/Code. _Updated 2026-10-06_
- [[hallucination]] — confident, plausible, wrong; countered by grounding (RAG, search), asking for sources, Product Discernment. _Updated 2026-10-06_
- [[lightweight-evals]] — 5–10 past examples → prompt → compare → adjust; no tooling. _Updated 2026-10-06_
- [[claude-projects]] — workspace = knowledge + instructions; automatic RAG near the context limit (~10x); name files well. _Updated 2026-10-06_
- [[claude-skills]] — reusable process packages Claude loads itself; "projects = what, skills = how". _Updated 2026-10-06_
- [[claude-connectors]] — MCP-based read/act access to your tools; sees only what you can see. _Updated 2026-10-06_
- [[claude-artifacts]] — standalone outputs (Design / Slides / Docs + dashboards etc.); editing, sharing, exports. _Updated 2026-10-06_
- [[agentic-loop]] — agent = LLM in a loop with tools: gather context → act → verify → repeat; human can steer anytime. _Updated 2026-10-06_
- [[explore-plan-code-commit]] — Claude Code's core workflow: Plan mode first (cheapest course-correction), success criteria + tests, subagent review, commit. _Updated 2026-10-06_
- [[context-management]] — context = finite working memory; auto-compaction, `/compact` vs `/clear` vs `/context`; specific prompts are cheaper. _Updated 2026-10-06_
- [[claude-md]] — CLAUDE.md project memory: read every session, project vs user level, start without one then `/init`; advisory, not enforced. _Updated 2026-10-06_
- [[subagents]] — isolated-context delegates that return only a summary; YAML-frontmatter md files; read-only reviewers. _Updated 2026-10-06_
- [[claude-code-hooks]] — deterministic lifecycle commands (PreToolUse/PostToolUse/…); exit 2 blocks and feeds stderr back. _Updated 2026-10-06_

## Entities

- [[obsidian]] — markdown vault app used as the browsing surface; Web Clipper, graph view, Dataview, attachment folder tips. _Updated 2026-09-17_
- [[qmd]] — local hybrid BM25/vector search for markdown with CLI + MCP; the upgrade path when the index isn't enough. _Updated 2026-09-17_
- [[vannevar-bush]] — proposed the Memex (1945). _Updated 2026-09-17_
- [[orcus]] — Zeta card-transaction system; the Interceptor calls Featurespace and runs queue-tag handlers. _Updated 2026-09-18_
- [[featurespace]] — FRM engine (ARIC): CardRT/CardNRT calls, FOLLOW UP + queue tags, receives transactionReturn feedback. _Updated 2026-09-18_
- [[luminos]] — Zeta's notification platform (a.k.a. Luminous / Notifications Centre): LNS + LNC modules, `CWFRMWorkflow` API, consumer of CLM consent. _Updated 2026-09-18_
- [[luminos-notification-system]] — LNS: the engine module — product/receiver/channel features, per-vendor priorities, send + delivery tracking. _Updated 2026-09-18_
- [[luminos-notification-center]] — LNC: the console module — templates, route plans, preference overrides, Tachyon bundle mapping. _Updated 2026-09-18_
- [[clm]] — Aries-space customer lifecycle system; system of record for communication consent; `communicationPreferences/update` API. _Updated 2026-09-18_
- [[tachyon]] — Zeta core platform name: the auth switch, the product catalogue notification products map to, and the `mars/tachyon/v4` API namespace. _Updated 2026-09-18_
- [[twilio]] — P1 vendor for SMS, WhatsApp and two-way (Flow) channels; already used for SMS and IVR. _Updated 2026-09-18_
- [[atropos]] — Zeta pub/sub: `orcus-transactions` and `notificationWorkflowResponse` topics, tenant-filtered subscriptions. _Updated 2026-09-18_
- [[cardworks]] — tenant the FRM contract is scoped to; Inbox + printed-letter channels; tenant-id discrepancy (600309 vs 600335) flagged. _Updated 2026-09-18_
- [[claude]] — Anthropic's assistant: Constitutional AI, steerable, 200K/1M context; hub for all surfaces and features. _Updated 2026-10-06_
- [[claude-code]] — agentic coding tool: permission modes, install + surfaces (terminal first, web = GitHub only), commands, PR flow; runs this KB. _Updated 2026-10-06_
- [[claude-cowork]] — desktop tab for handing off multi-step work: plans, saves files back, scheduled tasks, plugins. _Updated 2026-10-06_
- [[claude-in-chrome]] — browser sidebar that sees and acts on pages; not on Free; asks before purchases. _Updated 2026-10-06_
- [[model-context-protocol]] — MCP, the open "USB-C for AI" standard; in Claude Code: HTTP/stdio, local/user/project scopes, idle context cost, tool search. _Updated 2026-10-06_

## Syntheses

- [[choosing-a-claude-surface]] — which Claude tool for which job: by shape of work, kind of question, and where you're working. _Updated 2026-10-06_
- [[claude-code-extension-points]] — prompt vs CLAUDE.md vs skill vs subagent vs MCP vs hook, ranked by reliability and idle context cost. _Updated 2026-10-06_
- [[ai-fluency-glossary]] — **study sheet**: every AI Fluency term, confused pairs, and a folded-answer self-test. _Updated 2026-10-06_
