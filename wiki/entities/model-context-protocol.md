---
title: Model Context Protocol (MCP)
type: entity
tags: [ai-tools, llm-agents, integration, standard]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]"]
related: ["[[claude-connectors]]", "[[claude]]", "[[qmd]]"]
confidence: medium
status: seed
---

# Model Context Protocol (MCP)

An open standard for connecting AI models to external tools and data, pitched as "USB-C for
AI". It is the protocol underneath [[claude-connectors]].

## What we know

- Powers Claude's connectors, which let Claude both **read and act** in a tool (search,
  create, update) ([[claude-101-course-notes]]).
- Open standard: any tool can expose an MCP server, and a "custom connector" is the route when
  no listed connector exists ([[claude-101-course-notes]]).

## Relationships

- [[claude-connectors]]: the product feature built on it.
- [[qmd]] exposes an MCP server, which is how a search tool would plug into this KB's agent
  ([[llm-wiki-idea-file]]).

## Contradictions & open questions

- Only a one-line description so far. A primary source (the spec) would firm this up.

## Sources

- [[claude-101-course-notes]]
