# Personal Assistant — LLM-Maintained Knowledge Base

This repo is a personal knowledge base built and maintained mostly by an LLM agent (Claude Code, or any coding agent that reads `CLAUDE.md` / `AGENTS.md`). Instead of manipulating code, the agent mostly manipulates knowledge — stored as markdown files and images — following the workflow below.

## How it works

1. **Ingest (`raw/`)** — Source material goes here as-is: clipped web articles, papers, repo notes, datasets, screenshots. Use the [Obsidian Web Clipper](https://obsidian.md/clipper) (or a manual save) to drop articles in as markdown, and save any related images alongside them.
2. **Compile (`wiki/`)** — An LLM agent incrementally "compiles" a wiki from everything in `raw/`: summaries of each source, concepts extracted and written up as their own articles, and backlinks connecting related notes. `wiki/index.md` is the top-level table of contents.
3. **Browse (Obsidian)** — Open this repo as an Obsidian vault to read `raw/` and `wiki/` side by side, follow backlinks, and view rendered outputs.
4. **Ask (`outputs/`)** — Once the wiki has enough material, ask the agent complex questions against it. Answers get rendered as markdown, [Marp](https://marp.app/) slide decks, or images/plots — saved into `outputs/` — and interesting answers get filed back into `wiki/` to grow the knowledge base further.
5. **Maintain** — Periodic LLM-driven "health checks" (`lint`): `scripts/lint.py` for the mechanical layer (broken links, orphans, index drift), the agent for the semantic layer (contradictions, stale claims, gaps to research).

## Structure

```
CLAUDE.md       The schema — how the agent maintains this KB (AGENTS.md points here)
raw/            Immutable sources: YYYY-MM-DD-slug.md; images in raw/assets/
wiki/
  index.md      Catalog of every page, by category (agent reads this first)
  log.md        Append-only timeline of ingests / queries / lints
  overview.md   Living map: domains, current theses, open questions
  sources/      One summary page per raw source
  entities/     People, tools, orgs, products, projects
  concepts/     Ideas, techniques, patterns
  syntheses/    Comparisons, analyses, filed answers
outputs/        Rendered answers, Marp slides, charts (transient unless filed)
templates/      Page skeletons per type
scripts/        lint.py — mechanical health checks
```

## Getting started

1. Drop new source material into `raw/`.
2. Ask your agent to compile/update the wiki from `raw/`.
3. Open the repo in Obsidian to browse.
4. Ask the agent questions against the wiki; save interesting answers back into `wiki/`.
5. Occasionally ask the agent to run a health check (see `scripts/`).
