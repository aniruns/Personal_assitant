---
title: qmd
type: entity
tags: [tools, search]
created: 2026-09-17
updated: 2026-09-17
sources: ["[[2026-09-17-llm-wiki-pattern]]"]
related: ["[[llm-wiki-pattern]]", "[[retrieval-augmented-generation]]", "[[obsidian]]"]
confidence: medium
status: seed
---

# qmd

A local search engine for markdown files, recommended by the [[llm-wiki-pattern]] as the
upgrade path once `index.md` stops being enough for retrieval.

## What we know

- Hybrid BM25 + vector search with LLM re-ranking, all on-device ([[llm-wiki-idea-file|source]]).
- Exposes both a **CLI** (so an agent can shell out to it) and an **MCP server** (so an agent can
  use it as a native tool).
- Positioned as optional: "at small scale the index file is enough". The source also suggests
  vibe-coding a naive search script as an alternative.

**Assessment:** the KB has not installed or evaluated qmd. Trigger for revisiting: when reading
`index.md` no longer reliably surfaces the right pages (estimate: ~30–100 sources).

## Relationships

- [[llm-wiki-pattern]] — optional tooling layer.
- [[retrieval-augmented-generation]] — qmd is RAG-style retrieval applied to compiled wiki pages.
- [[obsidian]] — complementary search surfaces (human vs. agent).

## Contradictions & open questions

- Author, license, install method, and URL are not in the source. Research when needed.

## Sources

- [[llm-wiki-idea-file|LLM Wiki (source page)]]
