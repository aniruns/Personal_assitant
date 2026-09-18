---
title: LLM Wiki pattern
type: concept
tags: [knowledge-management, llm-agents, meta]
created: 2026-09-17
updated: 2026-09-17
sources: ["[[2026-09-17-llm-wiki-pattern]]"]
related: ["[[retrieval-augmented-generation]]", "[[memex]]", "[[obsidian]]", "[[qmd]]"]
confidence: high
status: seed
---

# LLM Wiki pattern

A way of building a personal knowledge base in which an LLM agent incrementally **compiles**
raw sources into a persistent, interlinked markdown wiki and keeps it maintained, rather than
retrieving from raw documents at query time. This KB is an instance of the pattern; its schema
is `CLAUDE.md`.

## Explanation

**Problem it solves.** Two prior approaches fail in opposite ways ([[llm-wiki-idea-file|source]]):
[[retrieval-augmented-generation]] gives the LLM access to documents but nothing accumulates —
each question re-derives the synthesis from fragments. Human-maintained wikis accumulate, but
the maintenance burden (cross-references, updating summaries, flagging contradictions) grows
faster than the value, so people abandon them. The pattern keeps the accumulation and removes
the burden by making the LLM the maintainer.

**Three layers.**
1. *Raw sources* — curated, immutable, the source of truth.
2. *Wiki* — LLM-generated pages: per-source summaries, entity pages, concept pages, syntheses,
   an overview. Owned entirely by the LLM; the human reads it.
3. *Schema* — a config document (CLAUDE.md / AGENTS.md) defining structure, conventions, and
   workflows. Human and LLM co-evolve it.

**Three operations.**
- *Ingest*: read the source, discuss takeaways, write a source page, update every affected
  entity/concept page, update the index, append to the log. 10–15 pages per source is normal.
- *Query*: index → relevant pages → synthesized answer with citations, in the form that fits
  (page, table, slides, chart). Answers worth keeping are filed back as wiki pages so
  explorations compound like sources do.
- *Lint*: periodic health check for contradictions, stale claims, orphans, missing pages,
  missing links, and gaps a web search could fill.

**Navigation.** `index.md` is the content catalog (read first on every query; claimed to work
without embeddings up to ~100 sources / hundreds of pages). `log.md` is an append-only,
grep-able timeline. A local search tool like [[qmd]] is the upgrade path.

**Division of labor.** Human: curate sources, direct analysis, ask questions, think.
LLM: everything else. Working setup: agent on one side, [[obsidian]] on the other —
"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

**Lineage.** A realization of [[vannevar-bush]]'s [[memex]]: private, curated, with associative
trails between documents; the missing piece in 1945 was a maintainer.

## Design choices made in this KB

Recorded here so the reasoning survives (the pattern says to document your workflow in the schema):

- Four page types (`source`, `entity`, `concept`, `synthesis`) in separate folders, with YAML
  frontmatter for Dataview.
- Ingest one source at a time with a brief takeaway discussion by default; "batch" on request.
- Contradictions are never overwritten — kept in a `Contradictions & open questions` section.
- Mechanical lint is a script (`scripts/lint.py`); semantic lint is the agent's job.
- Web research is written to `raw/` first and then ingested, so every wiki claim has a raw record.

## Contradictions & open questions

- The "index-first works to ~100 sources" claim is untested here. Revisit when the wiki reaches
  ~30 sources: does reading the index still find the right pages?
- Cost of a 10–15 page rewrite per ingest at scale — when does that become a problem, and does
  the answer change with batch ingestion?
- Not addressed by the source: very large sources (books, long transcripts), page-merging
  policy, and privacy of personal data.

## Sources

- [[llm-wiki-idea-file|LLM Wiki (source page)]]
