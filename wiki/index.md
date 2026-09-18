# Index

Catalog of every page in the wiki, by category. The agent reads this first on every query and
updates it on every ingest or filing. See [[overview]] for the big picture and [[log]] for history.

## Sources

- [[llm-wiki-idea-file|LLM Wiki: a pattern for building personal knowledge bases]] — the idea file this KB implements: compile a wiki, don't RAG; three layers, three ops, index + log. _Ingested 2026-09-17_
- [[two-way-notification-frm-cardworks-contract|Two way notification Integration with FRM for CardWorks: Contract]] — Zeta Confluence contract: Orcus ↔ Featurespace post-approval flow and the 2WAYNOTI action via Luminous. _Ingested 2026-09-18_

## Concepts

- [[llm-wiki-pattern]] — LLM compiles and maintains a persistent wiki from immutable raw sources; the design behind this KB. _Updated 2026-09-17_
- [[retrieval-augmented-generation]] — retrieve-then-generate over raw docs; the stateless foil to the wiki pattern. _Updated 2026-09-17_
- [[memex]] — Bush's 1945 curated knowledge store with associative trails; ancestor of the wiki pattern. _Updated 2026-09-17_
- [[post-approval-risk-assessment]] — CardRT (pre) + CardNRT (post) fraud scoring, FOLLOW UP tag, and the five queue-tag actions. _Updated 2026-09-18_
- [[two-way-notification]] — 2WAYNOTI: ask the customer to approve/deny a txn via Luminous; block + FS feedback on the answer. _Updated 2026-09-18_

## Entities

- [[obsidian]] — markdown vault app used as the browsing surface; Web Clipper, graph view, Dataview, attachment folder tips. _Updated 2026-09-17_
- [[qmd]] — local hybrid BM25/vector search for markdown with CLI + MCP; the upgrade path when the index isn't enough. _Updated 2026-09-17_
- [[vannevar-bush]] — proposed the Memex (1945). _Updated 2026-09-17_
- [[orcus]] — Zeta card-transaction system; the Interceptor calls Featurespace and runs queue-tag handlers. _Updated 2026-09-18_
- [[featurespace]] — FRM engine (ARIC): CardRT/CardNRT calls, FOLLOW UP + queue tags, receives transactionReturn feedback. _Updated 2026-09-18_
- [[luminous]] — workflow/notification service; `CWFRMWorkflow` initiate API and `notificationWorkflowResponse` topic. _Updated 2026-09-18_
- [[atropos]] — Zeta pub/sub: `orcus-transactions` and `notificationWorkflowResponse` topics, tenant-filtered subscriptions. _Updated 2026-09-18_
- [[cardworks]] — tenant the FRM contract is scoped to; tenant-id discrepancy (600309 vs 600335) flagged. _Updated 2026-09-18_

## Syntheses

_(none yet — filed answers, comparisons, and analyses go here)_
