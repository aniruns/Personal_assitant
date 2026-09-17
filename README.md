# Personal Assistant — LLM-Maintained Knowledge Base

This repo is a personal knowledge base built and maintained mostly by an LLM agent (Claude, or any coding agent that reads `AGENTS.md`). Instead of manipulating code, the agent mostly manipulates knowledge — stored as markdown files and images — following the workflow below.

## How it works

1. **Ingest (`raw/`)** — Source material goes here as-is: clipped web articles, papers, repo notes, datasets, screenshots. Use the [Obsidian Web Clipper](https://obsidian.md/clipper) (or a manual save) to drop articles in as markdown, and save any related images alongside them.
2. **Compile (`wiki/`)** — An LLM agent incrementally "compiles" a wiki from everything in `raw/`: summaries of each source, concepts extracted and written up as their own articles, and backlinks connecting related notes. `wiki/index.md` is the top-level table of contents.
3. **Browse (Obsidian)** — Open this repo as an Obsidian vault to read `raw/` and `wiki/` side by side, follow backlinks, and view rendered outputs.
4. **Ask (`outputs/`)** — Once the wiki has enough material, ask the agent complex questions against it. Answers get rendered as markdown, [Marp](https://marp.app/) slide decks, or images/plots — saved into `outputs/` — and interesting answers get filed back into `wiki/` to grow the knowledge base further.
5. **Maintain (`scripts/`)** — Periodic LLM-driven "health checks" over the wiki: find inconsistent or contradictory notes, fill in missing data (with web research), and suggest new articles or connections.

## Structure

```
raw/            Unprocessed source material (articles, papers, datasets, images)
wiki/           Compiled knowledge base — articles, summaries, backlinks
  index.md      Top-level index / table of contents
  concepts/     Individual concept/topic articles
outputs/        Generated outputs from Q&A sessions
  slides/       Marp-format slide decks
  images/       Generated charts/plots
  answers/      Markdown write-ups of research answers
scripts/        Ingest helpers and wiki health-check / linting scripts
templates/      Templates for new wiki articles
AGENTS.md       Instructions for the LLM agent maintaining this repo
```

## Getting started

1. Drop new source material into `raw/`.
2. Ask your agent to compile/update the wiki from `raw/`.
3. Open the repo in Obsidian to browse.
4. Ask the agent questions against the wiki; save interesting answers back into `wiki/`.
5. Occasionally ask the agent to run a health check (see `scripts/`).
