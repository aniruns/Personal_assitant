---
title: Claude Platform (API)
type: entity
tags: [ai-tools, claude, api, anthropic]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude]]", "[[tool-use]]", "[[agentic-loop]]", "[[model-selection]]", "[[claude-managed-agents]]", "[[context-management]]", "[[who-runs-the-agent-loop]]"]
confidence: medium
status: seed
---

# Claude Platform (API)

Anthropic's infrastructure for using [[claude]] **from code** instead of a chat window
([[claude-platform-101-course-notes]]). It is the layer underneath the products: to build
Claude into your own app, you work here.

## What we know

- **What you get:** a REST API usable from any language, SDKs for several languages
  (`@anthropic-ai/sdk`, `anthropic` for Python), CLIs, and the **Console**
  (platform.claude.com) for API keys, usage, managed agents and testing prompts. You need to buy
  credits before calling it ([[claude-platform-101-course-notes]]).
- **Three layers** ([[claude-platform-101-course-notes]]):

  | Layer | What | Examples |
  |---|---|---|
  | Primitives | building blocks you call from code | Messages API, [[tool-use]], files, web search, code execution, [[model-context-protocol|MCP]], [[claude-skills|skills]] |
  | Infrastructure | what you need to scale past a prototype | [[claude-managed-agents]], retries, queues, observability |
  | Controls | running it in production | dashboards, evals |

  Shorthand: *build with primitives, scale on infrastructure, run with control.*
- **The goal is integration, not a chatbot:** e.g. a "Draft reply" button inside a help desk
  app ([[claude-platform-101-course-notes]]).
- **One call** = `messages.create(model, max_tokens, messages, system?)`. `messages` is a list
  of `user` / `assistant` turns; `system` sets persona and rules
  ([[claude-platform-101-course-notes]]).
- **The response is a list of blocks**, not a string. Blocks can be text, tool calls or
  thinking, so loop over them and check `block.type`. `response.usage` reports input and
  output tokens, which is what you are billed on ([[claude-platform-101-course-notes]]).
- **Keys go in `.env.local`**, never in source code, so they don't leak to GitHub
  ([[claude-platform-101-course-notes]]).
- Several features (skills, MCP connections) are **beta** and need a beta header
  ([[claude-platform-101-course-notes]]).

## Relationships

- Choosing which model handles a call: [[model-selection]]. Making it reason first:
  [[extended-thinking]].
- Adding actions: [[tool-use]]; looping over them: [[agentic-loop]]; handing the loop to
  Anthropic: [[claude-managed-agents]]. The spectrum: [[who-runs-the-agent-loop]].
- Keeping calls affordable: [[context-management]].
- [[claude-code]] writes most of the platform code for you through its built-in Claude API
  skill.

## Contradictions & open questions

- Model names, beta flags and defaults are as of the course date. Check the docs before use.
- The "controls" layer (dashboards, evals) is named but not covered in the notes.

## Sources

- [[claude-platform-101-course-notes]]
