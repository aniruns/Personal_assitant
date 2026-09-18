---
title: Retrieval-Augmented Generation (RAG)
type: concept
tags: [llm, information-retrieval]
created: 2026-09-17
updated: 2026-09-17
sources: ["[[2026-09-17-llm-wiki-pattern]]"]
related: ["[[llm-wiki-pattern]]", "[[qmd]]"]
confidence: medium
status: seed
---

# Retrieval-Augmented Generation (RAG)

The dominant way LLMs are combined with document collections: index the documents, retrieve the
chunks most relevant to a query at answer time, and generate a response from them. In this KB it
matters mainly as the **foil** to the [[llm-wiki-pattern]].

## Explanation

The LLM Wiki source characterizes RAG as "rediscovering knowledge from scratch on every
question" — retrieval finds fragments, but no synthesis is stored, so a question that needs five
documents pieced together pays that cost every time. It names NotebookLM, ChatGPT file uploads,
and "most RAG systems" as examples ([[llm-wiki-idea-file|source]]).

**Assessment:** this is a fair description of the *stateless* use of RAG, not a refutation of
retrieval as a technique. The wiki pattern still needs retrieval — it just retrieves over
compiled pages via the index, and later via a search tool such as [[qmd]] (which is itself
hybrid BM25/vector search, i.e. RAG-style infrastructure). The real contrast is *compile once
and maintain* vs. *re-derive per query*, not "search vs. no search".

## How it connects

- [[llm-wiki-pattern]] — the alternative this KB is built on.
- [[qmd]] — where RAG-style retrieval re-enters the wiki pattern once the index outgrows itself.

## Contradictions & open questions

- Only one source so far, and it's an advocate for the alternative. A neutral or pro-RAG source
  would balance this page.

## Sources

- [[llm-wiki-idea-file|LLM Wiki (source page)]]
