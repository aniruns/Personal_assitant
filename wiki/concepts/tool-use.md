---
title: Tool use
type: concept
tags: [ai-tools, claude, api, llm-agents]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-platform-notes]]", "[[2026-10-06-claude-code-101-notes]]"]
related: ["[[agentic-loop]]", "[[claude-platform]]", "[[model-context-protocol]]", "[[claude-skills]]", "[[claude-managed-agents]]", "[[who-runs-the-agent-loop]]"]
confidence: medium
status: seed
---

# Tool use

A **tool** is a function you define and expose to Claude. **Claude decides when to call it;
your code actually runs it** ([[claude-platform-101-course-notes]]). Tools are what turn a
text generator into an agent: "tools are the backbone" of the [[agentic-loop]]
([[claude-code-101-course-notes]]).

## Explanation

**A tool definition has three parts** ([[claude-platform-101-course-notes]]):
- `name`
- `description` — Claude reads this to decide whether to use the tool
- `input_schema` — a JSON schema for the inputs

> The #1 reason agents misfire: vague tool descriptions. Be specific.

**Several tools:** Claude reads the descriptions and picks one, sometimes calling more than one
in a single turn. Your code dispatches on the tool name; adding a tool means adding it to the
array and adding a `case` ([[claude-platform-101-course-notes]]).

**Tool runner** (SDK shortcut for TypeScript, Python and Ruby): pass your **real functions**,
and it builds the schemas from your types and docs and runs the whole loop.
`runner.untilDone()` returns the final answer. No `while` loop, no `stop_reason` switch, no
schemas written twice ([[claude-platform-101-course-notes]]).

**Who runs the tool** ([[claude-platform-101-course-notes]]):

| Kind | Examples | Runs where | Loop needed? |
|---|---|---|---|
| **Your tools** | anything you define | your code | yes (or the tool runner) |
| **Server tools** | web search (with citations), web fetch, code execution (Python sandbox) | Anthropic | **no** — result arrives in the same response as `server_tool_use` + result blocks |
| **Client tools** | memory, bash (persistent shell) | your environment; SDK ships schema + runner | yes |
| **MCP tools** | a provider's server | the provider | discovered by Claude, no schemas from you ([[model-context-protocol]]) |

## How it connects

- **Tools vs skills vs MCP:** "Tools = your stuff · Skills = your processes · MCP = everyone
  else's stuff". A tool says *what* Claude can do; a [[claude-skills|skill]] says *how* you want
  it done ([[claude-platform-101-course-notes]]).
- The tool description plays the same role as a skill's or [[subagents|subagent]]'s
  description: it is the only thing Claude sees when deciding whether to use it
  ([[claude-code-101-course-notes]]). Assessment: writing descriptions is the core craft across
  all three.
- How much of the tool loop you run yourself: [[who-runs-the-agent-loop]].
- Every tool definition costs context on each call ([[context-management]]).

## Contradictions & open questions

- (none yet)

## Sources

- [[claude-platform-101-course-notes]]
- [[claude-code-101-course-notes]]
