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
