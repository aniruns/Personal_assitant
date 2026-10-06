---
title: Model Context Protocol (MCP)
type: entity
tags: [ai-tools, llm-agents, integration, standard]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-101-notes]]", "[[2026-10-06-claude-code-101-notes]]", "[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude-connectors]]", "[[claude]]", "[[qmd]]", "[[claude-code]]", "[[context-management]]", "[[claude-code-extension-points]]", "[[tool-use]]"]
confidence: medium
status: growing
---

# Model Context Protocol (MCP)

An open standard for connecting AI models to external tools and data, pitched as "USB-C for
AI". It is the protocol underneath [[claude-connectors]].

## What we know

- Powers Claude's connectors, which let Claude both **read and act** in a tool (search,
  create, update) ([[claude-101-course-notes]]).
- Open standard: any tool can expose an MCP server, and a "custom connector" is the route when
  no listed connector exists ([[claude-101-course-notes]]).

- **Why it exists:** if you write your own Asana, Slack and Google integrations, *you* maintain
  them every time their APIs change. With MCP the **service provider** publishes and maintains
  the server (tools, schemas, auth); when their API changes, they update it and you change
  nothing. "Tools = your stuff · Skills = your processes · MCP = everyone else's stuff"
  ([[claude-platform-101-course-notes]]). Server directory: modelcontextprotocol.io.

### On the API

- Beta, needs a beta header. `mcp_servers` declares the connection (type, URL, name, optional
  auth token); an `mcp_toolset` entry in `tools` says which of the server's tools Claude may use
  (all by default). Claude **discovers the tools itself**, so you write no schemas
  ([[claude-platform-101-course-notes]]).
- **Scoping down**, e.g. read-only Slack: `default_config: {"enabled": False}`, then enable only
  `search_messages` and `list_channels`. This also saves context
  ([[claude-platform-101-course-notes]], [[context-management]]).

### In Claude Code

- **Examples:** a Linear MCP server for your issues; Context7 for up-to-date docs; databases,
  production apps, repos ([[claude-code-101-course-notes]]).
- **Adding:** `claude mcp add`. Transport is **HTTP** (remote, hosted by the provider) or
  **stdio** (a local process on your machine). `/mcp` lists servers, shows their status and
  lets you disable them ([[claude-code-101-course-notes]]).
- **Scopes** ([[claude-code-101-course-notes]]):
  - *local:* this project, just you
  - *user:* all your projects
  - *project:* `.mcp.json` committed to git, so the whole team gets the same servers
- **Context cost:** tool definitions sit in context **even when unused**. If a CLI equivalent
  exists (gh, aws), use it instead because it is cheaper, or wrap it in a skill. When MCP tools
  exceed ~10% of context, Claude Code switches to **tool-search mode**, which finds tools on
  demand but is less reliable ([[claude-code-101-course-notes]], [[context-management]]).

## Relationships

- [[claude-connectors]]: the product feature built on it.
- [[claude-code]]: configured per scope; weighed against CLIs, skills and hooks in
  [[claude-code-extension-points]].
- [[qmd]] exposes an MCP server, which is how a search tool would plug into this KB's agent
  ([[llm-wiki-idea-file]]).

## Contradictions & open questions

- Still no primary source: everything here is from course notes (now three). The spec would
  firm up transports and the protocol model.
- Can Claude Code scope a server to a subset of tools the way the API's `mcp_toolset` can? That
  would ease its idle context cost. Not covered.

## Sources

- [[claude-101-course-notes]]
- [[claude-code-101-course-notes]]
- [[claude-platform-101-course-notes]]
