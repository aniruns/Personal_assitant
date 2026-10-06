---
title: Where an instruction belongs in Claude Code
type: synthesis
tags: [ai-tools, claude, coding, decision-guide]
created: 2026-10-06
updated: 2026-10-06
sources: ["[[2026-10-06-claude-code-101-notes]]", "[[2026-10-06-claude-101-notes]]", "[[2026-10-06-claude-platform-notes]]"]
related: ["[[claude-code]]", "[[claude-md]]", "[[claude-skills]]", "[[subagents]]", "[[model-context-protocol]]", "[[claude-code-hooks]]", "[[context-management]]", "[[choosing-a-claude-surface]]"]
confidence: medium
status: seed
question: "Given something I want Claude Code to know or do, which mechanism should hold it?"
---

# Where an instruction belongs in Claude Code

[[claude-code]] has six places to put behaviour: the prompt, [[claude-md]], [[claude-skills]],
[[subagents]], [[model-context-protocol|MCP servers]] and [[claude-code-hooks|hooks]]. They
differ on two axes: **how reliably** the behaviour happens and **how much context** it costs
when idle. Pick the cheapest mechanism that is reliable enough. This comparison is assembled
from the Claude Code 101 notes, which teach each mechanism separately
([[claude-code-101-course-notes]]).

## Analysis

| Mechanism | Reliability | Idle context cost | Persists across sessions | Use when |
|---|---|---|---|---|
| **Prompt** | follows it this turn | none until typed | no | one-off guidance |
| **[[claude-md]]** | *usually* (advisory) | **always loaded** (whole file) | yes; committed or per-user | stack, commands, style, repeated corrections |
| **[[claude-skills]]** | when Claude judges it relevant | name + description only | yes | a reusable *process* needed sometimes |
| **[[subagents]]** | when called, explicitly or via its description | description only; work happens in a separate context | yes | you want the answer, not the noise (search, review) |
| **[[model-context-protocol]]** | when Claude chooses the tool | **all tool definitions, even unused** | yes; local / user / project scope | live access to an external system with no CLI |
| **[[claude-code-hooks]]** | **always**, deterministic | none (runs outside the model) | yes; `.claude/settings.json` | must happen *every time*, or must be blocked |

Sources for the cells: [[claude-code-101-course-notes]]; skills' progressive loading also from
[[claude-101-course-notes]].

**Rules of thumb drawn from the notes:**
- If it must happen every time, use a hook, not a prompt or CLAUDE.md.
- If you've corrected it twice, write it into CLAUDE.md. Start with no CLAUDE.md and let it
  grow from corrections (`/init`).
- If a CLI exists (gh, aws), use it instead of an MCP server; it is cheaper on context. A skill
  can wrap the CLI usage.
- If you only need the answer, use a subagent so the exploration stays out of the main context.
- Reviewers get read-only tools, so they flag problems and don't edit.

## Implications / so what

- The idle cost of CLAUDE.md and MCP is the hidden one. Both are paid on every turn, which is
  why the course stresses keeping CLAUDE.md lean and disabling unused servers
  ([[context-management]]).
- **For this KB** (assessment): the schema lives in `CLAUDE.md` (always loaded, advisory). The
  mechanical parts that must never be skipped (lint, secret scanning) are better as hooks; the
  repeatable operations (ingest, query, lint) are natural candidates for skills, which would
  take bulk out of CLAUDE.md ([[llm-wiki-pattern]]).
- This is the Claude Code counterpart of the claude.ai split "projects = knowledge, skills =
  process, connectors = access" ([[choosing-a-claude-surface]]). CLAUDE.md ≈ knowledge,
  skills/subagents ≈ process, MCP ≈ access, and hooks add a fourth category, **enforcement**,
  that claude.ai has no equivalent for.
- **On the API** the rungs reappear as request parameters: `system` ≈ CLAUDE.md, `container.skills`
  ≈ skills, `mcp_servers` + `mcp_toolset` ≈ MCP (with per-tool scoping to cut idle cost), and the
  memory tool ≈ cross-session memory. Enforcement is your own loop code, or a permissions policy
  in [[claude-managed-agents]] ([[claude-platform-101-course-notes]]). Assessment: the mapping is
  ours; the course doesn't draw it.

## Contradictions & open questions

- Slash commands and plugins aren't covered by the notes. Where do they fit on the ladder?
- Is a subagent with a preloaded skill (loaded in full) cheaper or dearer overall than the
  main session loading that skill on demand?

## Draws on

- [[claude-code-101-course-notes]], [[claude-101-course-notes]], [[claude-md]],
  [[claude-skills]], [[subagents]], [[model-context-protocol]], [[claude-code-hooks]],
  [[context-management]], [[claude-platform-101-course-notes]]
