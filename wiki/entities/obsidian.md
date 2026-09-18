---
title: Obsidian
type: entity
tags: [tools, knowledge-management]
created: 2026-09-17
updated: 2026-09-17
sources: ["[[2026-09-17-llm-wiki-pattern]]"]
related: ["[[llm-wiki-pattern]]", "[[qmd]]"]
confidence: high
status: seed
---

# Obsidian

A local-first markdown note-taking app with wikilinks, backlinks, and a graph view. In this KB
it is the **browsing/reading surface** — the repo is opened as an Obsidian vault while the agent
edits it ("Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase").

## What we know

From the [[llm-wiki-idea-file|LLM Wiki source]]:

- **Web Clipper** — browser extension that converts web articles to markdown; the main way to
  get sources into `raw/`.
- **Local images** — set *Settings → Files and links → Attachment folder path* to a fixed
  directory (this vault uses `raw/assets/`, already configured in `.obsidian/app.json`), then
  bind *Download attachments for current file* to a hotkey. Images then live on disk so the
  agent can view them, instead of depending on URLs that may break.
- **Graph view** — best way to see the wiki's shape: hubs, clusters, orphans.
- **Dataview plugin** — queries over YAML frontmatter; the reason every wiki page here has
  `tags / created / updated / sources / status` fields.
- **Marp plugin** — renders markdown slide decks generated from wiki content.
- LLMs can't read markdown with inline images in one pass; the workaround is text first, then
  view the referenced images separately.

## Relationships

- [[llm-wiki-pattern]] — Obsidian is the recommended human-side interface for the pattern.
- [[qmd]] — complementary: Obsidian's search is for the human, qmd's is for the agent.

## Contradictions & open questions

- (none yet)

## Sources

- [[llm-wiki-idea-file|LLM Wiki (source page)]]
