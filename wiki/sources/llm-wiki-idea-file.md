---
title: "LLM Wiki: a pattern for building personal knowledge bases using LLMs"
type: source
tags: [knowledge-management, llm-agents, meta]
created: 2026-09-17
updated: 2026-09-17
sources: ["[[2026-09-17-llm-wiki-pattern]]"]
related: ["[[llm-wiki-pattern]]", "[[retrieval-augmented-generation]]", "[[obsidian]]", "[[memex]]"]
confidence: high
status: seed
author: unknown (attribution unverified — see Assessment)
published: unknown
url: n/a
source_type: article
---

# LLM Wiki: a pattern for building personal knowledge bases using LLMs

An "idea file" meant to be pasted into a coding agent (Claude Code, Codex, OpenCode) so the agent
builds a personal knowledge base around it. It argues that instead of retrieving chunks from raw
documents at query time ([[retrieval-augmented-generation]]), an LLM should incrementally
**compile and maintain a persistent, interlinked markdown wiki** that sits between the human and
the raw sources. This is the founding document of this KB: the schema in `CLAUDE.md` is a direct
implementation of it.

## Key claims

- RAG re-derives knowledge from scratch on every question; nothing accumulates. NotebookLM,
  ChatGPT file uploads, and most RAG systems work this way.
- A maintained wiki is a *compounding artifact*: cross-references already exist, contradictions
  are already flagged, the synthesis already reflects everything read.
- The human never (or rarely) writes the wiki. Human = sourcing, exploration, questions;
  LLM = summarizing, cross-referencing, filing, bookkeeping.
- Three layers: immutable **raw sources**, the LLM-owned **wiki**, and a co-evolved **schema**
  file (CLAUDE.md / AGENTS.md) that makes the agent "a disciplined wiki maintainer rather than
  a generic chatbot".
- Three operations: **ingest** (a source may touch 10–15 pages), **query** (answers with
  citations, in whatever form fits, and good answers get *filed back* into the wiki), and
  **lint** (contradictions, stale claims, orphans, missing pages, missing links, gaps).
- Two navigation files with distinct roles: `index.md` (content catalog, read first on every
  query; sufficient up to ~100 sources / hundreds of pages, no embeddings needed) and `log.md`
  (append-only, grep-able chronological record).
- Why it works: wikis fail because maintenance burden outgrows value; LLM maintenance cost is
  near zero, so the wiki stays maintained.
- The idea descends from [[vannevar-bush]]'s [[memex]] (1945); Bush's unsolved problem was who
  does the maintenance, and the LLM is the answer.
- Applies beyond research: personal self-tracking, book companion wikis (cf. Tolkien Gateway),
  team wikis fed by Slack/meetings, competitive analysis, trip planning, course notes.

## Notable quotes

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

> The tedious part of maintaining a knowledge base is not the reading or the thinking — it's
> the bookkeeping.

> The human's job is to curate sources, direct the analysis, ask good questions, and think about
> what it all means. The LLM's job is everything else.

## Tooling mentioned

[[obsidian]] (as the browsing IDE, plus Web Clipper, graph view, Dataview, Marp plugin, attachment
folder + "Download attachments" hotkey for local images), [[qmd]] (local hybrid BM25/vector
search over markdown, CLI + MCP) as an optional search layer once the index outgrows itself,
Marp for slides, matplotlib for charts, git for history.

## Assessment

- Strong, practical, and the design choices are mostly justified by failure modes of the
  alternatives (RAG → no accumulation; human wikis → abandoned). The index-first retrieval claim
  ("works surprisingly well at ~100 sources") is asserted from experience, not measured — worth
  testing as this KB grows.
- Deliberately underspecified: it says "your agent will build out the specifics". The specifics
  here live in `CLAUDE.md`.
- Gaps the source doesn't address: how to handle *very* large sources (books, long transcripts),
  how to keep page count from exploding, when to merge pages, privacy of personal data, and
  the cost of a 15-page rewrite per ingest at scale.
- **Attribution:** pasted without author or URL. The style and the references (Claude Code /
  Codex, qmd, Memex) are consistent with a widely-shared 2026 idea file commonly attributed to
  Andrej Karpathy, but that is unverified here. Treat authorship as unknown until a URL is
  added to the raw file.

## Wiki changes

- Created: [[llm-wiki-pattern]], [[retrieval-augmented-generation]], [[memex]], [[obsidian]],
  [[qmd]], [[vannevar-bush]], [[overview]]
- Updated: [[index]], [[log]]

## Raw

[[2026-09-17-llm-wiki-pattern]]
